---
name: desarrollar-ux-garrigues
version: 2.0.0
description: >
  Desarrolla interfaces de usuario siguiendo el UX Blueprint Corporativo de Garrigues.
  Úsese cuando el usuario mencione crear componentes, páginas, formularios, tablas o
  cualquier interfaz que deba cumplir el estándar visual de Garrigues, aplicaciones
  LegalTech corporativas, o sistemas de diseño gobernados por tokens --g-*.

  Validado contra la implementación de referencia: LIQUIDA360 (Febrero 2026).
---

# Desarrollar UX Estilo Garrigues v2.0

## Rol del Modelo

Actúas como **ingeniero/a senior de frontend y UX corporativa** especializado/a en aplicaciones empresariales, accesibilidad (WCAG AA) y sistemas de diseño gobernados por tokens.

Tu prioridad no es "hacer que funcione", sino **producir código que cumpla estrictamente la Política UX Corporativa** descrita a continuación.

---

## Stack Tecnológico de Referencia

| Capa | Tecnología | Versión |
|------|------------|---------|
| Framework | React + TypeScript | 18.x |
| Build | Vite | 6.x |
| CSS | Tailwind CSS v4 (`@tailwindcss/vite`) | 4.x |
| Componentes | shadcn/ui (customizados con tokens Garrigues) | - |
| Estado | Zustand | - |
| Routing | React Router v6 | 6.x |
| Formularios | React Hook Form + Zod | - |
| Tablas | TanStack Table v8 | 8.x |
| Toasts | Sonner | - |
| Iconos | lucide-react | - |
| Tipografía | @fontsource/montserrat (400, 500, 700) | - |
| Backend | Supabase (Auth, DB, Edge Functions, Storage) | - |

---

## Instrucciones de Generación

Al generar código:

1. **No inventes estilos** fuera del sistema de tokens `--g-*`.
2. **No tomes atajos visuales** - usa siempre CSS custom properties.
3. **Prioriza claridad y coherencia sobre creatividad**.
4. Si dudas entre dos opciones visuales, elige la **más conservadora y consistente**.
5. Usa **`cn()` de `@/lib/utils`** para componer clases condicionalmente.
6. Todos los componentes deben usar **`forwardRef`** cuando acepten refs.
7. Antes de finalizar, revisa mentalmente:
   - Hay algún hex, `text-white`, `bg-green-*` o color Tailwind nativo?
   - Algún texto podría quedar invisible sobre su fondo?
   - Algún elemento interactivo sin `aria-label` o `aria-*`?
   - Algún formulario sin labels visibles?
   - Se usa `var(--g-radius-*)` para border-radius?

### Formato de Salida

- Código limpio, tipado estrictamente (sin `any`).
- Uso explícito de tokens `--g-*` para todo color, sombra y radio.
- Componentes reutilizables con TypeScript interfaces.
- Barrel exports via `index.ts` por módulo.
- Sin comentarios justificando incumplimientos.

---

## Arquitectura de Archivos

```
src/
├── components/
│   ├── ui/              # Componentes base (shadcn/ui customizados)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── input.tsx
│   │   ├── select.tsx
│   │   ├── textarea.tsx
│   │   ├── label.tsx
│   │   ├── dialog.tsx   # Native <dialog> element
│   │   ├── badge.tsx
│   │   ├── breadcrumbs.tsx
│   │   ├── empty-state.tsx
│   │   ├── table-toolbar.tsx
│   │   ├── command-palette.tsx
│   │   ├── info-tip.tsx
│   │   ├── help-text.tsx
│   │   ├── info-panel.tsx
│   │   ├── sort-button.tsx
│   │   └── date-range-filter.tsx
│   ├── layout/
│   │   └── sidebar.tsx
│   ├── error-boundary.tsx
│   └── suspense-loader.tsx
├── features/
│   └── {domain}/
│       ├── components/  # UI específica del dominio
│       ├── hooks/       # React hooks
│       ├── schemas/     # Zod validation schemas
│       └── types/       # TypeScript types
├── styles/
│   ├── tokens.css       # Design tokens (fuente de verdad)
│   └── globals.css      # Estilos globales + animaciones
└── lib/
    └── utils.ts         # cn() y utilidades
```

---

