---
id: SRT-NEURO-OBJECTIFICATION-SCALE-PR1051-REVIEW-RESOLUTION-AUDIT-20260924
type: review_resolution_audit
status: active
version: v0_1
record_stage: phase4_major_revision_audit
date: 2026-09-24
layer: operations
epistemic_layer: experimental
claim_mode: audit
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, ReviewResolution, Modularity, Scale, Audit]
---

# PR #1051 review-resolution audit

## Scope and non-actions

This audit independently checks the major-review findings supplied for PR
`#1051` against completed runtime outputs. It reads saved window-level `Q_max`,
Phase 3C transformation distributions, synthetic summaries, Hamburg per-
recording results, metadata, protocol files and the existing summarization code.

It does not run a new correlation, graph construction, Louvain optimization,
modularity calculation, Hamburg Sleep analysis, robustness control or external
network-effect analysis. It does not amend any frozen experiment owner.

Machine-readable detail is in:

- `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PR1051_REVIEW_RESOLUTION_AUDIT_2026-09-24.json`
- `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PR1051_REVIEW_RESOLUTION_RECORDING_UNCERTAINTY_2026-09-24.csv`
- `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_PR1051_REVIEW_RESOLUTION_HAMBURG_ROI_COUNTS_2026-09-24.csv`

The computational audit script used to derive these attachments is retained in
the ignored `.local/` runtime area and is not an experimental source or result
owner.

## B1 — recording-level uncertainty

The audit used the existing RIKEN multi-recording window table and calculated,
for each recording × grain,

`SE(DeltaQ) = sqrt(var(Q_wake)/n_wake + var(Q_target)/n_target)`.

This is a descriptive within-recording uncertainty calculation, not a formal
z-test and not a replacement for animal-level inference.

- 30 recording × grain cells were checked.
- 18 cells had estimable sample variances in both states.
- 12 cells had at least one state with `n=1`, so `SE(DeltaQ)` is not
  estimable and was left blank.
- Of the 18 estimable cells, 17 had `SE(DeltaQ) > 0.01`.

The 12 non-estimable state cells are:

| recording | condition | grain | state | `Q_max` | reason |
|---|---|---|---|---:|---|
| mouse01_sleep | Sleep | G1/G2/G3 | Wake | 0.757798 / 0.320230 / 0.289890 | one Wake window |
| mouse03_sleep | Sleep | G1/G2/G3 | Wake | 0.724467 / 0.307820 / 0.193808 | one Wake window |
| mouse04_day1_sleep | Sleep | G1/G2/G3 | Wake | 0.639307 / 0.331536 / 0.309202 | one Wake window |
| mouse05_ane | Anesthesia | G1/G2/G3 | target | 0.693110 / 0.436888 / 0.239327 | one target window |

Examples show why the `±0.01` class band cannot be interpreted as a sampling-
error boundary: `mouse02_sleep/G1` has `DeltaQ=0.03052` and `SE=0.01491`,
whereas `mouse02_sleep/G3` has `DeltaQ=-0.00217` and `SE=0.01358`. The full
30-row table, including every `n`, mean, `DeltaQ`, estimable SE and threshold
class, is in the JSON attachment.

### RIKEN animal-level reassessment

The existing recording-level values were independently regrouped by animal,
with the two mouse04 Sleep sessions averaged within animal. The bootstrap uses
10,000 animal-level resamples and the same declared percentile-interval logic;
windows, recordings and Louvain repeats are not biological replicates.

| condition | metric | mean | median | bootstrap 95% interval |
|---|---|---:|---:|---:|
| Sleep | G1 effect | 0.079779 | 0.097086 | [0.050390, 0.107307] |
| Sleep | G3 effect | 0.003681 | -0.002174 | [-0.040873, 0.055422] |
| Sleep | paired G3−G1 | -0.076098 | -0.086787 | [-0.126928, -0.024503] |
| Anesthesia | G1 effect | 0.058848 | 0.062366 | [-0.010092, 0.127788] |
| Anesthesia | G3 effect | -0.024867 | -0.020714 | [-0.117993, 0.067739] |
| Anesthesia | paired G3−G1 | -0.083714 | -0.042486 | [-0.227351, 0.018693] |

