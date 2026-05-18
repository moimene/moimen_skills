# Fiscalidad detallada — Gemswell (TCH3 + Valdorba subgrupo + SW Infrasports + cadena Quarter/Grand View)

> Snapshot 31/12/2025 · LIS + PGC NRV 19ª · BD `savenikqhmcuwmcnabca` + audit provisional TCH3 02/04/2026.

## Art. 21 LIS — exención dividendos y plusvalías en grupo

Requisito clave: participación ≥ 5% (o coste adquisición ≥ 20M€) y permanencia ≥ 1 año.

### Aplicación en cadena Gemswell

| Flujo | Cap% | ¿Aplica art. 21 LIS? | Notas |
|---|---|---|---|
| **MdL pool (IPN/TCH2) sobre TCH3** | 46,86% agregado (IPN 36,45% + TCH2 10,41%) | **SÍ — cada socio individual >5%** | IPN 36,45% > 5% y TCH2 10,41% > 5% — exención plena para flujos TCH3 → IPN y TCH3 → TCH2 |
| **TCH3 sobre Valdorba Parques** | 88% | **SÍ** | Flujos Valdorba → TCH3 exentos |
| **Valdorba Parques sobre VM** | 100% | **SÍ** | Flujos VM → Valdorba Parques exentos |
| **Valdorba Parques sobre VPS** | 100% | **SÍ** | Aplica cuando VPS genere distribuciones (fase desarrollo aún) |
| **Valdorba Parques sobre VPSH** | 100% | **SÍ** (cuando aplique) | VPSH en latencia, sin distribuciones |
| **TCH3 sobre SW Infrasports** | 50% | **SÍ** | Flujos SWI → TCH3 exentos |
| **VM sobre MPS** | 10,31% | **SÍ** (>5%) | Aplica si MPS distribuye |
| **IPN sobre Quarter Capital** | 32,29% | **SÍ** (>5%) | Flujos QC → IPN exentos |
| **Quarter Capital sobre Grand View** | 100% | **SÍ** | Flujos GV → QC exentos |

### Tipo IS aplicable a TCH3

- **25% IS general** sobre base imponible NO exenta (renta operativa propia TCH3, intereses crédito intragrupo, etc.).
- Para dividendos y plusvalías cubiertos por art. 21 LIS: exención plena (no entra en base imponible).

### Tipo IS aplicable a subgrupo

- VM (operativo, ingresos 2M€): **25% IS** sobre resultado operativo. Sin exención aplicable (ingresos surf park son renta operativa, no rendimientos de cartera).
- VPS, VPSH (en desarrollo / latencia): 25% IS pero sin base imponible significativa por inactividad / fase pre-operativa.
- Valdorba Parques (cabecera holding): 25% sobre renta no exenta; exención plena sobre flujos VM/VPS/VPSH → Valdorba Parques.

## NRV 19ª PGC — Inversiones en empresas del grupo, multigrupo y asociadas

Norma de Registro y Valoración 19ª del PGC 2007 (RD 1514/2007). Coste menos deterioros.

### Aplicación a TCH3

- **TCH3 → Valdorba Parques (88%)**: inversión en empresa del grupo (cap% mayoritario). NRV 19ª 1. Valoración a coste menos deterioros.
- **TCH3 → SW Infrasports (50%)**: inversión en empresa multigrupo (50% sin control unilateral). NRV 19ª 1. Coste menos deterioros.
- No consolida estados financieros formales a nivel TCH3 (TCH3 no es matriz consolidante PGC salvo confirmación auditor en función de obligación legal).

### Aplicación a Valdorba Parques

- Valdorba Parques → VM, VPS, VPSH (100%): empresas del grupo, NRV 19ª 1. Coste menos deterioros.

### Aplicación a IPN

- IPN → TCH3 (36,45%): empresa del grupo (cap% >20% y control significativo agregado pool MdL). NRV 19ª.
- IPN → Quarter Capital (32,29%): empresa del grupo. NRV 19ª.
- IPN → TCH2 (100%): empresa del grupo. NRV 19ª.

