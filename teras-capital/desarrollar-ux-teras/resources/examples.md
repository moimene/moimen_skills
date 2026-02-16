# Ejemplos de Aplicación TERAS

Implementaciones de referencia siguiendo el Brand Manual v1.0.

---

## 1. Landing Page Corporativa

```tsx
import { 
  TerasHeader, 
  TerasSection, 
  TerasHeading, 
  TerasText, 
  TerasButton,
  TerasCard,
  TerasFooter 
} from './components';

export default function LandingPage() {
  return (
    <>
      <TerasHeader 
        logo="/logos/teras-logo.svg"
        navItems={[
          { label: 'Nosotros', href: '/nosotros' },
          { label: 'Servicios', href: '/servicios' },
          { label: 'Portfolio', href: '/portfolio' },
          { label: 'Contacto', href: '/contacto' },
        ]}
      />

      {/* Hero Section - Fondo blanco, impacto por tipografía */}
      <TerasSection variant="default">
        <div style={{ maxWidth: '800px' }}>
          <TerasHeading level={1}>
            Capital privado con visión estratégica
          </TerasHeading>
          <TerasText variant="secondary" size="lg">
            Inversión enfocada en generación de valor sostenible 
            para empresas en crecimiento.
          </TerasText>
          <div style={{ marginTop: '32px', display: 'flex', gap: '16px' }}>
            <TerasButton variant="primary">Conocer más</TerasButton>
            <TerasButton variant="secondary">Contactar</TerasButton>
          </div>
        </div>
      </TerasSection>

      {/* Sección de valores - Fondo alternativo */}
      <TerasSection variant="alt">
        <TerasHeading level={2}>Nuestro enfoque</TerasHeading>
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(3, 1fr)', 
          gap: '24px',
          marginTop: '32px' 
        }}>
          <TerasCard 
            title="Rigor analítico"
            description="Evaluación exhaustiva de oportunidades con metodología probada."
          />
          <TerasCard 
            title="Visión a largo plazo"
            description="Compromiso con el crecimiento sostenible y la generación de valor."
          />
          <TerasCard 
            title="Acompañamiento activo"
            description="Participación estratégica en la gestión y toma de decisiones."
          />
        </div>
      </TerasSection>

      {/* CTA Section - Fondo Red Teras */}
      <TerasSection variant="red">
        <div style={{ textAlign: 'center' }}>
          <TerasHeading level={2}>
            ¿Tiene un proyecto que nos quiera presentar?
          </TerasHeading>
          <TerasButton 
            variant="secondary" 
            style={{ 
              marginTop: '24px',
              borderColor: '#FFFFFF',
              color: '#FFFFFF',
            }}
          >
            Iniciar conversación
          </TerasButton>
        </div>
      </TerasSection>

      <TerasFooter logoNegative="/logos/teras-logo-negative.svg">
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(4, 1fr)',
          gap: '32px' 
        }}>
          <div>
            <h4 style={{ marginBottom: '16px', fontWeight: 400 }}>Compañía</h4>
            <nav style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <a href="/nosotros" style={{ color: '#FFFFFF' }}>Nosotros</a>
              <a href="/equipo" style={{ color: '#FFFFFF' }}>Equipo</a>
              <a href="/contacto" style={{ color: '#FFFFFF' }}>Contacto</a>
            </nav>
          </div>
          {/* ... más columnas */}
        </div>
      </TerasFooter>
    </>
  );
}
```

---

## 2. Dashboard Financiero

