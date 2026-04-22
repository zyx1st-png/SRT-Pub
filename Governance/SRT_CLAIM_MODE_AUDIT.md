---
id: SRT-CLAIM-MODE-AUDIT
type: governance
tags: [Governance, ClaimMode, Audit, Demotion, Hardening]
status: active_v0
layer: meta
epistemic_layer: os
claim_mode: governance
dependency: [SRT-CLAIM-LADDER, SRT-EDIT-PROTOCOL, SRT-CANONICAL-REGISTRY, SRT-CROSS-DOMAIN-MATRIX]
---

# SRT Claim-Mode Audit

> **Role**: first-pass governance ledger for claim-mode hardening. This file records downgrades and exposure controls; it does not create new theory or promote any claim.

## 1. Scan Scope

Full-repo markdown scan on 2026-04-22 found approximately:

| Label family | Occurrences | Files containing any scanned label |
|---|---:|---:|
| `T-*` | 1887 | 209 |
| `Ax-*` | 2803 | 209 |
| `H-*` | 603 | 209 |

This round does **not** claim to finish all historical label cleanup. It handles only high-leverage, low-risk demotions and adds guardrails where old labels remain for compatibility.

## 2. Demotion Decisions

| Old label / phrase | New label / status | Level | Action |
|---|---|---|---|
| `T-Phys-2` | `H-Phys-2` | hypothesis / bridge | Demote discrete-time claim from theorem voice to candidate bridge reading. |
| `T-Phys-4` | `H-Phys-4` | hypothesis / bridge | Demote gravity-friction claim from theorem voice to weak compatibility hypothesis. |
| `Ax-NEURO-4b` | `H-NEURO-4b` | hypothesis / operational proxy | Demote prediction-error friction mapping to P3/P4 candidate. |
| “不可言说性定理” / `T-Phil-1` where used as theorem of principle | `H-Phil-Ineffability` | hypothesis / bridge | Demote from theorem voice to dimensional-mismatch hypothesis with counterexample slots. |
| `Ax-Spirit-*` domain theology / praxis mappings | `H-Spirit-*` in active spirituality bridge files | bridge / hypothesis / companion | Demote obvious spiritual bridge labels that were historically written as axioms. |

## 3. Quick Rationale

| Claim | Can it be derived from L0/L1 alone? | Current honest status |
|---|---|---|
| `H-Phys-2` | No; depends on physical time interpretation and possible QG bridges. | P3/P4 candidate. |
| `H-Phys-4` | No; tensor-level GR reconstruction is missing. | P3/P4 weak compatibility hypothesis. |
| `H-NEURO-4b` | No; depends on measurable PE / metabolic coupling. | P3/P4 operational proxy. |
| `H-Phil-Ineffability` | Not as a theorem; depends on language capacity and dimensional assumptions. | P3 hypothesis with explicit escape routes. |
| `H-Spirit-*` | No; theology and praxis mappings do not define core necessity. | P3/P5 bridge / companion material. |

## 4. Downstream Reminder Rule

Any downstream conclusion that relies on a demoted item must add a level reminder in the nearest relevant section:

> **Level reminder**: this conclusion depends on a demoted bridge / hypothesis. It may guide interpretation or testing, but cannot be cited as a P0/P1 theorem.

## 5. Open Audit Debt

- Many older files still use `Theorem` and `Axiom` in historical or domain-local senses.
- Split / annex files mirror old labels and were not globally rewritten in this round.
- Generated / public / video material contains stronger rhetorical versions; those require a separate public-surface cleanup pass.
- P0-04 / “where selectability comes from” remains an unresolved core exposure point, not a solved theorem.
