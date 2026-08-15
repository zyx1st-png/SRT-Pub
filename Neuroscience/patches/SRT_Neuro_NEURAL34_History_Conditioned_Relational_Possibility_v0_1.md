---
id: SRT-NEURO-NEURAL34-HISTORY-CONDITIONED-RELATIONAL-POSSIBILITY
patch_id: PATCH-NEURO-NEURAL34-HISTORY-CONDITIONED-RELATIONAL-POSSIBILITY
type: bridge_patch
status: active
version: v0_1
canonical: false
claim_level: P3-P4
claim_mode: synthesis
evidence_mode: multi_source_primary_evidence_synthesis
layer: operations
epistemic_layer: os
domain: Neuroscience
created: 2026-08-15
target_future_doc:
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
  - Neuroscience/SRT_Neuro_Predictions_Table.md
  - Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
  - Experiments/SRT_Experimental_Roadmap_v1.md
related_claims:
  - historical_efficacy
  - history_conditioned_future_selectability
  - relational_writeback
  - activity_silent_state
  - metaplasticity
  - selection_history
  - transient_distributed_coordination
  - relational_reinstatement
  - NEURAL23
  - NEURAL31
  - NEURAL33
tags:
  - relational-possibility
  - history
  - metaplasticity
  - working-memory
  - functional-connectivity
  - selection-history
  - ripple
  - replay
  - relational-writeback
  - matched-state
---

# NEURAL34 — History-conditioned relational possibility structure

> **Boundary**: non-canonical P3 synthesis bridge with P4 differential predictions. NEURAL34 does **not** claim that relations are ontologically prior to components, that synchrony is understanding, that ripple is selection, or that a new canonical SRT variable has been discovered. It isolates a narrower empirical pressure: **past co-participation and plastic history can change which coordinated states are later realizable, even when currently observed component activity is similar or when no persistent activity code is detectable.**

---

## 1. Core question

NEURAL33 asks:

```text
which distributed relation is actually realized now?
```

NEURAL34 asks one step earlier:

> **Why was this relation easier to realize than another relation in the first place?**

The candidate answer is not simply `similarity` and not simply `anatomical connectivity`.

The proposed bridge is:

```text
past joint / coupled history
-> plastic reconfiguration
-> altered future relational compatibility
-> current opportunity / phase / context
-> realized coordination
-> further relational writeback
```

Compactly:

\[
H_t \rightarrow K_t \rightarrow R_t \rightarrow K_{t+1},
\]

where all notation is local to this patch.

---

## 2. Local notation: K is not current synchrony

Define, only for analysis:

\[
K_{ij}(t)
=
\text{history-conditioned transition disposition between components }i,j.
\]

Operational meaning:

> Given a declared current state, input and context, how strongly does prior history change the conditional probability that components `i` and `j` will enter a particular coordinated / jointly changing state?

Then:

\[
P\!\left(R_{ij}(t+\Delta t)\right)
=
F\!\left(X_t,K_{ij}(t),E_t,C_t,G_t\right),
\]

where:

- `X_t` = currently observed component activity;
- `K_ij` = history-conditioned relational transition disposition;
- `E_t` = momentary eligibility / timing state;
- `C_t` = task / cue / ecological context;
- `G_t` = shared / global driver variables where declared;
- `R_ij` = realized coordinated relation.

Guards:

```text
K_ij != correlation
K_ij != synaptic weight by definition
K_ij != direct anatomical edge
K_ij != ripple probability
K_ij != latent consciousness
```

`K_ij` is a bridge-level conditional property inferred only if matched-state history manipulations or longitudinal evidence justify it.

---

## 3. Evidence anchor A — Ji & Wilson: experience-specific cross-region relation appears in POST, not PRE

Ji & Wilson, *Nature Neuroscience* 10, 100–107 (2007), DOI `10.1038/nn1825`, simultaneously recorded visual cortex and hippocampus in a `PRE sleep -> RUN -> POST sleep` design.

