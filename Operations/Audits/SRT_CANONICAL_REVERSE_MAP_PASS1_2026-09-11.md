---
id: SRT-CANONICAL-REVERSE-MAP-PASS1-20260911
type: audit
status: active
record_stage: canonical_reverse_map_pass1
layer: operations
epistemic_layer: os
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
root_question: Which current canonical owners survive, require retyping, or must remain open after the author-adjudicated PR936 canonical-independent reconstruction?
comparative_claim: none
named_comparator: none
n_mode_triggered: false
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PR936_CANONICAL_INDEPENDENT_RECONSTRUCTION_2026-09-11.md
  - Core_Law/SRT_L0_Metaphysics.md
  - Core/SRT_Core_21b_Constitutive_Theorems.md
  - Core_Law/SRT_Individuation.md
  - Core/SRT_Core_12b_Ontology_L2.md
  - _SRT_D_VALUE_CANONICAL.md
  - Core/SRT_OPEN_TENSIONS.md
  - Governance/SRT_EDIT_PROTOCOL.md
  - Governance/SRT_CANONICAL_FREEZE.md
tags: [CanonicalReverseMap, PR936, One, StableISP, SubjectPosition, Individuation, Sigma, L2, DValue, EditRisk]
---

# SRT canonical reverse-map — Pass 1 — 2026-09-11

## 0. Purpose and hard boundary

This audit is the first workline after the author-adjudicated canonical-independent reconstruction merged in PR #936.

It does **not** edit canonical theory. It asks a narrower question:

> given the author-adjudicated reconstruction baseline, what should happen to the current owners if/when a later canonical rewrite is authorized?

The action vocabulary is:

```text
RETAIN
REWRITE
DEMOTE
MERGE / ALIAS
RETIRE
ADD
OPEN
```

This is a reverse-map, not a landing PR. A classification here is a proposed future treatment, not a current definition change.

### Controlling author adjudication from PR #936

```text
D1 = ACCEPT
state vocabulary != process grammar

D2 = ACCEPT AS RECONSTRUCTION DIRECTION
L2-core = scale-relative durable / re-enterable background organization
          through which Selection continues at structural grain
final universal gates = OPEN

D3 = ACCEPT AS LIVE SPLIT ONLY
Stable ISP < subject-position
subject sufficiency = OPEN
S1 / S2 / S3 remain separately auditable

D4a = ACCEPT
One = localized, lineage-relative, processual formed unity
      recurrently reconstituted through Selection-mediated history

D4b = OPEN
exact minimum future-selectability burden of every One

D4c = OPEN
exact One / passive / active Selection relation
```

Additional guards retained from #936:

```text
d-value may not be used circularly to prove subjecthood;
bearing / self-consequence / 承担 remain typed at different strengths;
sigma phase ownership must be re-audited;
One != Active Selection by definition;
phenomenality / experiencer necessity remains OPEN.
```

### Repository state at start

```text
main = 733bb5c0d64cd0813fbf1d3afcf3acbf2456ed02
open PRs at start = 0
PR #936 = merged
canonical theory edits in this pass = 0
Level 2 = HOLD
scientific distinctiveness = NOT ESTABLISHED
whole-architecture non-substitutability = NOT ESTABLISHED
```

`STATUS.md` still summarizes the earlier #931/#933 checkpoint. It is therefore used here only as historical/current-dashboard context and does not override the later author adjudication merged in #936.

---

## 1. Mapping method

For each owner, this audit separates four questions:

1. **what the current owner actually owns now;**
2. **what PR #936 changes or does not change;**
3. **the proposed reverse-map action;**
4. **the future edit risk if that action is landed.**

Edit-risk letters follow `Governance/SRT_EDIT_PROTOCOL.md`:

```text
A = no theory-definition change
B = interface / routing / bridge role change
C = canonical or core theory-definition semantic change
```

The classification of a claim and the edit-risk of changing its file are separate axes.

---

# 2. Executive reverse-map

## 2.1 File-level summary

