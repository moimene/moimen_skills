---
name: escenario-templus
capa: L3b-escenarios
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras, challenge-cognitivo-teras]
triggers: >
  Se activa cuando el usuario menciona Templus, TEMPLUS, Templus CD, Templus Centros
  de Datos, Templus Data Centers, Templus Madrid, Templus Alcala, Templus Málaga,
  Templus Spain, Templus Barcelona, Templus Properties, Templus Ceuta, data centers,
  datacenters, TCH4, Teras Capital Holding 4, Vesta, VESTA, Vesta Invest, ICG,
  Roosevelt, Project Colorado, AE HoldCo II, AE Group HoldCo, Global Cabria,
  IN25-6924, Class B Templus, Class D Templus, Privilegiadas Class D,
  ISHA Vesta, Financing Agreement Vesta, steerco Templus, sponsor ICG,
  cupón Class D, hurdle Templus, refinanciación Vesta.
description: >
  Precarga contexto operativo, contable, legal y fiscal del activo TEMPLUS DATA
  CENTERS (TCH4 → Vesta Invest S.à r.l. → Templus CD → 7 filiales España +
  Project Colorado vía AE Group HoldCo II → 4 Roosevelt). Sponsor financiero ICG
  vía Vesta. MdL participa con cap% efectivo agregado 1,62% en Templus CD por dos
  paths (TCH4 → Vesta → Templus CD 96% Class A + TCIH → Templus CD 2% Class B
  directo). ISHA 11/10/2023 enmendado 11/12/2025: Class B 25% Ord + Class D 75%
  Pref con cupón 12%. SIN exención art. 21 LIS por <5% en Templus CD. Único
  escudo fiscal: intereses préstamo Vesta 8% deducibles a nivel TCH4. 4 escenarios
  exit calibrados con BD savenikqhmcuwmcnabca, hurdle 300M€.
---

# Escenario: Templus

> **Snapshot**: 31/12/2025 — última actualización 2026-05-18 (Claude Code)
> **Fuente principal**: BD Supabase `savenikqhmcuwmcnabca` (`business_lines.templus`, `entities`, `participations`, `shareholders`, `entity_balances`, `exit_scenarios`, `waterfall_params`) + auditoría EY IN25-6924 abril 2026 (TCH4) + ISHA 11/10/2023 + Enmienda ISHA 11/12/2025 + Financing Agreement Vesta 11/12/2025 + Pack Miguel 10-may-2026 (Balance Consolidado 2025 + P&L by Site + Revenues + Budget 2026 + Colorado Mgmt Accounts + org chart v8 14/04/2026).

## 1. Snapshot ejecutivo

Templus es la línea de negocio de TERAS Capital sobre **data centers** (España + Project Colorado pan-europeo), vehiculada a través de **Templus Centros de Datos S.L.U.** (en adelante Templus CD, NIF B-56381379) y **AE Group HoldCo II S.à r.l.** (LUX), financiada por **ICG** vía **Vesta Invest S.à r.l.** (LUX) con compromiso 300M€. MdL participa vía dos paths simultáneos en Templus CD:

- **Path 1 — vía TCH4 → Vesta → Templus CD**: 32,60% MdL en TCH4 × 2% TCH4 en Vesta × 96% Vesta en Templus CD = **0,626% efectivo MdL**.
- **Path 2 — vía TCIH directo en Templus CD**: 51,665% MdL en TCIH × 2% TCIH directo en Templus CD Class B = **1,033% efectivo MdL**.

Cap% efectivo agregado MdL en Templus CD: **1,62%** (BD `business_lines.templus.mdl_position_pct`). Inversión MdL agregada en TCH4: **677.653,17€** (BD `waterfall_params.mdl_total_invested`). Fase: operativo (Templus Madrid Alcalá fase 1 con 89,2M€ inmovilizado + 23,6M€ deuda bancaria) + greenfield Project Colorado (4 Roosevelt, ~76,7M€ activos en IT/NL/DK/FR) + reciente adquisición Templus Spain (Espacio Edge, 25/06/2025, Goodwill 20,8M€) y Templus Ceuta (Waterways Global, constituida 11/06/2025). Hurdle ISHA 300M€ (recuperación pref invested). Escenario base ICG sale price 400M€ devuelve aprox **5,2M€ netos MdL**. Sin exención art. 21 LIS por cap% <5% en Templus CD: único escudo fiscal son los intereses del préstamo Vesta 8% deducibles a nivel TCH4.

## 2. Ficha del activo

