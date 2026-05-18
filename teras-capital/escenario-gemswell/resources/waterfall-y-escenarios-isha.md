# Waterfall y escenarios ISHA — Gemswell

> Snapshot 31/12/2025 · BD `savenikqhmcuwmcnabca` (`waterfall_params`) + ISHA Gemswell + Pacto Socios SHA SW Infrasports nov 2024 + calculadora `/waterfall-gemswell`.

## Estructura del waterfall — visión general

El waterfall Gemswell distribuye flujos de exit / distribución consolidada entre los socios de TCH3 (12 socios) y los compartimentos vehiculados por SW Infrasports (VSO II / Wave Park + pipeline). Aplican tres mecánicas:

1. **Waterfall TCH3 propio**: hurdle 8% + promote 20% sobre exceso, distribución pro-rata cap%.
2. **Waterfall SW Infrasports**: paritario 50/50 con Stoneweg sobre carry compartimentos.
3. **Cadena lateral Quarter Capital / Grand View**: cuelga de IPN directo (32,29%), capitalizada doctrinalmente en TCH3 pero jurídicamente IPN → QC → Grand View.

## Parámetros calculadora — BD `waterfall_params`

### Parámetros estructurales

| Parámetro BD | Valor | Descripción | Fuente |
|---|---|---|---|
| `hurdle_rate_pct` | 8,0% | Hurdle ISHA sobre capital invertido | Acuerdo socios Gemswell |
| `promote_pct` | 20,0% | Promote sobre exceso hurdle | ISHA Gemswell |
| `swi_tch3_pct` | 50,0% | Cap% TCH3 en SW Infrasports | Pacto Socios SHA nov 2024 |
| `tch3_promote_pct_swi` | 50,0% | Promote sobre carry SWI para TCH3 | Pacto Socios SHA |
| `swi_fixed_fee_eur` | 250.000€ | Fee anual fijo SW Infrasports | Pacto Socios SHA |
| `mgmt_fee_per_project_eur` | 200.000€ (BD default) | Fee gestión por proyecto | ISHA Gemswell |

### Parámetros Kelpa (referencia)

| Parámetro BD | Valor BD default | Valor calculadora actual | Fuente |
|---|---|---|---|
| `kelpa_debt_eur` | 50.000.000€ | 74.700.000€ | Acuerdo Kelpa |
| `kelpa_equity_eur` | 30.000.000€ | 49.000.000€ | Acuerdo Kelpa |
| Total compartimento | 80.000.000€ | 123.700.000€ | derivado |
| `num_projects` | 2 | 2 | BD |
| `tx_costs_pct` | 1,5% | 1,5% | BD |

> **Discrepancia documentada**: el `business_lines.gemswell.total_investment = 80.000.000€` coincide con el default BD (50M + 30M), pero la calculadora actual usa 74,7M / 49M. A reconciliar.

### Parámetros VSO II (Wave Park) — factores históricos

| Parámetro BD | Valor | Fuente |
|---|---|---|
| `vso_ii_unaudited_nav_pct` | 124,48% | Email Stoneweg/Ramón Romero 7-may-2026 |
| `vso_ii_credito_face_eur` | 1.000.000€ | Acuerdo TCH3 con compartimento Wave Park |
| Fair value derivado | 1.244.800€ | calculado 1.000.000 × 1,2448 |

## Mecánica waterfall TCH3 — orden de distribución

Para un evento de exit o distribución consolidada, el orden es:

### Etapa 1: Costes de transacción

- Tx costs 1,5% sobre proceeds brutos (`tx_costs_pct`).

### Etapa 2: Servicio deuda Kelpa (compartimento VM)

- Repago deuda Kelpa: 50M€ (BD default) / 74,7M€ (calculadora actual).
- Aplica antes de cualquier distribución a equity.

### Etapa 3: Retorno capital invertido (return of capital)

- Devolución del capital aportado por cada socio a TCH3.
- Pro-rata sobre `total_investment` por cap%.

### Etapa 4: Hurdle 8% sobre capital invertido

- Pago preferente del 8% acumulado sobre capital invertido a los socios de TCH3.
- Catch-up para alinear retorno mínimo.

### Etapa 5: Promote 20% sobre exceso

- 80% restante para los socios pro-rata cap%.
- 20% para promote vehicle (mgmt / TERAS).

### Etapa 6: Distribución pro-rata final

- Reparto del 80% del exceso entre los 12 socios TCH3 según cap%:
  - Pool MdL (IPN 36,45% + TCH2 10,41%): 46,86%
  - MM Sports: 36,41%
  - MCT: 5,55%
  - I. Velilla: 2,78%
  - Indeps + LSS: ~10,38%
  - Faura: 0,21%

