---
id: SRT-EXP-CYCLE1-HISTORY-LOCATION-TOY-README
type: proposal
status: active
record_stage: cycle1_toy_coherence_result
date: 2026-09-05
layer: meta
epistemic_layer: bridge
claim_mode: experiment_design
canonical: false
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_REENTRY_CYCLE1_PASS3_2026-09-05.md
  - Operations/Proposals/SRT_AUTHOR_REENTRY_CYCLE1_HISTORY_LOCATION_MINIMAL_CAUSAL_MODEL_2026-09-05.md
  - Operations/Audits/SRT_AUTHOR_REENTRY_CYCLE1_INTERNAL_OWNER_REUSE_AUDIT_2026-09-05.md
tags: [AuthorReentry, Cycle1, Experiment, HistoryLocation, Multiplicity, Bearer, Reset]
---

# Cycle 1 history-location toy model

> **Status:** toy causal-coherence test only. It is not empirical support for SRT ontology, does not define Bearer identity, and does not earn Level 2 by itself.

## Question

Can one shared Selection history leave two independently manipulable causal residues:

```text
H_M  history carried in the surrounding field / 多
H_1  history carried in the candidate One
```

such that selective reset produces different temporal Selection signatures?

The live author motivation is:

```text
bearer 出现以前选择沉积在多

当历史痕迹沉积在一时，变为 Bearer
```

The experiment does **not** identify `H_1 = Bearer`. It only tests whether the two history-location channels are causally separable in a minimal model.

## Design

One agent is trained once. During training, choosing action `A` does two things:

1. it progressively changes the external field (`field_hazard`) — toy M-side sedimentation;
2. the consequences update the agent's internal Q values — toy One-side sedimentation.

After the same training history, the pair is forked into a 2 x 2 reset design:

| condition | field / `H_M` | agent / `H_1` |
|---|---|---|
| `00` | reset | reset |
| `10` | preserve | reset |
| `01` | reset | preserve |
| `11` | preserve | preserve |

The probe then permits ordinary learning but holds the retained field trace fixed, so the temporal response identifies which historical carrier is doing causal work.

## Reference run

Deterministic parameterization:

- training steps: 250;
- probe steps: 160;
- seeds: 1–30;
- Q-learning rate: 0.12;
- softmax temperature: 0.25;
- field increment per selected `A`: 0.012;
- base reward: `A = 1.25`, `B = 1.00`;
- field penalty: `1.25 * field_hazard`;
- Gaussian reward noise SD: 0.08.

Run:

```bash
python run_history_location_toy.py
```

The script writes `results_summary.json` when executed.

A locally verified reference run using the committed parameterization produced:

| condition | initial P(A) | early P(A) | late P(A) | mean reward |
|---|---:|---:|---:|---:|
| `00` | 0.500 | 0.599 | 0.775 | 1.182 |
| `10` M-side only | 0.500 | 0.242 | 0.046 | 0.957 |
| `01` One-side only | 0.093 | 0.146 | 0.732 | 1.142 |
| `11` both | 0.093 | 0.088 | 0.071 | 0.956 |

The key temporal crossing is:

```text
initial:
P(A)_10 - P(A)_01 = +0.407

late:
P(A)_10 - P(A)_01 = -0.686
```

with paired sign-flip `p < 0.0001` for both differences at the 20,000-resample resolution.

## Interpretation

### `01` — One-side history only

The agent begins the probe already history-conditioned because the adaptive state travels with the candidate One:

```text
initial P(A) ~ 0.09
```

But the field has been restored. As safe evidence accumulates, the agent gradually re-learns that `A` is advantageous:

```text
late P(A) ~ 0.73
```

### `10` — M-side history only

The fresh/reset agent initially has no internal historical bias:

```text
initial P(A) = 0.50
```

After re-contact with the historically altered field, it progressively learns to avoid `A`:

```text
late P(A) ~ 0.05
```

### Why this matters

The toy result is stronger than the phrase `history matters` in one limited sense:

> history location generates different **temporal response shapes** under selective reset.

It is weaker than an ontological result because both channels were explicitly engineered by the modeler.

## Internal owner subtraction

This experiment must be read together with:

- `Operations/Proposals/SRT_NEURAL_UNITY_D2_DISCRIMINATOR_DESIGN_2026-08-28.md`;
- `Philosophy/patches/SRT_Philosophy_PH_IND05_Occurrence_Trace_L2_Bearer_Experiencer_Discrimination_v0_1.md`;
- `AI/patches/SRT_AI_AICONSC01_Affective_Uncertainty_Stake_Gate_v0_1.md`;
- `Operations/Audits/SRT_AUTHOR_REENTRY_CYCLE1_INTERNAL_OWNER_REUSE_AUDIT_2026-09-05.md`.

Those older assets already paid for reset / replacement / same-unit writeback as an operational discriminator. Cycle 1 therefore cannot claim this 2 x 2 architecture as a new scientific invention.

The current Cycle-1 increment is instead the proposed **genetic reading**:

```text
Selection sedimentation in 多
-> history attribution shifts into 一
-> Bearer transition
```

The toy only shows that an M-side / One-side causal split is coherent and intervention-visible.

## Negative controls / limitations

1. The agent's Q vector is the complete toy One-side carrier. Copying it to a fresh agent reproduces the same initial policy by construction. Therefore this model does **not** solve historical or numerical identity.
2. `field_hazard` is an engineered field variable, not a model of metaphysical `多`.
3. There is no cognition or phenomenality claim here.
4. A richer RL / Bayesian state model can represent both carriers. The toy does not show that SRT is non-Markovian.
5. The experiment tests **causal localization of historical efficacy**, not whether the author's ontology is true.

## Pass / fail use

The toy pays only one burden:

```text
Can the proposed distinction be made causally coherent without contradiction?
```

For this model, the answer is **yes**.

It does not pay:

```text
Does nature instantiate the distinction?
Is the distinction scientifically unique to SRT?
Does One-side history suffice for Bearer identity?
```

Those remain open.
