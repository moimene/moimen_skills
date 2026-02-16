# Lint Legal‑Reputacional + Métricas — CLO TERAS Capital

Sistema de control de calidad y métricas de rendimiento del CLO.

---

## 1. Los 10 Lint Checks

| # | Check | Verifica | FAIL si | Severidad |
|---|-------|---------|---------|-----------|
| 1 | **Posicionamiento** | TERAS = operating manager + coinversor minoritario | "VC", "fondo", "GP", "family office" | 🔴 CRÍTICA |
| 2 | **Perímetro Sectorial** | Solo telco, infra, energía, RE, deportivo | Sector fuera de perímetro | 🔴 CRÍTICA |
| 3 | **Economics** | Fees ↔ responsabilidad explicados | Fees sin justificación | 🟡 ALTA |
| 4 | **Autoridad = Responsabilidad** | No obligaciones sin derechos | Accountability sin RACI | 🔴 CRÍTICA |
| 5 | **Evidencia** | Solo datos del usuario | Track record inventado | 🔴 CRÍTICA |
| 6 | **Audiencia** | Output calibrado (sponsor vs IC vs counsel) | Material IC a counsel | 🟡 ALTA |
| 7 | **Confidencialidad** | Sin cross‑contamination entre deals | Datos de otros deals | 🔴 CRÍTICA |
| 8 | **Trazabilidad Valor→Cláusula** | Cada cláusula → palanca + KPI + owner | Cláusula "huérfana" | 🟡 ALTA |
| 9 | **Coherencia Documental** | Definiciones consistentes, refs correctas | Definición ambigua, ref rota | 🟡 ALTA |
| 10 | **Validación Local** | Puntos jurisdiccionales marcados | Sin disclaimer jurisdiccional | 🟡 ALTA |

---

## 2. Formato del Lint Report

```
══════════════════════════════════════
      LINT REPORT — CLO TERAS
══════════════════════════════════════
Deal:      {deal}
Documento: {tipo}
Audiencia: {sponsor / IC / counsel}
Fecha:     {fecha}
──────────────────────────────────────
CHECK 1 — POSICIONAMIENTO    [🟢/🔴]
CHECK 2 — PERÍMETRO          [🟢/🔴]
CHECK 3 — ECONOMICS          [🟢/🔴]
CHECK 4 — AUTORIDAD          [🟢/🔴]
CHECK 5 — EVIDENCIA          [🟢/🔴]
CHECK 6 — AUDIENCIA          [🟢/🔴]
CHECK 7 — CONFIDENCIALIDAD   [🟢/🔴]
CHECK 8 — TRAZABILIDAD       [🟢/🔴]
CHECK 9 — COHERENCIA DOC.    [🟢/🔴]
CHECK 10 — VALIDACIÓN LOCAL  [🟢/🔴]
──────────────────────────────────────
RESULTADO: {X}/10 PASS
SEMÁFORO:  🟢 Listo | 🟡 Correcciones | 🔴 NO ENTREGAR
══════════════════════════════════════
```

---

## 3. Métricas de Efectividad

### Familia 1: Ciclo y Calidad Documental

| Métrica | Target | Alerta |
|---------|--------|--------|
| Tiempo LOI → 1er borrador IC‑grade | ≤{X} días | >{X+Y} |
| % aceptación primera pasada | ≥70% | <50% |
| Iteraciones por documento | ≤3 | >5 |
| Lint fail rate | Tendencia ↓ | Tendencia ↑ |
| Concentración de fails | Distribuido | >40% en 1 cat. |

### Familia 2: Control de Riesgos

| Métrica | Target | Alerta |
|---------|--------|--------|
| Delta modelo vs términos firmados | ≤{X}% | >{X}% |
| Claims contra escrows | 0 | >0 |
| Disputas post-cierre | 0 | >0 |
| % cláusulas con KPI+owner+cadencia | ≥90% | <75% |

### Familia 3: Gobernanza y Reputación

| Métrica | Target | Alerta |
|---------|--------|--------|
| Incidentes confidencialidad | 0 | >0 |
| Near‑misses | Tendencia ↓ | Tendencia ↑ |
| Puntualidad reporting | ≥95% | <85% |
| Quórum comités | 100% | <90% |

---

## 4. Bucle de Mejora Continua

| Trigger | Acción Correctiva |
|---------|-------------------|
| Tiempo 1er borrador > umbral | Revisar intake + ampliar library templates |
| Iteraciones ↑ | Inspeccionar matrices + mejorar definiciones |
| Claims escrow > 0 | Recalibrar definiciones contables |
| Disputas earn‑out > 0 | Rediseñar métricas + expert determination |
| Lint fails concentrados | Ajustar meta‑prompt + reforzar templates |
| Near‑misses ↑ | Reforzar etiquetado + restringir acceso |

### Cadencia

| Revisión | Frecuencia | Output |
|----------|-----------|--------|
| Lint (por deal) | Cada entrega | Lint report |
| Dashboard métricas | Mensual | Alert flags |
| Deep dive | Trimestral | Improvement plan |
| Meta‑prompt tuning | Semestral | Updated prompt |
