# Governance — Gemswell

> Snapshot 31/12/2025 · Estructura governance TCH3 + Valdorba subgrupo + SW Infrasports + cadena Quarter/Grand View.

## Foros principales

| Foro | Cadencia | Asistencia TERAS | Owner agenda | Notas |
|---|---|---|---|---|
| **Consejo TCH3** | Trimestral | CIO + CFO TERAS | TCH3 (Pool MdL + MMS designados) | Voz coordinada MdL 46,86% / MMS 36,41% |
| **Comité industrial SW Infrasports** | Trimestral | TERAS + Stoneweg paritario | SW Infrasports SHA nov 2024 | Decisiones paritarias 50/50, mediación |
| **Steerco Valdorba Parques** (cabecera) | Trimestral | CIO TERAS | TERAS coordina vía TCH3 | Supervisión subgrupo operativo |
| **Steerco VM / VPS / VPSH** (operativo) | Bimestral / trimestral | CFO + ops TERAS | Management Valdorba | KPIs operativos, capex, retention |
| **Comité Kelpa** (acreedor VM) | Ad-hoc / semestral | CFO TERAS + Kelpa | Acuerdo Kelpa | Servicio deuda, condiciones refinanciación |
| **Auditoría externa TCH3 + subgrupo** | Anual | CFO | Audit firm | Provisional 02/04/2026 (B88547567) — definitiva Q2 2026 |
| **Asambleas TCH3** (12 socios) | Mínimo anual + ad-hoc | Todos socios | TCH3 (MM Sports / IPN designados) | Aprobación cuentas, ampliaciones, modificaciones ISHA |
| **Comité gestor TERAS** (interno) | Mensual | Equipo TERAS | CIO TERAS | Coordinación líneas Gemswell vs Olin / Templus / TCIH |
| **Cierre formal Quarter Capital + Grand View** | Anual | CFO MdL + García Ruiz | García Ruiz | Mayores 2018-2025 cuentas 25200x + 5510x — pendientes procesar |

## RACI extendido — actividades clave

### Subsanación capital TCH3 (dic-2025 — completada parcialmente)

| Actividad | Responsable | Aprobador | Consultado | Informado |
|---|---|---|---|---|
| Acta subsanación | CLO TERAS | Consejo TCH3 | Asesores legales | Socios TCH3 (12) |
| Elevación pública | Notario | Consejo TCH3 | CLO | Socios TCH3 |
| Inscripción RM | Notario / RM | RM Madrid | CLO | Socios TCH3 + I. Velilla (condición suspensiva) |
| Reflejo contable cierre 2025 | CFO TERAS | Audit firm | CFO MdL | Pool MdL + socios |
| Audit provisional 02/04/2026 | Audit firm B88547567 | CFO | CLO | Socios TCH3 |

### Cap table movements sept 2025

| Movimiento | Responsable | Aprobador |
|---|---|---|
| Capitalización créditos MCT +300K | CFO TERAS | Asamblea TCH3 |
| Capitalización créditos Gurrea +50K | CFO TERAS | Asamblea TCH3 |
| Capitalización deuda R. Romero +100K (nuevo socio) | CFO TERAS | Asamblea TCH3 |
| Capitalización deuda Lafarga +50K (nuevo socio) | CFO TERAS | Asamblea TCH3 |
| Adquisición I. Velilla desde TCIH +200K | CFO TERAS | Asamblea TCH3 + Consejo TCIH | Condición suspensiva inscripción RM |

### Audit provisional 02/04/2026 (B88547567)

