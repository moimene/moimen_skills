---
name: orquestar-agentes
description: Framework para orquestación multi-agente, gestión de contexto y auto-mejora recursiva. Úsese cuando el usuario quiera implementar sistemas de múltiples agentes coordinados, optimizar el rendimiento de agentes existentes, gestionar contexto compartido entre agentes, o implementar ciclos de mejora continua basados en métricas de performance.
---

# Orquestar Agentes - Agent Orchestration Framework

Blueprint para diseñar e implementar sistemas de múltiples agentes con gestión de contexto, auto-mejora recursiva y optimización de rendimiento.

## Rol del Modelo

Actúas como **arquitecto de sistemas multi-agente** especializado en orquestación, optimización de performance y gestión de estado distribuido. Tu objetivo es diseñar sistemas escalables donde múltiples agentes colaboran eficientemente, mantienen contexto coherente, y se auto-mejoran basándose en métricas de rendimiento.

---

## Cuándo Usar Esta Skill

- Diseñar sistemas con múltiples agentes especializados que colaboran
- Implementar gestión de contexto compartido entre agentes
- Optimizar el rendimiento de agentes mediante análisis de métricas
- Crear ciclos de auto-mejora recursiva (prompt engineering automático)
- Coordinar agentes con diferentes capacidades y especializaciones
- Resolver conflictos de información entre agentes
- Implementar observabilidad y debugging de flujos multi-agente

---

## Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────────┐
│              ORQUESTADOR CENTRAL                            │
│  - Distribución de tareas                                   │
│  - Gestión de contexto global                               │
│  - Resolución de conflictos                                 │
└────────────────┬────────────────────────────────────────────┘
                 │
      ┌──────────┼──────────┬──────────────┐
      │          │          │              │
┌─────▼────┐ ┌──▼──────┐ ┌─▼────────┐ ┌───▼────────┐
│ Agent A  │ │ Agent B │ │ Agent C  │ │ Context    │
│ Spec.    │ │ Spec.   │ │ Spec.    │ │ Manager    │
│ Domain 1 │ │ Domain 2│ │ Domain 3 │ │            │
└──────────┘ └─────────┘ └──────────┘ └────────────┘
      │          │          │              │
      └──────────┴──────────┴──────────────┘
                 │
           ┌─────▼──────┐
           │ Knowledge  │
           │ Base       │
           │ Compartida │
           └────────────┘
```

---

## 1. Context Manager - Gestión de Estado Compartido

### Responsabilidades Core

El Context Manager es el "tejido conectivo" que mantiene coherencia entre agentes:

- **Dynamic Context Tracking**: Seguimiento de objetivos actuales y sub-tareas
- **Selective Persistence**: Decisión de qué información mantener vs. descartar
- **Context Window Optimization**: Gestión inteligente del presupuesto de tokens
- **Cross-Agent Synchronization**: Estado coherente entre todos los agentes
- **Relevance Filtering**: Filtrado de información irrelevante o redundante

### Estrategia de Tracking

```python
# Pseudo-código: Actualización de estado
def update_workflow_state(message, current_state):
    """
    Analiza mensaje y actualiza estado global del workflow.
    """
    # 1. Extraer contexto semántico del mensaje
    new_context = extract_semantic_context(message)
    
    # 2. Fusionar con estado actual
    updated_state = merge_state(current_state, new_context)
    
    # 3. Eliminar contexto obsoleto
    pruned_state = prune_stale_context(updated_state)
    
    return pruned_state
```

### Memoria de Dos Niveles

| Tipo | Contenido | Persistencia |
|------|-----------|--------------|
| **Short-term** | Historial inmediato de chat | Volátil (sesión) |
| | Variables de tarea actual | Volátil |
| | Resultados intermedios | Volátil |
| **Long-term** | Patrones recurrentes | Persistente (Knowledge Base) |
| | Soluciones a problemas conocidos | Persistente |
| | Preferencias del usuario | Persistente |

### Optimización de Contexto

```python
def compress_history(history, max_tokens=2000):
    """
    Comprime historial manteniendo información crítica.
    """
    if count_tokens(history) <= max_tokens:
        return history
    
    # Resumen jerárquico
    summary = generate_hierarchical_summary(history)
    
    # Extraer fragmentos críticos
    critical_fragments = extract_critical_data_points(history)
    
    # Combinar resumen + fragmentos críticos
    return combine(summary, critical_fragments)
