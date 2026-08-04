---
id: SRT-PAPER-FORCING-CH-EVIDENCE-D05-C5OP-GOEDEL-TO-COHEN
title: "D05 — C5-op Audit: Gödel Stage to Cohen Event"
type: evidence_dossier
status: active
canonical: false
layer: philosophy_bridge
epistemic_layer: evidence
claim_mode: evidence
date: 2026-08-04
submission_ready: false
evidence_state: partially_adjudicated
binding_strategy: Philosophy/Papers/Mathematical_Reachability_and_Problem_Individuation_Strategy.md@strategy_note_v0_7
linked_manuscript: Philosophy/Papers/Forcing_CH_Research_Regime_Staged_Draft_EN.md
depends_on_dossiers:
  - Philosophy/Papers/Forcing_CH_Evidence/D03_Goedel_Stage_Baseline.md
  - Philosophy/Papers/Forcing_CH_Evidence/D03_Cohen_Event_Baseline.md
---

# D05 — C5-op Audit: Gödel Stage to Cohen Event

**Dossier state:** first formal-historical C5-op adjudication; not submission-ready

**Comparator pair:** the documented Gödel-stage CH regime → the Cohen event-level construction

**Primary obligation:** `EVD-D05-0001`

**Carried forward, not adjudicated here:** `EVD-D04-0002`

**Method:** adversarial. The audit began by attempting to defeat C5-op failure, not by assuming forcing was novel.

## Verdict snapshot

| Evidence obligation | Verdict | Narrow result |
|---|---|---|
| `EVD-D05-0001` | **qualified** | C5-op failure is supported for a bounded background–operation–output relation: the one whose load-bearing generative component is the externally constructed complete sequence that Cohen states is not definable in the ground model. The unbounded claim — that no historically admissible Gödel-stage operation reproduces the Cohen relation — is not established, because the Gödel-stage repertoire in evidence is limited to Gödel's own published operations, `EVD-D04-0002` remains unresolved, and the finding is relative to a method individuation the frozen strategy leaves open (§7.1, §9.3(3)). |
| `EVD-D04-0002` | **unresolved** (unchanged) | This audit adds the Cohen-stage background as a translation target and surfaces a prior typing question about the semantic model premise. No background-translation verdict is issued. |

Registered translation candidates: `D05-T01`–`D05-T05`. One (`D05-T02`) is the best preservation case, is presented at full strength, and is adjudicated **granularity-dependent** rather than defeated: a genuine partial preservation reading at coarse proof-goal granularity, a failure at the generation-sensitive granularity this audit uses (§7.1). One (`D05-T03`) is ruled inadmissible for this obligation on type grounds and is carried to D09.

## 1. Scope and non-claims

This dossier tests `EVD-D05-0001` only: whether the Cohen event-level background–operation–output relation can be conservatively reproduced by a historically admissible, type-correct translation registered in this audit.

It does **not** adjudicate, and nothing in it may be read as adjudicating:

- `EVD-D05-0002`, which concerns the mature CH-local forcing regime;
- heritability, non-locality, or scaffold formation;
- the institutionalization of forcing;
- CH-local research-regime reconstruction;
- the global set-theoretic update regime;
- C2 or strong semantic re-individuation;
- either calibration control;
- the SRT bridge.

> **SCOPE LOCK**
>
> C5-op failure establishes operation-level novelty and nothing more. Under frozen `strategy_note_v0_7` §5.3, regime innovation requires `¬C5_op(m*) ∧ Inst(m*)`, and `Inst = H ∧ N ∧ S` is a separate conjunctive evidence burden assigned to D06. No inference from this dossier to regime innovation is permitted, and none is made.

The purpose of the audit was not to defend the manuscript. Sections 4 and 7 record the strongest reconstructions found against the manuscript's central prerequisite, stated at full strength before any assessment.

## 2. Evidence inherited from D03

No source text is re-verified here. Every item below is already adjudicated in the two D03 dossiers at the status shown there; stable keys and exact locations are reproduced so that each step of this audit is traceable. Qualified findings are carried forward as qualified.

### 2.1 From the Gödel-stage baseline

| Inherited proposition | Status in D03 | Key and location |
|---|---|---|
| Gödel's backgrounds are the specific von Neumann/Bernays class-set system (`Σ`, 1940) and Zermelo-style systems (1939), with "definite property" identified with a propositional function over all sets; modern ZF/ZFC is a retrospective normalization. | supported (`EVD-D03-0006`) | `GODEL1938-AC-GCH`, p. 556; `GODEL1939-GCH`, p. 224 n. 1; `GODEL1940-MONOGRAPH`, pp. 1–2; `BERNAYS1941-REVIEW`, p. 112 |
| The operation is construction of an inner model/class of constructible sets by transfinite recursion and definability, followed by axiom verification and formal contradiction reduction. In 1940 the rigorous exposition proceeds set-by-set through eight binary operations; the `Def(L_α)` presentation is retrospective. | supported (`EVD-D03-0006`) | `GODEL1938-AC-GCH`, pp. 556–557; `GODEL1939-GCH`, pp. 223–224, Ths. 7–10; `GODEL1940-MONOGRAPH`, pp. 35–61; `KANAMORI1996-DEVELOPMENT`, pp. 36–38 |
| The output is a model satisfying the base axioms plus constructibility, AC and GCH, and a one-directional relative-consistency consequence. | supported (`EVD-D03-0006`) | `GODEL1939-GCH`, pp. 223–224; `GODEL1940-MONOGRAPH`, pp. 35–61 |
| The result explicitly does **not** license consistency of `ZF + not-CH`, full independence of CH, or a countable transitive model of ZFC from bare `Con(ZFC)`. | supported (`EVD-D03-0006`; `EVD-D03-0007`) | `GODEL1938-AC-GCH`, p. 557 n. 5; D03 Gödel §3.4 non-licensing list |
| Completeness and Löwenheim–Skolem may yield a model, and a countable model, but supply neither transitivity, well-foundedness, nor standardness; a countable transitive model is a strictly stronger premise. | supported as a prohibition (`EVD-D03-0007`) | `KENNEDY2025-GODEL-SEP`, §2.1.3; `MARKS2026-SET-THEORY-NOTES`, §18, p. 75, Ths. 18.1–18.3 |
| Independence-type discussion was not wholly absent by 1947: Gödel lists demonstrability, disprovability and undecidability, calls undecidability most likely, calls its proof a promising attack, and identifies his own result as establishing non-disprovability. | supported as counterevidence to total absence (`EVD-D03-0008`) | `GODEL1947-CH`, pp. 519–520 |
| A stable field-wide Gödel-stage response-role structure is **not** established. | qualified (`EVD-D03-0008`) | D03 Gödel §4.2 and bounded-search TODO |
| Forward and reverse Gödel-stage background translations are **not** complete. | unresolved (`EVD-D04-0002`) | D03 Gödel §5.1 candidate table |

### 2.2 From the Cohen-event baseline

