---
id: SRT-NEURO-OBJECTIFICATION-MANUSCRIPT-OUTLINE-20260924
type: manuscript_outline
status: draft
version: v0_2_major_revision
record_stage: phase4_major_revision
date: 2026-09-24
layer: operations
epistemic_layer: experimental
claim_mode: report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, Manuscript, Outline, FigurePlan, ReviewResolution]
---

# Manuscript outline — stability of modularity inference across spatial grains

This is a manuscript architecture only. It contains no full manuscript prose
and authorizes no new computation. Its claim ceiling is defined in
`Paper/SRT_NEURO_OBJECTIFICATION_MANUSCRIPT_CLAIM_FREEZE_2026-09-24.md` and the
review-resolution audit.

## Working title

**A stability audit of state-dependent modularity across spatial grains in
cellular-resolution neural networks**

## Narrative spine

### R1 — Source calibration and pipeline provenance

- Identify the pinned source, released data, result files and runtime path.
- Report Phase 0 R0A/R0B at the released-result and qualitative level.
- State `R0-PARTIAL`: native MATLAB was unavailable and the Octave/Q
  compatibility check showed material differences in part of the spot-check.
- Treat this as source calibration, not exact native-script replication.

Owners: Phase 0 result records.

### R2 — Primary cellular matrix

- Define the analysis pipeline: signal → cell inclusion → spatial grain → graph
  → Q/max-Q → state contrast.
- Show the source-recording S1/S2/S3 × G1/G2/G3 matrix for Sleep and Anesthesia.
- Keep the `±0.01` band as a descriptive class rule, not an uncertainty or
  significance threshold.
- Make clear that windows are not biological replicates.

Owner: Phase 1 preregistration/result.

### R3 — Exploratory single-source diagnostics

- Present density, degree and selected connected-graph checks as exploratory
  diagnostics.
- State what each named check weakens and what it does not control.
- Keep graph fragmentation, finite-size differences and implementation limits in
  the same panel or supplement.
- Do not place these controls in the primary claim sentence.

Owners: Phase 1 density, mean-degree and connected-graph records.

### R4 — RIKEN multi-recording extension

- Use animal as the biological unit and show sessions nested within animal.
- Report G1 effect, G3 effect, paired G3−G1 shift and categorical recording
  reversals separately.
- Show the animal-level means, medians and bootstrap intervals.
- Describe the stage as a multi-recording extension: the Phase 1 source lineage
  overlaps the Phase 2 `mouse05` recordings by animal label and state-frame
  structure, although the materialized MAT files differ in ROI shape and hash.

Owner: multi-recording preregistration/result and review audit.

### R5 — Hamburg external stress test

- Separate object/metadata availability from interpretability of the outcome.
- Analyze only the frozen Wake–Isoflurane Anesthesia contrast.
- Show 39 Awake and 49 Isoflurane recordings from seven animals, nested at the
  animal level.
- Show per-recording accepted ROI/node counts and the condition-linked G1
  imbalance before any Q contrast interpretation.
- Include the existing-Q diagnostic regression as a limitation analysis, not a
  confirmatory correction.
- Label the outcome: directionally compatible but inconclusive external stress
  test; not clean external replication.

Owners: Hamburg availability/preregistration/result and review audit.

### R6 — Representation and transformation decomposition

- Define R0 full cellular representation, R1 N-only transformation, R2 random
  aggregation and R3 spatial aggregation.
- Report R0/R1/R2/R3 distributions and C1 finite-size/max-Q, C2 aggregation,
  C3 spatial and C4 total differences.
- Report the RIKEN animal×grain table directly; do not use a dataset-level
  transformation label as the result.
- Emphasize that C1 is major and consistently negative in the eight RIKEN cells,
  while C2/C3/C4 remain heterogeneous.

Owner: Phase 3C result and review-resolution audit.

### R7 — Synthetic finite-size/max-Q calibration

- Treat the synthetic matrix as auxiliary calibration, not biological data.
- Show planted versus estimated contrast, estimated/planted ratio, mean bias,
  sign-error rate and substantive reversal rate for all nine cells.
- State the maximum sign-error rate (`0.53`) separately from the maximum
  substantive reversal rate (`0.06`).
- State that large planted effects are also attenuated.
- State that the calibration covers connected RIKEN-like `k-bar=16`, not Hamburg
  `k-bar=4`.

Owner: Phase 3C result and compute amendments.

### R8 — Synthesis and limitations

- Conclude that spatial coarse-graining materially changes the measured
  state-dependent modularity contrast under the tested pipelines.
- Describe finite-size/max-Q as a major contribution and aggregation/spatial
  terms as heterogeneous contributors.
- Present the Hamburg result as a limitation-aware external stress test.
- Describe the programme as sequentially preregistered and adaptive across
  stage-local freezes.
- End with the distinction between methodological inference stability and any
  biological or causal interpretation.

