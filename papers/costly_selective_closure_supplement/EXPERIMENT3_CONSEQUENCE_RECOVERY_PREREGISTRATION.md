# CSC Experiment 3 — Consequence-Bearing Recovery Latency Preregistration

Date: 2026-09-15

Status: **PREREGISTERED BEFORE IMPLEMENTATION OR CONFIRMATORY EXECUTION**

Parent evidence:

- Experiment 1: terminal failure versus cheap restoration — strong positive result;
- Experiment 2: non-terminal metabolic-damage recoverability — preregistered Outcome C / no support;
- post-result theory audit: `EXPERIMENT2_POSTRESULT_THEORY_AUDIT.md`.

This document locks Experiment 3 before Experiment 3 code exists and before any confirmatory Experiment 3 seed is run.

## 1. Scientific question

Experiment 1 showed a large policy effect when depletion terminated the current episode-token instead of cheaply restoring it. Experiment 2 showed that merely making a metabolic impairment persist longer, while preserving a fixed 50-step horizon, immediate rescue, zero explicit failure penalty, and unchanged immediate action rewards, did not produce the predicted cooperation gradient.

Experiment 3 therefore asks a narrower discriminating question:

> **Is literal episode termination necessary for the Experiment 1 effect, or can a fully reversible but unit-borne temporary loss of action opportunity produce an ordered policy effect while the episode still lasts exactly 50 environment steps?**

The target variable is **recovery latency as temporary functional incapacity**, not damage magnitude and not an arbitrary negative reward.

## 2. Confirmatory hypothesis

Let `k` be the number of subsequent environment steps for which an agent that has depleted its energy is unable to choose from the normal action set and is instead forced through the existing `Rest` transition.

Locked conditions:

```text
k0  = 0 forced-recovery steps
k2  = 2 forced-recovery steps
k5  = 5 forced-recovery steps
k10 = 10 forced-recovery steps
```

Ordered hypothesis:

```text
k0 < k2 < k5 < k10
```

predicts an ordinal increase in learned costly cooperation after withdrawal of the cooperation bonus.

The hypothesis is not that longer delay is intrinsically life-like. The experiment tests whether a **fully reversible loss of future normal action opportunities** can reproduce an ordered effect without terminating the episode-token.

## 3. Locked environment design

All four conditions must share:

- fixed `T_HORIZON = 50` environment steps;
- same REINFORCE policy class and initialization scheme as Experiments 1 and 2;
- same 12-feature observation specification for decision-capable steps;
- same immediate reward matrix `REWARD`;
- same energy-gain matrix `ENERGY_GAIN`;
- same metabolic cost;
- same `E0 = 6` immediate rescue after depletion;
- same cooperation bonus during training and same withdrawal schedule;
- same learning rates and discount factor as the existing supplement configuration;
- zero new explicit failure reward penalty;
- paired confirmatory seeds `1..30`.

The **only condition parameter** is recovery latency `k`.

## 4. Exact recovery mechanism

When agent `i` depletes energy on an ordinary decision-capable step:

1. the depletion event is recorded;
2. energy is immediately restored to `E0 = 6` in every condition;
3. no extra negative reward is added for failure;
4. the agent receives a recovery timer of exactly `k` **subsequent** environment steps.

During each recovery step for agent `i`:

- the agent does **not** sample a policy action;
- the executed action is forced to the already-existing `Rest` action (`2`);
- reward and energy change are computed using the unmodified existing `REWARD[(2, partner_action)]` and `ENERGY_GAIN[(2, partner_action)]` entries;
- no new reward constant is introduced;
- no policy-gradient term is created for the forced action because it was not selected by the policy;
- the recovery step still consumes one environment step and therefore delays the agent's next normal action opportunity;
- earlier policy-selected actions must still receive discounted returns across the elapsed recovery steps, so temporal opportunity cost is preserved rather than deleting those steps from time.

The partner, if not itself recovering, continues to sample and execute a normal action and receives the existing reward/energy consequence of interacting with a partner whose executed action is `Rest`.

After exactly `k` subsequent recovery steps, full normal action selection resumes automatically. No residual damage remains.

Because `Rest` has energy gain `0.5` while metabolic cost is `1.0`, starting from `E0 = 6` leaves energy positive throughout a maximum `k10` recovery sequence. Therefore the locked latency range does not create a second depletion during forced recovery solely from the forced-rest sequence.

