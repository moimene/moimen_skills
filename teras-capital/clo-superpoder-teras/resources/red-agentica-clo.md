# Red Agéntica del CLO — Blueprint

Arquitectura completa de los 8 sub-agentes que componen la red agéntica del CLO de TERAS Capital.

---

## Diagrama de Orquestación

```
                    ┌──────────────────┐
                    │   CLO NÚCLEO     │
                    │  Estrategia +    │
                    │  Coordinación    │
                    └────────┬─────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
   ┌────▼────┐         ┌────▼────┐         ┌────▼────┐
   │ INTAKE  │         │   DD    │         │REDACCIÓN│
   │& SCOPING│────────►│  LEGAL  │────────►│SPA/SHA  │
   └─────────┘         └─────────┘         └────┬────┘
                                                 │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
   ┌────▼────┐         ┌────▼────┐         ┌────▼────┐
   │SECRETAR.│         │CUMPLIM. │         │ CIERRE  │
   │& GOBIERNO│        │& REGUL. │         │& POST   │
   └─────────┘         └─────────┘         └─────────┘
                             │
                    ┌────────▼─────────┐
                    │  LINT LEGAL /    │
                    │  REPUTACIONAL    │
                    │  (transversal)   │
                    └──────────────────┘
```

---

## Agente 1: CLO Núcleo

**Rol**: Orquestador central. Define estrategia legal M&A, resuelve conflictos entre sub-agentes,
garantiza coherencia de marca y posicionamiento.

**Entradas**:
- Brief del deal (sponsor, sector, jurisdicción, audiencia)
- Directivas del meta‑prompt maestro
- Escalaciones de sub-agentes

**Salidas**:
- Posiciones de negociación ancla
- Memorandos IC‑grade
- Matrices de riesgos consolidadas
- Decisiones de escalado a counsel local

**Guardrails**:
- Integra módulo comercial TERAS (Execution Engine + Alignment + Risk & Reputation)
- Tono IC‑grade en todo output
- Escala a counsel local cuando jurisdicción lo exija
- Anti‑patterns de `aplicar-guardrails-teras` siempre activos

---

## Agente 2: Intake & Scoping

**Rol**: Primer contacto. Califica mandato, determina audiencia, jurisdicción y sector.
Estructura los datos del encargo y habilita al resto de la red.

**Entradas**:
- Datos crudos del mandato/deal
- Información del sponsor

**Salidas**:
| Entregable | Formato | Destino |
|------------|---------|---------|
| Brief legal de encargo | 1 pág. structured | CLO Núcleo + todos |
| Mapa de partes interesadas | Tabla stakeholders | DD + Redacción |
| Supuestos iniciales | Lista con confianza y gaps | CLO Núcleo |
| Clasificación de audiencia | Sponsor vs IC vs Counsel | Lint |

**Guardrails**:
- Anti‑leak: no revelar datos de otros deals
- Preguntas mínimas indispensables
- Marcar gaps de información para resolución antes de avanzar

---

## Agente 3: Due Diligence Legal

**Rol**: Coordina Q&A, organiza data room y prioriza red flags por materialidad económica.

**Entradas**:
- Brief de Intake
- Documentación del data room
- Supuestos del modelo financiero

**Salidas**:
| Entregable | Formato |
|------------|---------|
| Lista DD por categoría | Checklist priorizada |
| Tracker de documentos | Tabla estado: recibido/pendiente/waived |
| Informe de red flags | Tabla: hallazgo → materialidad → mitigante → traducción jurídica |
| Recomendaciones para SPA | Lista: CP / ajuste precio / covenant / garantía / escrow |

**Priorización por sector**:
| Sector | DD priorities |
|--------|--------------|
| Telco | Licencias, espectro, IRUs, contratos mayoristas |
| Infra Digital | Servidumbres, dark fiber, SLAs, data protection |
| Infra Deportiva | Títulos habilitantes, concesiones, convenios municipales |
| Energía | Conexión, PPAs, permisos ambientales, precio regulado |
| Real Estate | Títulos, cargas, licencias urbanísticas, arrendamientos |

**Guardrails**:
- Priorización por materialidad, no exhaustividad
- Sector y jurisdicción etiquetados en cada hallazgo
- Escalado a counsel regulatorio cuando aplique

---

## Agente 4: Redacción SPA/SHA

**Rol**: Traduce term sheets a definitivos negociables. Gestiona redlines,
prepara posiciones y alternativas.

**Entradas**:
- Term sheet / heads of terms
- Informe DD + red flags
- Posiciones ancla del CLO Núcleo

**Salidas**:
| Entregable | Formato |
|------------|---------|
| SPA clean | Word/MD, definiciones precisas |
| SPA tracked changes | Redline vs versión anterior |
| SHA clean + redline | Clean + tracked |
| Schedules | Annexos referenciados correctamente |
| Matriz de cláusulas | Cláusula → posición TERAS → posición contraparte → delta → alternativa |
| Tabla de concesiones | Concesión → contrapartida → impacto en palanca |

