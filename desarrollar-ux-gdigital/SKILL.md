---
name: desarrollar-ux-gdigital
description: Desarrolla interfaces de usuario siguiendo la UX de g-digital, operador tecnológico del Grupo Garrigues. Úsese cuando el usuario mencione crear demostradores, productos legaltech enterprise, plataformas de innovación jurídica, o cualquier UI que deba transmitir autoridad jurídica + solvencia tecnológica dentro del ecosistema Garrigues.
---

# Desarrollar UX Estilo g-digital

Sistema de diseño para interfaces de innovación jurídica dentro del ecosistema Garrigues.

## Rol del Modelo

Actúas como **diseñador/a de producto especializado/a en legaltech enterprise**, con experiencia en interfaces para firmas de abogados, productos de innovación jurídica y entornos regulados.

Tu prioridad es producir interfaces que transmitan que **la innovación tecnológica no sustituye al abogado, sino que amplifica la seguridad jurídica del cliente**.

---

## Cuándo Usar Esta Skill

- Crear demostradores Lovable para productos g-digital
- Desarrollar interfaces de innovación jurídica
- Implementar dashboards enterprise para clientes corporativos
- Diseñar portales de soluciones legaltech
- Crear páginas institucionales del ecosistema Garrigues
- Implementar formularios de contacto cualificado

---

## Marco Estratégico

### Triángulo de Legitimidad

```
        ┌─────────────────┐
        │    GARRIGUES    │  → Autoridad jurídica (marco)
        └────────┬────────┘
                 │
        ┌────────┴────────┐
        │    g-digital    │  → Capacidad de producto (acción)
        └────────┬────────┘
                 │
        ┌────────┴────────┐
        │    EADTrust     │  → Infraestructura regulada (cierre)
        └─────────────────┘
```

### Objetivo UX Principal

> Transmitir que la innovación tecnológica **no sustituye al abogado**, sino que **amplifica la seguridad jurídica del cliente**.

### La UX Busca

| ✓ Objetivo | ❌ Evitar |
|------------|-----------|
| Credibilidad | Conversión agresiva |
| Comprensión progresiva | Autoservicio masivo |
| Predisposición al contacto cualificado | Funnels de venta |
| Relato de solvencia | Storytelling emocional |

---

## Arquitectura de la Información

### Navegación Principal

Estructura corta y controlada (lógica de firma profesional):

```
Nosotros | Soluciones | Recursos | Contacto
```

**Lo que NO hay:**
- ❌ Pricing
- ❌ Features
- ❌ Funnels explícitos
- ❌ CTAs comerciales agresivos

### Jerarquía de Lectura

1. **Quiénes somos** — Legitimación institucional
2. **Por qué existimos** — Propósito claro
3. **Cómo lo hacemos** — Capacidad de ejecución
4. **Con quién** — Ecosistema y partners
5. **Quién responde** — Personas reales

> La UX fuerza una lectura **institucional antes que comercial**.

---

## Paleta Cromática

### Colores Principales (Herencia Garrigues)

| Token | Valor | Uso |
|-------|-------|-----|
| `--gd-brand-primary` | #004438 | Pantone 3308 C - Color institucional |
| `--gd-brand-accent` | #009a77 | Acentos, estados activos |
| `--gd-brand-dark` | #003030 | Textos destacados |

### Colores de Soporte

| Token | Valor | Uso |
|-------|-------|-----|
| `--gd-white` | #ffffff | Fondos principales |
| `--gd-gray-50` | #f9fafb | Fondos secundarios |
| `--gd-gray-100` | #f3f4f6 | Cards, secciones |
| `--gd-gray-500` | #6b7280 | Textos secundarios |
| `--gd-gray-700` | #374151 | Textos de cuerpo |
| `--gd-gray-900` | #111827 | Títulos principales |

### Regla Cromática

- Fondos claros dominantes
- Color de marca solo en puntos focales
- Sin colores vivos ni llamativos
- Ritmo visual ordenado y lento

---

## Tipografía

### Familia Principal

**Sans-serif corporativa** (Montserrat, Inter, o equivalente):

```css
font-family: 'Montserrat', 'Inter', system-ui, -apple-system, sans-serif;
```

### Escala Tipográfica

