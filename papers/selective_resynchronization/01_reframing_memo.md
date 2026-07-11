---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-REFRAMING-MEMO-20260710
type: reframing_memo
status: draft_v0_2
layer: paper_working
epistemic_layer: bridge
claim_mode: proposal
claim_level: P3-P4
canonical: false
created: 2026-07-10
revised: 2026-07-10
depends_on:
  - PAPER-SELECTIVE-RESYNCHRONIZATION-SOURCE-AUDIT-20260710
---

# Reframing Memo: From Fisher Identity to Selective Resynchronization

## 0. Editorial decision

The old Entropy manuscript should not be revised as an identity or proof paper. It should be replaced by a **preregistered theory-and-method proposal written in Stage-1-style / registered-report-style form**, with planned experiments and explicit falsification conditions. This wording describes the manuscript's internal design discipline; it does **not** claim acceptance into, or compliance with, a journal's formal Registered Report process.

Recommended article type for v0.1:

> **Registered-report-style theory-and-method proposal with a staged empirical protocol.**

Reason:

1. No new selective-resynchronization experiment has been completed.
2. The old reported experiments are not repository-verifiable because code, raw data and figures are missing.
3. The paper has one proposed contribution: an operational framework for studying selective resynchronization. The four-state taxonomy, two-shift protocol, retained-adaptability outcome and comparative Fisher test are components needed to make that single framework testable; they are not parallel contributions.
4. Writing an empirical-results paper now would either recycle unverifiable pilot numbers or invite fabricated `[RESULTS PENDING]` prose to masquerade as completed work.

If the full experiment plan is later implemented, the manuscript can be converted into an empirical methods paper without changing its conceptual spine.

Provisional field / venue type:

- primary: neural-learning dynamics, continual learning, distribution shift or machine-learning methodology;
- secondary: complex adaptive systems or applied information geometry, but only after the empirical protocol is executed;
- poor fit: ontology / consciousness journals, pure mathematical information geometry, or a broad SRT theory venue.

Literature positioning initiated in Stage 2 and still requiring completion before full drafting:

- nonstationary and distribution-shift learning;
- continual learning and the plasticity–stability problem;
- catastrophic forgetting, relearning and forward transfer;
- representation drift and feature-subspace change;
- synchronization / coordination in adaptive systems;
- critical transitions and early-warning indicators;
- Fisher information, empirical Fisher, natural gradient and curvature approximations;
- online change-point detection, including BOCPD and CUSUM.

No new reference should be inherited from the old bibliography without verification. Unverified slots in the later paper should remain `[CITATION NEEDED]`.

---

## 1. Old versus new positioning

| Dimension | Old manuscript | New manuscript |
|---|---|---|
| Primary question | Is selection cost a Fisher information metric? | How do adaptive systems reorganize perturbation-induced variability into stable adaptation while preserving future adaptability? |
| Fisher role | Proposed identity and central answer | Candidate local transition measure to be compared against simpler baselines |
| SRT role | Implicit source of ontological interpretation and proof target | Stated research heuristic that motivates one domain-level bridge hypothesis |
| Main outcome | Change detection / Fisher-spectrum spike | Selective resynchronization and retained adaptability after sequential shifts |
| Empirical structure | One regime shift | At least two environmental changes, with current adaptation and future adaptation evaluated separately |
| Failure posture | Fisher expected to reveal ontological friction | Fisher may add value, reduce to KL/curvature, lose to simple metrics or fail entirely |
| Claim level | Mixed mathematics, ontology and empirical claims | Established mathematics / method proposal / empirical hypothesis / SRT interpretation kept separate |
| Article type | Formal-interpretive empirical paper | Preregistered theory-and-method proposal in Stage-1-style / registered-report-style form |

---

## 2. Core research question

### Primary question

> **How do adaptive systems transform perturbation-induced desynchronization into stable adaptation while preserving the capacity for future adaptation?**

### Measurement question

> **Can Fisher-geometric transition measures help distinguish productive resynchronization from rigidity, noise, and collapse in neural learning?**

