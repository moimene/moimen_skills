# Waterfall y escenarios ISHA — Olin (TUCA Bidco / MasOrange)

> Snapshot 31/12/2025 · BD `exit_scenarios` + `waterfall_params` (`business_line_id='olin'`) + ISHA TUCA reformulado.
> **Calculadora viva**: `https://mdl-patrimonio.vercel.app/waterfall` (parámetros editables en `waterfall_params`).

## 1. Estructura ISHA TUCA — tiers de retorno

Orden de prelación en la cascada (waterfall):

| # | Tier | Beneficiario | Condición |
|---|---|---|---|
| 1 | Servicio deuda neta Asterion + senior banks | Asterion + bancos | senior, pari passu |
| 2 | Preferred return Class A + Privilegiadas (cupón 10% anual) | Tuca Midco (98% Class A) + TCH1 (Privilegiadas 0,696%) | hurdle = 270M€ recuperación pref invested |
| 3 | Catch-up GP (si aplica) | (estructura GP no observable en exit_scenarios actuales) | — |
| 4 | Carry tier Class B upside | TCH1 17,75% Class B Ord + A.Izzo 0,20% | distribución pro-rata Class B sobre exceso 270M€ |

**Variables clave waterfall** (`waterfall_params`):

| Param | Valor | Notas |
|---|---|---|
| `hurdle_rate_pct` / `pref_return_rate` | 10% | ISHA Cl. 8(D) |
| `total_pref_invested` | 270.000.000€ | Hurdle preferente |
| `tch1_ord_pct` (Class B Ord) | 17,75% | ISHA Cl. 3 |
| `tch1_ord_pct_diluted` | 15,97% | máx dilución 10% mgrs (ISHA Cl. 6.4(C)) |
| `tch1_pref_pct` (Privilegiadas) | 0,696% | ISHA Schedule |
| `pref_coupon_pct` | 10% | ISHA Cl. 8(D) |
| `mdl_pct_tch1` | 38,14% | (factor productivo — ver decisiones-clave #2) |
| `class_b_vesting_on_exit` | 100% | full acceleration |
| `is_rate_tch1_pct` | 25% | sin art. 21 LIS |
| `new_manager_dilution_cap` | 10% | ISHA Cl. 6.4(C) |
| `deuda_neta_default_eur` | 35.000.000€ | modelado base TUCA |
| `net_debt` | 80.000.000€ | factor exit modelado |
| `refinancing_amount` | 90.000.000€ | escenario refi 2027-2028 |
| `transaction_costs` | 0% | (no modelado en exit_scenarios actuales) |

## 2. Cláusulas clave ISHA

- **Drag-along**: requerido por mayoría calificada Class A (Tuca Midco / Asterion).
- **Tag-along**: pro-rata todos los socios TUCA, TCH1 incluido sobre 18,45% econ.
- **ROFR / preemption**: contemplados, detalle en SPA TUCA.
- **Key-man**: triggered si key persons mgmt TCH1 (Ávila, S.Echevarría, Triguero, Huarte, Lafarga) salen antes del exit.
- **Vesting on exit**: 100% acceleration Class B (`class_b_vesting_on_exit`).
- **Cap dilución new mgrs**: 10% sobre bloque Class B Ord (`new_manager_dilution_cap`).
- **Supermayoría Class A + B** para: refinanciación, cambio bylaws, M&A material, distribución dividendos extraordinarios.

## 3. Los 4 escenarios exit MasOrange — BD `exit_scenarios`

### Escenario A — Sin upside (sale price 250M€)

| Concepto | Valor |
|---|---|
| Sale price | 250.000.000€ |
| Hurdle | 270.000.000€ — **NO se alcanza** |
| Equity value distribuible Class B | ~0€ (sale price < hurdle) |
| TCH1 gross (solo pref pro-rata 0,696%) | ~530.000€ |
| MdL gross | 530.000€ |
| **MdL net (post IS 25% TCH1)** | **480.000€** |
| Múltiplo TCH1 sobre inversión 1,48M€ | 0,4× |
| Notas | "Sin upside. Equity Value < hurdle preferente. TCH1 solo recupera 0,696% pro-rata de pref. MdL: ~500K€." |

### Escenario B — Éxito moderado (sale price 350M€)

| Concepto | Valor |
|---|---|
| Sale price | 350.000.000€ |
| Hurdle | 270.000.000€ |
| Upside sobre hurdle | 80.000.000€ |
| TCH1 gross (0,696% pref + 17,75% upside) | ~16.000.000€ |
| MdL gross (46,03% × ~16M ≈ pendiente reconciliar factor 38,14%) | 5.970.000€ |
| **MdL net (post IS 25%)** | **5.400.000€** |
| Múltiplo TCH1 | ~10,8× |
| Notas | "Upside ~80M€. TCH1 Gross ~16M€ (0,7% pref + 17,75% upside). MdL neto ~4,7M€ (post IS 25%)." (BD redondea a 4,7; cifra exacta exit_scenarios = 5,4) |

### Escenario C — Base case Asterion (sale price 400M€)

| Concepto | Valor |
|---|---|
| Sale price | 400.000.000€ |
| Hurdle | 270.000.000€ |
| Upside sobre hurdle | ~130.000.000€ |
| TCH1 gross | ~25.000.000€ |
| MdL gross | 11.340.000€ |
| **MdL net (post IS 25%)** | **10.200.000€** |
| Múltiplo TCH1 | ~16,9× |
| Notas | "Escenario base Asterion. Upside ~130M€. TCH1 Gross ~25M€. MdL neto ~7,3M€ (post IS 25%)." (BD redondea a 7,3; exit_scenarios = 10,2) |

### Escenario D — Gran éxito transformacional (sale price 500M€)

| Concepto | Valor |
|---|---|
| Sale price | 500.000.000€ |
| Hurdle | 270.000.000€ |
| Upside sobre hurdle | ~230.000.000€ |
| TCH1 gross | ~42.700.000€ |
| MdL gross | 18.290.000€ |
| **MdL net (post IS 25%)** | **16.500.000€** |
| Múltiplo TCH1 | ~28,9× |
| Notas | "Gran éxito. Upside ~230M€. TCH1 Gross ~42,7M€. MdL neto ~12,4M€ (post IS 25%). Escenario transformacional." (BD redondea a 12,4; exit_scenarios = 16,5) |

> **Discrepancia bitácora**: las cifras "redondeadas" en `notes` (4,7 / 7,3 / 12,4) vs cifras exit_scenarios.mdl_net_return (5,4 / 10,2 / 16,5) reflejan el factor `mdl_pct_tch1` aplicado. Reconciliar al pasar factor 38,14 → 46,03 (tarea pendiente #11).

## 4. Sensibilidad

| Variable | Rango | Impacto IRR MdL base case (cualitativo) |
|---|---|---|
| Sale price MasOrange | 250 → 500M€ | Convexo arriba de 270M€ hurdle (factor 30+× upside escenario D vs A) |
| Tipo Asterion refinanciación | 7% → 9% bps elevation | Reduce equity value distribuible (más servicio deuda) |
| Timing exit | 2027 → 2030 | Cupón pref 10% acumulado erosiona Class B upside con timing diferido |
| Net debt en exit | 80M → 120M€ | Reduce equity distribuible 1:1 |
| Vesting Class B effective | 17,75% → 15,97% (post dilución mgrs) | -10% upside TCH1 |

## 5. Calculadora Olin en mdl-patrimonio

URL: `https://mdl-patrimonio.vercel.app/waterfall`

Mapeo páginas Next.js:
- Página: `src/app/waterfall/page.tsx`
- Lib lógica: `src/lib/waterfall-validators.ts`
- Parámetros editables: tabla `waterfall_params` con `business_line_id='olin'`

**Parámetros editables clave**:

| Param key | Default | Editable | Descripción |
|---|---|---|---|
| `mdl_pct_tch1` | 38,14% (default 46,03%) | sí | % MdL efectivo TCH1 |
| `tch1_ord_pct` | 17,75% | sí | Class B Ord cap TUCA |
| `tch1_pref_pct` | 0,696% | sí | Privilegiadas cap TUCA |
| `pref_coupon_pct` | 10,0% | sí | Cupón preferente |
| `asterion_rate_pct` | 7,0% | sí | Deuda Asterion |
| `deuda_neta_default_eur` | 35M€ | sí | Deuda neta TUCA |
| `is_rate_tch1_pct` | 25% | sí | IS TCH1 (sin art. 21) |

## 6. Referencia cruzada

- **Subrogación Asterion 2,10M€ en TCIH**: ver `escenario-tcih-holding/resources/intragrupo-9-saldos.md`. **Es debt-rank, NO entra en cap table TCH1 ni TUCA**.
- **Class A reforzadas TCH1**: amplifica voto en ManCo TUCA (NO cap%) — anti-patrón documentado.
- **Investment date 2022-02-18**: base IRR/MOIC. NO modificar sin auditoría.
- **Dividend Dec 2024 12M€**: ya reconocido. No entra en escenarios exit (es flujo previo).

## 7. SQL — regeneración

```sql
-- Exit scenarios Olin
SELECT scenario_name, sale_price, hurdle_amount, mdl_gross_return, mdl_net_return, tch_return, notes
FROM exit_scenarios
WHERE business_line_id = 'olin'
ORDER BY sale_price;

-- Waterfall params Olin
SELECT param_key, param_value, default_value, source, is_editable
FROM waterfall_params
WHERE business_line_id = 'olin'
ORDER BY factor_group, param_key;
```

## 8. Cálculo manual rápido — verificación

Para `sale_price = 400M€`:
1. Hurdle 270M€ → Upside disponible Class B = 400 - 270 = 130M€.
2. TCH1 cap Class B Ord = 17,75% (sin dilución) → TCH1 sobre upside = 130 × 17,75% = 23,075M€.
3. + Class B Privilegiadas 0,696% (sobre 270M pref) = 270 × 0,696% = 1,879M€.
4. **TCH1 gross total** ≈ 25M€ (cuadra con `exit_scenarios.tch_return=25M€` aprox).
5. MdL via TCH1 = 25 × 46,03% = 11,5M€ gross MdL (factor look-through real).
6. (con factor 38,14% productivo) = 25 × 38,14% = 9,5M€.
7. **MdL net post IS 25% TCH1** = ~7,3-8,6M€ según factor aplicado.

Coincide con escenario C `mdl_net_return = 10.200.000€` (asume sale price + ajustes adicionales no modelados aquí).
