# Documentos referencia — Olin

> Listado curado de documentos relevantes para Olin. Cruce con tabla BD `bl_documents` filtrada por `business_line_id='olin'` + documentos en repositorios externos.

## Categorías de documentación

### A. Documentos societarios y contractuales

| # | Documento | Tipo | Owner | Localización |
|---|---|---|---|---|
| A1 | ISHA TUCA reformulado (post-Asterion entry) | ISHA | TERAS CLO | Drive `One_drive_Teras/Olin/ISHA/` |
| A2 | SPA TUCA original (Class B + Privilegiadas) | SPA | TERAS CLO | Drive `One_drive_Teras/Olin/SPA/` |
| A3 | Anexo IV Auditoría TCH1 (cap table + derechos económicos) | Audit Anexo | Audit firm | Drive `One_drive_Teras/Olin/Audit/` |
| A4 | Auditoría TUCA Bidco 2024 (cifras FY2024) | Audit | Audit firm TUCA | Drive `One_drive_Teras/Olin/Audit/2024/` |
| A5 | Financing Agreement Asterion ↔ Tuca Midco | Loan agreement | TERAS CLO + Asterion | Drive `One_drive_Teras/Olin/Asterion/` |
| A6 | Class B Manager agreements individuales | Mgmt agreements | TERAS CLO | Drive `One_drive_Teras/Olin/Mgmt/` |
| A7 | Acuerdos TCH1 ↔ Class A Independientes (Monforte/LSS/Gurrea/Menéndez) | Side letters | TERAS CLO | Drive `One_drive_Teras/Olin/TCH1/Acuerdos/` |
| A8 | Convenio España-Luxemburgo doble imposición (referencia genérica) | Tratado fiscal | Hacienda | Público / BOE |

### B. Documentación financiera y operativa

| # | Documento | Tipo | Fecha | Localización |
|---|---|---|---|---|
| B1 | Cierre TCH1 31/12/2025 | Balance + Cuentas | 2026 (pendiente firme) | `entity_balances.tch1` BD |
| B2 | Cierre TUCA Bidco 31/12/2024 (audit) | Balance + P&L | 2025 | `entity_balances.tuca` BD + Drive |
| B3 | KPI pack MasOrange trimestral | KPI dashboard | Continuo | Drive `One_drive_Teras/Olin/KPIs/` |
| B4 | Steerco minutes TUCA Q1-Q4 | Minutes | Continuo | Drive `One_drive_Teras/Olin/Steerco/` |
| B5 | Modelo financiero waterfall Olin (Excel) | Modelo | Vigente | Drive `One_drive_Teras/Olin/Modelo/` |
| B6 | Term sheet refinanciación Asterion 2027-2028 | Term sheet | Pendiente Q1 2027 | — |
| B7 | NBO MasOrange firme (esperado Q2 2026) | NBO | Pendiente | — |

### C. Documentación fiscal

| # | Documento | Tipo | Owner |
|---|---|---|---|
| C1 | Opinion letter art. 21 LIS Olin | Tax opinion | Asesor fiscal TERAS |
| C2 | SOPARFI LU compliance Tuca Bidco/Midco | Tax compliance | Asesor LU |
| C3 | Documentación NRV 19ª TCH1 (inversión grupo) | Memoria contable | Auditor TCH1 |
| C4 | Estudio escenarios fiscales exit | Análisis | Asesor fiscal TERAS |

### D. Documentación regulatoria / pública

| # | Documento | Tipo |
|---|---|---|
| D1 | Resolución CNMC fusión Orange+MásMóvil | Resolución regulatoria |
| D2 | MasOrange company report (público) | Annual report |
| D3 | Análisis de mercado telco España | Research externos |

### E. Documentación interna TERAS

| # | Documento | Tipo |
|---|---|---|
| E1 | Tesis inversión Olin (IC original) | IC paper |
| E2 | Plan 100 días Olin (CIO) | Operating plan |
| E3 | Risk register Olin (vivo) | Risk register |
| E4 | Comms plan TUCA (PR/IR) | Comms |
| E5 | Roadmap exit Olin 2027-2029 | Roadmap |

## SQL — extracción documentos vivos

```sql
SELECT id, name, doc_type, source, classification_source, uploaded_at, storage_path, summary
FROM bl_documents
WHERE business_line_id = 'olin'
ORDER BY doc_type, uploaded_at DESC;
```

Output esperado: documentos ingestados por bot `bot@terascap.es` + uploads manuales. `classification_source` muestra agent_auto / agent_reviewed / agent_corrected / human.

## Cómo localizar cada documento

### En Drive (Teras Capital)

Estructura `One_drive_Teras/Olin/`:
- `ISHA/` — versiones ISHA + amendments
- `SPA/` — SPA inicial + addendums
- `Audit/{TCH1,TUCA}/{año}/` — auditorías y Anexos IV
- `Steerco/{Q1-Q4 año}/` — minutes + decks
- `KPIs/` — packs trimestrales MasOrange
- `Asterion/` — facility agreement + amendments
- `Mgmt/` — agreements Class B
- `TCH1/Acuerdos/` — side letters Class A independientes
- `Modelo/` — modelos Excel waterfall
- `Comms/` — comms plan + PR

### En BD MdL (`bl_documents`)

- Documentos ingestados con metadata canónica `{business_line_id: 'olin', doc_type, source, bl_document_id}`.
- RAG indexado con `rag_documents.metadata.business_line_id = 'olin'`.

### En email (`bot@terascap.es`)

- Inbox bot recibe ingest emails con asunto/cuerpo clasificable.
- Cada documento ingerido se crea `bl_documents` row + `agent_inbox_log` row.

## Audit cycle

| Año | TCH1 | TUCA Bidco | Anexo IV TCH1 |
|---|---|---|---|
| 2022 | (entrada inversión) | Audit FY22 | — |
| 2023 | Audit FY23 | Audit FY23 | Anexo IV |
| 2024 | Audit FY24 | Audit FY24 ✓ | Anexo IV ✓ |
| 2025 | Pendiente firme (Q2-Q3 2026) | Pendiente firme (Q2-Q3 2026) | Pendiente Q3 2026 |

## Confidencialidad

- **A1-A7**: Sponsor-confidential (TERAS + Asterion + Tuca Midco + audit firm). NO compartir fuera del pool socios sin aprobación CLO.
- **B3-B5**: Operacional sensible. Comparte con steerco + socios.
- **C1-C4**: Privilegio cliente-abogado. NO compartir.
- **D1-D3**: Público.
- **E1-E5**: Interno TERAS.

## Pendientes documentales

1. Confirmar audit firm TCH1 + TUCA en `business_lines.olin` (campo no poblado).
2. Ingerir Anexo IV TCH1 FY2024 a `bl_documents`.
3. Recibir term sheet refinanciación Asterion (Q1 2027).
4. NBO MasOrange firme (Q2 2026).
5. Opinion letter art. 21 LIS actualizada.
