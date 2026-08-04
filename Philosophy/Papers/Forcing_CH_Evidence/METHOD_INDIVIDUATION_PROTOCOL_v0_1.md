---
id: SRT-PAPER-FORCING-CH-EVIDENCE-METHOD-INDIVIDUATION-PROTOCOL
title: "Method Individuation Protocol v0.1 — Forcing–CH Evidence Project"
type: evidence_protocol_candidate
status: frozen
canonical: false
layer: philosophy_bridge
epistemic_layer: evidence
claim_mode: evidence
date: 2026-08-04
version: v0_1
protocol_state: preregistered_frozen
epistemic_status: candidate
procedural_state: preregistered_frozen
freeze_scope: "v0.1 rule (section 2), exclusions (section 3), six audit tests (section 4), falsification plan (section 6)"
independent_validation: none
binding_scope: forcing_ch_evidence_dossiers_after_merge
strategy_amendment: false
binding_strategy: Philosophy/Papers/Mathematical_Reachability_and_Problem_Individuation_Strategy.md@strategy_note_v0_7
motivated_by: Philosophy/Papers/Forcing_CH_Evidence/D05_C5op_Goedel_to_Cohen_Audit.md
---

# Method Individuation Protocol v0.1

**What this is.** A preregistered, non-canonical operating rule for individuating methods (`M_t`) inside the forcing–CH evidence project.

**What this is not.** Not a strategy amendment. Not a v0.8. Not a canonical definition. Not a modification of any D05 verdict. Not an independently validated rule.

## 0. Status, scope and locks

Two statuses are tracked separately and must not be conflated. Procedural freezing is what makes the falsification round a test; it confers no evidential standing whatever.

| Field | Value |
|---|---|
| Canonical | **false** — this file may not be cited as a definition source for `M_t` |
| **Epistemic status** | **candidate** — motivated by the D05 case, **not independently validated**; §5.2 records why the D05 application cannot validate it |
| **Procedural state** | **preregistered, frozen** — frozen for the falsification round upon merge |
| **Freeze scope** | the v0.1 rule (§2), the exclusions (§3), the six audit tests (§4), and the falsification plan (§6) |
| Strategy amendment | **false** — `strategy_note_v0_7` remains frozen and unmodified; this confers no v0.8 eligibility by itself |
| Binding scope | forcing–CH evidence dossiers authored **after** this file is merged |
| Retroactive force | **none** — no merged dossier's verdict is reopened by it |

Frozen here means *fixed against outcome-driven revision*, not *established*. A frozen candidate is still a candidate.

> **SCOPE LOCK**
>
> This protocol changes no verdict. `EVD-D05-0001` remains **qualified**; `EVD-D04-0002` remains **unresolved**. It issues no institutionalization, H/N/S, CH-local regime, global update-regime, C2, calibration-control or SRT verdict. It does not modify `strategy_note_v0_7`, the staged manuscript, any canonical SRT file, any equation, or any symbol table. It introduces **no new formal symbol**.

## 1. Purpose

The merged D05 audit established that C5-op, stated in frozen §4.6 as a condition on the generation relation `(b,m) ⤳ o`, is applied to an `M_t` that frozen §3.3 and §5.2 characterize only extensionally — as the set of methods implementable for the problem, and as the restriction of the global repertoire to the problem. Neither section individuates "method."

That gap is not decorative. In the D05 case it decides a registered candidate: `D05-T02` preserves C5-op at one granularity and fails at another. It also propagates further than the D05 verdict. Frozen §12 and §19 both carry the rule *"两个控制案例无法区分：停止并重构判据"* — if the two controls cannot be distinguished, stop and rebuild the criterion. Whether that rule can even be evaluated depends on the unfixed granularity. A proof-goal individuation cannot secure the required distinction — under it, any two relative-consistency proofs preserve C5-op with respect to each other, so there is a serious risk that a result innovation and forcing would not be separable by the criterion at all. That is a structural risk, not an adjudicated outcome: **no control case has yet been selected or adjudicated**, and this protocol asserts no control result in advance of §6.

This protocol resolves the operational question — how a dossier should individuate a method when applying C5-op — **without** changing the frozen strategy, and it does so before the controls are selected, since frozen §7.6 requires those to be chosen only after the technical-history archive is complete. Fixing the individuation after control selection would invite the mirror image of the circularity the D05 correction removed: controls chosen to fit a granularity.

