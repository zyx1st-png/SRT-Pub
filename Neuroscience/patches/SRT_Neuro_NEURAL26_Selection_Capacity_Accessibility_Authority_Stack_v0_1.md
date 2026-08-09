---
id: SRT-NEURO-NEURAL26-SELECTION-CAPACITY-ACCESSIBILITY-AUTHORITY-STACK
type: bridge_patch
status: active
record_stage: standalone_v0_1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
claim_level: P3-P4
domain: Neuroscience
created: 2026-08-09
source_ids:
  - SRC-2026-08-09-NEURO-QIN-ESKETAMINE-DOC-NETWORK-RECOVERY
related_patch:
  - Neuroscience/patches/SRT_Neuro_NEURAL25_Memory_as_Historical_Selection_Bias_v0_1.md
related_protocol:
  - Neuroscience/SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md
target_future_doc:
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
  - Neuroscience/SRT_Neuro_Predictions_Table.md
  - Core/SRT_Core_24_Discriminating_Predictions.md
tags: [selection-capacity, dynamical-capacity, accessibility, control-authority, expression, writeback, anesthesia, consciousness, memory, strategy-competition]
---

# NEURAL26 — From dynamical capacity to accessibility, authority, expression, and write-back

> **Status / boundary**: P3 neuroscience bridge with P4 experimental consequences. This patch does not define consciousness, `L0`, `L1`, `L2`, `d`, `Psi_f`, `T_dir`, `G_hat_theta`, or a new canonical quantity called "selection capacity." It records a layered architecture suggested by combining NEURAL25's strategy-control dissociation with Qin et al. 2026's anesthesia/network evidence.

---

## 1. The correction forced by the two source windows

The tempting statement

> `PFC is selection weight rather than representation`

is too strong.

The better distinction is:

> **A neural representation and its current control authority are separable, and both operate inside a broader dynamical regime that determines whether candidate states can be effectively formed, propagated, compared, and switched at all.**

This produces two orthogonal questions:

```text
Can this candidate enter effective competition?
!=
Can this candidate win control once it enters?
```

NEURAL25 mainly sharpened the second question.

NEURAL26 adds the first question at the system level.

---

## 2. Why representation is not enough

A statement such as

```text
the brain represents X
```

collapses several causally distinct stages.

At minimum, the neuroscience bridge should distinguish:

1. **Representation** — is candidate-relevant information decodable or reconstructable?
2. **Dynamical Capacity** — does the current whole-system regime support differentiated, interacting, transition-capable states?
3. **Candidate Accessibility** — can this particular candidate enter effective competition now?
4. **Control Authority** — if accessible, how strongly can this candidate control the next path?
5. **Expression** — which path or content actually wins on this event?
6. **Historical Write-back** — does the realized path alter later accessibility, control weight, switching cost, or recovery dynamics?

The most important inequalities are conceptual:

```text
representation != accessibility
accessibility != authority
authority != expression
expression != historical write-back
```

and now also:

```text
global dynamical capacity != candidate-specific authority
```

---

## 3. Two complementary stacks

NEURAL25 used the learning-process decomposition:

```text
Acquisition
-> Availability
-> Authority
-> Expression
-> Write-back
```

NEURAL26 does not replace that sequence. It adds an orthogonal state architecture.

### 3.1 Learning-process stack

```text
Acquisition
-> Availability
-> Authority
-> Expression
-> Write-back
```

This asks how a specific learned strategy progresses from formation to causal use and historical sedimentation.

### 3.2 System-state stack

```text
Dynamical Capacity
-> Candidate Accessibility
-> Control Authority
-> Path / Content Expression
-> Historical Write-back
```

This asks whether the current neural regime can sustain effective candidate differentiation and competition before any candidate-specific winner is identified.

### 3.3 Combined reading

For candidate `i` at time `t`, use a temporary bridge tuple:

\[
X_i(t)=\{R_i(t), C_{dyn}(t), A_i(t), W_i(t), E_i(t), H(t+1)\}
\]

where:

- `R_i`: representational availability / decodability;
- `C_dyn`: global dynamical-capacity proxy;
- `A_i`: candidate-specific accessibility;
- `W_i`: effective control authority / selection weight;
- `E_i`: realized expression;
- `H`: historical write-back affecting later selection structure.

