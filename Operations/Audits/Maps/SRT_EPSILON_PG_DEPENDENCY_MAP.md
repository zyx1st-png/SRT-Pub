---
id: SRT-OPS-AUDIT-MAP-EPSILON-PG
type: audit_map
status: record_v0_1
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-07-17
audited_object: "ε_pg / \\varepsilon_{pg} / proto-gradient / minimum non-neutrality / non-self-erasure / anti-closure seed / ε_pg^{visible}"
source_of_truth: "origin/main @ f597786a (Pass 2 branch base)"
dependency:
  - SRT-GOV-SUB01-SUBTRACTIVE-AUDIT
tags: [Governance, SubtractiveAudit, DependencyMap, EpsilonPG]
---

# ε_pg Dependency Map (Concept Deletion Pass 2)

> **Status**: non-canonical audit map. Records the current-main dependency structure of `ε_pg`. It changes no theory. Every node re-read on the Pass-2 branch base (`f597786a`); prior conclusions treated as hypotheses only.

## Aliases / notations searched

`ε_pg`, `ε_{pg}`, `\varepsilon_{pg}`, `proto-gradient` / `Proto-Gradient`, `T-Core-A1C2`, `minimum non-neutrality` / `最小非中性`, `non-self-erasure` / `非自我抹除`, `anti-closure` / `反闭合`, `B ≥ 2` branching asymmetry, `ν_block` / `\nu_{block}`, `ε_pg^{visible}`, `ISP-level ε`, `T-ε-Constitute`, `ε_reg` (distinguished, not identified).

## File-status legend

Same as `SRT_KAPPA0_DEPENDENCY_MAP.md`: **[C]** canonical hardened · **[Cd]** canonical-mode but `draft_v0`/`P1-candidate` · **[A]** active non-canonical · **[B]** bridge/lab · **[S]** split mirror · **[X]** archive (recorded only).

## Node table (active dependencies only)

