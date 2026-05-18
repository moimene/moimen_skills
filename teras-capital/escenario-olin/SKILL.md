---
name: escenario-olin
capa: L3b-escenarios
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras, challenge-cognitivo-teras]
triggers: >
  Se activa cuando el usuario menciona Olin, OLIN, TUCA, Tuca Bidco, Tuca Midco,
  Asterion, MasOrange, Mas Orange, MORG, TCH1, Teras Capital Holding 1,
  steerco TUCA, refinanciación Asterion, Class A Clase A, Class B Clase B,
  Privilegiadas TUCA, ISHA TUCA, cupón preferente TUCA.
description: >
  Precarga contexto operativo, contable, legal y fiscal del activo OLIN (TCH1 →
  Tuca Bidco → MasOrange) con Asterion como sponsor financiero. Cubre cap table
  efectivo MdL 46,03% en TCH1, paquete económico Class B + Privilegiadas (8,49%
  efectivo en TUCA), ISHA con hurdle 270M€ y 4 escenarios exit calibrados con
  BD savenikqhmcuwmcnabca.
---

# Escenario: Olin

> **Snapshot**: 31/12/2025 — última actualización 2026-05-18 (Claude Code)
> **Fuente principal**: BD Supabase `savenikqhmcuwmcnabca` (`business_lines.olin`, `entities`, `participations`, `shareholders`, `entity_balances`, `exit_scenarios`, `waterfall_params`) + auditoría TUCA 2024 + ISHA + Anexo IV Auditoría TCH1.

## 1. Snapshot ejecutivo

Olin es la línea de negocio de TERAS Capital sobre **MasOrange** (telco España), vehiculada a través de **Tuca Bidco** y **Tuca Midco**, financiada por **Asterion**. MdL participa vía **TCH1** con cap% efectivo look-through **46,03%** (31,97% IPN directo + 14,06% vía TCH2), y desde TCH1 a TUCA con paquete Class B Ordinarias (17,75% econ) + Privilegiadas (0,696% econ) que totaliza **18,45% derechos económicos** sobre 1,80% del capital. El cap% efectivo final MdL en TUCA es **0,83% capital · 8,49% económico**. Inversión MdL agregada en TCH1: **1.479.243€**. Fase: operativo + NBO MasOrange firme pendiente + refinanciación Asterion en horizonte 2027-2028. Hurdle ISHA 270M€; escenario base sale price 400M€ devuelve aprox 7,3M€ netos MdL.

## 2. Ficha del activo

