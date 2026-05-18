# Documentos referencia — Gemswell

> Snapshot 31/12/2025 · Inventario de documentos clave para soporte del escenario Gemswell.

## 1. Audit provisional TCH3 — 02/04/2026 (B88547567)

| Atributo | Valor |
|---|---|
| Tipo | Auditoría provisional 2025 |
| Fecha | 02/04/2026 |
| Referencia | B88547567 |
| Firma auditora | (pendiente confirmar nombre) |
| Alcance | TCH3 + subgrupo Valdorba + cap table post-subsanación |
| Ubicación | `bl_documents` (etiqueta gemswell + tch3) |

**Cifras clave reconocidas**:
- Activo TCH3: 6.109.732,11€
- PN: 304.469,52€
- Pasivo: 5.805.262,59€
- Capital social post-subsanación: 7.203.820€
- Prima asunción total: 1.112.464€
- Efecto contable subsanación: retroactivo a 31/12/2025

**Uso**:
- Soporte cifras 2025 para informes banco, KYC, organigrama.
- Validación cap table post-capitalizaciones sept 2025.
- Override sobre cierre contable interno previo.

**Status**: provisional. Audit definitivo Q2 2026 pendiente.

## 2. Email Miguel de Lucas — 07/05/2026 (Quarter / Grand View capitalizados en TCH3)

| Atributo | Valor |
|---|---|
| Remitente | Miguel de Lucas (cliente) |
| Destinatario | TERAS Capital + CFO MdL |
| Fecha | 07/05/2026 |
| Asunto | Posición Quarter Capital + Grand View La Quinta (perímetro) |
| Ubicación | inbox + `bl_documents` |

**Contenido clave**:

> "Todo esto se ha capitalizado en el aumento de capital TCH3 y nunca era una posición de TCIH"

**Cifras override aportadas (a 31/12/2025)**:
- Quarter Capital: Activo 3.965.846€ · PN 3.298.655€ · Pasivo 667.191€
- Grand View La Quinta: Activo 4.391.565€ · PN 3.340.062€ · Pasivo 1.051.503€

**Decisiones doctrinales**:
1. Cadena Quarter Capital → Grand View La Quinta pertenece doctrinalmente a Gemswell (capitalizada en aumento TCH3 dic-2025).
2. Jurídicamente cuelga de IPN directo (32,29%), NO de TCH3 ni TCIH.
3. Cap% real Quarter Capital es 32,29% (NO 33,33% por redondeo "1/3").

**Pendientes mencionados**:
- Mayores 2018-2025 Quarter Capital + Grand View enviados a contable García Ruiz.
- Cuentas 25200x + 5510x pendientes procesar.

## 3. Email Stoneweg / Ramón Romero — 07/05/2026 (NAV VSO II 124,48%)

| Atributo | Valor |
|---|---|
| Remitente | Stoneweg (vía Ramón Romero) |
| Destinatario | TERAS Capital |
| Fecha | 07/05/2026 |
| Asunto | NAV no auditado compartimento VSO II Wave Park 31/12/2025 |
| Ubicación | inbox + `bl_documents` |

**Cifras clave**:
- NAV no auditado VSO II 31/12/2025: **124,48%**
- Crédito face value: 1.000.000€
- Fair value derivado: 1.244.800€ (1.000.000 × 1,2448)

**Uso**:
- Factor histórico registrado en BD `waterfall_params.vso_ii_unaudited_nav_pct`.
- Base de valoración para informes y exit scenarios.
- Fuente ÚNICA válida (no extrapolar variaciones sin email/comm posterior).

**Status**: NAV no auditado. Audit anual Wave Park / SW Infrasports pendiente Q4 2026 o posterior.

## 4. Pacto Socios SHA — SW Infrasports (noviembre 2024)

| Atributo | Valor |
|---|---|
| Tipo | Shareholders Agreement (SHA) |
| Fecha firma | noviembre 2024 |
| Partes | TCH3 (50%) + Stoneweg (50%) |
| Ubicación | `bl_documents` (etiqueta gemswell + sw-infrasports) |

**Términos económicos clave**:
- Cap%: 50/50 (150 partic cada uno, 300 totales).
- Fee anual fijo: 250.000€.
- Promote sobre carry compartimentos: 50% TCH3 (`tch3_promote_pct_swi`).
- Decisiones paritarias con mediación en bloqueo.

**Compartimentos vehiculados**:
- VSO II (Wave Park) — crédito face 1.000.000€.
- Pipeline adicional surf parks Iberia.

**Status**: en vigor. Sin modificaciones registradas a 31/12/2025.

## 5. Acuerdo Kelpa (acreedor de VM)

| Atributo | Valor |
|---|---|
| Tipo | Acuerdo de crédito (Loan agreement) |
| Partes | Kelpa Expansión + Valdorba Metropolitano (VM) |
| Ubicación | `bl_documents` (etiqueta gemswell + valdorba) |

