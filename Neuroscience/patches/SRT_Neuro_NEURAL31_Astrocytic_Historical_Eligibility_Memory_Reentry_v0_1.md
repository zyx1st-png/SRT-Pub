---
id: SRT-NEURO-NEURAL31-ASTROCYTIC-HISTORICAL-ELIGIBILITY-MEMORY-REENTRY
patch_id: PATCH-NEURO-NEURAL31-ASTROCYTIC-HISTORICAL-ELIGIBILITY-MEMORY-REENTRY
type: bridge_patch
status: active
version: v0_1
canonical: false
claim_level: P3-P4
claim_mode: evidence
layer: operations
epistemic_layer: os
domain: Neuroscience
source_ids:
  - SRC-2026-08-10-NEURO-BRZOSTOWICKI-ASTROENGRAM-MEMORY-TRACE
created: 2026-08-12
target_future_doc:
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
  - Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
  - Neuroscience/SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md
related_claims:
  - memory
  - historical_efficacy
  - history_conditioned_future_selectability
  - retrievability
  - reconsolidation
  - astrocytic_eligibility
  - NEURAL27
  - NEURAL29
  - T_L2_Scaffold
  - P1_T02
  - P1_T03
tags:
  - astrocytes
  - astroengram
  - memory
  - engram
  - retrievability
  - eligibility
  - reentry
  - reconsolidation
  - fear-conditioning
  - historical-constraint
---

# NEURAL31 — Astrocytic historical eligibility and memory re-entry

> **Boundary**: P3 neuroscience bridge with P4 experimental consequences. This patch does **not** redefine memory, engram, `L1`, `L2`, `G_hat_theta`, `Psi_f`, `d`, `T_dir`, ontological time, bearer, subjecthood or consciousness. It does not claim that astrocytes independently store memory content. It isolates a narrower mechanism candidate: experience-dependent astrocytic states can help determine whether, when and how a prior neuronal trajectory is re-entered, stabilized or generalized.

---

## 1. Source anchor

Primary trigger:

```text
David Brzostowicki
Are parts of the memory trace found in the ‘astroengram?’
The Transmitter
2026-08-10
```

Peer-reviewed anchors verified in the processing pass:

- Sánchez Romero & Navarrete, *Astroengrams: rethinking the cellular substrate for memory*, Nature Reviews Neuroscience (2026), doi:`10.1038/s41583-025-01012-2`.
- *Astrocyte ensembles manipulated with AstroLight tune cue-motivated behavior*, Nature Neuroscience (2025), doi:`10.1038/s41593-025-01870-0`.
- *Learning-associated astrocyte ensembles regulate memory recall*, Nature (2024), doi:`10.1038/s41586-024-08170-w`.
- *The astrocytic ensemble acts as a multiday trace to stabilize memory*, Nature (2025), doi:`10.1038/s41586-025-09619-2`.

SourceCard:

```text
Materials/2026/SRC_2026_08_10_Neuro_Brzostowicki_Astroengram_Memory_Trace.md
```

---

## 2. Why NEURAL31 is not NEURAL29 again

`NEURAL29` established the missing transformation stage:

```text
Retention
-> Transformation
-> later change in recognition / generalization / inference
```

NEURAL31 addresses a different question:

```text
A transformed / retained history exists
-> under what conditions can the old trajectory re-enter current processing?
-> how is that re-entry stabilized, sharpened or generalized?
```

The clean separation is:

```text
NEURAL29 = historical transformation before later use
NEURAL31 = historical eligibility and retrievability at later re-entry
```

The two should be linked but not collapsed.

---

## 3. Main bridge claim

> **Past experience can leave an astrocytic state that is not well described as a static copy of memory content but can alter the later retrievability, stabilization and precision of a memory-related neuronal ensemble.**

SRT-facing compression:

```text
past experience
-> latent astrocytic historical state
-> altered re-entry conditions
-> changed probability / stability / precision of later memory expression
```

This is a domain bridge, not a new canonical SRT memory definition.

---

## 4. Three-way decomposition: content, retrievability, eligibility

To prevent `causal influence on recall` from being mistaken for `content storage`, NEURAL31 separates three functions.

### 4.1 Content constraint

Local notation:

```text
N_m = neuronal / circuit-level pattern-specific constraint associated with memory m
```

Current engram evidence remains strongest for neurons as the core pattern-specific content substrate in the paradigms discussed.

### 4.2 Retrievability landscape

Local notation:

```text
R_m(t) = current accessibility of memory-related trajectory m under present cue/state
```

`R_m` can vary even when some content-bearing structure persists.

Therefore:

```text
failure of recall
!= absence of all historical trace
```

### 4.3 Historical eligibility state

Local notation:

```text
A_m^hist(t) = experience-dependent astrocytic state that changes how later signals affect m
```

This can include latent receptor/transcriptional priming, ensemble-specific calcium responsiveness or other declared astrocytic state variables.

NEURAL31 uses `A_m^hist` only as a bridge label. It is not canonical `L2` and not a claim that one astrocyte ensemble uniquely indexes one memory.

---

## 5. Minimal non-canonical re-entry model

Let:

- `C_t` = current cue/context;
- `S_t` = declared global physiological / affective state;
- `N_m` = local content-related neuronal constraint;
- `A_m^hist` = astrocytic historical eligibility state;
- `R_m` = resulting memory-trajectory retrievability.

A bounded bridge is:

\[
R_m(t) = f\!\left(C_t, S_t, N_m, A_m^{hist}(t)\right)
\]

with later expression:

\[
P\!\left(M_m^{reentry}\mid C_t,S_t\right)
= g\!\left(R_m(t)\right)
\]

The important discrimination is:

\[
A_m^{hist}\neq M_m^{content}
\]

unless independent content-carrying evidence is supplied.

This formalism is local to NEURAL31 and must not be read as an SRT core equation.

---

## 6. Evidence pattern A — learning-linked astrocyte ensembles can alter later behavior

AstroLight and learning-associated-astrocyte studies support the causal shape:

```text
experience-linked astrocyte tagging
+ later selective manipulation
-> changed learned / recall-related behavior
```

This shows that astrocytes can be causally consequential for later memory expression.

It does **not** yet establish:

```text
astrocytic ensemble alone
= complete cue-specific memory trace
```

The correct evidential upgrade is from `support only` to `causal component candidate`, not directly to `independent storage substrate`.

---

## 7. Evidence pattern B — multiday priming behaves like historical eligibility

The 2025 Nature multiday-trace study is the strongest bridge for NEURAL31 because the earlier event can alter later astrocytic responsiveness before strong recall-time activation.

SRT-safe process description:

```text
initial experience
-> persistent astrocytic priming
-> later local neuronal + neuromodulatory convergence
-> astrocytic engagement during recall
-> altered stabilization / precision of neuronal ensemble
```

The key conceptual increment is:

> **The past can remain effective by changing how future events are admitted into stabilization, not only by preserving a directly readable content object.**

This is why NEURAL31 uses the term `historical eligibility`.

---

## 8. Emotional-state confound is a required negative control

Fear-conditioning experiments can confound:

```text
memory-specific re-entry
```

with:

```text
general fear / arousal / stress-state modulation
```

A mouse freezing after astrocyte activation does not by itself show that a particular learned episode was retrieved.

NEURAL31 therefore requires:

```text
cue-specific recall effect
> matched general fear / arousal effect
```

for any stronger memory-specific interpretation.

This negative control is central, not optional.

---

## 9. Independent astroengram test

The strongest version of the astroengram hypothesis would require a dissociation approximately like:

```text
1. label astrocytes during learning
2. independently identify / suppress the relevant neuronal engram
3. reactivate only the learning-linked astrocytes with verified temporal precision
4. demonstrate cue-specific recall rather than generalized fear
5. verify neuronal suppression and astrocytic activation simultaneously
```

Possible outcomes:

### Outcome A — cue-specific recall survives neuronal-engram suppression

This would materially strengthen the hypothesis that astrocytes carry memory-specific information rather than merely regulate access.

### Outcome B — recall disappears but astrocyte manipulation still shifts state / gain

This supports a retrievability / state-regulation interpretation.

### Outcome C — effects vanish under better astrocyte-specific controls

This would weaken the astroengram bridge and require downgrading NEURAL31.

---

## 10. Memory persistence as preserved re-entry condition

NEURAL31 proposes the following P3 SRT-facing interpretation:

> **Memory persistence can partly consist in preserved conditions for selective re-entry, not only in preserved content.**

Compactly:

```text
Past selection
-> historical trace
-> changed future accessibility
-> biased re-entry
```

This does not mean that every memory is reducible to accessibility. It means that `what remains stored` and `what remains re-enterable` are experimentally separable questions.

---

## 11. Forgetting decomposition

NEURAL31 motivates three empirically separable failure modes.

### F1. Trace degradation

```text
content-bearing / historical structure weakens or disappears
```

### F2. Retrieval / access failure

```text
relevant history persists
but current cue/state does not reopen the trajectory
```

### F3. Competitive displacement

```text
old trajectory persists
but alternative trajectories acquire greater accessibility / authority
```

Therefore:

```text
behavioral forgetting
!= demonstrated erasure
```

This is a bridge-level decomposition, not a universal taxonomy of all forgetting.

---

## 12. Reconsolidation as re-entry plus write-back

