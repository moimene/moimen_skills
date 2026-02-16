---
name: preparar-reunion-clave
capa: L3b-escenarios
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras, challenge-cognitivo-teras]
triggers: >
  Se activa cuando el usuario diga: preparar reunión, meeting prep, preparar
  encuentro con [persona], pre-meeting, briefing de reunión, tengo reunión con,
  voy a ver a [persona], necesito preparar [nombre], o cualquier referencia
  a preparación de un encuentro con personas clave.
description: >
  Skill genérica de preparación de reuniones con personas clave. Genera un
  kit completo de preparación adaptado al interlocutor, contexto relacional,
  objetivos y riesgos. Funciona como sparring partner que prepara tanto
  el contenido como la estrategia relacional.
---

# Preparar Reunión Clave — Kit de Preparación TERAS

## 1. Misión

Cuando un miembro de TERAS dice "tengo reunión con [X]", este skill genera
un **kit completo de preparación** que cubre: quién es, qué quiere, qué
queremos nosotros, qué decir, qué no decir, y qué hacer después.

> **Principio**: Una reunión sin preparación es una reunión cedida al otro.

---

## 2. Intake Obligatorio

Antes de generar el kit, el sistema necesita (preguntar lo que falte):

```
INTAKE REUNIÓN:
  1. ¿Con quién? [Nombre, cargo, organización]
  2. ¿Qué relación tiene con TERAS? [Sponsor, management, advisor, regulador,
     potencial sponsor, coinversor, otro]
  3. ¿Qué se decide en esta reunión? [Objetivo específico]
  4. ¿Qué posición tiene TERAS? [Qué queremos conseguir]
  5. ¿Qué NO debemos decir? [Red lines de comunicación]
  6. ¿Hay antecedentes relevantes? [Última interacción, compromisos previos,
     temas pendientes, tensiones]
  7. ¿Contexto de activo? [Si aplica: Tuca, MPS, Templus, otro]
```

```
SI el usuario no proporciona todo:
  - Proceder con supuestos explícitos para los campos faltantes
  - Priorizar: Con quién + Qué se decide + Qué queremos
  - Los demás se pueden inferir razonablemente
```

---

## 3. Kit de Preparación — Estructura

### 3.1 Briefing de Contexto Relacional

```
═══════════════════════════════════════
BRIEFING REUNIÓN — [Nombre del interlocutor]
Fecha: [fecha]  |  Clasificación: [nivel]
═══════════════════════════════════════

INTERLOCUTOR:
  Nombre: [nombre]
  Cargo: [cargo]
  Organización: [org]
  Relación con TERAS: [tipo]

CONTEXTO RELACIONAL:
  - Historia: [resumen de la relación hasta ahora]
  - Último contacto: [fecha y tema]
  - Compromisos pendientes: [lista]
  - Tensiones/sensibilidades: [si las hay]

PERFIL DEL INTERLOCUTOR:
  - Qué le importa: [prioridades]
  - Qué teme: [preocupaciones]
  - Estilo de comunicación: [directo/diplomático/analítico/relacional]
  - Decision maker: [sí/no, quién decide]
```

### 3.2 Estrategia de la Reunión

```
OBJETIVO TERAS:
  Primario: [qué queremos conseguir]
  Secundario: [qué más sería positivo]
  Mínimo aceptable: [lo mínimo que justifica la reunión]

OBJETIVO DEL INTERLOCUTOR (estimado):
  [Qué creemos que busca y por qué]

ZONA DE ACUERDO:
  [Dónde coinciden los intereses → potencial de acuerdo]

ZONA DE TENSIÓN:
  [Dónde divergen los intereses → preparar posición]
```

### 3.3 Talking Points

```
TALKING POINTS — [reunión]

APERTURA (2 min):
  "[Agradecimiento breve + contexto + objetivo de la reunión en 1 frase]"

MENSAJE 1: [Tema principal]
  → Dato clave: [cifra o hecho que respalda]
  → Pedir: [qué queremos del interlocutor]

MENSAJE 2: [Tema secundario]
  → Dato clave: [cifra o hecho]
  → Pedir: [qué queremos]

MENSAJE 3: [Tema de relación / futuro]
  → Propuesta: [siguiente paso conjunto]

CIERRE:
  "[Resumen de acuerdos + next steps + timeline + agradecimiento]"
```