```

### Broadcast de Contexto Global

**Workflow de Sincronización:**

1. Agent A produce nueva información crítica
2. Context Manager detecta cambio de estado global
3. Broadcast a todos los agentes afectados
4. Actualización de contexto local en cada agente

**Resolución de Conflictos:**

```
┌─────────────────────────────────────────────┐
│ Conflicto detectado entre Agent A y Agent B│
├─────────────────────────────────────────────┤
│ 1. Analizar fuente y timestamp              │
│ 2. Aplicar lógica de resolución:            │
│    - Latest update wins (por defecto)       │
│    - Higher authority wins                  │
│    - Merge strategy (custom)                │
│ 3. Actualizar contexto global               │
│ 4. Notificar resolución a agentes           │
└─────────────────────────────────────────────┘
```

### Métricas de Evaluación

| Métrica | Target | Descripción |
|---------|--------|-------------|
| **Context Retention Rate** | >95% | % de información crítica preservada |
| **Token Efficiency** | >0.7 | Ratio información relevante / tokens |
| **Retrieval Latency** | <100ms | Tiempo para recuperar contexto histórico |
| **Orchestration Accuracy** | >98% | % de agentes con estado correcto |

---

## 2. Agent Self-Improvement - Mejora Recursiva

### Core Capabilities

- **Prompt Engineering Optimization**: Refinamiento iterativo de instrucciones
- **Reasoning Chain Analysis**: Análisis de cadenas de razonamiento
- **Tool Call Efficiency Auditing**: Auditoría de uso correcto de herramientas
- **Failure Mode Identification**: Identificación de patrones de fallo
- **Automated Capability Expansion**: Expansión automática de capacidades

### Análisis de Modos de Fallo (FMA)

#### Categorización de Fallos

| Categoría | Síntomas | Mitigación |
|-----------|----------|------------|
| **Reasoning Gaps** | Saltos en la lógica | Inyectar Chain-of-Thought (CoT) |
| **Tool Under-utilization** | No usar herramienta disponible | Refinar descripciones de herramientas |
| **Context Hallucination** | Inventar información | Implementar grounding checks |
| **Inefficient Paths** | Múltiples intentos innecesarios | Mejorar ejemplos few-shot |

#### Implementación de FMA

```python
def analyze_failure(interaction_log):
    """
    Analiza un fallo y sugiere mejora.
    """
    model_output = interaction_log['output']
    ground_truth = interaction_log['expected']
    
    # Detectar tipo de fallo
    if is_hallucination(model_output, ground_truth):
        return report_improvement_path(
            FAILURE_TYPE.HALLUCINATION,
            suggestion="Añadir grounding check explícito"
        )
    
    if tool_call_missed(model_output):
        return report_improvement_path(
            FAILURE_TYPE.TOOL_EFFICIENCY,
            suggestion="Ampliar docstring de herramienta"
        )
    
    if reasoning_incomplete(model_output):
        return report_improvement_path(
            FAILURE_TYPE.REASONING,
            suggestion="Forzar CoT paso a paso"
        )
```

### Optimización de Prompts (PO)

**Técnicas de Optimización:**

1. **Syntactic Refinement**: Mejorar claridad y estructura
2. **Few-Shot Engineering**: Seleccionar ejemplos más representativos
3. **Negative Constraint Injection**: Explicitar qué NO hacer

**Workflow de Optimización:**

```
1. Baseline: Ejecutar prompt actual con test suite
2. Generate: Crear 3 variantes del prompt
3. Evaluate: A/B testing con métricas objetivas
4. Select: Elegir elementos de mejor performance
5. Merge: Combinar mejores elementos
6. Deploy: Actualizar prompt en producción
```

### Refinamiento de Uso de Herramientas

**Acciones de Refinamiento:**

- ✓ Renombrar herramientas para mejor alineación semántica
- ✓ Expandir docstrings con descripciones detalladas de parámetros
- ✓ Añadir ejemplos de casos límite
- ✓ Documentar interacciones complejas entre herramientas

### Reasoning Chain Refinement (RCR)

**Métodos RCR:**

| Método | Descripción | Uso |
|--------|-------------|-----|
| **Step-by-Step Validation** | Validar cada paso antes de continuar | Razonamientos complejos |
| **Back-tracking Protocols** | Retry si output inválido | Operaciones críticas |
| **Self-Correction Loops** | Re-leer y buscar errores | Antes de output final |

---

## 3. Multi-Agent Optimization - Performance Engineering

### Profiling Multi-Agente

#### Agentes de Profiling Especializados

```python
class MultiAgentProfiler:
    """
    Orquesta profiling distribuido del sistema.
    """
    def __init__(self, target_system):
        self.agents = [
            DatabasePerformanceAgent(target_system),
            ApplicationPerformanceAgent(target_system),
            FrontendPerformanceAgent(target_system)
        ]
    
    def profile(self):
        performance_profile = {}
        
        # Profiling paralelo
        for agent in self.agents:
            profile = agent.profile()
            performance_profile[agent.name] = profile
        
        # Agregación de métricas
        return aggregate_performance_metrics(performance_profile)
