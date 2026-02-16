---
name: generar-presentacion-teras
capa: L3a-tareas
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras, challenge-cognitivo-teras, desarrollar-ux-teras]
triggers: >
  Se activa cuando el usuario pida: presentación, deck, slides, pitch,
  PPTX, "hazme unas slides", "prepara una presentación para", o cualquier
  referencia a crear material visual de presentación.
description: >
  Generador end-to-end de presentaciones TERAS. Workflow completo: intake de
  contexto → estructura de slides → contenido → challenge → guardrails lint →
  UX lint → entrega. Aplica automáticamente el brand system TERAS.
---

# Generar Presentación TERAS — Workflow End-to-End

## 1. Misión

Producir presentaciones **IC-grade** que cumplan el brand system TERAS, estén
calibradas para la audiencia correcta y hayan pasado validación de contenido
y forma antes de entrega.

> **Cadena**: Intake → Estructura → Contenido → Challenge → Guardrails → UX Lint → Entrega

---

## 2. Intake Obligatorio

```
INTAKE PRESENTACIÓN:
  1. ¿Para quién? [Audiencia: Sponsor IC / Sponsor deal team / Management /
     Board / LP / Interno TERAS / Público]
  2. ¿Objetivo? [Informar / Persuadir / Decidir / Reportar]
  3. ¿Sobre qué? [Tema, activo, deal, concepto]
  4. ¿Datos clave? [Cifras, KPIs, hitos que deben aparecer]
  5. ¿Sensibilidad? [Público / Sponsor-confidential / TERAS-internal / IC-LP-Adjacent]
  6. ¿Extensión? [5-8 slides / 8-12 slides / 12-20 slides]
  7. ¿Contexto adicional? [Escenario: Steerco, Consejo, reunión, etc.]

SI falta información:
  → Proceder con supuestos explícitos
  → Priorizar: Audiencia + Objetivo + Tema
```

---

## 3. Estructura de Slides por Tipo

### 3.1 Presentación a Sponsor (Pitch/Intro)

```
Slide 1: Cover — TERAS Capital + tema + fecha + clasificación
Slide 2: Executive Summary — 3-5 key messages en bullets
Slide 3: Contexto / Oportunidad — El execution gap o la situación
Slide 4: Propuesta TERAS — Qué hacemos, cómo, con qué mandato
Slide 5: Plan de Ejecución — Fases, hitos, KPIs
Slide 6: Economic Alignment — Fees + upside + governance
Slide 7: Track Record / Credenciales — (solo verificable)
Slide 8: Next Steps — Acciones concretas con fecha
```

### 3.2 Presentación de Status/Steerco

```
Slide 1: Cover
Slide 2: Executive Summary — Estado en 1 slide
Slide 3: KPI Dashboard — Semáforos, tendencias
Slide 4-6: Deep Dive — Por área (comercial, operativo, financiero)
Slide 7: Risk Register — Top risks con mitigantes
Slide 8: Decisiones / Escalado — Qué necesitamos
Slide 9: Next Steps / Timeline
```

### 3.3 Presentación IC/Board

```
Slide 1: Cover
Slide 2: Decision Required — Qué se pide al IC/Board
Slide 3: Investment Thesis / Contexto
Slide 4: Análisis — Datos, comparativas, sensibilidad
Slide 5: Riesgos y Mitigantes
Slide 6: Economic Terms / Alignment
Slide 7: Governance Proposed
Slide 8: Recomendación — GO/NO-GO/CONDITIONAL
Slide 9: Appendix — Detalles de soporte
```

---

## 4. Reglas de Contenido por Slide

| Regla | Descripción |
|-------|-------------|
| **1 mensaje por slide** | Cada slide tiene 1 takeaway claro |
| **Título = conclusión** | El título de cada slide es la conclusión, no el tema |
| **Datos sobre narrativa** | Cifra → fuente → insight, no al revés |
| **Max 5 bullets por slide** | Si hay más, dividir en 2 slides |
| **No wall of text** | Si el texto no cabe en 30 segundos de lectura, sobra |
| **Footnotes para fuentes** | Toda cifra con footnote de fuente |
| **Clasificación en footer** | Nivel de sensibilidad en cada slide |

---

## 5. Brand System (heredado de desarrollar-ux-teras)

| Elemento | Especificación |
|----------|---------------|
| **Colores primarios** | Negro #000000, Rojo TERAS #EA3348, Gris #C6C9CC |
| **Tipografía** | Matter (headings), Messina Serif (body). Solo Regular |
| **Jerarquía** | Por tamaño, nunca por peso (no Bold, no Light) |
| **Logo** | Según manual UX. Zona protegida. Min 150px digital |
| **Gráficos** | T-system, patrones triangulares, concepto "bandada" |
| **Tono visual** | Sobrio, técnico, riguroso, moderno, austero |
| **Anti-patrones** | No rounded borders, no off-palette, no emojis decorativos |

---

## 6. Validación Post-Generación

```
PASO 1: CHALLENGE COGNITIVO
  - ¿Los datos de la presentación son defendibles?
  - ¿Hay afirmaciones sin evidencia?
  - ¿Las conclusiones tienen fundamento?
  → Corregir antes de continuar

PASO 2: GUARDRAILS LINT
  - ¿TERAS posicionado correctamente?
  - ¿Tono institucional, sin hype?
  - ¿Confidencialidad respetada?
  - ¿Audiencia calibrada?
  → Corregir antes de continuar

PASO 3: UX LINT
  - ¿Colores TERAS correctos?
  - ¿Tipografía según manual?
  - ¿Logo según especificaciones?
  - ¿1 mensaje por slide?
  - ¿Max 5 bullets?
  → Corregir antes de entregar
```

---

## 7. Lint del Generador

```
PRES LINT 1 — ¿Audiencia identificada y calibrada?
PRES LINT 2 — ¿Estructura sigue template del tipo correcto?
PRES LINT 3 — ¿Cada slide tiene 1 takeaway claro?
PRES LINT 4 — ¿Cifras con fuente o marcadas como supuesto?
PRES LINT 5 — ¿Brand system TERAS aplicado?
PRES LINT 6 — ¿Clasificación de sensibilidad en footer?
PRES LINT 7 — ¿Challenge cognitivo ejecutado?
PRES LINT 8 — ¿Guardrails lint passed?
```

---

## Recursos

- [Slide Templates por Tipo](resources/slide-templates.md)
- [Biblioteca de Diagramas TERAS](resources/biblioteca-diagramas.md)
