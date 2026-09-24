---
status: frozen
type: experiment-preregistration
date: 2026-09-24
programme: SRT Neuro Objectification–Scale Stability
---

# RIKEN Sleep Population-Size Scaling Extension

## Status and freeze boundary

This is an independent follow-up experiment. It is not an amendment to PR #1051 or to the claim-freeze work associated with that pull request.

This protocol is frozen before inspection of any new RIKEN Sleep population-size outcome (`Sleep ΔQ(N)`, its slope, any zero crossing, or any animal-level pattern). The confirmatory/held-out domain is RIKEN Sleep. The earlier RIKEN Anesthesia N-only decomposition is hypothesis-generating context only and cannot be used to tune this test or to claim confirmatory support.

The protocol is a holdout test of whether the state contrast changes systematically with the number of randomly sampled single neurons. It does not preregister a mandatory sign reversal or a negative ΔQ at small N.

## Biological scope and units

The eligible RIKEN Sleep recordings are the previously accepted recordings only:

| recording | animal | session |
|---|---|---|
| `mouse01_sleep` | mouse01 | mouse01_sleep |
| `mouse02_sleep` | mouse02 | mouse02_sleep |
| `mouse03_sleep` | mouse03 | mouse03_sleep |
| `mouse04_day1_sleep` | mouse04 | mouse04_day1_sleep |
| `mouse04_day2_sleep` | mouse04 | mouse04_day2_sleep |
| `mouse05_sleep` | mouse05 | mouse05_sleep |

The biological unit is the animal. Sessions and recordings are nested within animals; windows are not biological replicates. The two mouse04 sessions are combined within mouse04 before cross-animal summaries. No new recording inclusion or exclusion is permitted, and no recording may be excluded based on a population-size result.

The mouse05 Sleep recordings overlap the broader Phase 1 lineage. They are treated as held out for this specific N-scaling hypothesis because Sleep was not used in the Phase 3C N-only transformation decomposition, but this is not a claim of complete programme-level independence.

## Frozen signal and graph pipeline

- Signal: the existing RIKEN S3 `smoothed_spike` implementation, exactly as used by the Phase 2 multi-recording analysis. No S1 or S2 substitution is allowed.
- Association: the existing correlation implementation and its fixed preprocessing.
- Graph: the existing RIKEN multi-recording rule: connected minimum-spanning-tree backbone plus the strongest remaining absolute-correlation edges, with target mean degree `16`. Tie handling and edge ordering are inherited from the existing implementation.
- Network: binary, connected graph.
- Louvain: 200 repeats per graph, inherited seed root `12345`, retaining max-Q. The repeat count is not reduced in this experiment.
- No fixed-density primary alternative, new graph family, parameter tuning, mechanism analysis, or null model is allowed before Gate 1.

## Frozen population-size design

For every eligible recording, begin with the full accepted single-neuron population. For each target, draw uniform random subsets without replacement. Do not spatially cluster, average, replace, or duplicate neurons. The same subset membership is reused across all state windows of the recording, so state contrasts are paired on the same sampled neurons.

The target grid is frozen as:

```text
100, 150, 225, 340, 510, 765, 1150, 1725, 2600, 3900, FULL
```

For each recording, the usable finite-N targets are the intersection of this grid with the number of accepted neurons. `FULL` uses all accepted neurons. A target that is larger than the recording population is unavailable; it is not extrapolated, duplicated, or replaced. The usable animal grid is the intersection of the usable finite-N grids across that animal's sessions. `FULL` remains a separate reference point and is available whenever the recording is eligible.

There are 100 subset repeats for every recording × finite target N. Each repeat has a deterministic subset seed:

```text
subset_seed = stable_seed(
    12345,
    "population_size_scaling_subset",
    recording_id,
    target_N,
    subset_repeat,
)
```

The selected indices are sorted after sampling for deterministic downstream matrix ordering. `FULL` has one deterministic full-population membership and is not treated as 100 random biological replicates.

The exact `stable_seed` function is the existing Phase 2 function: BLAKE2b over the stringified parts, 8-byte digest, reduced modulo `2**31 - 1` (with one used as the fallback). No result-dependent seed or subset selection is allowed.

## Frozen state contrast and outcome definitions

For each recording, subset, state window, and target N, compute the max-Q from the 200 Louvain trials. State-level Q is the mean of the window-level max-Q values for that recording and subset. The recording-level subset contrast is:

```text
ΔQ_recording(N, subset) = mean Q_NREM(N, subset) - mean Q_Wake(N, subset)
```

For each animal and finite N, first take the median of the 100 subset contrasts within each session. For animals with more than one session, average the session medians at that N. Thus mouse04 is reduced to one animal-level ΔQ(N) curve before any cross-animal summary. At each animal × N, report the subset median and the 2.5th–97.5th percentile across the 100 subset contrasts; this interval describes subset variability and is not biological uncertainty.

