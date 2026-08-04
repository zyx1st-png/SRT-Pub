---
id: SRT-PAPER-FORCING-CH-EVIDENCE-D03-COHEN-EVENT
title: "D03 — Cohen-Event Technical Baseline"
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
---

# D03 — Cohen-Event Technical Baseline

**Dossier state:** first-pass source adjudication; not submission-ready

**Stage window used here:** Cohen's published 1963–1964 construction; later formulations are marked retrospective

**Primary obligations:** `EVD-D03-0009`, `EVD-D03-0010`, `EVD-D03-0013`

## Verdict snapshot

| Evidence obligation | Verdict | Narrow result |
|---|---|---|
| `EVD-D03-0009` | **supported** | The original Cohen-stage ground model, conditions, ramified forcing relation, externally constructed complete sequence, extension `N`, and CH-relevant output are verified from Parts I and II. |
| `EVD-D03-0010` | **qualified** | The historical succession from Cohen's ramified construction to Boolean-valued models and the partial-order/generic-filter formulation is documented, and the modern forms can be related technically. A single unrestricted interchangeability or exact identity claim is not established. |
| `EVD-D03-0013` | **supported** | The assumptions behind the original semantic model construction, modern countable-transitive-model presentations, generic-filter existence, and the separate finite-fragment consistency argument are explicitly distinguished. |

## 1. Scope and stage lock

This dossier fixes the technical record for the **Cohen event**. It does not establish operation novelty relative to the strongest Gödel-stage reconstruction, adjudicate C5-op, document heritability, non-locality, or scaffold formation, establish the institutionalization of forcing, adjudicate C2, or support a global claim about the set-theoretic update regime [EVD-D03-0009; EVD-D03-0010; EVD-D03-0013].

The stage distinction is substantive. Cohen's 1963–1964 papers use a ramified language, finite conditions, a recursively defined forcing relation, and a complete sequence constructed outside a countable standard model. The now-familiar package `M`, `P`, `G`, and `M[G]` is a later normalization and generalization. Boolean-valued models are a further reformulation. The later formulations clarify Cohen's method, but their notation, assumptions, and proof organization must not be retrojected into the event as if they were Cohen's literal 1963 presentation [COHEN1963-CH-I, pp. 1144–1147; KANAMORI2008-COHEN, pp. 359–361, 369–370].

> **SCOPE LOCK**
>
> This dossier establishes a technical event-level baseline only. It supplies neither a C5-op verdict nor an institutionalization verdict. In particular, even a later finding that C5-op fails would not by itself establish regime innovation.

## 2. Source register and verification record

### 2.1 Primary Cohen sources