| Parámetro | Valor | Fuente |
|---|---|---|
| Línea BD | `business_lines.olin` short_name `OLIN` | BD |
| Sector | Telecomunicaciones | BD |
| Sponsor | Asterion | BD |
| Status | active | BD |
| Vehículo MdL en cadena | TCH1 (TCH Uno Holding & Management, S.L.) NIF B88547583 | BD `entities.tch1` |
| Vehículo operativo | Tuca Bidco SL (S.à r.l.) | BD `entities.tuca` |
| Vehículo aguas arriba | Tuca Midco Limited (98% TUCA, Class A + Privilegiadas, integra Asterion) | BD shareholders |
| Activo subyacente | MasOrange (telco España post-fusión Orange + MásMóvil) | público |
| Fase | Operativo + NBO MasOrange firme pendiente + refinanciación Asterion 2027-2028 | comunicación interna |
| Cap% MdL efectivo en TCH1 | **46,03%** (31,97% IPN + 14,06% TCH2) | look-through participations + audit Anexo IV |
| Cap% TCH1 declarado en `mdl_position_pct` business_line | 0,53% efectivo final TUCA (NO confundir con TCH1) | BD `business_lines.olin.mdl_position_pct` |
| Factor `waterfall_params.mdl_pct_tch1` | 38,14% (discrepancia con look-through real 46,03% — documentar en decisiones-clave) | BD `waterfall_params` |
| Cap% TCH1 en TUCA | 1,80% capital (Class B Ord 17,75% econ + Privilegiadas 0,696% econ = 18,45% econ total) | ISHA Cl. 3 + audit |
| Cap% MdL efectivo final en TUCA | 0,83% capital · **8,49% económico** | look-through compuesto |
| Total invertido TCH1 en TUCA | 1.479.243€ | BD `waterfall_params.tch1_total_invested` |
| Participaciones TCH1 en TUCA | 15.481 ordinarias + 13.966 preferentes | BD `waterfall_params` |
| Total participaciones TUCA | 87.207 ordinarias + 2.006.194 preferentes = 2.093.401 | BD `waterfall_params` |
| Cupón preferente TUCA | 10% anual | ISHA Cl. 8(D) |
| Tasa Asterion sobre deuda TCIH | 7% | Acuerdo financiación Asterion |
| Deuda neta default TUCA | 35.000.000€ | BD `waterfall_params` |
| Refinanciación amount referencia | 90.000.000€ | BD `waterfall_params.refinancing_amount` |
| Hurdle ISHA | 270.000.000€ | BD `exit_scenarios.hurdle_amount` |
| Total pref invested | 270.000.000€ | BD `waterfall_params.total_pref_invested` |
| Investment date | 2022-02-18 | BD `waterfall_params.investment_date` |
| New manager dilution cap | 10% (ISHA Cl. 6.4(C)) | BD |
| TCH1 cap% ord diluido | 15,97% (post dilución máx 10% managers) | ISHA |
| Cupón Class D — N/A | (es de Templus, no Olin) | — |
| Tipo IS aplicable a TCH1 | 25% — **SIN exención art. 21 LIS** (look-through MdL final < 5% en TUCA) | BD `waterfall_params.is_rate_tch1_pct` + LIS |
| TCH1 balance 2025 | Activo 4.080.441€ · PN 379€ · Pasivo 4.080.062€ (entidad de paso) | BD `entity_balances.tch1` |
| TUCA balance 2024 | Activo 405.767.446€ · PN 248.552.828€ · Pasivo 157.214.619€ | BD `entity_balances.tuca` |
| Audit firm | (pendiente confirmar — audit TUCA 2024 + Anexo IV TCH1 disponibles en `bl_documents`) | BD |
| Año fiscal referencia | 31/12/2025 (TCH1); TUCA usa FY 2024 | BD `entities` |

## 3. Estructura societaria

Cadena efectiva look-through MdL → MasOrange:

```
mdl-persona (Miguel de Lucas Gutiérrez)
  │ 100,00% (Ordinarias)
  ▼
IPN (Inteligencia Procesos de Negocio, SLU) NIF B87680328
  │ 31,97% directo TCH1 (Clase A)
  │ 100% TCH2
  ▼     ▼ 14,06% TCH1 (Clase A)
   ◀────┘
TCH1 (TCH Uno Holding & Management, S.L.) NIF B88547583
  │   Otros socios TCH1:
  │   • Monforte Consultoría Telecom 17,99% (Clase A)
  │   • LSSALMERON Inversiones 5,48% (Clase A)
  │   • Enrique Gurrea-Nozaleda 8,06% (Clase A, Asterion-financed via TCIH)
  │   • Moisés Menéndez Andrés 8,06% (Clase A, Asterion-financed via TCIH)
  │   • Pablo Ávila 5,00% (Clase B, Asterion-financed)
  │   • Santiago Sánchez Echevarría 3,13% (Clase B, Asterion-financed)
  │   • Triguero 3,13% (Clase B, Asterion-financed)
  │   • Gonzalo Huarte 1,67% (Clase B, Asterion-financed)
  │   • Ramiro Lafarga 1,46% (Clase B, Asterion-financed)
  │
  │ 1,80% capital + 18,45% económico (Clase B Ord 17,75% + Privilegiadas 0,696%)
  ▼
Tuca Bidco SL  (Activo total 405,8M€ · PN 248,6M€ FY2024)
  │   Otros socios TUCA:
  │   • Tuca Midco Limited 98,00% (Clase A + Privilegiadas — Asterion chain)
  │   • A. Izzo 0,20% (Clase B persona física)
  ▼
MasOrange (telco España post-fusión)
```

