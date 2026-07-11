---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-CONSTRUCT-HARDENING-20260710
type: construct_hardening
status: draft_v0_1
layer: paper_working
epistemic_layer: bridge
claim_mode: proposal
claim_level: P3-P4
canonical: false
created: 2026-07-10
depends_on:
  - PAPER-SELECTIVE-RESYNCHRONIZATION-SOURCE-AUDIT-20260710
  - PAPER-SELECTIVE-RESYNCHRONIZATION-REFRAMING-MEMO-20260710
---

# Construct Hardening: Selective Resynchronization

## 0. Decision in brief

**Provisional verdict: CONDITIONAL GO.**

Selective resynchronization can be made non-metaphorical, but it has not yet earned status as a distinct empirical construct. Its strongest differentiating claim is not that a system recovers after perturbation. It is that a measurable pre-second-shift trajectory—opening, selective incorporation, and restabilization—predicts later adaptation capacity after current performance has been matched.

The construct should be retained only if that prediction survives controls for ordinary adaptation, current accuracy and loss, optimizer state, training budget, representation drift, and established continual-learning outcomes. SRT provenance does not count toward construct validity.

## 1. Provenance and authority boundary

The source-level intuition is recorded in the remote non-canonical trace `SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md`. The only imported chain is:

\[
\text{desynchronization / randomization}
\rightarrow
\text{comparison}
\rightarrow
\text{selective resynchronization}
\rightarrow
\text{path formation}
\rightarrow
\text{renewed adaptive scaffold}.
\]

The trace is construct provenance, not evidence or definition authority. The present document supplies a domain-specific operational proposal that can fail independently of the source intuition.

