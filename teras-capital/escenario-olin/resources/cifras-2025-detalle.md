# Cifras 2025 detalle — Olin

> Snapshot 31/12/2025 · Vista canónica `v_entity_balances_canonical` BD `savenikqhmcuwmcnabca`. TCH1 = `mayor_pgc`; TUCA = audit 2024 (último FY auditado disponible).

## TCH1 — TCH Uno Holding & Management, S.L. (FY 2025)

| Concepto | Valor (€) | Detalle |
|---|---|---|
| Activo total | 4.080.441,01 | mayor PGC |
| Patrimonio neto | 379,27 | residual — entidad de paso |
| Capital social | 3.000,00 | RM |
| Reservas | 0,00 | |
| Resultados anteriores | -2.620,73 | |
| Resultado pendiente regularizar | 0,00 | |
| Aportaciones socios | 0,00 | |
| Shareholder loans as equity | 0,00 | |
| Total pasivo | 4.080.061,74 | |
| Bank debt | 0,00 | sin deuda bancaria propia |
| Pasivo NC bancario (pnc_bancario) | 0,00 | |
| Pasivo NC otra | 0,00 | |
| Pasivo NC vinculadas | 0,00 | |
| Pasivo C bancario | 0,00 | |
| Pasivo C vinculadas | 0,00 | |
| Other intragroup debt | 0,00 | |
| Ingresos | 0,00 | vehículo tenencia, sin operación |
| Gastos | 0,00 | |
| Source | `mayor_pgc` | |
| Frozen | (sin freeze) | |
| Notes | (sin override) | |

> El pasivo de 4M€ refleja principalmente saldos intragrupo con TCIH (`intragroup_balances.tcih→tch1` C/C 4.430.680€ + crédito LP 1.444.806€) y TUCA aguas arriba. Detalle en `escenario-tcih-holding/resources/intragrupo-9-saldos.md`.

## Tuca Bidco SL (FY 2024 audit — último disponible)

| Concepto | Valor (€) |
|---|---|
| Activo total | 405.767.446 |
| Patrimonio neto | 248.552.828 |
| Total pasivo | 157.214.619 |
| Fiscal year | 2024 |
| Entity type | S.à r.l. (Luxemburgo) |

Cifras 2025 TUCA pendientes hasta cierre auditoría (esperado Q2-Q3 2026).

## IPN — vehículo cabecera MdL (FY 2025, contexto)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 9.097.621,57 | |
| Patrimonio neto | 5.102.490,99 | |
| Capital social | 3.000,00 | |
| Reservas | 5.038.575,30 | |
| Ingresos | 77.549,69 | |
| Gastos | 16.634,00 | |
| Source | `mayor_pgc + parser_fix_bug14` | |
| Notes | Fix bug #14 (15-may-2026): cuenta 171xxx (5 préstamos a vinculadas/terceros — Grand View 1.519K, TCH2 566K, Quarter 400K, Ambarvalia 140K, Moises 25K) reclasificada de `pnc_bancario` a `pnc_otra` | |

## TCH2 — vehículo holding patrimonial MdL (FY 2025, contexto)

| Concepto | Valor (€) |
|---|---|
| Activo total | 5.245.462,16 |
| Patrimonio neto | 1.478.613,00 |
| Capital social | 3.000,00 |
| Reservas | 1.475.613,00 |
| Total pasivo | 3.766.849,16 |
| Bank debt | 0,00 |

> TCH2 movs 2026 NO consolidan (año fiscal referencia 31/12/2025).

## Saldos intragrupo relevantes Olin

`intragroup_balances` filtrados a 31/12/2025:

| From | To | Amount (€) | Type | Notas |
|---|---|---|---|---|
| TCIH | TCH1 | 4.430.680 | current_account | 55240006 C/C TCH UNO HOLDING (TCIH activo). Proyecto TUCA. |
| TCIH | TCH1 | 1.444.806 | loan_lp | 243xxxx Crédito LP a TCH UNO (TCIH activo). |
| TCH2 | TCIH | 606.408 | current_account | 55100010 PROYECTO TUCA |
| TCH2 | TCIH | 4.000.000 | participative | 52100001 PTMO PARTICIPATIVO TCH2→TCIH. Composición: 3M Jenkins UNO cedido + 1M cancelación cuenta crédito sep-2022. Hallazgo TCIH-C-02. |

## MasOrange — KPIs operativos (públicos)

> No almacenados en BD MdL (activo subyacente, no entidad TERAS consolidada). Cifras top-line desde MasOrange company report y prensa. Cuando se cite en informe, referenciar fuente externa.

| KPI (referencia 2025) | Valor (rango público) |
|---|---|
| Revenues | ~7-7,5B€ |
| EBITDA | ~2,8-3B€ |
| Subscribers móvil | 32M+ |
| Subscribers fijo | 7M+ |
| Net debt / EBITDA | ~3-4× (pendiente confirmar) |

> Para fuentes auditables: consultar `bl_documents` doc_type='masorange_report' business_line_id='olin'.

## Overrides bitacorados Olin

```sql
SELECT table_name, row_key, field_name, old_value, new_value, source, reason, applied_at
FROM data_overrides
WHERE row_key::text LIKE '%tch1%' OR row_key::text LIKE '%tuca%' OR row_key::text LIKE '%olin%'
ORDER BY applied_at DESC;
```

(Run query para extraer listado vivo — al snapshot 2026-05-18 sin overrides directos sobre TCH1/TUCA; los overrides cruzados están en TCIH por la subrogación Asterion.)

## SQL de regeneración

```sql
-- TCH1 + TUCA balances 2025/2024
SELECT entity_id, fiscal_year, total_assets, total_equity, total_liabilities, bank_debt, source, notes
FROM v_entity_balances_canonical
WHERE entity_id IN ('tch1','tuca')
ORDER BY entity_id, fiscal_year DESC;

-- Saldos intragrupo Olin
SELECT * FROM intragroup_balances
WHERE from_entity_id IN ('tcih','tch1','tch2','tuca') OR to_entity_id IN ('tch1','tuca');

-- Factor waterfall actual
SELECT param_key, param_value, default_value, source, is_editable
FROM waterfall_params
WHERE business_line_id = 'olin'
ORDER BY factor_group, param_key;
```
