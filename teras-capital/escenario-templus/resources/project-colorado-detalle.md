# Project Colorado detalle — Templus

> Snapshot 31/12/2025 · Pack Miguel 10-may-2026 (Colorado Mgmt Accounts) + org chart Templus v8 14/04/2026. Estructura paralela a Templus España, gestionada vía AE Group HoldCo II S.à.r.l. (LUX).

## 1. Definición y posicionamiento

**Project Colorado** es la rama greenfield pan-europea de la línea de negocio Templus, vehiculada a través de **AE Group HoldCo II S.à r.l.** (Luxemburgo) con TCH4 como parent. Comprende **4 filiales Roosevelt** desarrolladas en paralelo en Italia, Holanda, Dinamarca y Francia. Sponsor financiero ICG sigue siendo el mismo de Templus España vía Vesta Invest, con commit conjunto 300M€.

> **CRÍTICO**: Project Colorado es la MISMA línea de negocio business_line='templus' que Templus España, no una línea separada. Sin embargo, son **entidades societarias y operativas distintas**:
> - Templus España: vía Templus CD → 7 filiales operativas España.
> - Project Colorado: vía AE Group HoldCo II → 4 Roosevelt operativas IT/NL/DK/FR.
> Para reporting interno, se consolidan bajo Templus para inversores TCH4 + TCIH + Vesta/ICG. Para análisis por activo, se desagregan.

## 2. Estructura societaria Project Colorado

```
TCH4 (Teras Capital Holding 4, S.L.)
NIF B56563398
  │
  │ 100% (rama paralela a Vesta path)
  ▼
AE Group HoldCo II S.à.r.l. (Luxemburgo)
Parent: TCH4
  │
  │ 100% en cada una de las 4 Roosevelt
  │
  ├─ 100% ▶ roosevelt-italy (Italia)
  │
  ├─ 100% ▶ roosevelt-netherlands (Holanda)
  │
  ├─ 100% ▶ roosevelt-denmark (Dinamarca)
  │
  └─ 100% ▶ roosevelt-france (Francia)
```

### Cap% MdL en Project Colorado (look-through vía TCH4)

| Nivel | Cálculo | Cap% MdL |
|---|---|---|
| MdL → TCH4 efectivo | IPN 17% + TCH2 15,60% | 32,60% |
| TCH4 → AE Group HoldCo II | 100% | 100% |
| AE Group HoldCo II → cada Roosevelt | 100% | 100% |
| **MdL → AE Group HoldCo II efectivo** | 32,60% × 100% | **32,60%** |
| **MdL → cada Roosevelt efectivo** | 32,60% × 100% × 100% | **32,60%** |

> **CRÍTICO**: el cap% MdL en Project Colorado (32,60%) es DISTINTO del cap% MdL en Templus CD España (1,62%). En Project Colorado, MdL tiene cap% sustancialmente mayor porque la cadena pasa solo por TCH4 → AE HoldCo II → Roosevelt (sin Vesta ni Templus CD diluyendo).
> Implicación fiscal: en MdL → TCH4 → AE HoldCo II: cap% 32,60% > 5% → **SÍ aplica art. 21 LIS** sobre flujos AE HoldCo II → TCH4. Pero a aguas abajo, AE HoldCo II → Roosevelt es 100%, y desde TCH4 a AE HoldCo II depende del cap% TCH4 en AE HoldCo II.

### Verificación pendiente cap% TCH4 en AE Group HoldCo II

- Org chart v8 (14/04/2026) refleja AE Group HoldCo II con parent TCH4.
- **Pendiente confirmar exactitud**: si TCH4 tiene 100% AE HoldCo II o un % menor (con co-inversores).
- Tarea pendiente #9 BD MdL: modelar cadena completa Vesta → AE HoldCo II → 4 Roosevelt y validar look-through.

## 3. Cifras 2025 — las 4 Roosevelt (Colorado Mgmt Accounts)

### roosevelt-italy (Italia)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 24.207.504 | **Mayor activo Project Colorado** |
| Revenue 2025 | 7.300.000 | **Mayor revenue Project Colorado** |
| País | Italia | |
| Notas | Líder revenue Project Colorado. Operación más madura. | |

### roosevelt-netherlands (Holanda)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 20.616.130 | |
| Revenue 2025 | — | **Sin revenue operativo aún** |
| País | Holanda | |
| Notas | Greenfield en fase build-out, sin comercialización aún. | |

### roosevelt-denmark (Dinamarca)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 18.626.624 | |
| Revenue 2025 | 1.700.000 | |
| País | Dinamarca | |
| Notas | Comercialización inicial. | |

### roosevelt-france (Francia)

| Concepto | Valor (€) | Notas |
|---|---|---|
| Activo total | 13.241.905 | |
| Revenue 2025 | 2.800.000 | |
| País | Francia | |
| Notas | Comercialización progresiva. | |