The protocol must block two failure modes symmetrically:

1. **Too coarse** — proof-goal individuation, under which any two relative-consistency proofs count as the same method, C5-op becomes inert, and no innovation type is discriminable.
2. **Too fine** — individuation by every intermediate object, under which any construction introducing a new intermediate object counts as a new method, and Control A (an important new result inside a mature regime, expected to *preserve* C5-op) fails in the opposite direction.

## 2. The candidate rule

> **Characteristic generative resource, plus load-bearing test.**
>
> A later method `m'` counts as a **distinct operation candidate** relative to an earlier repertoire `M_t` only when all five conditions hold:
>
> 1. **Resource or role condition.** `m'` introduces a characteristic generative resource, or reorganizes an existing one into a different functional operation role.
> 2. **Relation-membership condition.** That resource or role is part of the *documented* background–operation–output generation relation `(b,m') ⤳ o` — not part of its exposition, motivation, or later rational reconstruction.
> 3. **Load-bearing condition.** Removing the resource, or replacing it by resources available in the earlier repertoire, **destroys** the target generation relation — rather than merely changing its notation, efficiency, proof length, convenience, or presentation.
> 4. **No-substitute condition.** No historically admissible, type-correct earlier substitute preserves the same generative function.
> 5. **Representation-neutrality condition.** The distinction survives representation-neutrality checks: it is not an artifact of the formalism in which either side is written.

Failing any one condition, `m'` is **not** a distinct operation candidate, and C5-op is not thereby shown to fail.

Satisfying all five makes `m'` a distinct operation **candidate** only. Under frozen §5.3 and §4.6, that is operation-level novelty at most; it is not institutionalization, and it is not regime innovation.

## 3. Required exclusions

Each is stated as a prohibition on inference. None may be weakened by a dossier without re-opening this protocol.

1. **Same proof goal does not imply same method.** Two constructions establishing the same type of statement — relative consistency, independence, model existence — are not thereby the same method. Proof-goal identity is not method identity.
2. **A new theorem or output does not imply a new method.** An output difference between two stages is what any theorem-adding history produces. It becomes evidence about `M_t` only when paired with a documented obstruction on the operation side.
3. **A new intermediate object does not by itself imply a new method.** Constructions routinely introduce new auxiliary objects. Only an object that passes the load-bearing test (§4.3) bears on individuation.
4. **Different notation or formal presentation does not imply a new method.** Rewriting a construction in a different formalism is a change of representation, not of generative resource.
5. **Greater efficiency, elegance, generality, or influence does not by itself imply a new method.** None of these is a property of the generation relation. Influence and uptake belong to the institutionalization burden (`H`, `N`, `S`), which is separate and conjunctive.
6. **Later reformulations may belong to one method family** when their characteristic generative role is preserved across the reformulation. Membership in a family must be *shown*, not assumed from mathematical interderivability.
7. **Historical unavailability cannot be inferred solely from absence of a modern formulation.** That a construction is not stated in later vocabulary is a fact about the record's presentation, not about what the earlier repertoire could implement.

Exclusions 1 and 3 are the two guards named in §1. Exclusion 1 blocks the coarse failure mode; exclusion 3 blocks the fine one. A dossier that invokes one and ignores the other has not applied this protocol.

## 4. Required audit tests

A dossier applying this protocol runs all six and records the outcome of each, including the ones that do not decide the case.

### 4.1 Historical-availability test

Is the earlier candidate operation documented as available in the earlier stage's own record, on that stage's own terms? Availability is established from the historical record, not from what is mathematically derivable in hindsight. Absence of a later formulation is not absence of the operation (exclusion 7); presence of a later reconstruction is not presence at the earlier stage.

### 4.2 Functional-role test

What role does the component play *inside* the generation relation? A component that determines the output, or on which the relation's central lemma is stated, holds a generative role. A component that organizes the presentation, motivates the construction, or anticipates that an output could exist does not. Anticipating an output is a fact about response-role structure (`R_t`), not about `M_t`, and belongs to a different criterion.

### 4.3 Load-bearing removal/replacement test

Remove the candidate resource, or replace it by resources drawn from the earlier repertoire, and ask what remains.

- If what remains is the same relation in weaker, slower, longer or uglier form — **not load-bearing**.
- If what remains no longer determines the target output, or leaves the relation's central lemma without a term to be stated about — **load-bearing**.