**Cap% efectivo MdL en TUCA** (compuesto):
- Capital: **0,83%** = 46,03% TCH1 × 1,80% TUCA
- Económico: **8,49%** = 46,03% TCH1 × 18,45% TUCA (Class B Ord 17,75% + Privilegiadas 0,696%)

> **CRÍTICO**: el campo `business_lines.olin.mdl_position_pct = 0,53%` refleja un cálculo previo con factor `mdl_pct_tch1 = 38,14%` (waterfall_params). El cap% efectivo real look-through MdL en TCH1 es **46,03%** según `participations` y Anexo IV ISHA. Discrepancia documentada en tarea pendiente #11 (BD MdL). Ver `resources/decisiones-clave.md`.

Detalle completo en `resources/cap-table-detallado.md`.

## 4. Deal económico

### Deuda Asterion

- **260M€** estructura mezzanine + senior (referencia general); deuda neta TUCA default modelada 35M€ + refinanciación referencia 90M€.
- **Tasa Asterion 7%** sobre deuda a través de TCIH (saldo intragrupo 1.802K€ en cuentas 17x TCIH, NO bancario).
- **Subrogación Asterion clase B** 2.101.899€ a socios externos en TCIH: Gurrea 541K + Menéndez 316K + Izzo 354K + Ávila 200K + Triguero 125K + S.Echevarría 92K + Huarte 67K + Caporaleti 58K + Gurrea TUCA 348K. **Es deuda intragrupo (debt-rank), NO equity-rank**. Documentado en `escenario-tcih-holding`.
- Refinanciación: horizonte 2027-2028. Riesgo re-pricing por entorno tipos.

### Equity y paquetes TCH1 ↔ TUCA

| Tramo | Quién | Cap TUCA | Económico TUCA |
|---|---|---|---|
| Ordinarias Clase A + Privilegiadas | Tuca Midco (Asterion chain) | 98,00% | mayoritario |
| Ordinarias Clase B | TCH1 | 1,80% (de 1,80% capital) | 17,75% econ |
| Privilegiadas | TCH1 | (incluido en 1,80%) | 0,696% econ |
| Ordinarias Clase B | A. Izzo (persona física) | 0,20% | minoritario |

**Inversión histórica TCH1 en TUCA**:
- Investment date: 2022-02-18.
- Total invertido: 1.479.243€ (15.481 ord + 13.966 pref).
- Dividend Dec 2024 distribuido: 12.000.000€ (a nivel TUCA, prorrateado).

Paquetes detallados (vesting, leaver provisions, key-man) en `resources/deal-terms.md`.

### ISHA y waterfall — 4 escenarios exit BD (`exit_scenarios`)

| Escenario | Sale Price | Hurdle | MdL Gross | MdL Net (post IS 25%) | TCH1 Gross | Múltiplo TCH1 |
|---|---|---|---|---|---|---|
| Sin upside | 250M€ | 270M€ | 530K€ | **480K€** | ~530K€ (solo pref pro-rata 0,696%) | 0,4× |
| Éxito moderado | 350M€ | 270M€ | 5,97M€ | **5,4M€** | ~16M€ | 10,8× |
| Base case Asterion | 400M€ | 270M€ | 11,34M€ | **10,2M€** | ~25M€ | 16,9× |
| Gran éxito | 500M€ | 270M€ | 18,29M€ | **16,5M€** | ~42,7M€ | 28,9× |

> **CRÍTICO**: la diferencia entre "Sin upside" (250M€) y "Éxito moderado" (350M€) es de **10×** en retorno MdL. El waterfall es altamente convexo arriba del hurdle 270M€. Sensibilidad y mecánica completa en `resources/waterfall-y-escenarios-isha.md`.

## 5. Stakeholders

