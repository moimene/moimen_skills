# Ejemplo: Formulario CRUD con React Hook Form + Zod

Patrón de referencia basado en la implementación real de LIQUIDA360.
Demuestra: validación Zod, React Hook Form, Dialog nativo, error handling, loading states.

## correspondent-form.tsx

```tsx
import { useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { toast } from 'sonner';
import { Loader2, Building2, Globe, Mail, Phone, AlertCircle } from 'lucide-react';
import { Dialog, DialogFooter } from '@/components/ui/dialog';
import { Input } from '@/components/ui/input';
import { Select } from '@/components/ui/select';
import { Textarea } from '@/components/ui/textarea';
import { Button } from '@/components/ui/button';
import { HelpText } from '@/components/ui/help-text';
import type { Correspondent } from '../types';

// Schema - colocado junto al formulario
const correspondentSchema = z.object({
  nombre: z
    .string()
    .min(1, 'El nombre es obligatorio')
    .max(200, 'Máximo 200 caracteres'),
  email: z
    .string()
    .email('Email no válido'),
  pais: z
    .string()
    .min(1, 'Selecciona un país de origen'),
  telefono: z
    .string()
    .optional(),
  direccion: z
    .string()
    .optional(),
  notas: z
    .string()
    .max(500, 'Máximo 500 caracteres')
    .optional(),
});

type CorrespondentFormData = z.infer<typeof correspondentSchema>;

// Props
interface CorrespondentFormProps {
  open: boolean;
  onClose: () => void;
  onSubmit: (data: CorrespondentFormData) => Promise<void>;
  initialData?: Correspondent;
  countries: { code: string; name: string }[];
}

export function CorrespondentForm({
  open,
  onClose,
  onSubmit,
  initialData,
  countries,
}: CorrespondentFormProps) {
  const isEditing = !!initialData;

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<CorrespondentFormData>({
    resolver: zodResolver(correspondentSchema),
    defaultValues: initialData
      ? {
          nombre: initialData.nombre,
          email: initialData.email,
          pais: initialData.pais,
          telefono: initialData.telefono ?? '',
          direccion: initialData.direccion ?? '',
          notas: initialData.notas ?? '',
        }
      : undefined,
  });

  // Reset form when dialog opens with new data
  useEffect(() => {
    if (open && initialData) {
      reset({
        nombre: initialData.nombre,
        email: initialData.email,
        pais: initialData.pais,
        telefono: initialData.telefono ?? '',
        direccion: initialData.direccion ?? '',
        notas: initialData.notas ?? '',
      });
    } else if (open) {
      reset();
    }
  }, [open, initialData, reset]);

  const submit = async (data: CorrespondentFormData) => {
    try {
      await onSubmit(data);
      toast.success(
        isEditing ? 'Corresponsal actualizado' : 'Corresponsal creado'
      );
      onClose();
    } catch {
      toast.error('Error al guardar', {
        description: 'Inténtalo de nuevo o contacta con soporte.',
      });
    }
  };

  return (
    <Dialog
      open={open}
      onClose={onClose}
      title={isEditing ? 'Editar Corresponsal' : 'Nuevo Corresponsal'}
      description="Los campos marcados con * son obligatorios."
    >
      <form onSubmit={handleSubmit(submit)} className="space-y-6">
        {/* Nombre */}
        <div className="space-y-2">
          <label
            htmlFor="nombre"
            className="block text-sm font-medium text-[var(--g-text-primary)]"
          >
            Nombre del despacho *
          </label>
          <div className="relative">
            <Building2 className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-[var(--g-text-secondary)]" />
            <Input
              id="nombre"
              error={!!errors.nombre}
              className="pl-10"
              placeholder="Ej: Baker McKenzie LLP"
              aria-describedby={errors.nombre ? 'nombre-error' : 'nombre-help'}
              {...register('nombre')}
            />
          </div>
          {errors.nombre ? (
            <p
              id="nombre-error"
              className="text-xs text-[var(--status-error)] flex items-center gap-1"
            >
              <AlertCircle className="h-3 w-3" />
              {errors.nombre.message}
            </p>
          ) : (
            <HelpText id="nombre-help">
              Nombre legal completo del despacho corresponsal.
            </HelpText>
          )}
        </div>

        {/* Email y País en row */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Email */}
          <div className="space-y-2">
            <label
              htmlFor="email"
              className="block text-sm font-medium text-[var(--g-text-primary)]"
            >
              Email de contacto *
            </label>
            <div className="relative">
              <Mail className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-[var(--g-text-secondary)]" />
              <Input
                id="email"
                type="email"
                error={!!errors.email}
                className="pl-10"
                placeholder="contacto@despacho.com"
                aria-describedby={errors.email ? 'email-error' : undefined}
                {...register('email')}
              />
            </div>
            {errors.email && (
              <p
                id="email-error"
                className="text-xs text-[var(--status-error)] flex items-center gap-1"
              >
                <AlertCircle className="h-3 w-3" />
                {errors.email.message}
              </p>
            )}
          </div>

          {/* País */}
          <div className="space-y-2">
            <label
              htmlFor="pais"
              className="block text-sm font-medium text-[var(--g-text-primary)]"
            >
              País de origen *
            </label>
            <div className="relative">
              <Globe className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-[var(--g-text-secondary)]" />
              <Select
                id="pais"
                error={!!errors.pais}
                className="pl-10"
                aria-describedby={errors.pais ? 'pais-error' : 'pais-help'}
                {...register('pais')}
              >
                <option value="">Selecciona un país</option>
                {countries.map((c) => (
                  <option key={c.code} value={c.code}>
                    {c.name}
                  </option>
                ))}
              </Select>
            </div>
            {errors.pais ? (
              <p
                id="pais-error"
                className="text-xs text-[var(--status-error)] flex items-center gap-1"
              >
                <AlertCircle className="h-3 w-3" />
                {errors.pais.message}
              </p>
            ) : (
              <HelpText id="pais-help">
                Determina el certificado de residencia fiscal necesario.
              </HelpText>
            )}
          </div>
        </div>

        {/* Teléfono */}
        <div className="space-y-2">
          <label
            htmlFor="telefono"
            className="block text-sm font-medium text-[var(--g-text-primary)]"
          >
            Teléfono
          </label>
          <div className="relative">
            <Phone className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-[var(--g-text-secondary)]" />
            <Input
              id="telefono"
              type="tel"
              className="pl-10"
              placeholder="+34 91 XXX XX XX"
              {...register('telefono')}
            />
          </div>
        </div>

        {/* Notas */}
        <div className="space-y-2">
          <label
            htmlFor="notas"
            className="block text-sm font-medium text-[var(--g-text-primary)]"
          >
            Notas internas
          </label>
          <Textarea
            id="notas"
            rows={3}
            placeholder="Notas opcionales sobre este corresponsal..."
            aria-describedby={errors.notas ? 'notas-error' : undefined}
            {...register('notas')}
          />
          {errors.notas && (
            <p
              id="notas-error"
              className="text-xs text-[var(--status-error)] flex items-center gap-1"
            >
              <AlertCircle className="h-3 w-3" />
              {errors.notas.message}
            </p>
          )}
        </div>
      </form>

      <DialogFooter>
        <Button variant="outline" onClick={onClose} disabled={isSubmitting}>
          Cancelar
        </Button>
        <Button
          type="submit"
          loading={isSubmitting}
          onClick={handleSubmit(submit)}
        >
          {isEditing ? 'Guardar Cambios' : 'Crear Corresponsal'}
        </Button>
      </DialogFooter>
    </Dialog>
  );
}
```