| Current owner | Pass-1 disposition | Why | Future risk |
|---|---|---|---|
| `Core_Law/SRT_L0_Metaphysics.md` | **RETAIN core / narrow clarification only** | Its subjectless Selection, actualisation/persistence/Stable-ISP separation, three-state non-parallel reading, consequence non-outsourcing and concern boundaries are broadly compatible with #936. The main problem is downstream files over-reading L0, not L0 itself. | Any semantic edit = C; no C-edit yet justified by #936 alone. |
| `Core/SRT_Core_21b_Constitutive_Theorems.md` P1-T06 | **RETAIN structural standing + REWRITE downstream identity links** | The four Stable-ISP conditions remain useful, but `T-IND-2 = entry into that same state` is incompatible with author-adjudicated `Stable ISP < subject-position`. Consequence-bearing also needs typed separation from subject-level 承担. | C |
| `Core_Law/SRT_Individuation.md` | **major REWRITE / partial RETIRE / sigma ownership OPEN** | The file explicitly identifies ISP entry with subject-position entry and makes `σ_sub` the subject-transition coordinate. That no longer survives D3 unchanged. | C |
| `Core/SRT_Core_12b_Ontology_L2.md` | **REWRITE / scope-split; retain structural-grain core** | Its strongest surviving core is already close to D2: Selection continues at structural grain. Historical sedimentation, low-Ψ, shareability and agency allocation cannot all remain universal L2 gates without further adjudication. | C for core definition; B/C for routing split |
| `_SRT_D_VALUE_CANONICAL.md` | **RETAIN downstream readout + REWRITE applicability guard** | `d` may remain a stake-coupled subject-level readout, but it cannot be used to establish the subject whose utility / closure it already presupposes. | C for canonical usage/definition boundary |

## 2.2 Main result

The reverse-map does **not** support a wholesale replacement of the current canonical stack.

The largest pressure is concentrated in three identities / universalizations:

```text
A. P1-T06 Stable ISP
   = T-IND-2 subject-position / ISP entry
   -> must be broken

B. sigma_sub
   = natural subject-entry phase owner
   -> must be reopened / demoted to model-local tracking until reassigned

C. L2
   = path sedimentation + low-Psi + shareability + agency layer
     as one universal definition
   -> must be decomposed into core vs realization-specific burdens
```

The strongest retained spine is:

```text
subjectless Selection
-> actualisation / manifestation
-> historical writeback / anchoring
-> processual formed continuity (One; D4a)
-> Stable ISP structural standing
-> subject-position as a thicker downstream standing (D3 live split)
```

The exact gates between these nodes remain partly OPEN. This audit does not invent missing sufficiency theorems.

---

# 3. Owner 1 — `Core_Law/SRT_L0_Metaphysics.md`

## 3.1 Current load-bearing claims

The current L0 owner already fixes several distinctions that remain useful after #936:

```text
Selection precedes manifest actuality;
Selection does not require a prior chooser;
primitive actualisation != anchoring persistence != Stable ISP;
potential / manifest / stable are three states of one process, not three independent worlds;
primitive actualisation and later constraint can co-evolve after actualisation;
承担 = own consequence cannot be fully externalized;
关切 = differential endogenous inclusion of conditions into continuity / payability / later selection space.
```

It also already says that stable structures are historical and reusable rather than eternal truths.

## 3.2 D1 mapping — state vocabulary vs process grammar

### Current L0 status

L0 already states:

```text
potential / manifest / stable
= three states of one Selection process
!= three independent worlds
```

and separately describes a bootstrap loop in which actualisation creates constraints that alter later actualisation.

Therefore #936 D1 does **not** require replacing L0's three-state vocabulary.

### Reverse-map

```text
three-state vocabulary: RETAIN
three-state vocabulary as exhaustive process grammar: REJECT / do not infer
bootstrap co-evolution: RETAIN
new wholesale L0 architecture: NOT REQUIRED by D1 alone
```

If a later landing adds an explicit `state vocabulary != process grammar` sentence, that is best treated as a clarification of role, not as evidence that old L0 described three parallel universes.

