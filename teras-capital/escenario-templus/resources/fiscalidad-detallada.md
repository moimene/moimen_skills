# Fiscalidad detallada — Templus

> Snapshot 31/12/2025 · LIS + NRV 19ª PGC + jurisprudencia TJUE/TS + ISHA Vesta 11/10/2023 + Enmienda 11/12/2025 + Financing Agreement Vesta 11/12/2025.

## 1. Art. 21 LIS — exención dividendos / plusvalías inversión grupo

### Test de aplicabilidad por eslabón en cadena Templus

| Eslabón | Cap% | ≥5%? | Art. 21 LIS aplica? |
|---|---|---|---|
| MdL persona → IPN | 100% | sí | N/A (persona física) |
| IPN → TCH4 | 17,00% | sí | **SÍ** (dividendos/plusvalías TCH4 exentas en IPN) |
| TCH2 → TCH4 | 15,60% | sí | **SÍ** |
| **TCH4 → Vesta Invest** | **2,00%** | **NO (<5%)** | **NO** (dividendos Vesta gravados 25% en TCH4) |
| Vesta → Templus CD | 96,00% | sí | SÍ (interno chain ICG, régimen LU SOPARFI parcial) |
| **TCIH → Templus CD directo (Path 2)** | **2,00%** | **NO (<5%)** | **NO** (dividendos Templus CD gravados 25% en TCIH) |
| Templus CD → 7 filiales España | 100% | sí | SÍ (interno chain Templus CD) |
| Templus CD → AE Group HoldCo II | (vía TCH4) | — | (estructura paralela vía TCH4 directamente) |
| AE Group HoldCo II → 4 Roosevelt | 100% | sí | SÍ (interno chain Project Colorado) |

### Implicación práctica (CRÍTICO)

**Doble peaje fiscal del 25% en cadena Templus**:

1. **TCH4 paga 25% IS sin exención** sobre dividendos/plusvalías Vesta. Confirmado en BD `waterfall_params.is_rate_tch4_pct=25, source='LIS art. 21 — sin exención (<5%)'`.
2. **TCIH paga 25% IS sin exención** sobre dividendos/plusvalías Templus CD vía Path 2 directo. Confirmado en BD.

**ÚNICO escudo fiscal de TCH4**:
- Los intereses del préstamo Vesta → TCH4 al 8% (saldo 976.756,13€ cuenta 17100000) son **deducibles** en IS TCH4.
- Reducen base imponible TCH4 y compensan parcialmente el 25% IS sobre cualquier flujo desde Vesta.
- Estimación intereses anuales: 976.756 × 8% ≈ 78.140€/año deducibles.
- Si saldo crece con tranches sucesivas Financing Agreement, el escudo aumenta proporcionalmente.

**TCIH NO tiene escudo equivalente para Path 2**:
- No hay préstamo Vesta → TCIH (TCIH adquirió 2% Templus CD directamente, sin financiación intermediada).
- TCIH paga 25% íntegro sobre cualquier flujo Templus CD del Path 2.
- Mitigante: TCIH tiene otros pasivos que generan intereses deducibles agregados.

### Aguas arriba en cadena MdL

- Cualquier flujo desde TCH4 → IPN/TCH2: **exención art. 21 LIS** (ambos >5%).
- Cualquier flujo desde TCIH → IPN/TCH2 (vía dividendo TCIH): **exención art. 21 LIS** (TCH2 25,83% en TCIH; MdL persona 25,83% directo).
- El "peaje fiscal" 25% se paga UNA VEZ en TCH4 (Path 1) o TCIH (Path 2), no doble imposición arriba.

### Cálculo en escenarios exit

- **Sale price 400M€ (escenario base ICG)** → equity surplus distribuible ~100M€ (sobre hurdle 300M€).
- Combinación de flujos a TCH4 (Path 1) + TCIH (Path 2) con sus respectivos 25% IS sin exención.
- En IPN/TCH2 puede aplicar exención art. 21 → flujo neto MdL ~5,2M€ (`exit_scenarios.mdl_net_return` para 400M€ base).
- Mitigante adicional: si Financing Agreement Vesta acumula intereses grandes hasta exit, reduce base IS TCH4.

## 2. NRV 19ª PGC — Inversiones en empresas grupo / multigrupo / asociadas

### Tratamiento contable TCH4 sobre Vesta

- TCH4 valora inversión en Vesta Invest como **inversión grupo** (≥20% control conjunto / influencia significativa NO se cumple, ya que TCH4 tiene 2,00% capital).
- Sin embargo, los derechos económicos modulados por ISHA Class B + Class D pueden encajar como **vinculada/asociada** según interpretación auditor.
- Valoración: **coste histórico menos deterioro** (no consolidación, NO valor razonable salvo deterioro).
- Cualquier dividendo se reconoce como ingreso financiero ordinario.
- Cualquier plusvalía sólo se reconoce al desinvertir (NO se anticipa).

### Tratamiento contable TCIH sobre Templus CD (Path 2)