| Parámetro | Valor | Fuente |
|---|---|---|
| Línea BD | `business_lines.templus` short_name `TEMPLUS` | BD |
| Sector | Data Centers | BD |
| Sponsor | ICG | BD |
| Status | active | BD |
| Vehículo MdL en cadena (Path 1) | TCH4 (Teras Capital Holding 4, S.L.) NIF B56563398 | BD `entities.tch4` |
| Vehículo intermedio LUX (Path 1) | Vesta Invest S.à r.l. (LUX) — ICG-controlled | BD `entities.vesta` |
| Vehículo intermedio MdL (Path 2) | TCIH (Teras Capital Investment Holding) NIF B88279880 | BD `entities.tcih` |
| Vehículo operativo agregador | Templus Centros de Datos S.L.U. (Templus CD) NIF B-56381379 | BD `entities.templus-cd` |
| Vehículo Project Colorado | AE Group HoldCo II S.à r.l. (LUX) | BD `entities.ae-holdco-ii` |
| Activo subyacente | Data centers España (7 filiales 100%) + Project Colorado (4 Roosevelt 100%) | BD `participations` |
| Fase | Operativo (Madrid/Alcalá fase 1) + greenfield (Spain/Ceuta/Colorado) + expansión M&A | comunicación interna |
| Cap% MdL efectivo en TCH4 | 32,60% (17,00% IPN + 15,60% TCH2) | look-through participations |
| Cap% TCH4 en Vesta Invest | 2,00% Class B Investor | ISHA Cl. 3 (11/10/2023) |
| Cap% Vesta en Templus CD | 96,00% Class A | BD `participations` |
| Cap% TCIH directo en Templus CD | 2,00% Class B | BD `participations` |
| Cap% Templus Managers en Templus CD | 2,00% Class C (sweet equity) | BD `participations` |
| **Cap% efectivo MdL en Templus CD agregado** | **1,62%** (0,626% vía Vesta + 1,033% vía TCIH) | BD `business_lines.templus.mdl_position_pct` |
| Total commit Vesta-ICG | 300.000.000€ | BD `waterfall_params.total_commit_eur` |
| Total invested (referencia abril 2026) | 183.934.000€ | Auditoría EY IN25-6924 TCH4 |
| Total invertido MdL en TCH4 | 677.653,17€ | BD `waterfall_params.mdl_total_invested` |
| MdL ord principal (Class B equivalent en TCH4) | 169.413,29€ | BD `waterfall_params.mdl_total_ord_principal` |
| MdL pref principal (Class D equivalent en TCH4) | 508.239,88€ | BD `waterfall_params.mdl_total_pref_principal` |
| Tranche 1 (15-nov-2023) | 106.652,76€ (26.663,19 ord + 79.989,57 pref) | BD `waterfall_params` |
| Tranche 2 (19-dic-2023) | 417.780,41€ (104.445,10 ord + 313.335,31 pref) | BD `waterfall_params` |
| Tranche 3 (12-jul-2024) | 153.220,00€ (38.305,00 ord + 114.915,00 pref) | BD `waterfall_params` |
| ord_split_pct (Class B) | 25,00% | ISHA Cl. 3 |
| pref_split_pct (Class D) | 75,00% | ISHA Cl. 3 |
| pref_coupon_pct (cupón Class D) | 12,00% | Enmienda ISHA 11/12/2025 |
| vesta_loan_rate_pct | 8,00% | Financing Agreement Vesta 11/12/2025 |
| loan_financing_pct | 70% | BD |
| Hurdle ISHA | 300.000.000€ | BD `exit_scenarios.hurdle_amount` |
| Tipo IS aplicable a TCH4 | **25% — SIN exención art. 21 LIS** (cap% MdL final <5% en Templus CD) | BD `waterfall_params.is_rate_tch4_pct` + LIS |
| TCH4 balance 2025 | Activo 3.733.930€ · PN -5.003,93€ · Pasivo 3.738.934€ | BD `entity_balances.tch4` |
| Templus CD balance 2025 | Activo 179.546.855€ · PN 177.174.036€ · Pasivo 2.372.819€ | BD `entity_balances.templus-cd` |
| Audit firm TCH4 | EY (IN25-6924, abril 2026) | BD `bl_documents` |
| Año fiscal referencia | 31/12/2025 | BD `entities` |
| Flag `exclude_from_group_totals` Templus CD | true (evitar doble conteo con Vesta) | BD `entities.templus-cd` |

## 3. Estructura societaria

Cadena efectiva look-through MdL → Templus CD (dos paths simultáneos):

