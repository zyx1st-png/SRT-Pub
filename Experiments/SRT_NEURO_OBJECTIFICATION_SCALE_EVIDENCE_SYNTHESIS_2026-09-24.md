---
id: SRT-NEURO-OBJECTIFICATION-SCALE-EVIDENCE-SYNTHESIS-20260924
type: evidence_synthesis
status: frozen
version: v0_1
record_stage: phase4_evidence_synthesis_claim_freeze
date: 2026-09-24
layer: operations
epistemic_layer: experimental
claim_mode: report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, EvidenceSynthesis, ClaimFreeze, Objectification, Modularity, Reproducibility]
---

# Phase 4 — evidence synthesis and claim freeze

## 1. Freeze boundary

This record synthesizes the completed, repository-visible Phase 0–3C evidence.
It does not run a new experiment, calculate a new network outcome, inspect
Hamburg Sleep network data, add a signal/graph/metric family, revise a frozen
preregistration or result record, or promote an SRT/GRG claim.

The experiment history is preserved on:

```text
experiments/neuro-objectification-phase1-20260918
HEAD: 9592917ab740dd389c70de1a1609a35f131c500c
```

The present synthesis is on the independent branch:

```text
paper/neuro-objectification-synthesis-20260924
```

The preceding experiment branch was pushed before this branch was created.
The `.local/` runtime area and unrelated user files remain untracked and are
not part of this synthesis commit.

## 2. Chronological evidence ledger

The entries below use the actual repository owners, not a reconstructed
summary detached from the records. The status column is the manuscript-use
status, not a new statistical significance label.

| stage | evidence owner | dataset / biological unit | objectification dimension or control | result relevant to synthesis | manuscript use |
|---|---|---|---|---|---|
| Phase 0 R0A | `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_R0A_RESULT_2026-09-17.md` | released `mouse_data.zip`; source-released sleep/anesthesia result files | source result and Fig. 3/Fig. 7 qualitative reconstruction | R0A released-result inventory, numerical reconstruction, and qualitative directions passed; native source-script execution was not established | `SUPPORTED-WITH-QUALIFICATION` as source calibration |
| Phase 0 R0B | `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE0_R0B_RESULT_2026-09-17.md` | source-selected sleep mouse 5 and anesthesia mouse 2; 30 windows | pinned author preprocessing, Octave/BCT compatibility path, 200 max-Q trials | all four targets completed; source-level direction preserved; 16/30 Q differences exceeded `1e-4`; native MATLAB unavailable; verdict `R0-PARTIAL` | `SUPPORTED-WITH-QUALIFICATION`; never call native exact replication |
| Phase 1 preregistration/result | `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_PREREGISTRATION_2026-09-18.md`; `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_RESULT_2026-09-19.md` | one source recording for Sleep and one for Anesthesia; windows are not biological replicates | S1/S2/S3 × C1 × G1/G2/G3; fixed density `K=0.05`; 200 Python max-Q repeats | both Wake–NREM and Wake–Isoflurane matrices received the preregistered `DIRECTION-REVERSED` label | `SUPPORTED-WITH-QUALIFICATION`; primary discovery matrix is exploratory and recording-level |
| compute audit | embedded in `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_RESULT_2026-09-19.md` | one completed baseline graph | serial versus four-worker scheduler; fixed seeds | 200 repeats retained because 25/50/100 failed the all-window convergence gate; exact per-seed/max-Q equivalence; `3.796845x` speedup | method/provenance only |
| density control | `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_DENSITY_SENSITIVITY_2026-09-21.md` | same two source recordings | `K=0.02, 0.05, 0.10`; selected cells declared before execution | selected S3 G1/G3 grain reversal persisted across K; signal branches were less stable and sparse/disconnected regimes remained | `EXPLORATORY-SUPPORT`; weakens K-only explanation, not all graph explanations |
| mean-degree control | `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_MEAN_DEGREE_CONTROL_2026-09-21.md` | same source recordings | exact `k-bar=4,8,16` top-ranked graphs | S3 G1/G3 reversal persisted in both conditions across degree targets; graphs were severely fragmented in many cells | `EXPLORATORY-SUPPORT`; informative but not clean connectivity control |
| connected-graph control and BCT diagnostic | `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_CONNECTED_GRAPH_CONTROL_2026-09-21.md` | same source recordings; selected S3 cells | MST backbone plus ranked edges; `k-bar=8,16`; Octave/BCT cross-check | reversal persisted in all connected graphs in selected cells; BCT reproduced selected first-window direction; Q vectors are not exact-equivalent | `EXPLORATORY-SUPPORT`; weakens disconnectedness as a sufficient explanation |
| multi-recording preregistration/result | `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_MULTIRECORDING_PREREGISTRATION_2026-09-21.md`; `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_MULTIRECORDING_RESULT_2026-09-22.md` | RIKEN: 5 Sleep animals/6 sessions and 4 Anesthesia animals/4 sessions; animal is unit | S3, G1/G2/G3, connected `k-bar=16`, all eligible recordings | Sleep median animal grain shift `-0.086787`, negative in `4/5`; Anesthesia median `-0.042486`, negative in `3/4`; `MR-C` descriptive labels | `SUPPORTED-WITH-QUALIFICATION`; strongest RIKEN recurrence evidence |
| Hamburg availability audit | `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_AVAILABILITY_AUDIT_2026-09-22.md` | independent Hamburg CA1; 7 Anesthesia animals/189 recordings; 3 Natural Sleep animals/54 candidates | result-blind object, metadata, Suite2p geometry and state feasibility audit | complete Anesthesia objects; `spks.npy`, `iscell.npy`, `stat.npy`, `ops.npy`; Sleep state vector remained uncertain and was not analyzed | feasibility and external-lineage qualification only |
| Hamburg Anesthesia preregistration/result | `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_ANESTHESIA_PREREGISTRATION_2026-09-22.md`; `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_ANESTHESIA_RESULT_2026-09-23.md` | 7 animals; 39 Awake and 49 Isoflurane recordings; recordings nested in animal | adapted Suite2p `spks` + frozen smoothing; local G1/G2/G3; connected `k-bar=4`; one 300 s recording window | 4/7 animal grain shifts negative; 2/7 categorical grain reversals; mean shift `-0.030945`, median `-0.048709`; bootstrap interval crossed zero; `EX-C` descriptive label | `SUPPORTED-WITH-QUALIFICATION`; convergent but heterogeneous external support |
| Phase 3C preregistration/amendments/result | `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_PREREGISTRATION_2026-09-23.md`; `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_COMPUTE_AMENDMENT_2026-09-23.md`; `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_SYNTHETIC_COMPUTE_AMENDMENT_2026-09-23.md`; `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_RESULT_2026-09-24.md` | RIKEN 4 animals; Hamburg 7 animals/88 recordings; animal-level nesting | R0 full, R1 N-only, R2 random aggregation, R3 spatial aggregation; C1–C4; SBM calibration | both datasets classified `T-D`; C1 finite-size contributions were negative on average; RIKEN C2 positive and Hamburg C2 near zero; synthetic classification `FS-B` with max bias `0.209318` and max substantive reversal rate `0.060` | `SUPPORTED-WITH-QUALIFICATION`; finite-size and transformation caveat |