## Puntos de Cumplimiento

### Zod + React Hook Form
- Schema `correspondentSchema` colocado junto al componente
- `zodResolver` conecta validación con el formulario
- `z.infer<typeof schema>` genera el tipo automáticamente
- `reset()` en `useEffect` para sincronizar con datos iniciales

### Labels
- Siempre visibles con `htmlFor` vinculado a `id`
- Campos obligatorios marcados con `*`
- `font-medium` weight, `text-sm` size, `--g-text-primary` color
- HelpText debajo de campos que lo necesitan

### Errores
- `aria-describedby` vincula input con mensaje de error
- `aria-invalid` via prop `error` del Input
- Icono AlertCircle + texto en `--status-error`
- Se muestran debajo del campo, no en modal ni toast

### Estados
- Loading: `loading` prop en Button muestra spinner
- Disabled: opacity reducida automática
- Success/Error: toast.success / toast.error via Sonner
- Submit: deshabilita todos los controles

### Layout
- Grid responsivo para campos relacionados: `grid-cols-1 md:grid-cols-2`
- Spacing consistente: `space-y-6` entre campos, `space-y-2` label-input-error
- Iconos en inputs: `absolute left-3`, input con `pl-10`
- Footer alineado a la derecha con gap-3

### Accesibilidad
- `aria-invalid` en campos con error
- `aria-describedby` para errores y help text
- `aria-label="Cerrar"` en botón X del Dialog
- `role="dialog"` + `aria-modal="true"` via Dialog nativo
- Escape key cierra el modal (nativo de `<dialog>`)

### Composición
- Dialog encapsula open/close
- DialogFooter para acciones
- Input/Select/Textarea reutilizables con `error` prop
- HelpText como componente separado
