# Cifras 2025 detalle — Gemswell (TCH3 + Valdorba subgrupo + Quarter/Grand View + SW Infrasports + VSO II)

> Snapshot 31/12/2025 · BD `savenikqhmcuwmcnabca` (`entity_balances`) + audit provisional TCH3 02/04/2026 (B88547567) + parser_fix_bug14 + email Miguel 7-may-2026 (override Quarter/Grand View) + email Stoneweg/Ramón Romero 7-may-2026 (NAV VSO II).

## TCH3 — vehículo de cabecera (FY 2025, post-subsanación)

| Concepto | Valor | Source |
|---|---|---|
| Activo total | 6.109.732,11€ | audit_2026_provisional |
| Patrimonio neto | 304.469,52€ | audit_2026_provisional |
| Capital social | **7.203.820€** | post-subsanación dic-2025 |
| Prima asunción | 1.112.464€ | (557K crédito MPS + 555K dineraria) |
| Resultados anteriores | -8.011.815€ | absorbidos por reorganización |
| Total pasivo | 5.805.262,59€ | mayoría intragrupo (créditos Valdorba no compensados) |
| Bank debt | 0€ | sin deuda bancaria propia |
| Cuenta 17100011 PTMO Telcogestores | 250.000€ | reclasificada pnc_bancario→pnc_otra (fix bug #14, 15-may-2026) |

**Observaciones críticas**:

- PN (304K€) muy inferior a capital social (7.203K€) refleja **pérdidas acumuladas previas absorbidas** en la subsanación dic-2025.
- Pasivo 5,8M€ corresponde a créditos intragrupo del subgrupo Valdorba **pendientes de capitalización futura**.
- Fix bug #14 reclasificó la cuenta 17100011 PTMO TELCOGESTORES (250K€) por ser tercero NO bancario. Aplicado 15-may-2026. Afecta a TCH3 y TCH4.

### SQL regeneración TCH3

```sql
SELECT * FROM entity_balances
WHERE entity_id = (SELECT id FROM entities WHERE short_name = 'TCH3')
  AND fiscal_year = 2025
  AND source IN ('audit_2026_provisional', 'parser_fix_bug14')
ORDER BY recorded_at DESC LIMIT 5;
```

## Subgrupo Valdorba (FY 2025)

### Valdorba Parques (cabecera, 88% TCH3)

| Concepto | Valor |
|---|---|
| Activo total | 4,67M€ |
| Patrimonio neto | 3,97M€ |
| Total pasivo | 0,70M€ |
| Source | entity_balances |

Cabecera holding del subgrupo operativo. Cuelga 88% de TCH3 con 12% a otros socios (cap table 12% pendiente detalle en BD).

### Valdorba Metropolitano (VM, 100% Valdorba Parques)

| Concepto | Valor | Notas |
|---|---|---|
| Activo total | 4,4M€ | |
| Patrimonio neto | 1,84M€ | |
| Total pasivo | 2,56M€ | |
| **Ingresos** | **2M€** | **Surf park operativo** |

**Observación**: VM es la única entidad del subgrupo Valdorba con ingresos operativos significativos a 31/12/2025. Surf park urbano en ramp-up.

Saldos intragrupo VM:
- Kelpa Expansión: derecho de crédito (cuenta 17100011 PTMO TELCOGESTORES 250K€ reclasificada pnc_otra).

### Valdorba Parques Surf (VPS, 100% Valdorba Parques)

| Concepto | Valor | Notas |
|---|---|---|
| Activo total | 4,05M€ | |
| Patrimonio neto | 4,01M€ | |
| Capital social | 4,03M€ | |
| Total pasivo | 0,04M€ | Casi cero — vehículo en desarrollo |

**Observación**: VPS es el vehículo del proyecto surf park resort. Sin ingresos operativos relevantes en 2025 (fase desarrollo). Cierre operativo proyectado Q3-Q4 2026.

### Valdorba Parques Surfhotel (VPSH, 100% Valdorba Parques)

| Concepto | Valor | Notas |
|---|---|---|
| Activo total | 170€ | SPV en latencia |
| Patrimonio neto | -820€ | Negativo — sin actividad efectiva |
| Total pasivo | 990€ | residual |

**Observación**: VPSH es SPV asociado al surf park resort (hotel adjunto). Sin actividad operativa a 31/12/2025. Activación pendiente arranque VPS Q3-Q4 2026.

### Madrid Playa Surf (MPS) — 10,31% vía VM

- Cifras BD MdL no disponibles directamente (entidad participada minoritaria de VM).
- `mdl_effective_pct` 4,25% (41,24% × 10,31%).
- Proyecto surf park pipeline Madrid (en desarrollo).

## SW Infrasports (50% TCH3)

- Cifras BD MdL no disponibles a 31/12/2025 (sociedad gestora paraguas — FY pendiente confirmar).
- Fee anual fijo 250.000€ (`swi_fixed_fee_eur`).
- Promote 50% sobre carry compartimentos (`tch3_promote_pct_swi`).

## VSO II — compartimento Wave Park (vehiculado vía SW Infrasports)

| Concepto | Valor | Source |
|---|---|---|
| Crédito face value | 1.000.000€ | Acuerdo TCH3 con compartimento Wave Park |
| NAV no auditado 31/12/2025 | **124,48%** | email Stoneweg/Ramón Romero 7-may-2026 |
| Fair value derivado | 1.244.800€ | calculado 1.000.000 × 1,2448 |

**Observaciones**:

- Es el único compartimento de SW Infrasports con valoración registrada a 31/12/2025.
- NAV 124,48% indica una sobrevaloración del 24,48% sobre el face value tras evolución del proyecto Wave Park.
- Fuente única: email Stoneweg / Ramón Romero del 07-may-2026. No extrapolar variaciones sin email/comunicación posterior.

## Cadena Quarter Capital → Grand View La Quinta (capitalizada en TCH3 dic-2025)

### Quarter Capital, S.L.

| Concepto | Valor | Source |
|---|---|---|
| Activo total | 3.965.846€ | override email Miguel 7-may-2026 |
| Patrimonio neto | 3.298.655€ | override email Miguel 7-may-2026 |
| Total pasivo | 667.191€ | override email Miguel 7-may-2026 |
| Cap% IPN | 32,29% | cap table real (no 33,33% por redondeo) |

### Grand View La Quinta, S.L.

| Concepto | Valor | Source |
|---|---|---|
| Activo total | 4.391.565€ | override email Miguel 7-may-2026 |
| Patrimonio neto | 3.340.062€ | override email Miguel 7-may-2026 |
| Total pasivo | 1.051.503€ | override email Miguel 7-may-2026 |
| Cap% Quarter Capital | 100% | |
| Naturaleza | Inversiones inmobiliarias Marbella | email Miguel |
| Mayores 2018-2025 | Cuentas 25200x + 5510x — enviados a contable García Ruiz, pendientes procesar | email Miguel |

### Saldo intragrupo Grand View → IPN

| Concepto | Valor |
|---|---|
| Cuenta | 17100002 PTMO GRAND VIEW LA QUINTA |
| IPN acreedor por | 1.519.092,12€ |
| Naturaleza | loan_lp |

**Decisión doctrinal**:

> "Todo esto se ha capitalizado en el aumento de capital TCH3 y nunca era una posición de TCIH" — Miguel de Lucas, email 7-may-2026.

Para perímetro Gemswell consolidado: se incluye Quarter Capital + Grand View La Quinta.
Para participations strictu sensu (BD `participations`): cuelgan de IPN directo, no de TCH3.

## Cifras consolidadas Gemswell — vista agregada (estimación)

| Entidad | Activo | PN | Pasivo | Cap% MdL look-through |
|---|---|---|---|---|
| TCH3 | 6,11M€ | 0,30M€ | 5,81M€ | 46,86% |
| Valdorba Parques | 4,67M€ | 3,97M€ | 0,70M€ | 41,24% |
| VM (operativo, ingresos 2M€) | 4,40M€ | 1,84M€ | 2,56M€ | 41,24% |
| VPS | 4,05M€ | 4,01M€ | 0,04M€ | 41,24% |
| VPSH | 0,00M€ | -0,00M€ | 0,00M€ | 41,24% |
| Quarter Capital | 3,97M€ | 3,30M€ | 0,67M€ | 32,29% (vía IPN) |
| Grand View | 4,39M€ | 3,34M€ | 1,05M€ | 32,29% (vía IPN) |
| **VSO II (fair value crédito)** | **1,24M€** | — | — | 23,44% (vía SWI) |

> Esta tabla es **suma simple** de balances (no consolidación contable formal). Hay solapamientos intragrupo que se eliminarían en consolidación NIC 27 (saldos cruzados, créditos intragrupo, etc.).

## SQL regeneración subgrupo Valdorba

```sql
SELECT e.short_name, eb.total_assets, eb.net_equity, eb.total_liabilities, eb.fiscal_year, eb.source
FROM entity_balances eb
JOIN entities e ON e.id = eb.entity_id
WHERE e.short_name IN ('VALDORBA-PARQUES', 'VM', 'VPS', 'VPSH', 'TCH3', 'QC', 'GRAND-VIEW')
  AND eb.fiscal_year = 2025
ORDER BY e.short_name, eb.recorded_at DESC;
```

## Cifras top-line MasOrange / mercado surf

Métricas de mercado / sectoriales (uso surf parks, plazas hoteleras, etc.) no se almacenan en BD MdL (es mercado subyacente, no entidad consolidada). Cifras de ramp-up VM disponibles vía steerco trimestral.

## Validación cifras — pendientes

- Confirmar NIF formal TCH3 (BD `entities.tch3.nif` pendiente).
- Cierre formal Quarter Capital + Grand View 2025: García Ruiz procesa mayores cuentas 25200x + 5510x (mayores 2018-2025 enviados).
- Audit definitivo TCH3 2025 (post audit provisional 02/04/2026).
- NAV VSO II actualizado periódicamente (próxima comunicación Stoneweg).
- SW Infrasports balance FY 2025 (sociedad gestora — pendiente).
