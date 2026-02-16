# Componentes Avanzados - Garrigues UX v2.0

Documento de referencia basado en la implementación real de LIQUIDA360 (Febrero 2026).
Todos los patrones aquí documentados son componentes en producción.

---

## Catálogo de Componentes UI

| Componente | Archivo | Descripción |
|------------|---------|-------------|
| Button | `ui/button.tsx` | Botones con 6 variantes, loading state |
| Card | `ui/card.tsx` | Composable: Card, Header, Title, Description, Content, Footer |
| Input | `ui/input.tsx` | Input con error state y aria-invalid |
| Select | `ui/select.tsx` | Select nativo con error state |
| Textarea | `ui/textarea.tsx` | Textarea con resize-y |
| Label | `ui/label.tsx` | Label con peer-disabled |
| Dialog | `ui/dialog.tsx` | Native `<dialog>` element |
| Badge | `ui/badge.tsx` | 6 variantes (default, secondary, destructive, outline, success, warning) |
| Breadcrumbs | `ui/breadcrumbs.tsx` | Navegación con ChevronRight y aria-current |
| EmptyState | `ui/empty-state.tsx` | Estado vacío con icono, título, acción |
| TableToolbar | `ui/table-toolbar.tsx` | Search + filters + export + record count |
| CommandPalette | `ui/command-palette.tsx` | Cmd+K global search |
| InfoTip | `ui/info-tip.tsx` | Tooltip posicionable |
| HelpText | `ui/help-text.tsx` | Texto auxiliar para formularios |
| InfoPanel | `ui/info-panel.tsx` | Panel informativo dismissible |
| SortButton | `ui/sort-button.tsx` | Botón de ordenación para TanStack Table |
| DateRangeFilter | `ui/date-range-filter.tsx` | Filtro de rango de fechas |
| ErrorBoundary | `error-boundary.tsx` | Captura de errores de renderizado |
| SuspenseLoader | `suspense-loader.tsx` | Spinner de carga para lazy loading |
| Sidebar | `layout/sidebar.tsx` | Sidebar colapsable con role-based nav |

---

## Sidebar de Navegación Completo

### Estructura Visual

```
+-------------------------------------+
|  [L3]  LIQUIDA360                   |  <- Logo + Título
|         Gestión de Pagos            |  <- Subtítulo
+--------------------- ---------------+
|  NAVEGACIÓN                         |  <- Group Label (caption, medium, 70%)
|                                     |
|  [icon] Panel                       |  <- NavLink items
|  [icon] Corresponsales             |
|  [icon] Certificados               |
|  [icon] Liquidaciones              |  <- Activo: bg sidebar-accent
|  [icon] Pagos                      |
|  [icon] Notificaciones [3]         |  <- Con badge contador
|                                     |
|  ADMINISTRACIÓN                     |  <- Solo para role admin
|  [icon] Configuración              |
+-------------------------------------+
|  [shield] Seguridad                |
|  [avatar] usuario@garrigues.com    |
|  [badge]  Admin                    |
|  [->] Cerrar Sesión               |
+-------------------------------------+
|  [<>] Colapsar                     |  <- Toggle collapse
+-------------------------------------+
```

### Implementación de Referencia

