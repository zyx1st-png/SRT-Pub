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

| # | Premise | Source in corpus | Explicit? | Global necessity / package role | Sufficient (alone)? | ε_pg co-reference | Countermodel if missing |
|---|---|---|---|---|---|---|---|
| P1 | `∅` (`A_t=∅`) is **absorbing** | `SRT_Irreversibility.md` Def-IRR / T-IRR-2; P1-T07 step 2 | **yes** | **framing prerequisite** — defines the terminal; not a proof-driving premise | no (says nothing about *reaching* `∅`) | none (pure irreversibility) | — (this one holds) |
| P2 | `∅` is **reachable** under neutral dynamics | — | **no** | **entailed *within* each sufficient package** (A/B/C each imply reachability); not a separate global necessity | no | **E — pending source**: could be an independent state-space geometry / neutral kernel, or a projection of ε_pg's `B≥2` favouring | D2 (closed 2-cycle, `∅` unreachable); D5 (deterministic non-`∅` orbit) |
| P3 | per-step death hazard **positive** (`h_t>0`) | P1-T07 step 3 (asserted) | asserted, not justified | **original proof assertion; not globally necessary** (Package C can absorb without per-step positivity) | no | **E — pending kernel**: a property of the transition kernel, not intrinsically ε | D5 (`h_t=0` deterministic survival) |
| P4 | **cumulative hazard diverges** (`Σ h_t=∞` along surviving histories) | — (identified only in this audit) | **no** | **sufficient Package B; exact necessity pending** (semantics-dependent) | **yes**, alone (closes Version B) | **E — pending neutral-kernel definition**: may restate ε_pg's non-self-erasure, or may follow from an independent kernel | D1 (`h_t=2^{-t}`, `Σh_t<∞`, survives); D6 (`h_t↓0`) |
| P5 | **uniform hazard lower bound** (`h_t≥δ>0`) | — | **no** | **sufficient Package A; not necessary** (stronger than needed) | **yes** (closes Version A: a.s. + finite `E[τ]`) | **E — pending kernel**: may arise from unbiased kernel geometry; **not** intrinsically pro-closure; absent from corpus | — (over-strong; not needed if B or C holds) |
| P6 | **no neutral closed communicating class avoiding `∅`** | — | **no** | **Package C component; not globally necessary** | **yes**, with recurrence (closes Version C) | **E — pending topology/model**: could be supplied by an independent kernel geometry rather than ε_pg | D2; D4 (reflecting non-terminating walk) |
| P7 | **recurrence / irreducibility to `∅`** | — | **no** | **Package C component; not globally necessary** | no (needs P6 too) | **E — pending model**: structural chain property, not intrinsically ε | D3 (transient toward a safe region) |
| P8 | **formal definition of "ε-neutral"** distinct from the closure condition | — (undefined in `Core/`, `Core_Law/`) | **no** | **semantic/model prerequisite** (else proof is vacuous or circular) | n/a | **decides the whole question**: if defined = "no hazard suppression" → theorem false; if defined = "non-summable hazard" → circular (**D**) | D1–D6 all ambiguous without it |
| P9 | **stochastic transition model + stability semantics** (S1/S2/S3) on `A_t` | P1-T07 step 3 only (not in P1-T06) | proof-only; semantics unfixed | **semantic/model prerequisite** (the argument is probabilistic; the theorem needs a chosen semantics) | no | none directly | — (modeling gap: P1-T06 is non-probabilistic and semantics-undetermined) |
| P10 | **askability / persistence prior** ("any accumulating/remembering position locally satisfies non-self-erasure") | `SRT_L0_Metaphysics.md:202` | **yes**, but scoped **local only** | **optional local ε bridge** (honest engine of the *local* argument; not required for Packages A/B/C) | closes a **local, conditional** version | **C** — the file says this **is** local ε, and only proves *local* ε | (the defensible core, see Proposals Option B) |

## Reading

- **P1** is the only premise that both holds and is settled ε-independent — and it is insufficient alone.
- The proof's validity turns on **P8** (undefined) + a chosen **P9** semantics + one sufficient package (**P4** alone, or **P5**, or **P6+P7**).
- **Only P10 is settled ε-co-referential (C); P8's circular horn is D.** The structural premises **P2/P3/P4/P5/P6/P7 are E — undecided pending an independently specified neutral kernel/geometry**; they are **not** automatically ε_pg in disguise (revised from Proof-Audit-1.0, which over-classified them as C/D, and from 1.1, which still tagged P5 as a pro-closure drift).
- No combination **currently** closes the *strong, unconditional, ε-independent* theorem — but ε-independence is **not disproven**; it turns on whether an independent neutral kernel can be shown to absorb a.s. (Proposals Option B-lite).

## Cross-refs

- Full analysis, countermodels, gates: `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`.
- Amendment options: `Operations/Proposals/SRT_P1_T07_HARDENING_OPTIONS.md`.
- Prior dependency context: `Operations/Audits/Maps/SRT_EPSILON_PG_DEPENDENCY_MAP.md` (E2/E3), `Operations/Audits/SRT_CONCEPT_DELETION_PASS2_KAPPA_EPSILON.md` §11.4.
