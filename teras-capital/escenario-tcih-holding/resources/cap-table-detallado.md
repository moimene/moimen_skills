# Cap table detallado — TCIH (Teras Capital Investment Holding)

> Snapshot 31/12/2025 · BD `savenikqhmcuwmcnabca` (`shareholders` entity_id='tcih' + `participations` + `entities`). 6 socios actuales tras ampliación sept 2022.

## Cap table TCIH — 6 socios actuales (FY 2025)

| # | Socio | Tipo | Cap% (BD) | Pool | NIF / DNI | Notas |
|---|---|---|---|---|---|---|
| 1 | IPN (Inteligencia Procesos de Negocio, SLU) | Persona jurídica | 25,83% | **MdL directo** | B87680328 | Participación directa MdL via IPN |
| 2 | TCH2 (TCH Dos Holding & Management, S.L.) | Persona jurídica | 25,83% | **MdL indirecto** | (TCH2 = 100% IPN) | Participación indirecta MdL via TCH2 (IPN → TCH2 100%) |
| 3 | Monforte Consultoría de Telecomunicaciones, S.L. | Persona jurídica | 25,83% | **Externo** | B87565131 | Tras ampliación sept 2022. Jorge Monforte. |
| 4 | LSSALMERON Inversiones, S.L. | Persona jurídica | 7,50% | **Externo** | (Luis Sánchez Salmerón) | Reducida desde posición original. LSS Admin Único TCIH. |
| 5 | Moisés Menéndez Andrés | Persona física | 7,50% | **Externo** | DNI Menéndez | Nuevo socio sept 2022. |
| 6 | Enrique Gurrea-Nozaleda Hörnlein | Persona física | 7,50% | **Externo** | DNI Gurrea | Nuevo socio sept 2022. |
| **TOTAL** | | | **100,02%** | | | (redondeo 0,02pp por ronding 2-decimales — despreciable) |

**Suma agregada por pool**:
- **Pool MdL** (IPN + TCH2): 25,83 + 25,83 = **51,66%** (equity-rank principal en override audit)
- **Externos**: Monforte 25,83% + LSS 7,50% + Menéndez 7,50% + Gurrea 7,50% = **48,33%**
- Total: 51,66 + 48,33 = 99,99% (suma ajustada eliminando rounding; BD muestra 100,02% por uso de 2 decimales en cada fila)

## Look-through MdL → TCIH

```
mdl-persona (Miguel de Lucas Sánchez)
  │ 100% Ordinarias
  ▼
IPN (Inteligencia Procesos de Negocio, SLU) NIF B87680328
  │
  ├─ 25,83% TCIH directo ──────────────────► TCIH (25,83% MdL directo)
  │
  └─ 100% TCH2 (Holding patrimonial personal MdL)
        │
        └─ 25,83% TCIH (indirecto) ────────► TCIH (25,83% MdL indirecto vía TCH2)
```

| Tramo look-through | Cálculo | Cap% MdL |
|---|---|---|
| MdL → IPN | 100% directo (persona física) | 100,00% |
| MdL → TCH2 | 100% IPN × 100% TCH2 (IPN posee 100% TCH2) | 100,00% |
| MdL → TCIH directo (vía IPN) | 100% × 25,83% | **25,83%** |
| MdL → TCIH indirecto (vía IPN → TCH2) | 100% × 100% × 25,83% | **25,83%** |
| **MdL → TCIH total efectivo** | 25,83 + 25,83 | **51,66%** |

> El campo `business_lines.teras-capital.mdl_position_pct = 51,67%` redondea por arriba 0,01pp. Para cálculos preciso usar **51,66%**; para presentaciones se puede citar 51,67% con nota "(redondeo a dos decimales)".

## Participations TCIH (BD)

`participations` salida del filtro `parent_entity_id = 'tcih'`:

| parent | child | ownership_pct | share_class | notes |
|---|---|---|---|---|
| TCIH | TCS (Teras Capital Spain) | 100,00% | Ordinarias | Filial 100% — confirmado Auditoría TCIH Situación Actual 2026 |
| TCIH | Templus CD | 2,00% | Class B (Teras) | Org chart Templus v8 14/04/2026 — 2% directo Class B Teras (no vía TCH4) |

Adicional `parent_entity_id = 'ipn' OR parent_entity_id = 'tch2'` AND `child_entity_id = 'tcih'`:

| parent | child | ownership_pct | share_class |
|---|---|---|---|
| IPN | TCIH | 25,83% | Ordinarias |
| TCH2 | TCIH | 25,83% | Ordinarias |

