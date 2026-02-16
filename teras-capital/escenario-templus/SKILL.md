---
name: escenario-templus
capa: L3b-escenarios
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras, aplicar-guardrails-teras, challenge-cognitivo-teras]
triggers: >
  Se activa cuando el usuario mencione: Templus, proyecto Templus, activo Templus,
  reunión Templus, governance Templus, KPIs Templus, o cualquier referencia al
  activo/proyecto Templus.
description: >
  Precarga contexto operativo del activo/proyecto Templus: estructura, fase,
  stakeholders, KPIs específicos, governance particular, riesgos y dinámicas.
  Permite respuestas contextualizadas a cualquier pregunta sobre este activo.
---

# Escenario: Activo/Proyecto — Templus

## 1. Naturaleza del Activo

**Templus** es un activo/proyecto dentro del portfolio operativo de TERAS Capital.
Este escenario precarga el contexto necesario para que toda interacción sobre
Templus esté contextualizada.

> **Nota**: Este skill funciona como template parametrizable. Cuando el usuario
> proporcione datos específicos de Templus (sector, fase, KPIs, stakeholders),
> estos se incorporan como contexto persistente.

### Ficha del Activo

| Parámetro | Valor | Fuente |
|-----------|-------|--------|
| **Nombre** | Templus | — |
| **Sector** | [A completar por usuario: Telco/Infra Digital/Sports Infra/Energía/RE] | Usuario |
| **Fase** | [A completar: Pre-adquisición/Transición/Ejecución/Madurez/Exit] | Usuario |
| **Sponsor** | [A completar] | Usuario |
| **Rol TERAS** | Operating Manager + coinversor minoritario | Default |
| **Mandate scope** | [A completar: operativo completo / funcional / advisory+] | Usuario |
| **Economics TERAS** | [A completar: paquete Lean/Core/Co-GP] | Usuario |
| **Governance** | [A completar: comités, RACI, reporting] | Usuario |

### Protocolo de Contexto

```
SI el usuario menciona Templus pero NO ha proporcionado la ficha:
  1. Generar output con supuestos explícitos
  2. Preguntar: "Para contextualizar mejor, ¿puedes confirmar sector,
     fase actual y principales KPIs de Templus?"
  3. Cuando el usuario complete, actualizar la ficha como contexto persistente

SI el usuario YA ha proporcionado contexto de Templus:
  1. Usar toda la información acumulada
  2. Mantener coherencia con datos anteriores de la conversación
  3. Si hay contradicción → señalar y pedir aclaración
```

---

## 2. Mapa de Stakeholders Templus

| Actor | Rol | Prioridades | Gestión TERAS |
|-------|-----|-------------|---------------|
| **Sponsor** | Propietario/Inversor | Retorno, timeline, governance | Reporting disciplinado, proactividad en riesgos |
| **Management** | Operación diaria | Recursos, estabilidad, mandato claro | Soporte + dirección, no micro-management |
| **TERAS** | Operating Manager | Ejecución del plan, KPIs, autoridad | Balance entre push y soporte |
| **Regulador** | (si aplica) | Cumplimiento | Anticipación, compliance proactivo |
| **Clientes/Usuarios** | (si aplica) | Servicio, precio, calidad | Métricas de satisfacción, churn, NPS |

---

## 3. Framework de Fases

### Fase 1: Transición (Días 0-30)

| Prioridad | Entregable | Owner |
|-----------|-----------|-------|
| Onboarding TERAS | Plan de primeras semanas, accesos, contactos | TERAS |
| Diagnóstico rápido | Mapa de execution gaps, quick wins | TERAS |
| Governance mínima | RACI, comités, reporting mínimo | TERAS + Sponsor |
| Línea base KPIs | Definición, medición baseline, targets | TERAS + Management |

### Fase 2: Ejecución (Días 30-180)

| Prioridad | Entregable | Owner |
|-----------|-----------|-------|
| Plan de 100 días | Hitos, KPIs, owners, dependencias | TERAS |
| Quick wins | 3-5 mejoras de impacto rápido | TERAS + Management |
| Governance operativa | Comités funcionando, reporting estable | TERAS |
| Pipeline/Revenue | Plan comercial o de ramp-up | Management + TERAS |

### Fase 3: Madurez (Día 180+)