### Aplicación a TCH2

- TCH2 → TCH3 (10,41%): inversión < 20% pero con influencia significativa por pertenencia al pool MdL. Discutible si NRV 19ª o NRV 9ª (instrumentos financieros). Audit firm define.

## Subsanación capital TCH3 — efecto fiscal

### 1ª ampliación (compensación de créditos intragrupo)

- 1.343.000€ capital + 557.000€ prima.
- **Operación neutra en IS** en sede de TCH3: la capitalización de créditos no genera renta gravable, los créditos pasan a capital social.
- En sede del socio acreedor (IPN, MMS, otros): conversión del activo "crédito" a "participación en capital". Si hay deterioro previo del crédito, podría reclasificarse el coste de adquisición de las nuevas participaciones.
- **Crédito MPS (Madrid Playa Surf) capitalizado** en la prima (557K): traslado de riesgo fiscal de potencial deterioro del crédito a coste de adquisición de participaciones TCH3.

### 2ª ampliación (dineraria)

- 850.000€ capital + 555.000€ prima.
- Aportación efectiva en metálico — neutra fiscalmente para los socios aportantes (capital aportado, no renta).

## Reclasificación bug #14 — efecto fiscal

- Cuenta **17100011 PTMO TELCOGESTORES SERVICIOS DE GESTION (250.000€)** reclasificada de `pnc_bancario` a `pnc_otra`.
- **Sin efecto fiscal directo** (reclasificación contable de naturaleza acreedor, no de renta).
- **Efecto en informes para el banco**: la reclasificación reduce la deuda bancaria reportada a TCH3 (NO es deuda bancaria sino con tercero no bancario — Telcogestores).

## Saldo intragrupo Grand View → IPN — efecto fiscal

- Cuenta **17100002 PTMO GRAND VIEW LA QUINTA**: 1.519.092,12€ con IPN acreedor frente a Grand View.
- **Loan_lp (préstamo largo plazo)** intragrupo. Genera intereses imputables si hay tipo pactado:
  - En sede de IPN: ingreso financiero por intereses (25% IS).
  - En sede de Grand View: gasto financiero deducible.
- Si el tipo es de mercado (operación vinculada art. 18 LIS), neutro a nivel grupo.
- Si por debajo de mercado: ajuste fiscal por operación vinculada (riesgo regularización).

## Planificación exit MdL

### Exit Wave Park (vía VSO II / SW Infrasports)

| Etapa | Cap% | Tributación |
|---|---|---|
| Venta participación VSO II | (compartimento — dependiente de % en compartimento) | 25% IS en SW Infrasports si plusvalía neta |
| Distribución SW Infrasports → TCH3 | 50% | Exención art. 21 LIS si plusvalía vehiculada como dividendo / liquidación |
| Distribución TCH3 → IPN (36,45%) y TCH2 (10,41%) | Cada >5% | Exención art. 21 LIS plena |
| Distribución IPN → MdL persona física | Persona física | Tributación IRPF ahorro (19-28%) sobre rendimiento de capital o ganancia patrimonial según vía |

### Exit La Quinta (vía Grand View)

| Etapa | Cap% | Tributación |
|---|---|---|
| Venta inmueble por Grand View | (operativa) | 25% IS sobre plusvalía neta |
| Distribución Grand View → Quarter Capital | 100% | Exención art. 21 LIS plena |
| Distribución Quarter Capital → IPN | 32,29% | Exención art. 21 LIS plena |
| Distribución IPN → MdL persona física | Persona física | IRPF ahorro |

### Exit consolidado Gemswell (subgrupo Valdorba + SWI)

