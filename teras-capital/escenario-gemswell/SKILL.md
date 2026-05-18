---
name: escenario-gemswell
capa: L3b-escenarios
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras, challenge-cognitivo-teras]
triggers: >
  Se activa cuando el usuario menciona Gemswell, GEMSWELL, Kelpa, KELPA,
  Kelpa Expansión, surf, surf park, surf parks, Wave Park, Wavegarden,
  VSO II, Stoneweg, TCH3, Teras Capital Holding 3, subsanación TCH3,
  subsanación capital TCH3, Valdorba, Valdorba Parques, Valdorba Metropolitano,
  VM, VPS, VPSH, SW Infrasports, Quarter Capital, QC, Grand View,
  Grand View La Quinta, La Quinta, MM Sports, MMS, MPS, Madrid Playa Surf,
  ramp-up surf, ISHA Gemswell, hurdle Gemswell, promote Gemswell.
description: >
  Precarga contexto operativo, contable, legal y fiscal del activo GEMSWELL
  (TCH3 → Valdorba Parques 88% + SW Infrasports 50% + cadena Quarter Capital
  IPN 32,29% → Grand View 100%) con Stoneweg como sponsor financiero / industrial.
  Cubre cap table efectivo MdL 46,86% en TCH3 (IPN 36,45% + TCH2 10,41%),
  paquete económico tras subsanación capital diciembre 2025 (capital 7.203.820€,
  prima 1.112.464€), 12 socios TCH3, NAV histórico VSO II 124,48% (Wave Park),
  hurdle ISHA 8% + promote 20%, calibrado con BD `savenikqhmcuwmcnabca`.
---

# Escenario: Gemswell

> **Snapshot**: 31/12/2025 — última actualización 2026-05-18 (Claude Code)
> **Fuente principal**: BD Supabase `savenikqhmcuwmcnabca` (`business_lines.gemswell`, `business_lines.quarter`, `entities`, `participations`, `shareholders`, `entity_balances`, `waterfall_params`, `intragroup_balances`) + auditoría provisional TCH3 02/04/2026 + email Miguel 7-may-2026 + email Stoneweg/Ramón Romero 7-may-2026 + Pacto Socios SHA SW Infrasports nov 2024 + Acuerdo Kelpa.

## 1. Snapshot ejecutivo

Gemswell es la línea de negocio de TERAS Capital sobre **surf parks operativos y en desarrollo en Iberia**, vehiculada a través de **TCH3** (TCH Tres Holding & Management, S.L.) como vehículo de cabecera y desplegada sobre el subgrupo **Valdorba Parques 88%** (con sus filiales operativas Valdorba Metropolitano VM, Valdorba Parques Surf VPS y Valdorba Parques Surfhotel VPSH) y la sociedad gestora **SW Infrasports 50%** (joint venture industrial con Stoneweg). MdL participa con cap% efectivo look-through **46,86%** en TCH3 (36,45% IPN directo + 10,41% vía TCH2). El sponsor industrial / financiero del proyecto es **Stoneweg** (NO Kelpa: Kelpa Expansión es entidad con derecho de crédito frente a Valdorba Metropolitano, no inversor en TCH3). El segundo socio principal de TCH3 es **MM Sports Servicios de Gestión SLU** con 36,41%. La fase actual es **ramp-up surf parks operativos** post-subsanación capital diciembre 2025. Adicionalmente, la cadena **Quarter Capital → Grand View La Quinta** (IPN 32,29% directo) ha sido capitalizada en el aumento de capital TCH3 dic-2025 — decisión doctrinal que la sitúa orgánicamente dentro de Gemswell aunque jurídicamente cuelga de IPN. Hurdle ISHA 8% sobre capital invertido; promote 20% sobre exceso. NAV histórico VSO II (compartimento Wave Park) 124,48% a 31/12/2025 según email Stoneweg / Ramón Romero 7-may-2026.

## 2. Ficha del activo