The distinction matters. Sleep has a positive fine-grain mean and a near-zero
coarse-grain mean, with 4/5 negative animal-level paired shifts; Anesthesia has
3/4 negative paired shifts, but its paired interval includes zero. Categorical
recording reversals are a separate descriptive count: 3/5 Sleep animals and
3/4 Anesthesia animals contain at least one reversed recording. The audit does
not collapse these into a single population claim.

**B1: CONFIRMED.** The review finding is supported. The local `±0.01` band
is useful for a declared descriptive classification, but it is not a reliable
uncertainty threshold for individual recording contrasts; several state cells
also lack estimable variance entirely.

## B2 — finite-size and max-Q decomposition

The audit directly read the completed Phase 3C `animal_transformation_results`
and `transformation_contrasts` files. For each RIKEN animal × grain, `R1` and
`R2` medians were reconstructed from the saved contrast distributions only;
no Q or graph was recomputed.

| animal | grain | R0 | median R1 | P(R1<−.01) / P(R1 reversal) | median R2 | P(R2<−.01) / P(R2 reversal) | R3 | C1 | C2 | C3 | C4 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mouse03 | G2 | -0.0209 | -0.1801 | 1.00 / 0.00 | 0.1638 | 0.00 / 1.00 | 0.1151 | -0.1592 | 0.3421 | -0.0487 | 0.1359 |
| mouse03 | G3 | -0.0209 | -0.0585 | 1.00 / 0.00 | 0.0383 | 0.00 / 1.00 | 0.0271 | -0.0376 | 0.0966 | -0.0112 | 0.0480 |
| mouse05 | G2 | 0.0007 | -0.0192 | 0.62 / n/a | 0.0400 | 0.00 / n/a | 0.0517 | -0.0199 | 0.0528 | 0.0118 | 0.0511 |
| mouse05 | G3 | 0.0007 | -0.0715 | 1.00 / n/a | -0.0017 | 0.32 / n/a | -0.0686 | -0.0721 | 0.0673 | -0.0668 | -0.0693 |
| mouse06 | G2 | 0.1315 | 0.0057 | 0.04 / 0.00 | 0.0482 | 0.00 / 0.00 | -0.0346 | -0.1258 | 0.0420 | -0.0828 | -0.1661 |
| mouse06 | G3 | 0.1315 | -0.0768 | 1.00 / 1.00 | 0.0014 | 0.02 / 0.02 | -0.1664 | -0.2083 | 0.0790 | -0.1678 | -0.2979 |
| mouse07 | G2 | 0.1241 | 0.0178 | 0.00 / 0.00 | 0.0613 | 0.00 / 0.00 | 0.0621 | -0.1063 | 0.0408 | 0.0009 | -0.0619 |
| mouse07 | G3 | 0.1241 | -0.0705 | 1.00 / 1.00 | 0.0006 | 0.04 / 0.04 | 0.1083 | -0.1945 | 0.0715 | 0.1078 | -0.0157 |

### B2-A/B2-B

- `C1` is negative in all 8 RIKEN animal × grain cells by both its saved
  distribution mean and median.
- At G3, saved N-only `R1` values are negative in every animal's transformation
  distribution: P(R1 negative) is 1.00 for mouse03, mouse05, mouse06 and
  mouse07. Where a substantive R0 sign exists, P(R1 reversal) is 1.00 for
  mouse06 and mouse07; it is 0.00 for mouse03 because R0 is already negative;
  mouse05 has a null R0, so reversal is not defined.

### B2-C

Across the 8 cells, the median absolute contributions were:

| contribution | median `|C|` | range of `|C|` |
|---|---:|---:|
| C1 finite size / max-Q | 0.1160 | 0.0199–0.2083 |
| C2 aggregation | 0.0694 | 0.0408–0.3421 |
| C3 spatial organization | 0.0578 | 0.0009–0.1678 |
| C4 total objectification | 0.0656 | 0.0157–0.2979 |

C1 is the largest median absolute component and is negative in every cell, so
the prior wording that treated finite size as merely a generic limitation
understated its contribution. It is not a universal single-component account:
C2 is largest in 3/8 cells, C1 in 3/8, and C4 in 2/8; C3 is also large in
some cells. The safe conclusion is a major finite-size/max-Q contribution plus
heterogeneous aggregation and spatial terms, not a unique causal decomposition.

