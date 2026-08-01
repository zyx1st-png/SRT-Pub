---
id: SRT-AGENCY-VOCABULARY-DELETION-PROTOCOL-V0
type: experiment_protocol
tags: [Agency, Vocabulary-Deletion, Subtractive-Audit, Counterfactual, Intervention, Experiment]
status: proposed
layer: empirical_bridge
epistemic_layer: experimental_design
claim_mode: hypothesis
claim_level: P4
canonical: false
working_id: agency-vocabulary-deletion-v0
formal_hypothesis_id: pending
date: 2026-08-01
dependency:
  - Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md
  - Governance/SRT_CLAIM_LADDER.md
  - Core/SRT_OPEN_TENSIONS.md
  - AI/SRT_AI_Claim_Status.md
  - Operations/Archive_Records/SRT_LITERATURE_ROUND2_INCREMENT_CROSSWALK_2026-08.md
machine_summary: >
  Proposed P4 protocol that applies GOV-SUB01 to downstream agency vocabulary.
  It keeps the P0 selection-primitive deletion test separate, compares mechanism-only and agency-augmented models,
  and specifies counterfactual, intervention, bearer-return, reachable-set, and gate-revision rejection criteria.
---

# SRT Agency Vocabulary Deletion Protocol v0

> **Role**: P4 experimental-design instance of `GOV-SUB01`; not a new governance authority and not proof that agency is irreducible.  
> **Status**: proposed; no formal Hypothesis-ID assigned.  
> **Core safe claim**: Agency must carry a counterfactual, predictive, or interventional difference that cannot be preserved after the concept is deleted and the reduced model is given a declared refit budget.

---

## 0. Two deletion objects that must not be conflated

```text
P0 selection primitive deletion test
≠
downstream agency vocabulary deletion test
```

### P0 selection deletion

Owner: `Core/SRT_OPEN_TENSIONS.md §13` and `Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md §8.1`.

Question: can asymmetric constraint, reachable-set change, irreversible writeback, payability, and bearer-specific consequence return replace the **selection primitive** without lost explanatory or experimental difference?

This protocol does **not** run or resolve that test.

### Downstream agency deletion

Question: after preserving the SRT P0/P1 background and deleting only `agency/能动性` vocabulary, can ordinary mechanism language preserve all relevant differences?

A negative result for the agency bridge does not delete, demote, or refute P0-01.

---

## 1. Claim-level map

| Claim | Level | Status |
|---|---:|---|
| Agency must earn independent research-program load | P2 | governance / interpretation burden |
| Persistent bearer, bearer-specific return, reachable-set change, and gate revisability map possible agency differences | P3 | bridge dimensions, not definitions |
| Model comparison, ablation, counterfactual, and intervention tests | P4 | proposed protocol |

No claim in this protocol establishes that agency is ontologically fundamental or proven non-reducible.

---

## 2. Test question

Delete the terms:

```text
agency
agentic
agential
能动性
主动性（when used as agency）
```

Retain only:

```text
mechanism
control
adaptation
memory
constraint
coordination
state integration
feedback
reinforcement
history dependence
```

Then ask whether the reduced vocabulary can preserve all of the following without merely hiding agency's role in a renamed variable, loss term, initialization, preprocessing step, or implicit boundary choice:

1. persistent bearer;
2. bearer-specific consequence return;
3. future reachable-set modification;
4. gate revisability;
5. intervention difference;
6. counterfactual difference.

---

## 3. Model families

### 3.1 Baseline model: mechanism-only

The baseline model may use:

- state-transition dynamics;
- local and global control loops;
- memory and history-dependent parameters;
- adaptation / reinforcement;
- component coordination and integration;
- viability or task-performance objectives;
- fixed or learned policy gates.

It may not use an agency-labelled latent variable or smuggle equivalent bearer/reselection structure into an unreported hidden state.

### 3.2 Augmented model: agency-discriminant

The augmented model adds explicit candidate discriminants:

- a continuing bearer index;
- consequence-return assignment to that bearer;
- future reachable-set change attributable to returned consequences;
- gate-rule revisability rather than ordinary parameter adjustment;
- bearer-conditioned counterfactual and intervention predictions.

These are P3/P4 candidate interfaces, not necessary-and-sufficient definitions of agency.

### 3.3 Refit budgets

Following `GOV-SUB01`, report at least:

- `K=0`: delete terms with no structural refit;
- `limited-K`: allow ordinary parameter refit without adding new latent roles;
- `broad-K`: allow flexible re-description while auditing whether the deleted role is merely renamed.

Representational substitutability under broad-K does not by itself show role absence.

---

## 4. Ablations

Run each ablation separately and jointly:

