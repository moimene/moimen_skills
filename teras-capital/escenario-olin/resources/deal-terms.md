# Deal terms — Olin (TUCA Bidco / MasOrange)

> Snapshot 31/12/2025 · Fuente: ISHA TUCA reformulado post-Asterion + auditoría TUCA 2024 + Anexo IV TCH1 + BD `waterfall_params` (`business_line_id='olin'`).

## 1. Estructura financiera

### Inversión inicial TCH1

- **Investment date**: 18-feb-2022 (`waterfall_params.investment_date`).
- **Total invertido TCH1 en TUCA**: 1.479.243€ (`tch1_total_invested`).
- Composición: 15.481 ordinarias Class B + 13.966 preferentes (`tch1_ord_shares` + `tch1_pref_shares`).

### Deuda Asterion (TCIH ↔ Asterion)

- **Asterion → TCIH** facility: deuda externa real 1.802K€ (saldo 31/12/2025, `entity_balances.tcih.notes`).
- **Tasa Asterion 7%** anual (`waterfall_params.asterion_rate_pct`).
- **Subrogación Asterion clase B** (2.101.899€): socios externos financiados por Asterion vía TCIH. Detalle por socio en `escenario-tcih-holding/resources/intragrupo-9-saldos.md`.

### Deuda neta TUCA (modelado base)

- **Deuda neta default modelada**: 35.000.000€ (`deuda_neta_default_eur`).
- **Refinanciación amount referencia**: 90.000.000€ (`refinancing_amount`).
- **Net debt waterfall**: 80.000.000€ (`net_debt`).
- Mezzanine + senior (estructura mixed, detalle en SPA TUCA).

## 2. ISHA TUCA — cláusulas clave

### Cap table reforzado

- **TCH1 1,80% capital** con **18,45% derechos económicos** = ratio 10× leverage económico/capital.
- Class B Ord (TCH1 + Izzo): **17,75% econ** (ISHA Cl. 3) → con dilución máx -10% por new managers cae a **15,97%** (ISHA Cl. 6.4(C)).
- Privilegiadas (TCH1 + Tuca Midco): **0,696% para TCH1** (ISHA Schedule cap structure).
- Cupón preferente TUCA: **10%** anual (`pref_coupon_pct`, ISHA Cl. 8(D)).

### Vesting y new managers

- New manager dilution cap: **10%** sobre el pool Class B Ord (`new_manager_dilution_cap`).
- Class B vesting on exit: **100%** (acceleration completa al cierre — `class_b_vesting_on_exit`).
- Modelo: managers vested adicionales reducen el 17,75% TCH1 hasta el 15,97% (ISHA Cl. 6.4(C)) — el 1,78pp se redistribuye a nuevos managers.

### Decision matrix (supermayorías)

- ISHA contempla supermayorías Class A (Tuca Midco) + Class B (TCH1) para decisiones de:
  - Refinanciación deuda Asterion
  - Cambio de estrategia material MasOrange
  - M&A relevantes
  - Distribución de dividendos
  - Cambios bylaws / class structure
- Detalle exacto en ISHA Cl. (pendiente referencia cláusula concreta) — consultar `bl_documents` doc_type='ISHA' business_line_id='olin'.

### Drag-along / Tag-along / ROFR

- Drag-along: requerido por mayoría calificada Class A (Asterion/Tuca Midco).
- Tag-along: pro-rata para todos los socios TUCA, incluido TCH1 sobre 18,45% econ.
- ROFR (Right of First Refusal) / Preemption: contemplados en ISHA, detalles en SPA.

### Key-man clauses

- Triggered si key persons del management (Ávila, S.Echevarría, Triguero, Huarte, Lafarga) salen antes del exit.
- Mitigante: vesting acceleration on exit + replacement mecanismo.

## 3. Distribuciones históricas

| Evento | Fecha | Importe TUCA | Notas |
|---|---|---|---|
| Dividendo | Dec 2024 | 12.000.000€ | `waterfall_params.dividend_dec2024`; distribución a Class A + B prorrata económico |

(Estructura TCH1 recibe: 12M × 18,45% econ = ~2,21M€ a nivel TCH1 — sujeto a IS 25% TCH1 = ~1,66M€ neto distribuible al pool socios TCH1.)

## 4. Hurdle y waterfall ISHA

| Param | Valor | Fuente |
|---|---|---|
| Total pref invested | 270.000.000€ | `total_pref_invested` |
| Hurdle | 270.000.000€ | `exit_scenarios.hurdle_amount` |
| Preferred return rate | 10% (`pref_return_rate` waterfall) — equivalente al cupón preferente Class A | ISHA Cl. 8(D) |
| Class B vesting on exit | 100% | `class_b_vesting_on_exit` |
| Net debt exit modelado | 80.000.000€ | `net_debt` |
| Transaction costs | 0% (no modelado adicional) | `transaction_costs` |

Mecánica waterfall completa en `waterfall-y-escenarios-isha.md`.

## 5. Documentos clave (referencia)

- ISHA TUCA reformulado (post-Asterion entry)
- SPA TUCA original (entrada Asterion)
- Anexo IV Auditoría TCH1 (cap table + derechos económicos detallados)
- Auditoría TUCA 2024 (audit firm + cifras)
- Financing Agreement Asterion ↔ Tuca Midco
- Cap table histórico (notarial)
- Acuerdos Class B managers individuales

Listado completo con paths en `documentos-referencia.md`.

## 6. Pendientes contractuales

- Confirmar audit firm de TUCA y TCH1 (no en BD `business_lines` aún).
- Refinanciación Asterion 2027-2028: term sheet pendiente.
- NBO MasOrange firme (Q2 2026 esperado).
