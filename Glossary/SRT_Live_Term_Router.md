---
id: SRT-GLOSSARY-LIVE-TERM-ROUTER
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
  - SRT-CANONICAL-REGISTRY
  - SRT-CONTEXT-ROUTER
  - SRT-GOV-SUB01-SUBTRACTIVE-AUDIT
---

# SRT / GRG Live Term Router

> Role: dynamic semantic routing **inside the existing Glossary entry surface**.
>
> This file does not define SRT or GRG. It only helps an agent decide whether a proposed repeated term is probably an alias, an overloaded word, a partial overlap, a genuinely distinct burden, or still just a working label, and then points to the real owner.
>
> Definitions, admission criteria, maturity and claim strength remain with the named owner.

## 0. Trigger

Exploratory dialogue may freely coin temporary wording.

Run this router before a term is **hardened for repeated repository use**.

For this protocol, “hardened” means at least one of:

- the term appears in a file title, section title used as a reusable named construct, frontmatter tag/key/value, schema/table key, or named mechanism/operator field;
- the same proposed term-of-art is intentionally repeated across **2 or more files**;
- the term is being presented as a stable SRT / GRG construct rather than a one-off explanatory phrase.

This gate does not apply to ordinary prose, metaphors or explicitly marked working labels.

## 1. Lexical / semantic triage

Use only these labels here:

~~~text
ALIAS_SAME_BURDEN
OVERLOADED_SAME_NAME
PARTIAL_OVERLAP
DISTINCT_BURDEN
WORKING_LABEL_ONLY
~~~

Meaning:

- ALIAS_SAME_BURDEN = prefer the existing routed term.
- OVERLOADED_SAME_NAME = qualify / namespace before reuse.
- PARTIAL_OVERLAP = keep both only with an explicit boundary.
- DISTINCT_BURDEN = lexical check found no existing owner that obviously absorbs it.
- WORKING_LABEL_ONLY = leave exploratory; do not harden yet.

Important:

> DISTINCT_BURDEN is **not** a retention verdict.

If the proposed distinct item is a new named mechanism, operator, scalar, layer, threshold, core symbol or irreducibility claim, route next to:

`Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md`

If it is a GRG candidate, also run the current GRG owner-overlap / absorption procedure. Those later procedures decide research retention; this router does not.

## 2. Relationship to other classification systems

These are different questions:

| System | Question | Owner |
|---|---|---|
| Live Term Router | Is this wording lexically/semantically new, overloaded, overlapping or only a working label? | this Glossary shard |
| GOV-SUB01 R0–R4 / N1 / N2 / P | Does a proposed named mechanism/operator/component survive subtraction / replacement testing? | Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md |
| GRG owner-overlap result | Does current GRG already carry the burden, is this only a realization/reorganization, or does a residual candidate remain? | current GRG protocol / reconstruction template named by STATUS |

Do not substitute one system for another.

## 3. Canonical / cross-owner structural families

