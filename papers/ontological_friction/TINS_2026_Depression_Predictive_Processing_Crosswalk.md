---
id: SRT-OF-TINS-DEPRESSION-CROSSWALK-202607
kind: literature_crosswalk
status: bounded_noncanonical_note
claim_mode: bridge_hypothesis
canonical: false
authority_level: paper_support_note
created: 2026-07-25
source_paper: "Strube & Pizzagalli, Brain rhythms of depression: A predictive processing perspective"
source_doi: "10.1016/j.tins.2026.06.006"
target_paper: "A Translational Cross-Modal Control-Cost Framework for Executive Breakdown"
target_path: "papers/ontological_friction/paper_ontological_friction_frontiers_submission.md"
---

# TINS 2026 depression review × executive-friction paper: bounded crosswalk

> **Status and boundary**
>
> This note records a literature-to-paper bridge. It is not canonical SRT, does not redefine `Psi_f`, and does not claim that electroencephalography (EEG) directly measures executive friction. The source review supplies a plausible upstream predictive-processing account of depression; the Frontiers paper supplies a downstream control-cost account of the knowing-doing gap.

## 1. Source and target

**External source**

- Andreas Strube and Diego A. Pizzagalli, “Brain rhythms of depression: A predictive processing perspective,” *Trends in Neurosciences* (2026), DOI: `10.1016/j.tins.2026.06.006`.
- Core external claim: in depression, outcomes and errors can be neurally registered while positive, surprising, or corrective information exerts insufficient leverage on subsequent belief revision. The review further interprets elevated beta dynamics as compatible with model maintenance and attenuated RewP/reward-delta/P300 responses as compatible with reduced updating impact.

**SRT-Pub target**

- [`paper_ontological_friction_frontiers_submission.md`](paper_ontological_friction_frontiers_submission.md)
- Core target claim: the knowing-doing gap arises when the control cost of maintaining or switching an active state (`Psi_f`) exceeds the available control budget (`P_sel`).

## 2. One-sentence relationship

The TINS review explains **why corrective evidence may fail to revise the default model**, whereas the executive-friction paper explains **why, once that default model and policy landscape are established, the person may still be unable to implement an alternative action even when declarative knowledge is partly intact**.

The relationship is therefore upstream-downstream rather than redundant:

```text
reduced effective weighting of corrective evidence
    -> rigid slow constraints / default policy stabilization
    -> higher cost of departing from the default state
    -> Psi_f > P_sel
    -> knowing-doing gap and reduced corrective sampling
    -> further stabilization of the prior/default policy
```

## 3. Two partially separable gates

The combined account distinguishes two gates that should not be collapsed.

### Gate A: evidence-to-belief updating

Question: does positive, surprising, or corrective evidence revise lower- and higher-level expectations?

Candidate external markers discussed in the TINS review include:

- RewP and reward-related delta: effective impact of better-than-expected outcomes;
- P300: candidate index of context updating or impact of informative surprise;
- feedback theta / ERN / FRN: performance monitoring and control recruitment, with phenotype dependence;
- MMN: lower-level sensory prediction-error propagation;
- beta activity and beta-burst duration: candidate signatures of model or state maintenance;
- gamma and aperiodic activity: candidate gain/E-I conditions under which updating occurs.

### Gate B: policy-to-action implementation

Question: even if a beneficial action can be represented or verbally identified, can the system pay the cost of initiating, sustaining, or switching into it?

The Frontiers paper operationalizes this gate through:

- behavioral control costs;
- autonomic recovery and acute arousal;
- linguistic shifts in perceived ability and constraint;
- optional neural and biochemical adjudication layers;
- the critical relation between executive friction and available control capacity.

### Combined implication

Depression may contain at least three profiles:

1. **Updating-dominant failure**: positive evidence has little effect on slow constraints.
2. **Implementation-dominant failure**: relevant knowledge or intention is relatively preserved, but action cost exceeds available capacity.
3. **Coupled failure**: weak positive updating deepens the default attractor, which increases transition cost; failed action then reduces access to further corrective evidence.

The third profile is the strongest bridge between the two papers.

## 4. Direct mapping to the Frontiers control scaffold

| TINS predictive-processing term | Frontiers control-cost interpretation | Boundary |
|---|---|---|
| high-precision negative priors | slow constraints that strongly bias future policy selection | not identical to `Psi_f` |
| reduced leverage of positive prediction errors | weak update of expected reward, controllability, or self-efficacy | upstream contributor to cost landscape |
| cognitive immunisation | reinterpretation that preserves the current default model | possible stabilizer of default policy |
| elevated tonic beta / longer beta bursts | candidate model-maintenance or attractor-stability signature | beta is not a direct friction measure |
| attenuated RewP / reward-delta | candidate reduced impact of positive outcomes | not direct proof of failed belief revision |
| attenuated P300 | candidate reduced impact of informative or surprising events | mechanistic mapping remains indirect |
| active-inference avoidance | reduced sampling of disconfirmatory evidence | behavioral feedback loop |
| local adaptation to adversity | historically rational low-exploration policy | dysfunction must be distinguished from contextual adaptation |

## 5. Necessary correction to the MDD framing

