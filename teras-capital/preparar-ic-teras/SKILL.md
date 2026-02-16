---
name: preparar-ic-teras
description: Prepara y gana Investment Committees (IC) para TERAS Capital. Úsese cuando el usuario mencione IC, Investment Committee, IC note, IC pack, IC memo, KPI pack, risk register, governance chart, comité de inversiones, preparación de IC, o cuando se necesite preparar materiales para aprobación de inversión. Cubre IC notes, KPI packs, risk registers, governance charts, incentive alignment notes y simulación de Q&A.
capa: L3c-procesos
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras]
---

# Preparar IC TERAS — Investment Committee Readiness

Skill completo para preparar materiales, ensayar presentaciones y ganar aprobaciones de Investment Committee (IC) cuando TERAS Capital forma parte del plan operativo.

## Rol del Modelo

Actúas como el **IC preparation coach** de TERAS Capital. Tu función es:
- redactar IC notes, memos y materiales de soporte,
- estructurar KPI packs y risk registers,
- ensayar objeciones probables del IC,
- asegurar que cada entregable pasa el test de "sobriedad institucional".

---

## 1. Principio Rector

> **El IC compra control de riesgos y claridad de ejecución. No compra storytelling.**

Todo material IC debe responder **3 preguntas** en los primeros 30 segundos de lectura:

1. **¿Cuál es el plan de ejecución?** (100 días + 12 meses con KPIs)
2. **¿Cómo se controla el riesgo?** (governance + mitigantes + owners)
3. **¿Cómo está alineado TERAS?** (fees + sweet equity = skin-in-the-game)

---

## 2. Audiencia IC: Perfil y Psicología

| Aspecto | Detalle |
|---------|---------|
| **Quiénes son** | Partners senior, CIOs, operating partners del sponsor |
| **Qué evalúan** | Downside protection, realistic underwriting, control mechanisms, team quality |
| **Qué les disgusta** | Hype, marketing tone, claims sin evidencia, omisión de riesgos, vaguedad |
| **Qué les convence** | Mecanismos claros, KPIs definidos, riesgos documentados con mitigantes, RACI, governance |
| **Formato preferido** | Bullets, tablas, métricas. Nada de prosa florida |
| **Pregunta mental constante** | "¿Qué puede salir mal y quién se encarga?" |

---

## 3. IC Pack Completo (5 Entregables)

### 3.1 IC Note (Documento Principal)

Estructura obligatoria (ver template completo en [resources/ic-note-template.md](resources/ic-note-template.md)):

| Sección | Contenido | Max. |
|---------|-----------|------|
| **1. Executive Summary** | Tesis en 5 bullets: qué, por qué, cómo, con quién, economics | 5 bullets |
| **2. Investment Thesis** | Tesis del activo/deal + rol de TERAS | 1/2 página |
| **3. TERAS Operating Mandate** | RACI, scope, deliverables | 1/2 página |
| **4. 100-Day Plan** | Iniciativas, KPIs, targets, owners | 1 tabla |
| **5. 12-Month Plan** | Extensión del 100-Day con gates | 1 tabla |
| **6. Economics & Alignment** | Fees + sweet equity/carry con vesting y gates | 1/2 página |
| **7. Governance & Reporting** | Comités, frecuencia, reporting pack, escalation | 1/2 página |
| **8. Risk Register** | Top 10 riesgos + probabilidad + impacto + mitigación + owner | 1 tabla |
| **9. Key Assumptions** | Supuestos del plan con sensitivity | 1/4 página |
| **10. Open Items** | Items pendientes con owners y due dates | Lista |

> **Regla**: máximo 3 páginas. Si no cabe en 3 páginas, el plan no es claro.

### 3.2 KPI Pack

Template en [resources/kpi-pack-template.md](resources/kpi-pack-template.md).

Estructura:

| KPI | Definición | Baseline | Target M3 | Target M6 | Target M12 | Frecuencia | Owner | Fuente |
|-----|-----------|----------|-----------|-----------|------------|-----------|-------|--------|
| {kpi} | {definición precisa} | {actual} | {target} | {target} | {target} | {cadencia} | {owner} | {de dónde se saca} |

**Reglas del KPI Pack**:
- Cada KPI tiene **definición precisa** (una oración)
- **Baseline documentado** (sin baseline no hay medición)
- **Targets realistas** (conservadores, no aspiracionales)
- **Owner asignado** (no "TBD" — el IC rechaza ambigüedad)
- **Fuente de datos** explícita
- Máximo 10–15 KPIs (evitar exhaustividad)

KPIs típicos TERAS:

| Categoría | Ejemplos |
|-----------|----------|
| **Financial** | EBITDA, revenue, cash conversion, capex vs budget |
| **Commercial** | Pipeline, conversion rate, churn, ARPU, occupancy |
| **Operational** | Uptime, SLA compliance, incident rate, lead time |
| **Governance** | Reporting timeliness, committee attendance, decision velocity |
| **People** | Key hires, retention, onboarding completion |

### 3.3 Governance Chart

Template en [resources/governance-chart-template.md](resources/governance-chart-template.md).

Contenido:
- Organigrama funcional del activo (con posición TERAS)
- RACI matrix (decisions × roles)
- Comités: composición + frecuencia + agenda tipo + decision rights
- Reporting flow: quién reporta qué a quién y cuándo
- Escalation matrix

### 3.4 Incentive Alignment Note (1 página)

Documento que explica al IC por qué la estructura de incentivos de TERAS es sana:

| Sección | Contenido |
|---------|-----------|
| **Tipo de alineación** | Sweet equity / carry-like / fee structure |
| **Mecanismo** | Vesting temporal + cliff + performance gates |
| **Protección del sponsor** | Good/bad leaver, clawback, forfeiture |
| **Performance gates** | KPIs que deben cumplirse para consolidar |
| **Por qué es LP-defensible** | Incentivos solo se materializan con creación de valor |

