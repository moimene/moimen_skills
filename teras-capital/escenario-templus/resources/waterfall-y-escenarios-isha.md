# Waterfall y escenarios ISHA — Templus (Vesta / Templus CD / Project Colorado)

> Snapshot 31/12/2025 · BD `exit_scenarios` + `waterfall_params` (`business_line_id='templus'`) + ISHA Vesta 11/10/2023 + Enmienda ISHA 11/12/2025 + Financing Agreement Vesta 11/12/2025.
> **Calculadora viva**: `https://mdl-patrimonio.vercel.app/waterfall-templus` (parámetros editables en `waterfall_params`).

## 1. Estructura ISHA Vesta — tiers de retorno

Orden de prelación en la cascada (waterfall) Templus:

| # | Tier | Beneficiario | Condición |
|---|---|---|---|
| 1 | Servicio Financing Agreement Vesta → TCH4 (8%) | Vesta (recupera principal + intereses) | Senior intragrupo Vesta-TCH4 |
| 2 | Hurdle pref recuperación | Class D Pref (TCH4 75% + ICG) | Hurdle 300M€ recuperación pref invested |
| 3 | Cupón preferente Class D (12%) | Class D Pref (TCH4 75% + ICG) | Cupón acumulado anual hasta exit |
| 4 | Class B Ord upside | TCH4 25% Class B Ord + ICG | Distribución pro-rata Class B sobre exceso hurdle + cupón Class D |
| 5 | Sweet equity Class C | Templus Managers (2% Templus CD) | 5% del upside operativo Templus CD |

**Variables clave waterfall** (`waterfall_params`):

| Param | Valor | Notas |
|---|---|---|
| `total_commit_eur` | 300.000.000€ | Compromiso Vesta-ICG |
| `total_invested_eur` | 183.934.000€ | Desplegado abril 2026 (EY IN25-6924) |
| `hurdle_amount` | 300.000.000€ | `exit_scenarios.hurdle_amount` — recuperación pref invested |
| `ord_split_pct` | 25,00% | Class B Ord (ISHA Cl. 3) |
| `pref_split_pct` | 75,00% | Class D Pref (ISHA Cl. 3) |
| `pref_coupon_pct` | 12,00% | Cupón Class D (Enmienda ISHA 11/12/2025) |
| `preferred_return_pct` | 12 | Equivalente cupón Class D |
| `vesta_loan_rate_pct` | 8,00% | Financing Agreement Vesta 11/12/2025 |
| `loan_financing_pct` | 70% | Vesta financia 70% ticket TCH4 |
| `mdl_pct_in_tch4` | 32,60% | IPN 17% + TCH2 15,60% |
| `teras_pct_global` | 2,00% | TCH4 en Vesta (Class B Investor) |
| `ipn_pct_tch4` | 17,00% | |
| `tch2_pct_tch4` | 15,60% | |
| `is_rate_tch4_pct` | 25,00% | LIS art. 21 — sin exención (<5%) |
| `mdl_total_invested` | 677.653,17€ | MdL en TCH4 agregado |
| `mdl_total_ord_principal` | 169.413,29€ | MdL Class B (25%) |
| `mdl_total_pref_principal` | 508.239,88€ | MdL Class D (75%) |
| `tranche1_amount / date` | 106.652,76€ / 2023-11-15 | Tranche 1 |
| `tranche2_amount / date` | 417.780,41€ / 2023-12-19 | Tranche 2 |
| `tranche3_amount / date` | 153.220,00€ / 2024-07-12 | Tranche 3 |

## 2. Cláusulas clave ISHA

- **Drag-along**: requerido por mayoría calificada Class A (ICG/Vesta).
- **Tag-along**: pro-rata todos los socios Vesta + Templus CD, TCH4 incluido sobre 2,00% capital.
- **ROFR / preemption**: contemplados en ISHA, detalle en SPA.
- **Key-man**: triggered si key persons Templus CD management salen antes del exit.
- **Vesting on exit Class C**: full acceleration Templus Managers sweet equity.
- **Cap dilución new mgrs**: contemplado en Enmienda 11/12/2025 (cláusula exacta pendiente confirmar).
- **Supermayoría Class A + Class B + Class C** para: refinanciación Vesta, cambio bylaws, M&A material, distribución dividendos extraordinarios, exit anticipado.

## 3. Los 4 escenarios exit Templus — BD `exit_scenarios`

### Escenario A — Sin upside (sale price 250M€)

| Concepto | Valor |
|---|---|
| Sale price | 250.000.000€ |
| Hurdle (recuperación pref invested) | 300.000.000€ — **NO se alcanza** |
| Equity value distribuible Class B | ~0€ (sale price < hurdle) |
| TCH4 gross (solo recuperación parcial Class D pref) | ~812.000€ |
| MdL gross | 812.000€ |
| **MdL net (post IS 25% TCH4)** | **750.000€** |
| Múltiplo MdL sobre inversión 677.653€ | ~1,1× |
| Notas | "Solo recuperación Class D con preferente 12%. Retorno = inversión × 1.2. Sin activación sweet equity Class B." |

