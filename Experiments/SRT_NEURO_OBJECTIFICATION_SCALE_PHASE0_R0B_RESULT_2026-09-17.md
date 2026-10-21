---
id: SRT-NEURO-OBJECTIFICATION-SCALE-PHASE0-R0B-RESULT-20260917
type: experiment_result
status: active
version: v0_1
record_stage: phase0_r0b_deterministic_recalculation_complete_native_louvain_pending
date: 2026-09-17
layer: operations
epistemic_layer: experimental
claim_mode: evidence
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
dependency:
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_REPLICATION_v0_1.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_R0A_RESULT_2026-09-17.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_MANIFEST_2026-09-17.json
  - Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md
tags: [Neuroscience, Phase0, R0B, Replication, Modularity, CoarseGraining, Reproducibility]
---

# Phase 0 R0B result — processed-time-series recalculation diagnostic

> **Scope**: independently recalculate the predeclared Phase-0 spot checks from extracted `smoothed_spike` time-series windows for the source example sleep mouse 5 and anesthesia mouse 2.
>
> **Boundary**: the deterministic signal -> correlation -> fixed-density graph -> coarse-graining path was recomputed directly. The current runtime does not provide MATLAB/Octave, so the 200-run stochastic Louvain layer was evaluated with a Python numerical-equivalent diagnostic implementation. It is **not** source-native MATLAB execution and cannot satisfy the locked exact-Q acceptance criterion by itself.

## 1. Input integrity

Two bounded R0B extraction bundles were received from the source `sleep_data.mat` and `ane_data.mat` files.

```text
phase0_sleep_r0b.npz
bytes: 23438127
sha256: b293f00ea52e3b4e484d9b175ebb488d57766ef895e5a234cf8a2c9077b5af8e
wake_spike:   6920 x 1500 float64
target_spike: 6920 x 1500 float64
centroid:     6920 x 2 float64
source target: NREM

phase0_ane_r0b.npz
bytes: 9747954
sha256: 85b007715f6d66eaf8c64892d70ea57cb3b2727fde646b1f78c31379e9896108
wake_spike:   3210 x 2900 float64
target_spike: 3210 x 2900 float64
centroid:     3210 x 2 float64
source target: anesthesia
```

The received hashes exactly match the extraction log produced when the bundles were created from the source MAT files.

The extraction log records:

```text
sleep_data.mat:
  smoothed_spike = 6920 x 19000
  centroid = 6920 x 2
  used_frame state count = 2
  wake usable frames = 9146
  NREM usable frames = 5660
  locked extracted j=1 windows = 1500 frames each

ane_data.mat:
  smoothed_spike = 3210 x 19562
  centroid = 3210 x 2
  used_frame state count = 2
  wake usable frames = 15528
  anesthesia usable frames = 2933
  locked extracted j=1 windows = 2900 frames each
```

This establishes integrity of the bounded R0B extraction objects. It does **not** substitute for the still-missing checksum/inventory of the original Zenodo `mouse_data.zip` archive.

## 2. Source-code path re-audited

Pinned source commit:

```text
90e1c7dc5823f9d413b1bddf5c649ec87d6598a3
```

The recalculation was checked against the pinned source implementations of:

```text
scripts/calc_modularity.m
functions/densityBasedThresh.m
functions/choosePC.m
functions/repeat_modularity_analysis.m
functions/modularity_analysis.m
functions/get_close_clustering.m
functions/spatial_coarse_graining.m
functions/2019_03_03_BCT/community_louvain.m
scripts/get_maxQ.m
```

The deterministic path was kept at:

```text
smoothed_spike
-> corrcoef(dataMat')
-> NaN correlations = 0
-> diagonal = 0
-> abs(corrMat)
-> source densityBasedThresh logic
-> K = 0.05 binary graph
```

For coarse-40:

```text
source get_close_clustering
-> N_neighbors = 40
-> arithmetic mean signal within each spatial group
-> same correlation / K = 0.05 graph path
```

No density, window, target state, neighbor level, exclusion, or SRT-specific transformation was tuned against the result.

## 3. Deterministic recalculation

### 3.1 Single-cell K = 0.05 graphs

The source threshold rule uses the `floor(N(N-1)/2 * K)`-th ranked upper-triangle absolute correlation and then applies `>= threshold`.

```text
Sleep wake:
  N = 6920
  threshold = 0.1820609522811058
  edges = 1,196,987
  realized density = 0.0500000000000000
  connected components = 1

Sleep NREM:
  N = 6920
  threshold = 0.1874141087770515
  edges = 1,196,987
  realized density = 0.0500000000000000
  connected components = 1

Anesthesia-package wake:
  N = 3210
  threshold = 0.1190624862201591
  edges = 257,522
  realized density = 0.0499999514605049
  connected components = 1

Anesthesia:
  N = 3210
  threshold = 0.1438927608837623
  edges = 257,522
  realized density = 0.0499999514605049
  connected components = 1
```

No threshold-boundary tie inflated any of the four selected single-cell edge counts.

### 3.2 Source coarse-40 construction

The source grouping algorithm produced:

```text
Sleep:
  6920 neurons -> 173 spatial groups
  all group sizes = 40

Anesthesia:
  3210 neurons -> 81 spatial groups
  80 groups of 40 + one group of 10
```

The resulting K = 0.05 graphs were:

```text
Sleep wake coarse-40:
  N = 173
  threshold = 0.3777975033064291
  edges = 743
  connected components = 41

Sleep NREM coarse-40:
  N = 173
  threshold = 0.3741838452606741
  edges = 743
  connected components = 13

Anesthesia-package wake coarse-40:
  N = 81
  threshold = 0.2152157902548800
  edges = 162
  connected components = 22

Anesthesia coarse-40:
  N = 81
  threshold = 0.4683106664748282
  edges = 162
  connected components = 49
```

