---
name: aplicar-tdd-workflows
description: Test-Driven Development (TDD) workflows para desarrollo disciplinado con ciclo red-green-refactor, orquestación multi-agente, y revisión de código con estándares modernos de 2024/2025.
---

# Test-Driven Development (TDD) Workflows

Esta skill proporciona un framework completo para implementar Test-Driven Development utilizando el ciclo **Red-Green-Refactor** con disciplina estricta.

## Componentes

### Agentes Especializados

1. **[TDD Orchestrator](./agents/tdd-orchestrator.md)** - Orquestador maestro que coordina todo el ciclo TDD, gestiona workflows multi-agente, y asegura el cumplimiento de mejores prácticas.

2. **[Code Reviewer](./agents/code-reviewer.md)** - Experto en revisión de código con análisis AI-powered, detección de vulnerabilidades, optimización de rendimiento, y fiabilidad en producción.

### Comandos TDD

1. **`/tdd-cycle`** - Workflow completo del ciclo TDD con validación estricta
2. **`/tdd-red`** - Fase RED: Escribir tests que fallen
3. **`/tdd-green`** - Fase GREEN: Implementación mínima para pasar tests
4. **`/tdd-refactor`** - Fase REFACTOR: Mejorar código manteniendo tests verdes

## El Ciclo TDD

```
    ┌─────────────────────────────────────────┐
    │                                         │
    │   🔴 RED → 🟢 GREEN → 🔄 REFACTOR      │
    │     │         │           │             │
    │     ▼         ▼           ▼             │
    │   Escribir  Código     Mejorar          │
    │   test que  mínimo     calidad          │
    │   FALLE     que PASE   (tests verdes)   │
    │                                         │
    └─────────────────────────────────────────┘
```

## Uso Rápido

### Iniciar Ciclo TDD Completo
```
/tdd-cycle [descripción de la funcionalidad]
```
Este comando orquesta automáticamente todas las fases del TDD.

### Fase RED - Escribir Tests que Fallen
```
/tdd-red [componente o funcionalidad a testear]
```
Genera tests comprehensivos que DEBEN fallar inicialmente.

### Fase REFACTOR - Mejorar Código
```
/tdd-refactor [código a refactorizar]
```
Aplica patrones de diseño, principios SOLID, y optimizaciones manteniendo todos los tests verdes.

## Configuración de Thresholds

### Cobertura Mínima
- **Line coverage**: 80%
- **Branch coverage**: 75%
- **Critical path**: 100%

### Triggers de Refactoring
- Complejidad ciclomática > 10
- Métodos > 20 líneas
- Clases > 200 líneas
- Código duplicado > 3 líneas

## Validación por Fase

### 🔴 RED Phase Validation
- [ ] Tests escritos ANTES de implementación
- [ ] Todos los tests fallan con mensajes claros
- [ ] Fallos por implementación faltante (no errores de sintaxis)
- [ ] Ningún test pasa accidentalmente

### 🟢 GREEN Phase Validation
- [ ] Todos los tests pasan
- [ ] Sin código extra más allá de lo requerido
- [ ] Cobertura cumple umbrales mínimos
- [ ] Ningún test modificado para hacerlo pasar

### 🔄 REFACTOR Phase Validation
- [ ] Todos los tests siguen pasando
- [ ] Complejidad reducida
- [ ] Duplicación eliminada
- [ ] Performance mejorada o mantenida

## Anti-Patrones a Evitar

❌ Escribir implementación antes de tests
❌ Escribir tests que ya pasan
❌ Saltarse la fase de refactor
❌ Modificar tests para hacerlos pasar
❌ Ignorar tests fallando
❌ Escribir tests después de la implementación

## Frameworks Soportados

| Lenguaje | Frameworks |
|----------|-----------|
| JavaScript/TypeScript | Jest, Vitest, @testing-library |
| Python | pytest, Hypothesis |
| Go | testing/T, testify |
| Ruby | RSpec |
| Java | JUnit |
| C# | NUnit |

## Métricas TDD

El skill rastrea y reporta:
- ⏱️ Tiempo en cada fase (Red/Green/Refactor)
- 🔄 Número de ciclos test-implementación
- 📈 Progresión de cobertura
- 🔧 Frecuencia de refactoring
- 🐛 Tasa de escape de defectos

## Ejemplos de Uso

### Ejemplo 1: Nueva Funcionalidad
```
/tdd-cycle Implementar servicio de autenticación con JWT
```

### Ejemplo 2: Tests Específicos
```
/tdd-red UserService.authenticate() con validación de credenciales
```

### Ejemplo 3: Refactorizar Código Existente
```
/tdd-refactor OrderProcessor - extraer métodos y aplicar Strategy pattern
```

## Recursos

- **Agentes**: `./agents/` - Definiciones de agentes especializados
- **Comandos**: `./commands/` - Workflows detallados por fase

## Créditos

Basado en el plugin [tdd-workflows](https://github.com/wshobson/agents/tree/main/plugins/tdd-workflows) de wshobson/agents.