| Actor | Rol | Prioridades | Gestión TERAS |
|---|---|---|---|
| Asterion | Sponsor financiero (Tuca Midco) | Servicio deuda, covenants, refinanciación 2027-2028, exit MasOrange | Reporting trimestral, transparencia |
| Tuca Midco | Vehicle Asterion chain | Governance ISHA, propuestas IC | Cooperación + escalado a Asterion |
| MasOrange management | Operación telco | ARPU, churn, capex network, retention post-fusión | Steerco trimestral, KPIs |
| Tuca Bidco management | Vehicle | Governance ISHA, ejecución plan | Comité bimestral |
| TCH1 — socios MdL | IPN 31,97% + TCH2 14,06% = 46,03% efectivo MdL | Retorno waterfall, alineamiento Class A vs Class B | Voz coordinada en consejo TCH1 |
| TCH1 — socios independientes | Monforte 17,99% + LSS 5,48% + Gurrea 8,06% + Menéndez 8,06% | Misma agenda upside | Asambleas TCH1, comités ad-hoc |
| TCH1 — Class B managers | Ávila 5% + S.Echevarría 3,13% + Triguero 3,13% + Huarte 1,67% + Lafarga 1,46% | Performance, vesting, payout | Mgmt incentive aligned, comités semestrales |
| Asesores legales | Cumplimiento ISHA, SPA, M&A | CLO super-poder | |
| Asesores fiscales | NRV 19ª, art. 21 LIS aplicable, planificación exit | CFO super-poder | |
| Auditor TUCA + TCH1 | Cierre anual + cifras consolidación | CFO + auditoría externa | Anexo IV TCH1 disponible |

## 6. Cifras 2025

> Snapshot: 31/12/2025. TCH1 = `mayor_pgc`; TUCA cifras FY 2024 (último disponible) audit + cap structure.

### TCH1 — vehículo MdL en cadena (FY 2025, `mayor_pgc`)

| Concepto | Valor | Notas |
|---|---|---|
| Activo total | 4.080.441,01€ | Mayor PGC |
| Patrimonio neto | 379,27€ | Casi cero — entidad de paso |
| Capital social | 3.000€ | |
| Resultados anteriores | -2.620,73€ | |
| Total pasivo | 4.080.061,74€ | Casi todo intragrupo |
| Bank debt | 0€ | Sin deuda bancaria propia |
| Ingresos / Gastos | 0€ / 0€ | Vehículo de tenencia |

### TUCA Bidco — vehículo operativo (FY 2024, audit)

| Concepto | Valor |
|---|---|
| Activo total | 405.767.446€ |
| Patrimonio neto | 248.552.828€ |
| Total pasivo | 157.214.619€ |
| Deuda neta default (modelado) | 35.000.000€ |
| Refinanciación referencia | 90.000.000€ |
| Dividend Dec 2024 | 12.000.000€ (a nivel TUCA) |

### MasOrange (públicos)

Métricas operativas no se almacenan en BD MdL (es activo subyacente, no entidad consolidada). Cifras top-line desde MasOrange company report. Ver `resources/cifras-2025-detalle.md`.

Detalle completo + SQL de regeneración en `resources/cifras-2025-detalle.md`.

## 7. Governance

| Foro | Cadencia | Asistencia TERAS | Owner agenda |
|---|---|---|---|
| Steerco TUCA Bidco | Trimestral | CIO + CFO TERAS | TERAS coordina vía TCH1 |
| Consejo MasOrange | Trimestral | Representante TERAS por TUCA | MasOrange + Asterion |
| Comité refinanciación Asterion | Ad-hoc 2027+ | CFO + CLO | Asterion + TERAS |
| Auditoría externa TUCA | Anual | CFO | Audit firm |
| Auditoría externa TCH1 | Anual (Anexo IV) | CFO | Audit firm |
| Asambleas TCH1 (socios) | Mínimo anual + ad-hoc | Todos socios | TCH1 (Monforte / IPN designados) |

RACI extendido + org chart Tuca chain en `resources/governance.md`.

## 8. Fiscalidad

### Art. 21 LIS (exención dividendos / plusvalías inversión grupo)

