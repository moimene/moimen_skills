# Template Risk Register — TERAS Capital

Risk register para IC pack. Mínimo 10 riesgos cubriendo las 5 categorías obligatorias.

---

## Instrucciones

1. **Mínimo 10 riesgos** — el IC sospecha si hay pocos
2. Cubrir las 5 categorías: Commercial, Financial, Operational, Regulatory, Reputational
3. Cada riesgo tiene **mitigación específica** (no genérica) y **owner asignado**
4. Vincular riesgos a KPIs cuando sea posible
5. Actualizar mensualmente y presentar cambios al Board

---

## Risk Register

| # | Riesgo | Categoría | Prob. | Impacto | Score | Mitigación | Owner | KPI Vinculado | Status | Última Revisión |
|---|--------|-----------|-------|---------|-------|------------|-------|---------------|--------|-----------------|
| 1 | {Pérdida de cliente(s) clave: concentración de revenue >X%} | Commercial | {A/M/B} | Alto | {score} | {Diversificación pipeline; retención proactiva; contratos largo plazo} | {TERAS / Commercial} | Churn, Revenue | Open | {fecha} |
| 2 | {Pipeline comercial insuficiente para targets} | Commercial | {A/M/B} | Alto | {score} | {Ramp-up comercial acelerado; hunting + farming; pricing review} | {TERAS} | Pipeline activo, Conversion | Open | {fecha} |
| 3 | {Cash burn superior al plan} | Financial | {A/M/B} | Alto | {score} | {Cash discipline: weekly cash monitoring; capex gates; covenant compliance} | {CFO + TERAS} | Cash conversion, Capex vs budget | Open | {fecha} |
| 4 | {Working capital deterioro post-close} | Financial | {A/M/B} | Medio | {score} | {WC monitoring mensual; cobros proactivos; gestión de proveedores} | {CFO} | WC days | Open | {fecha} |
| 5 | {Retraso en obtención de permisos/licencias} | Regulatory | {A/M/B} | Alto | {score} | {Early filing; seguimiento proactivo; buffer en timeline} | {Legal + TERAS} | Permit tracker | Open | {fecha} |
| 6 | {Cambio regulatorio adverso} | Regulatory | {A/M/B} | Medio | {score} | {Monitoring regulatorio; lobby; scenario planning} | {Legal} | Regulatory tracker | Open | {fecha} |
| 7 | {Pérdida de persona clave (C-suite)} | People | {A/M/B} | Alto | {score} | {Retention packages; succession planning; non-competes} | {HR + TERAS} | Retention rate | Open | {fecha} |
| 8 | {Retraso en deployment tecnológico} | Operational | {A/M/B} | Medio | {score} | {Project management riguroso; milestones con gates; vendor management} | {CTO + TERAS} | SLA compliance | Open | {fecha} |
| 9 | {Integración operativa post-deal más lenta de lo previsto} | Operational | {A/M/B} | Medio | {score} | {100-day plan con quick wins; dedicated integration team; weekly tracking} | {TERAS} | 100-day milestones | Open | {fecha} |
| 10 | {Riesgo reputacional: conflicto ético o ESG} | Reputational | Baja | Alto | {score} | {Due diligence ESG; compliance framework; whistleblower channel} | {TERAS + Legal} | ESG checklist | Open | {fecha} |

---

## Risk Scoring Methodology

### Probabilidad

| Nivel | Descripción | Score |
|-------|-------------|-------|
| **Alta** | >60% probabilidad de ocurrencia en 12 meses | 3 |
| **Media** | 30-60% probabilidad | 2 |
| **Baja** | <30% probabilidad | 1 |

### Impacto

| Nivel | Descripción | Score |
|-------|-------------|-------|
| **Alto** | Impacto material en value creation plan, economics, o reputación | 3 |
| **Medio** | Impacto significativo pero manejable con acción correctiva | 2 |
| **Bajo** | Impacto menor, absorbible sin cambios materiales | 1 |

### Risk Score = Probabilidad × Impacto

| Score | Nivel | Acción Requerida |
|-------|-------|-----------------|
| **7–9** | 🔴 Crítico | Mitigación inmediata; escalación a Board; IC awareness |
| **4–6** | 🟡 Significativo | Plan de mitigación activo; revisión mensual en Board |
| **1–3** | 🟢 Bajo | Monitoreo; revisión trimestral |

---

## Heat Map

```
          Impacto →
          Bajo (1)    Medio (2)    Alto (3)
Alta (3)  | 🟡 3  |   🟡 6   |   🔴 9   |
Prob. ↓   |--------|----------|----------|
Media (2) | 🟢 2  |   🟡 4   |   🟡 6   |
          |--------|----------|----------|
Baja (1)  | 🟢 1  |   🟢 2   |   🟡 3   |
```

---

## Risk Movement Tracker

Presentar en cada Board meeting los cambios vs mes anterior:

| # | Riesgo | Score Anterior | Score Actual | Movimiento | Comentario |
|---|--------|---------------|-------------|------------|------------|
| 1 | {riesgo} | {score} | {score} | ↑↓→ | {por qué cambió} |

---

## Categorías Obligatorias — Checklist

- [ ] **Commercial** (≥2 riesgos): demanda, pricing, competencia, concentración, churn
- [ ] **Financial** (≥2 riesgos): caja, deuda, capex, working capital, covenant compliance
- [ ] **Operational** (≥2 riesgos): ejecución, tecnología, supply chain, people, integración
- [ ] **Regulatory** (≥1 riesgo): permisos, licencias, cambios regulatorios, compliance
- [ ] **Reputational** (≥1 riesgo): conflictos, ética, ESG, confidencialidad

---

## Emerging Risks (Watch List)

Riesgos no materializados pero que merecen vigilancia:

| # | Riesgo Emergente | Categoría | Trigger de Activación | Monitoring |
|---|-----------------|-----------|----------------------|------------|
| E1 | {e.g., entrada de competidor nuevo} | Commercial | {trigger} | {cómo se monitorea} |
| E2 | {e.g., cambio geopolítico} | Regulatory | {trigger} | {cómo se monitorea} |
