---
id: EC-IG-FISHER-PSIF
type: evidence_card
status: draft_v1
layer: external_convergence
claim_mode: external_convergence
canonical: false
domain: mathematics_information
evidence_level: E2
target_srt_anchor:
  - Psi_f
  - selection_cost
---

# Evidence Card: Information Geometry / Fisher Metric as a Candidate Structural Interface for `Psi_f`

This draft card records a sourced structural-convergence candidate. It is not canonical, not accepted evidence, and not a proof of SRT.

## 1. External finding

Information geometry studies families of probability distributions as geometric objects. In this setting, the Fisher information matrix gives a local Riemannian metric on a statistical model, measuring how strongly nearby parameter changes alter the induced distribution.

The checked sources support three cautious points:

- Fisher-Rao geometry is a standard mathematical interface for local statistical distinguishability on model manifolds.
- Chentsov-style uniqueness results give the Fisher metric a non-arbitrary status under invariance / congruence conditions for statistical models.
- In machine learning, natural-gradient methods explicitly treat the parameter space as a Riemannian manifold whose metric is the Fisher information matrix.

For SRT, this makes Fisher geometry a candidate structural language for local transition burden, parameter-space friction, and selection-cost projection. It does not define `Psi_f`.

## 2. Source domain

Mathematics / information geometry / statistical manifolds / machine learning geometry.

## 3. SRT construct involved

Primary SRT anchor:

- [`../../_SRT_PSI_F_CANONICAL.md`](../../_SRT_PSI_F_CANONICAL.md), especially the distinction between the primary semantic anchor for `Psi_f` and the Fisher-Rao local information-geometric projection.

Secondary boundary anchor:

- [`../../_SRT_D_VALUE_CANONICAL.md`](../../_SRT_D_VALUE_CANONICAL.md), because Fisher distinguishability may contribute to capacity-style proxies only when stake-coupled concern is separately operationalized.

This card concerns `Psi_f` and selection cost. It does not treat Fisher geometry as a `d-value` card.

## 4. Support type

Structural convergence and bridge-support candidate.

This is not an operational proxy yet. It becomes operational only if a later card specifies a domain, a state space, a measurement procedure, and a testable relationship between Fisher-geometric quantities and transition burden / payability / recovery cost.

## 5. Evidence level: E0-E5

E2 = structural convergence.

Reason for E2: Fisher information geometry offers a mature formal structure for local distinguishability, curvature, and path geometry over probabilistic models. That structure resembles the formal side of `Psi_f` as local friction / transition burden under constrained selection.

Reason not to rate E3: no domain-specific operational proxy is established here. The card does not show that a Fisher metric measurement approximates SRT `Psi_f` in any concrete biological, cognitive, AI, social, or physical system.

## 6. Why it matters

SRT already treats `Psi_f` as the burden or resistance involved when open possibility is compressed into a maintainable reality-slice. In smooth statistical settings, Fisher geometry supplies a disciplined way to speak about nearby alternatives, distinguishability, and the cost-like geometry of moving through a model family.

The relevance is structural:

- A transition among possible parameterized states is not geometrically neutral if nearby states differ strongly in the induced distribution.
- A path through a statistical manifold can have local geometric length or energy-like accumulation.
- Natural-gradient learning shows that Fisher geometry can change what counts as a steep or efficient update direction, which makes it relevant to update friction and selection path structure.
- Chentsov-style uniqueness results reduce the worry that the Fisher metric is merely an arbitrary coordinate choice within statistical geometry.

This makes Fisher information geometry a serious candidate formal interface for one projection of `Psi_f`. It does not show that statistical distinguishability is already stake, value, subjecthood, or reality-selection.

## 7. Alternative explanations

The same external findings can be explained without SRT:

- Generic statistical distance: Fisher geometry may only measure local distinguishability between probability distributions.
- Optimization difficulty: high Fisher curvature may indicate ordinary training sensitivity, stiffness, or model identifiability problems.
- Predictive-processing or FEP-style accounts: the geometry may describe inference and prediction-error structure without requiring SRT's selection-reality framing.
- Model-choice artifact: the relevant parameterization, state space, or probability family may fail to match the real system whose `Psi_f` is being discussed.
- Computational cost: observed update burden may be better explained by hardware, sample size, Hessian curvature, or algorithmic inefficiency.

## 8. What would weaken this

This card should be downgraded toward E1 if:

- Fisher-geometric quantities do not distinguish SRT-relevant transition burden from ordinary model difficulty.
- a proposed Fisher proxy fails to track payability, recovery cost, lock-in, or stability under perturbation in a specified domain;
- the chosen statistical manifold is an analyst convenience rather than a structure used by the system under study;
- simpler accounts using KL divergence, optimization stiffness, prediction error, or computational resource limits explain the case equally well;
- the interpretation drifts from `Psi_f` into `d-value` without separately demonstrating stake-coupled concern and consequence return.

It should be routed to the contradiction ledger if future operational cards repeatedly fail to connect Fisher structure to any SRT-relevant burden or payability condition.

## 9. Boundary: what this does not prove

This card does not establish any canonical SRT definition.

Specifically:

- Fisher information geometry does not define `Psi_f`.
- Fisher geometry does not establish `d-value`.
- statistical distinguishability alone does not imply stake-coupled concern.
- this card is a structural convergence / bridge-support candidate, not proof of SRT.
- Fisher-Rao geometry should not be read as a direct measure of consciousness, subjecthood, value, or irreversible consequence.
- no bridge or evidence card may override the canonical `Psi_f` or `d-value` files.

## 10. Upgrade path

Possible next steps:

1. Create a bridge note comparing Fisher-Rao geometry, natural gradient, and the `Psi_f` formal projection.
2. Define a scoped lab hypothesis only for a specific system class, such as model update burden, neural state transition, or behavioral recovery cost.
3. Upgrade toward E3 only if a measurable Fisher-style quantity predicts transition burden, recovery cost, payability, or lock-in better than simpler alternatives.
4. Keep `d-value` out of scope unless stake-coupled concern, consequence return, and self-modulation are independently operationalized.
5. Add pressure entries if Fisher projections fail, overgeneralize, or collapse into generic optimization difficulty.

## Sources Checked

The following sources were checked online for this draft. They are used only to support the external information-geometry background, not to establish SRT.

- [S1] Frank Nielsen, "An elementary introduction to information geometry," *Entropy* 22(10), 1100, 2020. Also available as arXiv:1808.08271. Used as a high-quality overview of statistical manifolds, Fisher-Rao geometry, divergences, and the information-geometric setting. <https://www.mdpi.com/1099-4300/22/10/1100>
- [S2] Shun-ichi Amari, *Information Geometry and Its Applications*, Springer, 2016. Used as an authoritative monograph on information geometry and its applications. <https://link.springer.com/book/10.1007/978-4-431-55978-8>
- [S3] Shun-ichi Amari, Ryo Karakida, and Masafumi Oizumi, "Fisher Information and Natural Gradient Learning in Random Deep Networks," *Proceedings of Machine Learning Research* 89, 2019. Used for the machine-learning claim that parameter spaces can be treated as Riemannian manifolds with the Fisher information matrix as metric. <https://proceedings.mlr.press/v89/amari19a.html>
- [S4] Hông Vân Lê, "The uniqueness of the Fisher metric as information metric," *Annals of the Institute of Statistical Mathematics* 69, 879-896, 2017. Used for the uniqueness / invariance boundary around the Fisher metric. <https://link.springer.com/article/10.1007/s10463-016-0562-0>
- [S5] Nihat Ay, Jürgen Jost, Hông Vân Lê, and Lorenz Schwachhöfer, *Information Geometry*, Springer, 2017. Used as a reference for modern information geometry and invariant metric context. <https://link.springer.com/book/10.1007/978-3-319-56478-4>