**Naturaleza**:
- **Kelpa Expansión** es acreedor de VM (derecho de crédito), **NO inversor en TCH3 ni sponsor de Gemswell**.
- Tratamiento contable: pasivo financiero NO bancario (post fix bug #14 cuenta 17100011 250K€ a `pnc_otra`).

**Parámetros referencia para waterfall**:
- BD default `kelpa_debt_eur`: 50.000.000€
- BD default `kelpa_equity_eur`: 30.000.000€
- Total compartimento Kelpa default: 80M€ (= `business_lines.gemswell.total_investment`)

**Discrepancia con calculadora actual** (`/waterfall-gemswell`):
- Deuda: 74.700.000€ (calculadora actual)
- Equity: 49.000.000€ (calculadora actual)
- Total: 123,7M€

> Documentar en `decisiones-clave.md` la discrepancia entre parámetros BD default y calculadora actual.

## 6. Mayores PGC 2018-2025 — Quarter Capital + Grand View La Quinta

| Atributo | Valor |
|---|---|
| Tipo | Mayores PGC históricos |
| Período | 2018-2025 |
| Cuentas clave | 25200x (inversiones inmobiliarias) + 5510x (cuentas corrientes) |
| Estado | Enviados a contable García Ruiz, **pendientes procesar** |
| Ubicación | inbox + carpeta cliente |

**Pendientes**:
- Procesamiento completo por García Ruiz.
- Cierre formal Quarter Capital + Grand View 2025.
- Reconciliación con cifras override email Miguel 7-may-2026.

**Importancia**:
- Soporte fiscal cuentas 25200x (inversiones inmobiliarias Marbella en Grand View).
- Soporte fiscal cuentas 5510x (cuentas corrientes y saldos intragrupo).
- Audit definitivo de la cadena lateral Quarter / Grand View depende de este procesamiento.

## 7. Acta subsanación capital TCH3 (diciembre 2025)

| Atributo | Valor |
|---|---|
| Tipo | Acta de junta + escritura subsanación |
| Fecha firma acta | < 31/12/2025 (antes cierre fiscal) |
| Fecha elevación pública | enero 2026 |
| Fecha inscripción RM (esperada) | Q1 2026 (condición suspensiva I. Velilla) |
| Ubicación | Notaría + `bl_documents` |

**Contenido**:
- 1ª ampliación: compensación créditos IPN/MMS + crédito MPS — 1.343.000€ capital + 557.000€ prima.
- 2ª ampliación: dineraria — 850.000€ capital + 555.000€ prima.
- Capital social pre: 5.010.628€.
- Capital social post: 7.203.820€.
- Prima total post: 1.112.464€.

**Efecto contable**: retroactivo a 31/12/2025, reconocido en audit provisional 02/04/2026.

## 8. Comunicación cap table sept 2025

| Atributo | Valor |
|---|---|
| Tipo | Actas asamblea + documentación capitalizaciones |
| Fecha | septiembre 2025 |
| Ubicación | `bl_documents` + `shareholders` BD |

**Movimientos clave**:
- MCT (Monforte): +300K€ capitalizados → 5,55%.
- Gurrea: +50K€ → 2,08%.
- Ramón Romero (nuevo socio): cap deuda 100K€ → 1,39%.
- Lafarga (nuevo socio): cap deuda 50K€ → 0,69%.
- I. Velilla: adq desde TCIH 200K partic → 2,78% (condición suspensiva RM).

## 9. ISHA Gemswell (formal completo) — pendiente

| Atributo | Valor |
|---|---|
| Tipo | Investors and Shareholders Agreement (ISHA) Gemswell |
| Estado | Parcial / pendiente formalización completa |
| Términos preliminares conocidos | Hurdle 8%, promote 20%, mecánica capitalización créditos |
| Ubicación | `bl_documents` (parcial) |

**Pendientes en ISHA formal**:
- Vesting / leaver provisions detallados.
- Key-man (I. Velilla, equipo gestor TERAS).
- Drag-along / tag-along articulado.
- Mecánica supermayorías.
- Cláusulas exit y mecánica waterfall completa.

## 10. Documentación calculadora `/waterfall-gemswell`

| Atributo | Valor |
|---|---|
| Path UI | `/waterfall-gemswell` |
| Fuente parámetros | BD `waterfall_params` con prefijo gemswell |
| Componente edición | `<WaterfallFactorsPanel>` |
| Componente factor individual | `<EditableFactor>` |
| Discrepancias documentadas | Kelpa debt/equity, mgmt_fee, num_projects |

## Inventario consolidado de fuentes citables

| Fuente | Tipo | Uso |
|---|---|---|
| `business_lines.gemswell` (BD) | Cifra agregada | Cap% MdL, total investment, sponsor |
| `business_lines.quarter` (BD) | Cifra agregada | Cadena lateral Quarter Capital |
| `entities.tch3` (BD) | Entidad jurídica | NIF, año fiscal |
| `entities.valdorba-parques` etc (BD) | Entidad subgrupo | Cap%, balances |
| `entity_balances` 2025 (BD) | Cifras balance | Activo / PN / Pasivo por entidad |
| `participations` (BD) | Cap% jurídicos | Estructura societaria look-through |
| `shareholders` (BD) | Cap table | 12 socios TCH3 con %s y partic |
| `waterfall_params` (BD) | Factores calculadora | Hurdle, promote, fees, Kelpa params |
| `intragroup_balances` (BD) | Saldos intragrupo | Cuenta 17100002 Grand View → IPN, 17100011 Telcogestores |
| Audit provisional 02/04/2026 (B88547567) | Documento externo | Override cifras 2025 TCH3 |
| Email Miguel 7-may-2026 | Comunicación cliente | Decisión doctrinal Quarter/GV en Gemswell |
| Email Stoneweg/R. Romero 7-may-2026 | Comunicación sponsor | NAV VSO II 124,48% |
| Pacto Socios SHA SW Infrasports nov 2024 | Acuerdo formal | JV 50/50 |
| Acuerdo Kelpa | Acuerdo formal | Deuda VM, parámetros referencia waterfall |
| Mayores 2018-2025 García Ruiz | Documentación contable | Pendiente procesar cuentas 25200x + 5510x |
| Acta subsanación dic-2025 | Documento societario | Cap social post 7.203.820€ |
