---
id: SRT-NEURO-OBJECTIFICATION-SCALE-PHASE0-R0B-RESULT-20260917
type: experiment_result
status: active
version: v0_1
record_stage: phase0_r0b_complete_native_matlab_unavailable
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
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_R0A_RESULT_2026-09-17.md
  - Neuroscience/SRT_NEURO_OBJECTIFICATION_SCALE_STABILITY_BENCHMARK_v0_1.md
tags: [Neuroscience, Phase0, R0B, Replication, Modularity, CoarseGraining, Reproducibility]
---

# Phase 0 R0B result — source-data recalculation spot-check

## 1. Execution identity and boundary

This record completes the four prespecified R0B target recalculations for the locked Phase 0 protocol. It does not redesign the experiment, alter a scientific parameter, or make an SRT-facing theoretical claim.

At execution start, the live local `origin/main` was `d89b883683e55cb18f1088cd597618ec0438b64b`. `git fetch origin` was attempted but could not reach GitHub over port 443; the live local remote-tracking value was therefore retained as the recorded baseline. The working branch was `experiments/neuro-objectification-phase0-r0b-20260917`.

The author source snapshot is the exact requested commit `90e1c7dc5823f9d413b1bddf5c649ec87d6598a3`. A normal GitHub clone was unavailable, so the commit-specific GitHub codeload archive was reconstructed as a local Git repository and checked against the GitHub API tree: 196/196 blob hashes matched. The reconstructed author repository was clean before and after execution; no pinned source file was modified.

The required native MATLAB execution was not run because no MATLAB executable or application was available locally. Octave execution below is explicitly classified as a compatibility runtime, not native MATLAB replication.

## 2. Data materialization and integrity

