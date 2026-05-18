# Cap table detallado — Gemswell (TCH3 → Valdorba Parques + SW Infrasports + cadena Quarter/Grand View)

> Snapshot 31/12/2025 · BD `savenikqhmcuwmcnabca` (`participations` + `shareholders` + `entities` + audit provisional TCH3 02/04/2026 + email Miguel 7-may-2026).

## Cadena completa MdL → surf parks + La Quinta

```
mdl-persona (Miguel de Lucas Sánchez)
  │ 100,00% Ordinarias
  ▼
IPN (Inteligencia Procesos de Negocio, SLU)
NIF: B87680328
  │
  ├─ 36,45% TCH3 (Ordinarias, 2.625.910 partic VN 1€) — directo
  │
  ├─ 100% TCH2 (Ordinarias)
  │     │
  │     └─ 10,41% TCH3 (Ordinarias, 750.000 partic VN 1€) — indirecto MdL
  │
  └─ 32,29% Quarter Capital (cadena lateral capitalizada en aumento TCH3 dic-2025)
        │ 100%
        ▼
     Grand View La Quinta, S.L.
     [Inversiones inmobiliarias Marbella — mayores 2018-2025
      cuentas 25200x + 5510x pendientes procesar García Ruiz]

                              ▼
TCH3 (TCH Tres Holding & Management, S.L.)
NIF: pendiente · Capital social 7.203.820€ (post-subsanación dic-2025)
Prima asunción 1.112.464€ · Activo 6.109.732€ · PN 304.469€ · Pasivo 5.805.262€
  │ Cap%: 36,45% IPN + 10,41% TCH2 = 46,86% MdL efectivo
  │
  │ ▼ 88% Valdorba Parques (Ordinarias)
  │       │  Activo 4,67M€ · PN 3,97M€
  │       │
  │       ├─ 100% Valdorba Metropolitano (VM)
  │       │      Activo 4,4M€ · PN 1,84M€ · Ingresos 2M€
  │       │      [Operativo — surf park urbano]
  │       │      │
  │       │      ├─ 0% Kelpa Expansión (DERECHO DE CRÉDITO, NO participación)
  │       │      │   Cuenta 17100011 PTMO TELCOGESTORES (250K€) reclasificada
  │       │      │   a pnc_otra por fix bug #14 (15-may-2026)
  │       │      │
  │       │      └─ 10,31% Madrid Playa Surf (MPS)
  │       │            mdl_effective_pct 4,25%
  │       │
  │       ├─ 100% Valdorba Parques Surf (VPS)
  │       │      Activo 4,05M€ · PN 4,01M€ · Capital 4,03M€
  │       │      [Vehículo del proyecto surf park resort]
  │       │
  │       └─ 100% Valdorba Parques Surfhotel (VPSH)
  │              Activo 170€ · PN -820€
  │              [SPV hotel en latencia]
  │
  ▼ 50% SW Infrasports (Ordinarias, 150 partic — Pacto Socios SHA nov 2024)
       │ 50% Stoneweg (150 partic, paritario)
       │ Sociedad gestora paraguas surf parks Gemswell
       │ mdl_effective_pct 23,44%
       │ Fee anual fijo 250.000€; promote 50% sobre carry compartimentos
       │
       └─ Compartimento VSO II (Wave Park):
             crédito face 1.000.000€ · NAV 124,48% · fair value 1.244.800€
```

## Cap table TCH3 — 12 socios

| Socio | Pool | Cap% | Partic | Notas |
|---|---|---|---|---|
| IPN | **Pool MdL** | **36,45%** | 2.625.910 | Aportación capital 2.625.910€ |
| MM Sports Servicios de Gestión SLU | MMS | **36,41%** | 2.622.910 | 2º socio principal — alineado con MdL |
| TCH2 | **Pool MdL** | **10,41%** | 750.000 | Aportación capital 750.000€ |
| Monforte Consultoría (MCT) | MCT | 5,55% | 400.000 | +300.000€ capitalizadas sept 2025 |
| I. Velilla | Teras | 2,78% | 200.000 | Adquiridas desde TCIH sept 2025 — condición suspensiva inscripción RM |
| Gurrea | Indep | 2,08% | 150.000 | +50.000€ cap sept 2025 |
| Gálvez | Indep | 1,94% | 140.000 | |
| Ramón Romero | Indep | 1,39% | 100.000 | Nuevo socio sept 2025 — capitalización deuda 100.000€ |
| LSS (LSS group) | LSS | 1,39% | 100.000 | |
| Lafarga | Indep | 0,69% | 50.000 | Nuevo socio sept 2025 — cap deuda 50.000€ |
| L. Osorio | Indep | 0,69% | 50.000 | |
| Faura | Indep | 0,21% | 15.000 | |
| **Total** | | **100,00%** | 7.203.820 | Capital social post-subsanación |

## Pools de socios — consolidado