### Escenario B — Éxito moderado (sale price 350M€)

| Concepto | Valor |
|---|---|
| Sale price | 350.000.000€ |
| Hurdle | 300.000.000€ |
| Upside sobre hurdle | 50.000.000€ |
| TCH4 gross (Class D recuperado + 12% cupón 812K€ + sweet equity 5% Class B sobre 50M€) | ~3,25M€ |
| MdL gross (32,60% TCH4 + path TCIH agregado) | 3.250.000€ |
| **MdL net (post IS 25%)** | **2.900.000€** |
| Múltiplo MdL | ~4,8× |
| Notas | "Class D recuperada + 12% preferente 812K€. Upside 50M€ → 5% sweet equity Class B = 2,5M€. ~4,8× múltiplo." |

### Escenario C — Escenario base ICG (sale price 400M€)

| Concepto | Valor |
|---|---|
| Sale price | 400.000.000€ |
| Hurdle | 300.000.000€ |
| Upside sobre hurdle | 100.000.000€ |
| TCH4 gross (Class D + preferente + sweet equity 5% × 100M = 5M) | ~5,812M€ |
| MdL gross | 5.812.000€ |
| **MdL net (post IS 25%)** | **5.200.000€** |
| Múltiplo MdL | ~8,6× |
| Notas | "Class D recuperada + preferente 812K€. Upside 100M€ → sweet equity 5% = 5M€. Total 5,8M€ ~8,6× múltiplo." |

### Escenario D — Gran éxito (sale price 500M€)

| Concepto | Valor |
|---|---|
| Sale price | 500.000.000€ |
| Hurdle | 300.000.000€ |
| Upside sobre hurdle | 200.000.000€ |
| TCH4 gross (Class D + preferente + 5% × 200M = 10M) | ~10,812M€ |
| MdL gross | 10.812.000€ |
| **MdL net (post IS 25%)** | **9.700.000€** |
| Múltiplo MdL | ~16× |
| Notas | "Class D + preferente 812K€. Upside 200M€ → 5% sweet equity = 10M€. Total ~10,8M€ ~16× múltiplo." |

> **CRÍTICO**: la diferencia entre "Sin upside" (250M€) y "Gran éxito" (500M€) es de **~13×** en retorno MdL neto. El waterfall Templus es **convexo en upside Class B activado solo por encima del hurdle 300M€ + recuperación cupón Class D 12%**. La sensibilidad al sale price es alta, particularmente al pasar 350M€ (activación Class B sweet equity 5%).

## 4. Sensibilidad

| Variable | Rango | Impacto IRR MdL base case (cualitativo) |
|---|---|---|
| Sale price Templus | 250 → 500M€ | Convexo arriba de 300M€ hurdle. Sweet equity 5% activada con upside positivo. Factor ~13× upside escenario D vs A |
| Cupón Class D | 10% → 14% bps elevation | Eleva barrera de activación Class B → retrasa upside MdL |
| Timing exit | 2027 → 2030 | Cupón pref 12% acumulado erosiona Class B upside con timing diferido (cada año adicional cuesta 12% sobre 300M€ = 36M€/año en cupón) |
| Total invested | 183M → 300M€ | Si Vesta despliega commit completo 300M€, hurdle 300M€ se mantiene pero más capital base preferente |
| Vesta loan rate | 8% → 10% | Reduce capital distribuible TCH4 (más servicio intereses), erosiona escudo fiscal proporcionalmente |
| IS TCH4 | 25% → cambio LIS | Aumento >25% reduciría MdL net 1:1. Disminución >25% (reintroducción exención) sería sustancial mejora |
| Sweet equity Class B % | 5% → 7% | Cada 1pp adicional = 1-2M€ MdL gross |

## 5. Calculadora Templus en mdl-patrimonio

URL: `https://mdl-patrimonio.vercel.app/waterfall-templus`

Mapeo páginas Next.js:
- Página: `src/app/waterfall-templus/page.tsx`
- Lib lógica: `src/lib/waterfall-validators.ts` (compartido con Olin/Gemswell)
- Parámetros editables: tabla `waterfall_params` con `business_line_id='templus'`

**Parámetros editables clave**:

| Param key | Default | Editable | Descripción |
|---|---|---|---|
| `mdl_pct_in_tch4` | 32,60% | sí | % MdL efectivo TCH4 (IPN 17% + TCH2 15,60%) |
| `teras_pct_global` | 2,00% | sí | Cap% TCH4 en Vesta |
| `ord_split_pct` | 25,00% | sí | Class B Ord split |
| `pref_split_pct` | 75,00% | sí | Class D Pref split |
| `pref_coupon_pct` | 12,00% | sí | Cupón Class D (Enmienda 11/12/2025) |
| `vesta_loan_rate_pct` | 8,00% | sí | Vesta loan (Financing Agreement) |
| `loan_financing_pct` | 70% | sí | % financiado por Vesta |
| `is_rate_tch4_pct` | 25% | sí | IS TCH4 (sin art. 21) |
| `total_commit_eur` | 300.000.000€ | sí | Commit Vesta-ICG |
| `total_invested_eur` | 183.934.000€ | sí | Invested abril 2026 |
| `hurdle_amount` | 300.000.000€ | sí | Hurdle pref invested |