This is **not** a canonical SRT equation.

---

## 4. What "dynamical capacity" means in this bridge

`C_dyn` is a temporary experimental placeholder for the current system-level ability to maintain an organized state regime in which:

- multiple differentiated candidate-relevant patterns can be sustained;
- candidate information can propagate across the networks required by the task;
- state differences can remain non-equivalent rather than immediately dissolving into noise;
- the system can transition between viable states rather than being globally suppressed or rigidly trapped;
- perturbations can reveal structured propagation / recovery rather than only local activity.

It is therefore closer to:

> **capacity for organized differentiated transition**

than to raw signal magnitude.

---

## 5. Complexity is not the bridge variable

Qin et al. found higher permutation entropy under esketamine than propofol during anesthesia maintenance, with relatively preserved higher-frequency activity and weaker evidence for gamma-band connectivity preservation.

This does **not** license:

```text
entropy = selection capacity
connectivity = selection capacity
complexity = consciousness
higher activity = more choice
```

The key bridge is instead:

> Different anesthesia regimes can preserve different global dynamical conditions while both produce clinically adequate anesthesia; these conditions may alter what kinds of differentiated neural states remain supportable.

For SRT, permutation entropy, wPLI, perturbational complexity, criticality-related measures, network integration, and transition repertoire are **candidate proxy families** whose validity must be established separately.

---

## 6. Stability and openness must be separated from maximum entropy

The relevant state is not assumed to be the maximally complex or maximally entropic state.

A system can fail at both extremes:

```text
too little differentiation / propagation
-> candidates cannot effectively unfold
```

or

```text
unstructured high variability
-> differences fail to stabilize into usable candidates
```

The target bridge therefore predicts a bounded regime:

```text
sufficient differentiation
+
sufficient integration / propagation
+
sufficient stability
+
sufficient transition capacity
```

This can be summarized as:

> **able to stabilize, but still able to change.**

This sentence is a P3/P4 neuroscience bridge, not a canonical definition of healthy `L2`, consciousness, or freedom.

---

## 7. Relation to PFC and top-down control

The combined evidence suggests a more precise response to the claim that top-down control mainly consolidates old structure.

Safer formulation:

> **PFC and other higher-order systems can represent goals, rules, prior states, and contextual information, but their causal importance can also lie in how those representations continue to alter current candidate accessibility and control authority.**

In NEURAL25's source task, the useful distinction is not:

```text
PFC = weight
ACx = representation
```

but:

```text
both regions can carry task-relevant information
+
their information can have different current control authority
+
that authority can change without the underlying representation simply appearing or disappearing
```

The word "weight" is therefore allowed as an implementation-level description of current strategy influence, not as an anatomical identity.

---

## 8. Memory is now a three-level problem

NEURAL25 already rejected `memory = selection weight`.

NEURAL26 makes the decomposition sharper.

### 8.1 Memory content

```text
What from the past remains representable?
```

### 8.2 Memory control

```text
How much current authority does that historical structure retain?
```

### 8.3 Memory geometry / future-path structure

```text
Has the past changed which alternatives are easy to access,
how costly switching is,
and how the system returns after perturbation?
```

A strong SRT-facing memory hypothesis concerns the third level.

The causal progression is:

```text
past selection history
-> current candidate accessibility / authority
-> realized path
-> new write-back
-> altered future accessibility / authority
```

---

## 9. Consciousness relevance — bounded only

The Qin et al. paper concerns disorders of consciousness and anesthesia, but this patch must not turn network complexity into a consciousness definition.

The only safe bridge is:

> Conscious access or recovery may require a neural regime capable of sustaining differentiated and interacting states, but global dynamical capacity alone is not sufficient to establish phenomenal consciousness, stake, subjecthood, or stable SRT anchoring.

This preserves the distinction:

```text
capacity for differentiated neural dynamics
!=
consciousness
```

and also:

```text
behavioral responsiveness
!=
consciousness
```

where supported by broader anesthesia literature.

---

## 10. Mapping to selection-event audit

