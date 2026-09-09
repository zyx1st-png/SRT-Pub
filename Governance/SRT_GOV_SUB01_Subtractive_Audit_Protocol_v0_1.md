---
id: SRT-GOV-SUB01-SUBTRACTIVE-AUDIT
type: governance_protocol
status: protocol_v0_1
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
source_ids:
  - SRC-2026-07-16-METHOD-SAWYER-SUBTRACTION
  - SRC-2026-09-08-METHOD-TODD-BAYESIAN-DESCRIPTIONS-REALISATION-GAP
dependency:
  - SRT-CLAIM-LADDER
  - SRT-EDIT-PROTOCOL
  - SRT-CORE-21-MINIMAL-AXIOMS
tags: [Governance, SubtractiveAudit, Minimality, VariableAudit, ClaimDiscipline, Falsification, Redundancy, MechanismRealisation, HeldOutIntervention]
---

# GOV-SUB01 — SRT Subtractive Audit Protocol v0.1

## 0. Role and boundary

This protocol turns a limited insight from Chris Sawyer's *Subtraction* into an SRT-safe governance procedure.

> **2026-09-08 mechanism-realisation hardening:** Ian Todd's realisation-gap argument is used here only to strengthen how `E_int / E_cf / E_mech` are earned. A successful description, fit or same-projection prediction does not establish a mechanism. Mechanism-level irreducibility claims must independently nominate a physical / operational realiser and face a held-out intervention on which bounded rival mappings prospectively diverge. This hardening applies symmetrically to SRT and its competitors; it is not evidence that SRT is true.

Adopted insight:

```text
A component should not be retained merely because it is familiar,
elegant, historically central, or repeatedly invoked.
Test what changes when it is removed.
```

Required correction:

```text
removable under one target / metric / horizon
!= false
!= nonexistent
!= universally dispensable

survives removal testing
!= true
!= primitive
!= ontologically fundamental
```

This file governs theory editing and model comparison. It does not define SRT ontology and does not authorize empirical deletion of safety, clinical, legal, or rights protections.

---

## 1. When the protocol must be used

Run a subtractive audit before:

1. introducing a new P0 primitive;
2. promoting a P2 interpretation to P1;
3. introducing a new core symbol, scalar, operator, layer, threshold or named mechanism;
4. claiming that an SRT term is irreducible to a competitor vocabulary;
5. merging several domain bridges into a single explanatory identity;
6. claiming that a variable is necessary because it appears in many files;
7. treating a residual unexplained feature as evidence for a new entity;
8. declaring a model simpler after only renaming or redistributing its assumptions.

A lightweight audit is sufficient for prose-level edits. A full audit is required for P0/P1, equations, experiments, canonical definitions and cross-domain identity claims.

---

## 2. Audit object

Define the audit tuple:

\[
\mathcal A=\langle M,x,Y,C,E,H,P,K,\tau\rangle
\]

where:

- `M`: current model, theory fragment or document architecture;
- `x`: component proposed for deletion;
- `Y`: target phenomenon or claim the model is supposed to preserve;
- `C`: context specification;
- `E`: evaluation vector;
- `H`: observation horizon;
- `P`: perturbation / counterexample set;
- `K`: allowed refit or replacement budget;
- `tau`: loss threshold.

The context `C` must include, when relevant:

```text
bearer
scale / grain
system boundary
historical state
measurement regime
domain
normative authority
time horizon
```

An audit without an explicit `Y` and `C` is invalid.

---

## 3. Removal operator

Let:

\[
M^{-x}=R_x(M;K)
\]

be the model after removing `x` under an allowed refit budget `K`.

`K` must be declared because three different questions are otherwise conflated:

| Refit budget | Question |
|---|---|
| `K=0` | Does the current implementation literally depend on `x`? |
| limited `K` | Can nearby parameters or representations compensate? |
| broad `K` | Is the role of `x` replaceable by a substantially different model? |

If unlimited refitting is allowed, almost any named component may appear removable. That result shows representational replaceability, not absence of the underlying role.

---

## 4. Evaluation vector

Do not use a single performance score. Define:

\[
E(M)=\langle E_{pred},E_{int},E_{cf},E_{mech},E_{phen},E_{norm},E_{orient}\rangle
\]

where applicable:

- `E_pred`: predictive coverage and calibration;
- `E_int`: intervention effectiveness;
- `E_cf`: counterfactual discrimination;
- `E_mech`: mechanism identifiability and causal specificity;
- `E_phen`: preservation of first-person or lived distinctions;
- `E_norm`: responsibility, rights, stakes and bearer attribution;
- `E_orient`: whether the model changes actionable orientation rather than only preserving procedure.