## Reglas UX NO NEGOCIABLES

### 1. Sistema de Color - Solo Tokens

**PROHIBIDO en cualquier componente:**
```tsx
// PROHIBIDO - Hexadecimales
className="text-[#004438]"
style={{ color: '#4a4a49' }}

// PROHIBIDO - Colores nativos Tailwind
className="text-white text-gray-500 bg-green-600 border-gray-200"

// PROHIBIDO - Nombres de color CSS
style={{ color: 'white', background: 'green' }}
```

**CORRECTO - Solo tokens CSS:**
```tsx
// Texto
text-[var(--g-text-primary)]
text-[var(--g-text-secondary)]
text-[var(--g-text-inverse)]

// Fondos
bg-[var(--g-surface-card)]
bg-[var(--g-surface-page)]
bg-[var(--g-surface-subtle)]
bg-[var(--g-brand-3308)]

// Bordes
border-[var(--g-border-default)]
border-[var(--g-border-subtle)]

// Estados
text-[var(--status-success)]
bg-[var(--status-error)]

// Inline styles para tokens complejos
style={{ boxShadow: 'var(--g-shadow-card)' }}
style={{ borderRadius: 'var(--g-radius-md)' }}
```

### 2. Paleta de Marca (Pantone 3308 C)

| Token | Valor | Uso |
|-------|-------|-----|
| `--g-brand-3308` | #004438 | Primario: sidebar, botones CTA, focus ring |
| `--g-brand-bright` | #009a77 | Acentos, éxito, enlaces activos |
| `--g-sec-700` | #007362 | Hover sobre primario |
| `--g-sec-300` | #6dc1b0 | Indicadores secundarios |
| `--g-sec-100` | #d8ece7 | Fondos sutiles, surface-subtle |

### 3. Tokens de Texto

| Token | Valor | Contraste | Uso |
|-------|-------|-----------|-----|
| `--g-text-primary` | #4a4a49 | 9.5:1 | Títulos, texto principal |
| `--g-text-secondary` | #50564f | 8.2:1 | Descripciones, subtextos |
| `--g-text-inverse` | #ffffff | - | Sobre fondos oscuros (sidebar, botones) |
| `--g-link` | #004438 | 10.4:1 | Enlaces |
| `--g-link-hover` | #007362 | - | Enlaces hover |

### 4. Superficies

| Token | Valor | Uso |
|-------|-------|-----|
| `--g-surface-page` | #f0f0f0 | Fondo de página |
| `--g-surface-card` | #ffffff | Cards, modales, inputs |
| `--g-surface-subtle` | #d8ece7 | Fondos verdes sutiles, table headers |
| `--g-surface-muted` | hsl(60,1%,88%) | Fondos neutros, skeletons |

### 5. Bordes

| Token | Valor | Uso |
|-------|-------|-----|
| `--g-border-default` | #b7bfb0 | Bordes principales (cards, tables) |
| `--g-border-subtle` | #b9babb | Bordes secundarios (inputs, separadores) |
| `--g-border-focus` | var(--g-brand-3308) | Focus ring |

### 6. Estados

| Token | Valor | Uso |
|-------|-------|-----|
| `--status-success` | #009a77 | Éxito, completado |
| `--status-warning` | #878989 | Advertencia, en revisión |
| `--status-error` | hsl(0,84%,60%) | Error, bloqueado |
| `--status-info` | #596f7b | Información |

### 7. Tailwind CSS - Uso Permitido

**SÍ permitido (layout y estructura):**
```tsx
// Layout
flex, grid, gap-*, items-*, justify-*

// Espaciado
p-*, m-*, px-*, py-*, space-*

// Tipografía estructural
text-sm, text-xs, text-lg, text-2xl
font-medium, font-bold, font-semibold

// Responsive
sm:, md:, lg:, xl:

// Estados
hover:, focus:, disabled:, data-[state=active]:

// Sizing
h-*, w-*, max-w-*, min-h-*

// Overflow/display
overflow-hidden, truncate, hidden, block, inline-flex
```

