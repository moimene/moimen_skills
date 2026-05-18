# Decisiones clave — Gemswell

> Snapshot 31/12/2025 · Decisiones técnicas, contables, legales y doctrinales que definen el escenario Gemswell.

## D-1. Subsanación capital TCH3 — efecto contable 31/12/2025 (NO RM)

- **Decisión**: la subsanación de capital social de TCH3 de diciembre 2025 tiene **efecto contable retroactivo a 31/12/2025**, independientemente de la inscripción RM (esperada Q1-2026).
- **Justificación**: acta firmada antes 31/12/2025 + elevación pública ene-2026 + auditoría provisional 02/04/2026 (B88547567) que reconoce el efecto.
- **Implicación**: cifras de cierre 2025 de TCH3 incorporan capital social **7.203.820€** (post) y NO 5.010.628€ (pre).
- **Quién decide**: Audit firm + CFO TERAS + CLO + cliente. Decisión doctrinal del grupo.
- **Source**: audit_2026_provisional + decisión interna documentada.
- **Riesgo**: si RM impugna o demora más de lo previsto, podría requerir ajustes. Mitigante: audit provisional confirma + acta firmada antes cierre.

## D-2. Override audit 02/04/2026 (B88547567) sobre cifras balanceadas

- **Decisión**: cifras de TCH3 31/12/2025 son las del audit provisional 02/04/2026, NO las del cierre contable interno previo.
- **Cifras override**:
  - Activo: 6.109.732,11€
  - PN: 304.469,52€
  - Pasivo: 5.805.262,59€
- **Implicación**: cualquier reporting interno o externo (informes banco, KYC, organigrama) usa las cifras audit, no las contables raw.
- **Source**: audit B88547567 + decisión CFO.

## D-3. Capitalización créditos IPN/MMS en 1ª ampliación

- **Decisión**: la primera ampliación de la subsanación dic-2025 capitalizó créditos intragrupo de IPN y MMS (y crédito MPS) por **1.343.000€ capital + 557.000€ prima**.
- **Justificación**: limpiar pasivo intragrupo TCH3, reforzar PN, preparar exits / refinanciaciones.
- **Implicación**:
  - IPN y MMS ven sus créditos convertidos en participaciones adicionales TCH3.
  - El crédito MPS (Madrid Playa Surf) capitalizado en la prima traslada riesgo deterioro del crédito a coste adquisición participaciones.
  - Pasivo TCH3 post-subsanación residual 5,8M€ es créditos intragrupo Valdorba subgrupo **NO compensados** (pendientes capitalización futura).
- **Source**: audit provisional 02/04/2026 + acta subsanación.

## D-4. Fix bug #14 (15-may-2026) — cuenta 17100011 reclasificada

- **Decisión**: la cuenta **17100011 PTMO TELCOGESTORES SERVICIOS DE GESTION (250.000€)** se reclasifica de `pnc_bancario` a `pnc_otra` por ser tercero **NO bancario**.
- **Justificación**: bug del clasificador PGC `pc_bancario` que mal clasificaba la cuenta como deuda bancaria. Telcogestores es entidad de servicios, no banco.
- **Aplicado en**: TCH3 y TCH4 (parser_fix_bug14).
- **Implicación**: la deuda bancaria reportada de TCH3 al banco se reduce en 250K€. Es deuda intragrupo / con tercero NO bancario.
- **Fecha**: 15-may-2026.
- **Source**: parser_fix_bug14 + decisión CFO + audit firm.

## D-5. NAV VSO II 124,48% — factor histórico registrado

- **Decisión**: registrar el NAV no auditado del compartimento VSO II (Wave Park) a 31/12/2025 como **124,48%** en `waterfall_params`.
- **Justificación**: única fuente válida es email Stoneweg / Ramón Romero del **07-may-2026**. No extrapolar variaciones sin comunicación posterior.
- **Implicación**:
  - Fair value derivado del crédito face 1.000.000€ = **1.244.800€**.
  - Factor histórico calibrado para la calculadora `/waterfall-gemswell` y exit scenarios.
  - Cualquier informe de valoración usa este valor con cita del email como fuente.
