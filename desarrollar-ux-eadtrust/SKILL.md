---
name: desarrollar-ux-eadtrust
description: Desarrolla interfaces de usuario siguiendo la identidad visual y branding de EADTrust QTSP. Úsese cuando el usuario mencione crear aplicaciones legaltech, servicios de confianza cualificados, interfaces para QTSP, certificaciones eIDAS, o cualquier UI que requiera estética institucional jurídico-técnica.
---

# Desarrollar UX Estilo EADTrust

Sistema de diseño para interfaces de Prestadores de Servicios de Confianza Cualificados (QTSP) bajo regulación eIDAS.

## Rol del Modelo

Actúas como **diseñador/a de producto especializado/a en legaltech institucional**, con experiencia en interfaces para servicios de confianza digital cualificados, regulación europea y sector público-privado.

Tu prioridad es producir interfaces que transmitan **confianza jurídica digital cualificada**, evitando cualquier estética "startup" o experimental.

---

## Cuándo Usar Esta Skill

- Crear interfaces para servicios de confianza cualificados (QTSP)
- Desarrollar aplicaciones relacionadas con eIDAS
- Implementar dashboards para certificación digital
- Diseñar portales de firma electrónica cualificada
- Crear visualizaciones de sellos de tiempo cualificados
- Implementar interfaces con certificaciones ISO/ENS visibles

---

## Posicionamiento de Marca

**Eje central:** *Confianza jurídica digital cualificada*

**Territorio:**
- Regulación europea (eIDAS)
- Sector público-privado
- Legaltech B2B

**Personalidad:**
- Institucional
- Técnica
- Sobria
- Certificadora

**Promesa:**
> Infraestructura legal robusta, auditable y reconocida oficialmente.

**Mensaje implícito:**
> "No nos creas a nosotros; créeles a los reguladores."

---

## Paleta Cromática

### Colores Principales

| Token | Valor | Uso |
|-------|-------|-----|
| `--ead-blue-primary` | #003366 | Color institucional profundo, headers, CTAs |
| `--ead-blue-dark` | #002244 | Textos destacados, sidebar |
| `--ead-blue-accent` | #0066cc | Enlaces, elementos interactivos |

### Colores de Soporte

| Token | Valor | Uso |
|-------|-------|-----|
| `--ead-white` | #ffffff | Fondos principales, limpieza visual |
| `--ead-gray-light` | #f5f7fa | Fondos secundarios, cards |
| `--ead-gray-medium` | #6b7280 | Textos secundarios |
| `--ead-gray-dark` | #374151 | Textos de cuerpo |
| `--ead-gray-border` | #e5e7eb | Bordes, separadores |

### Ausencia Deliberada

❌ **NO usar colores vivos** (rojos, naranjas, verdes llamativos)
→ Refuerza el carácter serio y no comercial.

**Lectura de marca:** "no persuadimos, certificamos"

---

## Tipografía

### Familia Principal

**Inter** (o equivalente enterprise-grade: Open Sans, Roboto)

```css
font-family: 'Inter', 'Open Sans', 'Roboto', system-ui, -apple-system, sans-serif;
```

### Características Buscadas

- Alta legibilidad en textos largos
- Neutralidad (sin rasgos identitarios fuertes)
- Excelente rendimiento en web y PDF oficiales

### Escala Tipográfica

| Elemento | Tamaño | Peso | Uso |
|----------|--------|------|-----|
| H1 | 2rem (32px) | 600 | Títulos de página |
| H2 | 1.5rem (24px) | 600 | Secciones principales |
| H3 | 1.25rem (20px) | 500 | Subsecciones |
| Body | 1rem (16px) | 400 | Texto de cuerpo |
| Small | 0.875rem (14px) | 400 | Notas, metadatos |
| Caption | 0.75rem (12px) | 400 | Etiquetas, badges |

### Reglas Tipográficas

- Interlineado amplio (1.6-1.8 para cuerpo)
- Sin tipografías decorativas o display
- La tipografía **no compite con el mensaje; lo vehicula**

---

## Uso de Certificaciones (Elemento Diferencial)