## Structured abstract skeleton

1. **Background** — State-dependent modularity contrasts depend on declared
   signals, nodes, grains and graph construction.
2. **Question** — Test whether the estimated contrast is stable across spatial
   grains in cellular-resolution recordings.
3. **Approach** — Source calibration; RIKEN primary matrix and multi-recording
   extension; exploratory density/degree/connectivity diagnostics; Hamburg CA1
   Anesthesia stress test; R0–R3 decomposition; synthetic finite-size/max-Q
   calibration.
4. **Primary result** — Spatial coarse-graining changes the contrast; RIKEN
   fine-grain effects are attenuated toward weaker and heterogeneous coarse-grain
   summaries.
5. **Decomposition** — Finite-size/max-Q is major; aggregation and spatial terms
   vary by animal and grain.
6. **External stress test** — Hamburg is directionally compatible but
   inconclusive because condition-linked ROI/node counts limit interpretation.
7. **Limitations** — Window-level variance is sometimes not estimable; the
   synthetic calibration is model- and degree-regime-specific; conditions are
   not same-session paired in Hamburg.
8. **Conclusion** — The tested modularity inference is transformation-sensitive;
   no causal mechanism is identified.

## Minimal figure architecture

### Figure 1 — Analysis pipeline and nesting

Recording → signal → cell inclusion → spatial grain → graph → Q/max-Q → state
contrast, with windows and recordings nested in animals where applicable.

Supplement: source/runtime provenance and Phase 0 gate.

### Figure 2 — RIKEN primary matrix and uncertainty boundary

- Sleep and Anesthesia `DeltaQ` across S1/S2/S3 × G1/G2/G3.
- Descriptive `±0.01` bands.
- Window counts, non-estimable state cells and a note that the band is not a
  formal uncertainty threshold.

Supplement: full window-level Q values and recording×grain SE table.

### Figure 3 — Exploratory diagnostics and RIKEN extension

- Selected density, degree and connected-graph diagnostics clearly marked
  exploratory.
- Animal-level RIKEN G1/G3 paired shifts and bootstrap intervals.
- Separate display of G1 effect, G3 effect, paired shift and categorical
  reversals.

Supplement: fragmentation diagnostics and all selected control cells.

### Figure 4 — Hamburg stress test and node-count limitation

- Seven-animal Awake–Isoflurane recording trajectories.
- Per-recording accepted ROI/node counts by condition.
- Unadjusted and existing-Q diagnostic adjusted coefficients with intervals.
- Explicit label: directionally compatible but inconclusive external stress test.

Supplement: per-recording metadata, group-size statistics and the uncompleted
Sleep state-recovery gate.

### Figure 5 — R0–R3 decomposition

- R0 full, R1 N-only, R2 random aggregation and R3 spatial aggregation.
- C1–C4 distributions for RIKEN and Hamburg.
- Raw distributions and contribution magnitudes; no dataset-level T-D headline.

Supplement: transformation membership hashes, saved distributions and seeds.

### Figure 6 — Synthetic finite-size/max-Q calibration

- Planted versus estimated contrast across all nine cells.
- Estimated/planted ratio and bias.
- Separate sign-error and substantive-reversal panels.
- Degree-regime annotation: RIKEN-like `k-bar=16`, not Hamburg `k-bar=4`.

Supplement: all 900 replicates, seeds and checkpoint manifest.

## Tables

1. Evidence ledger with owner, biological unit, stage-local freeze and claim
   status.
2. RIKEN recording and animal summaries, including estimable/non-estimable
   window uncertainty.
3. Hamburg eligibility, node-count imbalance, adaptation and diagnostic model.
4. R0–R3 and C1–C4 decomposition values.
5. Synthetic planted/estimated, bias, sign-error and substantive-reversal
   calibration.
6. Claim ladder: safe, exploratory, limitation-aware and prohibited wording.

## Neighbor and novelty boundary

The manuscript must acknowledge established work on Hamburg CA1 network
analysis, graph-size/degree comparability, node/parcellation choice,
modularity degeneracy and resolution limits, many-analysts variability, and
scale/zoning aggregation analogues. The residual contribution is the combined
stability-audit workflow and provenance record, not the generic proposition that
analytical choices can matter.

## Supplementary material boundary

Supplementary material may contain full Q tables, graph diagnostics, runtime and
seed records, control-cell outputs, Hamburg object inventories, node-count CSVs,
diagnostic regression details and the synthetic checkpoint manifest. It must not
silently promote exploratory controls or diagnostic regressions to primary
outcomes.

## Manuscript stop boundary

This outline is a major-revision draft, not a full manuscript. Do not start
Hamburg Sleep, add a metric family, run a new graph or robustness control,
promote a theory claim, or call the Hamburg result clean external replication.
The next authorized stage is a second independent review of this outline and the
claim boundary.