```
mdl-persona (Miguel de Lucas Sánchez)
  │ 100,00% (Ordinarias)
  ▼
IPN (Inteligencia Procesos de Negocio, SLU) NIF B87680328
  │
  ├─ 17,00% directo TCH4 (Class A — MdL pool)
  │
  ├─ 100% TCH2 ──▶ 15,60% TCH4 (Class A — MdL pool)
  │                       │
  │                       │ Cap% MdL en TCH4 (compuesto):
  │                       │   IPN 17,00% + TCH2 15,60% = 32,60% efectivo MdL
  │                       ▼
  │              TCH4 (Teras Capital Holding 4, S.L.) NIF B56563398
  │              Activo 3,73M€ · PN -5K€ · Pasivo 3,74M€ (entidad de paso, PN técnicamente negativo)
  │              Otros socios TCH4:
  │                • Monforte (MCT) 26,00% (mayor individual)
  │                • Gurrea 8,00% (Indep)
  │                • Menéndez 8,00% (Indep)
  │                • S.Echevarría 7,00% (Mgmt)
  │                • P.Ávila 6,80% (Mgmt)
  │                • G.Huarte 6,20% (Mgmt)
  │                • LSSI 5,40% (LSS)
  │                • TCIH 0,01% (residual)
  │                       │
  │                       │ 2,00% TCH4 en Vesta Invest (Class B Investor + Pref Class D)
  │                       ▼
  │              Vesta Invest S.à r.l. (LUX) — ICG-controlled
  │                       │ 96,00% Vesta en Templus CD (Class A)
  │                       │
  │                       │ Otros socios Templus CD:
  │                       │   • TCIH 2,00% (Class B directo)
  │                       │   • Templus Managers 2,00% (Class C sweet equity)
  │                       ▼
  │              ┌──────────────────────────────────────────┐
  └─▶ TCIH ───▶  │  Templus Centros de Datos S.L.U.        │
      (51,665%   │  NIF B-56381379                          │
       MdL en    │  Activo 179,5M€ · PN 177,2M€ · Pasivo 2,4M€
       TCIH)     │  exclude_from_group_totals=true          │
                 └─────────────────┬────────────────────────┘
                                   │ 100% en 7 filiales operativas España
                                   │
       ┌───────────┬───────────┬───┴───────┬───────────┬───────────┬──────────────┐
       ▼           ▼           ▼           ▼           ▼           ▼              ▼
   templus-    templus-    templus-    templus-    templus-    templus-       templus-
   madrid      alcala      malaga      spain       barcelona   properties     ceuta
   B56513781   A-79271961  B-67676023  B10947703   B66472788   B22585681      B-13931688
   Activo      Activo      Activo      Activo      Activo      Activo         Activo
   99,2M€      40,6M€      3,5M€       22,7M€      8,7M€       11,9M€         6,3M€
   PN 75,4M€   PN 38M€     PN 2,5M€    PN 22,4M€   PN 5,6M€    PN 11M€        PN 4,1M€
   Deuda banc. (Mavico    (Beta DC)   (Espacio    (MBA DCs)   (terrenos     (Waterways
   23,6M€!     legacy)                Edge,                   Alcalá)        Global,
   89,2M€ inm. resultado              adq.                                   constit.
   (DC Alcalá  +3,2M€!                25/06/25,                              11/06/25)
   fase 1)                            Goodwill
                                      20,8M€)

PROJECT COLORADO (rama paralela TCH4 → AE Group HoldCo II → 4 Roosevelt):

   TCH4 ─────────────────────────────────────▶ AE Group HoldCo II S.à.r.l. (LUX)
                                                       │ 100% en 4 Roosevelt filiales
                                                       │
                  ┌────────────────────┬───────────────┴────────────────┬─────────────────┐
                  ▼                    ▼                                ▼                 ▼
              roosevelt-           roosevelt-                       roosevelt-        roosevelt-
              italy                netherlands                      denmark           france
              Activo 24,2M€        Activo 20,6M€                    Activo 18,6M€     Activo 13,2M€
              Revenue 2025         (sin revenue                     Revenue 2025      Revenue 2025
              7,3M€                operativo aún)                   1,7M€             2,8M€
                                Total Project Colorado: ~76,7M€ activos
```

**Cap% efectivo MdL en Templus CD** (agregado dos paths):

- Path 1 (vía Vesta): **0,626%** = 32,60% TCH4 × 2,00% Vesta × 96% Templus CD.
- Path 2 (vía TCIH directo): **1,033%** = 51,665% TCIH × 2,00% directo Templus CD.
- **Total agregado MdL: 1,62%** (suma de los dos paths).

> **CRÍTICO**: el 1,62% es CAP% efectivo (no derechos económicos). Los derechos económicos en el waterfall ISHA Templus dependen de la mecánica Class B (25% Ord) + Class D (75% Pref con cupón 12%) — ver §4 y `resources/waterfall-y-escenarios-isha.md`. Cap% MdL final <5% en Templus CD: **NO aplica exención art. 21 LIS**.

> **CRÍTICO 2**: `Templus CD` tiene `exclude_from_group_totals=true` en BD para evitar doble conteo. Vesta Invest agrega las 7 filiales España + activos Templus CD; sumar también Templus CD directamente generaría sobre-conteo. Ver `resources/decisiones-clave.md` §6.

Detalle completo + tabla cap table TCH4 con los 10 socios en `resources/cap-table-detallado.md`.

## 4. Deal económico

### Compromiso Vesta-ICG (300M€)