| Inherited proposition | Status in D03 | Key and location |
|---|---|---|
| Cohen's background is a version of ZF without Choice and with Regularity, abbreviated `Z-F`. | supported (`EVD-D03-0009`) | `COHEN1963-CH-I`, p. 1143 |
| For the semantic construction Cohen fixes a countable standard model `M` of `Z-F` and takes it to satisfy `V=L`; membership is the actual membership relation on a transitive set-like domain. | supported (`EVD-D03-0009`) | `COHEN1963-CH-I`, p. 1144; `KANAMORI2008-COHEN`, pp. 359–360 |
| The event-stage operation has seven verified components: countable standard ground model; new intended subsets `a_α`; ramified language and ranked terms; finite conditions; forcing relation defined in the ground model; externally constructed complete sequence; interpreted extension `N`. | supported (`EVD-D03-0009`) | `COHEN1963-CH-I`, pp. 1144–1147, Defs. 2–8; `KANAMORI2008-COHEN`, pp. 360–361 |
| The complete sequence is constructed outside `M` by external enumeration, and Cohen explicitly notes it is **not definable in `M`**. | supported (`EVD-D03-0009`; `EVD-D03-0013`) | `COHEN1963-CH-I`, p. 1147, Def. 8 |
| Lemma 5 is the event-stage truth lemma: a statement is true in `N` exactly when some condition in the complete sequence forces it. | supported (`EVD-D03-0009`) | `COHEN1963-CH-I`, p. 1147, Lemma 5 |
| The output is `N ⊨ ZF + AC + not-CH`, under the stated semantic assumptions, followed by a separate finite-fragment relative-consistency reduction. | supported (`EVD-D03-0009`) | `COHEN1964-CH-II`, pp. 105–109, Lemmas 18–20; p. 110 |
| Cohen's finite-fragment discharge enumerates axioms, works with sufficiently large finite fragments, obtains countable standard models for those fragments, and transforms a contradiction in a finite target fragment into one in a finite source fragment; the only special property used is transitivity. | supported (`EVD-D03-0009`; `EVD-D03-0013`) | `COHEN1964-CH-II`, p. 110 |
| `M, P, G, M[G]` is **not** Cohen's literal 1963 formalism; the unramified partial-order/generic-filter form is later. | defeated as a historical identification (`EVD-D03-0010`) | contrast of `COHEN1963-CH-I`, pp. 1144–1147 with `KANAMORI2008-COHEN`, pp. 369–370 |
| Boolean-valued and generic-filter formulations are mathematically connected reformulations, not historically identical or unconditionally interchangeable. | qualified (`EVD-D03-0010`) | `KANAMORI2008-COHEN`, pp. 369–370; `HAN-VANDOORN2020-CH`, §1, pp. 1–2 |
| The Cohen event was **not** already the institutionalized forcing regime. | unresolved and blocked (`EVD-D03-0009`; `EVD-D03-0010`) | D03 Cohen §1 stage lock; `KANAMORI2008-COHEN`, pp. 369–370 |

### 2.3 Inherited limits that bound this audit

Three inherited limits constrain every verdict below and are a direct reason the final verdict is *qualified* rather than *supported*. They are not the only reason: a fourth, non-inherited one — the granularity dependence of `D05-T02` — is established in §7.1 and recorded at §9.3(3).

1. **The Gödel-stage operation repertoire in evidence is Gödel's own.** D03 Gödel §5 documents `M_t` from Gödel's publications. Its §10 states explicitly that D05 "still lacks … a historically admissible inventory of alternative earlier operations." No stage-wide 1938–1963 repertoire has been assembled.
2. **`EVD-D04-0002` is unresolved.** No proof-level bidirectional background interpretation exists between Gödel's formal systems and any later background, so `τ_B` and `ρ_B` are registered candidates only.
3. **`EVD-D03-0010` is qualified.** Cross-formulation relations are local and formulation-specific. This audit may therefore not treat Cohen's ramified construction, the partial-order/generic-filter form, and the Boolean-valued form as one object.

No new external source was required for this audit, and none was added. Every technical and historical assertion below traces to a proposition already adjudicated in §2.1 or §2.2. Where a technical question would have needed a new source, it is registered as unresolved in §13 rather than asserted.

## 3. Typed comparison objects

Unsupported cells are marked unresolved rather than filled by inference. Modern notation appears only where the source dossier already marked it retrospective.

| Component | Gödel stage | Cohen event | Evidence |
|---|---|---|---|
| `B` background | von Neumann/Bernays class-set system `Σ` (1940); Zermelo-style system with or without substitution (1939); "definite property" as propositional function over all sets | `Z-F`: ZF without Choice, with Regularity | `GODEL1938-AC-GCH`, p. 556; `GODEL1939-GCH`, p. 224 n. 1; `GODEL1940-MONOGRAPH`, pp. 1–2; `COHEN1963-CH-I`, p. 1143 |
| `B` additional premise carried in the presentation | none of the verified statements uses countability, standardness or transitivity as a premise | a countable standard model `M` of `Z-F`, taken to satisfy `V=L`, with actual membership on a transitive set-like domain | D03 Gödel §3.6; `COHEN1963-CH-I`, p. 1144 |
| `M` operation | transfinite recursion generating the constructible class by definability over preceding levels (1940: set-by-set via eight binary operations); axiom verification in the constructed class; formal contradiction reduction | seven-component assembly: ground model; intended new subsets `a_α`; ramified language and ranked terms `F_α`; finite conditions; forcing relation defined in `M`; externally constructed complete sequence; interpretation yielding `N` | `GODEL1938-AC-GCH`, pp. 556–557; `GODEL1939-GCH`, pp. 223–224; `GODEL1940-MONOGRAPH`, pp. 35–61; `KANAMORI1996-DEVELOPMENT`, pp. 36–38; `COHEN1963-CH-I`, pp. 1144–1147; `KANAMORI2008-COHEN`, pp. 360–361 |
| `M` characteristic generative resource | definability over the preceding level of the hierarchy, within the base structure | a complete sequence built outside `M` and explicitly **not definable in `M`** | `GODEL1939-GCH`, p. 224 n. 1; `KANAMORI1996-DEVELOPMENT`, pp. 36–38; `COHEN1963-CH-I`, p. 1147, Def. 8 |
| `O` output | model satisfying base axioms plus `V=L`, AC and GCH; one-directional relative consistency; associated descriptive-set outputs | `N ⊨ ZF + AC + not-CH`; separately, a finite-fragment relative-consistency consequence | `GODEL1938-AC-GCH`, p. 556; `GODEL1939-GCH`, pp. 223–224, Ths. 7–10; `COHEN1964-CH-II`, pp. 105–110 |
| generation relation `(b,m) ⤳ o` | from the stated base system, the recursion produces the constructible class; axiom verification and Theorems 8–10 yield AC and GCH in it; the final paragraph converts a contradiction in the extension into one in the base | from the stated base and the semantic premise, the ramified/conditions/forcing assembly plus the external complete sequence produces `N`; the truth lemma connects forcing in `M` to truth in `N`; Part II verifies the axioms, cardinal preservation and `not-CH`; p. 110 discharges to relative consistency | `GODEL1939-GCH`, pp. 223–224 and final paragraph; `GODEL1940-MONOGRAPH`, pp. 1–2, 35–61; `COHEN1963-CH-I`, p. 1147, Lemma 5; `COHEN1964-CH-II`, pp. 105–110 |
| documented dependency between the stages | — | the Cohen ground model is taken to satisfy `V=L`, i.e. the Cohen operation consumes the characteristic Gödel-stage output as an input | `COHEN1963-CH-I`, p. 1144 |
| stage-wide repertoire beyond the named actor | **unresolved** — no 1938–1963 inventory assembled | not applicable to this comparator | D03 Gödel §10 |

## 4. Registry of admissible conservative translations

