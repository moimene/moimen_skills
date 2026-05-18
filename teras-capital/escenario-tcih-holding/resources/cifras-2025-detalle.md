# Cifras 2025 detalle — TCIH

> Snapshot 31/12/2025 · BD `entity_balances.tcih` (source: `audit_2026_provisional + parser_fix_bug14`). Mayor PGC TCIH 2025 (7.428 asientos, 356 cuentas).

## Balance TCIH — FY 2025

| Concepto | Valor (€) | Detalle / cuentas mayor |
|---|---|---|
| **ACTIVO** | | |
| Activo total | 7.993.932,32 | |
| Caja | 109.069,96 | grupo 57 |
| Activo no corriente | 3.252.154,56 | |
| Activo corriente (sin caja) | 8.157.848,10 | |
| **PATRIMONIO NETO** | | |
| Total equity (contable) | **-2.441.138,31** | NEGATIVO |
| Capital social (BD) | 20.000,00 | Capital EFECTIVO (acordeón sep-22) |
|   ├ Capital inscrito RM | 3.099,00 | cuenta 100 |
|   └ AK pendiente inscripción | 16.901,00 | cuenta 55100008 (figura formalmente como acreedor hasta inscripción) |
| Reservas | 366.999,16 | |
| Resultados anteriores | 0,00 | |
| Resultado pendiente regularizar | -511.133,00 | Resultado 2025 |
| Aportaciones socios | 0,00 | |
| **Shareholder loans as equity (override)** | **7.666.559,00** | Override `audit_2026_provisional` — equity-rank 4 socios MdL |
| **PN ajustado (post equity-rank)** | **+5.225.420,69** | -2.441.138,31 + 7.666.559,00 |
| **PASIVO** | | |
| Total pasivo | 10.435.070,63 | |
| Pasivo no corriente bancario | 0,00 | (fix bug #14: 17100008 sale de aquí) |
| Pasivo no corriente otra | 1.802.438,86 | **Asterion deuda externa real** (cuenta 17100008) |
| Pasivo no corriente vinculadas | 0,00 | |
| Pasivo corriente bancario | 14.171,17 | **bank_debt real** — 12 VISA CAIXABANK + AMEX (cuentas 520xxxxx) |
| Pasivo corriente vinculadas | 0,00 | |
| Pasivo corriente comercial | 5.854,48 | |
| Pasivo corriente HP/SS | 130.345,14 | |
| Pasivo corriente otras | 4.817.297,81 | (incluye 521 PTMO PARTICIPATIVO + 5510x C/C socios + dividendo a cta) |
| Bank debt real | **14.171,17** | Solo tarjetas crédito |
| Other intragroup debt | **2.101.899** | Subrogación Asterion clase B (debt-rank, NO equity) |
| **P&L** | | |
| Ingresos | 1.674.208,05 | Fees advisory: Templus + Tuca/Olin + Gemswell + Mundo Pacífico + Pacífico Cable cliente activo 207K |
| Gastos | 2.185.341,05 | |
| Net result 2025 | -511.133,00 | |
| Descuadre balance | 0,00 | ✓ Cuadra A = PN + P (post override) |
| Flag descuadre | false | ✓ |
| Flag no clasificado | false | ✓ |
| Source override | `audit_2026_provisional + parser_fix_bug14` | |

## Reconciliación PN contable → PN ajustado

```
PN contable (BD `total_equity`)                    -2.441.138,31€
+ Shareholder loans as equity (override auditor)   +7.666.559,00€
─────────────────────────────────────────────────────────────────
PN ajustado                                        +5.225.420,69€
─────────────────────────────────────────────────────────────────

Capital efectivo (acordeón):                          20.000,00€
PN ajustado / Capital efectivo:                       261× ✓ (>> 1/2)
Conclusión: causa disolución art. 363.1.e LSC SALVADA
```

## Composición intragrupo (vista TCIH)

### TCIH es DEUDORA de:

| Contraparte | Importe (€) | Cuenta mayor | Naturaleza |
|---|---|---|---|
| TCH2 (PTMO PARTICIPATIVO) | 4.000.000 | 52100001 | Equity-rank (override) |
| Monforte (PTMO PARTICIPATIVO) | 690.000 | 52100005 | Equity-rank (override) |
| Gurrea (PTMO PARTICIPATIVO) | 200.000 | 52100008 | Debt-rank (parte subrogación) |
| IPN (C/C) | 1.140.452 | 55100002 | Equity-rank (override) |
| TCH2 (C/C) | 593.895 + 606.408 PROYECTO TUCA = 1.200.303 | 55100004 + 55100010 | Equity-rank (594K) + Operativo TUCA (606K) |
| Monforte (C/C) | 1.000.727 | 55100006 | Equity-rank (override) |
| LSS (C/C) | 241.485 | 55100001 | Equity-rank (override) |
| Gurrea (C/C) | 340.787 | 55100005 | Debt-rank (parte subrogación) |
| Menéndez (C/C) | 315.787 | 55100007 | Debt-rank (parte subrogación) |
| AK Pdte Inscripción (acordeón) | 16.901 | 55100008 | Capital efectivo no inscrito RM |
| Asterion (deuda externa) | 1.802.439 | 17100008 | Externo (pnc_otra) |
| **Subtotal pasivos socios + Asterion** | **~12.580.000** | | |

### TCIH es ACREEDORA de:

| Contraparte | Importe (€) | Cuenta mayor | Naturaleza |
|---|---|---|---|
| TCH1 (C/C) | 4.430.680 | 55240006 | Activo intercompany (PROYECTO TUCA) |
| TCH1 (Crédito LP) | 1.444.806 | 24230001 | Activo financiero LP |
| TCH3 (C/C deudor) | 8.110 | 55240004 | Residual |
| TCS (C/C deudor) | 26.699 | 55240002 | Residual |
| TCH TRES (cliente facturación) | 114.345 | 43000016 | Cliente comercial |
| Pacífico Cable (cliente facturación 2025) | 19.043 | 43000003 | Cliente activo (~207K facturado 2025) |
| Dividendo a Cuenta (CTA) | 2.300.103 | 557 | Activo derechos sobre socios — CAUSA PN NEGATIVO |
| **Subtotal activos intercompany + dividendo** | **~8.343.786** | | |

## Cuenta 557 — dividendo a cuenta 2,3M€

- **Origen**: distribución dividendo a cuenta 2021 tras desinversión Pacífico Cable.
- **Naturaleza**: devolución aportaciones socios + dividendo a cuenta combinado.
- **Por qué genera PN negativo**: el dividendo a cuenta se contabilizó como reducción de fondos propios sin contrapartida en reservas distribuibles suficientes.
- **Estado actual**: pendiente regularización formal vía cuentas anuales (acción recomendada audit punto 6 "Considerar operación de saneamiento patrimonial").
- **Solución alternativa**: la reclasificación equity-rank 7,67M€ ya ajusta PN a +5,22M€, suavizando el efecto del dividendo a cuenta.

## Snapshot histórico 2018-2026

Tabla `entity_balances_history` con snapshots TCIH disponibles (consulta SQL al final). Resumen movimientos críticos:

- **2018-2021**: TCIH opera con TCS Pacífico Cable. PN razonable.
- **Dic 2021**: desinversión Pacífico Cable, distribución dividendo a cuenta 2,3M€.
- **2022**: operación acordeón sep-22, entrada nuevos socios, PN sigue negativo por dividendo a cta.
- **2023-2025**: TCIH genera fees advisory, intenta sanear; PN mejora ligeramente pero sigue negativo.
- **2026**: auditoría provisional 02/04/2026 hace override equity-rank → PN ajustado positivo +5,22M€.

## Exposición total TCIH al grupo (capa por capa)

Según auditoría 30/03/2026 resumen ejecutivo:

```
CAPA 1 — Préstamos participativos (grupo 521)         4.890.000€
  52100001 TCH DOS:     4.000.000€
  52100005 Monforte:      690.000€
  52100008 Gurrea:        200.000€

CAPA 2 — Cuentas corrientes socios (grupo 5510x)      3.633.131€
  55100001 LSS:           241.485€
  55100002 IPN:         1.140.452€
  55100004 TCH DOS:       593.895€
  55100005 Gurrea:        340.787€
  55100006 Monforte:    1.000.727€
  55100007 Menéndez:      315.787€

CAPA 3 — Intercompany (552 + otros)                   5.910.295€ (deudor)
  55240006 TCH UNO:     4.430.680€
  24230001 Cdto TCH UNO: 1.444.806€
  55240004 TCH TRES:        8.110€
  55240002 TCS:            26.699€

CAPA 4 — Financiación externa                         1.802.439€
  17100008 Asterion:    1.802.439€

EXPOSICIÓN TOTAL TCIH a grupo/socios:                ~14.500.000€
```

## SQL — extracción cifras vivas

```sql
-- Balance TCIH 2025
SELECT *
FROM entity_balances
WHERE entity_id = 'tcih' AND fiscal_year = 2025;

-- Reconciliación PN
SELECT
  entity_id,
  fiscal_year,
  total_equity AS pn_contable,
  shareholder_loans_as_equity AS equity_rank_override,
  total_equity + shareholder_loans_as_equity AS pn_ajustado,
  capital_social AS capital_efectivo,
  ROUND((total_equity + shareholder_loans_as_equity) / NULLIF(capital_social, 0), 2) AS pn_ajustado_vs_capital
FROM entity_balances
WHERE entity_id = 'tcih' AND fiscal_year = 2025;

-- Histórico TCIH
SELECT fiscal_year, total_assets, total_equity, shareholder_loans_as_equity,
       (total_equity + COALESCE(shareholder_loans_as_equity, 0)) AS pn_ajustado, source
FROM entity_balances
WHERE entity_id = 'tcih'
ORDER BY fiscal_year DESC;

-- Saldos intragrupo TCIH (5 saldos donde participa)
SELECT from_entity_id, to_entity_id, amount, balance_type, accounts_from, accounts_to, crosses_categories, notes
FROM intragroup_balances
WHERE from_entity_id = 'tcih' OR to_entity_id = 'tcih'
ORDER BY amount DESC;

-- Overrides aplicados
SELECT table_name, row_key, field_name, old_value, new_value, source, reason, applied_at
FROM data_overrides
WHERE row_key::text LIKE '%tcih%'
ORDER BY applied_at DESC;
```

## Métricas derivadas

| Métrica | Valor | Notas |
|---|---|---|
| Total activos / total pasivos | 0,77× | Activo < pasivo, refleja PN negativo contable |
| Total activos / (pasivos - equity-rank override) | 2,95× | Tras override, ratio sano |
| Bank debt / activos | 0,18% | Despreciable — son tarjetas |
| Asterion / activos | 22,5% | Material |
| Equity-rank / activos | 95,9% | Casi la totalidad del activo está financiada por socios MdL en equity-rank |
| Cash / pasivo corriente | 2,18% | Liquidez ajustada |
| Ingresos 2025 / activo total | 20,9% | Fees recurrentes razonables sobre balance |
