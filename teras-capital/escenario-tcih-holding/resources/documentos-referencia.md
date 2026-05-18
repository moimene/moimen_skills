# Documentos referencia — TCIH

> Listado curado de documentos relevantes para TCIH. Cruce con tabla BD `bl_documents` (`business_line_id='teras-capital'`) + documentos en Drive + escrituras notariales + mayor PGC.

## Categorías documentación

### A. Documentos societarios y contractuales

| # | Documento | Tipo | Fecha | Owner / Localización |
|---|---|---|---|---|
| A1 | Escritura constitución TCIH | Escritura notarial | Constitución original | Notaría + RM Madrid |
| A2 | Escritura acordeón 25/11/2022 | Escritura notarial | 25-nov-2022 | Notaría + (PENDIENTE inscripción RM) |
| A3 | Estatutos texto refundido post-acordeón | Estatutos sociales | 2022 | CLO TERAS + (PENDIENTE inscripción RM) |
| A4 | Contratos préstamo dic-2019 (Jenkins UNO 3M, DOS 1M, Dime Shared 800K, Acinas 210K, Fco. López 100K, Monforte 50K) | Contratos préstamo | 23-dic-2019 | Drive `One_drive_Teras/TCIH/Préstamos_2019/` |
| A5 | Cesiones de crédito 26-29/12/2019 a tenedoras (TCH2, TCH3) | Cesión crédito | dic-2019 | Drive + audit support |
| A6 | Cuentas en participación TCH2 ↔ Jenkins (Signaturit 31/12/2019 13:08 UTC) | Cuentas en participación | 31-dic-2019 | Signaturit + Drive |
| A7 | Liquidación TCH DOS (Jenkins) 30/09/2022 — 4.087.160,81€ | Acta liquidación | 30-sep-2022 | Drive `One_drive_Teras/TCIH/Liquidaciones/` |
| A8 | Liquidaciones Acinas + Fco. López + QC/Barrena 16/02/2022 | Actas liquidación | 16-feb-2022 | Drive |
| A9 | Side letters socio-a-socio (cesión crédito + subrogación Asterion) | Side letters | Varios | CLO TERAS — repositorio centralización pendiente |
| A10 | Acuerdo Admin Único LSS — vigencia | Acuerdo gobierno | Constitución + renovaciones | CLO |

### B. Documentación financiera y operativa

| # | Documento | Tipo | Fecha | Localización |
|---|---|---|---|---|
| B1 | Auditoría provisional TCIH 02/04/2026 (B88279880) | Audit | 02-abr-2026 | Drive + BD `bl_documents` |
| B2 | Diario operaciones TCIH (Pacífico Cable + Reorganización) auditado 30/03/2026 | Audit | 30-mar-2026 | https://savenikqhmcuwmcnabca.supabase.co/storage/v1/object/public/documents/teras-capital/Auditoria_Pacifico_Cable_TCIH.docx |
| B3 | Conciliación Mayor 2025 vs Auditoría (Excel) | Excel | 30-mar-2026 | https://savenikqhmcuwmcnabca.supabase.co/storage/v1/object/public/documents/teras-capital/Conciliacion_Mayor_vs_Auditoria_TCIH.xlsx |
| B4 | Balance TCIH 31/12/2025 (cuentas anuales pendiente firma definitiva) | Balance + P&L | 2025 | BD `entity_balances.tcih` + Drive |
| B5 | Mayor PGC TCIH 2025 (7.428 asientos, 356 cuentas) | Mayor PGC | 2025 | Carpeta sandbox `Cierres historicos/` + parser output |
| B6 | Snapshots históricos `entity_balances_history` 2018-2026 | Snapshots BD | 2018-2026 | BD |
| B7 | Modelo 200 IS TCIH 2024 (último presentado) | Modelo IS | 2024 | Asesor fiscal + Drive |
| B8 | Conciliación bilateral C/C TCIH ↔ TCH1 (pendiente) | Conciliación | Pendiente Q2 2026 | CFO TERAS |
| B9 | Reporting trimestral Asterion (deuda 17100008) | Reporting | Continuo | CFO + Drive `One_drive_Teras/TCIH/Asterion/` |

### C. Documentación fiscal

