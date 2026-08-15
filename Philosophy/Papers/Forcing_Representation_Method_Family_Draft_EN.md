---
id: SRT-PAPER-FORCING-REPRESENTATION-METHOD-FAMILY-DRAFT-20260814
title: "Same Forcing, Different Operation? What Is Preserved Across Ramified, Generic-Filter, and Boolean-Valued Representations"
type: paper_draft
status: draft
version: v0_1
canonical: false
layer: philosophy_bridge
epistemic_layer: evidence
claim_mode: evidence
date: 2026-08-14
draft_stage: architecture_and_source_backed_core
submission_ready: false
language: English
target_length_words: 7500-8500
provisional_citation_style: Chicago author-date
paper_plan: Philosophy/Papers/Forcing_Representation_Method_Family_Paper_Plan.md
primary_evidence:
  - Philosophy/Papers/Forcing_CH_Evidence/D03_Cohen_Event_Baseline.md
  - Philosophy/Papers/Forcing_CH_Evidence/D05b_Forcing_Representation_and_Method_Family_Audit.md
---

# Same Forcing, Different Operation?

## What Is Preserved Across Ramified, Generic-Filter, and Boolean-Valued Representations

> **Working-draft notice.** This version fixes the article's question, distinction set, component matrix, endpoint analysis, and source-backed core. It is not submission-ready. Bracketed source checks are internal instructions, not manuscript prose. The draft does not modify the forcing–CH flagship manuscript, its protocol, or its control archive.

## Abstract

Are two mathematical methods the same when one can be reformulated in the language of the other? The history of forcing makes the question unusually precise. Cohen's 1963–1964 construction uses ramified terms, finite conditions, a recursively defined forcing relation, an externally constructed complete sequence, and an interpreted model `N`. The later generic-filter presentation instead uses a forcing poset `P`, `P`-names, an `M`-generic filter `G`, a modern forcing relation, and `M[G]`. Boolean-valued forcing reorganizes the method again around a complete Boolean algebra and algebra-valued truth. I argue that these are not literally one operation token, although they exhibit qualified continuity at the level of a forcing method family. The argument separates three questions: identity of historical operation tokens, preservation of load-bearing component roles, and continuity of a method family. A componentwise audit shows strong forward role preservation from Cohen's construction to generic-filter forcing but only presentation-dependent reverse reconstruction. A second audit distinguishes three Boolean endpoints: direct Boolean validity, an ordinary two-valued quotient, and a generic extension obtained through an appropriate generic ultrafilter or equivalent bridge. Equal independence results do not collapse these endpoints. The case therefore supports neither output-based identity nor syntax-based fragmentation. What survives representation change is a structured relation among partial information, truth determination, interpretation, and realization; what does not survive is the literal historical operation and, in direct Boolean proofs, the complete extension-generating endpoint.

**Keywords:** forcing; Boolean-valued models; generic filters; proof identity; mathematical methods; philosophy of mathematical practice; Cohen

## 中文摘要（内部工作版）

当一种数学方法可以被另一套语言重新表述时，它们是否仍是同一个方法？forcing 的历史使这个问题可以被精确拆解。Cohen 在 1963–1964 年的构造使用分层项、有限条件、递归定义的 forcing 关系、在可数模型外部构造的 complete sequence，以及由此解释得到的模型 `N`。后来的 generic-filter 表述改用偏序 `P`、`P`-names、`M`-generic filter `G`、现代 forcing 关系和 `M[G]`；Boolean-valued forcing 又把方法重组为完备布尔代数上的真值赋值。本文区分三个层次：历史操作 token 的同一性、承重组件角色的保存，以及较高层方法家族的连续性。逐组件核验显示，从 Cohen 构造到 generic-filter forcing 存在强的正向角色映射，但反向重建依赖可数性、枚举、编码和指定表述，不能恢复 Cohen 的字面语法与唯一序列。进一步地，Boolean-valued forcing 必须区分直接的布尔语义有效性、普通二值商模型，以及通过适当 generic ultrafilter 或等价桥接得到的 generic extension。三者即使导向同一个独立性结论，也不是同一个完整操作。本文据此主张一种受限定的方法家族连续性：被保存的是部分信息、真值决定、名称解释与实现之间的结构关系；没有被保存的是字面历史操作，而直接 Boolean 证明还缺少完整的 extension-generating endpoint。

**关键词：** forcing；Boolean-valued models；generic filters；证明同一性；数学方法；数学实践哲学；Cohen

