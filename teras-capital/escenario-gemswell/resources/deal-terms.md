# Deal terms — Gemswell (TCH3 + Valdorba subgrupo + SW Infrasports + Kelpa)

> Snapshot 31/12/2025 · BD `savenikqhmcuwmcnabca` (`waterfall_params`) + ISHA Gemswell + Pacto Socios SHA SW Infrasports nov 2024 + Acuerdo Kelpa + audit provisional TCH3 02/04/2026 (B88547567).

## Subsanación capital TCH3 — diciembre 2025 (operación estructurante)

Operación contable y societaria que define el snapshot 31/12/2025 de TCH3. Acta firmada antes 31/12/2025, elevación pública enero 2026, audit provisional 02/04/2026 reconoce efecto contable retroactivo.

### Estructura de las dos ampliaciones simultáneas

| Ampliación | Mecanismo | Capital nuevo | Prima asunción | Total |
|---|---|---|---|---|
| 1ª — Compensación de créditos intragrupo | Capitalización deuda IPN/MMS + crédito MPS | 1.343.000€ | 557.000€ | 1.900.000€ |
| 2ª — Dineraria | Aportación efectiva en metálico | 850.000€ | 555.000€ | 1.405.000€ |
| **Total ampliaciones** | | **2.193.192€** | **1.112.000€** | **3.305.192€** |

### Cifras pre y post

| Concepto | Pre-subsanación | Post-subsanación | Var |
|---|---|---|---|
| Capital social TCH3 | 5.010.628€ | **7.203.820€** | +2.193.192€ |
| Prima asunción total | 0€ (o residual previo) | 1.112.464€ | +1.112.464€ |
| Resultados anteriores | -8.011.815€ | absorbidos / netos | reorganización |
| Patrimonio neto | (PN cero o negativo previo) | 304.469,52€ | reorganizado |

### Capitalización deuda — socios concretos sept 2025

| Socio | Nuevo cap (€) | Notas |
|---|---|---|
| MCT (Monforte) | +300.000 | Capitalización créditos |
| Gurrea | +50.000 | Capitalización créditos |
| Ramón Romero | +100.000 | Nuevo socio sept 2025 — capitalización deuda |
| Lafarga | +50.000 | Nuevo socio sept 2025 — capitalización deuda |
| I. Velilla | +200.000 | Adquisición desde TCIH (condición suspensiva RM) |

### Decisión doctrinal — efecto contable a 31/12/2025

> Acta de subsanación firmada antes del 31/12/2025, elevación pública en enero 2026. Auditoría provisional de 02/04/2026 (B88547567) reconoce el efecto contable retroactivo a 31/12/2025. La inscripción RM (Q1-2026) es formalidad posterior; el cierre 2025 ya incorpora capital social 7.203.820€.

Es decisión doctrinal del cliente: **NO esperar a inscripción RM** para reconocer la subsanación en cifras de cierre 2025.

## ISHA Gemswell — términos económicos

### Hurdle y promote

- **Hurdle ISHA Gemswell**: 8% sobre capital invertido (`waterfall_params.hurdle_rate_pct = 8.0`, acuerdo socios Gemswell).
- **Promote sobre exceso**: 20% (`waterfall_params.promote_pct = 20.0`).
- Aplicable a flujos de exit / distribución por encima del hurdle, repartido entre socios pro-rata cap% (menos promote).

### Fee gestión por proyecto

- **BD default**: 200.000€ por proyecto (`waterfall_params.mgmt_fee_per_project_eur`).
- **Calculadora actual** (`/waterfall-gemswell`): 925.500€ alternativo. Discrepancia documentada en `decisiones-clave.md`.

### Estructura Kelpa — referencias de cálculo

| Parámetro | BD default | Calculadora actual | Fuente |
|---|---|---|---|
| Deuda Kelpa | 50.000.000€ | 74.700.000€ | `waterfall_params.kelpa_debt_eur` + Acuerdo Kelpa |
| Equity Kelpa | 30.000.000€ | 49.000.000€ | `waterfall_params.kelpa_equity_eur` |
| Total compartimento | 80.000.000€ | 123.700.000€ | derivado |
| Num proyectos default | 2 | 2 | `waterfall_params.num_projects` |
| Transaction costs | 1,5% | 1,5% | `waterfall_params.tx_costs_pct` |

> NOTA: el **techo Gemswell** declarado en `business_lines.gemswell.total_investment = 80.000.000€` coincide con la suma deuda + equity Kelpa default BD (50M + 30M). La calculadora actual usa parámetros distintos a documentar.

## Pacto Socios SHA SW Infrasports — noviembre 2024

### Estructura JV