### Negative-control question

> **Do Fisher measures add predictive information beyond loss, accuracy, output KL, gradient norm, parameter distance, predictive entropy, representation drift, Hessian / sharpness estimates and generic change-point detectors?**

The paper remains valuable if the answer to the measurement question is “no,” provided the experiment clarifies which simpler measures distinguish the four states and whether current performance predicts future adaptability.

---

## 3. Working construct: selective resynchronization

### 3.1 Domain-specific working definition

> **Selective resynchronization is a process through which an adaptive system reorganizes perturbation-induced variability into a new, stable, and reusable coordination structure while retaining the capacity for subsequent adaptation.**

In the neural-learning domain, the term should be admitted only when all of the following are empirically assessed:

1. a controlled perturbation disrupts the pre-existing coordination pattern;
2. the system exhibits structured internal change rather than only measurement noise;
3. a new coordination pattern stabilizes;
4. the new pattern supports performance under the changed environment;
5. acquired structure is not immediately erased by return or retention tests;
6. the system retains measurable capacity to adapt to a later shift.

This is a working empirical construct, not an SRT canonical definition and not a theorem.

### 3.2 Why the term may add something

The proposed increment is not a synonym for “the model adapted.” It is a conjunction of:

- perturbation-induced opening;
- selective retention and reorganization;
- renewed internal coordination;
- stable use under the current environment;
- preservation of later adaptability.

The term earns its place only if this conjunction produces discriminating predictions that are not captured by a single existing label.

### 3.3 Relabeling risk

The paper must directly compare the construct with adjacent concepts:

| Existing concept | What it already captures | Proposed residual role for selective resynchronization | Drop condition |
|---|---|---|---|
| Adaptation | improved fit to a changed environment | requires a structured opening-to-restabilization trajectory plus later adaptability | drop the new term if current performance recovery is sufficient |
| Recovery | return toward a prior functional level | allows formation of a new stable structure rather than simple return | drop if the data cannot distinguish reorganization from rollback |
| Synchronization | coordination / phase or activity alignment | adds selective retention, task relevance and future adaptability | drop if coherence alone explains the outcomes |
| Plasticity–stability trade-off | balancing change and retention | specifies an episode-level temporal sequence and four failure states | drop if it adds no testable temporal or state distinction |
| Continual learning | learning under task sequences while limiting forgetting | provides a candidate process-level signature within continual learning | do not claim a new field; treat continual learning as the host literature |
| Phase transition | qualitative regime change, sometimes with an order parameter | may supply transition language if a genuine regime boundary is demonstrated | do not use “phase transition” as a theorem or metaphor without evidence |
| Critical slowing down | early-warning dynamics near some transitions | possible baseline signature, not the adaptive reorganization itself | drop any special claim if standard warning metrics suffice |
| Representation drift | internal feature change | one component of desynchronization / reorganization | never equate drift with success |

If selective resynchronization does not add incremental description or prediction beyond these literatures after proper citation review, the term should be withdrawn rather than defended rhetorically.

---

## 4. Four-state dynamical taxonomy

| State | Internal opening | Current-environment adaptation | New coordination stability | Future adaptability | Operational reading |
|---|---:|---:|---:|---:|---|
| Rigidity | low or abortive | poor | old structure remains fixed | often low | surface stability without adequate adaptation |
| Productive desynchronization | transient and structured | incomplete / rising | not yet established | unresolved | an intermediate opening state, not a success outcome by itself |
| Selective resynchronization | transient opening followed by selective restabilization | good | new structure stable and reusable | retained | target process |
| Disorganization / collapse | persistent or diffuse | poor / unstable | no reusable coordination | low | noise, catastrophic forgetting, unstable lock-in or failure to recover |

Two additional controls are required:

- **Simple rollback**: apparent recovery produced by returning toward the old state rather than learning the new environment.
- **Noisy success**: acceptable current accuracy achieved without stable internal organization, potentially failing under the second shift.

