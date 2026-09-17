---
id: SRT-NEURO-OBJECTIFICATION-SCALE-PHASE0-R0A-RESULT-20260917
type: experiment_result
status: active
version: v0_1
record_stage: phase0_r0a_numeric_reconstruction_complete_native_runtime_unavailable_r0b_recorded_separately
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
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_MANIFEST_2026-09-17.json
  - Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md
tags: [Neuroscience, Phase0, R0A, Replication, Modularity, CoarseGraining, Reproducibility]
---

# Phase 0 R0A result — released-results numerical reconstruction

> **Scope**: reconstruct the source paper's Fig. 3 / Fig. 7 modularity comparisons from the released `results/` MATLAB files, using the aggregation and paired-test logic in the pinned author code.
>
> **Boundary**: this is **not full R0A native-runtime completion** because the unmodified MATLAB scripts were not executed in a MATLAB-compatible runtime. It is a numerical reconstruction from the released author result matrices. R0B was subsequently completed under the compatibility-runtime conditions documented in `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_R0B_RESULT_2026-09-17.md`.

## 1. Input received

A user-provided ZIP containing the Zenodo package's `results/` directory was materialized in the current execution environment.

```text
bundle: results.zip
bytes: 147233118
sha256: 24edc39620e704ecfa74436395316dc9e7195c8105589494e28fe0f4412fded2
scientific files in results/: 33
```

This hash identifies the **user-provided re-zipped results bundle**, not the original Zenodo `mouse_data.zip`; it must not be substituted for the source-archive checksum.

Key released files required for R0A were present, including:

```text
consensus_sp_res_sleep15_densityall_200_maxQ.mat
consensus_sp_res_ane15_densityall_200_maxQ.mat
coarse{2,5,10,20,40,80,160}_consensus_sp_res_sleep15_densityall_200_maxQ.mat
coarse{2,5,10,20,40,80,160}_consensus_sp_res_ane15_densityall_200_maxQ.mat
basic_info_sleep.mat
basic_info_ane.mat
```

## 2. Reconstruction method

Pinned source-code commit:

```text
90e1c7dc5823f9d413b1bddf5c649ec87d6598a3
```

The released MAT arrays were parsed read-only. The numerical aggregation followed the author scripts:

- `plot_fig/fig3_cdef_compare_modularity.m` for the single-cell density sweep;
- `plot_fig/fig7_bcde_Q_diff_lv_of_coarse.m` for the scale comparison at `K = 0.05`;
- `functions/get_x_sleep.m` for biological-mouse grouping;
- `functions/plot_state_comparison.m` for per-mouse averaging;
- paired one-sample t-tests on `Q_awake - Q_unconscious`, matching the source plotting code.

For sleep, the two sessions of mouse 4 are grouped as one biological mouse exactly as encoded by `get_x_sleep.m`; therefore the paired sleep analysis uses `n = 5` mice. The anesthesia analysis uses `n = 4` mice.

No SRT-specific transformation, metric, threshold, exclusion, or post-hoc parameter choice was introduced.

## 3. Fig. 3 logic — single-cell modularity density sweep

### 3.1 Wake vs NREM

Across every released single-cell connection density, the reconstructed mean modularity is higher in NREM than wakefulness.

At the Phase-0 common density `K = 0.05`:

```text
Wake mean Q = 0.282323
NREM mean Q = 0.333398
Wake - NREM = -0.051075
paired t-test p = 0.007904
n = 5 biological mice
```

Across the full source density grid (`0.008` through `0.30`), all reconstructed `Wake - NREM` mean contrasts are negative. The corresponding paired-test p-values range from approximately `0.0047` to `0.0285`.

### 3.2 Wake vs isoflurane anesthesia

Across every released single-cell connection density, the reconstructed mean modularity is higher under anesthesia than wakefulness.

At `K = 0.05`:

```text
Wake mean Q = 0.253169
Anesthesia mean Q = 0.339932
Wake - Anesthesia = -0.086763
paired t-test p = 0.002807
n = 4 mice
```

Across the full density grid, all reconstructed `Wake - Anesthesia` mean contrasts are negative; paired-test p-values are below `0.05` throughout the released grid.

### 3.3 R0A Fig. 3 numerical verdict

```text
directional source result: RECONSTRUCTED
single-cell unconscious-state Q > wake Q: YES
unexpected discrepancy: NONE DETECTED
```