---

## 1. Introduction

The word *forcing* now covers several presentations that are close enough to be taught as one method and different enough to organize proofs in visibly different ways. Cohen's first published construction proceeds through a ramified language, finite conditions, a forcing relation defined for that language, a complete sequence built outside a countable model, and an interpreted model `N` (Cohen 1963, 1144–47; Cohen 1964, 105–10). The mature presentation begins with a partial order `P`, defines `P`-names and a forcing relation, chooses an `M`-generic filter `G`, and forms `M[G]` (Shoenfield 1971, 359–65; Jech 2003, 201–18). The Boolean-valued presentation assigns truth values in a complete Boolean algebra and may either pass to an ordinary quotient or stop with an algebra-valued semantic proof (Scott 1967, 95–111).

Historians and set theorists are right to describe these as developments or reformulations of forcing. That description, however, leaves an identity question open. Does a reformulation preserve the same mathematical operation, replace it with another operation in the same method family, or merely reach the same theorem by a related route? The three answers are not equivalent. A method can survive a change in notation; it can also fail to survive a change in its load-bearing intermediate objects or endpoint. Conversely, counting every new syntax or data structure as a new method makes mathematical continuity impossible to state.

Forcing is a good test case because the available sources permit a componentwise answer. Cohen specifies his components. Shoenfield explicitly removes ramification and supplies an early generic-filter and name-based construction. Scott explains both what his Boolean assignment owes to Cohen and why Boolean values can be used without immediately passing to a two-valued model. Jech supplies the exact modern theorems connecting posets, Boolean completions, generic filters, ultrafilters, quotients, names, and extensions. One therefore need not decide method identity by impressionistic similarity.

The central claim of this paper is deliberately qualified. Cohen's ramified construction, generic-filter forcing, and Boolean-valued forcing are not one historically or procedurally identical operation token. They nevertheless belong to one bounded method family insofar as they preserve a characteristic relation among four roles: ordered partial information, ground-definable truth determination, interpretation of prospective extension objects, and realization or a stated semantic substitute. The phrase *or a stated semantic substitute* is essential. Boolean-valued semantics can prove a relative-consistency result directly, without exhibiting a generic ultrafilter or an ordinary extension. In that use it preserves a theorem-producing semantic role, not the whole operation of generating `M[G]`. The extension-generating role is recovered only when a suitable quotient or generic-ultrafilter step is added.

This thesis rejects two simple tests. The first identifies methods by their conclusion: if two proofs establish the same independence result, they count as the same method. Antos's practice-based account is useful here because it records that countable-transitive-model and Boolean-valued approaches deliver the same consistency and independence results while organizing forcing through different kinds of models (Antos 2024, §3.3). Result-equivalence is mathematically important, but it does not answer whether the same operation was performed. Rav's broader claim that the epistemic content of a proof exceeds the theorem it establishes provides a methodological reason not to make theorem output the identity criterion (Rav 1999). `[[SOURCE CHECK: verify the precise pages in Rav before this sentence becomes final prose.]]`

The second simple test identifies methods by their literal syntax: a sequence is not a filter, a ramified term is not a `P`-name, and a Boolean value is not a forcing condition; therefore there must be three methods. That test is too fine. Shoenfield's construction shows that ramification can be eliminated without losing the interpretation and truth roles. Jech's Boolean-completion results show that, for set forcing under the appropriate hypotheses, generic filters and generic ultrafilters determine one another and yield the same generic extension. Literal object identity is not required for preservation of a mathematical role.

The argument proceeds in four steps. Section 2 separates operation-token identity, component-role preservation, and method-family continuity. Section 3 reconstructs Cohen's published operation without retrojecting later notation. Section 4 gives a component-role matrix from Cohen's construction to generic-filter forcing and states the assumptions under which a reverse reconstruction is possible. Section 5 distinguishes direct Boolean validity, an ordinary two-valued quotient, and a generic extension. Section 6 then gives the bounded family verdict and addresses the two simple identity tests.

---

## 2. Three Questions Hidden in “the Same Method”

### 2.1 Operation-token identity

An **operation token** is a historically and mathematically specified performance: it has input objects, intermediate objects, an order of operations, a truth or satisfaction interface, background assumptions, and an endpoint. Two descriptions concern the same operation token only if they preserve those items strongly enough to identify the performance, not merely its theorem.