- Source: [official `mouse_network_2P` repository](https://github.com/oizumi-lab/mouse_network_2P), commit `90e1c7dc5823f9d413b1bddf5c649ec87d6598a3`.
- Data: [official Zenodo record](https://zenodo.org/records/17667863), archive `mouse_data.zip`.
- Archive size: `1,865,754,335` bytes.
- SHA-256: `dd29cf6adda2e04745834525a94122076152c31f5136acbc39b57d4a9013638c`.
- MD5: `d611c4577b4e3a32762860fa4ab7b5f6`, equal to the Zenodo-recorded MD5.
- ZIP CRC/integrity test: PASS (`unzip -t`, no errors).
- Extracted inventory: `sleep_data.mat`, `ane_data.mat`, 33 files under `results/`, and a present but empty `modularity_res/` directory.
- `sleep_data.mat`: `1,185,449,811` bytes; source matrix dimensions include `smoothed_spike` `6920 x 19000`.
- `ane_data.mat`: `538,646,196` bytes; source matrix dimensions include `smoothed_spike` `3210 x 19562`.
- The empty `modularity_res/` directory is recorded as an archive/package discrepancy; the advertised time-series and released result files required for this Phase 0 run were present.

The Phase 1 RIKEN CBS v3.0 dataset was not used.

## 3. Runtime and execution method

- MATLAB: unavailable (`matlab` command not found; no local MATLAB application detected).
- Octave: GNU Octave `11.3.0`.
- Octave packages: `statistics 1.9.3`, `datatypes 1.4.2`.
- Python: `3.14.0`; used for read-only checks and prior R0A released-result reconstruction, not as a replacement modularity implementation.
- Actual R0B runtime: Octave calling the pinned author modularity/BCT functions, with external runtime-only sparse `graph`/`conncomp` and vectorized `corrcoef` compatibility shims, plus an external fixed-seed worker scheduler. The source call remains `corrcoef(dataMat')`, followed by source NaN-to-zero, diagonal removal, `abs(corrMat)`, binary density thresholding at `K=0.05`, and author `modularity_analysis`.
- Randomness: the source seed root `12345`, 200 Louvain trials per window, and source max-Q first-hit semantics were retained. Worker output files record and verify their expected trial seeds.
- Smoke tests: synthetic author BCT/Louvain smoke and synthetic parallel scheduler smoke passed. Two real serial smoke attempts were stopped before completion when Octave performance bottlenecks were identified; their logs are retained. The vectorized runtime shim then allowed a completed real-window smoke test before the full resumable targets.

## 4. R0A status

- Previous released-results numerical reconstruction: PASS.
- Previous qualitative Fig. 3 result: PASS.
- Previous qualitative Fig. 7 result: PASS.
- Native unmodified MATLAB-script execution: NOT RUN; MATLAB unavailable.
- R0A discrepancy: no discrepancy was detected in the previous released-result numerical/qualitative reconstruction. The R0B runtime differences below are not silently reclassified as native R0A output.

The source plot scripts `plot_fig/fig3_cdef_compare_modularity.m` and `plot_fig/fig7_bcde_Q_diff_lv_of_coarse.m` were not labeled as executed because the required native MATLAB runtime was absent.

## 5. R0B target completion

All four frozen targets completed and were checkpointed after each window. Every window has 200 finite Q trials.

| Target | Source selection | Windows | Nodes | Result |
|---|---|---:|---:|---|
| Sleep single-cell | mouse 5; 6 awake + 3 NREM; 1500 frames | 9 | 6920 | COMPLETE |
| Sleep coarse40 | same windows; author `get_close_clustering` + `spatial_coarse_graining`; `N_neighbors=40` | 9 | 173 | COMPLETE |
| Anesthesia single-cell | mouse 2; 5 awake + 1 anesthesia; 2900 frames | 6 | 3210 | COMPLETE |
| Anesthesia coarse40 | same windows; author coarse-graining logic; `N_neighbors=40` | 6 | 81 | COMPLETE |

## 6. Numeric comparison against frozen R0A reference values

Reference values were taken from `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_R0A_RESULT_2026-09-17.md`; they were not reselected. `within_1e-4` means absolute difference `<=1e-4`.

| Condition | State | Scale | Window | Q reference | Q recomputed | Absolute difference | <=1e-6 | <=1e-4 |
|---|---|---|---:|---:|---:|---:|:---:|:---:|
| sleep | awake | single-cell | 1 | 0.31583972 | 0.3167719808055733 | 0.0009322608055733 | no | no |
| sleep | awake | single-cell | 2 | 0.27825815 | 0.2783191555212326 | 0.0000610055212326 | no | yes |
| sleep | awake | single-cell | 3 | 0.27316868 | 0.2731883943938384 | 0.0000197143939384 | no | yes |
| sleep | awake | single-cell | 4 | 0.28424811 | 0.2836781030845582 | 0.0005700069154418 | no | no |
| sleep | awake | single-cell | 5 | 0.29714956 | 0.2973167938612281 | 0.0001672338612281 | no | no |
| sleep | awake | single-cell | 6 | 0.31990769 | 0.3194121155400888 | 0.0004955744599113 | no | no |
| sleep | NREM | single-cell | 1 | 0.31295221 | 0.3145524830087031 | 0.0016002730087031 | no | no |
| sleep | NREM | single-cell | 2 | 0.35152735 | 0.3520075753106448 | 0.0004802253106448 | no | no |
| sleep | NREM | single-cell | 3 | 0.37613918 | 0.3770063907270110 | 0.0008672107270110 | no | no |
| sleep | awake | coarse40 | 1 | 0.39793841 | 0.3979384076413507 | 0.0000000023586493 | yes | yes |
| sleep | awake | coarse40 | 2 | 0.51678293 | 0.5167829305007345 | 0.0000000005007346 | yes | yes |
| sleep | awake | coarse40 | 3 | 0.45563347 | 0.4543872011361310 | 0.0012462688638690 | no | no |
| sleep | awake | coarse40 | 4 | 0.48534550 | 0.4844189555637271 | 0.0009265444362729 | no | no |
| sleep | awake | coarse40 | 5 | 0.47796029 | 0.4779602897568877 | 0.0000000002431124 | yes | yes |
| sleep | awake | coarse40 | 6 | 0.48767954 | 0.4876632327927413 | 0.0000163072072588 | no | yes |
| sleep | NREM | coarse40 | 1 | 0.40336546 | 0.4028799979711945 | 0.0004854620288055 | no | no |
| sleep | NREM | coarse40 | 2 | 0.48715060 | 0.4880563138417061 | 0.0009057138417061 | no | no |
| sleep | NREM | coarse40 | 3 | 0.36362080 | 0.3629270227823980 | 0.0006937772176021 | no | no |
| ane | awake | single-cell | 1 | 0.21996698 | 0.2192329323445045 | 0.0007340476554955 | no | no |
| ane | awake | single-cell | 2 | 0.31412077 | 0.3141278109509144 | 0.0000070409509144 | no | yes |
| ane | awake | single-cell | 3 | 0.29275178 | 0.2939007338288285 | 0.0011489538288285 | no | no |
| ane | awake | single-cell | 4 | 0.32444522 | 0.3240400431629837 | 0.0004051768370162 | no | no |
| ane | awake | single-cell | 5 | 0.29522828 | 0.2952329427748610 | 0.0000046627748610 | no | yes |
| ane | anesthesia | single-cell | 1 | 0.39955802 | 0.3991229509705345 | 0.0004350690294655 | no | no |
| ane | awake | coarse40 | 1 | 0.42118198 | 0.4211819844535895 | 0.0000000044535894 | yes | yes |
| ane | awake | coarse40 | 2 | 0.26863283 | 0.2686328303612254 | 0.0000000003612254 | yes | yes |
| ane | awake | coarse40 | 3 | 0.46008611 | 0.4600861149215059 | 0.0000000049215059 | yes | yes |
| ane | awake | coarse40 | 4 | 0.33760098 | 0.3376009754610578 | 0.0000000045389422 | yes | yes |
| ane | awake | coarse40 | 5 | 0.41729538 | 0.4172953818015547 | 0.0000000018015547 | yes | yes |
| ane | anesthesia | coarse40 | 1 | 0.27069044 | 0.2706904435299498 | 0.0000000035299498 | yes | yes |

Summary over 30 windows:

- maximum absolute difference: `0.0016002730087030792`.
- `<=1e-6`: `9/30`.
- `1e-6 < difference <= 1e-4`: `5/30`.
- `>1e-4`: `16/30`.

The largest discrepancy is sleep, NREM, single-cell, window 1: reference `0.31295221`, recomputed `0.3145524830087031`, difference `0.0016002730087031`. The most likely unresolved cause is cross-runtime numerical/algorithmic behavior in the MATLAB-versus-Octave BCT/Louvain path, including RNG/parallel ordering, tie handling, floating-point edge ranking, and near-degenerate max-Q selection. Evidence for this attribution is that the pinned author modularity functions and frozen data path were retained, the external shims are limited to runtime compatibility, all trial outputs are complete and finite, and all six anesthesia coarse40 windows agree within approximately `5e-9` while other windows do not. Native MATLAB rerun is required to resolve this attribution; no parameter was changed to force agreement.

The five rows in the diagnostic band `(1e-6,1e-4]` are not exact PASS. The 16 rows above `1e-4` are material for the strict numerical gate, although the observed state/scale pattern does not by itself constitute a contradiction of the source-level qualitative result.

## 7. Qualitative source result

- Single-cell unconscious Q > awake: directionally preserved at the source-comparison level already established by R0A; anesthesia is clearly higher than the awake rows, while sleep NREM is elevated in the group pattern but overlaps individual awake windows. This is not a claim that every NREM window exceeds every awake window.
- Coarse-grain difference not consistently retained: preserved as the source-level Fig. 7 qualitative conclusion from the released-results reconstruction; the coarse40 spot-check does not provide a basis for upgrading that conclusion to an SRT claim.

These are source-replication observations only. They do not establish SRT, objectification, Bearer, One, consciousness mechanism, Selection, or any SRT-facing empirical increment.

## 8. Checkpoints, logs, and files

Persistent runtime/checkpoint area: `.local/phase0_replication/` (excluded from Git and contains no canonical raw data commit).

- `phase0_state.json`: all four R0B target flags and comparison flag true; native MATLAB flag remains false/unavailable.
- `execution.log`, `commands.log`, `environment.txt`, `data_inventory.txt`, `checksums.txt`.
- `r0b_numeric_results.json`: 30 per-window records and summary counts.
- `logs/r0b_sleep_single.log`, `logs/r0b_sleep_coarse40.log`, `logs/r0b_ane_single.log`, `logs/r0b_ane_coarse40.log`.
- `logs/r0b_comparison.log` and `logs/r0b_results_integrity.log`.
- `results/r0b_sleep_single.mat`, `results/r0b_sleep_coarse40.mat`, `results/r0b_ane_single.mat`, `results/r0b_ane_coarse40.mat`.
- source-recovery and transport-repair evidence logs, including the official archive checksum/CRC verification.

Canonical files written in this repository:

- `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_R0B_RESULT_2026-09-17.md`
- updated `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_MANIFEST_2026-09-17.json`

## 9. Verdict

`R0-PARTIAL`

Materialization/integrity is complete, all four R0B targets are complete, and the source-level qualitative direction is preserved. Full `R0-PASS` is not assigned because the native MATLAB source-script gate is unavailable and the Octave compatibility rerun has 16/30 Q differences above `1e-4` (with 5 additional rows requiring diagnostic treatment). Phase 1 remains unauthorized.