The primary within-animal trend is an ordinary least-squares slope:

```text
ΔQ_animal(N) = α_animal + β_N,animal × log10(N) + error
```

`β_N` and Spearman rho are estimated from the finite target N points only. `FULL` is reported as a secondary reference because its neuron count is animal/session-specific and is not a common fixed x-coordinate; it is not included in the primary slope or rho. An animal with fewer than two usable finite-N points has an estimand marked unavailable rather than being rescued by extrapolation.

The primary directional expectation is `β_N > 0`: the Sleep ΔQ becomes larger at larger population size. A sign reversal or zero crossing is secondary and is not required for a positive result.

Secondary quantities:

- per-animal Spearman rho between `log10(N)` and animal-level ΔQ(N);
- per-animal linear β_N;
- `FULL` ΔQ;
- smallest-available-N ΔQ;
- range of finite-N ΔQ;
- cross-animal median and mean β_N with an animal-resampling bootstrap interval;
- direct zero-crossing bracket only when adjacent observed target values bracket zero. Report `N_low < N_zero < N_high`; do not interpolate a precise zero.

The cross-animal bootstrap resamples animals, not windows or subsets, with a fixed analysis seed `98765` and 10,000 resamples. It is descriptive; no p-value is required.

## Primary Gate 1

The success criterion is descriptive and fixed before execution:

```text
at least 4 of 5 animals have β_N > 0
AND
the cross-animal median β_N > 0
```

The classifications are:

- `PS-A`: at least 4/5 positive β_N and median β_N > 0 — prospective Sleep support for population-size dependence;
- `PS-B`: 3/5 positive β_N or a median near zero — heterogeneous/inconclusive;
- `PS-C`: at most 2/5 positive β_N or median β_N ≤ 0 — the Anesthesia hypothesis is not prospectively supported.

If `PS-B` or `PS-C`, stop the biological population-size programme and return to the stability-audit manuscript. If `PS-A`, stop and return for a separate null-calibration preregistration. Do not run any null, mechanism, or additional robustness control before this gate.

The legacy descriptive band `±0.01` may be shown lightly in figures for continuity only. It is not an uncertainty interval, significance threshold, or success criterion.

## Kiyooka anchor

The analysis will identify a session-specific minimum active-neuron count, or the closest faithfully recoverable equivalent, only if the original Kiyooka network-size-matched subsampling control can be reconstructed from the available source and method record. If the anchor cannot be faithfully reconstructed, it will be recorded as:

```text
N_Kiyooka_anchor = ANCHOR-UNRESOLVED
```

No silent approximation is allowed. This anchor is a published-method reference point, not a fitted parameter and not a target selected from the present outcomes.

The comparison will distinguish explicitly between: (1) the Kiyooka full/large-N cellular result; (2) the Kiyooka state-matched large-N subsampling control; and (3) this continuous N-sweep. The question is whether a positive large-N effect attenuates or crosses zero at smaller N, without implying that Kiyooka failed to control neuron count.

## Reconstructibility and audit trail

For every completed subset/window result, retain under the ignored `.local/` runtime area:

- recording ID, animal ID, session ID, condition, state, and window;
- accepted-neuron count, target N, subset repeat, subset seed;
- selected-neuron indices and their hash;
- deterministic graph provenance and graph seed policy;
- all 200 Louvain seeds and per-trial Q values;
- Q_max and the source data/provenance hashes.

The canonical result record will include the data inventory, file hashes, actual usable N grid, unavailable targets and reasons, runtime, and checkpoint lineage. No raw data or large runtime files will be committed to Git.

## Stopping and interpretation boundary

This experiment addresses population-size dependence of an operational network state contrast. It does not establish SRT, objectification, a mechanism, global synchronization, emergent modules, collective properties, consciousness, or any other theory-level claim. Generic facts about finite-size effects, subsampling, graph metrics, and coarse-graining are not novel claims. Any residual novelty claim would require an actual prospective result across random single-neuron subsamples, and a sign-crossover claim requires a directly observed zero bracket.

No Sleep ΔQ(N), slope, zero crossing, or animal pattern is inspected or used to alter this frozen protocol. Execution results will be written only after all scheduled computation and validation are complete.

## Source and lineage references

- Kiyooka et al., *Cell Reports* (2025), DOI: [10.1016/j.celrep.2025.116902](https://doi.org/10.1016/j.celrep.2025.116902).
- Existing RIKEN Phase 2 multi-recording implementation and its recorded data/checksum inventory in the local `.local/phase2_multirecording/` runtime area.
- Existing Phase 3C RIKEN Anesthesia N-only decomposition: hypothesis-generating context only; not used to tune this Sleep holdout test.