- **TCH1 sobre TUCA**: cap% TCH1 en TUCA = 1,80% capital — **< 5%, NO aplica exención art. 21 LIS**. Cualquier dividendo o plusvalía de TUCA tributa íntegro en TCH1 al **25% IS**. Confirmado en BD `waterfall_params.is_rate_tch1_pct=25, source='LIS art. 21 — sin exención (<5%)'`.
- **MdL (IPN/TCH2) sobre TCH1**: IPN 31,97% + TCH2 14,06% — **AMBOS > 5%, sí aplica exención** sobre dividendos/plusvalías de TCH1. Pero el problema fiscal está aguas abajo: TCH1 ya tributa al 25%, luego sube neto a IPN/TCH2 con exención.

### NRV 19ª PGC

- TCH1 valora su inversión en TUCA Bidco como **inversión en grupo NRV 19ª** (no consolida; coste menos deterioro). Cualquier dividendo distribuido se reconoce como ingreso financiero pero no genera plusvalía contable.

### Subrogación deuda Asterion 2,10M€ en TCIH

- **NO** se trata como equity-rank por auditoría provisional 02/04/2026. Se mantiene como **debt-rank** (deuda intragrupo subrogada). Esto afecta a la causa de disolución técnica de TCIH (art. 363.1.e LSC), no a Olin directamente. Detalle en `escenario-tcih-holding`.

### Exit fiscal MdL

- Planificación pendiente: cláusulas SPA, retención en origen, escalonamiento, posible reinversión en otra línea TERAS para diferir.
- Estimación neto post IS aplicada a escenarios `exit_scenarios` (10-15% gap entre gross y net, principalmente IS 25% sobre el upside).

Análisis detallado + escenarios alternativos en `resources/fiscalidad-detallada.md`.

## 9. Riesgos y mitigantes

| # | Categoría | Riesgo | P | I | Mitigante |
|---|---|---|---|---|---|
| 1 | Financiero | Refinanciación Asterion 2027-2028 con tipos elevados (referencia 7% subiría) | M | A | Negociación temprana, opcionalidad amortización |
| 2 | Comercial | Churn elevado MasOrange tras fusión Orange+MásMóvil | M | M | KPIs steerco trimestral, foco retention |
| 3 | Regulatorio | CNMC ex-post fusión telco (remedies, espectro) | B | A | Compliance proactivo, remedies negociados |
| 4 | Governance | Conflicto Class A (Asterion/Tuca Midco 98%) vs Class B (TCH1 1,80%) en decisiones supermayoría | B | A | ISHA contempla supermayorías, mediación |
| 5 | Operativo | Capex network mayor que budget MasOrange | M | M | Quarterly review, opex compensatorio |
| 6 | Reputacional | Caso público adverso MasOrange | B | A | Comms plan a nivel grupo |
| 7 | Fiscal | TJUE/TS jurisprudencia sobre cadenas holding | B | M | Asesoría continua, opinion letters |
| 8 | Liquidez TCH1 | TCH1 con PN 379€ y pasivo 4M€ depende de servicio dividendos TUCA | M | A | Política dividendos TUCA, refi |

## 10. Hitos próximos

| Fecha | Hito | Owner |
|---|---|---|
| Q2 2026 | NBO MasOrange firme + IC TERAS | CIO TERAS |
| Q2-Q3 2026 | Cierre auditoría externa TUCA 2025 + Anexo IV TCH1 | CFO + audit firm |
| Q3 2026 | Steerco TUCA Q3 | TERAS coordina |
| Q4 2026 | Asamblea TCH1 (alineamiento socios, dividendos) | TCH1 |
| 2027 | Inicio conversaciones refinanciación Asterion | CFO TERAS + Asterion |
| 2028 | Refinanciación Asterion ejecutada | CFO + Asterion |
| 2029+ | Ventana exit MasOrange (estimado, sale price referencia 400M€ base case) | CIO TERAS + Asterion + Tuca Midco |

