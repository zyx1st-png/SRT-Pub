---
id: SRT-TERM-ROUTER
type: retrieval_index
tags: [Terminology, Vocabulary, Router, Alias, Semantics, GRG, SRT]
status: draft
layer: meta
epistemic_layer: meta
claim_mode: navigation
canonical: false
dependency:
  - SRT-AGENT-RETRIEVAL-PROFILE
  - SRT-SYMBOL-TABLE
  - SRT-GLOSSARY
  - CANONICAL-REGISTRY
  - SRT-CONTEXT-ROUTER
---

# SRT / GRG Term Router

> Purpose: dynamic semantic routing for SRT / GRG terminology.
> This file helps answer: does a proposed term already exist under another name, overlap an existing burden, or need a genuinely new label?
>
> Non-authority guard: this router does not define SRT or GRG. Definitions, admission criteria and claim strength remain with the current canonical / research owner named in the row.
>
> Why this exists: SRT_Glossary.md is a large historical retrieval source and _SRT_SYMBOL_TABLE.md is the symbol authority. Neither is designed to prevent a live research conversation from repeatedly inventing a new label for an already-owned semantic burden.

## 0. How to use this router

Before hardening a new repo-wide SRT / GRG term-of-art:

1. search this router;
2. search the relevant current owner(s);
3. classify the proposed wording:

~~~text
ALIAS_SAME_BURDEN
OVERLOADED_SAME_NAME
PARTIAL_OVERLAP
DISTINCT_BURDEN
WORKING_LABEL_ONLY
~~~

4. prefer an existing term for ALIAS_SAME_BURDEN;
5. namespace / qualify OVERLOADED_SAME_NAME;
6. preserve both terms with an explicit boundary for PARTIAL_OVERLAP;
7. only harden a new term when DISTINCT_BURDEN survives owner comparison;
8. conversation-only exploratory wording may remain WORKING_LABEL_ONLY without repository-wide admission.

A new retained term should record:

~~~text
term:
owner:
scope:
nearest existing term(s):
why not an alias:
confusable with:
status / claim strength:
merge-or-retire condition:
~~~

Do not bulk-rename repository history from this router. Historical wording remains provenance unless a bounded cleanup is separately authorized.

---

## 1. Canonical / cross-owner structural families

| Preferred routing label | Near / historical / confusable labels | Relation | Current owner / route | Router action |
|---|---|---|---|---|
| Selection occurrence | actualised Selection, event-level Selection, descriptive/modelled change | Selection occurrence is not automatically retained history; genuine actualised Selection vs merely descriptive/modelled change remains OPEN | Core_Law/SRT_Generative_Ontology_Spine.md §§2–3; Phase-3 provenance map | DISTINGUISH |
| retained historical efficacy / history | sediment, sedimentation, retained consequence, writeback, inheritance | occurrence != history; history is the stronger burden where prior Selection remains materially effective later | Core_Law/SRT_Generative_Ontology_Spine.md §4; Core_Law/SRT_Irreversibility.md | PARTIAL_OVERLAP / OWNER-QUALIFY |
| One | formed process-unity, recurrent organization | One is a formed recurrent organization; it is not Stable ISP, Bearer, subject or consciousness | Core_Law/SRT_One_Formation.md; Spine §5 | DISTINGUISH |
| Selection-position | operative locality, position, perspective-position | time-local operative aspect of an already formed One; not a second universal endpoint and not automatically perspective/Bearer/subject-position | Core_Law/SRT_One_Formation.md; Spine §6 | DISTINGUISH |
| Stable ISP | stable position, recurrent standing, persistent ISP | stronger recurrent standing than One | Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06; Spine §7 | DISTINGUISH |
| Bearer | bearer-position, prospective self-exposure, subject carrier | separately gated from One / Selection-position / Stable ISP | Spine §8 + compatible Bearer owners | DISTINGUISH |
| perspective | positionality, Selection-position, subject-position | finite positionality != formed perspective; Selection-position != perspective-bearing subject-position automatically | Spine §6; One Formation | DISTINGUISH |
| anticipation | future-conditioning, prospective self-indexing | Selection changing later selectability != formed-position anticipation automatically; anticipation != Bearer gate automatically | Spine §6.3 | DISTINGUISH |