Desynchronization is therefore not inherently productive. Its status is determined retrospectively by structured restabilization and future-adaptation outcomes.

---

## 5. Provisional variables and measurement decisions

All variables below are empirical working variables. None is a direct measure of SRT ontology.

### 5.1 Desynchronization: `D_t`

Recommended MVP primary measures:

1. **Mini-batch gradient disagreement**: normalized dispersion or pairwise cosine disagreement among gradients computed on controlled mini-batches.
2. **Representation-subspace displacement**: change in a fixed probe set's feature subspace, measured by principal angles or a CKA-based distance at selected layers.

Why use two measures:

- gradient disagreement is sensitive to conflict in the immediate update field;
- representation displacement tracks internal structural movement;
- either measure alone can reflect ordinary stochastic noise, scale changes or estimator artifacts.

Noise controls:

- matched no-shift training windows;
- label-preserving augmentations;
- repeated probe evaluations;
- gradient estimates at fixed parameter states;
- seed-level dispersion;
- shuffled-label or temporally permuted controls where appropriate.

`D_t` should be treated as a vector or preregistered pair of measures in the primary analysis. A single composite may be reported only as exploratory unless its construction is fixed before outcome analysis.

### 5.2 Fisher-geometric burden: `G_t`

Primary candidate:

\[
G_t
=
\frac{1}{2}
\Delta\theta_t^\top
F_t
\Delta\theta_t.
\]

Path accumulation:

\[
\mathcal{G}_{t_0:t_1}
=
\sum_{t=t_0}^{t_1}
\frac{1}{2}
\Delta\theta_t^\top
F_t
\Delta\theta_t.
\]

Names permitted in the paper:

- Fisher-geometric update burden;
- local geometric transition load;
- Fisher-induced transition measure.

Names not permitted:

- complete selection cost;
- `Ψ_f` itself;
- ontological friction measured directly.

Recommended estimator for the first implementable version:

- empirical Fisher on a fixed, stratified probe set;
- compute the quadratic form through per-sample scores without materializing the full matrix:

\[
G_t^{\mathrm{EF}}
=
\frac{1}{2B}
\sum_{i=1}^{B}
\left(
s_i^\top \Delta\theta_t
\right)^2,
\qquad
s_i = \nabla_\theta \log p_\theta(y_i\mid x_i).
\]

Required sensitivity analyses:

- empirical Fisher versus model-sampled-label Fisher where feasible;
- full-probe quadratic form versus diagonal / block / K-FAC approximation;
- probe-set size and damping;
- layerwise versus whole-model values;
- alternative parameterizations or functionally equivalent rescalings where feasible;
- comparison with output KL, because locally `G_t` may reduce to a KL change;
- comparison with Hessian, gradient norm and sharpness estimates.

Projection failure is recorded if Fisher measures are unstable under reasonable estimator choices, primarily reflect redundant parameter directions, or add no outcome prediction beyond simpler function-space measures.

### 5.3 Resynchronization: `R_t`

`R_t` should not be defined as accuracy recovery or parameter stability alone. The primary outcome should remain a multidimensional profile:

1. **internal coherence recovery**: reduction of within-probe representation / prediction inconsistency after the opening phase;
2. **new-distribution performance**: task performance under environment B;
3. **retention**: preserved performance or reusable structure on the relevant A/B test set;
4. **post-adaptation robustness**: stability under matched corruption or resampling after adaptation.

A composite resynchronization score may be preregistered for summary visualization, but the four components must also be reported separately. A model does not count as resynchronized if a high composite is driven only by accuracy.

### 5.4 Retained adaptability: `Q_t`

Preferred paper-facing term:

> **retained adaptability**

Acceptable alternatives:

- future adaptation capacity;
- residual plasticity;
- reselectability, only after a narrow machine-learning definition and with an explicit statement that it is not canonical d-value or option count.

Primary measures after a second shift `B -> C`:

- adaptation speed or time-to-threshold;
- area under the learning curve;
- samples / updates required to reach matched performance;
- final C performance under a fixed budget;
- B and A forgetting after C;
- relearning speed after a controlled return condition.

