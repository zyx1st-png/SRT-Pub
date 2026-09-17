---
id: SRT-NEURO-OBJECTIFICATION-SCALE-PHASE0-REPLICATION
type: experiment_execution
status: active
version: v0_1
record_stage: phase0_r0b_complete_native_runtime_unavailable
date: 2026-09-17
layer: operations
epistemic_layer: experimental
claim_mode: evidence
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
dependency:
  - Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md
  - Materials/2026/SRC_2026_09_16_Neuro_Kiyooka_Scale_Dependent_Functional_Networks.md
  - Materials/2026/SRC_2026_09_16_Neuro_Oomoto_Wake_Sleep_Anesthesia_Open_Dataset.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_MANIFEST_2026-09-17.json
tags: [Neuroscience, Phase0, Replication, OpenData, Modularity, CoarseGraining, Reproducibility]
---

# SRT Neuro Objectification–Scale Benchmark — Phase 0 Replication v0.1

> **Purpose**: reproduce the source-paper analysis before any SRT-facing objectification interpretation.
>
> **Hard boundary**: Phase 0 is source replication only. It cannot establish SRT, NEURAL33, NEURAL34, consciousness, Bearer, One, or an objectification-specific empirical increment.

## 1. Replication target

Primary paper:

```text
Kiyooka D, Oomoto I, Kitazono J, Saito Y, Kobayashi M,
Matsubara C, Kobayashi K, Murayama M, Oizumi M. (2026).
Single-cell resolution functional networks during unconsciousness are
segregated into spatially intermixed modules.
Cell Reports 45(2):116902.
DOI: 10.1016/j.celrep.2025.116902
```

Official source code:

```text
repository: https://github.com/oizumi-lab/mouse_network_2P
pinned commit: 90e1c7dc5823f9d413b1bddf5c649ec87d6598a3
```

Official paper replication data identified by the source repository:

```text
Zenodo DOI: 10.5281/zenodo.17667863
expected archive name from source README: mouse_data.zip
```

The broader RIKEN CBS v3.0 dataset (`10.60178/cbs.20260708-001`) is **not** substituted into Phase 0. It is reserved for Phase 1 after source replication. This keeps source reproduction separate from the later full-sample benchmark.

## 2. Why Phase 0 is split into R0A and R0B

A figure can sometimes be regenerated from author-supplied precomputed results without independently reproducing the calculation that generated them. Therefore:

```text
R0A = official result / figure regeneration
R0B = source-code raw/processed-data recalculation spot-check
```

`R0-PASS` requires both levels to be adequate. R0A alone is not sufficient.

## 3. Source-code lock

The following settings are frozen from the pinned author code and must not be changed during source replication unless a source-breaking bug is documented first.

### 3.1 Network input

```text
signal: smoothed_spike
association: corrcoef(dataMat')
NaN correlations: set to 0
diagonal: removed
edge ranking: abs(corrMat)
primary graph type: binary
```

### 3.2 Connection-density grids

Single-cell:

```text
[0.008, 0.01:0.01:0.10, 0.15:0.05:0.30]
```

Coarse-grained:

```text
0.05:0.05:0.30
```

For the direct single-cell versus coarse-grain comparison in the source Fig. 7 logic, the locked common density is:

```text
K = 0.05
```

### 3.3 Time windows

```text
wake/sleep analysis: 1500 frames per network window
wake/anesthesia analysis: 2900 frames per network window
```

Only source-provided `used_frame` state indices are used for Phase 0.

### 3.4 Community detection

```text
Louvain iterations per parameter: 200
source random-seed root: 12345
max-Q selection: first maximal-Q partition returned for each parameter
```

Consensus-clustering outputs may be regenerated where required by the source figure pipeline, but Phase 0 must not silently swap max-Q and consensus definitions.

### 3.5 Coarse-graining

Source neighbor levels:

```text
N_neighbors = [2, 5, 10, 20, 40, 80, 160]
```

The source procedure groups spatially nearby neurons through `get_close_clustering.m`; each coarse signal and coordinate is the arithmetic mean of member neurons.

## 4. Phase 0 execution sequence

### Gate 0 — materialization / integrity

Before any run:

1. obtain `mouse_data.zip` from DOI `10.5281/zenodo.17667863`;
2. record archive filename, byte size and SHA-256 in the manifest;
3. unpack into the directory expected by the pinned source repository;
4. inventory actual files; do not infer absent files from script names;
5. verify that the public package supplies at least the advertised awake-sleep and awake-anesthesia example data;
6. record MATLAB/runtime version actually used;
7. record the pinned source-code commit again in the result record.

If the downloadable object or license differs from the source README, stop and document the discrepancy before analysis.

### R0A — official figure/result regeneration

Use the **unmodified pinned author code** to regenerate the source's main modularity comparisons from the public package wherever the package provides the corresponding author results.

Primary targets:

```text
Fig. 3 logic:
  single-cell modularity across awake vs NREM
  single-cell modularity across awake vs anesthesia
  effect tracked across the declared connection-density grid

Fig. 7 logic:
  modularity state contrast across increasing spatial coarse-graining
  common K = 0.05 for the direct scale comparison
```

R0A records:

- whether required result files are present;
- whether scripts run without source edits;
- regenerated numerical curves or tables;
- qualitative agreement with the source result;
- any runtime/version warnings.

### R0B — recalculation spot-check from public time-series data

R0B must recompute, rather than only replot, at least:

```text
sleep package:
  single-cell network calculation
  one prespecified coarse level: N_neighbors = 40

anesthesia package:
  single-cell network calculation
  one prespecified coarse level: N_neighbors = 40
```

The choice `40` is frozen before data inspection because it is a middle coarse-graining level in the source's seven-level sequence. It is not chosen based on effect size.

For each selected condition:

1. run the source correlation -> fixed-density graph -> 200-Louvain calculation;
2. extract `K = 0.05` modularity;
3. compare recomputed Q values with the corresponding packaged/source-author result when available;
4. record the state-effect direction;
5. document all source-code changes, ideally none.

If the package lacks the comparison object needed for numerical equality, R0B may still establish independent recalculation but must be classified `R0-PARTIAL` until the missing reference is resolved.

## 5. Numeric acceptance rules

### 5.1 Q agreement

For a deterministic source-code rerun against a directly corresponding packaged result:

```text
|Q_recomputed - Q_reference| <= 1e-6
```

is accepted as numerical reproduction.

Differences between `1e-6` and `1e-4` require a documented runtime / solver / tie-breaking diagnosis and cannot be silently treated as exact replication. Systematic differences above `1e-4`, or a changed source-level state/grain conclusion, trigger `R0-PARTIAL` or `R0-FAIL` depending on cause.

Community labels are not required to use identical integers because label permutation is meaningless. Near-degenerate Louvain partitions also require Q-level and conclusion-level comparison rather than raw label equality.

### 5.2 Qualitative source claims

Phase 0 is considered directionally reproduced only if the available public package supports the same qualitative pattern relevant to the benchmark:

```text
single-cell:
  unconscious-state modularity > awake modularity in the source comparison

coarse-graining:
  the awake-vs-unconscious modularity separation attenuates / is not retained
  across the source's increasing spatial coarse-graining analysis
```

Phase 0 does not require reproducing every figure in the paper.

## 6. Verdict contract

```text
R0-PASS
= materialization/integrity complete
+ R0A source results/figures regenerate without unexplained discrepancy
+ R0B recalculation spot-check agrees numerically or within declared tolerance
+ source-level qualitative scale conclusion is preserved.

R0-PARTIAL
= source-level direction broadly regenerates
but raw recalculation, package coverage, runtime compatibility,
or direct numeric comparison remains unresolved.

R0-FAIL
= a material source result cannot be regenerated from the released package/code,
or recalculation materially contradicts the packaged/source result without a resolved implementation explanation.
```

No Phase 1 SRT-facing objectification matrix is authorized under `R0-FAIL`. Under `R0-PARTIAL`, Phase 1 may only be exploratory after an explicit review; it cannot inherit confirmatory standing.

## 7. Anti-HARKing / non-substitution guards

During Phase 0:

- do not replace `smoothed_spike` with another signal because it gives a cleaner effect;
- do not tune density, gamma, windows, neighbor count or exclusions against the target result;
- do not substitute RIKEN v3.0 for the source replication package;
- do not reinterpret a failed source reproduction as stronger evidence that objectification matters;
- do not create a new SRT metric;
- do not use NREM versus anesthesia as a primary matched causal comparison;
- do not infer consciousness, One, Bearer or Selection from modularity.

## 8. Current execution state

```text
source paper identified: YES
source code repository identified: YES
source code commit pinned: YES
source analysis parameters audited: YES
source replication data DOI identified: YES
execution manifest created: YES
source archive materialized in current execution environment: YES
MATLAB-compatible runtime available in current execution environment: NO
R0A run: NO
R0B run: YES (Octave compatibility runtime; not native MATLAB)
R0 verdict: R0-PARTIAL
Phase 1 authorized: NO
```

The official Zenodo package was materialized and all four prespecified R0B targets were completed under an Octave compatibility runtime. The current environment lacks MATLAB, so the native unmodified MATLAB-script requirement remains unresolved; this is an execution limitation, not evidence for or against the source result.

## 9. Result writeback contract

When execution becomes possible, the result record must contain:

```text
dataset/archive SHA-256
source-code commit
runtime and relevant toolbox versions
actual file inventory
R0A command/script list and outputs
R0B selected windows / scale levels and numerical comparisons
all deviations
R0-PASS / PARTIAL / FAIL verdict
```

Only after that result is frozen may `Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md` move from Phase-0 lock into Phase 1 execution.
