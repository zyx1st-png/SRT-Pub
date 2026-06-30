---
id: SRT-DIRECTION2-WEDGE1-SIM-RESULTS
type: pilot_result
tags: [Direction2, Reselectability, Reward, Robustness, ToySimulation, RLInterface, DynamicsHalf, Wedge]
status: pilot_v0
layer: bridge
epistemic_layer: research_program
claim_mode: pilot_result
canonical: false
ai_do_not_use_for_definition: true
created: 2026-07-01
provenance: v1/v2/v3 toy non-stationary landscape runs reported in SRT working conversation
candidate_promotion_target: none; may later feed benchmark design or Direction 2 empirical wedge notes
dependency: [SRT-DIRECTION2-MORAL-GENEALOGY-SEED, SRT-OBJECTHOOD-AS-RESELECTABILITY-META-STANDARD, SRT-OPEN-TENSIONS, SRT-D-VALUE-CANONICAL, SRT-T-DIR-CANONICAL]
---

# Wedge 1: Reward–Reselectability Dissociation in a Toy Non-Stationary Landscape

> **File status**: non-canonical pilot result.  
> This file records a narrow dynamics-half wedge: in a controlled toy landscape, current reward and future reselectability / robustness can diverge.  
> It does **not** validate SRT ontology, d-value, morality, externalization/X, or a general RL claim.

---

## 0. Narrow question

Can a system's current reward optimum differ from the parameter region that best preserves future robustness / reselectability after environmental change?

The toy question is intentionally narrow:

> Does current reward carry all the information needed to choose a robust future path, or can option-diversity / re-sampling capacity carry warning information that reward misses?

---

## 1. Toy model reading

The simulation uses a scalar guidance / lock-in parameter `g`.

Interpretation:

- `g` low: more exploration / option-diversity, weaker current exploitation;
- `g` moderate: strong performance while preserving some option-diversity;
- `g` high: strong current exploitation, low option-diversity, possible lock-in;
- `g` very high: over-guidance / over-locking region.

Recorded quantities:

| quantity | reading |
|---|---|
| `pre_rew` | current performance before environmental change |
| `pre_div` | option-diversity / re-sampling proxy before change |
| `post_rew` | performance after shift or drift |
| `recov_frac` | fraction of trials recovering after change; use carefully, especially at very low `g` |

Boundary:

> `pre_div` is **not** canonical d-value. It is a toy proxy for re-sampling / option-diversity.  
> `post_rew` and `recov_frac` are robustness readouts, not moral readouts.

---

## 2. v1 scan: sudden regime shift, coarse sweep

Initial scan, 60 trials per point, 2000-step sudden regime shift.

| g | pre_rew | pre_div | post_rew |
|---:|---:|---:|---:|
| 0.5 | 0.554 | 7.81 | 0.474 |
| 2 | 0.663 | 6.85 | 0.519 |
| 4 | 0.794 | 4.64 | 0.637 |
| 8 | 0.936 | 2.05 | 0.830 |
| 16 | 0.995 | 1.10 | 0.779 |
| 32 | 0.931 | 1.13 | 0.710 |
| 64 | 0.798 | 1.00 | 0.684 |

Reading:

- pre-shift reward peaks around `g=16`;
- by this point diversity has already collapsed close to 1;
- `g=8` has slightly lower pre-reward but much better post-shift reward;
- this first run suggested a reward-health / re-sampling-death dissociation.

Limit:

> v1 showed the shape but did not include recovery-rate detail and used a coarse sweep.

---

## 3. v2 scan + two-policy contrast: sudden shift, finer sweep

100 trials per point, added recovery fraction and two selection rules:

- **reward-only**: choose the `g` with the highest pre-shift reward;
- **diversity-aware**: choose a high pre-reward point subject to preserving a minimum diversity floor in this toy run.

| g | pre_rew | pre_div | post_rew | recov_frac |
|---:|---:|---:|---:|---:|
| 4 | 0.789 | 4.63 | 0.638 | 0.00* |
| 6 | 0.886 | 2.91 | 0.771 | 0.00* |
| 8 | 0.938 | 2.03 | 0.841 | 0.86 |
| 11 | 0.974 | 1.46 | 0.851 | 0.85 |
| 16 | 0.995 | 1.08 | 0.784 | 0.63 |
| 22 | 0.999 | 1.01 | 0.753 | 0.56 |
| 32 | 0.906 | 1.12 | 0.763 | 0.50 |
| 45 | 0.860 | 1.02 | 0.665 | 0.33 |
| 64 | 0.844 | 1.00 | 0.596 | 0.25 |

`*` Low-`g` recovery is confounded: these settings are too exploratory / under-exploiting, not locked-in. Recovery should not be interpreted symmetrically across the whole range.

Key contrast:

| selection rule | chosen g | pre_rew | pre_div | post_rew | recov_frac |
|---|---:|---:|---:|---:|---:|
| reward-only | 22 | 0.999 | 1.01 | 0.753 | 0.56 |
| diversity-aware | 8 | 0.938 | 2.03 | 0.841 | 0.86 |

Interpretation:

- The reward-only rule chooses `g=22`, the pre-reward optimum.
- That point is already in a low-diversity region (`pre_div ≈ 1`).
- `g=8` sacrifices about 6 percentage points of pre-shift reward but gains substantially in post-shift reward and recovery.
- The result supports the target-level claim that the current reward optimum can diverge from the reselectability / robustness optimum.

Important narrowing:

> This does **not** prove that every reward optimizer will dynamically learn its way into the fragile point. It shows that, in this toy landscape, the reward-optimal target lies in a fragile low-diversity region.

---

## 4. v3b stress test: gradual drift instead of sudden swap

A further pressure test replaced sudden shift with a 600-step gradual drift.

Reported anchor results:

| g | pre_div | post_rew under gradual drift | reading |
|---:|---:|---:|---|
| 8 | 2.05 | 0.822 | robust / moderate-guidance point |
| 22 | 1.01 | 0.764 | pre-reward peak / low-diversity fragile point |

Reading:

- The key structure reproduced under gradual drift.
- The reward-peak region (`g≈22`) remained low-diversity and less robust.
- The moderate-guidance region (`g≈8`) remained more robust.

Boundary:

> The conversation record did not include the full v3b table. This file records only the reported anchor contrast. Do not cite this as a full sweep unless the complete run log is later added.

---

## 5. Failed Experiment A: endogenous adaptive controller

Attempted question:

> Can a toy adaptive reward optimizer endogenously climb toward the reward peak and thereby collapse its own diversity?

Result:

> Not achieved.

What happened:

- The first adaptive controller stalled around `g≈6.7`.
- A revised hill-climber with longer evaluation window and margin still failed, stalling around `g≈4.7`.
- The controller did not reliably climb to the known reward peak around `g≈22`.

Interpretation:

> This is a tooling / optimizer failure, not evidence for or against the SRT thesis.

It cannot be used to show:

- that reward optimizers do endogenously collapse diversity;
- that reward optimizers do **not** endogenously collapse diversity;
- that the target-level dissociation is false.

Correct status:

> Endogenous adaptive collapse remains **unshown** in this toy wedge and should be left to a real meta-controller / bandit / benchmark engineering pass.

---

## 6. Positive evidential claim

The supported claim is narrow:

> In this toy non-stationary landscape, the parameter point that maximizes current reward can lie in a low-diversity region that becomes fragile under future environmental change; option-diversity / re-sampling capacity can therefore carry future robustness information not visible in current reward.

Even narrower:

> The wedge supports **target-level reward–reselectability dissociation**, not a full training-dynamics theorem.

This is enough to serve as a measurement wedge for the SRT claim:

> current performance is not a sufficient proxy for object-health or reselectability-health.

---

## 7. What this does not show

This file does **not** show:

- SRT is validated;
- SRT is superior to RL;
- RL lacks exploration, entropy, robustness, or distribution-shift tools;
- diversity is canonical d-value;
- re-sampling capacity is canonical T_dir;
- moral status is measurable from toy diversity;
- externalization/X is captured;
- all reward optimization is pathological;
- endogenous reward-driven diversity collapse has been demonstrated;
- more options are always better.

---

## 8. Honest residues

1. **Endogenous adaptive-controller demo not achieved**: the toy hill-climber failed to reach the reward peak; this remains engineering work.
2. **Low-`g` recovery confound**: too much exploration / under-exploitation can also look like failure; recovery should be read mainly within the moderate-to-high `g` region.
3. **RL already has nearby tools**: entropy regularization, robust RL, exploration, uncertainty, and distribution-shift methods are strong adjacent baselines.
4. **Single toy family**: this is not a benchmark, not a validation, and not a general theorem.
5. **Proxy status**: `pre_div` is a toy proxy for option-diversity / re-sampling capacity, not d-value.
6. **Dynamics-half only**: the moral half, cross-position externalization, and X remain untouched.
7. **Code not included**: this file records reported run results. Reproducible code should be added only if/when the actual simulation source is available or rebuilt.

---

## 9. Relation to Direction 2 and objecthood-as-reselectability

This wedge is useful because it gives a concrete dynamics-half illustration of a broader SRT advantage-line:

> current performance can be purchased by hidden loss of reselectability.

It supports the non-canonical objecthood meta-standard:

> performance is output; reselectability is the lifeline of objecthood.

But the wedge remains subordinate:

- it is a measurement entry, not a foundation;
- it cannot define objecthood;
- it cannot define moral status;
- it cannot solve closure-boundary;
- it cannot explain P0-04 / first selectability.

---

## 10. Suggested next steps

Stop scratch-sim escalation here unless a real benchmark pass is planned.

If continued, the next proper step is not another hand-rolled hill-climber, but a benchmark design:

1. multiple toy families;
2. sudden shift + gradual drift + new-option appearance + deceptive reward;
3. reward-only, entropy-regularized, robust RL, uncertainty-aware baselines;
4. explicit re-sampling / recovery / hysteresis metrics;
5. open code, fixed seeds, confidence intervals;
6. clear separation between target-level dissociation and endogenous learning dynamics.

Until then, this file should be cited only as:

> a pilot wedge showing reward–reselectability dissociation in a toy non-stationary landscape.
