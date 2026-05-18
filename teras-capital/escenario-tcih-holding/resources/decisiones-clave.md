# Decisiones clave — TCIH

> Decisiones técnicas / contables / legales que han fijado el estado actual de TCIH. Cualquier reversión requiere análisis explícito + sign-off CFO + CLO + audit firm.

## 1. Override audit_2026_provisional 02/04/2026 — `shareholder_loans_as_equity = 7.666.559€`

- **Fecha**: 02/04/2026 (auditoría provisional, B88279880 audit firm).
- **Decisión**: 7.666.559€ de saldos en TCIH se reclasifican a `shareholder_loans_as_equity` (equity-rank).
- **Composición exacta**:
  - **TCH2** 4.594.000€ (52100001 PTMO PARTICIPATIVO 4.000K + identificaciones C/C 594K)
  - **Monforte** 1.691.000€ (52100005 PTMO 690K + 55100006 C/C 1.001K)
  - **IPN** 1.140.000€ (55100002 C/C 1.140K)
  - **LSS** 241.000€ (55100001 C/C 241K)
  - **Total exacto**: 7.666.559€
- **Razón material**: estos saldos corresponden a **aportaciones directas de los socios MdL + LSS + Monforte con ánimo de permanencia**, identificadas por el auditor en las cuentas 521xxxxx (préstamos participativos codificación interna TCIH) + cuentas 55xxxxx (corrientes con socios cuyo origen es aportación). El flujo subyacente es Asterion → TCIH → aporte a Olin (TUCA) que el auditor identifica como equity de socios MdL.
- **Impacto contable**:
  - PN contable -2.441.138,31€ → PN ajustado **+5.225.420,69€** (-2,44M + 7,67M)
  - Causa disolución técnica art. 363.1.e LSC: SALVADA.
- **Override BD**: `entity_balances.tcih.source = 'audit_2026_provisional + parser_fix_bug14'`, campo `shareholder_loans_as_equity = 7666559`. Notes campo documenta composición.
- **Pendiente**: confirmación auditoría DEFINITIVA 2025 (audit firm completa sign-off).

## 2. Decisión equity-rank vs debt-rank — subrogación Asterion 2,10M€ NO entra como equity

- **Fecha**: misma auditoría provisional 02/04/2026.
- **Decisión**: los 2.101.899€ de saldos socios externos clase B financiados por Asterion (Gurrea 541K + Menéndez 316K + Izzo 354K + Ávila 200K + Triguero 125K + S.Echebarría 92K + Huarte 67K + Caporaleti 58K + Gurrea-TUCA 348K) NO se reclasifican como equity-rank. Se mantienen como **debt-rank** (`other_intragroup_debt = 2.101.899`).
- **Razón**: la subrogación no implica aportación de capital de los socios externos — Asterion sigue siendo el último acreedor económico vía cadena Tuca Midco → Tuca Bidco. Los socios B son meros conductos contractuales.
- **Documento soporte**: auditoría provisional + side letters individuales.
- **Anti-patrón frecuente**: agentes IA o presentaciones a bancos que confunden "subrogación" con "aportación" → meten 2,10M€ como capital de socios MdL ampliado. **Error material**.
- **Lint**: TCIH LINT 3 — distinguir explícitamente equity-rank (7,67M€) de debt-rank (2,10M€).

## 3. Fix bug parser #14 (15-may-2026) — cuentas 521xxxxx + 17100008

- **Fecha**: 15-may-2026.
- **Decisión**: corrección del parser PGC que clasificaba incorrectamente:
  - **17100008 PTMO ASTERION** (1.802.439€): salía de `pnc_bancario` (incorrecto) → recodificado a `pnc_otra` (correcto). NO es deuda bancaria.
  - **521xxxxx PTMO PARTICIPATIVO** (4.890.000€): salían de `pc_bancario` (incorrecto) → ahora cubierto por override `shareholder_loans_as_equity` agregado.
- **Razón**: la cuenta 521xxxxx en TCIH es codificación INTERNA (no estándar PGC, que sería 158/159 para participativos). El parser no lo reconocía y los clasificaba como deuda bancaria.
- **Estado bank_debt post-fix**: 14.171,17€ (solo tarjetas crédito reales — 12 VISA CAIXABANK + AMEX en cuentas 520xxxxx).
- **Diferencia override 7,67M - 4,89M = 2,78M**: corresponde a aportaciones identificadas por auditor en cuentas 55xxxxx (TCH2 594K + Monforte 1.001K + IPN 1.140K + LSS 241K = 2.976K total, suma exacta) reclasificadas a equity-rank desde C/C socios.
- **Otros entidades afectadas bug #14**: IPN, TCH3, TCH4 también recibieron fix similar para cuentas 17xxxxx + 55x (ver `07-known-issues.md`).