## 6. Mecánica del cálculo

### Cálculo TCH4 sobre upside Templus

Para sale price S sobre Templus CD valuation:

1. **Recuperación pref invested**: hasta hurdle 300M€ → Class D Pref recupera principal.
2. **Cupón Class D acumulado**: 12% × años transcurridos × principal Class D acumulado. Estimación 4 años hasta exit (referencia 2027-2029): ~12% × 4 × 75% × 300M = ~108M€ cupón acumulado teórico.
3. **Upside post-hurdle + post-cupón Class D**: si S > (hurdle + cupón Class D) = activación Class B.
4. **Class B Ord upside**: 25% del split. Sweet equity 5% sobre el upside neto.
5. **TCH4 share**: 2% capital Vesta × atribución MdL 32,60%.

### Path 2 TCIH directo a Templus CD

- TCIH 2% directo en Templus CD recibe pro-rata Class B sobre cualquier distribución Templus CD.
- Cap% MdL agregado en Templus CD vía Path 2: 51,665% TCIH × 2% = 1,033%.
- TCIH paga 25% IS sin exención sobre flujos Templus CD.

### Suma agregada MdL

- Cap% efectivo agregado MdL en Templus CD = 0,626% (Path 1) + 1,033% (Path 2) = **1,62%**.
- Los `exit_scenarios.mdl_gross/mdl_net` reflejan el agregado de ambos paths.

## 7. SQL — regeneración

```sql
-- Exit scenarios Templus
SELECT scenario_name, sale_price, hurdle_amount, mdl_gross_return, mdl_net_return, tch_return, notes
FROM exit_scenarios
WHERE business_line_id = 'templus'
ORDER BY sale_price;

-- Waterfall params Templus
SELECT param_key, param_value, default_value, source, is_editable, factor_group
FROM waterfall_params
WHERE business_line_id = 'templus'
ORDER BY factor_group, param_key;

-- Verificar tranches inversión
SELECT param_key, param_value
FROM waterfall_params
WHERE business_line_id = 'templus' AND param_key LIKE 'tranche%'
ORDER BY param_key;
```

## 8. Cálculo manual rápido — verificación escenario C (400M€ base ICG)

Para `sale_price = 400M€`:

1. **Hurdle pref**: 300M€ → Class D recupera principal. Excede hurdle por 100M€ disponible upside.
2. **Cupón Class D acumulado** (estimación a horizonte exit ~2027-2029, 4-5 años): 12% × 4 × 75% × 300M = ~108M€. Pero el upside disponible es solo 100M€ < cupón teórico → en escenario 400M€ Class B NO captura upside meaningful, solo sweet equity 5%.
3. **Sweet equity Class B (5% sobre upside 100M€)**: 5M€.
4. **Class D recuperación cupón parcial** (812K€ pref preferente devengado parcial atribuible a TCH4 vía 2% Vesta × 32,60% MdL): 812K€.
5. **TCH4 gross total ≈** 5M€ sweet equity + 812K€ cupón = **5,812M€** (cuadra con `exit_scenarios.tch_return=5,812M€`).
6. **MdL via TCH4** (Path 1 + parcial Path 2): ~5,812M€ gross MdL aprox (agregando ambos paths con sus factores).
7. **MdL net post IS 25% TCH4** = ~5,2M€ (cuadra con `exit_scenarios.mdl_net_return = 5,200,000€`).

Coincide con escenario C base ICG.

## 9. Referencia cruzada

- **Path 2 TCIH directo**: TCIH 2% Templus CD en composición agregada MdL 1,033%. Tributación TCIH 25% IS sin exención.
- **Project Colorado vía AE Group HoldCo II**: rama paralela vinculada a TCH4 directamente (no vía Vesta para parent). Pendiente modelado completo (tarea #9 BD MdL).
- **Templus CD `exclude_from_group_totals=true`**: evitar doble conteo con Vesta consolidado.
- **Global Cabria legacy**: NO usar (legacy duplicado de Templus CD).
- **Fix bug parser #14**: cuenta 17100000 Vesta reclasificada `pnc_otra` — afecta estructura pasivo TCH4 pero NO afecta waterfall.

## 10. Notas sobre coherencia escenarios

Las cifras en BD `exit_scenarios` aplican el factor `mdl_pct_in_tch4=32,60%` × `teras_pct_global=2,00%` con la mecánica Class B (25%) + Class D (75%) + cupón 12% + sweet equity 5% sobre upside. Los net post-IS aplican 25% IS sin exención.

Cualquier informe que cite exit scenarios Templus debe:
1. Citar BD `exit_scenarios` con los 4 niveles (250/350/400/500M€).
2. NO inventar IRR / MOIC sin verificar contra BD.
3. Distinguir explícitamente que Class D 12% es la versión Enmienda 11/12/2025 (vigente).
4. Aclarar que cap% MdL final agregado en Templus CD = 1,62% (no 32,60% ni 2,00% aislados).