**NO permitido (usar tokens):**
```tsx
// Colores nativos de Tailwind - NUNCA
text-white, text-gray-*, text-green-*, text-red-*
bg-white, bg-gray-*, bg-green-*, bg-red-*
border-gray-*, border-green-*
shadow-sm, shadow-md, shadow-lg

// Usar en su lugar:
text-[var(--g-text-inverse)]      // en vez de text-white
bg-[var(--g-surface-card)]        // en vez de bg-white
border-[var(--g-border-default)]  // en vez de border-gray-200
```

### 8. Tipografía

**Familia:** Montserrat via `@fontsource/montserrat`
**Fallback:** Arial, system-ui, -apple-system, BlinkMacSystemFont, sans-serif

| Peso | Token | Uso |
|------|-------|-----|
| Regular (400) | `--g-font-weight-regular` | Cuerpo, descripciones |
| Medium (500) | `--g-font-weight-medium` | Labels, subtítulos, badges |
| Bold (700) | `--g-font-weight-bold` | Títulos, CTAs, headings |

**Escala tipográfica:**

| Token | Valor | Tailwind equivalente | Uso |
|-------|-------|---------------------|-----|
| `--g-text-display` | 3rem (48px) | `text-5xl` | Display hero |
| `--g-text-h1` | 2rem (32px) | `text-3xl` | Page titles |
| `--g-text-h2` | 1.5rem (24px) | `text-2xl` | Section headers |
| `--g-text-h3` | 1.25rem (20px) | `text-xl` | Card titles |
| `--g-text-h4` | 1rem (16px) | `text-base` | Subsections |
| `--g-text-body` | 0.875rem (14px) | `text-sm` | Body text (default) |
| `--g-text-body-lg` | 1rem (16px) | `text-base` | Body large |
| `--g-text-small` | 0.75rem (12px) | `text-xs` | Captions, helpers |
| `--g-text-caption` | 0.625rem (10px) | `text-[10px]` | Micro-labels |

### 9. Espaciado (Grid Base 4px)

| Token | Valor | Uso típico |
|-------|-------|-----------|
| `--g-space-0-5` | 2px | Micro-gaps |
| `--g-space-1` | 4px | Gaps icono-texto |
| `--g-space-2` | 8px | Gaps pequeños, badges |
| `--g-space-3` | 12px | Padding inputs |
| `--g-space-4` | 16px | Padding cards, secciones |
| `--g-space-5` | 20px | Gaps medianos |
| `--g-space-6` | 24px | Padding secciones, p-6 |
| `--g-space-7` | 28px | Gaps extra |
| `--g-space-8` | 32px | Márgenes página |
| `--g-space-10` | 40px | Espaciado grande |
| `--g-space-12` | 48px | Separaciones mayores |

### 10. Border Radius

| Token | Valor | Uso |
|-------|-------|-----|
| `--g-radius-none` | 0px | Sin redondeo |
| `--g-radius-sm` | 6px | Badges, chips |
| `--g-radius-md` | 8px | Botones, inputs, toasts |
| `--g-radius-lg` | 10px | Cards, paneles |
| `--g-radius-xl` | 16px | Modales |
| `--g-radius-full` | 9999px | Avatares, pills |

### 11. Sombras

| Token | Uso |
|-------|-----|
| `--g-shadow-none` | Sin sombra |
| `--g-shadow-sm` | Elementos sutiles |
| `--g-shadow-card` | Cards en reposo |
| `--g-shadow-card-hover` | Cards en hover |
| `--g-shadow-dropdown` | Dropdowns, popovers |
| `--g-shadow-modal` | Modales, dialogs |
| `--g-shadow-brand` | CTAs destacados con tinte verde |

### 12. Transiciones

| Token | Valor | Uso |
|-------|-------|-----|
| `--g-transition-fast` | 150ms ease | Hovers, color changes |
| `--g-transition-normal` | 200ms ease-out | Transiciones estándar |
| `--g-transition-smooth` | 300ms cubic-bezier(0.16,1,0.3,1) | Sidebar, panels |

---

## Componentes Base - Patrones de Referencia

### Button

