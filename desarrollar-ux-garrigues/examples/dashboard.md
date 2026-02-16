# Ejemplo: Dashboard con Métricas y Tabla

Patrón de referencia basado en la implementación real de LIQUIDA360.
Demuestra: layout responsivo, cards de métricas, tabla con TanStack Table, toolbar, y badges.

## dashboard-page.tsx

```tsx
import { lazy, Suspense, useState } from 'react';
import {
  LayoutDashboard, Users, FileCheck, Receipt,
  TrendingUp, Clock, CheckCircle2, AlertTriangle,
  Plus
} from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { EmptyState } from '@/components/ui/empty-state';
import { SuspenseLoader } from '@/components/suspense-loader';

// Metric Card - Reusable pattern
interface MetricCardProps {
  icon: React.ElementType;
  title: string;
  value: string | number;
  change?: string;
  trend?: 'up' | 'down' | 'neutral';
}

function MetricCard({ icon: Icon, title, value, change, trend }: MetricCardProps) {
  return (
    <Card className="hover:border-[var(--g-brand-3308)]/30 transition-all duration-200"
      style={{ boxShadow: 'var(--g-shadow-card)' }}
    >
      <CardContent className="p-6">
        <div className="flex items-center justify-between mb-4">
          <div
            className="w-10 h-10 flex items-center justify-center"
            style={{
              backgroundColor: 'var(--g-sec-100)',
              borderRadius: 'var(--g-radius-md)',
            }}
          >
            <Icon className="h-5 w-5" style={{ color: 'var(--g-brand-3308)' }} />
          </div>
          {change && (
            <Badge
              variant={trend === 'up' ? 'success' : trend === 'down' ? 'destructive' : 'outline'}
              className="text-[10px]"
            >
              {change}
            </Badge>
          )}
        </div>
        <p className="text-sm font-medium text-[var(--g-text-secondary)] mb-1">{title}</p>
        <p className="text-2xl font-bold text-[var(--g-text-primary)]">{value}</p>
      </CardContent>
    </Card>
  );
}

// Activity Item
interface ActivityItemProps {
  icon: React.ElementType;
  variant: 'success' | 'info' | 'warning';
  title: string;
  description: string;
  time: string;
}

const activityVariants = {
  success: { bg: 'var(--status-success)', opacity: '0.1' },
  info: { bg: 'var(--g-brand-3308)', opacity: '0.1' },
  warning: { bg: 'var(--status-error)', opacity: '0.08' },
};

function ActivityItem({ icon: Icon, variant, title, description, time }: ActivityItemProps) {
  const colors = activityVariants[variant];
  return (
    <div className="flex items-start gap-4 py-4 border-b border-[var(--g-border-subtle)] last:border-0">
      <div
        className="w-8 h-8 flex items-center justify-center shrink-0"
        style={{
          backgroundColor: `color-mix(in srgb, ${colors.bg} 10%, transparent)`,
          borderRadius: 'var(--g-radius-full)',
        }}
      >
        <Icon className="h-4 w-4" style={{ color: colors.bg }} />
      </div>
      <div className="flex-1 min-w-0">
        <p className="text-sm font-medium text-[var(--g-text-primary)]">{title}</p>
        <p className="text-sm text-[var(--g-text-secondary)] truncate">{description}</p>
      </div>
      <time className="text-xs text-[var(--g-text-secondary)] shrink-0">{time}</time>
    </div>
  );
}

// Page
export function DashboardPage() {
  const navigate = useNavigate();

  return (
    <div className="animate-fade-in">
      {/* Header */}
      <header className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-2xl font-bold text-[var(--g-text-primary)]">
            Panel de Control
          </h1>
          <p className="text-sm text-[var(--g-text-secondary)] mt-1">
            Resumen de actividad y métricas clave
          </p>
        </div>
        <Button onClick={() => navigate('/liquidations/new')}>
          <Plus className="h-4 w-4" />
          Nueva Liquidación
        </Button>
      </header>

      {/* Metrics Grid */}
      <section className="mb-8">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <MetricCard
            icon={Users}
            title="Corresponsales Activos"
            value={42}
            change="+3"
            trend="up"
          />
          <MetricCard
            icon={FileCheck}
            title="Certificados por Vencer"
            value={7}
            change="30 días"
            trend="neutral"
          />
          <MetricCard
            icon={Receipt}
            title="Liquidaciones Pendientes"
            value={15}
            change="-2"
            trend="down"
          />
          <MetricCard
            icon={TrendingUp}
            title="Pagos este Mes"
            value="€284K"
            change="+12%"
            trend="up"
          />
        </div>
      </section>

      {/* Main Content */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Recent table */}
        <section className="lg:col-span-2">
          <Card>
            <CardHeader className="pb-4">
              <CardTitle>Liquidaciones Recientes</CardTitle>
            </CardHeader>
            <CardContent className="p-0">
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="bg-[var(--g-surface-subtle)]">
                      <th className="px-6 py-3 text-left text-xs font-medium text-[var(--g-text-primary)] uppercase tracking-wider">
                        Corresponsal
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-[var(--g-text-primary)] uppercase tracking-wider">
                        Estado
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-[var(--g-text-primary)] uppercase tracking-wider">
                        Importe
                      </th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-[var(--g-border-subtle)]">
                    <tr className="hover:bg-[var(--g-surface-subtle)]/50 transition-colors cursor-pointer">
                      <td className="px-6 py-4">
                        <p className="text-sm font-medium text-[var(--g-text-primary)]">
                          Baker McKenzie
                        </p>
                        <p className="text-xs text-[var(--g-text-secondary)]">LIQ-2026-0042</p>
                      </td>
                      <td className="px-6 py-4">
                        <Badge variant="success">
                          <CheckCircle2 className="h-3 w-3" />
                          Aprobada
                        </Badge>
                      </td>
                      <td className="px-6 py-4 text-sm font-medium text-[var(--g-text-primary)]">
                        €12,450.00
                      </td>
                    </tr>
                    <tr className="hover:bg-[var(--g-surface-subtle)]/50 transition-colors cursor-pointer">
                      <td className="px-6 py-4">
                        <p className="text-sm font-medium text-[var(--g-text-primary)]">
                          Freshfields Bruckhaus
                        </p>
                        <p className="text-xs text-[var(--g-text-secondary)]">LIQ-2026-0041</p>
                      </td>
                      <td className="px-6 py-4">
                        <Badge variant="warning">
                          <Clock className="h-3 w-3" />
                          Pendiente
                        </Badge>
                      </td>
                      <td className="px-6 py-4 text-sm font-medium text-[var(--g-text-primary)]">
                        €8,200.00
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </CardContent>
          </Card>
        </section>

        {/* Activity sidebar */}
        <section>
          <Card>
            <CardHeader className="pb-4">
              <CardTitle>Actividad Reciente</CardTitle>
            </CardHeader>
            <CardContent>
              <ActivityItem
                icon={CheckCircle2}
                variant="success"
                title="Pago procesado"
                description="Baker McKenzie - €12,450"
                time="Hace 2h"
              />
              <ActivityItem
                icon={Clock}
                variant="info"
                title="Certificado renovado"
                description="Uría Menéndez - Alemania"
                time="Hace 4h"
              />
              <ActivityItem
                icon={AlertTriangle}
                variant="warning"
                title="Certificado por vencer"
                description="Clifford Chance - Francia (15 días)"
                time="Hace 6h"
              />
            </CardContent>
          </Card>
        </section>
      </div>
    </div>
  );
}
```

## Puntos de Cumplimiento

### Colores
- Todos los textos usan `--g-text-primary` o `--g-text-secondary`
- Fondos usan `--g-surface-*` tokens
- Bordes usan `--g-border-*` tokens
- Estados usan `--status-*` a través de Badge variants
- Marca a través de `--g-brand-3308` y `--g-sec-*`

### Componentes
- Card composable (CardHeader + CardTitle + CardContent)
- Badge con variantes semánticas (success, warning)
- Button con icono + texto
- EmptyState disponible si no hay datos

### Layout
- Grid responsivo: `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4`
- Sidebar de actividad en 2/3 + 1/3 en desktop
- `animate-fade-in` para entrada de página

### Tabla
- Cabecera: `bg-[var(--g-surface-subtle)]` + uppercase tracking
- Celdas: text-primary para destacado, text-secondary para secundario
- Hover: `hover:bg-[var(--g-surface-subtle)]/50`
- Overflow horizontal en mobile

### Accesibilidad
- Headings semánticos (h1, h2 via CardTitle)
- `<time>` element para timestamps
- Focus visible en botones e interactivos
- Truncate con `min-w-0` para prevenir overflow
