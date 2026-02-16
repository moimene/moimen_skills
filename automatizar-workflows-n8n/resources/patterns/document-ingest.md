# Pipeline de Ingestión de Documentos

Sistema completo para ingestar documentos desde fuentes externas (Drive, S3) hasta almacenamiento vectorial.

## Arquitectura General

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PIPELINE DE INGESTIÓN                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  SOURCE          DOWNLOAD        EXTRACT         PROCESS           │
│    │                │               │               │               │
│    ▼                ▼               ▼               ▼               │
│ ┌──────┐       ┌─────────┐    ┌──────────┐    ┌──────────┐         │
│ │Drive │──────▶│Download │───▶│ Extract  │───▶│ Chunk +  │         │
│ │ /S3  │       │ + Hash  │    │  Text    │    │ Metadata │         │
│ └──────┘       └─────────┘    └──────────┘    └──────────┘         │
│                     │                               │               │
│                     ▼                               │               │
│              Supabase Storage                       │               │
│                     │                               ▼               │
│                     │         ┌─────────────────────┼───────────┐  │
│                     │         │                     │           │  │
│                     │         ▼                     ▼           │  │
│                     │    ┌─────────┐          ┌──────────┐      │  │
│                     │    │pgvector │          │ LightRAG │      │  │
│                     │    │/Pinecone│          │  (Graf)  │      │  │
│                     │    └─────────┘          └──────────┘      │  │
│                     │         │                     │           │  │
│                     │         └─────────────────────┘           │  │
│                     │                   │                       │  │
│                     │                   ▼                       │  │
│                     │         [Dual RAG Ready]                  │  │
│                     │                                           │  │
└─────────────────────┴───────────────────────────────────────────┴──┘
```

---

## Fase 1: Source & Trigger

### Opción A: Google Drive Trigger

```json
{
  "name": "Drive File Created",
  "type": "n8n-nodes-base.googleDriveTrigger",
  "parameters": {
    "event": "fileCreated",
    "folderId": "{{ $env.DRIVE_FOLDER_ID }}",
    "options": {
      "includeSharedWithMe": true
    }
  }
}
```

### Opción B: Webhook Manual

```json
{
  "name": "Ingest Webhook",
  "type": "n8n-nodes-base.webhook",
  "parameters": {
    "path": "ingest-document",
    "httpMethod": "POST"
  }
}
```

**Payload esperado**:
```json
{
  "file_id": "1abc123def456",  // ID de Drive o S3 key
  "source": "google_drive",    // google_drive | s3 | url
  "run_id": "uuid-v4",         // Para tracking
  "metadata": {
    "client_id": "...",
    "project_id": "..."
  }
}
```

---

## Fase 2: Download + Hash

### Nodo: Download File

```json
{
  "name": "Download from Drive",
  "type": "n8n-nodes-base.googleDrive",
  "parameters": {
    "operation": "download",
    "fileId": "={{ $json.file_id }}"
  }
}
```

### Nodo: Calculate Hash (Deduplicación)

```javascript
// Code Node: MD5 Hash
const crypto = require('crypto');
const binaryData = $input.first().binary.data;
const buffer = Buffer.from(binaryData.data, 'base64');
const hash = crypto.createHash('md5').update(buffer).digest('hex');