## 3.3 D3 mapping — subject boundary

L0's own subject boundary is already thicker than Stable ISP:

```text
展开选择 consequences may be environmentally absorbed;
主体选择 consequences must be irreversibly borne by the selector's own state space.
```

This is directionally compatible with D3:

```text
Stable ISP < subject-position
```

because P1-T06 consequence-bearing need not yet equal L0 `承担`.

### Reverse-map

```text
subjectless Selection: RETAIN
subject / unfolding distinction: RETAIN
承担 as non-outsourcing boundary: RETAIN
关切 as endogenous relevance relation: RETAIN for now
identity Stable ISP = subject: NOT OWNED BY L0; must not be imported into L0
```

## 3.4 D2 mapping — stable domain and L2

L0 describes the stable domain as historical constraint sediment. D2 adds an important process reading:

```text
Selection continues at structural grain through durable / re-enterable background organization.
```

These are not yet contradictory:

```text
stable-domain description
!=
full L2 process grammar
```

### Reverse-map

```text
stable as reusable historical structure: RETAIN
"sediment" as exhaustive explanation of L2: DO NOT INFER
L2 final universal definition in L0: OPEN / out of scope for L0
```

No C-class L0 rewrite is justified yet merely to land D2.

## 3.5 Pass-1 disposition

```text
L0 core: RETAIN
semantic rewrite required now: NO
possible later cross-reference clarification: B/A if genuinely non-semantic; otherwise C
```

### Blast radius if later changed

Very high. L0 is frozen and downstream of nearly every core owner. Avoid using the reverse-map as a reason to rewrite L0 unless a concrete downstream inconsistency cannot be solved at the lower owner.

---

# 4. Owner 2 — `Core/SRT_Core_21b_Constitutive_Theorems.md` / P1-T06

## 4.1 Current P1-T06 standing

P1-T06 defines Stable ISP through four conditions:

```text
1. iterative exposure to currently effective non-equivalent candidates;
2. perspective-bearing;
3. history-bearing / writeback;
4. continued-selectable as the same history-bearing process,
   including downstream consequence bearing.
```

ST-A further says stability is recurrent historical reconstitution rather than microstate identity.

These remain strongly compatible with #936's structural standing.

## 4.2 Core definition

### Reverse-map

```text
Stable ISP as persistent structural standing: RETAIN
iterative condition: RETAIN
structural perspective: RETAIN, with non-phenomenal guard
history-bearing / writeback: RETAIN
continued selectability: RETAIN
microstate identity not required: RETAIN
generative reselectability != P1 minimum: RETAIN
```

No author adjudication in #936 requires collapsing Stable ISP into One or subject-position.

## 4.3 P1 consequence-bearing

Condition 4 says the same process continues while bearing downstream consequences of what it selected.

The current best typed ladder is:

```text
history-to-reconstitution bearing
<
own-consequence return / self-consequence closure
~ closest current neighbor: P1-T06 downstream consequence bearing
<
L0 承担 / non-outsourcable own consequence
```

The `~` above is not identity.

### Reverse-map

```text
P1 consequence-bearing: RETAIN
exact identity with self-consequence closure: OPEN
identity with L0 承担: REJECT AS CURRENTLY DEFINED
subjecthood from condition 4 alone: NOT ESTABLISHED
```

A future P1 rewrite should clarify the type without inflating it into subject-level stake.

## 4.4 Dynamic-layer paragraph is no longer valid as written

P1-T06 currently says:

```text
P1-T06 four conditions = result-state criterion for stable ISP;
T-IND-2 = entry-dynamics criterion for when a process crosses into that state.
```

But T-IND-2 currently defines subject-position entry and explicitly adds burdens not present in P1-T06.

Author D3 now fixes only:

```text
Stable ISP < subject-position
```

Therefore the old identity cannot survive.

### Reverse-map

```text
P1 result-state owner: RETAIN
T-IND-2 as entry dynamics into the same standing: RETIRE
new relation to Individuation: REWRITE
```

