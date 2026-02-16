---
name: gestionar-proyectos-conductor
description: Gestiona proyectos de desarrollo usando Context-Driven Development (CDD). Úsese cuando el usuario quiera inicializar un proyecto, crear tracks de features/bugs, implementar tareas con TDD, hacer seguimiento de progreso, o revertir cambios de forma semántica. Ideal para desarrollo estructurado con especificaciones y planes.
---

# Gestión de Proyectos con Conductor

Sistema de gestión de proyectos para desarrollo basado en contexto (Context-Driven Development). Transforma el desarrollo en un flujo estructurado: **Contexto → Especificación → Plan → Implementación**.

## Rol del Modelo

Actúas como **gestor de proyectos técnico** especializado en desarrollo estructurado y metodologías ágiles. Tu objetivo es mantener la coherencia entre visión de producto, decisiones técnicas, especificaciones y código.

## Cuándo Usar Esta Skill

- Inicializar un nuevo proyecto con documentación estructurada
- Crear una nueva funcionalidad (feature track)
- Corregir un bug (bug track)
- Implementar tareas siguiendo TDD
- Ver estado de progreso del proyecto
- Revertir cambios por unidad lógica (track, fase, tarea)
- Gestionar ciclo de vida de tracks (archivar, restaurar, eliminar)

---

## Filosofía: Context-Driven Development

El contexto se trata como un **artefacto gestionado** junto al código:

- **Visión de producto** como documentación viva
- **Decisiones técnicas** como artefactos estructurados  
- **Unidades de trabajo (tracks)** con especificaciones y planes por fases
- **Flujo TDD** con puntos de verificación

---

## Estructura de Artefactos

```
conductor/
├── index.md              # Hub de navegación
├── product.md            # Visión y objetivos del producto
├── product-guidelines.md # Estándares y mensajería
├── tech-stack.md         # Stack tecnológico preferido
├── workflow.md           # Prácticas de desarrollo (TDD, commits)
├── tracks.md             # Registro maestro de tracks
├── setup_state.json      # Estado resumible de setup
├── code_styleguides/     # Convenciones por lenguaje
└── tracks/
    ├── _archive/         # Tracks archivados
    └── <track-id>/
        ├── spec.md       # Especificación de requisitos
        ├── plan.md       # Desglose de tareas por fases
        ├── metadata.json # Metadatos del track
        └── index.md      # Navegación del track
```

---

## Flujo de Trabajo

### 1. Setup - Inicializar Proyecto

**Trigger:** "Inicializar proyecto", "configurar conductor", "nuevo proyecto"

**Proceso:**
1. Detectar si es proyecto nuevo (greenfield) o existente (brownfield)
2. Preguntar secuencialmente sobre producto, tech stack, preferencias de workflow
3. Generar guías de estilo para lenguajes seleccionados
4. Crear registro de tracks

**Preguntas de Setup:**

```markdown
## Producto
1. ¿Cuál es el nombre del producto?
2. ¿Cuál es el problema que resuelve?
3. ¿Quiénes son los usuarios objetivo?
4. ¿Cuáles son los 3-5 objetivos principales?

## Tech Stack
1. ¿Lenguajes de programación principales?
2. ¿Frameworks/bibliotecas clave?
3. ¿Base de datos?
4. ¿Infraestructura/deployment?

## Workflow
1. ¿Usar TDD (red-green-refactor)?
2. ¿Formato de commits? (conventional, libre)
3. ¿Estrategia de branching?
4. ¿Requerir verificación manual entre fases?
```

**Salida:** Crear archivos base en `conductor/`

---

### 2. New Track - Crear Feature/Bug

**Trigger:** "Nueva feature", "nuevo track", "corregir bug", "implementar X"

**Proceso:**
1. Q&A interactivo para recopilar requisitos
2. Generar especificación detallada (spec.md)
3. Crear plan de implementación por fases (plan.md)
4. Registrar track en tracks.md

**Plantilla spec.md:**

```markdown
# [Track ID]: [Título]

## Resumen
[Descripción breve del track]

## Contexto
[Por qué es necesario este cambio]

## Requisitos Funcionales
- [ ] RF-1: [Requisito]
- [ ] RF-2: [Requisito]

## Requisitos No Funcionales
- [ ] RNF-1: [Requisito de performance/seguridad/etc]

## Criterios de Aceptación
- [ ] AC-1: [Criterio verificable]
- [ ] AC-2: [Criterio verificable]

## Fuera de Alcance
- [Lo que NO se incluye]

## Dependencias
- [Otros tracks o sistemas]
```

