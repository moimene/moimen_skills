---
name: automatizar-workflows-n8n
description: Orquesta automatizaciones con n8n usando patrones de agentes adversariales, pipelines de ingestión de documentos y RAG híbrido. Úsese cuando el usuario quiera crear workflows de procesamiento de documentos, implementar flujos paranoico-validador-sanitizer, integrar LightRAG con n8n, o controlar workflows via MCP.
---

# Automatizar Workflows con n8n

Blueprint para crear y orquestar automatizaciones complejas en n8n, con foco en procesamiento de documentos, agentes adversariales, y RAG híbrido.

## Rol del Modelo

Actúas como **arquitecto de automatizaciones** especializado en n8n y pipelines de procesamiento de documentos. Tu objetivo es diseñar workflows robustos que implementen patrones de agentes adversariales, ingestión de documentos, y búsqueda híbrida (vectorial + grafo).

---

## Cuándo Usar Esta Skill

- Diseñar pipelines de ingestión de documentos (Drive/S3 → Storage → Vectores)
- Implementar flujos de agentes adversariales (Paranoico → Validador → Sanitizer)
- Integrar LightRAG para búsqueda conceptual en workflows n8n
- Controlar y ejecutar workflows desde Antigravity via MCP
- Crear feedback loops con Supabase Realtime

---

## Arquitectura Multi-Agente Adversarial

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PIPELINE ADVERSARIAL                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  INPUT           PARANOICO         VALIDADOR        SANITIZER       │
│    │                │                  │                │           │
│    ▼                ▼                  ▼                ▼           │
│ ┌──────┐       ┌─────────┐       ┌──────────┐      ┌──────────┐    │
│ │ DOC  │──────▶│ EXTRAE  │──────▶│ VERIFICA │─────▶│ LIMPIA   │    │
│ │ RAW  │       │ + ALERTA│       │ + CRUZA  │      │ + FORMATA│    │
│ └──────┘       └─────────┘       └──────────┘      └──────────┘    │
│                     │                  │                │           │
│                     ▼                  ▼                ▼           │
│               Findings Raw       Validated Set     Clean Output     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Los Tres Agentes

| Agente | Personalidad | System Prompt Core | Output |
|--------|--------------|-------------------|--------|
| **Paranoico** | Desconfiado, obsesivo | "Asume que TODO puede contener errores o riesgos ocultos. Extrae absolutamente todo." | Findings brutos + alertas |
| **Validador** | Escéptico, metódico | "Verifica cada claim contra las fuentes. Marca contradicciones. No confíes en el agente anterior." | Set validado + discrepancias |
| **Sanitizer** | Pragmático, ordenado | "Normaliza formatos, elimina duplicados, estructura output final. Prioriza claridad." | Output limpio estructurado |

### Implementación en n8n

```
[Webhook Trigger]
       │
       ▼
[AI Agent: Paranoico]  ◄── System prompt paranoico
       │                    Model: gpt-4o / claude-3-opus
       │
       ▼
[AI Agent: Validador]  ◄── System prompt validador
       │                    Recibe: output paranoico + documento original
       │
       ▼
[AI Agent: Sanitizer]  ◄── System prompt sanitizer
       │                    Recibe: output validador
       │
       ▼
[HTTP Request: Webhook Callback]  ◄── Notifica resultado final
```

> ⚠️ **Crítico**: Cada agente debe recibir el **documento original** además del output del agente anterior, para poder verificar independientemente.

---

## Pipeline de Ingestión de Documentos

```
┌─────┐   ┌──────────┐   ┌───────────┐   ┌─────────┐   ┌──────────┐
│Drive│──▶│ Download │──▶│ Extract   │──▶│ Chunk   │──▶│ Vectorize│
│/S3  │   │ + Hash   │   │ Text/PDF  │   │ + Meta  │   │ + Store  │
└─────┘   └──────────┘   └───────────┘   └─────────┘   └──────────┘
     │          │                                              │
     │          ▼                                              ▼
     │    Supabase Storage                              pgvector/Pinecone
     │          │
     │          └──▶ [Opcional] LightRAG Ingest (Batch=1)
     │
     └──▶ Webhook: run_id para tracking
```

### Nodos Típicos

| Paso | Nodo n8n | Notas |
|------|----------|-------|
| Trigger | `Webhook` o `Google Drive Trigger` | Recibe file_id + run_id |
| Download | `Google Drive: Download` | Binary data |
| Hash | `Code Node` | MD5 para deduplicación |
| Extract | `Extract from File` o `HTTP Request` a servicio OCR | Soporta PDF, DOCX |
| Chunk | `Code Node` | Split por tokens (1000-2000) con overlap |
| Vectorize | `OpenAI: Embeddings` | text-embedding-3-small |
| Store | `Supabase: Insert` o `Pinecone: Upsert` | Con metadatos |

### Ejemplo: Nodo de Chunking

```javascript
// Code Node: Chunk Document
const text = $input.first().json.content;
const CHUNK_SIZE = 1500;
const OVERLAP = 200;

const chunks = [];
for (let i = 0; i < text.length; i += CHUNK_SIZE - OVERLAP) {
  chunks.push({
    content: text.slice(i, i + CHUNK_SIZE),
    chunk_index: chunks.length,
    start_char: i,
    metadata: {
      source: $input.first().json.filename,
      run_id: $input.first().json.run_id
    }
  });
}

return chunks.map(c => ({ json: c }));
```

---

## Integración con LightRAG (Nodo RAG Graph)

Para búsqueda conceptual basada en grafos de conocimiento, integrar con el microservicio LightRAG.

> 📚 **Referencia completa**: Ver skill `integrar-lightrag-grafo-conocimiento`

