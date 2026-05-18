# Fiscalidad detallada — Olin

> Snapshot 31/12/2025 · LIS + NRV 19ª PGC + jurisprudencia TJUE/TS.

## 1. Art. 21 LIS — exención dividendos / plusvalías inversión grupo

### Test de aplicabilidad en la cadena Olin

| Eslabón | Cap% | ≥5%? | Art. 21 LIS aplica? |
|---|---|---|---|
| MdL persona → IPN | 100% | sí | N/A (persona física) |
| IPN → TCH1 | 31,97% | sí | **SÍ** (dividendos/plusvalías TCH1 exentas en IPN) |
| TCH2 → TCH1 | 14,06% | sí | **SÍ** |
| TCH1 → TUCA | 1,80% | **NO** (<5%) | **NO** (dividendos TUCA gravados 25% en TCH1) |
| TUCA → MasOrange | (sub TUCA control) | sí | N/A (interno TUCA) |

### Implicación práctica

- **Cualquier dividendo TUCA → TCH1 paga 25% IS en TCH1** sin exención (BD `waterfall_params.is_rate_tch1_pct=25, source='LIS art. 21 — sin exención (<5%)'`).
- Una vez en TCH1, distribución a IPN / TCH2 puede beneficiarse de art. 21 LIS si IPN/TCH2 tienen ≥5% en TCH1 (sí: 31,97% y 14,06%).
- El "peaje fiscal" del 25% se paga UNA VEZ en TCH1 (no doble imposición arriba en cadena).

### Cálculo en escenarios exit

- Sale price 400M€ → equity surplus distribuible TUCA ~130M€ (sobre hurdle 270M€).
- TCH1 recibe ~25M€ gross (cap% 18,45% econ TUCA + Class B Ord 17,75%).
- TCH1 paga 25% IS → ~6,25M€ IS.
- TCH1 distribuible a socios TCH1: ~18,75M€.
- MdL (46,03% TCH1) recibe ~8,6M€ gross MdL.
- En IPN/TCH2 puede aplicar exención art. 21 → flujo neto MdL ~7,3M€ (`exit_scenarios.mdl_net_return` para 400M€ base).

## 2. NRV 19ª PGC — Inversiones en empresas grupo / multigrupo / asociadas

### Tratamiento contable TCH1 sobre TUCA

- TCH1 valora inversión en TUCA Bidco como **inversión grupo** (≥20% control conjunto / influencia significativa NO se cumple ya que TCH1 tiene 1,80% capital; sin embargo, los **derechos económicos 18,45%** y la **integración en ISHA** pueden encajar como vinculada/asociada según interpretación auditor).
- Valoración: **coste histórico menos deterioro** (no consolidación, NO valor razonable salvo deterioro).
- Cualquier dividendo se reconoce como ingreso financiero ordinario.
- Cualquier plusvalía sólo se reconoce al desinvertir (NO se anticipa).

### Implicación para informes consolidados

- TCH1 NO consolida TUCA (cap% 1,80% no llega a control).
- TCH1 reflexión NRV 19ª: inversión a coste con prueba anual de deterioro.
- Cualquier informe del grupo MdL sobre Olin debe distinguir: **valor contable TCH1** (coste 1.479.243€) vs **fair value implícito** (look-through 18,45% × 248,55M€ PN TUCA = ~45,9M€ aprox a NAV PN, no a NAV exit).

## 3. IS — Impuesto de Sociedades

| Entidad | Régimen | Tipo | Notas |
|---|---|---|---|
| TCH1 | General | 25% | Sin exención art. 21 en dividendos TUCA |
| IPN | General | 25% | Exención art. 21 sobre TCH1 (31,97%) |
| TCH2 | General | 25% | Exención art. 21 sobre TCH1 (14,06%) |
| Tuca Bidco | Luxemburgo (S.à r.l.) | Régimen LU SOPARFI (parcial) | Estructuración fiscal de eficiencia |
| Tuca Midco | Luxemburgo / chain Asterion | LU SOPARFI | Diseño Asterion fund |

