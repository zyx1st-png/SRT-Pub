---
id: SRT-PAPER-FORCING-CH-EVIDENCE-D05B-REPRESENTATION-METHOD-FAMILY
title: "D05b — Forcing Representation and Method-Family Audit"
type: evidence_dossier
status: active
canonical: false
layer: philosophy_bridge
epistemic_layer: evidence
claim_mode: evidence
date: 2026-08-05
updated: 2026-08-11
submission_ready: false
evidence_state: partially_adjudicated
binding_strategy: Philosophy/Papers/Mathematical_Reachability_and_Problem_Individuation_Strategy.md@strategy_note_v0_7
linked_manuscript: Philosophy/Papers/Forcing_CH_Research_Regime_Staged_Draft_EN.md
depends_on_dossiers:
  - Philosophy/Papers/Forcing_CH_Evidence/D03_Cohen_Event_Baseline.md
  - Philosophy/Papers/Forcing_CH_Evidence/D05_C5op_Goedel_to_Cohen_Audit.md
depends_on_protocol:
  - Philosophy/Papers/Forcing_CH_Evidence/METHOD_INDIVIDUATION_PROTOCOL_v0_1.md
---

# D05b — Forcing Representation and Method-Family Audit

**Dossier state:** first multi-representation falsification round under the frozen Method Individuation Protocol v0.1; not submission-ready

**Audit objects:** Cohen's 1963–1964 ramified construction; the later partial-order / generic-filter / generic-extension formulation; the Boolean-valued formulation

**Primary inherited obligation:** `EVD-D03-0010`

**Bounded obligations registered by this dossier:** `EVD-D05-0005`, `EVD-D05-0006`

## Verdict snapshot

| Object or obligation | Verdict | Narrow result |
|---|---|---|
| Ramified construction ↔ generic-filter / generic-extension formulation | `qualified_same_method_family` | The later formulation preserves the condition-based approximation, external generic completion, name interpretation, forcing relation, and truth-in-extension role, while eliminating the ramified term hierarchy and replacing Cohen's complete sequence by a generic filter. The mapping is technically and functionally strong but historically retrospective and not a literal identity of operations. |
| Generic-filter / generic-extension ↔ Boolean-valued formulation | `supported_same_method_family` | For set forcing, separative quotient and Boolean completion give a bidirectional route between a poset generic filter and a generic ultrafilter; the forcing relation is definable by Boolean values; and both presentations yield the same generic extension. This establishes same-family status at the representation-neutral generation level, not historical identity or identity of every proof architecture. |
| Ramified construction ↔ Boolean-valued formulation | `qualified_same_method_family` | A common generative role is recoverable through the generic-filter bridge, but the direct historical and componentwise translation is incomplete. Boolean-valued semantics removes both the ramified hierarchy and the need to organize the proof around Cohen's literal complete sequence, and it can support consistency proofs without an explicit two-valued generic extension. |
| Higher-level forcing method family | `qualified_same_method_family` | A non-empty common family exists: ordered partial information plus a ground-definable forcing/Boolean truth relation and a generic realization or equivalent quotient that determines truth in a model extension. The family claim is qualified because it preserves the characteristic generation role and extension semantics, not every historical component, metamathematical route, or proof organization. |
| `EVD-D03-0010` | **qualified — unchanged** | The new evidence supports bounded same-family judgments and an exact generic-filter/Boolean-completion equivalence, but it does not establish unrestricted interchangeability, literal historical identity, or full operation-role identity across all three forms. |
| `EVD-D05-0006` | **supported** | Without an explicit generic ultrafilter or an appropriate Boolean-algebra homomorphism and quotient, direct Boolean-valued forcing reaches Boolean validity and theorem-producing semantics, not an ordinary two-valued model or the completed generic-extension operation. The full extension role is recovered when the quotient/generic step is added; Jech's theorem chain then identifies the Boolean and poset routes with the same generic extension. |
| Method Individuation Protocol v0.1 | **qualified; not falsified** | The representation-invariance test does not force three unrelated methods, and it does not collapse all differences. It succeeds only after distinguishing a representation-specific operation token from a representation-neutral method family. The protocol therefore survives this round but exposes an unresolved level-of-individuation interface that a future v0.2 may need to state explicitly. |
| D06 target object | **provisional / qualified** | D06 should predicate `H`, `N`, and `S` of the bounded forcing method family specified in §12, not of Cohen's event token, not of every forcing notion, and not of the entire later forcing ecosystem. No `H/N/S` verdict is issued here. |

> **SCOPE LOCK**
>
> This dossier does not modify `strategy_note_v0_7`, the staged manuscript, the frozen Method Individuation Protocol v0.1, D05, any canonical SRT file, any equation, or any symbol table. It does not adjudicate `H`, `N`, `S`, institutionalization, the CH-local research regime, the global set-theoretic update regime, C2, either control case, or the SRT bridge. It does not upgrade `EVD-D05-0001`.

---

## 1. Audit question and unit of comparison

The frozen strategy uses `m` in the generation relation

\[
(b,m)\leadsto o
\]

and later predicates `H(m)`, `N(m)`, and `S(m)` of an operation. D05 established that the Cohen event contains a generation-sensitive resource not reproduced by the bounded Gödel-stage candidates, but it also recorded a granularity problem: a proof-goal description is too coarse, while individuation by every intermediate object is too fine. Method Individuation Protocol v0.1 was preregistered to control that problem through a characteristic-generative-resource and load-bearing test.

The present audit asks whether three historically and technically distinct presentations should be treated as:

1. three representations of one forcing method family;
2. several related but distinct operations;
3. or an unresolved mixture for which no non-empty family core has yet been shown.

The comparison does **not** use any of the following as a sufficient identity condition:

- proving the same relative-consistency conclusion;
- yielding a model satisfying the same sentence;
- appearing in the same modern textbook chapter;
- mathematical intertranslatability without a functional-role audit;
- historical succession;
- or shared use of the word *forcing*.

It also does not use any of the following as a sufficient difference condition:

- different notation;
- a different language of names;
- replacement of a sequence by a filter;
- replacement of a poset by its Boolean completion;
- a different order of exposition;
- or introduction of a new intermediate object.

The operative question is narrower:

> Do the representations preserve a characteristic resource and its load-bearing role in generating or semantically determining a forcing extension, or does one representation replace that operation with a different theorem-producing mechanism?

---

## 2. Source register and verification record

### 2.1 Primary sources

| Stable key | Type and source-level status | Verified metadata | Exact locations used | Use and limit |
|---|---|---|---|---|
| `COHEN1963-CH-I` | primary; `VERIFIED` in D03 against complete publisher page images | Paul J. Cohen, “The Independence of the Continuum Hypothesis,” *Proceedings of the National Academy of Sciences* 50(6), 1963, 1143–1148. DOI: 10.1073/pnas.50.6.1143. | pp. 1144–1145, Definitions 2–5; p. 1146, Definitions 6–7; p. 1147, Lemmas 2–5 and Definition 8. | Original ramified terms, finite conditions, forcing relation, complete sequence, interpreted model, and event-stage truth lemma. It does not contain the later literal package `M,P,G,M[G]`. |
| `COHEN1964-CH-II` | primary; `VERIFIED` in D03 against complete publisher page images | Paul J. Cohen, “The Independence of the Continuum Hypothesis, II,” *Proceedings of the National Academy of Sciences* 51(1), 1964, 105–110. DOI: 10.1073/pnas.51.1.105. | pp. 105–108, Theorem 2 and Lemmas 6–20; p. 109, Lemmas 21–22; p. 110, finite-fragment reduction. | Axiom verification, cardinal preservation, Choice, failure of CH, and the separate formal consistency discharge. It does not establish later representation identity. |
| `SCOTT1967-BOOLEAN-CH` | primary early Boolean-valued presentation; `VERIFIED` against the complete article scan, printed pp. 89–111 | Dana Scott, “A Proof of the Independence of the Continuum Hypothesis,” *Mathematical Systems Theory* 1(2), 1967, 89–111. DOI: 10.1007/BF01705520. | pp. 95–96, construction and completeness of the Boolean algebra; pp. 97–105, Boolean values for formulas, connectives, quantifiers, logic, functions and witness/fullness property; pp. 106–108, suitable model and direct proof that `(CH')` has Boolean value `0`; pp. 108–110, relation to Cohen forcing and scope of “reformulation”; pp. 110–111, Boolean-valued versus ordinary models, Löwenheim–Skolem, Rasiowa–Sikorski, homomorphism/quotient, complete conditions and order of realization. | Primary source for the direct Boolean-validity endpoint and its historical relation to Cohen's method. It supports a source-level route from Boolean values to ordinary models, but the exact same-generic-extension theorem is supplied by Jech, not attributed to Scott. The complete scan is evidence only and is not committed to this repository. |
| `SHOENFIELD1971-UNRAMIFIED` | primary early unramified presentation; bibliographic record `VERIFIED`; exact opening location corroborated by the stable scan and Kanamori | J. R. Shoenfield, “Unramified Forcing,” in Dana Scott (ed.), *Axiomatic Set Theory*, Proceedings of Symposia in Pure Mathematics 13, Part I, American Mathematical Society, 1971, 357–381. MR 0280359. | p. 357, opening rationale and stated removal of the ramified hierarchy; pp. 357–381, full construction. | Early source whose explicit purpose is direct construction of forcing models without Cohen's ramified hierarchy. It is evidence of historical reformulation, not evidence that the unramified form was already available in 1963. |