The future wording should state at minimum:

```text
P1-T06 owns Stable ISP standing.
Individuation may model transitions downstream of or through this standing,
but subject-position entry is not identical to Stable ISP entry.
```

Exact entry dynamics of Stable ISP remain OPEN unless separately owned.

## 4.5 Relation to D4a One

P1-T06 already presupposes a recognizable continuing process. D4a now author-adopts `One` as a real processual formed unity.

However, the following is not yet author-adjudicated as an identity theorem:

```text
P1-T06 continuity role = full D4a One definition
```

### Reverse-map

```text
formed-continuity role inside P1-T06: RETAIN
explicit One dependency: ADD / MERGE-ALIAS candidate
exact identity: OPEN pending landing design
Stable ISP = One: REJECT
One -> Stable ISP sufficiency: REJECT / not established
```

A later landing should avoid making One disappear into P1-T06. D4a gives One its own ontological work: formed unity before the thicker Stable-ISP standing.

## 4.6 Pass-1 disposition

```text
P1-T06 core criteria: RETAIN
consequence-bearing type: REWRITE / clarify
P1-T06 = T-IND-2 same-standing relation: RETIRE
One crosslink: ADD candidate, exact dependency OPEN
future edit risk: C
```

---

# 5. Owner 3 — `Core_Law/SRT_Individuation.md`

## 5.1 Why this is the highest-pressure owner

The current Individuation file does three things at once:

```text
A. gives a transition theory from subjectless Selection;
B. uses sigma_sr as a phase/order-parameter tracker;
C. identifies the first transition simultaneously as Stable-ISP entry and subject-position entry.
```

D3 directly reopens C.

This is therefore not a minor wording mismatch.

## 5.2 Role of the file

The broad role remains valuable:

```text
how thicker organized positions emerge from subjectless Selection
```

### Reverse-map

```text
Individuation as transition-theory owner: RETAIN
Individuation as proof of subject existence: RETAIN prohibition
self-consciousness downstream of subject-position: RETAIN as candidate architecture
```

But the exact phase architecture must change or be reopened.

## 5.3 T-IND-1 / sigma ownership

Current T-IND-1 says a pattern crosses from unfolding Selection into subject Selection when `sigma_sr` crosses a structural threshold.

The same file's later truth-up already limits sigma to:

```text
model-local historical/writeback-balance proxy;
representation-dependent coordinate;
not proof of unique attribution;
not proof of causal-control share;
not proof of a natural phase boundary.
```

D3 now adds another problem: subject-position is no longer identical to Stable ISP.

Therefore `sigma_sub` cannot keep silently owning both transitions.

### Reverse-map

```text
sigma_sr as model-local tracking coordinate: RETAIN
sigma_sr as unique/natural individuation variable: REJECT / already guarded
sigma_sub = Stable-ISP entry: OPEN
sigma_sub = subject-position entry: OPEN
one threshold serving both by identity: RETIRE
three-phase ownership as currently named: REWRITE / OPEN
```

This is a required reverse-map target before any canonical rewrite.

## 5.4 T-IND-2 four conditions

Current T-IND-2 requires:

```text
1. self-reference closure no longer dissolves;
2. 承担 internalization;
3. concern stabilization;
4. local epsilon-direction readability.
```

and explicitly gives dissociation cases:

```text
closure without 承担 = pathological self-reference;
承担 without concern = pure execution;
承担 + concern without readability = blind struggle.
```

#936 did **not** authorize deleting these burdens.

D3 instead author-adopted a live split and kept subject sufficiency OPEN.

### Reverse-map

```text
S1 non-outsourcable consequence / 承担: RETAIN as subject candidate burden
S2 stabilized endogenous relevance / 关切: RETAIN as subject candidate burden
S3 regulative readability: RETAIN as separate subject candidate burden
umbrella stake relation: RETAIN as organizing language only
S1 / S2 / S3 mutual entailment: REJECT / not established
S1+S2+S3 sufficiency theorem: OPEN
```