An earlier benchmark-specific independent content-review artifact was not found
among the tracked repository files or the reachable history under the expected
objectification/neuroscience names. This synthesis therefore does not cite an
unavailable review as evidence; its claim audit is itself explicitly recorded
below.

## 3. Primary claim audit and freeze

### 3.1 Candidate claim, clause by clause

Candidate:

> State-dependent modularity inference in cellular-resolution neural recordings
> is not invariant across spatial grain. Grain-dependent changes, including
> substantive sign reversals in some settings, recur across recordings and
> animals and receive heterogeneous support in an independent CA1 dataset.
> Controlled decomposition indicates that these effects cannot be uniformly
> attributed to node-count reduction, aggregation, or spatial organization
> alone.

| clause | audit | disposition |
|---|---|---|
| state-dependent modularity inference | The measured outcome is `DeltaQ` from Q, with max-Q Louvain as the window statistic. | retain, always name modularity/Q/max-Q context |
| not invariant across spatial grain | Phase 1 has positive and negative cells in both primary recording-level contrasts; RIKEN multi-recording G1/G3 shifts are predominantly negative; Hamburg is heterogeneous with an overall negative shift. | retain, bounded to tested pipelines and grains |
| substantive sign reversals in some settings | Directly supported by Phase 1, controls, selected RIKEN recordings and 2/7 Hamburg animal-level categorical reversals. | retain “some settings,” never “universal” |
| recur across recordings and animals | RIKEN has multiple independent recordings and animals; Hamburg has repeated recordings nested in seven animals. | retain, do not treat windows or recordings as independent animals |
| heterogeneous support in independent CA1 | Hamburg is independent in lab/brain-region/acquisition lineage, but is an adaptation and condition-level rather than same-session paired. | retain “heterogeneous convergent support,” with adaptation and pairing qualification |
| cannot be uniformly attributed to one transformation alone | Phase 3C gives dataset-level T-D classifications; C1–C3 are heterogeneous; synthetic FS-B makes finite-size/max-Q limitations substantive. | retain as a bounded decomposition result, not causal exclusion |