### 2.2 Authoritative technical and historical sources

| Stable key | Type and source-level status | Verified metadata | Exact locations used | Use and limit |
|---|---|---|---|---|
| `KANAMORI2008-COHEN` | peer-reviewed historical/technical retrospective; `VERIFIED` in D03 | Akihiro Kanamori, “Cohen and Set Theory,” *The Bulletin of Symbolic Logic* 14(3), 2008, 351–378. DOI: 10.2178/bsl/1231081371. | pp. 359–361, Cohen's original model and five-part scheme; p. 364, semantic and syntactic routes; p. 369, Boolean-valued reformulation; p. 370, Shoenfield's unramified partial-order/generic-filter form and early-1970s stabilization. | Main historical bridge. It distinguishes succession and reformulation from literal identity. |
| `JECH2003-SET-THEORY` | authoritative technical monograph; `VERIFIED` against the chapter scan and Springer metadata | Thomas Jech, *Set Theory: The Third Millennium Edition, Revised and Expanded*, Springer Monographs in Mathematics, Springer, 2003. DOI: 10.1007/3-540-44761-X. | Ch. 14, pp. 201–224: Def. 14.1; Lemma 14.4; Ths. 14.5–14.7; Th. 14.10; Cor. 14.12; Lemmas 14.13–14.14 and 14.19; Th. 14.24; Defs. 14.25–14.27; Th. 14.29; Cor. 14.30; Lemma 14.31; equations (14.30)–(14.32). | Exact technical relation among posets, separative quotients, Boolean completions, generic filters/ultrafilters, Boolean values, full Boolean-valued models, ordinary quotients, names, and generic extensions. This is a modern reconstruction, not evidence of 1963 vocabulary. |
| `MOORE2019-FORCING` | expert technical exposition; `VERIFIED` in D03 | Justin Tatch Moore, “The Method of Forcing,” arXiv:1902.03235v1, 2019. | §3, pp. 4–6, especially Definition 3.1, Definition 3.2, and the dense-equivalence observation; §§5–6, pp. 7–12, names, forcing relation, and forcing theorem. | Independent modern account of the generic-object, condition, name, and truth-determination roles. It does not settle historical identity. |
| `HAN-VANDOORN2020-CH` | peer-reviewed technical formalization; `VERIFIED` in D03 | Jesse Michael Han and Floris van Doorn, “A Formal Proof of the Independence of the Continuum Hypothesis,” in *CPP 2020*, 2020, 353–366. DOI: 10.1145/3372885.3373826; arXiv:2102.02901. | abstract and §1, pp. 353–354; §1.1, pp. 354–355. | Evidence that a Boolean-valued proof can bypass countable-transitive-model and explicit generic-filter machinery while preserving a forcing proof of both consistency directions. This is important counterevidence to an over-strong “identical mechanism” claim. |
| `BELL2005-BOOLEAN` | authoritative technical monograph; metadata and chapter ranges `VERIFIED` against Oxford Academic | John L. Bell, *Set Theory: Boolean-Valued Models and Independence Proofs*, 3rd ed., Oxford University Press, 2005. DOI: 10.1093/acprof:oso/9780198568520.001.0001. | Ch. 2, “Forcing and Some Independence Proofs,” pp. 55–70; Ch. 4, “Generic Ultrafilters and Transitive Models of ZFC,” pp. 88–108. | Corroborates the division between Boolean-valued truth calculation and the generic-ultrafilter route to actual two-valued models. No theorem number from an inaccessible page is asserted here. |

### 2.3 Evidence discipline used in this dossier

The source hierarchy is:

1. Cohen for the 1963–1964 operation;
2. Scott and Shoenfield for early alternative formulations;
3. Kanamori for the historical succession and its chronology;
4. Jech for exact representation translations;
5. Moore, Bell, and Han–van Doorn for technical and metamathematical cross-checks.

No search-result summary is used as evidence. Where direct page access was not sufficient for a component-level assertion, the assertion is assigned either to a source already verified in D03 or to Jech's exact theorem chain. Modern notation is explicitly marked retrospective.

---

## 3. Representation-by-representation reconstruction

### 3.1 Cohen's original ramified construction

| Audit field | Reconstruction |
|---|---|
| 1. Historical stage and source | Published 1963–1964 in Cohen Parts I and II. |
| 2. Background/model premise | A countable standard model `M` of Cohen's `Z-F`, taken to satisfy `V=L`, with the stronger semantic premise later separated from the finite-fragment consistency reduction. |
| 3. Input object | A cardinal `δ` in `M`; intended new subsets `a_\alpha` of the integers; a finite-condition system encoding membership/non-membership information. |
| 4. Characteristic generative resource | A coherent completion of finite condition information constructed outside `M`: Cohen's complete sequence, explicitly not definable in `M`, together with the recursively defined forcing relation that makes its information truth-determining. |
| 5. Key operation steps | Build ramified terms; define finite conditions; recursively define forcing; enumerate requirements using external countability; construct a complete descending/increasing-information sequence; interpret terms to obtain `N`; verify truth and axioms. |
| 6. Load-bearing intermediate objects | Ramified terms `F_\alpha`; finite conditions; the forcing relation; the complete sequence; interpreted model `N`. The complete sequence and forcing relation are the load-bearing generation pair; the ramified hierarchy is a serious historical component but is later eliminable. |
| 7. Output object | An interpreted extension `N` satisfying the base axioms, Choice, and `not-CH` under the semantic assumptions, followed by a relative-consistency transformation. |
| 8. Central truth/satisfaction relation | Cohen's Lemma 5, p. 1147: truth in `N` is connected to forcing by a condition in the complete sequence. |
| 9. Later eliminated/replaced components | The ramified term hierarchy and Cohen's literal complete-sequence presentation are removed or replaced in later formulations; the semantic countable-standard-model route can be replaced by a syntactic forcing argument for consistency. |
| 10. Components retaining the same function later | Conditions as partial approximations; ground-definable forcing relation; external generic coherence across all ground-model requirements; interpretation of names/terms; truth lemma; resulting extension. |
| 11. Merely notational/retrospective similarities | Writing Cohen's construction as `M,P,G,M[G]`; calling the complete sequence literally a modern generic filter without a mapping argument; treating his ramified terms as identical to later `P`-names. |
| 12. Candidate genuine differences | The historical operation constructs and interprets a ramified language and a sequence; later generic-filter forcing starts from an abstract poset and filter; Boolean-valued proofs can organize generation around algebra-valued truth and may not construct an explicit two-valued extension. |

#### Load-bearing judgment

Removing the complete sequence while leaving only the ramified vocabulary and finite conditions leaves no object that jointly realizes the dense requirements and determines `N`. Removing the forcing relation leaves no ground-defined bridge from conditions to truth in `N`. By contrast, removing the ramified hierarchy does not destroy forcing as such, because Shoenfield's program and the later name hierarchy reconstruct the extension and truth theorem without it. The ramified hierarchy is therefore historically central but not part of the minimal representation-neutral family core.

### 3.2 Partial-order / generic-filter / generic-extension formulation