### Etapa 7: Fees recurrentes

- Fee anual fijo SW Infrasports: 250.000€ recurrente.
- Fee por proyecto: 200.000€ (BD default) / 925.500€ (calculadora actual) recurrente operativo.

## Mecánica waterfall SW Infrasports — compartimento VSO II

Para exit del compartimento Wave Park (VSO II):

| Etapa | Mecánica |
|---|---|
| 1 | Repago face crédito 1.000.000€ a TCH3 |
| 2 | Promote 50%/50% sobre el exceso (NAV > 100%): TCH3 50%, Stoneweg 50% |
| 3 | Subida proceeds a TCH3 como dividendo / liquidación de SW Infrasports |
| 4 | Aplicación waterfall TCH3 standard (etapas 1-7 anteriores) |

**Ejemplo VSO II — exit a NAV actual 124,48%**:

- Face value: 1.000.000€
- NAV current: 124,48%
- Proceeds compartimento: 1.244.800€
- Exceso sobre face: 244.800€
- Promote split TCH3: 244.800 × 50% = 122.400€
- TCH3 recibe: 1.000.000 (face) + 122.400 (promote 50% sobre exceso) = **1.122.400€**
- Stoneweg recibe: 244.800 × 50% = 122.400€

## Escenarios exit consolidado Gemswell — estimaciones simplificadas

> Estimaciones aproximadas. NO sustituyen al modelo completo de `/waterfall-gemswell`. Cifras orientativas.

### Escenario base — exit consolidado 100M€ NAV

| Concepto | Valor |
|---|---|
| Proceeds brutos | 100.000.000€ |
| Tx costs (1,5%) | -1.500.000€ |
| Proceeds netos | 98.500.000€ |
| Repago deuda Kelpa (default) | -50.000.000€ |
| Distribución a equity | 48.500.000€ |
| Capital invertido aprox (techo) | 30.000.000€ |
| Hurdle 8% acumulado (asumido 5 años) ~13M€ | -13.000.000€ |
| Total pre-promote | 5.500.000€ |
| Promote 20% | -1.100.000€ |
| Disponible pro-rata socios TCH3 | 4.400.000€ |
| **Pool MdL (46,86%)** | **2.062.080€** |
| MM Sports (36,41%) | 1.601.640€ |
| MCT (5,55%) | 244.200€ |
| I. Velilla + Indeps + LSS (~13,2%) | 580.800€ |

> NOTA: este escenario es **muy simplificado**. La calculadora real usa parámetros distintos (74,7M Kelpa / 49M equity), múltiples proyectos (num_projects=2), capital invertido por etapas, etc. Usar `/waterfall-gemswell` para cálculos precisos.

### Escenario upside — exit consolidado 150M€ NAV

| Concepto | Valor |
|---|---|
| Proceeds brutos | 150.000.000€ |
| Tx costs (1,5%) | -2.250.000€ |
| Repago deuda Kelpa | -50.000.000€ |
| Distribución a equity | 97.750.000€ |
| Capital invertido | -30.000.000€ |
| Hurdle 8% acumulado | -13.000.000€ |
| Total pre-promote | 54.750.000€ |
| Promote 20% | -10.950.000€ |
| Disponible pro-rata | 43.800.000€ |
| **Pool MdL (46,86%)** | **20.524.680€** |

### Escenario conservador — exit consolidado 50M€ NAV

| Concepto | Valor |
|---|---|
| Proceeds brutos | 50.000.000€ |
| Tx costs (1,5%) | -750.000€ |
| Repago deuda Kelpa (parcial — 50M no cubierto) | -49.250.000€ |
| Distribución a equity | 0€ |
| **Pool MdL** | **0€** |

> En escenario conservador, todo el proceeds se va al servicio deuda Kelpa. NO hay distribución a equity. Hurdle ISHA queda sin satisfacer.

## Sensibilidad — driver principal

El driver principal del retorno MdL es **el ratio NAV proceeds / deuda Kelpa**:

- Si NAV < deuda Kelpa default (50M€) → equity wipe out completo, MdL 0€.
- Si NAV ≈ deuda Kelpa: marginal retorno solo si supera capital invertido + hurdle.
- Si NAV >> deuda Kelpa: retorno convexo a partir del punto de cruce.

> El waterfall es **altamente convexo** arriba del punto deuda + capital invertido + hurdle. Pequeñas variaciones en NAV consolidado tienen impacto multiplicado en retorno MdL.

## Wave Park / VSO II — escenarios exit aislados