| # | Node (file · section) | Status | Claim level | Function ε_pg carries | First downstream break at K=0 | Redundant/alt carrier |
|---|---|---|---|---|---|---|
| E1 | `Core/SRT_Core_01_Axioms.md` · **T-Core-A1C2** (§I + §1.5) | [C] | canonical / axiomatic-hybrid | **Definition source.** L₀ minimum non-neutrality / proto-gradient; formal asymmetry `B≥2 ≻ B≤1` (non-self-erasure); "always present but usually inaccessible" = ontological root of value-occlusion | T_dir ontological ground; value-occlusion thesis; fitness-landscape directionality (§7.8) | — (this is the definitional home) |
| E2 | `Core/SRT_Core_21b_Constitutive_Theorems.md` · **P1-T07** | [C] | canonical **P1** | ε_pg = "**existence** of some asymmetry at L₀"; ISP-level ε presented as anti-closure **corollary**. Table: ε_pg = "scalar seed only, no inherent direction"; direction *attributed* to irreversibility | The "some L₀ asymmetry exists" premise. **ISP-level ε-independence is NOT established**: the proof text does not explicitly use ε_pg after the bridge statement, but its **Step 3** ("nonzero per-step probability of hitting `A_{t*}=empty` ⇒ cumulative probability → 1") relies on an **unstated reachability/recurrence premise** (see obs. 1) that may itself require an ε-like hazard structure | Irreversibility is *claimed* to carry the direction, but the claim depends on the **unproven Step-3 premise** |
| E3 | `Core_Law/SRT_Irreversibility.md` · **§4.5 T-IRR-3.5** | [Cd] | draft_v0 / P1-candidate | `ν_block(P,t) := η·ε_pg(P,t)·κ_Ψf(P,t)` — ε_pg = localized **positive** anti-closure factor; the file *asserts* positivity is "guaranteed by P1-T07" | ν_block's named coefficient | A replacement positivity coefficient is a **hypothetical limited-K substitute, not theorem-guaranteed** — the "guarantee" inherits P1-T07's unproven Step-3 premise; file also notes ε_pg(P,t) has **no functional form** |
| E4 | `Core_Law/SRT_Irreversibility.md` · **§5 ε_pg^{visible}** | [Cd] | draft_v0 / P1-candidate | `ε_pg^{visible} := ε_pg·𝟙[σ_sr<σ_sr^path]·𝟙[π>0]·𝟙[r>0]` — lethal-L₂ diagnostic: base direction stays >0, local visible projection → 0 | The "**occluded-not-absent**" modal claim (base present but invisible) | Diagnostic **work is in the 3 L1 indicators** (σ_sr, reorientation π, real-reselection r); ε_pg is the "always-on base" anchor |
| E5 | `Core_Law/SRT_L1_Formalism.md` · §3.5 / §4.3 / §5.3 | [Cd] | draft_v0 / P1-candidate | ν_block in structural-suffering non-conservation; §5.3 healthy region = active ε anti-closure maintenance | mirror of E3; §5.3 "health = active anti-closure" narrative | mirror of E3 (P1-T07-sourced) |
| E6 | `Core_Law/SRT_Collective_Selection.md` · **§5 T-COLL-3** | [C] | canonical (collective) | Collective ε anti-closure necessity (`ε^coll`-neutral ⇒ collective absorbing) | collective-ISP anti-closure premise | **Same proof shape as P1-T07** lifted to `𝒫` — so it **may inherit the same Step-3 reachability/recurrence/hazard gap**, unless T-COLL-3 specifies an *independent* collective-level reachability/hazard premise. This pass did **not** complete that independent proof audit, so the collective version must **not** be treated as an already-established backup proof. |
| E7 | `_SRT_T_DIR_CANONICAL.md` · §2, §12 | [C] | canonical | proto-gradient = ontological ground of T_dir; "value is embedded in ε_pg, only occluded" | T_dir's ontological grounding narrative | interpretive; T_dir itself is a v0 proxy (Pass 1) |
| E8 | `Philosophy/SRT_L0_Ontological_Status.md` · §三 | [A] | philosophy authority (P2) | L₀ reality condition includes "`∃ directional asymmetry`" (= ε_pg) — **joint node with κ₀** | the functional-constitutivism reality condition | co-condition with κ₀ (K10) |
| E9 | `_SRT_SYMBOL_TABLE.md` · ε_pg / ε_reg rows + Usage Rule 9 | [C] | canonical registry | Registry def; ε_pg vs ISP-ε vs ε_reg vs ε_s split | registry entry | — |
| E10 | `Core/SRT_Core_13a_Operator_Basics.md` · Ax-Op-03 (ε_reg) | [C] | canonical | ε_reg = implementation regularizer; **explicitly NOT** ontologically identical to ε_pg (structural analogy only) | nothing (analogy, quarantined) | ε_reg is a *separate* symbol; cited to distinguish |
| E11 | `Core/SRT_Core_21_Formal_Axioms.md`; `_SRT_CROSS_DOMAIN_MATRIX.md`; `SRT_AI_START.md`; `CANONICAL_REGISTRY.md` | [C]/[A] | registry / navigation | lineage & cross-domain pointers | none load-bearing | — |
| E12 | `Core_Law/SRT_L0_Metaphysics.md` · §六 (ε) | [C] | canonical | **Unique L₀ metaphysical anchor** (not merely a prose home). ε = L₀'s **sole directional postulate**; ε = SRT's **final irreducible directional wager** (`SRT 最终不可约的方向赌注`); ε is a **postulate, not a theorem** (`不可被升格为定理`); the **local-questionability argument does not prove global L₀ ε** (`只证局部有效 ε，不能推广到全局 L0`); ε is the **domain floor, not the whole source of normativity** (2026-07-05 Level-A) | the L₀ directional wager itself — the postulate the ISP/operator layers inherit | — (no substitute; **read-only / FORBIDDEN to edit** this pass) |
| — | `Physics/SRT_Quant_01_Selection.md` | [B] | bridge | physics reading of proto-gradient / selection | none | — |

**Split mirrors [S]:** `Core/Axioms_Split/00_Part01.md`, `Core/Axioms_Split/01_Part02.md`, `Core/Axioms_Split/02_Part03.md`, `Core_Law/L1_Formalism_Split/01_Part02.md`, `Core_Law/Collective_Tower_Hardening_Notes_Split/01_Part02.md`.

