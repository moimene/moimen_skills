---
name: integrar-lightrag-grafo-conocimiento
description: Integra LightRAG como complemento del RAG clásico en flujos de trabajo. Úsese cuando el usuario quiera añadir búsqueda conceptual (entidades/relaciones) a un pipeline RAG existente, implementar Hybrid RAG (vectores + grafo), o crear un Knowledge Graph con extracción automática de entidades.
---

# Integrar LightRAG - Grafo de Conocimiento

Blueprint para añadir LightRAG como complemento de búsqueda conceptual en pipelines RAG existentes.

## Rol del Modelo

Actúas como **arquitecto de sistemas RAG** especializado en pipelines de recuperación híbridos (vectorial + grafo). Tu objetivo es integrar LightRAG para complementar la búsqueda semántica tradicional con búsqueda conceptual basada en grafos de conocimiento.

---

## Arquitectura Hybrid RAG

```
           ┌─────────────────────────────────────────────────┐
           │               QUERY DE USUARIO                  │
           └─────────────────────┬───────────────────────────┘
                                 │
           ┌─────────────────────┴───────────────────────────┐
           │              ORQUESTADOR (n8n)                  │
           └─────────────────────┬───────────────────────────┘
                                 │
         ┌───────────────────────┼───────────────────────────┐
         │                       │                           │
    ┌────┴────┐            ┌─────┴─────┐              ┌──────┴──────┐
    │  VÍA A  │            │   VÍA B   │              │   FUSIÓN    │
    │ Clásica │            │ LightRAG  │              │  Respuesta  │
    └────┬────┘            └─────┬─────┘              └──────┬──────┘
         │                       │                           │
    ┌────┴────┐            ┌─────┴─────┐                     │
    │Pinecone │            │   Grafo   │                     │
    │ Vectors │            │Conocimiento│                    │
    └─────────┘            └───────────┘                     │
         │                       │                           │
         └───────────────────────┴───────────────────────────┘
```

### Vía A: RAG Clásico (Semántica)

- Búsqueda vectorial tradicional
- Pinecone / Supabase pgvector / etc.
- **Ideal para:** hechos específicos, fragmentos exactos

### Vía B: LightRAG (Conceptual)

- Extracción de entidades (LLM)
- Extracción de relaciones (LLM)
- Grafo (NetworkX + nano-vectordb)
- **Ideal para:** conceptos abstractos, relaciones entre temas

---

## Componentes del Sistema

### 1. Microservicio LightRAG (FastAPI)

**Tecnologías:**
- Python 3.11+
- FastAPI + Uvicorn
- LightRAG 1.4.9+
- OpenAI API (gpt-4o-mini + text-embedding-3-small)

**Endpoints:**

| Endpoint | Método | Auth | Descripción |
|----------|--------|------|-------------|
| `/health` | GET | ❌ | Health check |
| `/ingest` | POST | ✅ | Ingestar documento en grafo |
| `/query` | POST | ✅ | Consultar grafo de conocimiento |

### 2. Orquestador (n8n)

- Webhook de entrada
- Bifurcación a Vía A + Vía B
- Fusión de respuestas
- Envío de respuesta final

### 3. Almacenamiento

- **Grafo:** Railway Volume `/app/data`
- **Vectores:** nano-vectordb (integrado) o Pinecone

---

## Implementación Paso a Paso

### Paso 1: Crear Servicio FastAPI

```python
# main.py - Estructura base

from fastapi import FastAPI, BackgroundTasks, Depends, Header, HTTPException
from pydantic import BaseModel, Field
from lightrag import LightRAG
from lightrag.utils import EmbeddingFunc
from lightrag.base import QueryParam
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
import asyncio
import os

# Configuración
WORKDIR = os.getenv("LIGHTRAG_WORKDIR", "/app/data")
SERVICE_API_KEY = os.getenv("SERVICE_API_KEY", "")

app = FastAPI(title="LightRAG Knowledge Graph")

# Singleton RAG
_rag_instance = None
_ingest_lock = None

async def get_rag():
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = LightRAG(
            working_dir=WORKDIR,
            llm_model_func=llm_func,
            embedding_func=embedding_func,
        )
        await _rag_instance.initialize_storages()
    return _rag_instance
```

### Paso 2: Endpoint de Ingesta

```python
class IngestRequest(BaseModel):
    text: str = Field(..., min_length=10)
    metadata: dict = Field(default_factory=dict)

@app.post("/ingest")
async def ingest(req: IngestRequest, background_tasks: BackgroundTasks):
    """Acepta documento y procesa en background."""
    background_tasks.add_task(process_ingest, req.text, req.metadata)
    return {"status": "accepted", "message": "Procesamiento iniciado"}

async def process_ingest(text: str, metadata: dict):
    global _ingest_lock
    if _ingest_lock is None:
        _ingest_lock = asyncio.Lock()
    
    async with _ingest_lock:  # Serializar para evitar corrupción
        rag = await get_rag()
        
        # Enriquecer con metadatos
        enriched = ""
        if metadata.get("summary"):
            enriched += f"Summary: {metadata['summary']}\n\n"
        if metadata.get("keywords"):
            enriched += f"Keywords: {', '.join(metadata['keywords'])}\n\n"
        enriched += text
        
        await rag.ainsert(enriched)
```