| Audit element | NEURAL26 contribution |
|---|---|
| CG-0 / DMF | asks whether candidate-relevant differences can effectively enter an active neural regime |
| CG-1 / NER | requires non-equivalent internal registration, not merely global activity |
| CG-2 / PEF | requires candidate state to alter actual path / response probability |
| CG-3 / CBP | not established by entropy/connectivity; must be separately audited |
| CG-4 / HEF | supplied only when realized history changes later accessibility, switching cost, recovery, or reachability |

`C_dyn` is not a sixth CG gate. It is an enabling-condition hypothesis that may constrain whether CG-0/CG-1 processes are even operationally available in a given neural state.

---

## 11. New experimental wedge: capacity vs accessibility vs authority

A strong future experiment should manipulate or stratify **global neural regime** separately from **candidate-specific history / control weight**.

Minimal 2×2 logic:

```text
higher vs lower global dynamical-capacity proxy
x
higher vs lower old-strategy authority
```

Measure separately:

1. whether the novel candidate becomes neurally decodable (`R_i`);
2. whether it enters effective competition (`A_i`);
3. whether it controls behavior (`W_i / PEF`);
4. switching cost;
5. post-perturbation recovery / hysteresis.

### Differential predictions

If global capacity changes only generic arousal or movement:

- candidate-specific accessibility and authority should be explained after controlling generic performance.

If the proposed capacity layer is meaningful:

- matched candidate representations may differ in effective accessibility across global regimes;
- matched accessibility may still differ in authority because candidate-specific historical weights remain separate;
- a global-capacity manipulation should not automatically erase history-dependent switching asymmetry.

This allows three separable failures rather than one vague "consciousness complexity" result.

---

## 12. Relation to NEURAL25 experimental protocol

`SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md` tests:

```text
matched current strategy state
+
different history depth
->
different future accessibility / switching / hysteresis ?
```

NEURAL26 adds a future extension:

```text
matched candidate-specific representation / history state
+
different global dynamical regime
->
different candidate accessibility ?
```

Together they separate:

```text
History-dependent geometry
from
Current global capacity
from
Candidate-specific authority
```

The two effects must not be collapsed into one latent "selection strength" variable.

---

## 13. Strong failure conditions

This bridge must be weakened if:

1. global complexity/connectivity proxies add no predictive value for candidate accessibility or transition capacity beyond generic arousal, signal power, drug identity, or motor performance;
2. candidate accessibility is fully explained by representation strength alone;
3. candidate authority is fully explained by accessibility alone with no independent control-weight / arbitration effect;
4. history-dependent switching and hysteresis vanish once current global capacity and current policy state are matched;
5. high entropy states show no organized candidate differentiation and are better modeled as unstructured variability;
6. a simpler ordinary network/arousal model predicts held-out data as well as the proposed layered architecture.

---

## 14. Forbidden upgrades

Do **not** write:

- `PFC is not representational; it is a selection weight`;
- `PFC = control authority`;
- `entropy = selection capacity`;
- `gamma connectivity = consciousness`;
- `criticality = SRT selection space`;
- `esketamine preserves L0`;
- `propofol collapses L0`;
- `network complexity proves consciousness`;
- `more options / more entropy = more freedom`.

Safer replacements:

- higher-order representations can differ in current control authority;
- global neural dynamics may constrain candidate accessibility without determining which candidate wins;
- entropy/connectivity can be candidate proxy families for an enabling dynamical regime under stated conditions;
- consciousness requires separate evidence beyond global complexity.

---

## 15. De-materialized synthesis sentence

Candidate future compact-core sentence:

> **Neural selection should not be reduced to representation strength. A candidate must arise within a network regime that can sustain differentiated transitions, become accessible to effective competition, obtain enough control authority to alter a real path, and—if the event is history-bearing—write back into the conditions of later selection.**

Do not merge this sentence into the compact core until the proxy distinction and experimental route are reviewed.

---

## 16. Minimal theory increment

NEURAL26's reusable increment is the following separation:

```text
Dynamical Capacity
!=
Candidate Accessibility
!=
Control Authority
!=
Expression
!=
Historical Write-back
```

with representation retained as a separate observable dimension rather than silently identified with any of them.

This turns the question from:

> "Where is the representation?"

into the stronger sequence:

> **What can be represented? What can still enter? What can currently win? What becomes actual? What does that actualization change about the next field of possibilities?**