On this standard, Cohen's 1963 construction is not literally the modern `M,P,G,M[G]` construction. The point is chronological before it is philosophical. Cohen's published definitions use a ramified hierarchy of terms, finite positive and negative assertions, a forcing relation divided according to his language, and a complete sequence of conditions (Cohen 1963, 1144–47). The complete sequence is externally constructed by enumerating the relevant requirements made available by countability; it determines the interpretation of the new sets and the model `N` (Cohen 1963, 1147). Part II verifies the axioms and the failure of CH in `N`, then separates this semantic construction from the finite-fragment consistency argument (Cohen 1964, 105–10). The mature generic-filter package is a later normalization and generalization, not hidden notation in the original paper (Kanamori 2008, 359–61, 370).

Token identity is intentionally strict. It prevents a retrospective translation from erasing the historical problem Cohen actually solved and the resources with which he solved it. But strict token identity cannot be the only notion in play. Mathematical methods routinely survive changes in representation, coding, and abstraction. A useful analysis needs a second level.

### 2.2 Component-role preservation

A **component role** is the load-bearing function an object or relation performs in an operation. The relevant question is typed: which later object bears the earlier role, and which structural facts make the substitution work? Calling two items “analogous” is not enough. The substitution must preserve the relation between input, intermediate construction, truth determination, and output.

For the forcing case, five roles are central:

1. partial conditions approximate information about the intended new objects;
2. a coherent completion meets the ground-model requirements and determines the generic information;
3. terms or names are ground-coded placeholders for objects in the intended extension;
4. a ground-definable forcing or Boolean-truth relation connects partial information to formulas;
5. interpretation or quotient produces the relevant semantic endpoint.

These roles permit a controlled comparison between objects of different mathematical types. A sequence and a filter need not be identical to perform the same coherence role. A ramified term and a `P`-name need not have the same syntax to support rank-founded interpretation. At the same time, role language does not make differences disappear. If a presentation omits generic realization and stops at Boolean validity, it does not produce an ordinary extension merely because it proves the same relative-consistency theorem.

Role preservation is directional. An earlier component may have a clear later image even when the later object does not canonically determine the earlier syntax. This asymmetry is decisive in the transition from Cohen's complete sequence to an arbitrary generic filter and from ramified terms to modern names.

### 2.3 Method-family continuity

A **method family** is a bounded class of operation types whose characteristic roles and load-bearing relations survive admissible representation changes. Family continuity is weaker than token identity and stronger than output equivalence. It requires:

- a non-empty shared operational core;
- typed forward translations for the load-bearing components;
- a statement of what each representation eliminates or replaces;
- preservation of the relation between truth determination and the relevant endpoint;
- and explicit restrictions on any reverse translation.

This paper does not offer these conditions as a universal analysis of mathematical methods. They are an evidential standard for this case. Their purpose is to block two opposed errors: an output criterion that puts any proofs of the same theorem in one family, and a syntax criterion that splits a family whenever one representational bearer changes.

The forcing sources also impose a further restriction. “Same family” cannot mean “interchangeable in every proof architecture.” A Boolean-valued consistency argument without a generic ultrafilter has a different endpoint from an operation that forms `M[G]`. Family continuity must therefore be indexed to the preserved role. It can be strong at the truth-determination level while qualified at the full extension-generation level.

---

## 3. Cohen's Published Operation

### 3.1 The five components

Cohen's Part I begins from a suitable countable standard model and introduces prospective new subsets through a ramified hierarchy of terms (Cohen 1963, 1143–45). Conditions are finite collections of assertions about the intended new sets. Their order is informational: stronger conditions extend the finite commitments already made. Cohen then defines forcing recursively for the ramified language (Cohen 1963, 1146, Definitions 6–7).

The complete sequence is not an incidental enumeration. It is the object through which the finitely specified information becomes jointly decisive. Cohen enumerates statements and ordinal requirements and constructs a sequence that meets the resulting demands; he notes that the sequence is not definable in the ground model (Cohen 1963, 1147, Definition 8). The terms are interpreted using this sequence, yielding `N`. Cohen's Lemma 5 connects truth in `N` to forcing by some condition in the complete sequence (Cohen 1963, 1147).

Part II confirms that this endpoint bears the promised mathematical load. It verifies the axioms for `N`, proves the relevant cardinal facts and Choice, and derives the failure of CH (Cohen 1964, 105–09). The final page then discharges relative consistency through finite fragments rather than treating the existence of the original full model as a consequence of bare consistency (Cohen 1964, 110). This separation matters because later presentations vary not only in notation but also in the metamathematical route by which a consistency statement is obtained.