| Routing label | Near / confusable wording | Owner-grounded boundary | Current owner / route | Status / maturity | Collision / routing note |
|---|---|---|---|---|---|
| Selection occurrence | actualised Selection, event-level Selection, descriptive/modelled change | occurrence != retained history; genuine actualised Selection vs merely descriptive/modelled change remains OPEN | Spine §§2–3; Phase-3 provenance map | canonical routing + OPEN edge | PARTIAL_OVERLAP |
| retained historical efficacy / history | sediment, sedimentation, retained consequence, writeback, inheritance | later-effect burden where prior Selection remains materially effective; not required for every occurrence | Spine §4; SRT_Irreversibility.md | canonical routing | PARTIAL_OVERLAP |
| One | formed process-unity, recurrent organization | formed process-unity carried by a **relatively separable Selection-mediated vertical reconstitution / self-conditioning path**; ordinary causal recurrence is insufficient | SRT_One_Formation.md §2; Spine §5 | canonical semantic owner / P1-candidate architecture | do not collapse with neighboring terms |
| Selection-position | operative locality, position, perspective-position | time-local operative aspect of an already formed One; not a second universal endpoint and not automatically perspective/Bearer/subject-position | One Formation §3; Spine §6 | canonical semantic owner | do not collapse with neighboring terms |
| Stable ISP | stable position, recurrent standing, persistent ISP | stronger recurrent standing than One | Core_21b P1-T06; Spine §7 | canonical theorem owner | do not collapse with neighboring terms |
| Bearer | bearer-position, prospective self-exposure, subject carrier | separately gated from One / Selection-position / Stable ISP | Spine §8 + compatible Bearer owners | gated / stronger standing | do not collapse with neighboring terms |
| perspective | positionality, Selection-position, subject-position | finite positionality != formed perspective; Selection-position != perspective-bearing subject-position automatically | Spine §6; One Formation | partly OPEN / owner-routed | PARTIAL_OVERLAP |
| anticipation | future-conditioning, prospective self-indexing | later-selectability effect != formed-position anticipation automatically; formed anticipation != prospective self-indexing P automatically | Spine §6.3 | gated / partly OPEN | PARTIAL_OVERLAP |

## 4. GRG research-term families

These rows are research routing, not canonical SRT definitions.