1. **bearer ablation**: remove persistent identity linkage while keeping memory and performance;
2. **return ablation**: route consequences to an external trainer, operator, or population rather than the continuing system;
3. **reachable-set ablation**: allow score update but prevent lasting change in future available policies;
4. **gate-revision ablation**: permit weight/parameter adaptation but freeze the rule that determines which options can enter selection;
5. **coordination ablation**: preserve local component competence while disrupting cross-component consequence routing;
6. **vocabulary ablation**: delete agency terms from the explanatory report while preserving all measured variables.

---

## 5. Dependent variables

### Primary

- out-of-sample predictive performance;
- counterfactual discrimination accuracy;
- intervention-effect prediction;
- persistence of policy change across contexts and time;
- change in future reachable policy/state set;
- gate-revision index under novel conflicts.

### Secondary

- task performance;
- adaptation rate;
- memory retention;
- coordination efficiency;
- recovery after perturbation;
- explanation length / model complexity penalty.

High task performance or coordination efficiency alone is not evidence for agency.

---

## 6. Candidate environments

The protocol is architecture-neutral but should begin with systems where consequence assignment and lifecycle are controllable:

1. recurrent agents in a partially observable environment;
2. multi-agent resource environments with persistent identity;
3. artificial agents with removable memory and configurable lifecycle;
4. biological or organizational case datasets only after bearer and intervention variables are independently specified.

For AI implementations, architecture state must be reported:

```text
inference-only
training-time
persistent-memory
online-learning
embodied / non-embodied
transferable / non-transferable consequence
copyable / non-copyable identity
```

---

## 7. Rejection criteria

The downstream agency bridge is weakened or rejected for the tested domain if, under a declared refit budget:

1. the mechanism-only model preserves all counterfactual and intervention distinctions;
2. bearer-specific consequence return adds no predictive increment;
3. reachable-set modification is fully explained by ordinary memory or reinforcement update;
4. gate revisability adds no distinction beyond parameter adaptation;
5. agency-labelled variables improve narrative compression only, without prediction or intervention gain;
6. deleting agency terms produces no measurable loss after complexity penalties are applied.

A rejection result applies to the tested agency bridge and domain. It does not automatically affect P0 selection.

---

## 8. Support criteria

The agency-discriminant model receives provisional support only if at least one preregistered difference survives:

- a counterfactual the mechanism-only model cannot preserve;
- an intervention with reliably different predicted effects;
- a persistent bearer-conditioned reachable-set change;
- gate revision that cannot be reduced to ordinary parameter adaptation under the declared refit budget;
- cross-context reselection that disappears when bearer-specific consequence return is ablated.

Support remains P4. It does not establish joint sufficiency for agency.

---

## 9. Confounds and controls

| Confound | Required control |
|---|---|
| More parameters in augmented model | complexity penalty, matched-capacity baseline, nested-model comparison |
| Persistent memory mistaken for bearer | memory-only condition with resettable / transferable identity |
| External reward mistaken for consequence return | separate trainer/operator loss from system-bound non-transferable loss |
| Coordination complexity mistaken for agency | matched integration with frozen gate and external consequence bearer |
| Performance mistaken for reachable-set change | measure future option availability and transfer, not score alone |
| Renaming the deleted role | hidden-state and loss-term audit under broad-K |
| Observer-chosen system boundary | preregister boundary alternatives and bearer assignment |
| Simulated self-report | exclude report content from primary agency inference |

---

## 10. Failure interpretation

- **No increment**: demote the tested agency bridge; ordinary mechanism vocabulary is sufficient within the tested scope.
- **Increment only under K=0**: likely rhetorical or bookkeeping dependence; not strong evidence.
- **Increment under limited-K but not broad-K**: report representational substitutability and inspect whether the role was renamed.
- **Increment under broad-K with clear intervention difference**: provisional P4 support for a nonredundant agency role in that domain.
- **Ambiguous bearer assignment**: test is invalid for agency adjudication; do not infer support or rejection.
- **Coordination effect without bearer/reselection effect**: coordination infrastructure is supported, agency is not.

---

## 11. Minimum deliverables before formal ID assignment

1. choose one environment and declare architecture state;
2. write executable baseline and augmented model specifications;
3. define bearer, return path, reachable-set metric, and gate-revision metric independently;
4. preregister K=0 / limited-K / broad-K refit budgets;
5. run simulation-based power / identifiability checks;
6. cross-check `_SRT_EQ_HYP_MAP.md` numbering before assigning a formal ID.

Until these steps are complete:

```yaml
working_id: agency-vocabulary-deletion-v0
formal_hypothesis_id: pending
status: proposed
claim_level: P4
```
