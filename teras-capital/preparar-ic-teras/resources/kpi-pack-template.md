# Template KPI Pack — TERAS Capital

Pack de KPIs para reporting IC. Definiciones precisas, baselines documentados, targets realistas.

---

## Instrucciones

1. Máximo 10–15 KPIs (no más — el IC pierde foco)
2. Cada KPI tiene definición de 1 línea
3. Baseline siempre documentado — sin baseline, no hay KPI
4. Targets conservadores (no aspiracionales)
5. Owner asignado — no "TBD"
6. Fuente de datos explícita

---

## KPI Table

| # | KPI | Definición | Categoría | Baseline | Target M3 | Target M6 | Target M12 | Frecuencia | Owner | Fuente |
|---|-----|-----------|-----------|----------|-----------|-----------|------------|-----------|-------|--------|
| 1 | {Revenue} | {Ingresos netos mensuales según P&L} | Financial | {€X} | {€Y} | {€Z} | {€W} | Monthly | {CFO} | {ERP / Contabilidad} |
| 2 | {EBITDA} | {EBITDA ajustado (definir ajustes)} | Financial | {€X} | {€Y} | {€Z} | {€W} | Monthly | {CFO} | {P&L ajustado} |
| 3 | {Cash conversion} | {Cash from operations / EBITDA} | Financial | {%} | {%} | {%} | {%} | Monthly | {TERAS} | {Cash flow statement} |
| 4 | {Pipeline activo} | {# oportunidades en fase ≥ qualification} | Commercial | {#} | {#} | {#} | {#} | Weekly | {TERAS} | {CRM} |
| 5 | {Conversion rate} | {Deals cerrados / oportunidades calificadas} | Commercial | {%} | {%} | {%} | {%} | Monthly | {TERAS} | {CRM} |
| 6 | {Churn} | {Clientes perdidos / total clientes, mensual} | Commercial | {%} | {%} | {%} | {%} | Monthly | {Commercial} | {CRM + billing} |
| 7 | {Capex vs budget} | {Capex ejecutado / capex presupuestado, acumulado} | Financial | {%} | {%} | {%} | {%} | Monthly | {CFO + TERAS} | {Budget tracker} |
| 8 | {Reporting timeliness} | {Días para cerrar monthly reporting pack} | Governance | {# días} | {# días} | {# días} | {# días} | Monthly | {TERAS} | {Calendar} |
| 9 | {Key hires} | {# posiciones clave cubiertas vs plan} | People | {#/total} | {#/total} | {#/total} | {#/total} | Monthly | {HR + TERAS} | {Hiring tracker} |
| 10 | {SLA compliance} | {% servicios que cumplen SLA definido} | Operational | {%} | {%} | {%} | {%} | Weekly | {Ops} | {Monitoring system} |

---

## KPI Definitions Dictionary

### Financial
- **Revenue**: Ingresos netos mensuales reconocidos según norma contable aplicable, excluyendo {exclusiones}
- **EBITDA**: Resultado operativo antes de amortización, depreciación e items extraordinarios. Ajustes permitidos: {lista}
- **Cash conversion**: Cash flow de operaciones / EBITDA del periodo. Benchmark sector: {rango}
- **Capex vs budget**: Ratio acumulado; >110% requiere escalación a operating committee

### Commercial
- **Pipeline activo**: Oportunidades en CRM con probabilidad ≥ {%} y actividad en últimos {días}
- **Conversion rate**: Deals firmados en periodo / oportunidades que entraron en fase qualified en periodo
- **Churn**: Clientes que cancelan o no renuevan / total clientes activos al inicio del periodo

### Operational
- **SLA compliance**: % servicios/contratos que cumplen los SLAs definidos en el periodo
- **Uptime**: % disponibilidad del sistema/servicio principal

### Governance
- **Reporting timeliness**: Días naturales desde cierre de mes hasta entrega del monthly pack completo
- **Committee attendance**: % asistencia de miembros obligatorios a comités programados

### People
- **Key hires**: Ratio posiciones cubiertas del hiring plan trimestral vs posiciones target
- **Retention**: % empleados clave retenidos al cierre del periodo (key = C-suite + critical roles)

---

## Traffic Light Dashboard

| KPI | Status | Trend | Comment |
|-----|--------|-------|---------|
| {KPI} | 🟢 On track / 🟡 At risk / 🔴 Off track | ↑↗→↘↓ | {1 línea} |

---

## Reporting Cadence

| Cadencia | KPIs Reportados | Foro | Formato |
|----------|----------------|------|---------|
| Weekly | Pipeline, SLA, operational | Operating committee | Dashboard + voice update |
| Monthly | All financial + commercial + governance | Board subcommittee | Full KPI pack + commentary |
| Quarterly | All + trend analysis + vs plan | IC update | Summary report |
