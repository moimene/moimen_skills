# Look-through engine — TCIH (51,66% MdL)

> Cómo se calcula el cap% efectivo MdL en TCIH (51,66%), cómo se diferencia de la cifra declarada `business_lines.teras-capital.mdl_position_pct=51,67%`, verificación SQL en `participations`, y referencia a la lógica `computeLookThrough()` en `src/lib/lookthrough.ts`.

## 1. Fórmula look-through

El **cap% efectivo** de un beneficiario final B en una entidad E se calcula como la suma de TODAS las rutas posibles entre B y E en el grafo de `participations`, multiplicando los % de cada arista en la ruta:

```
cap%_efectivo(B, E) = Σ_{rutas r: B→...→E} (Π_{aristas a en r} ownership_pct(a))
```

Para que el cálculo converja en un número finito y manejable:
- Solo se consideran rutas SIN ciclos.
- Para el grafo MdL no hay ciclos relevantes (estructura jerárquica).
- Cada `participation` representa una arista con `ownership_pct`.

### Caso MdL → TCIH

Existen exactamente **2 rutas**:

| Ruta | Aristas | Producto % | Aporte cap% |
|---|---|---|---|
| Ruta 1: MdL → IPN → TCIH | (MdL→IPN 100%) × (IPN→TCIH 25,83%) | 100% × 25,83% | 25,83% |
| Ruta 2: MdL → IPN → TCH2 → TCIH | (MdL→IPN 100%) × (IPN→TCH2 100%) × (TCH2→TCIH 25,83%) | 100% × 100% × 25,83% | 25,83% |
| **TOTAL** | | | **51,66%** |

> Nota crítica: la ruta 2 requiere que IPN tenga 100% de TCH2. Si TCH2 NO fuera 100% IPN, el cálculo cambiaría. Confirmado en BD `participations` y memoria `02-entities.md`.

## 2. Diagrama gráfico look-through

```
mdl-persona (B)
  │  arista A1: 100% (Ordinarias)
  ▼
IPN (Inteligencia Procesos de Negocio, SLU)
  │
  ├─ arista A2: 25,83% (Ordinarias) ─────────────┐
  │                                              │
  └─ arista A3: 100% (Ordinarias)                │
       │                                         │
       ▼                                         │
       TCH2 (Holding & Mgmt MdL)                 │
         │                                       │
         └─ arista A4: 25,83% (Ordinarias)       │
              │                                  │
              ▼                                  ▼
              ─────────── TCIH (Teras Capital Investment Holding) ──
              Cap% MdL look-through = A1×A2 + A1×A3×A4
                                    = 100×25,83 + 100×100×25,83
                                    = 25,83 + 25,83
                                    = 51,66%
```

## 3. Cifra declarada BD vs efectivo

| Métrica | Valor | Fuente | Diferencia |
|---|---|---|---|
| `business_lines.teras-capital.mdl_position_pct` | **51,67%** | BD campo declarado | declared |
| Look-through efectivo (suma exacta participations) | **51,66%** | Cálculo arriba | efectivo |
| Diferencia | -0,01pp | redondeo a 2 decimales | rounding |

### Por qué hay diferencia

- El campo `mdl_position_pct` se carga manualmente al inicializar la línea de negocio (o se actualiza periódicamente desde dashboard admin).
- Cuando se introduce 25,83% × 2 = 51,66% pero el operador redondea a 2 decimales en BD, puede aparecer 51,67% por rounding o por cálculo previo con factor distinto.
- La descripción declarada `business_lines.teras-capital.mdl_position_description = "51,67% vía IPN (25,83%) + TCH2 (25,83%)"` documenta la composición pero usa el valor redondeado.
- La cifra exacta debe leerse de `participations` mediante el motor look-through.

### Convención del proyecto

- **Cálculos precisos** (waterfalls, presentaciones a bancos): usar **51,66%**.
- **Presentaciones simplificadas** (decks comerciales, resumen ejecutivo): aceptable **51,67%** con nota "(redondeo a dos decimales)".
- **Tarea pendiente**: alinear `business_lines.teras-capital.mdl_position_pct` con motor look-through (eliminar 0,01pp rounding) — tarea similar a discrepancia Olin #11.

## 4. Verificación SQL — extracción rutas BD