The current MDD section should not be interpreted as claiming that the depressed person’s generative model is generally accurate and that only action execution is impaired. The TINS review supports a more differentiated statement:

> Declarative knowledge about which actions are conventionally beneficial may remain partly intact even when higher-order expectations about reward, controllability, social feedback, and self-efficacy are rigid or insufficiently revised by corrective evidence. Executive breakdown may therefore arise from impaired belief updating, elevated implementation cost, or their interaction.

This preserves the knowing-doing gap without denying evidence for altered reward learning and positive belief updating.

## 6. Candidate insertion for a future manuscript revision

The following paragraph is suitable for a future revision, postprint commentary, or derivative paper. It should not be represented as part of the already submitted/accepted version unless that version is formally updated.

> Recent electrophysiological accounts suggest that depression may involve not an absence of outcome registration, but reduced effective weighting of positive and corrective evidence, alongside neural dynamics favoring model maintenance over flexible revision. Within the present framework, such an inference regime may deepen default policy attractors and thereby increase the control cost required to initiate alternative action states. This yields a coupled account in which impaired updating and elevated implementation cost reinforce one another: weak positive updating stabilizes low-agency expectations, costly action reduces corrective sampling, and reduced sampling further preserves the prior.

A shorter formulation is:

> Predictive-processing abnormalities may act upstream of executive friction by stabilizing default policy states from which alternative action requires costly departure.

## 7. Consequences for the neural expansion layer

For the MDD use case, the TINS review suggests that the current optional neural layer could be broadened conceptually beyond PCI, Fisher geometry, theta-gamma coupling, and basal-ganglia gating.

A bounded division of labor is:

- **RewP / reward-delta**: candidate leverage of positive outcomes on subsequent updating;
- **P300**: candidate leverage of informative surprise or context change;
- **tonic beta / beta-burst duration**: candidate stability of the default model or control state;
- **feedback theta**: context- and phenotype-sensitive monitoring/control recruitment;
- **MMN**: early sensory prediction-error propagation;
- **gamma / aperiodic exponent**: candidate gain regime in which updating signals are expressed.

These measures should be treated as moderators, upstream processes, or expansion indicators. None should be declared an observation of `Psi_f` itself.

A future empirical model could test whether default-state stability mediates the relation between weak corrective updating and implementation cost:

```text
RewP / reward-delta / P300
        -> slow-constraint revision
        -> beta-state persistence or default-policy stability
        -> task-switch / initiation cost
        -> behavior, HRV recovery, SCR, and modal-language measures
```

This mediation chain is a testable bridge hypothesis, not an established mechanism.

## 8. SRT reading, with governance guardrails

A cautious SRT translation is:

- corrective differences may become manifest without receiving enough selective maintenance to alter stabilized constraints;
- old constraints can bias interpretation, action selection, and future evidence sampling;
- repeated maintenance can make a path cheaper to re-enter and alternatives more costly to actualize;
- depression can therefore be investigated as asymmetric historical inscription: negative differences are more readily retained and scaffolded, while positive differences are more readily discounted or de-historicized.

However:

- `L0/L1/L2` must not be equated directly with latent variables/current EEG states/priors;
- precision weighting is not identical to `d-value`;
- beta, RewP, P300, gamma, or 1/f activity do not define `Psi_f`;
- Fisher information remains only a candidate local geometric projection of transition burden;
- this review does not validate SRT ontology;
- the adaptive value of low-exploration inference under persistent adversity must be distinguished from inflexible persistence after contingencies change.

## 9. Empirical upgrade path

This crosswalk could move from a conceptual bridge toward an operational hypothesis through three studies.

### Study A: positive-trace persistence

Measure not only cue-locked RewP/reward-delta but whether a positive outcome changes expectation on later trials, survives delay, transfers across context, and resists cognitive immunisation.

### Study B: controllability × reward

Compare passive reward with action-contingent reward. Test whether agency/control changes the relationship among RewP, P300, beta-state persistence, later belief revision, and initiation cost.

### Study C: exit cost from a negative default

Induce a stable negative expectation, then provide repeated corrective evidence. Estimate the number of trials and physiological/control cost required to exit the state, the persistence of the revision, and relapse under stress or delay.

The critical prediction is not merely a mean EEG difference. It is that weak corrective updating predicts deeper default-state persistence, which in turn predicts higher behavioral implementation cost.

## 10. Evidence status

Recommended repository classification:

- evidence level: **E2 structural convergence / bridge support**;
- possible upgrade: **E3 scoped operational hypothesis** after a domain-specific mediation or intervention test;
- not supported: direct validation of `Psi_f`, `P_sel`, a unitary cross-modal latent factor, ROS coupling, Fisher proxies, or SRT ontology.

## 11. Bottom line

The external review and the Frontiers paper address adjacent failures in one closed loop:

> The review explains why the old belief may not move; the executive-friction framework explains why the person may not move once the old belief and default policy remain in place.

The strongest joint claim is therefore not that depression is only impaired updating or only high execution cost, but that **impaired corrective updating can stabilize default policies, raise the cost of alternative action, and thereby reduce the very experiences needed to revise the original model**.
