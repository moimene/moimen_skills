# Cap table detallado — Olin (TCH1 → Tuca Bidco → MasOrange)

> Snapshot 31/12/2025 · BD `savenikqhmcuwmcnabca` (`participations` + `shareholders` + `entities` + Anexo IV ISHA).

## Cadena completa MdL → MasOrange

```
mdl-persona (Miguel de Lucas Gutiérrez)
  │ 100,00% Ordinarias
  ▼
IPN (Inteligencia Procesos de Negocio, SLU)
NIF: B87680328 · Activo 2025: 9.097.622€ · PN 5.102.491€
  │
  ├─ 31,97% TCH1 (Clase A) — directo
  │
  └─ 100% TCH2 (Ordinarias)
        │
        └─ 14,06% TCH1 (Clase A) — indirecto MdL
              │
              ▼
TCH1 (TCH Uno Holding & Management, S.L.)
NIF: B88547583 · Activo 4.080.441€ · PN 379€ · Pasivo 4.080.062€
  │ Cap%: 31,97% IPN + 14,06% TCH2 = 46,03% MdL efectivo
  │ Class structure: Ordinarias Clase A (MdL+Mon+LSS+Gurrea+Menéndez) +
  │                  Ordinarias Clase B (mgmt: Ávila/S.Echevarría/Triguero/Huarte/Lafarga)
  │
  │ ▼ 1,80% capital + 18,45% económico (Class B Ord 17,75% + Privilegiadas 0,696%)
  ▼
Tuca Bidco SL (S.à r.l. Luxemburgo)
FY 2024 audit: Activo 405.767.446€ · PN 248.552.828€ · Pasivo 157.214.619€
  │ Socios:
  │   • Tuca Midco Limited 98,00% (Class A Ord + Privilegiadas) — Asterion chain
  │   • TCH1 1,80% (Class B Ord 17,75% econ + Privilegiadas 0,696% econ = 18,45% econ)
  │   • A. Izzo 0,20% (Class B persona física)
  │ Total participaciones: 87.207 ord + 2.006.194 pref = 2.093.401
  │
  ▼
MasOrange (telco España, activo subyacente)
```

## Cap% efectivo MdL — composición

| Nivel | Cálculo | Cap% MdL |
|---|---|---|
| MdL → IPN | 100% directo (persona física) | 100,00% |
| MdL → TCH2 | 100% IPN × 100% TCH2 | 100,00% |
| MdL → TCH1 directo (vía IPN) | 100% × 31,97% | 31,97% |
| MdL → TCH1 vía TCH2 | 100% × 100% × 14,06% | 14,06% |
| **MdL → TCH1 total efectivo** | 31,97 + 14,06 | **46,03%** |
| MdL → TUCA capital | 46,03% × 1,80% | **0,83%** |
| MdL → TUCA económico | 46,03% × 18,45% | **8,49%** |
| MdL → MasOrange (activo subyacente, no consolidado) | — | look-through TUCA |

> **`business_lines.olin.mdl_position_pct=0,53%`** refleja un cálculo previo con `waterfall_params.mdl_pct_tch1=38,14%` (no 46,03%). Discrepancia documentada en `decisiones-clave.md` (factor antiguo vs look-through real).

## Cap table TCH1 completo (FY 2025, audit Anexo IV ISHA)

| # | Socio | Class | Cap% | Partner Group | Asterion-financed |
|---|---|---|---|---|---|
| 1 | IPN | Ordinarias Clase A | 31,97% | MdL | NO |
| 2 | TCH2 (Holding & Mgmt) | Ordinarias Clase A | 14,06% | MdL | NO |
| 3 | Monforte Consultoría Telecom | Ordinarias Clase A | 17,99% | LSS group | NO |
| 4 | Enrique Gurrea-Nozaleda | Ordinarias Clase A | 8,06% | Indep | **SÍ** (vía TCIH) |
| 5 | Moisés Menéndez Andrés | Ordinarias Clase A | 8,06% | Indep | **SÍ** (vía TCIH) |
| 6 | LSSALMERON Inversiones | Ordinarias Clase A | 5,48% | LSS | NO |
| 7 | Pablo Ávila | Ordinarias Clase B | 5,00% | Mgmt | **SÍ** |
| 8 | Santiago Sánchez Echevarría | Ordinarias Clase B | 3,13% | Mgmt | **SÍ** |
| 9 | Triguero | Ordinarias Clase B | 3,13% | Mgmt | **SÍ** |
| 10 | Gonzalo Huarte | Ordinarias Clase B | 1,67% | Mgmt | **SÍ** |
| 11 | Ramiro Lafarga | Ordinarias Clase B | 1,46% | Mgmt | **SÍ** |
| **TOTAL** | | | **100,01%** | | |

Suma 100,01% (rounding 0,01%, despreciable).

**Socios MdL agregados**: 46,03% (IPN+TCH2).
**Socios Asterion-financed**: 30,51% (Gurrea+Menéndez+Ávila+S.Echevarría+Triguero+Huarte+Lafarga). Su deuda vía TCIH = 2.101.899€ (subrogación clase B).

## Cap table TUCA completo (audit 2024)

| Socio | Class | Cap | Económico |
|---|---|---|---|
| Tuca Midco Limited | Ordinarias Clase A + Privilegiadas | 98,00% | mayoritario |
| TCH1 (TCH Uno Holding) | Ordinarias Clase B + Privilegiadas | 1,80% | **18,45%** (B 17,75 + Priv 0,696) |
| A. Izzo (persona física) | Ordinarias Clase B | 0,20% | minoritario |

## Detalle participaciones TCH1 ↔ TUCA

- TCH1 posee 15.481 ordinarias TUCA + 13.966 preferentes TUCA = 29.447 partic. de 2.093.401 totales (1,406% sin diferenciar clase).
- Pero con las clases reforzadas:
  - 15.481 / 87.207 ord = 17,75% del bloque Class B Ord
  - 13.966 / 2.006.194 pref = 0,696% del bloque Privilegiadas
- Suma derechos económicos efectivos: 17,75% + 0,696% = **18,45% econ TUCA** (sobre 1,80% capital).

## Verificación SQL

```sql
-- Look-through MdL en TCH1
SELECT
  parent_entity_id, child_entity_id, ownership_pct, share_class, notes
FROM participations
WHERE child_entity_id = 'tch1';

-- Cap table TCH1
SELECT shareholder_name, share_class, ownership_pct, partner_group, is_asterion_class_b
FROM shareholders
WHERE entity_id = 'tch1'
ORDER BY ownership_pct DESC;

-- Cap table TUCA
SELECT shareholder_name, share_class, ownership_pct
FROM shareholders
WHERE entity_id = 'tuca'
ORDER BY ownership_pct DESC;

-- Factor waterfall actual
SELECT param_key, param_value, default_value, source
FROM waterfall_params
WHERE business_line_id = 'olin' AND param_key LIKE '%pct_tch1%';
```

## Discrepancia documentada

`waterfall_params.mdl_pct_tch1 = 38,14%` con default 46,03%. La aplicación productiva usa 38,14% (factor histórico) pero look-through real es 46,03% según participations. **Tarea pendiente #11 BD MdL**: reconciliar factor con look-through y propagar a `business_lines.olin.mdl_position_pct` (actualmente 0,53% basado en 38,14%, debería ser ~0,83% basado en 46,03%).