Critical design rule:

> Compare models at matched current performance on B before measuring adaptation to C.

Without performance matching, `Q_t` can be confounded by the simple fact that one model learned B better.

---

## 6. Rewritten hypotheses and explicit null outcomes

### H1. Temporal-organization hypothesis

Successful adaptation is predicted to show a reproducible ordering:

\[
\text{perturbation}
\rightarrow
D_t \uparrow
\rightarrow
G_t \text{ transiently increases}
\rightarrow
R_t \uparrow
\rightarrow
Q_t \text{ remains above a preregistered floor}.
\]

This ordering must be compared with:

- rigidity: low `D_t`, limited restructuring, poor B adaptation;
- persistent disorganization: sustained `D_t`, absent `R_t`, low `Q_t`;
- rollback: recovery of old structure without adequate B learning;
- ordinary stochastic fluctuation: `D_t` changes without later outcome relevance.

H1 fails if the ordering is not reproducible, if `D_t` is indistinguishable from noise, or if equally successful adaptation occurs without the predicted transition sequence.

### H2. Productive-transition-window hypothesis

Adaptation outcomes may be non-monotonic in cumulative geometric burden. Low burden may indicate insufficient opening; intermediate burden may support reorganization; high burden may accompany instability or collapse.

Permitted names:

- feasible transition regime;
- productive transition window;
- intermediate-burden adaptation regime.

H2 fails if the relation is monotonic, absent, task-specific without replication, or better explained by learning rate, update norm, output KL or generic optimization instability.

### H3. Limited incremental-prediction hypothesis

Fisher burden alone is not expected to determine success. The preregistered comparison is:

\[
\text{baseline controls}
\quad\text{vs}\quad
G_t + \text{baseline controls}
\quad\text{vs}\quad
G_t + D_t + \text{baseline controls}.
\]

Outcomes are `R_t` components and `Q_t` components.

H3 succeeds only if Fisher measures add out-of-sample predictive information beyond the baseline set. If Fisher loses to output KL, gradient norm, representation drift or a simple change-point score, the correct conclusion is that Fisher has limited or no incremental value in that regime.

### H4. Current-performance / future-adaptability dissociation

Models with matched current B performance may retain different capacity to adapt to C. The analysis compares their preceding Fisher path, representation reorganization, forgetting and C adaptation.

H4 fails if matched-performance models do not differ reliably in later adaptation, or if any difference is fully explained by ordinary controls such as optimizer state, learning-rate schedule, model capacity or training budget.

---

## 7. Content disposition: retain, rewrite, remove

| Old content | Decision | Reason / new placement |
|---|---|---|
| Fisher metric definition | Retain | established background, with citation and regularity conditions |
| local KL quadratic expansion | Retain | motivates `G_t` as a local candidate measure, not `Ψ_f` identity |
| natural gradient | Retain as related method / comparison | optimizer geometry is relevant but not evidence for selective resynchronization |
| empirical Fisher + fixed probe + Gram trick | Retain and update | executable measurement method; add approximation and cost audit |
| Fisher spectrum trace / eigenvalue / condition proxies | Retain as secondary measures | compare with quadratic burden and simple baselines; no privileged status |
| mixture and Digits tasks | Rewrite as Stage-0 / Stage-1 debugging seeds | all old results must be rerun; add two-shift sequence and future-adaptation outcome |
| BOCPD | Retain as verified baseline after reimplementation | it is a change detector, not a resynchronization measure |
| CUSUM | Add as verified baseline | old abstract mentioned it but no result was found |
| curvature focusing theorem | Remove from main claim spine | standard geometry does not establish stochastic learning reorganization; optional background / exploratory appendix only if assumptions are complete |
| “insight-like event” language | Remove | construct and labels are absent; use controlled adaptation transitions |
| `κ_body` as existential gate | Remove | supervised stream coupling does not establish embodied ontological cost |
| `Ψ_f ≡ g_F` / Ax-IG-1 | Delete | violates current canonical and mathematical object-type boundary |
| `d log d` theorem / care-dimension scaling | Delete from main paper | assumption-driven, conflates capacity and stake; `[PROOF REQUIRED]` if ever revived separately |
| PCI / consciousness extrapolation | Delete | outside domain and unsupported by neural-network results |
| old result table | Quarantine | may guide debugging but cannot appear as evidence without reproduction |

