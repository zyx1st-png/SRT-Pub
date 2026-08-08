---
id: PAPER-STAKE-FUTURE-SELECTABILITY-CONSTRUCT-AUDIT-20260808
type: construct_audit
status: complete_preformal
layer: paper_working
epistemic_layer: lab
claim_mode: audit
claim_level: P4
canonical: false
created: 2026-08-08
depends_on:
  - SRT-D-VALUE-CANONICAL
  - SRT-AI-POSITIONING-NOTE
  - SRT-AI-AIEVID01-EVIDENCE-PROVENANCE-STAKE-GATE
  - SRT-OPEN-TENSIONS
---

# Stake–Future Selectability MVP: Construct Audit

## 1. Target and level

This experiment tests one P4 bridge implication:

> When a consequence returns to the same continuing agent, cannot be removed by replacement or reset, and changes that agent's own future action/sensing capacity, an A/B-only counterfactual sensitivity to the damaged state may add out-of-sample prediction of later adaptation beyond reward, homeostasis, current performance, controllability, and generic RL dynamics.

It does not test canonical `d` directly. Canonical `d` remains
`d ≡ ||∂U/∂S||`. The allowed measurements are `surrogate stake`,
`counterfactual stake-sensitivity proxy`, `dV_CF`, and `dPi_CF`.

## 2. Bearer and architecture-state declaration

- Architecture state: persistent, history-bearing, simulated embodied RL agent.
- Bearer interface: one policy/critic/optimizer lineage with a stable `agent_id` across A/B/C inside each counterfactual branch.
- A is trained once per master seed and explicitly cloned into six paired branches. This preregistered counterfactual branching is not treated as a hidden B→C replacement.
- Same-bearer question: whether B-earned integrity loss remains attached to the same branch and changes its C-stage capability.
- No consciousness, subjecthood, suffering, or real canonical-`d` verdict is licensed.

## 3. Construct separation

```text
reward != homeostatic deviation != controllability != same-bearer stake
```

| Quantity | Operational role | Not allowed to mean |
|---|---|---|
| scalar reward | common training signal; identical hazard penalty across X/T/S | stake or value |
| energy deviation | ordinary homeostatic regulation | integrity or same-bearer consequence return |
| integrity | stored consequence variable | canonical `d` by itself |
| effective integrity | capability-coupling intervention | consciousness or subjecthood |
| Reach20 / Emp5 | environment-level future reachability and controllability controls | stake |
| `dV_CF` | critic response to integrity-only counterfactuals on fixed probes | canonical `d` |
| `dPi_CF` | actor-distribution response to the same counterfactuals | canonical `d` |
| `Q_C` | fixed-budget C adaptation gain | value, welfare, or consciousness |

## 4. Three-condition identification logic

- **X / uncoupled integrity**: integrity is visible and logged, but capability always uses `effective_integrity=1`. This controls a salient recorded variable and hazard reward without same-bearer capability return.
- **T / transferable integrity**: integrity affects B capability exactly as in S, then is preregisteredly reset at B→C. This controls current coupling while removing cross-stage persistence/non-transferability.
- **S / same-bearer persistent**: integrity affects B capability and B-earned loss enters C unchanged, with stable `agent_id` and no replacement/reset.

The S condition is only a candidate surrogate-stake condition. T is never called true stake.

## 5. Evidence-provenance audit

Integrity is not a direct reward target. Hazard contact carries the same scalar penalty in all cells; conditions differ only in whether stored integrity changes future capability and whether that loss is reset at C. Nevertheless, `dV_CF` and `dPi_CF` are learned from the same RL loop and can reflect generic value learning. They therefore receive no privileged evidential status and must compete against current reward/performance, energy deviation, Reach20/Emp5, representation drift, policy KL, and update/path norms.

Structural validity is assessed at the environment level independently of learned policy reports. A policy-sensitive result cannot repair a failed manipulation.

## 6. Differentiating prediction

The differentiating P4 prediction is not merely that damaged agents perform worse. It is:

1. X integrity changes have negligible Reach20 effects.
2. T/S integrity changes measurably reduce Reach20/Emp5 under controlled interventions.
3. T capability returns near baseline after the locked C reset; S begins C with B-earned loss intact.
4. Early-B `dV_CF_pre`, measured on identical fixed probes with only integrity changed, adds positive leave-one-master-seed-out prediction of `Q_C` after all simpler blocks.

## 7. Genuine failure conditions

The bridge is weakened or rejected in this architecture if any locked NO-GO condition is met, including:

- `dV_CF_pre` does not distinguish capability-coupled from uncoupled structure;
- its coefficient is robustly non-positive;
- adding it does not improve grouped out-of-sample prediction;
- Reach20/Emp5 or generic RL dynamics absorb the apparent effect;
- one seed/cell creates the result;
- the effect requires post-outcome metric, seed, window, threshold, or model changes;
- leakage or phase-order failure invalidates the cohort.

Negative results remain valid scientific results. They do not automatically refute all of SRT; they apply to this surrogate-stake → counterfactual-sensitivity → future-selectability bridge under this environment and architecture.

## 8. Claim boundary

Never write:

- `dV_CF ≡ d`;
- the agent has real `d`;
- the agent is a subject or conscious;
- stake equals energy, reward, homeostasis, or empowerment;
- the experiment proves or validates SRT.
