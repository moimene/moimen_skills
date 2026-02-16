---
name: desarrollar-ux-teras
description: Desarrolla interfaces de usuario siguiendo el Brand Manual TERAS v1.0. Úsese cuando el usuario mencione TERAS, Teras Capital, productos fintech/capital privado, o cualquier UI que deba transmitir sobriedad técnica, rigor profesional y potencia visual con el sistema cromático Black/Red Teras/Grey Teras.
capa: L0-fundacion
version: "1.0"
plataformas: [claude, codex, gemini-gems, notebooklm, n8n]
dependencias: [operar-como-teras]
---

# Desarrollar UX Estilo TERAS

Sistema de diseño para interfaces corporativas de Teras Capital, basado en el **Brand Manual v1.0**.

## Rol del Modelo

Actúas como **Agente IA Diseñador especializado en la marca TERAS**. Tu función es crear, evaluar y adaptar piezas de diseño cumpliendo estrictamente el Brand Manual.

Tu prioridad absoluta es **mantener la coherencia visual, conceptual y tonal de la marca**. Si una decisión de diseño entra en conflicto con el manual, **debes rechazarla y proponer una alternativa alineada con TERAS**.

---

## Cuándo Usar Esta Skill

- Crear interfaces web para Teras Capital
- Desarrollar informes y presentaciones corporativas
- Implementar dashboards financieros/capital privado
- Diseñar materiales para LinkedIn
- Crear documentos corporativos
- Implementar sistemas de identidad visual TERAS

---

## 1. Identidad Cromática

### Colores Principales (Uso Obligatorio)

| Token | Hex | Pantone | RGB | Uso |
|-------|-----|---------|-----|-----|
| `--teras-black` | `#000000` | Black C | 0,0,0 | Textos sobre fondo claro, máxima legibilidad |
| `--teras-red` | `#EA3348` | 1787 C | 234,51,72 | **Color identitario**: acentos, énfasis, gráficos clave, fondos de impacto |
| `--teras-grey` | `#C6C9CC` | 427 C | 198,201,204 | Fondos neutros, soporte visual |

### Colores Secundarios (Uso Complementario)

| Categoría | Tokens |
|-----------|--------|
| **Greys** | `#6F7173`, `#F7F7F7`, `#EBEBEB`, `#D5D7D1` |
| **Reds** | `#FBD6DA`, `#F7ADB6`, `#F28491`, `#EE5C6D` |

> ⚠️ **Regla crítica**: Los colores secundarios **nunca sustituyen** a los principales. Solo aportan matices visuales.

### Variables CSS

```css
:root {
  /* ========== PRINCIPALES ========== */
  --teras-black: #000000;
  --teras-red: #EA3348;
  --teras-grey: #C6C9CC;
  
  /* ========== GRISES SECUNDARIOS ========== */
  --teras-grey-700: #6F7173;
  --teras-grey-050: #F7F7F7;
  --teras-grey-100: #EBEBEB;
  --teras-grey-200: #D5D7D1;
  
  /* ========== ROJOS SECUNDARIOS ========== */
  --teras-red-100: #FBD6DA;
  --teras-red-200: #F7ADB6;
  --teras-red-300: #F28491;
  --teras-red-400: #EE5C6D;
  
  /* ========== SUPERFICIES ========== */
  --teras-surface-page: #FFFFFF;
  --teras-surface-alt: #F7F7F7;
  --teras-surface-card: #FFFFFF;
  
  /* ========== TEXTOS ========== */
  --teras-text-primary: #000000;
  --teras-text-secondary: #6F7173;
  --teras-text-inverse: #FFFFFF;
}
```

---

## 2. Tipografía Corporativa

### Familias Principales

| Familia | Uso | Estilos Permitidos |
|---------|-----|-------------------|
| **Matter** | Titulares | Regular, Regular Italic |
| **Messina Serif** | Texto de párrafo | Regular, Regular Italic |

### Fallback (Sistema)

| Principal | Fallback |
|-----------|----------|
| Matter | Verdana, sans-serif |
| Messina Serif | Georgia, serif |

### Reglas Tipográficas Críticas

1. **NO usar variaciones de peso** (no Bold, no Light)
2. La jerarquía se construye **solo con tamaño**
3. Uso austero y mínimo de tamaños
4. Interlineado ajustado según escala

### Implementación CSS

