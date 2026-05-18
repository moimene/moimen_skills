# Intragrupo — 9 saldos detallados

> Snapshot 31/12/2025 · BD `intragroup_balances` filtrado por fiscal_year=2025. Lista canónica + categorización equity-rank vs debt-rank + cross-cat / intra-cat + SQL extracción.

## Vista canónica — los 9 saldos

```sql
SELECT id, from_entity_id, to_entity_id, amount, balance_type,
       accounts_from, accounts_to, crosses_categories, source, notes
FROM intragroup_balances
WHERE fiscal_year = 2025
ORDER BY amount DESC;
```

### Tabla completa ordenada por importe

| # BD | From entity | To entity | Importe (€) | Balance type | Cross-cat | Source | Categorización |
|---|---|---|---|---|---|---|---|
| 20 | tcih | tch1 | 4.430.680 | current_account | NO (intra-cat teras) | audit_2026 | Activo TCIH — operativo TUCA |
| 12 | tch2 | tcih | 4.000.000 | **participative** | SÍ (personal → teras) | mayor_inferred | Pasivo TCIH — equity-rank override |
| 15 | ipn | tch3 | 1.588.669 | investment | SÍ (personal → teras) | mayor_inferred | Inversión capital TCH3 |
| 19 | ipn | lalu | 1.563.000 | short_term_investment | SÍ (personal → patrimonial) | mayor_inferred | Inversión CP IPN → LALU |
| 18 | grand-view | ipn | 1.519.092,12 | loan_lp | SÍ (quarter → personal) | mayor_inferred | Préstamo Grand View → IPN |
| 21 | tcih | tch1 | 1.444.806 | loan_lp | NO (intra-cat teras) | audit_2026 | Activo TCIH — crédito LP |
| 14 | ipn | tcih | 1.403.258,40 | current_account | SÍ (personal → teras) | mayor_inferred | Pasivo TCIH — equity-rank parcial |
| 13 | tch2 | tcih | 606.408,42 | current_account | SÍ (personal → teras) | mayor_inferred | Pasivo TCIH — Proyecto TUCA |
| 17 | tch2 | ipn | 566.436,95 | loan_lp | NO (intra-cat personal) | mayor_inferred | Préstamo TCH2 → IPN |

**Suma total intragrupo BD**: 17.122.350,89€ (suma de 9 saldos)

## Detalle por saldo

### Saldo 1 (id=20) — TCIH → TCH1 — 4.430.680€ (current_account)

- **From**: TCIH (acreedor) → **To**: TCH1 (deudor)
- **Cuentas**:
  - From: `55240006 C/C TCH UNO HOLDING (TCIH activo)`
  - To: `5510x C/C TCIH (TCH1 pasivo)`
- **Naturaleza**: cuenta corriente activa TCIH ↔ TCH1 — Proyecto TUCA (canalización financiación Asterion al holding TUCA chain).
- **Cross-cat**: NO (intra-categoría teras: TCIH y TCH1 son del bloque Teras Capital).
- **Source**: `audit_2026` (auditoría provisional capa 3 intercompany).
- **Notas**: TCIH es acreedora de TCH1 por importe principal del proyecto TUCA. Es un saldo deudor desde TCIH (cuenta 552).

### Saldo 2 (id=12) — TCH2 → TCIH — 4.000.000€ (participative)

- **From**: TCH2 (acreedor) → **To**: TCIH (deudor)
- **Cuentas**:
  - From: `52100001 PTMO PARTICIPATIVO TCH DOS`
  - To: `521 (TCIH)` — cuenta interna TCIH grupo participativos
- **Naturaleza**: préstamo participativo TCH2 → TCIH (cuenta 521 codificación interna NO estándar PGC).
- **Composición**:
  - 3M€ — Jenkins UNO original cedido a TCH2 (dic-2019).
  - 1M€ — cancelación parcial cuenta crédito sep-2022 reestructurada a participativo.
