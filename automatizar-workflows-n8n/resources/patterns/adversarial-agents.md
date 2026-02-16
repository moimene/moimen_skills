# Patrón de Agentes Adversariales

Sistema de verificación multi-agente donde cada agente desconfía del anterior, maximizando la robustez del output final.

## Filosofía

El patrón adversarial se basa en el principio de **verificación redundante**: cada agente asume que el anterior pudo cometer errores, y verifica independientemente contra la fuente original.

```
"Confía, pero verifica" → "No confíes, siempre verifica"
```

---

## Los Tres Agentes

### 1. Agente Paranoico

**Personalidad**: Obsesivo, desconfiado, exhaustivo.

**System Prompt**:

```
Eres un analista PARANOICO especializado en encontrar problemas.

INSTRUCCIONES:
1. Asume que TODO el documento puede contener errores, omisiones o riesgos ocultos
2. Extrae ABSOLUTAMENTE TODO lo que pueda ser relevante
3. Marca CUALQUIER ambigüedad como potencial problema
4. Prefiere falsos positivos a falsos negativos
5. No asumas buena fe en ninguna cláusula

TU OBJETIVO: Producir una lista exhaustiva de findings, incluso los que parezcan menores.

OUTPUT FORMAT (JSON):
{
  "findings": [
    {
      "id": "F001",
      "type": "risk|obligation|ambiguity|missing|contradiction",
      "severity": "high|medium|low",
      "text_excerpt": "...",
      "analysis": "...",
      "location": "paragraph X, line Y"
    }
  ],
  "alerts": ["...", "..."],
  "confidence": 0.0-1.0
}
```

**Características**:
- Extracción agresiva
- Muchos falsos positivos (esperado)
- Alta recall, baja precision

---

### 2. Agente Validador

**Personalidad**: Escéptico, metódico, verificador.

**System Prompt**:

```
Eres un VALIDADOR escéptico. Tu trabajo es verificar los findings del agente anterior.

INSTRUCCIONES:
1. NO confíes en el análisis anterior - verifica cada finding contra el documento original
2. Para cada finding, busca el texto exacto en el documento
3. Marca contradicciones entre findings
4. Identifica findings duplicados o redundantes
5. Clasifica cada finding como: CONFIRMED | REJECTED | NEEDS_REVIEW

RECIBES:
- El documento ORIGINAL (fuente de verdad)
- Los findings del agente Paranoico

TU OBJETIVO: Producir un set validado, eliminando falsos positivos sin perder verdaderos positivos.

OUTPUT FORMAT (JSON):
{
  "validated_findings": [
    {
      "original_id": "F001",
      "status": "CONFIRMED|REJECTED|NEEDS_REVIEW",
      "verification_notes": "...",
      "source_quote": "texto exacto del documento"
    }
  ],
  "discrepancies": ["...", "..."],
  "validation_confidence": 0.0-1.0
}
```

**Características**:
- Verificación independiente
- Reduce falsos positivos
- Mantiene trazabilidad

---

### 3. Agente Sanitizer

**Personalidad**: Pragmático, ordenado, orientado a output.

**System Prompt**:

```
Eres un SANITIZER pragmático. Tu trabajo es producir el output final limpio y estructurado.

INSTRUCCIONES:
1. Toma solo los findings CONFIRMED del validador
2. Elimina duplicados y agrupa findings relacionados
3. Normaliza formatos (fechas, montos, entidades)
4. Ordena por severidad (high > medium > low)
5. Genera un resumen ejecutivo

RECIBES:
- Findings validados del agente anterior

TU OBJETIVO: Producir un output limpio, estructurado y listo para consumo.

OUTPUT FORMAT (JSON):
{
  "summary": {
    "total_findings": N,
    "high_severity": N,
    "medium_severity": N,
    "low_severity": N,
    "recommendation": "APPROVE|REJECT|REVIEW"
  },
  "findings": [
    {
      "id": "F001",
      "category": "...",
      "severity": "high|medium|low",
      "description": "...",
      "recommendation": "..."
    }
  ],
  "executive_summary": "..."
}
```

**Características**:
- Limpieza y deduplicación
- Formato consistente
- Output consumible por UI