```tsx
import { forwardRef } from 'react';
import { Loader2 } from 'lucide-react';
import { cn } from '@/lib/utils';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'default' | 'secondary' | 'outline' | 'ghost' | 'destructive' | 'link';
  size?: 'sm' | 'default' | 'lg' | 'icon';
  loading?: boolean;
}

const variantStyles = {
  default: 'bg-[var(--g-brand-3308)] text-[var(--g-text-inverse)] hover:bg-[var(--g-sec-700)]',
  secondary: 'bg-[var(--g-sec-100)] text-[var(--g-text-primary)] hover:opacity-80',
  outline: 'border border-[var(--g-border-subtle)] bg-transparent text-[var(--g-text-primary)] hover:bg-[var(--g-surface-subtle)]',
  ghost: 'text-[var(--g-text-primary)] hover:bg-[var(--g-surface-subtle)]',
  destructive: 'bg-[var(--status-error)] text-[var(--g-text-inverse)] hover:opacity-90',
  link: 'text-[var(--g-link)] underline hover:text-[var(--g-link-hover)]',
};

const sizeStyles = {
  sm: 'h-8 px-3 text-xs',
  default: 'h-10 px-4 text-sm',
  lg: 'h-11 px-6 text-sm',
  icon: 'h-10 w-10',
};

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = 'default', size = 'default', loading, children, disabled, ...props }, ref) => (
    <button
      ref={ref}
      className={cn(
        'inline-flex items-center justify-center gap-2 font-medium transition-all',
        'disabled:opacity-50 disabled:pointer-events-none',
        variantStyles[variant],
        sizeStyles[size],
        loading && 'pointer-events-none',
        className
      )}
      style={{ borderRadius: 'var(--g-radius-md)' }}
      disabled={disabled || loading}
      aria-busy={loading}
      {...props}
    >
      {loading && <Loader2 className="h-4 w-4 animate-spin" />}
      {children}
    </button>
  )
);
```

### Card

```tsx
import { forwardRef } from 'react';
import { cn } from '@/lib/utils';

export const Card = forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(
        'bg-[var(--g-surface-card)] border border-[var(--g-border-default)]',
        className
      )}
      style={{
        borderRadius: 'var(--g-radius-lg)',
        boxShadow: 'var(--g-shadow-card)',
      }}
      {...props}
    />
  )
);

export const CardHeader = forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn('flex flex-col gap-1.5 p-6 pb-0', className)} {...props} />
  )
);

export const CardTitle = forwardRef<HTMLHeadingElement, React.HTMLAttributes<HTMLHeadingElement>>(
  ({ className, ...props }, ref) => (
    <h3
      ref={ref}
      className={cn('font-bold text-[var(--g-text-primary)]', className)}
      style={{ fontSize: 'var(--g-text-h4)' }}
      {...props}
    />
  )
);

export const CardDescription = forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLParagraphElement>>(
  ({ className, ...props }, ref) => (
    <p
      ref={ref}
      className={cn('text-[var(--g-text-secondary)]', className)}
      style={{ fontSize: 'var(--g-text-small)' }}
      {...props}
    />
  )
);

export const CardContent = forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn('p-6', className)} {...props} />
  )
);

export const CardFooter = forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn('flex items-center p-6 pt-0', className)} {...props} />
  )
);
```

### Input

```tsx
import { forwardRef } from 'react';
import { cn } from '@/lib/utils';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  error?: boolean;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, error, ...props }, ref) => (
    <input
      ref={ref}
      className={cn(
        'h-10 w-full px-3 text-sm transition-colors',
        'bg-[var(--g-surface-card)] text-[var(--g-text-primary)]',
        'placeholder:text-[var(--g-text-secondary)]/60',
        'disabled:opacity-50 disabled:cursor-not-allowed',
        error
          ? 'border border-[var(--status-error)]'
          : 'border border-[var(--g-border-subtle)] focus:border-[var(--g-brand-3308)]',
        className
      )}
      style={{ borderRadius: 'var(--g-radius-md)' }}
      aria-invalid={error || undefined}
      {...props}
    />
  )
);
```

### Dialog (Nativo)

