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
  - SRT-GLOSSARY-LIVE-TERM-ROUTER
  - SRT-GLOSSARY
  - SRT-SYMBOL-TABLE
  - SRT-AGENT-RETRIEVAL-PROFILE
  - SRT-GOV-SUB01-SUBTRACTIVE-AUDIT
  - SRT-GENERATIVE-ONTOLOGY-SPINE
  - SRT-GRG-FOUNDATIONAL-PROTO-GRAMMAR-V0-3-20260921
---

# SRT / GRG terminology duplication census — 2026-09-24

## 0. Scope

This is the first bounded terminology census after #1042.

Question:

> Is the repository repeatedly creating new labels for already-owned or partly-owned explanatory burdens, and what routing is needed before any normalization?

Current verdict:

~~~text
historical glossary = YES
canonical symbol registry = YES
subtractive mechanism/operator governance = YES (GOV-SUB01)
bounded vocabulary/provenance audits = YES
live alias / overlap / owner routing inside the glossary entry = MISSING before #1043
duplicate / overloaded terminology risk = REAL
bulk rename now = NOT ADVISED
~~~

This audit is noncanonical. It does not redefine SRT / GRG terms and does not authorize canonical edits.

Explicit non-actions:

- no bulk rename;
- no historical-provenance rewrite;
- no canonical owner edit;
- no Spine thinning;
- no #1039 edit;
- no new GRG candidate.

## 1. Existing infrastructure and the actual gap

### 1.1 Historical glossary

`SRT_Glossary.md` is a large mixed historical / retrieval source, with connector routing through `Glossary/README.md`.

It is valuable for lineage and search, but it is not a compact answer to:

> “Is this new proposed term already carried by an active owner?”

### 1.2 Canonical symbol registry

`_SRT_SYMBOL_TABLE.md` owns symbol / notation governance.

It is intentionally not a general concept-term deduplication surface.

### 1.3 Phase-3 vocabulary / provenance audit

`Operations/Audits/SRT_REPOSITORY_SELF_RECONSTRUCTION_PHASE3_PROVENANCE_VOCABULARY_MAP_2026-09-23.md` already records important distinctions and collision guards around the 09-22 GRG records.

It is bounded audit provenance, not a standing live lexical router.

### 1.4 GOV-SUB01 already owns subtraction / “is this really new?” for mechanisms

`Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md §1` already requires subtraction before:

- new core symbols / operators / layers / thresholds / named mechanisms;
- irreducibility claims;
- residual-to-new-entity moves;
- rename-only simplification claims.

§7.4 further guards against hidden reparameterization / renamed terms.

Therefore #1043 must **not** claim that the repository lacked all novelty / duplication governance.

The actual gap is narrower:

> a small, revisable lexical-semantic router inside the existing Glossary entry that catches alias / overload / partial-overlap problems **before** a proposed term reaches GOV-SUB01 or GRG candidate admission.

That role is now:

`Glossary/README.md -> Glossary/SRT_Live_Term_Router.md`.

This satisfies the repository's navigation “one in / one out” rule: no new root-level index/router entry is created.

## 2. Relationship among the three classification systems

Do not merge these vocabularies.

| System | Question | Output role |
|---|---|---|
| Live Term Router | Is the wording an alias, overload, partial overlap, distinct burden, or working label? | lexical / semantic triage |
| GOV-SUB01 | Does a named mechanism/operator/component survive subtraction / replacement testing? | mechanism / component governance |
| current GRG owner-overlap protocol | Is a putative GRG candidate already inherited / realized / reorganized / absorbed, or is a residual candidate left? | GRG programme admission |

Flow:

~~~text
working label
-> term-router lexical check
-> if still DISTINCT_BURDEN and proposed as named mechanism/operator:
     GOV-SUB01
-> if also a GRG candidate:
     current GRG owner-overlap / absorption gate
~~~

The Term Router is not a substitute for either downstream audit.

## 3. Census method

This pass is a **bounded semantic census**, not an exhaustive corpus-frequency count.

For each high-risk family it records:

- current owner(s);
- representative repository instances;
- likely alias / overload / partial-overlap risk;
- maturity caveat.

Independent review should treat owner files as controlling and the census as routing evidence only.

## 4. High-risk terminology families

### T1 — Selection occurrence / actualisation / retained history / sedimentation / inheritance

Representative instances:

- `SRT_AI_START.md:43–49` — actualised Selection; occurrence != sediment / retained history / inheritance.
- `Core_Law/SRT_Generative_Ontology_Spine.md:124–133` — occurrence != retained historical efficacy / sedimentation; terminal Selection remains genuine.
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_GENERATIVE_CAPACITY_INTERVENTION_GRAMMAR_2026-09-22.md §A / §C–D` — same-day correction plus “actualisation of capacity”.

Risk:

“actualisation” is used for at least two nearby burdens:

~~~text
actualising Selection occurrence
vs
actualisation of an already distinguished capacity
~~~

Recommendation:

Do not globally normalize. Always qualify which burden is meant.

### T2 — One / Selection-position / perspective / Stable ISP / Bearer

Representative instances:

- `Core_Law/SRT_One_Formation.md:80–82` — One = formed process-unity through a relatively separable Selection-mediated vertical reconstitution path; stronger than generic causal recurrence.
- `Core_Law/SRT_One_Formation.md:168–184` — Selection-position = time-local operative from-where of an already formed One.
- `Core_Law/SRT_Generative_Ontology_Spine.md:260, 297, 353` — One self-conditioning, Selection-position, Bearer gate.

Risk:

Conversational terms “position / perspective / stable position / bearer-position” can appear synonym-like even though owners explicitly separate them.

Recommendation:

DO NOT COLLAPSE. Route to exact owner before introducing another “position”-family term.

### T3 — proxy

Representative instances:

- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SELECTION_GENERATIVE_VERTICAL_DYNAMICS_2026-09-22.md §E` — proxy as selective compression.
- `...GRG_GENERATIVE_CAPACITY_INTERVENTION_GRAMMAR... §Q` — proxy as operative generative partition.
- `...GRG_REACH_RECONSTRUCTIBILITY_GENERATIVE_DEBT... §Q` — proxy vs support in reach dynamics.
- `STATUS.md:144` — GRG proxy != measurement / operational proxy automatically.

Risk:

Same word spans GRG, measurement and operational contexts.

Recommendation:

QUALIFY / NAMESPACE; no universal Proxy definition.

### T4 — reconstructibility / reconstruction / recoverability

Representative instances:

- `...GRG_REACH_RECONSTRUCTIBILITY_GENERATIVE_DEBT... §§A–K` — generative reconstructibility.
- `Operations/Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md §9` — reconstruction-output view.
- `Operations/Audits/SRT_GRG_POST1041_OPUS_REVIEW_CORRECTIVE_AUDIT_2026-09-24.md §8` — repository / dialogue recovery must not be redescribed as GRG reconstructibility.

Risk:

Ordinary workflow recovery can be mistaken for evidence about a GRG research construct.

Recommendation:

Use object-qualified “reconstruction”; reserve “generative reconstructibility” for the GRG burden; use repository/dialogue recoverability for workflow.

### T5 — reach / reachability / accessibility

Representative instances:

- `SRT_AI_START.md:43` — reachable possibilities can themselves be generated through Selection.
- `Selection Vertical §F:197–217` — expectation reshapes reachability.
- `capacity §R:590+` — generative reach parent burden.
- `reach §M:468+` — active vs latent reconstructive reach.
- `capacity §D:190+` — accessibility appears in the capacity split.

Risk:

“reachability” already has author/canonical-facing use; it is not merely a domain word. “reach”, “reachability” and “accessibility” partially overlap but are not licensed as synonyms.

Recommendation:

Always route by burden and owner. Do not map model reachable-set structure directly to GRG reach.

### T6 — capacity / availability / accessibility / actualisation

Representative instances:

- `capacity §C:154+` — generative capacity.
- `capacity §D:190+` — lists capacity / availability / accessibility / actualisation.
- `capacity §D:201+` — contrasts capacity with proxy/support-blocked access.

