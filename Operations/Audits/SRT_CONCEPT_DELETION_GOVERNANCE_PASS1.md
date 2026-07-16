---
id: SRT-OPS-AUDIT-CONCEPT-DELETION-GOV-PASS1
type: audit_record
status: record_v0_1
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-07-16
dependency:
  - SRT-GOV-SUB01-SUBTRACTIVE-AUDIT
  - SRT-CLAIM-LADDER
  - SRT-EDIT-PROTOCOL
  - SRT-SYMBOL-TABLE
  - SRT-OPEN-TENSIONS
tags: [Governance, SubtractiveAudit, AuditRecord, SymbolTable, ClaimDiscipline]
---

# Concept Deletion Governance Pass 1 — Audit Record

> **Status**: non-canonical Operations record. This file logs a low-risk governance pass under `Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md`. It does **not** define SRT ontology, does not assign residue labels (`R*/N*/P`) to any core symbol, and does not promote any deletion result to a theorem.

## 0. Scope of this pass

This pass applies GOV-SUB01 at the **governance / classification layer only**. It reclassifies and annotates; it deletes, renames, and refits nothing. No actual subtractive deletion test (`M^{-x}`) was executed against any core symbol. What the pass produces is the *scaffolding* that a real Pass-2 deletion test needs: a tier separation, thin universal definitions, a namespace guard, and a registered irreducibility test.

## 1. GOV-SUB01 audit targets used

The pass was scoped to preserve the following targets (`Y`, per GOV-SUB01 §2 / §6 Step 1), under context `C` = repository-wide canonical registry, cross-domain writing, and AI parsing:

1. **Preserve the "selection precedes stable existence" theoretical difference** — protected by leaving `P0-01` untouched and registering the irreducibility test as open (not closed either way).
2. **Preserve the real-choice / script-execution / ordinary-transition distinction** — protected by leaving `P1-T05` untouched and citing it inside the deletion test.
3. **Preserve the subject / stake / consequence-bearer distinction** — protected by keeping `d`, `Ψ_f`, `T_dir`, bearing, and consequence-return language canonical and unmodified.
4. **Preserve history-lock / pathological-closure / reselectability diagnostics** — protected by leaving `ε_pg`, `κ_0`, `ν_block`, and `ε_pg^{visible}` and their equations untouched.
5. **Preserve the capacity to generate experiments, counterfactuals, and interventions** — advanced by registering the §13 deletion test with an explicit `E_cf / E_int / E_phen / E_norm` discharge condition.

**Additional table-hygiene target**: stop "registered in the canonical symbol table" from being read as "equal theoretical indispensability" (GOV-SUB01 §0, §1.6, §7.4).

## 2. Per-modification refit-budget classification (K = 0 / limited K / broad K)

Per GOV-SUB01 §3, refit budget `K` is declared for each change so representational replaceability is not confused with role absence. **Every edit in this pass is `K = 0` (governance annotation; literal dependencies and equations unchanged).** No `limited K` or `broad K` deletion test was performed; those are deferred (see §6).

| Edit | What changed | Refit budget | What was NOT tested this pass |
|---|---|---|---|
| **A. Symbol-table tier layering** | Added a 3-tier classification (Core semantic roles / Derived structural quantities / Bridge-Lab proxies & thresholds) as an overlay; no row removed or edited | `K = 0` | The `limited K` / `broad K` deletion tests that would justify actually *removing* any symbol from the table |
| **B. L0/L1 thin universal definitions** | Moved `∞-dim Hilbert space` (L₀) and `4D spacetime + qualia` (L₁) from the universal `Dimensions` cell to marked **domain projections** with backlinks; universal cell thinned | `K = 0` | Whether L₀/L₁ can dispense with the Hilbert / spacetime realizations under any refit — a domain-projection question, not run here |
| **C. κ namespace guard** | Added Usage Rule 15 distinguishing `κ_0`/`κ(t)` (L₀ curvature) from `κ_{c1}`/`κ_{c1.5}` (consciousness thresholds), with claim-level annotation | `K = 0` | No rename (a rename would be a `limited K` representational change); no equation over any `κ` touched |
| **D. §13 selection-irreducibility tension** | Registered the competitor-vocabulary deletion test for `selection` as **open**; classified `selection` as `N1 + P` | none executed — registers the `limited K` and `broad K` questions as future work | The deletion test itself: no `selection` removal was performed; `N1 → N2` remains undischarged |

## 3. Modified files

1. `_SRT_SYMBOL_TABLE.md` — Task A (new "Governance Tier Layering" section), Task B (L₀ + L₁ rows: thin universal definition + domain-projection notes), Task C (Usage Rule 15 κ namespace split).
2. `Core/SRT_OPEN_TENSIONS.md` — Task D (new §13 + one summary-table row).
3. `Operations/Audits/SRT_CONCEPT_DELETION_GOVERNANCE_PASS1.md` — this record (new; new directory `Operations/Audits/`).

## 4. Explicitly unmodified (protected) files

Read and/or depended upon, but **not** modified — semantics, equations, axioms, theorems, and canonical definitions intact:

- `Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md` — read as the governing protocol.
- `Core_Law/SRT_L0_Metaphysics.md` — L₀/L₁ substantive semantics untouched (Task B only relocated table-level dimensional readings; the thin structural home is this file, unchanged).
- `Core/SRT_Core_21_Minimal_Axioms.md` — `P0-01…P0-04` semantics untouched.
- `Core/SRT_Core_22_Equations.md` — all equations untouched; `d_max = min(rank_eff, Ψ_f^{budget}/κ_0)` intact.
- `Core_Law/SRT_Irreversibility.md` — `ν_block = η·ε_pg·κ_{Ψf}` and `ε_pg^{visible}` untouched.
- `Core/SRT_Core_21b_Constitutive_Theorems.md` — `P1-T05 / P1-T06 / P1-T07` untouched.
- `_SRT_D_VALUE_CANONICAL.md`, `_SRT_PSI_F_CANONICAL.md`, `_SRT_T_DIR_CANONICAL.md` — canonical definitions of `d`, `Ψ_f`, `T_dir` untouched.
- `Philosophy/SRT_Consciousness_Conditions.md`, `Philosophy/SRT_L0_Ontological_Status.md` — the `κ_{c1}/κ_{c1.5}` and `κ_0` canonical sources cited by Usage Rule 15 are untouched.

## 5. Found-but-deferred dependencies

Surfaced during the pass; deliberately **not** acted on (out of this pass's low-risk scope):

- **`κ_0` is load-bearing in the d-value equation layer.** `Core/SRT_Core_22_Equations.md` Eq-DValue-Max-1 uses `Ψ_f^{budget}/κ_0` as the stability-bottleneck denominator, and `κ(t) = κ_0 + ∫F[…]` (T-L0-NonStatic) couples it to operator dynamics. Any future `κ_0` change ripples into `d_max` and `κ(t)`. Not touched.
- **`ε_pg` is load-bearing in the L1 operator layer.** `Core_Law/SRT_Irreversibility.md` binds `ε_pg` into `ν_block` and into the lethal-`L_2` diagnostic `ε_pg^{visible}`; `Core/SRT_Core_21b P1-T07` bridges `ε_pg` → ISP-level `ε`. Deleting or downgrading `ε_pg` is therefore **not** a free `K = 0` move; it requires the Pass-2 dependency graph. Not touched.
- **Scope-column vs claim-level mismatch.** `κ_{c1}`, `κ_{c1.5}`, and the `σ_{sr}^{sub/self/health}` thresholds carry Scope `"Core"` in the table while their canonical sources mark them P3/P4. This pass annotated the mismatch (tier + Usage Rule 15) but did **not** rewrite those rows' Scope cells (row edits on equation-referenced rows are out of scope). A Scope truth-up is a Pass-2 candidate.
- **Borderline tier assignments.** `F_SRT`, `S_c`, `μ`, `ε_reg`, and `σ_{sr}^{coll}` are provisional Tier-2/Tier-3 calls; flagged in the table as revisited in Pass 2.

## 6. Pass 2 plan — `κ_0` / `ε_pg` dependency-graph audit

Before any residue label (`R*/N*/P`) is assigned to `κ_0` or `ε_pg`, Pass 2 must:

1. **Enumerate the full citation graph** for each: every equation, theorem, and bridge that references it — at minimum `Core/SRT_Core_22_Equations.md` (Eq-DValue-Max-1, Eq-Multi-03), `Core/SRT_Core_12a` (T-L0-Kappa0, T-L0-NonStatic, Co-Evo-1 `κ(t)` coupling), `Core_Law/SRT_Irreversibility.md` (T-IRR-3 / T-IRR-3.5, `ν_block`, `ε_pg^{visible}`), `Core/SRT_Core_21b` (P1-T07), and `Philosophy/SRT_L0_Ontological_Status.md`.
2. **Run GOV-SUB01 §5 single-removal and §6 joint-removal** at each declared refit budget (`K = 0` literal, limited `K`, broad `K`), recording `Δ_x` per the §4 evaluation vector — especially `E_cf`, `E_mech`, and the §7.2 short-horizon-masking and §7.3 redundancy checks (a backup path may hide necessity).
3. **Only then** assign a residue label and route any status change through `Governance/SRT_CLAIM_LADDER.md`. Pass 1 assigns none.

The `selection` irreducibility test (`OPEN_TENSIONS §13`) is a parallel Pass-2+ workstream with its own discharge condition; it is not blocked on the `κ_0`/`ε_pg` graph.

## 7. Canonical-invariance statement

**This pass changes no canonical SRT ontology.** Specifically, it does not:

- delete, downgrade, or redefine `κ_0` or `ε_pg`;
- modify `d_max`, `ν_block`, `ε_pg^{visible}`, or any other equation;
- change the semantics of any `P0`/`P1` axiom or theorem;
- change the canonical definitions of `d`, `Ψ_f`, or `T_dir`;
- delete `L_0`, `L_1`, or `L_2`;
- introduce any new canonical symbol;
- promote any deletion-audit result to a theorem or to `N2`.

All changes are governance-layer classification, thin-definition relocation with retained backlinks, namespace annotation, and one open-tension registration. Residue classification of the audited concepts is explicitly **deferred** to Pass 2.
