"""
Multi-Agent Orchestrator - Coordinación y Optimización

Implementación de referencia basada en:
https://github.com/wshobson/agents/blob/main/plugins/agent-orchestration/commands/multi-agent-optimize.md
"""

from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import PriorityQueue
import time
import asyncio


@dataclass
class AgentTask:
    """Tarea asignada a un agente."""
    task_id: str
    description: str
    priority: int  # 1-10
    complexity: float  # 0.0-1.0
    estimated_tokens: int
    timeout_seconds: float = 30.0


@dataclass
class AgentResult:
    """Resultado de ejecución de un agente."""
    task_id: str
    agent_name: str
    output: Any
    success: bool
    latency_ms: float
    tokens_used: int
    error: Optional[str] = None


class BaseAgent:
    """Clase base para agentes especializados."""
    
    def __init__(self, name: str, specialization: str):
        self.name = name
        self.specialization = specialization
        self.performance_history: List[AgentResult] = []
    
    async def execute(
        self,
        task: AgentTask,
        context: Dict[str, Any]
    ) -> AgentResult:
        """
        Ejecuta una tarea.
        
        Args:
            task: Tarea a ejecutar
            context: Contexto compartido
        
        Returns:
            Resultado de la ejecución
        """
        start_time = time.time()
        
        try:
            # Implementación específica en subclases
            output = await self._execute_impl(task, context)
            
            latency_ms = (time.time() - start_time) * 1000
            
            result = AgentResult(
                task_id=task.task_id,
                agent_name=self.name,
                output=output,
                success=True,
                latency_ms=latency_ms,
                tokens_used=task.estimated_tokens  # Placeholder
            )
            
        except Exception as e:
            latency_ms = (time.time() - start_time) * 1000
            
            result = AgentResult(
                task_id=task.task_id,
                agent_name=self.name,
                output=None,
                success=False,
                latency_ms=latency_ms,
                tokens_used=0,
                error=str(e)
            )
        
        self.performance_history.append(result)
        return result
    
    async def _execute_impl(
        self,
        task: AgentTask,
        context: Dict[str, Any]
    ) -> Any:
        """
        Implementación específica del agente.
        Debe ser sobreescrita en subclases.
        """
        raise NotImplementedError
    
    def get_metrics(self) -> Dict[str, Any]:
        """Retorna métricas de performance del agente."""
        if not self.performance_history:
            return {}
        
        successes = sum(1 for r in self.performance_history if r.success)
        success_rate = successes / len(self.performance_history)
        
        avg_latency = sum(
            r.latency_ms for r in self.performance_history
        ) / len(self.performance_history)
        
        total_tokens = sum(r.tokens_used for r in self.performance_history)
        
        return {
            "agent_name": self.name,
            "specialization": self.specialization,
            "success_rate": success_rate,
            "avg_latency_ms": avg_latency,
            "total_tokens": total_tokens,
            "total_tasks": len(self.performance_history)
        }


class SearchAgent(BaseAgent):
    """Agente especializado en búsqueda."""
    
    def __init__(self):
        super().__init__("SearchAgent", "information_retrieval")
    
    async def _execute_impl(
        self,
        task: AgentTask,
        context: Dict[str, Any]
    ) -> Any:
        # Simulación de búsqueda
        await asyncio.sleep(0.1)
        return {
            "results": ["Result 1", "Result 2", "Result 3"],
            "source": "search_engine"
        }


class AnalysisAgent(BaseAgent):
    """Agente especializado en análisis."""
    
    def __init__(self):
        super().__init__("AnalysisAgent", "data_analysis")
    
    async def _execute_impl(
        self,
        task: AgentTask,
        context: Dict[str, Any]
    ) -> Any:
        # Simulación de análisis
        await asyncio.sleep(0.15)
        return {
            "analysis": "Detailed analysis results",
            "insights": ["Insight 1", "Insight 2"]
        }


class SynthesisAgent(BaseAgent):
    """Agente especializado en síntesis."""
    
    def __init__(self):
        super().__init__("SynthesisAgent", "synthesis")
    
    async def _execute_impl(
        self,
        task: AgentTask,
        context: Dict[str, Any]
    ) -> Any:
        # Simulación de síntesis
        await asyncio.sleep(0.08)
        return {
            "synthesis": "Combined results from multiple sources",
            "confidence": 0.85
        }