For disconnected coarse graphs, the diagnostic implementation retained the source `modularity_analysis.m` initialization rule: neurons/nodes in the first largest connected component start separately and nodes outside it start in one shared initial community.

## 4. Louvain runtime-equivalent diagnostic

### 4.1 Why this layer is diagnostic only

The source pipeline freezes:

```text
200 Louvain trials
root seed = 12345
per-trial reseeding
first maximal-Q partition
BCT community_louvain objective and hierarchy
```

The current environment has no MATLAB/Octave. A Python implementation of the same modularity objective and source hierarchy was therefore used to test numerical behavior, but Python random-integer/permutation streams are not source-native MATLAB `randi` / `randperm` streams.

This distinction is material: on some selected graphs the Python search found a higher local optimum than the packaged author 200-run maximum. Therefore these runs cannot be relabeled as exact source reproduction.

### 4.2 200-trial diagnostic table

`Q_reference` values were frozen in the R0A result before the raw-data rerun.

| Package / scale / state | Q reference | Python-equivalent 200-run max Q | Difference |
| --- | ---: | ---: | ---: |
| Sleep single wake | 0.31583972 | 0.3166832855 | +0.0008435655 |
| Sleep single NREM | 0.31295221 | 0.3139269706 | +0.0009747606 |
| Anesthesia single wake | 0.21996698 | 0.2204033568 | +0.0004363768 |
| Anesthesia single anesthesia | 0.39955802 | 0.3992347273 | -0.0003232927 |
| Sleep coarse-40 wake | 0.39793841 | 0.3979384076 | -0.0000000024 |
| Sleep coarse-40 NREM | 0.40336546 | 0.4046932428 | +0.0013277828 |
| Anesthesia coarse-40 wake | 0.42118198 | 0.4216582838 | +0.0004763038 |
| Anesthesia coarse-40 anesthesia | 0.27069044 | 0.2706904435 | +0.0000000035 |

Two coarse conditions reproduce the frozen author max-Q to approximately `1e-9`, while other conditions differ by `3e-4` to `1.3e-3`, including several Python maxima **above** the author packaged maxima.

That pattern is inconsistent with a simple raw-data/window mismatch and is instead compatible with different stochastic search trajectories / runtime details. It does not establish exact source equivalence.

## 5. State-direction check

Although exact max-Q equality is unresolved, the preselected wake-versus-target direction is preserved in all four selected scale/package comparisons:

```text
Sleep single-cell:
  reference NREM - wake = -0.00288751
  diagnostic NREM - wake = -0.00275631
  direction preserved = YES

Anesthesia single-cell:
  reference anesthesia - wake = +0.17959104
  diagnostic anesthesia - wake = +0.17883137
  direction preserved = YES

Sleep coarse-40:
  reference NREM - wake = +0.00542705
  diagnostic NREM - wake = +0.00675484
  direction preserved = YES

Anesthesia coarse-40:
  reference anesthesia - wake = -0.15049154
  diagnostic anesthesia - wake = -0.15096784
  direction preserved = YES
```

This is only a spot-check of the source example datasets and must not be generalized into a new confirmatory source claim.

## 6. Acceptance diagnosis

Locked acceptance rule:

```text
|Q_recomputed - Q_reference| <= 1e-6
  = numerical reproduction

1e-6 < difference <= 1e-4
  = runtime / solver / tie-breaking diagnosis required

systematic difference > 1e-4
  = R0-PARTIAL or R0-FAIL depending on cause
```

Current diagnosis:

```text
bounded source time-series inputs available: YES
input hashes verified against extraction log: YES
single-cell correlation / threshold / K=.05 graph recomputed: YES
coarse-40 grouping / averaging / graph recomputed: YES
all selected reference state-effect directions preserved: YES
source modularity objective independently exercised: YES
native unmodified MATLAB pipeline executed: NO
exact 200-run source RNG / randperm path reproduced: NO
all Q values within locked 1e-4 diagnostic ceiling: NO
material contradiction of source-level qualitative result: NO
```

Because the deterministic data path is coherent and no source-level qualitative contradiction was found, the unresolved stochastic-runtime mismatch is not classified as `R0-FAIL`.

Because the locked exact-Q/native-runtime condition is not met, it also cannot be classified as `R0-PASS`.

## 7. R0 verdict

```text
R0A = NUMERIC-PASS / NATIVE-PENDING
R0B deterministic raw/processed-data recalculation = PASS
R0B stochastic Louvain exact source reproduction = UNRESOLVED / NATIVE-PENDING
R0B overall = PARTIAL

R0 VERDICT = R0-PARTIAL
Phase 1 confirmatory standing = NOT AUTHORIZED
```

Under the locked protocol, an `R0-PARTIAL` result may support only an explicitly reviewed exploratory Phase 1. No such review is performed by this result record.

## 8. Required closure for possible R0-PASS

The shortest closure path is:

1. run the pinned unmodified source MATLAB code in a compatible MATLAB runtime;
2. use the original extracted/source MAT inputs corresponding to these windows;
3. record MATLAB and toolbox versions;
4. reproduce the four selected single/coarse-40 max-Q comparisons with the source 200-run RNG path;
5. resolve any remaining differences against the frozen references under the locked tolerance rule;
6. separately complete original `mouse_data.zip` archive SHA-256 / inventory integrity if full Gate-0 `R0-PASS` is sought.

Until then, do not promote Phase 0 to full replication PASS and do not inherit confirmatory standing into Phase 1.