| Audit field | Reconstruction |
|---|---|
| 1. Historical stage and source | Developed after Cohen; Shoenfield's 1971 “Unramified Forcing” is an early explicit source; Kanamori dates stabilization of the modern partial-order/generic-filter practice to the early 1970s. |
| 2. Background/model premise | Standard semantic presentation: a transitive model `M` of ZFC, a forcing poset `P\in M`, and an `M`-generic filter `G\subseteq P`. Syntactic consistency presentations need not assert an actual full generic extension. |
| 3. Input object | A partial order `P` of conditions, usually understood as finite or otherwise partial approximations; a class of `P`-names in `M`. |
| 4. Characteristic generative resource | An `M`-generic filter meeting every relevant dense set in `M`, with conditions coherently approximating a generic object; the forcing relation internal to `M` determines truth in the extension. |
| 5. Key operation steps | Choose/define `P`; define names and forcing; obtain or reason with an `M`-generic `G`; interpret names by `G`; form `M[G]`; apply the forcing theorem. |
| 6. Load-bearing intermediate objects | Poset `P`; dense sets; generic filter `G`; names; forcing relation. |
| 7. Output object | The minimal transitive generic extension `M[G]` containing `M` and `G`, or a syntactic consistency consequence expressed entirely via forcing. |
| 8. Central truth/satisfaction relation | Jech Th. 14.6: `M[G]\models\sigma` iff some `p\in G` forces `\sigma`; Moore's forcing theorem gives the same role. |
| 9. Eliminated/replaced components | Cohen's ramified language and literal complete sequence; actor-specific finite-condition syntax is abstracted to an arbitrary poset; the sequence is replaced by a filter object. |
| 10. Components retaining the same function | Conditions approximate the new object; genericity meets ground-model requirements; names are interpreted by the generic; forcing is ground-definable; truth in the extension is recovered through the forcing theorem. |
| 11. Merely notational/retrospective similarities | Treating every descending sequence as a generic filter; identifying `N` with `M[G]` without checking the term/name interpretation; assuming all posets are literally Cohen's finite conditions. |
| 12. Candidate genuine differences | The operation object is abstracted from a specific sequence construction to a filter on an arbitrary poset; the unramified name hierarchy is reorganized; semantic and syntactic proof routes are more sharply separable. |

#### Load-bearing judgment

Replacing one forcing poset with a dense-equivalent poset does not produce a new method: Moore notes that dense-equivalent forcings generate the same generic extensions, and Jech proves the exact generic-filter transfer through separative quotients and dense embeddings. The load-bearing role is not the literal identity of conditions but the ordered approximation and generic-coherence structure they carry.

### 3.3 Boolean-valued formulation

| Audit field | Reconstruction |
|---|---|
| 1. Historical stage and source | Boolean-valued models emerged shortly after Cohen, with early work by Scott, Solovay, and Vopěnka; Scott's 1967 paper is an early published Boolean-model proof. Kanamori records the reformulation at p. 369. |
| 2. Background/model premise | A complete Boolean algebra `B`, a Boolean-valued universe `V^B` or `M^B`, and Boolean values for atomic formulas and their recursive extensions. For an actual two-valued extension, use an `M`-generic ultrafilter `G` on `B`; for some formal consistency proofs, reason directly with Boolean values. |
| 3. Input object | Complete Boolean algebra `B`, often the Boolean completion `B(P)` of a forcing poset; Boolean-valued names/functions. |
| 4. Characteristic generative resource | The complete algebra of truth-support values encodes all condition-level forcing information; a generic ultrafilter selects a coherent two-valued quotient/interpretation, while Boolean validity can itself carry a consistency proof. |
| 5. Key operation steps | Form `V^B` or `M^B`; recursively define Boolean values of membership, equality, formulas, and quantifiers; verify ZFC has value `1`; optionally choose a generic ultrafilter; interpret names/quotient to obtain `M[G]`; recover ordinary truth. |
| 6. Load-bearing intermediate objects | Complete Boolean algebra; Boolean-valued universe; Boolean truth values; fullness/mixing properties where needed; generic ultrafilter for the two-valued quotient. |
| 7. Output object | A Boolean-valued model validating ZFC; with a generic ultrafilter, an ordinary generic extension `M[G]`; or directly a relative-consistency consequence. |
| 8. Central truth/satisfaction relation | Jech Def. 14.26 identifies `p\Vdash\varphi` with `e(p)\leq\|\varphi\|`; Th. 14.29 states ordinary truth in `M[G]` iff the Boolean value belongs to the generic ultrafilter. |
| 9. Eliminated/replaced components | The forcing relation can be defined through Boolean values; the poset is replaced by its separative quotient and complete Boolean algebra; an explicit generic extension can be omitted in a direct Boolean-valued consistency proof. |
| 10. Components retaining the same function | Conditions survive densely inside `B`; generic filters and ultrafilters are interdefinable; names retain their interpretation role; forcing truth becomes an order relation to Boolean values; the same `M[G]` is recovered. |
| 11. Merely notational/retrospective similarities | Calling `V^B` itself an ordinary model without quotient/interpretation; identifying every Boolean-valued proof with an explicit generic-extension construction; equating the algebra element `\|\varphi\|` with a condition token. |
| 12. Candidate genuine differences | The semantic mechanism distributes truth over a complete algebra before two-valued realization; some proofs use Boolean validity without constructing `G` or `M[G]`; the metamathematical dependency profile can therefore differ from the semantic generic-filter route. |

#### Load-bearing judgment

For set forcing, Boolean completion is not a merely analogous apparatus. Jech Th. 14.10 and Cor. 14.12 place a separative poset densely in a unique complete Boolean algebra; Lemma 14.13 makes the poset generic filter and Boolean generic ultrafilter definable from each other and yields `M[G]=M[H]`; Def. 14.26 recovers the forcing relation from Boolean values; Th. 14.29 recovers ordinary truth after generic interpretation. This is enough for a same-family judgment. It is not enough for an “identical operation in every use” judgment, because direct Boolean-valued consistency proofs can stop before a generic quotient is formed.

---

## 4. What `m` denotes for D06

Before running the pairwise tests, this dossier fixes the provisional audit unit.

### 4.1 Rejected units

`m` must not denote any of the following:

1. **the proof goal** “establish a relative-consistency result”;
2. **the output** `M[G]`, `N`, or `not-CH`;
3. **an individual condition**, name, dense set, sequence element, or Boolean value;
4. **Cohen's entire 1963 paper**, including every expository and historical component;
5. **an arbitrary forcing notion** such as Cohen forcing, random forcing, or a collapse;
6. **the entire mature forcing ecosystem**, including iteration, preservation, forcing axioms, generic absoluteness, textbooks, and training;
7. **institutional uptake itself**, since that is what `H/N/S` must test rather than presuppose.

### 4.2 Provisional positive unit

For D06, `m` denotes the following **bounded forcing method family**:

> A background-relative operation in which ordered partial information is equipped with a ground-definable forcing or Boolean-truth relation, and is generically completed—or represented by an equivalent Boolean-valued construction and generic quotient—so that names/terms are interpreted and truth in a model extension is determined.

This unit contains five functional roles:

1. **approximation role:** conditions or dense Boolean elements encode partial information;
2. **coherence role:** a complete sequence, generic filter, or generic ultrafilter meets the relevant background requirements;
3. **interpretation role:** terms or names receive values from the coherent generic object;
4. **truth-determination role:** forcing or Boolean values connect the background construction to truth;
5. **extension role:** the interpretation yields, or semantically represents, a model extension with the target property.

A representation may replace the bearer of one role without leaving the family, provided the role is preserved and the translation is load-bearing, bidirectional at the relevant level, and not merely output-preserving.

### 4.3 Token, representation, and family

Three levels must remain distinct:

| Level | Example | Identity standard |
|---|---|---|
| Historical operation token | Cohen's 1963–1964 ramified construction | actor-, time-, source-, and component-specific |
| Representation-specific operation | generic-filter forcing; Boolean-valued forcing | specific mathematical objects and central truth/generation relation |
| Method family | the five-role forcing core in §4.2 | characteristic generation role preserved under admissible representation changes |

This distinction is not a modification of Method Individuation Protocol v0.1. It is the dossier's application of the frozen granularity and representation-invariance tests. The fact that the protocol did not name these three levels is one reason its result is **qualified** rather than independently validated.

---

## 5. Pairwise audit I: ramified ↔ generic-filter

### 5.1 Strongest same-family argument