```tsx
import { NavLink, useNavigate } from 'react-router-dom';
import { cn } from '@/lib/utils';
import {
  LayoutDashboard, Users, FileCheck, Receipt, CreditCard,
  Bell, Settings, Shield, LogOut, ChevronLeft, ChevronRight
} from 'lucide-react';
import { useAuth } from '@/features/auth/hooks/use-auth';
import type { UserRole } from '@/features/auth/types';

interface NavItem {
  label: string;
  path: string;
  icon: React.ElementType;
  roles?: UserRole[];
}

const mainNav: NavItem[] = [
  { label: 'Panel', path: '/', icon: LayoutDashboard },
  { label: 'Corresponsales', path: '/correspondents', icon: Users },
  { label: 'Certificados', path: '/certificates', icon: FileCheck },
  { label: 'Liquidaciones', path: '/liquidations', icon: Receipt },
  { label: 'Pagos', path: '/payments', icon: CreditCard, roles: ['financiero', 'admin'] },
  { label: 'Notificaciones', path: '/notifications', icon: Bell },
];

const adminNav: NavItem[] = [
  { label: 'Configuración', path: '/settings', icon: Settings, roles: ['admin'] },
];

interface SidebarProps {
  collapsed: boolean;
  onToggle: () => void;
}

export function Sidebar({ collapsed, onToggle }: SidebarProps) {
  const { user, role, signOut } = useAuth();
  const navigate = useNavigate();

  const canAccess = (item: NavItem) =>
    !item.roles || item.roles.includes(role);

  return (
    <aside
      className="flex flex-col h-screen border-r transition-all"
      style={{
        width: collapsed ? 'var(--sidebar-width-collapsed)' : 'var(--sidebar-width)',
        backgroundColor: 'hsl(var(--sidebar-background))',
        borderColor: 'hsl(var(--sidebar-border))',
        transition: `width var(--g-transition-smooth)`,
      }}
      aria-label="Navegación principal"
    >
      {/* Header */}
      <div className="p-4 border-b" style={{ borderColor: 'hsl(var(--sidebar-border) / 0.5)' }}>
        {!collapsed && (
          <div className="flex items-center gap-3">
            <div
              className="w-10 h-10 flex items-center justify-center font-bold text-lg"
              style={{
                backgroundColor: 'hsl(var(--sidebar-accent))',
                color: 'hsl(var(--sidebar-foreground))',
                borderRadius: 'var(--g-radius-md)',
              }}
            >
              L3
            </div>
            <div>
              <h1 className="text-base font-bold" style={{ color: 'hsl(var(--sidebar-foreground))' }}>
                LIQUIDA360
              </h1>
              <p className="text-xs" style={{ color: 'hsl(var(--sidebar-foreground) / 0.7)' }}>
                Gestión de Pagos
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Navigation */}
      <nav className="flex-1 p-2 space-y-1 overflow-y-auto">
        <SidebarGroupLabel collapsed={collapsed}>Navegación</SidebarGroupLabel>
        {mainNav.filter(canAccess).map((item) => (
          <SidebarItem key={item.path} item={item} collapsed={collapsed} />
        ))}

        {adminNav.some(canAccess) && (
          <>
            <SidebarGroupLabel collapsed={collapsed}>Administración</SidebarGroupLabel>
            {adminNav.filter(canAccess).map((item) => (
              <SidebarItem key={item.path} item={item} collapsed={collapsed} />
            ))}
          </>
        )}
      </nav>

      {/* Footer */}
      <div className="p-3 border-t" style={{ borderColor: 'hsl(var(--sidebar-border) / 0.5)' }}>
        {!collapsed && (
          <div className="mb-3">
            <p className="text-sm font-medium truncate" style={{ color: 'hsl(var(--sidebar-foreground))' }}>
              {user?.email}
            </p>
            <Badge variant="secondary" className="mt-1 text-[10px]">
              {role}
            </Badge>
          </div>
        )}
        <button
          onClick={signOut}
          className="flex items-center gap-2 w-full px-3 py-2 text-sm rounded-lg transition-colors"
          style={{ color: 'hsl(var(--sidebar-foreground) / 0.8)' }}
          aria-label="Cerrar sesión"
        >
          <LogOut className="h-4 w-4" />
          {!collapsed && 'Cerrar Sesión'}
        </button>
      </div>

      {/* Collapse Toggle */}
      <button
        onClick={onToggle}
        className="flex items-center justify-center p-3 border-t transition-colors"
        style={{
          borderColor: 'hsl(var(--sidebar-border) / 0.5)',
          color: 'hsl(var(--sidebar-foreground) / 0.6)',
        }}
        aria-label={collapsed ? 'Expandir sidebar' : 'Colapsar sidebar'}
      >
        {collapsed ? <ChevronRight className="h-4 w-4" /> : <ChevronLeft className="h-4 w-4" />}
      </button>
    </aside>
  );
}

function SidebarGroupLabel({ children, collapsed }: { children: React.ReactNode; collapsed: boolean }) {
  if (collapsed) return null;
  return (
    <div
      className="px-3 py-2 font-medium tracking-wider uppercase"
      style={{
        fontSize: 'var(--g-text-caption)',
        color: 'hsl(var(--sidebar-foreground) / 0.7)',
      }}
    >
      {children}
    </div>
  );
}

function SidebarItem({ item, collapsed }: { item: NavItem; collapsed: boolean }) {
  const Icon = item.icon;
  return (
    <NavLink
      to={item.path}
      end={item.path === '/'}
      className={({ isActive }) => cn(
        'flex items-center gap-3 px-3 py-2.5 rounded-lg transition-all',
        collapsed && 'justify-center',
        isActive
          ? 'font-medium'
          : ''
      )}
      style={({ isActive }) => ({
        backgroundColor: isActive
          ? 'hsl(var(--sidebar-accent))'
          : 'transparent',
        color: isActive
          ? 'hsl(var(--sidebar-foreground))'
          : 'hsl(var(--sidebar-foreground) / 0.8)',
      })}
      title={collapsed ? item.label : undefined}
    >
      <Icon className="h-5 w-5 shrink-0" />
      {!collapsed && <span className="text-sm">{item.label}</span>}
    </NavLink>
  );
}
```

