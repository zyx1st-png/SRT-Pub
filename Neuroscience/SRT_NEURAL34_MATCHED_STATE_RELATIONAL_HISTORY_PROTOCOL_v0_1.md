---
id: SRT-NEURO-NEURAL34-MATCHED-STATE-RELATIONAL-HISTORY-PROTOCOL
type: experimental_protocol
status: draft
record_stage: draft_active
version: v0_1
layer: empirical_bridge
epistemic_layer: experimental
claim_mode: prediction
claim_level: P4-P5
canonical: false
domain: neuroscience_history_relational_compatibility_metaplasticity
created: 2026-08-15
dependency:
  - Neuroscience/patches/SRT_Neuro_NEURAL34_History_Conditioned_Relational_Possibility_v0_1.md
  - Neuroscience/patches/SRT_Neuro_NEURAL33_Distributed_Ripple_Relational_Reinstatement_v0_1.md
  - Neuroscience/SRT_NEURAL33_EXPERIMENT_PROTOCOL_v0_1.md
tags:
  - matched-state
  - different-history
  - relational-possibility
  - metaplasticity
  - causal-test
  - falsification
---

# NEURAL34 Protocol v0.1 — Matched Current State / Different Relational History

> **Purpose**: distinguish ordinary current-state explanations from a genuine history-conditioned relational disposition. The protocol is deliberately stricter than observing replay or synchrony after learning.

---

## 1. Core discriminating question

Can two trials / systems be closely matched on currently observed component state and current input, yet differ in the probability of a future coordinated relation because their prior relational histories differ?

Target form:

\[
P(R_{future}|X,E,C,G,H,\tau)
>
P(R_{future}|X,E,C,G,\tau)
\]

where:

- `X` = current component activity / excitability proxies;
- `E` = current phase / temporal eligibility;
- `C` = cue / task context;
- `G` = common-driver / global-state proxies;
- `H` = preregistered relation-specific history;
- `tau` = declared timescale / retention regime of the hypothesized history-conditioned disposition;
- `R_future` = future coordinated relation.

If the history term adds no stable predictive or causal value after strong controls, NEURAL34 should be downgraded.

---

## 2. Timescale declaration before testing

NEURAL34 evidence spans intertrial, learning-to-rest, memory-age and metaplasticity regimes. Do not assume a single biological `K` across them.

For any experiment declare:

\[
K_{ij}^{(\tau)}
\]

as a **timescale-indexed test-local relation-disposition family**.

Examples:

```text
K^(fast): seconds / intertrial latent-state regime
K^(intermediate): minutes-to-hours learning / consolidation / metaplasticity regime
K^(slow): days-to-weeks memory-age / long-term reorganization regime
```

These labels are analytical bins, not claims of three discrete neural substances.

Default guard:

\[
K^{(\tau_1)} \neq K^{(\tau_2)}
\]

unless a dedicated experiment establishes cross-scale mapping.

---

## 3. Minimal within-subject design

Create two relation classes using the same component pool where feasible:

```text
Pair class H+
A-B repeatedly co-participates in a task with reliable joint consequence / reinforcement / successful retrieval history

Pair class H-
A-C has matched exposure / component activation opportunities but lacks the same joint consequence-bearing history
```

Before the critical probe, match or model:

```text
current firing rate;
recent spike count;
current phase state;
ripple / oscillatory power;
current task cue;
arousal;
trial position;
component identity or excitability proxy;
recording quality;
major shared-input proxies.
```

Then deliver the same class of probe / retrieval opportunity and compare:

\[
P(R_{AB}^{future})
\quad vs \quad
P(R_{AC}^{future}).
\]

The strongest result is a relation-specific history effect under matched current state.

---

## 4. Human intracranial version

Preferred context:

```text
clinically indicated intracranial monitoring;
repeated item-pair or sequence learning;
single-unit + LFP recording;
pre-learning baseline rest;
learning;
post-learning rest;
retrieval.
```

Required relation-level longitudinal measurements:

```text
PRE pair coupling;
learning-time pair coupling;
POST ripple-window pair coupling;
retrieval-time reinstatement;
```

Primary test:

```text
learning-history strength
predicts POST / retrieval coordination
beyond PRE coupling and current firing / phase / power.
```

This explicitly improves on a simple `RUN correlation predicts POST correlation` result by controlling pre-existing compatibility.

---

## 5. Stronger item-pair manipulation

Use an associative-memory design in which the same item can enter different relation histories.

Example:

```text
A-B learned repeatedly and successfully;
A-C presented equally often but without the same association / consequence structure.
```

At retrieval, hold cue `A` constant and ask whether:

```text
A-related ensemble
preferentially coordinates with B-related ensemble
rather than C-related ensemble
```

under matched current activity.

This directly tests whether relational history shapes future coalition identity.

---

## 6. Ripple-window test

Cross with NEURAL33:

```text
current co-ripple event = opportunity window
history-conditioned K^(tau) = relation-selection bias within the declared timescale regime
```

Test:

\[
P(R_{AB}|coR,H+)
>
P(R_{AC}|coR,H-)
\]

while matching:

```text
co-ripple duration;
power;
regional event rate;
number of spikes;
trial load;
cue identity.
```

If all pairs become equally coordinated once co-ripple occurs, the stronger `history-shaped relation landscape` hypothesis is weakened.

---

## 7. Neutral-ping / perturbation test

Inspired by selection-history ping paradigms, use an identical neutral probe to reveal latent history-conditioned response structure.

