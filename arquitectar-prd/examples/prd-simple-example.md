# PRD: Sistema de Prioridad de Tareas

## Introducción

Añadir niveles de prioridad a las tareas para que los usuarios puedan enfocarse en lo más importante. Las tareas pueden marcarse como alta, media o baja prioridad, con indicadores visuales y filtrado.

## Objetivos

- Permitir asignar prioridad (alta/media/baja) a cualquier tarea
- Proporcionar diferenciación visual clara entre niveles
- Habilitar filtrado y ordenación por prioridad
- Asignar prioridad media por defecto a tareas nuevas

## Historias de Usuario

### US-001: Añadir campo de prioridad a base de datos
**Descripción:** Como desarrollador, necesito almacenar la prioridad de tareas para que persista entre sesiones.

**Criterios de Aceptación:**
- [ ] Columna `priority` añadida a tabla `tasks`: 'high' | 'medium' | 'low' (default 'medium')
- [ ] Migración generada y ejecutada correctamente
- [ ] `npm run typecheck` pasa

### US-002: Mostrar indicador de prioridad en tarjetas
**Descripción:** Como usuario, quiero ver la prioridad de cada tarea de un vistazo para saber qué requiere atención primero.

**Criterios de Aceptación:**
- [ ] Cada tarjeta muestra badge de color (rojo=alta, amarillo=media, gris=baja)
- [ ] Badge incluye icono: 🔴 alta, 🟡 media, ⚪ baja
- [ ] Prioridad visible sin hover ni click
- [ ] `npm run typecheck` pasa
- [ ] Verificar en navegador usando skill dev-browser

### US-003: Añadir selector de prioridad al editar tarea
**Descripción:** Como usuario, quiero cambiar la prioridad de una tarea cuando la edito.

**Criterios de Aceptación:**
- [ ] Dropdown de prioridad en modal de edición
- [ ] Muestra prioridad actual como seleccionada
- [ ] Guarda inmediatamente al cambiar selección
- [ ] `npm run typecheck` pasa
- [ ] Verificar en navegador usando skill dev-browser

### US-004: Filtrar tareas por prioridad
**Descripción:** Como usuario, quiero filtrar la lista de tareas para ver solo las de alta prioridad cuando estoy enfocado.

**Criterios de Aceptación:**
- [ ] Dropdown de filtro con opciones: Todas | Alta | Media | Baja
- [ ] Filtro persiste en parámetros de URL
- [ ] Mensaje de estado vacío cuando no hay tareas que coincidan
- [ ] `npm run typecheck` pasa
- [ ] Verificar en navegador usando skill dev-browser

## Requisitos Funcionales

- **FR-1:** Añadir campo `priority` a tabla tasks ('high' | 'medium' | 'low', default 'medium')
- **FR-2:** Mostrar badge de prioridad con color en cada tarjeta de tarea
- **FR-3:** Incluir selector de prioridad en modal de edición de tarea
- **FR-4:** Añadir dropdown de filtro por prioridad en header de lista
- **FR-5:** Ordenar por prioridad dentro de cada columna de estado (alta → media → baja)

## No-Objetivos (Fuera de Scope)

- Sin notificaciones o recordatorios basados en prioridad
- Sin asignación automática de prioridad por fecha de vencimiento
- Sin herencia de prioridad para subtareas

## Consideraciones Técnicas

- Reutilizar componente `Badge` existente con variantes de color
- Estado de filtro gestionado via URL search params
- Prioridad almacenada en DB, no calculada

## Métricas de Éxito

- Usuarios pueden cambiar prioridad en < 2 clicks
- Tareas de alta prioridad inmediatamente visibles arriba de listas
- Sin regresión en rendimiento de lista de tareas

## Preguntas Abiertas

- [ ] ¿Debería la prioridad afectar el ordenamiento dentro de una columna?
- [ ] ¿Añadir atajos de teclado para cambiar prioridad?