| Elemento | Tamaño | Peso | Uso |
|----------|--------|------|-----|
| H1 | 2.5rem (40px) | 700 | Títulos de página |
| H2 | 2rem (32px) | 600 | Secciones principales |
| H3 | 1.5rem (24px) | 600 | Subsecciones |
| Body | 1rem (16px) | 400 | Texto de cuerpo |
| Small | 0.875rem (14px) | 400 | Notas, metadatos |

### Características

- Jerarquías claras
- Mucho espacio en blanco
- Textos explicativos, no slogans
- **Priorizar comprensión sobre impacto**

---

## Principios de Diseño Visual

| Principio | Implementación |
|-----------|----------------|
| Fondos claros | Blanco y grises muy suaves |
| Imágenes corporativas | Sobrias, no emocionales |
| Ilustraciones | Geométricas, abstractas |
| Ritmo visual | Lento y ordenado |
| Interacciones | Sin micro-interacciones innecesarias |

---

## UX de Confianza (Trust-UX)

### Elementos a Mostrar

```jsx
const trustElements = {
  institutional: ['Garrigues', 'g-digital'],
  technical: ['Azure', 'Oracle', 'EU Sovereign Cloud'],
  regulatory: ['EADTrust QTSP', 'eIDAS', 'ENS']
};
```

### Implementación

```jsx
<section className="bg-[var(--gd-gray-50)] py-12">
  <div className="max-w-6xl mx-auto px-6">
    <h3 className="text-lg font-semibold text-center text-[var(--gd-gray-700)] mb-8">
      Ecosistema de Confianza
    </h3>
    <div className="grid grid-cols-3 md:grid-cols-6 gap-8 items-center">
      {partners.map(partner => (
        <img 
          key={partner.id}
          src={partner.logo}
          alt={partner.name}
          className="h-8 w-auto mx-auto grayscale hover:grayscale-0 transition-all"
        />
      ))}
    </div>
  </div>
</section>
```

---

## UX de Personas (Human-in-the-Loop)

### Presentación del Equipo

- ✓ Fotos reales, no stock
- ✓ Roles claramente definidos
- ✓ Enlaces a perfiles profesionales
- ✓ Mensaje: "Hay personas responsables, no solo tecnología"

```jsx
<div className="grid md:grid-cols-3 gap-8">
  {team.map(member => (
    <article key={member.id} className="text-center">
      <img 
        src={member.photo}
        alt={member.name}
        className="w-24 h-24 rounded-full mx-auto mb-4 object-cover"
      />
      <h4 className="font-semibold text-[var(--gd-gray-900)]">
        {member.name}
      </h4>
      <p className="text-sm text-[var(--gd-gray-500)]">
        {member.role}
      </p>
      <a 
        href={member.linkedin}
        className="text-xs text-[var(--gd-brand-accent)] hover:underline mt-2 inline-block"
      >
        Ver perfil
      </a>
    </article>
  ))}
</div>
```

---

## Componentes Base

### Card de Solución

```jsx
<article className="bg-white border border-gray-200 rounded-xl p-6 hover:shadow-lg transition-shadow">
  {/* Icono/Ilustración */}
  <div className="w-16 h-16 rounded-lg bg-[var(--gd-brand-primary)]/10 flex items-center justify-center mb-4">
    <Icon className="h-8 w-8 text-[var(--gd-brand-primary)]" />
  </div>

  {/* Título */}
  <h3 className="text-xl font-semibold text-[var(--gd-gray-900)] mb-2">
    Firma Electrónica Cualificada
  </h3>

  {/* Descripción explicativa (no slogan) */}
  <p className="text-[var(--gd-gray-500)] leading-relaxed mb-4">
    Servicio de firma electrónica con plena equivalencia legal, 
    integrado con la infraestructura de EADTrust.
  </p>

  {/* Enlace sutil */}
  <a href="/soluciones/firma" className="text-[var(--gd-brand-accent)] font-medium hover:underline">
    Conocer más →
  </a>
</article>
```

### Sección "Nosotros" (Pieza Central)

```jsx
<section className="py-20">
  <div className="max-w-4xl mx-auto px-6 text-center">
    {/* Misión */}
    <h1 className="text-3xl md:text-4xl font-bold text-[var(--gd-gray-900)] mb-6">
      Innovación con seguridad jurídica
    </h1>
    
    {/* Legitimación institucional */}
    <p className="text-lg text-[var(--gd-gray-500)] mb-8 leading-relaxed">
      g-digital es el operador tecnológico del Grupo Garrigues, 
      el puente entre el derecho de los negocios y el producto digital.
    </p>

    {/* Badge de pertenencia */}
    <div className="inline-flex items-center gap-3 px-4 py-2 bg-[var(--gd-gray-50)] rounded-full">
      <img src="/logos/garrigues.svg" alt="Garrigues" className="h-5" />
      <span className="text-sm text-[var(--gd-gray-700)]">
        Grupo Garrigues
      </span>
    </div>
  </div>
</section>
```