- **Cross-cat**: SÍ (TCH2 es categoría personal MdL → TCIH es categoría teras).
- **Source**: `mayor_inferred`.
- **Hallazgo TCIH-C-02**: 4M contable vs 3M contractual original → conciliación bilateral pendiente.
- **Tratamiento override audit_2026_provisional**: este saldo entra en equity-rank (parte de los 4.594K de TCH2 reclasificados a `shareholder_loans_as_equity`).
- **Categorización**: **EQUITY-RANK** post override (parte del 7,67M€).

### Saldo 3 (id=15) — IPN → TCH3 — 1.588.669€ (investment)

- **From**: IPN (inversor) → **To**: TCH3 (capital + reservas)
- **Cuentas**:
  - From: `24030005 PARTICIPACIONES TCH TRES (IPN)`
  - To: Capital + Reservas TCH3
- **Naturaleza**: inversión IPN en capital social de TCH3 (capitalizada vía aumento de capital).
- **Cross-cat**: SÍ (personal IPN → teras TCH3).
- **NO era posición de TCIH** — relación directa IPN ↔ TCH3.
- **Source**: `mayor_inferred`.
- **Categorización**: NO afecta TCIH directamente; figura en lista canónica de 9 saldos del grupo.

### Saldo 4 (id=19) — IPN → LALU — 1.563.000€ (short_term_investment)

- **From**: IPN (inversor) → **To**: LALU (vehículo patrimonial)
- **Cuentas**:
  - From: `54200002 LALU & TATI (IPN)`
  - To: `551/512 (LALU)`
- **Naturaleza**: inversión financiera corto plazo IPN → LALU.
- **Cross-cat**: SÍ (personal → patrimonial).
- **NO afecta TCIH**.
- **Source**: `mayor_inferred`.

### Saldo 5 (id=18) — Grand View → IPN — 1.519.092,12€ (loan_lp)

- **From**: Grand View (acreedor) → **To**: IPN (deudor)
- **Cuentas**:
  - From: `24x` (cuenta acreedora Grand View)
  - To: `17100002 PTMO GRAND VIEW LA QUINTA (IPN, acreedor)`
- **Naturaleza**: préstamo LP Grand View → IPN (relación cross-categoría quarter → personal).
- **Cross-cat**: SÍ (Grand View es categoría quarter → IPN es personal).
- **Dirección corregida**: la dirección del flujo se corrigió en audit (originalmente registrada al revés en mayor).
- **NO afecta TCIH**.
- **Source**: `mayor_inferred`.

### Saldo 6 (id=21) — TCIH → TCH1 — 1.444.806€ (loan_lp)

- **From**: TCIH (acreedor) → **To**: TCH1 (deudor)
- **Cuentas**:
  - From: `243xxxx Crédito LP a TCH UNO (TCIH activo)`
  - To: `17xxxx Préstamo LP de TCIH (TCH1 pasivo)`
- **Naturaleza**: crédito a largo plazo de TCIH a TCH1 (identificado en auditoría TCIH capa 3 intercompany).
- **Cross-cat**: NO (intra-categoría teras).
- **Source**: `audit_2026`.
- **Categorización**: activo financiero TCIH.

### Saldo 7 (id=14) — IPN → TCIH — 1.403.258,40€ (current_account)

- **From**: IPN (acreedor) → **To**: TCIH (deudor)
- **Cuentas**:
  - From: `5510x C/C IPN`
  - To: `55100009 + 55100002 + 55250001 (TCIH)`
- **Naturaleza**: cuenta corriente IPN ↔ TCIH (combinado).
- **Composición**:
  - PROYECTO TUCA 1.176.354€
  - Base 24.098€
  - Saldo Miguel persona física = realmente IPN 202.806€