The strongest same-family case is functional, not notational.

- Cohen's finite conditions give partial information about intended new subsets.
- The complete sequence is constructed outside `M`, meets the enumerated requirements, and determines the interpretation `N`.
- In the unramified form, conditions are elements of a poset, an `M`-generic filter meets all dense requirements in `M`, names are interpreted by the filter, and `M[G]` is formed.
- Cohen's Lemma 5 and the modern forcing theorem perform the same load-bearing bridge: background-defined forcing plus membership in the generic completion determines truth in the extension.
- Shoenfield's explicit project is to obtain forcing models directly without the ramified hierarchy, which is evidence that the hierarchy can be removed while preserving the forcing-model construction.
- Kanamori's historical reconstruction identifies the later partial-order/generic-filter form as the unramified successor to Cohen's scheme, while explicitly keeping the chronology distinct.

The characteristic resource is therefore not the ramification itself. It is the combination of partial conditions, an external generic completion meeting background requirements, and a forcing/truth bridge that interprets names/terms and generates an extension.

### 5.2 Strongest different-operation argument

The strongest split case is also substantive.

- Cohen constructs a particular complete sequence by an external enumeration tied to the ramified language and then defines `N`.
- The modern operation takes an abstract poset and a filter object as primitive elements of the presentation.
- The modern name hierarchy and filter semantics reorganize the operation object, not just the typography.
- A filter is not literally a sequence; many filters have no distinguished enumeration, and the poset abstraction generalizes far beyond Cohen's original finite assertions.
- The later form sharply separates semantic and syntactic forcing routes in a way not identical to the published event-stage proof organization.

Thus the two are not the same historical operation token and not componentwise identical operations.

### 5.3 Frozen six-test matrix

| Frozen test | Result | Evidence and rationale |
|---|---|---|
| 1. Historical availability | **asymmetric / pass with lock** | The ramified operation is documented in 1963–1964. The mature generic-filter form is later; Shoenfield 1971 and Kanamori p. 370 document the reformulation. Later availability cannot be projected backward. |
| 2. Functional role | **pass** | Complete sequence and generic filter each provide coherent generic completion; ramified terms and names each support interpretation; Lemma 5 and the forcing theorem connect forcing to truth. |
| 3. Load-bearing removal/replacement | **pass, qualified** | Removing generic completion or forcing/truth destroys the extension relation. Replacing the complete sequence by a generic filter preserves it. Removing ramification degrades/reorganizes the presentation but does not destroy forcing. |
| 4. Conservative substitution | **pass at family level; fail at token level** | The unramified operation substitutes for the ramified generation function retrospectively. It does not show that a 1963 practitioner had the later operation available on its own terms. |
| 5. Representation invariance | **pass, qualified** | The novelty verdict does not depend on ramified syntax. The common role survives the rewrite. The result would fail if identity were defined by literal intermediate objects, showing why token-level identity is too fine. |
| 6. Granularity sanity | **pass** | Proof-goal identity is rejected as too coarse; counting the ramified hierarchy and sequence/filter difference as automatically distinct methods is rejected as too fine. The case sits at a representation-specific operation / family boundary. |

### 5.4 Direction and preservation level

| Direction | Status | What is preserved |
|---|---|---|
| Ramified → generic-filter | technically strong, historically retrospective | target extension construction, partial-information ordering, generic coherence, term/name interpretation, forcing-to-truth relation |
| Generic-filter → ramified | not established as a general inverse | a modern forcing may be encoded into ramified machinery in principle, but no source-backed general historical reconstruction is established here |
| Bidirectional full operation identity | **not supported** | literal sequence, ramified hierarchy, proof organization, and historical availability are not preserved |
| Bidirectional family role | **qualified support** | generation role and truth/extension semantics are preserved |

### 5.5 Pair verdict

`qualified_same_method_family`

**Boundary:** same method family at the characteristic generation level; different representation-specific operations and different historical tokens.

---

## 6. Pairwise audit II: generic-filter ↔ Boolean-valued

### 6.1 Strongest same-family argument

This pair has the strongest exact technical translation.

Jech establishes the following chain for set forcing:

1. every separative poset densely embeds in a complete Boolean algebra, unique up to isomorphism (Th. 14.10);
2. every poset has a separative quotient and Boolean completion preserving compatibility and a dense image (Lemma 14.11; Cor. 14.12);
3. generic filters transfer in both directions across the quotient and dense embedding (Lemma 14.13);
4. the poset generic filter `G` and the induced Boolean generic ultrafilter `H` are definable from each other and yield the same extension, `M[G]=M[H]`;
5. `P`-names are identified with the Boolean-valued names over `B(P)` (Def. 14.26);
6. `p\Vdash\varphi` is equivalent to `e(p)\leq\|\varphi\|`;
7. interpretation by a generic ultrafilter produces `M[G]` (Def. 14.27);
8. ordinary truth in the extension is equivalent to membership of the Boolean value in the ultrafilter (Th. 14.29);
9. the general poset case is recovered from the Boolean case with identical name interpretation and the same extension (equations (14.32), pp. 218–219).

The conversion therefore preserves more than the conclusion and more than the proof target. It preserves:

- the generic object;
- the extension;
- the name interpretation;
- the forcing/truth relation;
- compatibility and density structure;
- and the central generation role.

### 6.2 Strongest different-operation argument

The strongest split argument concerns the stopping point and semantic architecture.

- Generic-filter forcing presents generation through an actual or postulated filter `G` and interprets names to form `M[G]`.
- Boolean-valued forcing first creates an algebra-valued universe and distributes truth across `B`.
- A direct Boolean-valued consistency proof may use a nonzero Boolean value or validity in `V^B` without constructing an external generic ultrafilter or ordinary two-valued extension.
- Han and van Doorn explicitly exploit Boolean-valued models in formalization to avoid the usual countable-transitive-model and generic-filter route.
- Thus the Boolean apparatus can carry a theorem-producing semantic function even when the generic-realization step is omitted.

This is a genuine operation-architecture difference. It does not defeat family identity because the generic-filter operation is recoverable through Boolean completion and ultrafilter interpretation, but it blocks an unconditional claim that every Boolean-valued proof token performs the complete generic-extension operation.

### 6.3 Frozen six-test matrix

| Frozen test | Result | Evidence and rationale |
|---|---|---|
| 1. Historical availability | **asymmetric / pass with lock** | Boolean-valued models arose after Cohen and alongside the later stabilization of forcing. The exact modern equivalence is retrospective; it does not establish 1963 availability. |
| 2. Functional role | **pass** | Poset conditions correspond densely to nonzero Boolean values; filters correspond to generic ultrafilters; names and truth relations are explicitly mapped; the same extension is obtained. |
| 3. Load-bearing removal/replacement | **pass** | Replacing `P` by `B(P)` does not destroy the extension. Removing generic interpretation from a proof that requires an ordinary `M[G]` does destroy that output, but direct Boolean-valued consistency proofs may have a different endpoint. |
| 4. Conservative substitution | **pass for set-forcing extension generation** | Jech gives type-correct bidirectional substitutions preserving genericity, name interpretation, truth, and extension. The substitution is not merely same-goal or same-result. |
| 5. Representation invariance | **pass** | The method-family verdict is invariant under poset/Boolean completion. Treating the complete algebra as automatically a new method would violate exclusion 4 and the dense-equivalence facts. |
| 6. Granularity sanity | **pass** | A proof-goal unit would be too coarse. A unit counting every completion, quotient, or Boolean value as a new method would be too fine. The exact equivalence fixes an intermediate family level. |

### 6.4 Direction and preservation level

| Direction | Status | What is preserved |
|---|---|---|
| Poset/filter → Boolean-valued | **supported** | compatibility, density, genericity, names, forcing values, truth, and `M[G]` |
| Boolean-valued + generic ultrafilter → poset/filter | **supported up to dense presentation** | generic extension and forcing relation; recover a dense poset presentation |
| Boolean-valued proof without generic quotient → generic-extension operation | **not automatic** | conclusion/consistency may be preserved without the complete realization role |
| Bidirectional family role | **supported** | full extension-generating role is preserved when the generic-ultrafilter/quotient step is included |

### 6.5 Pair verdict

`supported_same_method_family`