| Hito | Responsable |
|---|---|
| Programa auditoría | Audit firm |
| Verificación cap table post-subsanación | Audit firm + CFO TERAS |
| Reconocimiento efecto contable 31/12/2025 | Audit firm |
| Reclasificación cuenta 17100011 (fix bug #14) | CFO + parser team (15-may-2026) |
| Audit definitivo 2025 | Audit firm — Q2 2026 |

### KPIs operativos VM (ramp-up surf park urbano)

| KPI | Cadencia | Responsable | Foro |
|---|---|---|---|
| Visitantes / mes | Mensual | Ops VM | Steerco trimestral |
| ARPU / sesión surf | Mensual | Ops VM | Steerco trimestral |
| Ingresos | Mensual | Ops VM | Steerco trimestral |
| Tasa ocupación | Mensual | Ops VM | Steerco trimestral |
| Eventos H&S | Continuo | Ops VM | Comms plan |
| Capex network | Trimestral | CFO Valdorba | Steerco TCH3 |

### NAV VSO II / Wave Park

| Actividad | Responsable | Cadencia |
|---|---|---|
| NAV unaudited compartimento | Stoneweg / SW Infrasports | Trimestral o ad-hoc |
| Comunicación email/comm a TERAS | Stoneweg (R. Romero) | Trimestral |
| Registro en BD `waterfall_params.vso_ii_unaudited_nav_pct` | CFO TERAS | Tras recepción comm |
| Audit anual Wave Park | Audit firm SW Infrasports | Anual |

## Composición consejos / órganos de gobierno

### Consejo TCH3 (estimado — pendiente formalización ISHA)

- Representantes Pool MdL (IPN / TCH2): designados por IPN (CFO MdL + asesor).
- Representante MM Sports (36,41%): designado por MMS SLU.
- Representante MCT (5,55%): Monforte Consultoría.
- Representantes Indeps + LSS + Teras (rotatorios o por bloque).

### Asamblea TCH3 (12 socios — voto pro-rata)

Pool MdL 46,86% + MM Sports 36,41% = **83,27% conjunto** suficiente para mayoría simple. Supermayorías estatutarias / ISHA pueden requerir umbral superior (a confirmar ISHA formal).

### Comité industrial SW Infrasports (paritario)

- 2 miembros designados por TCH3.
- 2 miembros designados por Stoneweg.
- Decisiones por consenso; en bloqueo, mediación.

### Steerco Valdorba Parques

- CIO TERAS (presidencia).
- CFO TERAS.
- Management Valdorba (CEO subgrupo + CFO Valdorba).
- Asistencia ad-hoc Stoneweg si proyecto en perímetro SHA.

## Documentación governance

| Documento | Estado | Ubicación |
|---|---|---|
| ISHA Gemswell (formal) | Pendiente formalización completa | `bl_documents` (parcial) |
| Pacto Socios SHA SW Infrasports | Firmado nov 2024 | `bl_documents` |
| Acuerdo Kelpa (VM acreedor) | Firmado | `bl_documents` |
| Audit provisional TCH3 02/04/2026 | Recibido | `bl_documents` (B88547567) |
| Acta subsanación capital TCH3 dic-2025 | Firmada antes 31/12/2025 | Notaría + `bl_documents` |
| Elevación pública subsanación ene-2026 | Pendiente verificación | Notaría |
| Email Stoneweg/Ramón Romero NAV VSO II 124,48% (7-may-2026) | Recibido | inbox + `bl_documents` |
| Email Miguel 7-may-2026 (Quarter/Grand View capitalizados) | Recibido | inbox + `bl_documents` |
| Mayores 2018-2025 Quarter + Grand View | Enviados García Ruiz, pendientes procesar | inbox |

## Conflictos potenciales — protocolos

| Conflicto | Protocolo |
|---|---|
| Pool MdL (46,86%) vs MM Sports (36,41%) | Voto pro-rata; supermayoría ISHA pendiente confirmar; mediación previa |
| TCH3 (50%) vs Stoneweg (50%) en SW Infrasports | Mediación SHA, escalado consejo SW Infrasports |
| Bloqueo Wave Park / VSO II exit timing | Comité industrial SW Infrasports; en bloqueo, cláusula deadlock SHA |
| Disputa con Kelpa (acreedor VM) | Comité Kelpa, asesoría jurídica TERAS, en última instancia tribunales |
| Reclasificación contable (bug #14 y similares) | CFO TERAS + parser team + audit firm |
| Inscripción RM subsanación demorada | CLO TERAS + Notaría + audit firm para mantener efecto contable provisional |

## Confidencialidad

- ISHA Gemswell + Pacto Socios SHA SW Infrasports + Acuerdo Kelpa: estrictamente confidencial.
- Cifras 2025 TCH3 + subgrupo: confidencial salvo extracción para informes banco / auditoría externa.
- Cap table 12 socios TCH3: confidencial; en informes para terceros usar agregados por pool (MdL, MMS, MCT, Indeps, etc.).
- Subsanación dic-2025: comunicada a socios; comunicación externa solo tras inscripción RM.
- NAV VSO II 124,48%: confidencial; uso interno valoración + audit support.
