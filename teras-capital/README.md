# TERAS Capital — Capa Cognitiva IA

Suite completa de skills de IA para operar, analizar, negociar y ejecutar como TERAS Capital. Organizada en 4 capas jerárquicas que garantizan que **todo output IA del equipo TERAS** cumpla estándar institucional desde el primer prompt.

**Versión**: 2.0  |  **Skills**: 18  |  **Archivos**: ~60  |  **Clasificación**: TERAS-Internal

---

## Arquitectura: 4 Capas

```
L0 FUNDACIÓN ──────────────────────────── Siempre activa
  operar-como-teras | aplicar-guardrails | desarrollar-ux

L1 COMPORTAMIENTO ─────────────────────── Rigor analítico
  challenge-cognitivo | validar-analisis

L2 ROLES ──────────────────────────────── Alter egos funcionales
  clo-superpoder | coo-superpoder | cfo-superpoder | cio-superpoder | head-ir-superpoder

L3a TAREAS ────────────────────────────── Generadores de entregables
  generar-presentacion | generar-one-pager | generar-board-memo | generar-email | generar-exec-summary

L3b ESCENARIOS ────────────────────────── Contextos situacionales
  escenario-steerco-tuca | escenario-consejo-mps | escenario-templus | preparar-reunion-clave

L3c PROCESOS ──────────────────────────── Workflows de negocio
  negociar-mandatos | negociar-ma | preparar-ic
```

---

## Índice de Skills

### L0: Fundación (siempre activa)

| Skill | Propósito |
|-------|-----------|
| [operar-como-teras](operar-como-teras/SKILL.md) | Identidad, modelo económico, tono, modos de output. **Base de todo.** |
| [aplicar-guardrails-teras](aplicar-guardrails-teras/SKILL.md) | Anti-patrones, vocabulario, lint de marca y reputación |
| [desarrollar-ux-teras](desarrollar-ux-teras/SKILL.md) | Brand system: colores, tipografía, componentes, tono visual |

### L1: Comportamiento Cognitivo

| Skill | Propósito |
|-------|-----------|
| [challenge-cognitivo-teras](challenge-cognitivo-teras/SKILL.md) | Challenge socrático, red team, escala de confianza, anti-complacencia |
| [validar-analisis-teras](validar-analisis-teras/SKILL.md) | QA numérico, coherencia narrativa, benchmarking, sensibilidad |

### L2: Roles (Super-Poderes)

| Skill | Propósito |
|-------|-----------|
| [clo-superpoder-teras](clo-superpoder-teras/SKILL.md) | CLO: 8 sub-agentes legales, M&A, governance, compliance |
| [coo-superpoder-teras](coo-superpoder-teras/SKILL.md) | COO: planes 100 días, KPIs, reporting, governance operativa |
| [cfo-superpoder-teras](cfo-superpoder-teras/SKILL.md) | CFO: modelos financieros, cash discipline, covenants, budget |
| [cio-superpoder-teras](cio-superpoder-teras/SKILL.md) | CIO: tesis de inversión, portfolio, VCP, exit readiness |
| [head-ir-superpoder-teras](head-ir-superpoder-teras/SKILL.md) | Head IR: LP reporting, fundraising, sponsor comms, data room |

### L3a: Generadores de Entregables

| Skill | Output |
|-------|--------|
| [generar-presentacion-teras](generar-presentacion-teras/SKILL.md) | Presentaciones PPTX con brand TERAS |
| [generar-one-pager-teras](generar-one-pager-teras/SKILL.md) | One-pagers ejecutivos (1 página) |
| [generar-board-memo-teras](generar-board-memo-teras/SKILL.md) | Memos para Consejo/IC/Board |
| [generar-email-teras](generar-email-teras/SKILL.md) | Emails institucionales calibrados |
| [generar-exec-summary-teras](generar-exec-summary-teras/SKILL.md) | Executive summaries (1-2 páginas) |

### L3b: Escenarios de Negocio

| Skill | Contexto |
|-------|----------|
| [escenario-steerco-tuca](escenario-steerco-tuca/SKILL.md) | Steering Committee del activo Tuca |
| [escenario-consejo-mps](escenario-consejo-mps/SKILL.md) | Consejo de Administración de MPS |
| [escenario-templus](escenario-templus/SKILL.md) | Activo/proyecto Templus |
| [preparar-reunion-clave](preparar-reunion-clave/SKILL.md) | Preparación genérica de reuniones con personas clave |