| Parámetro | Valor | Fuente |
|---|---|---|
| Línea BD | `business_lines.gemswell` short_name `GEMSWELL` | BD |
| Sector | Infraestructuras Deportivas | BD |
| Sponsor | **Stoneweg** (NO Kelpa) | BD `business_lines.gemswell.sponsor` |
| Status | active | BD |
| Vehículo MdL en cadena | TCH3 (TCH Tres Holding & Management, S.L.) NIF pendiente | BD `entities.tch3` |
| Vehículo industrial JV | SW Infrasports (50% TCH3 / 50% Stoneweg, 150 participaciones cada uno) | BD + Pacto Socios SHA nov 2024 |
| Subgrupo operativo | Valdorba Parques 88% TCH3 → VM 100% + VPS 100% + VPSH 100% | BD `participations` |
| Cadena lateral | IPN → Quarter Capital 32,29% → Grand View La Quinta 100% (capitalizada en aumento TCH3 dic-2025) | BD `business_lines.quarter` + email Miguel 7-may-2026 |
| Activo subyacente | Surf parks operativos (Valdorba Metropolitano), surf park resort (VPS/VPSH), pipeline Wave Park (vía VSO II) y proyectos La Quinta Marbella (Grand View) | público + email Miguel |
| Fase | Ramp-up surf parks operativos + inscripción RM subsanación capital (ene-2026) + exit Wave Park posible | comunicación interna |
| Cap% MdL efectivo en TCH3 | **46,86%** (36,45% IPN + 10,41% TCH2) | BD `business_lines.gemswell.mdl_position_pct` + cap table audit |
| Cap% TCH3 declarado en `mdl_position_pct` business_line | 46,86% efectivo | BD `business_lines.gemswell.mdl_position_pct` |
| Total investment Gemswell (techo) | 80.000.000€ | BD `business_lines.gemswell.total_investment` |
| Capital social TCH3 (post-subsanación dic-2025) | **7.203.820€** | audit provisional 02/04/2026 (B88547567) |
| Capital social TCH3 (pre-subsanación) | 5.010.628€ | audit provisional 02/04/2026 |
| Prima asunción TCH3 (total post-subsanación) | 1.112.464€ | audit provisional 02/04/2026 |
| Aportación capital IPN en TCH3 | 2.625.910€ (2.625.910 partic ordinarias VN 1€) | BD `participations` + cap table |
| Aportación capital TCH2 en TCH3 | 750.000€ (750.000 partic ordinarias VN 1€) | BD `participations` + cap table |
| Pool MdL TCH3 (IPN + TCH2) | **3.375.910 partic = 46,86%** | cap table audit |
| Segundo socio TCH3 | MM Sports Servicios de Gestión SLU **36,41%** (2.622.910 partic) | cap table audit |
| Hurdle ISHA Gemswell | 8% | BD `waterfall_params.hurdle_rate_pct` |
| Promote sobre exceso | 20% | BD `waterfall_params.promote_pct` |
| SW Infrasports % TCH3 | 50% | BD `waterfall_params.swi_tch3_pct` + Pacto Socios SHA nov 2024 |
| SW Infrasports — promote sobre carry | 50% para TCH3 | BD `waterfall_params.tch3_promote_pct_swi` |
| SW Infrasports — fee anual fijo | 250.000€ | BD `waterfall_params.swi_fixed_fee_eur` + SHA |
| Fee gestión por proyecto | 200.000€ (BD default) / 925.500€ (alt calculadora actual) | BD `waterfall_params.mgmt_fee_per_project_eur` |
| Kelpa debt referencia | 50.000.000€ (BD default) / 74.700.000€ (calculadora actual) | BD `waterfall_params.kelpa_debt_eur` + Acuerdo Kelpa |
| Kelpa equity referencia | 30.000.000€ (BD default) / 49.000.000€ (calculadora actual) | BD `waterfall_params.kelpa_equity_eur` |
| Num proyectos default | 2 | BD `waterfall_params.num_projects` |
| Transaction costs | 1,5% | BD `waterfall_params.tx_costs_pct` |
| VSO II unaudited NAV % | **124,48%** a 31/12/2025 | email Stoneweg/Ramón Romero 7-may-2026 |
| VSO II crédito face value | 1.000.000€ (Acuerdo TCH3 con compartimento Wave Park) | Acuerdo Wave Park / VSO II |
| VSO II fair value calculado | 1.244.800€ (1.000.000 × 124,48%) | derivado |
| Mdl_effective_pct SW Infrasports | 23,44% (46,86% × 50%) | look-through |
| Tipo IS aplicable a TCH3 | 25% — sí aplica exención art. 21 LIS para flujos de IPN/TCH2 a TCH3 (pool MdL 46,86% > 5%) | LIS art. 21 + BD |
| TCH3 balance 2025 (post-subsanación) | Activo 6.109.732,11€ · PN 304.469,52€ · Pasivo 5.805.262,59€ | audit provisional 02/04/2026 + parser_fix_bug14 |
| Año fiscal referencia | 31/12/2025 (TCH3 con subsanación de efecto contable retroactivo) | audit provisional + decisión doctrinal |
| Audit firm | (pendiente confirmar nombre — audit provisional 02/04/2026 disponible) | BD |

## 3. Estructura societaria

Cadena efectiva look-through MdL → surf parks + La Quinta:

