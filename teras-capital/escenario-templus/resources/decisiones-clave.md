# Decisiones clave — Templus

> Decisiones técnicas / contables / legales / fiscales que han fijado el estado actual de Templus y cuya inversión podría requerir aprobación explícita.

## 1. Override audit EY IN25-6924 + audit_2026_provisional sobre filiales

- **Fecha**: Auditoría EY IN25-6924 emitida abril 2026 (TCH4) + Pack Miguel 10-may-2026 (Templus CD + 7 filiales España + 4 Roosevelt).
- **Decisión**: las cifras 2025 de las 7 filiales España + 4 Roosevelt Project Colorado se cargan en BD `entity_balances` con `source='audit_2026_provisional'`.
- **Razón**: cifras provisionales hasta cierre auditoría externa consolidada de Templus CD (esperada Q2 2026). El audit EY IN25-6924 confirma TCH4 con cifras EY-validadas; las filiales operativas dependen de audit firm consolidado Templus CD pendiente.
- **Documento**: `bl_documents` doc_type='audit' business_line_id='templus' name='EY IN25-6924 TCH4 abril 2026'.
- **Impacto en Templus**:
  - TCH4 cifras 2025 EY-validadas (PN -5K€ técnicamente negativo confirmado).
  - 7 filiales España: cifras 2025 provisionales pendientes audit consolidado.
  - 4 Roosevelt Project Colorado: cifras 2025 provisionales (Colorado Mgmt Accounts, no audit aún).
- **Reconciliación pendiente**: cifras Templus CD agregadas (Activo 179,5M€ · PN 177,2M€) vs suma de las 7 filiales individuales (~192,9M€ · ~159M€). La diferencia se explica por participaciones intragrupo + ajustes consolidación intergrupo (referencia `exclude_from_group_totals=true` Templus CD para no duplicar con Vesta).

## 2. Fix bug parser #14 — cuenta 17100000 PTMO VESTA INVEST reclasificada

- **Fecha**: mayo 2026 (parser_fix_bug14).
- **Decisión**: la cuenta 17100000 PTMO VESTA INVEST S.A.R.L. en TCH4 (saldo 31/12/2025: 976.756,13€) se reclasifica de `pnc_bancario` (deuda bancaria) a `pnc_otra` (deuda con socios / equity-rank).
- **Razón**: Vesta Invest S.à r.l. es sponsor ICG externo (vehículo LU del fondo ICG), NO es banco. El parser PGC original detectaba cuenta 171 (Deudas a LP con entidades de crédito) y la clasificaba automáticamente como bancaria. Con la corrección manual, se identifica que el préstamo es de un **socio + sponsor** según ISHA + Financing Agreement 11/12/2025, no de una entidad de crédito.
- **Documento**: ISHA Vesta 11/10/2023 + Enmienda 11/12/2025 + Financing Agreement 11/12/2025.
- **Impacto en TCH4**:
  - `bank_debt` TCH4 corregido de 976.756€ → 0€ (no tiene deuda bancaria propia).
  - `pnc_bancario` TCH4 corregido a 0€.
  - `pnc_otra` TCH4 incluye 976.756€ Vesta + otros saldos intragrupo.
- **Impacto fiscal**: los intereses 8% siguen siendo deducibles (gasto financiero), pero el tratamiento como deuda bancaria vs deuda socio cambia presentación en informe a bancos (deuda neta bancaria 0, no 976K€).
- **Bitácora**: `data_overrides` con `source='parser_fix_bug14'`, `reason` detallado en notes.

## 3. Decisión IS 25% sin exención art. 21 LIS — TCH4 → Vesta + TCIH → Templus CD

- **Fecha**: decisión doctrinal continua, formalizada en BD `waterfall_params` con fix bug #14.
- **Decisión**: TCH4 paga 25% IS íntegro sobre dividendos/plusvalías Vesta. TCIH paga 25% IS íntegro sobre dividendos/plusvalías Templus CD vía Path 2.
- **Razón**: cap% TCH4 en Vesta = 2,00% < 5% LIS art. 21 → NO aplica exención. Cap% TCIH en Templus CD directo = 2,00% < 5% → NO aplica exención.
- **Único escudo fiscal de TCH4**: intereses préstamo Vesta 8% deducibles (cuenta 17100000).
- **Sin escudo equivalente para TCIH Path 2**: no hay préstamo Vesta → TCIH.
- **Documentado en BD**: `waterfall_params.is_rate_tch4_pct=25, source='LIS art. 21 — sin exención (<5%)'`.
- **Anti-patrón frecuente**: agentes IA citan exención art. 21 → error material. El cap% MdL efectivo agregado en Templus CD es 1,62%, muy lejos del umbral 5%.

