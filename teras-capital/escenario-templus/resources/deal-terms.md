# Deal terms — Templus (TCH4 → Vesta → Templus CD)

> Snapshot 31/12/2025 · Fuente: ISHA Vesta 11/10/2023 + Enmienda ISHA 11/12/2025 + Financing Agreement Vesta 11/12/2025 + auditoría EY IN25-6924 (TCH4) abril 2026 + BD `waterfall_params` (`business_line_id='templus'`).

## 1. Estructura financiera

### Inversión inicial TCH4 en Vesta — 3 tranches

- **Total invertido MdL (vía TCH4)**: 677.653,17€ (`waterfall_params.mdl_total_invested`).
- **MdL ord principal (Class B)**: 169.413,29€ (`mdl_total_ord_principal`).
- **MdL pref principal (Class D)**: 508.239,88€ (`mdl_total_pref_principal`).
- **Split ord/pref**: 25/75 según ISHA Cl. 3.

| Tranche | Fecha | Total tranche (€) | Class B Ord (25%) | Class D Pref (75%) |
|---|---|---|---|---|
| 1 | 2023-11-15 | 106.652,76 | 26.663,19 | 79.989,57 |
| 2 | 2023-12-19 | 417.780,41 | 104.445,10 | 313.335,31 |
| 3 | 2024-07-12 | 153.220,00 | 38.305,00 | 114.915,00 |
| **TOTAL MdL** | | **677.653,17** | **169.413,29** | **508.239,88** |

(Cifras BD `waterfall_params.tranche{1,2,3}_amount/_ord/_pref`. Las cifras representan la atribución MdL prorrateada al 32,60% sobre el ticket TCH4 total. El ticket TCH4 total en Vesta es ~2,08M€ = 32,60% × 6,38M€ aprox; total invested global Vesta-ICG es 183.934.000€ abril 2026.)

### Compromiso Vesta-ICG (300M€)

- **Total commit**: 300.000.000€ (`waterfall_params.total_commit_eur`).
- **Total invested abril 2026 (referencia EY IN25-6924)**: 183.934.000€ desplegados (61% del commit).
- **Pending commit (no desplegado)**: ~116.066.000€ (39%) reserva para nuevas adquisiciones M&A Templus y expansión Project Colorado.

### Financing Agreement Vesta → TCH4 (escudo fiscal único)

