# Decisiones clave — Olin

> Decisiones técnicas / contables / legales que han fijado el estado actual de Olin y cuya inversión podría requerir aprobación explícita.

## 1. Calificación subrogación Asterion 2,10M€ como debt-rank (NO equity)

- **Fecha**: auditoría provisional TCIH 02/04/2026 (B88279880).
- **Decisión**: los saldos de socios externos clase B en TCIH financiados por Asterion (Gurrea 541K, Menéndez 316K, Izzo 354K, Ávila 200K, Triguero 125K, S.Echevarría 92K, Huarte 67K, Caporaleti 58K, Gurrea TUCA 348K = total 2.101.899€) NO se reclasifican como equity. Se mantienen como **deuda intragrupo** (cuentas 5510/5525 + 17xxx + 521xxx selectivos).
- **Razón**: la subrogación no implica aportación de capital de los socios — Asterion sigue siendo el último acreedor económico vía cadena Tuca Midco → Tuca Bidco. Los socios B son meros conductos contractuales.
- **Documento**: Auditoría provisional TCIH 02/04/2026 (`bl_documents` doc_type='audit' business_line_id='teras-capital').
- **Impacto en Olin**: ninguno directo en TCH1/TUCA. Impacto indirecto: TCIH PN negativo se justifica con equity-rank ampliado (7,67M€) + debt-rank confirmado, no entra en cadena Olin.
- **Anti-patrón frecuente**: agentes IA que confunden "subrogación" con "aportación" → meten 2,10M€ como capital de socios. **Error**.

## 2. Factor `waterfall_params.mdl_pct_tch1=38,14%` vs look-through real 46,03%

- **Fecha**: factor histórico (pre-Asterion + revisión ISHA reformulado).
- **Estado**: discrepancia activa.
- **Decisión pendiente**: reconciliar factor con look-through real.
  - Look-through real (BD `participations`): IPN 31,97% + TCH2 14,06% = **46,03%**.
  - Factor productivo (BD `waterfall_params`): **38,14%**.
  - Diferencia: -7,89pp.
- **Impacto**: `business_lines.olin.mdl_position_pct = 0,53%` se calcula con 38,14%. Si se actualiza a 46,03%, el cap% efectivo final sería **0,83%**.
- **Razón posible del factor 38,14%**: dilución por managers Class B vested + ajustes ISHA Cl. 6.4(C) — pendiente confirmar.
- **Tarea pendiente**: #11 BD MdL (resolver discrepancia `bl.mdl_position_pct` vs efectivo).
- **Default en BD `waterfall_params`**: 46,03% (default si is_editable=true).

## 3. Override audit TCIH 02/04/2026 — equity-rank 7.666.559€

- **Fecha**: auditoría provisional 02/04/2026 (B88279880).
- **Decisión**: 7.666.559€ de saldos en TCIH se reclasifican de pasivo financiero / cuentas socios a **`shareholder_loans_as_equity`** (equity-rank).
  - Composición: TCH2 4.594K + Monforte 1.691K + LSS 241K + IPN 1.140K = **7.666K** equity-rank (suma exacta).
- **Razón**: aportaciones directas de los socios MdL + LSS/Monforte tienen ánimo de permanencia (cuentas 521 PTMO PARTICIPATIVO MdL + 5510/5525 con auditor confirmación).
- **Impacto**:
  - PN TCIH contable -2.441.138€ → PN ajustado +5,22M€ (-2,44M + 7,67M).
  - Causa disolución técnica art. 363.1.e LSC SE SALVA con el ajuste.
  - Indirectamente sanea TCH1 (entidad de paso) aguas abajo.
- **Override BD**: `source = 'audit_2026_provisional + parser_fix_bug14'`, `notes` extenso documenta la composición.
- **Bug parser**: fix #14 (15-may-2026) recodificó cuentas 521xxxxx PTMO PARTICIPATIVO como `prestamos_participativos`, no `pc_bancario`.