```tsx
import { TerasCard, TerasHeading, TerasBadge } from './components';

export default function Dashboard() {
  return (
    <div style={{ 
      backgroundColor: '#F7F7F7', 
      minHeight: '100vh',
      padding: '32px' 
    }}>
      {/* Header del Dashboard */}
      <div style={{ marginBottom: '32px' }}>
        <TerasHeading level={2}>Portfolio Overview</TerasHeading>
        <p style={{ 
          fontFamily: "'Messina Serif', Georgia, serif",
          color: '#6F7173',
          marginTop: '8px'
        }}>
          Resumen de inversiones activas
        </p>
      </div>

      {/* KPIs Grid */}
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(4, 1fr)', 
        gap: '24px',
        marginBottom: '32px'
      }}>
        <TerasCard>
          <p style={{ 
            fontFamily: "'Matter', Verdana, sans-serif",
            color: '#6F7173',
            fontSize: '14px',
            marginBottom: '8px'
          }}>
            Total AUM
          </p>
          <p style={{ 
            fontFamily: "'Matter', Verdana, sans-serif",
            fontSize: '32px',
            color: '#000000'
          }}>
            €245M
          </p>
        </TerasCard>

        <TerasCard>
          <p style={{ 
            fontFamily: "'Matter', Verdana, sans-serif",
            color: '#6F7173',
            fontSize: '14px',
            marginBottom: '8px'
          }}>
            Compañías activas
          </p>
          <p style={{ 
            fontFamily: "'Matter', Verdana, sans-serif",
            fontSize: '32px',
            color: '#000000'
          }}>
            12
          </p>
        </TerasCard>

        <TerasCard>
          <p style={{ 
            fontFamily: "'Matter', Verdana, sans-serif",
            color: '#6F7173',
            fontSize: '14px',
            marginBottom: '8px'
          }}>
            IRR promedio
          </p>
          <p style={{ 
            fontFamily: "'Matter', Verdana, sans-serif",
            fontSize: '32px',
            color: '#EA3348'
          }}>
            18.5%
          </p>
        </TerasCard>

        <TerasCard>
          <p style={{ 
            fontFamily: "'Matter', Verdana, sans-serif",
            color: '#6F7173',
            fontSize: '14px',
            marginBottom: '8px'
          }}>
            Exits realizados
          </p>
          <p style={{ 
            fontFamily: "'Matter', Verdana, sans-serif",
            fontSize: '32px',
            color: '#000000'
          }}>
            5
          </p>
        </TerasCard>
      </div>

      {/* Tabla de Portfolio */}
      <TerasCard title="Inversiones actuales">
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ borderBottom: '1px solid #EBEBEB' }}>
              <th style={{ 
                textAlign: 'left', 
                padding: '12px 0',
                fontFamily: "'Matter', Verdana, sans-serif",
                fontWeight: 400,
                color: '#6F7173',
                fontSize: '14px'
              }}>
                Compañía
              </th>
              <th style={{ textAlign: 'left', padding: '12px 0', fontFamily: "'Matter', Verdana, sans-serif", fontWeight: 400, color: '#6F7173', fontSize: '14px' }}>Sector</th>
              <th style={{ textAlign: 'right', padding: '12px 0', fontFamily: "'Matter', Verdana, sans-serif", fontWeight: 400, color: '#6F7173', fontSize: '14px' }}>Inversión</th>
              <th style={{ textAlign: 'right', padding: '12px 0', fontFamily: "'Matter', Verdana, sans-serif", fontWeight: 400, color: '#6F7173', fontSize: '14px' }}>Estado</th>
            </tr>
          </thead>
          <tbody>
            <tr style={{ borderBottom: '1px solid #EBEBEB' }}>
              <td style={{ padding: '16px 0', fontFamily: "'Messina Serif', Georgia, serif" }}>Acme Tech</td>
              <td style={{ padding: '16px 0', fontFamily: "'Messina Serif', Georgia, serif", color: '#6F7173' }}>Software</td>
              <td style={{ padding: '16px 0', fontFamily: "'Messina Serif', Georgia, serif", textAlign: 'right' }}>€12.5M</td>
              <td style={{ padding: '16px 0', textAlign: 'right' }}>
                <TerasBadge variant="red">Activa</TerasBadge>
              </td>
            </tr>
            {/* ... más filas */}
          </tbody>
        </table>
      </TerasCard>
    </div>
  );
}
```

---

## 3. Informe PDF / Presentación

### Estructura de Slides

