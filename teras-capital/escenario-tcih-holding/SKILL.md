---
name: escenario-tcih-holding
capa: L3b-escenarios
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras, challenge-cognitivo-teras]
triggers: >
  Se activa cuando el usuario menciona TCIH, Teras Capital Investment Holding,
  B88279880, Teras Capital, TERAS CAPITAL, intragrupo, intragroup, intragroup_balances,
  saldos intragrupo, 9 saldos, equity-rank, debt-rank, shareholder loans,
  shareholder_loans_as_equity, préstamos participativos, PTMO PARTICIPATIVO,
  cuenta 521, subrogación Asterion, art 363 LSC, art 363.1.e, disolución técnica,
  causa disolución, PN ajustado, NRV 19, NRV 19ª, inversiones grupo, inversiones
  empresas grupo, look-through, look through, look-through engine, 51,66%, 51,67%,
  acordeón sep-22, acordeón septiembre 2022, capital efectivo TCIH, capital RM TCIH,
  TCS, Teras Capital Spain, Templus CD 2%, dividendo a cuenta 557, cuenta 557,
  Pacífico Cable, Pacifico Cable, chasis legal Teras, chasis Teras.
description: >
  Precarga contexto operativo, contable, legal y fiscal del activo transversal
  TCIH (Teras Capital Investment Holding, S.L.), chasis legal del grupo Teras
  Capital. NO es una línea operativa con waterfall: es la holding de servicios y
  vehículo de canalización equity/debt para todo el grupo. Cubre cap table 6
  socios (51,66% pool MdL + 48,34% externos), composición equity-rank 7,67M€ vs
  debt-rank Asterion 2,10M€, los 9 saldos intragrupo BD, PN contable -2,44M€ vs
  PN ajustado +5,22M€ que salva art. 363.1.e LSC, override audit_2026_provisional
  02/04/2026 y fix bug #14 sobre cuentas 521xxxxx + 17100008.
---

# Escenario: TCIH (Teras Capital Investment Holding)

> **Snapshot**: 31/12/2025 — última actualización 2026-05-18 (Claude Code)
> **Fuente principal**: BD Supabase `savenikqhmcuwmcnabca` (`business_lines.teras-capital`, `entities.tcih`, `participations`, `shareholders`, `entity_balances`, `intragroup_balances`) + Auditoría provisional TCIH 02/04/2026 (B88279880) + Mayor PGC TCIH 2025 + fix bug #14 (15-may-2026).

## 1. Snapshot ejecutivo

TCIH (Teras Capital Investment Holding, S.L., NIF **B88279880**) es el **chasis legal transversal** del grupo Teras Capital. No tiene un activo operativo propio ni un waterfall ISHA propio: es la holding que (i) canaliza la financiación Asterion al grupo, (ii) tiene 100% de TCS (Teras Capital Spain), (iii) ostenta 2% directo en Templus CD vía Class B Teras, (iv) genera fees recurrentes de advisory (Templus, Tuca/Olin, Gemswell, Mundo Pacífico — histórico Pacífico Cable). MdL participa **51,66% efectivo look-through** (25,83% IPN directo + 25,83% TCH2 vía IPN 100%); el campo `business_lines.teras-capital.mdl_position_pct=51,67%` redondea esa cifra. Los 48,34% restantes son socios externos: Monforte 25,83% + LSS 7,50% + Menéndez 7,50% + Gurrea-Nozaleda 7,50%. PN contable a 31/12/2025: **-2.441.138€** (negativo, causa de disolución art. 363.1.e LSC). PN ajustado tras override auditor sobre equity-rank: **+5.225.421€** (-2.441K + 7.667K). La causa de disolución técnica se SALVA con la reclasificación de la auditoría provisional 02/04/2026 que califica 7,67M€ de saldos como `shareholder_loans_as_equity`, distinguidos de los 2,10M€ de subrogación Asterion clase B (debt-rank, NO equity).

## 2. Ficha del activo