- Sociedad gestora paraguas de los proyectos surf parks Gemswell.
- Participación: **50% TCH3 / 50% Stoneweg** (150 partic cada uno, total 300).
- Decisiones paritarias con resolución de conflictos vía mediación.

### Términos económicos SHA

| Concepto | Valor | BD param |
|---|---|---|
| Fee anual fijo | 250.000€ | `swi_fixed_fee_eur` |
| Promote sobre carry compartimentos — TCH3 | 50% | `tch3_promote_pct_swi` |
| Promote sobre carry compartimentos — Stoneweg | 50% | (derivado) |
| Cap% TCH3 en SW Infrasports | 50% | `swi_tch3_pct` |

### Compartimentos vehiculados

- **VSO II (Wave Park)**: crédito face 1.000.000€ — Acuerdo TCH3 con compartimento Wave Park.
  - NAV no auditado 31/12/2025: **124,48%** (email Stoneweg / Ramón Romero 7-may-2026).
  - Fair value derivado: 1.244.800€.
- **Pipeline adicional**: surf parks operativos y en desarrollo Iberia.

## Acuerdo Kelpa — naturaleza

**Kelpa Expansión** es **acreedor** de Valdorba Metropolitano (NO inversor en TCH3, NO sponsor de Gemswell).

- Estructura: derecho de crédito frente a VM con condiciones específicas.
- Tratamiento contable: pasivo financiero NO bancario (fix bug #14: cuenta 17100011 PTMO TELCOGESTORES 250K€ reclasificada de `pnc_bancario` a `pnc_otra`).
- **Sponsor real del proyecto industrial**: Stoneweg (vía SW Infrasports).

## Cap structure efectiva — paquetes económicos

### Para TCH3 (vehículo MdL)

- **Ordinarias** únicas, sin clases de privilegio dentro de TCH3 (a diferencia de TCH1 con Class A/B + Privilegiadas).
- Distribución pro-rata cap% para retornos ordinarios.
- Promote ISHA 20% sobre exceso hurdle aplica sobre el agregado.

### Para Valdorba Parques (88% TCH3)

- TCH3 mayoritario 88%; 12% restante a otros (pendiente cap table detallado en BD).
- Estructura simple sin tramos diferenciados.

### Para SW Infrasports (50/50 TCH3-Stoneweg)

- Paritario absoluto en capital.
- Carry compartimentos: 50/50.
- Fee anual: 250.000€ a sociedad gestora (operativa).

## Mecánica de retornos — perfil esperado

Distribución esperada en orden:

1. **Servicio deuda Kelpa** (compartimento VM): default debt 50M€ (BD) / 74,7M€ (calculadora actual).
2. **Retorno capital invertido** TCH3 + socios externos.
3. **Hurdle 8%** sobre capital invertido (catch-up para socios).
4. **Promote 20%** sobre exceso para mgmt / promote vehicle.
5. **Distribución pro-rata** restante sobre cap%.
6. **Fee anual SW Infrasports** 250.000€ recurrente.
7. **Fee por proyecto** 200.000€ (BD default) / 925.500€ (alt) recurrente operativo.

## Investment timeline

| Hito | Fecha | Notas |
|---|---|---|
| Constitución TCH3 | (anterior 2022) | NIF pendiente confirmar |
| Pacto Socios SHA SW Infrasports | nov 2024 | JV 50/50 con Stoneweg |
| Capitalización deuda socios | sept 2025 | MCT +300K, Gurrea +50K, R. Romero +100K, Lafarga +50K, Velilla +200K (RM pte) |
| Acta subsanación capital TCH3 | < 31/12/2025 | Firmada antes cierre |
| Cierre contable 2025 (efecto subsanación) | 31/12/2025 | Capital 7.203.820€ |
| Elevación pública subsanación | ene-2026 | Notaría |
| Audit provisional B88547567 | 02/04/2026 | Reconoce efecto retroactivo |
| Inscripción RM (esperada) | Q1-2026 | Condición suspensiva I. Velilla |
| Fix bug #14 cuenta 17100011 | 15-may-2026 | parser_fix_bug14 |
| Email Stoneweg / R. Romero NAV VSO II 124,48% | 07-may-2026 | Soporte valoración |
| Email Miguel — capitalización Quarter/Grand View en TCH3 | 07-may-2026 | Decisión doctrinal |

## Leaver provisions, vesting, key-man

A documentar en cuanto se reciba ISHA Gemswell formal completo. Términos preliminares conocidos:

- Vesting de partic adicionales para nuevos socios sept 2025 (R. Romero, Lafarga) condicionado a permanencia / hitos.
- Key-man del equipo gestor TERAS (I. Velilla) protegido por condición suspensiva RM sobre 200K partic.
- Drag-along / tag-along: pendiente articulado ISHA.