The critical relation-level result is:

```text
visual-cortex / hippocampal cell pairs
with high correlation during RUN
-> high correlation in POST
but not PRE
```

and high, rather than low, RUN correlation predicted stronger POST correlation. Awake multicell sequences were also replayed in coordinated cortical–hippocampal sleep frames.

Safe pressure:

> **The relation expressed during experience predicts a later cross-region relation that was not equivalently present in PRE sleep.**

This does not establish whether the relevant change resides in direct synapses, common drivers, altered excitability or distributed circuit state.

---

## 4. Evidence anchor B — Miyawaki & Mizuseki: local ensembles can pre-exist while inter-regional coactivation develops after experience

Miyawaki & Mizuseki, *Nature Communications* 13, 1272 (2022), DOI `10.1038/s41467-022-28929-x`, recorded BLA, vCA1 and prelimbic cortex across fear conditioning.

Key dissociation:

```text
some local ensembles were already configured before acquisition
but
significant BLA–PL5 and vCA1–PL5 ensemble coactivation emerged / strengthened in post-conditioning NREM
and reappeared during retrieval
```

These cross-region coactivations were concentrated around HFOs, SWRs and cortical ripples.

The important inference is not `experience creates every component`. It is:

> **experience can selectively create, amplify or stabilize inter-regional coordination among partially preconfigured local elements.**

This directly motivates:

```text
component availability
!=
relational compatibility
```

and:

```text
oscillatory opportunity
!=
which relation is recruited within that opportunity
```

---

## 5. Evidence anchor C — Abbaspoor et al.: experience stabilizes higher-order assembly coupling

Abbaspoor, Aljishi & Hoffman, *Nature Neuroscience* (2026), DOI `10.1038/s41593-026-02357-2`, recorded hippocampal and connected-region assemblies in freely moving macaques.

With greater memory age / experience, assemblies showed:

```text
stronger network connectivity;
stronger sleep reactivation;
more stable task-to-sleep assembly coupling;
longer time-extended interactions.
```

Importantly, the experience-dependent coupling pattern persisted after excluding assembly pairs with high membership similarity, arguing against the effect being only redundant component composition.

Safe pressure:

> **experience can reorganize higher-order inter-assembly dynamics independently of simple assembly-member overlap.**

This strengthens a relation-level account but does not prove that relation variables are independent of all microphysical component states.

---

## 6. Evidence anchor D — Panichello et al.: currently observed firing can return to baseline while cue-specific functional-connection structure remains

Panichello et al., *Nature* (2024), DOI `10.1038/s41586-024-08139-9`, recorded large simultaneous lateral-prefrontal populations in monkeys performing working memory.

During mnemonic `Off` states:

```text
single-neuron cue selectivity collapsed;
average firing returned to spontaneous levels;
```

while mnemonic information remained available in cue-specific patterns of functional connections among neuronal ensembles.

The paper used large simultaneous populations and functional-connection analyses to show that mnemonic state cannot be read from firing-rate magnitude alone during these periods.

Safe pressure:

\[
X_A\approx X_B
\not\Rightarrow
K_A\approx K_B
\]

for the **measured state description**.

Critical guard:

> This does **not** prove that two complete microphysical states are identical while only a relation differs. Unmeasured receptor, synaptic, intracellular or circuit variables may carry the latent difference.

---

## 7. Evidence anchor E — Barbosa et al.: latent synchrony trace can causally bias future behavior

Barbosa et al., *Nature Neuroscience* 23, 1016–1024 (2020), DOI `10.1038/s41593-020-0644-4`, found that previous-trial stimulus information was not decodable from ordinary spiking between trials but was retained in PFC spiking-synchrony structure.

Before the next stimulus, the latent trace reactivated into an activity pattern related to the previous stimulus; reactivation strength tracked serial behavioral bias. Single-pulse TMS over human PFC during the intertrial period altered subsequent serial bias.