| Routing label | Near / confusable wording | Owner-grounded boundary | Current owner / route | Status / maturity | Collision / routing note |
|---|---|---|---|---|---|
| object / relation as cuts | objectification, partition, coordinate, relation-first | object and relation are cuts rather than primitive furniture; relation-first is not automatically privileged | Selection Vertical §B; GRG v0.3 §7; capacity §§I/L | author-source + v0.3 research | PARTIAL_OVERLAP |
| objectification | compression, coarse-graining, working cut | broad stabilization/organization of a cut; not automatically an error | capacity §§I, AB–AC; cross-objectification method | source-level / method | PARTIAL_OVERLAP |
| re-objectification / recutting | recut, reclassification, reconstruction of cuts | reopening and changing the operative cut when consequence/friction requires it | capacity §AC | source-level research | PARTIAL_OVERLAP |
| generative capacity | possibility, capability, potential | real conditional organization that can alter future Selection under relevant conditions | capacity §C | source-level research | PARTIAL_OVERLAP |
| availability | presence, accessibility | owner **names and author-confirms the need to distinguish** availability in the four-way capacity split, but does not yet supply a sufficiently independent definition | capacity §D | source-level / OWNER-NAMED, UNDER-SPECIFIED | preserve the owner label; do not strengthen or discard it |
| accessibility | reachability, availability, activation | owner distinguishes accessibility from capacity and actualisation; exact relation to broader reach remains research-level | capacity §D; reach owners below | source-level research | PARTIAL_OVERLAP |
| actualisation of capacity | occurrence, execution, realization | a capacity enters a concrete Selection | capacity §§C–D | source-level research | PARTIAL_OVERLAP |
| GRG generative proxy | proxy, representation, measurement proxy, operational proxy | selective compression / operative partition; must not be identified with measurement or operational proxy automatically | Selection Vertical §E; capacity §Q; reach §Q; STATUS guards | source-level research | OVERLOADED_SAME_NAME |
| generative reach | reach, influence, propagation, reachability | where a difference can actually propagate / become consequence-bearing | capacity §R; Selection Vertical §§E–F | source-level parent burden | PARTIAL_OVERLAP |
| active generative reach | active reach, active access | a difference currently enters wider Selection loops | reach §M | source-level research | PARTIAL_OVERLAP |
| latent reconstructive reach | latent reach, recoverability, archived possibility | currently compressed/local difference may later regain generative reach; repository retrievability is a different issue | reach §M; STATUS CURRENT NEXT | **ACTIVE PRESSURE-TEST / not presumed retained** | PARTIAL_OVERLAP |
| generative reconstructibility | reconstructibility, reconstruction, recoverability | theory-side ability to reopen sufficient generative provenance/cuts; not repository/data/dialogue recoverability | reach §§A–K; #1042 corrective guard | source-level research | OVERLOADED_SAME_NAME |
| reconstruction | source-native reconstruction, structural reconstruction, repository reconstruction | generic process word; qualify what is reconstructed | GRG v0.3 §9; cross-objectification protocol | mixed / context-dependent | OVERLOADED_SAME_NAME |
| generative equivalence | equivalence, sameness, neutrality | bounded and intervention-relative; not identity | capacity §K | source-level research | PARTIAL_OVERLAP |
| supported / subsidized equivalence | maintained equivalence, scaffolded equivalence | equivalence whose continued validity depends on support conditions | reach §R | source-level research | PARTIAL_OVERLAP |
| support | resource support, generative support, compensatory support, gating | earlier owner: generativity-restructuring, not mere resource provision; later reach record separates proxy/support and distinguishes parasitic vs integrative compensation | Selection Vertical §I; capacity §§D/R; reach §§Q/R/W | source-level; internally differentiated | OVERLOADED_SAME_NAME |
| friction | maintenance cost, transformation pressure, boundary friction, constitutive friction, Psi_f | Selection Vertical §H gives maintenance/transformation roles; capacity §M splits constitutive/boundary; reach §§V/X further narrows maintained-equivalence cost and friction conversion; not automatically canonical Psi_f | those owners + STATUS guard | source-level family; canonical Psi_f separate | OVERLOADED_SAME_NAME |
| maintenance-friction interface | Psi_f^maint, maintenance cost of equivalence | historical glossary Psi_f^maint is close to reach §V “cost of maintaining current equivalence”; identity is **not established** and requires owner reconciliation before reuse | SRT_Glossary.md ~2188; reach §V | historical glossary vs source-level GRG; UNRESOLVED COLLISION | PARTIAL_OVERLAP |
| generative debt | debt, maintenance debt, reconciliation debt | not repository maintenance/reconciliation debt; later support burden can borrow present stability from future reconstructibility | reach §§Y–AB; STATUS guard | source-level research | OVERLOADED_SAME_NAME |
| prediction | forecast, Generative Prediction P_G | Selection Vertical distinguishes prediction vs expectation; P_G is a later typed GRG output | Selection Vertical §F; GRG v0.3 §13 | source + v0.3 research | PARTIAL_OVERLAP |
| structural generative expectation | expectation, anticipation, forecast | structural burden broader than explicit predictive model; normativity route is typed in 09-20 author adjudication | Generative Expectation Typing §§2–5; Selection Vertical §F | author-source research | PARTIAL_OVERLAP |
| Generative Expectation (E_G) | generative expectation, structural expectation, normative expectation | E_G is the v0.3 typed programme output indexed to admitted Generative Order; structural/operative expectation != E_G automatically | GRG v0.3 §15; 09-21 adjudication; STATUS guard | v0.3 programme object | PARTIAL_OVERLAP |
| normativity route | normative expectation, ought, good | generative expectation may open indexed normative comparison; complete moral ought / legitimacy not established | 09-20 Generative Expectation Typing §5; 09-21 adjudication | author-source; moral bridge OPEN | PARTIAL_OVERLAP |
| Generative Order | order, stability, persistence, hierarchy, analyst goal | admitted order has explicit GO1–GO5 burden; existence/persistence/stability/hierarchy are insufficient | GRG v0.3 §14; 09-21 adjudication §3 | v0.3 programme object | PARTIAL_OVERLAP |
| wholeward | wholeward integration, higher-order gain, hierarchy growth | weak source-level wholeward in Selection Vertical; capacity §§F–G distinguish regeneration/transformation/wholeward gain; reach §AC sharpens via friction conversion/reconstructive reach; v0.3 §17 owns programme direction | those owners | multi-stage research; not canonical SRT | PARTIAL_OVERLAP |
| higher-order | hierarchy, integration, composition | broader generative integration, not merely more hierarchy; relation to wholeward/composition must be stated | Selection Vertical §J; capacity §E; GRG v0.3 §11 | research family | OVERLOADED_SAME_NAME |
| Generative Transformation Signature (GTS) | relation record, grammar card, candidate operator | primary bounded record unit; a record schema, not an ontic object or automatically a new grammar candidate | GRG v0.3 §8 | v0.3 active research schema | PARTIAL_OVERLAP |
| grammar candidate | operator, relation, higher-order operator, pattern | only after current owner/neighbor absorption leaves a nontrivial residual | current STATUS-routed GRG protocol/template | admission-gated research | lexical distinctness never substitutes for downstream audits |
| gating (organization-level) | gate, valve, selective permeability, Maxwell-demon gate, support | a formed organization in which an Ĝ-type Selection role is realized / carried; primitive Selection is not gating of a pregiven flow | 2026-09-24 pre-object vertical source §6 + second adjudication D-1; reconciliation plan PV-K1 | author-source; canonical wording pending | PARTIAL_OVERLAP (with `support`) |
| gate geometry | coarse-graining geometry, partition geometry, stability geometry, gating geometry | 2026-09-25 author source uses this as a working formulation for the stable equivalence / boundary / neighborhood / transition structure by which formed organization coarse-grains differences; it is not primitive Selection, not a new field substance, and not yet distinct from existing gating + objectification/coarse-graining + stability burdens | 2026-09-25 gate-geometry author adjudication §§2–3; objectification row; organization-level gating row; One/stability owners | **SHORT-TERM HIGH-PRIORITY WORKING CONSTRUCT** | WORKING_LABEL_ONLY / PARTIAL_OVERLAP; retain only if bounded reconciliation shows gain beyond existing owners |
| pre-object vertical inquiry | vertical, verticality, vertical structure, vertical research | research direction "under the object cut"; does not redefine One Formation Def-OF-1 or Spine event-level verticality | 2026-09-24 pre-object vertical source §1; One Formation §1; Spine §3; GRG v0.3 §4 | author-source research | OVERLOADED_SAME_NAME |
| glue | stability, maintained coherence, support, friction, vertical reconstitution | working metaphor for dynamically maintained generative coherence; not a substance / force | 2026-09-24 pre-object vertical source §10; plan PV-K4 | working label | WORKING_LABEL_ONLY; likely PARTIAL_OVERLAP |
| generative divinity | 神性, inexhaustible generativity, non-preclosure | author-endorsed generativity reading; no entity / survival drive / moral direction | 2026-09-24 pre-object vertical source §16 + second adjudication D-2; plan PV-K8 | founding metaphysical intuition | WORKING_LABEL_ONLY |