| Parámetro | Valor | Fuente |
|---|---|---|
| Línea BD | `business_lines.teras-capital` short_name `TERAS CAPITAL` | BD |
| Sector | Advisory/Servicios | BD |
| Sponsor | NULL — no aplica (chasis legal) | BD |
| Status | active | BD |
| Naturaleza | Holding transversal, no línea operativa con waterfall | doctrinal |
| Entidad principal | Teras Capital Investment Holding, S.L. | BD `entities.tcih` |
| NIF | B88279880 | BD + audit |
| Entity type | SL (sociedad limitada) | BD |
| Admin Único | Luis Sánchez Salmerón (DNI 00696300K) | escrituras + audit |
| Filial 100% | TCS (Teras Capital Spain) | BD `participations` |
| Participación directa Class B Teras | 2,00% Templus CD (no vía TCH4) | BD `participations` + Org chart Templus v8 14/04/2026 |
| Participación residual TCH4 | 0,01% (cc_balance 15.264€, NO en `participations` — figura como referencia residual operativa) | mayor PGC + nota interna |
| Cap% MdL look-through | **51,66%** (25,83% IPN + 25,83% TCH2 × 100% IPN/TCH2) | participations + look-through |
| Cap% declarado BD | 51,67% (redondeo en `business_lines.teras-capital.mdl_position_pct`) | BD |
| 6 socios TCIH | IPN 25,83% + TCH2 25,83% + Monforte 25,83% + LSS 7,50% + Menéndez 7,50% + Gurrea 7,50% | BD `shareholders` (suma 100,02% por redondeo) |
| Capital RM inscrito | 3.099€ | mayor 100 + nota auditor |
| Capital efectivo (acordeón) | 20.000€ (3.099€ inscritos + 16.901€ AK pendiente inscripción RM cuenta 55100008) | mayor + escritura 25/11/2022 |
| Activo total 2025 | 7.993.932,32€ | BD `entity_balances.tcih` 2025 |
| PN contable 2025 | -2.441.138,31€ (NEGATIVO) | BD |
| PN ajustado (post equity-rank) | +5.225.421€ | derivado override audit |
| Pasivo total 2025 | 10.435.070,63€ | BD |
| Shareholder loans as equity | 7.666.559€ (override auditor) | BD + audit_2026_provisional |
| Bank debt | 14.171,17€ (solo tarjetas crédito reales — 12 VISA CAIXABANK + AMEX en cuentas 520xxxxx) | BD + parser_fix_bug14 |
| Asterion deuda externa real (PNC otra) | 1.802.438,86€ (cuenta 17100008) | BD pnc_otra + fix bug #14 |
| Subrogación Asterion clase B (debt-rank, NO equity) | 2.101.899€ (other_intragroup_debt) | BD + audit override |
| Ingresos 2025 | 1.674.208,05€ (fees advisory) | BD |
| Gastos 2025 | 2.185.341,05€ | BD |
| Net result 2025 | -511.133,00€ | BD |
| Causa art. 363.1.e LSC | TÉCNICAMENTE ACTIVA en PN contable, SALVADA en PN ajustado | derivado |
| Año fiscal referencia | 31/12/2025 | BD |
| Source override | `audit_2026_provisional + parser_fix_bug14` | BD `entity_balances.source` |

## 3. Estructura societaria

Cadena look-through MdL → TCIH (chasis) → activos del grupo:

```
mdl-persona (Miguel de Lucas Sánchez)
  │ 100,00% (Ordinarias)
  ▼
IPN (Inteligencia Procesos de Negocio, SLU) NIF B87680328
  │
  ├─ 25,83% TCIH (Ordinarias) — directo
  │
  └─ 100% TCH2 (Holding patrimonial personal MdL)
        │
        └─ 25,83% TCIH (Ordinarias) — indirecto MdL (TCH2 = 100% IPN ⇒ 100% MdL)
              │
              ▼
TCIH (Teras Capital Investment Holding, S.L.) NIF B88279880
  │   Otros socios TCIH (48,34% externos):
  │   • Monforte Consultoría de Telecomunicaciones, S.L. 25,83% (Jorge Monforte — tras ampliación sept 2022)
  │   • LSSALMERON Inversiones, S.L. 7,50% (Luis Sánchez Salmerón — reducida desde posición original)
  │   • Moisés Menéndez Andrés 7,50% (nuevo socio sept 2022)
  │   • Enrique Gurrea-Nozaleda Hörnlein 7,50% (nuevo socio sept 2022)
  │
  ├─ 100,00% TCS (Teras Capital Spain) — filial 100%
  │       │
  │       └─ histórico Pacífico Cable Chile (desinvertido dic-2021)
  │       └─ cliente activo 2025 ~207K€ facturado
  │
  ├─ 2,00% Templus CD (Class B Teras directo) — Org chart Templus v8 14/04/2026
  │       (relación TERAS CD operativa con TCH4 paralela, NO consolidada con TCH4)
  │
  └─ ~0,01% TCH4 (participación residual, cc_balance 15.264€ — figura en mayor pero NO en participations)
```

