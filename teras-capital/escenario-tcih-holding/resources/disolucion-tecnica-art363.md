# Disolución técnica art. 363.1.e LSC — TCIH

> Análisis legal completo del riesgo de disolución técnica de TCIH bajo art. 363.1.e LSC, situación tras override audit_2026_provisional, y jurisprudencia TS aplicable.

## 1. Marco legal — art. 363 LSC

### Texto literal (relevante)

> **Art. 363 LSC — Causas de disolución**
> 1. La sociedad de capital deberá disolverse:
> ...
> e) Por pérdidas que dejen reducido el patrimonio neto a una cantidad inferior a la mitad del capital social, a no ser que éste se aumente o se reduzca en la medida suficiente, y siempre que no sea procedente solicitar la declaración de concurso.

### Interpretación operativa

- **Condición**: PN < ½ Capital Social.
- **Plazo de acción**: el órgano de administración tiene **2 meses** desde que conoce la situación para:
  1. Convocar junta general para acordar disolución, restablecimiento PN, o solicitud concurso, o
  2. Solicitar disolución judicial / concurso (si junta no se convoca o no adopta acuerdo).
- **Responsabilidad solidaria de administradores** (art. 367 LSC) por deudas posteriores al hecho.
- **Modalidad de salvación**: aumento capital, reducción capital simétrica, aportaciones socios, condonación deuda, reclasificación pasivos.

## 2. Situación TCIH — análisis técnico

### Cifras a 31/12/2025

| Métrica | Valor (€) | Fuente |
|---|---|---|
| Capital social inscrito RM | 3.099 | mayor 100 + RM |
| Capital efectivo (acordeón sep-22) | 20.000 | BD + escritura 25/11/2022 |
| PN contable | -2.441.138,31 | BD `entity_balances.tcih.total_equity` |
| ½ Capital social inscrito | 1.549,50 | derivado |
| ½ Capital social efectivo | 10.000 | derivado |

### Test condición legal

#### Si capital de referencia = RM (3.099€):

```
PN contable -2.441.138 < ½ × 3.099 = 1.549,50  ✓ CAUSA ACTIVA
PN ajustado +5.225.421 > ½ × 3.099 = 1.549,50  ✗ CAUSA SALVADA
```

#### Si capital de referencia = efectivo (20.000€):

```
PN contable -2.441.138 < ½ × 20.000 = 10.000   ✓ CAUSA ACTIVA
PN ajustado +5.225.421 > ½ × 20.000 = 10.000   ✗ CAUSA SALVADA
```

**Conclusión**: en ambos casos, el PN contable activa la causa de disolución; el PN ajustado tras override audit la SALVA con holgura amplia.

## 3. Solución aplicada — override audit_2026_provisional 02/04/2026

### Mecánica del override

La auditoría provisional reclasifica 7.666.559€ de saldos pasivo financiero (cuentas 521 PTMO PARTICIPATIVO + 55x C/C socios identificados) como `shareholder_loans_as_equity` (préstamos socios con tratamiento equity para presentación PN):

```
PN contable          -2.441.138,31€
+ Equity-rank        +7.666.559,00€
─────────────────────────────────
PN ajustado          +5.225.420,69€
```

### Composición exacta equity-rank 7,67M€

| Socio aportante | Importe (€) | Pool |
|---|---|---|
| TCH2 | 4.594.000 | MdL |
| Monforte | 1.691.000 | Externo |
| IPN | 1.140.000 | MdL |
| LSS | 241.000 | Externo |
| **TOTAL** | **7.666.000** | (cifra exacta 7.666.559€) |

### Lo que NO se incluye en el ajuste

- **Subrogación Asterion clase B 2.101.899€**: socios externos B (Gurrea, Menéndez, Izzo, Ávila, Triguero, S.Echebarría, Huarte, Caporaleti, Gurrea-TUCA) → debt-rank, NO equity. Asterion sigue siendo el último acreedor económico.
- **Deuda Asterion externa directa 1.802.439€** (cuenta 17100008): pnc_otra. NO equity.
- **Bank debt 14.171€** (tarjetas crédito 520xxxxx): pasivo financiero estándar.

## 4. Validación de la calificación equity-rank

### Criterios contables para reclasificar deuda a equity (NRV PGC + jurisprudencia)

Un pasivo financiero puede tratarse como capital en presentación PN si:

| Criterio | Aplicación TCIH | Resultado |
|---|---|---|
| Ánimo de permanencia del aportante | Socios MdL (IPN + TCH2 + Monforte + LSS) llevan en TCIH desde constitución / acordeón 2022 | ✓ |
| Subordinación a otros acreedores | Préstamos participativos (521) están subordinados a acreedores ordinarios + financieros | ✓ |
| Remuneración vinculada a resultados | Cuentas 521 PTMO PARTICIPATIVO codificación interna refiere participación en rentabilidad | ✓ parcial |
| Inexistencia de vencimiento fijo o vencimiento muy largo | Saldos C/C sin plan amortización fijo | ✓ |
| Aportación efectiva con flujo de caja documentado | Auditor identifica los flujos en cuentas 5510x + cuentas 521 | ✓ |

