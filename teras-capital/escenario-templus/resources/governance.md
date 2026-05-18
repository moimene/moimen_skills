# Governance — Templus (Vesta chain + AE Group HoldCo II)

> Snapshot 31/12/2025 · BD `entities` + `shareholders` + audit EY IN25-6924 (TCH4) + ISHA 11/10/2023 + Enmienda 11/12/2025 + org chart Templus v8 14/04/2026.

## Org chart resumido

```
                    ┌─────────────────────────────────┐
                    │   ICG (Sponsor financiero)      │
                    └────────────┬────────────────────┘
                                 │ Class A + Pref via chain ICG
                                 ▼
                    ┌─────────────────────────────────┐
                    │   Vesta Invest S.à r.l. (LUX)   │
                    │   ICG-controlled                │
                    │   Commit 300M€ (Financing Agreement 11/12/2025)
                    └────────┬────────────────────────┘
                             │ 96% en Templus CD
                             ▼
       ┌─────────────────────────────────────────────┐
       │   Templus Centros de Datos S.L.U. (CD)      │
       │   NIF B-56381379                            │
       │   Activo 179,5M€ · PN 177,2M€               │
       │   exclude_from_group_totals=true            │
       │   Audit firm consolidado pendiente confirmar│
       │                                             │
       │   ▶ Consejo Templus CD                      │
       │   ▶ Steerco Templus trimestral              │
       └────┬────────────────────────────────────────┘
            │ 100% en 7 filiales operativas España
            │
            ▼
       [7 filiales España: Madrid, Alcalá, Málaga, Spain, Barcelona, Properties, Ceuta]


PROJECT COLORADO (rama paralela TCH4 → AE Group HoldCo II):

       ┌─────────────────────────────────────────────┐
       │   AE Group HoldCo II S.à r.l. (LUX)         │
       │   Parent: TCH4                              │
       │                                             │
       │   ▶ Consejo AE Group HoldCo II              │
       │   ▶ Reporting trimestral a Steerco Templus  │
       └────┬────────────────────────────────────────┘
            │ 100% en 4 Roosevelt filiales
            │
            ▼
       [4 Roosevelt: Italy, Netherlands, Denmark, France]


PATH TCH4 (vehículo MdL en cadena):

       ┌─────────────────────────────────────────────┐
       │   TCH4 (Teras Capital Holding 4, S.L.)      │
       │   NIF B56563398                             │
       │   PN -5K€ (técnicamente negativo)           │
       │   Pasivo 3,74M€ (incluye Vesta 976K€ + intragrupo)
       │   Audit firm: EY (IN25-6924 abril 2026)     │
       │                                             │
       │   ▶ Asamblea TCH4 (10 socios)               │
       │   ▶ Comités ad-hoc                          │
       └────┬─────────────┬───────────────────────────┘
            │             │
            │ 2,00% Vesta │ 100% AE HoldCo II (Colorado)
            ▼             ▼
         (Vesta)      (AE HoldCo II)


PATH TCIH directo a Templus CD (Path 2 MdL):

       ┌─────────────────────────────────────────────┐
       │   TCIH (Teras Capital Investment Holding)   │
       │   NIF B88279880                             │
       │   Cap% MdL en TCIH: 51,665%                 │
       │                                             │
       │   ▶ Voz directa en consejo Templus CD       │
       └────┬────────────────────────────────────────┘
            │ 2,00% Class B directo en Templus CD
            ▼
       (Templus CD)
```

## Foros y cadencia

### Steerco Templus

- **Cadencia**: trimestral.
- **Asistencia TERAS**: CIO + CFO TERAS (representante TCH4 + TCIH).
- **Asistencia ICG/Vesta**: representante senior ICG + dirección Vesta Invest.
- **Asistencia operativa**: CEO + CFO Templus CD + responsables operativos por filial.
- **Agenda típica**:
  - KPIs operativos por filial España (ARPU, utilización DC, capex run-rate)
  - Status integración Templus Spain (Espacio Edge, adq. 25/06/2025) + Templus Ceuta build-out
  - Project Colorado roll-out (4 Roosevelt): comercialización + capex actuales
  - Refinanciación commit Vesta + cupón Class D devengado
  - M&A pipeline adicional
  - Budget vs actuals trimestral
- **Owner agenda**: TERAS coordina vía TCH4 + Templus CD management.
- **Reporting input**: KPI pack mensual + financial pack trimestral consolidado.

