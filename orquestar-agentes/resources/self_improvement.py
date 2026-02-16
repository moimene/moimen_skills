"""
Agent Self-Improvement Framework

Implementación de referencia basada en:
https://github.com/wshobson/agents/blob/main/plugins/agent-orchestration/commands/improve-agent.md
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
import json


class FailureType(Enum):
    """Tipos de fallos identificables."""
    HALLUCINATION = "hallucination"
    TOOL_UNDERUSE = "tool_underuse"
    REASONING_GAP = "reasoning_gap"
    EFFICIENCY = "efficiency"
    UNKNOWN = "unknown"


@dataclass
class InteractionLog:
    """Log de una interacción del agente."""
    task: str
    output: str
    expected: Optional[str] = None
    tools_used: List[str] = None
    reasoning_steps: List[str] = None
    success: bool = False
    latency_ms: float = 0.0
    tokens_used: int = 0


@dataclass
class ImprovementSuggestion:
    """Sugerencia de mejora para el agente."""
    failure_type: FailureType
    description: str
    suggested_action: str
    priority: int  # 1-10
    estimated_impact: str  # "low", "medium", "high"


class FailureModeAnalyzer:
    """
    Analiza patrones de fallo y sugiere mejoras.
    """
    
    def __init__(self):
        self.failure_patterns: Dict[FailureType, int] = {}
    
    def analyze_interaction(
        self,
        interaction: InteractionLog
    ) -> List[ImprovementSuggestion]:
        """
        Analiza una interacción y detecta fallos.
        
        Args:
            interaction: Log de la interacción
        
        Returns:
            Lista de sugerencias de mejora
        """
        suggestions = []
        
        # 1. Detectar hallucination
        if interaction.expected and not interaction.success:
            if self._is_hallucination(
                interaction.output,
                interaction.expected
            ):
                suggestions.append(
                    ImprovementSuggestion(
                        failure_type=FailureType.HALLUCINATION,
                        description="Agent fabricated information",
                        suggested_action=(
                            "Add explicit grounding check: "
                            "'Only use information from the provided context'"
                        ),
                        priority=9,
                        estimated_impact="high"
                    )
                )
        
        # 2. Detectar tool under-utilization
        if self._tool_call_missed(interaction):
            suggestions.append(
                ImprovementSuggestion(
                    failure_type=FailureType.TOOL_UNDERUSE,
                    description="Failed to use available tool",
                    suggested_action=(
                        "Expand tool docstring with explicit use cases. "
                        "Add few-shot examples."
                    ),
                    priority=7,
                    estimated_impact="medium"
                )
            )
        
        # 3. Detectar reasoning gaps
        if self._reasoning_incomplete(interaction):
            suggestions.append(
                ImprovementSuggestion(
                    failure_type=FailureType.REASONING_GAP,
                    description="Logical steps missing in reasoning",
                    suggested_action=(
                        "Inject Chain-of-Thought requirement: "
                        "'Think step-by-step before answering'"
                    ),
                    priority=8,
                    estimated_impact="high"
                )
            )
        
        # 4. Detectar inefficiency
        if interaction.latency_ms > 5000 or interaction.tokens_used > 10000:
            suggestions.append(
                ImprovementSuggestion(
                    failure_type=FailureType.EFFICIENCY,
                    description="High latency or token usage",
                    suggested_action=(
                        "Optimize prompt length. "
                        "Use more efficient model for simple tasks."
                    ),
                    priority=5,
                    estimated_impact="medium"
                )
            )
        
        # Registrar patrones
        for suggestion in suggestions:
            self.failure_patterns[suggestion.failure_type] = (
                self.failure_patterns.get(suggestion.failure_type, 0) + 1
            )
        
        return suggestions
    
    def _is_hallucination(self, output: str, expected: str) -> bool:
        """Detecta si el output contiene información inventada."""
        # Implementación simplificada
        # En producción: usar embeddings para detectar divergencia semántica
        
        output_lower = output.lower()
        expected_lower = expected.lower()
        
        # Check si output contiene información no presente en expected
        output_words = set(output_lower.split())
        expected_words = set(expected_lower.split())
        
        # Si >50% de palabras no están en expected, probablemente hallucination
        unique_output = output_words - expected_words
        hallucination_ratio = len(unique_output) / max(len(output_words), 1)
        
        return hallucination_ratio > 0.5
    
    def _tool_call_missed(self, interaction: InteractionLog) -> bool:
        """Detecta si el agente no usó una herramienta disponible."""
        # Heurística: si la tarea requería herramienta pero no se usó
        task_lower = interaction.task.lower()
        
        tool_keywords = {
            "search": ["search", "find", "lookup"],
            "calculate": ["calculate", "compute", "math"],
            "analyze": ["analyze", "examine", "study"]
        }
        
        for tool_name, keywords in tool_keywords.items():
            if any(kw in task_lower for kw in keywords):
                if not interaction.tools_used or tool_name not in interaction.tools_used:
                    return True
        
        return False
    
    def _reasoning_incomplete(self, interaction: InteractionLog) -> bool:
        """Detecta si el razonamiento tiene gaps."""
        if not interaction.reasoning_steps:
            return True
        
        # Heurística: si tarea compleja pero pocos pasos de razonamiento
        task_complexity = len(interaction.task.split())
        reasoning_depth = len(interaction.reasoning_steps)
        
        # Tarea compleja (>20 palabras) debería tener >3 pasos
        if task_complexity > 20 and reasoning_depth < 3:
            return True
        
        return False
    
    def get_top_failures(self, n: int = 3) -> List[FailureType]:
        """Retorna los n tipos de fallo más frecuentes."""
        sorted_failures = sorted(
            self.failure_patterns.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return [f[0] for f in sorted_failures[:n]]


class PromptOptimizer:
    """
    Optimiza prompts basándose en análisis de performance.
    """
    
    def __init__(self):
        self.baseline_performance: Optional[Dict[str, float]] = None
    
    def optimize(
        self,
        current_prompt: str,
        failure_suggestions: List[ImprovementSuggestion]
    ) -> str:
        """
        Genera prompt optimizado basándose en sugerencias.
        
        Args:
            current_prompt: Prompt actual
            failure_suggestions: Lista de sugerencias de mejora
        
        Returns:
            Prompt optimizado
        """
        optimized = current_prompt
        
        # Ordenar por prioridad
        sorted_suggestions = sorted(
            failure_suggestions,
            key=lambda x: x.priority,
            reverse=True
        )
        
        # Aplicar mejoras top 3
        for suggestion in sorted_suggestions[:3]:
            if suggestion.failure_type == FailureType.HALLUCINATION:
                optimized = self._inject_grounding_check(optimized)
            
            elif suggestion.failure_type == FailureType.REASONING_GAP:
                optimized = self._inject_cot(optimized)
            
            elif suggestion.failure_type == FailureType.TOOL_UNDERUSE:
                optimized = self._emphasize_tools(optimized)
            
            elif suggestion.failure_type == FailureType.EFFICIENCY:
                optimized = self._compress_prompt(optimized)
        
        return optimized
    
    def _inject_grounding_check(self, prompt: str) -> str:
        """Inyecta checks de grounding."""
        grounding_instruction = (
            "\n\nIMPORTANT: Only use information explicitly provided "
            "in the context. If the answer is not in the context, "
            "say 'I don't have enough information to answer that.'"
        )
        
        if grounding_instruction not in prompt:
            return prompt + grounding_instruction
        return prompt
    
    def _inject_cot(self, prompt: str) -> str:
        """Inyecta Chain-of-Thought."""
        cot_instruction = (
            "\n\nThink step-by-step before providing your answer:"
            "\n1. Understand the question"
            "\n2. Identify relevant information"
            "\n3. Reason through the logic"
            "\n4. Formulate your answer"
        )
        
        if "step-by-step" not in prompt.lower():
            return prompt + cot_instruction
        return prompt
    
    def _emphasize_tools(self, prompt: str) -> str:
        """Enfatiza el uso de herramientas."""
        tool_instruction = (
            "\n\nREMEMBER: You have access to powerful tools. "
            "Always check if a tool can help before attempting "
            "to answer manually."
        )
        
        if "tools" not in prompt.lower():
            return prompt + tool_instruction
        return prompt
    
    def _compress_prompt(self, prompt: str) -> str:
        """Comprime el prompt eliminando redundancia."""
        # Implementación simplificada
        lines = prompt.split('\n')
        
        # Eliminar líneas duplicadas
        unique_lines = []
        seen = set()
        for line in lines:
            if line.strip() and line not in seen:
                unique_lines.append(line)
                seen.add(line)
        
        return '\n'.join(unique_lines)
    
    def a_b_test(
        self,
        variants: List[str],
        test_cases: List[Dict[str, Any]]
    ) -> str:
        """
        Ejecuta A/B testing de variantes de prompts.
        
        Args:
            variants: Lista de prompts a testear
            test_cases: Casos de prueba
        
        Returns:
            Mejor prompt según métricas
        """
        # En producción: ejecutar cada variante con LLM real
        # Por ahora: simulación
        
        results = {}
        for i, variant in enumerate(variants):
            # Simular métricas
            results[i] = {
                "success_rate": 0.0,  # Placeholder
                "avg_tokens": 0,
                "avg_latency_ms": 0.0
            }
        
        # Seleccionar mejor basándose en success_rate
        best_idx = max(results.items(), key=lambda x: x[1]["success_rate"])[0]
        return variants[best_idx]


class SelfImprovingAgent:
    """
    Agente con capacidad de auto-mejora recursiva.
    """
    
    def __init__(self, initial_prompt: str):
        self.system_prompt = initial_prompt
        self.fma = FailureModeAnalyzer()
        self.optimizer = PromptOptimizer()
        
        self.interaction_history: List[InteractionLog] = []
        self.improvement_history: List[Dict] = []
    
    def execute_and_learn(
        self,
        task: str,
        expected: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Ejecuta tarea y aprende de los resultados.
        
        Args:
            task: Tarea a ejecutar
            expected: Resultado esperado (para evaluación)
        
        Returns:
            Resultado de la ejecución
        """
        # En producción: ejecutar con LLM real
        # Por ahora: simulación
        
        interaction = InteractionLog(
            task=task,
            output="Simulated output",
            expected=expected,
            tools_used=[],
            reasoning_steps=[],
            success=False,  # Placeholder
            latency_ms=1000.0,
            tokens_used=500
        )
        
        self.interaction_history.append(interaction)
        
        # Analizar y mejorar si es necesario
        self._auto_improve()
        
        return {
            "output": interaction.output,
            "prompt_version": len(self.improvement_history)
        }
    
    def _auto_improve(self):
        """Auto-mejora basada en historial."""
        # Analizar últimas 10 interacciones
        recent = self.interaction_history[-10:]
        
        all_suggestions = []
        for interaction in recent:
            suggestions = self.fma.analyze_interaction(interaction)
            all_suggestions.extend(suggestions)
        
        # Si hay >3 sugerencias de alta prioridad, mejorar
        high_priority = [
            s for s in all_suggestions if s.priority >= 7
        ]
        
        if len(high_priority) >= 3:
            improved_prompt = self.optimizer.optimize(
                self.system_prompt,
                high_priority
            )
            
            # Log de mejora
            self.improvement_history.append({
                "previous_prompt": self.system_prompt,
                "new_prompt": improved_prompt,
                "reason": [s.description for s in high_priority[:3]]
            })
            
            self.system_prompt = improved_prompt
    
    def get_metrics(self) -> Dict[str, Any]:
        """Retorna métricas de performance del agente."""
        if not self.interaction_history:
            return {}
        
        successes = sum(1 for i in self.interaction_history if i.success)
        success_rate = successes / len(self.interaction_history)
        
        avg_latency = sum(
            i.latency_ms for i in self.interaction_history
        ) / len(self.interaction_history)
        
        avg_tokens = sum(
            i.tokens_used for i in self.interaction_history
        ) / len(self.interaction_history)
        
        return {
            "success_rate": success_rate,
            "avg_latency_ms": avg_latency,
            "avg_tokens": avg_tokens,
            "total_interactions": len(self.interaction_history),
            "improvements_made": len(self.improvement_history),
            "top_failure_types": [
                f.value for f in self.fma.get_top_failures()
            ]
        }


# Ejemplo de uso
if __name__ == "__main__":
    agent = SelfImprovingAgent(
        initial_prompt="You are a helpful assistant."
    )
    
    # Ejecutar varias tareas
    tasks = [
        ("Search for information about AI", None),
        ("Calculate 123 * 456", "56088"),
        ("Analyze this data: [1,2,3,4,5]", None)
    ]
    
    for task, expected in tasks:
        result = agent.execute_and_learn(task, expected)
        print(f"Task: {task}")
        print(f"Result: {result}\n")
    
    # Ver métricas
    metrics = agent.get_metrics()
    print("Agent Metrics:")
    print(json.dumps(metrics, indent=2))
