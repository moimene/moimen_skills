---
name: iterar-con-lovable
description: Guía para iterar eficientemente con Lovable AI en construcción de prompts y revisión de peticiones. Úsese cuando el usuario trabaje con Lovable para crear demostradores, apps MVP, o itere sobre código generado. Incluye estructura de prompts, Knowledge files, guardrails y patrones de iteración.
---

# Iterar con Lovable

Sistema para trabajar eficientemente con Lovable AI en la construcción de aplicaciones y demostradores.

## Rol del Modelo

Actúas como **experto en prompt engineering para Lovable**, especializado en estructurar peticiones que generen código de alta calidad, iteración efectiva y debugging de resultados.

---

## Cuándo Usar Esta Skill

- Preparar prompts para Lovable
- Revisar y mejorar peticiones antes de enviarlas
- Iterar sobre código generado
- Debuggear problemas de generación
- Estructurar proyectos complejos en Lovable

---

## Principios Fundamentales

### 1. Knowledge File (Cerebro del Proyecto)

Crear un archivo de conocimiento que se envía con cada prompt:

```markdown
# Knowledge File: [Nombre Proyecto]

## Visión del Producto
[Qué es y para quién]

## User Journeys Principales
1. [Journey 1]
2. [Journey 2]

## Features Clave
- [Feature 1]
- [Feature 2]

## Stack Técnico
- Framework: [Next.js / React / etc.]
- Styling: [Tailwind / CSS Modules]
- Backend: [Supabase / Firebase / etc.]

## Guías de Diseño
- Paleta: [colores]
- Tipografía: [fuentes]
- Estilo general: [moderno / corporativo / etc.]
```

### 2. Prompts Claros y Verbosos

Lovable solo sabe lo que le dices. Más contexto = mejor resultado.

```markdown
# ❌ Incorrecto
Añade un formulario de login

# ✅ Correcto
Añade un formulario de login en la página /auth/login que:
- Tenga campos email y password
- Valide email con formato correcto
- Password mínimo 8 caracteres
- Botón "Iniciar sesión" deshabilitado hasta validación
- Estado de loading mientras se procesa
- Integre con Supabase Auth
- Redirija a /dashboard tras login exitoso
```

---

## Estructura de Prompt Óptimo

### Template

```markdown
## Contexto
[Situación actual del proyecto]

## Tarea
[Qué quieres que haga, específicamente]

## Archivos Relevantes
- `/src/pages/login.tsx`
- `/src/lib/auth.ts`

## Directrices
- [Patrón a seguir]
- [Estilo de componentes]
- [Convenciones de nombres]

## Restricciones
- NO modificar: `/src/shared/Layout.tsx`
- Mantener: [funcionalidad existente]

## Verificación
Cuando termines, verifica que:
- [ ] El formulario valida correctamente
- [ ] El loading state funciona
- [ ] La redirección ocurre tras login
```

---

## Guardrails Esenciales

### Proteger Archivos

```markdown
## ⚠️ NO MODIFICAR
- `/src/shared/Layout.tsx`
- `/src/lib/supabase.ts`
- `/src/styles/globals.css`
```

### Mantener Funcionalidad

```markdown
## MANTENER (no romper)
- La navegación existente
- Los estilos del header
- La autenticación actual
```

### Especificar Scope

```markdown
## SCOPE de esta tarea
SOLO modifica:
- `/src/pages/settings.tsx`
- `/src/components/SettingsForm.tsx`
```

---

## Patrones de Iteración

### 1. Chunks Pequeños

```markdown
# Bloque 1: Crear componente base
Crea el componente UserProfile en /src/components/UserProfile.tsx
con estructura básica...

# [VERIFICAR antes de continuar]

# Bloque 2: Añadir fetch de datos
Ahora añade el fetch de datos del usuario...

# [VERIFICAR antes de continuar]

# Bloque 3: Añadir edición
Ahora añade la capacidad de editar...
```

### 2. Chat Mode para Validación

Entre bloques de trabajo, usa chat para verificar:

```markdown
Antes de continuar, confirma:
1. ¿El componente renderiza correctamente?
2. ¿Los estilos coinciden con el diseño?
3. ¿La consola muestra errores?
```

### 3. Roles de Usuario

Si hay múltiples roles, especificar:

```markdown
## Rol: Admin
Esta funcionalidad es SOLO para admins.
El usuario regular NO debe ver este botón.
Verificar que el RLS de Supabase filtre correctamente.
```

---

## Debugging de Problemas

### Error de Generación

```markdown
## Problema Observado
[Screenshot o descripción exacta del error]

## Comportamiento Esperado
[Qué debería pasar]

## Comportamiento Actual
[Qué está pasando]

## Código Relevante
```tsx
// Pega el código problemático
```

## Hipótesis
Creo que el problema es [X] porque [Y].
```

### UI No Coincide

```markdown
## Problema Visual
[Screenshot del resultado actual]

## Referencia Esperada
[Screenshot o descripción del diseño esperado]

## Diferencias Específicas
- El botón debería ser azul, no gris
- El spacing entre elementos es muy pequeño
- Falta el borde redondeado
```

---

## Checklist Pre-Prompt

Antes de enviar a Lovable, verificar:

### Contexto
- [ ] ¿Incluí el Knowledge File o contexto del proyecto?
- [ ] ¿Especifiqué el stack técnico?
- [ ] ¿Mencioné archivos relevantes?

### Tarea
- [ ] ¿Es específica y detallada?
- [ ] ¿Tiene criterios de aceptación claros?
- [ ] ¿Es lo suficientemente pequeña para un contexto?

### Guardrails
- [ ] ¿Especifiqué qué NO modificar?
- [ ] ¿Protegí archivos críticos?
- [ ] ¿Limité el scope?

### Verificación
- [ ] ¿Incluí pasos de verificación?
- [ ] ¿Definí qué significa "terminado"?

---

## Templates Rápidos

### Nueva Feature

```markdown
## Contexto
App de [tipo] con [stack]. Proyecto en fase [MVP/producción].

## Tarea
Implementar [feature] que permita [acción] para [usuario].

## Archivos a Crear/Modificar
- [lista de archivos]

## Criterios de Aceptación
- [ ] [criterio 1]
- [ ] [criterio 2]

## NO Modificar
- [archivos protegidos]
```

### Fix de Bug

```markdown
## Bug
[descripción breve]

## Reproducción
1. Ir a [página]
2. Hacer [acción]
3. Observar [problema]

## Esperado vs Actual
- Esperado: [comportamiento correcto]
- Actual: [comportamiento incorrecto]

## Archivos Sospechosos
- [archivo 1]
- [archivo 2]
```

### Refactoring

```markdown
## Objetivo
Refactorizar [componente/función] para [mejorar X].

## Estado Actual
[descripción o código actual]

## Estado Deseado
[descripción o estructura deseada]

## Restricciones
- Mantener la misma API pública
- No cambiar tests existentes
- [otras restricciones]
```

---

## Anti-patrones a Evitar

| ❌ Evitar | ✅ Usar |
|-----------|--------|
| "Hazme una app de tareas" | Descripción detallada con features específicas |
| "Arregla los estilos" | "El botón debe ser azul #0066cc con padding 12px" |
| Prompt de 3 líneas | Prompt estructurado con contexto |
| Cambiar todo a la vez | Chunks pequeños con verificación |
| Sin guardrails | Archivos protegidos explícitos |

---

## Integración con Otras Skills

- **desarrollar-ux-garrigues**: Incluir tokens en Knowledge File
- **desarrollar-ux-gdigital**: Incluir triángulo de legitimidad
- **aplicar-react-best-practices**: Validar código generado

---

## Recursos

- [Lovable Docs](https://docs.lovable.dev)
- [Templates de Prompts](resources/templates/)
- [Knowledge File de Ejemplo](resources/knowledge-file.md)

---

## Regla Final

> **Prompt detallado + Knowledge File + Guardrails + Chunks pequeños = Generación exitosa con Lovable.**
