---
id: SRT-NEURO-OBJECTIFICATION-MANUSCRIPT-OUTLINE-20260924
type: manuscript_outline
status: frozen
version: v0_1
record_stage: phase4_outline_and_figure_plan
date: 2026-09-24
layer: operations
epistemic_layer: experimental
claim_mode: report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, Manuscript, Outline, FigurePlan, ClaimFreeze]
---

# Manuscript outline — neuro objectification scale benchmark

This is a manuscript architecture only. It contains no full manuscript prose
and does not authorize new computation. The claim ceiling is defined in
`Paper/SRT_NEURO_OBJECTIFICATION_MANUSCRIPT_CLAIM_FREEZE_2026-09-24.md`.

## Working title

**State-dependent modularity inference is not invariant across spatial grain in
cellular-resolution neural networks**

The title is deliberately methodological. It does not claim that spatial grain
causes an effect, that all recordings reverse, or that the result validates a
theory of consciousness.

## Narrative spine

### R1 — Source calibration compatibility

- State the locked author source, released result reconstruction and data/code
  provenance.
- Report R0A as reproduced at the released-result/qualitative level.
- Report R0B as `R0-PARTIAL`: all four recalculations completed, but native MATLAB
  was unavailable and Octave Q differences were material in part of the spot-check.
- Do not present this as native exact source replication.

Owners: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_R0A_RESULT_2026-09-17.md`,
`Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_R0B_RESULT_2026-09-17.md`.

### R2 — Preregistered matrix reveals instability

- Introduce the source-recording benchmark and its fixed signal/grain matrix.
- Show the Wake–NREM and Wake–Isoflurane `DeltaQ` matrices.
- State that both received the local `DIRECTION-REVERSED` label.
- Keep the one-recording-per-condition and no-population-inference boundary visible.

Owner: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_RESULT_2026-09-19.md`.

### R3 — Sequential controls weaken single-artifact explanations

- Density: selected S3 G1/G3 reversal persists across `K=0.02, 0.05, 0.10`,
  while signal branches are not uniformly stable.
- Mean degree: selected S3 grain reversal persists at `k-bar=4,8,16`, with a
  prominent fragmentation warning.
- Connectivity: selected S3 reversal persists in connected MST-backed graphs;
  BCT reproduces selected qualitative directions.
- Wording: “weakens simple explanations,” never “all artifacts excluded.”

Owners: density, mean-degree and connected-graph control records dated
2026-09-21.

### R4 — Multi-recording/animal recurrence

- Move the biological unit from source recording to animal-level nested summaries.
- Show recording-level G1/G2/G3 trajectories and animal-level paired grain shifts.
- Report Sleep `4/5` negative animal shifts and Anesthesia `3/4`, with concrete
  medians and intervals as descriptive summaries.
- Do not treat sessions, windows or Louvain trials as animals.

Owner: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_MULTIRECORDING_RESULT_2026-09-22.md`.

### R5 — Independent Hamburg CA1 external validation

- Separate feasibility from result: processed objects and geometry were available;
  Sleep state recovery remained blocked.
- Analyze only the frozen Wake–Isoflurane anesthesia contrast.
- Show seven animal trajectories, 39 Awake and 49 Isoflurane recordings, and
  heterogeneous support: 4/7 negative grain shifts and 2/7 categorical reversals.
- Explain that this is an independent CA1 experimental lineage and a declared
  adaptation, not numerical or same-session replication.

Owners: Hamburg availability audit, anesthesia preregistration and result dated
2026-09-22/23.

### R6 — R0–R3 transformation decomposition

- Define R0 full single-neuron, R1 N-only, R2 random aggregation and R3 spatial
  aggregation.
- Report C1 finite size, C2 aggregation, C3 spatial organization and C4 total
  shifts separately for RIKEN and Hamburg.
- Freeze T-D at dataset level for both datasets.
- Explain that the decomposition is heterogeneous and does not identify a causal
  mechanism or a single artifact.

Owner: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_RESULT_2026-09-24.md`.

### R7 — Synthetic finite-size/max-Q calibration and synthesis

- Report the degree-controlled SBM calibration as auxiliary, not biological data.
- State `FS-B`, 100 replicates per cell, 200 Louvain repeats, maximum absolute
  cell bias `0.209318`, and maximum substantive reversal rate `0.060`.
- Explain that weak effects can be attenuated or sign-misclassified under the
  frozen max-Q procedure, qualifying rather than erasing empirical results.