- **Total commit**: 300.000.000€ (Financing Agreement 11/12/2025 + ISHA 11/10/2023).
- **Total invested abril 2026 (referencia EY IN25-6924)**: 183.934.000€ desplegados (61% del commit).
- **Loan financing pct**: 70% (Vesta financia a TCH4 70% del ticket de Class B via préstamo subordinado al 8%).
- **vesta_loan_rate_pct**: 8,00% anual (Financing Agreement 11/12/2025) — escudo fiscal único de TCH4.

### Tranches inversión TCH4 en Vesta (Class B + Class D)

| Tranche | Fecha | Total | Class B Ord (25%) | Class D Pref (75%) |
|---|---|---|---|---|
| 1 | 15-nov-2023 | 106.652,76€ | 26.663,19€ | 79.989,57€ |
| 2 | 19-dic-2023 | 417.780,41€ | 104.445,10€ | 313.335,31€ |
| 3 | 12-jul-2024 | 153.220,00€ | 38.305,00€ | 114.915,00€ |
| **MdL agregado** | | **677.653,17€** | **169.413,29€** | **508.239,88€** |

(Cifras BD `waterfall_params.tranche{1,2,3}_amount` y `mdl_total_{ord,pref}_principal`. MdL agregado = TCH4 share 32,60% aplicado a total invested correspondiente).

### Equity y paquetes — estructura ISHA Cl. 3

| Tier | Quién | Cap Vesta | Económico |
|---|---|---|---|
| Class A | Vesta Invest (ICG) | mayoritario | senior pref + control |
| Class B Ord (25% split) | TCH4 + Templus Mgrs | 2,00% TCH4 en Vesta | 25,00% del split económico exit |
| Class D Pref (75% split) | TCH4 + ICG | 2,00% TCH4 en Vesta | 75,00% del split + cupón 12% (Enmienda 11/12/2025) |

**Mecánica Class B vs Class D**:
- Class D (75% Pref) recupera principal invested + cupón preferente 12% anual hasta hurdle 300M€.
- Class B (25% Ord) recibe sweet equity sobre upside una vez recuperado el principal y cupón Class D.
- Class C Templus Managers (2% Templus CD): sweet equity adicional sobre upside Templus operativo (no Vesta).

### Enmienda ISHA 11/12/2025 — cupón Class D 12%

- La enmienda 11/12/2025 fijó el cupón Class D preferente al **12,00% anual** (`waterfall_params.pref_coupon_pct=12, source='Enmienda ISHA 11/12/2025'`).
- Antes de la enmienda, el cupón era inferior (referencia 8-10% según versión ISHA original 11/10/2023, pendiente confirmar histórico exacto).
- Impacto: incrementa significativamente la barrera para que Class B Ord (TCH4 mgrs) capture upside.

### Préstamo Vesta → TCH4 (escudo fiscal único)

- **Cuenta 17100000 PTMO VESTA INVEST S.A.R.L. en TCH4**: 976.756,13€ (saldo 31/12/2025).
- **Tasa**: 8,00% anual (`vesta_loan_rate_pct`).
- **Bug parser corregido #14 (mayo 2026)**: la cuenta 17100000 fue inicialmente clasificada como `pnc_bancario` (deuda bancaria). Correctamente reclasificada a `pnc_otra` (Vesta es sponsor ICG externo, no banco). Ver `resources/decisiones-clave.md` §2.
- **Beneficio fiscal**: los intereses 8% son deducibles en IS TCH4, único escudo fiscal porque cap% MdL final <5% en Templus CD invalida art. 21 LIS.

### ISHA y waterfall — 4 escenarios exit BD (`exit_scenarios`)

| Escenario | Sale Price | MdL Gross | MdL Net (post IS 25%) | Múltiplo |
|---|---|---|---|---|
| Sin upside | 250M€ | 812K€ | **750K€** | ~1,2× |
| Éxito moderado | 350M€ | 3,25M€ | **2,9M€** | ~4,8× |
| Escenario base ICG | 400M€ | 5,812M€ | **5,2M€** | ~8,6× |
| Gran éxito | 500M€ | 10,812M€ | **9,7M€** | ~16× |

> **CRÍTICO**: la diferencia entre "Sin upside" (250M€) y "Gran éxito" (500M€) es de **~13×** en retorno MdL neto. El waterfall Templus es convexo en upside Class B activado solo por encima del hurdle 300M€ + recuperación cupón Class D 12%. Sensibilidad y mecánica completa en `resources/waterfall-y-escenarios-isha.md`.

## 5. Stakeholders