Finding:

The owner **names** all four labels, but “availability” is not independently defined strongly enough to support a hard four-way ontology.

Recommendation:

- keep capacity / accessibility / actualisation distinctions where owner text supports them;
- mark availability as UNDER-SPECIFIED;
- do not invent a stronger definition in the Router.

### T7 — object / relation / cut / objectification / re-objectification / recut

Representative instances:

- `Selection Vertical §B:82+` — object and relation are cuts.
- `capacity §I:324+` — identity / role / capacity / dependency are also cuts.
- `capacity §AB–AC:868+` — objectification closure and re-objectification.

Risk:

“cut”, “objectification”, “compression”, “coarse-graining”, “recut”, “re-objectification” and “reconstruction” can drift into one undifferentiated family.

Recommendation:

Keep as PARTIAL OVERLAP; owner text must decide exact use.

### T8 — equivalence / neutrality / supported / subsidized equivalence

Representative instances:

- `capacity §K:400+` — bounded intervention-relative generative equivalence.
- `reach §R:608+` — genuine vs supported/subsidized equivalence.
- downstream / Card work also uses neutrality language.

Risk:

A new “neutrality” term can simply redescribe support-dependent equivalence.

Recommendation:

Before hardening a neutrality/equivalence term, state the burden not already paid by equivalence + support.

### T9 — support / compensation / friction / debt / Psi_f

Representative instances:

- `Selection Vertical §H:241+` — friction as maintenance cost + transformation pressure.
- `Selection Vertical §I:267+` — support = generativity-restructuring, not resource provision.
- `reach §Q:580+` — proxy vs support.
- `reach §W:775+` — parasitic vs integrative compensation/support.
- `reach §V:749+` — cost of maintaining current equivalence.
- `SRT_Glossary.md:2188+` — historical `Psi_f^maint` “maintenance friction”.
- `STATUS.md:145,147` — GRG friction != Psi_f automatically; GRG debt != repository debt.

Important unresolved collision:

`Psi_f^maint` is semantically close to reach §V “cost of maintaining current generative equivalence”, but identity is **not established**.

Recommendation:

Add explicit routing guard; do not merge without owner reconciliation.

### T10 — prediction / expectation / E_G / normativity

Representative instances:

- `Selection Vertical §F:197+` — prediction and expectation are different; expectation reshapes reachability.
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GENERATIVE_EXPECTATION_TYPING_2026-09-20.md §§2–5` — structural generative expectation and normativity route.
- `GRG v0.3 §§13–15` — P_G, Generative Order, E_G.
- `STATUS.md:143` — structural/operative expectation != E_G automatically.

Correction to the first census:

Normativity is **not** an ownerless routing question. The 09-20 author adjudication already owns a bounded route:

~~~text
structural generative expectation
-> indexed comparison
-> normative direction
while
complete moral ought / legitimacy remains NOT ESTABLISHED
~~~

Recommendation:

Router must point there rather than inventing a new expectation/normativity bridge.

### T11 — wholeward / higher-order / integration / hierarchy / composition

Representative instances:

- `Selection Vertical §J:291+` — higher-order = broader generative integration, not merely “more hierarchical”.
- `Selection Vertical §M:360+` — weak wholeward direction.
- `capacity §§F–G:251+` — regeneration / transformation / wholeward gain distinction.
- `reach §AC:970+` — wholeward sharpened through friction conversion / reconstructive reach.
- `GRG v0.3 §17:759+` — programme wholeward direction.

Correction:

The first router cited v0.3 §16. Correct section is **§17**.

Recommendation:

Do not use a new higher-order term unless it states why current wholeward / composition / reorganization language is insufficient.

### T12 — GTS / relation record / operator / grammar candidate

Representative instances:

- `GRG v0.3 §8:304+` — GTS as primary bounded record unit.
- `GRG v0.3 §11:471+` — composition.
- current post-#1042 protocol/template — candidate extraction only after owner overlap leaves a residual.

Risk:

Machine analysis may name a “new operator / relation / grammar” when it has only described a source process in GTS terms.

Recommendation:

Term Router may say DISTINCT_BURDEN provisionally, but that is not candidate retention. Route onward to GOV-SUB01 if it is a named mechanism/operator and to GRG owner-overlap if it is a GRG candidate.

## 5. Recent collisions already resolved by #1042

These are examples, not a second owner vocabulary.

| Old / working wording | Current routing | Owner |
|---|---|---|
| dual reconstruction | plain source-cut + GRG-cut reconstruction | post-#1042 corrective audit / protocol |
| continuity_role fourth axis | retired; use authority + retrieval value + currentness | #1042 corrective audit |
| CALIBRATION as generic disposition | do not reuse generically | #1042 + existing framework-vs-calibration meaning |
| L1/L2/L3/L4 writeback layers | retired due canonical namespace collision | #1042 corrective audit |

The Live Term Router should point to these decisions, not duplicate the active GRG result/action lists.

## 6. Bare “继续” is retrieval semantics, not term governance

The same PR also preserves the author's clarification that bare continuation often implies directional acceptance.

Owner:

`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CONTINUE_DIRECTIONAL_ACCEPTANCE_2026-09-24.md`.

Important scope after review:

~~~text
accepted / boundedly continued analysis
-> must remain routeable
-> consult when the relevant topic enters task scope
!= preload every historical package at fresh-session start
~~~

This keeps continuity compatible with bounded retrieval.

## 7. Normalization strategy

Do not global-replace.

### Pass A — current PR

- Glossary-internal Live Term Router;
- bounded terminology census;
- no canonical owner edit.

### Pass B — possible later active-surface cleanup

Only after independent review.

Possible actions:

- alias notes;
- qualification of overloaded terms;
- routing fixes;
- removing clearly retired working labels from **active** templates / handoffs where meaning is unchanged.

Historical source/provenance remains unchanged.

### Pass C — accepted-analysis re-entry audit

Separate PR.

Purpose:

- recover old accepted/continued machine reasoning;
- map old labels to current owners using the Live Term Router;
- identify PARTIALLY ABSORBED / ACTIVE BUT UNROUTED branches.

## 8. Spine status

The author instructed:

> “按你刚才建议的处理顺序开始依次处理，开 PR 方便做独立评审”

This authorizes the staged audit workflow.

It does **not** by itself override current STATUS:

~~~text
FURTHER OWNER CLEANUP PAUSED BY DEFAULT
~~~

Therefore:

> Generative Ontology Spine thinning is **not yet an active scheduled edit**.

After the re-entry audit, a separate bounded author decision is required before opening a canonical Spine-thinning PR.

## 9. Review questions

1. Does the Glossary-internal router stay non-authoritative?
2. Are owner references complete enough?
3. Does the Router understate or overstate any owner semantics?
4. Is availability correctly marked UNDER-SPECIFIED?
5. Does latent reconstructive reach remain explicitly under CURRENT NEXT pressure-test rather than pre-retained?
6. Are support / friction / Psi_f^maint collisions represented without premature identity?
7. Is the Term Router -> GOV-SUB01 -> GRG admission sequence clear?
8. Does the “continue” retrieval rule remain bounded enough to preserve 6+2 retrieval discipline?
9. Is any proposed future canonical cleanup still being implied without separate author adjudication?

## 10. Current verdict

~~~text
dynamic lexical / semantic router:
  NEEDED, but inside existing Glossary entry

new root router:
  NO

fixed final glossary:
  NO

GOV-SUB01:
  EXISTING DOWNSTREAM MECHANISM / OPERATOR GOVERNANCE

bulk renaming:
  NO

active-owner normalization:
  POSSIBLE LATER, AFTER REVIEW

accepted-analysis re-entry audit:
  NEXT SEPARATE PR IF #1043 PASSES

Spine thinning:
  NOT YET AUTHORIZED AS A CANONICAL EDIT
  REQUIRES SEPARATE BOUNDED AUTHOR DECISION
~~~
