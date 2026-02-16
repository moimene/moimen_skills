---
description: Cómo usar el sistema de auto-carga de skills en un proyecto
---

# Auto-Cargar Skills en un Proyecto

Este workflow detecta automáticamente el tipo de proyecto y sugiere las skills más relevantes.

---

## Requisitos

1. **Catálogo global instalado** en `~/.agent/skills/`
2. **Skills locales** en `/Users/moisesmenendez/Dropbox/Codigo/agent/skills/`
3. **Script de auto-detección** en `.agent/auto-load-skills.sh`

---

## Uso del Script de Auto-Detección

Desde el directorio raíz de tu proyecto, ejecuta:

```bash
/Users/moisesmenendez/Dropbox/Codigo/agent/skills/.agent/auto-load-skills.sh .
```

El script:
1. Analiza los archivos del proyecto (package.json, tsconfig.json, etc.)
2. Detecta el tipo de proyecto (React, Python, n8n, Supabase, LegalTech, etc.)
3. Sugiere skills relevantes del catálogo global y local
4. Genera comandos de symlink listos para copiar/pegar

---

## Tipos de Proyecto Detectados

| Tipo | Archivos Detectores | Skills Sugeridas |
|------|---------------------|------------------|
| **React/Next.js** | `package.json` con "react" o "next" | react-best-practices, react-patterns, nextjs-best-practices |
| **TypeScript** | `tsconfig.json` | typescript-expert, typescript-patterns |
| **Python** | `pyproject.toml`, `requirements.txt` | python-patterns, async-python-patterns |
| **Supabase** | `supabase/` directory | supabase-development, database-design |
| **n8n/Workflows** | `*.workflow.json`, `W*_*.json` | workflow-automation + automatizar-workflows-n8n (local) |
| **DevOps** | `Dockerfile`, `.github/workflows` | docker-expert, github-actions |
| **LegalTech** | `*guardian*`, `*contract*` | desarrollar-ux-garrigues + orquestar-agentes (local) |
| **TERAS** | Contiene "teras" o "TERAS" | desarrollar-ux-teras (local) |
| **AI/Agents** | `langchain`, `openai` en deps | prompt-engineer, rag-engineer, orquestar-agentes |

---

## Esenciales (Siempre Incluidas)

Estas skills se recomiendan para TODOS los proyectos:

- `concise-planning` - Siempre empieza con un plan
- `lint-and-validate` - Mantén tu código limpio
- `git-pushing` - Guarda tu trabajo de forma segura
- `kaizen` - Mejora continua
- `systematic-debugging` - Depuración como un pro

---

## Ejemplo Completo

```bash
# 1. Navega a tu proyecto
cd ~/Proyectos/mi-app-react

# 2. Ejecuta el detector
/Users/moisesmenendez/Dropbox/Codigo/agent/skills/.agent/auto-load-skills.sh .

# Output esperado:
# 📦 Tipos de proyecto detectados:
#    • React/Next.js
#    • TypeScript
#    • Supabase
#
# ✅ Skills recomendadas:
# 📌 Global (desde ~/.agent/skills/skills/):
#    ✓ react-best-practices
#    ✓ typescript-expert
#    ✓ supabase-development
#    ...

# 3. Crea la carpeta de skills en el proyecto
mkdir -p .agent/skills

# 4. Copia los comandos de symlink sugeridos
ln -s ~/.agent/skills/skills/react-best-practices .agent/skills/
ln -s ~/.agent/skills/skills/typescript-expert .agent/skills/
# ...etc
```

---

## Configuración Avanzada

El mapeo de proyectos a skills está definido en:

```
/Users/moisesmenendez/Dropbox/Codigo/agent/skills/.agent/project-skills.yaml
```

Puedes editar este archivo para añadir nuevos tipos de proyecto o modificar las skills asociadas.

---

## Skills Disponibles

| Fuente | Cantidad | Ubicación |
|--------|----------|-----------|
| **Catálogo Global** | 621 | `~/.agent/skills/skills/` |
| **Colección Local** | ~15 | `/Users/moisesmenendez/Dropbox/Codigo/agent/skills/` |

Ver catálogo completo: `~/.agent/skills/CATALOG.md`
