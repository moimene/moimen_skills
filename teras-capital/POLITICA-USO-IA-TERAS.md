# Política de Uso de IA — TERAS Capital

**Versión**: 1.0
**Fecha**: Febrero 2026
**Clasificación**: TERAS-Internal
**Owner**: Equipo TERAS Capital

---

## 1. Principio Rector

> **Cualquier interacción con un sistema IA en contexto TERAS debe producir output indistinguible de lo que produciría el mejor profesional del equipo con tiempo ilimitado.**

Las skills son el mecanismo que garantiza este estándar. No son opcionales.

---

## 2. Arquitectura de la Capa Cognitiva

### 2.1 Capas

| Capa | Propósito | Skills | Activación |
|------|-----------|--------|------------|
| **L0: Fundación** | Identidad, modelo económico, tono, marca | operar-como-teras, aplicar-guardrails-teras, desarrollar-ux-teras | **Siempre activa** |
| **L1: Comportamiento** | Rigor analítico, challenge, validación | challenge-cognitivo-teras, validar-analisis-teras | **Siempre activa** en outputs analíticos |
| **L2: Roles** | Alter egos funcionales con sub-agentes | clo-superpoder, coo-superpoder, cfo-superpoder, cio-superpoder, head-ir-superpoder | Por contexto funcional |
| **L3a: Tareas** | Generadores de entregables end-to-end | generar-presentacion, generar-one-pager, generar-board-memo, generar-email, generar-exec-summary | Por tipo de entregable |
| **L3b: Escenarios** | Contextos situacionales con actores | escenario-steerco-tuca, escenario-consejo-mps, escenario-templus, preparar-reunion-clave | Por situación de negocio |
| **L3c: Procesos** | Workflows de negocio (pipeline, M&A, IC) | negociar-mandatos, negociar-ma, preparar-ic | Por fase de deal |

### 2.2 Herencia

Las capas superiores heredan las inferiores. Esto significa:
- Todo output respeta L0 (identidad + guardrails + marca)
- Todo análisis pasa por L1 (challenge + validación)
- Los roles, tareas y escenarios añaden contexto específico sobre esta base

---

## 3. Reglas de Uso Obligatorio

### 3.1 Siempre activar L0

Antes de cualquier trabajo en IA, cargar operar-como-teras como contexto base.

| Plataforma | Cómo activar L0 |
|-----------|-----------------|
| **Claude (Cowork/Code/Antigravity)** | Tener SKILL.md en workspace o .skills/ |
| **Gemini Gems** | Usar el Gem con L0 en instrucciones |
| **NotebookLM** | Incluir operar-como-teras.md como fuente |
| **Codex** | Referencia en AGENTS.md del proyecto |
| **n8n** | System prompt del nodo AI Agent |

### 3.2 Seleccionar skill por tarea

No hacer prompts genéricos. Identificar qué skill cubre tu necesidad y activarla. Si no existe skill para tu caso, escalar para crearla.

### 3.3 No bypassear el challenge

Si el sistema te hace push-back, es una feature, no un bug. Responder con datos, no con "hazlo como te digo". El challenge existe para proteger la calidad de TERAS.

**Excepción**: Si hay urgencia genuina, usar `[CHALLENGE: OFF]` pero documentar por qué.

### 3.4 Validar antes de enviar

Todo output que salga de TERAS al exterior debe pasar el lint de guardrails. Sin excepciones. Esto incluye emails, presentaciones, memos, one-pagers.

### 3.5 Clasificar confidencialidad

Usar `[SENSITIVITY: nivel]` en cada prompt que involucre información de deals, sponsors o términos económicos.

| Nivel | Uso |
|-------|-----|
| Public | Web y terceros sin NDA |
| Sponsor-confidential | Default para todo output a sponsors |
| TERAS-internal | Solo dentro del equipo |
| IC-LP-Adjacent | Máxima sobriedad, factual puro |

### 3.6 Documentar el contexto

Si usas un escenario, indicar siempre `[AUDIENCE:]` y `[SENSITIVITY:]` para calibrar el output.

---

## 4. Matriz de Decisión: Qué Skill Usar

| Si necesitas... | Skill principal | Complementar con |
|-----------------|----------------|------------------|
| Preparar un Steerco de un activo | escenario-steerco-[activo] | generar-presentacion + COO |
| Redactar un one-pager para un sponsor | generar-one-pager-teras | negociar-mandatos + guardrails |
| Preparar un Consejo de Administración | escenario-consejo-mps | generar-board-memo + CLO |
| Negociar un SPA/SHA | negociar-ma-teras | CLO superpoder + guardrails |
| Preparar un IC | preparar-ic-teras | CIO superpoder + challenge |
| Revisar un modelo financiero | cfo-superpoder-teras | validar-analisis + challenge |
| Reunión con persona clave nueva | preparar-reunion-clave | negociar-mandatos (si es sponsor) |
| Construir tesis de inversión | cio-superpoder-teras | challenge + validar-analisis |
| Reportar a LPs | head-ir-superpoder-teras | CFO + guardrails |
| Crear material de marca | desarrollar-ux-teras | guardrails + tarea específica |
| Plan de 100 días para activo | coo-superpoder-teras | challenge + escenario del activo |
| Email a sponsor | generar-email-teras | negociar-mandatos + guardrails |
| Resumen ejecutivo de documento | generar-exec-summary-teras | validar-analisis |

