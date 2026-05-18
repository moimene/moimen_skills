# Governance — TCIH

> Snapshot 31/12/2025 · BD `entities.tcih` + `shareholders` + Auditoría provisional 02/04/2026 (B88279880) + escritura acordeón sep-22.

## Estructura institucional

```
                  ┌─────────────────────────────────────────┐
                  │   Asamblea TCIH (6 socios)              │
                  │   • IPN 25,83%  (MdL directo)           │
                  │   • TCH2 25,83% (MdL indirecto)         │
                  │   • Monforte 25,83% (externo)           │
                  │   • LSS 7,50% (externo)                 │
                  │   • Menéndez 7,50% (externo)            │
                  │   • Gurrea-Nozaleda 7,50% (externo)     │
                  └────────────┬────────────────────────────┘
                               │ designa
                               ▼
                  ┌─────────────────────────────────────────┐
                  │   Administrador Único                   │
                  │   Luis Sánchez Salmerón (LSS)           │
                  │   DNI 00696300K                         │
                  │   • Firma operativa contratos           │
                  │   • Representación legal frente a       │
                  │     terceros (bancos, Asterion, audit)  │
                  └────────────┬────────────────────────────┘
                               │ supervisa
                               ▼
                  ┌─────────────────────────────────────────┐
                  │   Asesor fiscal + CFO TERAS             │
                  │   Asesor legal + CLO TERAS              │
                  │   Auditor B88279880 (provisional)       │
                  └─────────────────────────────────────────┘
```

## Asamblea TCIH — 6 socios

| Socio | Cap% | Pool | Voto |
|---|---|---|---|
| IPN | 25,83% | MdL | 25,83% |
| TCH2 | 25,83% | MdL | 25,83% |
| Monforte Consultoría | 25,83% | Externo (Jorge Monforte) | 25,83% |
| LSSALMERON Inversiones | 7,50% | Externo (LSS) | 7,50% |
| Moisés Menéndez Andrés | 7,50% | Externo | 7,50% |
| Enrique Gurrea-Nozaleda | 7,50% | Externo | 7,50% |

- **Mayoría simple**: 50% + 1 voto. Pool MdL (51,66%) suficiente.
- **Mayoría reforzada / supermayoría**: depende estatutos — típicamente 75% para acordeón, fusiones, escisiones, modificación estatutos.
- **Quórum mínimo asamblea**: depende convocatoria (1ª vs 2ª). Estatutos TCIH específicos.

## Administrador Único — Luis Sánchez Salmerón

- **Identidad**: Luis Sánchez Salmerón, DNI 00696300K (persona física).
- **Cargo**: Admin Único TCIH desde constitución (sin cambios).
- **Función**: firma operativa de TODOS los contratos en nombre de TCIH (cesiones crédito, financiación Asterion, contratos advisory).
- **Documentos firmados (audit 30/03/2026)**:
  - Contratos préstamos dic-2019 Pacífico Cable
  - Cesiones de crédito 26-29/12/2019 a tenedoras
  - Cuentas en participación TCH2 ↔ Jenkins (31/12/2019)
  - Liquidaciones 2022 (Acinas, Fco. López, QC, TCH2)
  - Escritura acordeón 25/11/2022
- **Riesgo gobierno**: concentración firma operativa en una persona. Mitigante: validación previa CFO + CLO TERAS antes de firma material.

## Foros y cadencia

| Foro | Cadencia | Asistencia | Owner agenda |
|---|---|---|---|
| Asamblea ordinaria TCIH | Anual (1 ejercicio fiscal) | 6 socios + Admin Único | LSS coordina |
| Asamblea extraordinaria TCIH | Ad-hoc (acordeón, modificación bylaws, autorización litigios) | 6 socios + asesor legal | LSS + CLO TERAS |
| Auditoría externa provisional | Ejecutada 02/04/2026 | Audit firm B88279880 | CFO TERAS + audit firm |
| Auditoría externa definitiva | Pendiente firma final 2025 | Misma firma | CFO + audit firm |
| Conciliación intercompany | Continua (5 saldos TCIH ↔ TCH1/TCH2/IPN) | CFO + auditores cada entidad | CFO TERAS |
| Comité riesgo legal (363.1.e LSC) | Ad-hoc 2026 (regularización dividendo cta + acordeón RM) | CLO + CFO + asesor legal | CLO TERAS |
| Comité refinanciación Asterion | Ad-hoc 2027+ (negociación 17100008 1,80M€) | CFO + CLO + Asterion | CFO + Asterion |
| Inbox bot agente documentalista | Continuo | Bot `bot@terascap.es` clasifica | TERAS automatizado |

## RACI extendido — procesos clave