- **Cross-cat**: SÍ (personal IPN → teras TCIH).
- **Source**: `mayor_inferred`.
- **Tratamiento override**: parte de este saldo (~1.140K€) entra en equity-rank (parte del 1.140K de IPN identificado por auditor).
- **Categorización**: parcialmente **EQUITY-RANK** post override.

### Saldo 8 (id=13) — TCH2 → TCIH — 606.408,42€ (current_account)

- **From**: TCH2 (acreedor) → **To**: TCIH (deudor)
- **Cuentas**:
  - From: `5510x C/C TCH DOS`
  - To: `55100010 C/C TCH DOS - PROYECTO TUCA`
- **Naturaleza**: cuenta corriente TCH2 ↔ TCIH dentro Proyecto TUCA (operativo Olin).
- **Cross-cat**: SÍ (personal TCH2 → teras TCIH).
- **Source**: `mayor_inferred`.
- **Tratamiento override**: parte del flujo TCH2 reclasificado a equity-rank (parte del 594K identificación auditor TCH2).
- **Categorización**: parcialmente **EQUITY-RANK** post override (la otra parte es operativo Proyecto TUCA).

### Saldo 9 (id=17) — TCH2 → IPN — 566.436,95€ (loan_lp)

- **From**: TCH2 (acreedor) → **To**: IPN (deudor)
- **Cuentas**:
  - From: `24x C/P TCH2`
  - To: `17100005 PTMO TCH DOS (IPN, acreedor)`
- **Naturaleza**: préstamo TCH2 → IPN (cuenta 17x acreedora IPN, dirección corregida).
- **Cross-cat**: NO (intra-categoría personal MdL).
- **Source**: `mayor_inferred`.
- **NO afecta TCIH directamente**.

## Categorización agregada

### Por categoría cruce

| Categoría | # saldos | Importe (€) | Descripción |
|---|---|---|---|
| **Intra-categoría** | 3 | 6.441.923,95 | TCIH→TCH1 (4,43M + 1,44M) + TCH2→IPN (566K) |
| **Cross-categoría** | 6 | 10.680.426,94 | Personal↔Teras (4,40M), Personal↔Teras (1,40M), Personal↔Teras (606K), Personal↔Teras (1,59M), Quarter→Personal (1,52M), Personal→Patrimonial (1,56M) |

### Por equity-rank vs debt-rank vs neutro

| Tipo | # saldos | Importe (€) | Notas |
|---|---|---|---|
| **Equity-rank** (post override audit_2026) | 3 (parcial) | ~5.700.000 | Saldo 2 (4M TCH2 partic) + Saldo 7 (1,14M IPN parte) + Saldo 8 (~594K TCH2 parte) |
| **Operativo Proyecto TUCA** (NO equity, NO debt-rank explícito) | 4 | ~6.500.000 | Saldo 1, 6, 7 (parte), 8 (parte) |
| **Inversiones / préstamos cross-cat no TCIH** | 4 | ~5.236.000 | Saldos 3, 4, 5, 9 (no afectan TCIH directamente) |

### Posición TCIH agregada (5 de los 9 saldos)

| # | Saldo | TCIH es | Importe (€) | Notas |
|---|---|---|---|---|
| 1 | tcih → tch1 (C/C) | acreedor | 4.430.680 | Activo TCIH — operativo |
| 2 | tch2 → tcih (participative) | deudor | 4.000.000 | Pasivo TCIH — equity-rank |
| 6 | tcih → tch1 (loan_lp) | acreedor | 1.444.806 | Activo TCIH — crédito LP |
| 7 | ipn → tcih (C/C) | deudor | 1.403.258,40 | Pasivo TCIH — equity-rank parcial |
| 8 | tch2 → tcih (C/C) | deudor | 606.408,42 | Pasivo TCIH — Proyecto TUCA + equity-rank parcial |
| **Activos TCIH** | | | **5.875.486** | Total créditos a TCH1 |
| **Pasivos TCIH (intragrupo)** | | | **6.009.667** | Total saldos socios + Proyecto TUCA |

