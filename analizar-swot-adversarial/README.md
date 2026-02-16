# 🎯 Skill: Análisis SWOT Adversarial para Litigación

**El Abogado del Diablo** - Análisis despiadado de escritos procesales.

## Instalación

Esta skill forma parte del ecosistema de skills de Antigravity. Para activarla:

```bash
# La skill está lista para usar - no requiere instalación adicional
# Asegúrate de tener los requisitos para el script logic.py:
pip install pymupdf python-docx
```

## Uso Rápido

### Como Skill de Agente

Menciona la skill al agente:

```
@analizar-swot-adversarial

Analiza la demanda adjunta y genera matriz DAFO estratégica.
```

### Como Script Python

```python
from scripts.logic import execute_skill

result = execute_skill(
    file_path="demanda.pdf",
    temperature=0.2
)

print(result['executive_summary'])
print(result['swot_matrix'])
```

## Estructura

```
analizar-swot-adversarial/
├── SKILL.md                    # Definición principal
├── README.md                   # Este archivo
├── resources/
│   ├── skill.yaml              # Manifiesto de seguridad
│   └── system_prompt.md        # Prompt adversarial para LLM
├── scripts/
│   └── logic.py                # Lógica de ejecución
└── examples/
    └── sample_output.json      # Ejemplo de salida
```

## Capacidades

| Detección | Descripción |
|-----------|-------------|
| **Falacias Lógicas** | Ad Hominem, Non Sequitur, Petición de Principio, Hombre de Paja |
| **Déficit Probatorio** | Afirmaciones sin prueba documental |
| **Contradicciones** | Inconsistencias entre párrafos |

## Output

Genera matriz DAFO con:
- **W (Weaknesses)**: Debilidades argumentales del contrario
- **O (Opportunities)**: Huecos probatorios para impugnar
- **T (Threats)**: Puntos de riesgo para nuestro caso
- **S (Strengths)**: Fortalezas del contrario (defensa difícil)

## Seguridad

Diseñada para ejecución 100% local:
- Sin conexión a Internet
- Inferencia en modelo local (Llama/Mixtral)
- Datos solo en RAM del Enclave

---

**Autor**: Legal Engineering Dept. | **Versión**: 1.0.2