return [{
  json: {
    ...$input.first().json,
    file_hash: hash,
    file_size: buffer.length
  },
  binary: $input.first().binary
}];
```

### Nodo: Check Duplicate

```json
{
  "name": "Check Existing",
  "type": "n8n-nodes-base.supabase",
  "parameters": {
    "operation": "get",
    "tableId": "documents",
    "filters": {
      "file_hash": "={{ $json.file_hash }}"
    }
  }
}
```

**IF Node**: Si ya existe → Skip (return existing doc_id)

---

## Fase 3: Upload to Storage

### Nodo: Upload to Supabase Storage

```json
{
  "name": "Upload to Storage",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "={{ $env.SUPABASE_URL }}/storage/v1/object/documents/{{ $json.run_id }}/{{ $json.filename }}",
    "headers": {
      "Authorization": "Bearer {{ $env.SUPABASE_SERVICE_KEY }}",
      "Content-Type": "={{ $binary.data.mimeType }}"
    },
    "body": "={{ $binary.data }}"
  }
}
```

### Nodo: Insert Document Record

```json
{
  "name": "Insert Document",
  "type": "n8n-nodes-base.supabase",
  "parameters": {
    "operation": "insert",
    "tableId": "documents",
    "fields": {
      "id": "={{ $json.doc_id }}",
      "run_id": "={{ $json.run_id }}",
      "filename": "={{ $json.filename }}",
      "file_hash": "={{ $json.file_hash }}",
      "storage_path": "documents/{{ $json.run_id }}/{{ $json.filename }}",
      "status": "UPLOADED",
      "created_at": "={{ new Date().toISOString() }}"
    }
  }
}
```

---

## Fase 4: Extract Text

### Opción A: PDF con Servicio Externo

```json
{
  "name": "Extract PDF Text",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://api.ocr.space/parse/image",
    "headers": {
      "apikey": "={{ $env.OCR_API_KEY }}"
    },
    "body": {
      "base64Image": "data:application/pdf;base64,{{ $binary.data.data }}",
      "language": "spa",
      "isOverlayRequired": false
    }
  }
}
```

### Opción B: DOCX con n8n Nativo

```json
{
  "name": "Extract DOCX",
  "type": "n8n-nodes-base.extractFromFile",
  "parameters": {
    "operation": "text",
    "binaryPropertyName": "data"
  }
}
```

### Opción C: Unstructured.io (Recomendado)

```json
{
  "name": "Unstructured Extract",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://api.unstructured.io/general/v0/general",
    "headers": {
      "unstructured-api-key": "={{ $env.UNSTRUCTURED_API_KEY }}"
    },
    "body": {
      "files": "={{ $binary.data }}"
    }
  }
}
```

---

## Fase 5: Chunking

### Estrategia de Chunking

| Parámetro | Valor Recomendado | Razón |
|-----------|------------------|-------|
| Chunk Size | 1000-1500 tokens | Balance entre contexto y precisión |
| Overlap | 100-200 tokens | Mantener continuidad semántica |
| Separator | Párrafos/Secciones | Chunks coherentes |

### Código: Chunk por Tokens (Aproximado)

```javascript
// Code Node: Smart Chunking
const text = $input.first().json.extracted_text;
const metadata = $input.first().json.metadata;

// Aproximación: 1 token ≈ 4 caracteres
const CHUNK_SIZE_CHARS = 4000;  // ~1000 tokens
const OVERLAP_CHARS = 400;      // ~100 tokens

// Intentar cortar en párrafos
const paragraphs = text.split(/\n\n+/);
const chunks = [];
let currentChunk = '';
let chunkStart = 0;

for (const para of paragraphs) {
  if ((currentChunk + para).length > CHUNK_SIZE_CHARS && currentChunk) {
    chunks.push({
      content: currentChunk.trim(),
      chunk_index: chunks.length,
      start_char: chunkStart,
      end_char: chunkStart + currentChunk.length,
      metadata: {
        ...metadata,
        total_chunks: null  // Se actualiza después
      }
    });
    
    // Overlap: mantener último párrafo
    const overlapText = currentChunk.slice(-OVERLAP_CHARS);
    chunkStart = chunkStart + currentChunk.length - OVERLAP_CHARS;
    currentChunk = overlapText;
  }
  currentChunk += para + '\n\n';
}

// Último chunk
if (currentChunk.trim()) {
  chunks.push({
    content: currentChunk.trim(),
    chunk_index: chunks.length,
    start_char: chunkStart,
    end_char: chunkStart + currentChunk.length,
    metadata: {
      ...metadata,
      total_chunks: null
    }
  });
}

// Actualizar total_chunks
chunks.forEach(c => c.metadata.total_chunks = chunks.length);