### Total Project Colorado agregado

| Concepto | Total (€) |
|---|---|
| Activo agregado | ~76.692.163 |
| Revenue 2025 agregado | ~11.800.000 |
| Filiales operativas | 4 (IT/NL/DK/FR) |
| Ratio revenue/activo agregado | 15,4% |

## 4. AE Group HoldCo II S.à.r.l. (Luxemburgo)

### Datos societarios

- **Razón social**: AE Group HoldCo II S.à.r.l.
- **Jurisdicción**: Luxemburgo (régimen LU SOPARFI).
- **Parent**: TCH4 (Teras Capital Holding 4, S.L.).
- **Cap% en cada Roosevelt**: 100%.
- **Vesta agente**: Vesta Invest actúa como agente y co-inversor del fondo ICG en Project Colorado (relación contractual pendiente confirmar exacta).

### Función como vehículo Project Colorado

- Agregador de las 4 Roosevelt filiales operativas.
- Permite consolidación LU SOPARFI con tratamiento fiscal favorable.
- Recibe capital de TCH4 (atribución MdL prorrateada) y posiblemente de Vesta/ICG.
- Reporta a Steerco Templus consolidado.

### Documentación pendiente

- Cap table exacto AE Group HoldCo II (composición TCH4 + Vesta + posibles co-inversores).
- Financing Agreement AE Group HoldCo II (si existe similar al Vesta-TCH4 8%).
- Audit firm consolidado Project Colorado.

## 5. Tarea pendiente #9 BD MdL — Templus CD orphan

### Problema identificado

- **Templus CD 178,5M€ orphan**: en BD `entity_balances` y `entities` Templus CD aparece con activo cargado (179,5M€) pero su enlace `participations` actual no refleja completamente la cadena hacia AE Group HoldCo II + 4 Roosevelt.
- La estructura Project Colorado vía AE Group HoldCo II parece ser **rama paralela TCH4** independiente de Vesta → Templus CD para la cadena España.

### Modelado pendiente

1. Confirmar si AE Group HoldCo II es:
   - Path A: TCH4 → AE Group HoldCo II → 4 Roosevelt (independiente de Vesta).
   - Path B: TCH4 → Vesta → AE Group HoldCo II → 4 Roosevelt (Vesta como matriz intermedia).
2. Crear entradas `participations` correspondientes:
   - `parent_entity_id=tch4, child_entity_id=ae-holdco-ii, ownership_pct=100` (referencia org chart v8).
   - `parent_entity_id=ae-holdco-ii, child_entity_id=roosevelt-italy, ownership_pct=100` (y similares para NL/DK/FR).
3. Determinar si Templus CD tiene alguna participación en AE Group HoldCo II o las Roosevelt (puede no tenerla — son ramas paralelas).
4. Actualizar `business_lines.templus` para reflejar correctamente cap% MdL en cada eslabón Colorado (32,60% en AE HoldCo II vs 1,62% en Templus CD).

### Owner

- CFO + CTO TERAS coordinan modelado.
- Deadline: Q4 2026.

## 6. Fiscalidad Project Colorado

### Cap% MdL > 5% → SÍ aplica exención art. 21 LIS

A diferencia de Templus España (1,62% < 5%), el cap% MdL efectivo en cada Roosevelt es **32,60%** (vía TCH4 → AE HoldCo II → Roosevelt). Por tanto:

- **TCH4 sobre AE Group HoldCo II**: cap% probable 100% (pendiente confirmar) → **SÍ aplica exención art. 21 LIS** sobre dividendos/plusvalías AE HoldCo II → TCH4.
- **IPN/TCH2 sobre TCH4**: 17% + 15,60% > 5% → **SÍ aplica exención art. 21 LIS**.
- **AE Group HoldCo II sobre cada Roosevelt**: 100% → **SÍ aplica exención** (interno LU SOPARFI).

### Implicación práctica fiscal Project Colorado

- Si TCH4 tiene 100% en AE Group HoldCo II: flujos AE HoldCo II → TCH4 → IPN/TCH2 son **exentos** art. 21 LIS.
- Diferencia con Templus España: en Templus España, TCH4 → Vesta es 2% < 5%, NO exención.
- **Implicación CRÍTICA**: Project Colorado puede tener **tratamiento fiscal mejor que Templus España** para MdL si el cap% TCH4 en AE Group HoldCo II es >5%.

### Régimen LU SOPARFI AE Group HoldCo II

- Mismo tratamiento que Vesta Invest.
- Dividendos / plusvalías entre LU + España con tratado de doble imposición.
- BEPS Pilar 2 / GloBE compliance pendiente análisis.

## 7. Governance Project Colorado

### Consejo AE Group HoldCo II