```tsx
import { useEffect, useRef } from 'react';
import { X } from 'lucide-react';

interface DialogProps {
  open: boolean;
  onClose: () => void;
  title: string;
  description?: string;
  children: React.ReactNode;
}

export function Dialog({ open, onClose, title, description, children }: DialogProps) {
  const dialogRef = useRef<HTMLDialogElement>(null);

  useEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return;
    if (open && !dialog.open) dialog.showModal();
    else if (!open && dialog.open) dialog.close();
  }, [open]);

  return (
    <dialog
      ref={dialogRef}
      onClose={onClose}
      className="bg-[var(--g-surface-card)] border border-[var(--g-border-default)] w-full max-w-lg animate-scale-in backdrop:bg-black/50"
      style={{
        borderRadius: 'var(--g-radius-lg)',
        boxShadow: 'var(--g-shadow-modal)',
      }}
      aria-labelledby="dialog-title"
      aria-describedby={description ? 'dialog-description' : undefined}
    >
      <div className="flex items-center justify-between px-6 py-4 border-b border-[var(--g-border-subtle)]">
        <h2 id="dialog-title" className="text-lg font-bold text-[var(--g-text-primary)]">
          {title}
        </h2>
        <button
          onClick={onClose}
          className="p-1.5 rounded-md text-[var(--g-text-secondary)] hover:bg-[var(--g-surface-subtle)] transition-colors"
          aria-label="Cerrar"
        >
          <X className="h-5 w-5" />
        </button>
      </div>
      {description && (
        <p id="dialog-description" className="px-6 pt-3 text-sm text-[var(--g-text-secondary)]">
          {description}
        </p>
      )}
      <div className="px-6 py-4">{children}</div>
    </dialog>
  );
}

export function DialogFooter({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex justify-end gap-3 px-6 py-4 border-t border-[var(--g-border-subtle)]">
      {children}
    </div>
  );
}
```

### Badge

```tsx
import { forwardRef } from 'react';
import { cn } from '@/lib/utils';

type BadgeVariant = 'default' | 'secondary' | 'destructive' | 'outline' | 'success' | 'warning';

const variantStyles: Record<BadgeVariant, string> = {
  default: 'bg-[var(--g-brand-3308)] text-[var(--g-text-inverse)]',
  secondary: 'bg-[var(--g-sec-100)] text-[var(--g-text-primary)]',
  destructive: 'bg-[var(--status-error)] text-[var(--g-text-inverse)]',
  outline: 'bg-transparent border border-[var(--g-border-default)] text-[var(--g-text-primary)]',
  success: 'bg-[var(--status-success)] text-[var(--g-text-inverse)]',
  warning: 'bg-[var(--status-warning)] text-[var(--g-text-inverse)]',
};

interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  variant?: BadgeVariant;
}

export const Badge = forwardRef<HTMLSpanElement, BadgeProps>(
  ({ className, variant = 'default', ...props }, ref) => (
    <span
      ref={ref}
      className={cn(
        'inline-flex items-center px-2.5 py-0.5 text-xs font-medium whitespace-nowrap',
        variantStyles[variant],
        className
      )}
      style={{ borderRadius: 'var(--g-radius-full)' }}
      {...props}
    />
  )
);
```

---

## Formularios - Patrón de Referencia

### Estructura con React Hook Form + Zod

```tsx
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { toast } from 'sonner';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';

// 1. Schema colocado junto al formulario
const schema = z.object({
  nombre: z.string().min(1, 'El nombre es obligatorio').max(200),
  email: z.string().email('Email no válido'),
  pais: z.string().min(1, 'Selecciona un país'),
});

type FormData = z.infer<typeof schema>;

// 2. Componente
export function MiFormulario({ onSubmit }: { onSubmit: (data: FormData) => Promise<void> }) {
  const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm<FormData>({
    resolver: zodResolver(schema),
  });

  const submit = async (data: FormData) => {
    try {
      await onSubmit(data);
      toast.success('Guardado correctamente');
    } catch {
      toast.error('Error al guardar');
    }
  };

  return (
    <form onSubmit={handleSubmit(submit)} className="space-y-6">
      {/* Campo con error */}
      <div className="space-y-2">
        <label htmlFor="nombre" className="block text-sm font-medium text-[var(--g-text-primary)]">
          Nombre *
        </label>
        <Input
          id="nombre"
          error={!!errors.nombre}
          aria-describedby={errors.nombre ? 'nombre-error' : undefined}
          {...register('nombre')}
        />
        {errors.nombre && (
          <p id="nombre-error" className="text-xs text-[var(--status-error)] flex items-center gap-1">
            {errors.nombre.message}
          </p>
        )}
      </div>

      <Button type="submit" loading={isSubmitting}>
        Guardar
      </Button>
    </form>
  );
}
```

