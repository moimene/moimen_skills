# SPA/SHA Playbook — CLO TERAS Capital

Diseño documental completo de SPA y SHA como instrumentos de ejecución del plan industrial.

---

## 1. Decisión: Locked Box vs Completion Accounts

### Árbol de Decisión

```
¿El target tiene cash flow estable y WC predecible?
  ├── SÍ → ¿El período signing→closing es < 3 meses?
  │         ├── SÍ → LOCKED BOX (preferido)
  │         └── NO → Locked box con protección reforzada de leakage
  │
  └── NO → ¿Existe estacionalidad fuerte o calidad de cobros volátil?
            ├── SÍ → COMPLETION ACCOUNTS con definiciones cerradas
            └── NO → Evaluar caso a caso; sesgo hacia locked box si
                     existe confort con la calidad de las cuentas
```

### Comparativa

| Criterio | Locked Box | Completion Accounts |
|----------|------------|---------------------|
| **Cuándo** | Cash estable, WC predecible, signing→closing corto | Estacionalidad, cobros volátiles, signing→closing largo |
| **Ventaja TERAS** | Previsibilidad, foco en ejecución post-cierre | Protección contra sorpresas de WC |
| **Riesgo principal** | Leakage no detectado | Arbitraje contable, retrasos |
| **Mitigante** | Leakage taxativo, locked box date claro | Definiciones cerradas, mecanismo anti-juego, expert determination |
| **Control de caja** | Covenants interinos restrictivos | Reconciliación con perímetro cerrado |

### Locked Box — Cláusulas Esenciales

| Componente | Diseño | Nota CLO |
|------------|--------|----------|
| Locked box date | Fecha de referencia para cuentas | Elegir cierre contable reciente con cuentas auditadas si posible |
| Permitted leakage | Lista taxativa: salarios ordinarios, opex normal, impuestos corrientes | Cada ítem definido y caped; NO "catch-all" categories |
| Non-permitted leakage | Todo lo que no está en permitted leakage | Incluir: dividendos, management fees, préstamos intragrupo, bonuses |
| Ticker interest | Compensación al vendedor por el tiempo signing→closing | Tasa y base acordadas; alineada con coste de oportunidad razonable |
| Seller covenants | Conducción ordinaria del negocio entre locked box date y closing | Consentimiento escrito para decisiones fuera de lo ordinario |

### Completion Accounts — Cláusulas Esenciales

| Componente | Diseño | Nota CLO |
|------------|--------|----------|
| Accounting policies | Políticas contables específicas para el cálculo | Iguales a las usadas en cuentas históricas; sin cambio unilateral |
| Working capital target | NWC target y rango de normalidad | Basado en media 12-24 meses; ajustado por estacionalidad |
| Cash / debt definitions | Qué entra y qué no en la definición | Cash-like y debt-like items listados exhaustivamente |
| Dispute resolution | Mecanismo de resolución de discrepancias | Expert determination > arbitraje (más rápido y económico) |
| True-up mechanism | Ajuste post-closing | Plazo de preparación, revisión y pago definidos |

---

## 2. Representaciones y Garantías (Reps & Warranties)

### Principio: Enfoque de Materialidad

> Concentrar en materias que destruyen valor si fallan. No buscar cobertura exhaustiva
> sino protección contra los riesgos que realmente erosionan múltiplos o caja.

### Diseño por Área

| Área de Reps | Materialidad | Selección CLO |
|-------------|-------------|---------------|
| **Financiera** | Alta — directa sobre valoración | P&L, BS, CF sin distorsiones materiales; WC conforme |
| **Contratos clave** | Alta — revenue concentration risk | Top 10-20 contracts vigentes; sin notice de terminación |
| **Empleo** | Media-Alta — litigios y costes ocultos | Headcount, salarios, planes de pensiones, litigios |
| **IP / Tecnología** | Sector-dependent | Propiedad limpia, licencias vigentes, sin infringement |
| **Regulatorio** | Alta en regulated sectors | Licencias vigentes, cumplimiento, sin procedimientos |
| **Fiscal** | Media-Alta | Declaraciones al día, sin inspecciones abiertas, sin contingencias |
| **Medio ambiente** | Sector-dependent | Permisos, contaminación, pasivos ambientales |
| **Litigios** | Alta | Listado, cuantificación de riesgo, provisiones |

### Régimen de Responsabilidad

| Componente | Diseño Recomendado | Justificación |
|------------|-------------------|---------------|
| **Overall cap** | % del equity value (typo: 15-30%) | Proporcionado al tamaño del deal |
| **Fundamental reps cap** | 100% equity value | Title, capacity, authority — no se negocian caps bajos |
| **De minimis** | 0.05-0.1% equity value | Filtro de claims triviales |
| **Basket (deductible/tipping)** | 0.5-1% equity value (tipping basket preferido) | Evitar primer-dólar liability en claims pequeños |
| **Survival: general** | 18-24 meses post-closing | Cubre período de integración |
| **Survival: fundamental** | Prescripción legal aplicable | Title, capacity — sin límite artificial |
| **Survival: fiscal** | Prescripción fiscal + 3-6 meses | Cubrir último ejercicio inspeccionable |
| **Survival: medio ambiente** | 3-5 años (sector-dependent) | Contaminación puede manifestarse tarde |

### W&I Insurance — Decisión

```
¿Deal size > €15-20M y mercado competitivo para seguros?
  ├── SÍ → W&I es herramienta eficiente
  │         ├── Comprador: elimina cap y basket del SPA
  │         ├── Vendedor: clean exit
  │         └── TERAS: facilita cierre, desbloquea pricing
  │
  └── NO → Régimen contractual con caps y baskets
            ├── Considerar for top-up insurance para riesgos específicos
            └── Evaluar coste vs beneficio
```