Logic:

```text
same neutral probe I
+ matched current observable state X
+ different H
-> different relation-specific evoked response R
```

Possible probes:

```text
visual ping;
single-pulse TMS;
brief electrical microstimulation where clinically / ethically justified;
optogenetic / sensory pulse in animal models.
```

The probe should not itself encode the learned relation.

---

## 8. Animal causal version

A stronger causal test can manipulate relation history while minimizing component-history differences.

One possible family:

```text
same neuronal ensembles A, B, C identified before training;
A-B repeatedly coactivated in a consequence-bearing behavioral context;
A-C receives matched total stimulation / firing exposure without the same temporal / consequence relation;
```

Later:

```text
return current activity toward matched baseline;
apply identical probe;
measure A-B vs A-C coordinated reactivation / plasticity.
```

A positive result would support history-conditioned relational disposition more strongly than naturalistic replay alone.

---

## 9. Metaplasticity test

The cleanest generic form is:

```text
priming history differs;
baseline output after priming is matched;
identical induction follows;
future plastic response differs.
```

At pair / network level, test whether prior joint history changes:

```text
LTP/LTD induction threshold;
coactivation probability;
cross-region evoked response;
ripple recruitment probability;
relation-specific reactivation stability.
```

This establishes future-transition differences despite similar current output, but still requires localization to distinguish relational from single-node hidden-state explanations.

Do not generalize a metaplasticity result at one `tau` to a working-memory or memory-age `K^(tau)` without an explicit bridge experiment.

---

## 10. Mandatory competing models

### Model N — node-only hidden state

```text
history changes hidden variables inside component A or B;
pair effect is fully explained once those variables are measured.
```

### Model G — common driver

```text
history changes global driver G;
A and B only appear relationally coupled.
```

### Model A — anatomy / fixed connectivity

```text
future relation follows pre-existing anatomy;
learning history contributes no incremental effect.
```

### Model K — relation-disposition model

```text
relation-specific history retains predictive / causal value after node, common-driver and anatomy controls within a declared tau regime.
```

NEURAL34 requires explicit model comparison, not only significance of `H`.

---

## 11. State-matching hierarchy

Perfect microphysical matching is impossible in vivo. Therefore claims must be tiered.

### Match-1 — coarse observed state

```text
mean firing / power / task / arousal matched
```

Supports only weak history-conditioned latent-state inference.

### Match-2 — rich component state

Adds:

```text
single-cell firing histories;
intrinsic excitability proxies;
local connectivity / waveform features;
phase;
neuromodulatory proxies;
```

Allows stronger relation-level residual inference.

### Match-3 — causal component equalization

Experimentally manipulate or clamp important component-level variables where feasible.

Only Match-3 begins to strongly discriminate relational disposition from unmeasured node-state explanations.

No level licenses a metaphysical claim of complete microstate identity.

---

## 12. Outcome metrics

Primary:

```text
future pair / ensemble co-firing probability;
encoding-to-retrieval relation similarity;
POST ripple coupling;
evoked cross-region response;
relation-specific plasticity change.
```

Secondary:

```text
behavioral RT;
recognition / recall;
choice bias;
later memory stability.
```

Prefer relation identity prediction over generic `more synchrony`.

---

## 13. Statistical criterion

Use hierarchical subject/session models and held-out prediction.

Required comparison:

```text
Base:
R_future ~ X + E + C + G + PRE_relation + tau

History model:
R_future ~ X + E + C + G + PRE_relation + tau + H

Interaction model:
R_future ~ ... + H:E + H:C
```

If multiple timescale regimes are pooled, include explicit `H:tau` and regime effects or fit separate models; do not treat pooled `K` as a single mechanism by default.

A meaningful NEURAL34 result requires:

```text
stable out-of-sample gain;
non-trivial effect size;
subject-level consistency;
replication across sessions / subjects.
```

Very small P values from massive neuron-pair counts are insufficient.

---

## 14. Direct falsifiers

Substantially downgrade NEURAL34 if high-quality studies repeatedly show:

1. `H` adds no prediction once PRE relation and rich current node state are included;
2. pair-specific effects vanish after common-driver controls;
3. all history effects are explained by one component's excitability / synaptic state;
4. neutral probes reveal only generic readiness, never relation identity;
5. co-ripple windows erase history-specific coalition differences;
6. causal manipulation of relational history fails to alter later relation-specific response;
7. apparent POST relation changes are fully attributable to selection / recording drift;
8. apparent cross-scale unity disappears when `tau` is modeled explicitly, in which case retain only regime-specific bridge claims.

---

## 15. Strongest positive pattern

The most informative result would be:

```text
PRE coupling comparable
+ current X/E/C/G comparable
+ different controlled relation history H
-> different future relation identity / probability
-> intervention on the history or latent state changes the future relation
```

This would justify the claim:

> **History is functionally retained partly in the conditional structure of which joint transitions are later realizable within the tested timescale regime.**

It would still not prove that relations are ontologically independent of physical component states.

---

## 16. Link back to SRT

If supported, NEURAL34 would provide a concrete neuroscience implementation pattern for the abstract SRT claim:

```text
past selection / consequence
-> writeback
-> changed future selectability
```

with a new refinement:

```text
writeback may change not only candidate weights
but the relation geometry among future candidates / components.
```

This is the specific empirical increment to test. `K^(tau)` remains a local model family and is not a canonical SRT symbol.