- End with transformation-dependent inference instability and the limitations.

Owner: Phase 3C result and its two result-blind compute amendments.

## Structured abstract skeleton

Use the following headings in a future abstract draft. The claim freeze file
contains the sentence-level map.

1. **Background** — Modularity-based state inference may depend on declared
   representation and spatial grain.
2. **Gap** — Need an explicit stability benchmark that records direction changes,
   control sequence, animal nesting and representation transformations.
3. **Approach** — Frozen source calibration; RIKEN primary/multi-recording matrix;
   density, degree and connectivity diagnostics; Hamburg CA1 anesthesia adaptation;
   R0–R3 decomposition and synthetic calibration.
4. **Primary result** — Direction-dependent modularity contrast changes across
   grain, recurs in RIKEN animals and has heterogeneous Hamburg support.
5. **Controls** — Named controls weaken simple density/degree/disconnectedness
   accounts without establishing a causal grain effect.
6. **External validation** — Hamburg is independent-lineage CA1 evidence under
   an adapted, non-same-session-paired protocol; Sleep was not analyzed.
7. **Decomposition** — No universal finite-size/aggregation/spatial component
   explains both datasets.
8. **Calibration caveat** — Max-Q/finite-size effects attenuate weak synthetic
   effects and can occasionally reverse estimated direction.
9. **Conclusion** — Tested modularity inference is transformation-sensitive;
   no consciousness, mechanism, SRT or GRG claim follows.

## Minimal figure architecture

### Figure 1 — Benchmark and objectification framework

Main elements:

- recording → signal → cell inclusion → grain → graph → Q/max-Q → state contrast;
- explicit nesting: windows/recordings within animals;
- predeclared practical direction bands and result-blind sequence.

Supplement candidate: full source/code/data provenance and R0 gate.

### Figure 2 — Primary RIKEN objectification matrix

Main elements:

- Sleep and Anesthesia `DeltaQ` across S1/S2/S3 × G1/G2/G3;
- practical null band and direction-reversed cells;
- no inferential population bars for the single-recording primary matrix.

Supplement candidate: every window-level Q and all 200-trial diagnostics.

### Figure 3 — Degree, connectivity and multi-recording controls

Main elements:

- selected S3 G1/G3 trajectories across K and matched degree;
- connected-graph control with graph-invariant inset;
- animal-level RIKEN multi-recording paired grain shifts.

Supplement candidate: full fragmentation diagnostics and BCT Q comparison.

### Figure 4 — Hamburg external validation

Main elements:

- seven-animal Awake–Isoflurane trajectories;
- G1/G2/G3 condition contrasts and grain shifts;
- explicit label: independent CA1, adapted pipeline, condition-level recordings.

Supplement candidate: object inventory, Suite2p fields, eligibility and the
unexecuted Sleep state-recovery gate.

### Figure 5 — R0–R3 transformation decomposition

Main elements:

- R0 full, R1 N-only, R2 random aggregation, R3 spatial aggregation;
- C1–C4 distributions at animal level for RIKEN and Hamburg;
- T-D labels shown as descriptive heterogeneity, not a causal pathway.

Supplement candidate: transformation membership hashes and repeat distributions.

### Figure 6 — Synthetic finite-size calibration and synthesis

Main elements:

- planted versus estimated `DeltaQ` by N/effect cell;
- bias and sign-error/reversal calibration;
- final synthesis panel separating empirical evidence, controls, external support
  and limitations.

Supplement candidate: all nine cells, 100 replicates each, seed and checkpoint
manifest.

## Tables

1. Evidence ledger with exact owner, biological unit, result status and remaining
   alternative explanation.
2. RIKEN primary and multi-recording numerical summaries.
3. Hamburg eligibility, adaptation and animal-level results.
4. Phase 3C C1–C4 and synthetic FS-B calibration.
5. Claim ladder: safe main text, discussion, exploratory/future, prohibited.

## Supplementary material boundary

Supplementary material may contain full window-level Q values, graph diagnostics,
runtime/version records, seed manifests, BCT cross-check details, all density and
degree cells, Hamburg object inventory, and the protocol deviation. It must not
silently promote these diagnostics to new primary outcomes.

## Manuscript stop boundary

This outline is the final Phase 4 deliverable. Do not automatically run Hamburg
Sleep, add a metric family, amend old records, promote GRG concepts, or write the
full manuscript. The next authorized stage is a separately reviewed manuscript
v1 using this claim freeze.
