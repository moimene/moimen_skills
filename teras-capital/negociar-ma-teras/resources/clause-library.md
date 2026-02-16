# Biblioteca de Cláusulas M&A — TERAS Capital

Módulos de cláusulas con lógica de selección, variantes y consideraciones operativas.

---

## 1. Price and Consideration

### 1.1 Locked Box vs Completion Accounts — Decision Logic

```
¿Hay buen acceso a información financiera pre-signing?
├── SÍ
│   ├── ¿El vendedor prefiere price certainty?
│   │   └── SÍ → LOCKED BOX
│   └── ¿El comprador necesita ajustes post-closing?
│       └── SÍ → COMPLETION ACCOUNTS
└── NO
    └── COMPLETION ACCOUNTS (default)
```

#### Locked Box
- **Ventaja**: Price certainty para ambas partes
- **Riesgo**: Leakage post-locked box date
- **Cláusulas necesarias**:
  - Locked box date definition
  - Permitted leakage list (salaries, trade payables, pre-agreed dividends)
  - Non-permitted leakage: dividends, management fees, intercompany loans, asset disposals
  - Monitoring plan: monthly reporting + access rights
  - Interest rate on equity value (ticker) from locked box date to closing

#### Completion Accounts
- **Ventaja**: Adjustments reflect actual closing position
- **Riesgo**: Dispute sobre working capital / net debt
- **Cláusulas necesarias**:
  - Net debt definition (include/exclude list)
  - Working capital target + normalisation methodology
  - Dispute resolution: accountant determination, expert vs arbitration
  - Information access post-closing para preparation of accounts
  - Timeline: draft → objections → resolution

### 1.2 Earn-Out Design

| Elemento | Best Practice |
|----------|---------------|
| **Métricas** | Revenue, EBITDA, specific KPIs — bien definidas, sin ambigüedad |
| **Periodo** | 1–3 años (evitar >3 años — complejidad y litigio) |
| **Anti-manipulation** | Covenant to operate business in ordinary course; no changes to accounting policies; no cost-cutting that hurts long-term |
| **Floor/Cap** | Mínimo y máximo para limitar riesgo bilateral |
| **Acceleration** | Earn-out paid in full on change of control |
| **Dispute** | Expert determination por contable independiente |

### 1.3 Escrow/Holdback

- Sizing: vinculado a quantified risks del DD
- Duration: alineado con survival periods de warranties
- Release: automatic (time) + conditions (claims pendientes)
- Joint instructions required para releases

---

## 2. Representations & Warranties

### 2.1 Warranty Package por Deal Type

| Deal Type | Coverage | Key Areas |
|-----------|----------|-----------|
| **Share deal** | Amplitud total: business + legal + financial + tax + regulatory | All operations, assets, liabilities |
| **Asset deal** | Focussen sobre los assets transferidos | Title, encumbrances, contracts, employees |
| **Distressed** | Reducido (as-is); specific indemnities | Known risks only |

### 2.2 Disclosure Letter Standards

- **Fair disclosure**: información proporcionada con suficiente detalle para que un comprador razonable pueda identificar riesgo y cuantificarlo
- **Disclosure bundles**: organizar por warranty section
- **Qualification**: general disclosures (public info, data room content) + specific disclosures

### 2.3 Limitations Framework

| Limitation | Buyer-side (resistir) | Seller-side (negociar) |
|------------|----------------------|----------------------|
| **Cap** | 100% of price ideally; accept lower for specific | Push for cap % of price (30-50%) |
| **Basket (deductible)** | Lower threshold preferred | Higher threshold, deductible not tipping |
| **De minimis** | Lower preferred | Higher to filter nuisance claims |
| **Survival** | Longer (24-36 months); tax/environmental longer | Shorter (12-18 months) |
| **Fraud carve-out** | Absolute — no limitation on fraud claims | Accept (standard) |
| **Tax** | Specific tax indemnity with longer survival | Tax covenant only; resist indemnity |

### 2.4 W&I / R&W Insurance Decision Tree

