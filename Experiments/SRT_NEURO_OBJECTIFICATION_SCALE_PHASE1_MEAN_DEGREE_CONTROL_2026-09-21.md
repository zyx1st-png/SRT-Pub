---
id: SRT-NEURO-OBJECTIFICATION-SCALE-PHASE1-MEAN-DEGREE-CONTROL-20260921
type: experiment_result
status: active
version: v0_1
record_stage: phase1_mean_degree_control_complete
date: 2026-09-21
post_primary_exploratory: true
layer: operations
epistemic_layer: experimental
claim_mode: evidence
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, Phase1, MeanDegreeControl, Objectification, Modularity, CoarseGraining, Reproducibility]
---

# Phase 1 mean-degree-matched graph control

## SCOPE

This is a post-primary exploratory control. It does not amend the Phase-1 preregistration and does not inspect or promote an SRT-facing claim. It reuses the ten representative cells declared for the completed density-sensitivity audit.

- Target mean degrees: `k̄ = 4, 8, 16`, frozen before any control Q inspection.
- Graph: absolute pairwise correlation, diagonal removed, NaN/Inf set to zero, exactly `M = round(N × k̄ / 2)` top-ranked unique undirected edges.
- No MST augmentation, forced connectivity, state-specific repair or post-hoc edge addition.
- Runtime: Python 3.14.0; NetworkX 3.6.1; python-louvain 0.16; four workers; 200 repeats; fixed Phase-1 seed identity and max-Q rule.
- Completed: 10 cells, 225 graph/windows, 45,000 Q trials.

No persisted hashable correlation matrices were available in the runtime cache. The existing Phase-1 loader, source-style coarse-graining and window logic were rerun deterministically; no scientific parameter was changed.

## SLEEP

`ΔQ = mean(Q_max,target) − mean(Q_max,wake)`.

| Cell | k̄=4 | k̄=8 | k̄=16 |
|---|---:|---:|---:|
| `sleep_S1_C1_G1` | -0.003566274 | +0.008330413 | +0.018721149 |
| `sleep_S2_C1_G1` | +0.062185104 | +0.070946703 | +0.074655120 |
| `sleep_S3_C1_G1` | +0.036207447 | +0.072736651 | +0.114543343 |
| `sleep_S3_C1_G2` | +0.049562393 | +0.054983154 | +0.045884554 |
| `sleep_S3_C1_G3` | -0.041058978 | -0.046423758 | -0.074039811 |

S3 grain axis:

- k̄=4: G1 `+0.036207447`, G2 `+0.049562393`, G3 `−0.041058978`.
- k̄=8: G1 `+0.072736651`, G2 `+0.054983154`, G3 `−0.046423758`.
- k̄=16: G1 `+0.114543343`, G2 `+0.045884554`, G3 `−0.074039811`.
- The substantive sign reversal persists at all three matched degrees: `MD-C` evidence, with a strong `MD-D` fragmentation warning.

## ANESTHESIA

| Cell | k̄=4 | k̄=8 | k̄=16 |
|---|---:|---:|---:|
| `ane_S1_C1_G1` | +0.123126479 | +0.125595205 | +0.114856578 |
| `ane_S2_C1_G1` | +0.301886215 | +0.222901238 | +0.122710754 |
| `ane_S3_C1_G1` | +0.240659589 | +0.182228480 | +0.146835240 |
| `ane_S3_C1_G2` | -0.054341718 | -0.090257216 | -0.070158162 |
| `ane_S3_C1_G3` | -0.110379515 | -0.147793781 | -0.126337925 |

S3 grain axis:

- k̄=4: G1 `+0.240659589`, G2 `−0.054341718`, G3 `−0.110379515`.
- k̄=8: G1 `+0.182228480`, G2 `−0.090257216`, G3 `−0.147793781`.
- k̄=16: G1 `+0.146835240`, G2 `−0.070158162`, G3 `−0.126337925`.
- The substantive sign reversal persists at all three matched degrees: `MD-C` evidence, with a strong `MD-D` fragmentation warning.