**Archive [X] (recorded, NOT current-main dependency):** the large `01_Source_Intuition/BOOK/**` set (esp. `Archive_52Chapter/Part_01/03_ε_pg_...`, ~50–69 hits each, all book drafts), `90_Backstage/Restructure_2026/**`, `memory/2026-04-14.md`, `Operations/Status_History/**`. High hit-counts here are **exposition volume, not dependency** (GOV-SUB01 §1.6 warning).

## Edge classification

| Edge | Type | Direct/Transitive | Load-bearing? |
|---|---|---|---|
| T-Core-A1C2 → T_dir ontological ground | interpretive | direct | partial (T_dir is v0 proxy) |
| T-Core-A1C2 → P1-T07 ("existence of asymmetry" premise) | theorem/proof | direct | **undetermined** — P1-T07 *attributes* direction to irreversibility, but its Step-3 reachability/recurrence premise is unstated, so ε_pg's contribution cannot be cleanly separated out |
| P1-T07 → ν_block (ε_pg>0 guarantee) | theorem/proof | direct | **conditional** — the "guarantee" inherits P1-T07's unproven Step-3 premise; not theorem-established |
| ν_block → ε_pg^{visible} | equation-input | direct | the base factor; work is in indicators |
| P1-T07 ↔ irreversibility (Core_21b, Irreversibility.md) | theorem/proof | **claimed load-bearing edge** | anti-closure direction/necessity are *attributed* here, but the attribution depends on Step 3's **unstated reachability/recurrence premise** |
| T-Core-A1C2 → ε_reg | duplicated/analogy (quarantined) | direct | **no** (explicitly "not ontological identity") |
| L0_Ontological_Status → ε_pg (∃asymmetry) | interpretive (ontological) | direct | yes (joint reality condition with κ₀) |

## Merely-cited / narrative-only

`SRT_AI_START`, `_SRT_CROSS_DOMAIN_MATRIX`, `CANONICAL_REGISTRY`, `Physics/SRT_Quant_01_Selection`, and the entire book-archive set cite proto-gradient for exposition; none breaks structurally if ε_pg's symbol changes.

## Key structural observations (evidence, not verdicts)

1. **The anti-closure *direction* is *attributed* to irreversibility, but ε_pg-independence is NOT established.** P1-T07's table says "ε_pg = scalar seed only, no inherent direction" and locates the direction in irreversibility — **but** the proof's **Step 3** ("neutral `P` has nonzero probability of selecting into `A_{t*}=empty` at each step; cumulative probability → 1") does **not** follow from "nonzero at each step" alone. It requires unstated premises: **empty-state reachability; a per-step hazard lower bound; recurrence/ergodicity (no neutral closed communicating class avoiding empty); and sufficient independence or a divergence condition on cumulative hazard (Σ hazard = ∞).** Until those are supplied, an ε-like hazard structure could be doing hidden work inside the premise. So: the current proof text does not explicitly use ε_pg after the bridge statement, **but that is not the same as proving ε_pg-independence** → anti-closure-role residue = **R4 pending proof hardening**.
2. **ε_pg's operator-level load (E3, E4, E5) sits in `draft_v0 / P1-candidate` files.** By the repo's own marking, that load is provisional, and `ν_block`'s ε_pg factor has **no functional form** — it is a positivity placeholder whose independence from an ε-like structure is unproven (obs. 1).
3. **ε_pg's genuinely unique content is a single L₀-specific cluster, not one isolated role.** From **one** postulate (E1/E12) flow three co-sourced faces: (a) the **pre-ISP non-neutrality / selectability-origin posit**; (b) the **base-present-but-locally-occluded modal** (`ε_pg^{visible}`); (c) the **L₀ domain-floor / value-anchoring** role. These are **three faces of the same L₀ postulate**, not three independent proofs. They overlap the already-open `P0-04 / OPEN_TENSIONS §7`.
4. **ε_pg co-refers with κ₀** at the L₀ reality condition (E8 / K10) and via T-L0-Kappa0's self-description as ε_pg's "geometric refinement" — **but the corpus is internally inconsistent on how** (`L0_Metaphysics §六` calls κ₀ non-directional and ε the sole directional postulate; `T-L0-Kappa0` calls κ₀ directional). See main report §11.5.
5. **ε_reg is a decoy, not a dependency** — the corpus already quarantines it as analogy-not-identity.