## 5. Working / retired wording

These are routing warnings, not a copied classification owner.

| Wording | Route | Decision owner |
|---|---|---|
| dual reconstruction | use plain source-cut + GRG-cut reconstruction | post-#1042 corrective audit / active protocol |
| continuity_role as fourth retrieval axis | retired; use authority + retrieval value + currentness | #1042 corrective audit |
| CALIBRATION as generic owner-overlap disposition | do not reuse generically; programme-level meaning already exists | #1042 corrective audit + framework-vs-calibration record |
| OPERATIONALIZATION as generic disposition | avoid as named result class | #1042 corrective audit |
| SOURCE_REALIZATION | use current GRG result vocabulary owner; do not maintain a copy here | #1042 active protocol/template |
| L1/L2/L3/L4 writeback layers | retired to avoid collision with canonical L0/L1/L2 | #1042 corrective audit |
| semantic reconstructibility for repository/session recovery | use semantic continuity / recoverability | #1042 corrective audit |

For the **current GRG owner-overlap result vocabulary and GRG-cut action vocabulary**, follow the active protocol/template routed by STATUS. Do not copy those lists here.

## 6. Maintenance

Update this shard when:

- a repeated term is about to harden;
- a new collision / alias is found;
- an owner changes;
- an accepted-analysis re-entry audit recovers an older label that current retrieval no longer exposes.

Do not update it merely because a one-off conversation uses a metaphor or exploratory phrase.

A router update alone does not authorize a canonical edit.
