---
id: SRC-2026-08-09-NEURO-QIN-ESKETAMINE-DOC-NETWORK-RECOVERY
type: source_card
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
domain: Neuroscience
source_type: peer_reviewed_clinical_study
verdict: A_bounded
integration_priority: high
created: 2026-08-09
source_title: Esketamine Preserves Network Connectivity and Promotes Recovery in Consciousness Disorders
authors: [Xuewei Qin, Xuanling Chen, Lan Yao, Bo Wang, Hongchuan Niu, Zhenhu Liang, Zhibin Zhao, Jian Wang, Jiapeng Huang, Xiangyang Guo, Xiaoli Li]
journal: CNS Neuroscience & Therapeutics
year: 2026
volume: 32
issue: 5
article: e70890
doi: 10.1002/cns.70890
pmid: 42126345
pmcid: PMC13170474
source_url: https://doi.org/10.1002/cns.70890
tags: [disorders-of-consciousness, anesthesia, esketamine, propofol, EEG, permutation-entropy, functional-connectivity, recovery, network-capacity]
---

# SourceCard — Qin et al. 2026: Esketamine, network dynamics, and recovery in disorders of consciousness

## 1. Why this source matters to SRT

This paper supplies a clinically grounded pressure point for the neuroscience bridge:

> A system's ability to express or switch among candidate states may depend not only on which representation or strategy has higher control weight, but also on whether the global neural dynamics retain enough organized complexity and connectivity for candidate formation, propagation, competition, and reconfiguration.

This is useful only as a **P3/P4 bridge window**. The paper does not measure SRT `L_0`, `L_1`, `L_2`, `d`, `Psi_f`, `T_dir`, real choice, or a canonical "selection capacity" variable.

---

## 2. Verified bibliographic anchor

Peer-reviewed open-access original article:

- Qin X, Chen X, Yao L, et al. *Esketamine Preserves Network Connectivity and Promotes Recovery in Consciousness Disorders*.
- *CNS Neuroscience & Therapeutics*. 2026;32(5):e70890.
- DOI `10.1002/cns.70890`.
- PMID `42126345`; PMCID `PMC13170474`.
- First published 13 May 2026.

---

## 3. Study design

Prospective, non-randomized comparative-effectiveness study in adults with disorders of consciousness undergoing spinal cord stimulation implantation.

- total `n = 34`;
- esketamine group `n = 17`;
- propofol group `n = 17`;
- anesthetic assignment followed clinical practice rather than random allocation;
- perioperative EEG plus clinical recovery outcomes;
- preoperative and 3-month CRS-R assessment.

This design supports association and mechanistic plausibility, not strong causal claims about long-term neurological recovery.

---

## 4. Main empirical findings used here

The source reports that, relative to propofol:

1. esketamine anesthesia was associated with faster spontaneous-respiration recovery;
2. esketamine preserved more beta-range activity during maintenance, while propofol showed stronger delta/theta dominance;
3. permutation entropy during maintenance was higher under esketamine;
4. whole-brain functional connectivity declined under both anesthetics; gamma-band connectivity was relatively higher under esketamine, but the between-group result was weaker than the entropy finding;
5. unadjusted 3-month consciousness recovery favored esketamine only as a trend, while adjusted models reported an association with improvement;
6. recovery-period gamma connectivity was associated with consciousness improvement in exploratory analysis.

The evidence therefore supports a narrow statement:

> Different anesthetic regimes can preserve substantially different neural dynamical regimes even when both satisfy clinical anesthesia requirements.

It does **not** establish that higher entropy or gamma connectivity is itself consciousness, selection capacity, or long-term neuroprotection.

---

## 5. SRT-facing increment

NEURAL25 separated:

```text
representation
!=
accessibility
!=
control authority
!=
expression
!=
historical write-back
```

Qin et al. adds pressure for an upstream, system-level question:

```text
Does the neural system currently retain enough organized dynamical capacity
for candidate states to form, propagate, compete, and switch at all?
```

This suggests a new bridge variable class:

```text
Dynamical Capacity
-> Candidate Accessibility
-> Control Authority
-> Expression
-> Historical Write-back
```

where `Dynamical Capacity` is a **temporary bridge concept**, not a canonical SRT symbol.

---

## 6. What "dynamical capacity" means here

For this bridge only, dynamical capacity means the system-level ability to sustain differentiated but interacting neural states over the relevant time window such that:

- candidate-specific activity can be formed or reinstated;
- candidate information can propagate across required networks;
- multiple candidates can remain non-equivalent long enough to compete;
- network state can transition rather than being globally suppressed or rigidly trapped.

It is deliberately **not** defined as:

- maximum entropy;
- maximum firing rate;
- maximum connectivity;
- criticality itself;
- wakefulness;
- consciousness;
- global workspace ignition;
- `L_0` breadth;
- canonical `d`;
- canonical `Psi_f`.

---

## 7. Proxy guardrail

The paper uses permutation entropy and wPLI connectivity. For SRT these can only be treated as **candidate measurements of parts of the dynamical-capacity window**.

Forbidden:

```text
Permutation entropy = selection capacity
Gamma connectivity = consciousness
Higher complexity = more real choice
Esketamine preserves L0
Propofol collapses L0
```

Safer:

> Under anesthesia, entropy and connectivity measures may help index whether the neural system retains a richer organized dynamical regime, but they do not by themselves identify candidate accessibility, control authority, consciousness, or SRT variables.

---

## 8. Relation to NEURAL25

Lu et al. primarily pressure the distinction:

```text
candidate represented
!=
candidate controls behavior
```

Qin et al. pressures an upstream distinction:

```text
candidate-specific competition
requires
an enabling network regime
```

The combined architecture is therefore not "PFC = weight" and not "complexity = consciousness".

A safer synthesis is:

> Neural selection involves at least two separable scales: a system-level regime that permits differentiated candidates to form and interact, and candidate-specific mechanisms that determine which available state or strategy obtains effective control.

---

## 9. Falsification / downgrade conditions

The proposed bridge should be weakened if future work shows that:

1. entropy/connectivity changes under anesthesia do not predict any candidate-specific accessibility, transition, perturbational response, or recovery property beyond generic drug effects;
2. apparently richer dynamical regimes are fully explainable by unstructured noise without improved organized state differentiation or transition capacity;
3. candidate accessibility and switching remain unchanged across matched global-complexity states;
4. the proposed upstream capacity layer adds no predictive value beyond ordinary arousal, signal power, or task engagement.

---

## 10. Landing recommendation

Verdict: **A, bounded**.

Recommended outputs:

- new NEURAL26 P3/P4 bridge patch;
- future experimental distinction between global dynamical capacity and candidate-specific accessibility / authority;
- no canonical or compact-core body rewrite in this pass.

The source should be used as evidence pressure for a layered selection architecture, not as evidence that SRT ontology has been validated.