## SIGNAL AXIS

At G1, no substantive positive/negative signal-axis reversal remains under matched degree in either condition:

- Sleep: S1/S2/S3 are all positive at k̄=8 and 16; k̄=4 has a small S1 value (`−0.003566274`) that does not meet the ±0.01 substantive threshold.
- Anesthesia: S1/S2/S3 are all positive at k̄=4, 8 and 16. The previous selected anesthesia S2 negative direction under fixed-density K is therefore not robust to this matched-degree control.
- This result is not a clean attribution because the matched graphs are highly fragmented and sparse.

## GRAIN AXIS

The strongest selected grain contrast remains anesthesia S3 at k̄=4 (`+0.240659589` at G1 versus `−0.110379515` at G3). Sleep S3 also reverses at every target degree.

The finite-size caveat remains: matching mean degree does not match node count, graph diameter, modularity finite-size behavior or component structure.

## GRAPH DIAGNOSTICS

The table reports, across all windows for each cell/degree: `N / M / achieved k̄ / components min–max / largest-component fraction min–max / isolated nodes min–max / tie excess max`.

| Cell | k̄ | N / M / achieved k̄ / components / largest component / isolates / ties |
|---|---:|---|
| `sleep_S1_C1_G1` | 4 | 6920 / 13840 / 4 / 3357–4614 / 0.279–0.479 / 3129–4337 / 0 |
| `sleep_S1_C1_G1` | 8 | 6920 / 27680 / 8 / 2241–3667 / 0.431–0.654 / 2105–3463 / 0 |
| `sleep_S1_C1_G1` | 16 | 6920 / 55360 / 16 / 1273–2533 / 0.611–0.805 / 1200–2392 / 0 |
| `sleep_S2_C1_G1` | 4 | 6920 / 13840 / 4 / 1487–2193 / 0.651–0.765 / 1364–2015 / 0 |
| `sleep_S2_C1_G1` | 8 | 6920 / 27680 / 8 / 464–957 / 0.852–0.930 / 446–894 / 0 |
| `sleep_S2_C1_G1` | 16 | 6920 / 55360 / 16 / 79–224 / 0.966–0.989 / 77–215 / 0 |
| `sleep_S3_C1_G1` | 4 | 6920 / 13840 / 4 / 2487–3805 / 0.287–0.585 / 2187–3407 / 0 |
| `sleep_S3_C1_G1` | 8 | 6920 / 27680 / 8 / 1159–2483 / 0.574–0.817 / 1054–2246 / 0 |
| `sleep_S3_C1_G1` | 16 | 6920 / 55360 / 16 / 308–1215 / 0.803–0.952 / 285–1106 / 0 |
| `sleep_S3_C1_G2` | 4 | 692 / 1384 / 4 / 117–292 / 0.543–0.815 / 106–272 / 0 |
| `sleep_S3_C1_G2` | 8 | 692 / 2768 / 8 / 30–170 / 0.737–0.957 / 28–158 / 0 |
| `sleep_S3_C1_G2` | 16 | 692 / 5536 / 16 / 8–59 / 0.915–0.990 / 7–57 / 0 |
| `sleep_S3_C1_G3` | 4 | 173 / 346 / 4 / 34–78 / 0.538–0.803 / 32–74 / 0 |
| `sleep_S3_C1_G3` | 8 | 173 / 692 / 8 / 15–46 / 0.717–0.919 / 14–42 / 0 |
| `sleep_S3_C1_G3` | 16 | 173 / 1384 / 16 / 3–19 / 0.890–0.988 / 2–17 / 0 |
| `ane_S1_C1_G1` | 4 | 3210 / 6420 / 4 / 2023–2315 / 0.221–0.313 / 1893–2230 / 0 |
| `ane_S1_C1_G1` | 8 | 3210 / 12840 / 8 / 1243–1775 / 0.410–0.593 / 1186–1684 / 0 |
| `ane_S1_C1_G1` | 16 | 3210 / 25680 / 16 / 599–1115 / 0.630–0.807 / 578–1056 / 0 |
| `ane_S2_C1_G1` | 4 | 3210 / 6420 / 4 / 520–2468 / 0.158–0.835 / 507–2337 / 0 |
| `ane_S2_C1_G1` | 8 | 3210 / 12840 / 8 / 86–1501 / 0.490–0.973 / 83–1399 / 0 |
| `ane_S2_C1_G1` | 16 | 3210 / 25680 / 16 / 3–304 / 0.904–0.999 / 2–298 / 0 |
| `ane_S3_C1_G1` | 4 | 3210 / 6420 / 4 / 912–2158 / 0.116–0.703 / 872–2015 / 0 |
| `ane_S3_C1_G1` | 8 | 3210 / 12840 / 8 / 311–1477 / 0.313–0.898 / 295–1322 / 0 |
| `ane_S3_C1_G1` | 16 | 3210 / 25680 / 16 / 38–724 / 0.738–0.988 / 37–673 / 0 |
| `ane_S3_C1_G2` | 4 | 321 / 642 / 4 / 59–228 / 0.277–0.810 / 55–222 / 0 |
| `ane_S3_C1_G2` | 8 | 321 / 1284 / 8 / 15–163 / 0.480–0.953 / 13–158 / 0 |
| `ane_S3_C1_G2` | 16 | 321 / 2568 / 16 / 2–76 / 0.751–0.997 / 1–71 / 0 |
| `ane_S3_C1_G3` | 4 | 81 / 162 / 4 / 22–49 / 0.407–0.741 / 21–48 / 0 |
| `ane_S3_C1_G3` | 8 | 81 / 324 / 8 / 11–34 / 0.593–0.877 / 10–33 / 0 |
| `ane_S3_C1_G3` | 16 | 81 / 648 / 16 / 4–12 / 0.864–0.963 / 3–11 / 0 |