- **Cadencia**: trimestral.
- **Asistencia TERAS**: representante TCH4.
- **Asistencia ICG**: representante Vesta (si aplica directamente o como agente).
- **Agenda**: estado Project Colorado por país (IT/NL/DK/FR), Roosevelt operations.
- **Reporting**: a Steerco Templus consolidado.

### Reporting a Steerco Templus

- **Pack Miguel 10-may-2026 incluye Colorado Mgmt Accounts** como pack separado.
- Steerco Templus trimestral consolida cifras España + Colorado.
- Decisiones M&A o capex material Project Colorado requieren aprobación Steerco + TCH4 board.

### Asistencia por país

- Cada Roosevelt tiene CEO/CFO local + audit firm local (IT/NL/DK/FR).
- AE Group HoldCo II coordina supervisión a nivel pan-europeo.

## 8. Riesgos específicos Project Colorado

| # | Riesgo | P | I | Mitigante |
|---|---|---|---|---|
| 1 | Capex agregado 4 países simultáneo (~76,7M€ ya invertido + roll-out) | A | A | Quarterly review por país, AE Group HoldCo II coordina |
| 2 | Ramp-up comercial Roosevelt NL (sin revenue 2025) | M | A | Plan comercialización Q3 2026 |
| 3 | Permisos eléctricos / capacity allocation por país | M | A | Lobby + compliance proactivo |
| 4 | Tipos cambio EUR vs DKK Roosevelt Denmark | B | M | Hedge natural (commit en EUR) |
| 5 | Regulación local DC (RGPD + sectorial telco) por país | M | M | Compliance local + asesores |
| 6 | Talento técnico DC por país (escasez especialistas) | M | M | Hub modelo + soporte central |
| 7 | Geopolítica EU (capacity allocation + permisos) | B | A | Diversificación 4 países mitiga concentración |

## 9. Hitos próximos Project Colorado

| Fecha | Hito | Owner |
|---|---|---|
| Q3 2026 | Comercialización Roosevelt NL operativa | AE Group HoldCo II + Roosevelt NL mgmt |
| Q4 2026 | Modelado completo cadena Vesta → AE HoldCo II → 4 Roosevelt (tarea #9 BD MdL) | CFO + CTO TERAS |
| Q4 2026 | Audit reports 4 Roosevelt 2025 disponibles | Audit firms locales |
| 2027 | Hito comercialización Roosevelt IT (utilización >80% target) | Roosevelt IT mgmt |
| 2027 | Permisos completos Roosevelt FR fase 2 | Roosevelt FR mgmt |
| 2027-2028 | Refinanciación AE Group HoldCo II (si aplica facility separada) | CFO TERAS + ICG/Vesta |
| 2029+ | Ventana exit Project Colorado consolidado con Templus España | CIO TERAS + ICG |

## 10. SQL — extracción Project Colorado

```sql
-- 4 Roosevelt balances 2025
SELECT entity_id, fiscal_year, total_assets, total_equity, total_liabilities, source, notes
FROM v_entity_balances_canonical
WHERE entity_id LIKE 'roosevelt%'
ORDER BY entity_id;

-- AE Group HoldCo II
SELECT * FROM v_entity_balances_canonical
WHERE entity_id = 'ae-holdco-ii';

-- Participaciones AE Group HoldCo II → 4 Roosevelt (pendiente cargar — tarea #9)
SELECT child_entity_id, ownership_pct, share_class
FROM participations
WHERE parent_entity_id = 'ae-holdco-ii'
ORDER BY child_entity_id;
```

## 11. Anti-patrones específicos Project Colorado

1. **NO mezclar cifras Roosevelt con cifras 7 filiales España** sin etiquetar claramente. Ambas son Templus pero son entidades distintas.
2. **NO citar cap% MdL en Roosevelt como 1,62%**. El cap% MdL en Project Colorado (vía TCH4 → AE HoldCo II → Roosevelt) es **32,60%**, no 1,62% (que es el agregado Templus CD España).
3. **NO clasificar Project Colorado como rama Vesta**. Es rama paralela TCH4 → AE Group HoldCo II (vehículo LUX separado).
4. **NO afirmar que NO aplica art. 21 LIS en Project Colorado**. A diferencia de Templus España (1,62% <5%), Project Colorado vía TCH4 100% en AE HoldCo II (pendiente confirmar) puede tener cap% >5% y SÍ aplicar exención.
5. **NO citar Roosevelt como entidades operativas Templus CD**. Son filiales de AE Group HoldCo II, no de Templus CD.
6. **NO confundir AE Group HoldCo II con Vesta Invest**. Ambos son LU SOPARFI pero AE HoldCo II es vehículo Project Colorado (TCH4 parent) mientras Vesta es vehículo Templus España (ICG controlled, TCH4 socio 2%).