## 4. Fig. 7 logic — scale dependence at K = 0.05

Scale labels below are the source's single-cell baseline followed by the seven spatial coarse-graining neighbor counts.

```text
scale:          single   2        5        10       20       40       80       160
```

### 4.1 Sleep

Reconstructed `Wake - NREM` mean Q contrast:

```text
single  -0.051075   p=0.007904
2       -0.060413   p=0.005291
5       -0.052944   p=0.013475
10      -0.035631   p=0.064049
20      -0.012821   p=0.645641
40      -0.019601   p=0.670853
80      -0.037833   p=0.559177
160     -0.071982   p=0.312502
```

The important source-level pattern is **loss of a stable/significant state separation with coarsening**, not monotonic shrinkage of the raw contrast magnitude. The contrast is significant at the single-cell, 2-neighbor and 5-neighbor levels, but is not retained from the 10-neighbor level onward in this paired analysis.

### 4.2 Anesthesia

Reconstructed `Wake - Anesthesia` mean Q contrast:

```text
single  -0.086763   p=0.002807
2       -0.087202   p=0.004620
5       -0.042327   p=0.098776
10       0.025696   p=0.510403
20       0.074032   p=0.124028
40       0.132008   p=0.132751
80       0.122157   p=0.116550
160      0.225377   p=0.081917
```

Here the source-level scale dependence is especially clear: the single-cell and 2-neighbor contrasts favor higher modularity under anesthesia, the difference is no longer significant at 5 neighbors, and the mean contrast changes sign from 10 neighbors onward. Those coarse-scale reversed means are themselves not significant in the released comparison.

### 4.3 R0A Fig. 7 numerical verdict

```text
source scale-dependence pattern: RECONSTRUCTED
single-cell state difference retained uniformly under coarse-graining: NO
unexpected discrepancy: NONE DETECTED
```

This supports the bounded wording already used in the benchmark: the state-wise modularity difference is **not consistently retained** after spatial coarse-graining. It should not be rewritten as a claim of monotonic attenuation at every scale.

## 5. R0A status

The released-results layer is internally coherent with the author analysis code and reproduces the source-facing pattern relevant to the benchmark.

However, the locked Phase-0 contract distinguishes result-file reconstruction from running the original pipeline. Therefore the current state is:

```text
R0A released-file inventory: PASS
R0A numerical reconstruction: PASS
R0A qualitative Fig.3 result: PASS
R0A qualitative Fig.7 result: PASS
R0A native unmodified MATLAB-script execution: NOT RUN
R0A overall status: NUMERIC-PASS / NATIVE-UNAVAILABLE
```

No full `R0-PASS` may be assigned from this result alone.

## 6. Reference values frozen for R0B

The public example datasets used by the source calculation code correspond to sleep mouse index 5 and anesthesia mouse index 2. At `K = 0.05`, the released reference Q values are frozen here before raw-data recalculation.

### Sleep — source mouse index 5

Single cell:

```text
Awake windows: 0.31583972, 0.27825815, 0.27316868, 0.28424811, 0.29714956, 0.31990769
NREM windows:  0.31295221, 0.35152735, 0.37613918
```

`N_neighbors = 40`:

```text
Awake windows: 0.39793841, 0.51678293, 0.45563347, 0.48534550, 0.47796029, 0.48767954
NREM windows:  0.40336546, 0.48715060, 0.36362080
```

### Anesthesia — source mouse index 2

Single cell:

```text
Awake windows:      0.21996698, 0.31412077, 0.29275178, 0.32444522, 0.29522828
Anesthesia window:  0.39955802
```

`N_neighbors = 40`:

```text
Awake windows:      0.42118198, 0.26863283, 0.46008611, 0.33760098, 0.41729538
Anesthesia window:  0.27069044
```

These values are now frozen as the comparison targets for R0B; they were not selected after seeing a raw-data rerun.

## 7. Next gate

R0B requires processed time-series input from `sleep_data.mat` and `ane_data.mat`, at minimum enough to independently recompute:

```text
smoothed_spike -> correlation -> K=0.05 binary graph -> 200 Louvain runs -> max-Q
```

for single-cell and the predeclared `N_neighbors = 40` coarse level.

The recalculation was completed and is recorded separately. The current Phase 0 state is:

```text
R0 verdict = R0-PARTIAL
Phase 1 authorized = NO
```

No SRT-facing inference is promoted from R0A alone.
