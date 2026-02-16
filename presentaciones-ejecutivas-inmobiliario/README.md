# Presentaciones Ejecutivas Inmobiliario (estructura 5 slides, estilo TERAS)

Guía completa para usar esta skill en agentes (Codex, Claude Code, otros) y en chatbots estándar (ChatGPT, Gemini, etc.) maximizando el contexto sin depender de orquestación agéntica.

## 1) Qué hace
Genera teasers ejecutivos de oportunidades inmobiliarias (oficinas, living, logístico, hotelero) en 5–8 diapositivas: portada, resumen ejecutivo, market update, comparable, contacto/disclaimer, con tabla de highlights, gráficos y look & feel **TERAS** (Black/Red/Grey, tipografías Matter / Messina Serif). Mantiene la estructura compacta inspirada en Bolivia, pero con la identidad visual TERAS.

## 2) Contenido del skill
- `SKILL.md`: instrucciones operativas, flujo y estilo visual.
- `agents/openai.yaml`: metadatos UI (Codex/OpenAI chips).
- `references/outline.md` (ES) y `references/outline-en.md` (EN): storyboard slide a slide.
- `references/datos-requeridos.md`: checklist de insumos y formato de la tabla de highlights.
- `assets/modelo-bolivia.pdf`: teaser de referencia para narrativa/estructura.
- `assets/teaser-template.pptx`: plantilla PPTX base de 5 slides con placeholders en paleta TERAS (bordes 0, Matter/Messina fallback Verdana/Georgia).
- `assets/charts/sample_takeup_vacancy.png`, `assets/charts/sample_absorption_grade.png`: gráficos de ejemplo/placeholder.
- `scripts/build_template.py`: genera/actualiza la plantilla PPTX.
- `scripts/generate_charts.py`: crea gráficos PNG rápidos para placeholders.

## 3) Requisitos
- Python 3.9+ con `python-pptx` y `matplotlib`:
  ```bash
  python3 -m pip install --user python-pptx matplotlib
  ```
- Opcional para inspección de PDFs: `poppler` (`pdftoppm`).

## 4) Uso en agentes (Codex, Claude Code, etc.)
1) Coloca esta carpeta completa en tu workspace de skills (p.ej. `~/…/skills/presentaciones-ejecutivas-inmobiliario`).
2) Carga contexto mínimo:
   - Siempre: `SKILL.md`, `references/outline*.md`, `references/datos-requeridos.md`.
   - Visual: `assets/modelo-bolivia.pdf` (renderizar o revisar) y/o `assets/teaser-template.pptx`.
3) Pide al agente seguir `SKILL.md` y el outline elegido (ES/EN). Ejemplo prompt corto:
   ```
   Usa el skill presentaciones-ejecutivas-inmobiliario. Sigue outline-es, respeta estilo TERAS (Black/Red/Grey, tipografías Matter/Messina, bordes 0), y llena con estos datos: [inputs]. Actualiza la plantilla PPTX y exporta PDF.
   ```
4) Generar plantilla o refrescarla:
   ```bash
   python3 scripts/build_template.py
   ```
   Salida: `assets/teaser-template.pptx`.
5) Gráficos placeholder:
   ```bash
   python3 scripts/generate_charts.py
   ```
   Salida: PNGs en `assets/charts/`. Reemplaza con datos reales si los tienes.
6) QA: pedir al agente que renderice o revise el PDF final (alineación, cortes, fuentes).

### Casos rápidos por plataforma
- **Claude Code**: Adjunta `SKILL.md`, `outline*.md`, `datos-requeridos.md` y `teaser-template.pptx` al thread. Prompt: “Sigue SKILL, usa outline-es, paleta TERAS, edita el PPTX adjunto con estos datos [inputs] y dame PDF + changelog”. Permite ejecución de `python3 scripts/build_template.py` si quieres regenerar desde cero.
- **Codex (desktop/CLI)**: Añade la carpeta a tu ruta de skills, referencia paths absolutos y ejecuta los scripts directamente. Ejemplo comando: `python3 /ruta/skills/presentaciones-ejecutivas-inmobiliario/scripts/build_template.py`.
- **Flujo n8n**: Crea un workflow con nodos: (1) HTTP/Webhook recibe payload del deal; (2) Code node Python/JS que escribe `inputs.json`; (3) Command node ejecuta `python3 scripts/build_template.py`; (4) Otro Code node rellena placeholders en el PPTX (usando `python-pptx`) con los datos del payload; (5) Command node exporta a PDF (LibreOffice headless o `unoconv`); (6) Email/Slack node envía el PDF. Monta el repositorio en el contenedor n8n y usa rutas absolutas a `scripts/` y `assets/`.