The first current T-IND-2 condition, self-reference closure, needs retyping rather than deletion.

If Stable ISP is already upstream of subject-position, some persistence / history closure is already paid by P1-T06. Therefore:

```text
self-reference closure as subject-specific extra burden: OPEN
self-reference closure as inherited Stable-ISP prerequisite: leading candidate
```

Do not decide this identity in the rewrite without a dedicated check.

## 5.5 The sentence that must not survive

Current text says:

```text
"这就是主体位进入（ISP entry）"
=
P1-T06 four conditions simultaneously satisfied.
```

Under author D3 this is no longer admissible.

### Reverse-map

```text
Stable-ISP entry = subject-position entry: RETIRE
P1-T06 = subject standing: RETIRE
subject-position downstream of Stable ISP: ACCEPTED LIVE SPLIT
exact subject sufficiency: OPEN
```

## 5.6 d-value dependency

Current T-IND-2 uses `d > 0` language inside subject entry.

But canonical `d` itself is defined with:

```text
subject utility gradient;
subject closure;
consequence return to subject identity / later choice capacity.
```

Using current `d` to prove the subject would therefore be circular.

### Reverse-map

```text
d-value as subject-admission proof: RETIRE
stake / concern burdens may be assessed structurally before d readout: RETAIN candidate
canonical d readout after subject admission: RETAIN
```

## 5.7 Pass-1 disposition

```text
file role: RETAIN
T-IND-1 subject-threshold ownership: REWRITE / OPEN
a single sigma_sub owning ISP + subject transition: RETIRE
T-IND-2 burden set: RETAIN but retype
"ISP entry = subject entry": RETIRE
self-consciousness as later condensate: RETAIN candidate
future edit risk: C
```

This owner should not be patched piecemeal before P1-T06 and the One / Stable-ISP / subject boundary are jointly mapped.

---

# 6. Owner 4 — `Core/SRT_Core_12b_Ontology_L2.md`

## 6.1 Current file contains several different L2 jobs

The current owner uses L2 for at least:

```text
historical accumulation / hysteresis;
path-trace closure;
background scaffold formation;
low-friction compatible path structure;
inheritability / shareability / re-entry;
continuous structural-grain Selection;
agential / authorized position allocation;
rights / legitimacy in social-institutional realizations.
```

D2 does not authorize deleting these mechanisms. It does require asking which are universal L2-core conditions and which are realization-specific.

## 6.2 Strongest surviving core — structural-grain Selection

`Def-L2-DualLayer` already states:

```text
L1 Selection = event grain;
L2 Selection = structural grain;
L2 does not mean Selection stops;
Selection's temporal form changes.
```

This is the closest current canonical owner to D2.

### Reverse-map

```text
Selection continues at structural grain: RETAIN / leading L2 core
L2 as dead/passive residue only: REJECT
historical sedimentation as one formation mechanism: RETAIN
```

## 6.3 Historical trace / closure / scaffold ladder

The file already distinguishes:

```text
trace
-> minimal closure
-> L2-grade closure
-> scaffold threshold
```

That distinction is valuable and should survive.

However, current L2-grade closure requires:

```text
inheritable + shareable + re-enterable + backgrounded
```

D2 explicitly leaves universal shareability OPEN.

### Reverse-map

```text
trace != closure != scaffold: RETAIN
re-enterability / durable backgrounding: RETAIN as leading core burden
inheritability: RETAIN candidate, exact universality OPEN
shareability as universal L2 gate: OPEN / do not assume
```

The future owner may need to distinguish:

```text
internal / single-unit structuralized L2-like regime
shared / institutional L2 regime
```

without declaring today that both use an identical gate set.

## 6.4 Low-Psi

Current path-layer language uses `P_low-Psi` and a threshold `Psi_c`.

D2 did not adjudicate low friction as the representation-invariant essence of L2.

### Reverse-map

```text
low-Psi as operational signature / one realization metric: RETAIN
low-Psi threshold as universal constitutive definition: DEMOTE / OPEN
```