**Boundary:** supported for set forcing at the extension-generating level. A Boolean-valued proof that deliberately stops at algebra-valued validity is a related proof architecture within the family, not automatically the same complete operation token as forming `M[G]`.

---

## 7. Pairwise audit III: ramified ↔ Boolean-valued

### 7.1 Strongest same-family argument

The common core can be reconstructed by composition through the generic-filter form:

\[
\text{ramified complete-sequence construction}
\longrightarrow
\text{generic-filter forcing}
\longleftrightarrow
\text{Boolean completion / Boolean-valued forcing}.
\]

Across that chain:

- finite conditions remain partial-information carriers;
- generic coherence remains the device that jointly satisfies background requirements;
- terms/names remain interpretation devices;
- forcing remains a background-definable truth predictor;
- and the target is an extension or an equivalent semantic model supporting the consistency conclusion.

Scott's early Boolean-model proof and Kanamori's p. 369 historical account show that Boolean-valued models were developed as a reformulation of Cohen's method, not as an unrelated later technique that happened to prove the same theorem.

### 7.2 Strongest different-operation argument

The direct split case is stronger here than in the generic-filter pair.

- Cohen's central truth lemma is stated using a condition from a particular externally constructed complete sequence and truth in `N`.
- Boolean-valued semantics assigns every formula an element of a complete Boolean algebra before any generic selection.
- The ramified hierarchy disappears.
- The complete sequence may disappear.
- The ordinary extension may disappear from the proof architecture if one reasons directly with Boolean validity.
- The direct component map from each Cohen term/definition/lemma to the Boolean-valued hierarchy is not established in the primary historical sources used here.

Therefore the pair cannot be called unqualifiedly identical in operation role.

### 7.3 Frozen six-test matrix

| Frozen test | Result | Evidence and rationale |
|---|---|---|
| 1. Historical availability | **asymmetric / pass with lock** | Cohen's form is 1963–1964; the Boolean-valued form appears afterward. Historical succession is documented, but no backward availability is inferred. |
| 2. Functional role | **qualified pass** | Both determine truth from condition-like information and support an extension/consistency construction. The Boolean-valued form can also terminate at algebra-valued validity, changing the endpoint. |
| 3. Load-bearing removal/replacement | **qualified pass** | Ramification is removable; the forcing/truth structure is preserved. Replacing the complete sequence by Boolean values alone preserves consistency semantics but not necessarily an actual extension; adding a generic ultrafilter restores it. |
| 4. Conservative substitution | **qualified** | A substitution preserving the full extension role exists by composing ramified→generic-filter with generic-filter↔Boolean completion. A direct historical quasi-inverse is not established. |
| 5. Representation invariance | **pass at family level** | The forcing novelty/family verdict survives the formal change. The result is not stable at literal-operation-token granularity, which is expected rather than a protocol failure. |
| 6. Granularity sanity | **pass, qualified** | Same-output reasoning is rejected as too coarse; counting the removed ramified hierarchy or Boolean truth values as decisive by themselves is rejected as too fine. The compositional nature of the translation prevents an unqualified verdict. |

### 7.4 Direction and preservation level

| Direction | Status | What is preserved |
|---|---|---|
| Ramified → Boolean-valued | qualified, compositional | condition information, forcing semantics, names/terms in reconstructed form, consistency target, and—when a generic ultrafilter is added—the extension |
| Boolean-valued → ramified | not established generally | no source-backed general reconstruction into Cohen's literal hierarchy and sequence |
| Conclusion preservation | strong | CH consistency/independence outputs |
| Full generation-role preservation | qualified | requires the generic-realization/quotient step; direct Boolean validity alone preserves less than Cohen's actual `N` construction |

### 7.5 Pair verdict

`qualified_same_method_family`

**Boundary:** same higher forcing family through a supported intermediate equivalence; not a direct, historically symmetric, componentwise identity.

---

## 8. Cross-representation generation-resource table

| Functional role | Cohen ramified | Generic-filter / extension | Boolean-valued | Invariance judgment |
|---|---|---|---|---|
| Background | countable standard `M`, taken `V=L`, plus later finite-fragment discharge | transitive `M`, poset `P\in M`, or syntactic ground-universe presentation | complete Boolean algebra `B` in a background; `V^B`/`M^B`; optional generic ultrafilter | **not invariant as premise package** |
| Partial-information carrier | finite elementary membership assertions | conditions in a poset | dense nonzero elements of `B`, with `P` densely embedded | **invariant role** |
| Coherent generic completion | complete sequence external to `M` | `M`-generic filter `G` | generic ultrafilter `H` on `B`; or no explicit realization in direct Boolean proof | **invariant when extension is generated; optional in weaker semantic endpoint** |
| Term/name resource | ramified terms `F_\alpha` | `P`-names | Boolean-valued names/functions | **invariant interpretation role; non-identical objects** |
| Truth predictor | recursively defined forcing relation | `p\Vdash\varphi` internal to `M` | Boolean value `\|\varphi\|`, with `p\Vdash\varphi \iff e(p)\leq\|\varphi\|` | **strongly invariant** |
| Truth/realization theorem | Cohen Lemma 5 | forcing theorem | Boolean truth theorem plus generic interpretation | **strongly invariant with quotient** |
| Generated object | interpreted `N` | minimal `M[G]` | `M[H]`, equal to `M[G]`, or algebra-valued model alone | **invariant for extension route; broader Boolean endpoint** |
| Eliminable shell | ramified hierarchy | particular dense presentation of `P` | choice of Boolean completion presentation up to isomorphism | **representation-dependent** |
| Historical token | Cohen 1963–1964 | Shoenfield/later stabilized form | Scott–Solovay/Vopěnka tradition | **not invariant** |

### 8.1 Common characteristic generative resource

The non-empty common resource is:

> **generic completion of ordered partial information, controlled by a background-definable forcing/Boolean truth relation, with an interpretation step that determines truth in a model extension.**

This formulation is deliberately narrower than “produces a generic extension” and broader than “uses a complete sequence.” It includes the load-bearing roles and excludes merely shared conclusions.

### 8.2 Components outside the common core

The following are representation-specific or route-specific:

- Cohen's ramified hierarchy;
- a distinguished enumerated complete sequence;
- a literal poset/filter presentation;
- complete Boolean algebra semantics;
- an actual countable transitive ground model;
- the finite-fragment syntactic consistency discharge;
- and direct Boolean-valued proof without generic quotient.

None of these differences is ignored. They determine whether two **operation tokens** are identical, but they do not by themselves defeat the family relation.

---

## 9. Strongest arguments and final method-family adjudication

### 9.1 Strongest same-family argument

The strongest argument is the exact preservation chain, not the historical naming convention.

1. Cohen's load-bearing pair is generic coherence plus a forcing/truth bridge.
2. Shoenfield's unramified form removes ramification while retaining conditions, genericity, name interpretation, extension generation, and the forcing theorem.
3. Jech proves that poset forcing and Boolean completion preserve genericity in both directions, define the same extension, and identify forcing with Boolean truth support.
4. Therefore the family core survives both eliminations: ramification can be removed, and a poset can be replaced by its complete Boolean algebra, without destroying the extension-generating relation.
5. The result is not merely same theorem or same goal. The central generative and truth-determining roles are translated.

### 9.2 Strongest split argument

The strongest split argument is that “forcing” has at least three legitimate operation levels.

1. Cohen's event token includes a specific ramified construction and external sequence.
2. Generic-filter forcing reorganizes the operation around an abstract poset and filter.
3. Boolean-valued forcing reorganizes it around algebra-valued truth and can support consistency without actual generic realization.
4. Translation is historically asymmetric.
5. Ramified↔Boolean mapping is compositional rather than a direct componentwise quasi-inverse.
6. Thus there is no evidence for one literally identical operation across all uses, and “same generic-extension conclusion” would be too coarse.

### 9.3 Required final verdict

\[
\boxed{\texttt{qualified\_same\_method\_family}}
\]

This verdict applies to the higher-level relation among:

- Cohen's original ramified operation;
- the generic-filter / generic-extension operation;
- the Boolean-valued operation.

It means:

- **same family:** the characteristic generative resource and load-bearing truth/extension function survive admissible representation changes;
- **qualified:** the historical tokens, premise packages, intermediate objects, proof architectures, and endpoints are not all preserved, and one pairwise relation is established only compositionally.

It does **not** mean “the three are interchangeable without qualification,” “Cohen already had the modern form,” or “every Boolean-valued proof constructs a generic extension.”