- **Source**: email Stoneweg / Ramón Romero 7-may-2026 + `waterfall_params.vso_ii_unaudited_nav_pct`.

## D-6. Quarter Capital / Grand View capitalizados en TCH3 — perímetro doctrinal Gemswell, jurídico IPN

- **Decisión**: la cadena Quarter Capital → Grand View La Quinta pertenece **doctrinalmente al perímetro Gemswell** (capitalizada en aumento de capital TCH3 dic-2025) aunque **jurídicamente cuelga de IPN directo (32,29%)**.
- **Justificación**: email Miguel de Lucas del **07-may-2026**: *"Todo esto se ha capitalizado en el aumento de capital TCH3 y nunca era una posición de TCIH"*.
- **Implicación**:
  - Para informes consolidados Gemswell: se incluye Quarter Capital + Grand View La Quinta.
  - Para `participations` strictu sensu (BD): la cadena cuelga de IPN, no de TCH3.
  - Cap% MdL look-through: 32,29% (no 33,33% como se decía antes por redondeo "1/3").
  - NO se sitúa en TCIH bajo ninguna circunstancia.
- **Source**: email Miguel 7-may-2026 + decisión doctrinal cliente.

## D-7. Sponsor Gemswell = Stoneweg (NO Kelpa)

- **Decisión**: el sponsor industrial / financiero de Gemswell es **Stoneweg**, NO Kelpa.
- **Justificación**:
  - Campo `business_lines.gemswell.sponsor = "Stoneweg"` en BD.
  - Pacto Socios SHA SW Infrasports nov 2024 con Stoneweg como contraparte 50/50.
  - **Kelpa Expansión** es **acreedor** (derecho de crédito frente a Valdorba Metropolitano), NO inversor en TCH3 ni partner industrial.
- **Implicación**:
  - Todos los informes deben citar Stoneweg como sponsor.
  - Kelpa figura como acreedor de VM con condiciones específicas (Acuerdo Kelpa).
  - Comité Kelpa es ad-hoc / semestral, NO governance principal.
- **Source**: BD `business_lines.gemswell.sponsor` + Pacto Socios SHA nov 2024 + Acuerdo Kelpa.

## D-8. Cap% MdL en TCH3 = 46,86% efectivo (NO 33,33% ni otros valores)

- **Decisión**: el cap% efectivo look-through de MdL en TCH3 es **46,86%** (IPN 36,45% directo + TCH2 10,41% indirecto).
- **Justificación**: cap table validado por audit provisional 02/04/2026 + cifras BD `business_lines.gemswell.mdl_position_pct = 46,86%` + `business_lines.gemswell.mdl_position_description`.
- **Implicación**:
  - Para informes: citar 46,86% como cap% MdL en TCH3.
  - 36,45% + 10,41% = 46,86% (no 46,86% por casualidad, es agregado real).
  - Pool MdL + MM Sports (36,41%) = 83,27% conjunto (mayoría sólida).
- **Source**: BD `business_lines.gemswell` + cap table audit + audit provisional.

## D-9. Capitalizaciones sept 2025 — nuevos socios y aumentos

- **Decisión**: en septiembre 2025 se realizaron varias capitalizaciones que alteraron el cap table TCH3:
  - **MCT (Monforte)**: +300.000€ capitalizadas → llega a 5,55%.
  - **Gurrea**: +50.000€ → 2,08%.
  - **Ramón Romero (nuevo socio)**: capitalización deuda 100.000€ → 1,39%.
  - **Lafarga (nuevo socio)**: capitalización deuda 50.000€ → 0,69%.
  - **I. Velilla**: adquisición desde TCIH de 200.000 partic → 2,78%, condición suspensiva inscripción RM.
- **Implicación**: cap table sept 2025 → dic 2025 (post-subsanación) refleja estos movimientos.
- **Source**: BD `shareholders` + audit provisional.

## D-10. Pasivo TCH3 5,8M€ es intragrupo NO compensado

