---
id: SRT-NEURO-OBJECTIFICATION-SCALE-TRANSFORMATION-DECOMPOSITION-PREREGISTRATION-20260923
type: experiment_preregistration
status: frozen
version: v0_1
record_stage: phase3c_finite_size_objectification_transformation_preregistration
date: 2026-09-23
layer: operations
epistemic_layer: experimental
claim_mode: hypothesis
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
post_primary_exploratory: true
alternative_explanation_test: finite_size_and_transformation
tags: [Neuroscience, Objectification, Transformation, FiniteSize, ResultBlind, Preregistration]
dependency:
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_MULTIRECORDING_PREREGISTRATION_2026-09-21.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_MULTIRECORDING_RESULT_2026-09-22.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_ANESTHESIA_PREREGISTRATION_2026-09-22.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_ANESTHESIA_RESULT_2026-09-23.md
---

# Phase 3C — finite-size and objectification-transformation decomposition

## 1. Freeze boundary and scope

This is a post-primary exploratory decomposition of the already completed
connected-graph Anesthesia chains. It is frozen before any new N-only subset,
random-aggregation, synthetic or other Phase 3C outcome is inspected. It does
not amend the Phase 1, RIKEN multi-recording, Hamburg Anesthesia, density,
mean-degree or connected-graph records.

The question is:

> Does the observed grain-dependent inference shift arise from node-count
> reduction, many-to-one aggregation, spatial organization of aggregation, or
> a combination of these transformations?

This record authorizes only the finite-size/transformation decomposition below.
It does not authorize Hamburg Sleep, new biological datasets, matched-component
analysis, new network metric families, a new graph family, or SRT/GRG theory
validation claims. The bounded methodological term used here is
`bounded inference equivalence`; it is not ontological or generative
equivalence.

## 2. Primary datasets and hierarchy

Only the two completed Anesthesia chains are primary:

```text
RIKEN Anesthesia:
  animals: mouse03, mouse05, mouse06, mouse07
  recording unit: one frozen anesthesia recording per animal
  graph regime: connected MST backbone plus strongest remaining abs-correlation edges
  target mean degree: k_bar = 16

Hamburg Anesthesia:
  animals: 37527, 37528, 37529, 37530, 48, 51, 53
  recordings: 88 total; 39 Awake and 49 Isoflurane
  graph regime: connected MST backbone plus strongest remaining abs-correlation edges
  target mean degree: k_bar = 4
```

The graph regimes are not harmonized across datasets. They are inherited from
the respective frozen records and are compared only within dataset.

The hierarchy is fixed:

```text
window nested in recording
recording nested in condition
condition nested in animal
primary biological unit = animal
```

Windows, subsets, aggregations, Louvain trials and recordings are never treated
as independent biological animals.

## 3. Signal and graph invariants

The primary signals are inherited without re-comparing alternatives:

```text
RIKEN: frozen S3 smoothed deconvolved activity (`spike_smoothed`)
Hamburg: frozen S3-equivalent `spks.npy` plus the preregistered Gaussian smoothing
```

For both datasets and every representation, use Pearson correlation across
window time points, set non-finite correlations to zero, remove the diagonal,
rank edges by absolute correlation, and use a binary undirected graph.

The frozen connected graph construction is:

```text
maximum-spanning-tree backbone using abs(correlation)
+ strongest remaining non-MST edges
exact M = round(N * k_bar / 2) edges
deterministic upper-triangle tie ordering
```

No density threshold, degree target, connectivity repair, resolution, signal,
window or seed parameter may be changed in this decomposition. Every generated
graph must be connected, have zero isolated nodes, and have exactly the frozen
edge count.

## 4. Representation family

For every recording and target grain, the four representations are:

```text
R0 = full single-neuron representation (G1)
R1 = N-only single-neuron subset
R2 = random many-to-one aggregation
R3 = frozen spatial aggregation (actual G2 or G3)
```

R0 and R3 are reused from the completed trusted connected-graph outputs when
their implementation and seed provenance match the frozen source records. They
are not rerun merely to create new outcomes. A rerun is permitted only when
needed to make a complete, exact matched implementation; such a rerun must be
recorded as inherited/recomputed and cannot alter the scientific rules.

