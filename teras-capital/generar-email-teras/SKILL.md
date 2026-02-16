---
name: generar-email-teras
capa: L3a-tareas
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras]
triggers: >
  Se activa cuando el usuario pida: email, correo, escribir un email,
  redactar correo, responder email, follow-up email, intro email,
  o cualquier referencia a comunicación escrita por email.
description: >
  Generador de emails institucionales TERAS. Calibra tono, densidad y
  estructura según destinatario y objetivo. Desde intros a sponsors
  hasta follow-ups operativos.
---

# Generar Email TERAS — Workflow End-to-End

## 1. Misión

Producir emails que reflejen el estándar institucional TERAS: sobrios, precisos,
orientados a acción, y calibrados para el destinatario.

---

## 2. Intake

```
INTAKE EMAIL:
  1. ¿Para quién? [Nombre, cargo, organización, relación con TERAS]
  2. ¿Objetivo? [Intro / Follow-up / Request / Update / Escalation / Thank you]
  3. ¿Contexto? [Qué ha pasado, qué motiva el email]
  4. ¿Qué queremos? [Call to action específico]
  5. ¿Tono? [Formal / Profesional / Directo]
  6. ¿Sensibilidad? [Lo que NO debe mencionarse]
```

---

## 3. Templates por Tipo

### 3.1 Intro Email a Sponsor

```
Subject: [3 opciones de asunto, max 8 palabras]

[Saludo personalizado],

[1-2 frases de contexto: quién somos, por qué escribimos]

[3 bullets máximo:
  • Qué hacemos (operating manager + coinversor)
  • Por qué relevante para ellos (execution gap / sector fit)
  • Qué proponemos (conversación de 30 min)]

[CTA claro: "¿Tiene sentido una conversación de 30 minutos
la semana del [fecha]?"]

[Cierre profesional]
[Firma]

Longitud total: 8-12 líneas. No más.
```

### 3.2 Follow-Up Operativo

```
Subject: [Tema] — Follow-up [fecha reunión]

[Saludo],

[1 frase de referencia a la reunión/conversación anterior]

Según acordamos:
  1. [Acción 1] — Owner: [nombre] — Deadline: [fecha]
  2. [Acción 2] — Owner: [nombre] — Deadline: [fecha]
  3. [Acción 3] — Owner: [nombre] — Deadline: [fecha]

[Si hay decisiones pendientes: "Queda pendiente confirmar [qué] antes de [cuándo]"]

[Próximo touchpoint: "[tipo] el [fecha]"]

[Cierre]
```

### 3.3 Escalation Email

```
Subject: [Tema] — Requiere atención / decisión

[Saludo],

[1-2 frases de contexto]

Situación:
  [2-3 líneas factuales describiendo el issue]

Impacto:
  [Qué pasa si no se actúa]

Opciones:
  A) [Opción + implicación]
  B) [Opción + implicación]

Recomendación: [Opción X] por [razón en 1 línea]

Necesitamos decisión antes de [fecha].

[Cierre]
```

---

## 4. Reglas del Email TERAS

| Regla | Descripción |
|-------|-------------|
| **Brevedad** | Max 12-15 líneas. Si necesita más, adjuntar memo |
| **1 CTA** | Un solo call to action, claro, con fecha |
| **Subject informativo** | Que diga qué y qué se pide, no solo el tema |
| **No hype** | Cero adjetivación vacía |
| **Datos si hay** | Cifra concreta > "hemos progresado" |
| **Firma TERAS** | Profesional, sin quotes ni disclaimers excesivos |
| **BCC con criterio** | No copiar a quien no necesita verlo |

---

## 5. Calibración por Destinatario

| Destinatario | Tono | Densidad | Longitud |
|-------------|------|----------|----------|
| Sponsor IC member | Ultra-formal | Alta (cifras, hechos) | 8-10 líneas |
| Sponsor deal team | Profesional-directo | Media-alta | 10-12 líneas |
| Management activo | Colaborativo-directo | Media | 8-12 líneas |
| Potencial sponsor (cold) | Institucional-respetuoso | Baja (hook + CTA) | 8-10 líneas |
| Advisor/Counsel | Técnico-preciso | Alta | 10-15 líneas |
| Interno TERAS | Directo | Variable | Variable |

---

## 6. Lint Email

```
EMAIL LINT 1 — ¿Subject informativo (no genérico)?
EMAIL LINT 2 — ¿CTA claro con fecha?
EMAIL LINT 3 — ¿Max 12-15 líneas?
EMAIL LINT 4 — ¿Tono calibrado para destinatario?
EMAIL LINT 5 — ¿No hay hype ni promesas?
EMAIL LINT 6 — ¿Confidencialidad protegida?
EMAIL LINT 7 — ¿TERAS posicionado correctamente?
EMAIL LINT 8 — ¿3 opciones de subject generadas?
```

---

## Recursos

- [Biblioteca de Subject Lines](resources/subject-lines.md)
- [Templates de Firma TERAS](resources/firma-teras.md)