**Conclusión**: la calificación equity-rank tiene sustancia económica + respaldo auditor + criterios contables aplicables.

### Diferencia entre reclasificación CONTABLE y reclasificación JURÍDICA

- **Reclasificación contable** (este override): cambio en presentación PN sin afectar la titularidad jurídica de los créditos. Los acreedores siguen siendo TCH2, Monforte, IPN, LSS con sus créditos vivos.
- **Reclasificación jurídica** (no aplicada): convertir formalmente los créditos en capital social mediante operación acordeón con compensación de créditos + inscripción RM.

> La reclasificación contable BASTA para salvar la causa de disolución art. 363.1.e LSC en presentación financiera. La reclasificación jurídica sería más robusta pero requiere nueva operación acordeón + inscripción RM.

## 5. Jurisprudencia TS aplicable

### Sentencias relevantes

1. **STS 1ª 9-mar-2007** (RJ 2007/2479): la causa de disolución por pérdidas no opera automáticamente; requiere acuerdo social o resolución judicial. Los administradores tienen 2 meses para actuar.
2. **STS 1ª 30-jun-2010** (RJ 2010/5681): si la junta acuerda restablecimiento del PN (aumento capital, condonación deuda, aportaciones socios), la causa se entiende salvada.
3. **STS 1ª 25-nov-2019** (RJ 2019/5012): la reclasificación contable de pasivos a fondos propios mediante NRV 19ª o NRV 22ª (préstamos participativos) puede ser válida si tiene sustancia económica.
4. **SAP Barcelona 13ª 12-jul-2018**: los préstamos participativos cumplidos los requisitos del art. 20 RD-ley 7/1996 se consideran patrimonio neto a efectos de la causa de disolución art. 363.1.e LSC. Para TCIH la codificación interna 521 debería verificarse contra art. 20 RD-ley.
5. **DGRN (resoluciones diversas)**: la inscripción RM no es constitutiva de las operaciones de capital. Validez inter partes desde formalización notarial (relevante para acordeón sep-22 no inscrito).

### Requisitos art. 20 RD-ley 7/1996 para préstamos participativos (verificar TCIH cuentas 521)

Para que un préstamo sea participativo con tratamiento PN bajo art. 20:

1. Remuneración fija + variable vinculada a beneficios.
2. Prohibición devolución hasta cancelación de obligaciones con acreedores prioritarios.
3. Subordinación frente a otros acreedores.
4. Plazo amplio (sin liquidación anticipada).

**Estado TCIH cuentas 521xxxxx**: codificación interna "PTMO PARTICIPATIVO" — verificar contratos individuales:
- 52100001 PTMO TCH DOS 4M: contrato participativo formalizado.
- 52100005 PTMO Monforte 690K: pendiente verificación contrato.
- 52100008 PTMO Gurrea 200K: SIN contrato formalizado (H-03 audit) → riesgo calificación.

> Si auditor + asesor legal confirman cumplimiento art. 20 RD-ley 7/1996 para 521xxxxx, el tratamiento PN es robusto. Si no, queda como reclasificación contable equity-rank sin respaldo legal específico (más débil pero válida bajo NRV PGC).

## 6. Riesgos asociados

| # | Riesgo | P | I | Mitigante |
|---|---|---|---|---|
| 1 | Hacienda recalifica equity-rank como pasivo y exige IS por intereses imputados | B | A | Opinion letter independiente + auditoría definitiva con sign-off |
| 2 | Tercero acreedor TCIH inicia acción concurso art. 367 LSC | B | A | PN ajustado positivo + monitoreo cifras + comunicación stakeholders |
| 3 | Asamblea TCIH no ratifica override audit | B | A | Pool MdL 51,66% + alineamiento con Monforte 25,83% — quorum holgado |
| 4 | Nuevo auditor cuestiona override en cuentas 2026 | B | A | Documentación robusta + opinion letter art. 20 RD-ley 7/1996 |
| 5 | RM no acepta inscripción acordeón sep-22 retroactiva | B | M | Subsanación + nueva escritura si necesario |
| 6 | Inspección Hacienda investiga dividendo cta 2,3M€ (cuenta 557) | M | A | Regularización proactiva Q4 2026 |
| 7 | TS revoca jurisprudencia equity-rank en futuro | B | A | Reclasificación jurídica (nueva operación acordeón) como Plan B |
| 8 | Asterion ejecuta deuda 1,80M€ + subrogación 2,10M€ en escenario stress | B | A | Renegociación calendario + refinanciación 2027+ |

## 7. Plan acción 2026-2027

### Prioridad 1 — Q2 2026

- **Inscribir escritura acordeón 25/11/2022 RM** (CLO + notaría).
- **Convocar asamblea extraordinaria** para ratificar override audit_2026_provisional + autorizar acciones derivadas.
- **Auditoría definitiva 2025** — firma final con override equity-rank validado por audit firm.
- **Conciliación bilateral hallazgo TCIH-C-02** (PTMO TCH2 4M vs 3M).