### 4.1 Governing interpretation used in this audit

C5-op is applied as frozen `strategy_note_v0_7` §4.6 defines it: a property of a **comparison between two regimes together with registered translation data**, not a unary predicate of an operation. A Cohen-stage component may *witness* failure; it is not itself the failure.

Two interpretive points had to be fixed before candidates could be assessed. Both are recorded as freeze-exception candidates in §14; neither modifies the frozen strategy.

**(a) Modality of "conservative reproduction."** Frozen §4.6 states the preservation requirement but does not say whether reproduction is tested against in-principle derivability from the earlier system's mathematical resources or against the earlier system's historically documented operative repertoire. This audit uses the **repertoire reading**, because the task's admissibility conditions require each candidate to be "historically documented as available at the Gödel stage," and because the in-principle reading would make C5-op unfalsifiable in the other direction — under it, essentially no later method would fail preservation, and the criterion could not discriminate any case.

**(b) Granularity of `M_t`.** Frozen §3.3 types `M_t` as the set of methods implementable for the problem and §5.2 as `𝔘_t↾_{Q_φ}`. Neither fixes how a method is individuated. The verdict is granularity-sensitive: see `D05-T02`.

This audit uses a **generation-sensitive** individuation — a method is individuated by the background–operation–output generation relation it realizes, including that relation's load-bearing intermediate objects, not by the proof goal it serves. The ground is internal to C5-op: frozen §4.6 states the criterion as a condition on `(b,m) ⤳ o`, so an individuation that discards the objects the relation runs through cannot test the condition it is being applied to.

A second consideration is recorded together with its limit. Frozen §7.5–7.7 and §19(6) require the criterion to discriminate a result innovation (Control A), a local technical innovation (Control B) and forcing; under a proof-goal individuation that three-case calibration could not be performed, because Control A and forcing would fall on the same side. That consequence is real and is reported. It is **not** used here as a demonstration that the proof-goal individuation is the wrong one. Selecting a granularity because it yields the discriminations the calibration exercise expects would make the calibration a test of the granularity chosen to pass it, which is circular. What the observation establishes is that the frozen strategy is under-specified at exactly this point — recorded as a freeze-exception candidate in §14(b) — not that the coarse reading has been refuted.

**Admissibility.** A candidate is admissible only if it is historically documented as available at the Gödel stage; type-correct for backgrounds, methods and outputs; compatible with the `B_t`/`M_t`/`O_t` profile recorded in D03 Gödel §5; stated without importing post-Cohen forcing vocabulary as already available; explicit enough to test operation–output generation rather than a loose analogy; and registered here before the verdict. No attempt is made to refute every logically imaginable reconstruction; the claim tested is bounded to the candidates below.

`D05-T01`–`D05-T05` are audit identifiers, not theoretical symbols.

### 4.2 `D05-T01` — Inner-model construction as the model-construction predecessor

| Field | Record |
|---|---|
| `b_G` | `Σ` or the Zermelo-style base [`GODEL1938-AC-GCH`, p. 556; `GODEL1939-GCH`, p. 224 n. 1; `GODEL1940-MONOGRAPH`, pp. 1–2] |
| `m_G` | transfinite recursion generating the constructible class by definability; axiom verification; contradiction reduction [`GODEL1939-GCH`, pp. 223–224; `GODEL1940-MONOGRAPH`, pp. 35–61] |
| `o_G` | model of base + `V=L` + AC + GCH; one-directional relative consistency [`GODEL1939-GCH`, pp. 223–224, Ths. 7–10] |
| `b_C` | `Z-F` plus the countable standard `V=L` model premise [`COHEN1963-CH-I`, pp. 1143–1144] |
| `m_F` | the seven-component ramified assembly [`COHEN1963-CH-I`, pp. 1144–1147] |
| `o_C` | `N ⊨ ZF + AC + not-CH` [`COHEN1964-CH-II`, pp. 105–109] |
| proposed `ρ_M` | send the forcing assembly to "construct a structure from a given base by ordinal-indexed recursion, then verify the axioms in it" |
| function allegedly preserved | building a model of a target theory from a base, without assuming that theory |
| generation relation allegedly preserved | `(base, ordinal-indexed model construction) ⤳ (model of base + target statement)` |
| type-correctness | partial. Both `m` are model-construction operations, so the codomain sort is right; but the mapping identifies operations whose characteristic generative resources differ (see below) |
| historical admissibility | the Gödel operation is documented as available; the *mapping* is what is at issue |
| retrojection risk | **high.** D03 Gödel §3.2 marks `Def(L_α)` as an expository reconstruction, and D03 Cohen §8 defeats `M,P,G,M[G]` as Cohen's literal formalism. Conducting the comparison in modern notation on both sides would manufacture similarity that neither primary record supports |
| strongest preservation argument | both are ordinal-indexed recursive constructions of a structure from a given base, both verify base axioms inside the constructed structure, and both discharge to a conditional relative-consistency statement by contradiction transformation |
| strongest failure argument | the two operations' generative resources are complementary rather than translatable. The Gödel operation generates its output from definability over the preceding level within the base structure; the Cohen operation's output-determining component is a complete sequence that the primary source states is *not definable in `M`* [`COHEN1963-CH-I`, p. 1147]. A `ρ_M` satisfying the candidate would have to send an operation whose load-bearing component is ground-non-definable to an operation whose only documented generative resource is ground-definability. No such mapping is documented, and the direction of the construction differs correspondingly: `L` is obtained by restricting to definable sets, `N` by adjoining an object that escapes ground definability |
| provisional verdict | **does not preserve** |

### 4.3 `D05-T02` — Relative-consistency proof as the operation–output type

| Field | Record |
|---|---|
| `b_G`, `m_G`, `o_G` | as in `D05-T01`, with `m_G` read as "prove relative consistency by constructing a model and transforming a contradiction" |
| `b_C`, `m_F`, `o_C` | as in `D05-T01`, with `m_F` read at the same coarseness, and with `o_C` taken as the finite-fragment relative-consistency consequence rather than `N` [`COHEN1964-CH-II`, p. 110] |
| proposed `ρ_M`, `ρ_O` | identity on the proof-goal type: both regimes contain "relative-consistency proof by constructed model plus contradiction transformation," and both outputs are conditional one-directional relative-consistency statements |
| function allegedly preserved | conditionality, one-directionality, the discharge from a semantic construction to a syntactic reduction |
| generation relation allegedly preserved | `(base system, relative-consistency proof method) ⤳ (conditional relative-consistency statement)` |
| type-correctness | correct **iff** `M_t` is individuated by proof-goal type. Frozen §3.3 and §5.2 do not fix this |
| historical admissibility | **admissible.** The contradiction-transformation move is documented at the Gödel stage [`GODEL1939-GCH`, p. 224 final paragraph; `GODEL1940-MONOGRAPH`, pp. 1–2], and Cohen's p. 110 discharge is a finite-fragment contradiction transformation of the same shape [`COHEN1964-CH-II`, p. 110] |
| retrojection risk | **low.** The candidate uses only vocabulary attested on both sides |
| strongest preservation argument | see §7. This is the best preservation case found and is presented there at full strength |
| strongest failure argument | one defeater and one exposure, kept apart. **Defeater, at the granularity under test.** C5-op is a condition on `(b,m) ⤳ o`, and the Cohen relation's load-bearing intermediate output is the extension `N`, not the consistency statement; D03 Cohen §4.2 separates the semantic construction route from the finite-fragment reduction as two routes with different premises and outputs, so collapsing them discards a distinction the primary record itself draws. Under the generation-sensitive individuation of §4.1(b) the candidate has no image for `N` and therefore reproduces a consequence of the relation rather than the relation. **Exposure, not a defeater.** Under a proof-goal individuation the frozen triple calibration could not be performed, since any two relative-consistency proofs would preserve C5-op with respect to each other and Control A could not be distinguished from forcing. That is a cost borne by the frozen strategy's calibration architecture and evidence of its under-specification of `M_t` granularity; it does not independently refute the coarse preservation reading. See §4.1(b), §7 and §14(b) |
| provisional verdict | **granularity-dependent.** At coarse proof-goal granularity it is a genuine *partial* preservation reading — partial because it reproduces the conditional relative-consistency statement while dropping `N`. At the generation-sensitive granularity used by this audit it fails: no image for `N`, no image for the event-level generation relation, and therefore no reconstruction of the relation under test |