## 4. Anti-confusión: 65,81% voto ManCo TUCA NO es cap%

- **Fecha**: aclaración recurrente, documentada en `06-decisions.md` (memoria mdl-patrimonio).
- **Decisión doctrinal**: las Class A reforzadas TCH1 amplifican voto en ManCo TUCA (decisión gobierno) pero **NO modifican cap% económico**.
- **Cap% real MdL en TUCA**: 0,83% capital · 8,49% económico.
- **Voto% MdL en ManCo TUCA** (cuando existe — ver gobernanza específica TUCA): pendiente confirmar magnitud exacta. La cifra 65,81% se ha citado pero su composición exacta requiere verificación con ISHA + Anexo IV.
- **Anti-patrón frecuente**: presentar 65,81% como cap% económico → error material en presentaciones a bancos.

## 5. Investment date 2022-02-18

- **Fecha registrada**: 18-feb-2022 (`waterfall_params.investment_date`).
- **Decisión**: fecha de referencia para cálculos IRR / MOIC TCH1 sobre TUCA.
- **No modificar** sin auditoría que lo justifique. Cualquier modelo financiero (IC notes, board memo) debe usar esta fecha como base.

## 6. Hurdle 270M€ — diseño base ISHA

- **Decisión**: hurdle preferente (recuperación pref invested) = 270M€ (`waterfall_params.total_pref_invested` + `exit_scenarios.hurdle_amount`).
- **Razón**: total inversión Class A + Privilegiadas en TUCA al ratio acordado ISHA.
- **Implicación waterfall**: por debajo de 270M€ sale price, los socios Class B (incluido TCH1) no reciben upside — solo pro-rata 0,696% Privilegiadas.

## 7. Dividend Dec 2024 — 12M€

- **Fecha**: Dec 2024.
- **Decisión**: distribución dividendo 12M€ a nivel TUCA Bidco.
- **Tratamiento TCH1**: recibe pro-rata económico (18,45% × ~12M = ~2,21M€), tributa 25% IS → ~1,66M€ neto distribuible.
- **Documentado en**: `waterfall_params.dividend_dec2024 = 12000000`.

## 8. Refinanciación amount 90M€ — referencia 2027-2028

- **Decisión**: estructura de refinanciación contempla amount de referencia 90M€ (`waterfall_params.refinancing_amount`).
- **Owner ejecución**: CFO TERAS + Asterion.
- **Trigger inicio negociación**: 2027.
- **Mitigante riesgo tipo**: opcionalidad amortización + early refi window.

## 9. ISHA cap dilución 10% new managers — Cl. 6.4(C)

- **Decisión**: la entrada de nuevos managers Class B limita la dilución máxima TCH1 al 10% del bloque Class B Ord.
- **Implicación**: cap% TCH1 Class B Ord pasa de 17,75% → 15,97% (máx dilución).
- **Documentado**: `waterfall_params.tch1_ord_pct_diluted=15.97, source='ISHA Cl. 6.4(C) — máx 10%'`.

## 10. Tasa Asterion 7% sobre deuda TCIH

- **Decisión**: la deuda Asterion en TCIH tributa al 7% anual (`waterfall_params.asterion_rate_pct`).
- **Importe vivo 31/12/2025**: 1.802K€ deuda externa real (override audit TCIH).
- **Importe subrogación clase B**: 2.101.899€ (NO equity, ver decisión 1).

## SQL — extracción overrides Olin

```sql
SELECT table_name, row_key, field_name, old_value, new_value,
       source, reason, applied_at, applied_by
FROM data_overrides
WHERE (row_key::text LIKE '%tch1%' OR row_key::text LIKE '%tuca%' OR row_key::text LIKE '%olin%')
   OR (source LIKE '%olin%' OR source LIKE '%tuca%')
ORDER BY applied_at DESC;
```