```
┌─────────────────────────────────────────┐
│ [PORTADA]                               │
│                                         │
│         TERAS LOGO (negativo)           │
│                                         │
│    Informe Trimestral Q4 2025           │
│                                         │
│ ████████████████████████████████████████│ ← Red Teras fondo
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ [CONTENIDO - FONDO BLANCO]              │
│                                         │
│ Resumen Ejecutivo                        │ ← Matter, tamaño grande
│                                         │
│ Lorem ipsum dolor sit amet...            │ ← Messina Serif, regular
│                                         │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐     │
│ │  €245M  │ │   12    │ │  18.5%  │     │
│ │   AUM   │ │ Activas │ │   IRR   │     │
│ └─────────┘ └─────────┘ └─────────┘     │
│                                         │
│                          ▲▲▲▲           │ ← Sistema T (glifos)
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ [SEPARADOR - GREY TERAS]                │
│                                         │
│         ▲                               │
│        ▲ ▲       TERAS LOGO             │ ← Sistema "bandada"
│       ▲   ▲                             │   apuntando al logo
│      ▲     ▲                            │
│                                         │
└─────────────────────────────────────────┘
```

### CSS para Documentos

```css
/* Estilos para informes/presentaciones */

.teras-doc-page {
  background: var(--teras-surface-page);
  color: var(--teras-text-primary);
  font-family: var(--teras-font-body);
  padding: 40px;
}

.teras-doc-cover {
  background: var(--teras-red);
  color: var(--teras-text-inverse);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.teras-doc-title {
  font-family: var(--teras-font-heading);
  font-size: var(--teras-text-4xl);
  margin-bottom: 16px;
}

.teras-doc-subtitle {
  font-family: var(--teras-font-body);
  font-size: var(--teras-text-lg);
  opacity: 0.9;
}

.teras-doc-section-divider {
  background: var(--teras-grey);
  padding: 60px;
  text-align: center;
  position: relative;
}
```

---

## 4. LinkedIn Posts

### Formato de Imagen

| Elemento | Especificación |
|----------|----------------|
| **Fondo** | Red Teras (`#EA3348`) para impacto |
| **Texto** | Blanco sobre rojo, tipografía Matter |
| **Logo** | Versión negativa, esquina inferior |
| **Sistema gráfico** | Glifos T direccionales como apoyo |

### Ejemplo Canvas (1200x627)

```
┌────────────────────────────────────────────────┐
│                                                │
│   ▲                                            │
│  ▲ ▲                                           │
│                                                │
│        "Inversión con                          │
│         visión estratégica"                    │  ← Matter, blanco
│                                                │
│                                                │
│                                    TERAS       │  ← Logo negativo
└────────────────────────────────────────────────┘
  Fondo: #EA3348
```

---

## 5. Tarjeta de Visita

### Anverso
```
┌─────────────────────────────┐
│                             │
│                             │
│          TERAS              │  ← Logo (mín. 20mm)
│                             │
│                             │
└─────────────────────────────┘
  Fondo: Blanco
```

### Reverso
```
┌─────────────────────────────┐
│                             │
│  María García               │  ← Matter
│  Partner                    │  ← Messina Serif, gris
│                             │
│  m.garcia@terascapital.com  │
│  +34 91 XXX XX XX           │
│                             │
│                         ▲   │  ← Glifo T decorativo
└─────────────────────────────┘
  Fondo: Blanco / Gris claro
```

---

## Checklist de Verificación por Pieza

| Pieza | Paleta | Tipografía | Sistema T | Tono | Logo |
|-------|--------|------------|-----------|------|------|
| Web | ✓ Black/Red/Grey | ✓ Matter + Messina | ✓ Como decoración | ✓ Sobrio | ✓ 150px mín |
| Informe | ✓ | ✓ | ✓ Separadores | ✓ Técnico | ✓ |
| LinkedIn | ✓ Red fondo | ✓ Matter | ✓ Direccional | ✓ Potente | ✓ Negativo |
| Tarjeta | ✓ | ✓ | ✓ Decorativo | ✓ Austero | ✓ 20mm mín |