| Etapa | Cap% | Tributación |
|---|---|---|
| Venta VM / VPS / VPSH (asset deal o share deal) | (varía) | 25% IS sobre plusvalía |
| Distribución a Valdorba Parques | 100% | Exención art. 21 LIS plena |
| Distribución Valdorba Parques → TCH3 | 88% | Exención art. 21 LIS plena |
| Distribución TCH3 → pool MdL (IPN/TCH2) | Cada >5% | Exención art. 21 LIS plena |
| Distribución IPN → MdL | Persona física | IRPF ahorro (19-28%) |

### Cláusulas SPA / mecánica fiscal exit

A negociar en SPA:

- **Retención en origen**: aplica solo si exit con compradores no residentes.
- **Earn-outs**: tributación diferida hasta cobro efectivo (criterio devengo modificado).
- **Reinversión TERAS en otra línea** (Olin, Templus): no aplica diferimiento art. 33 LIS (no es reinversión empresarial en inmovilizado material). Sí podría diferir vía mantenimiento en holding aguas arriba.
- **Escalonamiento**: si exit fraccionado, plusvalía imputada cada período.

## Riesgos fiscales identificados

| # | Riesgo | Impacto | Mitigante |
|---|---|---|---|
| 1 | TJUE / TS jurisprudencia sobre cadenas holding intragrupo (limitación art. 21 LIS) | Pérdida exención parcial / total | Asesoría continua, opinion letters, monitoreo doctrina |
| 2 | Operaciones vinculadas art. 18 LIS — tipo intereses intragrupo no de mercado | Regularización por inspección | Documentación precios transferencia, justificación tipo |
| 3 | Inspección IS sobre subsanación capital (interpretación capitalización deuda) | Riesgo recalificación | Opinion letter, dossier sustentado, audit firm soporte |
| 4 | Aplicación NRV 19ª vs NRV 9ª (TCH2 10,41% en TCH3) | Discutible | Audit firm define + opinion letter |
| 5 | Fiscalidad indirecta (IVA, ITP-AJD) operación subsanación | Riesgo si no se aplica exención | Asesoría tributaria + Notaría |
| 6 | Cierre formal Quarter Capital + Grand View pendiente — mayores 2018-2025 sin procesar | Riesgo regularización si cifras override no cuadran con mayores | García Ruiz procesa + audit firm valida |
| 7 | Saldo intragrupo Grand View → IPN 1,52M€ — interés operación vinculada | Ajuste si tipo no de mercado | Documentar tipo + comparables |

## Análisis sensibilidad fiscal — exit escenarios

| Escenario exit consolidado | Plusvalía bruta | IS subgrupo (25%) | Plusvalía neta a TCH3 | Plusvalía neta a IPN/TCH2 (exenta) | MdL pers. física (IRPF ~25% sobre rendim. neto) |
|---|---|---|---|---|---|
| Conservador (50M€ NAV total) | 50M€ | 12,5M€ | 37,5M€ → 88% = 33M€ | 33M€ × 46,86% = 15,5M€ | ~11,6M€ neto MdL personal |
| Base case (100M€) | 100M€ | 25M€ | 75M€ → 88% = 66M€ | 66M€ × 46,86% = 30,9M€ | ~23,2M€ neto MdL personal |
| Upside (150M€) | 150M€ | 37,5M€ | 112,5M€ → 88% = 99M€ | 99M€ × 46,86% = 46,4M€ | ~34,8M€ neto MdL personal |

> Estimación simplificada. Aplica hurdle ISHA 8% + promote 20% sobre exceso antes de cap%. Mecánica completa en `waterfall-y-escenarios-isha.md`.

## Documentación fiscal pendiente

- Opinion letter art. 21 LIS para flujos TCH3 → IPN/TCH2 con cap% individuales (a confirmar interpretación pool).
- Documentación precios transferencia para créditos intragrupo subgrupo Valdorba (tipos de interés).
- Análisis ITP-AJD subsanación capital dic-2025.
- Cierre fiscal definitivo TCH3 2025 (post audit definitivo Q2 2026).
- Análisis fiscal exit VSO II / Wave Park (estructura vehiculación SW Infrasports).