---

## 2. GRG research-term families

These rows are research routing, not canonical SRT definitions.

| Preferred routing label | Near / confusable labels | Relation | Current owner / route | Router action |
|---|---|---|---|---|
| object / relation as cuts | objectification, partition, coordinate, relation-first | object and relation are revisable analytical / stabilized cuts; neither object-first nor relation-first is automatically privileged | GRG v0.3 §7; 09-22 capacity record | PARTIAL_OVERLAP |
| objectification | compression, coarse-graining, working cut | broad process of stabilizing / organizing a cut; not automatically an error | 09-22 capacity §§I, AB–AC; #1040/#1041 method | RETAIN |
| re-objectification / recutting | recut, reclassification, reconstruction of cuts | reopening and forming a new cut; not a synonym for ordinary retrieval or repository refactor | 09-22 capacity §AC | ALIAS-FAMILY / QUALIFY |
| generative capacity | possibility, capability, potential | capacity must be kept separate from availability, accessibility and actualisation | 09-22 capacity §§C–D | RETAIN |
| availability | presence, accessibility | a capacity may be structurally present without being currently accessible through existing organization | 09-22 capacity §D | DISTINGUISH |
| accessibility | reachability, availability, activation | access to a capacity under current proxy/support organization; not the same as capacity or actualisation | 09-22 capacity §D | DISTINGUISH |
| actualisation of capacity | occurrence, execution, realization | capacity entering a concrete Selection; do not collapse into mere availability/accessibility | 09-22 capacity §§C–D | DISTINGUISH |
| GRG generative proxy | proxy, representation, measurement proxy, operational proxy | GRG proxy organizes distinctions / equivalence / access; measurement or operational proxy is a different object family unless explicitly mapped | 09-22 capacity §Q; STATUS vocabulary guards | OVERLOADED_SAME_NAME — namespace |
| active generative reach | reach, influence, active access | a difference currently enters wider Selection loops | 09-22 reach §M | RETAIN |
| latent reconstructive reach | latent reach, recoverability, archived possibility | compressed/screened difference can later be reconstructed and regain consequence; not repository-file retrievability | 09-22 reach §M; current STATUS next | RETAIN / DISTINGUISH |
| generative reconstructibility | reconstructibility, reconstruction, recoverability | theory-side ability to reopen sufficient generative provenance / cuts; not repository/data/dialogue recoverability | 09-22 reach §§A–K; #1042 guard | OVERLOADED_SAME_NAME — qualify |
| reconstruction | source-native reconstruction, structural reconstruction, repository reconstruction | generic process word; always qualify the object being reconstructed | GRG v0.3 §9; cross-objectification protocol | OVERLOADED_SAME_NAME — qualify |
| generative equivalence | equivalence, sameness, neutrality | bounded and intervention-relative GRG equivalence; not identity | 09-22 capacity §K | RETAIN |
| supported / subsidized equivalence | maintained equivalence, scaffolded equivalence | equivalence whose maintenance depends on support; distinguish from genuine equivalence | 09-22 reach §R | RETAIN |
| constitutive friction / boundary friction | friction, resistance, cost, Psi_f | GRG friction family must not be automatically identified with canonical Psi_f; capacity record explicitly splits friction roles | 09-22 capacity §M; STATUS guard | OVERLOADED_SAME_NAME — qualify |
| generative debt | debt, maintenance debt, reconciliation debt | GRG debt is not repository maintenance / reconciliation debt | 09-22 reach §Y + STATUS guard | OVERLOADED_SAME_NAME — qualify |
| Generative Order | order, stability, persistence, hierarchy, analyst goal | admitted GRG order has its own burden; existence/persistence/stability/hierarchy do not establish it | GRG v0.3 §14 | RETAIN |
| Generative Expectation (E_G) | expectation, prediction, structural expectation, normative expectation | E_G is a typed GRG output; structural/operative generative expectation does not automatically equal E_G | GRG v0.3 §15 + STATUS guard | DISTINGUISH |
| Generative Prediction (P_G) | prediction, expectation | distinct GRG output from E_G | GRG v0.3 | DISTINGUISH |
| wholeward integration | integration, hierarchy growth, scale increase, higher-order formation | must show additional real dependency inclusion; scale/hierarchy alone does not establish it | GRG v0.3 §16 / 09-21 author record | RETAIN |
| Generative Transformation Signature (GTS) | relation record, grammar card, candidate operator | primary bounded GRG record unit; a record schema, not an ontic object or automatically a new grammar candidate | GRG v0.3 §8 | RETAIN |
| grammar candidate | operator, relation, higher-order operator, pattern | only after owner/neighbor absorption leaves a nontrivial residual; do not name merely to summarize source process | #1042 active method/handoff | RETAIN / ADMISSION-GATED |