### L3c: Procesos de Negocio

| Skill | Workflow |
|-------|---------|
| [negociar-mandatos-teras](negociar-mandatos-teras/SKILL.md) | Pipeline comercial, stakeholders, paquetes económicos |
| [negociar-ma-teras](negociar-ma-teras/SKILL.md) | M&A: SPA/SHA, BATNA/ZOPA, cláusulas |
| [preparar-ic-teras](preparar-ic-teras/SKILL.md) | IC notes, KPI packs, risk registers, Q&A simulation |

---

## Matriz de Decisión Rápida

| Si necesitas... | Usa | + Complementa con |
|-----------------|-----|-------------------|
| Preparar Steerco de un activo | escenario-steerco-[activo] | generar-presentacion + COO |
| One-pager para un sponsor | generar-one-pager | negociar-mandatos |
| Consejo de Administración | escenario-consejo-mps | generar-board-memo + CLO |
| Negociar SPA/SHA | negociar-ma | CLO superpoder |
| Preparar IC | preparar-ic | CIO + challenge |
| Revisar modelo financiero | cfo-superpoder | validar-analisis |
| Reunión con persona clave | preparar-reunion-clave | escenario del activo |
| Tesis de inversión | cio-superpoder | challenge + validar-analisis |
| Reporting a LPs | head-ir-superpoder | CFO |
| Plan de 100 días | coo-superpoder | escenario del activo |
| Email a sponsor | generar-email | negociar-mandatos |

---

## Configuración por Plataforma

| Plataforma | Setup | Uso recomendado |
|-----------|-------|-----------------|
| **Claude (Cowork/Code/Antigravity)** | Skills en workspace/.skills/ | Trabajo principal: análisis, documentos, tareas complejas |
| **Gemini Gems** | Pegar .md en instrucciones del Gem | Consultas rápidas, brainstorming |
| **NotebookLM** | Subir .md como fuentes | Research, síntesis, podcasts, preparación |
| **Codex (OpenAI)** | .md en repo + AGENTS.md | Coding, automatización |
| **n8n / Agentes** | System prompt del nodo AI | Workflows automáticos |

---

## Documentación

- [Política de Uso IA TERAS](POLITICA-USO-IA-TERAS.md) — Reglas obligatorias para todo el equipo
- [Plan Maestro Capa Cognitiva](plan-maestro-capa-cognitiva-teras.docx) — Documento completo del plan

---

## Estructura de Archivos

```
teras-capital/
├── README.md                          ← Este archivo
├── POLITICA-USO-IA-TERAS.md          ← Política de uso para el equipo
├── plan-maestro-capa-cognitiva-teras.docx ← Plan maestro (DOCX)
│
├── operar-como-teras/                 ← L0: Fundación
├── aplicar-guardrails-teras/          ← L0: Guardrails
├── desarrollar-ux-teras/              ← L0: Brand/UX
│
├── challenge-cognitivo-teras/         ← L1: Challenge socrático
├── validar-analisis-teras/            ← L1: QA analítico
│
├── clo-superpoder-teras/              ← L2: CLO (8 sub-agentes)
├── coo-superpoder-teras/              ← L2: COO (ejecución)
├── cfo-superpoder-teras/              ← L2: CFO (finanzas)
├── cio-superpoder-teras/              ← L2: CIO (inversión)
├── head-ir-superpoder-teras/          ← L2: Head IR (inversores)
│
├── generar-presentacion-teras/        ← L3a: Generador presentaciones
├── generar-one-pager-teras/           ← L3a: Generador one-pagers
├── generar-board-memo-teras/          ← L3a: Generador board memos
├── generar-email-teras/               ← L3a: Generador emails
├── generar-exec-summary-teras/        ← L3a: Generador exec summaries
│
├── escenario-steerco-tuca/            ← L3b: Escenario Steerco Tuca
├── escenario-consejo-mps/             ← L3b: Escenario Consejo MPS
├── escenario-templus/                 ← L3b: Escenario Templus
├── preparar-reunion-clave/            ← L3b: Preparar reunión genérica
│
├── negociar-mandatos-teras/           ← L3c: Pipeline comercial
├── negociar-ma-teras/                 ← L3c: M&A transaccional
├── preparar-ic-teras/                 ← L3c: Preparación IC
│
└── _metaprompts-source/               ← Metaprompts originales (referencia)
```
