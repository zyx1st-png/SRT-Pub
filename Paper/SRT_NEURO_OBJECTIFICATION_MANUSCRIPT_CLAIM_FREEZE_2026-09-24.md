---
id: SRT-NEURO-OBJECTIFICATION-MANUSCRIPT-CLAIM-FREEZE-20260924
type: manuscript_claim_freeze
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
tags: [Neuroscience, Manuscript, ClaimFreeze, ReviewResolution, Modularity]
---

# Manuscript claim boundary after PR #1051 review

## Scope

This is a major-revision claim boundary for a future manuscript. It is derived
from the review-resolution audit:

`Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PR1051_REVIEW_RESOLUTION_AUDIT_2026-09-24.md`.

It does not alter frozen experiment records, authorize new computation, or
constitute full manuscript prose. The status is `draft` pending a second
independent review.

## Revised primary claim

> **Across the tested cellular-resolution datasets, spatial coarse-graining
> materially altered the estimated state-dependent modularity contrast. In the
> RIKEN recording extension, this was characterized primarily by attenuation from
> positive fine-grain contrasts toward weaker and heterogeneous coarse-grain
> estimates. Finite-size/max-Q effects were a major contributor, while
> aggregation and spatial grouping introduced additional heterogeneous changes.
> The Hamburg Anesthesia stress test was limited by condition-linked differences
> in recorded cell counts and therefore does not constitute clean external
> replication.**

This is a methodological claim about the stability of a measured modularity
contrast under declared representations. It does not identify a causal neural
mechanism or measure consciousness.

## Clause guards

| clause | allowed meaning | forbidden upgrade |
|---|---|---|
| tested cellular-resolution datasets | the named RIKEN extension and Hamburg Anesthesia stress test | all neural recordings or all graph analyses |
| materially altered | saved DeltaQ changes across declared grain/representation operations | spatial grain is itself a biological cause |
| RIKEN recording extension | multi-recording continuation with source-lineage overlap documented | fully independent replication of Phase 1 |
| attenuation from positive fine-grain contrasts | animal-level RIKEN summaries and heterogeneous recording-level results | every animal or every recording attenuates |
| finite-size/max-Q major contributor | C1 negative in all 8 RIKEN animal×grain cells; synthetic bias is material | finite size alone explains the empirical pattern |
| heterogeneous aggregation/spatial changes | C2/C3 distributions vary by animal and grain | a unique causal aggregation or spatial mechanism |
| Hamburg stress test | independent experimental lineage, adapted pipeline, condition-level recordings | clean external replication or same-session pairing |

## Secondary claim ledger

| ID | status | permitted wording | owner / limitation |
|---|---|---|---|
| S1 | `SUPPORTED-WITH-QUALIFICATION` | RIKEN animal-level G3−G1 shifts are negative in 4/5 Sleep and 3/4 Anesthesia animals, with heterogeneous recording signs. | multi-recording result; windows are not animals; Phase 1 lineage overlap |
| S2 | `EXPLORATORY` | selected S3 G1/G3 diagnostic contrast was not specific to the tested density values. | single-source selected cells; not a global K control |
| S3 | `EXPLORATORY` | selected matched-degree diagnostics weaken a simple degree-collapse explanation. | fragmentation and finite-size differences remain |
| S4 | `EXPLORATORY` | selected connected MST-backed diagnostics show the contrast can occur without graph fragmentation. | does not exclude other graph differences |
| S5 | `SUPPORTED-WITH-QUALIFICATION` | finite-size/max-Q effects are material and can strongly attenuate estimates. | synthetic calibration is model-dependent; k-bar=16 only |
| S6 | `SUPPORTED-WITH-QUALIFICATION` | C2 aggregation and C3 spatial contributions are heterogeneous. | raw distributions, not T-D headline labels |
| S7 | `INCONCLUSIVE-EXTERNAL` | Hamburg is directionally compatible but not cleanly interpretable as external replication. | condition-linked G1 N imbalance; adjusted diagnostic coefficient is not causal |
| S8 | `PROVENANCE-QUALIFICATION` | the programme is sequentially preregistered and adaptive across stage-local freezes. | not one globally frozen pipeline |

## Label policy

`MR-C` is not a manuscript claim. The result record's operational rule was
supplied after the complete multi-recording result rather than fully formalized
in the preregistration.

