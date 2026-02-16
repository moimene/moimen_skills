"""
LightRAG Knowledge Graph Service - Referencia de Implementación

FastAPI server for ingesting documents into a LightRAG Knowledge Graph.
Uses background tasks to avoid timeout issues with n8n webhook calls.
"""

import os
import asyncio
from datetime import datetime
from typing import Optional, Dict, Any

from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# =============================================================================
# Configuration
# =============================================================================

WORKDIR = os.getenv("LIGHTRAG_WORKDIR", "/app/data")
os.makedirs(WORKDIR, exist_ok=True)

SERVICE_API_KEY = os.getenv("SERVICE_API_KEY", "")

# =============================================================================
# Security
# =============================================================================

async def verify_api_key(x_api_key: str = Header(None)):
    if not SERVICE_API_KEY:
        return True  # Dev mode
    if x_api_key != SERVICE_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return True

# =============================================================================
# LightRAG Setup
# =============================================================================

from lightrag import LightRAG
from lightrag.utils import EmbeddingFunc
from lightrag.base import QueryParam
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status
import numpy as np

async def llm_func(prompt, system_prompt=None, history_messages=[], **kwargs) -> str:
    return await openai_complete_if_cache(
        "gpt-4o-mini",
        prompt,
        system_prompt=system_prompt,
        history_messages=history_messages,
        api_key=os.getenv("OPENAI_API_KEY"),
        **kwargs
    )

async def embed_texts(texts: list) -> np.ndarray:
    return await openai_embed(
        texts,
        model="text-embedding-3-small",
        api_key=os.getenv("OPENAI_API_KEY")
    )

embedding_func = EmbeddingFunc(
    embedding_dim=1536,
    max_token_size=8192,
    func=embed_texts
)

# =============================================================================
# FastAPI App
# =============================================================================

app = FastAPI(title="LightRAG Knowledge Graph")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================================================================
# RAG Singleton
# =============================================================================

_rag_instance: Optional[Any] = None
_rag_initialized = False
_rag_init_lock = None
_ingest_lock = None

async def ensure_rag_initialized():
    global _rag_instance, _rag_initialized, _rag_init_lock
    
    if _rag_init_lock is None:
        _rag_init_lock = asyncio.Lock()
    
    if _rag_initialized:
        return _rag_instance
    
    async with _rag_init_lock:
        if _rag_initialized:
            return _rag_instance
        
        _rag_instance = LightRAG(
            working_dir=WORKDIR,
            llm_model_func=llm_func,
            embedding_func=embedding_func,
        )
        
        await _rag_instance.initialize_storages()
        await initialize_pipeline_status()
        
        _rag_initialized = True
        print("[INFO] LightRAG initialized")
    
    return _rag_instance

# =============================================================================
# Models
# =============================================================================

class IngestRequest(BaseModel):
    text: str = Field(..., min_length=10)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class IngestResponse(BaseModel):
    status: str
    message: str
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

class QueryRequest(BaseModel):
    query: str
    mode: str = Field(default="hybrid")  # local | global | hybrid

class QueryResponse(BaseModel):
    answer: str
    mode: str
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

class HealthResponse(BaseModel):
    status: str
    workdir_exists: bool
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

# =============================================================================
# Background Ingestion
# =============================================================================

async def process_ingest(text: str, metadata: Dict[str, Any]):
    global _ingest_lock
    
    rag = await ensure_rag_initialized()
    
    if _ingest_lock is None:
        _ingest_lock = asyncio.Lock()
    
    async with _ingest_lock:  # Serialize to prevent file corruption
        try:
            # Enrich with metadata
            enriched = ""
            if metadata.get("summary"):
                enriched += f"Summary: {metadata['summary']}\n\n"
            if metadata.get("keywords"):
                keywords = metadata["keywords"]
                if isinstance(keywords, list):
                    keywords = ", ".join(keywords)
                enriched += f"Keywords: {keywords}\n\n"
            enriched += text
            
            await rag.ainsert(enriched)
            print(f"[INGEST] Completed: {metadata.get('filename', 'unnamed')}")
            
        except Exception as e:
            print(f"[ERROR] Ingestion failed: {e}")

# =============================================================================
# Endpoints
# =============================================================================

@app.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(
        status="ok",
        workdir_exists=os.path.exists(WORKDIR)
    )

@app.post("/ingest", response_model=IngestResponse, dependencies=[Depends(verify_api_key)])
async def ingest(req: IngestRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_ingest, req.text, req.metadata)
    return IngestResponse(status="accepted", message="Processing started")

@app.post("/query", response_model=QueryResponse, dependencies=[Depends(verify_api_key)])
async def query(req: QueryRequest):
    rag = await ensure_rag_initialized()
    
    if req.mode not in ["local", "global", "hybrid"]:
        raise HTTPException(status_code=400, detail="Invalid mode")
    
    param = QueryParam(mode=req.mode)
    answer = await rag.aquery(req.query, param=param)
    
    if not isinstance(answer, str):
        answer = "".join(list(answer))
    
    return QueryResponse(answer=answer, mode=req.mode)

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