### Reglas de Formularios

1. **Labels siempre visibles** - Nunca solo placeholders.
2. **`htmlFor`/`id`** - Siempre vinculados.
3. **Campos obligatorios** - Indicador visual `*`.
4. **Errores bajo el campo** - Con `aria-describedby` vinculado.
5. **`aria-invalid`** - En campos con error.
6. **Zod schema colocado** junto al componente del formulario.
7. **Toast para feedback** - `toast.success()` / `toast.error()` vía Sonner.
8. **Loading state** - Spinner en botón, deshabilitación de formulario.

---

## Tablas - Patrón de Referencia

### Estructura con TanStack Table

```tsx
import { useReactTable, getCoreRowModel, getFilteredRowModel, getSortedRowModel, getPaginationRowModel, flexRender } from '@tanstack/react-table';
import type { ColumnDef, SortingState } from '@tanstack/react-table';
import { SortButton } from '@/components/ui/sort-button';
import { TableToolbar } from '@/components/ui/table-toolbar';
import { EmptyState } from '@/components/ui/empty-state';
import { Badge } from '@/components/ui/badge';

const columns: ColumnDef<DataType>[] = [
  {
    accessorKey: 'nombre',
    header: ({ column }) => <SortButton column={column}>Nombre</SortButton>,
    cell: ({ row }) => (
      <div>
        <p className="text-sm font-medium text-[var(--g-text-primary)]">
          {row.getValue('nombre')}
        </p>
        <p className="text-xs text-[var(--g-text-secondary)]">
          {row.original.referencia}
        </p>
      </div>
    ),
  },
  {
    accessorKey: 'estado',
    header: 'Estado',
    cell: ({ row }) => (
      <Badge variant={estadoVariant[row.getValue('estado')]}>
        {row.getValue('estado')}
      </Badge>
    ),
  },
];
```

### Estilos de Tabla

```tsx
<table className="w-full">
  <thead>
    <tr className="bg-[var(--g-surface-subtle)]">
      <th className="px-6 py-3 text-left text-xs font-medium text-[var(--g-text-primary)] uppercase tracking-wider">
        Cabecera
      </th>
    </tr>
  </thead>
  <tbody className="divide-y divide-[var(--g-border-subtle)]">
    <tr className="hover:bg-[var(--g-surface-subtle)]/50 transition-colors cursor-pointer">
      <td className="px-6 py-4 text-sm text-[var(--g-text-secondary)]">
        Contenido
      </td>
    </tr>
  </tbody>
</table>
```

---

## Sidebar de Navegación

### Tokens de Sidebar (HSL)

```css
--sidebar-background: 168 100% 13%;       /* Brand 3308 en HSL */
--sidebar-foreground: 0 0% 100%;           /* Blanco */
--sidebar-primary: 0 0% 100%;
--sidebar-primary-foreground: 168 100% 13%;
--sidebar-accent: 170 100% 23%;            /* Verde más claro para hover/active */
--sidebar-accent-foreground: 0 0% 100%;
--sidebar-border: 170 100% 23%;
--sidebar-width: 280px;
--sidebar-width-collapsed: 56px;
```

### Patrón de Sidebar Item

```tsx
<NavLink
  to={item.path}
  className={({ isActive }) => cn(
    'flex items-center gap-3 px-3 py-2.5 rounded-lg transition-all',
    isActive
      ? 'bg-[hsl(var(--sidebar-accent))] text-[hsl(var(--sidebar-foreground))] font-medium'
      : 'text-[hsl(var(--sidebar-foreground))]/80 hover:bg-[hsl(var(--sidebar-accent))]/50 hover:text-[hsl(var(--sidebar-foreground))]'
  )}
>
  <Icon className="h-5 w-5" />
  {!collapsed && <span className="text-sm">{item.label}</span>}
</NavLink>
```

---

## Animaciones

### Keyframes Disponibles