```
mdl-persona (Miguel de Lucas Sánchez)
  │ 100,00% (Ordinarias)
  ▼
IPN (Inteligencia Procesos de Negocio, SLU) NIF B87680328
  │
  ├─ 36,45% directo TCH3 (Ordinarias, 2.625.910 partic VN 1€)
  │
  ├─ 100% TCH2 (Ordinarias)
  │     │
  │     └─ 10,41% TCH3 (Ordinarias, 750.000 partic VN 1€)
  │
  └─ 32,29% directo Quarter Capital (cadena lateral capitalizada en TCH3 dic-2025)
        │
        ▼
     Quarter Capital, S.L.
     Activo 3.965.846€ · PN 3.298.655€ · Pasivo 667.191€ (override email Miguel 7-may-2026)
        │
        │ 100%
        ▼
     Grand View La Quinta, S.L.
     Activo 4.391.565€ · PN 3.340.062€ · Pasivo 1.051.503€ (override email Miguel 7-may-2026)
     Inversiones inmobiliarias Marbella
     [Saldo intragrupo Grand View → IPN 1.519.092,12€ loan_lp,
      cuenta 17100002 PTMO GRAND VIEW LA QUINTA IPN acreedor]

                            ▼
TCH3 (TCH Tres Holding & Management, S.L.) NIF pendiente
Capital social 7.203.820€ (post-subsanación dic-2025)
Prima asunción 1.112.464€
Activo 6.109.732,11€ · PN 304.469,52€ · Pasivo 5.805.262,59€
  │   Cap table TCH3 (12 socios):
  │   • IPN 36,45% (Pool MdL — 2.625.910 partic)
  │   • MM Sports Servicios de Gestión SLU 36,41% (2.622.910 partic) — 2º socio principal
  │   • TCH2 10,41% (Pool MdL — 750.000 partic)
  │   • Monforte Consultoría 5,55% (MCT, 400K partic, +300K cap sept 2025)
  │   • I.Velilla 2,78% (Teras, adq desde TCIH 200K partic sept 2025,
  │                       condición suspensiva inscripción RM)
  │   • Gurrea 2,08% (Indep, +50K cap sept 2025)
  │   • Gálvez 1,94% (Indep, 140K partic)
  │   • Ramón Romero 1,39% (Indep, nuevo socio sept 2025, capitalización deuda 100K)
  │   • LSS 1,39% (LSS group, 100K partic)
  │   • Lafarga 0,69% (Indep, nuevo socio sept 2025, cap deuda 50K)
  │   • L.Osorio 0,69% (Indep, 50K partic)
  │   • Faura 0,21% (Indep, 15K partic)
  │
  ├─ 88% Valdorba Parques (Ordinarias)
  │      │  Activo 4,67M€ · PN 3,97M€
  │      │
  │      ├─ 100% Valdorba Metropolitano (VM)
  │      │      Activo 4,4M€ · PN 1,84M€ · Ingresos 2M€
  │      │      [Operativo — surf park urbano]
  │      │      │
  │      │      ├─ 0% Kelpa Expansión — DERECHO DE CRÉDITO (NO participación)
  │      │      │   [Cuenta 17100011 reclasificada por bug #14 fix
  │      │      │    de pnc_bancario a pnc_otra — tercero NO bancario]
  │      │      │
  │      │      └─ 10,31% Madrid Playa Surf (MPS) — mdl_effective_pct
  │      │            [Proyecto surf park en pipeline Madrid]
  │      │
  │      ├─ 100% Valdorba Parques Surf (VPS)
  │      │      Activo 4,05M€ · PN 4,01M€ · Capital 4,03M€
  │      │      [Vehículo del proyecto surf park resort]
  │      │
  │      └─ 100% Valdorba Parques Surfhotel (VPSH)
  │             Activo 170€ · PN -820€
  │             [Vehículo SPV hotel asociado al surf park, en latencia]
  │
  └─ 50% SW Infrasports (Ordinarias, 150 partic — pacto socios SHA nov 2024)
         mdl_effective_pct 23,44% = 46,86% × 50%
         [JV industrial con Stoneweg — sociedad gestora paraguas
          de los proyectos surf parks Gemswell]
         Fee anual fijo 250.000€; promote 50% sobre carry.
         Compartimento VSO II (Wave Park):
            crédito face 1.000.000€ · NAV 124,48% · fair value 1.244.800€
```

**Cap% efectivo MdL look-through**:
- En TCH3: **46,86%** = 36,45% (IPN directo) + 10,41% (IPN × 100% × TCH2 × 10,41%)
- En Valdorba Parques: 46,86% × 88% = **41,24%**
- En VM / VPS / VPSH (vía Valdorba Parques 100%): **41,24%**
- En SW Infrasports: 46,86% × 50% = **23,44%**
- En MPS (vía VM 10,31%): 41,24% × 10,31% = **4,25%**
- En Quarter Capital (IPN directo 32,29%): **32,29%** (cadena lateral capitalizada en aumento TCH3 dic-2025)
- En Grand View La Quinta (vía QC 100%): **32,29%**

