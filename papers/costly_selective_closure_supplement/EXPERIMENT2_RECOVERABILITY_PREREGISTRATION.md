# CSC Experiment 2 — Recoverability Gradient Preregistration

Date locked: 2026-09-15

Status: **LOCKED BEFORE CONFIRMATORY RESULT GENERATION**

Parent publication candidate: Draft PR #978 (`publication/csc-artificial-life-v17-20260915`)

Experiment branch: `experiment/csc-v17-recoverability-e2-20260915`

## 1. Purpose

The current CSC v17 experiment establishes a large policy difference between episode termination and cheap full-energy restoration. That result is valid but does not separate **persistent consequence** from **return-stream truncation**: in the terminal condition, depletion ends the episode and therefore changes the learner's return horizon.

Experiment 2 tests a narrower causal question:

> **When episode length, immediate rescue, reward function, observation specification, policy architecture, training schedule, seeds, and explicit failure penalty are held fixed, does the recoverability of a non-terminal damage state change the learned policy?**

This experiment is designed specifically to test CSC's vulnerability/recoverability interpretation without using episode termination as the manipulation.

## 2. Declared CSC profile context

- **organizational unit:** episode-token interacting through one controller instance;
- **boundary:** agent policy plus its in-environment energy state; external trainer and experiment runner remain outside the unit;
- **timescale:** one 50-step episode for damage persistence, with controller learning evaluated across the full 1000 + 300 episode schedule;
- **recovery regime:** the duration for which a depletion-triggered metabolic-efficiency loss remains in force after identical immediate rescue.

The experiment does not claim organism-level irreversibility. `tau = infinity` means **not recoverable within the current episode-token**, not metaphysically or physically irreversible across all levels.

## 3. Locked environment and learning architecture

Unless stated below, Experiment 2 inherits the current v17 environment and learner exactly:

- two independent REINFORCE policies;
- 12 observation features;
- one hidden layer with 16 tanh units;
- 3 actions: cooperate, solo, rest;
- learning rate `0.04` in training and withdrawal;
- discount `gamma = 0.97`;
- horizon `T = 50`;
- initial energy `E0 = 6`;
- metabolic cost `1.0` per step;
- existing reward matrix and energy-gain matrix;
- 1000 training episodes with cooperation bonus active;
- 300 online-adaptation episodes with cooperation bonus withdrawn;
- primary summary window = final 100 withdrawal episodes;
- paired seeds `1..30` in every condition.

No PPO/actor-critic replication is part of this preregistered experiment.

## 4. The single manipulated variable: damage recoverability

All Experiment 2 conditions are **non-terminal**. Energy depletion never ends the episode.

When an agent reaches `energy <= 0`, every condition receives the same immediate transition:

1. record one depletion/failure event;
2. apply **no explicit failure reward penalty** (`failure_penalty = 0.0`);
3. restore current energy to the same value `E0 = 6`;
4. activate the same metabolic-efficiency damage magnitude: future energy gains are multiplied by `q = 0.75` while damage is active.

Only the **duration of that damage** differs:

| condition | locked recovery duration after depletion | interpretation |
|---|---:|---|
| `tau0` | 0 subsequent steps | immediate recovery / cheap restore |
| `tau5` | 5 subsequent steps | short-lived damage |
| `tau15` | 15 subsequent steps | longer-lived damage |
| `tau_inf` | remainder of the current episode | non-recoverable within the episode-token |

For finite `tau`, a new depletion event while damage is active resets the countdown to the full condition-specific duration. For `tau_inf`, damage remains active to the episode horizon.

At the next episode reset, damage is cleared in all conditions. Therefore the manipulation concerns **within-token consequence persistence** while controller-lineage learning continues across episodes.

### Why `q = 0.75` is locked

The damage magnitude is fixed before confirmatory runs and will not be tuned after observing outcomes. With the existing energy matrix, `q = 0.75` preserves mutual cooperation as energetically viable (`2.0 * 0.75 - 1.0 = +0.5` net per step) while making less cooperative energy gains substantially less viable. The manipulation therefore degrades energetic efficiency without directly removing or rewarding any action.

## 5. Matching constraints

Across `tau0`, `tau5`, `tau15`, and `tau_inf`, the following must remain identical:

- episode horizon (`50` steps in every episode);
- immediate rescue energy (`6`);
- explicit failure penalty (`0.0`);
- reward matrix;
- undamaged energy-gain matrix;
- damage magnitude (`q = 0.75`);
- observation feature specification;
- network architecture and initialization procedure;
- optimizer/update rule;
- training and withdrawal schedule;
- random seeds;
- cooperation bonus schedule.

No condition-specific mortality cue, danger penalty, reward shaping, action deletion, or early termination is allowed.

The implementation must use one shared code path parameterized by recovery duration; four separately hand-edited environments are not allowed.

## 6. Primary outcome

Primary outcome:

`post_coop` = mean mutual-cooperation rate over the final 100 bonus-withdrawal episodes.

This is the same primary behavioral outcome used in Experiment 1.

## 7. Primary hypothesis and confirmatory test

### H1 — recoverability gradient

As recovery becomes less immediate, post-withdrawal mutual cooperation will tend to increase:

`tau0 < tau5 < tau15 < tau_inf`

in the ordinal sense of recovery duration.