The historical operation may therefore be represented as:

```text
ramified terms + finite conditions
→ original recursive forcing relation
→ externally constructed complete sequence
→ interpretation of terms
→ ordinary two-valued N
→ separate finite-fragment consistency discharge.
```

This display is a reconstruction of the published roles, not a claim that Cohen stated an abstract pipeline. Its purpose is to identify the items that a later representation must preserve or replace.

### 3.2 What can be removed without removing forcing?

The components are not equally load-bearing at the family level. Removing the forcing relation leaves no ground-defined bridge from finite information to truth in the interpreted model. Removing every coherent completion leaves no object that jointly realizes the requirements and determines the new sets. Those roles must reappear in any full extension-generating reformulation.

The ramified hierarchy is different. It is historically central to Cohen's token, but Shoenfield's explicit aim is to develop forcing without ramification (Shoenfield 1971, 357). He uses finite-map conditions and a generic filter, recursively interprets ground-model codes as names, constructs `M[G]`, and establishes the relevant definability, extension, and truth results (Shoenfield 1971, 359–65). The removal of ramification changes the representation-specific operation. It does not destroy the interpretation or truth-determination roles.

This is the first reason the token/family distinction is needed. If every historical component defines family identity, Shoenfield's unramified forcing is a different method simply because it succeeds in eliminating an apparatus that the later theory shows to be dispensable. If only theorem output matters, by contrast, one cannot explain why the forcing relation and coherent generic completion are more central than the eliminated ramified syntax. A role audit provides the intermediate grain.

---

## 4. From Complete Sequences to Generic Filters

### 4.1 Component-role matrix

The following matrix states both directions. “Reverse” never means historical reversal. It asks whether later mathematical data determine Cohen's literal component or only permit a Cohen-style reconstruction after additional choices.

| Cohen component | Later image | Preserved role | Eliminated or replaced? | Forward mapping | Reverse mapping | Exact sources |
|---|---|---|---|---|---|---|
| complete sequence | an `M`-generic filter `G ⊆ P`; under a chosen countable presentation, a descending sequence generating a filter | coherent accumulation of finite information; meeting decision and witness requirements; determination of the generic object; support for the truth lemma | the distinguished enumeration is replaced by a filter meeting all relevant dense sets | Cohen's sequence meets an enumerated requirement family; in the later form those requirements are organized as dense sets and their coherent realization is a generic filter | **qualified and non-canonical:** an arbitrary `G` has no distinguished Cohen sequence; reconstruction needs external countability or a countable requirement family plus a chosen enumeration | Cohen 1963, 1147; Kanamori 2008, 360–61; Shoenfield 1971, 359–60; Jech 2003, 202–03 |
| ramified terms | ground-model `P`-names interpreted by `G` | ground-coded placeholders for prospective extension elements; rank-founded interpretation; generation of all elements of the extension | the ramified syntax and indexed language are eliminated | Shoenfield's name recursion and Jech's `P`-name interpretation preserve the interpreted-value role | **qualified and presentation-dependent:** no source-backed lossless inverse recovers Cohen's literal syntax; one may choose a ramified coding whose values agree | Cohen 1963, 1144–45, 1147; Shoenfield 1971, 357, 361–62; Jech 2003, 203, 215–18; Kanamori 2008, 370 |
| finite conditions | conditions in a forcing poset `P`; for Cohen forcing, finite partial functions or an isomorphic finite-information presentation | ordered partial approximation; compatibility and density organize possible joint extensions | Cohen's specific assertion syntax is abstracted | strong for the corresponding Cohen forcing and then generalized to arbitrary posets | **strong only after the forcing is fixed:** arbitrary posets do not recover Cohen's literal condition tokens; dense-equivalent presentations may differ | Cohen 1963, 1145; Shoenfield 1971, 359–60; Jech 2003, 201–02; Kanamori 2008, 361, 370 |
| Cohen's forcing relation | modern relation on `P`-names together with the forcing theorem | a ground-definable bridge from conditions to truth; monotonicity, decision, witness, and truth roles | the ramified limited/unlimited recursion is replaced and generalized | specializing the modern relation to Cohen forcing preserves the truth-determination role | **qualified:** reconstruction needs name/formula translation and does not recover Cohen's literal clauses | Cohen 1963, 1146–47; Shoenfield 1971, 362–64; Jech 2003, 204–05, 215; Kanamori 2008, 361, 370 |
| interpreted `N` | generic extension `M[G]` | ordinary two-valued extension retaining the ground, containing the generic object, interpreting every name, and satisfying the target theory | the historical presentation is reorganized rather than erased | fixed Cohen forcing plus a designated `G` and term/name translation yields the corresponding extension content | **coded or isomorphic, not literal in general:** a bare `M[G]` does not determine the historical `M`, `P`, `G`, coding, or `N` | Cohen 1963, 1147; Cohen 1964, 105–10; Shoenfield 1971, 361–65; Jech 2003, 203–04, 216–18; Kanamori 2008, 361 |

