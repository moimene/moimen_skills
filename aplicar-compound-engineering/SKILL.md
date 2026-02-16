---
name: aplicar-compound-engineering
description: Metodología de desarrollo donde cada unidad de trabajo hace el trabajo futuro más fácil. Úsese al planificar features, ejecutar trabajo, revisar código o codificar aprendizajes. Sigue el bucle Plan → Work → Review → Compound. Activar con planificar feature, implementar, revisar código, compound learnings.
---

# Compound Engineering

Metodología de desarrollo donde cada unidad de trabajo hace el trabajo futuro más fácil, no más difícil.

## Filosofía Central

> **Cada unidad de trabajo de ingeniería debe hacer que las unidades futuras sean más fáciles, no más difíciles.**

El desarrollo tradicional acumula deuda técnica. Cada feature añade complejidad. Compound Engineering invierte esto creando un bucle de aprendizaje donde cada bug, test fallido o insight se documenta y reutiliza.

---

## El Bucle Compound Engineering

```
Plan (40%) → Work (20%) → Review (20%) → Compound (20%) → (repetir)
```

**80% es planificación y revisión. 20% es ejecución.**

---

## Paso 1: Plan (40%)

Antes de escribir código, crear un plan comprehensivo. Buenos planes empiezan con investigación.

### Fase de Investigación

1. **Análisis del Codebase**: Buscar patrones similares, convenciones, precedentes
2. **Historial de Commits**: `git log` para entender cómo se construyeron features relacionadas
3. **Documentación**: README, AGENTS.md, documentación inline
4. **Investigación Externa**: Buscar best practices relevantes

### Estructura del Documento de Plan

```markdown
# Feature: [Nombre]

## Contexto
- ¿Qué problema resuelve?
- ¿A quién afecta?
- ¿Comportamiento actual vs deseado?

## Hallazgos de Investigación
- Patrones similares en codebase: [lista con links]
- Implementaciones previas: [referencias de commits]
- Best practices descubiertas: [referencias externas]

## Criterios de Aceptación
- [ ] Criterio 1 (testeable)
- [ ] Criterio 2 (testeable)
- [ ] Criterio 3 (testeable)

## Enfoque Técnico
1. Paso 1: [acción específica]
2. Paso 2: [acción específica]
3. Paso 3: [acción específica]

## Ejemplos de Código
[Snippets que siguen patrones existentes]

## Estrategia de Testing
- Unit tests: [qué testear]
- Integration tests: [qué testear]
- Verificación manual: [pasos]

## Riesgos y Mitigaciones
- Riesgo 1: [mitigación]
- Riesgo 2: [mitigación]
```

### Niveles de Detalle

| Nivel | Cuándo | Tiempo estimado |
|-------|--------|-----------------|
| **Mínimo** | Issues simples | 1-2 horas |
| **Estándar** | Consideraciones técnicas | 1-2 días |
| **Comprehensivo** | Decisiones de arquitectura | Multi-día |

---

## Paso 2: Work (20%)

Ejecutar el plan sistemáticamente.

### Flujo de Ejecución

1. **Crear entorno aislado**: Feature branch o git worktree
2. **Dividir en tareas**: Crear TODO list del plan
3. **Ejecutar sistemáticamente**: Una tarea a la vez
4. **Validar continuamente**: Tests después de cada cambio
5. **Commits incrementales**: Pequeños, enfocados, mensajes claros

### Principios de Trabajo

- Seguir patrones existentes descubiertos en investigación
- Ejecutar tests después de cada cambio significativo
- Si algo falla, entender por qué antes de continuar
- Mantener cambios enfocados—sin scope creep

### Quality Checks Durante Trabajo

```bash
# Después de cada cambio, verificar:
npm run typecheck    # o equivalente
npm test             # tests afectados
npm run lint         # calidad de código
```

---

## Paso 3: Review (20%)

Antes de mergear, realizar revisión comprehensiva.

### Checklist de Revisión

**Calidad de Código**
- [ ] Sigue patrones y convenciones del codebase
- [ ] Sin complejidad innecesaria—preferir duplicación sobre abstracción incorrecta
- [ ] Naming claro que coincide con convenciones
- [ ] Sin código de debug o console.logs