class PerformanceTracker:
    """Seguimiento de performance del sistema."""
    
    def __init__(self):
        self.executions: List[AgentResult] = []
        self.agent_metrics: Dict[str, List[float]] = {}
    
    def log(self, agent_name: str, result: AgentResult):
        """Registra resultado de ejecución."""
        self.executions.append(result)
        
        if agent_name not in self.agent_metrics:
            self.agent_metrics[agent_name] = []
        
        self.agent_metrics[agent_name].append(result.latency_ms)
    
    def get_bottlenecks(self) -> List[str]:
        """Identifica cuellos de botella."""
        bottlenecks = []
        
        for agent_name, latencies in self.agent_metrics.items():
            avg_latency = sum(latencies) / len(latencies)
            
            # Si latencia promedio > 1000ms, es cuello de botella
            if avg_latency > 1000:
                bottlenecks.append(agent_name)
        
        return bottlenecks
    
    def get_system_metrics(self) -> Dict[str, Any]:
        """Retorna métricas del sistema completo."""
        if not self.executions:
            return {}
        
        successes = sum(1 for e in self.executions if e.success)
        success_rate = successes / len(self.executions)
        
        total_latency = sum(e.latency_ms for e in self.executions)
        avg_latency = total_latency / len(self.executions)
        
        total_tokens = sum(e.tokens_used for e in self.executions)
        
        return {
            "total_executions": len(self.executions),
            "success_rate": success_rate,
            "avg_latency_ms": avg_latency,
            "total_tokens": total_tokens,
            "bottlenecks": self.get_bottlenecks()
        }


class CostOptimizer:
    """Optimización de costos LLM."""
    
    def __init__(self, monthly_budget_tokens: int = 100000):
        self.token_budget = monthly_budget_tokens
        self.token_usage = 0
        
        self.model_costs = {
            'gpt-4o': 0.03,          # $/1K tokens
            'claude-opus': 0.015,
            'claude-haiku': 0.0025
        }
    
    def select_optimal_model(
        self,
        task_complexity: float  # 0.0-1.0
    ) -> str:
        """
        Selecciona modelo óptimo según complejidad y presupuesto.
        
        Args:
            task_complexity: Complejidad de 0.0 a 1.0
        
        Returns:
            Nombre del modelo recomendado
        """
        remaining_budget = self.token_budget - self.token_usage
        budget_ratio = remaining_budget / self.token_budget
        
        # High complexity + suficiente presupuesto = modelo premium
        if task_complexity > 0.8 and budget_ratio > 0.5:
            return 'gpt-4o'
        
        # Medium complexity = modelo intermedio
        elif task_complexity > 0.5:
            return 'claude-opus'
        
        # Low complexity o presupuesto bajo = modelo económico
        else:
            return 'claude-haiku'
    
    def track_usage(self, tokens: int, model: str):
        """Registra uso de tokens."""
        self.token_usage += tokens
    
    def get_cost_metrics(self) -> Dict[str, Any]:
        """Retorna métricas de costos."""
        remaining = self.token_budget - self.token_usage
        usage_percent = (self.token_usage / self.token_budget) * 100
        
        return {
            "token_budget": self.token_budget,
            "tokens_used": self.token_usage,
            "tokens_remaining": remaining,
            "usage_percent": usage_percent
        }


