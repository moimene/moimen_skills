# Template Governance Chart — TERAS Capital

Estructura de governance para IC pack. Incluye organigrama funcional, RACI, comités, reporting y escalation.

---

## 1. Organigrama Funcional

```
┌─────────────────────────────────────────┐
│              SPONSOR (IC)               │
│         Oversight + Capital             │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│          BOARD / SUBCOMMITTEE           │
│   Sponsor rep + TERAS + Independent     │
│   Frecuencia: {mensual}                │
└──────────────────┬──────────────────────┘
                   │
         ┌─────────┴─────────┐
         │                   │
┌────────▼────────┐ ┌────────▼────────┐
│  TERAS CAPITAL  │ │   MANAGEMENT    │
│ Operating Mgr   │ │   Day-to-day    │
│ Mandate: {scope}│ │   Operations    │
└────────┬────────┘ └────────┬────────┘
         │                   │
         └─────────┬─────────┘
                   │
┌──────────────────▼──────────────────────┐
│         OPERATING COMMITTEE             │
│   TERAS + Management + {invitados}      │
│   Frecuencia: {semanal}                │
└─────────────────────────────────────────┘
```

---

## 2. RACI Matrix

| Decisión / Área | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
|-----------------|-----------------|------------------|----------------|---------------|
| Estrategia comercial | TERAS | Sponsor | Management | IC |
| Ejecución comercial (pipeline, pricing) | TERAS | TERAS | Management | Sponsor |
| Control financiero (P&L, cash) | TERAS + CFO | TERAS | Sponsor | IC |
| Capex execution | TERAS + Mgmt | Sponsor | | IC |
| Hiring (C-suite) | Management | TERAS | Sponsor | IC |
| Hiring (below C-suite) | Management | Management | TERAS | |
| Reporting & KPIs | TERAS | TERAS | CFO | Sponsor + IC |
| Governance & compliance | TERAS | Sponsor | Legal | IC |
| Budget approval | Board | Sponsor | TERAS + Mgmt | IC |
| Material contracts (>€{threshold}) | Management | TERAS | Sponsor | IC |
| {área adicional} | {R} | {A} | {C} | {I} |

**Leyenda RACI**:
- **R** = Hace el trabajo
- **A** = Aprueba / rinde cuentas (solo 1 por fila)
- **C** = Se le consulta antes de decidir
- **I** = Se le informa después de decidir

---

## 3. Comités

### 3.1 Operating Committee

| Aspecto | Detalle |
|---------|---------|
| **Composición** | TERAS lead + Management team + {invitados ad hoc} |
| **Frecuencia** | Semanal |
| **Duración** | 60 min |
| **Agenda tipo** | 1. KPIs review (15') 2. Pipeline update (15') 3. Cash / financial update (10') 4. Issues & escalation (10') 5. Actions & next steps (10') |
| **Decision rights** | Decisiones operativas dentro del mandato y budget aprobado |
| **Output** | Action log actualizado + KPI dashboard |
| **Secretaría** | TERAS |

### 3.2 Board Subcommittee (o Board Meeting)

| Aspecto | Detalle |
|---------|---------|
| **Composición** | Sponsor rep (chair) + TERAS + Independent(s) + Management CEO/CFO |
| **Frecuencia** | Mensual |
| **Duración** | 90–120 min |
| **Agenda tipo** | 1. Financials review: P&L, BS, CF (20') 2. KPI pack & traffic lights (15') 3. Strategy & commercial update (20') 4. Capex & budget variance (10') 5. Risk register update (10') 6. People & organization (10') 7. AOB & actions (15') |
| **Decision rights** | Aprobación presupuestos operativos, contrataciones C-suite, contratos materiales |
| **Output** | Board minutes + reporting pack archivado |
| **Secretaría** | TERAS o rotativo |

### 3.3 IC Update (Quarterly)

| Aspecto | Detalle |
|---------|---------|
| **Composición** | Sponsor → IC (TERAS prepara materiales) |
| **Frecuencia** | Trimestral |
| **Formato** | IC update memo (2 páginas max) + KPI summary + risk update |
| **Contenido** | Performance vs plan, KPI trends, risk changes, key decisions, outlook |
| **Preparación** | TERAS redacta draft → Sponsor revisa y presenta |

---

## 4. Reporting Flow

```
MANAGEMENT (datos operativos)
     │
     ▼
TERAS (consolida + analiza + KPI pack)
     │
     ├──► OPERATING COMMITTEE (semanal — dashboard + voice)
     │
     ├──► BOARD SUBCOMMITTEE (mensual — full pack)
     │
     └──► SPONSOR → IC (trimestral — summary memo)
```

### Reporting Pack — Contenido

| Componente | Cadencia | Responsable |
|------------|----------|-------------|
| P&L (actual vs budget vs prior year) | Monthly | CFO + TERAS |
| Balance sheet | Monthly | CFO |
| Cash flow statement | Monthly | CFO + TERAS |
| KPI dashboard (traffic lights) | Weekly (summary) / Monthly (full) | TERAS |
| Pipeline report | Weekly | TERAS / Commercial |
| Capex tracker (actual vs budget) | Monthly | CFO + TERAS |
| Risk register update | Monthly | TERAS |
| Hiring tracker | Monthly | HR + TERAS |

### Reporting Timeline

| Día del mes | Deliverable |
|-------------|-------------|
| D+5 | Flash financiero (preliminary P&L + cash position) |
| D+10 | Monthly reporting pack completo |
| D+12 | Operating committee review |
| D+15 | Board / subcommittee meeting |

---

## 5. Escalation Matrix

| Nivel | Trigger | Quién Escala | A Quién | Timeline |
|-------|---------|-------------|---------|----------|
| **L1 — Operativo** | KPI ≤{threshold} o issue operativo | TERAS / Mgmt | Operating Committee | Próximo comité semanal |
| **L2 — Táctico** | KPI off-track 2 meses consecutivos | TERAS | Board Subcommittee | Convocatoria ad hoc (48h) |
| **L3 — Estratégico** | Riesgo material o budget overrun >{%} | TERAS + Sponsor rep | Board + IC awareness | Inmediato (24h) |
| **L4 — Crisis** | Evento reputacional, regulatorio o financiero grave | Sponsor rep | IC + Legal | Inmediato |

---

## 6. Decision Rights Summary

| Tipo de Decisión | Quién Decide | Quién Aprueba | Threshold |
|------------------|-------------|---------------|-----------|
| Gasto operativo | Management | TERAS | <€{threshold} |
| Gasto operativo > threshold | TERAS | Board | >€{threshold} |
| Contratación below C-suite | Management | Management | n/a |
| Contratación C-suite | Management | TERAS + Sponsor | n/a |
| Contrato comercial material | TERAS | Board | >€{threshold} |
| Cambio de estrategia | Board | Sponsor | n/a |
| Capex > budget | TERAS + CFO | Board | >{%} variance |