return chunks.map(c => ({ json: c }));
```

---

## Fase 6: Vectorización

### Nodo: Generate Embeddings

```json
{
  "name": "OpenAI Embeddings",
  "type": "n8n-nodes-base.openAi",
  "parameters": {
    "operation": "embedding",
    "model": "text-embedding-3-small",
    "input": "={{ $json.content }}"
  }
}
```

### Nodo: Store in pgvector

```json
{
  "name": "Insert Vector",
  "type": "n8n-nodes-base.supabase",
  "parameters": {
    "operation": "insert",
    "tableId": "document_chunks",
    "fields": {
      "document_id": "={{ $json.metadata.doc_id }}",
      "chunk_index": "={{ $json.chunk_index }}",
      "content": "={{ $json.content }}",
      "embedding": "={{ $json.embedding }}",
      "metadata": "={{ JSON.stringify($json.metadata) }}"
    }
  }
}
```

### Alternativa: Pinecone

```json
{
  "name": "Upsert Pinecone",
  "type": "n8n-nodes-base.pinecone",
  "parameters": {
    "operation": "upsert",
    "vectors": [
      {
        "id": "={{ $json.metadata.doc_id }}-{{ $json.chunk_index }}",
        "values": "={{ $json.embedding }}",
        "metadata": "={{ $json.metadata }}"
      }
    ]
  }
}
```

---

## Fase 7: LightRAG Ingest (Opcional)

Para habilitar búsqueda conceptual además de semántica.

> ⚠️ **Crítico**: Batch Size = 1 para evitar corrupción del grafo

```json
{
  "name": "Split Batches",
  "type": "n8n-nodes-base.splitInBatches",
  "parameters": {
    "batchSize": 1
  }
}
```

```json
{
  "name": "LightRAG Ingest",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "={{ $env.LIGHTRAG_URL }}/ingest",
    "headers": {
      "x-api-key": "={{ $env.LIGHTRAG_API_KEY }}"
    },
    "body": {
      "text": "={{ $json.content }}",
      "metadata": {
        "doc_id": "={{ $json.metadata.doc_id }}",
        "chunk_index": "={{ $json.chunk_index }}",
        "source": "={{ $json.metadata.filename }}"
      }
    },
    "options": {
      "timeout": 120000
    }
  }
}
```

---

## Fase 8: Finalización

### Nodo: Update Document Status

```json
{
  "name": "Mark Complete",
  "type": "n8n-nodes-base.supabase",
  "parameters": {
    "operation": "update",
    "tableId": "documents",
    "filters": {
      "id": "={{ $json.doc_id }}"
    },
    "fields": {
      "status": "INDEXED",
      "chunk_count": "={{ $json.total_chunks }}",
      "indexed_at": "={{ new Date().toISOString() }}"
    }
  }
}
```

### Nodo: Callback Webhook

```json
{
  "name": "Notify Complete",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "={{ $env.CALLBACK_URL }}",
    "body": {
      "run_id": "={{ $json.run_id }}",
      "status": "COMPLETED",
      "doc_id": "={{ $json.doc_id }}",
      "chunks": "={{ $json.total_chunks }}"
    }
  }
}
```

---

## Error Handling

### Error Trigger Global

```json
{
  "name": "Error Handler",
  "type": "n8n-nodes-base.errorTrigger"
}
```

Conectar a:

```json
{
  "name": "Notify Failure",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "={{ $env.CALLBACK_URL }}",
    "body": {
      "run_id": "={{ $json.run_id }}",
      "status": "FAILED",
      "error": "={{ $json.error.message }}",
      "node": "={{ $json.error.node }}"
    }
  }
}
```

---

## Checklist de Implementación

### Variables de Entorno Requeridas

- [ ] `SUPABASE_URL`
- [ ] `SUPABASE_SERVICE_KEY`
- [ ] `OPENAI_API_KEY`
- [ ] `LIGHTRAG_URL` (si usa LightRAG)
- [ ] `LIGHTRAG_API_KEY` (si usa LightRAG)
- [ ] `CALLBACK_URL`
- [ ] `DRIVE_FOLDER_ID` (si usa Drive trigger)

### Tablas de Base de Datos

```sql
-- documents
CREATE TABLE documents (
  id UUID PRIMARY KEY,
  run_id UUID,
  filename TEXT,
  file_hash TEXT UNIQUE,
  storage_path TEXT,
  status TEXT,  -- UPLOADED | PROCESSING | INDEXED | FAILED
  chunk_count INTEGER,
  created_at TIMESTAMPTZ,
  indexed_at TIMESTAMPTZ
);

-- document_chunks
CREATE TABLE document_chunks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  document_id UUID REFERENCES documents(id),
  chunk_index INTEGER,
  content TEXT,
  embedding vector(1536),
  metadata JSONB,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Índice para búsqueda vectorial
CREATE INDEX ON document_chunks 
  USING ivfflat (embedding vector_cosine_ops)
  WITH (lists = 100);
```
