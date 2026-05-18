# Fiscalidad detallada — TCIH

> Snapshot 31/12/2025 · LIS + NRV 19ª PGC + jurisprudencia TJUE/TS aplicable + diario operaciones TCIH 2019-2026.

## 1. NRV 19ª PGC — Inversiones empresas grupo / multigrupo / asociadas

### Aplicación TCIH

TCIH es titular de tres tipos de inversiones financieras:

| Inversión | Cap% | Calificación NRV 19ª | Tratamiento |
|---|---|---|---|
| **TCS (Teras Capital Spain)** | 100% | Empresa del grupo (control ≥50%) | Coste menos deterioro. Prueba deterioro anual. NO consolida en TCIH como tal (no se publican cuentas consolidadas TCIH); el control opera a través del grupo MdL |
| **Templus CD** | 2,00% (Class B Teras) | Inversión financiera (cap% <20% sin influencia significativa documentada) | Coste menos deterioro o valor razonable según política. Ingresos dividendos: ordinarios |
| **TCH4** | 0,01% residual | Inversión financiera residual | Coste; saldo intercompany 15.264€ figura en mayor PGC pero NO en `participations` BD |

### Implicaciones

- TCIH NO consolida (no llega a control ≥50% en Templus CD ni TCH4).
- TCIH reflexión NRV 19ª: inversiones a coste con prueba anual deterioro.
- Para presentaciones consolidadas a bancos: distinguir **valor contable TCIH** (coste histórico aportaciones) vs **fair value implícito** (look-through cap% × NAV TCS y NAV Templus).

## 2. Art. 21 LIS — exención dividendos / plusvalías inversión grupo

### Test aplicabilidad cadena TCIH

| Eslabón | Cap% | ≥5%? | Art. 21 LIS aplica? |
|---|---|---|---|
| MdL persona → IPN | 100% | sí | N/A (persona física) |
| IPN → TCIH | 25,83% | **SÍ** | **SÍ** — dividendos/plusvalías TCIH exentas en IPN |
| TCH2 → TCIH | 25,83% | **SÍ** | **SÍ** — dividendos/plusvalías TCIH exentas en TCH2 |
| TCIH → TCS | 100% | sí | **SÍ** — dividendos/plusvalías TCS exentas en TCIH |
| TCIH → Templus CD | 2% | **NO** | **NO** — dividendos Templus CD gravados 25% en TCIH |
| TCIH → TCH4 | 0,01% residual | NO | NO (irrelevante por importe) |

### Implicaciones prácticas

- **Dividendos TCS → TCIH**: exentos art. 21 LIS (100% cap%).
- **Dividendos Templus CD → TCIH**: NO exentos. TCIH paga 25% IS sobre cualquier dividendo recibido de Templus CD.
- **Dividendos TCIH → IPN/TCH2**: exentos art. 21 LIS (25,83% cada uno).
- **Plusvalías venta TCS (hipotética desinversión)**: exentas en TCIH (100% cap%).
- **Plusvalías venta participación Templus CD**: gravadas 25% en TCIH (sin exención).

### Cadena dividendo Pacífico Cable (histórico)

```
Pacífico Cable Chile → TCS (100%)         → exención en TCS aplicada
TCS → TCIH (100%)                          → exención art. 21 LIS (≥5%)
TCIH → distribución a socios               → cada socio aplica su régimen:
  ├ IPN: exención art. 21 LIS (25,83% ≥5%)
  ├ TCH2: exención art. 21 LIS (25,83% ≥5%)
  ├ Monforte (SL): exención art. 21 LIS (25,83% ≥5%)
  ├ LSS (SL): exención art. 21 LIS (7,50% ≥5%)
  ├ Menéndez (persona física): IRPF — no aplica art. 21 LIS
  └ Gurrea (persona física): IRPF — no aplica art. 21 LIS
```

> El dividendo a cuenta 2,3M€ (cuenta 557) que generó el PN negativo se contabilizó en 2021 sobre el resultado desinversión Pacífico Cable. La cadena de exenciones se aplicó correctamente; el problema es **contable** (presentación PN), no fiscal.

## 3. Equity-rank vs debt-rank — implicación fiscal

### Equity-rank 7,67M€ (override audit_2026_provisional)

- **Tratamiento contable**: reclasificación a `shareholder_loans_as_equity` en presentación financiera. Mejora PN +5,22M€.
- **Tratamiento jurídico**: NO se reclasifica a capital social. Siguen siendo pasivo financiero (cuentas 521 + 55x).
- **Tratamiento fiscal**:
  - Para los acreedores (TCH2, Monforte, IPN, LSS): los intereses devengados son **ingreso financiero**. Si la entidad acreedora es SL ≥5%, puede aplicar exención si los rendimientos son calificados como dividendos del grupo (NO si son intereses sobre préstamos — son ingresos financieros gravados).
  - Para TCIH: gasto financiero deducible (con limitación art. 16 LIS — 30% EBITDA o 1M€).
  - **Conclusión clave**: la calificación equity-rank es contable / financiera (presentación PN), NO societaria ni fiscal.