---

## Command Palette (Cmd+K)

### Características

- **Atajo global:** `Cmd+K` (Mac) / `Ctrl+K` (Windows)
- **Busca en:** Corresponsales, Liquidaciones, Certificados, Pagos
- **Navegación por teclado:** ArrowUp/Down, Enter, Escape
- **Índice de búsqueda:** buildSearchIndex + searchEntities utilities

### Estructura

```tsx
interface SearchableEntity {
  type: 'correspondent' | 'liquidation' | 'certificate' | 'payment';
  id: string;
  href: string;
  title: string;
  subtitle: string;
}

const typeConfig: Record<string, { label: string; icon: React.ElementType; badgeVariant: BadgeVariant }> = {
  correspondent: { label: 'Corresponsal', icon: Users, badgeVariant: 'default' },
  liquidation: { label: 'Liquidación', icon: Receipt, badgeVariant: 'secondary' },
  certificate: { label: 'Certificado', icon: FileCheck, badgeVariant: 'success' },
  payment: { label: 'Pago', icon: CreditCard, badgeVariant: 'outline' },
};
```

### Patrón de Implementación

```tsx
export function CommandPalette() {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [activeIndex, setActiveIndex] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);
  const navigate = useNavigate();

  // Keyboard shortcut
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setOpen(prev => !prev);
      }
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, []);

  // Focus input on open
  useEffect(() => {
    if (open) inputRef.current?.focus();
  }, [open]);

  return open ? (
    <div className="command-palette-backdrop" onClick={() => setOpen(false)}>
      <div
        className="command-palette-panel"
        role="dialog"
        aria-modal="true"
        onClick={(e) => e.stopPropagation()}
        style={{
          position: 'fixed', top: '20%', left: '50%', transform: 'translateX(-50%)',
          width: '100%', maxWidth: '560px',
          backgroundColor: 'var(--g-surface-card)',
          borderRadius: 'var(--g-radius-lg)',
          boxShadow: 'var(--g-shadow-modal)',
          border: '1px solid var(--g-border-default)',
        }}
      >
        {/* Search input */}
        <div className="flex items-center gap-3 px-4 py-3 border-b border-[var(--g-border-subtle)]">
          <Search className="h-5 w-5 text-[var(--g-text-secondary)]" />
          <input
            ref={inputRef}
            value={query}
            onChange={(e) => { setQuery(e.target.value); setActiveIndex(0); }}
            className="flex-1 bg-transparent text-sm text-[var(--g-text-primary)] placeholder:text-[var(--g-text-secondary)] outline-none"
            placeholder="Buscar corresponsales, liquidaciones, certificados..."
            aria-label="Buscar"
          />
        </div>

        {/* Results */}
        <div className="max-h-80 overflow-y-auto p-2" role="listbox">
          {results.map((item, i) => (
            <button
              key={item.id}
              role="option"
              aria-selected={i === activeIndex}
              className={cn(
                'w-full flex items-center gap-3 px-3 py-2.5 rounded-md text-left transition-colors',
                i === activeIndex ? 'bg-[var(--g-surface-muted)]' : ''
              )}
              onClick={() => { navigate(item.href); setOpen(false); }}
            >
              <TypeIcon className="h-4 w-4 text-[var(--g-text-secondary)]" />
              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium text-[var(--g-text-primary)] truncate">{item.title}</p>
                <p className="text-xs text-[var(--g-text-secondary)] truncate">{item.subtitle}</p>
              </div>
              <Badge variant={typeConfig[item.type].badgeVariant} className="text-[10px]">
                {typeConfig[item.type].label}
              </Badge>
            </button>
          ))}
        </div>

        {/* Footer */}
        <div className="flex items-center justify-between px-4 py-2 border-t border-[var(--g-border-subtle)] text-xs text-[var(--g-text-secondary)]">
          <span>ESC para cerrar</span>
          <span>{results.length} resultados</span>
        </div>
      </div>
    </div>
  ) : null;
}
```

