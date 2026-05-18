# Cap table detallado — Templus (TCH4 → Vesta → Templus CD + TCIH → Templus CD directo)

> Snapshot 31/12/2025 · BD `savenikqhmcuwmcnabca` (`participations` + `shareholders` + `entities`) + ISHA TUCA 11/10/2023 + Enmienda ISHA 11/12/2025 + audit EY IN25-6924 (TCH4) + Pack Miguel 10-may-2026.

## Cadena completa MdL → Templus CD (dos paths simultáneos)

```
mdl-persona (Miguel de Lucas Sánchez)
  │ 100,00% Ordinarias
  ▼
IPN (Inteligencia Procesos de Negocio, SLU)
NIF: B87680328 · Activo 9.097.622€ · PN 5.102.491€
  │
  ├─ 17,00% TCH4 (Class A — MdL pool) — directo
  │
  └─ 100% TCH2 (Ordinarias)
        │
        └─ 15,60% TCH4 (Class A — MdL pool) — indirecto MdL
              │
              ▼
TCH4 (Teras Capital Holding 4, S.L.)
NIF: B56563398 · Activo 3.733.930€ · PN -5.003,93€ · Pasivo 3.738.934€
  │ Cap% MdL en TCH4: 17,00% IPN + 15,60% TCH2 = 32,60% MdL efectivo
  │ Class structure: Class A reforzadas (MdL pool + Indep + LSS) +
  │                  Class A managers (S.Echevarría, Ávila, Huarte)
  │
  │ ▼ 2,00% Class B Investor + Pref Class D (ISHA Cl. 3, 11/10/2023)
  ▼
Vesta Invest S.à r.l. (LUX) — ICG-controlled
Sponsor: ICG (Intermediate Capital Group)
  │ Otros socios Vesta:
  │   • ICG (Class A + Pref) — mayoritario
  │   • TCH4 2,00% (Class B Investor + Pref Class D)
  │ Financing Agreement Vesta 11/12/2025: préstamo Vesta → TCH4 al 8% (loan_financing_pct=70%)
  │
  │ ▼ 96,00% Vesta en Templus CD (Class A)
  ▼
       ┌──────────────────────────────────────────┐
       │  Templus Centros de Datos S.L.U. (CD)    │
       │  NIF: B-56381379                         │
       │  Activo 179.546.855€ · PN 177.174.036€   │
       │  Pasivo 2.372.819€                       │
       │  exclude_from_group_totals=true          │
       │  (evitar doble conteo con Vesta)         │
       └─────┬────────────────────────────────────┘
             │
             │ Otros socios Templus CD:
             │   • Vesta Invest 96,00% (Class A)
             │   • TCIH 2,00% (Class B directo)
             │   • Templus Managers 2,00% (Class C sweet equity)
             │
             │ 100% en 7 filiales operativas España
             │
   ┌─────────┴─────────┬─────────────┬───────────┬───────────┬───────────┬──────────────┐
   ▼                   ▼             ▼           ▼           ▼           ▼              ▼
templus-           templus-       templus-    templus-    templus-    templus-       templus-
madrid             alcala         malaga      spain       barcelona   properties     ceuta

PATH 2 (TCIH directo a Templus CD):

MdL (IPN+TCH2+Monforte+LSS+otros) ──▶ TCIH ──▶ 2,00% Class B directo en Templus CD
                                  (NIF B88279880)
                                  Cap% MdL en TCIH: 25,83% TCH2 + 25,83% MdL_persona = 51,665%
```

## Cap% efectivo MdL en Templus CD (composición agregada)