### 3.2 Frozen strongest defensible primary claim

> **Across the frozen cellular-recording pipelines tested, the direction of the
> modularity-based state contrast changed with spatial grain, recurred across
> multiple RIKEN animals, and showed heterogeneous convergent support in an
> independent Hamburg CA1 anesthesia dataset. Matched-degree and connected-graph
> controls weakened simple density/degree/disconnectedness explanations, while
> the Phase 3C decomposition showed that finite-size effects are substantive but
> not a uniform account: transformation contributions were heterogeneous and
> synthetic max-Q calibration attenuated weak effects and occasionally produced
> sign errors. This is a claim about the stability of a measured modularity
> inference under declared representations, not about consciousness, a causal
> neural mechanism, or SRT/GRG.**

This is the main-text ceiling. “Spatial grain destabilizes” is not used as the
title or as a causal verb. “Objectification causes reversal” is prohibited.

## 4. Secondary claim statuses

| ID | frozen claim | exact evidence owner | paper status | qualification |
|---|---|---|---|---|
| S1 | Direction changes are present in specific RIKEN primary cells and selected multi-recording/external animal settings, not universally in every animal or grain. | Phase 1 result; multi-recording result; Hamburg result | `SUPPORTED-WITH-QUALIFICATION` | report concrete cells/animals and heterogeneity |
| S2 | The tested density variation weakens a K-only explanation for the selected S3 G1/G3 reversal. | Phase 1 density sensitivity | `EXPLORATORY-SUPPORT` | post-primary selected cells; degree and connectivity were not simultaneously matched there |
| S3 | Mean-degree-matched controls weaken a simple fixed-density-induced degree-collapse explanation. | Phase 1 mean-degree control | `EXPLORATORY-SUPPORT` | severe fragmentation and finite-size differences remain |
| S4 | Connected-graph controls show that the selected reversal can occur without graph fragmentation. | Phase 1 connected-graph control and BCT diagnostic | `EXPLORATORY-SUPPORT` | this does not show that connectivity is irrelevant or that all cells are controlled |
| S5 | Finite-size effects are a substantive contributor and can strongly attenuate weak estimated effects under the frozen synthetic/max-Q procedure. | Phase 3C result, C1 and FS-B | `SUPPORTED-WITH-QUALIFICATION` | synthetic calibration is model-dependent; finite size is not a uniform explanation of empirical shifts |
| S6 | Aggregation effects are heterogeneous: RIKEN C2 is positive on average, whereas Hamburg C2 is near zero on average. | Phase 3C result | `SUPPORTED-WITH-QUALIFICATION` | descriptive decomposition, not a causal aggregation mechanism |
| S7 | Spatial organization contributes in some conditions/representations but has no universal direction across datasets and animals. | Phase 3C result, C3 distributions | `SUPPORTED-WITH-QUALIFICATION` | no causal mechanism claim |
| S8 | Hamburg provides convergent but heterogeneous external support for grain-dependent modularity instability. | Hamburg availability audit and Anesthesia result | `SUPPORTED-WITH-QUALIFICATION` | different CA1 dataset and preprocessing lineage; Awake/Isoflurane are condition-level, not same-session paired |

## 5. Historical wording reconciliation

Frozen experiment records are not edited. The following table controls how their
language is carried into a manuscript.

| historical wording or label | current status | why qualification is required | manuscript replacement |
|---|---|---|---|
| “The S3 grain reversal persists after controlling both mean degree and disconnectedness.” | Diagnostic result remains true for the selected connected graphs; it is not a universal artifact exclusion. | Mean-degree graphs were highly fragmented; connected controls used selected S3 cells and still leave network-size, sparsity, and implementation differences. | “In selected predeclared controls, the reversal persisted under matched degree and under a connected MST-backed graph; these controls weaken, but do not eliminate, simple degree or disconnectedness explanations.” |
| “The selected condition-level and S3 grain reversals persist across K.” | Valid for the selected density-control cells. | K variation does not match degree, component structure, or finite-size behavior; signal branches were less stable. | “The selected S3 G1/G3 contrast was not specific to `K=0.05`, although other signal/grain cells remained density-sensitive.” |
| `EX-C` / “external method replication/adaptation.” | Keep as the frozen local label and method description. | Hamburg has a different brain region, lab/acquisition lineage, smoothing/window adaptation, and non-paired condition recordings. | “Independent Hamburg CA1 data provided heterogeneous convergent external support under a declared adapted pipeline; this was not a numerical or same-session replication of Kiyooka.” |
| “robustness” or “robust reversal” labels attached to controls. | Use only for the tested diagnostic contrast, not for a global finding. | The primary outcome is Q/max-Q; Phase 0 is R0-PARTIAL; finite-size and synthetic calibration remain material. | “stability under the named control” or “reversal in the selected control cells.” |
| Literal searches for “grain reversal persists after controlling all artifacts,” “simple artifacts excluded,” and “robust reversal.” | No exact literal match was found in the tracked benchmark records. | Near-equivalent active wording can still invite the same overreading. | Apply the replacements above throughout any future manuscript prose without rewriting historical records. |

