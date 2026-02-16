# Plantilla: plan.md (Plan de Implementación)

```markdown
# Plan de Implementación: [TRACK-ID]

> **Track:** [Título]
> **Inicio:** [Fecha]
> **Estimación Total:** [X] días
> **Fases:** [N]

---

## Resumen de Fases

| Fase | Nombre | Tareas | Estimación | Estado |
|------|--------|--------|------------|--------|
| 1 | [Nombre] | [N] | [X]h | [ ] |
| 2 | [Nombre] | [N] | [X]h | [ ] |
| 3 | [Nombre] | [N] | [X]h | [ ] |

---

## Fase 1: [Configuración Inicial / Fundamentos]

> **Objetivo:** [Qué se logra al completar esta fase]
> **Estimación:** [X] horas
> **Dependencias:** Ninguna

### Tareas

#### T1.1: [Crear estructura base]
- **Descripción:** [Detalle de qué hacer]
- **Archivos:**
  - Crear: `src/features/[feature]/index.ts`
  - Modificar: `src/app/routes.ts`
- **Tests:** `tests/features/[feature]/index.test.ts`
- **Criterio de done:** [Cómo saber que está completo]
- **Estado:** [ ] Pendiente

#### T1.2: [Configurar dependencias]
- **Descripción:** [Detalle]
- **Archivos:**
  - Modificar: `package.json`
  - Crear: `src/config/[feature].ts`
- **Tests:** N/A (configuración)
- **Criterio de done:** [Criterio]
- **Estado:** [ ] Pendiente

### Verificación de Fase 1
- [ ] Estructura de archivos creada
- [ ] Dependencias instaladas
- [ ] Build exitoso
- [ ] Tests base pasan

### Commit de Fase
```
feat(TRACK-ID): Phase 1 complete - Initial setup
```

---

## Fase 2: [Core Implementation]

> **Objetivo:** [Qué se logra]
> **Estimación:** [X] horas
> **Dependencias:** Fase 1 completada

### Tareas

#### T2.1: [Implementar modelo de datos]
- **Descripción:** [Detalle con especificaciones técnicas]
- **Archivos:**
  - Crear: `src/models/[model].ts`
  - Crear: `src/repositories/[model].repository.ts`
- **Tests:** 
  - `tests/models/[model].test.ts`
  - `tests/repositories/[model].repository.test.ts`
- **TDD Steps:**
  1. RED: Test para validación de campos
  2. GREEN: Implementar modelo con validación
  3. REFACTOR: Extraer validadores reutilizables
- **Estado:** [ ] Pendiente

#### T2.2: [Implementar lógica de negocio]
- **Descripción:** [Detalle]
- **Archivos:**
  - Crear: `src/services/[feature].service.ts`
- **Tests:** `tests/services/[feature].service.test.ts`
- **TDD Steps:**
  1. RED: Test para caso principal
  2. GREEN: Implementar caso principal
  3. RED: Tests para edge cases
  4. GREEN: Manejar edge cases
  5. REFACTOR: Limpiar y documentar
- **Estado:** [ ] Pendiente

### Verificación de Fase 2
- [ ] Todos los tests unitarios pasan
- [ ] Cobertura > 80% para nuevos archivos
- [ ] Lógica de negocio validada
- [ ] Sin errores de linting

### Commit de Fase
```
feat(TRACK-ID): Phase 2 complete - Core logic implementation
```

---

## Fase 3: [API / Integration]

> **Objetivo:** [Qué se logra]
> **Estimación:** [X] horas
> **Dependencias:** Fase 2 completada

### Tareas

#### T3.1: [Crear endpoints]
- **Descripción:** Implementar endpoints REST según spec
- **Archivos:**
  - Crear: `src/routes/[feature].routes.ts`
  - Crear: `src/controllers/[feature].controller.ts`
- **Tests:** 
  - `tests/routes/[feature].routes.test.ts`
  - `tests/integration/[feature].integration.test.ts`
- **Estado:** [ ] Pendiente

#### T3.2: [Documentar API]
- **Descripción:** Añadir documentación OpenAPI
- **Archivos:**
  - Modificar: `docs/openapi.yaml`
- **Tests:** Validar schema con herramienta
- **Estado:** [ ] Pendiente

### Verificación de Fase 3
- [ ] Endpoints funcionan según spec
- [ ] Tests de integración pasan
- [ ] Documentación API actualizada
- [ ] Postman/Insomnia collection actualizada

---

## Fase 4: [UI / Frontend] (si aplica)

> **Objetivo:** [Qué se logra]
> **Estimación:** [X] horas
> **Dependencias:** Fase 3 completada

### Tareas

#### T4.1: [Crear componentes UI]
- **Descripción:** [Detalle con referencia a mockups]
- **Archivos:**
  - Crear: `src/components/[Feature]/[Component].tsx`
  - Crear: `src/components/[Feature]/[Component].test.tsx`
- **Tests:** Tests de componente con Testing Library
- **Estado:** [ ] Pendiente

#### T4.2: [Integrar con API]
- **Descripción:** Conectar UI con endpoints
- **Archivos:**
  - Crear: `src/hooks/use[Feature].ts`
  - Modificar: `src/pages/[Feature]Page.tsx`
- **Tests:** Mock de API en tests
- **Estado:** [ ] Pendiente

### Verificación de Fase 4
- [ ] UI matches mockups
- [ ] Integración con API funcional
- [ ] Tests de componente pasan
- [ ] Revisión de UX completada

---

## Fase 5: [QA / Polish]

> **Objetivo:** Asegurar calidad y preparar para release
> **Estimación:** [X] horas
> **Dependencias:** Todas las fases anteriores

### Tareas

#### T5.1: [Tests E2E]
- **Descripción:** Crear tests end-to-end para flujos críticos
- **Archivos:**
  - Crear: `e2e/[feature].spec.ts`
- **Estado:** [ ] Pendiente

#### T5.2: [Fix issues de QA]
- **Descripción:** Resolver issues encontrados en testing
- **Archivos:** TBD
- **Estado:** [ ] Pendiente

#### T5.3: [Documentación final]
- **Descripción:** Actualizar README, guías de usuario
- **Archivos:**
  - Modificar: `README.md`
  - Crear: `docs/guides/[feature].md`
- **Estado:** [ ] Pendiente

### Verificación Final
- [ ] Todos los criterios de aceptación cumplidos
- [ ] Tests E2E pasan
- [ ] Documentación completa
- [ ] Code review aprobado
- [ ] Ready for merge

---

## Notas de Implementación

### Decisiones Tomadas
- [Decisión 1]: [Razón]

### Problemas Encontrados
- [Problema 1]: [Solución aplicada]

### Deuda Técnica Identificada
- [ ] [Item de deuda técnica para futuro track]

---

## Historial de Progreso

| Fecha | Fase | Tarea | Commit | Notas |
|-------|------|-------|--------|-------|
| | | | | |
```