> SOPARFI Luxemburgo permite estructuración eficiente: dividendos / plusvalías entre Lux + España con tratado de doble imposición; deuda Asterion en cadena escudada con intereses deducibles a nivel Bidco/Midco.

## 4. Subrogación deuda Asterion 2,10M€ — fiscalidad

- **NO** se trata como aportación de capital de los socios B en TCIH. Es **deuda intragrupo** (debt-rank, cuentas 5510/5525 + 17xxx). 
- Fiscalidad para TCIH: pasivo financiero, NO reduce base IS.
- Fiscalidad para socios B: la "subrogación" Asterion les genera una obligación de pago a TCIH (no es renta del trabajo ni rendimiento del capital — es operación financiera personal).
- Mitigante TCIH: la causa de disolución técnica art. 363.1.e LSC se salva con la reclasificación auditoría provisional 02/04/2026 de aportaciones equity-rank (7.666.559€) que ajustan PN +5,22M€.

## 5. Exit fiscal MdL — escenarios

### Vía dividendo TUCA → TCH1 → IPN/TCH2

- TUCA distribuye → TCH1 paga 25% (IS sin exención) → IPN/TCH2 reciben con exención art. 21.
- Tasa efectiva total: ~25% sobre flujo (un solo nivel).

### Vía venta TCH1 en TUCA (transferencia paquete Class B)

- TCH1 vende participaciones TUCA → realiza plusvalía → 25% IS sobre ganancia.
- IPN/TCH2 venden TCH1 → exención art. 21 LIS sobre ganancia (≥5% MdL).
- Tasa efectiva: ~25% una vez.

### Vía exit Class B vested (cláusula ISHA exit)

- ISHA Cl. 6.4: Class B vesting on exit 100%. Genera plusvalía TCH1.
- Mismo tratamiento que vía venta TCH1.

### Vía dividend extraordinario tras refinanciación

- Refinanciación Asterion 2028 puede generar dividendo extraordinario TUCA si saneamiento permite.
- Tratamiento: IS 25% en TCH1, exención en IPN/TCH2.

### Reinversión en otra línea TERAS (Templus / Gemswell)

- Mecanismo: TCH1 reinvierte en TCH4 o TCH3 (con ≥5% mantiene exención).
- Cuidado: TCH4 también está <5% en Templus CD → mismo problema fiscal aguas abajo.

## 6. Riesgos fiscales

| # | Riesgo | P | I | Mitigante |
|---|---|---|---|---|
| 1 | Calificación NRV 19ª pone en duda exención art. 21 sobre TCH1 si auditor lo califica como mero financiero | B | M | Opinion letter asesor + sustancia económica documentada |
| 2 | TJUE / TS jurisprudencia restringe encadenamiento exención (cláusula "general anti-elusión") | B | A | Asesoría continua + sustancia operativa real |
| 3 | Cambio LIS art. 21 (recordatorio: PGE retrocedió reforma cap%) | B | A | Lobby + planificación contingente |
| 4 | LU SOPARFI restricciones futuras EU (BEPS pilar 2 / GloBE) | M | M | Monitor + estructura compatible |
| 5 | TUCA reclasificada como cartera (no estratégica) por Hacienda → 25% IS TUCA + 19-21% IRNR dividendos a TCH1 | B | A | Sustancia inversión estratégica + actas |

## 7. Documentos referencia fiscal

- Opinion letter art. 21 LIS sobre Olin (asesor pendiente identificar)
- SOPARFI LU compliance Tuca Bidco / Midco
- Convenio España-Luxemburgo doble imposición
- Auditoría TCH1 cifras tax expense
- Anexo IV ISHA estructura fiscal

Listado completo en `documentos-referencia.md`.

## 8. SQL — verificación factor fiscal

```sql
SELECT param_key, param_value, source
FROM waterfall_params
WHERE business_line_id = 'olin' AND factor_group = 'fiscal';
```

Esperado:
```
is_rate_tch1_pct | 25.0 | LIS art. 21 — sin exención (<5%)
```
