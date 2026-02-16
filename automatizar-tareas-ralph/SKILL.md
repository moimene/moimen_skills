---
name: automatizar-tareas-ralph
description: Automatiza tareas repetitivas de desarrollo usando el patrón Ralph de bucle autónomo. Úsese cuando el usuario quiera ejecutar múltiples tareas de un PRD automáticamente, implementar features completas sin intervención, o repetir ciclos de test/build/commit hasta que todo pase. Ideal para desarrollo con Amp o Claude Code.
---

# Automatizar Tareas con Ralph

Sistema de bucle autónomo para ejecutar tareas de desarrollo repetitivas hasta completar todos los items de un PRD.

## Rol del Modelo

Actúas como **orquestador de desarrollo autónomo** especializado en el patrón Ralph. Tu objetivo es configurar y ejecutar bucles de desarrollo que implementen features completas de forma autónoma, con feedback loops de tests y typecheck.

---

## Cuándo Usar Esta Skill

- Implementar múltiples user stories de un PRD sin intervención
- Ejecutar bucles de test-fix-commit automáticos
- Automatizar features que requieren varias iteraciones
- Mantener contexto entre sesiones via git + progress.txt
- Actualizar AGENTS.md con learnings automáticamente

---

## Concepto: El Patrón Ralph

```
┌─────────────────────────────────────────────────────────────┐
│                      BUCLE RALPH                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Leer prd.json → encontrar story con passes: false       │
│                          ↓                                  │
│  2. Implementar esa única story                             │
│                          ↓                                  │
│  3. Ejecutar quality checks (typecheck, tests)              │
│                          ↓                                  │
│  4. Si pasa → commit + marcar passes: true                  │
│     Si falla → arreglar y repetir paso 3                   │
│                          ↓                                  │
│  5. Actualizar progress.txt con learnings                   │
│                          ↓                                  │
│  6. ¿Todas las stories pasan? → FIN                        │
│     ¿Quedan stories? → Volver a paso 1 (nueva iteración)   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Memoria Entre Iteraciones

Cada iteración es un contexto fresco. La memoria persiste via:

| Artefacto | Propósito |
|-----------|-----------|
| `prd.json` | Qué stories están done/pending |
| `progress.txt` | Learnings y contexto acumulado |
| Git history | Commits de iteraciones anteriores |
| `AGENTS.md` | Patrones descubiertos para futuras sesiones |

---

## Estructura de Archivos

```
proyecto/
├── prd.json              # PRD en formato JSON (stories con passes)
├── progress.txt          # Log de progreso y learnings
├── AGENTS.md             # Patrones descubiertos (leído por AI tools)
├── tasks/
│   └── prd-feature.md    # PRD original en markdown
└── scripts/
    └── ralph/
        ├── ralph.sh      # Script principal del bucle
        └── prompt.md     # Prompt para cada iteración
```

---

## Flujo de Trabajo

### 1. Crear PRD

```markdown
# PRD: [Nombre de Feature]

## User Stories

### US-001: [Título]
**Como** [rol]
**Quiero** [acción]
**Para** [beneficio]

**Criterios de Aceptación:**
- [ ] AC-1: [criterio verificable]
- [ ] AC-2: [criterio verificable]

### US-002: [Título]
...
```

### 2. Convertir a Formato Ralph (prd.json)

```json
{
  "name": "Feature Name",
  "branchName": "feature/my-feature",
  "userStories": [
    {
      "id": "US-001",
      "title": "Implementar login form",
      "description": "Como usuario quiero un form de login...",
      "priority": 1,
      "acceptanceCriteria": [
        "Form con email y password",
        "Validación de campos",
        "Submit llama a API /auth/login"
      ],
      "passes": false
    },
    {
      "id": "US-002",
      "title": "Añadir validación de errores",
      "priority": 2,
      "acceptanceCriteria": [...],
      "passes": false
    }
  ]
}
```

### 3. Ejecutar Ralph

```bash
# Usando Amp (default)
./scripts/ralph/ralph.sh [max_iterations]

# Usando Claude Code
./scripts/ralph/ralph.sh --tool claude [max_iterations]
```

Default: 10 iteraciones máximas.

---

## Cada Iteración

El script ejecuta estos pasos:

```bash
1. git checkout -b $branchName (si no existe)
2. Leer prd.json | jq primera story sin pasar
3. Invocar AI tool con prompt + story
4. AI implementa la story
5. Ejecutar: npm run typecheck && npm test
6. Si pasa:
   - git add . && git commit
   - Actualizar prd.json: passes: true
   - Append a progress.txt