| Proceso | Responsable | Accountable | Consultado | Informado |
|---|---|---|---|---|
| Aprobación cuentas anuales TCIH | LSS (Admin Único) firma | Asamblea TCIH | Audit firm + CFO | RM + Hacienda + socios |
| Override equity-rank | Audit firm B88279880 propone | CFO + asesor fiscal | Asamblea (ratifica) | Socios + bancos |
| Cesión crédito TCIH → socios TCH1 | CFO TERAS planifica | Asamblea TCIH (autoriza) | Asesor fiscal + CLO | Audit firm + socios TCH1 |
| Conciliación bilateral C-02 (PTMO TCH2 4M vs 3M) | CFO TERAS | Audit firm (sign-off) | CFO TCH2 + auditor TCH2 | Asamblea |
| Inscripción acordeón sep-22 RM | CLO TERAS | LSS (firma) | Notaría + RM | Asamblea + audit |
| Regularización dividendo cta 2,3M€ (cuenta 557) | CFO TERAS | Asamblea TCIH | Asesor fiscal | Audit firm + socios |
| Refinanciación Asterion 17100008 | CFO TERAS lead | CFO + Asterion conjunto | CLO + asesor financiero | Asamblea + socios |
| Reporting trimestral a Asterion | CFO TERAS | Admin Único firma | CFO TCH1/TUCA | Asterion |
| Servicio advisory (fees Templus / Tuca / Gemswell / Mundo Pacífico) | TCS comercial | TCS + TCIH | CFO TERAS | Socios |

## Documentos gobierno

- **Estatutos TCIH** (vigentes desde acordeón sep-22 — texto refundido pendiente registro tras inscripción RM)
- **Acta constitución** y actas asambleas histórico
- **Side letters** socio-a-socio (cesiones crédito + subrogación Asterion)
- **Acuerdo Admin Único** LSS (renovación / vigencia)
- **Estatutos texto refundido 2022** (escritura 25/11/2022)

## Confidencialidad

- **Información sensible TCIH (override equity-rank, subrogación Asterion clase B)**: tratamiento estricto sponsor-confidential. NO compartir fuera del pool socios sin aprobación CLO.
- **Cap table TCIH**: confidencial entre socios + audit firm.
- **Cuentas anuales TCIH**: depósito RM (público) tras inscripción + cuentas auditadas socios.
- **Saldos intragrupo**: confidencial entre entidades del grupo + auditoría cruzada.

## Decisiones materiales que requieren consenso

1. **Inscripción acordeón RM** (Q2 2026) — desbloquea oponibilidad terceros.
2. **Cesión crédito 4,08M€ TCIH → socios TCH1** — pendiente Escenario A/B/C asesor fiscal.
3. **Regularización dividendo cta 2,3M€ (cuenta 557)** — saneamiento patrimonial formal.
4. **Refinanciación o liquidación 17100008 Asterion** — calendario 2027+.
5. **Renovación advisory Pacífico Cable / TCS** — renovación contractual.

## Comunicación con stakeholders externos

| Stakeholder | Frecuencia | Output | Owner |
|---|---|---|---|
| Asterion | Trimestral | Reporting deuda 17100008 + posiciones subrogación | CFO TERAS |
| RM Madrid | Anual + ad-hoc inscripciones | Depósito cuentas + acuerdos sociales | CLO + LSS |
| Audit firm | Anual + extraordinarias overrides | Cuentas auditadas + override sign-off | CFO |
| Hacienda | Anual IS + IVA | Modelo 200 + autoliquidaciones | Asesor fiscal |
| Bancos (uso tarjetas crédito) | Continuo (12 VISA CAIXABANK + AMEX) | Movimientos operativos | LSS |
| Bot agente documentalista | Continuo | Ingest documentos clasificados | TERAS auto |

## Reporting cadence interna

| Output | Cadencia | Destinatario | Owner |
|---|---|---|---|
| Cuenta de resultados mensual | Mensual | CFO TERAS | Contabilidad |
| Balance trimestral | Trimestral | CFO + auditoría | Contabilidad |
| Estado conciliación intercompany | Trimestral | CFO TERAS + cada CFO entidad | CFO TERAS |
| Cuentas anuales auditadas | Anual | Socios + RM + Hacienda | Audit firm |
| Override equity-rank actualizado | Anual (con auditoría) | Audit firm + CFO + socios | Audit firm |
| Risk register TCIH (legal + contable) | Trimestral | CLO + CFO | CLO |

## Pendientes gobierno (a 18-may-2026)

1. Convocar asamblea extraordinaria Q2 2026 para ratificar override audit_2026_provisional y autorizar inscripción acordeón RM.
2. Renovar mandato Admin Único LSS (vigencia formal).
3. Documentar side letters socio-a-socio en repositorio CLO (centralizar).
4. Ajustar power-of-attorney para CFO TERAS con autoridad firma operativa secundaria (mitigar concentración).
5. Documentar identidad Dime Shared ↔ Quarter Capital (hallazgo H-02 audit).
