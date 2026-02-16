---
name: presentaciones-ejecutivas-inmobiliario
description: "Generar presentaciones/teasers ejecutivos para oportunidades de inversión inmobiliaria (oficinas, living, logístico, hotelero). Úsalo al crear decks tipo investment memo o executive summary en PPT/PDF/Canva, con narrativa de inversión, KPIs, market update y comparables. Por defecto aplica estilo TERAS (Black/Red/Grey) y la estructura compacta de 5 slides."
---

# Presentaciones Ejecutivas Inmobiliario

## Overview
Crear de forma consistente teasers ejecutivos de inversión inmobiliaria siguiendo la estructura compacta de 5 slides (portada, resumen ejecutivo, market update, comparable, contacto). Incluye narrativa, tablas de KPIs, gráficos sencillos y disclaimer listo para imprimir en PDF o presentar en PPT/Canva. **Modo TERAS**: aplica paleta Black/Red/Grey y tipografías Matter / Messina Serif (fallback Verdana/Georgia) según Brand Manual v1.0.

## Quick start
- Recolecta datos clave con `references/datos-requeridos.md`.
- Usa el flujo `references/outline.md` (ES) o `references/outline-en.md` (EN) y el asset visual `assets/modelo-bolivia.pdf` como guía de look & feel.
- Genera deck editable con `scripts/build_template.py` (crea `assets/teaser-template.pptx`) y reemplaza placeholders; exporta PDF. La plantilla sale en paleta TERAS y bordes 0.

## Workflow
### 1) Insumos
- Completa checklist de deal, CapEx, financiación, leasing y mercado (`references/datos-requeridos.md`).
- Si faltan datos críticos, marca `[pendiente]` y suaviza claims ("preliminary", "subject to DD").

### 2) Storyboard
- Sigue el orden y microcopy de `references/outline.md`.
- Mantén bullets cortos (1–2 líneas) y tabla de highlights en cada proyecto.
- Añade extensiones opcionales solo si agregan decisión (capex/timeline/capital stack/ESG/sensibilidades).

### 3) Producción
- Formato preferido: PPTX o Canva; exporta PDF final.
- Gráficos: si no hay datos, coloca placeholders etiquetados con la métrica y fuente esperada.
- Mapas: resalta 2–3 hitos y ancla el solar; usa los colores base.
- Traducción: duplicar deck si se requieren versiones ES/EN.

### 4) QA
- Consistencia numérica: unidades (€/psm mes, €/psm A/G, %), sumas y yields.
- Etiquetas claras en tablas y gráficos; cita fuente y año.
- Disclaimer legal en la última slide; confirma confidencialidad en portada y pie.
- Exporta y revisa PDF renderizado (fuentes, cortes, superposiciones).

## Estilo visual (Brand TERAS)
- Paleta obligatoria: Black `#000000`, Red `#EA3348`, Grey `#C6C9CC` (fondos claros). Secundarios: greys `#6F7173`, `#F7F7F7`, `#EBEBEB`, `#D5D7D1`. No usar otros colores.
- Tipografía: Titulares **Matter** (Regular, fallback Verdana); cuerpo **Messina Serif** (Regular, fallback Georgia). No usar bold/ligth; jerarquía solo con tamaño.
- Bordes: radio 0; estética técnica y austera.
- Gráficos: líneas finas, acento Red para series clave, textos en Black/Muted. Fondos blancos/grises; evitar sombras y degradados.
- Si el proyecto **no** es TERAS y requiere otro brand, documenta la paleta solicitada antes de cambiar colores.

## Recursos incluidos
- `references/outline.md` y `references/outline-en.md`: storyboard slide a slide (ES/EN) con campos a rellenar y variantes opcionales.
- `references/datos-requeridos.md`: checklist de inputs, formato de la tabla de highlights y guías de mercado.
- `assets/modelo-bolivia.pdf`: teaser de referencia para look & feel y redacción.
- `scripts/build_template.py`: genera un PPTX base en `assets/teaser-template.pptx` (5 slides).
- `scripts/generate_charts.py`: exporta gráficos de ejemplo a `assets/charts/` para usarlos como placeholders o base.

## Entregables esperados
- Deck editable (PPTX/Canva/Google Slides) y PDF final.
- Slide count sugerido: 5 básicas; añadir extensiones solo si aportan decisión.
- Ficheros nombrados como `YYYYMMDD-proyecto-teaser-v1.[pptx|pdf]`.