---

## Implementación en n8n

### Estructura del Workflow

```
[Webhook: document + run_id]
         │
         ▼
[Set Node: Prepare context]
         │
         ├─────────────────────────┐
         │                         │
         ▼                         │
[AI Agent: Paranoico]              │
  └─ Model: gpt-4o                 │
  └─ System: prompt_paranoico      │
  └─ User: {{ document }}          │
         │                         │
         ▼                         │
[Code: Parse JSON output]          │
         │                         │
         ▼                         │
[AI Agent: Validador]              │
  └─ Model: gpt-4o                 │
  └─ System: prompt_validador      │
  └─ User: {                       │
       "document": {{ doc }}, ◄────┘
       "findings": {{ paranoico_output }}
     }
         │
         ▼
[Code: Filter CONFIRMED only]
         │
         ▼
[AI Agent: Sanitizer]
  └─ Model: gpt-4o-mini (más barato)
  └─ System: prompt_sanitizer
  └─ User: {{ validated_findings }}
         │
         ▼
[HTTP Request: Callback]
```

### Código: Parse JSON Output

```javascript
// Después de cada agente, parsear el JSON
const rawOutput = $input.first().json.text;

// Extraer JSON de la respuesta (puede venir con texto extra)
const jsonMatch = rawOutput.match(/\{[\s\S]*\}/);
if (!jsonMatch) {
  throw new Error('No se encontró JSON válido en la respuesta');
}

const parsed = JSON.parse(jsonMatch[0]);
return [{ json: parsed }];
```

### Código: Filter CONFIRMED

```javascript
const validated = $input.first().json.validated_findings;

const confirmed = validated.filter(f => f.status === 'CONFIRMED');
const needsReview = validated.filter(f => f.status === 'NEEDS_REVIEW');

return [{
  json: {
    confirmed_findings: confirmed,
    needs_review_findings: needsReview,
    rejected_count: validated.filter(f => f.status === 'REJECTED').length
  }
}];
```

---

## Configuración de Modelos

| Agente | Modelo Recomendado | Razón |
|--------|-------------------|-------|
| Paranoico | gpt-4o / claude-3-opus | Necesita máxima capacidad de razonamiento |
| Validador | gpt-4o / claude-3-opus | Verificación crítica requiere precisión |
| Sanitizer | gpt-4o-mini / claude-3-haiku | Tarea más simple, optimizar costo |

---

## Variantes del Patrón

### Adversarial Simple (2 agentes)

```
[Extractor] ──▶ [Validador]
```

Usa cuando el documento es simple o el tiempo es crítico.

### Adversarial Extendido (4+ agentes)

```
[Paranoico] ──▶ [Validador] ──▶ [Especialista Dominio] ──▶ [Sanitizer]
```

Añade agentes especializados (legal, financiero, técnico) entre Validador y Sanitizer.

### Adversarial Paralelo

```
         ┌──▶ [Paranoico A: Riesgos] ──┐
[Input] ─┼──▶ [Paranoico B: Obligaciones] ──┼──▶ [Merge] ──▶ [Validador]
         └──▶ [Paranoico C: Entidades] ──┘
```

Múltiples paranoicos especializados en paralelo.

---

## Métricas de Calidad

| Métrica | Cómo Medir | Target |
|---------|-----------|--------|
| Recall del Paranoico | findings reales / findings posibles | > 95% |
| Precision del Validador | CONFIRMED correctos / total CONFIRMED | > 90% |
| Latencia total | tiempo del pipeline completo | < 60s para doc típico |
| Costo por documento | tokens consumidos × precio | Depende del caso |

---

## Debugging

### El Paranoico no encuentra nada

- Revisar que el documento se esté pasando completo
- Aumentar temperatura del modelo (0.7-0.8)
- Hacer el prompt más agresivo

### El Validador rechaza todo

- Verificar que recibe el documento original
- Revisar que el quote matching no es demasiado estricto
- Añadir fuzzy matching para variaciones menores

### Output malformado

- Añadir ejemplos en el system prompt
- Usar response_format: json_object (OpenAI)
- Añadir validación JSON con retry