`T-D` is not a manuscript dataset-level finding. The Phase 3C prose names a
variable pattern, but the implementation calls a distribution `variable` when
it is not confined to one sign band, and the dataset aggregation removes
`other` labels before selecting a single label. The manuscript reports
R0/R1/R2/R3 and C1/C2/C3/C4 distributions directly.

## Title

> **A stability audit of state-dependent modularity across spatial grains in
> cellular-resolution neural networks**

The title is methodological and does not imply a biological causal effect.

## Abstract skeleton

**Background:** Modularity-based state contrasts can depend on how cellular
recordings are represented as signals, nodes and graphs.

**Question:** Do declared spatial-grain transformations preserve the estimated
state-dependent modularity contrast in a cellular-resolution benchmark?

**Approach:** We completed a source-calibration gate, a result-blind RIKEN
recording matrix and multi-recording extension, selected density/degree/
connectivity diagnostics, an adapted Hamburg CA1 Anesthesia stress test, and an
R0–R3 transformation decomposition with synthetic finite-size/max-Q calibration.

**Primary result:** Spatial coarse-graining materially changed the estimated
contrast. RIKEN animal summaries were positive at G1 and weaker/heterogeneous at
G3; finite-size/max-Q effects were major, with additional heterogeneous
aggregation and spatial contributions.

**External stress test:** Hamburg had 39 Awake and 49 Isoflurane recordings from
seven animals, but condition-linked ROI/node-count differences and non-paired
recordings limit external replication claims.

**Limitations:** The `±0.01` classification band is not a sampling-error bound;
some RIKEN state cells have one window; synthetic sign error differs from
substantive reversal; the synthetic calibration is RIKEN-like `k-bar=16` and not
Hamburg `k-bar=4`.

**Conclusion:** Under the tested representations, the measured modularity
contrast is transformation-sensitive. The result is not a causal or
consciousness claim.

## Main-text evidence rules

- Treat animal as the biological unit wherever animal-level data exist.
- Report G1 effect, G3 effect, paired G3−G1 shift and categorical reversals as
  separate summaries.
- Do not use the `±0.01` band as a significance threshold.
- Report finite-size/max-Q before discussing aggregation or spatial terms.
- Keep selected density, degree and connectivity analyses in exploratory or
  supplementary sections.
- Name Hamburg's node-count imbalance and condition-level non-pairing before any
  directionally compatible description.
- Describe Phase 2 as a multi-recording extension because of source-lineage
  overlap with Phase 1.
- Describe the programme as sequentially preregistered and adaptive.

## Neighbor boundary

The manuscript must cite the established methodological neighborhood rather than
claiming priority for scale sensitivity itself:

- [Yang et al. 2021](https://doi.org/10.1371/journal.pbio.3001146) — Hamburg
  CA1 source biology and network analysis;
- [van Wijk et al. 2010](https://doi.org/10.1371/journal.pone.0013701) — N and
  mean-degree comparability;
- [Zalesky et al. 2010](https://doi.org/10.1016/j.neuroimage.2009.12.027) —
  node/parcellation scale;
- [Good et al. 2010](https://doi.org/10.1103/PhysRevE.81.046106) — Qmax size
  dependence and degeneracy;
- [Fortunato & Barthélemy 2007](https://doi.org/10.1073/pnas.0605965104) —
  modularity resolution limit;
- [Botvinik-Nezer et al. 2020](https://doi.org/10.1038/s41586-020-2314-9) —
  analytic-choice variability;
- [MAUP literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC7151983/) —
  cross-domain scale/zoning analogue.

The residual increment is a sequential, provenance-preserving stability audit
that joins a RIKEN extension, explicit finite-size/transformation decomposition
and a limitation-aware external stress test. It is not nine individually novel
claims.

## Prohibited manuscript sentences

```text
The experiment validates a theory of consciousness.
Objectification causes the neural reversal.
The RIKEN extension is a fully independent replication of Phase 1.
Hamburg provides clean convergent external replication.
MR-C or T-D is a preregistered primary replication criterion.
All simple artifacts have been excluded.
Finite size, aggregation, spatial organization, density, degree or
disconnectedness alone explains the finding.
Modularity Q directly measures consciousness.
Phase 0 is native MATLAB exact replication or R0-PASS.
```

## Stop boundary

This claim boundary does not authorize new analysis or full manuscript prose.
The next gate is a second independent review; only after that review may the
claim freeze be considered for a final manuscript draft.