The same source windows and state labels are used for R0–R3 within a recording.
The target state is Isoflurane and the reference state is Awake. For each
representation, `DeltaQ = mean(Q_max,Iso) - mean(Q_max,Awake)` at the recording
level. The existing frozen `DeltaQ` values are not reselected or redefined.

## 5. R1 — N-only subset

For each recording and each actual target grain G2/G3, let `N_target` be the
number of output groups in the already frozen spatial representation.

For each of 100 independent subset repeats:

```text
sample exactly N_target accepted G1 neurons without replacement
retain their original single-neuron time series
do not average or spatially cluster
sort retained source indices before graph construction
```

The subset membership seed is:

```text
stable_seed(12345, dataset, recording_id, target_grain, "N-only", repeat_index)
```

The complete seed and membership manifest is written before any Q summary is
aggregated. Exactly 100 repeats are used for every eligible recording and both
target grains. A change to 50 would require a separate result-blind amendment
before any R1/R2 outcome is inspected; no silent reduction is allowed.

## 6. R2 — random aggregation

For each recording and target grain, recover the exact frozen spatial group-size
multiset from R3, including the final remainder group. The random aggregation
must match:

```text
output node count
group-size multiset
remainder handling
aggregation statistic = arithmetic mean
```

For each of 100 independent repeats:

```text
randomly permute all accepted G1 neuron indices
partition the permutation using the exact R3 group-size multiset
average the member time series within each group
average member coordinates only for provenance
never use centroid distance, nearest-neighbor order, or spatial clustering
```

The partition seed is:

```text
stable_seed(12345, dataset, recording_id, target_grain, "random-aggregation", repeat_index)
```

The output node order is the deterministic partition order generated from that
seed. No R2 partition may be discarded because its Q or DeltaQ is inconvenient.

## 7. R3 — actual spatial aggregation

R3 is the already frozen actual G2/G3 construction for each dataset:

```text
RIKEN: pinned source-compatible G2/G3 spatial grouping
Hamburg: frozen dataset-size-aware local grouping from the Hamburg preregistration
```

The grouping is formed from accepted ROI geometry before state comparison and
reused across all windows and states. The existing connected-graph R3 results
are the preferred source. Their group labels, group-size multiset, input
recording ID, graph diagnostics and seed provenance are copied into the Phase
3C provenance manifest.

## 8. Louvain and Q

For new R1/R2 graphs, use the already frozen Python Louvain implementation,
resolution 1.0, 200 repeats per complete window, and maximum Q as the window
statistic. The Louvain seed list is common to R1 and R2 for a given dataset,
recording, target grain, state/window and repeat:

```text
stable_seed(12345, dataset, recording_id, target_grain,
            state_index, window_index, "louvain", repeat_index)
```

The transformation membership seed and Louvain seed are separate. Parallel
execution may change scheduling only; it may not change graph identity,
algorithm, seed list, repeat count or max-Q selection. All 200 Q trials, the
maximum and first maximum, graph diagnostics, representation ID and membership
hash are retained.

## 9. Predeclared contrasts

For each recording/animal and target grain, retain the continuous values:

```text
C1 finite-size contribution       = DeltaQ_R1 - DeltaQ_R0
C2 aggregation contribution       = DeltaQ_R2 - DeltaQ_R1
C3 spatial-organization contribution = DeltaQ_R3 - DeltaQ_R2
C4 total objectification shift    = DeltaQ_R3 - DeltaQ_R0
```

At the animal level, first average recording-level `DeltaQ` within animal and
representation, then summarize across animals. R1/R2 repeats are transformation
replicates and are summarized as within-animal distributions; they are never
counted as biological `n=100`.

The practical state-effect bands remain:

```text
positive: DeltaQ > +0.01
null: -0.01 <= DeltaQ <= +0.01
negative: DeltaQ < -0.01
```

No threshold will be chosen after inspecting new results.

## 10. Transformation labels and diagnostic patterns

For each transformed representation relative to the same-animal R0 contrast:

```text
PRESERVES-DIRECTION:
  both are positive or both are negative and both remain outside the null band

ATTENUATES-BUT-PRESERVES:
  same substantive sign remains and absolute magnitude is reduced without
  entering the null band

CROSSES-NULL:
  R0 is substantive but the transformed representation is inside the null band

REVERSES-DIRECTION:
  R0 and transformed representation are on opposite substantive sides

HETEROGENEOUS:
  animal/recording classifications do not support one of the above as a
  dataset-level description
```

