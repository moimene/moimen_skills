# Plantilla: workflow.md

```markdown
# Flujo de Trabajo de Desarrollo

## Metodología TDD

### Ciclo Red-Green-Refactor

1. **RED** - Escribir test que falle
   - El test debe fallar por la razón correcta
   - Verificar mensaje de error esperado
   
2. **GREEN** - Implementar código mínimo
   - Solo lo necesario para pasar el test
   - No optimizar prematuramente
   
3. **REFACTOR** - Mejorar código
   - Eliminar duplicación
   - Mejorar nombres y estructura
   - Tests deben seguir pasando

### Tipos de Tests

| Tipo | Cobertura Objetivo | Herramienta |
|------|-------------------|-------------|
| Unit | 80%+ | Vitest |
| Integration | Críticos | Vitest + Supertest |
| E2E | Happy paths | Playwright |

## Estrategia de Branching

```
main ─────────────────────────────────────────────►
         │                    │
         └── feat/FEAT-001 ──┘
                  │
                  ├── commit: T1.1
                  ├── commit: T1.2
                  └── merge ─► main
```

### Convenciones de Ramas

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| Feature | `feat/<track-id>` | `feat/FEAT-001` |
| Bugfix | `fix/<track-id>` | `fix/BUG-001` |
| Hotfix | `hotfix/<descripción>` | `hotfix/security-patch` |

## Convención de Commits

### Formato

```
<tipo>(<track-id>): <tarea> - <descripción>
```

### Tipos

| Tipo | Uso |
|------|-----|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de bug |
| `refactor` | Mejora de código sin cambio funcional |
| `test` | Añadir o modificar tests |
| `docs` | Documentación |
| `chore` | Mantenimiento, dependencias |

### Ejemplos

```
feat(FEAT-001): T1.2 - Implementar endpoint de registro
fix(BUG-001): T1.1 - Corregir timeout en login
refactor(FEAT-001): T1.3 - Extraer lógica de validación
test(FEAT-001): T2.1 - Añadir tests de integración
```

## Code Review

### Checklist de PR

- [ ] Tests pasan localmente
- [ ] Cobertura de tests adecuada
- [ ] Sin errores de linting
- [ ] Documentación actualizada
- [ ] Plan.md actualizado con tareas completadas
- [ ] Commits siguen convención

### Aprobaciones Requeridas

| Tipo de Cambio | Aprobaciones |
|----------------|--------------|
| Feature pequeña | 1 |
| Feature grande | 2 |
| Cambio arquitectónico | 2 + Tech Lead |
| Hotfix | 1 (fast-track) |

## Verificación Manual

### Puntos de Verificación

1. **Pre-implementación**: Spec y plan aprobados
2. **Entre fases**: Verificar criterios de fase antes de continuar
3. **Pre-merge**: Demo o revisión de funcionalidad
4. **Post-deploy**: Smoke test en staging/producción

### Template de Verificación

```markdown
## Verificación Fase [N]

- [ ] Todos los tests pasan
- [ ] [Verificación específica 1]
- [ ] [Verificación específica 2]
- [ ] Listo para siguiente fase

Verificado por: [Nombre]
Fecha: [Fecha]
```

## Deployment

### Ambientes

| Ambiente | Branch | Auto-deploy | URL |
|----------|--------|-------------|-----|
| Development | `develop` | Sí | dev.example.com |
| Staging | `main` | Sí | staging.example.com |
| Production | `main` + tag | Manual | example.com |

### Proceso de Release

1. Merge a `main`
2. Deploy automático a staging
3. Verificación en staging
4. Crear tag de versión
5. Deploy manual a producción
6. Verificación post-deploy
```