class MultiAgentOrchestrator:
    """
    Orquestador central de sistema multi-agente.
    
    Responsabilidades:
    - Distribución de tareas a agentes especializados
    - Ejecución paralela coordinada
    - Gestión de contexto compartido
    - Tracking de performance y costos
    """
    
    def __init__(self, agents: List[BaseAgent]):
        self.agents = {agent.name: agent for agent in agents}
        self.execution_queue = PriorityQueue()
        self.performance_tracker = PerformanceTracker()
        self.cost_optimizer = CostOptimizer()
        
        self.shared_context: Dict[str, Any] = {}
    
    async def execute_task(
        self,
        task: AgentTask,
        agent_selector: Optional[Callable] = None
    ) -> AgentResult:
        """
        Ejecuta una tarea individual.
        
        Args:
            task: Tarea a ejecutar
            agent_selector: Función para seleccionar agente
                           (None = auto-select por especialización)
        
        Returns:
            Resultado de la ejecución
        """
        # Seleccionar agente
        if agent_selector:
            agent = agent_selector(task, self.agents)
        else:
            agent = self._auto_select_agent(task)
        
        # Ejecutar
        result = await agent.execute(task, self.shared_context)
        
        # Tracking
        self.performance_tracker.log(agent.name, result)
        self.cost_optimizer.track_usage(
            result.tokens_used,
            self.cost_optimizer.select_optimal_model(task.complexity)
        )
        
        # Actualizar contexto si exitoso
        if result.success:
            self.shared_context[task.task_id] = result.output
        
        return result
    
    async def execute_parallel(
        self,
        tasks: List[AgentTask]
    ) -> List[AgentResult]:
        """
        Ejecuta múltiples tareas en paralelo.
        
        Args:
            tasks: Lista de tareas a ejecutar
        
        Returns:
            Lista de resultados
        """
        # Ejecutar todas las tareas concurrentemente
        results = await asyncio.gather(*[
            self.execute_task(task)
            for task in tasks
        ])
        
        return results
    
    async def execute_workflow(
        self,
        workflow: List[List[AgentTask]]
    ) -> List[List[AgentResult]]:
        """
        Ejecuta workflow con etapas secuenciales y paralelismo intra-etapa.
        
        Args:
            workflow: Lista de etapas, cada etapa es lista de tareas paralelas
        
        Returns:
            Resultados organizados por etapa
        """
        all_results = []
        
        for stage_tasks in workflow:
            # Ejecutar etapa en paralelo
            stage_results = await self.execute_parallel(stage_tasks)
            all_results.append(stage_results)
            
            # Actualizar contexto para siguiente etapa
            for result in stage_results:
                if result.success:
                    self.shared_context[f"stage_{len(all_results)}_{result.task_id}"] = result.output
        
        return all_results
    
    def _auto_select_agent(self, task: AgentTask) -> BaseAgent:
        """Selecciona agente automáticamente según heurística."""
        # Heurística simplificada basada en keywords
        task_lower = task.description.lower()
        
        if any(kw in task_lower for kw in ["search", "find", "lookup"]):
            return self.agents.get("SearchAgent", list(self.agents.values())[0])
        
        elif any(kw in task_lower for kw in ["analyze", "examine", "study"]):
            return self.agents.get("AnalysisAgent", list(self.agents.values())[0])
        
        elif any(kw in task_lower for kw in ["synthesize", "combine", "merge"]):
            return self.agents.get("SynthesisAgent", list(self.agents.values())[0])
        
        # Default: primer agente disponible
        return list(self.agents.values())[0]
    
    def optimize_performance(self) -> Dict[str, Any]:
        """
        Analiza performance y sugiere optimizaciones.
        
        Returns:
            Reporte de optimización
        """
        system_metrics = self.performance_tracker.get_system_metrics()
        bottlenecks = system_metrics.get("bottlenecks", [])
        
        optimizations = []
        
        # Optimizar cuellos de botella
        for agent_name in bottlenecks:
            optimizations.append({
                "agent": agent_name,
                "issue": "High latency",
                "suggestion": "Consider caching results or using faster model"
            })
        
        # Optimizar costos si usage > 80%
        cost_metrics = self.cost_optimizer.get_cost_metrics()
        if cost_metrics.get("usage_percent", 0) > 80:
            optimizations.append({
                "area": "Token usage",
                "issue": "High budget consumption",
                "suggestion": "Switch to more efficient models for low-complexity tasks"
            })
        
        return {
            "system_metrics": system_metrics,
            "cost_metrics": cost_metrics,
            "optimizations": optimizations
        }
    
    def get_agent_metrics(self) -> Dict[str, Any]:
        """Retorna métricas de todos los agentes."""
        return {
            agent_name: agent.get_metrics()
            for agent_name, agent in self.agents.items()
        }


# Ejemplo de uso
async def main():
    # Crear agentes especializados
    agents = [
        SearchAgent(),
        AnalysisAgent(),
        SynthesisAgent()
    ]
    
    # Crear orquestador
    orchestrator = MultiAgentOrchestrator(agents)
    
    # Definir workflow con 2 etapas
    workflow = [
        # Etapa 1: Búsqueda y análisis en paralelo
        [
            AgentTask(
                task_id="search_1",
                description="Search for AI trends",
                priority=8,
                complexity=0.6,
                estimated_tokens=500
            ),
            AgentTask(
                task_id="analyze_1",
                description="Analyze current data",
                priority=7,
                complexity=0.7,
                estimated_tokens=800
            )
        ],
        # Etapa 2: Síntesis de resultados
        [
            AgentTask(
                task_id="synthesize_1",
                description="Synthesize findings",
                priority=9,
                complexity=0.8,
                estimated_tokens=1000
            )
        ]
    ]
    
    # Ejecutar workflow
    results = await orchestrator.execute_workflow(workflow)
    
    print("=== Workflow Results ===")
    for i, stage_results in enumerate(results):
        print(f"\nStage {i+1}:")
        for result in stage_results:
            print(f"  Task {result.task_id}: {'✓' if result.success else '✗'} "
                  f"({result.latency_ms:.2f}ms)")
    
    # Análisis y optimización
    print("\n=== Performance Analysis ===")
    optimization_report = orchestrator.optimize_performance()
    
    import json
    print(json.dumps(optimization_report, indent=2))
    
    # Métricas por agente
    print("\n=== Agent Metrics ===")
    agent_metrics = orchestrator.get_agent_metrics()
    print(json.dumps(agent_metrics, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