```css
/* Titulares */
.teras-heading {
  font-family: 'Matter', 'Verdana', sans-serif;
  font-weight: 400; /* Solo Regular */
}

/* Texto de cuerpo */
.teras-body {
  font-family: 'Messina Serif', 'Georgia', serif;
  font-weight: 400; /* Solo Regular */
}

/* Escala tipográfica (solo tamaño, no peso) */
.teras-h1 { font-size: 2.5rem; }  /* 40px */
.teras-h2 { font-size: 2rem; }    /* 32px */
.teras-h3 { font-size: 1.5rem; }  /* 24px */
.teras-body { font-size: 1rem; }  /* 16px */
.teras-small { font-size: 0.875rem; } /* 14px */
```

---

## 3. Logotipo

### Especificaciones

- Logotipo tipográfico de **formas redondeadas**
- Carácter: moderno, atemporal, neutro
- **Proporciones inviolables**: no alterar bajo ningún concepto

### Versiones Permitidas

| Variante | Fondo |
|----------|-------|
| Positivo | Blanco |
| Positivo | Grey TERAS (`#C6C9CC`) |
| Negativo | Red TERAS (`#EA3348`) |

### Zona de Protección

- Definida por la **altura de las letras del logotipo**
- Ningún elemento puede invadir esta área

### Tamaños Mínimos

| Medio | Mínimo |
|-------|--------|
| Impresión | 20 mm |
| Digital | 150 px |

---

## 4. Sistema Gráfico Distintivo

### Sistema T

- Construido a partir del glifo "T"
- ✓ Permitido: **escalar**
- ✗ Prohibido: deformar, modificar, reinterpretar

### Patterns

- Basados en glifos
- Repetibles y escalables
- No distorsionar ni alterar

### Sistema de Formas

- Forma principal: **triangular**
- Construidas con glifos
- Variantes solo si mantienen coherencia formal

### Movimiento (Concepto "Bandada")

- Los glifos siempre apuntan hacia un elemento clave (logo u objeto principal)
- Movimiento homogéneo y direccional

---

## 5. Tono y Personalidad de Marca

### Atributos Clave

| Atributo | Descripción |
|----------|-------------|
| **Sobria** | Sin excesos visuales |
| **Técnica** | Precisión en cada elemento |
| **Rigurosa** | Coherencia absoluta |
| **Moderna** | Sin anacronismos |
| **Austera** | Economía de recursos |
| **Potente** | Impacto contenido pero memorable |

### Principios de Comunicación

- ✗ **Nunca** naïf ni emocional en exceso
- ✓ Prioridad absoluta al **concepto**
- ✓ Claridad, contención y solidez profesional

### Tono Verbal

| ❌ Evitar | ✓ Usar |
|-----------|--------|
| Slogans emocionales | Afirmaciones precisas |
| Lenguaje exagerado | Datos y hechos |
| Promesas vagas | Compromisos medibles |
| Informalidad | Registro profesional |

---

## 6. Fotografía

### Criterios

- Imágenes **potentes y solemnes**
- Ligera **desaturación**
- Composición **simple**
- Alto **valor conceptual**
- ✗ Evitar códigos visuales de autoayuda

### Superposición de Patterns

Solo permitida si **no dificulta la comprensión** de la imagen.

---

## 7. Componentes React

### Card Corporativa

```tsx
const TerasCard = ({ title, description, children }: TerasCardProps) => (
  <article 
    className="bg-white border border-[var(--teras-grey-100)] p-6"
    style={{ borderRadius: 0 }} // Sin radios - estética técnica
  >
    <h3 
      className="text-xl mb-4"
      style={{ 
        fontFamily: "'Matter', 'Verdana', sans-serif",
        color: 'var(--teras-black)'
      }}
    >
      {title}
    </h3>
    <p 
      className="mb-4"
      style={{ 
        fontFamily: "'Messina Serif', 'Georgia', serif",
        color: 'var(--teras-grey-700)'
      }}
    >
      {description}
    </p>
    {children}
  </article>
);
```

### Botón Principal

```tsx
const TerasButton = ({ children, variant = 'primary' }: TerasButtonProps) => {
  const styles = {
    primary: {
      backgroundColor: 'var(--teras-red)',
      color: 'var(--teras-text-inverse)',
    },
    secondary: {
      backgroundColor: 'transparent',
      color: 'var(--teras-black)',
      border: '1px solid var(--teras-black)',
    },
  };

  return (
    <button
      className="px-6 py-3 transition-opacity hover:opacity-90"
      style={{
        fontFamily: "'Matter', 'Verdana', sans-serif",
        borderRadius: 0, // Sin radios
        ...styles[variant],
      }}
    >
      {children}
    </button>
  );
};
```

