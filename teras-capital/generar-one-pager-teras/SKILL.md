---
name: generar-one-pager-teras
capa: L3a-tareas
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras, challenge-cognitivo-teras]
triggers: >
  Se activa cuando el usuario pida: one-pager, one pager, resumen ejecutivo
  de 1 página, ficha de una página, teaser, "resume esto en una página",
  o cualquier referencia a producir un documento ejecutivo de 1 página.
description: >
  Generador end-to-end de one-pagers TERAS. Máxima densidad informativa en
  1 página. Workflow: intake → estructura → contenido → challenge → lint → entrega.
---

# Generar One-Pager TERAS — Workflow End-to-End

## 1. Misión

Producir one-pagers de **máxima densidad informativa** en exactamente 1 página,
con estructura, tono y brand TERAS.

> **Un buen one-pager dice más en 1 página que un mal informe en 20.**

---

## 2. Intake

```
INTAKE ONE-PAGER:
  1. ¿Para quién? [Audiencia]
  2. ¿Sobre qué? [Tema/activo/deal/concepto]
  3. ¿3-5 key messages? [Los mensajes que DEBEN estar]
  4. ¿Sensibilidad? [Nivel de confidencialidad]
  5. ¿Call to action? [Qué queremos que haga el lector]
```

---

## 3. Estructura por Tipo

### 3.1 One-Pager de Activo/Deal

```
[LOGO TERAS]                                    [Clasificación]

TÍTULO: [Nombre del activo/deal]
SUBTÍTULO: [1 frase que capture la tesis]

CONTEXTO                          PROPUESTA TERAS
[3-4 líneas: sector, tamaño,     [3-4 líneas: qué hacemos,
situación, oportunidad]           cómo, con qué mandato]

PLAN DE EJECUCIÓN                 ECONOMIC ALIGNMENT
[3-5 bullets: fases y KPIs]       [3 bullets: fees, upside, governance]

KEY METRICS
| Métrica 1 | Métrica 2 | Métrica 3 | Métrica 4 |
|-----------|-----------|-----------|-----------|
| [valor]   | [valor]   | [valor]   | [valor]   |

NEXT STEPS
[2-3 acciones concretas con fecha]

[Footer: TERAS Capital | Fecha | Clasificación | Contacto]
```

### 3.2 One-Pager Corporativo TERAS

```
[LOGO TERAS]

QUÉ ES TERAS CAPITAL
[3-4 líneas: operating manager + coinversor minoritario, sectores, modelo]

CÓMO OPERAMOS                     ALINEACIÓN ECONÓMICA
[4-5 bullets: execution engine]   [3 bullets: fees + upside + governance]

SECTORES CORE
[Telco | Infra Digital | Sports Infra | Energía | Real Estate]

DIFERENCIACIÓN
[3-4 bullets: por qué somos distintos, SIN hype]

CONTACTO
[Datos mínimos]
```

### 3.3 One-Pager de Tema/Análisis

```
[LOGO TERAS]                                    [Clasificación]

TÍTULO: [Tema]

CONTEXTO (por qué importa)
[3-4 líneas]

ANÁLISIS CLAVE
[5-7 bullets con datos y conclusiones]

IMPLICACIONES PARA [ACTIVO/TERAS]
[3-4 bullets: qué significa esto para nosotros]

RECOMENDACIÓN / POSICIÓN TERAS
[2-3 líneas claras]

NEXT STEPS
[2-3 acciones]
```

---

## 4. Reglas de Densidad

| Regla | Descripción |
|-------|-------------|
| **Exactamente 1 página** | Si no cabe, cortar. Si sobra, añadir |
| **Cada palabra cuenta** | Eliminar todo adjetivo que no añada info |
| **Datos > narrativa** | Preferir cifra a párrafo |
| **No repetir** | Cada idea aparece 1 sola vez |
| **Títulos informativos** | "Revenue +15% YoY" no "Resultados financieros" |
| **Visual hierarchy** | Usar layout 2 columnas, tablas compactas, negrita selectiva |
| **Brand system** | Colores, tipografía y tono TERAS |

---

## 5. Validación

```
ONE-PAGER LINT 1 — ¿Cabe en exactamente 1 página?
ONE-PAGER LINT 2 — ¿El lector capta los 3-5 key messages en 30 segundos?
ONE-PAGER LINT 3 — ¿Toda cifra tiene fuente o está marcada como supuesto?
ONE-PAGER LINT 4 — ¿Tono institucional, sin hype?
ONE-PAGER LINT 5 — ¿TERAS posicionado correctamente?
ONE-PAGER LINT 6 — ¿Clasificación de sensibilidad presente?
ONE-PAGER LINT 7 — ¿Call to action claro?
ONE-PAGER LINT 8 — ¿Brand system aplicado?
```

---

## Recursos

- [One-Pager Templates por Tipo](resources/one-pager-templates.md)