### 4.4 `D05-T03` — Cohen supplied only the missing opposite direction

| Field | Record |
|---|---|
| `b_G`, `m_G`, `o_G` | **unfillable on the operation side.** The candidate offers no Gödel-stage `m_G`; it offers a Gödel-stage *response form*. That the registry format cannot be completed here is the finding, not an omission |
| `b_C`, `m_F`, `o_C` | as in `D05-T01` |
| steelman | The metamathematical response form was already in place. Gödel in 1947 lists demonstrability, disprovability and undecidability, calls undecidability the most likely option, calls its proof a promising attack, and identifies his own result as having established non-disprovability [`GODEL1947-CH`, pp. 519–520]. On this reading the later regime is the earlier regime with one instance filled in, and no new operation type is required |
| what would be preserved | the response form "show a statement is not refutable/not provable by exhibiting a model," and its evaluative standing |
| type assessment | this is a claim about `R_t` and `E_t`, not about `M_t`. C5-op tests the background–operation–output generation relation. Anticipating that an output could exist is not an operation that generates it, and frozen §4.8 assigns response-role structure to C2, not to C5-op |
| historical admissibility | the historical evidence is verified and strong, but it is evidence of the wrong type for this obligation |
| retrojection risk | not applicable; the risk here is the converse, namely importing an `R_t` finding into an `M_t` test |
| provisional verdict | **inadmissible for `EVD-D05-0001`** on type grounds. Explicitly carried to D09, where D03 Gödel §10 already requires Gödel 1947 to be treated as a named countercandidate |

### 4.5 `D05-T04` — Forcing as a technically generalized continuation of existing model-construction practice

| Field | Record |
|---|---|
| `b_G`, `m_G`, `o_G` | as in `D05-T01`, with `m_G` read as "construct a ranked hierarchy over a base and interpret the result" |
| `b_C`, `m_F`, `o_C` | as in `D05-T01` |
| steelman | This is the candidate with the strongest textual support. Cohen's ground model is taken to satisfy `V=L` [`COHEN1963-CH-I`, p. 1144], so the Cohen construction literally begins from the characteristic Gödel-stage output. Both constructions use ordinal-ranked hierarchies — the constructible levels on one side, the ramified terms `F_α` on the other [`KANAMORI1996-DEVELOPMENT`, pp. 36–38; `COHEN1963-CH-I`, pp. 1144–1145, Defs. 2–4]. On this reading forcing is the existing practice carried further |
| proposed `ρ_M` | send the forcing assembly to the Gödel-stage practice of constructing a ranked hierarchy of terms/sets over a base and interpreting the result |
| function allegedly preserved | ordinal ranking as the organizing device; verification of base axioms inside the constructed structure; composability of the two constructions |
| generation relation allegedly preserved | `(base, ranked-hierarchy construction) ⤳ (interpreted structure satisfying the base)` |
| type-correctness | the sorts match, but the candidate establishes composition rather than reproduction |
| historical admissibility | admissible as a claim about the Gödel-stage practice; its evidence is verified |
| retrojection risk | **moderate.** "Ramified hierarchy" similarity must not be inflated into method identity: D03 Cohen §5.2 records that the ramified language was *eliminated* in the later unramified form, so it was not the component that later practice carried forward |
| strongest preservation argument | the two operations are documented as composable, and the later one is documented as consuming the earlier one's output; a continuation reading is therefore not merely conceivable but textually grounded |
| strongest failure argument | composition is not conservative reproduction. `ρ_M` must land inside the Gödel-stage repertoire; showing that `m_F` *consumes* `o_G` shows the opposite ordering. The candidate's own best evidence tells against it: because the Cohen presentation starts from a ground model already satisfying `V=L` and then adjoins a resource explicitly not definable in that model [`COHEN1963-CH-I`, pp. 1144, 1147], the primary record shows the Cohen operation treating the Gödel-stage output as a starting point that must be supplemented, not as a repertoire within which the new relation can be reproduced |
| provisional verdict | **does not preserve**; its evidence corroborates the failure witness in §8 |

### 4.6 `D05-T05` — The Gödel-stage model-existence apparatus

| Field | Record |
|---|---|
| `b_G`, `m_G`, `o_G` | `b_G` as in `D05-T01`; `m_G` here is the model-existence apparatus (completeness, Löwenheim–Skolem) rather than the constructible-class recursion; `o_G` is a set-sized model of the base theory |
| `b_C`, `m_F`, `o_C` | as in `D05-T01`; the component under test is `b_C`'s semantic premise |
| steelman | Completeness and Löwenheim–Skolem were available at the Gödel stage and yield a model, and a countable model, from consistency [`KENNEDY2025-GODEL-SEP`, §2.1.3; `MARKS2026-SET-THEORY-NOTES`, §18, p. 75, Th. 18.1]. Cohen's construction needs a countable model. If that apparatus supplies `b_C`'s semantic component, then at least the background side of the Cohen relation is Gödel-stage reconstructible |
| proposed `ρ_B` | send Cohen's countable standard `V=L` ground-model premise back to a Gödel-stage model-existence argument |
| function allegedly preserved | obtaining a set-sized model of the base theory from a consistency assumption |
| type-correctness | correct in sort; the question is whether the codomain premise is reachable |
| historical admissibility | the apparatus is documented as available |
| retrojection risk | low |
| strongest preservation argument | countability, which Cohen uses to enumerate requirements and build the complete sequence [`COHEN1963-CH-I`, p. 1147], is exactly what Löwenheim–Skolem delivers |
| strongest failure argument | D03 Gödel §3.6 is explicit and verified: neither completeness nor Löwenheim–Skolem supplies transitivity, well-foundedness or standardness, and a countable transitive model is a strictly stronger premise not inferred anywhere in that dossier [`MARKS2026-SET-THEORY-NOTES`, §18, p. 75, Ths. 18.2–18.3]. Cohen requires a *standard* model whose membership is the actual membership relation on a transitive set-like domain [`COHEN1963-CH-I`, p. 1144]. The available apparatus therefore does not reach `b_C` |
| provisional verdict | **does not preserve**; blocks the background component independently of the operation component |

## 5. Forward-preservation audit

The forward direction asks whether the documented Gödel-stage relation can be carried into the Cohen-stage profile without distortion:

`(b_G, m_G) ⤳ o_G  ⟹  (τ_B(b_G), τ_M(m_G)) ⤳ τ_O(o_G)`