| # | Documento | Tipo | Owner |
|---|---|---|---|
| C1 | Opinion letter art. 21 LIS TCIH (pendiente identificar asesor) | Tax opinion | Asesor fiscal TERAS |
| C2 | Memoria contable TCIH NRV 19ª (inversiones TCS + Templus CD + TCH4) | Memoria contable | Auditor |
| C3 | Estudio escenarios cesión crédito TCIH → socios TCH1 (A/B/C) | Análisis fiscal | Asesor fiscal |
| C4 | Convenio España-Chile doble imposición (referencia histórica Pacífico Cable) | Tratado fiscal | Hacienda |
| C5 | Cuantificación BINs acumuladas TCIH | Análisis BINs | Asesor + CFO |
| C6 | Documentación operación vinculada art. 18 LIS (cesión crédito futura) | Memoria operación vinculada | Asesor + CFO |

### D. Documentación regulatoria / pública

| # | Documento | Tipo |
|---|---|---|
| D1 | RM Madrid — depósito cuentas anuales TCIH 2018-2024 (último depositado) | Depósito RM |
| D2 | RM Madrid — inscripción acordeón sep-22 (PENDIENTE >3 años) | Inscripción RM |
| D3 | BORME (Boletín Oficial Registro Mercantil) — publicaciones TCIH | Publicación oficial |
| D4 | AEAT (Hacienda) — modelos IS / IVA / 200 históricos | Tributario |

### E. Documentación interna TERAS

| # | Documento | Tipo |
|---|---|---|
| E1 | Risk register TCIH (legal + contable) | Risk register |
| E2 | Comms plan TCIH (interno) | Comms |
| E3 | Roadmap saneamiento patrimonial TCIH 2026-2028 | Roadmap |
| E4 | Inventario side letters socio-a-socio (centralización pendiente) | Inventario CLO |
| E5 | Calendario fiscal + legal TCIH | Calendario |

### F. Bot agente documentalista — ingest activo

| # | Email | Asunto / clasificación | Ingest |
|---|---|---|---|
| F1 | `bot@terascap.es` — inbox tracking | Documentos clasificados con `business_line_id='teras-capital'` | Continuo |
| F2 | `agent_inbox_log` BD | Log de cada documento ingerido | BD `agent_inbox_log` |

## SQL — extracción documentos vivos

```sql
SELECT id, name, doc_type, source, classification_source, uploaded_at, storage_path, summary
FROM bl_documents
WHERE business_line_id = 'teras-capital'
ORDER BY doc_type, uploaded_at DESC;

-- Inbox log para TCIH
SELECT *
FROM agent_inbox_log
WHERE business_line_id = 'teras-capital' OR business_line_id IS NULL
ORDER BY received_at DESC
LIMIT 50;
```

`classification_source` muestra `agent_auto` / `agent_reviewed` / `agent_corrected` / `human`.

## Estructura Drive TCIH

```
One_drive_Teras/TCIH/
├── Constitucion/
│   └── Escritura constitución + estatutos originales
├── Acordeon_2022/
│   ├── Escritura 25-11-2022
│   ├── Acuerdos sociales asamblea
│   └── PENDIENTE: notificación inscripción RM
├── Préstamos_2019/
│   ├── Jenkins UNO 3M
│   ├── Jenkins DOS 1M
│   ├── Dime Shared 800K
│   ├── Acinas 210K
│   ├── Fco. López 100K
│   ├── Monforte 50K
│   ├── Gurrea (PENDIENTE H-03)
│   └── IPN (PENDIENTE H-03)
├── Cesiones_2019/
│   ├── A TCH2 (Jenkins UNO)
│   └── A TCH3 (Jenkins DOS + Dime + Monforte + Acinas)
├── Liquidaciones/
│   ├── 16-02-2022 Acinas
│   ├── 16-02-2022 Fco. López
│   ├── 16-02-2022 QC/Barrena/Yornolds
│   └── 30-09-2022 TCH DOS Jenkins
├── Auditoria_2026/
│   ├── Auditoría provisional 02-04-2026 (B88279880)
│   ├── Diario operaciones auditado 30-03-2026
│   └── Conciliación Mayor 2025 vs Audit
├── Asterion/
│   ├── Facility Asterion → TCIH (cuenta 17100008 1,80M€)
│   ├── Subrogación clase B 2,10M€ (side letters)
│   └── Reportings trimestrales
├── TCS/
│   ├── Cuentas anuales TCS
│   ├── Cliente Pacífico Cable (renovación + facturas)
│   └── Histórico desinversión 2021
├── Templus_CD_2pct/
│   └── Documentación 2% Class B Teras (Org chart Templus v8)
└── Side_letters/
    └── (PENDIENTE centralización CLO)
```

## Confidencialidad