### Debt-rank Asterion 2,10M€ (subrogación clase B)

- **Tratamiento contable**: `other_intragroup_debt`.
- **Tratamiento fiscal**:
  - Para TCIH: pasivo financiero, NO reduce base IS (no es aportación capital).
  - Para socios B subrogados: obligación de pago a TCIH como **operación financiera personal**. No es renta del trabajo ni rendimiento del capital (es financiación canalizada).
  - Asterion sigue siendo el último acreedor económico vía cadena Tuca Midco; por eso esta posición NO se trata como aportación capital.

## 4. BINs acumuladas (Bases Imponibles Negativas)

### Cuantificación

- PN negativo histórico TCIH: -2.441.138€ (acumulado).
- Result. neg. arrastrado del dividendo cta 2021 + ejercicios sucesivos.
- **Cuantificación exacta BINs**: pendiente extracción (acción auditoría 30/03/2026 punto 7).

### Capacidad compensación (art. 26 LIS)

- Límite anual compensación: **70% base imponible positiva** previa a la compensación.
- Mínimo siempre compensable: 1M€ anual (umbral mínimo).
- Para activar BINs: TCIH necesita generar **bases positivas futuras** que cubran las BINs acumuladas.

### Vías para activar BINs

1. **Cesión crédito TCIH → socios TCH1**: si cesión genera intereses, esos intereses son ingresos financieros TCIH compensables con BINs.
2. **Fees advisory ampliados**: si TCIH amplía servicios advisory (Mundo Pacífico, Templus, Tuca, Gemswell) → más base positiva → más compensación BINs.
3. **Distribución dividendos TCS → TCIH**: aunque exentos art. 21 LIS, generan base contable positiva (incluso si neutralizada fiscalmente).

## 5. Cesión crédito TCIH → socios TCH1 (planificación)

### Hipótesis operativa

TCIH cede su crédito de 4.079.904€ (suma C/C TCH1 + ajustes) a los 11 socios de TCH1 prorrata su % en TCH1:

| Socio TCH1 | % TCH1 | Cesión (€) |
|---|---|---|
| IPN | 31,97% | 1.304.153 |
| Monforte | 17,99% | 734.099 |
| TCH2 | 14,06% | 573.737 |
| Gurrea | 8,06% | 328.942 |
| Menéndez | 8,06% | 328.942 |
| LSS | 5,48% | 223.545 |
| Ávila | 5,00% | 203.995 |
| S. Echevarría | 3,13% | 127.497 |
| Triguero | 3,13% | 127.497 |
| Huarte | 1,67% | 67.998 |
| Lafarga | 1,46% | 59.499 |
| **TOTAL** | 100% | **4.079.904** |

### Cuestiones fiscales a resolver

| # | Cuestión | Análisis |
|---|---|---|
| 1 | Valor cesión: nominal vs descuento | Si nominal: neutralidad fiscal. Si descuento: pérdida en TCIH (¿deducible art. 13.1 LIS?). |
| 2 | Vinculación socios SL ↔ entidad SL TCIH | Art. 18 LIS sobre operaciones vinculadas: valor mercado obligatorio. Justificar. |
| 3 | Ingreso financiero futuro TCIH | Si tras cesión TCIH retiene parcialmente intereses: ingresos compensables con BINs. |
| 4 | Personas físicas (Menéndez, Gurrea — más Lafarga, etc.): | El cesionario persona física registra adquisición crédito a coste; ganancia futura tributa IRPF al cobrar. |
| 5 | Conciliación 55240006 (TCIH) 4,43M€ vs TCH1 55240001 4,08M€ — gap 350K | Resolver antes de cesión (acción auditoría conciliación bilateral). |

### Escenarios planificación (asesor fiscal)

- **Escenario A**: cesión nominal completa, sin descuento. Neutralidad fiscal. Limpia intercompany.
- **Escenario B**: TCIH retiene crédito y cobra intereses TCH1 → ingreso financiero TCIH → activa BINs.
- **Escenario C**: combinación A + B (cesión parcial 50% + retención 50% para activar BINs).

## 6. IS — Impuesto de Sociedades

| Entidad | Régimen | Tipo | Notas |
|---|---|---|---|
| TCIH | General | 25% | BINs acumuladas pendientes cuantificar |
| TCS | General (filial 100%) | 25% | Beneficios desinversión Pacífico Cable ya tributados |
| IPN | General | 25% | Exención art. 21 LIS sobre TCIH |
| TCH2 | General | 25% | Exención art. 21 LIS sobre TCIH |

### Régimen consolidación fiscal

- **NO aplica** régimen de consolidación fiscal grupo MdL en TCIH (estructura no presentada).
- Si se activase: requeriría ≥75% participación entre todas las entidades del grupo + opción formal Hacienda + cuentas consolidadas obligatorias.
- Alternativa: planificación caso-a-caso individual.

## 7. Operación acordeón sep-22 — fiscalidad