No obstruction was found, and one was actively looked for. The Cohen-stage profile retains a ZF-style base [`COHEN1963-CH-I`, p. 1143]; it retains the constructible-model construction, since the ground model is taken to satisfy `V=L` [`COHEN1963-CH-I`, p. 1144]; and it retains contradiction transformation as a discharge move [`COHEN1964-CH-II`, p. 110]. The Gödel-stage relation therefore appears to survive forward translation.

Two limits are recorded rather than passed over.

1. This is **provisional, not verified**. `τ_B` is not established: `EVD-D04-0002` is unresolved, and the base systems differ (`Σ` / Zermelo-style versus `Z-F`) with no proof-level bidirectional interpretation on record.
2. Forward success carries no weight for the obligation. Frozen §4.6 requires preservation "反向亦然" — in both directions. A one-directional embedding of the earlier relation into the later profile is exactly what one expects when a repertoire grows, and it is compatible both with conservative extension and with the introduction of an irreducibly new relation. The audit therefore does not treat §5 as partial evidence for preservation.

## 6. Reverse-reconstruction audit

The reverse direction is the novelty test:

`(b_C, m_F) ⤳ o_C  ⟹  (ρ_B(b_C), ρ_M(m_F)) ⤳ ρ_O(o_C)`

Assessed component by component against the registered candidates.

### 6.1 Background component `ρ_B`

Blocked, on evidence, by `D05-T05`. Cohen's background carries a premise — a countable *standard* model with actual membership on a transitive domain — that the documented Gödel-stage model-existence apparatus does not deliver, since completeness and Löwenheim–Skolem supply neither transitivity nor standardness [D03 Gödel §3.6; `COHEN1963-CH-I`, p. 1144].

A qualification is required and is recorded rather than resolved. It is not settled whether the semantic model premise belongs to `B_C` or to `M_C`. If it belongs to the operation rather than the background, this blockage relocates to `ρ_M` instead of disappearing; the reverse reconstruction is obstructed either way, but the *component* named as obstructed changes. See §13 Q3 and §14(c).

### 6.2 Operation component `ρ_M`

Blocked by `D05-T01` and `D05-T04`. The Cohen operation's load-bearing generative component is a complete sequence built outside `M` and explicitly not definable in `M` [`COHEN1963-CH-I`, p. 1147, Def. 8]. The documented Gödel-stage operation generates its output from definability over the preceding level within the base structure [`GODEL1939-GCH`, p. 224 n. 1; `KANAMORI1996-DEVELOPMENT`, pp. 36–38]. No registered candidate exhibits a `ρ_M` carrying the former into the latter, and `D05-T04`'s evidence shows the Cohen presentation adjoining that resource *on top of* a ground model already satisfying `V=L`.

### 6.3 Output component `ρ_O`

The output types differ: a model of base + `V=L` + AC + GCH on one side, `N ⊨ ZF + AC + not-CH` on the other, and D03 Gödel §3.4's non-licensing list explicitly refuses consistency of `ZF + not-CH` as a Gödel-stage consequence.

**This difference is recorded as insufficient on its own.** A new theorem is not a new reusable operation. Under frozen §5.3 and the distinctions the task requires this audit to preserve, an output difference between two stages is what any theorem-adding history produces; it becomes evidence about `M_t` only when paired with a documented obstruction on the operation side. Here it is so paired, by §6.2. Standing alone it would carry nothing, and no part of the verdict rests on it alone.

### 6.4 Generation relation

The failure that survives scrutiny is located in the relation itself, not in any single component read in isolation. Cohen's relation runs: from the base and its semantic premise, through the ramified/conditions/forcing assembly, through an externally constructed non-ground-definable complete sequence, to the extension `N`, whose truth is tied back to ground-model forcing by Lemma 5 [`COHEN1963-CH-I`, p. 1147]. Removing the non-definable component does not leave a weaker version of the same relation; it removes the object that determines `N` and the term on which the truth lemma is stated. No registered admissible candidate reconstructs that relation, and `D05-T02` — the only candidate that preserves anything at the relation level — does so at a proof-goal granularity that drops `N`, i.e. it preserves a coarser relation than the one C5-op is being applied to here. Whether that coarser relation is the intended object of `M_t` is not settled by the frozen strategy; see §7 and §14(b).

## 7. Best preservation case

Stated at full strength, without hedging, as the strongest case found that C5-op is preserved.

> Both stages contain one and the same operation type: prove a relative-consistency statement by constructing a model of the target theory from the base and then transforming a putative contradiction. Gödel's 1939 final paragraph states exactly this conversion — the construction can be carried out in the corresponding formal systems so that a contradiction from the extension yields a contradiction in the unextended theory [`GODEL1939-GCH`, p. 224] — and the 1940 introduction repeats it as the metamathematical content of the monograph [`GODEL1940-MONOGRAPH`, pp. 1–2]. Cohen's published consistency conclusion has the same shape and, notably, is *not* left resting on the semantic construction: on p. 110 he enumerates the axioms, works with sufficiently large finite fragments, obtains countable standard models for those fragments, and transforms a contradiction in a finite target fragment into one in a finite source fragment, remarking that the only special property used is transitivity [`COHEN1964-CH-II`, p. 110]. D03 Cohen §4.2 records that this discharge is what carries the published relative-consistency theorem. So at the level at which each author states his own metamathematical result, both regimes contain the same background–operation–output relation: `(base system, model-construction-plus-contradiction-transformation) ⤳ (conditional one-directional relative-consistency statement)`. `ρ_M` and `ρ_O` are then the identity on that type, `ρ_M` is historically documented on both sides, and no post-Cohen vocabulary is needed to state it. On this reading C5-op is preserved, the manuscript's central prerequisite fails, and the paper stops.

This is a serious case and the audit does not dismiss it. Two objections were raised against it. They do not have the same force, and the difference matters enough to state before either is used.

**First objection — it discards a distinction the primary record draws.** This one holds. D03 Cohen §4.2 separates the event-stage semantic construction from the finite-fragment reduction as two routes with different premises and different outputs, and the Cohen dossier's claim-type matrix keeps `N ⊨ ZF+AC+not-CH` and `Con(ZFC) → Con(ZFC+not-CH)` as distinct claims. `D05-T02` preserves C5-op only by taking `o_C` to be the second and dropping the first. But the extension `N` is not an optional intermediate: it is the object Part II verifies the axioms in, the object Lemma 20 establishes `not-CH` in, and the object the truth lemma is about [`COHEN1963-CH-I`, p. 1147; `COHEN1964-CH-II`, pp. 105–109]. A translation that reproduces the consistency statement while having no image for `N` has not reproduced the relation `(b,m) ⤳ o`; it has reproduced a consequence of it. Stated precisely, this objection is decisive against `D05-T02` **at any individuation under which the event-level generation relation, with its intermediate objects, is what C5-op ranges over** — which is the individuation this audit uses and states in §4.1(b).

**Second objection, reclassified — the calibration consequence is an exposure, not an independent refutation.** If `M_t` is individuated by proof-goal type, then any two relative-consistency proofs preserve C5-op with respect to each other. Frozen §7.5–7.7 requires the criterion to discriminate a result innovation (Control A), a local technical innovation (Control B) and forcing; §19(6) makes triple calibration a submission condition. Under the coarse individuation, Control A — an important result inside a mature regime — and forcing would fall on the same side of C5-op, and the required three-case calibration could not be performed at all.

