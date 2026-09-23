---
id: SRT-TERMINOLOGY-DUPLICATION-CENSUS-20260924
type: audit
tags: [Terminology, Vocabulary, Duplication, Alias, SemanticRouting, GRG, SRT]
status: draft
date: 2026-09-24
layer: operations
epistemic_layer: operations
claim_mode: audit
canonical: false
dependency:
  - SRT-TERM-ROUTER
  - SRT-GLOSSARY
  - SRT-SYMBOL-TABLE
  - SRT-AGENT-RETRIEVAL-PROFILE
  - SRT-GENERATIVE-ONTOLOGY-SPINE
  - SRT-GRG-FOUNDATIONAL-PROTO-GRAMMAR-V0-3-20260921
---

# SRT / GRG terminology duplication census — 2026-09-24

## 0. Scope

This is the first bounded terminology census after the post-#1042 governance repair.

Question:

> Is the repository repeatedly creating new words for already-owned explanatory burdens, and what semantic-routing infrastructure is needed before any bulk terminology cleanup?

Verdict:

~~~text
existing glossary = YES
existing symbol registry = YES
live semantic term router = NO before this PR
duplicate / overloaded terminology risk = REAL
bulk rename now = NOT ADVISED
dynamic router + bounded normalization = ADVISED
~~~

This audit is noncanonical and does not redefine any SRT / GRG term.

It does not:

- edit canonical theory owners;
- rewrite historical dialogue / source-intuition records;
- change GRG v0.3;
- create a new canonical glossary;
- make working labels permanent;
- perform the accepted-analysis re-entry audit;
- thin the Generative Ontology Spine.

Those later tasks remain separately reviewable.

---

## 1. Existing terminology infrastructure

### 1.1 SRT_Glossary.md

Observed current main:

~~~text
lines ≈ 2224
role = mixed historical glossary / retrieval source
canonical authority = subordinate to current canonical anchors
connector-safe route = Glossary/README.md + shards
~~~

Strength:

- rich historical coverage;
- many aliases / concepts already present;
- useful retrieval source.

Limitation for current research:

- contains historical and superseded formulations;
- is not optimized for “should I invent a new term now?”;
- does not provide a compact active owner / alias / collision decision surface.

### 1.2 _SRT_SYMBOL_TABLE.md

Observed current main:

~~~text
lines ≈ 206
role = canonical symbol registry
~~~

Strength:

- exact glyph / notation governance;
- namespace and symbol-scope protection.

Limitation:

- intentionally does not solve ordinary concept-term duplication;
- many important GRG / source-intuition terms have no symbols and should not gain symbols merely to be governed.

### 1.3 Phase-3 vocabulary map

The Phase-3 provenance / vocabulary audit already identified several collisions and distinctions around 2026-09-22 GRG material.

Strength:

- proves vocabulary conflict is already a recognized repository problem.

Limitation:

- bounded to one reconstruction phase;
- not a standing live term-admission surface.

### 1.4 Gap

The missing layer was therefore not “a glossary” in general.

The missing layer was:

> a small, revisable, non-authoritative semantic router that answers owner / alias / overlap / collision questions before a working label hardens into repo-wide terminology.

This PR adds that layer as:

_SRT_TERM_ROUTER.md

---

## 2. Census method

This pass inspected current-main routing and owner surfaces, especially:

- Core_Law/SRT_Generative_Ontology_Spine.md
- Core_Law/SRT_One_Formation.md
- _SRT_SYMBOL_TABLE.md
- SRT_Glossary.md
- STATUS.md vocabulary guards
- Operations/Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md
- 2026-09-22 capacity / intervention grammar record
- 2026-09-22 reach / reconstructibility / generative debt record
- post-#1041 / #1042 corrective records.

Classification:

~~~text
ALIAS_SAME_BURDEN
OVERLOADED_SAME_NAME
PARTIAL_OVERLAP
DISTINCT_BURDEN
WORKING_LABEL_ONLY
~~~

This is a semantic triage, not an exhaustive word-frequency count.

A full historical corpus census can be run later if the initial router survives review.

---

## 3. High-priority duplication / collision findings

### T1 — Selection occurrence / actualisation / retained consequence / history

Current owner discipline already requires:

~~~text
Selection occurrence
!= retained historical efficacy
!= sedimentation
!= inheritance
~~~

Risk:

- “actualisation” can mean actual Selection occurrence in one discussion and actualisation of a capacity in another;
- historical records sometimes use consequence / sediment language close to occurrence.

Disposition:

PARTIAL_OVERLAP / MUST QUALIFY.

Recommendation:

- “Selection occurrence” for the event burden;
- “actualisation of capacity” only when a prior capacity distinction is explicitly in scope;
- “retained historical efficacy / history” for later-effect burden.

