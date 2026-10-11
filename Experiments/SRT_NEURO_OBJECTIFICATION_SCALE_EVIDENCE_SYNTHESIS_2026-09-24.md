---
id: SRT-NEURO-OBJECTIFICATION-SCALE-EVIDENCE-SYNTHESIS-20260924
type: evidence_synthesis
status: draft
version: v0_2_major_revision
record_stage: phase4_major_revision
date: 2026-09-24
layer: operations
epistemic_layer: experimental
claim_mode: review_resolution
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, EvidenceSynthesis, ReviewResolution, Modularity, Reproducibility]
---

# Phase 4 — evidence synthesis after independent major review

## 1. Scope and audit gate

This draft synthesizes the completed Phase 0–3C evidence after the independent
PR #1051 review-resolution audit:

`Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PR1051_REVIEW_RESOLUTION_AUDIT_2026-09-24.md`.

The audit used only saved Q/metadata/code outputs. It did not run a new
correlation, graph, Louvain, modularity, Hamburg Sleep analysis, robustness
control or external network-effect analysis. Frozen experiment owners remain
unchanged.

The current synthesis branch is `paper/neuro-objectification-synthesis-20260924`.
The experiment branch remains `experiments/neuro-objectification-phase1-20260918`
at `9592917ab740dd389c70de1a1609a35f131c500c`. This synthesis is a review
draft, not a refreeze and not a full manuscript.

## 2. Revised evidence ledger

| stage | evidence owner | bounded result | manuscript use after audit |
|---|---|---|---|
| Phase 0 R0A/R0B | Phase 0 result records | released-result reconstruction and qualitative directions passed; native MATLAB was unavailable; R0B is `R0-PARTIAL` | source calibration with explicit runtime limitation |
| Phase 1 primary matrix | Phase 1 result/preregistration | one source-selected recording per condition; positive and negative `DeltaQ` cells across signal/grain; no animal inference | recording-level discovery evidence, qualified |
| density/degree/connectivity controls | dated control records | selected reversals persist in named diagnostic cells; fragmentation and other differences remain | exploratory single-source diagnostics only |
| RIKEN multi-recording | multi-recording preregistration/result | 5 Sleep animals/6 sessions and 4 Anesthesia animals/4 recordings; negative animal-level G3−G1 shifts in 4/5 and 3/4 | strongest RIKEN extension evidence, not fully independent of Phase 1 |
| Hamburg availability/anesthesia | Hamburg audit/preregistration/result plus review audit | 39 Awake and 49 Isoflurane recordings from 7 animals; G1 Iso/Awake ROI counts were condition-linked; adjusted and unadjusted diagnostic coefficients changed sign | inconclusive external stress test, not convergent replication |
| Phase 3C decomposition | Phase 3C preregistration/result plus review audit | C1 negative in all 8 RIKEN animal×grain cells; C1 largest median absolute contribution, but C2/C3/C4 can dominate individual cells; synthetic max-Q bias is large | major finite-size/max-Q qualification plus heterogeneous transformation description |

The complete sampling, decomposition, synthetic and Hamburg audit outputs are
in the machine-readable review-resolution attachments. No reviewer numbers were
copied into an experiment record without independent recalculation.

## 3. Primary claim ceiling after audit

> **Across the tested cellular-resolution datasets, spatial coarse-graining
> materially altered the estimated state-dependent modularity contrast. In the
> RIKEN recording extension, this was characterized primarily by attenuation from
> positive fine-grain contrasts toward weaker and heterogeneous coarse-grain
> estimates. Finite-size/max-Q effects were a major contributor, while
> aggregation and spatial grouping introduced additional heterogeneous changes.
> The Hamburg Anesthesia stress test was limited by condition-linked differences
> in recorded cell counts and therefore does not constitute clean external
> replication.**

This is a claim about the stability of a measured modularity contrast under
declared signal, node and graph representations. It is not a claim about a
causal neural mechanism, consciousness, or a theory-level ontology.

The title is revised to:

> **A stability audit of state-dependent modularity across spatial grains in
> cellular-resolution neural networks**

This title describes the programme and does not imply that spatial grain itself
causes a biological change.

## 4. What the audit changes

### B1 — sampling uncertainty: confirmed

