"""
Ejemplo: Sistema de Análisis de Sentimiento Multi-Agente

Este ejemplo demuestra cómo usar el framework de orquestación
para construir un sistema de análisis de sentimiento con múltiples
agentes especializados que colaboran y se auto-mejoran.
"""

import asyncio
from typing import Dict, Any
import sys
sys.path.append('../resources')

from orchestrator import (
    MultiAgentOrchestrator,
    BaseAgent,
    AgentTask,
    AgentResult
)
from context_manager import ContextManager
from self_improvement import SelfImprovingAgent


class DataCollectorAgent(BaseAgent):
    """Agente que recolecta datos de múltiples fuentes."""
    
    def __init__(self):
        super().__init__("DataCollector", "data_collection")
    
    async def _execute_impl(self, task: AgentTask, context: Dict[str, Any]) -> Any:
        # Simular recolección de datos
        await asyncio.sleep(0.1)
        
        return {
            "sources": ["Twitter", "Reddit", "News"],
            "data_points": 1500,
            "raw_texts": [
                "Great product, highly recommend!",
                "Terrible experience, waste of money.",
                "Average quality, nothing special."
            ]
        }


class SentimentAnalyzerAgent(BaseAgent):
    """Agente que analiza sentimiento de textos."""
    
    def __init__(self):
        super().__init__("SentimentAnalyzer", "sentiment_analysis")
    
    async def _execute_impl(self, task: AgentTask, context: Dict[str, Any]) -> Any:
        # Obtener datos del contexto
        collection_data = context.get("data_collection", {})
        raw_texts = collection_data.get("raw_texts", [])
        
        # Simular análisis de sentimiento
        await asyncio.sleep(0.15)
        
        sentiments = []
        for text in raw_texts:
            if any(word in text.lower() for word in ["great", "recommend", "excellent"]):
                sentiment = "positive"
                score = 0.85
            elif any(word in text.lower() for word in ["terrible", "waste", "bad"]):
                sentiment = "negative"
                score = 0.15
            else:
                sentiment = "neutral"
                score = 0.50
            
            sentiments.append({
                "text": text,
                "sentiment": sentiment,
                "score": score
            })
        
        return {
            "sentiments": sentiments,
            "summary": {
                "positive": sum(1 for s in sentiments if s["sentiment"] == "positive"),
                "negative": sum(1 for s in sentiments if s["sentiment"] == "negative"),
                "neutral": sum(1 for s in sentiments if s["sentiment"] == "neutral")
            }
        }


class TrendDetectorAgent(BaseAgent):
    """Agente que detecta tendencias en el sentimiento."""
    
    def __init__(self):
        super().__init__("TrendDetector", "trend_detection")
    
    async def _execute_impl(self, task: AgentTask, context: Dict[str, Any]) -> Any:
        # Obtener análisis de sentimiento del contexto
        sentiment_data = context.get("sentiment_analysis", {})
        summary = sentiment_data.get("summary", {})
        
        # Simular detección de tendencias
        await asyncio.sleep(0.12)
        
        total = sum(summary.values())
        positive_ratio = summary.get("positive", 0) / max(total, 1)
        
        if positive_ratio > 0.6:
            trend = "improving"
            recommendation = "Product reception is positive, maintain current strategy"
        elif positive_ratio < 0.3:
            trend = "declining"
            recommendation = "Negative sentiment detected, investigate issues urgently"
        else:
            trend = "stable"
            recommendation = "Mixed sentiment, consider targeted improvements"
        
        return {
            "trend": trend,
            "positive_ratio": positive_ratio,
            "recommendation": recommendation,
            "confidence": 0.78
        }


class ReportGeneratorAgent(BaseAgent):
    """Agente que genera reportes finales."""
    
    def __init__(self):
        super().__init__("ReportGenerator", "report_generation")
    
    async def _execute_impl(self, task: AgentTask, context: Dict[str, Any]) -> Any:
        # Recolectar toda la información del contexto
        collection = context.get("data_collection", {})
        sentiment = context.get("sentiment_analysis", {})
        trends = context.get("trend_detection", {})
        
        # Simular generación de reporte
        await asyncio.sleep(0.08)
        
        report = {
            "title": "Sentiment Analysis Report",
            "data_summary": {
                "sources": collection.get("sources", []),
                "total_data_points": collection.get("data_points", 0)
            },
            "sentiment_summary": sentiment.get("summary", {}),
            "trends": {
                "current_trend": trends.get("trend", "unknown"),
                "positive_ratio": trends.get("positive_ratio", 0),
                "confidence": trends.get("confidence", 0)
            },
            "recommendation": trends.get("recommendation", ""),
            "timestamp": "2026-01-28T16:00:00Z"
        }
        
        return report