### 4.2 Why complete sequence is not simply another name for generic filter

The forward relation is strong. Cohen's complete sequence is coherent, accumulates finite information, and meets an enumerated family of formula-decision and interpretation requirements. In the mature presentation an `M`-generic filter meets the dense sets coded in `M`, and the forcing theorem recovers truth from a condition in the filter. Both bear the role of making ground-defined partial information jointly decisive for the interpreted extension.

The reverse relation is weaker. Filters are not sequences, and an arbitrary generic filter has no distinguished enumeration. If the relevant dense family is externally countable, one may enumerate it and choose a descending sequence inside `G` that successively meets its members. Directedness supplies common strengthenings and genericity ensures intersection with each dense requirement. The upward closure of the chosen sequence generates the needed filter behavior. But a different enumeration or a different series of choices gives a different sequence. What is recovered is a Cohen-style presentation of the generic role, not Cohen's literal complete sequence.

The qualification is not a defect in the forward translation. It identifies the level at which continuity holds. Coherence and requirement-meeting survive; a distinguished enumeration does not. Any claim of exact operation identity that includes the sequence token is therefore false. Any claim that no significant structure survives the change from sequence to filter is also false.

### 4.3 Names preserve interpretation, not syntax

The same pattern recurs with ramified terms. Cohen's terms are ranked and interpreted to obtain the elements of `N`. Modern `P`-names are also ground-coded and rank-founded, and every element of `M[G]` arises by interpreting a name with `G` (Jech 2003, 203–04). Shoenfield's unramified construction is especially probative because the elimination is the point of the presentation, not an accidental change of symbols (Shoenfield 1971, 357, 361–62).

The role map is therefore robust: term or name syntax in the ground supports recursive interpretation into the extension. Yet later names do not carry enough information to recover Cohen's literal ramified hierarchy, indexed quantifiers, or exact formula presentation. A translation can be fixed for the corresponding Cohen forcing, and interpreted values can be made to agree. That is a coding result, not syntax-level identity.

### 4.4 Four forcing-relation records

Talk of “the forcing relation” can conceal four records:

1. Cohen's Definitions 6–7 recurse through his ramified language, and Lemmas 2–5 establish the associated decision, monotonicity, and truth behavior (Cohen 1963, 1146–47).
2. Shoenfield first gives a semantic relation and then a recursively defined modified relation, proving definability, extension, and truth lemmas while explaining the relation to Cohen's concept (Shoenfield 1971, 362–64).
3. The mature recursive relation is formulated for `P`-names and arbitrary forcing posets, with the standard connective, quantifier, monotonicity, decision, and witness properties (Jech 2003, 204–05, 215).
4. The forcing theorem or truth lemma connects the relation to ordinary truth after generic interpretation; it is not the same mathematical object as the recursive definition it validates.

These records preserve a load-bearing relation without being one transhistorical definition. The modern theorem should not be retrojected into Cohen's pages as if he had stated it in the later language. Conversely, changed clauses do not by themselves show that truth-determination has been replaced.

### 4.5 Exact assumptions for reverse reconstruction

The source-backed reverse is a composition, not a total inverse. It requires:

1. an externally countable ground model or at least a countable family of relevant dense, decision, and witness requirements;
2. Cohen forcing, or a fixed isomorphic or dense-equivalent presentation with an explicit order convention;
3. a chosen enumeration of the requirements;
4. a chosen translation between later names/formulas and a ramified presentation;
5. designated data `M`, `P`, and `G`, rather than only an abstract extension;
6. any coding or collapse used to identify the interpreted structures.

Under these assumptions one can pass from a designated Cohen-forcing generic `G` to a chosen requirement-meeting sequence in `G`, choose a ramified coding, translate the forcing clauses, and obtain a Cohen-style presentation of the corresponding extension. One cannot pass invariantly from an arbitrary `G` to a unique sequence, from arbitrary names to Cohen's literal syntax, or from a bare `M[G]` to the historical `N`.