---

## 10. Relation to `EVD-D03-0010`

### 10.1 Verdict movement

`EVD-D03-0010` does **not** move. It remains **qualified**.

The prior obligation was intentionally broader than the present pairwise findings. It concerned the cross-formulation relation and prohibited unrestricted interchangeability or exact identity. This dossier now supplies:

- a qualified family relation for ramified↔generic-filter;
- a supported family relation for generic-filter↔Boolean-valued set forcing;
- a qualified compositional family relation for ramified↔Boolean-valued.

Those results refine the qualification rather than remove it.

### 10.2 Why no upgrade is licensed

An upgrade to `supported` for the unrestricted obligation would require all of the following:

1. a direct, source-backed mapping from Cohen's ramified components to both later forms;
2. a clear statement of which operation level the identity concerns;
3. bidirectional preservation of the full generation role, not only conclusion or extension;
4. explicit treatment of Boolean-valued proofs that do not form a generic quotient;
5. and no historical retrojection.

The present record does not meet all five.

### 10.3 Newly registered obligations

| Evidence ID | Obligation | Closure condition | Withdrawal condition |
|---|---|---|---|
| `EVD-D05-0005` | Directly map Cohen's complete sequence, ramified terms, forcing relation, and interpreted `N` to the later generic-filter/name construction using primary or authoritative technical sources, and determine whether a source-backed reverse reconstruction exists. | Close as `supported` when each load-bearing Cohen component has a typed later image, the preserved role is stated, and any reverse direction and its assumptions are documented with exact locations. Close as `qualified` if only the forward functional map or a compositional reverse is available. | Withdraw if the task is shown to be ill-typed because the historical token has no meaningful componentwise reverse and only family-level comparison is legitimate. |
| `EVD-D05-0006` | Determine whether Boolean-valued forcing without an explicit generic ultrafilter preserves the same extension-generating operation role or only a weaker theorem-producing semantic role. | Close when a source-backed comparison states the endpoint, premises, and preserved function for direct Boolean validity versus generic quotient, including at least one exact theorem-level bridge. | Withdraw if D06 explicitly excludes non-extension Boolean-valued proofs from its target family, making the distinction outside the target object's scope. |

No manuscript index is modified in this PR. The obligations are registered only in this evidence directory.

---

## 10A. `EVD-D05-0006` — bounded adjudication supplement (2026-08-11)

**Obligation verdict:** `supported`

**Question adjudicated:** When Boolean-valued forcing is used without an explicit generic ultrafilter, appropriate homomorphism, or two-valued quotient, does it perform the complete extension-generating operation, or does it stop at a weaker theorem-producing semantic role?

> **SUPPLEMENT SCOPE LOCK**
>
> This supplement adjudicates only `EVD-D05-0006`. It does not move `EVD-D03-0010`, `EVD-D05-0001`, `EVD-D05-0005`, or `EVD-D04-0002`; does not adjudicate D06 `H/N/S`, institutionalization, Control A, Control B, Part II, C2, the paper as a whole, or SRT; and does not modify the frozen Method Individuation Protocol v0.1 or the staged manuscript. Scott 1967 is outside the 1938–1963 control-archive window and is used only for the forcing-representation question.

### 10A.1 Source-level result from Scott 1967

The complete article scan was checked page by page from printed p. 95 through p. 111. PDF page 7 is printed p. 95 and PDF page 23 is printed p. 111. The following ledger records controlled paraphrases, not substituted source text.

| Printed pages | Checked result | Endpoint implication |
|---|---|---|
| pp. 95–96 | Scott begins the model construction by reinterpreting logical as well as non-logical primitives. The quotient event algebra modulo null sets is complete; Scott says this completeness is essential to the method's success. The countable-chain condition permits arbitrary suprema to be reduced to suitable countable subfamilies. | Completeness is a load-bearing resource for assigning values to quantifiers and for later witness/choice constructions. It is not decorative probability notation. |
| pp. 97–98 | Atomic formulas receive event values; propositional connectives receive the corresponding Boolean operations; universal and existential quantifiers receive infima and suprema over all instances. | The operation directly computes formula values in a complete Boolean algebra. No ultrafilter or ordinary satisfaction relation appears at this endpoint. |
| pp. 99–105 | Boolean validity is value `1`. Scott distinguishes this from an ordinary model, checks logical inference, defines random functions and functionals, and proves that an existential Boolean value is attained by an instance. | Endpoint A is a genuine semantic model and theorem-producing apparatus. The attained-witness property supplies the fullness needed for controlled quotienting, but does not itself perform a quotient. |
| pp. 106–108 | Scott constructs the product-space Boolean model and proves directly that the two disjuncts of the selected CH formulation have value `0`; hence `(CH')` has Boolean value `0`. | The independence argument is completed at endpoint A by Boolean-value calculation. No ordinary two-valued model is constructed in this proof step. |
| pp. 108–109 | Scott reports Solovay's observation that weak forcing conditions determine pairs forming a complete Boolean algebra and that Boolean assignment exposes the algebraic properties carrying the construction. Scott's “reformulation of Cohen's original method” concerns this forcing-to-Boolean-value reconstruction and the use of arbitrary complete Boolean algebras. | “Reformulation” supports same-family status for the truth/forcing resource. It does not erase the later distinction Scott himself draws between Boolean-valued and ordinary endpoints. |
| pp. 109–110 | Scott explains that one may work with Boolean values without constructing full transfinite set theory and that arbitrary complete Boolean algebras, not probability measure as such, carry the construction. | The theorem-producing endpoint is not merely an abbreviation for a hidden generic filter. It can be used on its own. |
| pp. 110–111 | Avoiding countable models means retaining Boolean-valued, not ordinary `{0,1}`-valued, models. Scott says forcing can likewise be used without “going over to a model.” To obtain ordinary models one adds a homomorphism to the two-element algebra; an arbitrary homomorphism may yield a nonstandard, non-well-founded model, so Scott first invokes Löwenheim–Skolem for a suitable countable submodel and then Rasiowa–Sikorski for a homomorphism preserving enough suprema. Cohen's complete set of conditions performs the corresponding role in the forcing framework. | The source explicitly separates endpoint A from endpoints B/C. The homomorphism/quotient is an additional load-bearing realization step. Scott's “first” versus “last or not at all” comparison identifies order of realization, not identity of endpoints when the last step is omitted. |

### 10A.2 Three endpoints that must not be collapsed