```

#### Tipos de Agentes de Profiling

**Database Performance Agent:**
- Query execution time analysis
- Index utilization tracking
- Resource consumption monitoring

**Application Performance Agent:**
- CPU and memory profiling
- Algorithmic complexity assessment
- Concurrency and async operation analysis

**Frontend Performance Agent:**
- Rendering performance metrics
- Network request optimization
- Core Web Vitals monitoring

### Optimización de Context Window

**Técnicas:**

- Intelligent context compression
- Semantic relevance filtering
- Dynamic context window resizing
- Token budget management

```python
def compress_context(context, max_tokens=4000):
    """
    Compresión semántica basada en embeddings.
    """
    compressed_context = semantic_truncate(
        context,
        max_tokens=max_tokens,
        importance_threshold=0.7  # Solo contenido >70% relevante
    )
    return compressed_context
```

### Coordinación Eficiente de Agentes

**Principios de Coordinación:**

1. **Parallel Execution Design**: Maximizar paralelismo
2. **Minimal Inter-Agent Communication**: Reducir overhead
3. **Dynamic Workload Distribution**: Balanceo de carga automático
4. **Fault-Tolerant Interactions**: Resiliencia ante fallos

```python
class MultiAgentOrchestrator:
    """
    Orquestador con ejecución paralela y tracking de performance.
    """
    def __init__(self, agents):
        self.agents = agents
        self.execution_queue = PriorityQueue()
        self.performance_tracker = PerformanceTracker()
    
    def optimize(self, target_system):
        # Ejecución paralela con coordinación
        with ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(agent.optimize, target_system): agent
                for agent in self.agents
            }
            
            for future in as_completed(futures):
                agent = futures[future]
                result = future.result()
                self.performance_tracker.log(agent, result)
```

### Gestión de Costos LLM

**Estrategias de Optimización de Costos:**

| Estrategia | Impacto | Implementación |
|------------|---------|----------------|
| Token usage tracking | -30% costos | Logging detallado por agente |
| Adaptive model selection | -50% costos | Modelo según complejidad |
| Caching and result reuse | -40% costos | Cache inteligente |
| Efficient prompt engineering | -20% costos | Prompts más concisos |

```python
class CostOptimizer:
    def __init__(self):
        self.token_budget = 100000  # Presupuesto mensual
        self.token_usage = 0
        self.model_costs = {
            'gpt-4o': 0.03,
            'claude-opus': 0.015,
            'claude-haiku': 0.0025
        }
    
    def select_optimal_model(self, task_complexity):
        """
        Selección dinámica basada en complejidad vs presupuesto.
        """
        remaining_budget = self.token_budget - self.token_usage
        
        if task_complexity > 0.8 and remaining_budget > 50000:
            return 'gpt-4o'
        elif task_complexity > 0.5:
            return 'claude-opus'
        else:
            return 'claude-haiku'
```

### Reducción de Latencia

**Técnicas de Aceleración:**

- ✓ Predictive caching (pre-cargar contexto probable)
- ✓ Pre-warming agent contexts (inicialización anticipada)
- ✓ Intelligent result memoization (cache de resultados)
- ✓ Reduced round-trip communication (batching)

---

## Workflows de Referencia

### Workflow 1: Optimización Recursiva de Agente

```
┌──────────────────────────────────────────────────────┐
│ 1. ANÁLISIS DE MÉTRICAS                              │
│    - Recolectar logs históricos                      │
│    - Calcular success rate, tool efficiency          │
│    - Identificar patrones de fallo                   │
├──────────────────────────────────────────────────────┤
│ 2. FAILURE MODE ANALYSIS                             │
│    - Categorizar fallos (hallucination, tools, etc.) │
│    - Priorizar por frecuencia e impacto              │
├──────────────────────────────────────────────────────┤
│ 3. PROMPT OPTIMIZATION                               │
│    - Generar 3 variantes del prompt                  │
│    - A/B testing con test suite                      │
│    - Seleccionar mejores elementos                   │
├──────────────────────────────────────────────────────┤
│ 4. VALIDATION                                        │
│    - Unit tests para lógica específica               │
│    - Integration tests para workflows                │
│    - Stress tests con inputs adversariales           │
├──────────────────────────────────────────────────────┤
│ 5. DEPLOYMENT                                        │
│    - Deploy improved prompt                          │
│    - Monitor performance metrics                     │
│    - Iterate si no alcanza target                    │
└──────────────────────────────────────────────────────┘
```

### Workflow 2: Sistema Multi-Agente E-Commerce

```
User Query: "Buscar productos similares y comparar precios"
    │
    ▼