> **CRÍTICO**: la cadena Quarter Capital → Grand View La Quinta cuelga **jurídicamente de IPN directo** (32,29%, no de TCH3). Pero **doctrinalmente está dentro del perímetro Gemswell** porque sus créditos fueron capitalizados en el aumento de capital TCH3 de diciembre 2025 y nunca fue una posición de TCIH. Decisión registrada (Miguel 7-may-2026): "Todo esto se ha capitalizado en el aumento de capital TCH3 y nunca era una posición de TCIH". Para informes consolidados Gemswell se incluye QC + Grand View; para participations strictu sensu cuelgan de IPN.

Detalle completo en `resources/cap-table-detallado.md`.

## 4. Deal económico

### Subsanación capital TCH3 — diciembre 2025 (CRÍTICO)

La operación contable y societaria que define el snapshot 31/12/2025 de TCH3 es la **subsanación de capital social de diciembre 2025**, formalizada vía dos ampliaciones simultáneas:

- **1ª ampliación — compensación de créditos intragrupo**: 1.343.000€ capital + 557.000€ prima de asunción (con el crédito MPS — Madrid Playa Surf). Capitaliza créditos pendientes de IPN/MMS y otros socios.
- **2ª ampliación — dineraria**: 850.000€ capital + 555.000€ prima de asunción. Aportación efectiva.
- **Total capital pre-subsanación**: 5.010.628€.
- **Total capital post-subsanación**: **7.203.820€**.
- **Prima asunción total post-subsanación**: 1.112.464€.

**Efecto contable retroactivo a 31/12/2025**: el acta de subsanación fue firmada antes de 31/12/2025, con elevación pública en enero 2026. La auditoría provisional de 02/04/2026 (B88547567) reconoce el efecto contable retroactivo a 31/12/2025. **No se debe esperar a inscripción RM para reflejar la subsanación en cifras de cierre 2025**: es decisión doctrinal documentada.

PN TCH3 inferior al capital social (304.469,52€ vs 7.203.820€) indica **pérdidas acumuladas previas absorbidas** (resultados anteriores -8.011.815€ se absorben con la operación). Pasivo de 5,8M€ corresponde a **créditos intragrupo NO compensados** (subgrupo Valdorba pendiente de capitalización futura).

### Fix bug #14 (15-may-2026) — cuenta 17100011 PTMO TELCOGESTORES

- Reclasificación de la cuenta **17100011 PTMO TELCOGESTORES SERVICIOS DE GESTION (250.000€)** desde `pnc_bancario` a `pnc_otra`, por tratarse de un **tercero NO bancario** (no se debe consolidar como deuda bancaria en informes para el banco).
- Afecta a TCH3 y TCH4 (parser_fix_bug14).

### Hurdle ISHA + promote

- **Hurdle ISHA Gemswell**: 8% sobre capital invertido (acuerdo socios Gemswell — `waterfall_params.hurdle_rate_pct`).
- **Promote sobre exceso**: 20% (`waterfall_params.promote_pct`).
- **SW Infrasports — promote sobre carry**: 50% para TCH3 (`waterfall_params.tch3_promote_pct_swi`).
- **Fee anual fijo SW Infrasports**: 250.000€ (`waterfall_params.swi_fixed_fee_eur`).
- **Fee gestión por proyecto**: 200.000€ (BD default `mgmt_fee_per_project_eur`) — coexiste con valor alternativo de 925.500€ en la calculadora actual; documentar discrepancia.

### Estructura Kelpa — referencias de cálculo

- **Acuerdo Kelpa**: define deuda y equity del compartimento por proyecto.
- **Default BD**: deuda 50.000.000€ + equity 30.000.000€ = 80M€ total (techo Gemswell).
- **Calculadora actual** (`/waterfall-gemswell`): deuda 74.700.000€ + equity 49.000.000€ = 123,7M€. Discrepancia con default BD a documentar.
- **Num proyectos default**: 2 (`num_projects`).
- **Transaction costs**: 1,5% (`tx_costs_pct`).

### VSO II (Wave Park) — compartimento histórico

- **Crédito face value**: 1.000.000€ — Acuerdo TCH3 con compartimento Wave Park (estructura VSO II).
- **NAV no auditado a 31/12/2025**: **124,48%** según email Stoneweg / Ramón Romero del 7-may-2026.
- **Fair value derivado**: 1.244.800€ (1.000.000 × 1,2448).
- Registrado como factor histórico en `waterfall_params`. NO inventar variaciones.