The matched-degree graphs are not near-connected in many cells. For example, sleep S3 G1 at k̄=4 has largest-component fraction `0.287–0.585` and up to 3,407 isolated nodes; anesthesia S3 G1 at k̄=4 has largest-component fraction `0.116–0.703` and up to 2,015 isolated nodes. All threshold tie-excess values were zero.

## OVERALL

`mixed MD-C / MD-D diagnostic result`.

The S3 grain reversal survives all three predeclared mean-degree regimes, weakening the simple fixed-density-induced mean-degree explanation. However, the graph family is severely fragmented for many cells, so this is not a clean connectivity-controlled replication. The control is informative as an alternative-explanation test, not as evidence that grain itself is causal.

### WHAT THIS CONTROL WEAKENS

- A simple K-only explanation of the grain reversal.
- A robust interpretation of the selected anesthesia G1 signal-axis reversal as independent of mean degree.

### WHAT IT DOES NOT RULE OUT

- Network-size and modularity finite-size effects.
- Disconnected-graph and fragmentation effects.
- Sparse signal/correlation suitability and zero inflation.
- Python-louvain versus MATLAB/BCT implementation differences.
- Any population-level, cross-animal or SRT-facing inference.

### NEXT HIGHEST-INFORMATION GATE

If separately authorized: a predeclared connectivity-/component-matched control or broader multi-animal replication. Neither was run here. Per the execution boundary, this control is now stopped.

## FILES AND INTEGRITY

- Runtime state: `.local/phase1_objectification/mean_degree_control/mean_degree_control_state.json`.
- Runtime per-cell records: `.local/phase1_objectification/mean_degree_control/*.json`.
- Author source commit: `90e1c7dc5823f9d413b1bddf5c649ec87d6598a3`.
- Dataset archive SHA-256: `dd29cf6adda2e04745834525a94122076152c31f5136acbc39b57d4a9013638c`.
- Integrity: 10/10 cells; 225/225 graphs/windows; 45,000/45,000 finite Q values; edge-count and achieved-degree checks PASS; all tie excess zero; log errors 0.