- **A1-A10 (societarios)**: privilegio cliente-abogado. NO compartir fuera del pool socios sin aprobación CLO.
- **B1-B9 (financieros)**: sponsor-confidential. Compartir con audit firm + asesores.
- **C1-C6 (fiscal)**: privilegio cliente-abogado. NO compartir.
- **D1-D4 (regulatorio público)**: público tras depósito RM / BORME.
- **E1-E5 (interno TERAS)**: confidencial interno.
- **F1-F2 (bot ingest)**: bot procesa cualquier doc; clasificación posterior aplica reglas confidencialidad.

## Documentos prioritarios para localizar / reconstruir

| Prioridad | Documento | Fuente alternativa | Owner |
|---|---|---|---|
| ALTA | Contratos Gurrea 200K (52100008) + IPN ~853K (H-03) | Reconstrucción + opinion letter | CLO + asesor fiscal |
| ALTA | SPA Pacífico Cable + acuerdo dividendo TCS → TCIH (H-04) | Búsqueda Drive + email + notaría | CLO + TCS |
| MEDIA | Documentación identidad Dime Shared ↔ Quarter Capital (H-02) | Histórico Drive + CLO | CLO |
| MEDIA | Mayores PGC 2022-2024 (trazabilidad C/C 5510x multi-ejercicio) | Mayor históricos sandbox | Contabilidad |
| MEDIA | Side letters socio-a-socio centralizar repositorio CLO | Acopio desde cada socio | CLO |
| MEDIA | Reporting trimestral Asterion histórico (cuenta 17100008) | CFO archivos + Drive | CFO |
| BAJA | Modelo 200 IS TCIH 2018-2023 | Asesor + AEAT | Asesor fiscal |
| BAJA | Opinion letter art. 21 LIS sobre TCIH | Asesor — encargo nuevo | CFO + asesor |

## Audit cycle TCIH

| Año | Auditor | Cuentas anuales | Override equity-rank | Inscripción RM |
|---|---|---|---|---|
| 2018 | (histórico) | Depositadas | N/A | OK |
| 2019 | (histórico) | Depositadas | N/A | OK |
| 2020 | (histórico) | Depositadas | N/A | OK |
| 2021 | (histórico) | Depositadas | N/A — dividendo cta 2,3M€ registrado | OK |
| 2022 | (histórico) | Depositadas | N/A — acordeón sep-22 ejecutado | **PENDIENTE acordeón** |
| 2023 | (histórico) | Depositadas | N/A | **PENDIENTE acordeón** |
| 2024 | (histórico) | Depositadas | N/A | **PENDIENTE acordeón** |
| 2025 | B88279880 (provisional 02/04/2026) | Pendiente firme definitiva | **7.666.559€ aplicado** | **PENDIENTE acordeón** |
| 2026 | B88279880 (estimado) | Pendiente | Pendiente revisión | Pendiente |

## Cómo localizar cada documento

### En BD `bl_documents`

- `business_line_id='teras-capital'` + `doc_type` (audit/contract/sale/...) filtra docs vivos.
- Storage Supabase: bucket `documents/teras-capital/`.

### En Drive Teras

- Estructura `One_drive_Teras/TCIH/` (ver árbol arriba).
- Sincronización: bot `bot@terascap.es` clasifica + storage.

### En Signaturit

- Documentos firmados electrónicamente 2019 (Jenkins, cuentas en participación, cesiones).
- Acceso CLO + LSS.

### En notaría

- Acordeón 25/11/2022 + estatutos texto refundido.
- Acta constitución + actas asambleas extraordinarias.

### En RM Madrid

- Depósitos cuentas anuales 2018-2024 (público).
- Inscripciones históricas anteriores acordeón.

### En AEAT / Hacienda

- Modelos 200 IS + autoliquidaciones IVA + IS.

## Pendientes documentales prioritarios (a 18-may-2026)

1. **Inscribir escritura acordeón 25/11/2022 RM** (Q2 2026, CLO + notaría).
2. **Localizar / reconstruir contratos H-03** (Gurrea 200K + IPN ~853K).
3. **Localizar / reconstruir SPA Pacífico Cable + acuerdo dividendo TCS H-04**.
4. **Centralizar side letters socio-a-socio** en repositorio CLO único.
5. **Auditoría definitiva 2025** — firma final con override equity-rank ratificado.
6. **Opinion letter art. 21 LIS** sobre TCIH (encargo asesor).
7. **Mayores PGC 2022-2024** — trazabilidad C/C 5510x multi-ejercicio.
8. **Memoria contable NRV 19ª** TCIH formalizada.