## 11. Anti-patrones IA — errores típicos a evitar

1. **NO confundir cap% MdL en TCH1 (46,03%) con cap% en TUCA (0,83% cap / 8,49% econ) ni con `mdl_position_pct=0,53%` del business_line**. Son 3 capas distintas. El valor `business_lines.olin.mdl_position_pct=0,53%` es el cap% económico FINAL en TUCA calculado con factor `mdl_pct_tch1=38,14%` (discrepa de 46,03% look-through real — anotar).
2. **NO meter la subrogación Asterion 2,10M€ como equity-rank de TCIH**. Es debt-rank. Los socios financiados por Asterion (Gurrea, Menéndez, Izzo, Ávila, Triguero, S.Echevarría, Huarte, Caporaleti, Lafarga, Gurrea-TUCA) tienen deuda intragrupo con TCIH, no aportación de capital.
3. **NO confundir TCH1 con Tuca Bidco**. TCH1 es vehículo MdL en cadena (holding); Tuca Bidco es vehículo operativo que controla MasOrange. **Tuca Midco** es la matriz aguas arriba que integra Asterion (98% de Tuca Bidco).
4. **NO inventar cifras NAV de Asterion**. Pedirlas al sponsor o citar email. Si no hay, etiquetar `[estimado]` con fuente del estimado.
5. **NO clasificar Olin como private equity tradicional**. Es co-inversión estructurada con paquetes Class A/B + Privilegiadas + ManCo. La narrativa "fondo VC/PE genérico" es incorrecta.
6. **NO mezclar Olin con Templus o Gemswell**. Son líneas de negocio distintas, confidencialidad y deal terms independientes.
7. **NO citar 17,75% como cap% TCH1**: 17,75% son los derechos económicos Class B Ord; sumado a 0,696% Privilegiadas = 18,45% econ total en TUCA, pero el capital es solo 1,80%.
8. **NO afirmar que TUCA tributa con exención art. 21 LIS en TCH1**: la participación TCH1 en TUCA es 1,80% < 5%, NO aplica. TCH1 paga 25% IS sobre dividendos/plusvalías TUCA.
9. **NO citar Investment Date posterior a 2022-02-18 sin verificar BD** — esa es la fecha registrada `waterfall_params.investment_date`.

## 12. Lint específico Olin

```
OLIN LINT 1 — ¿Has citado fuente para cada cifra (audit / mayor / email / BD)?
OLIN LINT 2 — ¿Has distinguido cap% MdL: en TCH1 (46,03%) vs en TUCA cap (0,83%) vs econ (8,49%) vs `mdl_position_pct` BD (0,53%)?
OLIN LINT 3 — ¿Has reflejado el estado de refinanciación Asterion (2027-2028 referencia)?
OLIN LINT 4 — ¿La subrogación 2,10M€ está marcada como debt-rank, no equity?
OLIN LINT 5 — ¿Has revisado si hay NBO MasOrange firme reciente?
OLIN LINT 6 — ¿Has tributado los dividendos TUCA en TCH1 al 25% IS (sin exención)?
OLIN LINT 7 — ¿El output respeta confidencialidad (no se mezcla con Templus/Gemswell/TCIH)?
OLIN LINT 8 — ¿La calculadora waterfall consulta usa `waterfall_params` actualizado (factor mdl_pct_tch1)?
OLIN LINT 9 — ¿Has citado `exit_scenarios` con sus 4 niveles (250/350/400/500M€) en lugar de inventar IRR/MOIC?
```

## Recursos

- [Cap table detallado](resources/cap-table-detallado.md)
- [Deal terms](resources/deal-terms.md)
- [Cifras 2025 detalle](resources/cifras-2025-detalle.md)
- [Governance](resources/governance.md)
- [Fiscalidad detallada](resources/fiscalidad-detallada.md)
- [Decisiones clave](resources/decisiones-clave.md)
- [Documentos referencia](resources/documentos-referencia.md)
- [Waterfall y escenarios ISHA](resources/waterfall-y-escenarios-isha.md)