---

## Info Panel (Dismissible)

### Variantes

| Variante | Icono | Borde | Fondo | Uso |
|----------|-------|-------|-------|-----|
| `info` | Info | `--status-info` | `--g-surface-subtle` | Información contextual |
| `tip` | Lightbulb | `--g-brand-3308` | `--g-sec-100` | Consejos y mejores prácticas |
| `warning` | AlertTriangle | `--status-error` | error/10 | Advertencias |

### Implementación

```tsx
import { useState, useEffect } from 'react';
import { Info, Lightbulb, AlertTriangle, X } from 'lucide-react';
import { cn } from '@/lib/utils';

type InfoPanelVariant = 'info' | 'tip' | 'warning';

interface InfoPanelProps {
  children: React.ReactNode;
  variant?: InfoPanelVariant;
  icon?: React.ElementType;
  dismissible?: boolean;
  dismissKey?: string;
  className?: string;
}

const variantConfig = {
  info: {
    icon: Info,
    borderColor: 'var(--status-info)',
    bgColor: 'var(--g-surface-subtle)',
    iconColor: 'var(--status-info)',
  },
  tip: {
    icon: Lightbulb,
    borderColor: 'var(--g-brand-3308)',
    bgColor: 'var(--g-sec-100)',
    iconColor: 'var(--g-brand-3308)',
  },
  warning: {
    icon: AlertTriangle,
    borderColor: 'var(--status-error)',
    bgColor: 'hsl(0, 84%, 60%, 0.08)',
    iconColor: 'var(--status-error)',
  },
};

export function InfoPanel({
  children,
  variant = 'info',
  icon,
  dismissible = false,
  dismissKey,
  className,
}: InfoPanelProps) {
  const [dismissed, setDismissed] = useState(false);
  const config = variantConfig[variant];
  const Icon = icon || config.icon;

  useEffect(() => {
    if (dismissKey) {
      const stored = localStorage.getItem(`liquida360:dismiss:${dismissKey}`);
      if (stored === 'true') setDismissed(true);
    }
  }, [dismissKey]);

  if (dismissed) return null;

  const handleDismiss = () => {
    setDismissed(true);
    if (dismissKey) localStorage.setItem(`liquida360:dismiss:${dismissKey}`, 'true');
  };

  return (
    <div
      className={cn('flex gap-3 p-4', className)}
      style={{
        backgroundColor: config.bgColor,
        borderLeft: `4px solid ${config.borderColor}`,
        borderRadius: 'var(--g-radius-md)',
      }}
      role="note"
    >
      <Icon className="h-5 w-5 shrink-0" style={{ color: config.iconColor }} />
      <div className="flex-1 text-sm text-[var(--g-text-secondary)]">{children}</div>
      {dismissible && (
        <button
          onClick={handleDismiss}
          className="p-1 shrink-0 text-[var(--g-text-secondary)] hover:bg-black/5 rounded transition-colors"
          aria-label="Cerrar"
        >
          <X className="h-4 w-4" />
        </button>
      )}
    </div>
  );
}
```