## 6.5 Agency layer

Current `Def-L2-DualLayer` makes authorized agency-position allocation a universal second component of L2.

This is well-motivated for institutional / social L2, but #936 explicitly left its universal status OPEN.

### Reverse-map

```text
agency-position allocation in social/institutional L2: RETAIN
agency layer as universal component of every L2 regime: DEMOTE / OPEN
rights / legitimacy deductions: RETAIN within scoped social owner if prerequisites survive
```

This is a likely owner-boundary split, not necessarily a deletion of the social theory.

## 6.6 T-L2-Scaffold scope

The theorem is currently scoped to stable ISPs and emphasizes multi-agent superposition.

If D2 eventually allows scale-relative internal structuralization before subjecthood or before multi-agent sharing, T-L2-Scaffold cannot be the universal origin theorem of all L2.

### Reverse-map

```text
T-L2-Scaffold as one stable-ISP / multi-agent scaffold pathway: RETAIN
T-L2-Scaffold as universal origin of all L2: DEMOTE / not established
multi-agent superposition as universal L2 requirement: REJECT / not established
```

## 6.7 File title and ontology label

`The Vergence Domain`, `Consensus`, and the current symbol-table shorthand may become too narrow if D2 is later canonicalized.

### Reverse-map

```text
L2 = convergence domain only: REWRITE candidate
L2 = structural-grain Selection regime: leading reconstruction direction
final canonical label: OPEN
```

## 6.8 Pass-1 disposition

```text
structural-grain core: RETAIN
historical formation mechanisms: RETAIN but do not equate with total definition
shareability universal gate: OPEN
agency-layer universal gate: DEMOTE / OPEN
low-Psi universal gate: DEMOTE / OPEN
social/institutional specializations: RETAIN with narrower scope
future edit risk: C
```

A future rewrite should probably separate **L2 core** from **social/institutional L2 realization** before rewriting formulas or rights/legitimacy sections.

---

# 7. Owner 5 — `_SRT_D_VALUE_CANONICAL.md`

## 7.1 What can survive

The current owner distinguishes:

```text
canonical stake-coupled d
vs
capacity proxies such as D_eff / Fisher rank.
```

It also insists that distinguishability or competence does not equal concern.

Those are useful boundaries and do not conflict with #936.

### Reverse-map

```text
capacity != stake-coupled concern: RETAIN
D_eff as proxy rather than d definition: RETAIN
R / A / C factorization as within-stake diagnostic structure: RETAIN with scope guard
```

## 7.2 The circularity problem

Current `Def-d-canonical` and gate language use:

```text
subject utility gradient;
subject stake;
consequence return to subject closure / identity continuity.
```

Therefore canonical d already presupposes a subject-bearing unit.

It cannot then be cited upstream as the criterion that creates or proves that same subject.

### Reverse-map

```text
d as downstream subject-level readout: RETAIN
d as subject-admission criterion: RETIRE
d > 0 as proof of subject-position: RETIRE
```

Dependency direction for the reconstruction should be:

```text
independently admitted continuing unit / Stable ISP
-> separately paid subject-position burdens
-> canonical d becomes applicable as a stake-coupled readout
```

not:

```text
d gate
-> subjecthood
```

## 7.3 Should `subject` be replaced by `declared unit` inside d?

Not yet.

Replacing all subject language with unit-general language would broaden d to pre-subject systems and materially change its ontology. #936 did not authorize that move.

### Reverse-map

```text
subject-conditioned d definition: RETAIN for now
unit-general d definition: OPEN / not authorized
explicit applicability precondition: ADD / REWRITE candidate
```

## 7.4 R / A / C gate

The gate can continue to diagnose whether a direction is truly coupled to a stake **after** the relevant subject-bearing unit is independently admitted.

But it cannot be used as a non-circular subject generator because A and C currently reference subject utility and subject closure.

### Reverse-map

```text
R/A/C as downstream stake qualification: RETAIN
R/A/C as subject-formation theorem: REJECT
numerical gate sufficiency: already P3/P4 / retain guard
```

