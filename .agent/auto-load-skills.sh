#!/bin/bash
# =============================================================================
# auto-load-skills.sh
# Detecta el tipo de proyecto y sugiere skills recomendadas
# =============================================================================

set -e

PROJECT_DIR="${1:-.}"
GLOBAL_SKILLS="$HOME/.agent/skills/skills"
LOCAL_SKILLS="/Users/moisesmenendez/Dropbox/Codigo/agent/skills"

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔍 Analizando proyecto en:${NC} $PROJECT_DIR"
echo ""

# Arrays para skills detectadas
declare -a DETECTED_TYPES
declare -a GLOBAL_SKILLS_LIST
declare -a LOCAL_SKILLS_LIST

# === FUNCIONES DE DETECCIÓN ===

check_file_exists() {
  [[ -f "$PROJECT_DIR/$1" ]]
}

check_dir_exists() {
  [[ -d "$PROJECT_DIR/$1" ]]
}

check_file_contains() {
  local file="$1"
  local pattern="$2"
  [[ -f "$PROJECT_DIR/$file" ]] && grep -q "$pattern" "$PROJECT_DIR/$file" 2>/dev/null
}

check_any_file_pattern() {
  ls "$PROJECT_DIR"/$1 1>/dev/null 2>&1
}

# === DETECCIÓN DE TIPOS ===

# Essentials (siempre)
GLOBAL_SKILLS_LIST+=("concise-planning" "lint-and-validate" "git-pushing" "kaizen" "systematic-debugging")

# React/Next.js
if check_file_exists "package.json"; then
  if check_file_contains "package.json" '"react"' || check_file_contains "package.json" '"next"'; then
    DETECTED_TYPES+=("React/Next.js")
    GLOBAL_SKILLS_LIST+=("react-best-practices" "react-patterns" "nextjs-best-practices" "typescript-expert" "tailwind-patterns" "frontend-design")
    LOCAL_SKILLS_LIST+=("aplicar-react-best-practices")
  fi
fi

# Python
if check_file_exists "pyproject.toml" || check_file_exists "requirements.txt" || check_file_exists "setup.py"; then
  DETECTED_TYPES+=("Python")
  GLOBAL_SKILLS_LIST+=("python-patterns" "async-python-patterns" "python-best-practices")
fi

# Supabase
if check_dir_exists "supabase" || check_file_exists "supabase/config.toml"; then
  DETECTED_TYPES+=("Supabase")
  GLOBAL_SKILLS_LIST+=("supabase-development" "database-design" "api-patterns")
fi

# n8n/Workflows
if check_any_file_pattern "*.workflow.json" || check_any_file_pattern "W*_*.json" || check_dir_exists "workflows"; then
  DETECTED_TYPES+=("n8n/Workflows")
  GLOBAL_SKILLS_LIST+=("workflow-automation")
  LOCAL_SKILLS_LIST+=("automatizar-workflows-n8n")
fi

# TypeScript
if check_file_exists "tsconfig.json"; then
  DETECTED_TYPES+=("TypeScript")
  GLOBAL_SKILLS_LIST+=("typescript-expert" "typescript-patterns" "cc-skill-coding-standards")
fi

# Docker/DevOps
if check_file_exists "Dockerfile" || check_file_exists "docker-compose.yml" || check_dir_exists ".github/workflows"; then
  DETECTED_TYPES+=("DevOps")
  GLOBAL_SKILLS_LIST+=("docker-expert" "github-actions" "ci-cd-patterns")
fi

# LegalTech
if check_any_file_pattern "*guardian*" || check_any_file_pattern "*contract*" || check_dir_exists "supabase/functions"; then
  DETECTED_TYPES+=("LegalTech")
  LOCAL_SKILLS_LIST+=("desarrollar-ux-garrigues" "desarrollar-ux-gdigital" "orquestar-agentes")
fi

# TERAS
if check_file_contains "package.json" "teras" || check_file_contains "README.md" "TERAS"; then
  DETECTED_TYPES+=("Teras Capital")
  LOCAL_SKILLS_LIST+=("desarrollar-ux-teras")
fi

# AI/Agents
if check_file_contains "package.json" "langchain" || check_file_contains "package.json" "openai" || check_dir_exists "agents"; then
  DETECTED_TYPES+=("AI/Agents")
  GLOBAL_SKILLS_LIST+=("prompt-engineer" "rag-engineer" "langgraph")
  LOCAL_SKILLS_LIST+=("orquestar-agentes" "integrar-lightrag-grafo-conocimiento")
fi

# === OUTPUT ===

echo -e "${GREEN}📦 Tipos de proyecto detectados:${NC}"
if [ ${#DETECTED_TYPES[@]} -eq 0 ]; then
  echo "   (ninguno específico - usando solo Essentials)"
else
  for type in "${DETECTED_TYPES[@]}"; do
    echo -e "   ${CYAN}• $type${NC}"
  done
fi
echo ""

echo -e "${GREEN}✅ Skills recomendadas:${NC}"
echo ""

# Eliminar duplicados y mostrar
echo -e "${YELLOW}📌 Global (desde ~/.agent/skills/skills/):${NC}"
printf '%s\n' "${GLOBAL_SKILLS_LIST[@]}" | sort -u | while read skill; do
  if [[ -d "$GLOBAL_SKILLS/$skill" ]]; then
    echo -e "   ✓ $skill"
  else
    echo -e "   ○ $skill (no encontrada)"
  fi
done
echo ""

if [ ${#LOCAL_SKILLS_LIST[@]} -gt 0 ]; then
  echo -e "${YELLOW}📌 Local (desde Dropbox):${NC}"
  printf '%s\n' "${LOCAL_SKILLS_LIST[@]}" | sort -u | while read skill; do
    if [[ -d "$LOCAL_SKILLS/$skill" ]]; then
      echo -e "   ✓ $skill"
    else
      echo -e "   ○ $skill (no encontrada)"
    fi
  done
  echo ""
fi

# === COMANDOS DE ACTIVACIÓN ===

echo -e "${BLUE}💡 Para activar en tu proyecto:${NC}"
echo ""
echo "   # Crear directorio de skills en el proyecto"
echo "   mkdir -p .agent/skills"
echo ""
echo "   # Enlazar skills globales"

printf '%s\n' "${GLOBAL_SKILLS_LIST[@]}" | sort -u | head -5 | while read skill; do
  if [[ -d "$GLOBAL_SKILLS/$skill" ]]; then
    echo "   ln -s $GLOBAL_SKILLS/$skill .agent/skills/"
  fi
done

if [ ${#LOCAL_SKILLS_LIST[@]} -gt 0 ]; then
  echo ""
  echo "   # Enlazar skills locales"
  printf '%s\n' "${LOCAL_SKILLS_LIST[@]}" | sort -u | while read skill; do
    if [[ -d "$LOCAL_SKILLS/$skill" ]]; then
      echo "   ln -s $LOCAL_SKILLS/$skill .agent/skills/"
    fi
  done
fi

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "Total skills sugeridas: $(($(printf '%s\n' "${GLOBAL_SKILLS_LIST[@]}" | sort -u | wc -l) + $(printf '%s\n' "${LOCAL_SKILLS_LIST[@]}" | sort -u | wc -l)))"
