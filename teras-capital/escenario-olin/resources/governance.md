# Governance — Olin (TUCA chain)

> Snapshot 31/12/2025 · BD `entities` + `shareholders` + auditoría TUCA 2024 + ISHA reformulado.

## Org chart resumido

```
                    ┌─────────────────────────────────┐
                    │   Asterion (Sponsor)            │
                    └────────────┬────────────────────┘
                                 │ Class A + Privilegiadas via chain
                                 ▼
                    ┌─────────────────────────────────┐
                    │   Tuca Midco Limited (98%)      │
                    └────────────┬────────────────────┘
                                 │
                                 ▼
       ┌─────────────────────────────────────────────┐
       │   Tuca Bidco SL (S.à r.l. Lux)              │
       │   FY24: Activo 405,8M€ · PN 248,6M€         │
       │   Audit firm: pendiente confirmar           │
       │                                             │
       │   ▶ Consejo TUCA                            │
       │   ▶ Steerco trimestral                      │
       └────────┬────────────────────────────────────┘
                │ 1,80% cap / 18,45% econ
                ▼
       ┌─────────────────────────────────────────────┐
       │   TCH1 NIF B88547583                        │
       │   PN 379€ (entidad de paso) · Pasivo 4,1M€  │
       │                                             │
       │   ▶ Asamblea TCH1                           │
       │   ▶ Comités ad-hoc                          │
       └─────────────────────────────────────────────┘
```

## Foros y cadencia

### Steerco Tuca Bidco

- **Cadencia**: trimestral.
- **Asistencia TERAS**: CIO + CFO TERAS (representante TCH1).
- **Agenda típica**: KPIs MasOrange, status integración Orange+MásMóvil, capex review, refinanciación tracking, NBO updates.
- **Owner agenda**: TERAS coordina vía TCH1 + Tuca Bidco management.
- **Reporting input**: dashboard MasOrange + KPIs operativos + financial pack TUCA.

### Consejo MasOrange

- **Cadencia**: trimestral.
- **Asistencia TERAS**: representante designado por TUCA (puede rotar entre socios).
- **Agenda**: gestión operativa MasOrange.
- **Owner**: MasOrange management + Asterion (Class A).

### Asamblea TCH1 (socios)

- **Cadencia**: mínimo anual + ad-hoc.
- **Asistentes**: los 11 socios listados en `shareholders.tch1`:
  - **Pool MdL (46,03%)**: IPN, TCH2.
  - **Pool MMS / LSS group (37,53%)**: Monforte 17,99%, LSS 5,48%, Gurrea 8,06%, Menéndez 8,06%.
  - **Pool Mgmt Class B (14,39%)**: Ávila, S.Echevarría, Triguero, Huarte, Lafarga.
- **Decisiones**: aprobación cuentas, distribución dividendos TCH1, ajustes cap table.
- **Voto**: Class A (96,61%) vs Class B (14,39%) — ratificación supermayorías.

### Comité refinanciación Asterion

- **Cadencia**: ad-hoc desde 2027.
- **Asistencia**: CFO + CLO TERAS + Asterion + asesores legales.
- **Objetivo**: term sheet + ejecución refi 2028.

### Auditoría externa

- **TUCA Bidco**: anual (FY 2024 disponible).
- **TCH1**: anual con Anexo IV (cap table + derechos económicos detallados).
- **Owner**: CFO TERAS coordina con audit firm.
- **Output**: cuentas auditadas + Anexo IV + ajustes recomendados.

## RACI extendido — procesos clave

| Proceso | Responsable | Accountable | Consultado | Informado |
|---|---|---|---|---|
| Steerco Q | CFO TERAS prepara pack | CIO TERAS | TUCA mgmt + Tuca Midco | Asterion |
| NBO MasOrange | CIO TERAS lidera análisis | CIO TERAS | CFO + CLO + audit firm | Socios TCH1 + Asterion |
| Refinanciación 2027-2028 | CFO TERAS lead | CFO + Asterion conjunto | CLO + asesor financiero | Socios TCH1 |
| Dividendo TUCA → TCH1 → socios | CFO TERAS proceso pago | TCH1 board | Audit firm | Socios TCH1 + IPN/TCH2 |
| Vesting Class B (exit) | CLO TERAS aplica ISHA | TCH1 board | Mgmt afectados | Pool MdL |
| Cierre cuentas TCH1 anuales | CFO TERAS prepara | TCH1 board | Audit firm | Asamblea TCH1 |

## Decisiones que requieren supermayoría ISHA

(Pendiente listar exactamente con cláusulas — ver SHA TUCA + ISHA reformulado en `bl_documents`):

- M&A relevantes en TUCA / MasOrange.
- Cambios bylaws / class structure.
- Refinanciación deuda Asterion (cualquier cambio material).
- Distribución dividendos extraordinarios.
- Entrada de nuevos managers (sujeto a cap dilución 10% ISHA Cl. 6.4(C)).

## Reporting cadence

| Output | Cadencia | Destinatario | Owner |
|---|---|---|---|
| KPI pack TUCA | Mensual | Steerco + Asterion | TUCA mgmt + TERAS |
| Financial pack TUCA | Trimestral | Steerco | CFO TERAS |
| Status update TCH1 a socios | Trimestral | Socios TCH1 | TCH1 board |
| Auditoría TUCA | Anual | Socios + bancos | Audit firm |
| Anexo IV TCH1 | Anual | Socios TCH1 + auditor | CFO TERAS |
| NBO updates | Ad-hoc | Socios TCH1 + Asterion | CIO TERAS |

## Convenciones de comunicación

- **Información sensible TUCA/MasOrange**: clasificada como Sponsor-confidential. NO compartir fuera del pool socios TCH1 sin aprobación CLO.
- **Cap table TCH1**: confidencial entre socios. Audit Anexo IV es vinculante.
- **Distribución TCH1 → IPN/TCH2**: pasa por Asamblea TCH1 + Audit firm sign-off.
