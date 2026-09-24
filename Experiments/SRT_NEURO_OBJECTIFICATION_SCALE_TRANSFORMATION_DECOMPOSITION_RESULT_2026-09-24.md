---
id: SRT-NEURO-OBJECTIFICATION-SCALE-TRANSFORMATION-DECOMPOSITION-RESULT-20260924
type: experiment_result
status: frozen
version: v0_1
record_stage: phase3c_finite_size_objectification_transformation_result
date: 2026-09-24
layer: operations
epistemic_layer: experimental
claim_mode: report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, Objectification, Transformation, FiniteSize, Result]
---

# OBJECTIFICATION-TRANSFORMATION DECOMPOSITION

## Checkpoint repair

The legacy `primary_complete` flag was split into dataset-specific flags. Final empirical state is `RIKEN=true`, `Hamburg=true`, `empirical_primary=true`; 18,400 empirical units are complete. The original preregistration remains unchanged.

## RIKEN

RIKEN Anesthesia used 4 animals, k_bar=16, 800 new R1/R2 unit files, 50 transformation repeats, and 200 Louvain trials per window. Dataset-level diagnostic classification: **T-D**. Animal/grain labels: mouse03/G2=other, mouse03/G3=other, mouse05/G2=T-D, mouse05/G3=T-D, mouse06/G2=T-D, mouse06/G3=T-D, mouse07/G2=T-D, mouse07/G3=T-D.

## HAMBURG

Hamburg Anesthesia used 7 animals and 88 recordings (39 Awake, 49 Isoflurane), k_bar=4, 17,600 new R1/R2 unit files, 50 transformation repeats, and 200 Louvain trials per window. Dataset-level diagnostic classification: **T-D**. Animal/grain labels: 37527/G2=T-D, 37527/G3=T-D, 37528/G2=T-D, 37528/G3=T-D, 37529/G2=T-D, 37529/G3=T-D, 37530/G2=T-D, 37530/G3=T-D, 48/G2=T-D, 48/G3=T-D, 51/G2=other, 51/G3=other, 53/G2=T-D, 53/G3=T-D.

## Transformation contrasts

Values below summarize all transformation values and the mean of animal-level medians; transformation repeats are not biological n.

| dataset | contrast | all-value median | animal-median mean | animal-median range |
|---|---|---:|---:|---:|
| hamburg | C1_finite_size | -0.042397 | -0.026710 | [-0.097772, 0.090272] |
| hamburg | C2_aggregation | -0.001327 | -0.002518 | [-0.044298, 0.022977] |
| hamburg | C3_spatial_organization | -0.010131 | -0.009157 | [-0.047421, 0.021422] |
| hamburg | C4_total_objectification | -0.057229 | -0.037844 | [-0.151603, 0.084336] |
| riken | C1_finite_size | -0.116683 | -0.115470 | [-0.208297, -0.019914] |
| riken | C2_aggregation | 0.071174 | 0.099004 | [0.040795, 0.342052] |
| riken | C3_spatial_organization | -0.029034 | -0.032112 | [-0.167775, 0.107757] |
| riken | C4_total_objectification | -0.038811 | -0.046981 | [-0.297895, 0.135939] |

## Animal-level transformation distributions

The following table reports the result-blindly defined state bands after completion. `negative` means DeltaQ < -0.01, `null` is [-0.01,+0.01], and `positive` means DeltaQ > +0.01. R1/R2 probabilities are within-animal transformation-repeat probabilities.

| dataset | animal | grain | R0 | R1 | R2 | R3 | P(R1 negative) | P(R2 negative) | P(R1 reversal) | P(R2 reversal) | label |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---|
| hamburg | 37527 | G2 | positive | variable | variable | positive | 0.000 | 0.060 | 0.000 | 0.060 | T-D |
| hamburg | 37527 | G3 | positive | variable | variable | null | 0.000 | 0.120 | 0.000 | 0.120 | T-D |
| hamburg | 37528 | G2 | negative | variable | variable | positive | 0.080 | 0.200 | 0.780 | 0.340 | T-D |
| hamburg | 37528 | G3 | negative | variable | variable | null | 0.060 | 0.200 | 0.800 | 0.440 | T-D |
| hamburg | 37529 | G2 | positive | variable | variable | negative | 0.640 | 0.480 | 0.640 | 0.480 | T-D |
| hamburg | 37529 | G3 | positive | variable | variable | negative | 0.640 | 0.220 | 0.640 | 0.220 | T-D |
| hamburg | 37530 | G2 | negative | variable | variable | negative | 0.980 | 0.660 | 0.000 | 0.040 | T-D |
| hamburg | 37530 | G3 | negative | variable | variable | null | 0.620 | 0.320 | 0.120 | 0.260 | T-D |
| hamburg | 48 | G2 | positive | variable | variable | null | 0.060 | 0.000 | 0.060 | 0.000 | T-D |
| hamburg | 48 | G3 | positive | variable | variable | positive | 0.220 | 0.040 | 0.220 | 0.040 | T-D |
| hamburg | 51 | G2 | null | negative | negative | negative | 1.000 | 1.000 | NA | NA | other |
| hamburg | 51 | G3 | null | negative | negative | negative | 1.000 | 1.000 | NA | NA | other |
| hamburg | 53 | G2 | positive | variable | variable | null | 0.440 | 0.580 | 0.440 | 0.580 | T-D |
| hamburg | 53 | G3 | positive | variable | variable | positive | 0.320 | 0.040 | 0.320 | 0.040 | T-D |
| riken | mouse03 | G2 | negative | negative | positive | positive | 1.000 | 0.000 | 0.000 | 1.000 | other |
| riken | mouse03 | G3 | negative | negative | positive | positive | 1.000 | 0.000 | 0.000 | 1.000 | other |
| riken | mouse05 | G2 | null | variable | variable | positive | 0.620 | 0.000 | NA | NA | T-D |
| riken | mouse05 | G3 | null | negative | variable | negative | 1.000 | 0.320 | NA | NA | T-D |
| riken | mouse06 | G2 | positive | variable | positive | negative | 0.040 | 0.000 | 0.040 | 0.000 | T-D |
| riken | mouse06 | G3 | positive | negative | variable | negative | 1.000 | 0.020 | 1.000 | 0.020 | T-D |
| riken | mouse07 | G2 | positive | variable | positive | positive | 0.000 | 0.000 | 0.000 | 0.000 | T-D |
| riken | mouse07 | G3 | positive | negative | variable | positive | 1.000 | 0.040 | 1.000 | 0.040 | T-D |