### Consejo Templus CD

- **Cadencia**: trimestral.
- **Asistencia TERAS**: representante por TCH4 + TCIH directo (Path 2).
- **Asistencia ICG**: representante Vesta Invest (96% Class A).
- **Agenda**: gestión operativa Templus CD, decisiones M&A, distribución dividendos.
- **Owner**: Templus CD management + ICG/Vesta.

### Consejo AE Group HoldCo II (Project Colorado)

- **Cadencia**: trimestral.
- **Asistencia TERAS**: representante TCH4.
- **Asistencia ICG**: representante Vesta (si aplica directamente o vía AE HoldCo II).
- **Agenda**: estado Project Colorado por país (IT/NL/DK/FR), Roosevelt operations.
- **Reporting**: a Steerco Templus consolidado.

### Asamblea TCH4 (socios)

- **Cadencia**: mínimo anual + ad-hoc.
- **Asistentes**: los 10 socios listados en `shareholders.tch4`:
  - **Pool MdL (32,60%)**: IPN 17%, TCH2 15,60%.
  - **Pool MCT Monforte (26,00%)**: Jorge Monforte (mayor individual).
  - **Pool Indep (16,00%)**: Gurrea 8%, Menéndez 8%.
  - **Pool Mgmt Class A (20,00%)**: S.Echevarría 7%, Ávila 6,8%, Huarte 6,2%.
  - **Pool LSS (5,40%)**: LSSI.
  - **Pool residual (0,01%)**: TCIH.
- **Decisiones**: aprobación cuentas, distribución dividendos TCH4 (cuando los haya), ajustes cap table, aportaciones extraordinarias.
- **Voto**: cap%-weighted simple. Supermayorías para reformas estatutarias + decisiones materiales.
- **Designación portavoz**: Monforte (26%) actúa frecuentemente como portavoz dada su mayor participación individual.

### Comité M&A Templus (ad-hoc adquisiciones)

- **Cadencia**: ad-hoc por operación.
- **Asistencia**: CIO + CFO + CLO TERAS + Vesta/ICG + Templus CD management.
- **Objetivo**: evaluación + aprobación adquisiciones (referencia Espacio Edge 2025, Waterways Global 2025).

### Comité refinanciación Vesta (ad-hoc 2027-2028)

- **Cadencia**: ad-hoc desde 2027 (vinculado a despliegue commit 300M€).
- **Asistencia**: CFO + CLO TERAS + ICG + Vesta + asesores legales.
- **Objetivo**: term sheet refi + ejecución.

### Auditoría externa

- **TCH4**: anual. **EY (IN25-6924 abril 2026)** vigente.
- **Templus CD**: anual. Audit firm consolidado pendiente confirmar (audit_2026_provisional disponible).
- **7 filiales España**: cada una audit local (algunas legacy con audit firm propio, en proceso de unificación a audit firm consolidado).
- **4 Roosevelt Project Colorado**: cada una audit local (IT/NL/DK/FR), reporting consolidado vía AE Group HoldCo II.
- **Owner**: CFO TERAS coordina con EY (TCH4) + audit firm consolidado.
- **Output**: cuentas auditadas + audit findings + ajustes recomendados.

## RACI extendido — procesos clave

| Proceso | Responsable | Accountable | Consultado | Informado |
|---|---|---|---|---|
| Steerco Templus Q | CFO TERAS prepara pack | CIO TERAS | Templus CD mgmt + Vesta/ICG | TCH4 + TCIH socios |
| M&A nueva adquisición | CIO TERAS lidera análisis | CIO TERAS | CFO + CLO + Vesta + Templus CD mgmt | TCH4 socios + ICG |
| Refinanciación Vesta 2027-2028 | CFO TERAS lead | CFO + ICG conjunto | CLO + asesor financiero | TCH4 + TCIH socios |
| Dividendo Vesta → TCH4 → socios | CFO TERAS proceso pago | TCH4 board | EY audit firm | TCH4 socios + IPN/TCH2 |
| Dividendo Templus CD → TCIH (Path 2) | CFO TERAS proceso | Templus CD board | Audit firm | TCIH socios |
| Cierre cuentas TCH4 anuales | CFO TERAS prepara | TCH4 board | EY | Asamblea TCH4 |
| Cierre cuentas Templus CD consolidado | CFO Templus CD prepara | Templus CD board + Vesta | Audit firm + EY | TCH4 + TCIH |
| Project Colorado capex review | CFO Templus + CIO TERAS | AE Group HoldCo II board | Audit firm Roosevelt | Vesta + ICG |
| Plan 100 días Templus Spain (Espacio Edge) | CIO TERAS + Templus CD mgmt | Templus CD board | Legacy Espacio Edge team | Steerco |
| Build-out Templus Ceuta | Templus CD mgmt + Waterways legacy | Templus CD board | CIO TERAS | Vesta + ICG |