| Pool | Cap% | Composición |
|---|---|---|
| **MdL** | **46,86%** | IPN 36,45% + TCH2 10,41% |
| **MM Sports** | **36,41%** | MMS SLU 36,41% |
| **MCT** | 5,55% | Monforte Consultoría 5,55% |
| **Teras (mgmt)** | 2,78% | I. Velilla 2,78% (condición suspensiva RM) |
| **Indeps** | ~9,00% | Gurrea 2,08 + Gálvez 1,94 + R. Romero 1,39 + Lafarga 0,69 + L. Osorio 0,69 + Faura 0,21 |
| **LSS** | 1,39% | LSS group 1,39% |

## Cap% efectivo MdL — composición look-through

| Nivel | Cálculo | Cap% MdL |
|---|---|---|
| MdL → IPN | 100% directo (persona física) | 100,00% |
| MdL → TCH2 | 100% IPN × 100% TCH2 | 100,00% |
| MdL → TCH3 directo (vía IPN) | 100% × 36,45% | 36,45% |
| MdL → TCH3 vía TCH2 | 100% × 100% × 10,41% | 10,41% |
| **MdL → TCH3 total efectivo** | 36,45 + 10,41 | **46,86%** |
| MdL → Valdorba Parques | 46,86% × 88% | **41,24%** |
| MdL → VM / VPS / VPSH | 41,24% × 100% (cadena Valdorba Parques 100%) | **41,24%** |
| MdL → SW Infrasports | 46,86% × 50% | **23,44%** |
| MdL → MPS (vía VM 10,31%) | 41,24% × 10,31% | **4,25%** |
| MdL → Quarter Capital (cadena lateral IPN) | 100% × 32,29% | **32,29%** |
| MdL → Grand View La Quinta | 32,29% × 100% | **32,29%** |

## Subgrupo Valdorba — cap table detalle

| Entidad | Matriz | % | Notas |
|---|---|---|---|
| Valdorba Parques | TCH3 | 88,00% | Cabecera subgrupo; 12% restante a otros (pendiente cap table detallado) |
| Valdorba Metropolitano (VM) | Valdorba Parques | 100,00% | Surf park urbano operativo |
| Valdorba Parques Surf (VPS) | Valdorba Parques | 100,00% | Surf park resort (en desarrollo) |
| Valdorba Parques Surfhotel (VPSH) | Valdorba Parques | 100,00% | SPV hotel asociado (latencia) |
| Madrid Playa Surf (MPS) | VM | 10,31% | Pipeline Madrid — equity-method en VM |
| Kelpa Expansión | (acreedor VM) | 0,00% | Derecho de crédito, NO participación |

## SW Infrasports — cap table

| Socio | Partic | % | Notas |
|---|---|---|---|
| TCH3 | 150 | 50,00% | Pacto Socios SHA nov 2024 |
| Stoneweg | 150 | 50,00% | Pacto Socios SHA nov 2024 |
| **Total** | **300** | **100,00%** | |

- Promote sobre carry compartimentos: 50% TCH3 / 50% Stoneweg (paritario).
- Fee anual fijo: 250.000€ a sociedad gestora.
- Compartimentos vehiculados: VSO II (Wave Park — crédito 1M€, NAV 124,48%), pipeline adicional.

## Cadena Quarter Capital → Grand View La Quinta

| Entidad | Matriz | % MdL look-through | Notas |
|---|---|---|---|
| Quarter Capital | IPN | 32,29% | Cap table real (no 33,33% por redondeo) — email Miguel 7-may-2026 |
| Grand View La Quinta | Quarter Capital | 100% × 32,29% = 32,29% | Inversiones inmobiliarias Marbella |

- **Decisión doctrinal** (Miguel 7-may-2026): "Todo esto se ha capitalizado en el aumento de capital TCH3 y nunca era una posición de TCIH". Para perímetro Gemswell se incluye; jurídicamente cuelga de IPN.
- Saldo intragrupo: cuenta 17100002 PTMO GRAND VIEW LA QUINTA → IPN acreedor por 1.519.092,12€ loan_lp.

## Notas críticas

1. El cap% MdL 46,86% incluye agregado IPN + TCH2 (ambos del pool MdL). Ambos individualmente >5%, por lo que cada uno tiene exención art. 21 LIS aplicable a flujos TCH3 → IPN y TCH3 → TCH2.
2. La condición suspensiva de inscripción RM sobre las 200.000 partic de I. Velilla (adq desde TCIH) puede alterar el cap% si se revierte. Prudencia hasta confirmación RM Q1-2026.
3. La subsanación capital dic-2025 con efecto contable 31/12/2025 explica que las cifras de cap table reflejan capital 7.203.820€, no 5.010.628€ pre-subsanación.
4. Para participations strictu sensu (BD `participations`), Quarter Capital y Grand View cuelgan de IPN, no de TCH3. Para reporting consolidado Gemswell se mencionan.
