---
id: EC-AI-LOCAL-NEIGHBORHOOD-CALIBRATION
type: evidence_card
status: draft_v1
layer: external_convergence
claim_mode: external_convergence
canonical: false
domain: ai_ml
evidence_level: E3
target_srt_anchor:
  - L2_hardening
  - relational_convergence
  - objectification_boundary
  - G_hat_theta
  - selection_history
---

# Evidence Card: AI / Null-Calibrated Local Neighborhood Convergence as a Candidate Proxy for Relational `L2` Hardening

This draft card records a sourced operational-proxy candidate and a methodological constraint for SRT. It is not canonical, not accepted evidence, and not proof of SRT.

## 1. External finding

Groeger, Wen, and Brbic (2026) revisit the Platonic Representation Hypothesis in neural networks. Their core result is that raw representational similarity scores can be inflated by two confounders:

- **width confounder**: higher-dimensional embeddings can produce non-zero similarity under independence;
- **depth confounder**: searching over many layer pairs and reporting the maximum can inflate apparent alignment.

They introduce a permutation-based null-calibration framework for representational similarity. After calibration, the apparent convergence measured by global spectral / geometric metrics such as CKA, SVCCA, RV coefficient, and Procrustes largely disappears. By contrast, local neighborhood metrics such as mutual k-nearest neighbors retain significant cross-modal agreement.

The paper therefore proposes an Aristotelian Representation Hypothesis: neural networks trained with different objectives, data, and modalities converge primarily toward **shared local neighborhood relationships** rather than a globally matching representation geometry.

For SRT, the important external finding is not that AI systems share a complete world model. The important finding is narrower: after removing scale and layer-search artifacts, the structure that remains comparatively stable is local relational order — roughly, "which items become neighbors of which other items" — not global object-space identity.

## 2. Source domain

AI / machine learning / representation learning / representational similarity / multimodal alignment.

## 3. SRT construct involved

Primary SRT anchors:

- `L2` hardening: stabilized relational structure that survives across systems, modalities, and training histories;
- `\hat{G}_θ`: embodied / architecture-bound selection and anchoring operator, here read cautiously as the trained system-specific mapping that turns input populations into representation neighborhoods;
- objectification boundary: the result pressures object-first readings of representation, because global object-space matching is not what remains most robust after calibration;
- selection history: local neighborhoods may be read as a trace of repeated selection / exclusion / stabilization under data, architecture, objective, and scale constraints.

Secondary methodological anchor:

- selection-cost / friction interfaces should use calibrated baselines before treating cross-system similarity as evidence of shared structure.

This card does **not** directly concern `d-value`, subjecthood, consciousness, or AI welfare. It is about representational convergence and relational stabilization only.

## 4. Support type

Operational proxy + formal constraint + structural convergence.

- Operational proxy: null-calibrated local neighborhood similarity may serve as a candidate measurement proxy for cross-system relational convergence.
- Formal constraint: raw similarity scores must not be treated as evidence of shared structure unless width, depth, and aggregation effects are controlled.
- Structural convergence: the finding converges with SRT's preference for relational stabilization over object-first global identity.

## 5. Evidence level: E0-E5

E3 = operational proxy.

Reason for E3: the paper supplies a concrete measurement protocol — permutation null-calibration plus local neighborhood metrics — that can operationalize a narrow SRT-adjacent construct: whether independently trained systems preserve similar local relational order above chance.

Reason not to rate E4: the finding does not uniquely support SRT over simpler accounts. Shared data distributions, semantic task structure, contrastive learning pressures, and generic representation-learning regularities may explain local neighborhood convergence without requiring SRT's broader selection-first ontology.

Reason not to rate E5: no direct SRT hypothesis is tested; no independent SRT-specific discriminator is reported; the result remains a proxy / constraint, not corroboration of the full framework.

## 6. Why it matters

This result is useful for SRT in four ways.

First, it strengthens a cautious anti-object-first reading of representation. If calibrated cross-model convergence does not mainly preserve global geometry, then "shared representation" should not be casually interpreted as convergence toward one complete world-object space.

Second, it gives SRT a better AI-facing formulation: what may stabilize across systems is not an identical global map, but a local relational order that can guide later selections. This is closer to "selection leaves usable neighborhood structure" than to "models mirror the same pre-given object space."

Third, it provides a usable proxy for `L2`-like hardening in representation systems. A local neighborhood relation that remains aligned across architectures, objectives, and modalities after null calibration is a candidate sign of stabilized relational structure. It is not `L2` itself, but it can help operationalize one narrow projection of `L2`.