### Escenario 1: NAV mantiene 124,48%

- Face crédito TCH3: 1.000.000€
- NAV exit: 1.244.800€
- Promote 50% sobre exceso 244.800€: TCH3 122.400€, Stoneweg 122.400€
- **TCH3 recibe 1.122.400€**
- Subida pro-rata a Pool MdL (46,86%): **526.336€**

### Escenario 2: NAV sube a 150%

- NAV exit: 1.500.000€
- Promote 50% sobre exceso 500.000€: TCH3 250.000€, Stoneweg 250.000€
- **TCH3 recibe 1.250.000€**
- Pool MdL (46,86%): **585.750€**

### Escenario 3: NAV baja a 100% (sin exceso)

- NAV exit: 1.000.000€
- Sin promote.
- **TCH3 recibe 1.000.000€** (face crédito).
- Pool MdL (46,86%): **468.600€**

### Escenario 4: NAV bajo 100% (deterioro)

- NAV exit: 80% = 800.000€
- TCH3 recibe 800.000€ (no recupera face completo).
- Pool MdL (46,86%): **374.880€**
- Pérdida sobre face: 200.000€ (TCH3 absorbe).

## Mapping con calculadora `/waterfall-gemswell`

| Input UI | Parámetro BD | Notas |
|---|---|---|
| Hurdle rate | `hurdle_rate_pct` | 8,0% default |
| Promote | `promote_pct` | 20,0% default |
| Kelpa debt | `kelpa_debt_eur` | 50M default; calculadora 74,7M |
| Kelpa equity | `kelpa_equity_eur` | 30M default; calculadora 49M |
| Num projects | `num_projects` | 2 |
| Tx costs | `tx_costs_pct` | 1,5% |
| SW Infrasports fee | `swi_fixed_fee_eur` | 250K |
| Mgmt fee / project | `mgmt_fee_per_project_eur` | 200K default; calculadora 925,5K |
| VSO II NAV | `vso_ii_unaudited_nav_pct` | 124,48% |
| VSO II face | `vso_ii_credito_face_eur` | 1M€ |
| SWI promote TCH3 | `tch3_promote_pct_swi` | 50% |
| SWI cap% TCH3 | `swi_tch3_pct` | 50% |

## Discrepancias documentadas — pendiente reconciliar

| Parámetro | BD default | Calculadora actual | Decisión pendiente |
|---|---|---|---|
| Kelpa debt | 50M€ | 74,7M€ | Confirmar valor real con Acuerdo Kelpa actualizado |
| Kelpa equity | 30M€ | 49M€ | Confirmar valor real con Acuerdo Kelpa actualizado |
| Total compartimento | 80M€ | 123,7M€ | Total investment Gemswell techo BD = 80M€ |
| Mgmt fee / project | 200K | 925,5K | Confirmar fee real ISHA |

## Comparativa con otras líneas TERAS

| Línea | Hurdle | Promote | Sponsor | Vehículo MdL |
|---|---|---|---|---|
| Olin (TCH1 → TUCA / MasOrange) | n/a (waterfall por escenarios sale price 250-500M€) | n/a explícito | Asterion | TCH1 |
| Templus (TCH4 → data centers) | a confirmar | a confirmar | Vesta-ICG | TCH4 |
| **Gemswell (TCH3 → surf parks)** | **8%** | **20%** | **Stoneweg** | **TCH3** |

## Próximos pasos calculadora

1. **Reconciliar discrepancias** Kelpa debt/equity y mgmt fee BD vs calculadora actual.
2. **Modelar exit Wave Park** aislado en calculadora `/waterfall-gemswell` con sliders NAV.
3. **Modelar exit consolidado** Gemswell con sliders de NAV consolidado, mantener hurdle dinámico.
4. **Integrar capital invertido real** por socio (no agregado), reflejar capitalizaciones sept 2025.
5. **Versionar parámetros**: BD `waterfall_params` con metadata `source` y `valid_from` para histórico.
6. **Sensibilidad multi-driver**: NAV consolidado × tipo deuda Kelpa × num proyectos.

## Consideraciones ISHA pendientes confirmar

- **Catch-up clause**: en hurdle 8% — ¿full catch-up o pari passu?
- **Clawback**: si proceeds posteriores no satisfacen hurdle inicial, recuperación de promote pre-pagado.
- **Tier de promote**: ¿escalonado por múltiplo (2× → 25%, 3× → 30%) o linear 20%?
- **Promote vehicle**: a definir destinatarios mgmt (TERAS team) vs reparto en pool MdL.
- **Mecánica supermayorías** para decisiones estructurales (exits, refis, ampliaciones).