## 4. Acordeón sept 2022 NO inscrito en RM (escritura 25/11/2022)

- **Fecha escritura**: 25/11/2022.
- **Fecha registro RM**: PENDIENTE (>3 años a 18-may-2026).
- **Decisión**: mantener escritura formalizada sin inscripción no implica caducidad — el acuerdo societario es válido inter partes (art. 21 CCom). Lo que se pierde es oponibilidad frente a terceros de buena fe.
- **Riesgo de caducidad**: NO EXISTE.
- **Severidad**: MEDIA (no ALTA, como inicialmente clasificada en auditoría).
- **Acción**: inscribir cuanto antes (Q2 2026 owner CLO + notaría).
- **Impacto operativo**: capital RM = 3.099€, capital efectivo = 20.000€. Cualquier referencia a "capital social TCIH" debe explicitar la situación.

## 5. Capital RM 3.099€ vs Capital efectivo 20.000€

- **Decisión**: en presentaciones financieras + override BD `entity_balances.tcih.capital_social=20.000` se usa el capital **efectivo** 20.000€.
- **Razón**: refleja la realidad económica tras el acordeón sep-22 (compensación créditos por 16.901€ adicionales).
- **Implicación**: si tercero (banco, Hacienda) consulta el RM, leerá 3.099€. La diferencia debe explicarse vía documentación acordeón + auditoría provisional.
- **Lint**: TCIH LINT 5 — explicitar la situación al citar capital social.

## 6. Dividendo a cuenta 2,3M€ (cuenta 557) — origen PN negativo

- **Fecha**: 2021 (tras desinversión Pacífico Cable).
- **Decisión histórica**: distribuir adelanto resultados a socios sin reserva distribuible suficiente, generando cuenta 557 deudora.
- **Naturaleza**: devolución aportaciones + dividendo a cuenta (mixed).
- **Impacto**: causa PRINCIPAL del PN negativo contable (-2,44M€).
- **Regularización**: pendiente formalización vía cuentas anuales (acción Q4 2026 — asamblea ordinaria).
- **Solución parcial aplicada**: el override equity-rank 7,67M€ ajusta PN a +5,22M€, absorbiendo el efecto del dividendo a cta.
- **Riesgo si Hacienda recalifica**: dividendo distribuido sin reserva → IS adicional + sanción. Mitigante: regularizar formalmente con respaldo auditoría.

## 7. Distinción TCIH (chasis) vs TCH4 (Templus operativo)

- **Decisión doctrinal**: TCIH es chasis legal transversal del grupo Teras Capital. NO es línea operativa con waterfall ISHA. TCH4 sí lo es (Templus Data Centers).
- **Posiciones reales TCIH-Templus**:
  - TCIH → Templus CD 2,00% directo Class B Teras (Org chart Templus v8 14/04/2026).
  - TCIH → TCH4 ~0,01% residual (cc_balance 15.264€ — figura en mayor pero no en `participations`).
- **Anti-patrón**: confundir las dos posiciones o atribuir a TCIH un waterfall Templus.
- **Lint**: TCIH LINT 10 — separar TCIH (chasis) de líneas operativas.

## 8. Look-through 51,66% vs declarado 51,67% — rounding

- **Decisión**: la cifra **51,66%** es la suma exacta look-through (25,83% IPN + 25,83% TCH2 vía IPN 100%).
- **Cifra declarada BD**: `business_lines.teras-capital.mdl_position_pct = 51,67` (redondeo a dos decimales).
- **Diferencia**: -0,01pp por rounding.
- **Convención**: usar **51,66%** para cálculos precisos; **51,67%** se admite en presentaciones citando "redondeo".
- **Lint**: TCIH LINT 6 — usar 51,66% en cálculos.

## 9. Hallazgo TCIH-C-02 — PTMO TCH2 4M contable vs 3M contractual

- **Hallazgo**: auditoría 30/03/2026 detecta que el saldo PTMO PARTICIPATIVO TCH DOS (cuenta 52100001) figura en mayor por 4.000.000€ pero la documentación contractual original (Jenkins UNO cedido) es de 3.000.000€.
- **Composición probable**: 3M Jenkins UNO original cedido + 1M de cancelación parcial cuenta crédito sep-2022 reestructurada a participativo.
- **Estado**: conciliación bilateral pendiente con CFO TCH2.
- **Severidad**: ALTA.
- **Acción**: documentar la cancelación parcial cuenta crédito 1M con escritura sept-22 + sign-off auditoría TCH2.