## 4. Enmienda ISHA 11/12/2025 — cupón Class D 12%

- **Fecha**: 11/12/2025 (Enmienda ISHA original 11/10/2023).
- **Decisión**: el cupón preferente Class D Pref se fija en **12,00% anual**.
- **Razón**: ajuste a mercado mezzanine PE + alineamiento con financiación commit 300M€ ICG.
- **Versión anterior (ISHA original 11/10/2023)**: cupón inferior (referencia interna 8-10%, pendiente confirmar exacto histórico).
- **Impacto en waterfall**:
  - Incrementa la barrera económica para que TCH4 Class B Ord capture upside.
  - Hasta hurdle 300M€ + cupón Class D acumulado, Class B Ord no recibe upside meaningful.
  - Acelera el "punto de inflexión" del waterfall hacia upside Class B (escenarios sale price 350M€+).
- **Documentado en BD**: `waterfall_params.pref_coupon_pct=12, source='Enmienda ISHA 11/12/2025'`.

## 5. Financing Agreement Vesta 11/12/2025 — tipo 8%

- **Fecha**: 11/12/2025 (mismo día que Enmienda ISHA).
- **Decisión**: Vesta financia TCH4 al **8,00% anual** sobre tickets ord+pref invertidos en Vesta.
- **Razón**: mecanismo equity-rank socio según ISHA. Aporta liquidez a TCH4 para servicio operaciones (auditoría EY + costes intragrupo).
- **Loan financing pct**: 70% (Vesta financia 70% del ticket TCH4).
- **Documentado en BD**: `waterfall_params.vesta_loan_rate_pct=8, source='Financing Agreement Vesta 11/12/2025'`.
- **Tratamiento fiscal**: intereses 8% deducibles en IS TCH4 — único escudo fiscal.
- **Tratamiento contable**: cuenta 17100000 PTMO VESTA INVEST (reclasificado `pnc_otra` post fix bug #14).
- **Riesgo recalificación**: Hacienda podría recalificar intereses como dividendo encubierto si vinculación demostrable (ver `fiscalidad-detallada.md` §4).

## 6. Templus CD `exclude_from_group_totals=true` — evitar doble conteo con Vesta

- **Fecha**: decisión doctrinal continua, configurada en BD `entities.templus-cd`.
- **Decisión**: Templus CD se marca con `exclude_from_group_totals=true` en BD `entities` para evitar doble conteo en cifras consolidadas del grupo MdL.
- **Razón**: Vesta Invest (96% Templus CD) ya agrega Templus CD en sus cifras LUX. Si los informes MdL sumaran también Templus CD directamente, generarían sobre-conteo de los mismos activos.
- **Implicación práctica**:
  - Cifras Vesta (cuando estén disponibles auditadas) incluyen Templus CD agregado.
  - Cifras MdL consolidadas: NO se suma Templus CD adicional para no duplicar.
  - Las 7 filiales España aparecen agregadas en Templus CD, no individualmente en el grupo MdL.
- **Reporting interno TERAS**: para análisis operativo de Templus, se usan cifras Templus CD + 7 filiales + 4 Roosevelt directamente (no las cifras Vesta consolidadas).

## 7. Global Cabria — legacy DUPLICADO de Templus CD

- **Fecha**: identificación legacy, configurado en BD `entities.global-cabria` con `exclude_from_group_totals=true`.
- **Decisión**: Global Cabria es entidad legacy DUPLICADA de Templus CD. Se mantiene en BD `entities` por trazabilidad histórica pero NO entra en cifras consolidadas.
- **Razón**: Global Cabria fue probable denominación anterior o vehículo paralelo que se reemplazó por Templus CD. Para evitar confusión y doble conteo, se marca `exclude_from_group_totals=true`.
- **Anti-patrón frecuente**: agentes IA que citan Global Cabria como entidad activa Templus → error. La entidad operativa agregadora es Templus CD (NIF B-56381379), no Global Cabria.

## 8. Adquisición Templus Spain (Espacio Edge) 25/06/2025

- **Fecha**: 25/06/2025.
- **Decisión**: Templus CD adquiere Espacio Edge (NIF B10947703) por importe que genera Goodwill 20,8M€.
- **Razón**: expansión perímetro AE Group + capacity DC adicional en España.
- **Tratamiento contable**:
  - Activo Templus Spain post-adq: 22,7M€ (con Goodwill 20,8M€ incluido).
  - Plan integración 100 días pendiente Q2 2026.
- **Documentado**: SPA Espacio Edge + acuerdo M&A.
- **Riesgo**: deterioro Goodwill 20,8M€ si integración no genera sinergias o si capacity DC adquirido se subutiliza.

## 9. Constitución Templus Ceuta (Waterways Global) 11/06/2025

- **Fecha**: 11/06/2025.
- **Decisión**: constitución Templus Ceuta (NIF B-13931688) sobre legacy Waterways Global. Greenfield.
- **Razón**: capacity DC adicional en Ceuta (ubicación estratégica conectividad).
- **Estado 31/12/2025**: Activo 6,3M€ · PN 4,1M€. Build-out previsto Q3 2026.
- **Documentado**: SPA Waterways + constitución notarial.

## 10. Project Colorado modelado pendiente (tarea #9 BD MdL)

- **Estado**: pendiente.
- **Decisión pendiente**: modelar cadena Vesta → AE Group HoldCo II → 4 Roosevelt (IT/NL/DK/FR) en BD `participations` para reflejar look-through MdL completo.
- **Issue**: `templus-cd 178,5M€ orphan` — Templus CD activo registrado en BD pero sin enlace `participations` claro a AE Group HoldCo II o las Roosevelt filiales.
- **Razón pendiente**: estructura societaria Project Colorado vía AE Group HoldCo II depende de TCH4 directamente, no vía Vesta. Cadena exacta pendiente confirmar con org chart v8 (14/04/2026).
- **Owner**: CFO + CTO TERAS coordinan modelado.
- **Deadline**: Q4 2026 (referencia §10 hitos próximos SKILL).

## 11. Tarea pendiente #11 BD MdL — discrepancias `bl.mdl_position_pct` vs efectivo

- **Estado**: aplicable también a Templus.
- **Discrepancia documentada**: `business_lines.templus.mdl_position_pct=1,62%` cuadra con look-through real (0,626% Path 1 + 1,033% Path 2). Sin discrepancia activa actualmente.
- **Verificación**: re-run `participations` look-through cuando cambien tranches Financing Agreement Vesta (si TCH4 toma más tickets) o cambios en TCIH cap% (afectaría Path 2).

## 12. ISHA Vesta original 11/10/2023 vs Enmienda 11/12/2025

- **ISHA original 11/10/2023**: estructura Class B (25% Ord) + Class D (75% Pref) establecida. Cupón Class D inferior (referencia 8-10%).
- **Enmienda 11/12/2025**: cupón Class D elevado a **12%** + Financing Agreement Vesta firmado el mismo día.
- **Vigencia**: Enmienda 11/12/2025 es la versión actual aplicable a todos los cálculos waterfall y exit scenarios.
- **Documentado**: ambas versiones en `bl_documents` con metadata fecha + signatarios.

## SQL — extracción overrides Templus

```sql
SELECT table_name, row_key, field_name, old_value, new_value,
       source, reason, applied_at, applied_by
FROM data_overrides
WHERE (row_key::text LIKE '%tch4%' OR row_key::text LIKE '%templus%' OR row_key::text LIKE '%vesta%' OR row_key::text LIKE '%roosevelt%')
   OR (source LIKE '%templus%' OR source LIKE '%vesta%' OR source LIKE '%parser_fix_bug14%')
ORDER BY applied_at DESC;
```

## Resumen decisiones cardinales

| # | Decisión | Fecha | Estado | Documento clave |
|---|---|---|---|---|
| 1 | Override audit EY IN25-6924 + audit_2026_provisional | Abr-may 2026 | Aplicado | EY IN25-6924 + Pack Miguel |
| 2 | Fix bug parser #14 cuenta 17100000 Vesta | May 2026 | Aplicado | ISHA + Financing Agreement |
| 3 | IS 25% sin exención art. 21 LIS | Doctrinal | Vigente | LIS art. 21 + BD waterfall_params |
| 4 | Enmienda ISHA cupón Class D 12% | 11/12/2025 | Vigente | Enmienda ISHA 11/12/2025 |
| 5 | Financing Agreement Vesta 8% | 11/12/2025 | Vigente | Financing Agreement |
| 6 | Templus CD `exclude_from_group_totals=true` | Doctrinal | Vigente | BD entities |
| 7 | Global Cabria legacy duplicado | Doctrinal | Vigente | BD entities |
| 8 | Adquisición Templus Spain (Espacio Edge) | 25/06/2025 | Cerrada | SPA Espacio Edge |
| 9 | Constitución Templus Ceuta (Waterways) | 11/06/2025 | Cerrada | SPA Waterways + notarial |
| 10 | Modelado Project Colorado (tarea #9 BD) | Pendiente | Pendiente | Q4 2026 deadline |
