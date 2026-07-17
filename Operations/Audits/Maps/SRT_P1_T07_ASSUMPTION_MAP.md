---
id: SRT-OPS-AUDIT-MAP-P1-T07-ASSUMPTIONS
type: audit_map
status: record_v0_1
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-07-17
source_of_truth: "origin/main @ 14c0d7f8"
dependency:
  - SRT-OPS-AUDIT-P1-T07-PROOF-HARDENING
tags: [Governance, ProofAudit, AssumptionMap, P1-T07]
---

# P1-T07 Assumption Map

> **Status**: non-canonical audit map. One row per premise the P1-T07 proof needs or invokes. Columns: source (where it appears, if at all) · **explicit?** (is it stated) · **necessary?** (does the conclusion fail without it) · **sufficient?** (does it, with the stated context, close the proof) · **ε_pg co-reference** (does it restate ε_pg / non-self-erasure) · **countermodel if missing** (from audit §4 Version D).

## Premise ledger

| # | Premise | Source in corpus | Explicit? | Necessary? | Sufficient (alone)? | ε_pg co-reference | Countermodel if missing |
|---|---|---|---|---|---|---|---|
| P1 | `∅` (`A_t=∅`) is **absorbing** | `SRT_Irreversibility.md` Def-IRR / T-IRR-2; P1-T07 step 2 | **yes** | yes (frames the terminal) | no (says nothing about *reaching* `∅`) | none (pure irreversibility) | — (this one holds) |
| P2 | `∅` is **reachable** under neutral dynamics | — | **no** | yes | no | **C** — "neutrality can always reach self-erasure" negates ε_pg's `B≥2` favouring | D2 (closed 2-cycle, `∅` unreachable); D5 (deterministic non-`∅` orbit) |
| P3 | per-step death hazard **positive** (`h_t>0`) | P1-T07 step 3 (asserted) | asserted, not justified | yes | no | weak **C** — positive drift toward self-erasure | D5 (`h_t=0` deterministic survival) |
| P4 | **cumulative hazard diverges** (`Σ h_t=∞` a.s.) | — (identified only in this audit) | **no** | yes (for a.s. termination, via Lévy) | **yes**, with P1 (closes Version B) | **C** — = "neutrality cannot sustain non-self-erasure", contrapositive of ε_pg | D1 (`h_t=2^{-t}`, `Σh_t<∞`, survives); D6 (`h_t↓0`) |
| P5 | **uniform hazard lower bound** (`h_t≥δ>0`) | — | **no** | no (stronger than needed) | **yes** (closes Version A: a.s. + finite `E[τ]`) | **D/E** — a *pro-closure* drift; not a model of neutrality | — (over-strong; wrong direction) |
| P6 | **no neutral closed communicating class avoiding `∅`** | — | **no** | yes | **yes**, with P1 & recurrence (closes Version C) | **C/D** — = ε_pg's non-self-erasure necessity restated | D2; D4 (reflecting non-terminating walk) |
| P7 | **recurrence / irreducibility to `∅`** | — | **no** | yes (for Version C) | no (needs P6 too) | **C** | D3 (transient toward a safe region) |
| P8 | **formal definition of "ε-neutral"** distinct from the closure condition | — (undefined in `Core/`, `Core_Law/`) | **no** | yes (else proof is vacuous or circular) | n/a | **decides the whole question**: if defined = "no hazard suppression" → theorem false; if defined = "non-summable hazard" → circular | D1–D6 all ambiguous without it |
| P9 | **stochastic transition model** on `A_t` | P1-T07 step 3 only (not in P1-T06) | proof-only | yes (the argument is probabilistic) | no | none directly | — (modeling gap: P1-T06 is non-probabilistic) |
| P10 | **askability / persistence prior** ("any accumulating/remembering position locally satisfies non-self-erasure") | `SRT_L0_Metaphysics.md:202` | **yes**, but scoped **local only** | it is the honest engine of the argument | closes a **local, conditional** version | **C** — the file says this **is** local ε, and only proves *local* ε | (this is the defensible core, see Proposals Option B) |

## Reading

- **P1** is the only premise that both holds and is ε-independent — and it is insufficient alone.
- The proof's validity turns on **P8** (undefined) and one of **P4 / P5 / P6+P7** (all unstated, all ε-co-referential except the illegitimate P5).
- **P10** is the corpus's own honest form of the argument, and it is explicitly **local** and **postulate-grade** — matching Proposals Option B.
- No combination closes the *strong, unconditional, ε-independent* theorem. Every closing set imports an ε-co-referential premise (P2/P4/P6/P7/P10) or an illegitimate one (P5).

## Cross-refs

- Full analysis, countermodels, gates: `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`.
- Amendment options: `Operations/Proposals/SRT_P1_T07_HARDENING_OPTIONS.md`.
- Prior dependency context: `Operations/Audits/Maps/SRT_EPSILON_PG_DEPENDENCY_MAP.md` (E2/E3), `Operations/Audits/SRT_CONCEPT_DELETION_PASS2_KAPPA_EPSILON.md` §11.4.
