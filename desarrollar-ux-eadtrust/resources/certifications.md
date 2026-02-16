# Catálogo de Certificaciones - EADTrust

Guía de certificaciones y sellos oficiales para mostrar en interfaces QTSP.

## Certificaciones Principales

### eIDAS - QTSP

| Atributo | Valor |
|----------|-------|
| **Nombre** | Prestador de Servicios de Confianza Cualificado |
| **Regulación** | Reglamento (UE) 910/2014 |
| **Verificación** | [Trusted List EU](https://eidas.ec.europa.eu/efda/tl-browser/) |
| **Uso** | Obligatorio en header o footer |

```jsx
<CertBadge 
  type="eidas"
  label="QTSP eIDAS"
  regulation="Reg. (UE) 910/2014"
/>
```

---

### ENS - Esquema Nacional de Seguridad

| Atributo | Valor |
|----------|-------|
| **Nombre** | Esquema Nacional de Seguridad |
| **Nivel** | Alto / Medio / Básico |
| **Regulación** | RD 311/2022 |
| **Verificación** | CCN-CERT |

```jsx
<CertBadge 
  type="ens"
  level="alto"
  label="ENS Nivel Alto"
/>
```

---

### ISO 27001

| Atributo | Valor |
|----------|-------|
| **Nombre** | Sistema de Gestión de Seguridad de la Información |
| **Estándar** | ISO/IEC 27001:2022 |
| **Alcance** | Servicios de confianza digital |

---

### ISO 20000

| Atributo | Valor |
|----------|-------|
| **Nombre** | Sistema de Gestión de Servicios TI |
| **Estándar** | ISO/IEC 20000-1:2018 |

---

### ISO 9001

| Atributo | Valor |
|----------|-------|
| **Nombre** | Sistema de Gestión de Calidad |
| **Estándar** | ISO 9001:2015 |

---

## Componente de Certificaciones

```jsx
const certifications = [
  {
    id: 'eidas',
    name: 'QTSP eIDAS',
    logo: '/certs/eu-trust-mark.png',
    url: 'https://eidas.ec.europa.eu/efda/tl-browser/',
    regulation: 'Reg. (UE) 910/2014'
  },
  {
    id: 'ens',
    name: 'ENS Alto',
    logo: '/certs/ens-logo.png',
    url: 'https://ens.ccn.cni.es/',
    regulation: 'RD 311/2022'
  },
  {
    id: 'iso27001',
    name: 'ISO 27001',
    logo: '/certs/iso27001.png',
    url: null,
    regulation: 'ISO/IEC 27001:2022'
  },
  {
    id: 'iso20000',
    name: 'ISO 20000',
    logo: '/certs/iso20000.png',
    url: null,
    regulation: 'ISO/IEC 20000-1:2018'
  },
  {
    id: 'iso9001',
    name: 'ISO 9001',
    logo: '/certs/iso9001.png',
    url: null,
    regulation: 'ISO 9001:2015'
  }
];

export function CertificationGrid() {
  return (
    <div className="ead-cert-grid">
      {certifications.map(cert => (
        <a 
          key={cert.id}
          href={cert.url || '#'}
          target={cert.url ? '_blank' : undefined}
          rel="noopener noreferrer"
          className="flex flex-col items-center gap-2 text-center group"
          title={cert.regulation}
        >
          <img 
            src={cert.logo}
            alt={cert.name}
            className="h-12 w-auto"
          />
          <span className="text-xs text-[var(--ead-gray-medium)] group-hover:text-[var(--ead-blue-accent)]">
            {cert.name}
          </span>
        </a>
      ))}
    </div>
  );
}
```

---

## Ubicaciones Recomendadas

| Ubicación | Certificaciones |
|-----------|-----------------|
| Header | eIDAS (badge pequeño) |
| Footer | Todas (grid completo) |
| Página "Acerca de" | Todas con descripciones |
| Páginas de servicio | eIDAS + relevantes |

---

## Reglas de Uso

1. **Mostrar siempre eIDAS** en posición prominente
2. **Grayscale por defecto**, color on hover
3. **Incluir enlace** a Trusted List cuando aplique
4. **Citar regulación** en tooltip o caption
5. **No inventar certificaciones** - solo las reales