### Synthetic terminology correction

The nine frozen synthetic cells were re-summarized from the saved 900 rows.
`sign-error` means an estimated sign different from the planted sign; it is
not the same event as a substantive reversal, which requires an estimate below
`−0.01` for a positive planted effect.

| N regime | effect | mean planted | mean estimated | estimated/planted | mean bias | sign-error | substantive reversal |
|---|---|---:|---:|---:|---:|---:|---:|
| large | large | 0.2378 | 0.0285 | 0.1199 | -0.2093 | 0.00 | 0.00 |
| large | medium | 0.1210 | 0.0004 | 0.0034 | -0.1206 | 0.42 | 0.00 |
| large | small | 0.0358 | -0.0000 | -0.0011 | -0.0359 | 0.53 | 0.00 |
| medium | large | 0.2396 | 0.0928 | 0.3874 | -0.1468 | 0.00 | 0.00 |
| medium | medium | 0.1223 | 0.0038 | 0.0307 | -0.1186 | 0.15 | 0.00 |
| medium | small | 0.0353 | 0.0013 | 0.0364 | -0.0340 | 0.33 | 0.00 |
| small | large | 0.2362 | 0.1021 | 0.4323 | -0.1341 | 0.00 | 0.00 |
| small | medium | 0.1205 | 0.0120 | 0.0992 | -0.1085 | 0.09 | 0.01 |
| small | small | 0.0370 | 0.0020 | 0.0531 | -0.0350 | 0.42 | 0.06 |

Maximum sign-error rate is `0.53`; maximum substantive reversal rate is
`0.06`. Large planted effects are also strongly attenuated, including a
`-0.2093` mean bias in the large-N/large-effect cell. Therefore “attenuation
only weak effects” is not supported. This calibration uses the RIKEN-like
connected `k-bar=16` regime; it does not calibrate Hamburg's `k-bar=4` graphs.

**B2: CONFIRMED.** The review finding is supported and requires a stronger
finite-size/max-Q qualification in the manuscript. Sign error and substantive
reversal must remain separate quantities.

## B3 — Hamburg node-count confound

The audit read all 88 complete Hamburg Anesthesia result JSON files: 39 Awake
and 49 Isoflurane recordings from seven animals. The per-recording CSV records
accepted ROI count, G1/G2/G3 node count, group-size statistics, source path and
the already-saved per-recording `q_max`.

At G1, Isoflurane recordings had a larger accepted ROI count than Awake
recordings for every animal. The mean Iso/Awake ratios by animal were:

| animal | Awake mean N | Iso mean N | Iso/Awake | G1 Awake range | G1 Iso range |
|---|---:|---:|---:|---:|---:|
| 37527 | 198.1 | 609.6 | 3.08 | 141–280 | 548–652 |
| 37528 | 423.7 | 460.8 | 1.09 | 305–486 | 418–505 |
| 37529 | 253.2 | 450.7 | 1.78 | 207–395 | 346–580 |
| 37530 | 416.5 | 461.1 | 1.11 | 381–437 | 351–594 |
| 48 | 229.7 | 270.0 | 1.18 | 196–258 | 151–353 |
| 51 | 172.6 | 573.8 | 3.32 | 85–303 | 567–581 |
| 53 | 198.2 | 389.2 | 1.96 | 137–358 | 367–405 |

G2/G3 node counts are constrained by the frozen dataset-size-aware grouping
rule and are correspondingly closer: across all recordings, G2 means are
46.41 Awake versus 47.69 Isoflurane and G3 means are 24.26 versus 24.76. That
does not remove the G1 imbalance or the fact that the G1 recording population
is the input to the downstream grain construction.

The review-only diagnostic regression used existing one-window per-recording
Q values:

`Q ~ condition + log(N) + animal fixed effect`.

| grain | unadjusted Iso−Awake coefficient (SE; 95% CI) | adjusted coefficient (SE; 95% CI) |
|---|---|---|
| G1 | 0.0176 (0.0209; [-0.0239, 0.0591]) | -0.0265 (0.0193; [-0.0648, 0.0119]) |
| G2 | -0.0185 (0.0152; [-0.0488, 0.0117]) | 0.0122 (0.0179; [-0.0235, 0.0479]) |
| G3 | -0.0095 (0.0148; [-0.0390, 0.0200]) | 0.0282 (0.0180; [-0.0076, 0.0639]) |