The test is destruction versus degradation. Degradation is the null result.

### 4.4 Conservative-substitution test

Does any historically admissible, type-correct earlier operation preserve the same generative *function*, as opposed to the same goal or the same shape? Composition is not substitution: showing that the later operation consumes the earlier operation's output demonstrates ordering, not reproduction, and counts against substitution rather than for it.

### 4.5 Representation-invariance test

Would the individuation verdict change if either side were rewritten in a different admissible formalism? If yes, the distinction is an artifact of presentation and fails condition 5. Two directions must both be checked: notational similarity must not be inflated into method identity, and notational difference must not be inflated into method distinctness.

### 4.6 Granularity sanity test

Run both bounds explicitly and record both.

- **Coarseness bound.** Under the individuation used, would two constructions that share only a proof goal come out identical? If yes, the individuation is too coarse and C5-op is inert.
- **Fineness bound.** Under the individuation used, would a new result inside a mature regime — introducing new intermediate objects but no new characteristic generative resource — come out as a new method? If yes, the individuation is too fine and Control A fails in the reverse direction.

A dossier must state where its case sits between these bounds, not merely assert that it sits between them.

## 5. Retrospective application to D05 — consistency check only

**Status of this section.** A consistency check, and nothing stronger. The protocol was *motivated by* the D05 case; applying it back to that case therefore cannot confirm it. See §5.2.

### 5.1 Candidate by candidate

| Candidate | Protocol reading | Merged D05 outcome | Consistent? |
|---|---|---|---|
| `D05-T01` inner-model predecessor | Conditions 1–4 met on the Cohen side: the externally constructed, ground-non-definable complete sequence determines `N` and is the term the truth lemma is stated on (§4.2, §4.3); the earlier repertoire's generative resource is definability over the preceding level within the base, which does not preserve the same generative function (§4.4). | fails to preserve | yes |
| `D05-T02` relative-consistency proof type | Exclusion 1 applies directly: shared proof goal does not establish method identity, so the identity mapping on the proof-goal type does not by itself preserve `M_t`. The granularity sanity test (§4.6) flags the candidate at the **coarseness bound**. | **qualified / granularity-dependent** | yes — see §5.3 |
| `D05-T03` missing opposite direction | Fails the functional-role test (§4.2): the record offered is a response form, not a component with a generative role in `(b,m) ⤳ o`. No `m_G` is available to test, which is why the registry tuple was unfillable on the operation side. | inadmissible on type grounds | yes |
| `D05-T04` generalized continuation | Fails the conservative-substitution test (§4.4): the Cohen operation consumes the earlier output and adjoins a resource outside the earlier repertoire, which is ordering, not reproduction. Ranked-hierarchy similarity fails condition 5 as a ground for identity, since the ramified language was later eliminated and so was not the carried-forward component. | fails to preserve | yes |
| `D05-T05` model-existence apparatus | Passes the historical-availability test (§4.1) — the apparatus is documented — but fails the functional-role test on the background side: it does not deliver transitivity or standardness, which the target premise requires. | fails to preserve; blocks background independently | yes |

### 5.2 What this check does and does not establish

Recorded explicitly, as required:

- `D05-T02` **preserves a coarse proof-goal type.** That much is a real feature of the record, not an error, and this protocol does not deny it.
- `D05-T02` **does not preserve the finer event-level generation relation**, because the extension `N` — the object the axioms are verified in, the object `not-CH` is established in, and the object the truth lemma is about — has no image under it.
- **The protocol candidate explains the distinction**: exclusion 1 blocks the inference from shared proof goal to shared method, and the load-bearing test (§4.3) locates the operative difference at the generative resource rather than at the proof goal. The two facts above are not in tension; they are statements at two different granularities, and the protocol says which one C5-op ranges over.
- **This application is not independent validation.** The protocol was formulated in response to the D05 case. A rule tested only on the case that motivated it has been fitted, not tested. Its evidential standing depends entirely on the falsification plan in §6.

### 5.3 One flag carried forward

Exclusion 6 permits later reformulations to belong to one method family when the characteristic generative role is preserved. It must **not** yet be applied to merge Cohen's ramified construction with the unramified partial-order/generic-filter form or with the Boolean-valued form: `EVD-D03-0010` keeps cross-formulation relations qualified and formulation-specific, and this protocol does not upgrade it. Any future family-membership claim across those formulations is a separate obligation requiring its own evidence.