NEURAL31 connects naturally to NEURAL29 and NEURAL25:

```text
historical trace
-> re-entry
-> temporarily modifiable active state
-> current-input interaction
-> restabilization / write-back
```

A safe SRT-facing interpretation is:

> **Re-entry can expose an already sedimented historical constraint to new write-back without changing the irreversibility of the original event.**

This yields the distinction:

```text
history is irreversible
!= historical influence is immutable
```

Do not infer that every recall event triggers the same reconsolidation process.

---

## 13. Bridge to P1-T02 / P1-T03 and T-L2-Scaffold

Current SRT already fixes three structural claims:

```text
P1-T02
real selection leaves irreversible historical trace

P1-T03
sedimented L2 structure constrains future selection

T-L2-Scaffold
re-traversed compatible paths can become lower-friction / more accessible background scaffold
```

NEURAL31 does not prove these claims from neuroscience.

Its contribution is a biological implementation window:

```text
experience-dependent cellular history
-> altered later accessibility / stabilization
```

This is structurally consonant with history-conditioned future selection while preserving `memory != L2`.

---

## 14. Relation to the existing astrocytic associative-memory capacity line

The owner neuroscience file already contains an astrocyte associative-memory patch based on theoretical neuron-astrocyte models in which process-to-process signaling can generate higher-order effective coupling.

Keep the two lines orthogonal:

```text
Astrocytic associative-memory capacity line
= higher-order coupling / attractor capacity / geometry

NEURAL31 astroengram line
= eligibility / retrievability / stabilization / precision
```

Current astroengram experiments do not validate the specific quartic / higher-order coupling mechanism of the theoretical model.

---

## 15. Updated memory sequence

When the memory synthesis reopens, the preferred explanatory sequence becomes:

```text
NEURAL28
Identification / re-identification / relational re-entry indexing

-> NEURAL29
Retention / transformation / decontextualization / integration

-> NEURAL31
Historical eligibility / retrievability / re-entry conditions

-> NEURAL25
Accessibility / authority / expression / write-back

-> NEURAL27
Prospective history-use / future path-bias readout
```

This is a functional decomposition, not a mandatory anatomical or temporal pipeline.

---

## 16. P4 experimental consequences

### Test 1 — matched content, different astrocytic eligibility

Match conventional retention performance and neuronal content readouts as closely as possible while perturbing the learning-linked astrocytic state.

Prediction target:

```text
matched retained content
+ different astrocytic eligibility
-> different recall probability / precision / reconsolidation behavior
```

### Test 2 — memory-specificity against state control

Compare cue-specific recall with independent fear/arousal assays.

Required signature:

```text
memory-specific effect survives state matching
```

### Test 3 — timing decomposition

Perturb astrocytic signaling separately during:

```text
encoding
sleep / offline interval
pre-recall
recall
post-recall restabilization
```

The bridge strengthens if distinct timing windows dissociate formation, eligibility, retrieval and restabilization functions.

### Test 4 — independent neuronal suppression

The decisive strong-astroengram test remains selective astrocyte reactivation under verified suppression of the relevant neuronal engram with cue-specific behavioral readout.

---

## 17. Failure / downgrade conditions

Downgrade NEURAL31 if:

1. astrocyte effects reduce to general arousal/fear across sufficiently controlled paradigms;
2. tagged astrocytic state adds no predictive or causal power once neuronal ensemble state is measured;
3. temporal-specific astrocyte perturbation does not dissociate retrieval / stabilization from general performance changes;
4. method-independent replication fails;
5. the effects cannot be localized beyond broad astrocyte-network propagation.

Do **not** downgrade merely because astrocytes fail the strongest independent-content test; that would reject `astrocyte as independent engram` while leaving the weaker eligibility / retrievability bridge viable.

---

## 18. Do not include

- `astrocyte = memory`;
- `astrocyte = L2`;
- `neuronal engram = all memory content` as a universal identity;
- fear behavior as automatic proof of episodic recall;
- `Ca2+ activity = memory code`;
- astrocytic priming as direct measurement of `Psi_f`, `d` or `T_dir`;
- `reconsolidation = rewriting the past`;
- the theoretical astrocyte higher-order-coupling model as empirically confirmed by astroengram experiments;
- any claim that the current evidence establishes a complete cellular ontology of memory.

---

## 19. Compact synthesis

The strongest NEURAL31 sentence is:

> **Past experience can leave non-neuronal historical states that modify the future re-entry conditions of memory-related neuronal trajectories.**

The stronger SRT bridge is:

> **Memory is one mechanism by which irreversible history becomes causally effective in future selection; some of that efficacy may reside in preserved conditions for re-entry rather than preserved content alone.**

Keep the second sentence P3 unless a broader cross-domain memory theorem is separately hardened.
