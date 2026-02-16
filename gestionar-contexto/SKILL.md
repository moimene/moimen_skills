---
name: gestionar-contexto
description: Especialista en ingeniería de contexto avanzada, gestión de memoria semántica, bases de datos vectoriales, knowledge graphs y orquestación de flujos multi-agente. Preserva y restaura contexto de proyectos a través de sesiones con alta fidelidad.
---

# Context Management Skill

Skill de gestión inteligente de contexto para workflows de IA. Incluye capacidades de guardado, restauración y orquestación de contexto semántico.

## Componentes

### Agente: Context Manager
Especialista en ingeniería de contexto dinámico que domina:
- Bases de datos vectoriales (Pinecone, Weaviate, Qdrant)
- Knowledge graphs y sistemas semánticos
- Sistemas de memoria inteligente (long-term, episodic, semantic, working)
- RAG y recuperación de información
- Coordinación multi-agente

### Comandos

| Comando | Descripción |
|---------|-------------|
| `context-save` | Captura y serializa el estado del proyecto con embeddings semánticos |
| `context-restore` | Reconstruye contexto preservado con búsqueda por similitud |

## Uso

### Guardar Contexto
```bash
# Captura estándar
context-save $PROJECT_ROOT --type standard

# Captura comprehensiva con tags
context-save $PROJECT_ROOT --type comprehensive --tags "architecture,refactoring"
```

### Restaurar Contexto
```bash
# Restauración completa
context-restore project:mi-proyecto --mode full

# Restauración incremental
context-restore project:mi-proyecto --mode incremental

# Búsqueda semántica
context-restore project:mi-proyecto --query "estrategia de autenticación"
```

## Estructura
```
gestionar-contexto/
├── SKILL.md           # Este archivo
├── agents/
│   └── context-manager.md
└── commands/
    ├── context-save.md
    └── context-restore.md
```

## Patrones de Integración
- **RAG Pipelines**: Contexto como fuente para retrieval augmented generation
- **Multi-Agent**: Handoff de contexto entre agentes especializados
- **Enterprise KM**: Gestión de conocimiento institucional

## Ver También
- `orquestar-agentes`: Skill de orquestación multi-agente
- `integrar-lightrag-grafo-conocimiento`: Knowledge graph integration