## 6. Preregistered falsification plan

The protocol is registered **now**, before the cases that could falsify it are selected, so that outcomes can count against it.

It must later be tested against all four:

1. **At least one independently selected Control A candidate** — a result innovation inside a mature, stable method regime. Expected under frozen §7.5: C5-op **preserved**. Selection must follow frozen §7.6, from the technical-history archive, not by impression and not by fit to this protocol.
2. **At least one independently selected Control B candidate** — a local technical innovation with no conservative predecessor that nonetheless fails to become infrastructure. Expected under frozen §7.6: C5-op **fails**, `Inst` **fails**.
3. **Multiple representations of forcing** — the ramified 1963 construction, the unramified partial-order/generic-filter form, and the Boolean-valued form, run through the representation-invariance test (§4.5) to check that the individuation verdict is stable across formalism.
4. **At least one case in which a new result introduces new intermediate objects but no new characteristic generative resource** — the direct test of the fineness bound (§4.6) and of exclusion 3. If the protocol calls such a case a new method, the protocol is too fine.

### 6.1 No retrospective tuning

Control outcomes **may falsify or qualify** this protocol. They **must not** be used to adjust the protocol so that the preregistered three-case matrix succeeds.

Concretely, the following are prohibited:

- amending the rule, the exclusions, or the tests after seeing a control outcome, in order to move that control to the expected side;
- selecting or re-selecting a control case because it behaves as the matrix predicts under this protocol;
- treating "the calibration works under this individuation" as evidence *for* the individuation — that is the circularity the D05 correction removed, and re-importing it here would void the protocol's preregistration.

If a control falsifies the protocol, the correct response is to record the falsification and revise the protocol as a **new version** with its own preregistration, not to patch v0.1 in place.

## 7. Decision gate for a minimal v0.8

- **Passing the §6 tests makes a minimal v0.8 integration *eligible*, not automatic.** Eligibility is a precondition for proposing an amendment to frozen §3.3 / §5.2; the decision to open v0.8 remains an author decision, taken separately.
- **Failure to distinguish result innovation, local-technical innovation and regime innovation triggers the existing stop-and-reconstruct rule** in frozen §12 and §19 — *两个控制案例无法区分：停止并重构判据*. This protocol does not create that rule, weaken it, or exempt itself from it.
- **Until this gate is passed, `strategy_note_v0_7` remains frozen.** No dossier may cite this protocol as if it were a strategy amendment, and no dossier may treat `M_t` as canonically individuated.
- **No D06 institutionalization verdict may be finalized until the target operation or method family is individuated under this protocol.** `H`, `N` and `S` are predicated of an operation; without a fixed individuation, the object of those three claims is not determined, and a conjunctive verdict about it would be unstatable.

## 8. Freeze status of this file

**This protocol is frozen for the falsification round upon merge.** The freeze takes effect before D06 adjudication and before Control A / Control B selection under frozen §7.6, which is what makes §6 a test rather than a fitting exercise.

**Freeze scope:** the rule (§2), the exclusions (§3), the six audit tests (§4), and the falsification plan (§6).

Three consequences, stated as prohibitions:

1. **v0.1 may not be edited in response to outcomes.** No D06 result, no Control A or Control B outcome, and no forcing-representation finding may be answered by amending this file. That includes amendments presented as clarification, tightening, or scope repair.
2. **Failure requires a separately versioned v0.2 with a new preregistration.** If the protocol is falsified or qualified by §6, the response is a new file at a new version, carrying its own preregistration and its own freeze, with the falsifying outcome recorded. v0.1 stays on the record as falsified rather than being repaired into agreement.
3. **Editorial corrections require an explicit non-substantive erratum record.** Typographical fixes, broken links, and formatting repairs that do not affect the rule, the exclusions, the tests or the falsification plan are permitted, but each must be recorded as a dated non-substantive erratum stating what changed and why it does not touch the frozen scope. An unrecorded edit to a frozen file is a protocol violation regardless of how small it is.

Freezing is procedural only. It fixes the rule against outcome-driven revision; it does not make the rule correct, and it is not independent validation. The epistemic status remains **candidate** (§0, §5.2).

Nothing in this file establishes that forcing was novel, important, inheritable, non-local, scaffold-forming, or institutionalized. It establishes only how a dossier should decide whether two operations are the same operation.
