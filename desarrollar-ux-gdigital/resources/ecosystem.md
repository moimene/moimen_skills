# Ecosistema de Legitimidad - g-digital

Guía de uso del triángulo de legitimidad para interfaces g-digital.

## Triángulo de Legitimidad

### Arquitectura de Marca

```
        ┌─────────────────────────────────────┐
        │            GARRIGUES                │
        │    Autoridad jurídica (marco)       │
        │    • 125+ años de historia          │
        │    • Despacho Nº1 en España         │
        │    • Presencia internacional        │
        └─────────────────┬───────────────────┘
                          │
        ┌─────────────────┴───────────────────┐
        │            g-digital                │
        │   Capacidad de producto (acción)    │
        │    • Innovación + seguridad         │
        │    • Operador tecnológico           │
        │    • Productos legaltech            │
        └─────────────────┬───────────────────┘
                          │
        ┌─────────────────┴───────────────────┐
        │            EADTrust                 │
        │   Infraestructura regulada (cierre) │
        │    • QTSP eIDAS                     │
        │    • ENS Alto                       │
        │    • ISO 27001/9001                 │
        └─────────────────────────────────────┘
```

---

## Uso en Interfaces

### Header

```jsx
// Siempre mostrar pertenencia a Garrigues
<header className="border-b border-gray-200 bg-white">
  <div className="flex items-center justify-between max-w-6xl mx-auto px-6 py-4">
    
    {/* Logo g-digital */}
    <div className="flex items-center gap-3">
      <img src="/logos/gdigital.svg" alt="g-digital" className="h-8" />
    </div>

    {/* Badge de pertenencia */}
    <div className="flex items-center gap-2 text-sm text-gray-500">
      <span>Parte de</span>
      <img src="/logos/garrigues.svg" alt="Garrigues" className="h-5" />
    </div>
    
  </div>
</header>
```

### Footer

```jsx
// Mostrar triángulo completo en footer
<footer className="bg-gray-900 text-white py-12">
  <div className="max-w-6xl mx-auto px-6">
    
    {/* Ecosistema */}
    <div className="grid md:grid-cols-3 gap-8 mb-8">
      
      {/* Garrigues */}
      <div className="text-center">
        <img src="/logos/garrigues-white.svg" alt="Garrigues" className="h-6 mx-auto mb-3" />
        <p className="text-sm text-gray-400">Autoridad jurídica</p>
      </div>

      {/* g-digital */}
      <div className="text-center">
        <img src="/logos/gdigital-white.svg" alt="g-digital" className="h-6 mx-auto mb-3" />
        <p className="text-sm text-gray-400">Innovación con seguridad</p>
      </div>

      {/* EADTrust */}
      <div className="text-center">
        <img src="/logos/eadtrust-white.svg" alt="EADTrust" className="h-6 mx-auto mb-3" />
        <p className="text-sm text-gray-400">Infraestructura certificada</p>
      </div>

    </div>

    {/* Regulación */}
    <p className="text-xs text-gray-500 text-center">
      eIDAS | ENS Alto | ISO 27001 | Azure EU Sovereign Cloud
    </p>

  </div>
</footer>
```

---

## Partners Tecnológicos

### Lista de Partners a Mostrar

| Partner | Tipo | Relevancia |
|---------|------|------------|
| Microsoft Azure | Cloud | EU Sovereign Cloud |
| Oracle | Enterprise | Base de datos, ERP |
| EADTrust | QTSP | Certificación |
| Garrigues | Legal | Marco institucional |

### Implementación

```jsx
const partners = [
  { id: 'azure', name: 'Microsoft Azure', logo: '/partners/azure.svg' },
  { id: 'oracle', name: 'Oracle', logo: '/partners/oracle.svg' },
  { id: 'eadtrust', name: 'EADTrust', logo: '/partners/eadtrust.svg' },
];

<section className="py-12 bg-gray-50">
  <div className="max-w-6xl mx-auto px-6">
    <p className="text-sm text-gray-500 text-center mb-6">
      Entornos EU Sovereign Cloud
    </p>
    <div className="gd-trust-grid">
      {partners.map(p => (
        <img key={p.id} src={p.logo} alt={p.name} />
      ))}
    </div>
  </div>
</section>
```

---

## Reglas de Jerarquía

1. **Garrigues** siempre presente como marco
2. **g-digital** en primer plano de acción
3. **EADTrust** como cierre de confianza técnica
4. **Partners** como validación de ecosistema

---

## Mensajes de Legitimación

| Contexto | Mensaje |
|----------|---------|
| Header | "Parte del Grupo Garrigues" |
| Hero | "Innovación con seguridad jurídica" |
| About | "Operador tecnológico del Grupo Garrigues" |
| Trust Section | "Infraestructura certificada por EADTrust" |
| Footer | Links a Garrigues + EADTrust |