Primary statistic:

- tie-aware Spearman rank correlation between ordered recovery level (`0,1,2,3`) and `post_coop`;
- repeated-measures structure preserved by a **blocked-by-seed permutation test**, permuting the four condition labels only within each seed;
- two-sided permutation `p` with 20,000 resamples and a fixed permutation seed declared in code before the confirmatory run.

### Confirmatory decision rule

The preregistered H1 test is counted as **supported** only if both are true:

1. Spearman `rho > 0`; and
2. blocked-by-seed permutation `p < 0.05`.

If either condition fails, H1 is reported as **not supported**. No alternative condition ordering will replace the preregistered ordering after results are seen.

## 8. Prespecified effect-size checks

These are secondary and do not replace the primary test.

1. Endpoint paired effect: `mean(post_coop_tau_inf - post_coop_tau0)`.
2. Paired bootstrap 95% CI for the endpoint difference, resampling seeds as paired units with 10,000 resamples.
3. Descriptive practical-magnitude flag: absolute endpoint mean difference `>= 0.10`.

A manuscript-level claim that recoverability has a **substantively strong** effect requires:

- the primary H1 rule to pass; and
- endpoint difference `>= 0.10` with the paired 95% CI excluding `0`.

If H1 passes but this stronger effect-size criterion does not, the result will be described as statistically directional but modest rather than as strong support.

## 9. Distribution / attractor reporting

Because Experiment 1 shows seed-level heterogeneity, Experiment 2 will not rely on means alone.

For each condition, report:

- mean and 95% bootstrap CI;
- median and IQR;
- all 30 per-seed points;
- fraction of seeds with `post_coop > 0.50` as a **descriptive majority-cooperation threshold only**.

The `0.50` threshold is not a new significance test and will not replace the continuous primary outcome.

## 10. Mechanism diagnostics

The following are prespecified descriptive diagnostics:

- mean depletion events per episode in the final 100 withdrawal episodes;
- fraction of withdrawal steps spent in the damaged state;
- mean episode length, which must equal `50.0` in all conditions by construction;
- baseline cooperation over the final 100 training episodes;
- retention ratio using the existing paper convention, reported descriptively only.

These diagnostics are not alternative primary endpoints.

## 11. Implementation validation before confirmatory run

Before running seeds `1..30`, code may be exercised only for invariant/smoke checks. Such checks must not be used to tune `q`, recovery durations, reward values, learning rates, or the success criterion.

Required assertions:

1. every episode in every recovery condition has exactly 50 steps;
2. no Experiment 2 condition calls a terminal transition on depletion;
3. every depletion sets current energy to exactly `E0 = 6`;
4. explicit failure reward penalty is exactly `0.0` in every condition;
5. damage multiplier is exactly `0.75` while active and `1.0` otherwise;
6. `tau0`, `tau5`, `tau15`, and `tau_inf` differ only in damage recovery duration;
7. finite-duration repeat depletion refreshes the timer exactly as specified;
8. no condition-specific observation cue or reward term is introduced;
9. paired seeds `1..30` are used only after these invariants pass.

Debug/smoke runs must use seeds outside `1..30` and their behavioral outcomes are not part of the confirmatory evidence.

## 12. Frozen choices / no post-result tuning

After this preregistration commit, the following may not be changed in response to outcome magnitude or significance:

- `q = 0.75`;
- recovery levels `0, 5, 15, infinity`;
- `E0 = 6` immediate rescue;
- zero explicit failure penalty;
- 30 paired confirmatory seeds;
- primary `post_coop` endpoint;
- ordinal condition ordering;
- blocked-by-seed Spearman test;
- `p < 0.05` confirmatory threshold;
- endpoint practical-magnitude threshold `0.10`.

Changes are permitted only to fix a documented implementation error that violates this locked design. Any such correction must be committed and explained before rerunning the full confirmatory seed set.

## 13. Interpretation matrix

### Outcome A — strong support

Primary H1 passes and endpoint effect is at least `0.10` with paired 95% CI excluding zero.

Interpretation allowed:

> In this testbed, recoverability itself changes learned policy even when episode termination, immediate rescue, and explicit failure penalties are held fixed.

This would materially strengthen CSC-V beyond the current terminate-versus-restore demonstration.

### Outcome B — weak / limited support

Primary H1 passes but the stronger effect-size criterion fails.

Interpretation:

> Recoverability shows a detectable directional effect, but the effect is not strong enough to support a broad architectural claim without further work.

### Outcome C — no support

Primary H1 fails.

Interpretation:

> The current evidence does not show that non-terminal recoverability independently organizes cooperation in this architecture. The strong Experiment 1 effect may depend substantially on return truncation and/or the original terminal-versus-restore transition.

Outcome C must be retained and reported internally; parameters must not be retuned until a positive result appears.

## 14. Relationship to v17 submission decision

Experiment 2 is a publication-strengthening gate, not a retroactive requirement for the validity of Experiment 1.

Before Experiment 2 results are known:

```text
EXPERIMENT 1 VALIDITY = UNCHANGED
EXPERIMENT 2 DESIGN = LOCKED
V17 SUBMISSION = HOLD
#978 MERGE = HOLD
```

The submission decision will be revisited only after the preregistered Experiment 2 result and its distribution-level diagnostics are available.