---

## Table Toolbar

### Props

```tsx
interface TableToolbarProps {
  searchValue: string;
  onSearchChange: (value: string) => void;
  searchPlaceholder?: string;
  statusOptions?: { value: string; label: string }[];
  statusValue?: string;
  onStatusChange?: (value: string) => void;
  dateRange?: { from: string; to: string };
  onDateRangeChange?: (range: { from: string; to: string }) => void;
  onExport?: () => void;
  exportLabel?: string;
  totalRecords: number;
  recordLabel?: string;
}
```

### Layout

```
+-------------------------------------------------------------------+
| [🔍 Search input  ]  [Status ▼]  [From] [To] [Clear]  [↓ Export] |
| 42 registros                                                       |
+-------------------------------------------------------------------+
```

### Implementación

```tsx
export function TableToolbar({
  searchValue, onSearchChange, searchPlaceholder = 'Buscar...',
  statusOptions, statusValue, onStatusChange,
  dateRange, onDateRangeChange,
  onExport, exportLabel = 'Exportar',
  totalRecords, recordLabel = 'registros',
}: TableToolbarProps) {
  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-center gap-3">
        {/* Search */}
        <div className="relative flex-1 max-w-sm">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-[var(--g-text-secondary)]" />
          <Input
            value={searchValue}
            onChange={(e) => onSearchChange(e.target.value)}
            placeholder={searchPlaceholder}
            className="pl-9"
          />
        </div>

        {/* Status filter */}
        {statusOptions && onStatusChange && (
          <Select value={statusValue} onChange={onStatusChange} className="w-48">
            <option value="">Todos los estados</option>
            {statusOptions.map(opt => (
              <option key={opt.value} value={opt.value}>{opt.label}</option>
            ))}
          </Select>
        )}

        {/* Date range */}
        {dateRange && onDateRangeChange && (
          <DateRangeFilter range={dateRange} onChange={onDateRangeChange} />
        )}

        {/* Export */}
        {onExport && (
          <Button variant="outline" size="sm" onClick={onExport}>
            <Download className="h-4 w-4" />
            {exportLabel}
          </Button>
        )}
      </div>

      <p className="text-sm text-[var(--g-text-secondary)]">
        {totalRecords} {recordLabel}
      </p>
    </div>
  );
}
```

---

## Empty State

### Patrón

```tsx
interface EmptyStateProps {
  icon?: React.ElementType;
  title: string;
  description?: string;
  actionLabel?: string;
  onAction?: () => void;
  className?: string;
}

export function EmptyState({
  icon: Icon = Inbox,
  title,
  description,
  actionLabel,
  onAction,
  className,
}: EmptyStateProps) {
  return (
    <div className={cn('flex flex-col items-center justify-center py-12 px-4 text-center', className)}>
      <div
        className="h-12 w-12 flex items-center justify-center mb-4"
        style={{
          backgroundColor: 'var(--g-surface-muted)',
          borderRadius: 'var(--g-radius-full)',
        }}
      >
        <Icon className="h-6 w-6 text-[var(--g-text-secondary)]" />
      </div>

      <h3
        className="font-semibold text-[var(--g-text-primary)] mb-1"
        style={{ fontSize: 'var(--g-text-h4)' }}
      >
        {title}
      </h3>

      {description && (
        <p className="text-sm text-[var(--g-text-secondary)] max-w-sm mb-4">
          {description}
        </p>
      )}

      {actionLabel && onAction && (
        <Button onClick={onAction} className="mt-4">
          <Plus className="h-4 w-4" />
          {actionLabel}
        </Button>
      )}
    </div>
  );
}
```

---

## Error Boundary

### Patrón (Class Component)