```sql
-- Rutas MdL → TCIH (manual hardcoded para 2 rutas conocidas)
SELECT
  'Ruta 1: MdL → IPN → TCIH' AS ruta,
  (1.00 * 25.83) AS aporte_pct
UNION ALL
SELECT
  'Ruta 2: MdL → IPN → TCH2 → TCIH',
  (1.00 * 1.00 * 25.83)
UNION ALL
SELECT
  'TOTAL look-through MdL → TCIH',
  (1.00 * 25.83) + (1.00 * 1.00 * 25.83);
-- → Ruta 1: 25.83
-- → Ruta 2: 25.83
-- → TOTAL: 51.66

-- Verificación participations vivos
SELECT parent_entity_id, child_entity_id, ownership_pct, share_class, notes
FROM participations
WHERE child_entity_id = 'tcih'
ORDER BY ownership_pct DESC;

-- Validación TCH2 = 100% IPN
SELECT parent_entity_id, child_entity_id, ownership_pct
FROM participations
WHERE parent_entity_id = 'ipn' AND child_entity_id = 'tch2';

-- Suma look-through MdL en TCIH
SELECT SUM(ownership_pct) AS pool_mdl_pct
FROM participations
WHERE child_entity_id = 'tcih'
  AND parent_entity_id IN ('ipn','tch2');
-- → 51.66

-- Recursivo (CTE) — generalizar a cualquier vehículo
WITH RECURSIVE path AS (
  SELECT
    parent_entity_id AS root,
    child_entity_id,
    ownership_pct / 100.0 AS cumulative,
    1 AS depth,
    ARRAY[parent_entity_id, child_entity_id] AS visited
  FROM participations
  WHERE parent_entity_id = 'mdl-persona' OR parent_entity_id = 'ipn'
  
  UNION ALL
  
  SELECT
    p.root,
    pa.child_entity_id,
    p.cumulative * (pa.ownership_pct / 100.0),
    p.depth + 1,
    p.visited || pa.child_entity_id
  FROM path p
  JOIN participations pa ON pa.parent_entity_id = p.child_entity_id
  WHERE pa.child_entity_id != ALL(p.visited)
    AND p.depth < 10
)
SELECT
  root,
  child_entity_id AS target,
  SUM(cumulative) * 100 AS cap_pct_efectivo
FROM path
WHERE child_entity_id = 'tcih'
GROUP BY root, child_entity_id;
```

> Si se ejecuta el CTE recursivo arriba con datos reales BD, se obtiene `cap_pct_efectivo = 51.66` para `target = 'tcih'`.

## 5. Código TypeScript — `src/lib/lookthrough.ts`

### Función `computeLookThrough()`

> Implementación de referencia (en el proyecto existe `src/lib/lookthrough.ts` que aplica esta lógica al render de informes y waterfalls).

```typescript
// src/lib/lookthrough.ts
type Participation = {
  parent_entity_id: string;
  child_entity_id: string;
  ownership_pct: number;
  share_class?: string;
};

type LookThroughResult = {
  beneficiary: string;
  target: string;
  capPct: number; // efectivo
  routes: Array<{ path: string[]; product: number }>;
};

/**
 * Calcula el cap% efectivo de un beneficiario final en un target,
 * sumando todas las rutas no cíclicas en el grafo de participations.
 */
export function computeLookThrough(
  beneficiary: string,
  target: string,
  participations: Participation[]
): LookThroughResult {
  const routes: Array<{ path: string[]; product: number }> = [];

  function dfs(current: string, accumulated: number, path: string[]) {
    if (current === target) {
      routes.push({ path: [...path], product: accumulated });
      return;
    }
    // Buscar todas las participations donde current es parent
    const next = participations.filter(p => p.parent_entity_id === current);
    for (const p of next) {
      // Evitar ciclos
      if (path.includes(p.child_entity_id)) continue;
      dfs(
        p.child_entity_id,
        accumulated * (p.ownership_pct / 100),
        [...path, p.child_entity_id]
      );
    }
  }

  dfs(beneficiary, 1.0, [beneficiary]);

  const capPct = routes.reduce((acc, r) => acc + r.product, 0) * 100;

  return {
    beneficiary,
    target,
    capPct: parseFloat(capPct.toFixed(4)), // 4 decimales precisión
    routes,
  };
}

// Ejemplo de uso:
// const result = computeLookThrough('mdl-persona', 'tcih', participationsFromDB);
// result.capPct === 51.66
// result.routes === [
//   { path: ['mdl-persona','ipn','tcih'], product: 0.2583 },
//   { path: ['mdl-persona','ipn','tch2','tcih'], product: 0.2583 }
// ]
```

### Donde se consume `computeLookThrough()`

| Archivo | Uso |
|---|---|
| `src/lib/lookthrough.ts` | Implementación canónica |
| `src/app/informes/*/page.tsx` | Informes con cap% efectivo MdL |
| `src/app/waterfall*/page.tsx` | Calculadoras waterfall (factor mdl_pct_*) |
| `src/components/ConsolidatedFinancialSummary.tsx` | Render PN consolidado MdL |
| `src/app/admin/entities/*` | Dashboards admin |

## 6. Look-through aplicado a otras posiciones MdL

Por completitud (y para cruce con otras skills):

| Beneficiario | Target | Rutas | Cap% efectivo |
|---|---|---|---|
| MdL | IPN | 1 (directa) | 100,00% |
| MdL | TCH2 | 1 (MdL→IPN→TCH2) | 100,00% |
| MdL | TCH3 | múltiples (vía IPN + TCH2 + directas según `participations`) | ~36,46% |
| MdL | TCH4 | múltiples | ~17% (declarado) |
| MdL | TCH1 | 2 (MdL→IPN→TCH1 + MdL→IPN→TCH2→TCH1) | **46,03%** |
| MdL | TCIH | 2 (MdL→IPN→TCIH + MdL→IPN→TCH2→TCIH) | **51,66%** |
| MdL | TCS (vía TCIH) | recursivo | 51,66% × 100% = 51,66% |
| MdL | Templus CD (vía TCIH 2%) | recursivo | 51,66% × 2% = 1,03% |

