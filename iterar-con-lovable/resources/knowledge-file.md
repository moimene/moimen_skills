# Knowledge File: [Nombre del Proyecto]

> Este archivo se envía con cada prompt a Lovable para proporcionar contexto consistente.

## Visión del Producto

**Nombre:** [Nombre de la aplicación]

**Descripción:** [Qué es y qué problema resuelve]

**Usuarios objetivo:** [A quién va dirigido]

---

## User Journeys Principales

### Journey 1: [Nombre del Journey]
1. Usuario llega a [página]
2. Hace [acción]
3. Ve [resultado]
4. [Siguiente paso]

### Journey 2: [Nombre del Journey]
1. Usuario [acción]
2. [...]

---

## Features Clave

### MVP (Fase 1)
- [ ] Feature 1: [descripción]
- [ ] Feature 2: [descripción]
- [ ] Feature 3: [descripción]

### Futuras (Fase 2)
- [ ] Feature 4: [descripción]
- [ ] Feature 5: [descripción]

---

## Stack Técnico

| Capa | Tecnología | Notas |
|------|------------|-------|
| Frontend | React + Next.js 14 | App Router |
| Styling | Tailwind CSS | Con tokens personalizados |
| UI Components | shadcn/ui | Componentes base |
| Backend | Supabase | Auth + Database + Storage |
| Hosting | Vercel | Preview deployments |

---

## Estructura de Carpetas

```
src/
├── app/                    # Pages (App Router)
│   ├── (auth)/             # Rutas de autenticación
│   ├── (dashboard)/        # Rutas autenticadas
│   └── api/                # API routes
├── components/
│   ├── ui/                 # shadcn/ui components
│   ├── shared/             # Componentes compartidos
│   └── features/           # Componentes por feature
├── lib/
│   ├── supabase.ts         # Cliente Supabase
│   ├── utils.ts            # Utilidades
│   └── hooks/              # Custom hooks
└── styles/
    └── globals.css         # Estilos globales + tokens
```

---

## Guías de Diseño

### Paleta de Colores

| Token | Valor | Uso |
|-------|-------|-----|
| `--primary` | #[hex] | Botones principales, CTAs |
| `--secondary` | #[hex] | Elementos secundarios |
| `--background` | #[hex] | Fondos |
| `--foreground` | #[hex] | Texto principal |
| `--muted` | #[hex] | Texto secundario |

### Tipografía

- **Familia:** Inter / [otra]
- **Títulos:** font-bold, text-2xl
- **Body:** font-normal, text-base
- **Small:** text-sm, text-muted

### Componentes

- **Botones:** Redondeados (rounded-lg), padding consistente
- **Cards:** Borde sutil, sombra en hover
- **Inputs:** Borde gris, focus ring azul
- **Espaciado:** Usar scale de Tailwind (4, 6, 8, 12, 16)

---

## Convenciones de Código

### Nombres

- **Componentes:** PascalCase (`UserProfile.tsx`)
- **Funciones:** camelCase (`getUserData`)
- **Archivos:** kebab-case (`user-profile.tsx`)
- **Constantes:** SCREAMING_SNAKE_CASE (`API_URL`)

### Patrones

```tsx
// Componente típico
export function ComponentName({ prop1, prop2 }: Props) {
  // Estado
  const [state, setState] = useState();
  
  // Efectos
  useEffect(() => {}, []);
  
  // Handlers
  const handleClick = () => {};
  
  // Render
  return <div>...</div>;
}
```

---

## Autenticación

**Provider:** Supabase Auth

**Flujos:**
- Login con email/password
- [Magic link / OAuth / etc.]

**Roles:**
- `user` - Usuario regular
- `admin` - Administrador

---

## Base de Datos

### Tablas Principales

| Tabla | Descripción | RLS |
|-------|-------------|-----|
| `users` | Perfiles de usuario | ✅ |
| `[otra]` | [descripción] | ✅ |

---

## ⚠️ Archivos Protegidos (NO MODIFICAR)

```
/src/lib/supabase.ts
/src/components/shared/Layout.tsx
/src/styles/globals.css (tokens section)
```

---

## Notas Importantes

1. [Nota importante 1]
2. [Nota importante 2]
3. [Nota importante 3]

---

*Última actualización: [fecha]*