| Prioridad | Entregable | Owner |
|-----------|-----------|-------|
| KPIs en target | Dashboard automatizado | Management |
| Governance institucional | Reporting IC-grade, comités maduros | TERAS |
| Transferencia | Capacidades transferidas a management | TERAS |
| Exit readiness | Preparación para desinversión si aplica | TERAS + Sponsor |

---

## 4. KPIs Específicos Templus

### Template de KPI Pack

| Categoría | KPI | Definición | Baseline | Target Y1 | Target Y3 | Owner | Fuente | Frecuencia |
|-----------|-----|-----------|----------|-----------|-----------|-------|--------|------------|
| **Financiero** | Revenue | Ingresos netos | | | | | | Mensual |
| **Financiero** | EBITDA | EBITDA ajustado | | | | | | Mensual |
| **Financiero** | Cash conversion | EBITDA to cash | | | | | | Trimestral |
| **Comercial** | Pipeline | Valor pipeline cualificado | | | | | | Mensual |
| **Comercial** | Churn | Tasa de bajas | | | | | | Mensual |
| **Operativo** | Capex efficiency | Capex real vs plan | | | | | | Trimestral |
| **Operativo** | Project delivery | Hitos cumplidos en plazo | | | | | | Mensual |
| **Governance** | Reporting on-time | % reportes entregados en plazo | | | | | | Mensual |
| **Governance** | Comité attendance | Asistencia a comités | | | | | | Por comité |
| **Personas** | Key hires | Contrataciones clave completadas | | | | | | Trimestral |

> Estos KPIs se personalizan cuando el usuario proporciona sector y datos de Templus.

---

## 5. Risk Register Templus

### Template

| # | Categoría | Riesgo | Probabilidad | Impacto | Score | Mitigante | Owner | Status | Fecha revisión |
|---|-----------|--------|-------------|---------|-------|-----------|-------|--------|---------------|
| 1 | Operativo | | A/M/B | A/M/B | | | | Abierto/Mitigado/Cerrado | |
| 2 | Comercial | | | | | | | | |
| 3 | Regulatorio | | | | | | | | |
| 4 | Financiero | | | | | | | | |
| 5 | Personas | | | | | | | | |

### Categorías de Riesgo Estándar

- **Operativo**: Ejecución, delivery, calidad, procesos
- **Comercial**: Revenue, pipeline, clientes, competencia
- **Regulatorio**: Licencias, permisos, compliance
- **Financiero**: Cash, covenant, funding, FX
- **Personas**: Key man, retención, capacidad
- **Reputacional**: Marca TERAS, relación con sponsor
- **Governance**: RACI, comités, reporting, decisiones

---

## 6. Entregables por Contexto Templus

| Si el usuario pide... | Generar... | Con qué skills |
|-----------------------|------------|----------------|
| "Status de Templus" | KPI Dashboard + Risk update + Next steps | Este + COO |
| "Preparar Steerco Templus" | Kit completo Steerco (usar escenario-steerco como base) | Este + Steerco |
| "Presentation Templus" | Deck con brand TERAS, datos del activo | Este + generar-presentacion |
| "One-pager Templus" | One-pager ejecutivo | Este + generar-one-pager |
| "Risk review Templus" | Risk register actualizado + análisis | Este + challenge cognitivo |
| "Plan 100 días Templus" | Plan completo con hitos, KPIs, RACI | Este + COO |
| "Board memo Templus" | Memo formal para Consejo | Este + generar-board-memo |

---

## 7. Lint Templus

```
TEMPLUS LINT 1 — ¿La ficha del activo está completa o se han declarado supuestos?
TEMPLUS LINT 2 — ¿Los KPIs mencionados son coherentes con el sector?
TEMPLUS LINT 3 — ¿El risk register está actualizado?
TEMPLUS LINT 4 — ¿La fase del activo está correctamente identificada?
TEMPLUS LINT 5 — ¿Los entregables corresponden a la fase actual?
TEMPLUS LINT 6 — ¿La confidencialidad es Sponsor-confidential?
TEMPLUS LINT 7 — ¿No se mezcla información de otros activos?
```

---

## Recursos

- [Template Plan 100 Días](resources/template-plan-100-dias.md)
- [KPI Pack por Sector](resources/kpi-pack-sectorial.md)