This asymmetry fixes the first half of the paper's verdict: the generic-filter formulation preserves every load-bearing Cohen role in the forward direction, but it is a different representation-specific operation, and its reverse relation to Cohen's token is conditional and non-canonical.

---

## 5. Boolean-Valued Forcing and Three Endpoints

### 5.1 Completeness and algebra-valued truth

Scott's 1967 presentation changes more than the notation for a generic object. A complete Boolean algebra supplies values for formulas, and completeness is what makes arbitrary joins and meets available for the quantifier clauses (Scott 1967, 95–105). The Boolean-valued universe is then full enough for the required witness behavior, and the axioms receive top value. Scott applies the construction directly to the continuum problem, calculating that the relevant CH sentence has Boolean value `0` in the constructed model (Scott 1967, 106–08).

At this stage no ordinary two-valued extension has been formed. The proof works because algebra-valued semantics respects deduction: a statement with the appropriate nonzero or top Boolean support can yield a consistency consequence without choosing a generic ultrafilter. Hamkins later gives a concise modern account of this endpoint, explicitly observing that the Boolean-valued model can be developed without generic filters or dense sets for the purpose of relative-consistency reasoning (Hamkins 2012, 422–23).

This is a genuine theorem-producing method. Calling it weaker does not mean mathematically inferior. It means only that its endpoint is weaker than the particular operation “form an ordinary generic extension of the ground.”

### 5.2 Endpoint A: direct Boolean validity

The first endpoint is a Boolean-valued semantic proof:

```text
complete Boolean algebra B
→ Boolean-valued names and recursive truth values
→ ZFC has value 1 and the target sentence has the required Boolean support
→ relative-consistency or independence consequence.
```

No generic ultrafilter is part of this operation token. The output is not an ordinary two-valued model and not yet a generic extension. This is the exact sense in which Boolean-valued forcing can avoid the countable-model and generic-filter route used in standard semantic presentations. Scott's closing discussion does not claim that every ordinary well-founded model can thereby be produced without further assumptions; instead it distinguishes the Boolean assignment from the later homomorphism or quotient step (Scott 1967, 108–11).

### 5.3 Endpoint B: an ordinary two-valued quotient

A Boolean-valued structure can be quotiented by a suitable ultrafilter so that Boolean truth becomes ordinary two-valued satisfaction. But two-valuedness alone does not identify the quotient with the intended external generic extension. Hamkins emphasizes that an arbitrary ultrafilter on the Boolean algebra yields a classical quotient structure while warning that, for a non-generic ultrafilter, quotient equivalence need not coincide with ordinary valuation by that ultrafilter (Hamkins 2012, 424). Such a quotient may also be non-well-founded or nonstandard from the external perspective.

Scott's account makes a related historical point. A homomorphism onto the two-element algebra converts Boolean values to `0` or `1`, and Cohen's complete set of conditions performs the corresponding selecting role. On Scott's comparison, Cohen effectively performs this selection early, whereas the Boolean route can perform it at the end or omit it when Boolean validity is enough (Scott 1967, 110–11). The statement is a claim about order and endpoint, not a claim that every homomorphism is generic or that every quotient is the same model as Cohen's `N`.

### 5.4 Endpoint C: the generic extension

The full bridge to generic-extension forcing requires the modern theorem chain. Let `P` be a forcing poset in the ground model. Pass to its separative quotient and Boolean completion `B(P)`. The poset embeds densely into the complete Boolean algebra (Jech 2003, 208–10). A `P`-generic filter corresponds to an appropriate generic ultrafilter on `B(P)`, and the two are definable from one another in the relevant setting; their interpreted extensions agree (Jech 2003, 210–11). Boolean values define the forcing relation, and after generic interpretation ordinary truth is recovered by membership of the Boolean value in the ultrafilter (Jech 2003, 215–18).

The bridge can be displayed as:

```text
forcing poset P
→ separative quotient and complete Boolean algebra B(P)
→ corresponding generic ultrafilter H
→ quotient / interpretation of Boolean-valued names
→ ordinary model M[H] = M[G].
```

This chain supports a strong same-family claim between generic-filter and Boolean-valued forcing at the full extension-generating level—when the generic realization is included. It does not turn the direct Boolean-validity operation into an extension token that it does not perform.

### 5.5 Endpoint table