The following patterns are frozen as descriptive diagnostics:

```text
T-A: R0 positive; R1 negative; R2 negative; R3 negative
T-B: R0 positive; R1 positive; R2 negative; R3 negative
T-C: R0 positive; R1 positive; R2 positive/null; R3 negative
T-D: R1/R2/R3 are highly variable across animals or transformation repeats
```

These labels are not GRG proof, SRT validation, or causal identification.

## 11. Synthetic finite-size calibration

The synthetic component is supportive only. It uses a transparent,
degree-controlled stochastic block model, not a GRG-specific generative model.

Before any synthetic Q is calculated, the runtime writes a manifest using the
result-blind empirical node counts from RIKEN Anesthesia:

```text
large N  = median accepted G1 node count
medium N = median accepted G2 node count
small N  = median accepted G3 node count
```

The frozen model is:

```text
K = 4 equal planted communities
expected mean degree = 16 at every N regime
Wake within/between ratio r = 1.5
Target ratios r = 1.75 (small effect), 2.5 (medium effect), 4.0 (large effect)
```

For each N regime, effect level and state, solve the symmetric SBM edge
probabilities so that the expected mean degree is 16 while the within/between
ratio equals the frozen `r`. Use 200 paired synthetic datasets per cell, with
shared planted community membership within each pair and independent graph
edge draws. Use 200 Louvain repeats and maximum Q for each synthetic graph.

Synthetic seeds are:

```text
stable_seed(12345, "synthetic", N_regime, effect_level,
            replicate_index, state, "graph")
stable_seed(12345, "synthetic", N_regime, effect_level,
            replicate_index, state, "louvain", repeat_index)
```

Report estimated `DeltaQ`, bias relative to the paired planted-direction
ordering, sign-error rate, and substantive reversal rate
`P(estimated DeltaQ < -0.01 | true effect > 0)`. Synthetic graph validity,
finite Q, seeds and all replicate summaries are retained.

Predeclared synthetic labels:

```text
FS-A: any empirical-N/effect cell has substantive reversal rate >= 0.10
FS-B: no cell reaches 0.10, but some cell has absolute bias > 0.02
FS-C: no cell reaches 0.10 and all absolute biases are <= 0.02
FS-D: technical invalidity or model instability prevents interpretation
```

## 12. Checkpoint and provenance contract

All runtime state remains outside canonical source under:

```text
.local/phase3c_transformation/
```

At minimum, maintain:

```text
phase3c_state.json
execution.log
commands.log
environment.txt
source_manifest.json
seed_manifest.json
membership_manifest.json
per-recording and per-repeat result files
```

After every expensive recording/target-grain/transform repeat: flush the result,
validate graph invariants and seed/membership hashes, atomically update the
checkpoint, then continue. A resumed run must reuse only complete validated
outputs and must not repeat completed work. Stdout/stderr, exit code and failed
recording identity are preserved.

The following validation gates are mandatory:

```text
all preregistered RIKEN and Hamburg animals accounted for
R1 exact target N
R2 exact output N and exact R3 group-size multiset
R3 source implementation reused or explicitly recorded as exact rerun
graph regimes unchanged: RIKEN k_bar=16, Hamburg k_bar=4
all generated graphs connected with finite Q
all 200 Q trials retained for every new window
seed, membership and input signal hashes complete where feasible
no result-based exclusion
no new biological data
```

## 13. Reporting and stop boundary

The result record must report R0–R3 distributions, C1–C4, transformation labels,
animal-level summaries, finite-size calibration and the bounded inference
equivalence classification separately for RIKEN and Hamburg. It must state what
the decomposition rules down and what remains unresolved.

The allowed non-canonical research implication is only:

> Objectification changes may be treated as explicit transformations whose
> inferential consequences can be classified as preserving, attenuating, or
> breaking a bounded inference relation.

After the result record and validation are committed, STOP. Do not automatically
start Hamburg Sleep, matched-component analysis, a new graph control, an
association-measure family, a new dataset, or another GRG experiment.