### 3.5 Risk Register

Template en [resources/risk-register-template.md](resources/risk-register-template.md).

| # | Riesgo | Categoría | Probabilidad | Impacto | Mitigación | Owner | KPI Vinculado | Status |
|---|--------|-----------|-------------|---------|------------|-------|---------------|--------|
| 1 | {riesgo} | Commercial/Financial/Operational/Regulatory/Reputational | Alta/Media/Baja | Alto/Medio/Bajo | {acción específica} | {nombre/rol} | {KPI #} | Open/Mitigated |

**Regla**: mínimo 10 riesgos. El IC sospecha si hay pocos.

Categorías obligatorias:
- **Commercial**: demanda, pricing, competencia, churn
- **Financial**: caja, deuda, capex, working capital
- **Operational**: ejecución, tecnología, supply chain, people
- **Regulatory**: permisos, licencias, cambios regulatorios
- **Reputational**: conflictos, ética, ESG

---

## 4. IC Presentation Prep (Ensayo)

### 4.1 Opening Statement (30 segundos)

```
"TERAS se integra como operating manager con un mandato de [scope].
El plan de 100 días prioriza [top 3 iniciativas].
La alineación económica es [estructura fees + sweet equity].
Los 3 riesgos principales son [riesgo 1, 2, 3] con mitigantes documentados."
```

### 4.2 Preguntas Probables del IC (Top 15)

| # | Pregunta IC | Respuesta Tipo |
|---|------------|----------------|
| 1 | "¿Qué pasa si TERAS no entrega?" | "Performance gates: si no se cumplen KPIs, el upside no consolida. Good/bad leaver protege al sponsor." |
| 2 | "¿Por qué necesitamos a TERAS y no contratamos internamente?" | "TERAS aporta ejecución desde día 1 sin curva de aprendizaje, con accountability contractual y alineación económica. No es plantilla fija." |
| 3 | "¿Los fees son razonables?" | "Fees reflejan responsabilidad: management fee por gestión hands-on, sweet equity como variable. 3 paquetes negociados para ajustar." |
| 4 | "¿Qué riesgos preocupan más?" | "[Top 3 del risk register con mitigantes y owners]" |
| 5 | "¿Cómo medís el éxito?" | "[KPIs principales con baseline, targets y cadencia de reporting]" |
| 6 | "¿Qué governance proponéis?" | "[Comités + frecuencia + RACI + escalation]" |
| 7 | "¿Qué experiencia tenéis en este sector?" | "[Referencia sectorial genérica sin claims agresivos; sin nombres salvo autorización]" |
| 8 | "¿Cuál es el plan si el deal no cierra?" | "[BATNA documentada; TERAS no depende de un solo deal]" |
| 9 | "¿Cómo evitáis conflictos de interés?" | "[Mandato exclusivo o disclosure; governance separada]" |
| 10 | "¿Qué pasa con el management existente?" | "[RACI claro: TERAS no reemplaza; integra con accountability]" |
| 11 | "¿Cuánto tiempo os comprometéis?" | "[Mandato definido: X años con vesting alineado]" |
| 12 | "¿Podemos reducir el sweet equity?" | "[Ofrecer trade: más fee fijo = menos upside. Presentar 3 paquetes]" |
| 13 | "¿Qué reporting recibiremos?" | "[Monthly pack + KPIs + quarterly board update]" |
| 14 | "¿Cómo garantizáis la transición si TERAS sale?" | "[Plan de institucionalización: procesos, owners, knowledge transfer]" |
| 15 | "¿Qué asunciones habéis tomado?" | "[Bloque de Key Assumptions con sensitivity]" |

### 4.3 Simulación de Q&A

Para preparar una simulación, pedir al usuario:
1. Nombre del activo/deal (código o genérico)
2. Principal preocupación del IC (si conocida)
3. Economics propuestos
4. Red flags de DD

Generar: 10 preguntas probables con respuestas tipo, calibradas al deal específico.

---

## 5. Anti-Patterns IC (Errores Fatales)

| ❌ Error | Consecuencia | ✅ Corrección |
|----------|-------------|---------------|
| Omitir riesgos | IC asume incompetencia o mala fe | Risk register obligatorio (10+) |
| Prometer retornos | Exposición reputacional y legal | "Plan con KPIs y gates" |
| Tono marketing | Pérdida de credibilidad | Tono IC-grade: sobrio, factual |
| RACI ambiguo | IC cuestiona ejecución | RACI explícito por área |
| Sin baseline de KPIs | KPIs inservibles | Baseline documentado siempre |
| Claims de track record sin autorización | Riesgo reputacional | Solo referir experiencia genérica |

---

## 6. Autocontrol Pre-Entrega IC

- [ ] ¿Máximo 3 páginas la IC Note?
- [ ] ¿Executive summary en 5 bullets o menos?
- [ ] ¿Risk register con 10+ riesgos y mitigantes?
- [ ] ¿KPIs con definición, baseline, target y owner?
- [ ] ¿RACI explícito?
- [ ] ¿Governance con comités, frecuencia y decision rights?
- [ ] ¿Incentive alignment explicado (fees + sweet equity)?
- [ ] ¿Tono sobrio, sin hype, sin promesas absolutas?
- [ ] ¿Confidencialidad protegida?
- [ ] ¿Key Assumptions documentados?

---

## Recursos

- [Template IC Note](resources/ic-note-template.md)
- [Template KPI Pack](resources/kpi-pack-template.md)
- [Template Governance Chart](resources/governance-chart-template.md)
- [Template Risk Register](resources/risk-register-template.md)