| Endpoint | Immediate output | Needs generic ultrafilter? | Ordinary two-valued model? | Generic extension of the designated ground? |
|---|---|---:|---:|---:|
| A. Direct Boolean validity | Boolean-valued semantic proof and consistency consequence | no | no | no |
| B. Ordinary quotient | classical quotient structure | not necessarily | yes | not automatically |
| C. Generic realization | `M[G]` through the corresponding generic ultrafilter/quotient | yes, or an equivalent generic bridge | yes | yes, under the stated set-forcing assumptions |

The endpoint distinction blocks a common shortcut. The fact that A, B, and C can support the same independence conclusion does not show that they execute the same complete operation. Theorem output underdetermines both intermediate structure and semantic endpoint.

---

## 6. What Is Preserved?

### 6.1 A bounded family core

The source record supports the following bounded core:

1. a structured space of partial information, represented by finite conditions, a forcing poset, or dense elements of a Boolean completion;
2. a ground-definable relation that assigns truth-support to formulas, represented by forcing or Boolean values;
3. ground-coded prospective objects, represented by ramified terms, `P`-names, or Boolean-valued names;
4. an interpretation or semantic-evaluation architecture connecting those codes and truth supports to an endpoint;
5. for the full extension operation, a coherent generic realization or equivalent quotient that recovers ordinary truth in an extension.

Ramification is not in this minimal family core, because Shoenfield removes it while preserving the extension and truth functions. A distinguished sequence is also not invariant, because the generic-filter formulation preserves requirement-meeting without preserving an enumeration. A generic realization is different: it is invariant only when the compared endpoint is an ordinary generic extension. It is absent from the weaker direct-Boolean endpoint.

The resulting family claim is therefore indexed rather than unconditional. Cohen's ramified and modern generic-filter operations share the extension-generation core, with qualified reverse reconstruction. Generic-filter and Boolean-valued operations share that core strongly when Boolean completion and generic quotient are included. A direct Boolean-validity proof shares the truth-support and theorem-producing architecture but not the completed extension operation.

### 6.2 Objection: same result, same method

One might argue that the distinctions are philosophically idle because all three presentations establish the relevant independence or relative-consistency result. On this view, a mathematical method should be individuated by what it proves, and internal route differences are merely expository.

The forcing case supplies a direct counterexample to that criterion. Endpoint A does not form an ordinary model; endpoint C does. Cohen's complete sequence depends on an external countable enumeration; the direct Boolean proof does not. Modern generic forcing interprets names by a designated `G`; Boolean validity can stop before any such object appears. These are differences in assumption profile, intermediate operation, and semantic output even when the final metatheorem agrees. Antos's account usefully confirms the practice-level coexistence of approaches delivering the same mathematical results (Antos 2024, §3.3). That coexistence is evidence for equivalence of mathematical reach, not identity of operation token.

The output criterion is also too coarse outside this case. It would classify any two proofs of the same theorem as one method, erasing precisely the mathematical content carried by proof transformations, constructions, and explanatory routes. Rav's proof-centered epistemology motivates this broader point, although the present argument needs only the forcing-specific result (Rav 1999). `[[SOURCE CHECK: supply exact pages or delete the generalization.]]`

### 6.3 Objection: different objects, different methods

The opposite objection takes the sequence/filter, term/name, and condition/Boolean-value differences as decisive. It protects historical specificity, but at the cost of making representation invariance impossible. The technical translations show why that cost is too high. Shoenfield preserves recursive interpretation and the truth lemma while eliminating ramification. Jech preserves generic extensions through separative quotient and Boolean completion and identifies forcing support with the ordering of Boolean values. These are not analogies based on shared vocabulary; they are theorem-backed substitutions.

The right conclusion is not that the intermediate objects are unimportant. Their differences determine operation-token identity and can change the proof's metamathematical route. The conclusion is that object-type difference must be tested against preserved role. If the replacement carries the same load under an exact translation, it need not split the method family. If the replacement changes the endpoint—as direct Boolean validity does—it qualifies the continuity claim.

### 6.4 Provisional verdict

The three presentations support **qualified method-family continuity**. “Qualified” records three limits:

- the historical operation tokens are different;
- the reverse map from generic-filter forcing to Cohen's literal components is non-canonical and representation-dependent;
- Boolean-valued forcing without generic realization preserves a theorem-producing semantic role, not the full extension-generating operation.

This verdict is stronger than saying that the presentations are historically related and weaker than saying that they are interchangeable. It identifies exactly what the family relation preserves and where it stops.