## 6. Phase 3C interpretation freeze

The final interpretation is:

> **Neither dataset supports a single universal decomposition in which finite-size
> reduction, generic aggregation, or spatial organization alone determines the
> observed grain-dependent state contrast.**

The narrative therefore shifts from “find the artifact responsible for the
reversal” to:

> **Objectification transformations interact with dataset, animal and grain
> context, and their inferential consequences must be reconstructed rather than
> assumed to be preserved.**

The neutral methodological term is **transformation-dependent inference
instability**. It is not “GRG transformation grammar.”

### Bounded inference equivalence

One methodological concept is retained only in a bounded form:

> Two representations are direction-equivalent for a declared biological
> contrast and declared outcome when they preserve the same qualitative effect
> direction under the frozen practical threshold.

This concept is useful for describing R0–R3 without pretending that numerical
equality is required. It does **not** mean:

```text
bounded inference equivalence != GRG generative equivalence
bounded inference equivalence != ontological equivalence
```

It belongs in Methods/Discussion or a supplement, not in the title or abstract
unless the manuscript needs it to explain the decomposition table.

## 7. Limitations frozen for all manuscript versions

- Modularity Q, with a 200-repeat Louvain/max-Q rule, remains the primary outcome.
- Max-Q and Louvain implementation dependence remain material; Phase 0 native MATLAB was unavailable and Octave differences were documented.
- Finite-size bias is substantive; the synthetic calibration is model-dependent and auxiliary.
- The transformation decomposition is heterogeneous and does not identify a causal mechanism.
- Hamburg support is heterogeneous, and Hamburg brain regions differ from RIKEN.
- Signal preprocessing is not identical across datasets; Hamburg `spks.npy` plus smoothing is the nearest analogue, not byte-for-byte S3 equivalence.
- Hamburg Awake/Isoflurane recordings are condition-level and nested within animal, not same-session paired observations.
- Windows, recordings, transformation repeats and Louvain trials are not interchangeable biological replicates; primary biological unit is animal where animal-level data exist.
- No claim is made about a consciousness mechanism, causal neural mechanism, SRT, GRG, Selection, generative reach, or ontology.
- No independent replication from a second cortical laboratory exists in this programme; Hamburg is an independent CA1 lineage, not a cortical replication.
- Hamburg Sleep network analysis was not completed because the state-recovery gate was not executable as a faithful frozen protocol.
- The Phase 3C schema-inspection deviation in which one Hamburg `q_max` was accidentally printed is retained in the result record; no RIKEN outcome or result-based decision was based on it. This is a provenance limitation, not a reason to rewrite the result.

## 8. Theory boundary: SRT / GRG

Allowed, non-canonical and hypothesis-generating only:

- The programme operationalizes objectification choices as empirical dimensions of inference.
- The results motivate future work on transformation-sensitive and reconstructible scientific representations.
- Phase 3C suggests that a simple one-transformation/one-effect grammar is inadequate for these data.

Not allowed:

```text
SRT validated
GRG validated
Selection evidenced
generative reach measured
generative equivalence established
ontology supported by a modularity result
```

Any GRG-facing sentence must be marked `non-canonical`,
`hypothesis-generating`, and `future-work`.

## 9. Strongest-neighbor boundary

The programme must not claim that the following are novel in themselves:

- analytical choices can change conclusions;
- spatial scale can change a network result;
- parcellation/resolution affects graph metrics;
- Kiyooka et al. already reported scale-dependent modularity behavior;
- coarse-graining can change a modularity contrast.