**Cap% efectivo MdL en TCIH (look-through compuesto)**:
- Tramo directo MdL → IPN → TCIH: 100% × 25,83% = **25,83%**
- Tramo indirecto MdL → IPN → TCH2 → TCIH: 100% × 100% × 25,83% = **25,83%**
- **Total efectivo MdL: 51,66%** (suma exacta).
- `business_lines.teras-capital.mdl_position_pct = 51,67%` redondea 0,01pp por arriba.
- Verificación SQL: `SELECT SUM(ownership_pct) FROM participations WHERE child_entity_id='tcih' AND parent_entity_id IN ('ipn','tch2');` → 51,66.

Detalle completo y composición pool en `resources/cap-table-detallado.md` y `resources/look-through-engine.md`.

## 4. Estructura equity-rank vs debt-rank

TCIH NO tiene deal económico tradicional ni waterfall ISHA: es la pieza donde se canaliza la **financiación Asterion** al grupo MdL y donde se acumulan los saldos intragrupo con TCH1/TCH2/TCH3/TCH4. La arquitectura económica relevante son las **tres capas de pasivo** (préstamos participativos, cuentas corrientes socios, financiación externa Asterion) y el **override de auditoría provisional 02/04/2026** que reclasifica parte de esos pasivos a equity-rank.

### Composición equity-rank — 7.666.559€ (override audit_2026_provisional)

Aportaciones directas de los socios MdL + LSS + Monforte calificadas como `shareholder_loans_as_equity`:

| Socio aportante | Importe (€) | Cuentas origen |
|---|---|---|
| TCH2 | 4.594.000 | 52100001 PTMO PARTICIPATIVO TCH DOS (4.000K) + 55100004/55100010 C/C TCH2 (594K identificados auditor) |
| Monforte Consultoría | 1.691.000 | 52100005 PTMO Monforte (690K) + 55100006 C/C Monforte (1.001K identificados auditor) |
| IPN | 1.140.000 | 55100002 C/C IPN + identificaciones auditor |
| LSSALMERON | 241.000 | 55100001 C/C LSS |
| **TOTAL EQUITY-RANK** | **7.666.000** | (cifra exacta 7.666.559€ por residuales) |

Adicional cuenta 521 explícita en mayor: 52100008 PTMO Gurrea 200K (parte de la subrogación, no de equity MdL).

### Composición debt-rank Asterion — 2.101.899€ (NO equity)

Subrogación Asterion clase B: socios externos cuya posición acreedora en TCIH viene de canalización Asterion (cuentas 55100005 + 55100007 + 5525x según socio):

| Socio subrogado | Importe (€) |
|---|---|
| Gurrea-Nozaleda | 541.000 |
| Menéndez Andrés | 316.000 |
| Izzo (Tuca persona física) | 354.000 |
| Ávila | 200.000 |
| Triguero | 125.000 |
| S. Echebarría | 92.000 |
| Huarte | 67.000 |
| Caporaleti | 58.000 |
| Gurrea-TUCA | 348.000 |
| **TOTAL DEBT-RANK** | **2.101.000** |

Esta partida es **deuda intragrupo subrogada**, no aportación de capital. Asterion sigue siendo el último acreedor económico vía cadena Tuca Midco → Tuca Bidco; los socios B son conductos contractuales. Fiscal y contablemente debe presentarse en `other_intragroup_debt`, NO en `shareholder_loans_as_equity`.

### Asterion deuda externa directa — 1.802.439€

Cuenta 17100008 PTMO ASTERION. Tras el fix bug #14 (15-may-2026) sale de `pnc_bancario` a `pnc_otra` (es deuda intragrupo subrogación, no bancaria). Tasa de referencia 7% anual.