| Actor | Rol | Prioridades | Gestión TERAS |
|---|---|---|---|
| ICG | Sponsor financiero (vía Vesta Invest) | Servicio Class D pref + cupón 12%, hurdle 300M€, exit Templus 5-7 años, Project Colorado roll-out | Reporting trimestral, transparencia, alineamiento en Steerco |
| Vesta Invest (LUX) | Vehicle ICG chain | Governance ISHA, propuestas IC, ejecución plan despliegue | Cooperación + escalado a ICG |
| Templus CD management | Operación 7 data centers España + adquisiciones M&A | Ramp-up Madrid Alcalá fase 1, integración Espacio Edge, build Ceuta | Steerco trimestral, KPIs ARPU/utilización/capex |
| AE Group HoldCo II mgmt | Project Colorado pan-europeo | Build Roosevelt IT/NL/DK/FR, comercialización capacity | Reporting separado a Steerco |
| TCH4 — socios MdL | IPN 17,00% + TCH2 15,60% = 32,60% efectivo MdL | Retorno waterfall, alineamiento Class A/B/C/D, dilución mgrs | Voz coordinada en consejo TCH4 |
| TCH4 — socios independientes | Monforte 26% + Gurrea 8% + Menéndez 8% + LSSI 5,4% = 47,4% | Misma agenda upside | Asambleas TCH4, comités ad-hoc |
| TCH4 — managers (Class A en TCH4) | S.Echevarría 7% + Ávila 6,8% + Huarte 6,2% = 20% | Performance Templus, vesting, payout | Mgmt incentive aligned, comités semestrales |
| Templus Managers (Class C en Templus CD) | 2% sweet equity en Templus CD | Performance operativo Templus, sweet equity | Comités operativos Templus |
| Asesores legales | Cumplimiento ISHA, SPA, M&A, Financing Agreement | CLO super-poder | |
| Asesores fiscales | NRV 19ª, NO art. 21 LIS (cap% <5%), planificación exit | CFO super-poder | |
| Auditor TCH4 + Templus CD | Cierre anual + cifras consolidación | EY (IN25-6924 abril 2026 disponible) | CFO TERAS coordina |

## 6. Cifras 2025

> Snapshot: 31/12/2025. TCH4 = `mayor_pgc` + auditoría EY IN25-6924 abril 2026. Templus CD + 7 filiales España + 4 Roosevelt = `audit_2026_provisional` (Pack Miguel 10-may-2026).