A component may be dispensable for prediction and indispensable for intervention, explanation, phenomenology or normative attribution.

For mechanism-level claims, `E_int / E_cf / E_mech` are not satisfied by correlation, behavioural fit, a shared impairment after generic disruption, or additional data on a projection where the candidate mappings remain observationally equivalent. Use Step 6A.

---

## 5. Loss score

Define target-relative deletion loss:

\[
\Delta_x(Y\mid C,H,P,K)
=
D\big(E(M),E(M^{-x})\big)
\]

where `D` is a declared comparison function.

Interpretation:

```text
Delta_x <= tau
-> x is dispensable relative to Y, C, H, P and K

Delta_x > tau
-> x is a current indispensability candidate under those conditions
```

Neither result is universal.

---

## 6. Required audit sequence

### Step 1 — Target lock

State exactly what must remain explained.

Bad target:

```text
the theory should still work
```

Acceptable target:

```text
preserve matched-endpoint path dependence prediction
preserve bearer-specific consequence-return classification
preserve directional self-readability distinction
preserve object re-identification after perturbation
```

### Step 2 — Candidate inventory

List:

- entities;
- relations;
- variables;
- layers;
- thresholds;
- measurement proxies;
- background assumptions;
- bridge mappings;
- narrative labels.

### Step 3 — Single removal

Delete one item without changing unrelated assumptions.

Record:

- immediate loss;
- delayed loss;
- which metric changed;
- whether another component compensated;
- whether the target definition silently changed.

### Step 4 — Replacement test

Introduce a functionally plausible substitute `x'`.

```text
x removable, role preserved by x'
-> implementation-specific dispensability

no substitute preserves role
-> role-level indispensability candidate
```

### Step 5 — Joint removal

Test interactions.

For components `x` and `z`:

\[
\Delta_{x,z}
\neq
\Delta_x+\Delta_z
\]

is expected whenever redundancy, synergy or compensation exists.

Minimum tests:

- pairwise deletion for all core symbols;
- layer-level deletion for L0/L1/L2;
- joint deletion of a variable and its proxy;
- joint deletion of a mechanism and the history term that stabilizes it.

### Step 6 — Perturbation sweep

A component is not robustly dispensable until removal is tested across:

- ordinary cases;
- boundary cases;
- adversarial cases;
- path-dependent cases;
- scale changes;
- bearer changes;
- delayed failure windows.

### Step 6A — Realisation / held-out intervention gate

Use this gate whenever the conclusion would say that a surviving SRT term, variable, relation or mechanism is **mechanistically irreducible, causally identified, empirically superior, or physically realised** rather than merely descriptively useful.

Lock the following before reading the discriminating result:

```text
1. candidate mapping M
2. nominated physical / operational realiser R_M
3. the physical-history equivalence classes that M treats as the same state
4. bounded rival mapping M'
5. held-out intervention I* not used to fit, select or repair either mapping
6. preregistered divergent causal signature and decision margin
7. task / scale / boundary / horizon / measurement regime to which the verdict applies
```

A discriminating signature may concern:

```text
sign
dose-response
timing
mediation pattern
state transition
recovery / hysteresis
or another prospectively locked causal difference
```

The key test is not whether both mappings fit the same observed projection. It is whether they predict different results under `I*`:

\[
P(Y\mid do(I^*),M)
\not\approx
P(Y\mid do(I^*),M')
\]

within the declared margin.

If histories grouped into one candidate controller state differ in timing, phase, contact, field structure, bearer relation or another nominated physical distinction **and those differences change the intervention response**, then the proposed state is too coarse for the mechanism claim under that task and horizon. Enriching the mapping after seeing the result creates a new hypothesis; it does not rescue the preregistered mechanism claim.

A generic intervention that breaks a causal medium and impairs every rival establishes causal relevance, not mechanism identity. Prefer interventions that change the nominated relation while preserving the ordinary task and declared channel, or explicitly model unavoidable sensory / plant consequences and test the residual signature.

Interpret every result locally:

```text
mapping M fails under declared conditions
!= entire mechanism family is false

mapping M survives one held-out intervention
!= M is universally realised
!= SRT primitive is proven
```

If no feasible held-out intervention makes the candidate and bounded rival predict different causal signatures, classify `E_mech` as unresolved rather than converting same-projection fit into mechanism evidence.

### Step 7 — Residue classification

Use only the following labels:

| Label | Meaning |
|---|---|
| `R0 rhetorical redundancy` | wording can be removed with no structural change |
| `R1 proxy redundancy` | measured role remains but this proxy is unnecessary |
| `R2 implementation substitutable` | another mechanism or representation performs the same role |
| `R3 target-relative dispensable` | unnecessary for the declared target only |
| `R4 compensated / unresolved` | removal was masked by redundancy or refitting |
| `N1 current target-relative indispensable` | robust loss under declared conditions |
| `N2 cross-context indispensability candidate` | survives multiple contexts, horizons and perturbations |
| `P unresolved primitive admission` | currently not derivable or removable, but not externally proven |

Do not use `fundamental`, `ultimate`, `real` or `necessary simpliciter` as audit outputs.

### Step 8 — Claim-ladder routing

- `R0-R3`: delete, demote or rename.
- `R4`: keep provisional and design stronger tests.
- `N1`: may remain at its current claim level.
- `N2`: may justify stronger attention, not automatic promotion.
- `P`: must be marked as primitive admission and remain open to future subtraction.

Promotion still follows `Governance/SRT_CLAIM_LADDER.md`.

---

## 7. Mandatory failure checks

### 7.1 Measurement blindness

Ask whether the chosen metric can register the loss.

Example:

```text
removing T_dir does not change task accuracy
```

This says little if the metric never measured direction readability or reorientation.

### 7.2 Short-horizon masking

A deletion may preserve immediate output while damaging:

- long-term stability;
- learning;
- recovery;
- identity continuity;
- future option space;
- rare-event safety.

### 7.3 Redundancy and degeneracy

A backup path may hide necessity. Delete the backup jointly or perturb it independently.

### 7.4 Hidden reparameterization

Do not count a variable as removed when its function was merely moved into:

- initialization;
- a loss function;
- a prior;
- data preprocessing;
- architecture;
- a renamed term.

### 7.5 Target laundering

Do not redefine success after deletion.

### 7.6 Scale collapse

A component dispensable at one scale may be necessary for cross-scale translation.

### 7.7 Bearer relocation

A deletion can preserve aggregate behavior while moving cost or consequence to another bearer.

### 7.8 Ethical asymmetry

No live-system audit may remove protections merely because average output remains unchanged.

Safety, rights and welfare guardrails require:

- simulation;
- reversible staging;
- worst-case analysis;
- explicit affected-bearer review.

### 7.9 Same-projection equivalence / post-hoc rescue

Do not count more data on the same observable projection as mechanism discrimination when the candidate and rival are already equivalent on that projection.

Do not preserve an original prediction by adding realiser variables, changing factorisation, altering the state partition or broadening the mechanism only after the held-out result is known. Record the repaired mapping as a new hypothesis and test it prospectively.

---

## 8. SRT-specific audit matrix

### 8.1 Selection

Remove the word and primitive role of `selection`, retaining only:

- asymmetrical constraints;
- reachable-set restriction;
- history dependence;
- cost;
- consequence return.

Required question:

> What explanatory, counterfactual or experimental difference remains that is lost without selection language?

If the answer is intended to establish **mechanism-level** or **derivational** indispensability, language deletion is insufficient. Lock a bounded rival (for example an explicit constraint / recurrent-dynamics mapping), nominate the SRT-selection realiser independently, and require a held-out intervention on which the mappings predict different causal signatures. If

\[
P(Y\mid do(I^*),M_{SRT})
\approx
P(Y\mid do(I^*),M_{rival})
\]

within the declared margin, selection has not earned mechanism-level irreducibility for that target even if SRT remains a useful description.

### 8.2 L0 / L1 / L2

Run:

1. remove L2;
2. remove L1;
3. remove L0;
4. merge L1 and L2;
5. merge all layers into one state-space description;
6. test which distinctions, predictions and governance boundaries disappear.

### 8.3 `d-value`

Remove `d` while retaining salience, value, damage, control cost and information measures.

Required loss:

- bearer-relative concern;
- consequence return;
- non-substitutability;
- payability;
- failure-window distinction.

If those survive unchanged, `d` may be only a relabeling.

A mechanism-level projection additionally owes Step 6A: correlation with a neural, behavioural, metabolic or control variable does not identify that variable as the physical realiser of `d`.

### 8.4 `Psi_f`

Remove `Psi_f` while retaining optimization loss, Fisher geometry, energetic cost and transition barriers.

Required question:

> Does `Psi_f` identify a cross-domain payability / transition-friction role not exhausted by any one proxy?

A mechanism-level projection additionally owes Step 6A: fit to Fisher geometry, energetic cost, free-energy terms or transition barriers is not by itself a realisation mapping.

### 8.5 `T_dir`

Remove `T_dir` while retaining confidence, reward, valence, attention and policy certainty.

Required loss:

- self-readable direction;
- source discrimination;
- reorientation based on that reading.

A mechanism-level projection additionally owes Step 6A: a directed-flow, meta-attention or reorientation signal must have a prospectively distinct causal signature before it can be identified as the realiser of `T_dir`.

### 8.6 Objecthood and reselection

Remove reselectability while retaining persistence and performance.

Required question:

> Can the model still distinguish a robust object from a high-performing but unreopenable closure?

### 8.7 Origin of selectability

If all subject, value, information and object terms are removed and only an asymmetric transition structure remains, classify the residue carefully:

```text
asymmetric constraint
historical restriction
state-space truncation
or selection
```

The audit does not decide the naming by itself.

---

## 9. Audit ledger template

```md
### Subtractive audit record

- Audit ID:
- Date:
- Auditor:
- Target Y:
- Context C:
  - bearer:
  - scale/grain:
  - boundary:
  - history:
  - measurement regime:
- Candidate x:
- Removal operator:
- Refit budget K:
- Horizon H:
- Perturbation set P:
- Evaluation vector E:
- Threshold tau:
- Candidate mechanism mapping M:
- Nominated physical / operational realiser R_M:
- State-equivalence claim / ignored physical distinctions:
- Bounded rival mapping M':
- Held-out intervention I*:
- Preregistered divergent causal signature / margin:

#### Results
- single-removal loss:
- delayed loss:
- compensation detected:
- replacement candidate:
- joint-removal interactions:
- held-out intervention result:
- realiser-specific signature:
- rival discrimination result:
- post-hoc mapping change required:
- bearer/cost relocation:
- phenomenology loss:
- safety/normative risk:

#### Classification
- R0 / R1 / R2 / R3 / R4 / N1 / N2 / P

#### Claim-ladder consequence
- delete / demote / retain / redesign test / primitive admission

#### Surviving uncertainty
-
```

---

## 10. Sawyer source adoption and rejection map

### Adopted

- familiarity and repetition do not establish necessity;
- explanation can saturate without increasing orientation;
- removal should test indispensability;
- what survives is not thereby privileged;
- total exposure without gating, delay and repair is a collapse condition rather than ideal openness.

### Rejected or quarantined

- use of subtraction to establish alternative physics, chemistry, physiology or cosmology;
- pressure / space-medium accounts as scientific mechanisms;
- fire, oxygen, respiration, heart, motion and planetary claims;
- sixth-sense or clairvoyance mechanisms;
- the 63 total-openness statements as established formal axioms;
- the inference from conceptual removability to ontological nonexistence.

The source is therefore integrated as a governance trigger and retained as a warning about subtractive overreach.

---

## 10A. Todd source adoption and boundary map

SourceCard:

```text
Materials/2026/SRC_2026_09_08_Method_Todd_Bayesian_Descriptions_Realisation_Gap.md
```

Adopted methodological pressure:

- computational / behavioural description does not by itself identify physical mechanism;
- a mechanism mapping owes independently specified causal realisers and state-transition roles;
- same-projection observational equivalence must be broken by a prospectively discriminating intervention rather than by more fit on the same projection;
- generic disruption establishes causal relevance, not mechanism identity, when all rivals predict impairment;
- a mapping revised after the held-out result is a new hypothesis;
- rejection is local to the declared mapping / task / scale / horizon / margin, not a family-wide verdict.

Not adopted as SRT result:

- Todd's resource-bounded coupling hypothesis is not an SRT theorem or established empirical result;
- Bayesian mechanisms are not ruled out;
- coupling / dynamical descriptions do not receive a mechanism exemption;
- formal closure, dimensionality or representation growth do not distinguish SRT from rival mechanism families;
- Todd does not establish any SRT primitive, `d`, `Psi_f`, `T_dir`, bearer or ontology claim.

The source is integrated only as a governance-method hardening of mechanism attribution.

---

## 11. Stop rule

A subtractive audit stops when:

1. the declared target and measurement regime are exhausted;
2. remaining components are classified, not sanctified;
3. unresolved interactions are logged;
4. no further safe deletion can be tested without changing the target or imposing unacceptable harm;
5. residue is returned to the claim ladder as `N1`, `N2` or `P`, never as automatic P0 truth.

The audit should be rerun when the target, scale, data, experiment, competing model or canonical architecture changes.