`[[DRAFTING GAP: Before submission, compare this three-level analysis against Moore 1987 and the method/proof-identity literature. If the distinction is already standard for this case, narrow the novelty claim to the endpoint-sensitive component audit.]]`

---

## 7. Conclusion

Forcing did not remain unchanged as it moved from Cohen's ramified construction to generic filters and Boolean-valued models. The complete sequence became a generic filter; ramified terms gave way to names; finite assertions were abstracted into forcing posets; the forcing relation was generalized; and the interpreted `N` was reorganized as `M[G]`. These changes preserve load-bearing roles in the forward direction, but they do not provide a canonical inverse to Cohen's historical syntax and sequence.

The Boolean-valued transition adds a second limit. Direct algebra-valued validity, an ordinary quotient, and a generic extension are three endpoints, not three descriptions of one output. A Boolean proof can stop before generic realization and still establish the target consistency result. When the generic-ultrafilter or equivalent quotient bridge is added, the ordinary generic extension is recovered and the same-family relation becomes technically strong.

The forcing case therefore recommends a middle grain for method identity. Same theorem output is too coarse; literal syntax is too fine. What can survive a representation change is a structured set of component roles and relations. What need not survive is a historical operation token—and, when the endpoint changes, the complete operation itself.

---

## Working References

Alama, Jesse. 2014. “Proof Identity for Mere Mortals.” arXiv:1403.0641. `[[Optional; abstract-level review only.]]`

Antos, Carolin. 2024. “Models as Fundamental Entities in Set Theory: A Naturalistic and Practice-based Approach.” *Erkenntnis* 89: 1683–1710. https://doi.org/10.1007/s10670-022-00600-3.

Bell, John L. 2005. *Set Theory: Boolean-Valued Models and Independence Proofs*. 3rd ed. Oxford: Oxford University Press. https://doi.org/10.1093/acprof:oso/9780198568520.001.0001.

Carter, Jessica. 2019. “Philosophy of Mathematical Practice—Motivations, Themes and Prospects.” *Philosophia Mathematica* 27 (1): 1–32. https://doi.org/10.1093/philmat/nkz002. `[[Field-positioning reserve; detailed review pending.]]`

Cohen, Paul J. 1963. “The Independence of the Continuum Hypothesis.” *Proceedings of the National Academy of Sciences* 50 (6): 1143–48. https://doi.org/10.1073/pnas.50.6.1143.

Cohen, Paul J. 1964. “The Independence of the Continuum Hypothesis, II.” *Proceedings of the National Academy of Sciences* 51 (1): 105–10. https://doi.org/10.1073/pnas.51.1.105.

Hamkins, Joel David. 2012. “The Set-Theoretic Multiverse.” *Review of Symbolic Logic* 5 (3): 416–49. https://doi.org/10.1017/S1755020311000359.

Han, Jesse Michael, and Floris van Doorn. 2020. “A Formal Proof of the Independence of the Continuum Hypothesis.” In *Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs*, 353–66. https://doi.org/10.1145/3372885.3373826.

Jech, Thomas. 2003. *Set Theory: The Third Millennium Edition, Revised and Expanded*. Berlin: Springer. https://doi.org/10.1007/3-540-44761-X.

Kanamori, Akihiro. 2008. “Cohen and Set Theory.” *Bulletin of Symbolic Logic* 14 (3): 351–78. https://doi.org/10.2178/bsl/1231081371.

Moore, Gregory H. 1987. “The Origins of Forcing.” In *Logic Colloquium '86*, 143–73. *Studies in Logic and the Foundations of Mathematics* 124. https://doi.org/10.1016/S0049-237X(09)70656-1. `[[Metadata and abstract verified; relevant pages pending.]]`

Moore, Justin Tatch. 2019. “The Method of Forcing.” arXiv:1902.03235.

Rav, Yehuda. 1999. “Why Do We Prove Theorems?” *Philosophia Mathematica* 7 (1): 5–41. https://doi.org/10.1093/philmat/7.1.5. `[[Metadata and abstract verified; exact load-bearing pages pending.]]`

Scott, Dana. 1967. “A Proof of the Independence of the Continuum Hypothesis.” *Mathematical Systems Theory* 1 (2): 89–111. https://doi.org/10.1007/BF01705520.

Shoenfield, J. R. 1971. “Unramified Forcing.” In *Axiomatic Set Theory*, edited by Dana Scott, 357–81. Proceedings of Symposia in Pure Mathematics 13, Part I. Providence, RI: American Mathematical Society.