- **Fecha Financing Agreement**: 11/12/2025.
- **Loan financing pct**: 70% (Vesta financia 70% del ticket TCH4 vía préstamo subordinado).
- **vesta_loan_rate_pct**: 8,00% anual (`waterfall_params.vesta_loan_rate_pct`).
- **Saldo 31/12/2025 cuenta 17100000**: 976.756,13€ PTMO VESTA INVEST S.A.R.L. en TCH4 (reclasificado `pnc_otra` tras fix bug #14).
- **Beneficio fiscal**: intereses 8% deducibles en IS TCH4 — único escudo porque cap% MdL <5% en Templus CD invalida art. 21 LIS.
- **Tratamiento contable**: equity-rank socio según ISHA (NO bancario). Bug parser #14 corregido en mayo 2026.

### Deuda bancaria Templus CD chain

- **Templus CD agregado**: SIN deuda bancaria propia (pasivo 2,37M€ son provisiones LP + ajustes IS).
- **Templus Madrid**: ÚNICA filial con **deuda bancaria 23,6M€** (DC Alcalá fase 1, inmovilizado 89,2M€).
- **Otras 6 filiales España**: SIN deuda bancaria.
- **Project Colorado (4 Roosevelt)**: financiación vía AE Group HoldCo II — pendiente detalle facility.

## 2. ISHA Vesta — cláusulas clave (11/10/2023 + Enmienda 11/12/2025)

### Cap table reforzado

- **TCH4 2,00% capital Vesta** con derechos económicos modulados por ISHA Cl. 3 (Class B 25% Ord + Class D 75% Pref).
- Cap% económico TCH4 en Vesta depende del split ord/pref aplicado al 2% capital.
- **Class A Vesta (ICG)**: mayoritario, control.
- **Class B Investor (TCH4)**: 2,00% capital.
- **Pref Class D (TCH4)**: contemplado dentro del 2% capital con cupón preferente.

### Mecánica Class B vs Class D — ISHA Cl. 3

- **Class B Ord (25% split)**: TCH4 recibe 25% del split económico exit sobre la porción Class B disponible.
- **Class D Pref (75% split)**: TCH4 recibe 75% del split a través de Class D preferentes con cupón 12% acumulado.
- **Hurdle**: recuperación pref invested 300M€ (`exit_scenarios.hurdle_amount`).
- **Cupón Class D**: 12,00% anual (Enmienda ISHA 11/12/2025) — devenga hasta exit.

### Enmienda ISHA 11/12/2025 — cupón Class D 12%

- La enmienda 11/12/2025 fijó el cupón Class D preferente al **12,00% anual** (`waterfall_params.pref_coupon_pct=12, source='Enmienda ISHA 11/12/2025'`).
- Antes de la enmienda (ISHA original 11/10/2023), el cupón fue inferior (pendiente confirmar histórico exacto, referencia interna 8-10%).
- Impacto: incrementa la barrera económica para que TCH4 Class B Ord capture upside, dado que Class D acumula cupón 12% hasta hurdle.

### Sweet equity Class C — Templus Managers

- **2,00% capital Templus CD** atribuido a Templus Managers (NO Vesta, NO TCH4).
- Class C: sweet equity sobre upside operativo Templus CD (5% del upside según `exit_scenarios.notes`).
- Vinculado a permanencia mgrs + KPIs operativos.

### Decision matrix (supermayorías)

- ISHA Vesta contempla supermayorías Class A (ICG/Vesta) + Class B + Class C (Mgrs Templus) para decisiones de:
  - Refinanciación commit Vesta 300M€ o cualquier facility material
  - Cambio estrategia material Templus CD (M&A adicional, exit anticipado)
  - Cambios bylaws / class structure Templus CD o Vesta
  - Distribución dividendos extraordinarios
  - Entrada de nuevos managers (sujeto a cap dilución, pendiente cláusula exacta)

### Drag-along / Tag-along / ROFR

- **Drag-along**: requerido por mayoría calificada Class A (ICG/Vesta).
- **Tag-along**: pro-rata todos los socios Vesta + Templus CD, TCH4 incluido sobre 2,00% capital.
- **ROFR (Right of First Refusal) / Preemption**: contemplados en ISHA, detalles en SPA.

### Key-man clauses

- Triggered si key persons Templus CD management (CEO + COO + CFO Templus CD operativos) salen antes del exit.
- Mitigante: vesting acceleration on exit + replacement mecanismo.

## 3. Distribuciones históricas

| Evento | Fecha | Importe | Notas |
|---|---|---|---|
| (sin distribuciones de dividendos a fecha de snapshot 31/12/2025) | — | — | Vesta-Templus en fase despliegue commit, no se han generado dividendos distribuibles |

(A medida que avance commercialización Templus Madrid Alcalá fase 1 + Project Colorado, se esperan primeros dividendos referencia 2027-2028.)

## 4. Hurdle y waterfall ISHA

| Param | Valor | Fuente |
|---|---|---|
| Total commit Vesta-ICG | 300.000.000€ | `total_commit_eur` |
| Hurdle (recuperación pref invested) | 300.000.000€ | `exit_scenarios.hurdle_amount` |
| Preferred return rate Class D | 12% | `pref_coupon_pct` (Enmienda ISHA 11/12/2025) |
| Ord split pct (Class B) | 25% | `ord_split_pct` ISHA Cl. 3 |
| Pref split pct (Class D) | 75% | `pref_split_pct` ISHA Cl. 3 |
| Vesta loan rate | 8% | `vesta_loan_rate_pct` Financing Agreement 11/12/2025 |
| Loan financing pct | 70% | `loan_financing_pct` |
| IS rate TCH4 | 25% (sin art. 21 — <5%) | `is_rate_tch4_pct` |
| Total invested abril 2026 | 183.934.000€ | EY IN25-6924 |

Mecánica waterfall completa en `waterfall-y-escenarios-isha.md`.

## 5. Documentos clave (referencia)

- ISHA Vesta original 11/10/2023 (Class B + Class D)
- Enmienda ISHA 11/12/2025 (cupón Class D 12%)
- Financing Agreement Vesta → TCH4 11/12/2025 (8% loan rate)
- Auditoría EY IN25-6924 TCH4 abril 2026
- Pack Miguel 10-may-2026 (6 archivos):
  - Balance Consolidado 2025 Templus
  - P&L by Site (7 filiales España + 4 Roosevelt)
  - Revenues + Budget 2026
  - Colorado Mgmt Accounts (4 Roosevelt)
  - Org chart Templus v8 14/04/2026
  - Audit firm consolidado
- SPA legacy filiales adquiridas (MAVICO / Beta DC / Espacio Edge / MBA Datacenters / Waterways Global)

Listado completo con paths en `documentos-referencia.md`.

## 6. Pendientes contractuales

- Refinanciación Vesta 2027-2028 (vinculado a despliegue commit 300M€): term sheet pendiente.
- Modelado completo cadena Vesta → AE HoldCo II → 4 Roosevelt (tarea #9 BD MdL — templus-cd 178,5M€ orphan).
- Opinion letter art. 21 LIS Templus actualizada (escudo Vesta 8%).
- Plan 100 días integración Templus Spain (Espacio Edge, adq. 25/06/2025).
- Comercialización plan Templus Ceuta (constit. 11/06/2025).
- Cap table histórico Vesta detallado (composición ICG + Class A + Class B + Pref Class D).