---

## 3. Working labels that must not silently harden

| Working / retired wording | Current routing | Reason |
|---|---|---|
| dual reconstruction | use plain source-cut + GRG-cut reconstruction / “reconstruct relevant source and GRG cuts” | too close to existing dual reconstructibility and can be mistaken for a new construct |
| continuity_role as a fourth retrieval axis | retired; use existing retrieval value + currentness + authority | #1042 found the fourth axis redundant |
| CALIBRATION as generic owner-overlap disposition | do not use generically | already has a programme-level “framework vs calibration” meaning |
| OPERATIONALIZATION as generic disposition | avoid as a classification label | ordinary methodological word; too broad to carry a unique semantic disposition |
| SOURCE_REALIZATION | use REALIZATION in the owner-overlap result vocabulary | avoid duplicate result taxonomies |
| DECOMPOSITION as a generic new-term result class | use explicit GRG-cut action or REORGANIZATION where appropriate | avoid overlapping classification systems |
| L1 / L2 / L3 / L4 for writeback layers | do not use | collides with canonical SRT L0/L1/L2 namespace |
| semantic reconstructibility for repository/session recovery | use semantic continuity / recoverability | prevents GRG reconstructibility from swallowing repository workflow language |

Current owner-overlap result vocabulary:

~~~text
INHERIT
REALIZATION
REORGANIZATION
NO_GRG_GAIN
RESIDUAL_CANDIDATE
~~~

Current GRG-cut action vocabulary:

~~~text
RETAIN
SPLIT
MERGE
DEMOTE
DELETE
SOURCE_LOCAL
INSUFFICIENT_EVIDENCE
~~~

---

## 4. Initial high-risk duplication clusters

Check these before future term invention:

1. Selection / occurrence / actualisation / event / anchoring / stabilization
2. history / sedimentation / inheritance / writeback / retention
3. One / Selection-position / perspective / Stable ISP / Bearer / subject-position
4. object / relation / cut / objectification / proxy
5. capacity / availability / accessibility / actualisation / reachability
6. reach / reachability / accessibility / latent reconstructive reach
7. reconstructibility / reconstruction / recoverability
8. equivalence / neutrality / supported equivalence / subsidized equivalence
9. friction / cost / support / compensation / debt / Psi_f
10. prediction / expectation / generative expectation / normativity
11. wholeward / higher-order / integration / hierarchy / composition
12. GTS / relation / operator / grammar candidate / transformation

---

## 5. Maintenance rule

This router is intentionally revisable.

Update it when:

- a new term is proposed for repeated / repo-wide use;
- a collision or alias is discovered;
- an owner changes;
- a term is split / merged / demoted / retired;
- an accepted-analysis re-entry audit recovers an older term family that current routing no longer exposes.

Do not update it merely because a one-off conversation uses a metaphor or exploratory phrase.

A router change alone does not authorize a canonical edit.