| Endpoint | Required resources | Output and preserved function | What is not yet obtained |
|---|---|---|---|
| **A. Direct Boolean validity / Boolean-valued semantic proof** | Complete Boolean algebra; Boolean-valued domain; recursive values for atomic formulas, connectives and quantifiers; validity as value `1` | Algebra-valued truth determination, validity, and a direct consistency/independence proof; in Scott's construction, `(CH')` has value `0` | No ordinary two-valued satisfaction structure merely from the value calculation; no selected generic extension |
| **B. Ordinary two-valued model** | A full Boolean-valued model plus an ultrafilter, or equivalently a suitable homomorphism to `{0,1}`, followed by quotient/interpretation | Ordinary satisfaction in the quotient. Jech Lemma 14.14 gives `A/F ⊨ φ([a])` iff `||φ(a)|| ∈ F` | An arbitrary quotient need not be standard, well-founded, transitive, or a generic extension of a specified ground model |
| **C. Generic extension through quotient or generic ultrafilter** | Ground model `M`; forcing poset `P` or complete Boolean algebra `B(P)`; an `M`-generic filter/ultrafilter; interpretation of names | A transitive ordinary model `M[G]`; forcing truth; minimal extension containing `M` and the generic object; equality with the Boolean route's `M[H]` | Historical identity with Cohen's 1963 token, or identity of every proof architecture |

The shared independence conclusion does not identify these endpoints. Endpoint A preserves the forcing/Boolean truth resource and theorem-producing function. Endpoints B and C require a selection/quotient step that turns algebra-valued truth into ordinary truth; endpoint C additionally requires background-relative genericity and the generic-extension construction.

### 10A.3 Exact theorem-level bridge

The bridge uses Scott for the historical countable-submodel/homomorphism route and Jech Chapter 14 for the exact modern quotient and same-extension results. They are complementary records, not one source silently substituted for the other.

| Bridge step | Exact source location | What is established |
|---|---|---|
| Poset to complete Boolean algebra | Jech Th. 14.10, pp. 205–206; Cor. 14.12, p. 206 | A separative poset embeds densely in a complete Boolean algebra; an arbitrary poset has a separative quotient and Boolean completion preserving order/compatibility with dense image. |
| Boolean-valued model and fullness | Scott pp. 97–105, especially p. 105; Jech Boolean-valued semantics, pp. 206–208, and Lemma 14.19, p. 211 | Formulas and quantifiers have Boolean values; existential values are attained by instances in the full model. |
| Suitable countable submodel | Scott pp. 110–111 | Löwenheim–Skolem is applied to the Boolean model before the ordinary-model step; the attained-witness property is the stated reason the required submodel can be chosen. This is a source-level route, not a derivation of a countable transitive ground model from bare consistency. |
| Generic ultrafilter / appropriate homomorphism | Scott pp. 110–111; Jech Lemma 14.4, p. 203, and Lemma 14.13, p. 206 | Rasiowa–Sikorski supplies a homomorphism preserving the required countable suprema; equivalently its `1`-preimage is the relevant ultrafilter. In the modern forcing route, countably many dense requirements yield a generic filter, and filters transfer through separative quotient and dense Boolean embedding. |
| Quotient to an ordinary model | Jech Lemma 14.14, p. 208 | For a full Boolean-valued model `A` and ultrafilter `F`, the quotient `A/F` is two-valued and its ordinary satisfaction relation is exactly membership of Boolean values in `F`. |
| Forcing relation from Boolean values | Jech Def. 14.26, p. 215 | `p ⊩ φ(a)` iff `e(p) ≤ ||φ(a)||`; the forcing relation is recovered from Boolean support. |
| Generic interpretation and ordinary truth | Jech Def. 14.27, p. 216; Th. 14.29, pp. 216–217; Cor. 14.30, p. 217; Lemma 14.31, pp. 217–218 | Interpretation by an `M`-generic ultrafilter yields `M[G]`; ordinary truth is equivalent to membership of the Boolean value in the ultrafilter; the result is a ZFC model containing `M` and the generic object with the stated minimality. |
| Same generic extension | Jech Lemma 14.13, p. 206; equations (14.32), p. 218 | A poset-generic `G` and the induced Boolean generic ultrafilter `H` are definable from each other; name interpretations agree and `M[G]=M[H]`. |

This theorem chain is conditional in the precise place the endpoint distinction requires. It proves that **adding** an appropriate generic ultrafilter/quotient recovers the full extension-generating operation and the same generic extension. It does not turn a direct Boolean-validity proof that stops before that step into an already performed generic-extension construction.

### 10A.4 Frozen six-test matrix for the endpoint distinction

| Frozen test | Result | Evidence and rationale |
|---|---|---|
| 1. Historical availability | **pass with chronology lock** | Scott 1967 directly documents the Boolean endpoint and the later/optional homomorphism step. Nothing is projected into 1963 as Cohen's literal presentation. |
| 2. Functional role | **pass** | Complete Boolean values perform truth determination and the independence proof; the ultrafilter/homomorphism performs two-valued realization; genericity plus name interpretation performs extension generation. |
| 3. Load-bearing removal/replacement | **pass** | Removing completeness blocks the required quantifier suprema and witness constructions. Omitting the quotient leaves endpoint A intact but removes endpoints B/C. Adding an appropriate quotient restores them. |
| 4. Conservative substitution | **pass, endpoint-bounded** | Boolean values substitute for forcing in theorem production and truth support. They do not conservatively substitute for the ordinary/generic-extension output unless the quotient/generic step is included. |
| 5. Representation invariance | **pass** | Jech's dense Boolean completion preserves genericity, names, forcing truth and the same extension. The A-versus-C distinction remains when notation changes, because it turns on whether realization is performed, not on poset versus Boolean syntax. |
| 6. Granularity sanity | **pass** | Identifying all three endpoints because they prove the same independence result is too coarse. Treating each Boolean value or completion as a separate method is too fine. The operation-role boundary lies at theorem-producing Boolean semantics versus performed two-valued/generic realization. |

### 10A.5 D05b §10.3 closure and withdrawal conditions

| Registered condition | Result | Reason |
|---|---|---|
| State the endpoint for direct Boolean validity versus generic quotient | **met** | §10A.2 distinguishes A, B and C and states their outputs separately. |
| State the premises for each endpoint | **met** | §10A.2 names completeness/fullness, ultrafilter or homomorphism, ground model, genericity and name interpretation at the endpoint where each is required. |
| State the preserved function | **met** | §10A.1–§10A.4 distinguish theorem-producing Boolean truth from ordinary satisfaction and extension generation. |
| Supply at least one exact theorem-level bridge | **met** | §10A.3 supplies the Scott pp. 110–111 route and the Jech Lemma 14.14 / Def. 14.26 / Th. 14.29 / equation (14.32) chain with exact pages. |
| Withdraw if D06 explicitly excludes non-extension Boolean-valued proofs | **not triggered** | D05b §12.2 includes the complete-Boolean/Boolean-valued representation when its extension-generating **or exact equivalent semantic role** is documented; §12.8 instead requires this endpoint distinction to be resolved. Direct endpoint A is therefore inside the registered audit question, though it is not itself counted as a completed extension token. |

### 10A.6 Verdict and mandatory limits

\[
\boxed{\texttt{EVD-D05-0006: supported}}
\]

**Supported result:** Boolean-valued forcing without an explicit generic ultrafilter or appropriate homomorphism/quotient preserves the complete Boolean truth/forcing semantics and can directly produce the independence theorem, but it does **not** by itself perform the full ordinary-model or generic-extension-generating operation. That fuller role is recoverable by adding the quotient/generic-realization step; when the ultrafilter is generic over the stated ground model, Jech's exact bridge yields the same generic extension as the poset route.

**Mandatory limits:**

- “Reformulation of Cohen's original method” is licensed only at the forcing/Boolean-truth and method-family level documented on Scott pp. 108–111. It does not license historical identity or endpoint collapse.
- Scott's avoidance of countable models concerns endpoint A. It does not say that well-founded ordinary models can be obtained without the countability/genericity conditions Scott reintroduces for endpoint B.
- An arbitrary Boolean-algebra homomorphism may produce a nonstandard, non-well-founded ordinary model. Endpoint B is not automatically endpoint C.
- Under the existing §12.2 inclusion criteria, endpoint A alone is not a completed D06 `m_family` operation token; the documented quotient/generic-realization route must be part of the audited operation. This applies the existing target boundary and does not adjudicate `H`, `N`, or `S`.
- This verdict does not move the overall `qualified_same_method_family` finding, `EVD-D03-0010`, `EVD-D05-0005`, or the provisional D06 target. It issues no D06 `H/N/S` or institutionalization verdict.
- Scott 1967 is not admitted to the 1938–1963 control archive. No candidate enumeration, scoring, ranking, selection or individuation is performed.
- The source PDF is not committed or reproduced; only metadata, exact pages, controlled paraphrases, adjudication and limits are recorded.

---

## 11. Method Individuation Protocol v0.1 falsification result

### 11.1 Outcome

\[
\boxed{\text{protocol v0.1: qualified, not falsified}}
\]

No frozen rule, exclusion, test, or falsification plan is edited.

### 11.2 Why it is not falsified

The preregistered risk was that representation change might force one of two failures:

- **over-fineness:** every new intermediate object or formalism becomes a new method;
- **over-coarseness:** all forms proving the same result become one method.

The protocol avoids both in this case.

- Ramified terms, generic filters, and Boolean values are not counted as separate methods merely because they differ.
- The pairwise audit still records genuine operation-architecture differences.
- The generic-filter↔Boolean equivalence is decided by exact preservation of genericity, names, truth, and extension, not by same conclusion.
- The ramified pairs remain qualified because historical and full-operation preservation are incomplete.

The representation-invariance test therefore produces a stable higher-level family verdict without erasing representation-specific operations.

### 11.3 Why it is only qualified

The protocol uses “method,” “distinct operation candidate,” and “method family” without explicitly specifying their level relation. This dossier had to distinguish:

1. historical operation token;
2. representation-specific operation;
3. representation-neutral method family.

That distinction follows from the frozen granularity and representation-invariance tests, but it is not itself an independently preregistered clause. The outcome therefore cannot count as clean independent validation.

### 11.4 Potential v0.2 issue, not a v0.2 proposal

If later controls or D06 require a protocol revision, a separately preregistered v0.2 should consider adding an explicit output field for:

- token identity;
- representation-specific operation identity;
- method-family membership;
- and the level of preserved role: conclusion, extension, truth relation, or full operation.

This PR does not create v0.2 and does not recommend any wording change to v0.1 based on the outcome.

### 11.5 Falsification conditions carried forward

The protocol would be falsified or more strongly qualified if later evidence showed any of the following:

1. no non-circular family core can be stated without merely saying “all are called forcing” or “all prove consistency”;
2. the generic-filter↔Boolean conversion preserves only outputs and not the load-bearing generation relation;
3. the family verdict changes merely by choosing poset rather than Boolean notation;
4. a new intermediate object with no new generative role is classified as a new method;
5. or the controls cannot be distinguished under the same level of individuation.

None is established here.

---

## 12. Provisional D06 Target-Object Specification

**Status:** provisional and qualified. This section specifies the target only. It does not adjudicate `H`, `N`, or `S`.

### 12.1 D06 target

D06 should audit the **bounded forcing method family** defined in §4.2:

> ordered partial information + background-definable forcing/Boolean truth + generic coherence or equivalent quotient + term/name interpretation + truth in a model extension.

The target is not one literal notation and not the entire mature forcing tradition.

### 12.2 Inclusion criteria

An operation or representation is included in the D06 target only if all are documented:

1. it contains a condition-like ordered approximation or its dense Boolean equivalent;
2. it has a forcing or Boolean truth relation internal to the background;
3. it supplies generic coherence through a complete sequence, filter, ultrafilter, or equivalent realization;
4. it interprets terms or names;
5. it generates an ordinary extension or has a documented theorem-level route to the same extension-generating relation;
6. the role survives the frozen representation-invariance and load-bearing tests.

Included as representations:

- Cohen's original ramified operation, as the historical event token;
- the unramified partial-order/generic-filter/generic-extension operation;
- the complete-Boolean-algebra/Boolean-valued operation when the extension-generating or exact equivalent semantic role is documented.

### 12.3 Exclusion criteria

Exclude from the single `m`:

- the proof goal “relative consistency”;
- CH or `not-CH` as outputs;
- a single forcing notion or application;
- Cohen's ramified language considered by itself;
- genericity considered without a forcing/truth relation;
- a Boolean-valued model with no documented relation to the target extension role;
- institutional uptake, textbooks, and training, which are evidence for `H/S`, not components smuggled into `m`;
- and all later descendants merely because they use forcing vocabulary.

### 12.4 Cohen event versus institutionalized forcing

The **Cohen event** is a historical token and first verified representation of the family. It should be used to establish:

- the event-stage operation;
- its characteristic resource;
- its output;
- and the earliest documented generation relation.

**Institutionalized forcing** is a later practice state in which representations, applications, inheritance chains, preservation tools, teaching, and infrastructure may accumulate. It is not identical to Cohen's token and must not be treated as already present in 1963–1964.

D06 must therefore keep two records:

1. `m_event`: the Cohen token, used for origin and event-level comparison;
2. `m_family`: the bounded family, used as the provisional subject of `H/N/S`.

These labels are expository in this dossier and introduce no new formal symbol into the frozen strategy or manuscript.

### 12.5 Later iteration, preservation, forcing axioms, and generic absoluteness

| Later development | Provisional classification relative to the D06 target | Reason |
|---|---|---|
| Iterated forcing | **inheritance and extension of the same family**, but each iteration architecture may be a distinct operation candidate | It composes forcing operations and adds support/limit machinery; the base forcing core remains, but the composition resource can be load-bearing. |
| Preservation theorems and preservation technology | **subsequent scaffolding** | They determine when iterations retain cardinals, chain conditions, properness, etc.; they are infrastructure around forcing, not the base generic-extension operation itself. |
| Forcing axioms | **downstream principles enabled by the family; not the same operation** | They are statements/principles asserting generic-filter existence patterns and are not identical to performing a forcing construction. |
| Generic absoluteness | **downstream theorem/program; not the base operation** | It concerns invariance of truth across selected extensions and may use forcing plus large-cardinal resources; it should not be folded into one `m`. |
| Boolean and category-algebra iteration systems | **representation-specific inherited extensions** | Same-family status requires separate load-bearing and representation tests at the iteration level. |
| Individual forcing notions | **instances or operation parameters, not the whole family** | `Cohen`, `random`, `collapse`, `proper`, etc. may differ in resources and preservation properties while instantiating the family core. |

This classification is provisional and may generate later evidence obligations. It is not an `H/N/S` result.

### 12.6 What `H`, `N`, and `S` should predicate

- **`H(m)` — heritability:** predicate of the bounded family core and its reproducible representations. Evidence should show that researchers can reconstruct, learn, and reuse the operation beyond Cohen's private/event-specific procedure.
- **`N(m)` — non-locality:** predicate of the same family across multiple problems, model classes, or proof tasks. It must not be inferred from many variants of one CH construction alone.
- **`S(m)` — scaffold formation:** predicate of durable downstream infrastructure built around the family—iteration, preservation, standard languages, training, and tools. The scaffolding is evidence about the family; it is not silently included as a component of the family being tested.

### 12.7 Objects that must not be mixed into one `m`

Do not combine:

1. Cohen's literal ramified token;
2. the representation-neutral forcing family;
3. a particular forcing poset;
4. a Boolean completion;
5. a specific theorem output;
6. a syntactic consistency transformation;
7. iteration and support technology;
8. forcing axioms;
9. generic absoluteness;
10. and the institutional ecology of textbooks, seminars, notation, and training.

Mixing them would make `H/N/S` either trivially true by definition or impossible to interpret.

### 12.8 D06 stop rule

If `EVD-D05-0005` and `EVD-D05-0006` reveal that no stable family-level subject survives the direct mapping and endpoint distinction, D06 must remain provisional and must not issue final `H/N/S` verdicts. The present `qualified_same_method_family` verdict is sufficient to specify a bounded target for evidence collection, not sufficient to adjudicate institutionalization.

---

## 13. Active counterexamples and failure conditions

The audit actively tested the following possibilities.

| Possibility | Result |
|---|---|
| Ramified language is an eliminable shell while conditions, forcing, and generic completion carry the core | **supported, with qualification**: ramification is not in the minimal family core, but it remains part of the historical token. |
| Generic-filter formulation changes the operation object rather than merely notation | **supported**: it replaces the complete sequence/ramified assembly with an abstract poset/filter/name operation. This creates a different representation-specific operation, not a different higher family. |
| Boolean-valued method preserves result and semantics but changes generation mechanism | **partly supported**: with generic ultrafilter, exact generation is recovered; without it, the proof may stop at a weaker semantic endpoint. |
| Representations share an abstract operation role but are not historically the same operation | **supported**. |
| “All produce generic extensions” is too coarse | **supported as a warning**: the audit requires preservation of approximation, coherence, interpretation, and truth roles, not output alone. |
| Comparing every intermediate object is too fine | **supported as a warning**: dense-equivalent posets and Boolean completions show that intermediate-object identity is not method identity. |
| Representation-neutrality falsifies v0.1 | **not established**: the protocol survives but is qualified by the level-of-individuation interface. |

Mandatory withdrawal conditions:

- Withdraw the higher-family verdict if exact technical evidence defeats the poset/Boolean preservation chain.
- Downgrade ramified↔generic-filter to `unresolved` if `EVD-D05-0005` shows that only output equivalence, not generation-role preservation, is documented.
- Exclude direct Boolean-validity proofs from D06 if `EVD-D05-0006` shows they lack the target extension-generating role.
- Do not proceed to final D06 adjudication if the target cannot be kept stable without retrospective tuning.

---

## 14. Non-claims

Nothing in this dossier establishes that:

- forcing was institutionalized;
- forcing satisfies `H`, `N`, or `S`;
- forcing changed the CH-local research regime;
- forcing changed the global update regime of set theory;
- C2 failed;
- strong semantic re-individuation occurred;
- either control case has the expected outcome;
- `EVD-D05-0001` should be upgraded;
- D05-T02 is unconditionally defeated;
- or SRT received support.

The result is a method-family and target-object audit only.
