# Ejemplo: Dashboard de Servicios QTSP

Dashboard institucional para portal de servicios de confianza cualificados.

## Código Completo

```tsx
import { 
  Shield, 
  FileSignature, 
  Clock, 
  CheckCircle,
  ExternalLink,
  ChevronRight
} from 'lucide-react';

// Servicios QTSP disponibles
const services = [
  {
    id: 'qes',
    icon: FileSignature,
    title: 'Firma Electrónica Cualificada',
    description: 'Servicio de firma electrónica con plena equivalencia legal al documento firmado manuscritamente.',
    regulation: 'Art. 25-34 Reg. (UE) 910/2014',
    status: 'active'
  },
  {
    id: 'qtsa',
    icon: Clock,
    title: 'Sello de Tiempo Cualificado',
    description: 'Vinculación fiable de datos a un instante concreto, constituyendo prueba de existencia.',
    regulation: 'Art. 41-42 Reg. (UE) 910/2014',
    status: 'active'
  },
  {
    id: 'qcerts',
    icon: Shield,
    title: 'Certificados Cualificados',
    description: 'Emisión de certificados cualificados de firma electrónica y sello electrónico.',
    regulation: 'Anexos I-III Reg. (UE) 910/2014',
    status: 'active'
  }
];

const certifications = [
  { id: 'eidas', name: 'QTSP eIDAS', logo: '/certs/eu-trust-mark.png' },
  { id: 'ens', name: 'ENS Alto', logo: '/certs/ens.png' },
  { id: 'iso27001', name: 'ISO 27001', logo: '/certs/iso27001.png' },
  { id: 'iso9001', name: 'ISO 9001', logo: '/certs/iso9001.png' }
];

export function QTSPDashboard() {
  return (
    <div className="min-h-screen bg-[var(--ead-surface-page)]">
      {/* Header institucional */}
      <header className="bg-[var(--ead-surface-card)] border-b border-[var(--ead-border-color)]">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Shield className="h-8 w-8 text-[var(--ead-blue-primary)]" />
            <div>
              <h1 className="text-lg font-semibold text-[var(--ead-gray-dark)]">
                EADTrust
              </h1>
              <p className="text-xs text-[var(--ead-gray-medium)]">
                Prestador de Servicios de Confianza Cualificado
              </p>
            </div>
          </div>
          
          {/* Badge eIDAS en header */}
          <div className="flex items-center gap-2 px-3 py-1.5 bg-[var(--ead-blue-light)] rounded-md">
            <img src="/certs/eu-trust-mark.png" alt="eIDAS" className="h-5" />
            <span className="text-xs font-medium text-[var(--ead-blue-primary)]">
              QTSP Verificado
            </span>
          </div>
        </div>
      </header>

      {/* Contenido principal */}
      <main className="max-w-6xl mx-auto px-6 py-12">
        
        {/* Título de sección */}
        <div className="mb-10">
          <h2 className="text-2xl font-semibold text-[var(--ead-gray-dark)]">
            Servicios de Confianza Cualificados
          </h2>
          <p className="mt-2 text-[var(--ead-gray-medium)]">
            Servicios regulados conforme al Reglamento (UE) 910/2014 sobre identificación 
            electrónica y servicios de confianza para las transacciones electrónicas.
          </p>
        </div>

        {/* Grid de servicios */}
        <div className="grid md:grid-cols-3 gap-6 mb-12">
          {services.map(service => (
            <article 
              key={service.id}
              className="bg-[var(--ead-surface-card)] border border-[var(--ead-border-color)] rounded-lg p-6 hover:shadow-md transition-shadow"
            >
              {/* Icono */}
              <div className="w-12 h-12 rounded-lg bg-[var(--ead-blue-primary)]/10 flex items-center justify-center mb-4">
                <service.icon className="h-6 w-6 text-[var(--ead-blue-primary)]" />
              </div>

              {/* Título */}
              <h3 className="text-lg font-semibold text-[var(--ead-gray-dark)] mb-2">
                {service.title}
              </h3>

              {/* Descripción */}
              <p className="text-sm text-[var(--ead-gray-medium)] leading-relaxed mb-4">
                {service.description}
              </p>

              {/* Referencia normativa */}
              <p className="text-xs text-[var(--ead-gray-medium)] mb-4">
                <span className="font-medium">Regulación:</span> {service.regulation}
              </p>

              {/* Estado y enlace */}
              <div className="flex items-center justify-between">
                <span className="inline-flex items-center gap-1.5 px-2 py-1 bg-[var(--ead-success-light)] text-[var(--ead-success)] text-xs rounded-full">
                  <span className="w-1.5 h-1.5 rounded-full bg-current"></span>
                  Activo
                </span>
                
                <a 
                  href={`/servicios/${service.id}`}
                  className="text-sm text-[var(--ead-blue-accent)] hover:underline inline-flex items-center gap-1"
                >
                  Detalles <ChevronRight className="h-4 w-4" />
                </a>
              </div>
            </article>
          ))}
        </div>

        {/* Bloque de certificaciones */}
        <section className="bg-[var(--ead-gray-light)] border border-[var(--ead-border-color)] rounded-lg p-8">
          <h3 className="text-lg font-semibold text-[var(--ead-gray-dark)] text-center mb-6">
            Certificaciones y Acreditaciones
          </h3>
          
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {certifications.map(cert => (
              <div 
                key={cert.id}
                className="flex flex-col items-center gap-2 text-center"
              >
                <img 
                  src={cert.logo}
                  alt={cert.name}
                  className="h-12 w-auto grayscale hover:grayscale-0 transition-all cursor-pointer"
                />
                <span className="text-xs text-[var(--ead-gray-medium)]">
                  {cert.name}
                </span>
              </div>
            ))}
          </div>

          <p className="text-center text-xs text-[var(--ead-gray-medium)] mt-6">
            <a 
              href="https://eidas.ec.europa.eu/efda/tl-browser/"
              target="_blank"
              rel="noopener noreferrer"
              className="text-[var(--ead-blue-accent)] hover:underline inline-flex items-center gap-1"
            >
              Verificar en Trusted List de la UE <ExternalLink className="h-3 w-3" />
            </a>
          </p>
        </section>
      </main>

      {/* Footer institucional */}
      <footer className="border-t border-[var(--ead-border-color)] mt-16">
        <div className="max-w-6xl mx-auto px-6 py-8">
          <div className="text-xs text-[var(--ead-gray-medium)] space-y-2">
            <p>
              EADTrust S.L. – Prestador de Servicios de Confianza Cualificado inscrito 
              en el Ministerio para la Transformación Digital y la Función Pública.
            </p>
            <p>
              Regulado conforme al Reglamento (UE) 910/2014 (eIDAS) | 
              RD 311/2022 (ENS) | ISO 27001 | ISO 9001
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}
```

## Principios Aplicados

| Principio | Implementación |
|-----------|----------------|
| Azul institucional | Header, iconos, acciones |
| Colores sobrios | Solo grises y azul primario |
| Certificaciones prominentes | Sección dedicada + badge en header |
| Referencias normativas | En cada servicio y footer |
| Espacio en blanco | Padding generoso, ritmo lento |
| Copy técnico | Sin superlativos, solo regulación |
| Links a fuentes oficiales | Trusted List EU |