| Nivel | Cálculo | Cap% MdL |
|---|---|---|
| MdL → IPN | 100% directo (persona física) | 100,00% |
| MdL → TCH2 | 100% IPN × 100% TCH2 | 100,00% |
| MdL → TCH4 directo (vía IPN) | 100% × 17,00% | 17,00% |
| MdL → TCH4 vía TCH2 | 100% × 100% × 15,60% | 15,60% |
| **MdL → TCH4 total efectivo** | 17,00 + 15,60 | **32,60%** |
| MdL → Vesta | 32,60% × 2,00% | 0,652% |
| MdL → Templus CD vía Vesta (Path 1) | 32,60% × 2,00% × 96,00% | **0,626%** |
| MdL → TCIH | (look-through TCIH) | 51,665% |
| MdL → Templus CD vía TCIH directo (Path 2) | 51,665% × 2,00% | **1,033%** |
| **MdL → Templus CD agregado (Path 1 + Path 2)** | 0,626 + 1,033 | **1,62%** |

> **`business_lines.templus.mdl_position_pct=1,62%`** refleja el cap% efectivo agregado MdL en Templus CD por los dos paths simultáneos. Descripción BD: "1,62% efectivo agregado vía dos paths: TCH4 → Vesta → Templus CD (0,626% = 32,6%×2%×96%) + TCIH 2% directo en Templus CD (1,03% = 51,66%×2%). Sin exención art. 21 LIS (<5%)."

## Cap table TCH4 completo (FY 2025, audit EY IN25-6924 + shareholders BD)

| # | Socio | Class | Cap% | Partner Group | cc_balance (€) |
|---|---|---|---|---|---|
| 1 | Jorge Monforte (MCT) | Class A | **26,00%** | MCT (mayor individual) | 794.980 |
| 2 | IPN | Class A | 17,00% | MdL | 421.717 |
| 3 | TCH2 | Class A | 15,60% | MdL | 481.871 |
| 4 | Enrique Gurrea | Class A | 8,00% | Indep | 198.455 |
| 5 | Moisés Menéndez | Class A | 8,00% | Indep | 216.820 |
| 6 | Santiago Sánchez Echevarría | Class A | 7,00% | Mgmt | 158.108 |
| 7 | Pablo Ávila | Class A | 6,80% | Mgmt | 184.285 |
| 8 | Gonzalo Huarte | Class A | 6,20% | Mgmt | 140.039 |
| 9 | LSSI (Luis Sánchez Salmerón Inversiones) | Class A | 5,40% | LSS | 146.356 |
| 10 | TCIH | Residual | 0,01% | TCIH | 15.264 |
| **TOTAL** | | | **100,01%** | | **~2.758.000** |

Suma 100,01% (rounding 0,01%, despreciable).

**Pool MdL agregado en TCH4**: 32,60% (IPN+TCH2).
**Pool MCT (Monforte)**: 26,00% — mayor individual.
**Pool Indep (Gurrea+Menéndez)**: 16,00%.
**Pool Mgmt (S.Echevarría+Ávila+Huarte)**: 20,00%.
**Pool LSS**: 5,40%.
**Total socios externos a MdL**: 67,40%.

## Cap table Templus CD completo

| Socio | Class | Cap% | Notas |
|---|---|---|---|
| Vesta Invest S.à r.l. | Class A | **96,00%** | ICG-controlled. Vehículo LUX |
| TCIH | Class B (directo) | **2,00%** | Path 2 MdL. Cap% efectivo MdL via TCIH = 1,033% |
| Templus Managers | Class C (sweet equity) | **2,00%** | Sweet equity managers operativos Templus CD |
| **TOTAL** | | **100,00%** | |

## Cap table Vesta Invest (LUX) — composición ICG + TCH4

| Socio | Class | Cap% | Notas |
|---|---|---|---|
| ICG (vía vehículos ICG) | Class A + Pref | mayoritario | Sponsor financiero, control |
| TCH4 | Class B Investor + Pref Class D | **2,00%** | Path 1 MdL en Templus chain |

(Detalle exacto cap table Vesta + composición ICG aguas arriba pendiente confirmar — referencia ISHA 11/10/2023 + Enmienda 11/12/2025.)

## Detalle paquete TCH4 ↔ Vesta — Class B + Class D (ISHA Cl. 3)

