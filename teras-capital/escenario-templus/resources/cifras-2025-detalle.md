# Cifras 2025 detalle — Templus

> Snapshot 31/12/2025 · Vista canónica `v_entity_balances_canonical` BD `savenikqhmcuwmcnabca`. TCH4 = `mayor_pgc + audit EY IN25-6924` (abril 2026); Templus CD + 7 filiales España + 4 Roosevelt = `audit_2026_provisional` (Pack Miguel 10-may-2026: Balance Consolidado 2025 + P&L by Site + Colorado Mgmt Accounts).

## TCH4 — Teras Capital Holding 4, S.L. (FY 2025)

| Concepto | Valor (€) | Detalle |
|---|---|---|
| Activo total | 3.733.930 | mayor PGC + audit EY IN25-6924 |
| Patrimonio neto | **-5.003,93** | **Técnicamente negativo** — entidad de paso, depende de servicio Vesta |
| Capital social | 3.000 | RM |
| Reservas | 0 | |
| Resultados anteriores | 0 | (ajustado por bug parser #14) |
| Total pasivo | 3.738.934 | |
| Cuenta 17100000 PTMO VESTA INVEST | 976.756,13 | **Reclasificado `pnc_otra`** (fix bug #14, mayo 2026) |
| Bank debt | 0 | Sin deuda bancaria propia |
| Pasivo NC bancario (pnc_bancario) | 0 | (post-fix bug #14, antes erróneamente incluía 976.756€ Vesta) |
| Pasivo NC otra | 976.756,13 + intragrupo | Incluye Vesta + otros |
| Ingresos | mínimos | |
| Gastos | mínimos | (intereses Vesta deducibles 8% × 976.756 ≈ 78K€) |
| Source | `mayor_pgc + parser_fix_bug14 + audit_EY_IN25_6924` | |
| Notes | "Fix bug #14 cuenta 17100000 PTMO VESTA INVEST S.A.R.L. (976.756,13€) reclasificada de pnc_bancario a pnc_otra. Vesta es sponsor ICG externo, no banco; préstamo al 8% es vehículo equity-rank socio según ISHA (escudo fiscal único de TCH4, sin exención art. 21 LIS porque 2% < 5% participación en Templus CD)." | |

> PN técnicamente negativo (-5.003,93€): TCH4 entidad de paso con saldos intragrupo importantes y costes acumulados (auditoría EY + intereses Vesta) sin distribución dividendos Vesta aún. NO es causa disolución técnica art. 363.1.e LSC dado que aportaciones equity-rank de los socios cubren el ratio si se documentan correctamente.

## Templus CD — Templus Centros de Datos S.L.U. (FY 2025)

| Concepto | Valor (€) | Detalle |
|---|---|---|
| Activo total | 179.546.855 | audit_2026_provisional |
| Patrimonio neto | 177.174.036 | Sólido (98,7% del activo) |
| Total pasivo | 2.372.819 | |
| Inversión cartera (epígrafe 2403) | 169.900.000 | 100% en 7 filiales España + AE HoldCo II (Project Colorado) |
| Caja | 9.670.000 | |
| Provisiones LP | 1.900.000 | |
| Ajustes IS | 451.000 | |
| Bank debt | 0 | Sin deuda bancaria propia (la deuda 23,6M€ está en filial Templus Madrid) |
| Source | `audit_2026_provisional` | |
| `exclude_from_group_totals` | **true** | Evitar doble conteo con Vesta |

## 7 filiales operativas España (FY 2025)

### templus-madrid (NIF B56513781) — Data Center Alcalá fase 1

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 99.200.000 | |
| Patrimonio neto | 75.400.000 | |
| Total pasivo | 23.800.000 | |
| **Deuda bancaria** | **23.600.000** | **ÚNICA filial Templus con deuda bancaria** |
| Inmovilizado | 89.200.000 | DC Alcalá fase 1 operativa |
| Notas | Fase operativa. DC Alcalá fase 1 con build-out completado, fase de comercialización. | |

### templus-alcala (NIF A-79271961) — legacy MAVICO

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 40.600.000 | |
| Patrimonio neto | 38.000.000 | |
| **Resultado 2025** | **+3.200.000** | **ÚNICA filial Templus con beneficio en 2025** |
| Notas | Histórica MAVICO. Operativa, generadora de cashflow. | |

### templus-malaga (NIF B-67676023) — legacy Beta DC

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 3.500.000 | |
| Patrimonio neto | 2.500.000 | |
| Notas | Legacy Beta DC, filial pequeña. Operativa. | |

### templus-spain (NIF B10947703) — Espacio Edge (adq. 25/06/2025)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 22.700.000 | |
| Patrimonio neto | 22.400.000 | |
| **Goodwill** | **20.800.000** | Goodwill por adquisición |
| Notas | **Adquirida 25/06/2025** perímetro AE. Legacy Espacio Edge. Plan 100 días integración Q2 2026. | |

### templus-barcelona (NIF B66472788) — legacy MBA Datacenters

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 8.700.000 | |
| Patrimonio neto | 5.600.000 | |
| Notas | Legacy MBA Datacenters. Operativa. | |

### templus-properties (NIF B22585681) — terrenos Alcalá

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 11.900.000 | |
| Patrimonio neto | 11.000.000 | |
| **Inversiones inmobiliarias** | **9.980.000** | **Terrenos Alcalá NO construidos** — banco de tierra para fases futuras |
| Notas | Vehículo de propiedad inmobiliaria. NO operativo aún. | |

### templus-ceuta (NIF B-13931688) — Waterways Global (constit. 11/06/2025)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 6.300.000 | |
| Patrimonio neto | 4.100.000 | |
| Notas | **Constituida 11/06/2025** (greenfield reciente). Legacy Waterways Global. Build-out previsto Q3 2026. | |

### Total 7 filiales España

| Concepto | Total (€) |
|---|---|
| Activo agregado | ~192.900.000 |
| Patrimonio neto agregado | ~159.000.000 |
| Deuda bancaria agregada | 23.600.000 (toda en Templus Madrid) |
| Beneficio 2025 agregado | +3.200.000 (todo en Templus Alcalá legacy MAVICO) |

## 4 Roosevelt — Project Colorado (FY 2025, Colorado Mgmt Accounts)

### roosevelt-italy

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 24.207.504 | Mayor activo Project Colorado |
| Revenue 2025 | 7.300.000 | Mayor revenue Project Colorado |
| País | Italia | |

### roosevelt-netherlands

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 20.616.130 | |
| Revenue 2025 | — | Sin revenue operativo aún |
| País | Holanda | |

### roosevelt-denmark

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 18.626.624 | |
| Revenue 2025 | 1.700.000 | |
| País | Dinamarca | |

### roosevelt-france

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 13.241.905 | |
| Revenue 2025 | 2.800.000 | |
| País | Francia | |

### Total Project Colorado

| Concepto | Total (€) |
|---|---|
| Activo agregado | ~76.692.163 |
| Revenue 2025 agregado | ~11.800.000 |
| Notas | Vehiculado vía AE Group HoldCo II S.à.r.l. (LUX). Pendiente modelar cadena Vesta → AE HoldCo II → 4 Roosevelt en BD MdL (tarea #9). |

## IPN — vehículo cabecera MdL (FY 2025, contexto)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 9.097.621,57 | |
| Patrimonio neto | 5.102.490,99 | |
| Capital social | 3.000 | |
| Reservas | 5.038.575,30 | |
| Cap% IPN en TCH4 | 17,00% | Class A — MdL pool |
| Source | `mayor_pgc + parser_fix_bug14` | |

## TCH2 — vehículo holding patrimonial MdL (FY 2025, contexto)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 5.245.462,16 | |
| Patrimonio neto | 1.478.613,00 | |
| Capital social | 3.000 | |
| Reservas | 1.475.613,00 | |
| Total pasivo | 3.766.849,16 | |
| Bank debt | 0 | |
| Cap% TCH2 en TCH4 | 15,60% | Class A — MdL pool |

> TCH2 movs 2026 NO consolidan (año fiscal referencia 31/12/2025).

## Saldos intragrupo relevantes Templus

`intragroup_balances` filtrados a 31/12/2025:

| From | To | Amount (€) | Type | Notas |
|---|---|---|---|---|
| Vesta | TCH4 | 976.756,13 | loan_lp (8%) | Cuenta 17100000 PTMO VESTA. Fix bug #14: reclasificado `pnc_otra` (NO bancario) |
| TCH4 | Vesta | (commit ticket) | participation | 2,00% Class B Investor + Pref Class D en Vesta |
| TCIH | Templus CD | (cap inversión) | participation | 2,00% Class B directo Path 2 |

## Cifras Vesta Invest (pendiente)

Vesta Invest S.à r.l. (LUX) cifras 2025 pendientes hasta cierre auditoría LU + reporting ICG. Snapshot abril 2026 (EY IN25-6924) muestra total invested 183.934.000€ desplegados de 300.000.000€ commit.

## Overrides bitacorados Templus

```sql
SELECT table_name, row_key, field_name, old_value, new_value, source, reason, applied_at
FROM data_overrides
WHERE row_key::text LIKE '%templus%' OR row_key::text LIKE '%tch4%' OR row_key::text LIKE '%vesta%' OR row_key::text LIKE '%roosevelt%'
ORDER BY applied_at DESC;
```

### Override principal: TCH4 cuenta 17100000 (fix bug #14)

- `table_name`: `entity_balances`
- `row_key`: `{entity_id: 'tch4', fiscal_year: 2025}`
- `field_name`: `notes / pnc_bancario / pnc_otra`
- `old_value`: cuenta 17100000 clasificada como `pnc_bancario` 976.756,13€
- `new_value`: cuenta 17100000 reclasificada como `pnc_otra` 976.756,13€
- `source`: `parser_fix_bug14`
- `reason`: "Vesta Invest S.à r.l. es sponsor ICG externo (no banco). Préstamo 8% es vehículo equity-rank socio según ISHA. Reclasificación de pnc_bancario a pnc_otra. Escudo fiscal único de TCH4 (intereses deducibles), sin exención art. 21 LIS porque cap% MdL en Templus CD <5%."
- `applied_at`: mayo 2026.

## SQL de regeneración

```sql
-- TCH4 + Templus CD + 7 filiales España + 4 Roosevelt balances 2025
SELECT entity_id, fiscal_year, total_assets, total_equity, total_liabilities, bank_debt, source, notes
FROM v_entity_balances_canonical
WHERE entity_id IN (
  'tch4','templus-cd',
  'templus-madrid','templus-alcala','templus-malaga','templus-spain','templus-barcelona','templus-properties','templus-ceuta',
  'roosevelt-italy','roosevelt-netherlands','roosevelt-denmark','roosevelt-france',
  'ae-holdco-ii','vesta'
)
ORDER BY entity_id, fiscal_year DESC;

-- Saldos intragrupo Templus
SELECT * FROM intragroup_balances
WHERE from_entity_id IN ('tch4','tcih','templus-cd','vesta')
   OR to_entity_id IN ('tch4','vesta','templus-cd','ae-holdco-ii');

-- Factor waterfall Templus actual
SELECT param_key, param_value, default_value, source, is_editable
FROM waterfall_params
WHERE business_line_id = 'templus'
ORDER BY factor_group, param_key;

-- Override fix bug #14 TCH4
SELECT * FROM data_overrides
WHERE row_key::text LIKE '%tch4%' AND field_name LIKE '%pnc%'
ORDER BY applied_at DESC;
```