## 7.5 AI and collective implications

A future D3 landing will create a meaningful category:

```text
Stable ISP candidate
but not yet subject-position
```

Therefore downstream AI / collective files must not infer:

```text
stable structural continuity
-> d is automatically defined / positive
```

or:

```text
d approximately zero
-> no Stable ISP exists
```

Those are different questions after D3.

## 7.6 Pass-1 disposition

```text
core capacity/stake distinction: RETAIN
canonical d as downstream stake readout: RETAIN
subject-admission use: RETIRE
applicability / dependency guard: REWRITE / ADD
unit-general replacement: OPEN
future edit risk: C
```

---

# 8. New owner / owner-boundary implications

## 8.1 `One` needs an explicit landing decision

D4a is author-adjudicated:

```text
One
= localized, lineage-relative, processual formed unity
  recurrently reconstituted through Selection-mediated history.
```

No current frozen canonical owner cleanly owns this term at that exact standing.

### Reverse-map

```text
One canonical owner: ADD candidate
One = Stable ISP: REJECT
One = subject-position: REJECT
One = Active Selection: REJECT
D4b future-selectability minimum: OPEN
D4c passive/active relation: OPEN
```

The canonical reverse-map therefore identifies a genuine owner gap.

However, the later landing should be deliberately thin. It should not import:

```text
Bearer;
subject stake;
Active Selection;
creative reconstruction;
collective standing;
phenomenality;
```

into One merely to make the new owner look complete.

## 8.2 Stable ISP owner remains P1-T06

Do not create a second Stable-ISP definition in the new One owner.

Preferred owner hierarchy candidate:

```text
One owner
= formed unity / continuity

P1-T06
= Stable ISP standing built on a continuing process

Individuation
= transition / subject-position dynamics after the split is retyped
```

Exact formal dependency between One and P1-T06 remains to be landed, not assumed.

## 8.3 Subject-position owner remains unresolved

D3 authorizes the split, not the final sufficient definition.

Therefore:

```text
subject-position new canonical theorem: NOT READY
subject-position burden ledger S1/S2/S3: READY FOR HARDENING
```

Do not create a canonical subject theorem merely to fill the gap exposed by retiring `ISP entry = subject entry`.

---

# 9. Cross-owner contradiction ledger

## C1 — Stable ISP / subject identity

```text
current P1-T06 dynamic note + T-IND-2:
Stable ISP entry = subject-position / ISP entry

PR936 adjudication:
Stable ISP < subject-position
```

**Disposition:** current identity must be retired in future landing.

## C2 — sigma phase ownership

```text
current Individuation:
sigma_sub tracks subject / ISP entry as one transition

PR936:
Stable ISP and subject-position are split;
final sigma phase ownership explicitly OPEN
```

**Disposition:** sigma remains model-local; phase ownership must be reassigned or left open.

## C3 — d-value circularity

```text
current d:
uses subject utility / subject closure

current Individuation:
uses d > 0 inside subject entry
```

**Disposition:** dependency must be reversed; d cannot prove its own subject precondition.

## C4 — L2 universality

```text
current Core_12b:
path layer + agency layer;
L2-grade closure includes shareability;
low-Psi threshold language;

PR936 D2:
structural-grain Selection direction accepted;
shareability / agency layer / low-Psi universality OPEN
```

**Disposition:** retain mechanisms but de-universalize unresolved gates.

## C5 — One owner gap

```text
PR936 D4a:
One = author-adjudicated real processual formed unity

current canonical:
no exact owner for that standing
```

**Disposition:** ADD candidate; do not silently alias to Stable ISP.

---

# 10. Candidate post-map architecture — NOT YET CANONICAL

The minimum architecture that best fits the current reverse-map is:

```text
subjectless Selection
        ↓
actualisation / manifestation
        ↓
writeback / anchoring / historical constraint
        ↓
One
[formed processual unity]
        ↓
Stable ISP
[structural perspective + history + continued selectability]
        ↓
subject-position
[thicker downstream standing;
 S1/S2/S3 burdens separately payable]
        ↓
self-consciousness / phenomenality relations
[partly OPEN]
```