---

## 8. Minimal empirical route and expansion route

The executable protocol is specified in `03_two_shift_protocol.md`. The reframing decision is:

### Minimum viable sequence

1. **Mechanism debugging**: a synthetic or small tabular / low-dimensional nonstationary task with known perturbation timing and interpretable state changes.
2. **Fashion-MNIST-level task**: MLP and small CNN; controlled `A -> B -> C` shifts.
3. Multiple random seeds and fixed compute budgets.
4. At least two optimizer / regularization regimes that can plausibly generate rigidity versus instability.
5. Primary `D`, `G`, `R` and `Q` measures plus mandatory simple baselines.

### Expansion sequence

1. CIFAR-10 with a small CNN and a residual architecture.
2. Multiple shift families: corruption, class imbalance, texture/background and label-rule / task change.
3. SGD, Adam, natural-gradient / Fisher-preconditioned method, strong regularization, SAM-like method and replay / continual-learning baseline.
4. Estimator ablations for empirical Fisher, diagonal / block approximations and function-space KL.

The minimum version must be independently publishable as a null-friendly methods study. CIFAR is an expansion, not a prerequisite for starting implementation.

---

## 9. Single main contribution

The manuscript will make exactly one main contribution:

> **An operational framework for studying selective resynchronization: how an adaptive system reorganizes perturbation-induced variability into a stable adaptation while retaining capacity for subsequent adaptation.**

Everything else is subordinate to this framework:

| Component | Function within the one contribution | Not claimed as |
|---|---|---|
| Four-state taxonomy | supplies contrast classes and failure modes | an independent taxonomy contribution or universal law |
| `A -> B -> C` protocol | separates present adaptation from later adaptability | a new continual-learning benchmark by itself |
| retained adaptability outcome | makes the future-capacity clause testable | an SRT d-value or direct measure of reselectability |
| desynchronization and restabilization proxies | test the proposed process structure | definitions of the construct |
| Fisher-geometric burden | tests one candidate transition predictor | the construct, `Ψ_f`, selection cost or privileged answer |

The contribution survives only if the framework yields a discriminating, reproducible prediction beyond ordinary adaptation/recovery language. It is a domain-level method proposal, not a claim that SRT is proven.

---

## 10. Relationship to SRT

SRT contributes only a research heuristic:

- selection can be read as structured stabilization rather than mere endpoint choice;
- useful transitions may require non-zero but manageable burden;
- current stabilization should be evaluated together with preservation of future selection / adaptation capacity;
- perturbation is useful only when variability is selectively reorganized rather than merely amplified.

The paper-level bridge hypothesis is:

> In nonstationary neural learning, successful adaptation may be better characterized by a structured opening–restabilization trajectory plus retained adaptability than by endpoint convergence alone; Fisher geometry is one candidate measurement interface for the transition burden.

Required boundary statements for the eventual manuscript:

1. The study does not prove SRT.
2. It operationalizes one SRT-inspired bridge hypothesis in neural learning.
3. Results may support, weaken or reject that bridge.
4. Fisher geometry is not the complete definition of `Ψ_f`.
5. Machine-learning results do not establish claims about ontology, consciousness, subjectivity, stake or reality-selection.

If Fisher loses but the four-state taxonomy and two-shift protocol work, the paper remains valid while the Fisher bridge is weakened. If the taxonomy itself adds no value beyond established continual-learning concepts, the term selective resynchronization should also be weakened or removed.

---

## 11. Risk register and stop conditions