That consequence is real and is reported. It does **not** by itself refute the coarse preservation reading, and this dossier no longer states it as a second defeater. A calibration requirement says what the criterion must be able to discriminate; it cannot also select the method individuation under which the criterion discriminates that way, because doing so makes the calibration a test of the granularity chosen in order to pass it. The argument would be circular in exactly the place where it is asked to do work. What the observation does establish is that the frozen strategy **under-specifies `M_t` granularity**, and that the calibration architecture cannot repair that under-specification from inside. That finding is recorded as a freeze-exception candidate in §14(b), where it is the sharpest of the three.

### 7.1 Corrected status of `D05-T02`

Three statements, all of which this audit holds simultaneously:

1. **At coarse proof-goal granularity, `D05-T02` remains a genuine partial preservation reading.** It is not a defeated candidate at that granularity; it is a reading the frozen strategy does not exclude. It is *partial*, not full, because what it reproduces is the conditional one-directional relative-consistency statement, with `N` dropped.
2. **At the generation-sensitive granularity used by this audit (§4.1(b)), it fails.** It does not preserve `N`, and through `N` it does not preserve the event-level background–operation–output generation relation. This is the first objection above, applied at the granularity this audit fixes and defends on grounds internal to C5-op.
3. **This granularity dependence is a principal reason for the qualified verdict.** The verdict is not that the shared proof type has been shown to preserve nothing. It is that whether it preserves the thing C5-op ranges over turns on a method individuation the frozen strategy leaves open (§9.3, §9.5, §14(b)). No wording anywhere in this dossier may state the preservation claim as unconditionally defeated.

## 8. Best failure witness

**The witness.** The externally constructed complete sequence of conditions, which Cohen states is not definable in `M` [`COHEN1963-CH-I`, p. 1147, Def. 8], operating as a load-bearing component of the generation relation: it determines the new subsets `a_α` and the interpretation structure `N`, and the event-stage truth lemma is stated in terms of it — a statement is true in `N` exactly when some condition in the complete sequence forces it [`COHEN1963-CH-I`, p. 1147, Lemma 5]. Kanamori independently reconstructs the same component and records that the sequence is obtained outside `M` by a Baire-category argument [`KANAMORI2008-COHEN`, pp. 360–361].

**What exactly fails to be preserved.** Primarily the **operation** and, through it, the **generation relation**. The documented Gödel-stage operation generates its output from definability over the preceding level within the base structure [`GODEL1939-GCH`, p. 224 n. 1; `KANAMORI1996-DEVELOPMENT`, pp. 36–38]; the Cohen relation requires, as the component that fixes its output, an object characterized by *not* being so definable. Under the repertoire reading of §4.1(a), no registered admissible `ρ_M` carries the second into the first.

The **background** fails independently, at the countable-standard-model premise, by `D05-T05` — with the qualification in §6.1 that if that premise is typed into `M_C` rather than `B_C`, this failure relocates to the operation rather than dissolving.

The **output type** differs, but that difference is explicitly *not* part of the witness. It is recorded in §6.3 as insufficient standing alone.

**What the witness is not.** It is not a claim that forcing was revolutionary, important, or widely adopted; none of those is a C5-op property, and D03 Cohen leaves uptake unresolved and blocked. It is not a claim that the mathematical ingredients were unavailable in 1940 — that question is left open in §13 Q1 under the repertoire reading. It is not a claim about the mature partial-order or Boolean-valued formulations, which `EVD-D03-0010` keeps qualified and formulation-specific. And it is not a claim that the Cohen event was already institutionalized forcing, which D03 Cohen explicitly blocks.

## 9. Verdict

**`EVD-D05-0001`: qualified.**

C5-op failure is supported for a bounded background–operation–output relation — the Cohen relation whose load-bearing generative component is the externally constructed, ground-non-definable complete sequence — under the repertoire reading of §4.1(a) and the generation-sensitive method individuation of §4.1(b). The unbounded claim is not established, and the verdict is explicitly relative to that individuation (§9.3(3)).

### 9.1 Candidate by candidate

| Candidate | Admissible? | Outcome | Decisive record |
|---|---|---|---|
| `D05-T01` inner-model predecessor | yes | fails to preserve | generative resources are complementary: ground-definability versus a component explicitly not definable in `M` [`GODEL1939-GCH`, p. 224 n. 1; `COHEN1963-CH-I`, p. 1147] |
| `D05-T02` relative-consistency proof type | yes | **granularity-dependent**: a genuine partial preservation reading at proof-goal granularity; fails at the generation-sensitive granularity used here, having no image for `N` or for the event-level generation relation | D03 Cohen §4.2 two-route separation; `COHEN1964-CH-II`, pp. 105–110; individuation fixed at §4.1(b), assessed at §7.1 |
| `D05-T03` missing opposite direction | **no** — wrong type | inadmissible for this obligation; carried to D09 | `GODEL1947-CH`, pp. 519–520 is an `R_t` record; frozen §4.8 assigns response roles to C2 |
| `D05-T04` generalized continuation | yes | fails to preserve; its evidence corroborates failure | Cohen's ground model satisfies `V=L` and the non-definable resource is adjoined on top of it [`COHEN1963-CH-I`, pp. 1144, 1147] |
| `D05-T05` model-existence apparatus | yes | fails to preserve; blocks the background independently | completeness and Löwenheim–Skolem give neither transitivity nor standardness [D03 Gödel §3.6] |

### 9.2 Source by source

- `COHEN1963-CH-I`, p. 1147 (Def. 8, Lemma 5) is the single decisive record. It supplies the non-definability statement and shows the component is load-bearing for both `N` and the truth lemma.
- `COHEN1963-CH-I`, p. 1144 does double duty: it grounds `D05-T04`'s steelman (`V=L` ground model) and, read with p. 1147, converts that steelman into corroboration of failure.
- `COHEN1964-CH-II`, p. 110 is the strongest record *against* the verdict: it is the basis of `D05-T02`. It is not set aside on evidential grounds, and it is not set aside outright. It is bounded by the first objection in §7 at the granularity fixed in §4.1(b); at coarser granularity it remains a live partial preservation record (§7.1).
- `GODEL1939-GCH`, p. 224 n. 1 and `KANAMORI1996-DEVELOPMENT`, pp. 36–38 fix the Gödel-stage generative resource as definability, which is what makes the mismatch statable rather than impressionistic.
- D03 Gödel §3.6, resting on `KENNEDY2025-GODEL-SEP` §2.1.3 and `MARKS2026-SET-THEORY-NOTES` §18, blocks the background reconstruction. `MARKS2026` is corroborative only and the D03 dossier already carries a submission-stage TODO to replace it with a page-verified monograph; the background blockage should be regarded as resting on a source the sibling dossier itself flags for strengthening.
- `GODEL1947-CH`, pp. 519–520 is verified and materially relevant, but to D09, not here.

### 9.3 Why not *supported*

Three inherited limits, each recorded in §2.3, prevent the unbounded verdict.