---

## 5. Plataformas Aprobadas y Configuración

### 5.1 Claude (Cowork / Code / Antigravity)

**Configuración**: Skills como SKILL.md en workspace folder.
**Ventajas**: Contexto completo, sub-agentes, filesystem, ejecución.
**Uso recomendado**: Trabajo principal de análisis, generación de documentos, tareas complejas.

### 5.2 Gemini Gems

**Configuración**: Pegar contenido del .md en instrucciones del Gem.
**Limitación**: ~8K tokens por Gem. Usar versiones compact.
**Uso recomendado**: Consultas rápidas, brainstorming, cuando Claude no disponible.
**Setup**: Crear 1 Gem por combinación frecuente (ej: "TERAS Analyst" = L0 + L1 + CIO compact).

### 5.3 NotebookLM

**Configuración**: Subir .md como fuentes del notebook.
**Ventajas**: Multi-fuente, audio overview, ideal para investigación.
**Uso recomendado**: Research, síntesis de múltiples documentos, preparación de posiciones.
**Setup**: Notebook base con L0 + L1 como fuentes permanentes. Añadir skills específicas por proyecto.

### 5.4 Codex (OpenAI)

**Configuración**: .md en repo, referenciado en AGENTS.md.
**Limitación**: Contexto más limitado. Usar compact versions.
**Uso recomendado**: Coding, automatización, cuando Claude/Gemini no disponibles.

### 5.5 n8n / Agentes Automatizados

**Configuración**: System prompt del nodo AI Agent.
**Uso recomendado**: Workflows automáticos (reporting, alertas, procesamiento).
**Setup**: 1 nodo por skill, routing por tipo de tarea.

---

## 6. Gobernanza de las Skills

### 6.1 Ownership

Cada skill tiene un owner del equipo TERAS responsable de:
- Mantener el contenido actualizado
- Incorporar feedback del equipo
- Revisar trimestralmente contra la realidad operativa

### 6.2 Versionado

- Versión semántica: v1.0, v1.1 (minor), v2.0 (major)
- Cambios significativos (nueva sección, nuevo anti-patrón) suben major
- Correcciones y mejoras menores suben minor
- Cada cambio se documenta en commit message

### 6.3 Repositorio Único

Todas las skills viven en un repositorio Git central:
- Rama `main` = versión productiva
- PRs para cambios significativos
- Las versiones compact se generan automáticamente (o se mantienen manualmente)

### 6.4 Review Trimestral

Cada trimestre:
- Revisar skills contra la realidad operativa
- Añadir escenarios nuevos si hay activos nuevos
- Actualizar parámetros sectoriales
- Incorporar lecciones aprendidas
- Actualizar benchmarks y templates

### 6.5 Feedback Loop

- Cualquier miembro puede proponer mejoras
- El owner evalúa e integra
- Los bugs/fallos de las skills se documentan inmediatamente

---

## 7. Onboarding de Nuevos Miembros

Todo nuevo miembro del equipo recibe:

1. **Sesión de 1 hora** sobre la capa cognitiva: qué son las skills, cómo funcionan, por qué importan
2. **Acceso al repositorio** con todas las skills
3. **Setup de plataformas**: Claude workspace, Gems precargados, NotebookLM base
4. **Ejercicio práctico**: Producir un email, un one-pager y un exec summary usando las skills
5. **Buddy**: Un miembro senior asignado para las primeras 2 semanas de uso

---

## 8. Anti-Patrones de Uso

| ❌ No hacer | ✅ Hacer |
|-------------|---------|
| Usar IA sin cargar L0 | Siempre activar contexto TERAS primero |
| Hacer prompts genéricos sin skill | Seleccionar la skill correcta |
| Ignorar el challenge del sistema | Responder al challenge con datos |
| Enviar output sin lint | Ejecutar guardrails antes de toda entrega |
| Copiar output sin revisar | Revisar, matizar, personalizar |
| Usar plataforma no configurada | Configurar la plataforma con las skills antes de usarla |
| Inventar cifras o claims | Solo datos proporcionados o marcados como supuesto |
| Compartir prompts con info sensible en plataformas públicas | Verificar confidencialidad y plataforma |

---

## 9. Seguridad y Confidencialidad

- **Nunca** incluir información IC-LP-Adjacent en plataformas sin control de acceso
- **Nunca** compartir prompts que contengan nombres de deals, sponsors o términos económicos en herramientas públicas
- **Siempre** verificar que la plataforma cumple requisitos de confidencialidad antes de pegar contenido sensible
- Las skills en sí mismas son TERAS-Internal
- Los outputs generados heredan la clasificación del input más sensible

---

## 10. Métricas de Adopción

| Métrica | Target | Frecuencia de medición |
|---------|--------|----------------------|
| % outputs que usan skills | >90% | Trimestral (auto-report) |
| % equipo con plataformas configuradas | 100% | Mensual |
| Skills activas vs plan | >85% | Trimestral |
| NPS interno de las skills | >7/10 | Semestral |
| Tiempo medio de producción de entregables | Reducción >30% vs pre-skills | Semestral |
| Incidentes de guardrails (outputs que fallan lint) | Tendencia decreciente | Trimestral |