- TCIH valora su 2% directo en Templus CD como NRV 19ª (mismo tratamiento que TCH4 sobre Vesta).
- Sin control (2% < 20%), sin influencia significativa salvo derechos económicos Class B directo.
- Coste histórico menos deterioro.

### Implicación para informes consolidados

- TCH4 NO consolida Vesta (cap% 2% no llega a control).
- TCH4 NO consolida AE Group HoldCo II (pendiente confirmar — referencia tarea #9 BD MdL).
- TCIH NO consolida Templus CD vía Path 2 (cap% 2% directo).
- Vesta consolida Templus CD (96% control) en su consolidado LU SOPARFI.
- Templus CD consolida las 7 filiales España (100% cada una).

### Fair value implícito

Cualquier informe del grupo MdL sobre Templus debe distinguir:
- **Valor contable TCH4**: coste 677.653€ (atribución MdL) menos deterioro si aplica.
- **Valor contable TCIH (Path 2)**: coste invertido en 2% Templus CD directo (referencia pendiente confirmar).
- **Fair value implícito look-through** (a NAV PN): 1,62% × 177,2M€ PN Templus CD ≈ 2,87M€ a NAV PN (no a NAV exit).

## 3. IS — Impuesto de Sociedades

| Entidad | Régimen | Tipo | Notas |
|---|---|---|---|
| TCH4 | General | 25% | **Sin exención art. 21 en dividendos Vesta**. Escudo: intereses Vesta 8% deducibles |
| IPN | General | 25% | Exención art. 21 sobre TCH4 (17%) |
| TCH2 | General | 25% | Exención art. 21 sobre TCH4 (15,60%) |
| TCIH | General | 25% | **Sin exención art. 21 en dividendos Templus CD Path 2**. Sin escudo equivalente |
| Vesta Invest | Luxemburgo (S.à r.l.) | Régimen LU SOPARFI (parcial) | Estructuración fiscal de eficiencia. ICG-controlled |
| Templus CD | General España | 25% | Consolida 7 filiales España |
| AE Group HoldCo II | Luxemburgo (S.à r.l.) | Régimen LU SOPARFI | Project Colorado vehiculado |
| 7 filiales España | General | 25% | Consolidadas por Templus CD |
| 4 Roosevelt | Local (IT/NL/DK/FR) | Local | Consolidadas por AE Group HoldCo II |

> **SOPARFI Luxemburgo** permite estructuración eficiente: dividendos / plusvalías entre LU + España con tratado de doble imposición; ICG estructura el commit 300M€ aprovechando régimen LU para Project Colorado pan-europeo y Templus CD inversión grupo.

## 4. Préstamo Vesta → TCH4 (8%) — análisis fiscal detallado

### Tratamiento como deuda equity-rank (NO bancario)

- **Cuenta 17100000 PTMO VESTA INVEST S.A.R.L.**: 976.756,13€ saldo 31/12/2025.
- **Fix bug parser #14 (mayo 2026)**: reclasificado de `pnc_bancario` a `pnc_otra`. Vesta es sponsor ICG externo (no banco).
- **Tipo 8% anual**: Financing Agreement 11/12/2025.
- **Tratamiento contable**: pasivo financiero TCH4 con Vesta. Equity-rank socio según ISHA (Vesta es socio + acreedor financiero combinado).
- **Tratamiento fiscal**: intereses 8% son **gasto financiero deducible** en IS TCH4. Reducen base imponible.

### Riesgo recalificación intereses como dividendo encubierto

- **Hacienda podría recalificar** los intereses 8% como dividendo encubierto si:
  - Tipo 8% se considera superior al mercado.
  - Hay vinculación demostrada (Vesta es socio Class A en Templus CD + socio prestamista de TCH4 — relación vinculada PGC).
  - Falta sustancia económica financiera (operación intra-grupo sin facility comercial real).
- **Mitigante**:
  - Sustancia financiera documentada en Financing Agreement 11/12/2025.
  - Tipo 8% justificable vs mercado mezzanine equivalente.
  - Vesta es socio de Templus CD (96%), no socio directo TCH4 — argumento de no-vinculación parcial.
- **Probabilidad**: Baja. **Impacto**: Alto si materializa (intereses pasan a no deducibles).

### Operaciones vinculadas — PGC

- TCH4 y Vesta están vinculados por: Vesta es matriz Templus CD (96%) y TCH4 socio Class B Vesta (2%) + prestatario.
- Documentación operaciones vinculadas debe reflejar tipo de mercado + comparables.
- Opinion letter asesor fiscal pendiente actualizar.

## 5. Subrogación deuda Asterion 2,10M€ en TCIH — fiscalidad

- (Nota: la subrogación Asterion en TCIH afecta a línea Olin, no directamente a Templus. Sin embargo, TCIH es vehículo MdL en cadena que también tiene 2% directo Templus CD Path 2).
- La subrogación NO afecta a Path 2 Templus CD directamente.
- Fiscalidad TCIH sobre Templus CD (Path 2): 25% IS sin exención sobre dividendos/plusvalías.

## 6. Exit fiscal MdL — escenarios

### Vía dividendo Vesta → TCH4 → IPN/TCH2 (Path 1)

- Vesta distribuye → TCH4 paga 25% IS sin exención (mitigado parcialmente por escudo intereses 8%) → IPN/TCH2 reciben con exención art. 21.
- Tasa efectiva total Path 1: ~25% sobre flujo neto post-escudo (un solo nivel).

### Vía dividendo Templus CD → TCIH → IPN/TCH2 (Path 2)

- Templus CD distribuye → TCIH paga 25% IS sin exención (sin escudo equivalente) → IPN/TCH2 reciben con exención art. 21 sobre TCIH.
- Tasa efectiva total Path 2: ~25% sobre flujo (un solo nivel).

### Vía venta TCH4 en Vesta (transferencia paquete Class B + Class D)

- TCH4 vende participaciones Vesta → realiza plusvalía → 25% IS sin exención sobre ganancia.
- IPN/TCH2 venden TCH4 → exención art. 21 LIS sobre ganancia (≥5% MdL en TCH4).
- Tasa efectiva Path 1: ~25% una vez.

### Vía venta TCIH en Templus CD directo (Path 2)

- TCIH vende 2% directo Templus CD → plusvalía 25% IS sin exención.
- IPN/TCH2 venden TCIH → exención art. 21 LIS.
- Tasa efectiva Path 2: ~25% una vez.

### Vía exit Class C (Templus Managers)

- Sweet equity 5% upside Class C: aplica a Templus Mgrs directamente, no a TCH4 o TCIH MdL.
- No genera flujo a MdL.

### Reinversión en otra línea TERAS (Olin / Gemswell)

- Mecanismo: TCH4 o TCIH reinvierte en TCH1 (Olin) o TCH3 (Gemswell) con ≥5% mantiene exención.
- Cuidado: Olin TCH1 también <5% en TUCA → mismo problema fiscal aguas abajo (peaje 25% en TCH1).
- Gemswell TCH3 → Kelpa: pendiente analizar cap% (referencia `escenario-gemswell`).

## 7. Riesgos fiscales

| # | Riesgo | P | I | Mitigante |
|---|---|---|---|---|
| 1 | Hacienda recalifica préstamo Vesta 8% como dividendo encubierto → no deducible | B | A | Sustancia financiera Financing Agreement + tipo comparables mercado + opinion letter |
| 2 | TJUE / TS jurisprudencia restringe encadenamiento exención (cláusula "general anti-elusión") cadena IPN/TCH2 → TCH4 | B | A | Asesoría continua + sustancia operativa real |
| 3 | Cambio LIS art. 21 (reforma cap% o ámbito exención) | B | A | Lobby + planificación contingente |
| 4 | LU SOPARFI restricciones futuras EU (BEPS pilar 2 / GloBE) afectan Vesta + AE HoldCo II | M | M | Monitor + estructura compatible |
| 5 | Calificación NRV 19ª pone en duda exención art. 21 IPN/TCH2 → TCH4 si auditor lo califica como mero financiero | B | M | Opinion letter asesor + sustancia económica documentada |
| 6 | Vesta reclasificada como cartera (no estratégica) por Hacienda → tributación adicional | B | A | Sustancia inversión estratégica + actas |
| 7 | Hacienda cuestiona tipo 8% Financing Agreement como por encima de mercado | B | A | Comparables mercado + benchmark mezzanine PE |
| 8 | Templus CD reclasificada como sociedad patrimonial → tipo IS 25% + restricciones | B | M | Sustancia operativa 7 DC España + Project Colorado |

## 8. Documentos referencia fiscal

- Opinion letter art. 21 LIS sobre Templus (asesor pendiente identificar)
- SOPARFI LU compliance Vesta Invest + AE Group HoldCo II
- Convenio España-Luxemburgo doble imposición
- Convenio España-Italia / Holanda / Dinamarca / Francia doble imposición (Project Colorado)
- Auditoría EY IN25-6924 TCH4 (cifras tax expense)
- Documentación NRV 19ª TCH4 + TCIH (inversión grupo)
- Financing Agreement Vesta 11/12/2025 (sustancia financiera + tipo 8%)
- Estudio operaciones vinculadas TCH4 ↔ Vesta

Listado completo en `documentos-referencia.md`.

## 9. SQL — verificación factor fiscal

```sql
SELECT param_key, param_value, source
FROM waterfall_params
WHERE business_line_id = 'templus' AND factor_group = 'fiscal';
```

Esperado:
```
is_rate_tch4_pct | 25.0 | LIS art. 21 — sin exención (<5%)
vesta_loan_rate_pct | 8.0 | Financing Agreement Vesta 11/12/2025 — escudo fiscal único TCH4
```

## 10. Pendientes fiscales

1. Opinion letter art. 21 LIS actualizada para cadena IPN/TCH2 → TCH4 + TCIH.
2. Análisis Hacienda sobre Financing Agreement Vesta 8% (sustancia + comparables).
3. Estudio sobre BEPS pilar 2 / GloBE impacto en LU SOPARFI Vesta + AE HoldCo II.
4. Planificación exit Templus (escenarios fiscales detallados por escenario).
5. Coordinación con asesor fiscal Luxemburgo sobre Vesta + AE HoldCo II.