## 10. Conciliación 55240006 (TCIH) 4,43M€ vs 55240001 (TCH1) 4,08M€ — gap 350K

- **Hallazgo**: el saldo C/C TCH1 visto desde TCIH (4.430.680€) no coincide exactamente con el saldo C/C TCIH visto desde TCH1 (4.079.904€). Gap de 350.776€.
- **Hipótesis**: diferencia de momento de corte + ajustes pendientes 31/12/2025.
- **Acción**: conciliación bilateral antes de planificar cesión crédito a socios (Escenario A/B/C asesor fiscal).
- **Owner**: CFO TERAS + audit firm.

## 11. Cesión crédito 4,08M€ TCIH → socios TCH1 (planificación pendiente)

- **Decisión pendiente**: Escenario A (nominal) / B (retención TCIH cobra intereses) / C (combinación).
- **Razón estratégica**: simplificar intercompany + activar BINs TCIH + neutralidad fiscal socios.
- **Owner**: CFO + CLO + asesor fiscal (decisión Q3 2026).
- **Dependencia**: conciliación bilateral previa (decisión 10).

## 12. Préstamos Gurrea (200K) + IPN (~853K) sin contratos formales (H-03 audit)

- **Hallazgo**: la auditoría no localiza contratos formales para:
  - 52100008 PTMO Gurrea 200.000€ (registrado en mayor pero sin contrato base).
  - Préstamo IPN estimado 853.000€ (figura como acreedor en operación acordeón pero sin contrato original localizado).
- **Severidad**: ALTA (riesgo formalización + tratamiento fiscal).
- **Acción**: formalización ex-post + opinion letter (Q2-Q3 2026, CLO).

## 13. Identidad Dime Shared / Quarter Capital (H-02 audit)

- **Hallazgo**: el préstamo dic-2019 fue firmado con "Dime Shared Asociados S.L." 800.000€, pero la liquidación 16/02/2022 se atribuye a "Quarter Capital" (QC). Vínculo societario no documentado.
- **Severidad**: MEDIA.
- **Acción**: aclarar via CLO + búsqueda histórica.

## 14. SPA Pacífico Cable + acuerdo dividendo TCS → TCIH ausentes (H-04 audit)

- **Hallazgo**: la auditoría no localiza el SPA de venta Pacífico Cable (dic-2021) ni el acuerdo dividendo TCS → TCIH.
- **Severidad**: ALTA.
- **Acción**: búsqueda + reconstrucción documental (Q3 2026, CLO).

## 15. Pacífico Cable sigue como cliente activo TCS 2025 (C-06)

- **Observación**: tras la desinversión de la participación en 2021, Pacífico Cable mantiene relación comercial advisory con TCS (~207K€ facturado 2025, cuenta 43000003 saldo 19.043€).
- **Tratamiento**: cliente comercial estándar.
- **Continuidad**: renovación contractual continua (responsabilidad TCS comercial).

## SQL — extracción overrides + decisiones TCIH

```sql
SELECT table_name, row_key, field_name, old_value, new_value,
       source, reason, applied_at, applied_by
FROM data_overrides
WHERE row_key::text LIKE '%tcih%'
ORDER BY applied_at DESC;

-- Histórico balance vs override
SELECT fiscal_year, total_equity AS pn_contable,
       shareholder_loans_as_equity AS equity_rank_override,
       (total_equity + COALESCE(shareholder_loans_as_equity, 0)) AS pn_ajustado,
       other_intragroup_debt AS debt_rank,
       source, imported_at
FROM entity_balances
WHERE entity_id = 'tcih'
ORDER BY fiscal_year DESC;
```

## Cambios pendientes que requieren aprobación explícita

| # | Cambio | Owner | Sign-off requerido |
|---|---|---|---|
| 1 | Inscribir acordeón sep-22 RM | CLO + LSS | Asamblea + notario |
| 2 | Regularizar dividendo cta 2,3M€ | CFO + asesor | Asamblea Q4 2026 |
| 3 | Ejecutar cesión crédito TCIH → socios TCH1 | CFO + CLO | Asamblea TCIH + Asamblea TCH1 |
| 4 | Conciliación bilateral C-02 | CFO + audit firm TCH2 | Audit firms ambos |
| 5 | Formalizar contratos Gurrea + IPN (H-03) | CLO | CLO sign-off + asesor fiscal |
| 6 | Auditoría definitiva 2025 (sign-off final) | Audit firm B88279880 | Asamblea ratifica |