No bulk historical rewrite.

### T2 — One / Selection-position / perspective / Stable ISP / Bearer

Current canonical owners already contain strong non-identity guards.

Risk:

- conversational terms such as position, perspective, stable position, bearer-position can make the ladder look like synonyms.

Disposition:

DISTINCT_BURDENS.

Recommendation:

Router must make this one of the first high-risk families.

No normalization by collapsing terms.

### T3 — proxy

Observed object families include:

- GRG generative proxy;
- measurement proxy;
- operational proxy;
- domain proxy;
- representation-like uses.

Current STATUS already says:

~~~text
generative / GRG proxy
!= measurement / operational proxy
~~~

Disposition:

OVERLOADED_SAME_NAME.

Recommendation:

Require qualification when “proxy” carries an inferential burden.

Do not invent a single universal Proxy definition.

### T4 — reconstructibility / reconstruction / recoverability

Observed meanings include:

- GRG generative reconstructibility;
- source-native reconstruction;
- structural reconstruction;
- repository reconstruction;
- dialogue / semantic recoverability.

#1042 already corrected one important misuse: repository prompt failure should not be described as evidence for GRG reconstructibility.

Disposition:

OVERLOADED_SAME_NAME + NEAR-ALIAS RISK.

Recommendation:

- reserve “generative reconstructibility” for the GRG research burden;
- use “reconstruction” only with an object qualifier;
- use “repository / dialogue recoverability” for workflow recovery;
- avoid “semantic reconstructibility” for repository/session continuity.

### T5 — reach / reachability / accessibility

Observed families:

- active generative reach;
- latent reconstructive reach;
- source/model reachability;
- accessibility of capacity.

Risk:

A domain’s reachable set can be mislabeled “reach” and silently imported into GRG.

Disposition:

PARTIAL_OVERLAP.

Recommendation:

Always qualify:
- active generative reach;
- latent reconstructive reach;
- model/source reachability;
- capacity accessibility.

### T6 — capacity / availability / accessibility / actualisation

The 09-22 capacity record explicitly introduced this split.

Risk:

Later machine analyses may recompress the four burdens into “capacity” or invent new labels for a subset.

Disposition:

DISTINCT_BURDENS / RETAIN CURRENT SPLIT.

Recommendation:

Before naming any new capacity-like term, compare it against all four.

### T7 — object / relation / cut / objectification / re-objectification / recut

Current GRG direction treats object and relation as cuts.

Risk:

- “cut”, “objectification”, “compression”, “coarse-graining” and “proxy” can be used as if interchangeable;
- “recut”, “re-objectification” and “reconstruction” can also drift together.

Disposition:

PARTIAL_OVERLAP FAMILY.

Recommendation:

Do not force one synonym.

Route by burden:
- cut = bounded distinction / partition;
- objectification = stabilization / organization of a cut;
- re-objectification / recut = reopening and forming a different cut;
- reconstruction = qualified analytic process, not automatically a new cut.

These are router descriptions only; exact authority remains with owners.

### T8 — equivalence / neutrality / supported equivalence / subsidized equivalence

Observed progression:

- bounded generative equivalence;
- neutrality / treating differences as equivalent for a burden;
- supported / subsidized equivalence.

Risk:

New “neutrality” terms can simply redescribe support-dependent equivalence.

Disposition:

PARTIAL_OVERLAP / OWNER CHECK REQUIRED.

Recommendation:

Future new terms in this family must say what burden is not already paid by generative equivalence + support.

### T9 — friction / cost / support / compensation / debt / Psi_f

Current records already warn that friction cannot be a universal explanation word.

Risk:

- GRG boundary / constitutive friction can be conflated with canonical Psi_f;
- generative debt can be conflated with repository debt or generic cost;
- compensation/support can become new names for the same dependency.

Disposition:

OVERLOADED FAMILY.

Recommendation:

Namespace before use; do not infer identity from ordinary-language similarity.

### T10 — expectation / prediction / Generative Expectation / normativity

Current GRG v0.3 has typed outputs P_G and E_G.

Current STATUS already says:

~~~text
structural / operative generative expectation
!= E_G automatically
~~~

Risk:

Conversational “expected continuation”, “generative expectation” and “normativity” can be treated as one object.

Disposition:

DISTINGUISH.

Recommendation:

Use E_G only when its v0.3 admission burden is intended.

Keep normativity as a further routing question, not a lexical synonym.

### T11 — wholeward / higher-order / integration / hierarchy / composition

Current v0.3 says wholeward integration requires additional real dependency inclusion and cannot gain authority by scale alone.

Risk:

A new term for “higher-order” can repeatedly redescribe hierarchy / composition without added burden.

Disposition:

OWNER CHECK REQUIRED.

Recommendation:

Any new higher-order term must state why wholeward / composition / reorganization do not already carry it.

### T12 — GTS / relation record / operator / grammar candidate

Current v0.3 makes GTS the primary bounded record unit, not an ontic entity.

Risk:

A machine sees a recurrent source process and names:
- a new operator;
- a new relation;
- a new grammar object;
when the result is only a GTS description or an inherited burden.

Disposition:

ADMISSION-GATED.

Recommendation:

Owner/neighbor absorption before new naming:
INHERIT / REALIZATION / REORGANIZATION / NO_GRG_GAIN / RESIDUAL_CANDIDATE.

Only a residual candidate can justify a new grammar term.

---

## 4. Recent examples where vocabulary governance already prevented duplication

The post-#1041 corrective work supplied useful examples:

### 4.1 dual reconstruction

Problem:

Name collision / conceptual proximity with existing dual reconstructibility.

Current route:

~~~text
source-cut + GRG-cut reconstruction
~~~

Disposition:

WORKING_LABEL_ONLY / RETIRE AS TERM-OF-ART.

### 4.2 continuity_role

Problem:

Duplicated existing retrieval-value function as a fourth axis.

Current route:

~~~text
authority
retrieval value
currentness
~~~

Disposition:

RETIRED AS NEW AXIS.

### 4.3 CALIBRATION as generic disposition

Problem:

Already has programme-level meaning in framework-vs-calibration.

Disposition:

DO NOT REUSE AS GENERIC RESULT CLASS.

### 4.4 L1 / L2 / L3 / L4 writeback layers

Problem:

Namespace collision with canonical SRT L0/L1/L2.

Disposition:

RETIRED; use plain descriptive surface names.

These examples support the need for term-admission routing before new wording is hardened.

---

## 5. Normalization strategy

Do not run global search-and-replace.

Use three passes.

### Pass A — router / census

Current PR.

Actions:

- add dynamic term router;
- record high-risk families;
- add new-term admission rule;
- make no canonical theory changes.

### Pass B — active-owner normalization

Only after independent review.

Scope:

- current active owners / handoffs / templates;
- obvious same-burden duplicate labels;
- ambiguous unqualified terms with real retrieval risk.

Allowed actions:

- add alias notes;
- qualify overloaded terms;
- replace a retired working label where meaning is unchanged;
- point to existing owner.

Do not rewrite historical provenance merely for lexical uniformity.

### Pass C — historical compatibility annotations

Only where search/retrieval would otherwise fail.

Prefer:

~~~text
historical label X
-> current route Y
~~~

over deleting historical language.

---

## 6. New-term admission rule

Conversation exploration remains free.

A model may coin a temporary phrase while reasoning.

The gate applies only when a label is about to become repeated repository vocabulary.

Before hardening:

~~~text
1. search _SRT_TERM_ROUTER.md
2. search current owner(s)
3. identify nearest burden
4. classify alias / overload / overlap / distinct / working-only
5. if distinct, state the non-duplicate burden and owner
6. if not distinct, inherit or qualify existing vocabulary
~~~

This should reduce vocabulary churn without freezing the theory.

---

## 7. Relationship to the next two consolidation tasks

This audit intentionally precedes:

### Accepted-analysis re-entry audit

Reason:

A recovered historical branch may use an older label for a currently owned burden.

The term router gives that later audit a way to say:

~~~text
old wording
-> current owner / alias / partial overlap
~~~

without either deleting the old analysis or inventing another new term.

### Generative Ontology Spine thinning

Reason:

Spine thinning should happen only after terminology and historical continuity are mapped.

Otherwise a section might be removed as “duplicate explanation” when it is actually the only active route to a still-discrete burden.

---

## 8. Review questions

Independent review should test:

1. Does the router accidentally become a definition authority?
2. Are any listed “preferred labels” stronger than their owners support?
3. Are any genuinely distinct burdens incorrectly grouped as aliases?
4. Are any same-burden duplicates still missing from the high-risk clusters?
5. Does the new-term gate inhibit exploratory dialogue rather than only repository hardening?
6. Should any cluster be routed to a different current owner?
7. Does any proposed normalization silently alter canonical meaning?

---

## 9. Current verdict

~~~text
dynamic term router:
  NEEDED

fixed final glossary:
  NOT RECOMMENDED

bulk renaming:
  NOT NOW

active-owner bounded normalization:
  AFTER REVIEW

historical provenance rewrite:
  NO

new term invention in dialogue:
  ALLOWED AS WORKING LABEL

new repo-wide term hardening:
  OWNER + TERM ROUTER CHECK REQUIRED

accepted-analysis re-entry audit:
  NEXT SEPARATE PR

Spine semantic thinning:
  AFTER RE-ENTRY AUDIT
~~~
