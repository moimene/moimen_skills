# TERAS Capital — Skills Suite

Suite de skills de IA para operar, negociar y ejecutar como TERAS Capital. Diseñada para que **todo el equipo TERAS** use la IA con contexto institucional correcto, evitando errores de marca, posicionamiento y tono.

---

## Skills Disponibles

| # | Skill | Cuándo Usarla |
|---|-------|---------------|
| 1 | [operar-como-teras](operar-como-teras/SKILL.md) | **Siempre activa.** Define identidad, modelo económico, tono, modos de output |
| 2 | [aplicar-guardrails-teras](aplicar-guardrails-teras/SKILL.md) | Para revisar cualquier output TERAS: lint de marca, anti-patterns, tono |
| 3 | [negociar-mandatos-teras](negociar-mandatos-teras/SKILL.md) | Pipeline comercial con sponsors VC/infra/PE, stakeholders, paquetes económicos |
| 4 | [negociar-ma-teras](negociar-ma-teras/SKILL.md) | Negociación M&A: SPA/SHA/JV, clause library, BATNA/ZOPA |
| 5 | [preparar-ic-teras](preparar-ic-teras/SKILL.md) | Preparar IC: notes, KPI packs, risk registers, governance charts |
| 6 | [desarrollar-ux-teras](desarrollar-ux-teras/SKILL.md) | Branding y UX según identidad visual TERAS |
| 7 | [clo-superpoder-teras](clo-superpoder-teras/SKILL.md) | **🦸 Super‑poder CLO**: red agéntica de 8 sub-agentes, SPA/SHA/JV completo, lint legal 10‑check, supuestos sectoriales, métricas de efectividad |

---

## Uso en Antigravity (VS Code / Cursor)

Las skills se activan automáticamente cuando Antigravity detecta contexto relevante, o se pueden invocar manualmente.

### Activación Automática

Si el directorio de skills está configurado en tu workspace, Antigravity cargará las skills cuando detecte mención a TERAS, sponsors, mandatos, IC, M&A, etc.

### Activación Manual

Pide directamente al agente que use una skill:
- _"Usa la skill `negociar-mandatos-teras` para preparar un email de intro al sponsor X"_
- _"Aplica `aplicar-guardrails-teras` para revisar este borrador"_
- _"Con `preparar-ic-teras`, genera una IC note para el deal Y"_

### Casos de Uso por Skill

| Necesito… | Skill a usar |
|-----------|-------------|
| Redactar un email a un sponsor | `operar-como-teras` + `negociar-mandatos-teras` |
| Preparar un pitch para reunión comercial | `negociar-mandatos-teras` |
| Revisar que un documento no tenga errores de marca | `aplicar-guardrails-teras` |
| Preparar materiales para IC | `preparar-ic-teras` |
| Negociar términos de un SPA/SHA | `negociar-ma-teras` o `clo-superpoder-teras` |
| Crear una propuesta de mandato con economics | `negociar-mandatos-teras` |
| Diseñar una landing page o presentación visual | `desarrollar-ux-teras` |
| Orquestar un deal M&A completo (DD→SPA→SHA→Closing) | `clo-superpoder-teras` |
| Preparar closing set con checklists y certificados | `clo-superpoder-teras` |
| Due diligence legal por sector (telco, energía, RE…) | `clo-superpoder-teras` |
| Gestionar secretaría corporativa y cap table | `clo-superpoder-teras` |

### Combinaciones Recomendadas

- **Cualquier output TERAS**: `operar-como-teras` (base) + `aplicar-guardrails-teras` (lint)
- **Pipeline completo**: `negociar-mandatos-teras` (comercial) → `preparar-ic-teras` (IC)
- **Deal M&A completo**: `clo-superpoder-teras` (CLO) + `negociar-ma-teras` (transaccional) + `preparar-ic-teras` (IC)
- **CLO full stack**: `clo-superpoder-teras` (orquesta DD→SPA→SHA→closing→post-closing)

---

## Uso en Google NotebookLM

NotebookLM permite subir documentos como "fuentes" y luego interactuar con ellos vía chat, o generar contenido derivado (podcasts, presentaciones, etc.).

### Opción A: Notebook Único con Todas las Skills (Recomendado)

Crear **un solo notebook** llamado **"TERAS Capital — Sistema Operativo"** y subir todos los `SKILL.md` + resources como fuentes:

1. Ir a [notebooklm.google.com](https://notebooklm.google.com)
2. Crear nuevo notebook → Nombre: **"TERAS Capital — Sistema Operativo"**
3. Añadir fuentes → Subir como archivos **todos los `.md`** de esta carpeta:
   - `operar-como-teras/SKILL.md`
   - `operar-como-teras/resources/definitions.md`
   - `operar-como-teras/resources/output-templates.md`
   - `aplicar-guardrails-teras/SKILL.md`
   - `aplicar-guardrails-teras/resources/banned-terms.md`
   - `aplicar-guardrails-teras/resources/correction-examples.md`
   - `negociar-mandatos-teras/SKILL.md`
   - `negociar-mandatos-teras/resources/stakeholder-playbook.md`
   - `negociar-mandatos-teras/resources/economic-packages.md`
   - `negociar-mandatos-teras/resources/pipeline-templates.md`
   - `negociar-ma-teras/SKILL.md`
   - `negociar-ma-teras/resources/clause-library.md`
   - `negociar-ma-teras/resources/negotiation-map-template.md`
   - `negociar-ma-teras/resources/traceability-matrix-template.md`
   - `preparar-ic-teras/SKILL.md`
   - `preparar-ic-teras/resources/ic-note-template.md`
   - `preparar-ic-teras/resources/kpi-pack-template.md`
   - `preparar-ic-teras/resources/governance-chart-template.md`
   - `preparar-ic-teras/resources/risk-register-template.md`
   - `clo-superpoder-teras/SKILL.md`
   - `clo-superpoder-teras/resources/red-agentica-clo.md`
   - `clo-superpoder-teras/resources/spa-sha-playbook.md`
   - `clo-superpoder-teras/resources/supuestos-legales-sector.md`
   - `clo-superpoder-teras/resources/lint-metricas-clo.md`
   - `clo-superpoder-teras/resources/manejo-objeciones-clo.md`
4. NotebookLM indexará todo y lo tendrás listo para interactuar

### Opción B: Notebooks por Temática

Si prefieres notebooks separados:

| Notebook | Fuentes a subir |
|----------|----------------|
| "TERAS — Identidad y Guardrails" | `operar-como-teras/*` + `aplicar-guardrails-teras/*` |
| "TERAS — Negociación Sponsors" | `negociar-mandatos-teras/*` |
| "TERAS — Negociación M&A" | `negociar-ma-teras/*` |
| "TERAS — IC Preparation" | `preparar-ic-teras/*` |
| "TERAS — CLO Super‑Poder" | `clo-superpoder-teras/*` |

### Qué Puedes Hacer en NotebookLM

#### 💬 Chat Contextualizado
Pregunta directamente sobre cualquier tema TERAS y obtendrás respuestas que respetan la identidad, tono y posicionamiento:
- _"¿Cómo debo describir TERAS a un sponsor de infra?"_
- _"Redáctame un email de intro para un deal de energía"_
- _"¿Cuáles son los 3 paquetes económicos y cuándo uso cada uno?"_
- _"Hazme una checklist de preparación de IC"_

#### 🎙️ Audio Overview (Podcast)
NotebookLM puede generar un **podcast conversacional** a partir de las fuentes:
1. Selecciona las fuentes relevantes (e.g., todas las skills o solo `operar-como-teras`)
2. Click en **"Audio Overview"** → **"Generate"**
3. Personaliza con instrucciones:
   - _"Genera un podcast de 15 minutos explicando qué es TERAS Capital, su modelo de negocio y cómo se diferencia de un VC o una consultoría"_
   - _"Crea un episodio sobre cómo preparar un IC exitosamente"_
   - _"Genera una conversación explicando los 3 paquetes económicos de TERAS"_

**Casos de uso del podcast TERAS**:
- Onboarding de nuevos miembros del equipo
- Explicación rápida del modelo TERAS para partners
- Preparación de reuniones con sponsors (escuchar la tesis de camino a la reunión)

#### 📊 Generar Presentaciones e Informes
Usa el chat de NotebookLM para generar contenido estructurado:
- _"Genera una presentación de 10 slides sobre TERAS Capital para un sponsor de infra digital"_
- _"Crea un informe sobre el proceso de negociación de mandatos con los 3 paquetes económicos"_
- _"Genera un one-pager ejecutivo de TERAS para entregar en un evento"_

El output estará en texto/markdown — copia a Google Slides, PowerPoint o Canva para diseño final.

#### 📋 Generar Infografías
Pide al chat contenido esquemático para infografías:
- _"Crea una infografía con el pipeline comercial de TERAS en 5 fases"_
- _"Diseña una infografía comparando los 3 paquetes económicos (Lean / Core / Co-GP)"_
- _"Genera una infografía de la estructura de governance de TERAS con un sponsor"_

Copia la estructura al diseñador o a herramientas como Canva, Figma, o Gamma.

#### 🎬 Video Presentaciones
Combina el contenido generado con herramientas de video:
1. Genera el guión en NotebookLM: _"Crea un guión de 5 minutos para un video explicando el modelo de TERAS Capital"_
2. Usa el audio overview como narración base
3. Sube a herramientas como **Loom**, **Synthesia**, **Gamma** o **Beautiful.ai** para producir el video con slides animadas

---

## Uso en Google Gemini (Gems Personalizadas)

Las Gems de Gemini son chatbots personalizados con instrucciones y conocimiento específico.

### Crear un Gem TERAS

1. Ir a [gemini.google.com](https://gemini.google.com) → **Gems** → **Crear Gem**
2. **Nombre**: "TERAS Capital Co-Pilot"
3. **Instrucciones**: Copiar el contenido íntegro de `operar-como-teras/SKILL.md` como instrucciones base
4. **Añadir conocimiento**: Subir como archivos adjuntos los `SKILL.md` y resources de las demás skills

### Gems Especializadas Sugeridas

| Gem | Instrucciones (SKILL.md) | Archivos de conocimiento |
|-----|--------------------------|-------------------------|
| **TERAS Co-Pilot** (general) | `operar-como-teras/SKILL.md` | Todos los resources de `operar-como-teras` + `aplicar-guardrails-teras` |
| **TERAS Negociador** | `negociar-mandatos-teras/SKILL.md` | Resources de mandatos + `economic-packages.md` |
| **TERAS M&A** | `negociar-ma-teras/SKILL.md` | Resources de M&A + `clause-library.md` |
| **TERAS IC Coach** | `preparar-ic-teras/SKILL.md` | Resources de IC + `risk-register-template.md` |
| **TERAS CLO** | `clo-superpoder-teras/SKILL.md` | Todos los resources de `clo-superpoder-teras` |

### Ejemplo de Instrucciones para el Gem General

```
Eres el copiloto estratégico, comercial y de ejecución de TERAS Capital.

TERAS Capital es un operating manager y coinversor minoritario — NO es un VC, 
fondo, GP, family office, ni consultoría.

Siempre:
- Mantén tono institucional, sobrio, IC-grade
- Usa el modelo económico: fees + sweet equity con vesting y performance gates
- Describe a TERAS como operating manager + coinversor minoritario
- Protege confidencialidad: no inventes datos, nombres ni cifras

Nunca:
- Uses emojis, hype, promesas absolutas
- Digas "disruptivo", "revolucionario", "best-in-class" sin prueba
- Llames a TERAS VC, fondo, GP o family office
- Inventes track record o cifras no proporcionadas por el usuario

Antes de entregar cualquier output, ejecuta los 8 lint checks de marca.
```

---

## Resumen: Cuándo Usar Cada Plataforma

| Necesidad | Plataforma Recomendada |
|-----------|----------------------|
| Desarrollar código, templates, documentos técnicos | **Antigravity** (VS Code) |
| Chat rápido con contexto TERAS para el equipo | **NotebookLM** o **Gemini Gem** |
| Generar podcast para onboarding o preparación | **NotebookLM** (Audio Overview) |
| Crear presentaciones, infografías, one-pagers | **NotebookLM** → exportar a Canva/Slides |
| Generar informes o IC notes | **Antigravity** o **NotebookLM** |
| Video presentaciones con narración | **NotebookLM** (guión + audio) → **Gamma/Synthesia** |
| Chatbot del equipo 24/7 para preguntas TERAS | **Gemini Gem** |
| Due diligence o negociación transaccional | **Antigravity** con `clo-superpoder-teras` |
| Orquestar M&A end-to-end (DD→closing→post-closing) | **Antigravity** con `clo-superpoder-teras` |

---

## Estructura de Archivos

```
teras-capital/
├── README.md                       ← Este archivo
├── operar-como-teras/              ← Skill fundacional (siempre activo)
│   ├── SKILL.md
│   └── resources/
├── aplicar-guardrails-teras/       ← Lint y control de marca
│   ├── SKILL.md
│   └── resources/
├── negociar-mandatos-teras/        ← Actividad comercial con sponsors
│   ├── SKILL.md
│   └── resources/
├── negociar-ma-teras/              ← Negociación transaccional M&A
│   ├── SKILL.md
│   └── resources/
├── preparar-ic-teras/              ← Preparación de IC
│   ├── SKILL.md
│   └── resources/
├── desarrollar-ux-teras/           ← Branding y UX
│   ├── SKILL.md
│   └── resources/
├── clo-superpoder-teras/           ← 🦸 Super‑poder CLO (red agéntica 8 sub-agentes)
│   ├── SKILL.md
│   └── resources/
└── _metaprompts-source/            ← Metaprompts originales (referencia)
```