---

## 3. Condiciones Suspensivas (CPs)

### Principio: Operativizar hitos del plan de 100 días

| Tipo de CP | Ejemplos | Redacción CLO |
|------------|----------|---------------|
| **Regulatorias** | Aprobación competencia, licencias sectoriales | Plazos realistas; long-stop date con derecho a walk-away |
| **Consentimientos** | Contratos clave, landlords, JV partners | Best efforts con definición precisa; waiver mechanics |
| **Financiamiento** | Confirmación de funding del sponsor | Evidencia de financing commitment; MAC provisions |
| **Corporativas** | Board approvals, aprobaciones de IC | Timeline compatible con calendario institucional |
| **Material adverse change** | MAC/MAE como out | Definición restrictiva; excepciones de mercado, industria, pandemia |

### Temporal Design

| Fase | Plazo típico | Extensión |
|------|-------------|-----------|
| CPs regulatorias | 60-120 días | +30 días por esfuerzos razonables |
| Consentimientos | 30-60 días | Best efforts hasta long-stop |
| Long-stop date | 120-180 días post-signing | Derecho walk-away bilateral |

---

## 4. Covenants Interinos (Signing → Closing)

### Estándar de Conducción del Negocio

| Categoría | Covenant | Consentimiento Requerido |
|-----------|----------|--------------------------|
| **Capex** | No superar budget aprobado >10-15% | Escrito del comprador |
| **Contratación** | No contratar/despedir C-suite | Escrito |
| **Endeudamiento** | No nuevo endeudamiento >threshold | Escrito |
| **Dividendos** | No distribuciones fuera de lo ordinario | Escrito |
| **Contratos** | No firmar/modificar/terminar contratos materiales | Escrito |
| **Litigios** | No iniciar/resolver litigios >threshold | Escrito |
| **IP** | No disponer/licenciar IP material | Escrito |
| **Seguros** | Mantener cobertura vigente | Notificación |
| **Negocio ordinario** | Conducir con la diligencia debida | N/A — estándar general |

### Protección de Caja (Especial)

| Control | Mecanismo |
|---------|-----------|
| Cash monitoring | Reporte semanal de posición de caja |
| Cash sweep prohibition | No transferencias fuera del negocio ordinario |
| Capex freeze | Solo capex previamente aprobado y presupuestado |
| Advance payments | No anticipos fuera de práctica habitual |

---

## 5. SHA — Módulos

### Módulo de Governance

| Componente | Diseño CLO |
|-----------|------------|
| **Board composition** | Sponsor majority + TERAS seat(s) + Independent(s) when size permits |
| **Reserved matters** | Caja, capex >threshold, endeudamiento, disposiciones, M&A, C-suite |
| **Voting** | Simple majority ordinario; qualified majority para reserved matters |
| **Deadlock** | Escalation → mediation → put/call (último recurso) |
| **Committees** | Operating (semanal), Board (mensual), IC update (trimestral) |

### Módulo de Información

| Derecho | Cadencia | Formato |
|---------|----------|---------|
| Flash financiero | D+5 | P&L preliminar + cash position |
| Monthly reporting pack | D+10 | Full P&L, BS, CF, KPI dashboard |
| Board pack | D+12 | Reporting + strategy + risk + people |
| IC update memo | Trimestral | 2 pgs max + KPI summary |
| Audit access | Ad hoc | Con notice razonable |

### Módulo de Incentivos

| Componente | Diseño |
|-----------|--------|
| **Sweet equity allocation** | % definido en SHA; precio preferencial justificado |
| **Vesting temporal** | 3-4 años, cliff a 12 meses |
| **Vesting por hitos** | Performance gates ligados a KPIs específicos |
| **Good leaver** | FMV de equity vested; aceleración parcial |
| **Bad leaver** | Nominal value / cost; forfeiture de unvested |
| **Leaver events** | Definición precisa: dismissal for cause, voluntary resignation, etc. |
| **Performance gates** | Revenue, EBITDA, cash conversion, churn — con definiciones estables |

### Módulo de Transferencias

| Derecho | Diseño |
|---------|--------|
| **Lock-up** | 24-36 meses (alineado con vesting) |
| **ROFR/ROFO** | First refusal para sponsor; first offer para TERAS si aplica |
| **Tag-along** | Para TERAS en venta >threshold de control |
| **Drag-along** | Para sponsor si oferta >FMV + condiciones razonables |
| **Anti-dilución** | Limitada, weighted average, si procede por tesis |
| **Ruta a Co-GP** | Escalation clause si mandato demuestra track record institucional |

---

## 6. Tabla Levas de Negociación — Postura CLO

| Cláusula | Objetivo Sponsor | Postura CLO TERAS | Información Crítica |
|----------|-----------------|-------------------|---------------------|
| Precio y ajustes | Previsibilidad, protección caja | Locked box vs completion según WC risks | Histórico financiero, estacionalidad |
| Reps & Warranties | Cobertura riesgos materiales | Enfoque materialidad + disclosure | Red flags + contratos clave |
| Cap/basket/survival | Downside controlado | Caps por áreas, baskets razonables | Análisis prob×impacto + W&I |
| Escrow/retenciones | Cubrir riesgos latentes | % y duración proporcionales a red flags | Cuantificación contingencias |
| CPs | Certeza regulatoria | Redacción operativa + plazos realistas | Hitos regulatorios |
| Covenants interinos | Preservar valor | Conducción + vetos en decisiones críticas | Pipeline decisiones + capex |
| Governance SHA | Ejecución y control | Reserved matters proporcionales al mandato | RACI + KPIs definidos |
| Sweet equity | Alineación por resultados | Vesting + leavers + gates explícitos | KPI/cash targets |