```
¿Hay red flags significativos en DD?
├── SÍ → Specific indemnities + W&I for residual
│   (Note: W&I won't cover known risks)
└── NO
    ├── ¿Seller quiere clean exit?
    │   └── SÍ → Sell-side W&I policy (seller pays premium)
    └── ¿Buyer quiere protección extra?
        └── SÍ → Buy-side W&I policy
            ├── Recourse to seller? → Subrogation design
            └── No recourse → NIL seller liability (except fraud)
```

---

## 3. Signing–Closing Protection

### 3.1 Conditions Precedent — Checklist

- [ ] Regulatory approvals (antitrust, sector-specific, FDI)
- [ ] Third-party consents (change of control clauses in contracts)
- [ ] Clean-up actions (pre-agreed restructuring steps)
- [ ] Board/shareholder approvals
- [ ] W&I policy binding

### 3.2 Interim Covenants

**Ordinary course covenant** + negative covenants with thresholds:

| Covenant | Threshold |
|----------|-----------|
| No dividends/distributions | Absolute prohibition (except permitted) |
| No new material contracts | >€{threshold} without consent |
| No headcount changes | >€{threshold} salary or C-suite |
| No capex | >€{threshold} per item or aggregate |
| No acquisitions/disposals | Any without consent |
| No changes to accounting policies | Without consent |
| Maintain insurance | Current levels |
| No related-party transactions | Without consent |

### 3.3 Termination Rights

- **Outside date**: fecha límite para closing (typical: 3-6 months from signing)
- **Extension**: automatic if CPs still pending (limited extensions)
- **Break fees**: bilateral or one-way; amount as % of deal value
- **Remedies**: specific performance vs damages; assess enforceability per jurisdiction

---

## 4. MAC/MAE

### 4.1 Best Practice Guidelines

- Use **sparingly**: MAC/MAE is a nuclear option
- Define **significance threshold** (e.g., >X% decline in EBITDA)
- Include standard **carve-outs**:
  - General economic/market conditions
  - Industry-wide changes
  - Changes in law/regulation
  - Acts of God / force majeure
  - Effects of the transaction itself
  - Changes in accounting standards

### 4.2 Anti-"Rubber MAC" Rules

- ❌ No vague language ("any change that could adversely affect…")
- ✅ Specific metrics and thresholds
- ✅ Exclusion of known risks (already in DD)
- ✅ Time-bound measurement period

---

## 5. SHA / Partners' Pact — Module Details

### 5.1 Governance Architecture

| Element | Detail |
|---------|--------|
| Board composition | # seats per party; independent directors; chair rotation |
| Committees | Audit, compensation, investment; composition per committee |
| Information rights | Monthly financials, quarterly board pack, annual audit |
| Reporting pack | P&L, balance, cash, KPIs, pipeline, capex tracker |
| Observer rights | For minority positions |

### 5.2 Reserved Matters Tiers

| Tier | Threshold | Examples |
|------|-----------|---------|
| **Unanimous** | All parties | Change of articles; liquidation; related-party >threshold |
| **Supermajority** | 75%+ | Budget approval; M&A above threshold; new debt above threshold |
| **Board majority** | Simple majority | Operational decisions within budget; hiring below C-suite |

### 5.3 Transfer Restrictions

| Mechanism | Purpose |
|-----------|---------|
| **Lock-up** | Prevent early exit (typical: 2-3 years) |
| **ROFR/Pre-emption** | Right to match any third-party offer |
| **Permitted transfers** | Affiliates; estate planning; intra-group |
| **Tag-along** | Minority can join if majority sells |
| **Drag-along** | Majority can force minority to sell |
| **Exit process** | Dual-track (strategic + IPO); timeline; conduct rights |

### 5.4 Deadlock Resolution Ladder

```
Step 1: CEO/Chair discussion (5 business days)
    ↓ (if unresolved)
Step 2: Board resolution attempt (10 business days)
    ↓ (if unresolved)
Step 3: Mediation (30 days, neutral mediator)
    ↓ (if unresolved)
Step 4: Expert determination (for technical matters)
       OR
Step 5: Shotgun / Buy-sell (for fundamental disagreements)
    ↓ (as absolute last resort)
Step 6: Winding-up petition (only if all else fails)
```