These are established neighboring ideas. Kiyooka et al.'s published abstract
already reports higher single-cell modularity during sleep/anesthesia and no
consistent mesoscale difference, so the present work is not a priority claim for
scale dependence itself ([PubMed record](https://pubmed.ncbi.nlm.nih.gov/41653913/)).
Network-neuroscience multiverse work explicitly treats preprocessing,
parcellation, connectivity estimation and graph modeling as decision points
whose combinations can affect inference ([Comet toolbox article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12892349/));
parcellation-related spatial error has also been studied for graph metrics
including modularity ([Spatial Stability of Functional Networks](https://pmc.ncbi.nlm.nih.gov/articles/PMC8894326/)).
The many-analysts literature likewise establishes that defensible analytic
decisions can produce different conclusions ([One data set, many analysts](https://pmc.ncbi.nlm.nih.gov/articles/PMC9971968/)).

The candidate increment is narrower and methodological:

1. a prospectively frozen inference-stability benchmark for a declared state contrast;
2. direction-level practical classification rather than a single winning pipeline;
3. sequential alternative-explanation tests for density, degree and connectivity;
4. multi-recording, animal-level recurrence with explicit nested hierarchy;
5. an independent experimental-lineage external test with declared adaptation;
6. an explicit R0–R3 transformation decomposition;
7. synthetic finite-size/max-Q calibration that qualifies interpretation;
8. provenance-preserving reconstruction of how a declared inference changes across representations.

This is a candidate methodological increment, not a priority claim. The paper
must cite the neighboring work and state the comparison explicitly.

## 10. Final claim ladder

### A. SAFE MAIN-TEXT CLAIMS

1. Under the frozen tested pipelines, state-dependent modularity inference was
   not invariant across spatial grain. Owner: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_RESULT_2026-09-19.md`.
2. The direction-changing pattern recurred across multiple RIKEN recordings and
   animals under the connected, mean-degree-matched primary multi-recording
   construction. Owner: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_MULTIRECORDING_RESULT_2026-09-22.md`.
3. Independent Hamburg CA1 Anesthesia data provided heterogeneous convergent
   support under an adapted, non-same-session-paired pipeline. Owner:
   `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_EXTERNAL_HAMBURG_ANESTHESIA_RESULT_2026-09-23.md`.
4. Density, degree and connected-graph controls weakened named simple
   explanations but did not isolate a causal grain mechanism. Owners:
   `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_DENSITY_SENSITIVITY_2026-09-21.md`,
   `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_MEAN_DEGREE_CONTROL_2026-09-21.md`, and
   `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PHASE1_CONNECTED_GRAPH_CONTROL_2026-09-21.md`.
5. Phase 3C found heterogeneous transformation contributions and no single
   universal finite-size/aggregation/spatial decomposition. Owner:
   `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_RESULT_2026-09-24.md`.

### B. SAFE DISCUSSION CLAIMS

1. The practical scientific object is a representation-to-inference pipeline,
   not a scale-free modularity fact. Owner: Phase 1 preregistration and result.
2. Finite-size and max-Q behavior are substantive interpretive constraints,
   not merely nuisance details. Owner: Phase 3C result.
3. A bounded inference-equivalence vocabulary can describe direction preservation
   without implying ontological or generative equivalence. Owner: Phase 3C
   preregistration/result.
4. Result-blind preregistration, control sequencing, animal-level nesting and
   provenance records are useful safeguards for this class of benchmark. Owners:
   Phase 1, multi-recording, Hamburg and Phase 3C preregistrations.

### C. EXPLORATORY / FUTURE CLAIMS

1. A transformation-sensitive representation grammar may be useful for future
   scientific workflows, but this programme does not validate GRG. Owner:
   Phase 3C result, non-canonical implication.
2. A complete external Sleep replication could test whether the same stability
   pattern extends to Hamburg natural sleep, after a separately frozen state
   recovery protocol. Owner: Hamburg availability audit and Sleep recovery gate.
3. Other association measures, matched-component designs, and cross-laboratory
   regions may distinguish biological from measurement-level sources of
   instability. No such result is available in this programme.

### D. PROHIBITED CLAIMS

```text
SRT is validated
GRG is validated
Selection is evidenced
Bearer or One is measured
consciousness is measured by the network result
a causal neural mechanism has been identified
objectification causes the reversal
finite size, aggregation, spatial organization, density, degree or
disconnectedness alone explains the observed pattern
the effect is universal or numerically replicated across datasets
the Hamburg result is a same-session or same-region replication of Kiyooka
Phase 0 is R0-PASS or native MATLAB replication
```

## 11. Files and non-actions

This synthesis is accompanied by:

```text
Paper/SRT_NEURO_OBJECTIFICATION_MANUSCRIPT_CLAIM_FREEZE_2026-09-24.md
Paper/SRT_NEURO_OBJECTIFICATION_MANUSCRIPT_OUTLINE_2026-09-24.md
```

No historical experiment record, preregistration, manifest, result JSON/CSV,
or source repository was modified. No new computation was started.
