---
id: SRT-NEURO-NEURAL28-REIDENTIFIABLE-OBJECT-IDENTITY-DYNAMIC-CONCEPT-INDEX
patch_id: PATCH-NEURO-NEURAL28-REIDENTIFIABLE-OBJECT-IDENTITY-DYNAMIC-CONCEPT-INDEX
type: bridge_patch
status: active
version: v0_1
canonical: false
claim_level: P3-P4
claim_mode: evidence
layer: operations
epistemic_layer: os
domain: Neuroscience
source_ids: [SRC-2026-08-10-NEURO-CONCEPT-CELLS-REIDENTIFIABLE-OBJECT-IDENTITY]
created: 2026-08-10
target_future_doc:
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
  - 01_Source_Intuition/BOOK/Drafts_26Q/Q02_对象化.md
  - Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
related_claims: [objectification, L1, L2, NEURAL25, NEURAL27, memory, historical_efficacy, relational_binding]
tags: [concept-cells, objectification, object-identity, reidentification, reentry, abstraction, hippocampus, pronouns, working-memory, relational-binding]
---

# NEURAL28 — Re-identifiable object identity and dynamic concept indexing

> **Boundary**: P3 neuroscience bridge with P4 experimental consequences. This patch does not redefine objectification, objecthood, `L1`, `L2`, memory, `G_hat_theta`, real choice, subjecthood or consciousness. It uses human single-neuron evidence to sharpen one implementation question: what makes an already-formed identity remain available across changing presentations, references and relations?

## 1. Source anchor

Verified primary anchors:

- Quian Quiroga et al. (2005), *Nature*, DOI `10.1038/nature03687` — sparse invariant concept-related responses across different presentations.
- Bausch et al. (2021), *Nature Communications*, DOI `10.1038/s41467-021-26386-6` — relation-dependent concept-neuron reactivation and reinstatement after periods without detectable activity.
- Dijksterhuis et al. (2024), *Science*, DOI `10.1126/science.adr2813` — pronouns reactivate hippocampal neurons selective for the nouns to which the pronouns refer.
- Mackay et al. (2024), *Nature Communications*, DOI `10.1038/s41467-024-52295-5` — concept- and location-selective activity predicts successful item-location encoding and is compatible with indexing accounts.
- Daume et al. (2024), *Neuron*, DOI `10.1016/j.neuron.2024.09.013` — content-selective persistent activity during working-memory maintenance predicts later long-term memory formation while initial visually evoked activity does not show the same relation.

The trigger article is Quanta Magazine (2025-01-21). Its speculative "Swiss Army cell" framing is not used as an evidential premise.

---

## 2. Why this matters for SRT

Current SRT objectification prose correctly resists the idea that cognition simply copies a pre-cut world into an internal object inventory. But the dominant metaphor of "cutting" or "freezing" can be misread too statically.

NEURAL28 adds a narrower implementation pressure:

> **A usable object identity need not remain continuously instantiated in one unchanging internal state. It can remain stable by being re-identifiable — different presentations, references and task relations can still regain access to a sufficiently stable conceptual address.**

This does not answer the pre-objectification question. It operates downstream:

```text
pre-object flow / differentiation
-> provisional object stabilization
-> re-identifiable conceptual address
-> relational reinstatement
-> maintenance / binding
-> possible historical write-back
```

The bridge therefore extends Q02 rather than replacing it.

---

## 3. Main SRT bridge claim

### NEURAL28 core claim

> **Object stability should not be modeled only as persistence of a fixed representation. At the neural implementation level, a stronger criterion is re-identifiability across change: sufficiently different sensory tokens, discourse references or task-relevant relations can still reactivate the same concept-level identity.**

Short form:

> **Stable identity is not necessarily a frozen state; it can be a stable route of return.**

This is a P3 bridge sentence, not a canonical definition of objecthood.

---

## 4. Five-stage decomposition

NEURAL28 separates five processes that are often collapsed:

```text
Differentiation
-> Identification
-> Re-identification
-> Relational recruitment
-> Historical incorporation
```

1. **Differentiation** — current input is discriminated from alternatives.
2. **Identification** — the current event is stabilized as a particular concept / object identity.
3. **Re-identification** — a changed presentation or indirect cue regains access to that identity.
4. **Relational recruitment** — the identity is brought into current processing because a task, sentence or comparison requires it.
5. **Historical incorporation** — the episode changes later accessibility, binding, switching or prospective behavior.

Important negatives:

```text
perceptual discrimination != concept identity
concept identity != current relational recruitment
relational recruitment != control authority
working-memory maintenance != long-term write-back
```

This decomposition complements NEURAL25's:

```text
Acquisition -> Availability -> Authority -> Expression -> Write-back
```

NEURAL28 mainly hardens the upstream `Acquisition / Availability` side by distinguishing identity formation from later re-entry.

---

## 5. Pronoun reactivation: current input is underdetermined by itself

Dijksterhuis et al. provide the cleanest bridge case.

A pronoun such as `he` or `she` does not carry the full identity of its referent. Yet neurons selective for a previously introduced noun are reactivated when the later pronoun refers back to that noun.

Local bridge form:

\[
C_i(t)=F(x_t, H_t, R_t)
\]

where:

- `x_t` = current token / cue;
- `H_t` = discourse history;
- `R_t` = current reference relation;
- `C_i` = reactivated concept-level identity.

The relevant inequality is:

```text
current token alone
<
current token + prior relational history
```

for explaining which identity is reactivated.

SRT-safe interpretation:

> A current manifestation can be insufficient to determine its currently operative object identity; prior structured history can supply the route by which an underspecified cue re-enters an already stabilized identity.

Do not write `pronoun resolution = L2 selection`.

---

## 6. Relational recruitment: identity can be stable while access is task-dependent

Bausch et al. found that concept neurons can respond to non-preferred stimuli when the task requires comparing those stimuli with the neuron's preferred concept. This supports:

```text
stable preferred semantic relation
+
current task relation
-> context-sensitive reactivation
```

It does **not** support:

```text
neuron has no stable semantic preference
or
neuron can arbitrarily become any concept/place/time cell on demand
```

The important distinction is:

> **semantic address stability and relational recruitment flexibility can coexist.**

This is the bridge's anti-binary correction.

---

## 7. Re-entry without continuous manifestation

Bausch et al. also report reactivation after intervals without detectable activity. Even if later work constrains the strongest activity-silent interpretation, the safe claim remains:

```text
continuous overt firing is not required
for later reinstatement of the same concept relation
```

This offers a useful SRT analogy:

```text
current explicit L1-like neural expression absent
!=
historical accessibility necessarily absent
```

But the analogy must stop there. A silent neural state, synaptic trace or working-memory mechanism is not thereby canonical `L2`.

---

## 8. What/where binding and index-like addresses

Mackay et al. show that successful item-location memory formation is associated with stronger firing in concept-selective and location-selective neuron populations. Their indexing interpretation suggests a mechanism in which selective neurons can function as pointers into distributed semantic or contextual representations.

SRT-facing use:

> The same identity can become a reusable address that participates in new bindings without carrying the full sensory episode inside itself.

This supports the idea of a **conceptual address**, not the identity:

```text
concept cell = object
```

nor:

```text
hippocampal index = SRT selector
```

---

## 9. Working-memory maintenance and historical incorporation

Daume et al. sharpen a stage distinction:

```text
visually evoked category-selective response
!=
content-selective persistent maintenance
!=
later successful long-term recognition
```

A current concept can therefore be:

- identified;
- maintained as currently available;
- or successfully incorporated into longer-term memory;

without those being the same event.

This fits NEURAL25's general anti-collapse rule and blocks a tempting but invalid inference:

```text
concept neuron fired
therefore
history was durably rewritten
```

---

## 10. Relation to Q02 objectification

Q02 currently emphasizes that objectification cuts continuous process into a graspable, communicable format. NEURAL28 suggests a future refinement:

```text
boundary formation
+
re-identifiability across change
=
more complete cognitive object-stability picture
```

The important conceptual change is from:

> object = a frozen slice

Toward:

> object = a temporarily stabilized identity that can be found again despite changes in presentation and relation.

This wording is intentionally non-canonical and belongs first in companion/book synthesis, not in core ontology.

Potential native book sentence:

> **对象之所以稳定，不一定因为脑中一直保存着一个不变的副本；更可能因为变化之后，我们仍有办法重新回到“同一个东西”。稳定不是停止变化，而是在变化中保留一条可返回的身份路径。**

Do not insert this sentence into Q02 during the current material-backlog phase.

---

## 11. Relation to NEURAL25 and NEURAL27

The three bridges now form a clean chain:

```text
NEURAL28
what can be found again?
re-identifiable identity / relational re-entry
        ↓
NEURAL25
what can enter competition and gain control?
availability / authority / expression / write-back
        ↓
NEURAL27
how does past history alter a later prospective path?
history-conditioned anticipatory divergence
```

This prevents the memory line from starting too late. Future path bias requires some history-bearing content or relation to remain addressable enough to be recruited again.

---

## 12. Relation to `L1` / `L2`

A bounded mapping is possible:

```text
current concept activation / reactivation
~ current manifest neural event

historically supported re-accessibility
~ candidate L2-like implementation property
```

But:

```text
concept neuron != L1
hippocampus != L2
re-identifiability != canonical L2
semantic memory != L2 by definition
```

The bridge only says that history can affect what identities remain easy to reinstate in later current states.

---

## 13. Local formal bridge

Define a non-canonical **re-identification robustness** score for concept `i`:

\[
RI_i = E_{c \in C_i}\left[ P(\hat i=i\mid c,H_i,R_i,T_i) \right]
\]

where `C_i` is a declared set of altered presentations / references / task contexts belonging to concept `i`.

This is not an SRT primitive. It is a potential experimental descriptor.

A stronger history-sensitive test compares:

\[
P(C_i^{react}\mid x,H_1,R,T)
\neq
P(C_i^{react}\mid x,H_0,R,T)
\]

while holding the current cue `x` as constant as feasible and varying whether the relevant identity relation was established in prior history.

This isolates historical re-entry from simple stimulus-driven response.

---

## 14. P4 discriminating predictions

### P4-1 — Same cue, different referential history

Hold the current ambiguous / underspecified cue constant while changing prior discourse history. Predict concept-specific reinstatement according to the established referent rather than current cue features alone.

### P4-2 — Same preferred concept, different task relation

Present a non-preferred stimulus under relation-required vs relation-irrelevant tasks. Predict delayed reinstatement only when the preferred concept is required for the current relation.

### P4-3 — Re-identification robustness vs ordinary recognition strength

Across altered presentations, test whether cross-context re-identification predicts later associative binding or transfer beyond single-presentation recognition accuracy and current firing amplitude.

### P4-4 — Link to historical efficacy

After matching current recognition and immediate concept-reactivation strength, test whether deeper prior relational history predicts later accessibility, switching cost, transfer or prospective path bias. If not, NEURAL28 should remain a representation/retrieval bridge rather than an `L2`-hardening bridge.

---

## 15. Failure conditions

Weaken NEURAL28 if:

1. pronoun/reactivation effects reduce to local lexical or sensory similarity after appropriate controls;
2. relation-dependent reactivation does not replicate across tasks or is fully explained by generic attention/arousal;
3. cross-presentation concept selectivity fails to predict any re-identification or binding advantage beyond ordinary recognition strength;
4. history depth adds no residual prediction after current recognition, familiarity, attention and immediate representation strength are matched;
5. task-dependent responses support unrestricted remapping rather than relatively stable semantic addressing — in that case the "stable address" formulation must be weakened;
6. future evidence shows that the concept-cell framing has no explanatory advantage over a population-level account for the target discrimination.

Do not rescue the bridge by redescribing every successful retrieval as "re-entry" after the fact.

---

## 16. Do not infer

Do not write:

- concept cells prove SRT objectification;
- one concept is stored in one neuron;
- concept cells perform early object recognition;
- concept cell = object;
- hippocampal index = `G_hat_theta`;
- re-identification = `L2`;
- persistent firing = memory;
- activity silence proves latent `L2` storage;
- pronoun resolution = real choice;
- every task-dependent response is a new object identity;
- the "Swiss Army cell" hypothesis is established;
- stable identity requires a literally static neural state.

---

## 17. Integration sentence

Candidate de-materialized sentence for a future neuroscience synthesis:

> **An object representation can remain stable without remaining static. Human medial-temporal-lobe recordings show that an established concept can be recovered across altered presentations, indirect discourse references and task-relevant relations, while maintenance and later memory formation remain separable stages. This suggests an implementation-level criterion of object stability as re-identifiability: history preserves routes by which an identity can re-enter current processing, not necessarily an unchanged internal copy that stays continuously active.**

Do not merge into an owner document until the neuroscience synthesis queue or the book's material-backflow phase is reopened.

---

## 18. Abstract

Human concept-neuron studies provide a bounded bridge between SRT's objectification problem and its recent memory/historical-efficacy work. Cross-presentation concept selectivity shows that some medial-temporal-lobe neurons participate in abstract identities that are not reducible to current low-level features. Pronoun experiments show that an underspecified current token can reactivate the concept introduced by prior discourse history; relation-comparison experiments show task-dependent reinstatement of a stable preferred concept; item-location and working-memory studies separate concept availability, associative binding, maintenance and later long-term memory. The SRT increment is not "concept cells are objectification." It is a refinement of stability: a cognitive object may be stable because it remains re-identifiable and re-addressable across change. That bridge is P3/P4, compatible with but not constitutive of `L1/L2`, and must remain separate from claims about real choice, consciousness or canonical ontology.