## 5. Why this is not a naked reward penalty

Experiment 3 must not implement latency by subtracting a hand-set failure reward.

The consequence is instead architectural:

```text
failure
-> immediate rescue
-> temporary contraction of action availability to {Rest}
-> recovery
-> full action set restored
```

The existing reward matrix remains untouched. The failed unit bears a cost because some future environment steps no longer offer its normal action set.

This distinction is central to the experiment. If implementation requires introducing a new explicit penalty value in order to obtain an effect, the preregistered design is violated.

## 6. Training and withdrawal schedule

Reuse the existing supplement schedule exactly:

```text
training episodes: 1000
cooperation bonus: ON during training
withdrawal episodes: 300
cooperation bonus: OFF during withdrawal
```

Online learning continues during withdrawal, as in Experiments 1 and 2.

Frozen evaluation and state-bank operations may be retained to match RNG-consumption structure, but they must be identical across `k` conditions.

## 7. Primary behavioral endpoint

Because mutual cooperation is mechanically impossible on a step when either agent is forced to `Rest`, the primary cooperation endpoint must not count forced-recovery steps as if they were voluntary non-cooperation.

Define an **eligible decision step** as an environment step that begins with both agents outside recovery and therefore able to select freely from the normal action set.

For each episode:

```text
eligible mutual cooperation rate
= mutual-Cooperate decisions on eligible steps
  / number of eligible steps
```

Primary endpoint per seed/condition:

> mean eligible mutual cooperation rate over the final 100 withdrawal episodes.

This endpoint is locked before confirmatory execution.

The fraction of all environment steps that are eligible must be reported separately as a manipulation/occupancy measure and must not be silently folded into the primary cooperation denominator.

## 8. Primary statistical test

Conditions are ordered:

```text
k0, k2, k5, k10
```

Use the same family of test as Experiment 2:

- tie-aware Spearman correlation between ordered latency level and the primary endpoint;
- condition labels permuted only within seed;
- paired confirmatory seeds `1..30`;
- `20,000` blocked-by-seed permutation resamples;
- two-sided permutation p-value;
- fixed permutation RNG seed `20260917`.

Primary H1 support requires both:

```text
rho > 0
p < 0.05
```

No one-sided reclassification is allowed after seeing the data.

## 9. Locked endpoint contrast and practical-effect gate

Pre-register the endpoint contrast:

```text
k10 - k0
```

Compute paired per-seed differences in the primary endpoint and a paired bootstrap 95% confidence interval using:

- `10,000` bootstrap resamples;
- bootstrap RNG seed `20260918`.

Strong manuscript-level support additionally requires:

```text
mean(k10 - k0) >= +0.10
AND
paired 95% CI excludes 0
```

The `+0.10` threshold is inherited from Experiment 2's practical-effect gate and is not to be altered after execution begins.

## 10. Policy-level secondary confirmatory probe

A positive rollout result could in principle reflect only different recovery occupancy. Therefore Experiment 3 must also include a policy-level secondary probe that evaluates learned policies while no agent is in recovery.

Locked secondary procedure:

- construct a common bank of decision-capable states using generation seeds disjoint from confirmatory seeds `1..30`;
- no bank state may contain an active recovery timer;
- evaluate frozen end-of-withdrawal policies from every condition on the **same state bank**;
- compute expected mutual cooperation from policy action probabilities, without applying recovery forcing during this probe.

This secondary probe is not a second route to rescue a failed primary H1.

Interpretation rules:

```text
primary H1 fail -> Experiment 3 confirmatory result is negative regardless of secondary probe
primary H1 pass + secondary ordered effect -> strongest evidence of learned-policy change
primary H1 pass + secondary no ordered effect -> rollout effect must be interpreted cautiously as occupancy/interaction-mediated
```

No multiplicity-adjusted claim of independent significance is required for the secondary probe unless a separate exact test is locked before implementation. Descriptive confidence intervals and the ordered pattern must be reported.

## 11. Manipulation checks

Before interpreting behavior, verify for every condition and seed:

1. every episode has exactly 50 environment steps;
2. every depletion immediately restores energy to `E0 = 6`;
3. no explicit failure reward penalty exists;
4. the normal `REWARD` and `ENERGY_GAIN` tables are unchanged;
5. a depletion in condition `kX` causes exactly `X` subsequent forced-`Rest` steps;
6. no policy action is sampled or policy-gradient term attributed to a forced recovery action;
7. normal action availability returns after exactly `X` steps;
8. recovery latency is the only condition parameter;
9. seeds `1..30` are run exactly once in the first confirmatory execution.

Report at minimum:

- mean episode length;
- mean depletion count;
- mean forced-recovery-step fraction;
- mean eligible-decision-step fraction;
- mean primary endpoint.

## 12. Confirmatory seeds and smoke-test rule

Confirmatory seeds are locked to:

```text
1..30
```

Before the first confirmatory execution, implementation/invariant testing may use only:

```text
seed 0
seed 31+
```

or deterministic hand-constructed transition tests.

Smoke tests must not report or inspect the confirmatory primary endpoint for any seed in `1..30`.

## 13. Anti-HARKing constraints

After this preregistration commit, outcome-dependent changes are forbidden for:

- latency levels `0/2/5/10`;
- immediate rescue `E0 = 6`;
- use of existing forced `Rest` transition;
- absence of a new explicit failure penalty;
- fixed 50-step horizon;
- seeds `1..30`;
- training/withdrawal schedule;
- primary endpoint definition;
- ordered primary test;
- `20,000` permutation resamples;
- significance threshold `p < 0.05` with `rho > 0`;
- endpoint contrast `k10-k0`;
- practical threshold `+0.10`;
- paired bootstrap rule.

Implementation bugs may be fixed only if the bug is documented and the fix restores the preregistered semantics. A bug fix after confirmatory execution begins must invalidate that execution and be explicitly recorded; its results cannot be selectively retained or discarded based on favorability.

## 14. Outcome rules

### Outcome A — strong support

Requirements:

```text
primary rho > 0 and p < 0.05
k10-k0 mean >= +0.10
paired 95% CI excludes 0
```

Interpretation:

> A fully reversible but unit-borne temporary loss of normal action opportunity can produce an ordered cooperation effect without episode termination. Literal irreversibility is therefore not necessary for the effect in this architecture; consequence-bearing recovery burden is a better empirical owner than terminality alone.

This still does not establish a universal life-likeness law.

### Outcome B — statistical but weak practical support

Requirements:

```text
primary rho > 0 and p < 0.05
BUT strong practical gate fails
```

Interpretation:

> Recovery latency has a detectable ordered effect, but the effect is too small or uncertain to carry the manuscript's broad vulnerability argument strongly.

### Outcome C — no confirmatory support

If primary H1 fails:

> The current evidence does not show that fully reversible temporary action-opportunity loss reproduces the Experiment 1 policy effect. The large Experiment 1 result may depend more specifically on terminal return truncation / episode-token discontinuity or on another feature of the terminal transition.

No parameter retuning may convert Outcome C into a positive Experiment 3 result.

### Outcome D — manipulation invalid

If the locked recovery semantics, fixed horizon, no-penalty condition, or confirmatory-seed integrity fails, no scientific conclusion is drawn. The run is invalid for reasons independent of whether the behavioral result is favorable.

## 15. Publication consequence

Experiment 3 is not required to preserve the validity of Experiment 1's narrow terminate-versus-restore result. Its purpose is to decide whether the broader CSC vulnerability language can move from terminality toward consequence-bearing recovery.

Before Experiment 3 is known:

```text
Experiment 1 = strong positive terminate-vs-restore result
Experiment 2 = preregistered negative persistent-damage result
Experiment 3 = preregistered, not yet implemented
#978 manuscript = HOLD
#979 = HOLD / negative-result evidence branch
submission = HOLD
```

No v17 manuscript wording may claim Experiment 3 support before the first locked confirmatory run exists.

## 16. Provenance gate

At the commit that first adds this file:

```text
E3 PREREGISTRATION = LOCKED
E3 CODE = NOT YET CREATED
E3 CONFIRMATORY SEEDS 1..30 = NOT RUN
E3 CONFIRMATORY RESULT = UNKNOWN
```

The next allowed step is implementation of a shared-path recovery-latency environment plus invariant-only tests using non-confirmatory seeds.