- **Reducción capital por compensación créditos**: neutralidad fiscal (los créditos compensados deben estar correctamente valorados a su valor nominal). 
- **Ampliación capital**: aportaciones dinerarias / no dinerarias. Si no dinerarias: valoración auditor + memoria.
- **No inscripción RM**: NO afecta tratamiento fiscal interno entre socios. Sí afecta oponibilidad frente Hacienda en caso de litigio (terceros de buena fe).
- **Riesgo**: si Hacienda cuestiona la compensación de créditos sin auditoría formalizada, podría recalificar la operación. Mitigante: auditoría sep-22 + documentación contable.

## 8. Cuenta 557 — dividendo a cuenta 2,3M€

- **Naturaleza fiscal**: dividendo a cuenta + devolución aportaciones (mixed).
- **Tratamiento**: se registró como reducción fondos propios pero técnicamente como adelanto de resultados pendientes regularización.
- **Riesgo**: si Hacienda califica como dividendo distribuido (sin reserva distribuible suficiente), podría recalificarse y exigir IS adicional.
- **Solución**: regularizar formalmente en próxima asamblea ordinaria (Q4 2026) con respaldo de auditoría.

## 9. Estructuras LU SOPARFI (referencia cruzada con cadena Olin)

- Tuca Bidco / Tuca Midco operan bajo LU SOPARFI (estructura Asterion).
- TCIH NO opera bajo SOPARFI (es SL española).
- Conexión: deuda Asterion → TCIH 1,80M€ (cuenta 17100008) puede ser parte de la estructura más amplia Asterion - Tuca Midco; revisar si los intereses son deducibles para TCIH bajo art. 16 LIS (limitación 30% EBITDA).

## 10. Riesgos fiscales

| # | Riesgo | P | I | Mitigante |
|---|---|---|---|---|
| 1 | Hacienda cuestiona override equity-rank como reclasificación sin sustancia | B | A | Auditoría B88279880 formal + opinion letter independiente |
| 2 | Recalificación dividendo cta 2,3M€ como dividendo distribuido sin reserva | M | A | Regularización formal asamblea + ajuste cuentas |
| 3 | Recalificación cesión crédito TCIH → socios como liberalidad (no deducible) | B | M | Valor mercado + auditoría operación vinculada |
| 4 | BINs acumuladas no cuantificadas → riesgo caducidad parcial | M | M | Cuantificar y activar via ingresos financieros |
| 5 | Intereses Asterion 17100008 (1,80M€) no deducibles art. 16 LIS por limitación EBITDA | M | M | Verificar EBITDA TCIH suficiente + planificar |
| 6 | Cambio LIS art. 21 (reforma cap% mínimo) | B | A | Lobby + planificación contingente |
| 7 | TJUE / TS jurisprudencia cláusula general anti-elusión | B | A | Sustancia económica documentada + asesoría continua |
| 8 | Recalificación NRV 19ª Templus CD (2%) como activo financiero corriente vs no corriente | B | B | Política contable documentada |

## 11. Documentos referencia fiscal

- Opinion letter art. 21 LIS sobre TCIH (asesor fiscal TERAS — pendiente identificar firma)
- Modelo 200 IS TCIH ejercicios 2019-2024
- Memoria contable TCIH 2024 (referencia NRV 19ª)
- Auditoría provisional 02/04/2026 (B88279880) — soporta override equity-rank
- Conciliación Mayor 2025 vs Auditoría (Excel) — soporta partidas
- Convenio España-Chile doble imposición (histórico Pacífico Cable)

Listado completo + paths en `documentos-referencia.md`.

## 12. SQL — verificación factor fiscal

```sql
-- Override equity-rank TCIH
SELECT entity_id, fiscal_year, total_equity, shareholder_loans_as_equity,
       (total_equity + shareholder_loans_as_equity) AS pn_ajustado, source, notes
FROM entity_balances
WHERE entity_id = 'tcih' AND fiscal_year = 2025;

-- Histórico TCIH BINs proxy (resultados negativos)
SELECT fiscal_year, net_result, ingresos, gastos
FROM entity_balances
WHERE entity_id = 'tcih' AND net_result < 0
ORDER BY fiscal_year;

-- Composición ingresos 2025 (fees advisory)
-- (requiere mayor PGC desglose por cuenta 759 / 705)
```

## 13. Planificación 2026-2028

| Año | Acción fiscal | Owner |
|---|---|---|
| 2026 Q2 | Cuantificar BINs acumuladas TCIH | Asesor fiscal + CFO |
| 2026 Q2 | Validar override equity-rank con asesor fiscal | Asesor + CFO |
| 2026 Q3 | Decidir Escenario A/B/C cesión crédito | Asesor + CFO + CLO |
| 2026 Q4 | Regularización dividendo cta 2,3M€ asamblea | LSS + asesor |
| 2027 | Activación BINs via ingresos financieros | CFO |
| 2027+ | Refinanciación Asterion: optimizar deducibilidad intereses | CFO + asesor |
