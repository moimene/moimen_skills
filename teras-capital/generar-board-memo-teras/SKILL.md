---
name: generar-board-memo-teras
capa: L3a-tareas
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras, challenge-cognitivo-teras, validar-analisis-teras]
triggers: >
  Se activa cuando el usuario pida: board memo, memo para consejo, memo para
  board, nota al consejo, memo IC, nota para el comité, documento de decisión,
  o cualquier referencia a producir un memorando para un órgano de gobierno.
description: >
  Generador end-to-end de Board Memos y notas IC-grade. Documentos de decisión
  para Consejos de Administración, Investment Committees y otros órganos formales.
  Máxima formalidad y rigor analítico.
---

# Generar Board Memo TERAS — Workflow End-to-End

## 1. Misión

Producir memorandos de decisión **IC-grade** para órganos de gobierno formal.
Estos documentos soportan decisiones vinculantes y deben cumplir el estándar
más alto de rigor, claridad y trazabilidad.

---

## 2. Intake

```
INTAKE BOARD MEMO:
  1. ¿Para qué órgano? [Consejo de Administración / IC / Comité operativo / Board del activo]
  2. ¿Qué decisión se pide? [Aprobar / Autorizar / Tomar nota / Ratificar]
  3. ¿Sobre qué tema? [Específico]
  4. ¿Contexto? [Antecedentes, decisiones previas, urgencia]
  5. ¿Recomendación TERAS? [Si la hay]
  6. ¿Datos clave? [Cifras, KPIs, análisis disponible]
  7. ¿Sensibilidad? [IC-LP-Adjacent por defecto]
```

---

## 3. Estructura del Board Memo

```
═══════════════════════════════════════════════
MEMORANDO AL [ÓRGANO]
[Nombre de la entidad]

Punto del Orden del Día: [#]
Fecha: [fecha]
Preparado por: TERAS Capital
Clasificación: [IC-LP-Adjacent]
═══════════════════════════════════════════════

1. OBJETO
   [1-3 frases: qué se presenta y qué se solicita al órgano]

2. ANTECEDENTES
   [Contexto relevante: decisiones previas del órgano, evolución
   del tema, marco regulatorio si aplica. Factual.]

3. ANÁLISIS
   [Datos, métricas, comparativas. Todo con fuente.
   Si hay sensibilidad: caso base + estrés.
   Si hay opciones: ventajas/desventajas de cada una.
   Lenguaje IC-grade: sobrio, preciso, trazable.]

4. OPCIONES
   Opción A: [descripción]
     Ventajas: [lista]
     Riesgos: [lista]
     Impacto financiero: [cuantificado si posible]

   Opción B: [descripción]
     Ventajas: [lista]
     Riesgos: [lista]
     Impacto financiero: [cuantificado si posible]

5. RECOMENDACIÓN
   [Recomendación clara con fundamento.
   "Se recomienda al [órgano] que [acción específica] por [razones]."]

6. RIESGOS DE LA RECOMENDACIÓN
   [Principales riesgos + mitigantes + owners]

7. DECISIÓN SOLICITADA
   "Se solicita al [órgano] que:
   a) [Acción específica 1]
   b) [Acción específica 2 si aplica]"

8. PRÓXIMOS PASOS
   | Acción | Responsable | Plazo |
   |--------|------------|-------|

9. ANEXOS (si aplica)
   [Lista de documentos de soporte]
═══════════════════════════════════════════════
```

---

## 4. Reglas del Board Memo

| Regla | Descripción |
|-------|-------------|
| **Máx 3-4 páginas** | Si es más largo, hay un executive summary |
| **Decision-oriented** | Cada sección apunta a la decisión solicitada |
| **Opciones reales** | Mínimo 2 opciones cuando hay alternativas |
| **Riesgos explícitos** | Nunca omitir riesgos de la recomendación propia |
| **Lenguaje de gobierno** | "Se recomienda al Consejo que..." no "Nosotros creemos que..." |
| **Fuentes trazables** | Toda cifra con fuente |
| **Formato formal** | Numerado, estructurado, sin informalidades |

---

## 5. Validación

```
BOARD MEMO LINT 1 — ¿La decisión solicitada es clara y específica?
BOARD MEMO LINT 2 — ¿El análisis soporta la recomendación?
BOARD MEMO LINT 3 — ¿Hay opciones reales (no strawman)?
BOARD MEMO LINT 4 — ¿Los riesgos de la recomendación están explícitos?
BOARD MEMO LINT 5 — ¿Las cifras tienen fuente o están marcadas?
BOARD MEMO LINT 6 — ¿El lenguaje es de gobierno corporativo formal?
BOARD MEMO LINT 7 — ¿La clasificación de sensibilidad es correcta?
BOARD MEMO LINT 8 — ¿Se ha ejecutado challenge cognitivo?
BOARD MEMO LINT 9 — ¿Se ha ejecutado validación analítica?
BOARD MEMO LINT 10 — ¿Cabe en 3-4 páginas?
```

---

## Recursos

- [Board Memo Templates por Órgano](resources/board-memo-templates.md)
