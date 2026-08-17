---
id: SRT-OPS-AUDIT-P24-3-FLOOR-CHALLENGE-R2-DUEL-20260817
type: experiment_admission_audit
status: active
record_stage: pre_execution_no_go_for_d2
layer: meta
epistemic_layer: p4
claim_mode: audit
claim_level: P4_experiment_admission
canonical: false
date: 2026-08-17
dependency:
  - SRT-OPS-AUDIT-POST-RCA-SELECTION-D2-RANKING-20260817
  - SRT-CORE-24-DISCRIMINATING-PREDICTIONS
  - SRT-EXP-ANCHORING-CHAIN-AUDIT-2026-07-17
tags: [P24-3, L2, FloorChallenge, R2, RivalModel, D2, NoGo, ExperimentAdmission]
---

# P24-3 Floor-Challenge / Frozen-R2 Duel Spec

> **Admission verdict:** `NO-GO FOR D2 EXECUTION`.
>
> The existing P24-3 floor signature is measurable, but a bounded ordinary memory / hysteresis learner can prospectively predict the same qualitative and quantitative outcome family. Running the experiment now could calibrate the signature but could not discriminate SRT from the frozen R2 family.

## 1. Target

P24-3 currently expects a mature scaffold to show:

```text
compatible-path cost down
+ global constraint / switching cost up
+ hysteresis under perturbation
```

The 2026-08-17 background-floor audit adds a useful challenge sequence:

```text
mature background scaffold
-> targeted mismatch
-> friction / regulation demand rises
-> old-path persistence or failure
-> revision / bypass / replacement
-> possible new backgrounding
```

This is the target to be tested for **differential** value, not merely internal coherence.

## 2. Existing constructive model already exposes the absorption route

The frozen `anchoring_tiny_mdp_confirmatory` model carries a history-dependent memory vector `m` into a future task. The future policy is reset, while `m` exerts a bounded retention pull on the evolving policy.

That architecture already produces:

- aligned-history advantage;
- blocked-path stickiness / timeout;
- novel-goal cost;
- path-dependent future reachability.

The independent audit correctly classifies this as a designed-model feasibility result, not evidence that a natural system instantiates an SRT-specific mechanism.

Crucially, nothing in the future update requires a Selection primitive. At the implementation level it is an ordinary stateful adaptive controller with a retained memory state.

## 3. Frozen R2 family

Define the empirical rival before any new data as:

> **R2-HMR — bounded history-memory regularized learner.**

Allowed state:

```text
Q_t     current action values / policy state
m_t     retained history-conditioned memory vector
c_t     declared context / challenge state
```

Allowed update family:

```text
Q_(t+1) = U(Q_t, observation_t, action_t, outcome_t; beta)
m_(t+1) = (1-lambda)m_t + eta * H(history_t)
policy_t = softmax(Q_t / tau)
Q_t <- Q_t + kappa * (m_t - Q_t)
```

where:

- `H` is frozen before holdout;
- memory dimension is fixed;
- decay / learning / retention parameters are calibrated only on training data;
- challenge context may alter available actions but may not add new hidden state after holdout starts;
- no post-result architecture expansion is allowed.

This is an ordinary adaptive / hysteretic model family. It does not use SRT vocabulary or primitive Selection.

## 4. Prospective R2 predictions

R2-HMR predicts the same P24-3 family when `m_t` has been consolidated around a repeatedly successful path.

### Compatible condition

```text
history-consistent action
-> regularization aligns with current reward / transition structure
-> faster execution / lower switching pressure
```

### Blocked-floor condition

```text
old path becomes unavailable / ineffective
-> retention term still pulls policy toward old path
-> perseveration / timeout / switching cost rises
-> repeated new evidence gradually updates Q and/or m
-> adaptation occurs with hysteresis
```

### Novel condition

```text
novel target conflicts with retained m
-> slower acquisition / lower initial accessibility
-> eventual restabilization if new evidence is sustained
```

These predictions are not post-hoc. They follow directly from the frozen memory-regularization structure.

## 5. Prospective SRT shell

At the current level, SRT predicts:

```text
compatible floor:
local friction down

challenge:
old scaffold continues constraining current paths
-> switching / repair friction up
-> hysteresis

successful revision:
new path becomes historically effective
-> later compatible friction down
```

This is scientifically coherent but does not yet specify an observable that R2-HMR prospectively excludes.

Therefore:

```text
O_SRT ~= O_R2
```

for the currently named P24-3 observables.

## 6. Why stronger controls do not rescue D2

### Same current policy, different history

Matching visible `Q` while varying `m` can produce different futures, but R2-HMR explicitly contains `m`. This shows hidden/history state matters; it does not show SRT-specific Selection.

### Memory ablation

Removing `m` should reduce hysteresis. R2 predicts this directly.

### Memory swap

Transferring `m` should transfer path bias if the future reads `m`. Again R2 predicts this directly; in the existing tiny-MDP implementation some swap/null checks are mechanical pipeline validation.

### Cross-position friction distribution

Different positions with different histories can experience the same scaffold differently. R2 can condition `m` / context on those histories and predict the distribution.

### Re-foregrounding

A mismatch-induced rise in regulation demand is also expected under error-driven adaptive control.

None yields D2 by itself.

## 7. What would be required to reopen execution

The floor-challenge experiment becomes D2-admissible only if a pre-data theory step supplies one observable `O*` such that:

```text
SRT -> O* in direction / bound A
R2-HMR -> O* in incompatible direction / bound B
```

with all of the following frozen:

1. state variables;
2. memory dimension / horizon;
3. update family;
4. calibration set;
5. challenge intervention;
6. outcome metric;
7. model-complexity / revision budget;
8. SRT failure rule.

A merely larger SRT effect size is insufficient unless R2 has a preregistered upper bound that SRT independently predicts should be exceeded.

## 8. Legitimate non-D2 use

P24-3 remains worth testing for **construct calibration**.

A calibration study could establish whether the proposed L2 operational signature is internally useful across domains:

```text
cost reduction
+ constraint
+ hysteresis
+ challenge-induced re-foregrounding
```

But the report must say:

> “This calibrates an SRT-compatible L2 signature; it does not discriminate SRT from ordinary stateful adaptive models.”

No residue label for primitive Selection may follow.

## 9. Implication for existing anchoring chain

The old anchoring computational chain remains useful as:

- reproducibility proof;
- designed-model feasibility;
- directional reachable-set demonstration;
- test infrastructure.

It should **not** be upgraded into P24-3 D2 evidence merely because its behavior resembles backgrounding / stickiness / future constraint.

The existing audit's caution is therefore strengthened, not reversed.

## 10. Decision

```text
P24-3 operational coherence: YES
P24-3 calibration value: YES
P24-3 current D2 contrast vs bounded R2-HMR: NO
new empirical execution for SRT superiority: NO-GO
```

No new code, parameter sweep or holdout is justified until a prospective incompatible prediction is derived.

**Next pressure:** test whether P24-1 or P24-4 contains any prospective observable not already admitted by an equivalently bounded R2 family. If neither does, Core 24's current “discriminating predictions” title/status requires an explicit claim-level audit rather than more experiments.