### Notas específicas por agente
- **Codex (CLI / desktop)**: menciona la ruta absoluta al skill y ejecuta los scripts directamente. Si usas automations, añade este folder como CWD.
- **Claude Code / Cursor / VSCode Agents**: adjunta los archivos clave al thread y autoriza ejecución de los scripts; indica que `teaser-template.pptx` es el archivo a editar.
- **Otros agentes con funciones**: referencia explícita a `SKILL.md` en el mensaje del sistema o primeras instrucciones para asegurar que se cargue.

## 5) Uso en chatbots estándar (ChatGPT, Gemini, etc.) sin agente
Objetivo: dar suficiente contexto sin sobrecargar tokens.

1) Sube/pega solo lo necesario:
   - `references/outline.md` (o EN) y `references/datos-requeridos.md` completos.
   - Un resumen de 5–8 líneas de `SKILL.md` (o pega la sección “Quick start” y “Workflow”).
   - Si el chatbot admite archivos, adjunta `assets/teaser-template.pptx` para que entienda estructura/placeholder.
2) Prompt sugerido (ajusta idioma):
   ```
   Actúa como diseñador TERAS. Usa este outline [pega outline] y esta checklist [pega checklist]. Rellena la plantilla adjunta manteniendo paleta Black/Red/Grey, tipografías Matter/Messina (fallback Verdana/Georgia), bordes 0. Datos del deal: [datos]. Devuélveme: (1) bullets finales por slide, (2) tabla de highlights, (3) texto del disclaimer, (4) instrucciones para actualizar el PPTX adjunto.
   ```
3) Si no puedes adjuntar el PPTX, pide salida en Markdown estructurado por slide + tabla de highlights; luego copia/pega manualmente en tu presentación.
4) Para minimizar tokens:
   - Evita pegar el PDF completo; describe visualmente (colores, jerarquía).
   - Usa siglas consistentes: ERV, LTC, IRR, MOIC, Exit yield.
   - Pide respuestas concisas: 5–7 bullets máx por slide.

## 6) Flujo operativo recomendado
1) Recolecta insumos con `references/datos-requeridos.md` (marca `[pendiente]` lo que falte).  
2) Genera/abre `assets/teaser-template.pptx`.  
3) Completa slides siguiendo `references/outline.md` u `outline-en.md`; coloca gráficos de `assets/charts/` mientras llegan datos reales.  
4) Si es TERAS, NO cambies la paleta ni las tipografías; si es otro brand, documenta paleta/tipografía requerida antes de modificar.  
5) Exporta PDF y realiza QA visual (espaciado, etiquetas, fuentes, disclaimer).  
6) Si necesitas variantes (ES/EN), duplica slides y traduce microcopy manteniendo métricas intactas.

## 7) Integración con el repo moimene/teras_skills
- Copia esta carpeta tal cual dentro del repo (`skills/presentaciones-ejecutivas-inmobiliario/`).
- Añade una entrada en el índice del repo (si existe) apuntando a `SKILL.md`.
- Si usas pipelines CI para validación, ejecuta `scripts/quick_validate.py <path>` del skill-creator.

## 8) Comandos rápidos
- Validar estructura (si tienes skill-creator en tu entorno):  
  `python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py presentaciones-ejecutivas-inmobiliario`
- Regenerar plantilla PPTX:  
  `python3 presentaciones-ejecutivas-inmobiliario/scripts/build_template.py`
- Generar gráficos placeholder:  
  `python3 presentaciones-ejecutivas-inmobiliario/scripts/generate_charts.py`

## 9) Buenas prácticas de prompting
- Siempre indica idioma de salida (ES/EN) y límite de bullets por slide.
- Especifica si métricas son levered/pre-promote y unidades (€/psm mes, €/psm A/G, %).
- Pide citar fuente y año en gráficos; si no hay datos, que mantenga placeholders etiquetados.
- Solicita tono ejecutivo, frases cortas y cifras redondas (1 decimal máx para yields).

## 10) Licencia / disclaimers
- Usa el disclaimer del sponsor en la última slide; el texto de ejemplo está en `assets/modelo-bolivia.pdf` y en `SKILL.md`.  
- Verifica confidencialidad en portada y pie antes de distribuir.
