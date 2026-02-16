# Plantilla: spec.md (Especificación de Track)

```markdown
# [TRACK-ID]: [Título del Track]

> **Tipo:** Feature | Bug | Tech Debt | Docs
> **Prioridad:** Alta | Media | Baja
> **Estimación:** [X] días/horas
> **Autor:** [Nombre]
> **Fecha:** [YYYY-MM-DD]

## Resumen Ejecutivo

[1-2 párrafos describiendo qué es este track y por qué es importante]

---

## Contexto y Problema

### Situación Actual
[Describir el estado actual del sistema/proceso]

### Problema/Oportunidad
[Qué problema resuelve o qué oportunidad aprovecha]

### Impacto
[Qué pasa si NO se implementa]

---

## Solución Propuesta

### Descripción
[Descripción de alto nivel de la solución]

### Enfoque Técnico
[Cómo se implementará a nivel técnico]

---

## Requisitos Funcionales

| ID | Requisito | Prioridad | Estado |
|----|-----------|-----------|--------|
| RF-01 | [Requisito detallado] | Must | [ ] |
| RF-02 | [Requisito detallado] | Must | [ ] |
| RF-03 | [Requisito detallado] | Should | [ ] |
| RF-04 | [Requisito detallado] | Could | [ ] |

---

## Requisitos No Funcionales

| ID | Requisito | Métrica |
|----|-----------|---------|
| RNF-01 | Performance | Respuesta < 200ms p95 |
| RNF-02 | Seguridad | [Especificación] |
| RNF-03 | Accesibilidad | WCAG AA |

---

## Criterios de Aceptación

- [ ] **AC-01**: [Criterio verificable y medible]
- [ ] **AC-02**: [Criterio verificable y medible]
- [ ] **AC-03**: [Criterio verificable y medible]

---

## Diseño UI/UX

### Mockups/Wireframes
[Enlaces o imágenes embebidas]

### Flujo de Usuario
```
1. Usuario hace X
2. Sistema muestra Y
3. Usuario confirma Z
4. Sistema completa acción
```

---

## Cambios de API

### Nuevos Endpoints

```
POST /api/v1/resource
Request:
{
  "field": "value"
}

Response 201:
{
  "id": "uuid",
  "field": "value"
}
```

### Modificaciones a Endpoints Existentes
[Cambios a APIs existentes]

---

## Cambios de Base de Datos

### Nuevas Tablas
```sql
CREATE TABLE new_table (
  id UUID PRIMARY KEY,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Migraciones
[Descripción de migraciones necesarias]

---

## Fuera de Alcance

- [Funcionalidad explícitamente NO incluida]
- [Caso de uso que NO se cubre]
- [Integración que se deja para futuro]

---

## Dependencias

### Tracks Relacionados
- [TRACK-ID]: [Descripción de dependencia]

### Servicios Externos
- [API/Servicio]: [Tipo de dependencia]

### Bloqueos
- [Bloqueo identificado y plan de mitigación]

---

## Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| [Riesgo 1] | Media | Alto | [Plan] |

---

## Testing

### Casos de Prueba Principales
1. [Caso happy path]
2. [Caso edge case]
3. [Caso de error]

### Datos de Prueba
[Descripción de datos necesarios para testing]

---

## Rollback

### Estrategia
[Cómo revertir los cambios si hay problemas]

### Feature Flag
[Si aplica, nombre del feature flag]

---

## Aprobaciones

| Rol | Nombre | Estado | Fecha |
|-----|--------|--------|-------|
| Product Owner | | Pendiente | |
| Tech Lead | | Pendiente | |
| QA | | Pendiente | |
```