Las certificaciones son **elemento central del branding**, no decoración.

### Certificaciones a Mostrar

```jsx
// Bloque de certificaciones típico
<div className="certification-grid">
  <CertBadge type="eidas" label="QTSP eIDAS" />
  <CertBadge type="ens" label="ENS Alto" />
  <CertBadge type="iso27001" label="ISO 27001" />
  <CertBadge type="iso20000" label="ISO 20000" />
  <CertBadge type="iso9001" label="ISO 9001" />
</div>
```

### Función Estratégica

| Función | Descripción |
|---------|-------------|
| Prueba objetiva | Legitimidad demostrable |
| Reducción de fricción | Menor coste de confianza del cliente |
| Sustitución de copy | Los sellos hablan por la marca |

### Implementación Visual

```jsx
<div className="grid grid-cols-3 md:grid-cols-5 gap-4 items-center justify-center p-6 bg-[var(--ead-gray-light)] rounded-lg border border-[var(--ead-gray-border)]">
  {certifications.map(cert => (
    <div key={cert.id} className="flex flex-col items-center gap-2 text-center">
      <img 
        src={cert.logo} 
        alt={cert.name}
        className="h-12 w-auto grayscale hover:grayscale-0 transition-all"
      />
      <span className="text-xs text-[var(--ead-gray-medium)]">
        {cert.name}
      </span>
    </div>
  ))}
</div>
```

---

## Arquitectura Visual

### Principios de Diseño

| Principio | Implementación |
|-----------|----------------|
| Modular y simétrico | Grids regulares, alineación estricta |
| Espacio en blanco | Padding generoso, sin densidad excesiva |
| Ritmo visual lento | Sin animaciones agresivas |
| Navegación clara | Sin dark patterns |
| Trazabilidad | Timestamps visibles, IDs, estados |

### Layout Típico

```
┌─────────────────────────────────────────────────────────────┐
│  Logo EADTrust              Nav: Servicios | Docs | Portal  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  H1: Título claro y directo (sin superlativos)             │
│                                                             │
│  Descripción técnico-jurídica                              │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │ Servicio│  │ Servicio│  │ Servicio│  │ Servicio│        │
│  │    1    │  │    2    │  │    3    │  │    4    │        │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘        │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Certificaciones: [eIDAS] [ENS] [ISO 27001] [ISO 9001]      │
├─────────────────────────────────────────────────────────────┤
│  Footer: Enlaces legales | Referencias normativas          │
└─────────────────────────────────────────────────────────────┘
```

---

## Componentes Base

### Cards de Servicio

```jsx
<div className="bg-white border border-[var(--ead-gray-border)] rounded-lg p-6 hover:shadow-md transition-shadow">
  <div className="flex items-center gap-3 mb-4">
    <div className="w-10 h-10 rounded-lg bg-[var(--ead-blue-primary)]/10 flex items-center justify-center">
      <Icon className="h-5 w-5 text-[var(--ead-blue-primary)]" />
    </div>
    <h3 className="text-lg font-semibold text-[var(--ead-gray-dark)]">
      Firma Electrónica Cualificada
    </h3>
  </div>
  <p className="text-[var(--ead-gray-medium)] text-sm leading-relaxed">
    Servicio regulado bajo el Reglamento (UE) 910/2014 eIDAS.
  </p>
  <a href="#" className="inline-flex items-center gap-1 mt-4 text-sm text-[var(--ead-blue-accent)] hover:underline">
    Ver detalles <ChevronRight className="h-4 w-4" />
  </a>
</div>
```

### Botones

```jsx
// Primario - Institucional
<button className="px-6 py-3 bg-[var(--ead-blue-primary)] text-white font-medium rounded-lg hover:bg-[var(--ead-blue-dark)] transition-colors">
  Solicitar Servicio
</button>

// Secundario - Sobrio
<button className="px-6 py-3 bg-white border border-[var(--ead-gray-border)] text-[var(--ead-gray-dark)] font-medium rounded-lg hover:bg-[var(--ead-gray-light)] transition-colors">
  Ver Documentación
</button>

// Link - Técnico
<button className="text-[var(--ead-blue-accent)] hover:underline font-medium">
  Consultar normativa →
</button>
```