The RIKEN multi-recording window audit checked 30 recording×grain cells. Twelve
state cells had `n=1`, so sample variance and `SE(DeltaQ)` were not estimable;
of the 18 estimable recording×grain cells, 17 had `SE(DeltaQ)>0.01`. The
`±0.01` band remains a declared descriptive classification rule, not a formal
uncertainty boundary. Animal-level summaries therefore remain descriptive and
use animal nesting.

The safe RIKEN description is attenuation of the positive fine-grain summary
toward weaker and heterogeneous coarse-grain estimates, with individual
recording signs that are not uniform. “Direction changes across grain” remains
true for selected cells, but it is not a substitute for reporting uncertainty.

### B2 — finite-size/max-Q contribution: confirmed

`C1` is negative in all 8 RIKEN animal×grain cells. Its median absolute
contribution is `0.1160`, larger than the corresponding medians for C2
(`0.0694`), C3 (`0.0578`) and C4 (`0.0656`). The component is not alone:
C2 is largest in 3/8 cells, C1 in 3/8, and C4 in 2/8. The manuscript must
therefore say that finite-size/max-Q effects are a major contributor while
retaining heterogeneous aggregation and spatial terms.

The synthetic calibration has maximum sign-error rate `0.53`, maximum
substantive reversal rate `0.06`, and maximum absolute cell mean bias `0.2093`.
Sign error is not substantive reversal. Large planted effects are also strongly
attenuated, so the old “weak effects only” wording is removed. The synthetic
calibration is RIKEN-like connected `k-bar=16`; it does not calibrate Hamburg
`k-bar=4`.

### B3 — Hamburg node-count confound: confirmed

All seven Hamburg animals had larger mean G1 ROI/node counts in Isoflurane
than Awake recordings; the mean Iso/Awake ratios ranged from `1.09` to `3.32`.
Across the 88 recordings, the condition–`log(N_G1)` correlation was `0.638`,
with an auxiliary condition-plus-animal model `R²=0.553` and VIF `2.24`.
For G1/G2/G3 respectively, the unadjusted Iso−Awake coefficients
`0.0176/-0.0185/-0.0095` changed after `log(N)+animal fixed effect` to
`-0.0265/0.0122/0.0282`; all intervals included zero.

This is a review diagnostic using existing one-window Q values, not a new
confirmatory model. Because condition is recorded in separate Awake/Isoflurane
recordings rather than same-session paired observations, the adjusted
coefficient is not a causal correction. Hamburg is retained as a directionally
compatible but inconclusive external stress test.

## 5. RIKEN evidence and biological unit

RIKEN remains the strongest empirical extension, but its provenance is now
described accurately. Phase 1 source-selected Sleep and Anesthesia records
match Phase 2 `mouse05_sleep` and `mouse05_ane` in animal label and state-frame
lengths while differing in MAT hash and ROI shape. The exact Phase 1 session ID
is unavailable. Phase 2 is therefore a **multi-recording extension**, not a
fully independent replication of Phase 1.

At the animal level, the existing summaries remain:

| condition | G1 mean [95% bootstrap interval] | G3 mean [95% bootstrap interval] | paired G3−G1 mean [95% bootstrap interval] |
|---|---|---|---|
| Sleep | 0.079779 [0.050390, 0.107307] | 0.003681 [-0.040873, 0.055422] | -0.076098 [-0.126928, -0.024503] |
| Anesthesia | 0.058848 [-0.010092, 0.127788] | -0.024867 [-0.117993, 0.067739] | -0.083714 [-0.227351, 0.018693] |

Animal-level paired shifts are negative in 4/5 Sleep and 3/4 Anesthesia. These
are descriptive summaries; windows, sessions, recordings and Louvain trials
are not interchangeable biological replicates. The manuscript will not use
the post-complete-data `MR-C` label as a preregistered replication criterion.

## 6. Controls and exploratory status

Density, mean-degree and selected connected-graph analyses remain useful
diagnostics, but they are downgraded to exploratory single-source controls.
They weaken named simple explanations in the tested cells; they do not exclude
all artifacts or identify a causal grain mechanism. The multi-recording primary
construction itself used connected `k-bar=16` graphs, but that fact does not
retroactively promote the earlier selected controls.