### 3.4 Preguntas Anticipadas

```
PREGUNTAS QUE NOS HARÁN:
  Q1: "[Pregunta probable]"
  → R1: "[Respuesta preparada]"
  → Si insisten: "[Respuesta de segundo nivel]"

  Q2: "[Pregunta probable]"
  → R2: "[Respuesta preparada]"

  Q3: "[Pregunta difícil]"
  → R3: "[Respuesta calibrada]"
  → Red line: "[Hasta dónde responder]"

PREGUNTAS QUE DEBEMOS HACER:
  1. "[Pregunta para obtener información clave]"
  2. "[Pregunta para validar supuestos]"
  3. "[Pregunta para avanzar a next steps]"
```

### 3.5 Red Lines y No-Go Zones

```
RED LINES (no cruzar bajo ninguna circunstancia):
  1. [Red line 1 — por qué]
  2. [Red line 2 — por qué]

NO MENCIONAR:
  - [Tema que no debemos levantar y por qué]
  - [Información confidencial de otro activo/sponsor]

SI NOS PRESIONAN SOBRE [tema sensible]:
  → Respuesta: "[Frase preparada para desviar sin mentir]"
  → Fallback: "Ese punto requiere análisis interno. Os volvemos con posición"
```

### 3.6 Follow-Up Plan

```
POST-REUNIÓN (dentro de 24h):
  1. Email de follow-up con resumen de acuerdos y next steps
  2. Actualizar CRM/tracker con outcomes
  3. Briefing interno al equipo TERAS
  4. Si se han hecho compromisos: asignar owner + deadline
  5. Si hay desviación del plan: escalar internamente
```

---

## 4. Adaptación por Tipo de Interlocutor

| Tipo | Tono | Foco | Precaución |
|------|------|------|------------|
| **Sponsor (deal team)** | Profesional-directo | KPIs, execution, next steps | No prometer sin validar |
| **Sponsor (IC)** | Ultra-formal, factual | Riesgos, governance, returns | Zero hype, evidencia |
| **Management (activo)** | Colaborativo, operativo | Plan, recursos, hitos | No micro-manage |
| **Potencial sponsor** | Institucional, propuesta de valor | Execution gap, alineación, track record | No revelar otros deals |
| **Regulador** | Formal, compliance | Cumplimiento, plazos, cooperación | No prometer lo incierto |
| **Coinversor** | Profesional, alineación | Governance, rights, economics | Proteger posición |
| **Asesor / Counsel** | Técnico, preciso | Scope, deliverables, plazos | Scope claro, sin ambigüedad |

---

## 5. Challenge Integrado

El sistema de challenge se aplica al kit de preparación:

```
CHALLENGE PRE-REUNIÓN:
  1. ¿Los talking points son defendibles con datos?
     → Si no: reforzar con evidencia o marcar como posición débil
  2. ¿Hay riesgos reputacionales en la posición de TERAS?
     → Si sí: reformular o preparar fallback
  3. ¿Las preguntas anticipadas cubren el peor escenario?
     → Si no: añadir la pregunta más incómoda posible
  4. ¿Los red lines están definidos?
     → Si no: definir antes de la reunión
  5. ¿El follow-up plan es realista?
     → Si no: ajustar compromisos al capacity real
```

---

## 6. Lint Pre-Reunión

```
MEETING LINT 1 — ¿Interlocutor identificado con contexto relacional?
MEETING LINT 2 — ¿Objetivo TERAS definido (primario + mínimo)?
MEETING LINT 3 — ¿Talking points fundamentados con datos?
MEETING LINT 4 — ¿Preguntas anticipadas preparadas (mín. 5)?
MEETING LINT 5 — ¿Red lines definidos?
MEETING LINT 6 — ¿Tono calibrado para el tipo de interlocutor?
MEETING LINT 7 — ¿No se revela información confidencial de otros activos?
MEETING LINT 8 — ¿Follow-up plan definido?
MEETING LINT 9 — ¿Challenge ejecutado sobre los talking points?
```

---

## Recursos

- [Templates de Follow-Up Email por Tipo](resources/templates-follow-up.md)
- [Guía de Tonos por Interlocutor](resources/guia-tonos.md)
