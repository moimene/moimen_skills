---
name: escenario-steerco-tuca
capa: L3b-escenarios
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras, challenge-cognitivo-teras]
triggers: >
  Se activa cuando el usuario mencione: Steerco Tuca, Steering Committee Tuca,
  comité directivo Tuca, reunión Tuca, preparar Tuca, activo Tuca, o cualquier
  referencia al activo Tuca en contexto de gobierno o reporting.
description: >
  Precarga contexto completo del Steering Committee del activo Tuca:
  actores, dinámica, objetivos TERAS, riesgos, tono, entregables y
  preparación. Convierte al LLM en un sparring partner que conoce el
  foro y sus reglas no escritas.
---

# Escenario: Steering Committee — Activo Tuca

## 1. Naturaleza del Foro

El **Steering Committee (Steerco) de Tuca** es el foro de decisión operativa
principal donde TERAS rinde cuentas como operating manager y defiende su mandato
de ejecución ante el sponsor.

### Características del Foro

| Aspecto | Descripción |
|---------|-------------|
| **Tipo** | Comité directivo operativo |
| **Periodicidad** | Regular (mensual/quincenal según fase) |
| **Nivel de decisión** | Operativo-táctico, con escalado a IC si aplica |
| **Formalidad** | Media-alta: agenda, acta, follow-up items |
| **Confidencialidad** | Sponsor-confidential |

---

## 2. Mapa de Actores

| Actor | Rol | Qué busca | Qué teme | Cómo tratarlo |
|-------|-----|-----------|----------|---------------|
| **Sponsor Deal Team** | Oversight, challenge, reporting al IC | Control, visibilidad de KPIs, confort de ejecución | Sorpresas, pérdida de control, desalineación | Datos primero, proactividad en riesgos, transparencia |
| **Management Tuca** | Ejecución operativa diaria | Recursos, claridad de mandato, estabilidad | Micro-management, scope creep, cambio de dirección | Respeto a su expertise, directrices claras, no paternalismos |
| **TERAS (tú)** | Operating manager, puente sponsor↔management | Demostrar execution, mantener autoridad, alinear economics | Cuestionamiento de mandato, KPIs movidos, scope creep sin economics | Factual, proactivo, escalar antes de que escalen por ti |
| **Advisors / Consultores** | Apoyo puntual (legal, fiscal, técnico) | Scope claro, que se implementen sus recomendaciones | Ser ignorados, scope creep propio | Utilizar como refuerzo, no como competencia |

---

## 3. Objetivos TERAS en Cada Steerco

### Lo que TERAS debe demostrar (siempre)

1. **Execution ownership**: "Estamos ejecutando el plan con disciplina"
2. **KPI tracking**: "Los números dicen esto, y actuamos en consecuencia"
3. **Risk management proactivo**: "Hemos identificado estos riesgos antes de que escalen"
4. **Governance funcionando**: "Comités operan, RACI se respeta, reporting es fiable"
5. **Alineación económica**: "Los economics reflejan el valor que estamos generando"

### Lo que TERAS debe evitar (siempre)

- ❌ Defensividad ante preguntas del sponsor ("es que no nos dejaron...")
- ❌ Prometer sin plan ("lo arreglamos la próxima semana")
- ❌ Minimizar riesgos para evitar confrontación
- ❌ Aceptar scope creep sin renegociar autoridad/economics
- ❌ Culpar a management delante del sponsor

---

## 4. Tono y Comunicación

### Reglas de Tono en Steerco Tuca

| Situación | Tono | Ejemplo |
|-----------|------|---------|
| **Reportando progreso** | Factual, medido, con KPIs | "El churn se redujo de X% a Y% en el período, en línea con el plan" |
| **Escalando un problema** | Proactivo, con alternativas | "Identificamos riesgo en [área]. Opciones: A (recomendada), B, C. Decidir antes de [fecha]" |
| **Defendiendo posición** | Firme, basado en datos, sin emociones | "El plan se ejecuta según governance acordada. Cambios en scope requieren revisión de mandato" |
| **Recibiendo challenge** | Receptivo pero no sumiso | "Buen punto. Los datos muestran [evidencia]. Propongo [acción]" |

### Lenguaje Prohibido en Steerco

- "Creemos que..." → "Los datos muestran que..."
- "Esperamos..." → "El plan contempla..."
- "Es culpa de..." → "El root cause es... y la acción correctiva es..."
- "No sabíamos..." → "Al identificarlo, activamos..."

---

## 5. Kit de Preparación Steerco

Cuando el usuario pida preparar un Steerco de Tuca, generar automáticamente:

### 5.1 Agenda Estándar