### TCH4 — vehículo MdL en cadena (FY 2025)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 3.733.930 | Mayor PGC + audit EY IN25-6924 |
| Patrimonio neto | -5.003,93 | **Técnicamente negativo** — entidad de paso, depende de servicio Vesta/Templus para sanear |
| Total pasivo | 3.738.934 | Casi todo intragrupo + préstamo Vesta |
| Cuenta 17100000 PTMO VESTA | 976.756,13 | Reclasificado a `pnc_otra` (fix bug #14) — Vesta NO es banco |
| Bank debt | 0 | Sin deuda bancaria propia (Vesta NO es banco) |
| Ingresos / Gastos | 0 / mínimos | Vehículo de tenencia |

### Templus CD — vehículo operativo agregador (FY 2025)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 179.546.855 | audit_2026_provisional |
| Patrimonio neto | 177.174.036 | Sólido (98,7% del activo) |
| Total pasivo | 2.372.819 | |
| Inversión cartera epígrafe 2403 | 169.900.000 | Participaciones en 7 filiales España + AE HoldCo II Project Colorado |
| Caja | 9.670.000 | |
| Provisiones LP | 1.900.000 | |
| Ajustes IS | 451.000 | |
| `exclude_from_group_totals` | **true** | Evitar doble conteo con Vesta |

### 7 filiales operativas España (FY 2025, audit_2026_provisional)

| Entidad | NIF | Legacy | Activo (€) | PN (€) | Notas |
|---|---|---|---|---|---|
| **templus-madrid** | B56513781 | — | 99.200.000 | 75.400.000 | **ÚNICA con deuda bancaria 23,6M€**. Inmovilizado 89,2M€ — DC Alcalá fase 1 operativa |
| **templus-alcala** | A-79271961 | MAVICO | 40.600.000 | 38.000.000 | **ÚNICA con beneficio +3,2M€ 2025**. Histórica MAVICO |
| **templus-malaga** | B-67676023 | Beta DC | 3.500.000 | 2.500.000 | Legacy Beta DC, pequeño |
| **templus-spain** | B10947703 | Espacio Edge | 22.700.000 | 22.400.000 | Goodwill 20,8M€. **Adquirida 25/06/2025** perímetro AE |
| **templus-barcelona** | B66472788 | MBA Datacenters | 8.700.000 | 5.600.000 | Legacy MBA DCs |
| **templus-properties** | B22585681 | — | 11.900.000 | 11.000.000 | Inversiones inmobiliarias 9,98M€ — **terrenos Alcalá NO construidos** |
| **templus-ceuta** | B-13931688 | Waterways Global | 6.300.000 | 4.100.000 | **Constituida 11/06/2025** (greenfield reciente) |
| **TOTAL 7 filiales** | | | **~192.900.000** | **~159.000.000** | |

### 4 Roosevelt — Project Colorado (FY 2025, Colorado Mgmt Accounts)

| Entidad | País | Activo (€) | Revenue 2025 (€) | Notas |
|---|---|---|---|---|
| **roosevelt-italy** | Italia | 24.207.504 | 7.300.000 | Mayor activo + mayor revenue Project Colorado |
| **roosevelt-netherlands** | Holanda | 20.616.130 | — | Sin revenue operativo aún |
| **roosevelt-denmark** | Dinamarca | 18.626.624 | 1.700.000 | |
| **roosevelt-france** | Francia | 13.241.905 | 2.800.000 | |
| **TOTAL Project Colorado** | | **~76.692.163** | **~11.800.000** | |

> Project Colorado: ~76,7M€ activos vehiculados vía AE Group HoldCo II S.à.r.l. (LUX). Tarea pendiente #9 BD MdL: modelar cadena Vesta → AE HoldCo II → 4 Roosevelt (templus-cd 178,5M€ orphan — no enlazado actualmente vía `participations`). Ver `resources/project-colorado-detalle.md`.

### IPN — vehículo cabecera MdL (FY 2025, contexto)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 9.097.621,57 | Mayor PGC |
| Patrimonio neto | 5.102.490,99 | |
| Cap% IPN en TCH4 | 17,00% | Class A — MdL pool |

### TCH2 — vehículo holding patrimonial MdL (FY 2025, contexto)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 5.245.462,16 | |
| Patrimonio neto | 1.478.613,00 | |
| Cap% TCH2 en TCH4 | 15,60% | Class A — MdL pool |

Detalle completo + SQL de regeneración en `resources/cifras-2025-detalle.md`.

## 7. Governance

| Foro | Cadencia | Asistencia TERAS | Owner agenda |
|---|---|---|---|
| Steerco Templus | Trimestral | CIO + CFO TERAS | TERAS coordina vía TCH4 + Vesta |
| Consejo Templus CD | Trimestral | Representante TERAS por TCH4 + Vesta | Templus CD management |
| Consejo AE Group HoldCo II (Colorado) | Trimestral | Representante TERAS | AE Group HoldCo II + ICG |
| Comité M&A Templus (ad-hoc adquisiciones) | Ad-hoc | CIO + CFO + CLO | TERAS + Vesta |
| Auditoría externa TCH4 | Anual (EY IN25-6924 vigente) | CFO | EY |
| Auditoría externa Templus CD | Anual | CFO + audit firm | Audit firm Templus CD |
| Asambleas TCH4 (socios) | Mínimo anual + ad-hoc | Todos socios (10 socios) | TCH4 (Monforte 26% — mayor individual — designado portavoz) |

RACI extendido + org chart Templus chain (v8 14/04/2026) en `resources/governance.md`.

## 8. Fiscalidad

### Art. 21 LIS — test por eslabón

| Eslabón | Cap% | ≥5%? | Art. 21 LIS aplica? |
|---|---|---|---|
| MdL persona → IPN | 100% | sí | N/A (persona física) |
| IPN → TCH4 | 17,00% | sí | **SÍ** (dividendos/plusvalías TCH4 exentas en IPN) |
| TCH2 → TCH4 | 15,60% | sí | **SÍ** |
| TCH4 → Vesta Invest | 2,00% | **NO** (<5%) | **NO** (dividendos Vesta gravados 25% en TCH4) |
| Vesta → Templus CD | 96,00% | sí | SÍ (interno chain ICG) |
| TCIH → Templus CD directo | 2,00% | **NO** (<5%) | **NO** (dividendos Templus CD gravados 25% en TCIH) |

### Implicación práctica (CRÍTICO)

- **TCH4 paga 25% IS sin exención** sobre dividendos/plusvalías Vesta. Confirmado en BD `waterfall_params.is_rate_tch4_pct=25, source='LIS art. 21 — sin exención (<5%)'`.
- **TCIH paga 25% IS sin exención** sobre dividendos/plusvalías Templus CD directo (path 2). Confirmado en BD.
- **ÚNICO escudo fiscal de TCH4**: los intereses préstamo Vesta 8% (saldo 976.756,13€ cuenta 17100000) son **deducibles** en IS TCH4. Reducen base imponible y compensan parcialmente el 25% IS sobre cualquier flujo desde Vesta.
- Aguas arriba en cadena MdL: IPN/TCH2 sí aplican exención art. 21 sobre TCH4 (ambos >5%). El "peaje fiscal" 25% se paga UNA VEZ en TCH4/TCIH (no doble imposición arriba).

### NRV 19ª PGC

- TCH4 valora su 2% en Vesta como **inversión grupo NRV 19ª** (no consolida; coste menos deterioro). Cualquier dividendo Vesta se reconoce ingreso financiero ordinario, sin anticipar plusvalía.
- TCIH valora su 2% en Templus CD directo como NRV 19ª. Mismo tratamiento.
- Vesta consolida Templus CD (96% control) bajo régimen LU SOPARFI.

### Exit fiscal MdL — escenarios

- Sale price 400M€ (escenario base ICG) → equity surplus distribuible ~100M€ (sobre hurdle 300M€).
- TCH4 + TCIH reciben flujos combinados → IS 25% en cada nivel sin exención.
- En IPN/TCH2 puede aplicar exención art. 21 → flujo neto MdL ~5,2M€ (`exit_scenarios.mdl_net_return` para 400M€ base).
- Mitigante adicional: si refi Vesta genera intereses acumulados grandes deducibles en TCH4, reduce base IS.

Análisis detallado + escenarios alternativos + planificación reinversión en `resources/fiscalidad-detallada.md`.

## 9. Riesgos y mitigantes

| # | Categoría | Riesgo | P | I | Mitigante |
|---|---|---|---|---|---|
| 1 | Financiero | Refinanciación Vesta + servicio Class D pref 12% acumulado erosiona Class B upside | M | A | Negociación temprana, monitor cupón devengado |
| 2 | Comercial | Ramp-up DC Alcalá fase 1 más lento que budget → ARPU/utilización < target | M | A | KPIs steerco trimestral, comercialización proactiva |
| 3 | Regulatorio | Permisos eléctricos / capacity allocation Templus Madrid + Project Colorado | M | A | Lobby + compliance proactivo |
| 4 | Governance | Conflicto Class A Vesta (96%) vs Class B TCH4 (2%) + Class C Mgrs (2%) en supermayorías | B | A | ISHA Enmienda 11/12/2025 contempla protecciones, mediación |
| 5 | Operativo | Capex Project Colorado mayor que budget — 76,7M€ activos en 4 países simultáneo | A | A | Quarterly review por país, AE Group HoldCo II coordina |
| 6 | Fiscal | Cambio LIS art. 21 / TJUE jurisprudencia restringe exención cadena IPN/TCH2 → TCH4 | B | A | Opinion letter + sustancia económica |
| 7 | Fiscal | Hacienda recalifica préstamo Vesta 8% como dividendo encubierto → no deducible | B | A | Sustancia financiera + documentación Financing Agreement |
| 8 | Liquidez TCH4 | TCH4 con PN -5K€ negativo, depende de servicio dividendos Vesta o realización plusvalía | M | A | Política dividendos Vesta, refi, capitalización extraordinaria si necesario |
| 9 | M&A | Integración Espacio Edge (adq. 25/06/2025) + Waterways Global (Ceuta constit. 11/06/2025) con costes goodwill 20,8M€ | M | M | Plan integración 100 días + monitoreo deterioro goodwill |
| 10 | Sponsor | ICG / Vesta cambia estrategia o exige refi anticipada | B | A | Relación trimestral + alineamiento estratégico |

## 10. Hitos próximos

| Fecha | Hito | Owner |
|---|---|---|
| Q2 2026 | Cierre auditoría externa Templus CD 2025 + audit firm consolidado | CFO + audit firm |
| Q2 2026 | Plan 100 días integración Templus Spain (Espacio Edge) | CIO + Templus CD mgmt |
| Q3 2026 | Steerco Templus Q3 + revisión Project Colorado roll-out | TERAS coordina |
| Q3 2026 | Build-out Templus Ceuta operativo | Templus CD + Waterways legacy team |
| Q4 2026 | Asamblea TCH4 (alineamiento socios, política dividendos) | TCH4 |
| Q4 2026 | Modelado completo cadena Vesta → AE HoldCo II → 4 Roosevelt (tarea #9 BD MdL) | CFO + CTO TERAS |
| 2027 | Hito comercialización Templus Madrid Alcalá fase 1 (utilización >80% target) | Templus CD mgmt |
| 2027-2028 | Inicio conversaciones refinanciación Vesta (vinculado a despliegue commit 300M€) | CFO TERAS + ICG/Vesta |
| 2029+ | Ventana exit Templus (estimado, sale price referencia 400M€ base case ICG) | CIO TERAS + ICG |

## 11. Anti-patrones IA — errores típicos a evitar

1. **NO clasificar Templus como hospitality / hotelero**. Son **DATA CENTERS** (sector telco-infra). El sector BD es `Data Centers` con sponsor ICG.
2. **NO confundir Templus España (operativo) con Project Colorado (greenfield pan-europeo)**. Son la **MISMA línea de negocio business_line='templus'** aunque entidades distintas: España vía Templus CD → 7 filiales; Colorado vía AE Group HoldCo II → 4 Roosevelt. Pueden citarse juntas en informes Templus pero NO mezclar cifras por activo cuando se reporta por entidad.
3. **NO citar "Global Cabria" como entidad activa**. Es legacy DUPLICADO de Templus CD (`entities.global-cabria` con `exclude_from_group_totals=true`). En BD se mantiene por trazabilidad histórica, NO entra en consolidación ni en cifras Templus.
4. **NO afirmar que art. 21 LIS aplica en TCH4 → Vesta o TCIH → Templus CD**. Cap% TCH4 en Vesta = 2,00% **<5%, NO aplica exención**. Cap% TCIH en Templus CD directo = 2,00% **<5%, NO aplica exención**. Tributación 25% IS sin exención. Único escudo: intereses préstamo Vesta 8% deducibles en TCH4.
5. **NO mezclar Templus con Olin (TUCA/MasOrange) o Gemswell (Kelpa/surf parks)**. Son líneas de negocio distintas, sponsor distinto (Asterion/ICG/Kelpa), ISHA distinto, deal terms independientes y confidencialidad separada.
6. **NO inventar cifras Vesta**. Citar siempre: audit EY IN25-6924 abril 2026 (TCH4) + Pack Miguel 10-may-2026 (Balance Consolidado + P&L by Site + Colorado Mgmt Accounts) + BD `entity_balances` con `audit_2026_provisional`.
7. **NO confundir TCH4 con Templus CD**. TCH4 es vehículo MdL en cadena (holding spanish, NIF B56563398, PN técnicamente negativo); Templus CD es vehículo operativo agregador (NIF B-56381379, PN sólido 177,2M€). **Vesta Invest S.à r.l. (LUX)** es la matriz aguas arriba que integra ICG (96% Class A en Templus CD).
8. **NO confundir Vesta (sponsor ICG, externo) con un banco**. La cuenta 17100000 PTMO VESTA INVEST S.A.R.L. fue inicialmente mal clasificada como `pnc_bancario` por bug parser #14. Corregido en mayo 2026: es `pnc_otra` (préstamo equity-rank socio según ISHA, NO bancario).
9. **NO citar el cupón Class D como 10% o cualquier valor diferente a 12%**. La Enmienda ISHA 11/12/2025 fijó el cupón preferente Class D en **12,00% anual** (`waterfall_params.pref_coupon_pct=12`). Versiones anteriores del ISHA (11/10/2023) pueden tener cupones distintos pero la versión vigente es la enmendada.
10. **NO citar cap% MdL >5% en Templus CD**. El cap% efectivo agregado MdL es **1,62%** (0,626% vía Vesta + 1,033% vía TCIH). Cualquier cifra >5% es error de cálculo en el look-through o confusión con cap% en TCH4 (32,60%) o TCIH (51,665%).

## 12. Lint específico Templus

```
TEMPLUS LINT 1 — ¿Has citado fuente para cada cifra (audit EY IN25-6924 / Pack Miguel / BD / ISHA / Enmienda 11/12/2025)?
TEMPLUS LINT 2 — ¿Has distinguido cap% MdL: en TCH4 (32,60%) vs en Vesta (32,60% × 2% = 0,652%) vs en Templus CD agregado (1,62%) vs vía TCIH path 2 (1,033%)?
TEMPLUS LINT 3 — ¿Has reflejado que NO aplica art. 21 LIS en TCH4 → Vesta ni en TCIH → Templus CD (ambos <5%)?
TEMPLUS LINT 4 — ¿La cuenta 17100000 PTMO VESTA está como `pnc_otra` (no `pnc_bancario`)? Fix bug #14.
TEMPLUS LINT 5 — ¿Has citado el cupón Class D al 12% (Enmienda 11/12/2025), no a 10% u otro valor?
TEMPLUS LINT 6 — ¿Has tributado los dividendos Vesta en TCH4 al 25% IS con único escudo intereses Vesta 8%?
TEMPLUS LINT 7 — ¿El output respeta confidencialidad (no se mezcla con Olin/Gemswell/TCIH)?
TEMPLUS LINT 8 — ¿La calculadora `/waterfall-templus` consulta usa `waterfall_params` actualizado (factor mdl_pct_in_tch4=32,60%, teras_pct_global=2,00%, pref_coupon_pct=12%)?
TEMPLUS LINT 9 — ¿Has citado `exit_scenarios` con sus 4 niveles (250/350/400/500M€) en lugar de inventar IRR/MOIC?
TEMPLUS LINT 10 — ¿Templus CD está marcado con `exclude_from_group_totals=true` (evitar doble conteo)?
TEMPLUS LINT 11 — ¿Distingues claramente Templus España (operativo, 7 filiales) vs Project Colorado (greenfield, 4 Roosevelt vía AE HoldCo II)?
TEMPLUS LINT 12 — ¿Global Cabria está marcado como legacy duplicado de Templus CD (NO en cifras consolidadas)?
```

## Recursos

- [Cap table detallado](resources/cap-table-detallado.md)
- [Deal terms](resources/deal-terms.md)
- [Cifras 2025 detalle](resources/cifras-2025-detalle.md)
- [Governance](resources/governance.md)
- [Fiscalidad detallada](resources/fiscalidad-detallada.md)
- [Decisiones clave](resources/decisiones-clave.md)
- [Documentos referencia](resources/documentos-referencia.md)
- [Waterfall y escenarios ISHA](resources/waterfall-y-escenarios-isha.md)
- [Project Colorado detalle](resources/project-colorado-detalle.md)