| Risk | Diagnostic | Stop / downgrade condition |
|---|---|---|
| Relabeling existing constructs | systematic comparison with adaptation, continual learning, plasticity–stability, drift and critical-transition literature | remove the new term if it adds no discriminating prediction |
| `D_t` is noise | no-shift, permutation, probe-repeat and seed controls | reject a proxy if it cannot distinguish structured opening from stochastic variance |
| `R_t` is accuracy in disguise | report components separately; residualize / control current performance | reject the composite if internal coherence, retention and robustness add nothing |
| `Q_t` is confounded by B mastery | matched-performance evaluation before C | do not claim retained adaptability without successful matching / adjustment |
| Fisher reduces to output KL | direct comparison and residual prediction | report projection collapse; Fisher has no special added role in that regime |
| Fisher proxy is parameterization / estimator fragile | estimator, damping, probe and rescaling sensitivity | withdraw strong Fisher conclusions if rankings or effects are unstable |
| Intermediate-burden window is tuning artifact | hold learning rate / update norm / budget constant; cross-task replication | reject H2 if the window disappears under ordinary controls |
| Change-point detector mistaken for adaptation measure | separate detection, resynchronization and future-adaptation endpoints | never infer success from early detection alone |
| Old results cannot be reproduced | clean rerun from new code | exclude all old numbers from the new paper |
| SRT interpretation outruns domain result | claim audit and separate Relationship to SRT section | delete ontology / consciousness extrapolation rather than qualify it rhetorically |

Hard stop conditions for the paper program:

1. selective resynchronization cannot be operationally distinguished from ordinary adaptation or recovery;
2. no `D -> R -> Q` structure replicates across seeds or perturbation families;
3. current performance and future adaptability do not dissociate under controlled matching;
4. all Fisher measures are unstable or add no information and no non-Fisher measure supports the proposed process taxonomy;
5. the only positive patterns require post hoc thresholds, selected seeds or one task family;
6. the core result depends on interpreting a neural network as a subject, consciousness-bearing system or ontological selector.

---

## 12. Claim-level map for the planned manuscript

| Planned claim | Status |
|---|---|
| Fisher metric defines local statistical geometry | Established mathematics, subject to standard assumptions and citation |
| `G_t` is a chosen Fisher-induced quadratic transition measure | New method proposal / standard construction used for a new purpose |
| four dynamical states can be empirically distinguished | Empirical hypothesis |
| a productive intermediate-burden regime exists | Empirical hypothesis |
| Fisher adds predictive value beyond controls | Empirical hypothesis, explicitly null-friendly |
| current performance and future adaptability dissociate | Empirical hypothesis |
| selective resynchronization is useful as a construct | Methodological / construct-validity claim to be earned empirically |
| the framing is motivated by SRT | SRT-inspired interpretation |
| Fisher measures `Ψ_f` or proves SRT | Prohibited claim |
| neural-network results imply ontology, consciousness or subjectivity | Unsupported extrapolation; prohibited |

---

## 13. Provisional title direction

Do not finalize the title before the literature-positioning and experiment-plan phase. The current editorial preference is to put the phenomenon first and Fisher second.

Provisional working title:

> **Beyond Convergence: Selective Resynchronization and Retained Adaptability in Neural Learning**

Possible measurement subtitle:

> **A Comparative Test of Fisher-Geometric Transition Measures under Sequential Distribution Shift**

This is a positioning placeholder, not the final title / venue decision.

---

## 14. Stage-2 scope and gate

The first-stage direction has been approved. The current stage is limited to construct hardening, an executable two-shift protocol, a preregistered analysis plan and a paper skeleton. It must not produce an abstract, a Results section, a supportive conclusion or the full English manuscript.

The stage-2 outputs must determine whether the construct earns further development. Advancement to full drafting is conditional on:

1. a non-circular operational definition that separates a pre-`C` candidate signature from the later `Q` outcome;
2. discriminant validity relative to adaptation, recovery, plasticity and continual learning;
3. a feasible matched-performance `A -> B -> C` experiment;
4. preregistered failure, null and stopping interpretations;
5. a scientific `GO`, `CONDITIONAL GO` or `NO-GO` decision independent of SRT provenance.
