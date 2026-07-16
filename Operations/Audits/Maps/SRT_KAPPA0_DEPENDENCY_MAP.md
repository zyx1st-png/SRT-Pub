---
id: SRT-OPS-AUDIT-MAP-KAPPA0
type: audit_map
status: record_v0_1
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-07-17
audited_object: "κ₀ / \\kappa_0 / primordial curvature / T-L0-Kappa0 / κ(t)"
source_of_truth: "origin/main @ f597786a (Pass 2 branch base)"
dependency:
  - SRT-GOV-SUB01-SUBTRACTIVE-AUDIT
tags: [Governance, SubtractiveAudit, DependencyMap, Kappa0]
---

# κ₀ Dependency Map (Concept Deletion Pass 2)

> **Status**: non-canonical audit map. Records the current-main dependency structure of `κ₀`. It changes no theory. Prior Claude/ChatGPT conclusions were treated as hypotheses; every node below was re-read on the Pass-2 branch base (`f597786a`).

## Aliases / notations searched

`κ₀`, `κ_0`, `\kappa_0`, `kappa_0`, `T-L0-Kappa0`, `T-L0-NonStatic`, `primordial curvature` / `原初曲率`, `κ(t)` / `\kappa(t)`, `Ψ_f^min = f(κ₀)`, `Align(θ, κ₀)`, `curvature floor` / `曲率下界`, `Ψ_f^budget/κ₀`.

## File-status legend

- **[C]** active + canonical (`claim_mode: canonical`, hardened)
- **[Cd]** active + canonical-mode but `draft_v0` / `P1-candidate` (provisional)
- **[A]** active, non-canonical (interpretive / philosophy authority)
- **[B]** bridge / lab
- **[S]** split mirror of a parent file (duplicated dependency, not an independent source)
- **[X]** archive / historical / book-draft (recorded only; **not** usable as current-main dependency)

## Node table (active dependencies only)

| # | Node (file · section) | Status | Claim level | Function κ₀ carries | First downstream break at K=0 | Redundant/alt carrier |
|---|---|---|---|---|---|---|
| K1 | `Core/SRT_Core_12a_Ontology_L0L1.md` · **T-L0-Kappa0** | [C] | canonical / axiomatic-hybrid | **Definition source.** κ₀>0 = irreducible Riemann-curvature lower bound of L₀; roles: (a) co-evolution direction field, (b) bootstrap gradient → Ĝ\* fixed-point existence (flat L₀ ⇒ no "landing" ⇒ no selection) | Ĝ\* fixed-point-existence argument; C1 and C2 below lose their premise | Partly `ε_pg` — the theorem calls itself "the **geometric refinement of T-Core-A1C2** (ε_pg / L₀ min non-neutrality)" |
| K2 | `Core/SRT_Core_12a` · **T-L0-Kappa0-C1** | [C] | canonical | `Ψ_f^min = f(κ₀) > 0` — friction floor | Justification that `Ψ_f` has a strictly positive floor | `Ψ_f>0` is also independently posited (Def-Ψ) |
| K3 | `Core/SRT_Core_12a` · **T-L0-Kappa0-C2** | [C] | canonical | `κ_c1 = g(κ₀, ∫F)` — source of the consciousness threshold's existence | κ_c1 existence-derivation | κ_c1 is itself P3/P4 (Pass 1.5 truth-up); threshold could be posited directly |
| K4 | `Core/SRT_Core_12a` · **T-L0-NonStatic** | [C] | canonical | `κ(t) = κ₀ + ∫F[Ĝ_θ,κ]dτ` — κ₀ = initial condition **and** irreducible floor; guarantees minimum openness never → 0 (anti-total-closure) | κ(t) has no initial value / no floor; "L₀ never fully closed" loses its guarantee | A generic positive `κ(0)` + positive floor (limited-K) |
| K5 | `Core/SRT_Core_22_Equations.md` · **Eq-DValue-Max-1** | [C] | canonical | `d_max = min(rank_eff(I_F), Ψ_f^budget/κ₀)` — κ₀ = **unit alignment cost**, the divisor of the stability/payability bottleneck | Stability-bottleneck term becomes undefined (division by deleted symbol); info-vs-stability distinction unwritable | **Any positive unit-cost coefficient `c>0`** reproduces the two-bottleneck form (limited-K) |
| K6 | `_SRT_D_VALUE_CANONICAL.md` · d_max block | [C] | canonical | Restates Eq-DValue-Max-1 (`Ψ_f^budget/κ₀`); "d_max ≠ 0 because κ₀>0" | Same as K5 | Mirror of K5 (duplicated) |
| K7 | `Core/SRT_Core_01_Axioms.md` · **MA-1** | [C] | canonical (meta-axiom) | κ₀>0 = primordial directionality; structural prerequisite for Ĝ\* fixed points; "not a product of history" | MA-1's non-symmetry claim | Co-refers with T-Core-A1C2 (ε_pg) |
| K8 | `Core/SRT_Core_01_Axioms.md` · **MA-2** | [C] | canonical (meta-axiom) | `Align(θ, κ₀)` comparable across perspectives; d = operationalization of alignment degree | d-as-alignment interpretation | — (unique interpretive role) |
| K9 | `D_VALUE_ALIGNMENT.md` · §4.4 | [A] | interpretive (P2) | `d ∝ Align(θ, κ(t))`; `‖∂U/∂S‖` measures fit of concern-map with κ₀ / κ(t) — geometric base of d | "why ∂U/∂S is the right quantity" explanation | — (this is d's geometric grounding) |
| K10 | `Philosophy/SRT_L0_Ontological_Status.md` · §三 §四 | [A] | philosophy authority (P2) | **Deepest role.** L₀ reality ≡ `Ψ_f>0 ∧ κ₀>0 ∧ ∃asymmetry` (functional constitutivism); κ₀ = **L₀'s only accessible face**, encountered as asymmetric selection cost | The functional-constitutivism account of how L₀ is accessible at all | — (no substitute; §二 also admits κ₀'s own origin is **open**) |
| K11 | `Core/SRT_Core_12b_Ontology_L2.md` · Co-Evolution / κ_c1 | [C] | canonical | κ₀ in co-evolution & κ_c1 context | interpretive continuity | mirror of K3/K4 |
| K12 | `Philosophy/SRT_Causality_Time.md`; `Core_Law/SRT_Individuation.md`; `Philosophy/SRT_Consciousness_Conditions.md` | [A] | interpretive | cite κ₀ for bootstrap / time / κ_c1 | none load-bearing (cited, not constitutive) | — |
| K13 | `_SRT_SYMBOL_TABLE.md` · κ₀, κ(t) rows | [C] | canonical registry | Registry definition + κ namespace guard (Usage Rule 15) | registry entry | — |
| — | `Manifesto/SRT_MANIFESTO.md`; `Neuroscience/SRT_Neuro_08_Immune_Dist.md` | [A]/[B] | narrative / bridge | slogan / domain echo | none | — |

