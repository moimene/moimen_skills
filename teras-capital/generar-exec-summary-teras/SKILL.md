---
name: generar-exec-summary-teras
capa: L3a-tareas
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras, challenge-cognitivo-teras, validar-analisis-teras]
triggers: >
  Se activa cuando el usuario pida: executive summary, resumen ejecutivo,
  "resume esto", "dame el resumen", "hazme un exec summary", extracto
  ejecutivo, o cualquier referencia a sintetizar información en formato
  ejecutivo.
description: >
  Generador de Executive Summaries TERAS. Sintetiza documentos largos,
  análisis complejos o situaciones multidimensionales en 1-2 páginas
  con estándar IC-grade. Optimizado para tomadores de decisión.
---

# Generar Executive Summary TERAS — Workflow End-to-End

## 1. Misión

Producir executive summaries que permitan a un tomador de decisión
**entender la situación y decidir en 3 minutos de lectura**.

---

## 2. Intake

```
INTAKE EXEC SUMMARY:
  1. ¿Fuente? [Documento a resumir / Briefing oral / Múltiples fuentes]
  2. ¿Para quién? [Audiencia: IC / Board / Sponsor / Management]
  3. ¿Decisión requerida? [Sí: cuál / No: solo informativo]
  4. ¿Extensión? [1 página / 2 páginas max]
  5. ¿Key messages obligatorios? [Los que DEBEN aparecer]
```

---

## 3. Estructura

```
EXECUTIVE SUMMARY
[Tema/Documento]  |  [Fecha]  |  [Clasificación]

CONTEXTO (2-3 líneas)
  [Qué es, por qué importa ahora, qué ha cambiado]

HALLAZGOS CLAVE (5-7 bullets max)
  • [Hallazgo 1 con dato]
  • [Hallazgo 2 con dato]
  • [Hallazgo 3 con dato]
  • [Hallazgo 4 con dato]
  • [Hallazgo 5 con dato]

IMPLICACIONES (3-4 bullets)
  • [Qué significa para TERAS / para el activo / para el sponsor]

RIESGOS (2-3 bullets)
  • [Riesgo 1 + mitigante]
  • [Riesgo 2 + mitigante]

RECOMENDACIÓN / POSICIÓN (si aplica)
  [1-2 frases claras]

DECISIÓN REQUERIDA (si aplica)
  [Qué se pide, a quién, para cuándo]

NEXT STEPS
  1. [Acción] — [Owner] — [Fecha]
  2. [Acción] — [Owner] — [Fecha]
```

---

## 4. Reglas del Exec Summary

| Regla | Descripción |
|-------|-------------|
| **Máx 2 páginas** | Si no cabe, el contenido necesita más filtrado |
| **Hallazgos = conclusiones** | No hechos genéricos, sino insights con implicación |
| **Datos concretos** | "Revenue creció 15%" no "Revenue mejoró" |
| **Standalone** | Debe entenderse sin leer el documento fuente |
| **Decision-oriented** | Siempre apuntar a una acción o posición |
| **Sin repetición** | Cada idea aparece 1 sola vez |
| **Coherencia con fuente** | No contradecir el documento original |

### Regla de Filtrado

```
Para decidir qué incluir en el exec summary:
  1. ¿Cambia una decisión? → INCLUIR
  2. ¿Revela un riesgo nuevo? → INCLUIR
  3. ¿Modifica una hipótesis? → INCLUIR
  4. ¿Es contexto ya conocido? → EXCLUIR
  5. ¿Es detalle operativo? → EXCLUIR (va a appendix)
  6. ¿Es interesante pero no accionable? → EXCLUIR
```

---

## 5. Validación

```
EXEC SUMMARY LINT 1 — ¿Se entiende sin leer el documento fuente?
EXEC SUMMARY LINT 2 — ¿Cada hallazgo tiene dato concreto?
EXEC SUMMARY LINT 3 — ¿Las implicaciones son específicas (no genéricas)?
EXEC SUMMARY LINT 4 — ¿Los riesgos tienen mitigantes?
EXEC SUMMARY LINT 5 — ¿Hay recomendación o posición clara?
EXEC SUMMARY LINT 6 — ¿Cabe en 1-2 páginas?
EXEC SUMMARY LINT 7 — ¿Es coherente con la fuente (no contradice)?
EXEC SUMMARY LINT 8 — ¿Challenge cognitivo ejecutado?
EXEC SUMMARY LINT 9 — ¿Tono IC-grade?
```

---

## Recursos

- [Exec Summary Templates por Contexto](resources/exec-summary-templates.md)