```tsx
interface ErrorBoundaryProps {
  children: React.ReactNode;
  fallback?: React.ReactNode;
}

interface ErrorBoundaryState {
  hasError: boolean;
  error?: Error;
}

export class ErrorBoundary extends React.Component<ErrorBoundaryProps, ErrorBoundaryState> {
  state: ErrorBoundaryState = { hasError: false };

  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    console.error('[ErrorBoundary]', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || (
        <div className="flex flex-col items-center justify-center min-h-[400px] p-8" role="alert">
          <div
            className="h-16 w-16 flex items-center justify-center mb-6"
            style={{
              backgroundColor: 'hsl(0, 84%, 60%, 0.08)',
              borderRadius: 'var(--g-radius-full)',
            }}
          >
            <AlertTriangle className="h-8 w-8" style={{ color: 'var(--status-error)' }} />
          </div>
          <h2
            className="font-bold text-[var(--g-text-primary)] mb-2"
            style={{ fontSize: 'var(--g-text-h3)' }}
          >
            Ha ocurrido un error
          </h2>
          <p className="text-sm text-[var(--g-text-secondary)] mb-6 text-center max-w-md">
            Algo no ha ido bien. Intenta recargar la página.
          </p>
          {this.state.error?.message && (
            <pre className="text-xs font-mono text-[var(--g-text-secondary)] opacity-60 mb-6 max-w-md text-center">
              {this.state.error.message}
            </pre>
          )}
          <Button onClick={() => window.location.reload()}>
            <RotateCcw className="h-4 w-4" />
            Recargar página
          </Button>
        </div>
      );
    }

    return this.props.children;
  }
}
```

---

## Breadcrumbs

### Patrón

```tsx
interface BreadcrumbItem {
  label: string;
  href?: string;
}

export function Breadcrumbs({ items }: { items: BreadcrumbItem[] }) {
  return (
    <nav aria-label="Breadcrumb">
      <ol className="flex items-center gap-1.5 text-sm">
        {items.map((item, i) => (
          <li key={i} className="flex items-center gap-1.5">
            {i > 0 && <ChevronRight className="h-3.5 w-3.5 text-[var(--g-text-secondary)]" />}
            {item.href && i < items.length - 1 ? (
              <a
                href={item.href}
                className="text-[var(--g-text-secondary)] hover:text-[var(--g-text-primary)] transition-colors"
              >
                {item.label}
              </a>
            ) : (
              <span
                className="text-[var(--g-text-primary)] font-medium"
                aria-current={i === items.length - 1 ? 'page' : undefined}
              >
                {item.label}
              </span>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}
```

---

## InfoTip (Tooltip)

### Patrón

```tsx
interface InfoTipProps {
  content: string;
  position?: 'top' | 'bottom' | 'left' | 'right';
  children?: React.ReactNode;
}

export function InfoTip({ content, position = 'top', children }: InfoTipProps) {
  const [visible, setVisible] = useState(false);

  return (
    <span
      className="relative inline-flex"
      onMouseEnter={() => setVisible(true)}
      onMouseLeave={() => setVisible(false)}
    >
      {children || (
        <button
          type="button"
          className="text-[var(--g-text-secondary)] hover:text-[var(--g-text-primary)] transition-colors"
          aria-label="Más información"
        >
          <HelpCircle className="h-4 w-4" />
        </button>
      )}
      {visible && (
        <div
          className="absolute z-50 animate-tooltip-enter"
          role="tooltip"
          style={{ /* position based on `position` prop */ }}
        >
          <div
            className="px-3 py-2 text-xs text-[var(--g-text-inverse)] max-w-xs leading-relaxed"
            style={{
              backgroundColor: 'var(--g-text-primary)',
              borderRadius: 'var(--g-radius-sm)',
              boxShadow: 'var(--g-shadow-dropdown)',
            }}
          >
            {content}
          </div>
        </div>
      )}
      <span className="sr-only">{content}</span>
    </span>
  );
}
```

---

## CSV Export Utility

### Patrón

```tsx
interface ExportColumn<T> {
  header: string;
  accessor: keyof T | ((row: T) => string);
}

export function exportTableToCsv<T>(
  data: T[],
  columns: ExportColumn<T>[],
  filename: string
) {
  const headers = columns.map(c => c.header).join(',');
  const rows = data.map(row =>
    columns.map(col => {
      const value = typeof col.accessor === 'function'
        ? col.accessor(row)
        : String(row[col.accessor] ?? '');
      return `"${value.replace(/"/g, '""')}"`;
    }).join(',')
  );

  const csv = [headers, ...rows].join('\n');
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = `${filename}.csv`;
  link.click();
  URL.revokeObjectURL(url);
}
```

---

## Loading States

### SuspenseLoader

```tsx
import { Loader2 } from 'lucide-react';