**Split mirrors [S] (duplicated, not independent):** `Core/Ontology_L0L1_Split/00_Part01.md`, `Core/Equations_Split/00_Part01.md`, `Core/Axioms_Split/00_Part01.md`, `Core/Ontology_L2_Split/00_Part01.md`.

**Archive [X] (recorded, NOT current-main dependency):** `01_Source_Intuition/BOOK/Archive_52Chapter/**`, `90_Backstage/Restructure_2026/**`, versioned book drafts. These reuse κ₀ language for exposition; per GOV-SUB01 they cannot establish load-bearing dependency.

## Edge classification

| Edge | Type | Direct/Transitive | Load-bearing? |
|---|---|---|---|
| T-L0-Kappa0 → Eq-DValue-Max-1 (κ₀ as divisor) | equation-input | direct | **yes** (equation breaks at K=0) |
| T-L0-Kappa0 → T-L0-Kappa0-C1 (Ψ_f floor) | theorem/proof | direct | yes |
| T-L0-Kappa0 → T-L0-Kappa0-C2 (κ_c1 source) | theorem/proof | direct | partial (κ_c1 is P3/P4) |
| T-L0-Kappa0 → T-L0-NonStatic (κ₀ as κ(t) floor+IC) | definitional | direct | yes |
| T-L0-Kappa0 ↔ Ax-L0-Bootstrap (κ₀ = geometric source of fixed points; bootstrap = why κ₀ needs no prior cause) | definitional | **circular / mutually-defining** | yes (bootstrap anchor) |
| T-Core-A1C2 (ε_pg) ↔ T-L0-Kappa0 (κ₀) | definitional (co-reference) | direct | **shared commitment** — κ₀ = "geometric refinement" of ε_pg's non-neutrality |
| MA-2 / D_VALUE_ALIGNMENT → d (Align base) | interpretive | direct | yes (d's geometric grounding) |
| L0_Ontological_Status → κ₀ (only accessible face) | interpretive (ontological) | direct | yes (deepest, no substitute) |
| Consciousness_Conditions / Causality_Time / Individuation → κ₀ | narrative-only / cited | transitive | **no** (cited, not load-bearing) |

## Merely-cited-but-not-load-bearing

`Manifesto`, `Neuroscience/Immune_Dist`, `Causality_Time`, `Individuation`, `Consciousness_Conditions` cite κ₀ to inherit its authority but do not break if κ₀'s **symbol** changes (they depend on the *role*, sourced upstream).

## Key structural observations (evidence, not verdicts)

1. **κ₀ has a spread of roles, not one.** Equation divisor (K5/K6) · Ψ_f floor (K2) · κ_c1 source (K3) · κ(t) IC+floor (K4) · d-alignment base (K8/K9) · L₀ accessibility (K10) · fixed-point existence (K1/K7). A single residue label would be false; classification must be per-role (see main report §7).
2. **The divisor role (K5) is the most substitutable**; the accessibility role (K10) is the least.
3. **κ₀ co-refers with ε_pg.** T-L0-Kappa0 is self-described as the geometric refinement of T-Core-A1C2 (ε_pg). They are not fully independent primitives (see joint tests, main report §5–§8).
4. **κ₀'s own origin is admitted-open** by its own authority file (`L0_Ontological_Status §二`, §"open questions"), consistent with `Core/SRT_OPEN_TENSIONS.md §7 / P0-04`.