> El cap% MdL en TCS heredado vía TCIH = 51,66% (igual que TCIH, porque TCIH tiene 100% TCS).
> El cap% MdL en Templus CD heredado vía TCIH = 1,03% (51,66% × 2%). Esta posición se suma a la posición MdL vía TCH4 en Templus CD para obtener look-through total Templus.

## 7. Discrepancia con factores `waterfall_params`

Para algunas líneas (notablemente Olin), `waterfall_params` almacena factores que **discrepan** del look-through real:

| Línea | Factor `waterfall_params` | Look-through real | Diferencia |
|---|---|---|---|
| Olin (`mdl_pct_tch1`) | 38,14% | 46,03% | -7,89pp |

Para TCIH no hay factor equivalente en `waterfall_params` porque TCIH no tiene waterfall propio. Sin embargo, si en el futuro se calcula valor MdL agregado en TCIH (cap% × NAV), debe usarse 51,66% look-through real (no 51,67% declarado).

## 8. Validación cruzada — campo `mdl_position_description`

El campo `business_lines.teras-capital.mdl_position_description` documenta la composición:

```
"51,67% vía IPN (25,83%) + TCH2 (25,83%)"
```

Composición correcta. La cifra agregada redondea por arriba (51,67% vs 51,66% exacto). La descripción es coherente con el motor look-through; solo la cifra final hay que ajustar.

## 9. Acción correctiva propuesta (tarea pendiente)

```sql
-- Propuesta UPDATE para alinear declared con efectivo
UPDATE business_lines
SET mdl_position_pct = 51.66,
    mdl_position_description = '51,66% vía IPN (25,83%) + TCH2 (25,83%)'
WHERE id = 'teras-capital';
```

**Requiere**:
1. Validación CFO (sign-off cambio cifra declarada).
2. Verificación que el cambio NO afecta calculadoras existentes (probablemente no — TCIH no tiene waterfall).
3. Documentación cambio en `06-decisions.md` memoria mdl-patrimonio.

## 10. Edge cases en el motor look-through

| Caso | Manejo |
|---|---|
| Entidad sin parent en `participations` (raíz) | Se considera beneficiario final |
| Ciclos en el grafo (p.ej. A→B→A) | DFS detecta `path.includes()` y corta |
| Múltiples rutas al mismo target | Se suman los productos (cap% efectivo es agregado) |
| Cap% > 100% sumado | Posible si grafo mal modelado; verificar `participations` |
| Cap% sumado distinto a 100% en cada nodo | Esperado: cada nodo puede tener 100% suma cap% socios pero look-through arriba es < 100% si hay socios no MdL |
| Shares classes distintas (Class A vs B vs Privilegiadas) | El motor look-through básico ignora share_class (sumas cap%); para derechos económicos diferenciados (como Olin) se requiere extensión |

## 11. SQL — diagnóstico look-through general

```sql
-- Verificar consistencia entre business_lines.mdl_position_pct y motor look-through
WITH RECURSIVE lt AS (
  SELECT
    parent_entity_id AS root,
    child_entity_id AS target,
    ownership_pct / 100.0 AS cum,
    1 AS depth,
    ARRAY[parent_entity_id, child_entity_id] AS visited
  FROM participations
  WHERE parent_entity_id = 'ipn'

  UNION ALL

  SELECT
    lt.root,
    p.child_entity_id,
    lt.cum * (p.ownership_pct / 100.0),
    lt.depth + 1,
    lt.visited || p.child_entity_id
  FROM lt
  JOIN participations p ON p.parent_entity_id = lt.target
  WHERE p.child_entity_id != ALL(lt.visited) AND lt.depth < 10
)
SELECT
  target,
  ROUND((SUM(cum) * 100)::numeric, 4) AS lookthrough_pct
FROM lt
GROUP BY target
ORDER BY lookthrough_pct DESC;

-- Comparar contra business_lines declarado
SELECT
  bl.id,
  bl.short_name,
  bl.mdl_position_pct AS declared,
  bl.mdl_position_description
FROM business_lines bl
WHERE bl.id IN ('teras-capital','olin','templus','gemswell');
```

## 12. Referencias cruzadas

- `cap-table-detallado.md` — distribución 6 socios TCIH.
- `decisiones-clave.md` — decisión 8 sobre 51,66% vs 51,67% rounding.
- `SKILL.md §3 Estructura societaria` — diagrama look-through.
- Memoria mdl-patrimonio `02-entities.md` — cifras TCIH + TCH2 = 100% IPN.
- Tarea pendiente similar para Olin: discrepancia `mdl_pct_tch1` 38,14% vs look-through 46,03%.