**Nota residual TCH4**: cc_balance 15.264€ en mayor 2025 (cuenta intercompany). NO figura como participation formalizada en BD `participations`. Si se calcula look-through TCH4 inverso, esta partida queda como crédito/débito intercompany, no como cap%.

## Distinción pool MdL vs externos — implicación material

| Aspecto | Pool MdL (51,66%) | Externos (48,33%) |
|---|---|---|
| Composición | IPN + TCH2 | Monforte + LSS + Menéndez + Gurrea |
| Aportaciones equity-rank (override audit) | 4.594K (TCH2) + 1.140K (IPN) = **5.734K (74,8% del total equity-rank)** | 1.691K (Monforte) + 241K (LSS) = **1.932K (25,2% del total)** |
| Subrogación Asterion (debt-rank) | Sin posición | Gurrea 541K + Menéndez 316K + (más Izzo/Ávila/Triguero/S.Echebarría/Huarte/Caporaleti/Gurrea-TUCA) = **2.102K total** |
| Quorum decisiones materiales | 51,66% — quorum directo simple | 48,33% — necesario para supermayoría |
| Voz consejo / asamblea | Coordinada (Admin Único LSS) | Individual por socio |

## Historia cap table TCIH (resumen)

- **Constitución original**: TCIH se crea como holding de servicios del grupo Teras Capital. Capital inicial 3.099€ (que aún hoy es el inscrito en RM).
- **Dic 2019**: financiación inicial Pacífico Cable vía préstamos múltiples (Jenkins, Monforte, Acinas, Dime Shared/QC, Fco. López, Gurrea, IPN). Importes en `decisiones-clave.md`.
- **Dic 2019**: cesiones de crédito a tenedoras TCH1/2/3/4 (objetivo: capitalizar deuda como equity tenedoras).
- **Dic 2021**: desinversión Pacífico Cable. TCS recibe dividendo + reintegro prima emisión. TCIH recibe → distribuye dividendo a cuenta 2,3M€ (cuenta 557) que genera PN negativo histórico.
- **Sept 2022**: **operación acordeón** + entrada de nuevos socios. Capital se reduce a 0 y se amplía a 20.000€ por compensación créditos. Entran Menéndez 7,50% + Gurrea-Nozaleda 7,50% (nuevos), Monforte sube a 25,83%, LSS baja a 7,50%. Escritura 25/11/2022. **Inscripción RM pendiente >3 años**.
- **2026**: auditoría provisional 02/04/2026 (B88279880) hace override sobre `shareholder_loans_as_equity=7.666.559€` y deja explícita la subrogación Asterion clase B 2,10M€ como debt-rank.

## Verificación SQL

```sql
-- Cap table TCIH (6 socios)
SELECT shareholder_name, share_class, ownership_pct, notes
FROM shareholders
WHERE entity_id = 'tcih'
ORDER BY ownership_pct DESC, shareholder_name;

-- Look-through MdL en TCIH
SELECT parent_entity_id, child_entity_id, ownership_pct, share_class, notes
FROM participations
WHERE child_entity_id = 'tcih';

-- Participaciones TCIH como parent (TCS + Templus CD)
SELECT parent_entity_id, child_entity_id, ownership_pct, share_class, notes
FROM participations
WHERE parent_entity_id = 'tcih';

-- Suma pool MdL
SELECT SUM(ownership_pct) AS pool_mdl_pct
FROM participations
WHERE child_entity_id = 'tcih' AND parent_entity_id IN ('ipn','tch2');
-- → 51.66

-- Verificación business_lines campo declared
SELECT id, mdl_position_pct, mdl_position_description
FROM business_lines
WHERE id = 'teras-capital';
-- → 51,67 (redondeo) / "51,67% vía IPN (25,83%) + TCH2 (25,83%)"
```

## Discrepancia declarado vs efectivo

| Métrica | Declarado BD | Efectivo look-through |
|---|---|---|
| MdL en TCIH | 51,67% (`business_lines.teras-capital.mdl_position_pct`) | **51,66%** (suma exacta participations) |
| Diferencia | -0,01pp | redondeo a 2 decimales |

Por homogeneidad con los lints (ver `SKILL.md §12 LINT 6`): usar 51,66% para cálculos precisos; tolerar 51,67% en presentaciones citando "redondeo".

## Pendientes cap table

1. Verificar suma exacta 100,02% (rounding) — confirmar BD si se ajusta a 100,00% o se mantiene rounding.
2. Documentar TCH2 = 100% IPN explícitamente en `participations` (verificar registro).
3. Conciliar el dato residual TCH4 0,01% — si se quiere formalizar como participation, registrar; si no, mantener como saldo intercompany.
4. Inscribir acordeón sep-22 en RM (no afecta cap%, pero resuelve inoponibilidad).