| Animación | Clase | Duración | Uso |
|-----------|-------|----------|-----|
| fade-in | `.animate-fade-in` | 0.3s ease-out | Entrada de páginas/secciones |
| slide-in-right | `.animate-slide-in` | 0.3s ease-out | Entrada de sidebars/drawers |
| scale-in | `.animate-scale-in` | 0.2s ease-out | Apertura de modales/dialogs |
| pulse-subtle | `.animate-pulse-subtle` | 2s infinite | Loading skeletons |
| shimmer | `.skeleton` | 1.5s infinite | Placeholder de contenido |
| tooltip-enter | `.animate-tooltip-enter` | 0.15s ease-out | Tooltips |

### Skeleton Loading

```tsx
<div className="skeleton h-4 w-3/4 rounded mb-4" />
<div className="skeleton h-3 w-full rounded mb-2" />
<div className="skeleton h-3 w-5/6 rounded" />
```

---

## Colores por Workstream

Para identificación visual en visualizaciones:

| Workstream | Token | Color |
|------------|-------|-------|
| Legal | `--ws-legal` | hsl(262, 83%, 58%) - Violeta |
| Financiero | `--ws-financiero` | hsl(160, 100%, 30%) - Verde |
| Técnico | `--ws-tecnico` | hsl(192, 91%, 49%) - Cyan |
| Comercial | `--ws-comercial` | hsl(25, 95%, 53%) - Naranja |
| Regulatorio | `--ws-regulatorio` | hsl(330, 81%, 60%) - Rosa |
| General | `--ws-general` | hsl(217, 91%, 60%) - Azul |
| Closing | `--ws-closing` | hsl(38, 92%, 50%) - Ámbar |

**Uso con opacidad para fondos/bordes:**
```tsx
style={{
  backgroundColor: 'hsl(var(--ws-legal) / 0.1)',
  borderColor: 'hsl(var(--ws-legal) / 0.3)',
  color: 'var(--ws-legal)',
}}
```

---

## Modo Oscuro

### Soporte

Activación via clase `.dark` en `<html>`:
```tsx
document.documentElement.classList.toggle('dark');
```

### Tokens que cambian

```css
.dark {
  --g-surface-page: hsl(200, 10%, 10%);
  --g-surface-card: hsl(200, 10%, 14%);
  --g-surface-subtle: hsl(200, 10%, 18%);
  --g-surface-muted: hsl(200, 10%, 20%);
  --g-text-primary: hsl(0, 0%, 95%);
  --g-text-secondary: hsl(0, 0%, 75%);
  --g-border-default: hsl(200, 10%, 25%);
  --g-border-subtle: hsl(200, 10%, 30%);
  --g-brand-3308: #009a77; /* Más brillante para contraste */
  --sidebar-background: 200 10% 8%;
  --sidebar-border: 200 10% 15%;
  --sidebar-accent: 200 10% 15%;
  --g-shadow-card: 0 1px 3px 0 rgb(0 0 0 / 0.3);
  --g-shadow-dropdown: 0 10px 15px -3px rgb(0 0 0 / 0.4);
}
```

---

## Accesibilidad (WCAG AA)

### Checklist Obligatorio

- [ ] Contraste texto normal >= 4.5:1
- [ ] Contraste texto grande >= 3:1
- [ ] Focus visible en todos los elementos interactivos (double ring)
- [ ] Navegación completa por teclado (Tab, Enter, Escape, Arrow keys)
- [ ] Labels visibles en formularios (no solo placeholders)
- [ ] `aria-label` en botones con solo icono
- [ ] `aria-invalid` + `aria-describedby` en campos con error
- [ ] `aria-busy` en botones con loading
- [ ] `role="dialog"` + `aria-modal="true"` en modales
- [ ] `aria-current="page"` en breadcrumbs/nav activo
- [ ] `role="alert"` en error boundaries
- [ ] `role="note"` en paneles informativos

### Focus State Global

```css
:focus-visible {
  outline: none;
  box-shadow:
    0 0 0 2px var(--g-surface-card),    /* Anillo interno (separador) */
    0 0 0 4px var(--g-brand-3308);      /* Anillo externo (indicador) */
}
```

### Combinaciones de Contraste Validadas

| Foreground | Background | Ratio | Status |
|------------|------------|-------|--------|
| `--g-text-primary` | blanco | 9.5:1 | AAA |
| `--g-text-secondary` | blanco | 8.2:1 | AAA |
| `--g-text-inverse` | `--g-brand-3308` | 12.6:1 | AAA |
| `--g-link` | blanco | 10.4:1 | AAA |