## Decisiones que requieren supermayoría ISHA

(Pendiente listar exactamente con cláusulas — ver ISHA 11/10/2023 + Enmienda 11/12/2025 en `bl_documents`):

- M&A relevantes en Templus CD o filiales.
- Cambios bylaws / class structure Vesta o Templus CD.
- Refinanciación Vesta (cualquier cambio material commit).
- Distribución dividendos extraordinarios.
- Entrada de nuevos managers Class C (sweet equity Templus CD).
- Exit Templus o ventas materiales activos.
- Cambios en Financing Agreement Vesta → TCH4 (tipo 8%, principal).

## Reporting cadence

| Output | Cadencia | Destinatario | Owner |
|---|---|---|---|
| KPI pack mensual Templus CD | Mensual | Steerco + ICG/Vesta | Templus CD mgmt |
| P&L by Site (7 filiales España) | Trimestral | Steerco | CFO Templus CD |
| Colorado Mgmt Accounts (4 Roosevelt) | Trimestral | Steerco | AE Group HoldCo II + CFO TERAS |
| Financial pack consolidado Templus | Trimestral | Steerco + TCH4 + TCIH socios | CFO TERAS |
| Status update TCH4 a socios | Trimestral | 10 socios TCH4 | TCH4 board |
| Auditoría TCH4 (EY) | Anual | Socios TCH4 + bancos | EY |
| Auditoría Templus CD consolidado | Anual | Vesta + TCH4 + TCIH | Audit firm |
| Org chart Templus actualizado | Trimestral | Vesta + TCH4 + TCIH | CFO TERAS (v8 14/04/2026 vigente) |
| Refinanciación Vesta updates | Ad-hoc 2027+ | TCH4 + TCIH socios + ICG | CFO TERAS |

## Convenciones de comunicación

- **Información sensible Templus CD / Project Colorado**: clasificada como Sponsor-confidential. NO compartir fuera del pool socios TCH4 + TCIH sin aprobación CLO + Vesta.
- **Cap table TCH4**: confidencial entre los 10 socios. Audit EY es vinculante.
- **Distribución TCH4 → IPN/TCH2 (cuando aplique)**: pasa por Asamblea TCH4 + EY sign-off.
- **Distribución Templus CD → TCIH (Path 2)**: pasa por Templus CD board + audit firm sign-off.
- **Project Colorado reporting**: separado en pack pero consolidado en cifras Templus para inversores (TCH4 socios + Vesta).

## Org chart Templus v8 (14/04/2026)

Versión vigente del org chart Templus es la v8 del 14/04/2026 (`bl_documents` doc_type='org_chart' business_line_id='templus'). Incluye:
- Cadena completa MdL → IPN/TCH2 → TCH4 → Vesta → Templus CD
- Path 2 TCIH → Templus CD directo
- 7 filiales operativas España (NIFs + cap%)
- 4 Roosevelt Project Colorado vía AE Group HoldCo II
- Capacidad Class A/B/C/D cada eslabón

## Decisiones de governance recientes

- **11/12/2025**: Enmienda ISHA Vesta (cupón Class D 12%) + Financing Agreement Vesta → TCH4 (8%) firmados.
- **25/06/2025**: Adquisición Templus Spain (Espacio Edge) cerrada — aprobada por Comité M&A.
- **11/06/2025**: Constitución Templus Ceuta (Waterways Global) — aprobada por Comité M&A.
- **Abril 2026**: Auditoría EY IN25-6924 TCH4 emitida — recibida en TCH4 board.
- **10/05/2026**: Pack Miguel consolidado (6 archivos) entregado por dirección Templus a TCH4 + TCIH.
- **Mayo 2026**: Fix bug parser #14 aplicado a TCH4 (cuenta 17100000 reclasificada).