### Bank debt real — 14.171€

12 tarjetas VISA CAIXABANK + AMEX en cuentas 520xxxxx. Es el ÚNICO `bank_debt` material de TCIH; cualquier referencia a "deuda bancaria TCIH" que cite cifras mayores está mezclando deuda intragrupo (521 + 17100008) con bancaria.

Detalle composición por cuenta + verificación SQL en `resources/cifras-2025-detalle.md`.

## 5. Stakeholders

| Actor | Rol | Participación / Prioridades | Gestión TERAS |
|---|---|---|---|
| Pool MdL (IPN + TCH2) | Accionistas mayoritarios | 51,66% efectivo | Voz coordinada en asamblea, control consejo |
| Monforte Consultoría | Socio externo | 25,83% — segundo bloque más grande | Foro asamblea, alineamiento decisiones materiales |
| LSSALMERON Inversiones | Socio externo + Admin Único persona física LSS | 7,50% — Luis Sánchez Salmerón firmante operativo TCIH | Admin Único ejecuta, cuentas anuales, RM |
| Moisés Menéndez | Socio externo (nuevo sept 2022) | 7,50% + posición subrogación Asterion clase B 316K€ | Asamblea + reconciliación posición individual |
| Enrique Gurrea-Nozaleda | Socio externo (nuevo sept 2022) | 7,50% + posición subrogación Asterion clase B 541K€ + 348K vía TUCA | Asamblea + reconciliación posición individual |
| Asterion | Sponsor financiero (último acreedor económico de la subrogación) | Servicio deuda 1,80M€ + sigue acreedor económico de la subrogación 2,10M€ | Reporting trimestral, transparencia |
| Auditor provisional (B88279880) | Auditor 02/04/2026 | Override equity-rank 7,67M€ + identificación debt-rank 2,10M€ | CFO TERAS sign-off, conciliación final |
| Asesores legales | Cumplimiento art. 363.1.e LSC + inscripción acordeón sep-22 + cesiones crédito | CLO super-poder | |
| Asesores fiscales | NRV 19ª (TCIH→TCS/Templus CD/TCH4), BINs acumuladas, planificación cesión crédito a socios TCH1 | CFO super-poder | |
| TCH1 / TCH2 / TCH3 / TCH4 | Contrapartes intragrupo (9 saldos) | Conciliación bilateral, reclasificación cuentas | CFO TERAS + audit firm |
| TCS (filial 100%) | Vehículo histórico Pacífico Cable + cliente activo 2025 | Distribución dividendos, advisory continuo | TCIH directo |

Asamblea TCIH: anual + ad-hoc. Quórum de supermayoría requerido para decisiones materiales (acordeón, modificación bylaws, distribución dividendos, autorización litigios). Detalle gobierno en `resources/governance.md`.

## 6. Cifras 2025

> Snapshot 31/12/2025. Source BD `entity_balances.tcih` = `audit_2026_provisional + parser_fix_bug14`.

### Balance TCIH (FY 2025)