The condition–`log(N_G1)` Pearson correlation is `r=0.638`; the auxiliary
condition-plus-animal model gives `R²=0.553` and VIF `2.24`. These are not
perfect-collinearity statistics, but they document a material condition-linked
node-count imbalance. The coefficient sign changes in all three grains when
the diagnostic adjusts for `log(N)` and animal fixed effects. Because states
are condition-specific recordings rather than same-session paired observations,
the adjusted coefficient cannot be interpreted as a causal correction.

**B3: CONFIRMED.** Hamburg is not a clean external replication under this
recording structure. It is retained as a directionally compatible but
inconclusive external stress test, with condition-linked N confounding as a
primary interpretability limitation.

## Major-review findings M1–M5

### M1 — exploratory evidence promoted too high: CONFIRMED

The prior synthesis promoted selected density, degree and connected controls
and the Hamburg pattern into the main claim ladder. The audit supports only
single-source exploratory diagnostic status for the former and does not support
Hamburg “convergent support” after the B3 gate. The connected `k-bar=16`
multi-recording primary construction remains a result of that analysis, but it
does not retroactively convert earlier selected controls into confirmatory
tests.

### M2 — MR-C/T-D provenance: CONFIRMED WITH QUALIFICATION

The multi-recording preregistration defines the broad MR-A/MR-B/MR-C/MR-D
vocabulary, but the result record supplies the specific MR-C operationalization
(`at least two animals with a reversed recording plus a negative animal-level
median G3−G1 shift`) only after the complete result. It is therefore a
post-hoc descriptive label, not a fully pre-specified replication criterion.

The Phase 3C preregistration does contain the T-D pattern prose. The actual
code defines `distribution_sign` as: one sign if all values fall in one band,
`null` if all are null, otherwise `variable`; it assigns T-D when R1 or R2 is
`variable`. Thus “variable” means mixed band membership, not necessarily both
substantive signs. The dataset aggregation then filters out `other` labels
before reporting a single dataset label. This aggregation rule is not clearly
pre-registered. The revised manuscript will not present MR-C or dataset-level
T-D as primary findings; it will retain the raw R0/R1/R2/R3 and C1–C4
distributions with their implementation caveat.

### M3 — discovery/extension overlap: CONFIRMED

The Phase 1 source-selected Sleep record has shape `6920×19000`, source-context
animal label 5 and used-frame lengths `[9146, 5660]`. Phase 2
`mouse05_sleep.mat` has a different SHA-256 and ROI shape `7355×19000`, but the
same animal label and used-frame lengths. The Phase 1 Anesthesia record has
shape `3210×19562` and used-frame lengths `[15528, 2933]`; Phase 2
`mouse05_ane.mat` has different SHA-256 and ROI shape `6592×19562`, but the
same animal label and used-frame lengths. The Phase 1 raw files do not encode a
dedicated session identifier, so byte-level identity is excluded but exact
session identity cannot be recovered. Recording-lineage overlap is therefore
confirmed for both conditions.

Phase 2 is relabeled a **multi-recording extension**, not a fully independent
replication. As a descriptive check using existing Q only, excluding
`mouse05_sleep` leaves 5 Sleep recordings with mean G3−G1 `-0.0594` and 3/5
negative shifts; excluding `mouse05_ane` leaves 3 Anesthesia recordings with
mean G3−G1 `-0.0885` and 2/3 negative shifts. These are not new inferential
results and are not used to restore independence.

### M4 — adaptive programme provenance: CONFIRMED

The programme is a sequence of stage-local freezes, not one globally frozen
pipeline:

`Phase 0 result (2026-09-17)` → `Phase 1 freeze/result (09-18/09-19)` →
`density/degree/connectivity controls (09-21)` → `RIKEN multi-recording
freeze/result (09-21/09-22)` → `Hamburg availability and adaptation/result
(09-22/09-23)` → `Phase 3C freeze/result (09-23/09-24)`.

Each stage was frozen before its own outcome was inspected, while later-stage
design was informed by earlier observations. The correct description is a
**sequentially preregistered adaptive stability audit**. The manuscript will
state this provenance explicitly.

### M5 — strongest-neighbor literature: CONFIRMED