The preliminary literature search did not identify “selective resynchronization” as an established machine-learning construct. That observation is not a global novelty proof. “Resynchronization” already has domain-specific meanings, including sensorimotor correction after perturbation, so the paper must define its use and avoid implying neural-oscillatory or phase synchronization. Perturbation-response work in paced finger tapping, for example, uses resynchronization for return to sensorimotor timing after a stimulus change; that is narrower and does not include selective incorporation or retained future adaptability ([Laje et al., 2019](https://www.nature.com/articles/s41598-019-54133-x)).

## 2. Unit of analysis and temporal windows

The unit of analysis is a **training run under a prespecified environment sequence** `A -> B -> C`. The construct is attributed to a run trajectory, not to an isolated parameter vector.

The confirmatory protocol fixes four windows before outcome analysis:

| Window | Definition | Main role |
|---|---|---|
| `W_A` | final `K_A` checkpoints before the `A -> B` shift | estimate stable pre-perturbation baseline |
| `W_B^open` | first `K_open` checkpoints after the `A -> B` shift | measure perturbation-induced opening |
| `W_B^stable` | prespecified late-`B` window or earliest qualifying stability window | assess selective incorporation and restabilization |
| `W_C^early` | first `K_C` updates/checkpoints after `B -> C` | measure retained adaptability |

`K_A`, `K_open`, `K_C`, checkpoint cadence, and late-`B` stability rules are selected on calibration runs or fixed from training-time considerations, then frozen. Confirmatory runs do not set thresholds from their observed outcomes.

## 3. Minimal and full operational definitions

### 3.1 Minimal operational definition

> **Selective resynchronization is a temporally ordered adaptation episode in which a controlled perturbation measurably disrupts a previously stable internal organization, a task-relevant subset of the induced change is retained in a new stable organization, and the resulting system remains able to adapt under a later mechanistically distinct perturbation.**

This definition has four clauses:

1. prior stability;
2. measurable opening beyond ordinary training noise;
3. selective, task-relevant restabilization rather than rollback or diffuse drift;
4. retained later adaptability.

### 3.2 Full operational definition for neural learning

A run exhibits full selective resynchronization only if all of the following are observed under the preregistered protocol:

1. **Stable baseline:** performance and selected internal measures are stable during `W_A`.
2. **Controlled opening:** the `A -> B` perturbation causes at least one primary desynchronization proxy to exceed its no-shift calibration envelope during `W_B^open`.
3. **Selective incorporation:** a non-trivial component of the early `B` representation change remains aligned with the stable `B` representation change, exceeds a temporal-permutation / matched-no-shift null, and is associated with performance under `B`.
4. **New rather than restored organization:** the stable `B` representation is distinguishable from the `A` representation and supports `B`; simple return to the pre-shift state is excluded.
5. **Restabilization:** late-`B` performance and internal dynamics meet prespecified stability criteria for a fixed duration.
6. **Retained adaptability:** after current `B` performance has been matched, the run retains positive early adaptation capacity under a mechanistically distinct `B -> C` shift.

No single proxy establishes the construct. Full classification is a conjunction of prespecified observations, while the primary confirmatory analysis keeps the measures continuous.

### 3.3 Circularity guard: pre-`C` signature versus full construct

Future adaptation capacity cannot both define the predictor and serve as its test outcome. The analysis therefore distinguishes:

- **candidate pre-`C` signature, `SR_preC`:** the `W_A -> W_B^open -> W_B^stable` pattern of opening, selective incorporation, current-environment performance, and restabilization; it excludes all `C` outcomes;
- **full selective resynchronization:** `SR_preC` plus retained adaptability observed in `W_C^early`.

The primary empirical test is:

> Does `SR_preC` predict retained adaptability under `C` beyond matched `B` performance and baseline controls?

If the answer is no, the full construct has not earned predictive validity even if the descriptive trajectory looks plausible.

## 4. Conditions

### 4.1 Necessary conditions

| Necessary condition | Operational test | Failure meaning |
|---|---|---|
| Stable pre-shift organization | low slope and bounded variance of `A` performance and internal measures in `W_A` | no interpretable baseline to disrupt |
| Perturbation-induced opening | primary `D` proxy exceeds a frozen no-shift envelope after `A -> B` | rigidity, imperceptible shift, or insensitive proxy |
| Change beyond estimator noise | effect exceeds repeat-probe, mini-batch and temporal-permutation controls | ordinary stochastic noise, not opening |
| Task-relevant incorporation | early-to-stable change overlap plus positive `B` relevance | diffuse drift or incidental alignment |
| New stable `B` organization | stable late-`B` performance and internal dynamics; non-equivalence to `A` representation | no restabilization or simple rollback |
| Retained later adaptability | positive `Q_C` under matched `B` performance | adaptive lock-in, rigidity, or collapse |

### 4.2 Non-necessary conditions

The following are **not** required:

- a Fisher-burden peak;
- a loss or accuracy dip immediately after perturbation;
- a specific optimizer, natural-gradient method, architecture, or learning rate;
- monotonic accuracy recovery;
- neural oscillatory phase synchronization;
- return to the old parameter vector or representation;
- preservation of every feature learned in `A`;
- a formal phase transition;
- consciousness, subjectivity, embodiment, ontological selection, or SRT acceptance.

### 4.3 Exclusion conditions

A run is not counted as full selective resynchronization when any of the following holds:

- **pure fluctuation:** high proxy variance without stable, task-relevant incorporation;
- **simple rollback:** late-`B` state returns to `A` without adequate `B` adaptation;
- **rigid non-response:** old organization persists and `B` adaptation remains inadequate;
- **diffuse disorganization:** perturbation-induced variability remains high or unstable and no reusable `B` organization forms;
- **adaptive lock-in:** `B` performance is good but later `C` adaptability falls below the preregistered reference or non-inferiority floor;
- **technical invalidity:** corrupt data, logging failure, or infrastructure error prevents the necessary measures from being computed. Technical invalidity is excluded, not relabeled as collapse.

## 5. Candidate measures and proxy status

### 5.1 Primary desynchronization proxies, `D_t`

The MVP uses two complementary primary measures rather than an unvalidated composite.

#### A. Mini-batch gradient disagreement

At fixed checkpoint `t`, compute gradients `g_{t,b}` on `m` stratified mini-batches from a fixed probe distribution. Define:

\[
D_t^{\mathrm{grad}}
=
1-
\frac{2}{m(m-1)}
\sum_{b<b'}
\frac{g_{t,b}^{\top}g_{t,b'}}
{\lVert g_{t,b}\rVert\lVert g_{t,b'}\rVert+\epsilon}.
\]

Interpretation: local disagreement among update directions. Limitations: batch composition, class imbalance, gradient scale, near-zero gradients, optimizer state, and label noise can raise or distort the measure. It is an **operational proxy for update-field conflict**, not a definition of desynchronization.

#### B. Representation-subspace displacement

For a fixed stratified probe set, let `Z_t^ell` be centered activations at layer `ell`. Define:

\[
D_t^{\mathrm{repr},\ell}
=
1-\operatorname{CKA}(Z_t^\ell,Z_A^\ell),
\]

where `Z_A^ell` is the `W_A` reference representation. CKA is chosen because it permits systematic representation comparison and is insensitive to isotropic scaling and orthogonal transformations, but those invariances do not make it a direct measure of functional change ([Kornblith et al., 2019](https://proceedings.mlr.press/v97/kornblith19a)). Limitations include layer choice, probe composition, nonlinear reparameterizations, and functionally silent drift. It is an **operational proxy for internal displacement**.

Primary reporting keeps `D_t^grad` and `D_t^repr` separate. A composite `D_t` is exploratory unless its weights are frozen on calibration data without access to `C` outcomes.

### 5.2 Selective-incorporation proxy

Let `Z_A`, `Z_{B,e}`, and `Z_{B,s}` be fixed-probe representations at the `A` baseline, an early-`B` checkpoint, and a stable-`B` checkpoint. Let `U_e` and `U_s` contain the top `k` right-singular vectors of `Z_{B,e}-Z_A` and `Z_{B,s}-Z_A`. Define retained change-subspace overlap:

\[
S_B
=
\frac{1}{k}
\lVert U_e^{\top}U_s\rVert_F^2.
\]

`k` is fixed from calibration data or an explained-variance rule defined before confirmatory outcomes. `S_B` is interpreted only when:

1. early displacement exceeds the no-shift envelope;
2. overlap exceeds temporal-permutation and matched-no-shift nulls;
3. stable `B` performance improves by a prespecified practically meaningful amount;
4. the stable state is not equivalent to `A`.

High overlap alone can arise from rigidity or a dominant nuisance direction. `S_B` is therefore a **weak process proxy with guardrails**, not a direct measure of “selection.”

### 5.3 Restabilization profile, `R_preC`

Before `C`, restabilization is represented by separate components:

- balanced performance on held-out `B` data;
- absolute slope and variance of `B` performance during `W_B^stable`;
- checkpoint-to-checkpoint representation velocity during `W_B^stable`;
- decline of `D_t^grad` from its early peak without return to the `A` representation;
- robustness to held-out `B` corruptions or background realizations.

A summary score may be used for visualization, but confirmatory models report components separately. Accuracy recovery and parameter stability are insufficient by themselves.

### 5.4 Retained adaptability, `Q_C`

The primary outcome is early improvement in balanced accuracy under `C`:

\[
Q_C^{\mathrm{AULC}}
=
\frac{1}{K_C}
\sum_{k=1}^{K_C}
\left[
\operatorname{BA}_C(k)-\operatorname{BA}_C(0)
\right].
\]

It is evaluated after matching models on current `B` performance. Secondary outcomes are updates or samples to a fixed `C` threshold, final `C` performance at a fixed budget, `A/B` forgetting after `C`, and relearning speed in an optional return probe.

`Q_C` is a **domain-level outcome measure of retained adaptability**. It is not SRT d-value, option count, consciousness, or a direct measure of `Ψ_f`. Recent work explicitly distinguishes loss of plasticity—the declining capacity to learn new material—from catastrophic forgetting of old material, supporting the need to report both rather than collapse them ([Dohare et al., 2024](https://www.nature.com/articles/s41586-024-07711-7)).

### 5.5 Fisher-geometric burden is not a construct component

For update `Delta theta_t`, the candidate predictor is:

\[
G_t
=
\frac{1}{2}
\Delta\theta_t^{\top}F_t\Delta\theta_t.
\]

`G_t` is a Fisher-induced quadratic transition measure. It is neither a necessary nor a sufficient condition for selective resynchronization. It is not `Psi_f`, complete selection cost, realized compute/energy cost, or an ontological friction measure.

The empirical Fisher must be labeled as an approximation, not treated as the true Fisher or the Hessian. The approximation can have pathological behavior and does not generally carry the curvature interpretation often assigned to it ([Kunstner et al., 2019](https://proceedings.neurips.cc/paper/2019/hash/46a558d97954d0692411c861cf78ef79-Abstract.html)).

## 6. Discriminant-validity matrix

| Adjacent construct | What it already measures | What selective resynchronization would additionally require | Empirical discriminator | Redundancy / kill implication |
|---|---|---|---|---|
| Adaptation | improved fit or performance under change | opening, selective incorporation, restabilization, and later adaptability | `SR_preC` predicts `Q_C` after matching `B` performance | kill if endpoint adaptation explains all outcomes |
| Recovery | return toward a previous functional level | formation of a new `B` organization rather than restoration of `A` | representational non-equivalence to `A` plus `B` relevance | kill if all successful runs are rollback |
| Synchronization | coordination or phase/activity alignment | task-relevant selective reorganization and future adaptability | coherence alone versus full process predictors | rename if only synchrony restoration is measured |
| Resynchronization | re-establishment of coordination after perturbation | selective retention of induced differences and later adaptation capacity | compare return-to-baseline with new-state trajectories | kill adjective “selective” if no retained-change discriminator exists |
| Plasticity | capacity to change or learn | episode-level transition organization and stable reuse | same plasticity score, different `SR_preC`, predict `Q_C` | kill if plasticity measures subsume the process profile |
| Retained plasticity | capacity to continue learning after prior training | a proposed pre-`C` mechanism/signature for why it is retained | `SR_preC` adds prediction beyond standard plasticity correlates | retain `Q_C`, drop new construct if no added prediction |
| Continual learning | learning from a sequence while managing transfer and forgetting | a local process model within a continual-learning episode | nested prediction and state-trajectory analyses | never claim a new field; kill if standard CL metrics suffice |
| Representation drift | internal feature change over time | structured, task-relevant retention followed by stability and `Q_C` | drift magnitude versus retained subspace and future outcome | kill if drift alone performs equally and process ordering adds nothing |
| Catastrophic forgetting | loss of previous-task performance | also distinguishes future learning capacity and current restabilization | report `A/B` retention separately from `Q_C` | construct fails if it merely re-labels forgetting |
| Critical transition | qualitative regime shift, possibly near a bifurcation | no bifurcation claim; only a controlled adaptation trajectory | test for actual order parameter/bistability before using the term | remove phase/critical language without dynamical evidence |
| Critical slowing down | increasing recovery time or autocorrelation near some transitions | successful reorganization after the shift and later adaptability | compare autocorrelation/recovery-rate baselines with `SR_preC` | treat as baseline only; it can win |
| Change-point detection | identifies when a data-generating or metric regime changes | evaluates whether and how adaptation becomes stable and reusable | BOCPD/CUSUM detection versus `R_preC` and `Q_C` prediction | detection alone cannot establish the construct |
| Robustness | performance under perturbation/corruption | dynamic reorganization plus future adaptation, not invariance alone | robust-but-rigid versus adaptively reorganized conditions | kill if static robustness predicts all relevant outcomes |
| Stability-plasticity dilemma | trade-off between retaining old knowledge and learning new knowledge | testable temporal decomposition of one transition episode | opening/restabilization features beyond retention/plasticity endpoints | drop new term if it adds no temporal prediction |
| Catastrophic collapse / optimization instability | failure to train or maintain usable function | target construct excludes these trajectories | fixed collapse controls and numerical diagnostics | classification must not aestheticize failure as exploration |

Continual-learning research already measures transfer and forgetting, including sequential-task methods such as GEM ([Lopez-Paz & Ranzato, 2017](https://proceedings.neurips.cc/paper/2017/hash/f87522788a2be2d171666752f97ddebb-Abstract.html)) and Fisher-weighted protection of previous tasks in EWC ([Kirkpatrick et al., 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5380101/)). The proposed increment is therefore limited: a preregistered process signature that predicts later adaptability beyond these endpoints.

Critical slowing down and change-point detection are comparators, not synonyms. Critical slowing down concerns loss of recovery rate near some transitions ([Dakos et al., 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2567225/)); BOCPD estimates posterior run length for abrupt changes ([Adams & MacKay, 2007](https://arxiv.org/abs/0710.3742)); CUSUM accumulates sequential evidence for a change ([Page, 1954](https://academic.oup.com/biomet/article-abstract/41/1-2/100/456627)). None by itself measures whether a new adaptive organization remains able to change again.

## 7. Four-state operational framework

### 7.1 Important correction: states versus run labels

The four categories are **window-specific dynamical states in a state machine**, not four mutually exclusive labels for an entire run. A successful run can move from stable `A` to a desynchronization-open state and later to selective resynchronization. “Productive desynchronization” is retrospective: before the later outcome is known, the state is labeled **desynchronization-open**.

### 7.2 State table

| State | Permitted window | Performance pattern | Internal-change pattern | Stability pattern | Future adaptability | Operational rule |
|---|---|---|---|---|---|---|
| Rigidity | `W_B^open` through late `B` | inadequate `B` improvement under fixed budget | both primary `D` measures remain below opening threshold, or change is abortive | old `A` organization persists | measured but not required for initial label; often low | low opening + poor `B` adaptation; high `A` retention does not rescue label |
| Desynchronization-open | `W_B^open` only | may fall, remain flat, or begin improving | at least one primary `D` proxy exceeds no-shift envelope; not yet attributable to pure noise | no new stable organization yet | unknown | temporary state; “productive” only if followed by valid restabilization |
| Candidate selective resynchronization (`SR_preC`) | `W_B^stable` | adequate held-out `B` performance | prior opening + above-null selective incorporation + non-equivalence to `A` | stable late-`B` behavior and internal velocity | deliberately not used in label | all pre-`C` criteria pass; this is the predictor in the primary test |
| Full selective resynchronization | after `W_C^early` | prior `B` criteria remain satisfied | same pre-`C` trajectory | stable `B` structure was reusable | `Q_C` exceeds frozen adequacy/non-inferiority rule | `SR_preC` plus retained adaptability |
| Disorganization / collapse | late `B` or after `C` | poor, unstable, or catastrophically degraded; may include transient success | persistent/diffuse `D`, incoherent drift, numerical instability, or no selective retention | no reusable organization | low or unmeasurable for scientific reasons | persistent opening without valid restabilization, catastrophic failure, or adaptive lock-in |

### 7.3 Precedence and adjudication rules

1. Infrastructure or data-pipeline failures are technical exclusions, not scientific states.
2. During `W_B^open`, a threshold-crossing run is desynchronization-open regardless of Fisher behavior.
3. At late `B`, low opening plus inadequate `B` adaptation is rigidity.
4. Persistent opening plus inadequate or unstable `B` adaptation is disorganization/collapse.
5. Adequate `B` performance without selective incorporation or internal stability is “endpoint adaptation without classified resynchronization”; it remains unclassified rather than forced into the target state.
6. `SR_preC` is assigned without seeing `C` outcomes.
7. `SR_preC` followed by inadequate `Q_C` is **adaptive lock-in**, not full selective resynchronization.
8. Fisher burden never determines state assignment.

### 7.4 Threshold policy

Primary inference uses continuous measures. State labels are secondary and descriptive.

- opening thresholds: fixed from the 95th percentile of matched no-shift calibration runs;
- adequate `B` performance: fixed practical floor and common-support band from pilot/calibration runs;
- stable window: fixed maximum absolute slope and variance based on no-shift/calibration behavior;
- selective-incorporation threshold: fixed against permutation/no-shift distribution;
- retained-adaptability adequacy: fixed non-inferiority margin or reference floor before confirmatory `C` outcomes;
- all thresholds undergo prespecified sensitivity analyses, but the primary threshold is never chosen for favorable state counts.

## 8. Boundary cases

| Case | Classification | Reason / required analysis |
|---|---|---|
| `B` performance recovers by returning to the `A` representation | simple rollback, not selective resynchronization | new-state and `B`-relevance criteria fail |
| Excellent `B` performance but low `Q_C` | adaptive lock-in | present success is separated from future adaptability |
| Large representation change with unchanged output | latent reorganization, initially unclassified | test held-out robustness, calibration, changed versus unchanged classes, and later `Q_C`; do not assume productivity |
| Large Fisher burden and successful adaptation | classification independent of Fisher | supports Fisher only if incremental prediction survives controls |
| Small Fisher burden and failed adaptation | rigidity or collapse based on `D/R/Q`, not Fisher | directly permitted by the framework |
| Short apparent recovery followed by long collapse | disorganization/collapse | fixed stability duration prevents premature success label |
| High gradient disagreement caused by class imbalance | possible pseudo-opening | use balanced probe gradients and imbalance-matched nulls |
| High representation drift caused by scaling or nuisance background | possible pseudo-opening | CKA invariances, held-out backgrounds, task relevance, and subspace-retention controls |
| Stable `B` accuracy but highly unstable calibration or robustness | endpoint adaptation without classified resynchronization | accuracy alone is insufficient |
| Low `A` retention but high `B` and `C` adaptability | possible selective resynchronization with forgetting | report forgetting separately; construct does not require perfect preservation, but severe forgetting may limit interpretation |
| Strong `A` retention, weak `B` learning | rigidity | retention is not equivalent to adaptability |
| `C` differs only by another intensity of the `B` corruption | invalid test of future adaptability for the primary analysis | `B` and `C` must differ mechanistically |

## 9. Construct-retention criteria

The term may advance to a full manuscript only if the MVP supplies all of the following:

1. **Reliability:** primary `D`, incorporation, and restabilization measures have acceptable seed-level and probe-resampling reliability.
2. **Discriminant validity:** rigidity, open, restabilized, and disorganized anchor conditions are distinguishable without using Fisher burden.
3. **Non-circular prediction:** `SR_preC` predicts `Q_C` when `C` outcomes were not used to form `SR_preC`.
4. **Incremental validity:** prediction persists after matching/controlling `B` accuracy and loss, training budget, optimizer/architecture, and standard plasticity/forgetting correlates.
5. **Noise discrimination:** selective-incorporation measures exceed matched no-shift and temporal-permutation controls.
6. **Mechanism separation:** the result appears for at least two mechanistically distinct shift transitions or survives a shift-order robustness analysis.
7. **Threshold robustness:** conclusions do not depend on one favorable state-classification cutoff; continuous models agree in direction.
8. **Null openness:** Fisher may tie or lose without forcing reinterpretation of the construct result.

## 10. Construct kill criteria

Any of the following is sufficient to withdraw or substantially rename the construct:

1. After matched `B` performance, current accuracy/loss and ordinary controls explain `Q_C`, while `SR_preC` adds no reliable out-of-sample prediction.
2. “Selective incorporation” cannot be distinguished from drift magnitude, stochastic noise, or a no-shift/permutation null.
3. The state assignments are unstable under reasonable probe resampling or prespecified threshold sensitivity.
4. Ordinary adaptation, recovery, retained-plasticity, or continual-learning metrics predict the outcomes equally well and the temporal process variables add no explanatory value.
5. The predicted pattern appears only under one shift mechanism, one architecture, selected seeds, or post hoc thresholds.
6. The construct requires `Q_C` to define `SR_preC`, creating circular confirmation.
7. Successful cases are only simple return to the old state.
8. The only apparent support comes from Fisher behavior while non-Fisher process and outcome measures fail.

If criteria 1 or 4 hold, the recommended action is to retain the useful two-shift retained-adaptability protocol and drop “selective resynchronization” as a distinct scientific construct.

## 11. Claim-status ledger

| Statement | Status |
|---|---|
| CKA can compare representation similarity under stated invariances | Standard method |
| BOCPD and CUSUM detect changes in monitored sequences | Standard methods |
| `SR_preC` operationalization above is scientifically useful | New method proposal; unvalidated |
| Four states are reliably distinguishable | Empirical hypothesis |
| `SR_preC` predicts `Q_C` beyond current performance | Primary empirical hypothesis |
| Fisher burden adds incremental prediction | Secondary empirical hypothesis |
| The source-intuition chain motivated the construct | SRT-inspired provenance statement |
| The construct proves SRT or measures `Psi_f` | Prohibited / unsupported |

## 12. Stage-2 verdict

**CONDITIONAL GO.** The construct now has a non-circular primary test, explicit exclusions, discriminant comparators, and kill criteria. It has not yet demonstrated distinctness from retained plasticity or the stability-plasticity problem. Proceed to the MVP only; do not yet write a supportive empirical paper or treat the construct as established.
