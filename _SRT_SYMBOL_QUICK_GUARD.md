---
id: SRT-SYMBOL-QUICK-GUARD
type: guardrail
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
dependency: [SRT-SYMBOL-TABLE, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-CLAIM-LADDER]
ai_role: bootstrap_symbol_guard
ai_priority: 1
---

# SRT Symbol Quick Guard

> Fast symbol-risk guard for fresh sessions. This file is not a replacement for `_SRT_SYMBOL_TABLE.md`; use the full symbol table and canonical anchors when exact definitions, equations, or notation conflicts matter.

## Use this file when

- A fresh session needs the high-risk symbol boundaries before choosing retrieval depth.
- A claim mentions `d`, `D_eff`, `Ψ_f`, `T_dir`, `L_0/L_1/L_2`, `Ĝ_θ`, `ε`, or `σ`.
- A domain, bridge, lab, companion, public, or material-fusion text risks upgrading a proxy into a definition.

## Hard boundaries

| Symbol / term | Fast guard | Definition authority |
|---|---|---|
| `L_0` | Structured latent possibility, not nothingness and not physical vacuum by default. | `Core_Law/SRT_L0_Metaphysics.md`, `_SRT_SYMBOL_TABLE.md` |
| `L_1` | Manifest selected slice / event / state, not merely material objects. | `_SRT_SYMBOL_TABLE.md`, Core ontology files |
| `L_2` | Convergence-history / stable constraint domain; not identical to any one landscape, institution, memory, or scaffold. | `_SRT_SYMBOL_TABLE.md`, `Core/SRT_OPEN_TENSIONS.md` |
| `Ĝ_θ` | Embodied/parameterized selection or anchoring operator; implementation analogues do not define it. | `Core/SRT_Core_21_Minimal_Axioms.md`, `_SRT_SYMBOL_TABLE.md` |
| `d` | Scalar summary of stake-coupled concern / irreversible-risk sensitivity by default. Competence, capacity, preference, or distinguishability is not enough. | `_SRT_D_VALUE_CANONICAL.md`, `_SRT_SYMBOL_TABLE.md` |
| `D_eff` | Geometric capacity proxy / upper-bound candidate, not canonical `d`. | `_SRT_D_VALUE_CANONICAL.md`, `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ψ_f` | Payability burden / ontological friction. Fisher geometry, metabolic cost, stress, or pain are conditional projections only. | `_SRT_PSI_F_CANONICAL.md`, `_SRT_SYMBOL_TABLE.md` |
| `T_dir` | v0 operational proxy for readability / reorientation of the system's own selection direction; not reward, confidence, semantic valence, or coherence. | `_SRT_T_DIR_CANONICAL.md`, `_SRT_SYMBOL_TABLE.md` |
| `ε_pg` | L0 minimum non-neutrality postulate; do not identify with consciousness. | `_SRT_SYMBOL_TABLE.md`, Core P0/P1 sources |
| `ε_reg` | Implementation regularizer; only an analogy/echo of `ε_pg` unless separately argued. | `_SRT_SYMBOL_TABLE.md` |
| `ε_s` | Stake-threshold bridge for direction-level admission; not stake itself. | `_SRT_SYMBOL_TABLE.md`, `_SRT_D_VALUE_CANONICAL.md` |
| bare `σ` | Defaults to main-equation state field. Use `σ_sr` for self-reference ratio and `σ_j` for anchoring sub-targets. | `_SRT_SYMBOL_TABLE.md` |

## Proxy rule

If a statement says `proxy X = SRT variable Y`, rewrite it unless the canonical file explicitly licenses that identity.

Safer forms:

- `X is a candidate proxy for Y under stated conditions.`
- `X maps to one projection of Y, not to Y itself.`
- `X supports a bridge/lab hypothesis about Y, not a canonical definition.`

## Claim-level rule

- P0/P1 claims must route to canonical anchors.
- P3 bridge claims may be strong but remain mappings.
- P4 lab/proxy claims must state measurement boundary.
- P5 companion/public language must not carry proof load.

## Open-tension guard

Before presenting any of the following as closed, check `Core/SRT_OPEN_TENSIONS.md`:

- origin of selectability / P0-04;
- `D_eff -> d_stakes` gate;
- exact projection status of `Ψ_f`;
- minimal formalization of `T_dir`;
- healthy `L_2` support vs lethal `L_2` replacement;
- stable ISP entry and maintenance.

## AI guard

In AI contexts, always state architecture state before `d_AI`, AI burden, AI subjectivity, AI suffering, or AI consciousness claims:

- inference-only;
- training-time;
- persistent-memory / history-bearing;
- embodied non-transferable consequence return.

Current inference-only, non-history-bearing LLM deployments remain a strong P3 bridge case for `d_AI approx 0`, but this must not be generalized to all possible AI architectures.