| Stable key | Type and source-level status | Verified metadata | Exact locations used | Use and limit |
|---|---|---|---|---|
| `COHEN1963-CH-I` | primary; `VERIFIED` against complete publisher page images | Paul J. Cohen, “The Independence of the Continuum Hypothesis,” *Proceedings of the National Academy of Sciences* 50(6), 1963, 1143–1148. DOI: [10.1073/pnas.50.6.1143](https://doi.org/10.1073/pnas.50.6.1143). | p. 1143, opening, Theorem 1, and base theory; pp. 1143–1144, construction sketch and model premise; pp. 1144–1145, ramified terms and conditions; p. 1146, Definitions 6–7; p. 1147, Lemmas 2–5 and Definition 8; p. 1148, transition to Part II. | Original operation, semantic setup, forcing relation, complete sequence, truth lemma, and announced output. Part I defers the model and axiom verification to Part II. |
| `COHEN1964-CH-II` | primary; `VERIFIED` against complete publisher page images | Paul J. Cohen, “The Independence of the Continuum Hypothesis, II,” *Proceedings of the National Academy of Sciences* 51(1), 1964, 105–110. DOI: [10.1073/pnas.51.1.105](https://doi.org/10.1073/pnas.51.1.105). | p. 105, Theorem 2; pp. 106–108, Lemmas 6–17 and ZF-axiom verification; p. 108, Lemmas 18–20; p. 109, Lemmas 21–22 and model-existence discussion; p. 110, finite-fragment relative-consistency reduction and publication note. | Completes the model proof, cardinal preservation, AC, and the negative-CH result; then separates the stronger model premise from a finite-fragment consistency transformation. It does not alone prove the Gödel direction. |

### 2.2 Historical and modern technical reconstructions

| Stable key | Type and source-level status | Verified metadata | Exact locations used | Use and limit |
|---|---|---|---|---|
| `KANAMORI2008-COHEN` | peer-reviewed historical/technical retrospective; `VERIFIED` against author-hosted full text | Akihiro Kanamori, “Cohen and Set Theory,” *The Bulletin of Symbolic Logic* 14(3), 2008, 351–378. DOI: [10.2178/bsl/1231081371](https://doi.org/10.2178/bsl/1231081371). | pp. 359–361, Cohen's original model and five-part forcing scheme; p. 364, semantic and syntactic consistency routes; p. 369, Boolean-valued reformulation; p. 370, unramified partial-order/generic-filter form and early-1970s stabilization. | Historical bridge between the original and later formulations. Later stabilized practice is not evidence that Cohen used its mature notation in 1963. |
| `MOORE2019-FORCING` | expert technical exposition; `VERIFIED` against arXiv v1 full text | Justin Tatch Moore, “The Method of Forcing,” arXiv:1902.03235v1, 2019. | §§3 and 6, pp. 5–12; §7, pp. 13–14; §8, pp. 15–17. | Modern definitions of forcing, genericity, names, `M[G]`, the forcing theorem, Cohen forcing, c.c.c. preservation, and a negative-CH argument. This is a retrospective technical normalization, not a primary historical source. |
| `GUNTHER-PAGANO-SANCHEZ2020-ISABELLE` | peer-reviewed technical formalization; `VERIFIED` against full text | Emmanuel Gunther, Miguel Pagano, and Pedro Sánchez Terraf, “Formalization of Forcing in Isabelle/ZF,” in *Automated Reasoning*, IJCAR 2020, 221–235. arXiv:2001.09715v2. DOI: [10.1007/978-3-030-51054-1_13](https://doi.org/10.1007/978-3-030-51054-1_13). | abstract and §§1–3, pp. 1–4; §4, p. 5; §8, p. 13; §9, p. 14. | Explicit audit of a countable-transitive-model formalization, its generic-filter premise, external reasoning, and its inability to provide a finitary consistency proof. The paper had not yet formalized CH independence, so it cannot verify Cohen's exact CH output. |
| `HAN-VANDOORN2020-CH` | peer-reviewed technical formalization; `VERIFIED` against full conference text | Jesse Michael Han and Floris van Doorn, “A Formal Proof of the Independence of the Continuum Hypothesis,” in *CPP 2020*, 2020, 1–14. DOI: [10.1145/3372885.3373826](https://doi.org/10.1145/3372885.3373826). | abstract and §1, pp. 1–2; §1.1, pp. 2–3. | Boolean-valued proof of both directions; documents its relation to Cohen, Scott–Solovay, and Shoenfield and explains why this formalization bypasses countable-transitive-model and generic-filter machinery. It does not show that all presentations are historically or metatheoretically interchangeable. |

## 3. Cohen's original 1963–1964 construction

### 3.1 Background theory and model premise

Cohen begins Part I with a version of Zermelo–Fraenkel set theory without Choice and with Regularity, which he abbreviates `Z-F` [COHEN1963-CH-I, p. 1143]. Theorem 1 announces four relative-consistency results. The CH-relevant item is part 3: Choice holds while `aleph_1` differs from `2^{aleph_0}` [COHEN1963-CH-I, p. 1143]. Only that item is developed in the two PNAS papers.

For the semantic construction, Cohen fixes a countable standard model `M` of `Z-F`, takes it to satisfy `V=L`, and works with a presentation whose membership relation is the actual membership relation on a transitive set-like domain [COHEN1963-CH-I, p. 1144; KANAMORI2008-COHEN, pp. 359–360]. In modern language this is normally described as starting with a countable transitive model. That phrase is an expository normalization; the exact primary-source wording remains “countable model” and “standard model.”

This premise is stronger than bare syntactic consistency. Cohen recognizes the gap and does not use the semantic construction by itself as the final reduction from `Con(Z-F)` [COHEN1964-CH-II, pp. 109–110; KANAMORI2008-COHEN, pp. 360, 364].

### 3.2 Generic objects, ramified terms, and finite conditions

Cohen fixes a cardinal `δ` in `M` and seeks distinct subsets `a_α` of the integers indexed below `δ` [COHEN1963-CH-I, pp. 1143–1144]. These objects are not first selected as members of `M`; they are to be determined by requirements imposed from outside `M`. Conditions are finite sets of elementary assertions of the form that an integer belongs, or does not belong, to one of the `a_α` [COHEN1963-CH-I, p. 1145, Definition 5]. A stronger condition carries more information.

To describe sets in the intended extension, Cohen develops a ramified hierarchy of terms `F_α` and a ramified language [COHEN1963-CH-I, pp. 1144–1145, Definitions 2–4]. The relation between conditions and formulas is then defined recursively. Definition 6 supplies the central forcing clause for limited statements, and Definition 7 extends it to unlimited statements [COHEN1963-CH-I, p. 1146].

The historically exact operation therefore cannot be reduced to the modern slogan “choose a poset and take `M[G]`.” Its verified components are:

1. a countable standard ground model `M`;
2. new intended subsets `a_α` of the integers;
3. a ramified language and ranked terms for the extension;
4. finite conditions giving partial information about the `a_α`;
5. a forcing relation defined in the ground model;
6. an externally constructed complete sequence of increasingly informative conditions;
7. an interpreted extension `N` whose truth is connected to forcing.

Kanamori independently reconstructs these same components and stresses that the complete sequence is obtained by a Baire-category argument outside `M` [KANAMORI2008-COHEN, pp. 360–361].

### 3.3 Complete sequence, extension, and truth lemma

Cohen enumerates the relevant statements and ordinals because `M` is countable, then constructs a complete sequence of conditions `P_0,P_1,...` [COHEN1963-CH-I, p. 1147, Definition 8]. He explicitly notes that the sequence is not definable in `M`. The sequence determines the new subsets `a_α` and the interpretation structure `N` [COHEN1963-CH-I, p. 1147].

Lemma 5 is the event-stage truth lemma: a statement is true in `N` exactly when some condition in the complete sequence forces it [COHEN1963-CH-I, p. 1147]. This gives the bridge from the ground-model forcing relation to truth in the extension. Part I then defers the proof that `N` satisfies the base axioms and the desired cardinal statement [COHEN1963-CH-I, p. 1148].

### 3.4 Exact output of Parts I and II

Part II opens with Theorem 2, asserting that `N` is a model of `Z-F`, and verifies the axioms through the forcing machinery [COHEN1964-CH-II, pp. 105–108]. The forcing relation is formalizable in the original model, which is essential to the axiom checks [COHEN1964-CH-II, p. 106, Lemmas 6–7].

The cardinal argument then establishes the required preservation and size facts. Lemma 18 preserves the relevant cardinals, Lemma 19 establishes Choice in `N`, and Lemma 20 establishes that `aleph_1` is strictly below the continuum in `N` [COHEN1964-CH-II, p. 108]. This proves Theorem 1, part 3. Further lemmas refine the possible value of the continuum under additional choices in the construction [COHEN1964-CH-II, p. 109, Lemmas 21–22].

The narrow event-stage output is therefore:

\[
N \models ZF + AC + \neg CH,
\]

under the semantic model assumptions used to construct `N`, followed by a separate formal reduction yielding the corresponding relative-consistency consequence. It is not a proof of `not-CH` from `ZFC`, an assertion that `not-CH` is true in an unqualified intended universe, or a proof of both independence directions by Cohen alone.

Combining Cohen's negative-CH consistency result with Gödel's earlier positive-CH consistency result yields the familiar two-sided independence conclusion, under the appropriate consistency assumptions. The combination is a cross-stage inference; it must not be attributed to either one-directional construction alone [COHEN1963-CH-I, p. 1143; HAN-VANDOORN2020-CH, §1, p. 1].

## 4. Semantic construction and formal relative consistency

### 4.1 The stronger model-existence route

On p. 109 of Part II, Cohen considers a strengthened theory asserting the existence of a set model `M` of `Z-F`. Under the additional standard-model properties used in the construction, the semantic argument produces `N` satisfying the target theory [COHEN1964-CH-II, p. 109]. This is a model-existence route. It must not be compressed into the bare implication `Con(ZF) -> a countable transitive model of ZFC exists`.

Modern countable-transitive-model presentations make the same dependency transparent. Moore's semantic forcing theorem assumes a countable transitive model `M` of `ZFC`, a forcing `Q` in `M`, and an `M`-generic filter `G`; it then relates ground-model forcing to truth in `M[G]` [MOORE2019-FORCING, §6, p. 12, Theorem 6.10]. Moore immediately notes that full set models of `ZFC` cannot be proved to exist in `ZFC` itself if `ZFC` is consistent and that finite fragments are needed for a rigorous relative-consistency treatment [MOORE2019-FORCING, §6, p. 12, Remark 6.11].

The Isabelle/ZF formalization makes the stronger assumption explicit: it assumes a countable transitive model of `ZFC`, uses countability to obtain generic filters, and states that countability can instead be replaced by directly assuming the appropriate generic-filter existence [GUNTHER-PAGANO-SANCHEZ2020-ISABELLE, pp. 1–3]. Its authors also state that this approach does not supply a finitary consistency proof [GUNTHER-PAGANO-SANCHEZ2020-ISABELLE, p. 3].

### 4.2 Cohen's finite-fragment discharge

Cohen does not leave the consistency theorem dependent on the full standard-model premise. On p. 110 he enumerates the axioms, works with sufficiently large finite fragments, obtains countable standard models for those finite fragments, and argues that a contradiction in a finite target fragment can be transformed into a contradiction in a finite source fragment [COHEN1964-CH-II, p. 110]. He says that the only special property of the models used in this reduction is transitivity.

The resulting separation is mandatory:

| Route | Premise used in the presentation | Output | Prohibited inference |
|---|---|---|---|
| event-stage semantic construction | a suitable countable standard/transitive model `M` and an externally constructed complete sequence | a concrete extension `N` satisfying the target axioms | bare `Con(ZFC)` proves that a countable transitive model of `ZFC` exists |
| modern generic-extension semantics | a countable transitive `M`, `P in M`, and an external `M`-generic `G` | `M[G]` and the forcing theorem | `G` is internally constructed in `M`, or the semantic premise is free |
| Cohen's finite-fragment reduction | metatheoretic reasoning over finite fragments and contradiction transformations | relative consistency/non-provability consequence | a single full countable transitive model is derived from consistency |
| Boolean-valued syntactic route | complete Boolean algebra and Boolean-valued soundness/model construction in a stated metatheory | relative-consistency and independence results without generic-filter semantics | historical identity with Cohen's 1963 ramified construction |

This distinction is not cosmetic. It prevents a stronger model-existence assumption from being hidden inside the published relative-consistency theorem [EVD-D03-0013].

## 5. Relation among the three principal formulations

### 5.1 Cohen's ramified construction

Cohen's original forcing scheme is built around ramified terms, finite information about the intended generic subsets, a forcing relation internalized in `M`, and a complete sequence assembled externally [COHEN1963-CH-I, pp. 1144–1147]. It is the primary evidence for what happened at the Cohen event.

### 5.2 Partial orders, generic filters, and `M[G]`

In the mature generic-filter presentation, a forcing notion is a partial order `P`; a filter `G` is generic over `M` when it meets the appropriate dense requirements coded in `M`; names in `M` are interpreted by `G`; and the resulting structure is written `M[G]` [MOORE2019-FORCING, §§3, 6, pp. 5–6, 10–12]. Cohen forcing is represented by finite partial functions, ordered by extension, and the union of the generic filter supplies the generic object [MOORE2019-FORCING, §7, p. 14].

Kanamori attributes the general partial-order/generic-filter presentation and elimination of the ramified language to Shoenfield's unramified forcing, and reports that this form became standard practice after the later reformulation period [KANAMORI2008-COHEN, p. 370]. It is therefore legitimate to use `M,P,G,M[G]` as a checked modern reconstruction of the mathematical operation, but not as Cohen's literal event-stage notation.

For the CH application, the modern forcing `C_I` consists of finite partial functions from `I x omega` to `2`. It satisfies the countable chain condition, preserves the relevant cardinals, and with an index set of size `aleph_2` forces the continuum to have size at least `aleph_2`, hence forces `not-CH` [MOORE2019-FORCING, §§7–8, pp. 14–17]. Moore calls this the essence of Cohen's proof. The phrase marks a modern structural reconstruction, not a line-by-line identification with the ramified PNAS argument.

### 5.3 Boolean-valued models

Kanamori reports that Scott and Solovay recast forcing in terms of Boolean-valued models. This replaced Cohen's ramified language by a direct rank induction and made a countable standard ground model unnecessary for the syntactic relative-consistency argument [KANAMORI2008-COHEN, p. 369].

Han and van Doorn likewise describe Boolean-valued models as a Scott–Solovay simplification of Cohen's method and the partial-order form as a Shoenfield development. They state that the two later approaches have essentially the same mathematical content while explaining that their Boolean-valued formalization bypasses Löwenheim–Skolem, Mostowski collapse, countable transitive models, and generic-filter considerations [HAN-VANDOORN2020-CH, §1, pp. 1–2]. Their paper proves both CH directions within that formalized framework.

The checked relation is therefore one of mathematically connected reformulations with different proof organization and metatheoretic interfaces. The current dossier does not establish a representation-independent equivalence theorem covering every historical and modern variant, every ground model, and every consistency-strength formulation. That broader identity claim remains unavailable [EVD-D03-0010].

### 5.4 Comparison table

| Feature | Cohen 1963–1964 | Modern partial-order/generic-filter form | Boolean-valued form |
|---|---|---|---|
| Historical status | event-stage primary construction | later unramified/stabilized formulation | later Scott–Solovay reformulation |
| Conditions | finite membership/non-membership information about `a_α` | elements of a forcing partial order; for Cohen forcing, finite partial functions | elements/values in a complete Boolean algebra |
| Names | ramified terms `F_α` | recursively defined `P`-names | Boolean-valued sets/names |
| Semantic object | complete sequence determines the `a_α` and `N` | external `M`-generic filter `G` determines `M[G]` | truth values in a complete Boolean algebra; no generic filter required for the cited formalization |
| Countability use | enumerates requirements and constructs the complete sequence outside `M` | supplies an `M`-generic filter by meeting countably many dense requirements | bypassed in the cited Boolean-valued proof |
| CH output used here | `N models ZF+AC+not-CH` | suitable Cohen forcing forces `not-CH` while c.c.c. preserves cardinals | formal models for both CH and `not-CH` in the cited work |
| Safe relation claim | original forcing construction | retrospective normalization/generalization | connected reformulation with different metatheoretic interface |

## 6. Assumption and type audit

### 6.1 Ground model

`M` is a set-sized model used by an external metatheory in the cited semantic presentations. Transitivity permits actual membership and ordinals to be handled uniformly between the ambient metatheory and `M`, subject to the usual absoluteness limits [COHEN1963-CH-I, p. 1144; GUNTHER-PAGANO-SANCHEZ2020-ISABELLE, pp. 2–4]. `M` is not identified with the intended universe without qualification.

### 6.2 Generic filter or complete sequence

In Cohen's original paper, the complete sequence is constructed outside `M` and is explicitly not definable in `M` [COHEN1963-CH-I, p. 1147]. In the modern presentation, an `M`-generic `G` meets the dense requirements belonging to `M`; countability of `M` supplies the external enumeration used to construct such a filter [MOORE2019-FORCING, §3, pp. 5–6; §6, p. 12]. A nontrivial generic filter is not thereby a member of the ground model.

### 6.3 Generic extension

`M[G]` is formed by interpreting the names in `M` using `G`, and contains both the check-name copies of the members of `M` and `G` itself [MOORE2019-FORCING, §6, pp. 10–12]. This is the modern semantic counterpart of Cohen's interpreted `N`; it is not his literal notation or proof organization.

### 6.4 External metatheory

Assertions that `M` is countable, that an external enumeration covers its requirements, that `G` exists, or that `M[G]` satisfies a formula are made in an ambient metatheory. Cohen's internal definability of forcing does not erase this external level [COHEN1963-CH-I, pp. 1146–1147; COHEN1964-CH-II, p. 106]. Conversely, the finite-fragment proof transformation is not the construction of one full external countable transitive model [COHEN1964-CH-II, p. 110].

### 6.5 Claim-type matrix

| Claim | Type | Status here | Boundary |
|---|---|---|---|
| `N models ZF+AC+not-CH` | model-relative truth | verified for Cohen's construction under its stated semantic assumptions | does not assert intended-universe truth |
| `P forces not-CH` | forcing-language/syntactic claim relative to a stated forcing setup | verified in modern reconstructions and connected to Cohen's argument | does not by itself state which external model exists |
| `Con(ZFC) -> Con(ZFC+not-CH)` | relative-consistency claim | supported by Cohen's finite-fragment reduction, in modern normalization | does not produce a countable transitive model of full `ZFC` from bare consistency |
| `ZFC does not prove CH`, conditional on `Con(ZFC)` | syntactic non-provability consequence | supported | is one direction of independence only |
| CH is independent of `ZFC` | two-sided syntactic claim | available only by combining the Cohen and Gödel directions | not Cohen's negative direction alone |
| forcing reconstructed the CH research regime | historical research-regime claim | not adjudicated here | requires later C5-op and independent institutionalization evidence |

## 7. Evidence-obligation adjudication

### 7.1 `EVD-D03-0009`

**Exact obligation:** Cohen-stage ground model, forcing notion, generic extension, external metatheory, and exact output.

- **Supporting sources:** `COHEN1963-CH-I` (`VERIFIED`, pp. 1143–1148); `COHEN1964-CH-II` (`VERIFIED`, pp. 105–110); `KANAMORI2008-COHEN` (`VERIFIED`, pp. 359–361); `MOORE2019-FORCING` (`VERIFIED`, §§6–8, pp. 10–17, modern normalization only).
- **Counter-sources / qualifying records:** Kanamori and Moore show that the now-standard partial-order/generic-filter notation is later than Cohen's ramified presentation. The modern vocabulary can clarify the operation but cannot serve as sole evidence for the event-stage form.
- **Verified paraphrase:** Starting from a suitable countable standard model, Cohen uses finite conditions, ramified terms, an internally definable forcing relation, and an externally constructed complete sequence to build `N`; Part II verifies `ZF`, Choice, cardinal preservation, and `not-CH`, then gives a finite-fragment route to relative consistency.
- **Rationale:** The primary papers cover every requested component and distinguish the semantic construction from the final consistency reduction. The historical reconstruction confirms the operation's original architecture.
- **Verdict:** **supported**.
- **Mandatory limit:** No operation-novelty, institutionalization, C5-op, C2, or research-regime verdict follows.

### 7.2 `EVD-D03-0010`

**Exact obligation:** checked relation among forcing, Boolean-valued formulations, generic extensions, and the reverse-independence result without treating them as interchangeable by assertion.

- **Supporting sources:** `KANAMORI2008-COHEN` (`VERIFIED`, pp. 369–370); `MOORE2019-FORCING` (`VERIFIED`, §§3, 5–8, pp. 5–17); `HAN-VANDOORN2020-CH` (`VERIFIED`, abstract and §1, pp. 1–2); `COHEN1963-CH-I` and `COHEN1964-CH-II` (`VERIFIED`, full CH argument).
- **Counter-sources / qualifying records:** The formulations differ historically, semantically, and metatheoretically. The generic-extension presentation assumes an external generic in its semantic form; the cited Boolean-valued proof avoids that interface; Cohen's original proof uses neither mature package literally. “Essentially the same mathematical content” in one modern formalization is not a proof of unrestricted identity across all variants.
- **Verified paraphrase:** Boolean-valued models and the generic-filter approach are later reformulations of forcing that recover the relevant independence mathematics through different technical interfaces. Cohen supplies the negative-CH direction; Gödel's earlier result supplies the other direction.
- **Rationale:** The lineage, core technical relation, and division of independence directions are documented. A comprehensive equivalence theorem and a formulation-neutral assumption comparison have not been completed for every relevant variant.
- **Verdict:** **qualified**.
- **Mandatory fallback:** The manuscript may describe a documented family of related formulations and state their exact local connections. It must not call them historically identical, unconditionally interchangeable, or assumption-free.

### 7.3 `EVD-D03-0013`

**Exact obligation:** assumption audit for generic filters, model existence, ground models, and external metatheory.

- **Supporting sources:** `COHEN1963-CH-I` (`VERIFIED`, pp. 1144, 1147); `COHEN1964-CH-II` (`VERIFIED`, pp. 106, 109–110); `KANAMORI2008-COHEN` (`VERIFIED`, pp. 359–361, 364); `MOORE2019-FORCING` (`VERIFIED`, §6, pp. 10–12); `GUNTHER-PAGANO-SANCHEZ2020-ISABELLE` (`VERIFIED`, pp. 1–4); `HAN-VANDOORN2020-CH` (`VERIFIED`, §1, pp. 1–2).
- **Counter-sources / qualifying records:** The Isabelle result deliberately assumes a countable transitive model and explicitly does not provide the finitary consistency proof; it verifies the semantics of that approach, not a derivation of its premise from `Con(ZFC)`. The Boolean-valued formalization avoids this particular premise but works in a different metatheoretic framework.
- **Verified paraphrase:** Countability is used externally to meet the ground model's requirements and obtain a generic object; transitivity supports absoluteness and uniform membership; neither follows from bare consistency in the required form. Cohen's finite-fragment transformation supplies the relative-consistency result without inferring a full countable transitive model.
- **Rationale:** Primary and modern sources explicitly expose every assumption under audit and identify two different routes from forcing machinery to consistency claims.
- **Verdict:** **supported**.
- **Mandatory limit:** This verdict audits assumptions; it does not establish that one formulation is foundationally privileged or that their historical roles coincide.

## 8. Claim-to-evidence ledger

| Ledger claim | Evidence ID | Sources and exact locations | Adjudicated status | Downstream permission |
|---|---|---|---|---|
| Cohen's event-stage construction begins with a suitable countable standard model and uses a ramified language, finite conditions, a forcing relation, and an external complete sequence. | `EVD-D03-0009` | `COHEN1963-CH-I`, pp. 1144–1147; `KANAMORI2008-COHEN`, pp. 359–361. | supported | D05 may use this as the later event-stage operation record. |
| The extension `N` satisfies the base theory plus Choice and `not-CH`. | `EVD-D03-0009` | `COHEN1964-CH-II`, pp. 105–109, especially Lemmas 18–20. | supported | The manuscript may state Cohen's negative-CH model output with assumptions. |
| Cohen's published consistency conclusion is not left dependent on a full countable-transitive-model premise. | `EVD-D03-0009`; `EVD-D03-0013` | `COHEN1964-CH-II`, pp. 109–110; `KANAMORI2008-COHEN`, p. 364. | supported | Formal-constraint prose may distinguish semantic construction from finite-fragment reduction. |
| Bare consistency licenses the existence of a countable transitive model of full `ZFC`. | `EVD-D03-0013` | `COHEN1964-CH-II`, p. 110; `MOORE2019-FORCING`, p. 12; `GUNTHER-PAGANO-SANCHEZ2020-ISABELLE`, pp. 2–3. | defeated | This inference is prohibited. |
| An `M`-generic object is obtained externally by using countability to meet the requirements coded in `M`. | `EVD-D03-0013` | `COHEN1963-CH-I`, p. 1147; `KANAMORI2008-COHEN`, p. 361; `MOORE2019-FORCING`, pp. 5–6, 12. | supported | Technical prose may state the external construction and must name the countability premise. |
| `M,P,G,M[G]` is Cohen's literal 1963 formalism. | `EVD-D03-0010` | contrast between `COHEN1963-CH-I`, pp. 1144–1147, and `KANAMORI2008-COHEN`, pp. 369–370. | defeated | The notation may appear only as an explicitly modern reconstruction. |
| Boolean-valued and generic-filter formulations are historically identical and unconditionally interchangeable. | `EVD-D03-0010` | `KANAMORI2008-COHEN`, pp. 369–370; `HAN-VANDOORN2020-CH`, pp. 1–2. | defeated in this unrestricted form | Use formulation-specific claims and assumptions. |
| The later formulations are mathematically connected reformulations of Cohen's method. | `EVD-D03-0010` | `KANAMORI2008-COHEN`, pp. 369–370; `HAN-VANDOORN2020-CH`, pp. 1–2; `MOORE2019-FORCING`, pp. 14–17. | qualified | A bounded lineage and technical-reconstruction claim is available. |
| Cohen's result alone establishes full independence of CH. | `EVD-D03-0010` | `COHEN1963-CH-I`, p. 1143; `HAN-VANDOORN2020-CH`, p. 1. | defeated | Attribute independence to the combined Gödel and Cohen directions. |
| The Cohen event was already the institutionalized forcing regime. | `EVD-D03-0009`; `EVD-D03-0010` | stage boundary in §1; later stabilization in `KANAMORI2008-COHEN`, pp. 369–370. | unresolved and blocked | D06 must independently establish `H`, `N`, and `S`. |

## 9. Unresolved decisive questions

1. Which exact theorem-level translations preserve the operation–output relation between Cohen's ramified construction, partial-order/generic-filter forcing, and Boolean-valued models, and under which metatheories?
2. Which features of Cohen's use of `V=L` were essential to his published proof, and which were removed by immediate or later revisions?
3. How should the finite-fragment semantic reduction on p. 110 be compared proof-theoretically with later fully syntactic and Boolean-valued consistency proofs?
4. Which contemporaneous readers treated Cohen's complete-sequence construction, forcing relation, or model extension as the central novelty?
5. What is the strongest historically admissible Gödel-stage operation repertoire against which the Cohen operation should be tested in D05?
6. Can D05 exhibit a type-correct conservative translation that reproduces Cohen's background–operation–output relation without importing post-Cohen forcing language into the Gödel stage?
7. When did the partial-order/generic-filter formulation become teachable and reusable across researchers, and which evidence belongs to institutionalization rather than to the event itself?
8. Which later Boolean-valued and unramified presentations preserve the exact assumption profile of the event-stage construction, and which replace it?
9. What historically documented response role did the negative-CH result acquire before forcing was institutionalized?

> **TODO — submission-stage technical closure**
>
> - Add a standard-monograph cross-check for Cohen forcing, the forcing theorem, and the finite-fragment relative-consistency reduction, with exact edition and pages.
> - Verify the full primary text and exact locations of Shoenfield's “Unramified Forcing” before attributing any theorem or formulation directly to that paper; current historical attribution rests on Kanamori.
> - Add a theorem-level comparison of regular-open/Boolean completions and generic extensions before strengthening `EVD-D03-0010`.
> - Check whether Cohen's 1966 monograph changes the assumptions or proof organization relevant to `EVD-D03-0013`; bibliographic metadata alone is insufficient.
> - Build a separate contemporary-reception dossier before using any claim about what the 1963–1964 community regarded as the decisive operation.

## 10. Downstream consequences

### What D05 may now use

D05 may use the verified event-stage tuple: suitable countable standard ground model; ramified term system; finite information conditions; internally defined forcing relation; externally built complete sequence; interpreted extension `N`; and output `ZF+AC+not-CH` with a separate finite-fragment relative-consistency discharge [EVD-D03-0009; EVD-D03-0013].

D05 must compare that record to the strongest historically admissible Gödel-stage operation repertoire. It may not make novelty trivial by translating Cohen into mature forcing notation while denying equivalent retrospective reconstruction to the comparator.

### What remains unavailable

This dossier provides no verdict on:

- C5-op preservation or failure;
- heritability, non-locality, or scaffold formation;
- institutionalized forcing;
- CH-local research-regime reconstruction;
- a global reconstruction of set theory's update regime;
- C2 response-role non-conservativity;
- strong semantic re-individuation;
- the SRT bridge.

The qualified `EVD-D03-0010` verdict permits only local, formulation-specific relation claims. If later proof-level work does not close the remaining equivalence gaps, the manuscript must retain those distinctions rather than collapsing the formulations.

> **DOWNGRADE, WITHDRAWAL, AND SRT FALLBACK LOCK**
>
> If C5-op cannot be established, the paper stops. If C5-op is established but heritability, non-locality, and scaffold formation are not, the result cannot be called regime innovation. CH-local evidence cannot support a global set-theoretic update-regime claim. Strong semantic re-individuation remains conditional on completed C2 evidence relative to the Gödel stage; if C2 is incomplete or preserved, the weak title and weak abstract remain mandatory. If the SRT bridge fails its preregistered test, Level B or Level C applies. This dossier changes none of the frozen `strategy_note_v0_7` rules.

The supported verdicts in this dossier establish a technical event-stage baseline and an assumption audit. They do not establish that forcing reconstructed the CH research regime; that remains the paper's weak default thesis to be tested by later, separately adjudicated evidence.