| Concepto | Valor (€) | Notas |
|---|---|---|
| **Activo total** | 7.993.932,32 | |
| Caja | 109.069,96 | |
| Activo no corriente | 3.252.154,56 | Inversión TCS + Templus CD + créditos LP a TCH1 |
| Activo corriente (sin caja) | 8.157.848,10 | (incluye dividendo a cta 2,3M cuenta 557 + C/C deudoras intercompany) |
| **Patrimonio neto contable** | **-2.441.138,31** | NEGATIVO |
| Capital social (BD) | 20.000,00 | Capital efectivo (RM=3.099€, AK pendiente=16.901€ — acordeón sep-22 no inscrito) |
| Reservas | 366.999,16 | |
| Resultado pendiente regularizar | -511.133,00 | Resultado 2025 |
| Aportaciones socios | 0,00 | |
| **Shareholder loans as equity (override)** | **7.666.559,00** | Equity-rank: TCH2 4.594K + Monforte 1.691K + IPN 1.140K + LSS 241K |
| **PN ajustado (post equity-rank)** | **+5.225.421** | -2.441.138 + 7.666.559 — salva art. 363.1.e LSC |
| **Total pasivo** | 10.435.070,63 | |
| Pasivo NC bancario | 0,00 | (fix bug #14: 17100008 reclasificado) |
| Pasivo NC otra | 1.802.438,86 | Asterion deuda externa real (cuenta 17100008) |
| Pasivo NC vinculadas | 0,00 | |
| Pasivo C bancario | 14.171,17 | 12 VISA CAIXABANK + AMEX (cuentas 520xxxxx) |
| Pasivo C vinculadas | 0,00 | |
| Pasivo C comercial | 5.854,48 | |
| Pasivo C HP/SS | 130.345,14 | |
| Pasivo C otras | 4.817.297,81 | (incluye 521 PTMO PARTICIPATIVO + 5510x C/C socios + dividendo a cta) |
| **Bank debt real** | **14.171,17** | Solo tarjetas crédito |
| Other intragroup debt | 2.101.899 | Subrogación Asterion clase B (debt-rank, NO equity) |
| **Ingresos** | 1.674.208,05 | Fees advisory: Templus + Tuca/Olin + Gemswell + Mundo Pacífico + cliente Pacífico Cable 207K |
| **Gastos** | 2.185.341,05 | |
| **Net result 2025** | -511.133,00 | |
| Descuadre balance | 0,00 | Cuadra A = PN + P (post override) |

### Reconciliación PN contable → PN ajustado

```
PN contable (BD `total_equity`)                    -2.441.138,31€
+ Shareholder loans as equity (override auditor)   +7.666.559,00€
─────────────────────────────────────────────────────────────────
PN ajustado                                        +5.225.420,69€
```

La cifra +5,22M€ es la que justifica que la **causa de disolución técnica art. 363.1.e LSC se considera salvada** por la auditoría provisional. Detalle de cuentas + composición auditada en `resources/cifras-2025-detalle.md` y análisis legal completo en `resources/disolucion-tecnica-art363.md`.

### TCIH es contraparte de 5 de los 9 saldos intragrupo

| # | Saldo | Importe (€) | Posición TCIH |
|---|---|---|---|
| 6 | TCH2 → TCIH (C/C) | 606.408,42 | Acreedor TCH2 (pasivo TCIH) |
| 7 | TCH2 → TCIH (participative) | 4.000.000 | Acreedor TCH2 cuenta 521 (pasivo TCIH, equity-rank en override) |
| 4 | IPN → TCIH (C/C) | 1.403.258,40 | Acreedor IPN (pasivo TCIH, incluye PROYECTO TUCA 1.176K) |
| 8 | TCIH → TCH1 (C/C) | 4.430.680 | Deudor TCH1 (activo TCIH) |
| 9 | TCIH → TCH1 (loan_lp) | 1.444.806 | Deudor TCH1 (activo TCIH) |

Listado completo de los 9 saldos BD `intragroup_balances` con categorización cross-cat / intra-cat + equity-rank vs debt-rank en `resources/intragrupo-9-saldos.md`.

## 7. Governance

| Foro | Cadencia | Asistencia | Owner agenda |
|---|---|---|---|
| Asamblea ordinaria TCIH | Mínimo anual (1 ejercicio) | 6 socios (IPN, TCH2, Monforte, LSS, Menéndez, Gurrea) + Admin Único | LSS (Admin) coordina |
| Asamblea extraordinaria TCIH | Ad-hoc (acordeón, modificación bylaws, autorización litigios) | 6 socios + asesor legal | LSS + CLO TERAS |
| Auditoría externa provisional | 02/04/2026 ejecutada | B88279880 | CFO TERAS + audit firm |
| Auditoría externa definitiva | Pendiente firma final 2025 | Misma firma | CFO + audit firm |
| Conciliación intercompany | Continua (5 saldos TCIH ↔ TCH1/TCH2/IPN) | CFO + auditores TCIH + TCH1 + TCH2 + IPN | CFO TERAS |
| Comité riesgo legal (363.1.e LSC) | Ad-hoc 2026 | CLO + CFO + asesor legal | CLO TERAS |
| Comité refinanciación Asterion (cuando proceda) | Ad-hoc 2027+ | CFO + CLO + Asterion | CFO + Asterion |
| Inbox bot agente documentalista | Continuo | Bot `bot@terascap.es` clasifica | TERAS automatizado |

RACI extendido + org chart asistentes + ciclo cuentas anuales en `resources/governance.md`.

## 8. Fiscalidad

### Art. 363.1.e LSC — disolución técnica

- **Condición legal**: PN < ½ capital social → causa de disolución de pleno derecho.
- **Situación TCIH 2025**: PN contable -2.441.138€ vs capital efectivo 20.000€ → la condición se cumple ampliamente (PN es negativo, ya está por debajo de cualquier umbral).
- **Solución aplicada**: auditoría provisional 02/04/2026 reclasifica 7.666.559€ de aportaciones de socios (cuentas 521 + 55x identificadas) a `shareholder_loans_as_equity` → PN ajustado +5.225.421€ → causa SALVADA contable y financieramente.
- **Riesgo no resuelto**: la **inscripción en RM del acordeón sep-22** (escritura 25/11/2022) sigue **pendiente >3 años**. Severidad MEDIA (no ALTA): el acuerdo societario es válido entre las partes (art. 21 CCom); la no inscripción afecta solo inoponibilidad frente a terceros de buena fe. No hay riesgo de caducidad.
- Análisis legal completo + jurisprudencia TS aplicable en `resources/disolucion-tecnica-art363.md`.

### NRV 19ª PGC — inversiones empresas grupo / multigrupo / asociadas

TCIH valora sus participaciones a coste menos deterioro:
- **TCS (100%)**: empresa del grupo (control ≥50%). Coste histórico, prueba deterioro anual.
- **Templus CD (2% Class B Teras)**: cap% <20%, calificación como inversión financiera (NO grupo NRV 19ª salvo influencia significativa documentada).
- **TCH4 (0,01% residual)**: financiera, no consolidación.
- Detalle por inversión + amortizaciones contables en `resources/fiscalidad-detallada.md`.

### Equity-rank vs debt-rank — implicación fiscal

- **Equity-rank 7,67M€ (reclasificación auditor)**: técnicamente sigue siendo pasivo financiero en balance (cuenta 521 + 55x); NO se reclasifica jurídicamente a capital. Implicación fiscal: los intereses devengados son ingreso financiero para los acreedores y gasto financiero deducible para TCIH. La calificación "equity-rank" es contable / financiera (clasificación PN), no societaria.
- **Debt-rank Asterion 2,10M€ (subrogación clase B)**: pasivo financiero, NO reduce base IS. Para los socios B subrogados: obligación de pago a TCIH (operación financiera personal, no renta del trabajo).

### Cesión crédito TCIH → socios TCH1 (planificación pendiente)

- Hipótesis: TCIH cede su crédito de 4,08M€ contra TCH1 a los socios TCH1 prorrata participación, simplificando intercompany.
- Pendiente: valoración cesión (nominal vs descuento) + deducibilidad pérdida (art. 13.1 LIS si descuento) + cuantificación BINs TCIH compensables (art. 26 LIS, límite 70%).

### Cuenta 557 dividendo a cuenta 2,3M€

- Origen: distribución a cuenta 2021 tras desinversión Pacífico Cable.
- Naturaleza: devolución aportaciones + dividendo a cuenta combinado.
- Es la **CAUSA PRINCIPAL** del PN negativo contable.
- Pendiente: regularización formal vía cuentas anuales o saneamiento adicional.

Análisis completo + escenarios planificación en `resources/fiscalidad-detallada.md`.

## 9. Riesgos y mitigantes

| # | Categoría | Riesgo | P | I | Mitigante |
|---|---|---|---|---|---|
| 1 | Legal | Inscripción acordeón sep-22 en RM pendiente >3 años | A | M | Inscribir cuanto antes (no caduca pero genera inoponibilidad frente a terceros) |
| 2 | Legal | Art. 363.1.e LSC — causa disolución técnica si PN ajustado vuelve a quedar < ½ capital | M | A | Override auditor mantenido + monitorizar dividendos / pagos |
| 3 | Financiero | Refinanciación o ejecución Asterion 1,80M€ (cuenta 17100008) | M | M | Negociación, calendario con Asterion |
| 4 | Contable | Conciliación bilateral pendiente: hallazgo TCIH-C-02 (PTMO TCH2 4M contable vs 3M contractual) | A | M | Conciliación con TCH2 + audit firm sign-off |
| 5 | Contable | Préstamos Gurrea (200K) e IPN sin contratos formales localizados (H-03 audit) | A | M | Formalización ex-post + opinion letter |
| 6 | Documentos | SPA Pacífico Cable + acuerdo dividendo TCS→TCIH ausentes (H-04 audit) | M | A | Búsqueda + reconstrucción documental |
| 7 | Reputacional | Calificación equity-rank vs debt-rank cuestionada por nuevo auditor | B | A | Audit firm sign-off + opinion letter independiente |
| 8 | Fiscal | BINs acumuladas TCIH no aprovechadas (PN negativo histórico) | M | M | Cuantificar BINs + planificar cesión crédito a socios para activar |
| 9 | Operativo | TCS cliente activo Pacífico Cable 2025 (~207K facturado) — continuidad relación | B | B | Renovación contractual + monitorización |
| 10 | Identidades | Dime Shared / Quarter Capital vínculo societario no documentado (H-02 audit) | B | B | Aclaración legal vía CLO |
| 11 | Look-through | `business_lines.teras-capital.mdl_position_pct=51,67%` vs efectivo 51,66% | B | B | Documentar redondeo + propagar a calculadoras |

Detalle severidad + plan mitigación + dueño en risk register interno + `resources/decisiones-clave.md`.

## 10. Hitos próximos

| Fecha | Hito | Owner |
|---|---|---|
| Q2 2026 | Cierre auditoría definitiva TCIH 2025 (firma final) | CFO TERAS + audit firm B88279880 |
| Q2 2026 | Inscripción acordeón sep-22 en RM (eliminar inoponibilidad) | CLO TERAS + notaría |
| Q2 2026 | Conciliación bilateral hallazgo TCIH-C-02 (PTMO TCH2 4M vs 3M) | CFO + audit firm |
| Q2-Q3 2026 | Formalización contratos pendientes (Gurrea 200K, IPN) | CLO TERAS |
| Q3 2026 | Decisión cesión crédito TCIH → socios TCH1 (Escenario A/B/C planificación) | CFO + CLO + asesor fiscal |
| Q3 2026 | Localizar SPA Pacífico Cable + acuerdo dividendo TCS (H-04) | CLO TERAS |
| Q4 2026 | Asamblea ordinaria TCIH — aprobación cuentas + saneamiento patrimonial | LSS Admin Único + socios |
| 2027 | Cuantificación BINs + activación vía intereses cesión crédito | Asesor fiscal |
| 2027+ | Negociación refinanciación o liquidación 17100008 Asterion | CFO + Asterion |

## 11. Anti-patrones IA — errores típicos a evitar

1. **NO meter la subrogación Asterion 2.10M€ como equity-rank**. Es **debt-rank** (`other_intragroup_debt`). Los socios externos clase B (Gurrea, Menéndez, Izzo, Ávila, Triguero, S.Echebarría, Huarte, Caporaleti, Gurrea-TUCA) son conductos contractuales de la financiación Asterion, no aportantes de capital. La auditoría provisional 02/04/2026 lo dejó **explícitamente** fuera de `shareholder_loans_as_equity`.
2. **NO confundir cuenta 521 (PTMO PARTICIPATIVO) con préstamos bancarios estándar PGC**. La codificación 521 en TCIH es interna y se aplica a préstamos participativos de socios MdL (TCH2 4M, Monforte 690K, Gurrea 200K). El estándar PGC para préstamos participativos sería 158/159. El parser tenía un bug (#14) que clasificaba 521 como `pc_bancario`; tras el fix 15-may-2026 ya NO entra como deuda bancaria.
3. **NO presentar PN contable -2,44M€ sin mencionar el PN ajustado +5,22M€**. La cifra contable refleja la situación previa al override auditor; la cifra ajustada (-2,44M + 7,67M = +5,22M) refleja la situación tras la reclasificación de equity-rank, que es la base sobre la que se considera SALVADA la causa de disolución art. 363.1.e LSC. Citar solo una de las dos es inducir a error.
4. **NO presentar `bank_debt` 14.171,17€ como deuda bancaria material**. Son 12 tarjetas VISA CAIXABANK + AMEX en cuentas 520xxxxx. La "deuda financiera" relevante de TCIH (a discutir según contexto) es la Asterion 1,80M€ (cuenta 17100008, `pnc_otra`) y, si se incluye, la subrogación clase B 2,10M€ debt-rank. La cifra 14K€ no se cita como deuda bancaria a bancos ni en presentaciones.
5. **NO confundir capital RM (3.099€) con capital efectivo (20.000€)**. El acordeón sept-22 (escritura 25/11/2022) reduce a 0 y amplía a 20.000€ por compensación de créditos, pero la inscripción RM sigue **pendiente**. RM=3.099€, efectivo=20.000€. Cuando se presente capital social: usar 20.000€ con nota "(RM=3.099€, AK pendiente inscripción)" o explicitar la situación.
6. **NO citar "51,67%" como look-through preciso**. La cifra exacta es **51,66%** (25,83% IPN + 25,83% TCH2 vía IPN 100%). El campo `business_lines.teras-capital.mdl_position_pct=51,67%` redondea 0,01pp. Para cálculos preciso usar 51,66%; para presentaciones puede usarse 51,67% indicando "redondeo a dos decimales".
7. **NO confundir TCIH con TCH4**. TCIH es chasis legal transversal del grupo Teras; TCH4 es la línea Templus Data Centers. TCIH tiene 2% directo en Templus CD (Class B Teras) y 0,01% residual en TCH4; son posiciones distintas.
8. **NO presentar TCIH como línea operativa con waterfall ISHA**. NO existe waterfall ISHA propio TCIH; los waterfalls relevantes son Olin (TUCA), Templus (TCH4 chain) y Gemswell (TCH3 chain). TCIH es chasis legal + holding de servicios.

## 12. Lint específico TCIH

```
TCIH LINT 1 — ¿Has citado fuente para cada cifra (audit / mayor / email / BD)?
TCIH LINT 2 — ¿Distingues PN contable -2,44M€ del PN ajustado +5,22M€?
TCIH LINT 3 — ¿La subrogación Asterion clase B 2,10M€ está marcada como debt-rank (NO equity)?
TCIH LINT 4 — ¿La composición de equity-rank 7,67M€ cita los 4 socios MdL (TCH2/Monforte/IPN/LSS) con importes exactos?
TCIH LINT 5 — ¿Has reflejado el estado del acordeón sep-22 (no inscrito RM, pero válido inter partes)?
TCIH LINT 6 — ¿Has usado look-through 51,66% (no 51,67%) para cálculos precisos?
TCIH LINT 7 — ¿Has separado bank_debt 14K€ (tarjetas) del Asterion 1,80M€ (cuenta 17100008 pnc_otra)?
TCIH LINT 8 — ¿Has mencionado el fix bug #14 cuando se hable de cuentas 521xxxxx o 17100008?
TCIH LINT 9 — ¿La causa disolución art. 363.1.e LSC aparece como SALVADA (no activa) tras el override auditor?
TCIH LINT 10 — ¿El output NO confunde TCIH (chasis) con líneas operativas (Olin/Templus/Gemswell)?
TCIH LINT 11 — ¿Has separado los 9 saldos intragrupo en cross-cat (cruzan categorías personal/teras/patrimonial/quarter) vs intra-cat?
```

## Recursos

- [Cap table detallado](resources/cap-table-detallado.md)
- [Deal terms (ISHA cap structure + acordeón sep-22)](resources/deal-terms.md)
- [Cifras 2025 detalle](resources/cifras-2025-detalle.md)
- [Governance](resources/governance.md)
- [Fiscalidad detallada](resources/fiscalidad-detallada.md)
- [Decisiones clave](resources/decisiones-clave.md)
- [Documentos referencia](resources/documentos-referencia.md)
- [Intragrupo — 9 saldos detallados](resources/intragrupo-9-saldos.md)
- [Disolución técnica art. 363.1.e LSC](resources/disolucion-tecnica-art363.md)
- [Look-through engine (51,66% MdL)](resources/look-through-engine.md)
