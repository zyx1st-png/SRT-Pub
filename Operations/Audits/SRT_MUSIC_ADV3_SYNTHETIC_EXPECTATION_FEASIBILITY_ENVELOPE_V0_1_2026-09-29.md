---
id: SRT-MUSIC-ADV3-SYNTHETIC-EXPECTATION-FEASIBILITY-ENVELOPE-V0-1-20260929
type: audit
status: active
canonical: false
layer: operations
epistemic_layer: os
claim_mode: synthetic_feasibility
created: 2026-09-29
updated: 2026-09-29
research_mode: U_to_TEST
root_question: Is a source-faithful local-statistical manipulation capable in principle of shifting PAC expectedness enough to estimate it separately from cadence closure?
comparative_claim: none
named_comparator: "illustrative online Beta-Bernoulli learner; Chander-Aslin local-probability result"
n_mode_triggered: false
priority: current_next_bounded_companion
dependency:
  - Operations/Audits/SRT_MUSIC_ADV3_SOURCE_FIDELITY_IMPLEMENTATION_FEASIBILITY_V0_1_2026-09-29.md
  - Operations/Audits/SRT_MUSIC_ADV3_SOURCE_OWNED_PREDICTION_TABLE_STIMULUS_LOGIC_V0_1_2026-09-29.md
tags: [Music, ADV3, SyntheticFeasibility, Bayesian, Expectedness, Cadence, CellC]
---

# Music ADV-3 synthetic expectedness feasibility envelope v0.1

> Role: paper-only sanity check. This is not a fitted cognitive model and not evidence about human behaviour.
>
> Purpose: test whether the proposed local-statistical schedule can, in principle, create a useful expectedness shift for PAC while closure is held as a separate construct.

## 0. Source anchor

Chander–Aslin used:
- global PAC/DC incidence of 50/50;
- order schedules with local DC proportions including 20/80, 80/20 and 50/50 phases;
- trial-by-trial local DC probability from preceding trials;
- evidence that expectations adapt to the local statistics;
- an empirical result that prospective confidence began decreasing once local DC probability rose to roughly 74%.

They did **not** show complete erasure of the long-term PAC prior.

Therefore the synthetic target is not:

~~~text
prove PAC becomes absolutely improbable.
~~~

It is:

~~~text
test whether plausible online learners can generate
a meaningful PAC expectedness shift
under an 80% DC local history.
~~~

## 1. Minimal learner

Use an illustrative Beta-Bernoulli learner for PAC vs DC:

~~~text
P(PAC | history)
=
(alpha_PAC + count_PAC)
/
(alpha_PAC + beta_DC + n).
~~~

This is intentionally simple.

It is **not** claimed to be the Chander–Aslin fitted model, IDyOM, or the human learner.

## 2. Prior envelope

Three illustrative priors were used to separate:

~~~text
prior odds
from
prior strength / equivalent sample size.
~~~

### P1 weak schematic prior

~~~text
Beta(6,1)
PAC:DC prior odds = 6:1
equivalent prior count = 7.
~~~

### P2 stronger PAC prior

~~~text
Beta(24,1)
PAC:DC prior odds = 24:1
equivalent prior count = 25.
~~~

The 24:1 odds are motivated only as an illustrative scale by the Bach-chorale corpus contrast discussed in the Chander–Aslin paper; the equivalent sample size is not empirically fitted.

### P3 same 24:1 odds, much stronger memory

~~~text
Beta(96,4)
PAC:DC prior odds = 24:1
equivalent prior count = 100.
~~~

This condition isolates the effect of prior strength while holding prior odds constant.

## 3. One 20-trial local window

Compare two idealized local windows:

~~~text
PAC-high / DC-low:
16 PAC + 4 DC

DC-high / PAC-low:
4 PAC + 16 DC.
~~~

These match the 20/80 vs 80/20 proportions in the source-faithful schedule family.

Posterior PAC probability after the window:

| Illustrative prior | After 80% PAC window | After 80% DC window | Difference |
|---|---:|---:|---:|
| Beta(6,1) | 22/27 = 0.815 | 10/27 = 0.370 | 0.444 |
| Beta(24,1) | 40/45 = 0.889 | 28/45 = 0.622 | 0.267 |
| Beta(96,4) | 112/120 = 0.933 | 100/120 = 0.833 | 0.100 |

Interpretation:

~~~text
local history can create a large relative shift
without guaranteeing absolute prior reversal.
~~~

## 4. Random-order first-phase simulation

Reproducibility note:

~~~text
phase length = 20 trials;
PAC-high phase = 16 PAC + 4 DC;
DC-high phase = 4 PAC + 16 DC;
300 deterministic pseudo-random permutations per phase;
seeds = 0..299;
posterior evaluated immediately before each PAC trial.
~~~

A simple simulation randomized the order of the 16/4 or 4/16 events within a 20-trial first phase and evaluated the learner **before each PAC trial**.

Across 300 random schedules:

| Illustrative prior | Mean P(PAC), DC-low phase | Mean P(PAC), DC-high phase | Approx shift |
|---|---:|---:|---:|
| Beta(6,1) | 0.823 | 0.507 | 0.316 |
| Beta(24,1) | 0.917 | 0.760 | 0.157 |
| Beta(96,4) | 0.946 | 0.894 | 0.052 |

For the Beta(24,1) condition:
- no PAC trial dropped below 0.50 in this first 20-trial phase;
- some PAC predictions nevertheless dropped below 0.65;
- the mean expectedness shift remained substantial.

For the strong-memory Beta(96,4) condition:
- absolute PAC expectedness stayed high;
- the shift was much smaller.

## 5. What this establishes — and does not

Established only at synthetic-design level:

~~~text
source-faithful local schedules
can create a separable expectedness range
for the same PAC class
under some plausible prior strengths.
~~~

Not established:

~~~text
human prior strength;
human posterior form;
minimum perceptually meaningful shift;
PAC expectedness below 0.5;
completion independence;
E2 residual;
SRT increment.
~~~

## 6. Consequence for ADV-3

The simulation supports the source-fidelity correction:

~~~text
absolute Cell C
= poor hard requirement;

continuous expectedness separation
= feasible design target.
~~~

The prereg-preparation gate should eventually freeze a minimum expectedness separation criterion **before human outcome data are inspected**.

Examples of acceptable future criteria could be:
- model-based separation in q_t;
- separate-sample expectedness effect;
- a minimum standardized manipulation-check effect.

No numeric criterion is selected here.

## 7. Additional fail pressure from the source study

Chander–Aslin reported that:
- PACs remained favoured overall;
- local statistics modulated the rate of expectation adaptation;
- confidence decline emerged only once local DC probability became sufficiently high.

Therefore a strong long-term prior is not a design anomaly; it is part of the phenomenon to be modelled.

The experiment should not be tuned until PAC becomes artificially “unlikely enough.”

## 8. Current disposition

~~~text
synthetic feasibility
= PASS FOR RELATIVE EXPECTEDNESS SEPARATION;

absolute low-P PAC
= NOT ROBUST;

source-faithful continuous crossed design
= RETAIN;

completion independence
= STILL UNTESTED;

experiment
= NO;

preregistration
= NO;

next allowed move
= freeze an implementation-feasibility contract:
  schedule family,
  online expectedness estimator,
  independent completion check,
  minimum manipulation criterion,
  and fair baseline memory scope.
~~~