## Synthetic finite-size calibration

The result-blind synthetic compute amendment changed the design to 100 paired replicates per cell (9 cells, 900 total) and retained uniform R*=200 Louvain repeats. The convergence audit could not certify 25/50/100 because historical unit files did not retain per-seed Q; no unsupported optimizer reduction was made.

| N regime | N | effect | n | mean estimated DeltaQ | mean planted DeltaQ | mean bias | sign-error rate | substantive reversal rate |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| large | 5943 | large | 100 | 0.028519 | 0.237838 | -0.209318 | 0.000 | 0.000 |
| large | 5943 | medium | 100 | 0.000417 | 0.121003 | -0.120585 | 0.420 | 0.000 |
| large | 5943 | small | 100 | -0.000038 | 0.035849 | -0.035888 | 0.530 | 0.000 |
| medium | 595 | large | 100 | 0.092818 | 0.239597 | -0.146779 | 0.000 | 0.000 |
| medium | 595 | medium | 100 | 0.003759 | 0.122316 | -0.118557 | 0.150 | 0.000 |
| medium | 595 | small | 100 | 0.001283 | 0.035276 | -0.033993 | 0.330 | 0.000 |
| small | 149 | large | 100 | 0.102097 | 0.236181 | -0.134083 | 0.000 | 0.000 |
| small | 149 | medium | 100 | 0.011958 | 0.120484 | -0.108526 | 0.090 | 0.010 |
| small | 149 | small | 100 | 0.001962 | 0.036978 | -0.035015 | 0.420 | 0.060 |

Synthetic classification: **FS-B**. Maximum cell substantive-reversal rate: 0.060; maximum absolute cell mean bias: 0.209318.

## Bounded inference equivalence

Neither dataset supports a single uniform transformation-preserving relation across all animals and grains. Both are therefore classified T-D at the dataset level. RIKEN shows a negative finite-size contribution, a positive aggregation contribution, and a negative spatial-organization contribution on average. Hamburg shows a negative finite-size contribution, a near-zero aggregation contribution, and a negative spatial-organization contribution on average. These are bounded methodological descriptions, not generative or ontological equivalence claims.

## What this rules down

The empirical decomposition does not support attributing the observed grain-dependent shift to finite-size reduction alone, random aggregation alone, or spatial organization alone across both datasets. The synthetic calibration additionally shows that max-Q estimation can attenuate weak positive planted effects and can produce sign errors under the frozen graph/Louvain procedure; this is a calibration result, not a correction of the empirical outcomes.

## What remains

The result does not establish cross-dataset numerical replication, causal mechanism, biological consciousness state, SRT, GRG, or any ontology-level claim. It does not authorize Hamburg Sleep, a new network metric, matched-component analysis, or another robustness programme.

## Paper implication

Present the finding as a finite-size and representation-transformation sensitivity result. Report R0–R3 and C1–C4 separately, preserve animal-level nesting, and treat synthetic calibration as an auxiliary estimate of optimizer/finite-size limitations.

## GRG-facing non-canonical implication

Objectification changes may be treated as explicit transformations whose inferential consequences can preserve, attenuate, or break a bounded inference relation. This is not GRG generative equivalence and does not validate SRT.

## Files

- Preregistration: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_PREREGISTRATION_2026-09-23.md` (8ba4d5fe)
- Transformation compute amendment: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_COMPUTE_AMENDMENT_2026-09-23.md` (ef51dc82)
- Synthetic compute amendment: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_SYNTHETIC_COMPUTE_AMENDMENT_2026-09-23.md` (ef9eacfe)
- JSON result: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_RESULT_2026-09-24.json`
- Animal CSV: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_ANIMAL_RESULTS_2026-09-24.csv`
- Transformation distributions CSV: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_TRANSFORMATION_DISTRIBUTIONS_2026-09-24.csv`
- Synthetic summary CSV: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_SYNTHETIC_SUMMARY_2026-09-24.csv`

## Checks

- RIKEN units: 800/800; Hamburg units: 17,600/17,600; total: 18,400/18,400.
- All generated graphs were validated connected with zero isolated nodes and exact frozen edge count; all 200 Q trials were finite.
- R1/R2 membership rules, target node counts, group-size hashes and seed reconstruction metadata were retained; no result-based exclusion was used.
- Synthetic: 900/900 unit files, 9 cells × 100 replicates, uniform 200 Louvain repeats.
- Frontmatter check exited 0; runtime-only data remains under `.local/phase3c_transformation/` and is not added to Git.
- Process deviation retained: one Hamburg `q_max` was accidentally printed during early schema inspection; no RIKEN outcome or result-driven decision was made.

## Commits

- Working branch: `experiments/neuro-objectification-phase1-20260918`.
- Phase 3C preregistration: `8ba4d5fe`.
- Transformation compute amendment: `ef51dc82`.
- Synthetic compute amendment: `ef9eacfe`.

## Next

STOP robustness expansion → synthesis / claim freeze → manuscript v1