Paquetes detallados (vesting, leaver provisions, mecánica capitalización créditos) en `resources/deal-terms.md`.

## 5. Stakeholders

| Actor | Rol | Prioridades | Gestión TERAS |
|---|---|---|---|
| **Stoneweg** | Sponsor industrial / financiero (NO Kelpa) | Ramp-up surf parks operativos, pipeline pipelín Wave Park, expansión Iberia | Comité industrial JV SW Infrasports, NAV VSO II trimestral |
| MM Sports Servicios de Gestión SLU | 2º socio principal TCH3 (36,41%) | Alineación con MdL, retorno waterfall, governance ISHA | Voz coordinada con MdL en consejo TCH3 |
| TCH3 — Pool MdL | IPN 36,45% + TCH2 10,41% = 46,86% efectivo | Retorno waterfall, ramp-up operativo, exit Wave Park | Voz coordinada (consejo TCH3) |
| TCH3 — MCT (Monforte) | 5,55% (400K + 300K capitalizadas sept 2025) | Misma agenda upside | Asamblea TCH3 |
| TCH3 — I. Velilla | 2,78% (Teras, adq desde TCIH sept 2025) | Alineación con TERAS / mgmt | Equipo gestor TERAS |
| TCH3 — Indeps (Gurrea, Gálvez, R. Romero, Lafarga, L. Osorio, Faura) | ~9% agregado | Upside surf parks | Asambleas TCH3, comités ad-hoc |
| TCH3 — LSS group | 1,39% | Misma agenda upside | Asamblea TCH3 |
| Valdorba Parques / VM / VPS / VPSH management | Operativo surf parks | KPIs operativos, ramp-up, capex network | Steerco operativo trimestral |
| Kelpa Expansión | Acreedor de VM (derecho de crédito, NO inversor) | Cobro deuda según acuerdo | Comité financiero con VM, no governance |
| Asesores legales | Cumplimiento ISHA, SHA SW Infrasports, formalización subsanación RM | CLO super-poder | |
| Asesores fiscales | NRV 19ª, art. 21 LIS aplicable a flujos IPN/TCH2→TCH3, planificación exit | CFO super-poder | |
| Auditor TCH3 | Audit provisional 02/04/2026 (B88547567), cierre anual subgrupo | CFO + auditoría externa | Anexo en `bl_documents` |
| García Ruiz (contable Quarter Capital + Grand View) | Procesar mayores 2018-2025 cuentas 25200x + 5510x | Cierre formal QC / Grand View | Equipo CFO MdL |

## 6. Cifras 2025

> Snapshot: 31/12/2025. TCH3 = audit provisional 02/04/2026 + parser_fix_bug14; Valdorba subgrupo = entity_balances; Quarter / Grand View = override email Miguel 7-may-2026.

### TCH3 — vehículo de cabecera (FY 2025, post-subsanación)

| Concepto | Valor | Notas |
|---|---|---|
| Activo total | 6.109.732,11€ | audit provisional 02/04/2026 |
| Patrimonio neto | 304.469,52€ | Post-subsanación; PN<capital indica pérdidas previas absorbidas |
| Capital social | **7.203.820€** | Post-subsanación dic-2025 |
| Prima asunción | 1.112.464€ | (557K crédito MPS + 555K dineraria) |
| Resultados anteriores | -8.011.815€ | Absorbidos por reservas / reducción + ampliaciones |
| Total pasivo | 5.805.262,59€ | Mayoría intragrupo (créditos Valdorba subgrupo no compensados) |
| Bank debt | 0€ | Sin deuda bancaria propia |
| Source | audit_2026_provisional + parser_fix_bug14 | |

### Subgrupo Valdorba (FY 2025)

| Entidad | Activo | PN | Pasivo | Otros |
|---|---|---|---|---|
| Valdorba Parques (cabecera 88% TCH3) | 4,67M€ | 3,97M€ | 0,70M€ | |
| Valdorba Metropolitano (VM, 100%) | 4,4M€ | 1,84M€ | 2,56M€ | Ingresos 2M€ — operativo |
| Valdorba Parques Surf (VPS, 100%) | 4,05M€ | 4,01M€ | 0,04M€ | Capital social 4,03M€ — fase desarrollo |
| Valdorba Parques Surfhotel (VPSH, 100%) | 170€ | -820€ | 990€ | Latencia / SPV hotel |
| MPS (10,31% vía VM) | (no disponible BD MdL) | | | mdl_effective_pct 4,25% |

### SW Infrasports (50% TCH3)

- Cifras BD MdL no disponibles (sociedad gestora, FY pendiente confirmar).
- Fee anual fijo 250.000€ + promote 50% sobre carry compartimentos.