export function SuspenseLoader() {
  return (
    <div className="flex items-center justify-center min-h-[200px]">
      <div className="flex flex-col items-center gap-3">
        <Loader2
          className="h-8 w-8 animate-spin"
          style={{ color: 'var(--g-brand-3308)' }}
        />
        <p className="text-sm text-[var(--g-text-secondary)]" style={{ fontFamily: 'var(--g-font-family)' }}>
          Cargando...
        </p>
      </div>
    </div>
  );
}
```

### Card Skeleton

```tsx
function CardSkeleton() {
  return (
    <div
      className="border p-6"
      style={{
        backgroundColor: 'var(--g-surface-card)',
        borderColor: 'var(--g-border-default)',
        borderRadius: 'var(--g-radius-lg)',
      }}
    >
      <div className="skeleton h-4 w-3/4 rounded mb-4" />
      <div className="skeleton h-3 w-full rounded mb-2" />
      <div className="skeleton h-3 w-5/6 rounded mb-2" />
      <div className="skeleton h-3 w-2/3 rounded" />
    </div>
  );
}
```

### Table Skeleton

```tsx
function TableSkeleton({ rows = 5 }: { rows?: number }) {
  return (
    <div className="space-y-2">
      <div className="skeleton h-10 w-full rounded" />
      {Array.from({ length: rows }).map((_, i) => (
        <div key={i} className="skeleton h-12 w-full rounded" />
      ))}
    </div>
  );
}
```

---

## Iconografía por Dominio

```tsx
import {
  // Navegación
  LayoutDashboard, Users, FileCheck, Receipt, CreditCard, Bell, Settings,

  // Acciones
  Plus, Pencil, Trash2, Search, Filter, Download, Upload, Copy, Eye,

  // Estados
  CheckCircle2, AlertTriangle, XCircle, Info, Clock, Loader2, Ban,

  // UI
  X, Menu, ChevronRight, ChevronLeft, ChevronDown, ArrowUpDown,
  LogOut, Shield, HelpCircle, RotateCcw, Inbox, Lightbulb,

  // Dominio LegalTech
  Building2, Calendar, FileText, GanttChart, Network,
  Briefcase, UserCheck, ShieldCheck,
} from 'lucide-react';
```

### Regla de Tamaños

| Contexto | Clase | px |
|----------|-------|----|
| Badge icons | `h-3 w-3` | 12 |
| Buttons, inputs, inline | `h-4 w-4` | 16 |
| Nav items, form icons | `h-5 w-5` | 20 |
| Page headers | `h-6 w-6` | 24 |
| Empty states, features | `h-8 w-8` | 32 |
| Hero sections | `h-12 w-12` | 48 |

---

## Workstream Badge

### Patrón con tokens CSS

```tsx
const workstreamConfig: Record<string, { label: string; token: string }> = {
  legal: { label: 'Legal', token: '--ws-legal' },
  financiero: { label: 'Financiero', token: '--ws-financiero' },
  tecnico: { label: 'Técnico', token: '--ws-tecnico' },
  comercial: { label: 'Comercial', token: '--ws-comercial' },
  regulatorio: { label: 'Regulatorio', token: '--ws-regulatorio' },
  general: { label: 'General', token: '--ws-general' },
  closing: { label: 'Closing', token: '--ws-closing' },
};

function WorkstreamBadge({ type }: { type: string }) {
  const config = workstreamConfig[type];
  if (!config) return null;

  return (
    <span
      className="inline-flex items-center px-2 py-1 text-xs font-medium border"
      style={{
        backgroundColor: `color-mix(in srgb, var(${config.token}) 10%, transparent)`,
        borderColor: `color-mix(in srgb, var(${config.token}) 30%, transparent)`,
        color: `var(${config.token})`,
        borderRadius: 'var(--g-radius-sm)',
      }}
    >
      {config.label}
    </span>
  );
}
```