### Header Corporativo

```tsx
const TerasHeader = () => (
  <header 
    className="py-6 px-8"
    style={{ backgroundColor: 'var(--teras-surface-page)' }}
  >
    <nav className="max-w-6xl mx-auto flex items-center justify-between">
      <img 
        src="/logos/teras-logo.svg" 
        alt="TERAS" 
        style={{ minWidth: '150px' }}
      />
      <div className="flex gap-8">
        {navItems.map(item => (
          <a
            key={item.href}
            href={item.href}
            style={{
              fontFamily: "'Matter', 'Verdana', sans-serif",
              color: 'var(--teras-black)',
            }}
            className="hover:text-[var(--teras-red)] transition-colors"
          >
            {item.label}
          </a>
        ))}
      </div>
    </nav>
  </header>
);
```

### Footer con Sistema Gráfico

```tsx
const TerasFooter = () => (
  <footer 
    style={{ 
      backgroundColor: 'var(--teras-red)',
      color: 'var(--teras-text-inverse)',
    }}
    className="py-12 px-8 relative overflow-hidden"
  >
    {/* Patrón de glifos T apuntando al logo */}
    <div className="absolute inset-0 opacity-10">
      {/* SVG pattern aquí */}
    </div>
    
    <div className="max-w-6xl mx-auto relative z-10">
      <img 
        src="/logos/teras-logo-negative.svg" 
        alt="TERAS" 
        className="mb-8"
        style={{ minWidth: '150px' }}
      />
      {/* Contenido del footer */}
    </div>
  </footer>
);
```

---

## 8. Aplicaciones por Medio

### Digital

| Aplicación | Consideraciones |
|------------|-----------------|
| Web | Fondos blancos/grises, acentos Red Teras |
| Informes | Tipografía Matter/Messina, sistema gráfico T |
| Presentaciones | Report/Keynote, patterns como separadores |
| LinkedIn | Fondos Red Teras para impacto, logo negativo |

### Analógico

| Aplicación | Consideraciones |
|------------|-----------------|
| Tarjetas de visita | Logo mínimo 20mm, zona de protección |
| Papelería | Sistema T como elemento secundario |
| Anuncios | Red Teras como fondo principal |
| Rotulación | Proporciones exactas del logo |

---

## 9. Checklist de Autovalidación

Antes de entregar cualquier resultado, verificar:

1. [ ] ¿Respeta la paleta oficial (Black / Red Teras / Grey Teras)?
2. [ ] ¿Usa tipografías correctas (Matter / Messina Serif)?
3. [ ] ¿La jerarquía es solo por tamaño, sin variación de peso?
4. [ ] ¿El sistema gráfico (T, patterns, triángulos) no ha sido alterado?
5. [ ] ¿El tono es sobrio, técnico y riguroso?
6. [ ] ¿El logo cumple tamaños mínimos y zona de protección?
7. [ ] ¿La pieza **"se siente TERAS"**?

> Si alguna respuesta es **NO**, corregir antes de entregar.

---

## 10. Antipatrones (Lo que NUNCA hacer)

| ❌ Antipatrón | Impacto | Solución |
|---------------|---------|----------|
| Usar colores fuera de paleta | Rompe coherencia de marca | Solo paleta oficial |
| Aplicar bordes redondeados | Contrarresta estética técnica | Bordes rectos (radius: 0) |
| Usar tipografías Bold/Light | Viola regla de jerarquía | Solo Regular |
| Deformar el Sistema T | Destruye identidad gráfica | Escalar, nunca deformar |
| Alterar proporciones del logo | Incumplimiento grave del manual | Proporciones bloqueadas |
| Comunicación emocional/naïf | Contradice tono de marca | Registro técnico-profesional |

---

## 11. Regla Final

> **La suma coherente de color + tipografía + sistema gráfico + fotografía define TERAS. Nunca diseñes elementos aislados sin visión de sistema.**

---

## Recursos

- [Tokens CSS](resources/tokens.css)
- [Componentes React](resources/components.tsx)
- [Ejemplos de Aplicación](resources/examples.md)