```
STEERING COMMITTEE — TUCA
Fecha: [fecha]  |  Duración: 60-90 min  |  Clasificación: Sponsor-Confidential

1. Aprobación acta anterior y status follow-ups        (5 min)
2. KPI Dashboard: review de métricas clave             (15 min)
3. Ejecución del plan: hitos cumplidos / pendientes     (15 min)
4. Risk register: nuevos riesgos / actualización       (10 min)
5. Decisiones pendientes / escalado                     (10 min)
6. Governance & RACI: ajustes si aplica                 (5 min)
7. Next steps y asignación de acciones                  (5 min)
```

### 5.2 Status Report Template

```
KPI DASHBOARD — TUCA
Periodo: [mes/trimestre]

| KPI | Baseline | Target | Actual | Δ vs Target | Tendencia | Owner | Acción |
|-----|----------|--------|--------|-------------|-----------|-------|--------|
| [KPI 1] | | | | | ↑↓→ | | |
| [KPI 2] | | | | | ↑↓→ | | |
...

HITOS DEL PERIODO:
  ✅ Completados: [lista]
  🔄 En progreso: [lista con % y fecha estimada]
  ❌ Retrasados: [lista con causa y plan de recuperación]

RIESGOS ESCALADOS:
| # | Riesgo | Probabilidad | Impacto | Mitigante | Owner | Status |
|---|--------|-------------|---------|-----------|-------|--------|
```

### 5.3 Talking Points

Generar 5 mensajes clave adaptados a la situación del momento:

```
TALKING POINTS STEERCO TUCA — [fecha]

1. MENSAJE APERTURA (30 seg):
   "[Resumen estado general en 1 frase + principal logro + principal riesgo]"

2. EJECUCIÓN:
   "El plan de 100 días está al [X%] de cumplimiento. Highlight: [logro concreto]"

3. KPIs:
   "[KPI más relevante] ha evolucionado de [base] a [actual], [en línea / por encima / por debajo] del target"

4. RIESGOS:
   "El principal riesgo abierto es [riesgo]. Acción propuesta: [mitigante]. Necesitamos decisión sobre [qué] antes de [cuándo]"

5. CIERRE:
   "Próximos hitos: [2-3 hitos con fecha]. Pedimos al sponsor: [acción concreta]"
```

### 5.4 Pre-Read Materials

Lista de documentos que el sponsor debería recibir 48h antes:
- KPI Dashboard actualizado
- Acta del Steerco anterior con status de follow-ups
- Risk register actualizado
- Cualquier documento que requiera decisión

### 5.5 Preguntas Anticipadas

Generar las 10 preguntas más probables del sponsor, con respuesta preparada:

```
Q1: "¿Por qué [KPI] está por debajo de target?"
R1: "[Causa raíz]. Acción: [mitigante]. Estimamos recuperar en [plazo]."

Q2: "¿Cuándo se materializa el ramp-up comercial?"
R2: "[Timeline con hitos]. Principales dependencias: [lista]."

Q3: "¿Necesitáis más recursos?"
R3: "[Sí/No]. [Si sí: qué, cuánto, para qué, impacto en KPIs]."
...
```

---

## 6. Protocolo de Gestión de Crisis en Steerco

```
SI se presenta un KPI significativamente por debajo de target:
  1. Reconocer el dato factualmente (no minimizar)
  2. Presentar root cause analysis (no excusas)
  3. Presentar plan de recuperación con timeline
  4. Pedir recursos/decisiones específicas si necesarias
  5. Comprometerse con fecha de próximo update

SI el sponsor cuestiona el mandato de TERAS:
  1. No reaccionar emocionalmente
  2. Recordar governance acordada (RACI, reserved matters)
  3. Presentar evidencia de valor añadido (KPIs antes/después)
  4. Si el cuestionamiento es legítimo: proponer revisión estructurada
  5. Si es scope creep: "Esto requiere ajuste de mandato y economics"

SI management contradice a TERAS en el Steerco:
  1. No confrontar en la reunión
  2. Tomar nota, mantener posición con datos
  3. Resolver offline con management
  4. Reportar alineación en siguiente Steerco
```

---

## 7. Lint Pre-Steerco

```
STEERCO LINT 1 — ¿Agenda enviada con 48h de antelación?
STEERCO LINT 2 — ¿KPI Dashboard actualizado con datos recientes?
STEERCO LINT 3 — ¿Talking points preparados y ensayados?
STEERCO LINT 4 — ¿Risk register actualizado con nuevos riesgos?
STEERCO LINT 5 — ¿Preguntas anticipadas preparadas con respuestas?
STEERCO LINT 6 — ¿Follow-ups del Steerco anterior cerrados o con status?
STEERCO LINT 7 — ¿Tono calibrado (factual, proactivo, sin defensividad)?
STEERCO LINT 8 — ¿Confidencialidad verificada en todos los materiales?
```

---

## Recursos

- [Template de Acta Steerco](resources/template-acta-steerco.md)
- [Biblioteca de Respuestas a Preguntas Frecuentes](resources/faq-steerco-tuca.md)
