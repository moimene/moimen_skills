---
description: Cómo activar y usar skills en un proyecto o carpeta
---

# Activar Skills en un Proyecto

Las skills extienden las capacidades del agente AI con conocimientos especializados.

---

## Método 1: Referencia Directa (Más Simple)

Sin configurar nada. Simplemente pide al agente que use la skill:

```
Usa la skill en /Users/moisesmenendez/Dropbox/Codigo/agent/skills/iterar-con-lovable
```

O con múltiples skills:

```
Para esta tarea, usa las skills:
- /Users/moisesmenendez/Dropbox/Codigo/agent/skills/arquitectar-prd
- /Users/moisesmenendez/Dropbox/Codigo/agent/skills/iterar-con-lovable
```

> ✅ **Ideal para**: uso ocasional o cuando no quieres modificar tu proyecto.

---

## Método 2: Symlink (Recomendado para Proyectos)

Un **enlace simbólico** (symlink) es un acceso directo que apunta a otra ubicación. Ventajas:
- Las skills se actualizan automáticamente cuando modificas el original
- No duplicas archivos
- Puedes activar/desactivar skills eliminando el enlace

### Sintaxis del comando `ln -s`

```bash
ln -s <ruta_origen> <ruta_destino>
```

| Parámetro | Descripción |
|-----------|-------------|
| `-s` | Crea un enlace simbólico (no físico) |
| `<ruta_origen>` | Ruta **absoluta** a la skill original |
| `<ruta_destino>` | Dónde crear el enlace (tu proyecto) |

> ⚠️ **Importante**: Usa siempre rutas absolutas para el origen. Las rutas relativas fallan al moverte entre directorios.

### Paso a Paso: Enlazar una Skill

```bash
# 1. Navega a tu proyecto
cd /ruta/a/tu/proyecto

# 2. Crea la carpeta de skills (si no existe)
mkdir -p .agent/skills

# 3. Crea el symlink
ln -s /Users/moisesmenendez/Dropbox/Codigo/agent/skills/iterar-con-lovable .agent/skills/

# 4. Verifica que funciona
ls -la .agent/skills/
```

Deberías ver algo como:
```
iterar-con-lovable -> /Users/moisesmenendez/Dropbox/Codigo/agent/skills/iterar-con-lovable
```

### Paso a Paso: Enlazar Todas las Skills

```bash
# Desde la raíz de tu proyecto
mkdir -p .agent/skills

# Enlaza todas las carpetas de skills (excluye archivos sueltos)
for skill in /Users/moisesmenendez/Dropbox/Codigo/agent/skills/*/; do
  ln -s "$skill" .agent/skills/
done

# Verifica
ls -la .agent/skills/
```

### Eliminar un Symlink

```bash
# Elimina solo el enlace, NO la skill original
rm .agent/skills/iterar-con-lovable

# ⚠️ NUNCA uses rm -r sobre un symlink a carpeta, podrías borrar el contenido original
```

### Troubleshooting

| Problema | Solución |
|----------|----------|
| `ln: .agent/skills/skill-name: File exists` | El enlace ya existe. Elimínalo primero con `rm` |
| El symlink aparece roto (rojo en terminal) | La ruta origen no existe o está mal escrita |
| `Permission denied` | Verifica permisos de lectura en la carpeta origen |

### Ejemplo Completo

```bash
# Proyecto: mi-app-contratos
cd ~/Proyectos/mi-app-contratos

# Activar skills para desarrollo con Lovable y PRDs
mkdir -p .agent/skills
ln -s /Users/moisesmenendez/Dropbox/Codigo/agent/skills/iterar-con-lovable .agent/skills/
ln -s /Users/moisesmenendez/Dropbox/Codigo/agent/skills/arquitectar-prd .agent/skills/
ln -s /Users/moisesmenendez/Dropbox/Codigo/agent/skills/desarrollar-ux-garrigues .agent/skills/

# Verificar
ls .agent/skills/
# Output: arquitectar-prd  desarrollar-ux-garrigues  iterar-con-lovable
```

---

## Método 3: Copiar Skills

Si prefieres tener una copia local independiente (no se actualizará automáticamente):

```bash
mkdir -p .agent/skills
cp -r /Users/moisesmenendez/Dropbox/Codigo/agent/skills/arquitectar-prd .agent/skills/
```

> ⚠️ **Nota**: Los cambios al original no se reflejarán en tu copia.

---

## Skills Disponibles

| Skill | Propósito |
|-------|-----------|
| `arquitectar-prd` | Generar PRDs con patrón Architect-first |
| `automatizar-tareas-ralph` | Loops autónomos estilo Ralph |
| `iterar-con-lovable` | Prompt engineering para Lovable AI |
| `desarrollar-ux-garrigues` | Design system Garrigues (Pantone 3308 C) |
| `desarrollar-ux-gdigital` | Branding g-digital |
| `desarrollar-ux-eadtrust` | UX para QTSP EADTrust |
| `gestionar-proyectos-conductor` | Framework CDD (Context-Driven Development) |
| `aplicar-compound-engineering` | Ciclo Plan-Work-Review-Compound |
| `aplicar-react-best-practices` | Optimización React/Next.js |
| `error-handling-patterns` | Patrones de manejo de errores |
| `integrar-lightrag-grafo-conocimiento` | Hybrid RAG con LightRAG |

---

## Invocar una Skill

Una vez activada, invoca la skill por nombre:

```
/arquitectar-prd para [descripción del proyecto]
```

O simplemente menciona el contexto:

```
Necesito crear un PRD para un sistema de gestión de contratos
```

El agente detectará automáticamente skills relevantes y cargará el SKILL.md correspondiente.

---

## Estructura de una Skill

```
skill-name/
├── SKILL.md          # Instrucciones principales (obligatorio)
├── resources/        # Assets, templates, ejemplos
│   ├── template.md
│   └── examples/
└── scripts/          # Utilidades opcionales
```

## Crear Nueva Skill

Consulta `skillmaker.md` en el directorio de skills o pide:

```
Crea una nueva skill para [propósito]
```
