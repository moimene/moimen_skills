# Skill: Orquestar Agentes

Framework completo para orquestación de sistemas multi-agente con gestión de contexto compartido, auto-mejora recursiva y optimización de performance.

## 📋 Descripción

Esta skill te permite diseñar e implementar sistemas de múltiples agentes que:
- Colaboran eficientemente compartiendo contexto
- Se auto-mejoran basándose en métricas de rendimiento
- Optimizan costos y latencia de forma adaptativa
- Resuelven conflictos de información automáticamente
- Ejecutan workflows complejos con paralelismo controlado

## 🎯 Cuándo Usar

- Sistemas con múltiples agentes especializados (búsqueda, análisis, síntesis)
- Pipelines que requieren coordinación entre agentes
- Necesidad de gestión de contexto compartido
- Optimización continua de prompts y performance
- Análisis y reducción de costos LLM
- Debugging de flujos multi-agente complejos

## 📁 Estructura

```
orquestar-agentes/
├── SKILL.md                    # Blueprint principal con patrones y arquitectura
├── README.md                   # Este archivo
├── resources/                  # Implementaciones de referencia
│   ├── context_manager.py      # Gestión de estado compartido
│   ├── self_improvement.py     # Auto-mejora recursiva
│   ├── orchestrator.py         # Orquestador multi-agente
│   └── README.md              # Documentación de recursos
└── examples/                   # Ejemplos prácticos
    └── sentiment_analysis_system.py  # Sistema de análisis de sentimiento
```

## 🚀 Inicio Rápido

### 1. Activar la Skill

Desde tu proyecto, crea un enlace simbólico:

```bash
# Desde la raíz de tu proyecto
ln -s /Users/moisesmenendez/Dropbox/Codigo/agent/skills/orquestar-agentes .agent/skills/
```

O copia la skill a tu proyecto:

```bash
cp -r /Users/moisesmenendez/Dropbox/Codigo/agent/skills/orquestar-agentes tu-proyecto/.agent/skills/
```

### 2. Ejecutar Ejemplo

```bash
cd orquestar-agentes/examples
python sentiment_analysis_system.py
```

Esto ejecutará un sistema completo de análisis de sentimiento con:
- Recolección de datos
- Análisis de sentimiento
- Detección de tendencias
- Generación de reportes

### 3. Usar en tu Código

```python
from orchestrator import (
    MultiAgentOrchestrator,
    BaseAgent,
    AgentTask
)

# Crear agentes personalizados
class MiAgente(BaseAgent):
    def __init__(self):
        super().__init__("MiAgente", "mi_especialidad")
    
    async def _execute_impl(self, task, context):
        # Tu implementación
        return {"result": "output"}

# Orquestar
async def main():
    orchestrator = MultiAgentOrchestrator([MiAgente()])
    
    task = AgentTask("task_1", "Mi tarea", 8, 0.7, 500)
    result = await orchestrator.execute_task(task)
```

## 📖 Componentes Principales

### Context Manager
Gestiona estado compartido entre agentes con:
- Memoria de dos niveles (short-term / long-term)
- Resolución automática de conflictos
- Compresión de contexto
- Broadcast selectivo

### Self-Improvement Framework
Auto-mejora recursiva con:
- Análisis de modos de fallo (FMA)
- Optimización automática de prompts
- A/B testing de variantes
- Métricas de performance

### Multi-Agent Orchestrator
Coordinación de agentes con:
- Ejecución paralela de tareas
- Workflows con etapas secuenciales
- Auto-selección de agentes
- Tracking de costos y performance

## 🎓 Patrones Clave

### Patrón 1: Delegation
```python
orchestrator.execute_task(task)  # Auto-selecciona agente óptimo
```

### Patrón 2: Parallel Execution
```python
results = await orchestrator.execute_parallel([task1, task2, task3])
```

### Patrón 3: Multi-Stage Workflow
```python
workflow = [
    [task1, task2],  # Etapa 1: paralelo
    [task3]          # Etapa 2: secuencial
]
results = await orchestrator.execute_workflow(workflow)
```

### Patrón 4: Self-Improvement
```python
agent = SelfImprovingAgent(initial_prompt)
result = agent.execute_and_learn(task, expected_output)
# Auto-mejora si performance < threshold
```

## 📊 Métricas y Optimización

El sistema rastrea automáticamente:
- **Success rate**: % de tareas completadas exitosamente
- **Latency**: Tiempo de ejecución por tarea/agente
- **Token usage**: Consumo total y por agente
- **Bottlenecks**: Agentes con alta latencia
- **Conflicts**: Resoluciones en contexto compartido

Accede a las métricas:

```python
# Sistema completo
system_metrics = orchestrator.performance_tracker.get_system_metrics()

# Por agente
agent_metrics = agent.get_metrics()

# Sugerencias de optimización
report = orchestrator.optimize_performance()
```

## 🛠️ Extensión

### Crear Agente Personalizado

```python
from orchestrator import BaseAgent, AgentTask

class CustomAgent(BaseAgent):
    def __init__(self):
        super().__init__("CustomAgent", "custom_domain")
    
    async def _execute_impl(self, task: AgentTask, context):
        # Implementar lógica específica
        # Acceder a contexto compartido via context dict
        # Retornar output
        return {"output": "custom result"}
```

### Implementar Strategy de Resolución de Conflictos

```python
from context_manager import ContextManager

class CustomContextManager(ContextManager):
    def _handle_conflict(self, existing, new):
        # Implementar lógica custom
        # Por ejemplo: merge strategy
        merged_value = self.merge_values(existing.value, new.value)
        return ContextEntry(
            key=existing.key,
            value=merged_value,
            source_agent="merged",
            priority=max(existing.priority, new.priority)
        )
```

## 📚 Referencias

- [SKILL.md](SKILL.md) - Blueprint completo con arquitectura y patrones
- [resources/README.md](resources/README.md) - Documentación de implementaciones
- [GitHub: wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/agent-orchestration) - Inspiración original

## 🔗 Skills Relacionadas

- `automatizar-workflows-n8n` - Orquestación con n8n
- `integrar-lightrag-grafo-conocimiento` - RAG híbrido con grafos
- `error-handling-patterns` - Manejo de errores en sistemas distribuidos

## ⚡ Tips de Producción

1. **Persistir Context**: Usar Redis/PostgreSQL para long-term memory
2. **Monitoring**: Integrar OpenTelemetry para observabilidad
3. **Retry Logic**: Añadir circuit breakers para resiliencia
4. **Caching**: Implementar cache inteligente de resultados
5. **Model Selection**: Usar modelos eficientes para tareas simples (claude-haiku)

## 📝 Licencia

Basado en el plugin agent-orchestration de [wshobson/agents](https://github.com/wshobson/agents).

---

**Regla Final**: La orquestación efectiva requiere contexto coherente, mejora continua y optimización adaptativa.