Alongside, not as a simple ladder:

```text
historical structuralization
        ↓
L2
[Selection continuing at structural grain;
 final universal gates OPEN]
```

and:

```text
subject-position established independently
        ↓
d-value applicability
[stake-coupled downstream readout]
```

This architecture is a reverse-map aid only. It is not a new canonical theorem set.

---

# 11. Proposed canonical landing sequence after this audit

Do not land all five owners in one PR.

## Landing package A — One / Stable ISP / subject boundary

Target:

```text
ADD thin One owner;
retain P1-T06 as Stable-ISP owner;
retire P1-T06 <-> T-IND-2 same-standing identity;
retype P1 consequence-bearing vs L0 承担;
leave subject sufficiency OPEN.
```

Likely risk: **C**.

Reason to do first: later sigma, d and L2 routing depend on knowing what standing is being tracked.

## Landing package B — Individuation / sigma rebase

Target:

```text
remove sigma_sub as automatic joint ISP+subject threshold;
retain sigma_sr only as model-local tracker;
rebuild phase labels around the accepted Stable-ISP/subject split;
preserve S1/S2/S3 as separate burdens;
preserve self-consciousness as downstream candidate without overclaim.
```

Likely risk: **C**.

## Landing package C — L2 core / realization split

Target:

```text
make structural-grain Selection the core organizing read;
retain trace/closure/scaffold mechanisms;
stop treating shareability, low-Psi and agency allocation as automatically universal;
route social/institutional agency structure as scoped realization unless separately re-earned.
```

Likely risk: **C**.

## Landing package D — d-value applicability guard

Target:

```text
retain canonical stake readout;
forbid subject-forming circular use;
clarify that Stable ISP does not automatically imply d applicability;
then audit AI / collective downstream uses.
```

Likely risk: **C**.

---

# 12. What this pass does NOT decide

```text
One exact D4b future-selectability minimum: OPEN
One / passive / active Selection relation: OPEN
One exact formal dependency on P1-T06: OPEN
subject-position sufficiency theorem: OPEN
whether S1/S2/S3 are jointly sufficient: OPEN
whether self-reference closure is inherited or extra at subject transition: OPEN
sigma_sub final owner: OPEN
sigma_self final status: OPEN
phenomenality / experiencer necessity: OPEN
shareability as universal L2 gate: OPEN
agency layer as universal L2 component: OPEN
low-Psi as universal L2 definition: OPEN
unit-general d-value: OPEN
scientific distinctiveness: NOT ESTABLISHED
whole-architecture non-substitutability: NOT ESTABLISHED
Level 2: HOLD
```

---

# 13. Pass-1 verdict

```text
CANONICAL REVERSE-MAP PASS 1

L0:
RETAIN CORE
NO WHOLESALE REWRITE WARRANTED

P1-T06:
RETAIN STABLE-ISP CORE
REWRITE / RETIRE SAME-STANDING LINK TO T-IND-2
TYPE-CLARIFY CONSEQUENCE BEARING

Individuation:
MAJOR REWRITE REQUIRED
RETIRE ISP-ENTRY = SUBJECT-ENTRY IDENTITY
SIGMA PHASE OWNERSHIP OPEN

L2:
REWRITE / SCOPE-SPLIT
RETAIN STRUCTURAL-GRAIN SELECTION CORE
DE-UNIVERSALIZE UNPAID GATES

D-VALUE:
RETAIN DOWNSTREAM STAKE READOUT
RETIRE SUBJECT-ADMISSION USE
ADD APPLICABILITY GUARD

ONE:
NEW OWNER GAP IDENTIFIED
ADD CANDIDATE
D4b / D4c REMAIN OPEN

canonical edits in this pass = 0
research mode = U
new Level = 0
Level 2 = HOLD
```

The next valid step is external/internal review of this reverse-map itself. Only after the map survives owner-consistency review should any C-class landing PR be opened.