### Tablas (Datos técnicos)

```jsx
<table className="w-full border-collapse text-sm">
  <thead>
    <tr className="bg-[var(--ead-gray-light)] border-b border-[var(--ead-gray-border)]">
      <th className="px-4 py-3 text-left font-medium text-[var(--ead-gray-dark)]">
        Servicio
      </th>
      <th className="px-4 py-3 text-left font-medium text-[var(--ead-gray-dark)]">
        Regulación
      </th>
      <th className="px-4 py-3 text-left font-medium text-[var(--ead-gray-dark)]">
        Estado
      </th>
    </tr>
  </thead>
  <tbody>
    <tr className="border-b border-[var(--ead-gray-border)]">
      <td className="px-4 py-3 text-[var(--ead-gray-dark)]">
        Sello de Tiempo Cualificado
      </td>
      <td className="px-4 py-3 text-[var(--ead-gray-medium)]">
        Art. 42 Reg. (UE) 910/2014
      </td>
      <td className="px-4 py-3">
        <span className="inline-flex items-center gap-1 px-2 py-1 bg-green-50 text-green-700 text-xs rounded-full">
          <span className="w-1.5 h-1.5 rounded-full bg-green-500"></span>
          Activo
        </span>
      </td>
    </tr>
  </tbody>
</table>
```

---

## Tono Verbal y Copy

### Registro

**Jurídico-técnico institucional**

### Evitar

- ❌ Claims publicitarios ("El mejor", "Líder en")
- ❌ Superlativos emocionales
- ❌ Lenguaje de marketing/startup
- ❌ Urgencia artificial

### Usar

- ✓ Referencias normativas
- ✓ Marcos legales
- ✓ Listas oficiales
- ✓ Terminología eIDAS precisa

### Ejemplos

| ❌ Evitar | ✓ Usar |
|-----------|--------|
| "La firma digital más segura" | "Firma electrónica cualificada conforme a eIDAS" |
| "Confía en nosotros" | "Incluido en la Trusted List de la Comisión Europea" |
| "Solución innovadora" | "Prestador cualificado según Reglamento (UE) 910/2014" |

---

## Referencias Normativas (para mostrar en UI)

```jsx
const legalReferences = [
  { code: "eIDAS", text: "Reglamento (UE) 910/2014" },
  { code: "ENS", text: "RD 311/2022 – Esquema Nacional de Seguridad" },
  { code: "ISO 27001", text: "Sistema de Gestión de Seguridad de la Información" },
  { code: "LOPDGDD", text: "Ley Orgánica 3/2018 de Protección de Datos" },
];

<footer className="border-t border-[var(--ead-gray-border)] mt-12 pt-8">
  <div className="text-xs text-[var(--ead-gray-medium)]">
    <p>Prestador de Servicios de Confianza Cualificado inscrito en el Ministerio para la Transformación Digital.</p>
    <p className="mt-2">
      {legalReferences.map(ref => ref.code).join(' | ')}
    </p>
  </div>
</footer>
```

---

## Checklist de Validación

Antes de entregar código, verificar:

- [ ] ¿Colores sobrios (azul institucional, grises)?
- [ ] ¿Sin colores llamativos o "startup"?
- [ ] ¿Certificaciones visibles y prominentes?
- [ ] ¿Tipografía sans-serif limpia?
- [ ] ¿Copy jurídico-técnico (no marketiniano)?
- [ ] ¿Referencias normativas incluidas?
- [ ] ¿Mucho espacio en blanco?
- [ ] ¿Navegación clara sin dark patterns?

---

## Regla Final

> **La web habla poco y muestra mucho. Los sellos y referencias normativas son el mensaje.**

---

## Recursos

- [Tokens CSS](resources/tokens.css)
- [Paleta de Certificaciones](resources/certifications.md)
- [Trusted List EU](https://eidas.ec.europa.eu/efda/tl-browser/)