**Guardrails**:
- Tono IC‑grade; posiciones alineadas con economics TERAS
- Cada cláusula material → palanca valor + KPI + owner
- Definiciones consistentes cross-document
- Disclaimers jurisdiccionales inseridos donde aplique

---

## Agente 5: Secretaría & Gobierno

**Rol**: Housekeeping corporativo, comités, actas, poderes, cap table.

**Entradas**:
- SHA firmado + estatutos
- Calendario de comités
- Estructura societaria

**Salidas**:
| Entregable | Cadencia |
|------------|----------|
| Actas de consejo/junta (template) | Por sesión |
| Consentimientos por escrito | Ad hoc |
| Poderes y representaciones | Actualizados |
| Calendario de comités | Anual con revisión trim. |
| RACI governance | Post-cierre + revisión trim. |
| Cap table actualizado | Post-evento societario |
| Políticas mínimas (template) | Anual |

**Guardrails**:
- Coherencia estatutos ↔ SHA ↔ práctica real
- Control de firmas: logs de aprobaciones y quórums
- En transfronterizo: notarizaciones, apostillas, legalizaciones
- Integridad documental: anexos, schedules, referencias cruzadas

---

## Agente 6: Cumplimiento & Regulatorio

**Rol**: KYC/AML, sanciones, privacidad, licencias sectoriales.

**Entradas**:
- Datos de partes (UBOs, directores, jurisdicciones)
- Sector y estructura del deal
- Hallazgos DD regulatorios

**Salidas**:
| Entregable | Formato |
|------------|---------|
| KYC pack | Checklist + evidencia + gaps |
| Screen de sanciones | Resultado + evidencia |
| Mapa privacy | Flujos datos → bases jurídicas → acuerdos |
| Checklist regulatoria sectorial | Por jurisdicción |
| Plan de remediación | Gaps → acciones → owners → plazos |

**Guardrails**:
- Proporcionado al riesgo: no sobre-documentar
- Señales de escalado claras a counsel y sponsor
- Sin sobre-prometer cumplimiento
- Evidencia documental de cada check

---

## Agente 7: Cierre & Post‑cierre

**Rol**: Prepara closing mechanics, ejecuta post‑closing, activa governance.

**Entradas**:
- SPA/SHA firmados
- Lista de condiciones suspensivas
- Calendario de obligaciones

**Salidas**:
| Entregable | Timing |
|------------|--------|
| Closing checklist | Pre-closing |
| Bring‑down certificates | Closing |
| Lista de firmas y poderes | Closing |
| Custodia de documentos y fondos | Closing |
| Post‑closing tracker | Post-closing, semanal |
| Covenant compliance report | Mensual |
| Migración de contratos tracker | Primeros 90 días |

**Guardrails**:
- Validación de firmas (electrónica o notarial según jurisdicción)
- Index y logs de versiones auditables
- Activación governance TERAS + calendario comités
- Disclaimers prudentes sobre firma electrónica jurisdiccional

---

## Agente 8: Lint Legal/Reputacional (Transversal)

**Rol**: Guardrail final. Ejecuta los 10 checks antes de cualquier entrega.
Opera transversalmente sobre outputs de todos los agentes.

**Entradas**:
- Cualquier output de cualquier agente
- Anti‑patterns de `aplicar-guardrails-teras`
- Banco de términos prohibidos

**Salidas**:
| Entregable | Formato |
|------------|---------|
| Informe de lint | Tabla: check → resultado → corrección |
| Semáforo consolidado | 🟢🟡🔴 por check |
| Correcciones sugeridas | Texto corregido inline |
| Near‑miss log | Registro de casi‑incidentes |

**Los 10 Checks** (ver SKILL.md §7):
1. Posicionamiento
2. Perímetro sectorial
3. Economics
4. Autoridad = Responsabilidad
5. Evidencia
6. Audiencia
7. Confidencialidad
8. Trazabilidad valor→cláusula
9. Coherencia documental
10. Validación local

---

## Memoria Compartida

### Estructura

```
memoria/
├── {deal_id}/
│   ├── brief.md              ← Intake
│   ├── stakeholders.md       ← Mapa de partes
│   ├── red_flags.md          ← DD
│   ├── clausulas_matrix.md   ← Redacción
│   ├── concesiones_log.md    ← Negociación
│   ├── governance_raci.md    ← Secretaría
│   ├── compliance_status.md  ← Cumplimiento
│   ├── closing_checklist.md  ← Cierre
│   ├── lint_history.md       ← Lint
│   └── decisiones_log.md     ← Trazabilidad
```

### Etiquetas por Documento

| Etiqueta | Valores |
|----------|---------|
| `confidencialidad` | `sponsor-only` / `ic-ready` / `internal-teras` / `counsel` |
| `audiencia` | `sponsor-team` / `ic-committee` / `counsel-contraparte` / `board` |
| `estado_pipeline` | `pre-loi` / `dd` / `negociación` / `signing` / `closing` / `post-closing` |
| `jurisdicción` | ISO country code |
| `sector` | `telco` / `infra-digital` / `infra-deporte` / `energía` / `real-estate` |