1. **The Gödel-stage repertoire in evidence is one actor's.** D03 Gödel §10 states that D05 lacks a historically admissible inventory of alternative earlier operations. Candidates `D05-T01`–`D05-T05` exhaust what the merged dossiers document, not what the stage contained. A stage-wide 1938–1963 inventory could surface a model-construction technique used for independence or consistency results that is not Gödel's and not yet tested here; until that inventory exists, "no historically admissible Gödel-stage operation reproduces the Cohen relation" is stronger than the evidence.
2. **`EVD-D04-0002` is unresolved.** Reverse background reconstruction is assessed against a background profile that has no completed bidirectional interpretation, so `ρ_B` is evaluated against candidates rather than against an established translation.
3. **The verdict is granularity-relative, and `D05-T02` is where that bites.** §4.1(b) fixes the individuation from the structure of C5-op itself — the criterion is stated on `(b,m) ⤳ o`, so the relation's intermediate objects are part of what must be preserved. It is *not* fixed by appeal to the frozen calibration requirement, which cannot select a granularity without circularity (§7). At the generation-sensitive individuation, `D05-T02` fails; at coarse proof-goal granularity it remains a genuine partial preservation reading that the frozen strategy nowhere excludes. Since the frozen strategy does not settle which individuation `M_t` intends (§14(b)), the best preservation case is neither reconstructed nor refuted across the board — and that, together with limits 1 and 2, is a principal reason the verdict is qualified rather than supported. A strategy revision that fixes `M_t` granularity explicitly could move this verdict in either direction.

### 9.4 Why not *unresolved*

Because the five registered candidates include the two that the merged dossiers make available in their strongest form (`D05-T02` on the operation-type side, `D05-T04` on the continuity side), both were steelmanned before assessment, and each is adjudicated on a documented record rather than on absence of evidence. That includes `D05-T02`: its granularity dependence is a stated, bounded finding about the frozen strategy's under-specification, not a gap in the historical evidence. A bounded result is available and is reported.

### 9.5 Why not *defeated*

No registered candidate reconstructs the Cohen relation at the granularity at which C5-op is tested here. `D05-T02` came closest and is a principal reason the verdict is qualified rather than supported: at the generation-sensitive individuation it fails, having no image for `N` and hence none for the event-level generation relation, while at coarse proof-goal granularity it remains a genuine partial preservation reading the frozen strategy does not exclude. A *defeated* verdict would require the preservation case to have been refuted at every admissible individuation. It has not been, and this dossier does not claim it has.

### 9.6 Explicitly not upgraded for importance

No part of this verdict rests on forcing's later importance, adoption, teachability or influence. Those are D06 questions and remain untouched.

## 10. Stop-rule consequence

Stated as required by frozen `strategy_note_v0_7` §12 and §19.

- **If C5-op were preserved, the manuscript's central prerequisite would fail and the paper would stop.** That is not the present finding.
- **The verdict is qualified, not preserved.** The paper does not stop.
- **The verdict is qualified, not supported.** The manuscript may not assert unbounded operation novelty. Permitted wording is bounded: that the Cohen event-level relation has no conservative reproduction among the registered admissible Gödel-stage reconstructions, with the boundary in §9.3 stated.
- **C5-op failure, at whatever strength it is finally established, shows operation-level novelty only.** Frozen §5.3 requires `¬C5_op(m*) ∧ Inst(m*)` for regime innovation. `Inst = H ∧ N ∧ S` is conjunctive, requires independent evidence for each conjunct, and is assigned to D06. No regime-innovation inference is available from this dossier.
- **Institutionalization remains entirely open.** D03 Cohen blocks it explicitly.
- **CH-local research-regime reconstruction still requires `EVD-D05-0002` and practice evidence.** This dossier concerns the Cohen event only.
- **The global set-theoretic update regime is untouched** and, per frozen §7.3, requires cross-problem and infrastructure evidence beyond CH.
- **C2 is untouched.** `D05-T03` was registered and ruled inadmissible here precisely so that the Gödel-1947 record reaches D09 unadjudicated. The weak title and weak abstract remain mandatory.
- **The SRT bridge is untouched** and remains subject to its preregistered Level A/B/C fallback.

## 11. Next evidence task

D06 must establish, independently and conjunctively, for the forcing operation:

- **`H` heritability** — that other researchers could publicly reconstruct, learn and reuse the operation, with evidence separate from the Cohen event itself;
- **`N` non-locality** — documented use across distinct problems, model families or proof tasks, not a list of CH-adjacent applications;
- **`S` scaffold formation** — entry into later method chains, iteration and preservation practices, forcing axioms, generic-absoluteness programs, standard terminology, textbooks, training or durable infrastructure.

D06 must not treat this dossier's qualified verdict as licence for a regime-innovation conclusion, must keep the Cohen event separate from institutionalized forcing as D03 Cohen §1 requires, and must not substitute influence for the three conditions.

Two technical obligations are newly registered by this dossier. Both are recorded here for later promotion into the manuscript's evidence index; the staged manuscript is out of scope for this PR and was not modified.

| New obligation | Content | Why it matters |
|---|---|---|
| `EVD-D05-0003` | A historically admissible inventory of the **stage-wide** 1938–1963 operation repertoire available for consistency and independence results, beyond Gödel's own publications. | This is the principal reason the verdict is qualified rather than supported. Closing it is the highest-value next step for D05. |
| `EVD-D05-0004` | Verified technical determination of whether the **documented constructible-inner-model operation** — transfinite recursion generating the constructible class by definability over preceding levels, together with axiom verification in it — is *provably incapable* of yielding a model of `not-CH` **when that operation alone is applied and no outer-model or generic-extension operation is added to the repertoire**. The question is about the minimality and absoluteness behaviour of the constructible class under that one documented operation, and about nothing else. **Scope restriction, part of the obligation.** This is *not* the question whether some operation applied to a ground model satisfying `V=L` can yield `not-CH`. The Cohen construction is exactly such an operation and does yield it — that is precisely the relation §8 identifies as unreproduced — so no universal claim about operations over a `V=L` ground model is made, needed, or permitted here. | If verified, this converts "no documented Gödel-stage operation does it" into "the documented operation cannot do it," which strengthens the bounded finding in §9. It does **not** by itself close §9.3, since limit 1 (no stage-wide 1938–1963 repertoire inventory, `EVD-D05-0003`) and limit 2 (`EVD-D04-0002` unresolved) would both remain open, and an upgrade of `EVD-D05-0001` to supported requires those. **Not asserted here**: no source in the merged dossiers establishes it, and this audit added none. |

A third item belongs to `EVD-D04-0002` and is registered in §13 Q3: whether the countable-standard-model premise is typed into `B_C` or `M_C`.

## 12. Claim-to-evidence ledger