### Query Híbrido en n8n

```
[Query Input]
      │
      ├──────────────────┬────────────────────┐
      │                  │                    │
      ▼                  ▼                    │
[Pinecone Query]   [LightRAG Query]          │
      │                  │                    │
      └────────┬─────────┘                    │
               │                              │
               ▼                              │
        [Merge Results]                       │
               │                              │
               ▼                              │
        [LLM Fusion] ◄────────────────────────┘
               │
               ▼
        [Response Final]
```

### Configuración LightRAG en n8n

| Parámetro | Valor | Razón |
|-----------|-------|-------|
| Timeout | **300000ms** (5 min) | LightRAG queries pueden tardar 20-60s |
| Batch Size (ingesta) | **1** | Evitar corrupción del grafo |
| Retry on Failure | **3 intentos** | Red inestable |

---

## Patrones Esenciales de n8n

### 1. Split In Batches (size=1)

**Cuándo**: Operaciones que mutan estado compartido.

```json
{
  "parameters": {
    "batchSize": 1,
    "options": {}
  }
}
```

**Usar para**: LightRAG ingest, DB writes secuenciales, APIs con rate limit.

### 2. Error Trigger + Webhook Callback

**Cuándo**: Feedback loop a UI frontend.

```json
{
  "nodes": [
    {
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger"
    },
    {
      "name": "Notify Failure",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://project.supabase.co/functions/v1/update_run_status",
        "method": "POST",
        "body": {
          "run_id": "={{ $json.run_id }}",
          "status": "FAILED",
          "error_message": "={{ $json.error.message }}"
        }
      }
    }
  ]
}
```

### 3. IF Router por Score

**Cuándo**: Lógica condicional basada en confianza.

```javascript
// Condition: High Confidence
{{ $json.confidence_score > 0.8 }}
```

### 4. Parallel Execution con Merge

**Cuándo**: Queries a múltiples fuentes (RAG clásico + Graph).

- Usar nodo `Execute Workflow` con `Wait for Sub-Workflows`
- O bifurcación simple con `Merge` al final

---

## Control via MCP (Model Context Protocol)

n8n expone un servidor MCP que permite a Antigravity ejecutar workflows directamente.

### Configuración

1. En n8n Cloud: Habilitar "MCP Server" en Settings
2. Marcar workflows como "Available in MCP"
3. Configurar en Antigravity:

```json
// .gemini/settings.json
{
  "mcpServers": {
    "n8n": {
      "url": "https://your-instance.app.n8n.cloud/mcp",
      "transportType": "sse",
      "headers": {
        "Authorization": "Bearer YOUR_N8N_API_KEY"
      }
    }
  }
}
```

### Uso desde Antigravity

```
Usuario: Ejecuta el workflow W1_DriveIngest con file_id=abc123
Antigravity: [Usa herramienta MCP n8n para ejecutar workflow]
```

---

## Ejemplo Real: Contract Guardian Pipeline

Pipeline de 3 workflows para revisión de contratos:

### W1: DriveIngest

```
Trigger: Webhook (file_id, run_id)
    │
    ▼
Download from Drive
    │
    ▼
Upload to Supabase Storage
    │
    ▼
Insert record in 'documents' table
    │
    ▼
Trigger W3_ContractReview
```

### W2: ClauseReview (Sub-workflow)

```
Input: clause_text, clause_type, run_id
    │
    ▼
[Paranoico] Extract risks + obligations
    │
    ▼
[Validador] Cross-check vs policy_examples
    │
    ▼
[Sanitizer] Format decision + rationale
    │
    ▼
Return: { decision, confidence, findings }
```

### W3: ContractReview (Orchestrator)

```
Trigger: Webhook (document_id, run_id)
    │
    ▼
Fetch document from Storage
    │
    ▼
Split into clauses
    │
    ▼
Loop: Call W2_ClauseReview for each
    │
    ▼
Aggregate decisions
    │
    ▼
POST to update_run_status (COMPLETED)
```

---

## Checklist de Implementación

### Pre-despliegue

- [ ] Workflows probados en modo test
- [ ] Variables de entorno configuradas (API keys, URLs)
- [ ] Error Triggers conectados a webhook de fallback
- [ ] Timeouts configurados (LightRAG: 300s)

### Producción

- [ ] Workflows activados
- [ ] Logs habilitados para debugging
- [ ] Monitoring de executions en n8n
- [ ] Webhook de status conectado a frontend (Realtime)

### Agentes Adversariales

- [ ] System prompts definidos para cada agente
- [ ] Documento original pasado a cada agente (no solo output anterior)
- [ ] Output estructurado (JSON) para parsing automático

---

## Anti-patrones a Evitar

| ❌ Evitar | ✓ Usar |
|-----------|--------|
| Batch size > 1 para LightRAG | Batch size = 1 siempre |
| Timeout default (30s) para queries RAG | Timeout 300s |
| Solo pasar output entre agentes | Pasar output + documento original |
| Ignorar Error Trigger | Siempre configurar fallback webhook |
| Hardcodear run_id | Pasar run_id desde trigger inicial |

---

## Recursos

- [Patrones Adversariales](resources/patterns/adversarial-agents.md)
- [Pipeline de Ingestión](resources/patterns/document-ingest.md)
- [Template: W0_DriveIngest](resources/templates/W0_DriveIngest.json)
- [Template: W1_AdversarialReview](resources/templates/W1_AdversarialReview.json)
- [Skill LightRAG](../integrar-lightrag-grafo-conocimiento/SKILL.md)

---

## Regla Final

> **Agentes adversariales + feedback loops + LightRAG = pipelines de documentos robustos y verificables.**