### Prioridad 2 — Q3 2026

- **Opinion letter art. 20 RD-ley 7/1996** sobre cuentas 521xxxxx (asesor legal).
- **Formalización contratos H-03** (Gurrea 200K + IPN ~853K).
- **Cesión crédito TCIH → socios TCH1** (Escenario A/B/C) — descarga intercompany.

### Prioridad 3 — Q4 2026

- **Asamblea ordinaria** aprobación cuentas anuales 2025 con PN ajustado positivo.
- **Regularización dividendo cta 2,3M€** (cuenta 557).
- **Memoria contable NRV 19ª** formalizada con detalle inversiones (TCS + Templus CD + TCH4).

### Prioridad 4 — 2027+

- **Refinanciación / liquidación 17100008 Asterion** (1,80M€).
- **Reorganización debt-rank socios B** si Asterion exige.
- **Cuantificación + activación BINs** TCIH.

## 8. Contraste con otros precedentes del grupo

- **TCH3 (Gemswell)**: causa disolución técnica activa pre-subsanación. **Subsanación dic-2025** con efecto contable 31/12/2025 (NO esperar inscripción RM). Mismo patrón que TCIH pero con compensación de créditos diferentes.
- **TCH4 (Templus)**: PN saneable con estructura ISHA + capital reforzado. NO en situación 363.1.e.
- **TCH1 (Olin)**: PN residual 379€, no en situación 363.1.e (PN positivo).
- **IPN**: PN positivo 5,1M€, no aplica.

## 9. Comparativa formal — PN contable vs PN ajustado vs PN reclasificado jurídicamente

| Métrica | PN contable | PN ajustado (override) | PN reclasificado jurídicamente |
|---|---|---|---|
| Importe (€) | -2.441.138 | +5.225.421 | +5.225.421 (mismo importe) |
| Sustento | Mayor PGC + standard | Override audit_2026_provisional 02/04/2026 | Operación acordeón + inscripción RM |
| Salva art. 363.1.e LSC | NO | SÍ (en presentación financiera) | SÍ (en oponibilidad terceros) |
| Robustez frente tercero | BAJA | MEDIA | ALTA |
| Reversibilidad | — | Sí (sin nueva auditoría) | No |
| Acción requerida | — | Auditoría provisional firmada (ya hecha) | Nueva operación acordeón + RM + auditoría |
| Plazo | — | Inmediato | Q3-Q4 2026 |
| Coste | — | Audit firm (incluido en honorarios) | Notaría + RM + audit + asesores |

**Recomendación**: aplicar override contable como medida inmediata + planificar reclasificación jurídica como Plan B (Q3-Q4 2026) si nuevo auditor o tercero cuestiona la situación.

## 10. Referencias normativas

- **Art. 363 LSC** — causas de disolución
- **Art. 365-367 LSC** — disolución por concurrencia de causa + responsabilidad administradores
- **Art. 20 RD-ley 7/1996** — préstamos participativos
- **Art. 21 CCom** — validez actos no inscritos inter partes
- **NRV 9ª PGC** — instrumentos financieros (pasivos)
- **NRV 19ª PGC** — inversiones empresas grupo / multigrupo / asociadas
- **NRV 22ª PGC** — operaciones con propietarios (cuando aplica)
- **STS 1ª 9-mar-2007, 30-jun-2010, 25-nov-2019** — jurisprudencia aplicable
- **DGRN resoluciones diversas** — inscripción RM no constitutiva

## 11. SQL verificación situación TCIH

```sql
-- Estado PN contable vs ajustado vs capital
SELECT
  entity_id,
  fiscal_year,
  capital_social,
  capital_social / 2.0 AS half_capital,
  total_equity AS pn_contable,
  shareholder_loans_as_equity AS equity_rank_override,
  (total_equity + COALESCE(shareholder_loans_as_equity, 0)) AS pn_ajustado,
  CASE
    WHEN total_equity < (capital_social / 2.0) THEN 'CAUSA 363.1.e ACTIVA (contable)'
    ELSE 'OK (contable)'
  END AS estado_contable,
  CASE
    WHEN (total_equity + COALESCE(shareholder_loans_as_equity, 0)) < (capital_social / 2.0) THEN 'CAUSA 363.1.e ACTIVA (ajustado)'
    ELSE 'SALVADA (ajustado)'
  END AS estado_ajustado
FROM entity_balances
WHERE entity_id = 'tcih' AND fiscal_year = 2025;

-- Histórico evolución PN ajustado
SELECT fiscal_year, total_equity, shareholder_loans_as_equity,
       (total_equity + COALESCE(shareholder_loans_as_equity, 0)) AS pn_ajustado,
       capital_social
FROM entity_balances
WHERE entity_id = 'tcih'
ORDER BY fiscal_year DESC;
```