### Cadena Quarter Capital → Grand View La Quinta (capitalizada en TCH3 dic-2025)

| Entidad | Activo | PN | Pasivo | Notas |
|---|---|---|---|---|
| Quarter Capital | 3.965.846€ | 3.298.655€ | 667.191€ | Override email Miguel 7-may-2026 |
| Grand View La Quinta | 4.391.565€ | 3.340.062€ | 1.051.503€ | Override email Miguel; inversiones inmobiliarias Marbella; mayores 2018-2025 (cuentas 25200x + 5510x) enviados a García Ruiz, pendientes procesar |

### Saldo intragrupo asociado

- **Grand View → IPN**: 1.519.092,12€ loan_lp (cuenta **17100002** PTMO GRAND VIEW LA QUINTA — IPN acreedor frente a Grand View). Equity-rank intragrupo MdL pool.

### VSO II — compartimento Wave Park

| Concepto | Valor |
|---|---|
| Crédito face value | 1.000.000€ |
| NAV no auditado 31/12/2025 | 124,48% |
| Fair value derivado | 1.244.800€ |

Detalle completo + SQL de regeneración en `resources/cifras-2025-detalle.md`.

## 7. Governance

| Foro | Cadencia | Asistencia TERAS | Owner agenda |
|---|---|---|---|
| Consejo TCH3 | Trimestral | CIO + CFO TERAS | TCH3 (Pool MdL + MMS designados) |
| Comité industrial SW Infrasports | Trimestral | TERAS + Stoneweg paritario | SW Infrasports SHA nov 2024 |
| Steerco Valdorba Parques (VM/VPS/VPSH) | Bimestral / trimestral | TERAS + management Valdorba | Operativo surf parks |
| Comité Kelpa (acreedor VM) | Ad-hoc / semestral | CFO TERAS + Kelpa | Servicio deuda VM |
| Auditoría externa TCH3 + subgrupo | Anual | CFO | Audit firm — provisional 02/04/2026 ya en `bl_documents` |
| Asambleas TCH3 (12 socios) | Mínimo anual + ad-hoc | Todos socios | TCH3 (MM Sports / IPN designados) |
| Cierre formal Quarter Capital + Grand View | Anual | CFO MdL + García Ruiz | Pendiente procesar mayores 2018-2025 |

RACI extendido + org chart Gemswell / Valdorba chain en `resources/governance.md`.

## 8. Fiscalidad

### Art. 21 LIS (exención dividendos / plusvalías inversión grupo)

- **MdL (IPN/TCH2) sobre TCH3**: pool MdL agregado 46,86% (IPN 36,45% directo + TCH2 10,41% indirecto, ambos >>5%) — **SÍ aplica exención art. 21 LIS** sobre dividendos y plusvalías de TCH3 hacia IPN y TCH2 individualmente considerados (cada uno supera por sí solo el 5% mínimo). Confirmado.
- **TCH3 sobre Valdorba Parques**: cap% TCH3 = 88% — **SÍ aplica exención** sobre flujos Valdorba → TCH3.
- **TCH3 sobre SW Infrasports**: cap% TCH3 = 50% — **SÍ aplica exención** sobre flujos SWI → TCH3.
- **TCH3 sobre cadena Quarter / Grand View**: NO aplica directamente (la cadena cuelga de IPN, no de TCH3). IPN sobre Quarter Capital 32,29% — **SÍ aplica exención** sobre QC → IPN.
- **Tipo IS aplicable a TCH3**: 25% sobre base no exenta.

### NRV 19ª PGC

- TCH3 valora sus inversiones en Valdorba Parques (88%) y SW Infrasports (50%) como **inversiones en grupo/multigrupo NRV 19ª**: coste menos deterioro; no consolida estados financieros a nivel TCH3 (TCH3 no es matriz consolidante de grupo formal a efectos PGC, salvo confirmación auditor).
- IPN valora Quarter Capital 32,29% como **inversión en grupo NRV 19ª**.

### Subsanación capital — efecto fiscal

- La compensación de créditos intragrupo (1.343K capital + 557K prima) en la 1ª ampliación es **operación neutra en IS** en sede de TCH3 (no genera renta gravable; los créditos pasan a capital).
- La capitalización del crédito MPS (557K prima) traslada riesgo fiscal de potencial deterioro del crédito a coste de adquisición de participaciones.

### Planificación exit MdL

- En exit Wave Park / VSO II: plusvalía vía SW Infrasports tributa al 25% IS en TCH3 (con potencial exención si participación SW Infrasports en compartimento supera 5%); sube a IPN/TCH2 con exención art. 21 LIS sobre el cap% TCH3>5%.
- En exit La Quinta / Grand View: plusvalía en Grand View → QC (100%, exención >5%) → IPN (32,29%, exención >5%).
- Cláusulas SPA, retención en origen, escalonamiento y reinversión TERAS a evaluar.