## 7. Phase 3C reporting rule

The manuscript will report R0/R1/R2/R3 distributions and C1/C2/C3/C4 values
directly. The local T-D label is retained only as historical implementation
metadata: the preregistered prose names a variable pattern, while the actual
code assigns `variable` whenever values do not occupy one single sign band and
the dataset aggregation drops `other` labels before selecting a dataset label.
The result-specific MR-C rule is likewise post-complete-data descriptive. Neither
label is a primary manuscript finding.

The bounded interpretation is:

> Finite-size/max-Q, aggregation and spatial grouping make heterogeneous
> contributions to the observed representation-dependent contrast; the saved
> results do not identify one universal transformation as its cause.

## 8. Provenance of the programme

The work is a **sequentially preregistered adaptive stability audit**, not one
globally frozen pipeline:

`Phase 0 result (2026-09-17)` → `Phase 1 freeze/result (09-18/09-19)` →
`density/degree/connectivity controls (09-21)` → `RIKEN multi-recording
freeze/result (09-21/09-22)` → `Hamburg availability/adaptation/result
(09-22/09-23)` → `Phase 3C freeze/result (09-23/09-24)`.

Each stage was frozen before its own outcome, while later-stage design was
informed by earlier observations. The manuscript must say so.

## 9. Neighbor boundary and novelty

The paper does not claim priority for the general ideas that analytical choices,
node definition, spatial scale, network size, modularity optimization or
aggregation can change results. The strongest verified neighbors are:

- [Yang et al. 2021](https://doi.org/10.1371/journal.pbio.3001146), the Hamburg
  CA1 anesthetic network/biological source;
- [van Wijk et al. 2010](https://doi.org/10.1371/journal.pone.0013701), N and
  mean-degree comparability;
- [Zalesky et al. 2010](https://doi.org/10.1016/j.neuroimage.2009.12.027),
  node/parcellation scale;
- [Good et al. 2010](https://doi.org/10.1103/PhysRevE.81.046106), Qmax size
  dependence and modularity degeneracy;
- [Fortunato & Barthélemy 2007](https://doi.org/10.1073/pnas.0605965104), the
  modularity resolution limit;
- [Botvinik-Nezer et al. 2020](https://doi.org/10.1038/s41586-020-2314-9),
  many-analysts analytic-choice variability;
- the [MAUP methodological literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC7151983/),
  used explicitly as a cross-domain scale/zoning analogue.

The residual increment is narrower: a sequential, provenance-preserving
stability audit that combines a RIKEN extension, explicit finite-size and
transformation decomposition, and an external stress test whose limitations are
made visible. This is a methodological reanalysis/application claim, not nine
individually novel contributions.

## 10. Claim ladder

### Safe main-text claims

1. Under the tested pipelines, the estimated state-dependent modularity contrast
   was not invariant across declared spatial grains.
2. The RIKEN multi-recording extension shows predominantly negative animal-level
   G3−G1 shifts, with heterogeneous recording-level signs and material
   finite-size/max-Q contribution.
3. Hamburg is a directionally compatible but inconclusive external stress test
   because condition-linked ROI/node counts limit independent interpretation.
4. Selected density, degree and connected controls are exploratory diagnostics;
   they weaken named simple explanations without isolating a causal mechanism.

### Discussion claims

- The measured object is a representation-to-inference pipeline, not a
  scale-free modularity fact.
- Finite-size/max-Q behavior is an interpretive constraint, not a minor nuisance.
- Animal nesting and explicit provenance are necessary when state windows and
  recordings differ across conditions.

### Prohibited claims

```text
the programme validates a theory of consciousness
objectification causes a neural reversal
Hamburg is a clean external or same-session replication
MR-C or T-D is a preregistered primary replication criterion
finite size, aggregation, spatial organization, density, degree or
disconnectedness alone explains the pattern
the effect is universal or population-general
Phase 0 is native MATLAB exact replication or R0-PASS
```

## 11. Stop boundary

This is a major-revision synthesis draft. It does not authorize Hamburg Sleep,
new graph/Q calculations, new robustness controls, a new external dataset,
theory promotion or full manuscript drafting. The next gate is a second
independent review of the revised claim freeze and outline.