async def run_sentiment_analysis_system():
    """
    Ejecuta el sistema completo de análisis de sentimiento.
    """
    print("=" * 60)
    print("SENTIMENT ANALYSIS MULTI-AGENT SYSTEM")
    print("=" * 60)
    
    # 1. Crear agentes especializados
    agents = [
        DataCollectorAgent(),
        SentimentAnalyzerAgent(),
        TrendDetectorAgent(),
        ReportGeneratorAgent()
    ]
    
    # 2. Crear orquestador
    orchestrator = MultiAgentOrchestrator(agents)
    
    # 3. Definir workflow de 4 etapas
    workflow = [
        # Etapa 1: Recolección de datos
        [
            AgentTask(
                task_id="data_collection",
                description="Collect sentiment data from multiple sources",
                priority=10,
                complexity=0.5,
                estimated_tokens=300
            )
        ],
        
        # Etapa 2: Análisis de sentimiento
        [
            AgentTask(
                task_id="sentiment_analysis",
                description="Analyze sentiment of collected data",
                priority=9,
                complexity=0.7,
                estimated_tokens=800
            )
        ],
        
        # Etapa 3: Detección de tendencias
        [
            AgentTask(
                task_id="trend_detection",
                description="Detect trends in sentiment data",
                priority=8,
                complexity=0.6,
                estimated_tokens=500
            )
        ],
        
        # Etapa 4: Generación de reporte
        [
            AgentTask(
                task_id="report_generation",
                description="Generate comprehensive report",
                priority=10,
                complexity=0.8,
                estimated_tokens=600
            )
        ]
    ]
    
    # 4. Ejecutar workflow
    print("\n📊 Executing workflow...\n")
    results = await orchestrator.execute_workflow(workflow)
    
    # 5. Mostrar resultados por etapa
    stage_names = [
        "Data Collection",
        "Sentiment Analysis",
        "Trend Detection",
        "Report Generation"
    ]
    
    for i, (stage_name, stage_results) in enumerate(zip(stage_names, results)):
        print(f"\n{'=' * 60}")
        print(f"STAGE {i+1}: {stage_name}")
        print(f"{'=' * 60}")
        
        for result in stage_results:
            status = "✓ SUCCESS" if result.success else "✗ FAILED"
            print(f"\n{status}")
            print(f"Agent: {result.agent_name}")
            print(f"Task: {result.task_id}")
            print(f"Latency: {result.latency_ms:.2f}ms")
            print(f"Tokens: {result.tokens_used}")
            
            if result.success and result.output:
                print(f"\nOutput:")
                import json
                print(json.dumps(result.output, indent=2))
    
    # 6. Análisis de performance
    print(f"\n{'=' * 60}")
    print("PERFORMANCE ANALYSIS")
    print(f"{'=' * 60}")
    
    optimization_report = orchestrator.optimize_performance()
    
    print("\nSystem Metrics:")
    import json
    print(json.dumps(optimization_report["system_metrics"], indent=2))
    
    print("\nCost Metrics:")
    print(json.dumps(optimization_report["cost_metrics"], indent=2))
    
    if optimization_report["optimizations"]:
        print("\nOptimization Suggestions:")
        for opt in optimization_report["optimizations"]:
            print(f"\n- {opt}")
    
    # 7. Métricas por agente
    print(f"\n{'=' * 60}")
    print("AGENT METRICS")
    print(f"{'=' * 60}")
    
    agent_metrics = orchestrator.get_agent_metrics()
    for agent_name, metrics in agent_metrics.items():
        print(f"\n{agent_name}:")
        print(json.dumps(metrics, indent=2))
    
    print(f"\n{'=' * 60}")
    print("ANALYSIS COMPLETE")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    asyncio.run(run_sentiment_analysis_system())