Análisis detallado + escenarios alternativos en `resources/fiscalidad-detallada.md`.

## 9. Riesgos y mitigantes

| # | Categoría | Riesgo | P | I | Mitigante |
|---|---|---|---|---|---|
| 1 | Operativo | Ramp-up surf parks operativos (VM) por debajo de plan | M | A | KPIs steerco trimestral, plan retention, comms Stoneweg |
| 2 | Financiero | Deuda Kelpa frente a VM con condiciones onerosas o re-pricing | M | A | Comité Kelpa, opcionalidad refinanciación, capitalización selectiva |
| 3 | Capital | Inscripción RM subsanación dic-2025 demorada o impugnada | B | A | Acta firmada antes 31/12/2025, elevación pública ene-2026, audit provisional confirma efecto contable |
| 4 | Valoración | NAV VSO II 124,48% pierde respaldo si Wave Park no cierra exit | M | M | Acuerdo VSO II + email Stoneweg/Ramón Romero como soporte; revaluar trimestralmente |
| 5 | Governance | Conflicto MdL (46,86%) vs MM Sports (36,41%) en supermayorías | B | A | ISHA contempla supermayorías, mediación, voto coordinado pool MdL |
| 6 | Comercial | Demanda surf parks por debajo de business plan (VPS / VPSH ramp-up) | M | M | KPIs operativos, marketing performance, pricing dinámico |
| 7 | Reputacional | Caso público adverso surf park (seguridad, accidente, ambiental) | B | A | Comms plan, seguros, compliance H&S |
| 8 | Fiscal | TJUE/TS jurisprudencia sobre cadenas holding intragrupo | B | M | Asesoría continua, opinion letters |
| 9 | Cadena lateral | Cierre formal Quarter Capital + Grand View (mayores 2018-2025 sin procesar) | M | M | García Ruiz procesa cuentas 25200x + 5510x; consolidar override email Miguel |
| 10 | Parser PGC | Bug #14 cuenta 17100011 Telcogestores (250K€) reclasificada de pnc_bancario a pnc_otra | C | M | Fix aplicado 15-may-2026; verificar no recaída en otras cuentas similares |
| 11 | Liquidez TCH3 | Pasivo TCH3 5,8M€ depende de servicio créditos intragrupo Valdorba subgrupo | M | A | Capitalización selectiva pendiente, política tesorería subgrupo |

> Leyenda P/I: B=Bajo, M=Medio, A=Alto, C=Cerrado.

## 10. Hitos próximos

| Fecha | Hito | Owner |
|---|---|---|
| Ene-2026 | Elevación pública subsanación TCH3 + presentación RM | Notaría + CLO |
| Q1 2026 | Inscripción RM subsanación TCH3 (condición suspensiva I. Velilla) | Registro Mercantil |
| Q2 2026 | Cierre auditoría externa TCH3 2025 (definitiva, post-provisional 02/04/2026) | CFO + audit firm |
| Q2 2026 | Procesar mayores 2018-2025 Quarter Capital + Grand View (cuentas 25200x + 5510x) | García Ruiz + CFO MdL |
| Q2 2026 | KPIs ramp-up VM trimestral; revisión NAV VSO II | TERAS + Stoneweg |
| Q3 2026 | Comité industrial SW Infrasports — proyectos pipeline | TERAS + Stoneweg |
| Q3-Q4 2026 | Cierre operativo VPS (surf park resort) + arranque VPSH (surfhotel) | Management Valdorba |
| 2027 | Posible exit Wave Park / VSO II (en función NAV) | SW Infrasports + Stoneweg |
| 2027+ | Capitalización selectiva créditos intragrupo Valdorba subgrupo restantes | CFO TERAS |
| 2028+ | Ventana exit Gemswell consolidado (en función ramp-up surf parks + pipeline) | CIO TERAS + Stoneweg |

## 11. Anti-patrones IA — errores típicos a evitar