### Paso 3: Endpoint de Query

```python
class QueryRequest(BaseModel):
    query: str
    mode: str = "hybrid"  # local | global | hybrid

@app.post("/query")
async def query(req: QueryRequest):
    rag = await get_rag()
    
    param = QueryParam(mode=req.mode)
    answer = await rag.aquery(req.query, param=param)
    
    return {"answer": answer, "mode": req.mode}
```

### Paso 4: Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App
COPY main.py .

# Persistencia del grafo
VOLUME /app/data

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Paso 5: requirements.txt

```
fastapi>=0.104.0
uvicorn>=0.24.0
pydantic>=2.0.0
lightrag-hku>=1.4.9
openai>=1.0.0
numpy
```

---

## Integración con n8n

### Workflow de Ingesta

```json
{
  "nodes": [
    {
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook"
    },
    {
      "name": "Split In Batches",
      "parameters": { "batchSize": 1 }
    },
    {
      "name": "LightRAG Ingest",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://your-service.railway.app/ingest",
        "method": "POST",
        "headers": {
          "x-api-key": "={{$env.LIGHTRAG_API_KEY}}"
        },
        "body": {
          "text": "={{$json.content}}",
          "metadata": {
            "source": "={{$json.source}}",
            "filename": "={{$json.filename}}"
          }
        }
      }
    }
  ]
}
```

> ⚠️ **Crítico:** Batch Size = 1 para evitar corrupción del grafo

### Workflow de Query Híbrido

```json
{
  "nodes": [
    {
      "name": "Query Input"
    },
    {
      "name": "Parallel Queries",
      "type": "n8n-nodes-base.splitInBatches"
    },
    {
      "name": "Pinecone Query",
      "type": "n8n-nodes-base.httpRequest"
    },
    {
      "name": "LightRAG Query",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://your-service.railway.app/query",
        "timeout": 300000
      }
    },
    {
      "name": "Merge Results",
      "type": "n8n-nodes-base.merge"
    },
    {
      "name": "LLM Fusion",
      "type": "n8n-nodes-base.openAi"
    }
  ]
}
```

---

## Modos de Query LightRAG

| Modo | Descripción | Uso |
|------|-------------|-----|
| `local` | Solo entidades | Hechos precisos, definiciones |
| `global` | Solo relaciones | Temas abstractos, overview |
| `hybrid` | Ambos | **Recomendado** por defecto |

---

## Despliegue en Railway

### Variables de Entorno

| Variable | Descripción | Requerida |
|----------|-------------|-----------|
| `OPENAI_API_KEY` | API key OpenAI | ✅ |
| `SERVICE_API_KEY` | Auth para endpoints | ✅ |
| `LIGHTRAG_WORKDIR` | Path del grafo | `/app/data` |

### Volumen (CRÍTICO)

```
Mount path: /app/data
Tamaño mínimo: 1GB
```

> ⚠️ **Sin volumen, el grafo se pierde en cada deploy**

---

## Timeouts Recomendados

| Endpoint | Timeout | Motivo |
|----------|---------|--------|
| `/ingest` | 60s | Retorna rápido (background) |
| `/query` | **300s** | LightRAG puede tardar 20-60s |

---

## Checklist de Integración

### Pre-despliegue

- [ ] OpenAI API key configurada
- [ ] SERVICE_API_KEY generada
- [ ] Volumen Railway montado en `/app/data`
- [ ] Dockerfile probado localmente

### Post-despliegue

- [ ] `/health` responde OK
- [ ] Smoke test de ingesta exitoso
- [ ] Smoke test de query exitoso
- [ ] Workflow n8n importado
- [ ] Variable `LIGHTRAG_API_KEY` en n8n

### Producción

- [ ] Timeout de query = 300s en n8n
- [ ] Batch size = 1 para ingesta
- [ ] Logs de Railway monitoreados

---

## Anti-patrones a Evitar

| ❌ Evitar | ✓ Usar |
|-----------|--------|
| Ingesta paralela | Ingesta secuencial (lock) |
| Procesar en request | Background tasks |
| Sin timeout largo | Timeout 300s en queries |
| Sin volumen persistente | Railway Volume |

---

## Recursos

- [Código de Referencia](resources/main.py)
- [Dockerfile](resources/Dockerfile)
- [Workflow n8n](resources/n8n-workflow.json)
- [LightRAG Docs](https://github.com/HKUDS/LightRAG)

---

## Regla Final

> **LightRAG complementa, no reemplaza. Úsalo para búsqueda conceptual mientras el RAG clásico maneja hechos específicos.**