┌─────────────────────────────────┐
│ ORQUESTADOR                     │
│ - Parse query                   │
│ - Distribute sub-tasks          │
└────┬─────────┬──────────┬───────┘
     │         │          │
     ▼         ▼          ▼
┌─────────┐ ┌──────┐ ┌──────────┐
│Search   │ │Price │ │Review    │
│Agent    │ │Agent │ │Agent     │
└────┬────┘ └───┬──┘ └────┬─────┘
     │          │         │
     └──────────┴────┬────┘
                     ▼
            ┌─────────────────┐
            │ CONTEXT MANAGER │
            │ - Merge results │
            │ - Resolve conf. │
            └────────┬────────┘
                     ▼
            ┌─────────────────┐
            │ RESPONSE        │
            │ SYNTHESIS       │
            └─────────────────┘
```

---

## Patrones de Implementación

### Patrón 1: Agent Delegation

```python
class TaskOrchestrator:
    """
    Delega tareas a agentes especializados.
    """
    def __init__(self):
        self.agents = {
            'search': SearchAgent(),
            'analysis': AnalysisAgent(),
            'synthesis': SynthesisAgent()
        }
        self.context_manager = ContextManager()
    
    async def execute(self, task):
        # Determinar agentes necesarios
        required_agents = self.identify_agents(task)
        
        # Ejecutar en paralelo
        results = await asyncio.gather(*[
            agent.execute(task, self.context_manager)
            for agent in required_agents
        ])
        
        # Synthesis de resultados
        return self.synthesize(results)
```

### Patrón 2: Feedback Loop

```python
class SelfImprovingAgent:
    """
    Agente con ciclo de mejora continua.
    """
    def __init__(self):
        self.performance_metrics = PerformanceTracker()
        self.prompt_optimizer = PromptOptimizer()
    
    async def execute_with_improvement(self, task):
        # Ejecutar tarea
        result = await self.execute(task)
        
        # Registrar métricas
        self.performance_metrics.log(task, result)
        
        # Si performance < threshold, mejorar
        if self.performance_metrics.success_rate < 0.9:
            improved_prompt = self.prompt_optimizer.optimize(
                current_prompt=self.system_prompt,
                failures=self.performance_metrics.get_failures()
            )
            self.system_prompt = improved_prompt
        
        return result
```

---

## Checklist de Implementación

### Sistema Multi-Agente

- [ ] Definir roles y especializaciones de cada agente
- [ ] Implementar Context Manager centralizado
- [ ] Configurar comunicación inter-agente
- [ ] Establecer protocolo de resolución de conflictos
- [ ] Implementar logging distribuido

### Auto-Mejora

- [ ] Definir métricas de success (accuracy, latency, cost)
- [ ] Implementar recolección de logs de interacciones
- [ ] Crear test suite para validation
- [ ] Configurar pipeline de A/B testing
- [ ] Establecer thresholds para mejora automática

### Optimización

- [ ] Profiling inicial del sistema
- [ ] Identificar bottlenecks principales
- [ ] Implementar caching estratégico
- [ ] Configurar model selection adaptativo
- [ ] Establecer monitoring de costos

---

## Anti-patrones a Evitar

| ❌ Evitar | ✓ Usar |
|-----------|--------|
| Context sin límites | Context window con límite estricto |
| Broadcast indiscriminado | Broadcast selectivo (solo afectados) |
| Agentes monolíticos | Agentes especializados y modulares |
| Prompts estáticos | Prompts auto-optimizados |
| Sin métricas | Tracking exhaustivo de performance |
| Ejecución secuencial | Ejecución paralela cuando sea posible |
| Single source of truth mutable | Immutable state + versioning |

---

## Recursos

- [Context Manager Implementation](resources/context_manager.py)
- [Self-Improvement Framework](resources/self_improvement.py)
- [Multi-Agent Orchestrator](resources/orchestrator.py)
- [Performance Profiling Tools](resources/profiling_tools.py)

---

## Regla Final

> **La orquestación efectiva de agentes requiere: contexto compartido coherente, mejora continua basada en métricas, y optimización adaptativa de recursos.**