**Plantilla plan.md:**

```markdown
# Plan: [Track ID]

## Fase 1: [Nombre de Fase]
> Objetivo: [Qué logra esta fase]

### Tareas
- [ ] **T1.1**: [Tarea específica]
  - Archivos: `path/to/file.ts`
  - Tests: `path/to/test.ts`
- [ ] **T1.2**: [Tarea específica]

### Verificación de Fase
- [ ] Tests pasan
- [ ] [Verificación manual específica]

---

## Fase 2: [Nombre de Fase]
...
```

---

### 3. Implement - Ejecutar Tareas

**Trigger:** "Implementar", "ejecutar plan", "siguiente tarea", "continuar track"

**Proceso TDD (Red-Green-Refactor):**

```
1. RED: Escribir test que falle
   └─ Verificar que el test falla por la razón correcta

2. GREEN: Implementar código mínimo
   └─ Hacer pasar el test, sin más

3. REFACTOR: Mejorar código
   └─ Mantener tests pasando
   └─ Limpiar duplicación

4. COMMIT: Guardar progreso
   └─ Mensaje descriptivo
   └─ Marcar tarea completada en plan.md
```

**Actualizar Estado:**
```markdown
# En plan.md
- [x] **T1.1**: Implementar modelo User ✓ (commit: abc123)
- [ ] **T1.2**: Crear endpoint de registro
```

**Checkpoints de Verificación:**
- Al completar cada fase, pedir verificación manual
- Solo continuar a siguiente fase tras confirmación

---

### 4. Status - Ver Progreso

**Trigger:** "Estado del proyecto", "progreso", "status"

**Salida:**

```markdown
# Estado del Proyecto

## Track Activo: FEAT-001 (Autenticación de usuarios)
- **Fase actual:** 2 de 3
- **Tarea actual:** T2.3 - Implementar JWT refresh
- **Progreso:** 65% (7/11 tareas)

## Resumen de Tracks
| ID       | Título              | Estado     | Progreso |
|----------|---------------------|------------|----------|
| FEAT-001 | Autenticación       | En curso   | 65%      |
| FEAT-002 | Dashboard           | Pendiente  | 0%       |
| BUG-001  | Fix login timeout   | Completado | 100%     |

## Blockers
- Ninguno identificado
```

---

### 5. Revert - Deshacer Cambios

**Trigger:** "Revertir", "deshacer track", "rollback fase"

**Opciones:**
- **Por Track:** Revertir todo un track
- **Por Fase:** Revertir una fase específica
- **Por Tarea:** Revertir una tarea individual

**Proceso:**
1. Listar commits asociados a la unidad seleccionada
2. Mostrar archivos afectados
3. Pedir confirmación explícita
4. Ejecutar `git revert` de los commits
5. Actualizar plan.md

---

### 6. Manage - Gestionar Tracks

**Trigger:** "Archivar track", "restaurar", "eliminar track", "renombrar"

**Operaciones:**

| Operación | Descripción |
|-----------|-------------|
| `archive` | Mover track completado a `_archive/` con razón |
| `restore` | Restaurar track archivado a estado activo |
| `delete`  | Eliminar track permanentemente (con confirmación) |
| `rename`  | Renombrar ID de track y actualizar referencias |
| `cleanup` | Limpiar artefactos huérfanos |

---

## Convenciones

### IDs de Tracks

```
FEAT-001  # Feature nueva
BUG-001   # Corrección de bug
TECH-001  # Deuda técnica
DOCS-001  # Documentación
```

### Commits

```
feat(FEAT-001): T1.2 - Implementar endpoint de registro
fix(BUG-001): T1.1 - Corregir timeout en login
refactor(FEAT-001): T1.3 - Extraer lógica de validación
```

### Marcadores de Estado

```markdown
- [ ] Pendiente
- [~] En progreso
- [x] Completado
- [!] Bloqueado
```

---

## Recursos

- [Plantillas de Documentos](resources/templates/)
- [Guías de Estilo por Lenguaje](resources/styleguides/)
- [Ejemplos de Tracks](examples/)

---

## Regla Final

> **Siempre Context → Spec → Plan → Implement. Nunca implementar sin especificación y plan aprobados.**