The prior neighbor set was incomplete. The following verified sources now bound
the manuscript claim:

| neighbor | what it already establishes | what this work does not add | residual increment here |
|---|---|---|---|
| [Yang et al. 2021](https://doi.org/10.1371/journal.pbio.3001146) | Hamburg CA1 anesthetic network biology and modularity context | not a new Hamburg biological discovery | a declared reanalysis/stress test of scale-dependent inference |
| [van Wijk et al. 2010](https://doi.org/10.1371/journal.pone.0013701) | graph measures depend on N and mean degree; comparisons can be biased | not a new N/k comparability principle | applies the caveat to this cellular grain benchmark and audits it explicitly |
| [Zalesky et al. 2010](https://doi.org/10.1016/j.neuroimage.2009.12.027) | node/parcellation choice changes network parameters across spatial scales | not a new node-definition problem | records cellular spatial grouping as an explicit transformation |
| [Good et al. 2010](https://doi.org/10.1103/PhysRevE.81.046106) | modularity has degeneracy and `Q_max` depends on network size/module structure | not a new max-Q limitation | quantifies its contribution in the saved RIKEN decomposition and synthetic calibration |
| [Fortunato & Barthélemy 2007](https://doi.org/10.1073/pnas.0605965104) | modularity has a global resolution limit | not a new resolution-limit theory | treats resolution/size as a named alternative explanation |
| [Botvinik-Nezer et al. 2020](https://doi.org/10.1038/s41586-020-2314-9) | analytic flexibility can yield variable conclusions from one dataset | not a new many-analysts result | provides a sequential, provenance-preserving scale-stability audit in this application |
| [MAUP review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7151983/) | aggregation scale and zoning can change spatial results | not a neuroscience-specific priority claim | a clearly marked cross-domain methodological analogue for scale/aggregation sensitivity |

No unverified Patel “Janus effect” citation is added.

## Revised claim ceiling

### Primary claim before

> Across the frozen cellular-recording pipelines tested, the direction of the
> modularity-based state contrast changed with spatial grain, recurred across
> multiple RIKEN animals, and showed heterogeneous convergent support in an
> independent Hamburg CA1 anesthesia dataset. Matched-degree and connected-graph
> controls weakened simple density/degree/disconnectedness explanations, while
> the Phase 3C decomposition showed that finite-size effects are substantive but
> not a uniform account.

### Primary claim supported after audit

> Across the tested cellular-resolution datasets, spatial coarse-graining
> materially altered the estimated state-dependent modularity contrast. In the
> RIKEN recording extension, this was characterized primarily by attenuation from
> positive fine-grain contrasts toward weaker and heterogeneous coarse-grain
> estimates. Finite-size/max-Q effects were a major contributor, while
> aggregation and spatial grouping introduced additional heterogeneous changes.
> The Hamburg Anesthesia stress test was limited by condition-linked differences
> in recorded cell counts and therefore does not constitute clean external
> replication.

This is a methodological claim about the stability of a measured modularity
contrast under declared representations. It is not a claim about consciousness,
a causal neural mechanism, or a theory-level ontology.

## Resolution decisions

| item | audit status | manuscript action |
|---|---|---|
| B1 sampling uncertainty | CONFIRMED | show uncertainty/estimability boundary; no formal population claim from `±0.01` |
| B2 finite-size/max-Q | CONFIRMED | elevate finite-size/max-Q to major limitation; distinguish sign error from substantive reversal |
| B3 Hamburg N confound | CONFIRMED | gate Hamburg to inconclusive external stress test; remove convergent-support wording |
| M1 evidence level | CONFIRMED | downgrade selected controls to exploratory diagnostics |
| M2 labels | CONFIRMED WITH QUALIFICATION | remove MR-C/T-D from headline claims; retain raw distributions and provenance |
| M3 overlap | CONFIRMED | call Phase 2 a multi-recording extension |
| M4 timeline | CONFIRMED | describe the programme as sequentially preregistered and adaptive |
| M5 neighbors | CONFIRMED | add verified methodological and biological neighbors |

## Stop boundary

This audit does not authorize Hamburg Sleep, new graph/Q calculations, new
robustness controls, a new external dataset, SRT-facing theory interpretation,
or full manuscript drafting. The next authorized action is a second independent
review of the revised claim freeze and outline.