This supports a causal-shape claim:

```text
latent history-bearing state
-> later reactivation
-> future choice bias
```

It does not prove that synchrony itself is the unique substrate; the paper models an interaction between persistent activity and activity-silent mechanisms.

---

## 8. Evidence anchor F — selection-history ping: same neutral input can reveal different history-conditioned response dispositions

Duncan, van Moorselaar & Theeuwes, *Nature Communications* 14, 4749 (2023), DOI `10.1038/s41467-023-40405-8`, trained spatial selection history through unequal target-location probabilities.

During the intertrial period:

```text
ongoing EEG did not reliably expose the high-priority learned location
```

but an identical task-irrelevant visual ping revealed the history-mediated priority map in the evoked response. Controls addressed gaze, timing artifacts and preceding-trial repetition.

This is highly relevant to SRT because the logic is:

```text
same class of neutral probe
+ different selection history
-> different evoked response
```

Safe pressure:

> **history may persist as a changed response disposition rather than continuously explicit activity.**

This remains an attention / statistical-learning result, not proof of a general ontological relation principle.

---

## 9. Evidence anchor G — human inter-regional metaplasticity

A human TMS study of SMA-to-M1 metaplasticity showed that priming over supplementary motor area altered the subsequent plastic response of M1 to quadripulse stimulation, while the SMA priming did not itself change motor-evoked potential size.

Safe abstraction:

```text
current observable output remains approximately baseline
but
prior activity history changes how the system responds to the same later plasticity-inducing input
```

This is a direct human example of:

\[
X_t^{(A)}\approx X_t^{(B)}
\]

while:

\[
P(\Delta X_{future}|I,H_A)
\neq
P(\Delta X_{future}|I,H_B).
\]

Metaplasticity therefore supplies a mechanistic analogue of `future possibility structure`, but it must not be equated with SRT `L2` or with `K_ij` by definition.

---

## 10. Evidence synthesis — what is now supportable

Across these paradigms, a convergent weak-to-moderate claim is supportable:

```text
past co-participation / statistical regularity / plastic history
can alter later coordination, reactivation or plastic response
without requiring a continuously explicit current activity code.
```

A stronger but still bounded P3 bridge is:

> **History can become causally effective partly by restructuring the conditional space of future relations, not only by changing the current activation magnitude of individual components.**

This is the core NEURAL34 increment.

---

## 11. Similarity is not the right primitive — compatibility is

NEURAL34 rejects the crude rule:

```text
similar history -> synchrony
```

Different regions can play non-identical, complementary roles and still become tightly coordinated.

The safer concept is:

```text
co-adaptive history
-> dynamical compatibility
```

Analogy:

```text
key != lock
but key can fit lock
```

Therefore:

```text
homology
is one possible route to compatibility
but
compatibility does not require similarity.
```

For cross-bearer social cognition, `selection-history homology` may remain useful. For within-system neural coordination, `history-conditioned compatibility` is the preferred term.

---

## 12. Relation potential != realized relation

NEURAL34 separates:

### Latent relational possibility

\[
K_{ij}(t)
\]

= historically conditioned conditional disposition.

### Realized relation

\[
R_{ij}(t)
\]

= actual co-firing / coordination / coupled transition in a declared window.

### Relational writeback

\[
\Delta K_{ij}
\]

= change in later coordination disposition caused by learning, coactivation, reward/consequence, consolidation or plasticity.

Thus:

\[
K_t
\rightarrow
R_t
\rightarrow
K_{t+1}
\]

is a more useful dynamic bridge than treating a relation as a static graph edge.

---

## 13. Matrix / geometry version

For a system of candidate ensembles, history may reshape not one relation but a compatibility geometry:

\[
\mathcal K_t = [K_{ij}(t)].
\]

An event can then induce:

\[
\mathcal K_t
\rightarrow
\mathcal K_{t+1},
\]

with some relations strengthened, others weakened, separated or gated by context.

This avoids the false assumption:

```text
learning always increases integration
```

Memory systems also learn which contents must remain separated.

---

## 14. Link to NEURAL33 ripple coordination

NEURAL33 shows that brief cross-region ripple windows preferentially realize and reinstate distributed firing relations.

NEURAL34 supplies an upstream hypothesis:

```text
history
-> K / relational possibility structure
-> ripple-compatible opportunity
-> specific relation realization
```

Therefore ripple should not be interpreted as creating the full relation from zero.

A stronger hypothesis is:

> **ripple / phase windows may reveal or recruit a history-shaped relation landscape whose latent compatibility was produced by earlier experience and plasticity.**

This is a cross-study synthesis, not a direct result of the Verzhbinsky study.

---

## 15. Common-driver pressure

Observed synchrony does not establish direct reciprocal relation:

\[
G\rightarrow A,\qquad G\rightarrow B
\]

can yield:

\[
A\sim B.
\]

Therefore a more correct realized-relation model is context-indexed:

\[
R_{ij}(t)
=
F(K_{ij},X_t,E_t,C_t,G_t).
\]

NEURAL34 uses `effective relational compatibility`, not `direct synaptic edge`.

---

## 16. Strongest ontology guard

The evidence does **not** establish:

```text
relations exist independently of components;
relations are more fundamental than matter;
identical complete microstates can differ only relationally;
SRT relational ontology is empirically proven.
```

The strongest defensible philosophical bridge is narrower:

> **A relational property need not be ontologically independent of component microstates to be causally and explanatorily indispensable at a declared level.**

For example, a `key fits lock` relation depends on both material objects but is not a property of either one considered alone.

Likewise, neural coordination compatibility may ultimately be implemented by receptor states, connectivity, excitability, cellular plasticity and shared circuitry while remaining an indispensable relation-level description of future joint behavior.

---

## 17. Activity-silent guard

NEURAL34 must not become:

```text
memory = activity-silent relation state
```

Persistent and intermittent activity codes remain empirically important, and different tasks / brain areas can mix active and latent mechanisms.

Preferred form:

\[
\text{neural implementation}
=
X_t + \mathcal K_t + \text{context / timing variables}
\]

where neither `X` nor `K` is assumed universally sufficient.

---

## 18. Falsification pressure — prevent K from becoming a garbage variable

`K` must not mean `everything unmeasured`.

Operational admission rule:

> A `K`-like history-conditioned relational disposition is justified only when a preregistered history manipulation predicts a later relation-specific response after current observable component state, input and major shared-driver confounds are matched or modeled.

Required differential form:

\[
P(R_{future}|X,E,C,G,H)
>
P(R_{future}|X,E,C,G)
\]

in stable out-of-sample prediction or intervention.

Downgrade NEURAL34 if:

```text
history adds no relation-specific prediction after strong current-state controls;
all effects collapse to a single-node excitability variable;
common input fully explains pair-specific coordination;
relational metrics add no predictive value beyond component state;
matched-current-state history manipulations do not alter future joint response.
```

---

## 19. Relation to mutual intelligibility

NEURAL34 does **not** say brain regions understand one another.

The possible higher-order analogy is:

```text
neural system:
history-conditioned compatibility -> lower coordination friction

cross-bearer cognition:
selection-history homology -> lower translation / prediction friction
```

Shared abstraction:

> **past co-constraint can change future mutual responsiveness.**

This is a candidate common principle, not evidence that neural synchrony and interpersonal understanding are the same process.

---

## 20. Central SRT-facing compression

Retain as the main P3 bridge:

> **Past history can remain effective by changing not only which components are active, but which joint transitions and relations are easier or harder to realize next.**

Retain as the stronger relational version:

> **A relation need not first appear when synchrony is observed: prior history may already have changed the system's conditional ability to enter that coordinated state, while the current ripple / phase window merely makes that latent compatibility dynamically effective.**

These are bridge claims, not canonical SRT definitions.