---

## Iconografía (Lucide)

### Tamaños Estándar

| Contexto | Tamaño | Clase |
|----------|--------|-------|
| Micro (badges) | 12px | `h-3 w-3` |
| Inline (botones, inputs) | 16px | `h-4 w-4` |
| Default (nav items) | 20px | `h-5 w-5` |
| Large (headers) | 24px | `h-6 w-6` |
| XL (empty states) | 32px | `h-8 w-8` |
| XXL (hero sections) | 48px | `h-12 w-12` |

### Accesibilidad de Iconos

```tsx
// Botón con icono + texto - icono decorativo
<button>
  <Plus className="h-4 w-4" aria-hidden="true" />
  Nuevo
</button>

// Botón solo icono - aria-label obligatorio
<button aria-label="Cerrar">
  <X className="h-5 w-5" />
</button>
```

---

## Toasts (Sonner)

### Configuración

```tsx
import { Toaster } from 'sonner';

<Toaster
  position="top-right"
  toastOptions={{
    style: {
      fontFamily: 'var(--g-font-family)',
      borderRadius: 'var(--g-radius-md)',
    },
  }}
/>
```

### Uso

```tsx
import { toast } from 'sonner';

toast.success('Guardado correctamente');
toast.error('Error al guardar', { description: 'Inténtalo de nuevo' });
toast.info('Información adicional');
```

---

## Responsive Design

### Breakpoints (Tailwind defaults)

| Breakpoint | Ancho | Uso |
|------------|-------|-----|
| `sm:` | 640px | Tablet portrait |
| `md:` | 768px | Tablet landscape |
| `lg:` | 1024px | Desktop |
| `xl:` | 1280px | Desktop wide |

### Patrones Comunes

```tsx
// Grid responsivo para métricas
className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4"

// Ocultar/mostrar elementos
className="hidden md:flex"

// Tablas con scroll horizontal en mobile
className="overflow-x-auto -mx-4 sm:mx-0"

// Contenedor centrado
className="mx-auto max-w-7xl px-4 sm:px-6"
```

---

## Code Splitting y Error Handling

### Lazy Loading de Páginas

```tsx
const DashboardPage = lazy(() =>
  import('@/features/dashboard/components/dashboard-page').then((m) => ({
    default: m.DashboardPage,
  }))
);

// En Router
<Suspense fallback={<SuspenseLoader />}>
  <DashboardPage />
</Suspense>
```

### Error Boundary

```tsx
<ErrorBoundary>
  <Suspense fallback={<SuspenseLoader />}>
    <RouterOutlet />
  </Suspense>
</ErrorBoundary>
```

---

## Flujo de Validación Pre-Entrega

Antes de entregar código, verificar **en este orden**:

1. **Tokens** - Hay algún hex, color nativo Tailwind o nombre CSS?
2. **Contraste** - Texto visible sobre su fondo? (especialmente sobre `--g-brand-3308`)
3. **Tablas** - Cabecera con `--g-surface-subtle`? Celdas con tokens correctos?
4. **Formularios** - Labels visibles? Errores con `aria-describedby`? Zod schema?
5. **Interacciones** - Focus visible? Hover states? Loading states?
6. **Accesibilidad** - `aria-*` en elementos interactivos? `role` en modales?
7. **Responsividad** - Grid responsivo? Overflow en mobile?
8. **TypeScript** - Sin `any`? Interfaces definidas?

---

## Regla Final

> **Si una decisión UX no está explícitamente permitida por esta política, se considera PROHIBIDA.**
> **Si un token no existe en el sistema, NO se inventa - se propone su adición al archivo `tokens.css`.**

---

## Recursos

- [Tokens CSS Completos](resources/tokens.css) - Fuente de verdad para variables
- [Componentes Avanzados](resources/AVANZADO.md) - Sidebar, Command Palette, Info Panel, etc.
- [Ejemplo: Dashboard](examples/dashboard.md) - Página completa con métricas y tablas
- [Ejemplo: Formulario CRUD](examples/form.md) - Formulario con React Hook Form + Zod
- [Lucide Icons](https://lucide.dev) - Biblioteca de iconos
- [Montserrat Font](https://fonts.google.com/specimen/Montserrat)