- **Class B Ord (25% split)**: TCH4 recibe 25% de cualquier upside Class B sobre activo Templus CD vía Vesta.
- **Class D Pref (75% split)**: TCH4 recibe 75% del split a través de Class D preferentes con cupón 12% anual (Enmienda ISHA 11/12/2025).
- **Splits ord/pref aplicados sobre 2,00% capital TCH4 en Vesta**.
- **MdL ord principal**: 169.413,29€ (`waterfall_params.mdl_total_ord_principal`).
- **MdL pref principal**: 508.239,88€ (`waterfall_params.mdl_total_pref_principal`).
- **MdL total invertido en TCH4**: 677.653,17€ (suma ord + pref).

## Total commit Vesta-ICG y total invested

- **Total commit**: 300.000.000€ (`waterfall_params.total_commit_eur`).
- **Total invested abril 2026 (audit EY IN25-6924)**: 183.934.000€ — 61% del commit desplegado.
- **Loan financing pct**: 70% (Vesta financia 70% del ticket TCH4 vía préstamo subordinado 8%).
- **Vesta loan rate**: 8,00% (`vesta_loan_rate_pct`).

## Verificación SQL

```sql
-- Look-through MdL en TCH4
SELECT
  parent_entity_id, child_entity_id, ownership_pct, share_class, notes
FROM participations
WHERE child_entity_id = 'tch4';

-- Cap table TCH4
SELECT shareholder_name, share_class, ownership_pct, partner_group, cc_balance
FROM shareholders
WHERE entity_id = 'tch4'
ORDER BY ownership_pct DESC;

-- Cap table Templus CD
SELECT shareholder_name, share_class, ownership_pct
FROM shareholders
WHERE entity_id = 'templus-cd'
ORDER BY ownership_pct DESC;

-- Cap table Vesta Invest
SELECT shareholder_name, share_class, ownership_pct
FROM shareholders
WHERE entity_id = 'vesta'
ORDER BY ownership_pct DESC;

-- Participations Templus CD → 7 filiales España
SELECT child_entity_id, ownership_pct, share_class
FROM participations
WHERE parent_entity_id = 'templus-cd'
ORDER BY ownership_pct DESC;

-- Factor waterfall MdL en TCH4
SELECT param_key, param_value, default_value, source
FROM waterfall_params
WHERE business_line_id = 'templus' AND param_key LIKE '%pct%';
```

## Discrepancias documentadas

- **TCH4 PN técnicamente negativo (-5.003,93€)**: PN cae por debajo de cero por costes acumulados Templus operativos sin distribución dividendos Vesta aún. Dependencia de servicio Vesta para sanear. No es causa disolución técnica art. 363.1.e LSC si Vesta sirve dividendos.
- **TCIH 0,01% en TCH4**: participación residual (referencia BD `shareholders`). No relevante en cap table efectivo.
- **`templus-cd.exclude_from_group_totals=true`**: por doble conteo con Vesta. Documentado en `decisiones-clave.md` §6.
- **`global-cabria.exclude_from_group_totals=true`**: legacy DUPLICADO de Templus CD. NO usar como entidad activa.

## Cadena look-through completa MdL → Templus CD detalle

**Path 1 (vía TCH4 → Vesta → Templus CD)**:
- MdL persona → IPN: 100%
- IPN → TCH4: 17,00%
- TCH4 → Vesta: 2,00%
- Vesta → Templus CD: 96,00%
- **Combinado**: 100% × 100% × 17,00% × 2,00% × 96,00% = 0,3264% (vía IPN sola)
- Más TCH2 path: 100% × 100% × 15,60% × 2,00% × 96,00% = 0,2995% (vía TCH2)
- **Total Path 1**: 0,3264% + 0,2995% = **~0,626%** (cuadra con BD)

**Path 2 (vía TCIH → Templus CD directo)**:
- MdL → TCIH agregado: 51,665% (composición TCH2 25,83% + MdL_persona 25,83% en TCIH)
- TCIH → Templus CD: 2,00%
- **Total Path 2**: 51,665% × 2,00% = **1,033%**

**Cap% efectivo agregado MdL en Templus CD**: 0,626% + 1,033% = **1,62%** (BD `mdl_position_pct`).