- **Decisión**: el pasivo de 5.805.262,59€ de TCH3 post-subsanación es **mayoritariamente intragrupo** (créditos del subgrupo Valdorba **NO compensados** en la subsanación dic-2025).
- **Justificación**: la 1ª ampliación capitalizó solo IPN/MMS + crédito MPS. Los créditos del subgrupo Valdorba quedaron pendientes de capitalización futura.
- **Implicación**:
  - Para informes banco: NO confundir con deuda bancaria (que es 0€).
  - Trabajo futuro pendiente: capitalización selectiva créditos restantes 2026-2027.
- **Source**: audit provisional + análisis CFO.

## D-11. Total investment Gemswell 80M€ = techo (coincide deuda+equity Kelpa default)

- **Decisión**: el `business_lines.gemswell.total_investment = 80.000.000€` se interpreta como **techo agregado** del proyecto, coincidente con la suma deuda Kelpa default (50M€) + equity Kelpa default (30M€).
- **Implicación**:
  - 80M€ NO es inversión real ejecutada de MdL ni de TCH3, sino techo de compromiso del proyecto industrial.
  - Inversión real ejecutada por TCH3 = capital social aportado + créditos otorgados al subgrupo (≈ activo TCH3 6,1M€ desglosado).
  - Calculadora actual usa 74,7M / 49M (distinto al default). Documentar discrepancia.
- **Source**: BD `business_lines.gemswell.total_investment` + `waterfall_params`.

## D-12. SW Infrasports — JV 50/50 con Stoneweg (Pacto Socios SHA nov 2024)

- **Decisión**: SW Infrasports es **JV paritaria 50/50** TCH3-Stoneweg, sociedad gestora paraguas de los proyectos surf parks Gemswell.
- **Términos económicos clave**:
  - 150 partic cada uno (300 totales).
  - Fee anual fijo 250.000€.
  - Promote 50% sobre carry compartimentos para TCH3 (`tch3_promote_pct_swi`).
- **Implicación**:
  - Decisiones paritarias con mediación en bloqueo.
  - mdl_effective_pct 23,44% (46,86% × 50%).
  - SW Infrasports vehicula VSO II (Wave Park) y pipeline adicional.
- **Source**: Pacto Socios SHA nov 2024 + BD `waterfall_params`.

## Discrepancias documentadas pendiente resolver

| Parámetro | BD default | Calculadora actual | Acción |
|---|---|---|---|
| Kelpa debt | 50.000.000€ | 74.700.000€ | Alinear con Acuerdo Kelpa actualizado |
| Kelpa equity | 30.000.000€ | 49.000.000€ | Alinear con Acuerdo Kelpa actualizado |
| mgmt_fee_per_project | 200.000€ | 925.500€ | Confirmar fee real vs proyectado |

## Decisiones operativas registradas

- VPSH (Valdorba Parques Surfhotel) tratado como **SPV en latencia** (activo 170€, PN -820€). Cierre operativo proyectado Q3-Q4 2026.
- VPS (Valdorba Parques Surf) tratado como **vehículo en desarrollo** sin ingresos operativos a 31/12/2025.
- VM (Valdorba Metropolitano) es el **único entidad operativa** del subgrupo Valdorba con ingresos significativos (2M€).
- MPS (Madrid Playa Surf, 10,31% vía VM) en **pipeline / desarrollo**.

## Trazabilidad — quién decidió qué y cuándo

| Decisión | Fecha | Quién | Soporte |
|---|---|---|---|
| Subsanación efecto 31/12/2025 | < 31/12/2025 | Consejo TCH3 + CFO | Acta + audit provisional 02/04/2026 |
| Capitalización créditos IPN/MMS | dic-2025 | Asamblea TCH3 | Acta subsanación + audit |
| Override cifras audit 02/04/2026 | 02-abr-2026 | CFO + audit firm | Audit provisional B88547567 |
| NAV VSO II 124,48% | 07-may-2026 | Stoneweg / Ramón Romero | Email Stoneweg/R. Romero |
| Quarter/Grand View en perímetro Gemswell | 07-may-2026 | Miguel de Lucas | Email Miguel |
| Fix bug #14 cuenta 17100011 | 15-may-2026 | CFO + parser team | parser_fix_bug14 + audit |
| Capitalizaciones sept 2025 (MCT, Gurrea, R. Romero, Lafarga, Velilla) | sept-2025 | Asamblea TCH3 | Acta + BD shareholders |