1. **NO citar Kelpa como sponsor de Gemswell**. El sponsor industrial/financiero real es **Stoneweg**. **Kelpa Expansión** es entidad con **derecho de crédito** frente a Valdorba Metropolitano (NO participación, NO inversor en TCH3). El campo `business_lines.gemswell.sponsor` lo confirma: "Stoneweg".
2. **NO situar Quarter Capital / Grand View La Quinta dentro de TCIH**. Esta cadena cuelga **jurídicamente de IPN directo (32,29%)** y fue **capitalizada en el aumento de capital TCH3 de diciembre 2025**; nunca fue una posición de TCIH. Decisión doctrinal email Miguel 7-may-2026: "Todo esto se ha capitalizado en el aumento de capital TCH3 y nunca era una posición de TCIH".
3. **NO esperar a inscripción RM para reconocer la subsanación capital TCH3**. El acta fue firmada antes del 31/12/2025 y la auditoría provisional de 02/04/2026 (B88547567) la reconoce con **efecto contable retroactivo a 31/12/2025**. La elevación pública (ene-2026) y la inscripción RM (Q1-2026) son formalidades posteriores; el cierre 2025 ya incorpora capital social 7.203.820€.
4. **NO confundir TCH3 con Gemswell**. TCH3 es el **vehículo holding de cabecera** (entidad jurídica); Gemswell es la **línea de negocio** (subgrupo). TCH3 controla Valdorba Parques 88% + SW Infrasports 50%; Gemswell incluye además la cadena lateral Quarter Capital / Grand View (que cuelga de IPN).
5. **NO inventar cifras NAV de VSO II**. La única fuente válida a 31/12/2025 es el email Stoneweg / Ramón Romero del 7-may-2026: **124,48%**. Si se necesita actualización, pedirla al sponsor o citar email/comunicación posterior. No extrapolar.
6. **NO mezclar Gemswell con Olin o Templus**. Son líneas de negocio independientes con confidencialidad, deal terms, sponsors y cadenas societarias distintas. Olin = TCH1 → Tuca Bidco (Asterion). Templus = TCH4 → data centers (Vesta-ICG). Gemswell = TCH3 → surf parks (Stoneweg).
7. **NO citar 17,99% u otros porcentajes Olin/TCH1 como cap% TCH3**. El cap% MdL pool en TCH3 es **46,86%** (36,45% IPN + 10,41% TCH2). El segundo socio principal es **MM Sports 36,41%** (NO confundir con Monforte 5,55%, ni con MM Sports en TCH1 si existiera).
8. **NO afirmar que VPSH es operativo**. Valdorba Parques Surfhotel está en **latencia / SPV** con activo 170€ y PN -820€ a 31/12/2025; el cierre operativo del hotel se proyecta Q3-Q4 2026.
9. **NO reclasificar la cuenta 17100011 PTMO TELCOGESTORES como pnc_bancario** — el fix del bug #14 (15-may-2026) la reclasificó a `pnc_otra` por ser tercero NO bancario. Verificar siempre el clasificador PGC post-fix.
10. **NO usar el `business_lines.quarter.mdl_position_pct = 32,29%` como si fuera del perímetro TCIH ni del TCH3 jurídico**. Está jurídicamente en IPN, doctrinalmente en Gemswell. Para informes de Gemswell se incluye; para participations no se duplica.

## 12. Lint específico Gemswell

```
GEMSWELL LINT 1  — ¿Has citado fuente para cada cifra (audit / mayor / email Miguel / email Stoneweg / BD)?
GEMSWELL LINT 2  — ¿Has citado Stoneweg como sponsor (NO Kelpa)?
GEMSWELL LINT 3  — ¿La subsanación TCH3 dic-2025 está con efecto contable 31/12/2025 (NO en espera de RM)?
GEMSWELL LINT 4  — ¿El cap% MdL en TCH3 es 46,86% (36,45% IPN + 10,41% TCH2), NO 33,33% u otros?
GEMSWELL LINT 5  — ¿La cadena Quarter Capital / Grand View se atribuye a IPN directo (no TCIH) y se reconoce capitalizada en TCH3 dic-2025?
GEMSWELL LINT 6  — ¿Kelpa Expansión figura como acreedor (derecho de crédito de VM), NO como inversor / sponsor?
GEMSWELL LINT 7  — ¿VPSH se trata como entidad en latencia (activo 170€, PN -820€), NO como operativo?
GEMSWELL LINT 8  — ¿NAV VSO II 124,48% cita email Stoneweg/Ramón Romero 7-may-2026?
GEMSWELL LINT 9  — ¿La cuenta 17100011 PTMO Telcogestores está en pnc_otra (post-fix bug #14), NO pnc_bancario?
GEMSWELL LINT 10 — ¿El output respeta confidencialidad (no se mezcla con Olin / Templus / TCIH)?
GEMSWELL LINT 11 — ¿La calculadora /waterfall-gemswell consulta `waterfall_params` actualizados? Documentar discrepancias default BD (50M Kelpa debt / 30M equity / 200K fee) vs calculadora actual (74,7M / 49M / 925,5K).
GEMSWELL LINT 12 — ¿Has aplicado exención art. 21 LIS correctamente para flujos IPN/TCH2→TCH3 (sí aplica, ambos>5%)?
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