### Formulario de Contacto Cualificado

```jsx
<form className="max-w-xl mx-auto space-y-6">
  {/* Campos largos que filtran, no maximizan leads */}
  <div>
    <label className="block text-sm font-medium text-[var(--gd-gray-700)] mb-2">
      Nombre completo *
    </label>
    <input 
      type="text"
      required
      className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[var(--gd-brand-primary)] focus:border-transparent"
    />
  </div>

  <div>
    <label className="block text-sm font-medium text-[var(--gd-gray-700)] mb-2">
      Empresa / Organización *
    </label>
    <input type="text" required className="..." />
  </div>

  <div>
    <label className="block text-sm font-medium text-[var(--gd-gray-700)] mb-2">
      Cargo *
    </label>
    <input type="text" required className="..." />
  </div>

  <div>
    <label className="block text-sm font-medium text-[var(--gd-gray-700)] mb-2">
      Describa su necesidad *
    </label>
    <textarea 
      rows={5}
      required
      className="w-full px-4 py-3 border border-gray-300 rounded-lg resize-none"
      placeholder="¿Qué problema busca resolver? ¿En qué contexto regulatorio opera?"
    />
  </div>

  {/* Botón formal, no comercial */}
  <button 
    type="submit"
    className="w-full py-3 bg-[var(--gd-brand-primary)] text-white font-medium rounded-lg hover:bg-[var(--gd-brand-dark)] transition-colors"
  >
    Enviar consulta
  </button>

  <p className="text-xs text-[var(--gd-gray-500)] text-center">
    Su consulta será atendida por un profesional especializado.
  </p>
</form>
```

---

## Tono Verbal y Copy

### Registro

**Institucional-explicativo**, nunca comercial.

### Evitar

- ❌ Slogans emocionales
- ❌ CTAs agresivos ("¡Empieza ya!", "Prueba gratis")
- ❌ Lenguaje de startup
- ❌ Promesas exageradas

### Usar

- ✓ Textos explicativos y progresivos
- ✓ Referencias al ecosistema Garrigues
- ✓ Terminología jurídica precisa
- ✓ "Conocer más", "Consultar", "Ver detalles"

### Ejemplos

| ❌ Evitar | ✓ Usar |
|-----------|--------|
| "La mejor plataforma de firma" | "Servicio de firma con respaldo de EADTrust" |
| "Revoluciona tu forma de trabajar" | "Amplifica la seguridad jurídica de tu organización" |
| "Empieza gratis hoy" | "Consulte con nuestro equipo" |

---

## Evaluación UX

| Dimensión | Objetivo |
|-----------|----------|
| Claridad | Muy alta |
| Confianza | Muy alta |
| Emoción | Baja (intencional) |
| Escalabilidad SaaS | Media |
| Encaje enterprise | Excelente |
| Encaje sector público | Excelente |

---

## Checklist de Validación

Antes de entregar código, verificar:

- [ ] ¿Fondo claro dominante?
- [ ] ¿Color de marca solo en puntos focales?
- [ ] ¿Ritmo visual lento y ordenado?
- [ ] ¿Textos explicativos, no slogans?
- [ ] ¿Sin CTAs comerciales agresivos?
- [ ] ¿Referencia a Garrigues/EADTrust visible?
- [ ] ¿Mucho espacio en blanco?
- [ ] ¿Fotos reales del equipo (si aplica)?

---

## Regla Final

> **La UX de g-digital no es la de una startup legaltech, sino la de un operador institucional de innovación jurídica. Está diseñada para resistir auditorías y acompañar decisiones estratégicas.**

---

## Recursos

- [Tokens CSS](resources/tokens.css)
- [Ecosistema de Legitimidad](resources/ecosystem.md)
- [Skill UX Garrigues](../desarrollar-ux-garrigues/SKILL.md)
- [Skill UX EADTrust](../desarrollar-ux-eadtrust/SKILL.md)