**Seguridad**
- [ ] Sin secrets o datos sensibles expuestos
- [ ] Validación de input donde necesario
- [ ] Manejo seguro de datos de usuario

**Performance**
- [ ] Sin regresiones obvias de performance
- [ ] Queries de DB eficientes (sin N+1)
- [ ] Caching apropiado si aplica

**Testing**
- [ ] Tests cubren criterios de aceptación
- [ ] Edge cases considerados
- [ ] Tests mantenibles, no frágiles

**Arquitectura**
- [ ] Cambio consistente con diseño del sistema
- [ ] Sin coupling innecesario introducido
- [ ] Sigue separación de responsabilidades

### Revisión Multi-Perspectiva

| Perspectiva | Pregunta |
|-------------|----------|
| Mantenedor | ¿Será fácil modificar en 6 meses? |
| Performance | ¿Hay cuellos de botella? |
| Seguridad | ¿Hay vulnerabilidades? |
| Simplicidad | ¿Puede ser más simple? |

---

## Paso 4: Compound (20%)

Aquí está la magia—capturar aprendizajes para hacer el trabajo futuro más fácil.

### Qué Compound

**Patrones**
```markdown
## Patrón: [Nombre]
Cuándo usar: [contexto]
Implementación: [código ejemplo]
Ver: [referencia de archivo]
```

**Decisiones**
```markdown
## Decisión: [Elección Hecha]
Contexto: [situación]
Opciones consideradas: [alternativas]
Razón: [por qué esta elección]
Consecuencias: [trade-offs]
```

**Fallos**
```markdown
## Lección: [Qué Salió Mal]
Síntoma: [qué se observó]
Causa raíz: [problema real]
Fix: [solución]
Prevención: [cómo evitar en futuro]
```

### Dónde Codificar Aprendizajes

| Ubicación | Uso |
|-----------|-----|
| `AGENTS.md` | Guía project-wide |
| `subdirectorio/AGENTS.md` | Guía específica de subsistema |
| Comentarios inline | Solo cuando código no es auto-explicativo |
| Test cases | Convertir bugs en tests de regresión |

### Preguntas Post-Trabajo

- ¿Qué aprendí que otros deberían saber?
- ¿Qué error cometí que puede prevenirse?
- ¿Qué patrón descubrí o creé?
- ¿Qué decisión se tomó y por qué?

---

## Comandos Prácticos

### Planificar Feature
```
Planificar implementación para: [describir feature]
- Investigar codebase por patrones similares
- Revisar git history por cambios relacionados
- Crear plan detallado con criterios de aceptación
- Incluir ejemplos de código que sigan patrones existentes
```

### Ejecutar Trabajo
```
Ejecutar este plan: [referencia plan]
- Crear feature branch
- Dividir en TODO list
- Trabajar sistemáticamente
- Ejecutar tests después de cada cambio
- Crear PR cuando complete
```

### Revisar Código
```
Revisar este cambio: [referencia PR/diff]
- Revisar issues de calidad de código
- Buscar concerns de seguridad
- Evaluar implicaciones de performance
- Verificar coverage de tests
- Sugerir mejoras
```

### Compound Learnings
```
Compound learnings de: [trabajo completado]
- ¿Qué patrones se usaron o crearon?
- ¿Qué decisiones se tomaron y por qué?
- ¿Qué fallos ocurrieron y cómo prevenirlos?
- Actualizar AGENTS.md con guía relevante
```

---

## Principios Clave

1. **Preferir duplicación sobre abstracción incorrecta**
2. **Documentar mientras avanzas**
3. **La calidad compone**
4. **Sistemático mejor que heroico**
5. **El conocimiento debe codificarse**

---

## Métricas de Éxito

Estás haciendo Compound Engineering bien cuando:

- ✓ Cada feature toma menos esfuerzo que la anterior similar
- ✓ Bugs se vuelven eventos únicos (documentados y prevenidos)
- ✓ Nuevos miembros son productivos rápido
- ✓ Code reviews encuentran menos issues
- ✓ Deuda técnica disminuye con el tiempo

---

## Regla Final

> **No solo estás construyendo features—estás construyendo un sistema de desarrollo que mejora con cada uso.**
