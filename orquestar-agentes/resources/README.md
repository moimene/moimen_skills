# Agent Orchestration - Recursos

Este directorio contiene implementaciones de referencia para los componentes clave del framework de orquestación de agentes.

## Archivos

### `context_manager.py`
Gestión de estado compartido entre agentes.

**Características:**
- Memoria de dos niveles (short-term / long-term)
- Resolución automática de conflictos
- Compresión de contexto para optimización de tokens
- Broadcast selectivo a agentes afectados
- Métricas de retention y conflict resolution

**Uso:**
```python
from context_manager import ContextManager

cm = ContextManager()

# Agent A actualiza contexto
cm.update_context(
    key="user_preference",
    value="dark_mode",
    source_agent="PreferenceAgent",
    priority=8
)

# Obtener estado actual
state = cm.get_current_state()
```

### `self_improvement.py`
Framework de auto-mejora recursiva de agentes.

**Características:**
- Análisis de modos de fallo (FMA)
- Optimización automática de prompts
- A/B testing de variantes
- Tracking de métricas de performance
- Inyección automática de CoT y grounding checks

**Uso:**
```python
from self_improvement import SelfImprovingAgent

agent = SelfImprovingAgent(initial_prompt="You are a helpful assistant.")

# Ejecutar tarea y aprender
result = agent.execute_and_learn(
    task="Search for AI trends",
    expected="Expected output"
)

# Ver métricas
metrics = agent.get_metrics()
```

### `orchestrator.py`
Orquestador central para sistemas multi-agente.

**Características:**
- Ejecución paralela de tareas
- Auto-selección de agentes por especialización
- Workflows con etapas secuenciales
- Tracking de performance y costos
- Optimización adaptativa de modelos
- Detección de cuellos de botella

**Uso:**
```python
import asyncio
from orchestrator import (
    MultiAgentOrchestrator,
    SearchAgent,
    AnalysisAgent,
    SynthesisAgent,
    AgentTask
)

async def main():
    # Crear agentes
    agents = [SearchAgent(), AnalysisAgent(), SynthesisAgent()]
    
    # Crear orquestador
    orchestrator = MultiAgentOrchestrator(agents)
    
    # Definir workflow
    workflow = [
        [  # Etapa 1: paralelo
            AgentTask("search_1", "Search for AI", 8, 0.6, 500),
            AgentTask("analyze_1", "Analyze data", 7, 0.7, 800)
        ],
        [  # Etapa 2: síntesis
            AgentTask("synth_1", "Synthesize", 9, 0.8, 1000)
        ]
    ]
    
    # Ejecutar
    results = await orchestrator.execute_workflow(workflow)
    
    # Optimizar
    report = orchestrator.optimize_performance()

asyncio.run(main())
```

## Extensión

Para crear agentes personalizados, extender `BaseAgent`:

```python
from orchestrator import BaseAgent, AgentTask

class CustomAgent(BaseAgent):
    def __init__(self):
        super().__init__("CustomAgent", "custom_domain")
    
    async def _execute_impl(self, task: AgentTask, context):
        # Implementación específica
        return {"result": "custom output"}
```

## Testing

Ejecutar las implementaciones de referencia:

```bash
# Context Manager
python resources/context_manager.py

# Self-Improvement
python resources/self_improvement.py

# Orchestrator
python resources/orchestrator.py
```

## Dependencias

```
# requirements.txt
asyncio
dataclasses
typing
concurrent.futures
queue
```

## Notas de Producción

- **Context Manager**: En producción, persistir long-term memory en base de datos (Redis/PostgreSQL)
- **Self-Improvement**: Integrar con plataforma LLM real (OpenAI/Anthropic) para ejecución y testing
- **Orchestrator**: Añadir retry logic, circuit breakers y observability (OpenTelemetry)
