---
name: revisar-performance-testing
description: Performance testing y code review con AI. Incluye ingeniería de performance, automatización de tests, observabilidad con OpenTelemetry, y revisión de código multi-agente con análisis de seguridad, arquitectura y rendimiento.
---

# Performance Testing & AI-Powered Code Review

Esta skill proporciona herramientas avanzadas para testing de performance, automatización de pruebas con AI, y revisión de código multi-agente.

## Componentes

### Agentes Especializados

1. **[Performance Engineer](./agents/performance-engineer.md)** - Ingeniero de performance especializado en observabilidad moderna, optimización de aplicaciones, y rendimiento de sistemas escalables.

2. **[Test Automator](./agents/test-automator.md)** - Experto en automatización de tests con frameworks modernos, tests auto-reparables con AI, y estrategias de quality engineering.

### Comandos

1. **`/ai-review`** - Revisión de código con AI combinando análisis estático, detección de vulnerabilidades, y generación de comentarios accionables.

2. **`/multi-agent-review`** - Orquestación multi-agente para revisiones comprehensivas con especialistas en seguridad, arquitectura, y performance.

## Diagrama de Capacidades

```
┌─────────────────────────────────────────────────────────────────┐
│                    Performance & Testing Suite                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────┐     ┌─────────────────────────────────┐   │
│  │ Performance     │     │ Test Automator                  │   │
│  │ Engineer        │     │                                 │   │
│  ├─────────────────┤     ├─────────────────────────────────┤   │
│  │ • Observability │     │ • TDD Red-Green-Refactor        │   │
│  │ • Profiling     │     │ • AI-Powered Testing            │   │
│  │ • Load Testing  │     │ • Self-Healing Tests            │   │
│  │ • Caching       │     │ • CI/CD Integration             │   │
│  │ • Core Web      │     │ • Property-Based Testing        │   │
│  │   Vitals        │     │ • Cross-Platform                │   │
│  └─────────────────┘     └─────────────────────────────────┘   │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ AI Code Review                                           │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │ • Static Analysis (SonarQube, CodeQL, Semgrep)          │   │
│  │ • LLM Review (Claude, GPT-4, Copilot)                   │   │
│  │ • Security (OWASP Top 10, Secret Detection)              │   │
│  │ • Performance (N+1 Detection, Scalability Analysis)      │   │
│  │ • Architecture (SOLID, Microservices Patterns)           │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Multi-Agent Review Orchestration                        │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │ • Parallel Agent Execution                              │   │
│  │ • Intelligent Conflict Resolution                        │   │
│  │ • Weighted Result Aggregation                           │   │
│  │ • Context Propagation                                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Performance Engineer Capabilities

### Observability & Monitoring
- **OpenTelemetry**: Distributed tracing, metrics collection
- **APM platforms**: DataDog, New Relic, Dynatrace, Jaeger
- **RUM**: Core Web Vitals, user experience tracking
- **Metrics**: Prometheus, Grafana, SLI/SLO tracking

### Load Testing
- **Tools**: k6, JMeter, Gatling, Locust, Artillery
- **Chaos Engineering**: Chaos Monkey, Gremlin
- **API Testing**: REST, GraphQL, WebSocket
- **Browser Testing**: Puppeteer, Playwright

### Optimization Areas
- Frontend: Core Web Vitals, bundle optimization
- Backend: API optimization, async processing
- Database: Query optimization, connection pooling
- Cloud: Auto-scaling, serverless, container optimization

## Test Automator Capabilities

### TDD Excellence
- Red-Green-Refactor cycle automation
- Chicago School & London School approaches
- Property-based TDD with Hypothesis/fast-check
- TDD metrics tracking and compliance

### AI-Powered Testing
- Self-healing tests (Testsigma, Testim, Applitools)
- AI-driven test generation
- Visual AI testing for UI validation
- Intelligent test data generation

### Framework Support
| Category | Tools |
|----------|-------|
| Browser | Playwright, Selenium |
| Mobile | Appium, XCUITest, Espresso |
| API | Postman, REST Assured, Karate |
| Performance | k6, JMeter, Gatling |
| Contract | Pact, Spring Cloud Contract |

## AI Code Review

### Analysis Pipeline
1. **Initial Triage** - Parse diff, classify changes
2. **Static Analysis** - CodeQL, SonarQube, Semgrep
3. **AI Review** - Claude/GPT contextual analysis
4. **Security Scan** - OWASP, secrets detection
5. **Performance Check** - N+1 queries, scalability
6. **Report Generation** - Structured comments

### Security Focus (OWASP 2025)
- A01: Broken Access Control
- A02: Cryptographic Failures
- A03: Injection (SQL, NoSQL, Command)
- A04: Insecure Design
- A05: Security Misconfiguration
- A06: Vulnerable Components
- A07: Authentication Failures
- A08: Data Integrity Failures
- A09: Logging Failures
- A10: SSRF

## Multi-Agent Review

### Agent Types
1. Code Quality Reviewers
2. Security Auditors
3. Architecture Specialists
4. Performance Analysts
5. Compliance Validators
6. Best Practices Experts

### Execution Strategies
```python
# Parallel execution
multi_agent_review(
    target="/path/to/project",
    agents=[
        {"type": "security-auditor", "weight": 0.3},
        {"type": "architecture-reviewer", "weight": 0.3},
        {"type": "performance-analyst", "weight": 0.2}
    ]
)

# Sequential workflow
sequential_review_workflow = [
    {"phase": "design-review", "agent": "architect-reviewer"},
    {"phase": "implementation-review", "agent": "code-quality-reviewer"},
    {"phase": "testing-review", "agent": "test-coverage-analyst"}
]
```

## Uso Rápido

### Revisión de Performance
```
/ai-review src/api/users.ts --focus=performance
```

### Revisión de Seguridad
```
/ai-review src/auth/ --focus=security
```

### Revisión Multi-Agente Completa
```
/multi-agent-review /path/to/project
```

## Integración CI/CD

```yaml
name: AI Code Review
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - name: Static Analysis
        run: |
          sonar-scanner
          semgrep scan --config=auto
          
      - name: AI-Enhanced Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: python scripts/ai_review.py --pr-number ${{ github.event.number }}
```

## Recursos

- **Agentes**: `./agents/` - Performance Engineer, Test Automator
- **Comandos**: `./commands/` - AI Review, Multi-Agent Review

## Créditos

Basado en el plugin [performance-testing-review](https://github.com/wshobson/agents/tree/main/plugins/performance-testing-review) de wshobson/agents.