| Ledger claim | Evidence ID | Sources and exact locations | Adjudicated status | Downstream permission |
|---|---|---|---|---|
| The Cohen relation's load-bearing generative component is a complete sequence not definable in the ground model. | `EVD-D05-0001` | `COHEN1963-CH-I`, p. 1147, Def. 8 and Lemma 5; `KANAMORI2008-COHEN`, pp. 360–361 | supported | May be stated as the failure witness, with the component's role in `N` and the truth lemma named. |
| The documented Gödel-stage operation generates its output from definability over the preceding level within the base structure. | `EVD-D05-0001` | `GODEL1939-GCH`, p. 224 n. 1; `KANAMORI1996-DEVELOPMENT`, pp. 36–38 | supported (inherited) | May be stated as the earlier generative resource. |
| No registered admissible Gödel-stage reconstruction reproduces the Cohen background–operation–output relation. | `EVD-D05-0001` | `D05-T01`–`D05-T05` registry, §4 | supported **for the registered candidates only** | Bounded wording only; the §9.3 boundary must accompany it. |
| No historically admissible Gödel-stage operation whatsoever reproduces the Cohen relation. | `EVD-D05-0001` | — | **not established** | Prohibited. Requires `EVD-D05-0003`. |
| Both stages contain relative-consistency proof by constructed model plus contradiction transformation. | `EVD-D05-0001` | `GODEL1939-GCH`, p. 224; `GODEL1940-MONOGRAPH`, pp. 1–2; `COHEN1964-CH-II`, p. 110 | supported as the best preservation case | Must be reported in the manuscript's objection section, not suppressed. |
| That shared proof type establishes C5-op preservation. | `EVD-D05-0001` | §7, §7.1 assessment; individuation fixed at §4.1(b) | **qualified / granularity-dependent** | May not be reported as unconditionally defeated. Permitted wording: at the generation-sensitive individuation used here it does not establish preservation, having no image for `N` or the event-level generation relation; at coarse proof-goal granularity it remains a genuine partial preservation reading the frozen strategy does not exclude. The individuation must be stated wherever the claim is used. |
| The output-type difference between the stages establishes operation novelty. | `EVD-D05-0001` | §6.3 | defeated as a standalone inference | A new theorem is not a new operation. |
| Cohen's ground model satisfies `V=L`, so the Cohen operation consumes the Gödel-stage output. | `EVD-D05-0001` | `COHEN1963-CH-I`, p. 1144 | supported | Supports composition, **not** conservative reproduction. |
| Gödel-stage completeness/Löwenheim–Skolem apparatus supplies Cohen's ground-model premise. | `EVD-D05-0001` | D03 Gödel §3.6; `MARKS2026-SET-THEORY-NOTES`, §18, Ths. 18.2–18.3 | defeated | Neither transitivity nor standardness follows. Note the sibling dossier's own strengthening TODO on this source. |
| Gödel 1947 shows the later response form was already available. | — | `GODEL1947-CH`, pp. 519–520 | **not adjudicated here**; type-inadmissible for C5-op | Carried to D09 as a named countercandidate. |
| Forward and reverse Gödel-stage background translations are complete. | `EVD-D04-0002` | §5, §6.1; D03 Gödel §5.1 | unresolved (unchanged) | No background-translation verdict is available. |
| C5-op failure supports regime innovation. | — | frozen §5.3 | prohibited | `Inst = H ∧ N ∧ S` is a separate D06 burden. |

## 13. Unresolved decisive questions

1. Under the **in-principle** reading rejected in §4.1(a), were the mathematical resources for a Cohen-type construction available in the Gödel-stage systems? This audit does not answer it and does not need to, but a reader who rejects the repertoire reading will require it.
2. Does a stage-wide 1938–1963 inventory contain a model-construction operation, not Gödel's, that reproduces the Cohen relation? (`EVD-D05-0003`.)
3. Is the countable-standard-model premise part of `B_C` or of `M_C`? The reverse reconstruction is obstructed either way, but which component is named as obstructed depends on the answer, and `EVD-D04-0002` cannot be closed without it.
4. Is the documented constructible-inner-model operation, applied alone and with no outer-model or generic-extension operation added, *provably* incapable of yielding a `not-CH` model? The scope restriction is part of the question and not a hedge on it: the corresponding unrestricted question has a known negative answer, since the Cohen construction yields `not-CH` from a `V=L` ground model. (`EVD-D05-0004`.)
5. Which method individuation does the frozen strategy actually intend for `M_t`? The answer decides `D05-T02` and with it part of the §9 verdict, and it cannot be read off the calibration requirements without circularity (§7). (§4.1(b), §14(b).)
6. Does the finite-fragment discharge on `COHEN1964-CH-II`, p. 110 stand in a proof-theoretic relation to Gödel's contradiction transformation strong enough to revive `D05-T02` under a *fine* individuation? This audit found no such record; D03 Cohen §9 Q3 registers the comparison as open.
7. Would a page-verified standard monograph, replacing the corroborative teaching-note citation flagged in D03 Gödel §3.6, change the strength of the background blockage in `D05-T05`?

## 14. Freeze-exception candidates

Documented as required, and **not applied**. The frozen strategy was not modified by this PR, and none of these items was used to alter a verdict beyond what §4.1 states openly.

**(a) `strategy_note_v0_7` §4.6 does not fix the modality of "conservative reproduction."** The preservation requirement is stated without saying whether it is tested against in-principle derivability or against a historically documented repertoire. The two readings give opposite behaviour: in-principle makes C5-op failure nearly unobtainable, repertoire makes it nearly automatic unless bounded by admissibility conditions. This audit used the repertoire reading with explicit admissibility conditions. A strategy revision should fix the reading in §4.6 itself rather than leaving it to each dossier.

**(b) `M_t` granularity is not fixed, and the calibration requirements cannot fix it.** Frozen §3.3 and §5.2 type `M_t` without individuating "method." `D05-T02` shows the C5-op verdict is granularity-sensitive in a way that decides the candidate outright: at coarse proof-goal granularity it is a genuine partial preservation reading, at the generation-sensitive granularity of §4.1(b) it fails to preserve `N` and the event-level generation relation. This audit therefore fixes the individuation from the structure of C5-op itself, which frozen §4.6 states as a condition on `(b,m) ⤳ o`.

It is recorded explicitly that the frozen calibration architecture (§7.5–7.7, §19(6)) **cannot discharge this under-specification**. That a proof-goal individuation would prevent the required three-case calibration is a genuine consequence and is reported as such, but a requirement on what the criterion must discriminate cannot by itself select the individuation under which the criterion discriminates that way — doing so would make the calibration a test of the granularity chosen to pass it. An earlier draft of this dossier treated that consequence as an independent refutation of the coarse reading; it is not, and the treatment is corrected in §7 and §7.1.

This is the sharpest of the three under-specifications recorded here. A strategy revision should state the intended `M_t` individuation directly in §3.3 or §5.2, rather than leaving it to be inferred from the calibration requirements or fixed by dossier-level convention.

**(c) The typing of a semantic model premise is unassigned.** Frozen §3.3 gives `B_t` as "default backgrounds and live competing extensions" and `M_t` as methods. A premise such as "there is a countable standard model of the base theory" is a background assumption in one reading and a component of the construction in another. §13 Q3 records the consequence.

None of these is a demonstrated type error in the frozen framework. Each is an under-specification that a live audit was able to work around by stating its reading openly, and each should be resolved in a later strategy revision rather than by dossier-level convention.

> **DOWNGRADE, WITHDRAWAL, AND SRT FALLBACK LOCK**
>
> If later evidence shows C5-op preserved, the paper stops. C5-op failure at any strength establishes operation-level novelty only; regime innovation additionally requires independently evidenced heritability, non-locality and scaffold formation. CH-local evidence cannot support a global set-theoretic update-regime claim. Strong semantic re-individuation remains conditional on completed C2 evidence relative to the Gödel stage; while C2 is incomplete or preserved, the weak title and weak abstract remain mandatory. If the SRT bridge fails its preregistered test, Level B or Level C applies. This dossier changes none of the frozen `strategy_note_v0_7` rules.

This dossier establishes a bounded, source-adjudicated C5-op failure between the documented Gödel-stage regime and the Cohen event, names the boundary that keeps the verdict short of unbounded, and issues no institutionalization, CH-regime, global, C2, calibration or SRT verdict.