> **Posición neta intragrupo TCIH** = Activos 5,88M€ − Pasivos 6,01M€ = **-134K€** (ligeramente deudora). Esta posición se compone como mix de equity-rank (post override) + operativo Proyecto TUCA.

## Conciliación bilateral pendiente

| Hallazgo | Saldos involucrados | Acción |
|---|---|---|
| TCIH-C-02 | Saldo 2 (TCH2→TCIH 4M PTMO) | Conciliar con TCH2: 4M contable vs 3M contractual original; documentar 1M cancelación parcial cuenta crédito sep-22 |
| Gap 350K | Saldos 1+6 (TCIH→TCH1 5,87M) vs TCH1 view 4,08M | Conciliar bilateralmente antes de planificar cesión crédito a socios TCH1 |
| Composición agregada | Saldo 7 (IPN→TCIH 1,40M) | Desglosar Proyecto TUCA 1,18M + Miguel 203K + base 24K |

## Documentos referencia para verificar

- Mayor PGC TCIH 2025 (carpeta `Cierres historicos/`)
- Mayor PGC TCH1 2025 (idem)
- Mayor PGC TCH2 2025 (idem)
- Mayor PGC IPN 2025 (idem)
- Auditoría provisional 02/04/2026 TCIH (B88279880)
- Auditoría TCH1 (Anexo IV ISHA — referencia Olin)
- Side letters cesión crédito (CLO)

## SQL — extracción completa

```sql
-- Lista canónica 9 saldos
SELECT id, from_entity_id, to_entity_id, fiscal_year, amount, balance_type,
       accounts_from, accounts_to, crosses_categories, source, notes, imported_at
FROM intragroup_balances
WHERE fiscal_year = 2025
ORDER BY amount DESC;

-- Saldos TCIH (5 de 9)
SELECT *
FROM intragroup_balances
WHERE fiscal_year = 2025 AND (from_entity_id = 'tcih' OR to_entity_id = 'tcih')
ORDER BY amount DESC;

-- Equity-rank candidatos (cross-cat + balance_type='participative')
SELECT *
FROM intragroup_balances
WHERE fiscal_year = 2025
  AND balance_type IN ('participative','current_account')
  AND to_entity_id = 'tcih'
ORDER BY amount DESC;

-- Saldos por categoría cruce
SELECT crosses_categories, COUNT(*) AS num_saldos, SUM(amount) AS importe_total
FROM intragroup_balances
WHERE fiscal_year = 2025
GROUP BY crosses_categories;

-- Conciliación bilateral (vistas)
SELECT
  COALESCE(a.from_entity_id, b.to_entity_id) AS entity_a,
  COALESCE(a.to_entity_id, b.from_entity_id) AS entity_b,
  a.amount AS view_a_to_b,
  b.amount AS view_b_to_a,
  COALESCE(a.amount, 0) - COALESCE(b.amount, 0) AS diff
FROM intragroup_balances a
FULL OUTER JOIN intragroup_balances b
  ON a.from_entity_id = b.to_entity_id AND a.to_entity_id = b.from_entity_id
  AND a.fiscal_year = b.fiscal_year
WHERE a.fiscal_year = 2025;
```

## Acciones derivadas

1. **Conciliar TCIH-C-02** (TCH2 → TCIH 4M vs 3M contractual) — Q2 2026 CFO + audit firm.
2. **Conciliar gap 350K** entre vista TCIH (4,43M C/C) y vista TCH1 (4,08M C/C) — Q2 2026.
3. **Cuantificar equity-rank exacto por saldo intragrupo** (split entre equity-rank, debt-rank Asterion, y operativo Proyecto TUCA).
4. **Implementar conciliación bilateral automatizada** en pipeline (recomendación auditoría 30/03/2026).
5. **Aclarar dirección flujo** para saldos con `mayor_inferred` (refrescar con auditoría definitiva 2025).