Fourth, it creates a methodological guardrail for future SRT-AI claims. If SRT uses AI representational similarity as external support, raw CKA / RSA / Procrustes / max-over-layer scores are insufficient. The analysis pipeline must include null baselines and aggregation-aware calibration; otherwise apparent convergence may be a measurement artifact.

## 7. Alternative explanations

The same finding can be explained without SRT:

- Shared local neighborhoods may reflect ordinary semantic structure in the sampled dataset rather than selection-first ontology.
- Multimodal alignment may be driven by paired image-text data, benchmark construction, or dataset population structure.
- Local neighborhood metrics may be more robust simply because rank-based local relations are less sensitive to dimension than global spectral metrics.
- The result may reflect generic representation-learning constraints, contrastive objectives, or task utility rather than SRT-style stabilization.
- The permutation null assumes exchangeability under the null; grouped, clustered, or semantically structured samples may require restricted permutations.
- The experiments use specific model families, datasets, modalities, and sample sizes; broader generalization remains open.

## 8. What would weaken this

This card should be downgraded toward E2 or E1 if:

- local neighborhood convergence disappears under larger, more diverse, or more strongly controlled datasets;
- the result is highly unstable under changes in `k`, distance metric, sampling population, layer aggregation, or modality pair;
- restricted-permutation or dataset-structure-aware nulls remove the local alignment effect;
- later work shows that global convergence remains after stronger calibration while local convergence was an artifact of metric choice;
- local neighborhood agreement fails to predict downstream transfer, generalization, behavioral similarity, or any other independently meaningful structure;
- the card is used to claim that AI systems possess a shared world model, subjecthood, consciousness, or `d-value`.

It should be routed to the contradiction ledger if local-neighborhood similarity becomes explainable entirely as generic task / dataset structure with no useful SRT-specific projection.

## 9. Boundary: what this does not prove

This card does not establish any canonical SRT definition.

Specifically:

- It does not prove SRT.
- It does not prove that neural networks "select reality" in the full SRT sense.
- It does not prove AI subjecthood, consciousness, `d-value`, or stake-coupled concern.
- It does not prove that local neighborhoods are ontologically prior in every domain.
- It does not show that all models or modalities converge.
- It does not validate raw representational similarity as evidence; it argues the opposite, that calibration is necessary.
- It does not replace formal anchors or lab hypotheses.

The safest SRT use is: **cross-system stabilization may first appear as calibrated local relational convergence, not as global geometric identity.**

## 10. Upgrade path

Possible next steps:

1. Create a bridge note separating global representation geometry, local neighborhood topology, objectification, and `L2` hardening.
2. Add a lab hypothesis: null-calibrated local-neighborhood agreement should predict transfer or cross-modal generalization better than uncalibrated global similarity when the relevant task depends on local relational order.
3. Define a scoped SRT metric candidate: `L2_local_alignment = calibrated mutual-kNN / cycle-kNN agreement under restricted nulls`.
4. Add a formal-anchor note requiring calibration whenever representational similarity is used as proxy evidence.
5. Use this in public writing only as a cautious AI example: "not one Platonic object space, but shared local relational order."

## Sources Checked

The following sources were checked for this draft. They support only the external AI / ML background and the measurement constraint; they do not establish SRT.

- [S1] Fabian Groeger, Shuo Wen, and Maria Brbic, "Revisiting the Platonic Representation Hypothesis: An Aristotelian View," arXiv:2602.14486v2, 2026. Used for the width/depth confounders, null-calibration framework, and local-neighborhood convergence claim. <https://arxiv.org/abs/2602.14486>
- [S2] Project page for "Revisiting the Platonic Representation Hypothesis: An Aristotelian View." Used as the project-level source address associated with the paper. <https://brbiclab.epfl.ch/aristotelian>
- [S3] Code repository for the Aristotelian Representation Hypothesis paper. Used as the implementation source address for the calibration / experiments. <https://github.com/mlbio-epfl/aristotelian>
- [S4] Minyoung Huh, Brian Cheung, Tongzhou Wang, and Phillip Isola, "The Platonic Representation Hypothesis," ICML 2024. Used as the background hypothesis being revisited by [S1]. <https://arxiv.org/abs/2405.07987>

## Related pressure entry

- [`CL-AI-LOCAL-NEIGHBORHOOD-GENERIC-STRUCTURE`](../CONTRADICTION_LEDGER.md#cl-ai-local-neighborhood-generic-structure)