7. Repetir hasta max_iterations o todas pasan
```

---

## Reglas Críticas

### 1. Tareas Pequeñas

Cada story debe completarse en un solo contexto:

| ✅ Tamaño correcto | ❌ Demasiado grande |
|--------------------|---------------------|
| Añadir columna DB + migración | "Construir todo el dashboard" |
| Añadir componente UI a página existente | "Añadir autenticación" |
| Actualizar server action con nueva lógica | "Refactorizar la API" |
| Añadir dropdown de filtro a lista | "Implementar sistema de permisos" |

### 2. Feedback Loops Obligatorios

Ralph solo funciona con feedback automático:

- `npm run typecheck` — Errores de tipos
- `npm test` — Tests automáticos
- CI debe estar verde (errores se acumulan)

### 3. Actualizar AGENTS.md

Después de cada iteración, añadir learnings:

```markdown
## Learnings

### 2026-01-25: Login Form
- Este codebase usa Zod para validación de forms
- Los forms están en `src/components/forms/`
- No olvidar añadir loading state al submit button
```

### 4. Verificación Browser para UI

Stories de frontend deben incluir:

```json
{
  "acceptanceCriteria": [
    "...",
    "Verificar en browser usando dev-browser skill"
  ]
}
```

---

## progress.txt

Log acumulativo de cada iteración:

```
=== Iteration 1 ===
Story: US-001 - Login form
Status: PASSED
Commits: abc123
Learnings:
- Found existing auth utilities in src/lib/auth
- Form validation uses react-hook-form + zod

=== Iteration 2 ===
Story: US-002 - Error handling
Status: PASSED
Commits: def456
Learnings:
- Toast notifications via sonner library
```

---

## Condición de Parada

Cuando todas las stories tienen `passes: true`:

```
<promise>COMPLETE</promise>
```

El bucle termina.

---

## Debugging

```bash
# Ver qué stories están done
cat prd.json | jq '.userStories[] | {id, title, passes}'

# Ver learnings acumulados
cat progress.txt

# Ver commits recientes
git log --oneline -10
```

---

## Script ralph.sh

```bash
#!/bin/bash
set -e

TOOL="${1:-amp}"  # amp o claude
MAX_ITERATIONS="${2:-10}"

# Leer branch del PRD
BRANCH=$(jq -r '.branchName' prd.json)
git checkout -b "$BRANCH" 2>/dev/null || git checkout "$BRANCH"

for i in $(seq 1 $MAX_ITERATIONS); do
  echo "=== Iteración $i ==="
  
  # Encontrar primera story sin pasar
  STORY=$(jq -r '.userStories[] | select(.passes == false) | .id' prd.json | head -1)
  
  if [ -z "$STORY" ]; then
    echo "<promise>COMPLETE</promise>"
    exit 0
  fi
  
  echo "Implementando: $STORY"
  
  # Invocar AI tool
  if [ "$TOOL" = "claude" ]; then
    claude-code --prompt "$(cat scripts/ralph/prompt.md)"
  else
    amp --prompt "$(cat scripts/ralph/prompt.md)"
  fi
  
  # Quality checks
  npm run typecheck
  npm test
  
  # Commit
  git add .
  git commit -m "feat: $STORY - implementación completada"
  
  # Marcar como passed
  jq --arg id "$STORY" '.userStories |= map(if .id == $id then .passes = true else . end)' prd.json > tmp.json
  mv tmp.json prd.json
  git add prd.json
  git commit -m "chore: mark $STORY as passed"
  
done

echo "Max iteraciones alcanzadas"
```

---

## Checklist de Setup

### Pre-ejecución

- [ ] PRD convertido a prd.json
- [ ] Todas las stories tienen `passes: false` inicial
- [ ] `branchName` definido en prd.json
- [ ] Tests existentes pasan (`npm test`)
- [ ] Typecheck pasa (`npm run typecheck`)

### Durante ejecución

- [ ] Cada story es lo suficientemente pequeña
- [ ] progress.txt se actualiza
- [ ] AGENTS.md recibe learnings

### Post-ejecución

- [ ] Todas las stories con `passes: true`
- [ ] Branch listo para PR
- [ ] AGENTS.md actualizado con patrones

---

## Recursos

- [ralph.sh Script](resources/ralph.sh)
- [prompt.md Template](resources/prompt.md)
- [prd.json Example](resources/prd.json.example)
- [Ralph Original](https://github.com/snarktank/ralph)

---

## Regla Final

> **Tareas pequeñas + feedback loops + memoria persistente = implementación autónoma exitosa.**
