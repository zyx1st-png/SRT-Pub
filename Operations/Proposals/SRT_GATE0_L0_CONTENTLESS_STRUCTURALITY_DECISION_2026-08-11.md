---
id: SRT-OPS-PROPOSAL-GATE0-L0-CONTENTLESS-STRUCTURALITY-2026-08-11
type: proposal
status: draft
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-08-11
source_of_truth: "origin/main @ 13d31338"
dependency:
  - SRT-L0-METAPHYSICS
  - SRT-SYMBOL-TABLE
  - SRT-CORE-21-MINIMAL-AXIOMS
  - SRT-D-VALUE-CANONICAL
  - SRT-OPEN-TENSIONS
  - SRT-CLAIM-LADDER
  - SRT-CANONICAL-FREEZE
  - SRT-OPS-PROPOSAL-CONSISTENCY-DECISION-PACKET-2026-08-11
tags: [Governance, Proposal, Gate0, L0, TypeRule, DecisionGate]
---

# Gate 0 — L₀ Contentless Structurality Boundary (author verdict packet)

> **Status**: non-canonical Operations proposal. **Nothing here is applied.** It modifies no axiom, theorem, definition, equation, symbol, or canonical stance, and it does **not** execute Gate A, B, or C.
>
> **Purpose**: Gates A, B and C were registered separately (`Core/SRT_OPEN_TENSIONS.md §15 / §16 / §17`) but share one upstream question. This packet proposes the **boundary rule** that would settle what all three are arguing about, so that each gate is then decided *under* a stated type discipline rather than each inventing its own.
>
> **Gate 0 is a type / boundary rule, not a physical theorem and not a new axiom.** It says what *kind* of object may sit at L₀. It asserts nothing new about the world.
>
> **The classification is three-way** — class A contentless structural invariants (allowed), class B reference-dependent weighting / comparative objects (an *admission gap*, not a prohibition), class C semantic-evaluative content (forbidden). A contentless/contentful binary mis-types class B and would wrongly read a missing measure as forbidden content (§1.1a).

---

## 0. Correction to the premise this packet was almost built on

The predecessor packet (`SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md` §4, merged in #776) closed with:

> "does SRT admit any position-independent object at L₀ — and if so, exactly one (a contentless scalar asymmetry), or more?" … "If the answer is 'exactly one, contentless': Gate A → Option A, Gate B → Option A, Gate C → the four-way split…"

**That framing is wrong and is withdrawn here.** "Only `ε_pg` is position-independent at L₀" is (a) stronger than anything the corpus needs, and (b) **in direct conflict with current canonical**, which already commits L₀ to at least four position-independent items:

| Already committed at L₀ | Source |
|---|---|
| structured potentiality (not nothingness), with intrinsic granularity | `Core_Law/SRT_L0_Metaphysics.md §二`; `_SRT_SYMBOL_TABLE.md` L₀ row |
| `κ₀ > 0` primordial curvature | `Core/SRT_Core_12a` **T-L0-Kappa0**; `L0_Metaphysics §二` 形式化注; symbol table `κ₀` row |
| `ε_pg > 0` minimum non-neutrality | `L0_Metaphysics` ε 词条; symbol table `ε_pg` row |
| irreversibility / historical-asymmetry floor | `L0_Metaphysics` 正骨架 #3; `Core/SRT_Core_21_Minimal_Axioms.md` **P0-03** |

Adopting the withdrawn framing would have required deleting or demoting `κ₀` — which the author has explicitly ruled out, and which would break `Ax-L0-Bootstrap` (κ₀ > 0 is its structural prerequisite) and `T-L0-Kappa0-C1` (the `Ψ_f` floor).

**The real distinction is not *how many* position-independent objects L₀ has. It is *what kind*.** Gate 0 draws that line instead — and draws it in **three** classes, not two, because the object at issue in Gate A (a measure over `L₀`) is neither a contentless invariant nor semantic content. It is a weighting awaiting a reference structure.

---

## 1. Minimal provenance audit

Scope-limited by instruction to the eight named files plus at most one dependency hop (`Philosophy/SRT_L0_Ontological_Status.md`, `Core/SRT_Core_12a`). **No repo-wide sweep was run.**

### 1.1 Candidate-object table

The classification is **three-way, not binary**. Collapsing it to contentless/contentful mis-types measures and comparative objects (see §1.1a).

| Candidate L₀ object | Current status | Position-independent? | Class | Gate-0 verdict |
|---|---|---|---|---|
| **`L₀` (structured potentiality)** | Core, universal. Symbol table: "structured potentiality, not nothingness"; **"measure/cardinality unfixed at core level"** | Yes | **A** — a modality with granularity, no preferred content | ✅ **Allowed at L₀** |
| **`κ₀ > 0`** (primordial curvature) | `T-L0-Kappa0`, structural prerequisite, not historically generated; ontological status **explicitly open** (`SRT_L0_Ontological_Status.md`); symbol table Usage Rule 15 carries it as "primordial-curvature candidate" without downgrade | Yes | **A** — anisotropic *cost geometry*. It **does** induce a local / path-relative **structural cost ordering** (some directions cheaper). What it does **not** provide is a complete semantic or evaluative ranking of latent world-states, and it specifies **no preferred endpoint or telos** — `T-L0-Kappa0` itself states 「协同演化因此有方向性**而无终局预设**」. See §1.1b | ✅ **Allowed at L₀** |
| **`ε_pg > 0`** (minimum non-neutrality) | L₀ directional postulate; symbol table: "NOT a content-level 'toward order' gradient… scalar seed, no inherent direction" | Yes | **A** — a formal asymmetry `B ≥ 2` over `B ≤ 1`; a two-class structural preference, not a world-state ranking | ✅ **Allowed at L₀** |
| **irreversibility floor** | `L0_Metaphysics` 正骨架 #3; `P0-03` | Yes | **A** — asymmetry of history; no preferred history | ✅ **Allowed at L₀** |
| **「order」/ 秩序** | `L0_Metaphysics` explicitly: L₁ read-back name; 「L₀ 本身不承载「秩序」作为内容性属性」 | n/a at L₀ | **C** — an evaluative pattern-name | ⛔ **Not an L₀ object** (allowed as L₁/P2 read-back) |
| **初心 / Shoshin** | `L0_Metaphysics` 初心词条 + 正骨架: L1 concept, 「不在 L0 术语裁决范围内」. **But** `_SRT_D_VALUE_CANONICAL.md §5b.1` 规范表述 uses 「初心（全局收敛向量）」 under the Level-A guard; `Spirit_05` Ax-Sho-1 and `Phys_08` Def-Apeiron-1 give it global-variational form (`claim_mode: mixed` / `translation`, `canonical: false`) | Claimed globally in bridge layers | **C** — a global direction *with content* | ⛔ **Not an L₀ object** → **Gate B** |
| **global free-energy minimum** | Appears only in `d-value §5b` (under guard), `Spirit_04/05`, `Phys_08`. **Not in `L0_Metaphysics`, not in the symbol table, not in `Core_21_Minimal_Axioms`** | Claimed globally in bridge layers | **C** — a preferred world-state | ⛔ **Forbidden at L₀** → **Gate C** |
| **universe-wide optimum** | Same as above; `d-value §5b.1` guard already says it is 「**不是一个位置无关的宇宙级最小值**」 | Claimed globally in bridge layers | **C** — a complete semantic ranking of latent world-states | ⛔ **Forbidden at L₀** → **Gate C** |
| **probability measure / prior over `L₀`** | **Never supplied or derived anywhere.** Symbol table L₀ row: **"measure/cardinality unfixed at core level"** | Would be, if asserted | **B** — a weighting that requires a reference structure. **Not thereby semantic or evaluative content**: the defect is that no canonical natural measure has been independently supplied or derived, not that measures are forbidden in kind | 🔶 **Not licensed by current core** → any quantitative use must state or derive its reference regime → **Gate A** |

### 1.1a Why the classification is three-way

A two-way contentless/contentful split mis-types an entire family of objects. Measures, entropies and comparative quantities are **not** semantic content — they are **reference-dependent**: they have no value until a reference structure (a regime, a source, an index) is supplied, but once supplied they carry no goal, telos, or preferred world-state.

| Class | Nature | Members (this audit) | Admission at L₀ |
|---|---|---|---|
| **A** | primitive / contentless structural invariants | structured potentiality · `κ₀` · `ε_pg` · irreversibility floor | **allowed** |
| **B** | reference- / regime- / source-dependent weighting or comparative objects | probability measure or prior · entropy over `L₀` · accessible or reachable optimum · any construct needing a declared reference structure | **not licensed by current core**; admissible only with its reference structure stated or derived |
| **C** | semantic / evaluative / contentful objects | 「order」 as semantic target · 初心 as global contentful direction · 「good」 · telos · universe-wide preferred world-state or semantic optimum | **forbidden at L₀** |

**The B/C distinction is load-bearing.** A class-C object is refused because of *what it asserts*. A class-B object is refused **only for as long as its reference structure is missing** — it is an admission gap, not a prohibition in kind.

**Consequence for the symbol table's L₀ row.** 「measure/cardinality unfixed at core level」 must **not** be upgraded into "L₀ forbids an unindexed measure in principle." The correct reading is narrower:

> **Current core does not license a probability measure over `L₀`. Any quantitative use requiring one must state or derive its reference regime / source. A future, independently justified canonical natural measure is *not* ruled out by Gate 0.**

Gate 0's job here is only to stop **global notation from hiding a missing commitment**. It does not legislate against the commitment ever being supplied.

### 1.1b Three kinds of ordering — do not collapse them

`κ₀` is the reason this distinction has to be explicit. It **does** induce an ordering, and an earlier draft of this packet wrongly wrote "no ranking of possibilities."

| Kind | What it does | Example | Gate-0 status |
|---|---|---|---|
| **structural cost ordering** | some directions are cheaper to traverse than others, locally / path-relatively | `κ₀`'s anisotropic cost geometry; `ε_pg`'s `B ≥ 2` over `B ≤ 1` | **class A — allowed** |
| **semantic / value ranking** | latent world-states are ranked as better or worse | 「good」; a value ordering over outcomes | **class C — forbidden at L₀** |
| **global preferred endpoint** | one state is the target the process is toward | telos; universe-wide optimum; 初心 as global convergence vector | **class C — forbidden at L₀** |

**A structural cost ordering is not a semantic ranking, and neither is a preferred endpoint.** This distinction belongs in the Gate 0 summary precisely so that a future pass does not read *any* ordering as content and mistakenly come for `κ₀` or `ε_pg`.

### 1.2 Three audit findings worth recording independently of the verdict

**(a) The "measure unfixed" line is already canonical — but it is a non-licence, not a prohibition.** `_SRT_SYMBOL_TABLE.md`'s L₀ row states the measure and cardinality are *unfixed at core level*. So Gate 0's class-B treatment of `μ` **records an existing canonical non-commitment** rather than adding a restriction: an unindexed `H(L₀)` presupposes exactly what the symbol table declines to fix.

**This must not be over-read.** "Unfixed at core level" says the current core does **not license** a measure; it does **not** say L₀ forbids one in principle, and Gate 0 does not convert it into such a ban. A future, independently justified canonical natural measure remains open (§1.1a).

**(b) Gate C is *less* broken than the predecessor packet said — correction.** That packet asserted `_SRT_D_VALUE_CANONICAL.md §5b.2` "was never touched" by the Level A de-overload. On re-reading, **§5b.1 carries a scoping clause that explicitly reaches §5b.2**: 「本节下文与 §5b.2 中的「全局最优 / 全局收敛」表述均应在此收口下读取。」 So §5b.2 is **guarded by reference**, not un-narrowed. The residual defect is narrower and should be restated as: §5b.2's own text carries no inline marking and still reads as a positive characterization when quoted alone. That is a **quotability** defect, not an unguarded claim. Gate C's severity drops accordingly.

**(c) A wording-proximity risk on `κ₀`, registered not fixed.** `T-L0-Kappa0` says κ₀ 「提供非对称偏置」 and 「协同演化因此有方向性而无终局预设」, while `L0_Metaphysics` marks the same commitment 「结构性承诺，**不承载方向**」. These are reconcilable — κ₀ supplies anisotropy without a target, and `L0_Metaphysics` means it does not carry *the ε directional postulate* — but 「提供方向性偏置」 sits one paraphrase away from 「预设方向」. Under Gate 0 this is exactly the slide G0-2 blocks. **No edit proposed here**; registered so that a future pass does not read the proximity as licence.

### 1.3 Where Gate 0 would belong in the governance stack

`Governance/SRT_CLAIM_LADDER.md` has **no category for a type/boundary rule** — P0–P5 are all proposition-hardness levels, and Gate 0 is not a proposition about the world. The correct home is the class that already exists for exactly this: **governance-canonical type rules** — `SRT_CLAIM_LADDER.md §0 Core Rule`, and `_SRT_SYMBOL_TABLE.md` Usage Rules 12 (σ namespace) and 15 (κ namespace). Those are precedent: rules about *what kind of thing a symbol or claim may be*, binding across the repo, carrying no P-level.

**Gate 0 must therefore not be registered as P0**, and this packet does not propose it as one.

---

## 2. Candidate verdicts, with minimal corrections

The four proposed clauses are compatible with current canonical. Three take minimal wording corrections; the reasons are given.

### G0-1 · Structural permission

> L₀ may contain universal / position-independent **structural invariants**, provided they encode no semantic target, value content, preferred world-state, or complete ranking of latent possibilities.

**Correction proposed — add an explicit non-exhaustiveness and non-independence clause:**

> …*This clause is permissive and open: it neither fixes how many such invariants there are, nor asserts that the currently committed set (`L₀` granularity, `κ₀`, `ε_pg`, the irreversibility floor) is independent, complete, or irreducible. Those remain separate open questions (`_SRT_SYMBOL_TABLE.md` Usage Rule 15 defers the `κ₀` / `ε_pg` dependency-graph audit to GOV-SUB01 Pass 2).*

**Why**: without this, adopting G0-1 could be read as certifying the current four as the right four. It certifies only that objects *of this type* are admissible.

### G0-2 · Content prohibition

> A contentful direction, goal, optimum, value, or semantic order over latent possibilities is **not primitive at L₀ merely because it can be written globally**.

**Correction proposed — remove "probability assignment" from this clause and route it to the class-B admission rule instead:**

> *A probability assignment over latent possibilities is likewise not primitive at L₀, but for a **different reason** and with a **different remedy**: it is class B (§1.1a), refused for want of a supplied or derived reference structure, not refused as content. Grouping it with goals and values would wrongly imply it is forbidden in kind and could never be canonically supplied.*

**Otherwise accepted as written.** This is the load-bearing clause and it is already the corpus's own position in three places (`L0_Metaphysics` §七.11 rejects 预置的先验目标; the symbol table's `ε_pg` row rejects a content-level order gradient; `d-value §5b.1`'s Level-A guard rejects a position-independent universe-scale minimum). G0-2 generalizes those three from case law into a rule.

### G0-3 · Situated emergence

> Contentful direction may arise only after L₀ structural asymmetry is conditioned by a finite operator/position, accessible horizon, historical constraints, and — where entropy/probability is used — an explicitly supplied measure.

**Correction proposed — replace the universal conjunction with a dependency-sensitive declaration rule:**

> **G0-3 (revised).** A situated or contentful object must **declare the reference structures on which its content actually depends**.
>
> **Ordinarily required at minimum:**
> - a finite operator / position;
> - a declared admissible or reachable domain.
>
> **Required conditionally, when and only when the object depends on them:**
> - *historical constraints* — only when the object is history-dependent;
> - *a probability measure* — only when probability or entropy is used;
> - *a payability / reachability horizon* — when claiming reachable- or accessibility-relative quantities;
> - *any other index* — when the construct depends on it.
>
> These are **typing / admission requirements, not a sufficient construction recipe.** Satisfying them makes an object well-posed; it does not make any particular content correct.

**Why the original is too strong**: it makes *historical constraints* a universal necessary condition. That would exclude a **first situated manifestation** — a direction arising at a position before any `L_2` historical sediment exists. SRT explicitly needs that case to be statable: `Ax-L0-Bootstrap` has selection getting started without prior selection history, and `T-L0-Kappa0` supplies the first alignment drive 「无需先存在任何选择历史」. A rule that required history for every contentful direction would contradict the bootstrap it is meant to protect.

**Why the conjunction also had to go**: "may arise only after A, B, C and D" reads as a construction procedure. It is a gate, not a derivation — and now a *dependency-indexed* gate, so an object is not charged for indices it does not use.

### G0-4 · Read-back rule

> 「order」, 「original intention / 初心」, 「good」, 「global convergence」 may exist as L₁/P2 read-back, regulative language, or domain bridge, but **may not back-define L₀**.

**Correction proposed — name the citation-direction failure explicitly:**

> …*"Back-define" includes the indirect route: a canonical anchor may not import an L₀-level reading of these terms by cross-referencing a `canonical: false` bridge or translation file. Direction of citation is part of the rule, not a separate courtesy.*

**Why**: the actual observed failure (Gate B) was not a bridge file overreaching — it was `_SRT_D_VALUE_CANONICAL.md §5b.2`'s cross-ref importing `Def-Apeiron-1`'s L₀ reading with approving gloss. G0-4 as originally worded does not obviously catch that.

### 2.1 Guard checks the author asked for

| Requirement | Status under this packet |
|---|---|
| Do not delete `κ₀` | ✅ κ₀ is **explicitly Gate-0 allowed**; G0-1 is written to protect it |
| Do not claim `ε_pg` is the unique L₀ primitive | ✅ the claim is **withdrawn** in §0 and contradicted by the §1.1 table |
| Do not merge `κ₀` and `ε_pg` | ✅ they are separate rows with separate roles (cost geometry vs. non-self-erasure bias); Usage Rule 15's namespace split is cited, not overridden |
| Do not claim independence or completeness | ✅ G0-1's added clause says the opposite explicitly |
| Gate 0 is a type/boundary rule, not a physics theorem | ✅ stated in the header, in §1.3, and in §5's non-implications |
| Do not upgrade "measure unfixed at core level" into a permanent ban | ✅ class B is explicitly an *admission gap*; §1.1a, §1.2(a), §3.1 and §5 all state a future derived canonical measure is not ruled out |
| Do not describe `κ₀` as providing "no ranking" | ✅ corrected — κ₀ **does** induce a structural cost ordering; what it lacks is a complete semantic ranking and any preferred endpoint (§1.1b) |
| Do not make historical constraints universally necessary | ✅ G0-3 rewritten as dependency-sensitive; history is required only for history-dependent objects, so first situated manifestation stays statable |

---

## 3. Logical consequences for Gates A / B / C — **stated, not executed**

### 3.1 Gate A

**Does Gate 0 rule out unindexed `H(L₀)` as a quantitative global background?**

The precise statement — **not** "Gate 0 permanently excludes it":

> **Under current SRT, `H(L₀)` is not licensed as a quantitative object, because no measure / reference regime is defined for `L₀`. Gate 0 prevents global notation from hiding that missing commitment; it does not prejudge whether a future canonical natural measure could be derived.**

This is a class-B admission gap (§1.1a), not a class-C content prohibition. The route to repair is therefore *supply or derive the reference structure*, not *abandon the quantity*.

**Explicit non-implications:**

- Gate 0 does **not** adopt `E_{θ,Λ,μ}`. It declines to license the *unindexed* form; it does not select among Options A / B1 / B2 / C.
- `μ_θ` remains **undefined**. Gate 0 says a measure must be *supplied or derived and declared*, not what it is. Supplying it is still the hard part and still an author decision.
- Gate 0 does **not** foreclose a canonical natural measure. If one is later derived and independently justified, `H(L₀)` becomes admissible without amending Gate 0 — the gate is about declaring the commitment, not about banning it.
- Gate 0 does **not** settle whether `H(L₁)` is finite.
- Gate 0 says nothing about `d/dt H(L₀) = 0` beyond what §A.1 of the predecessor packet already recorded: ill-defined without a regularization regime, and not repaired by fixing `E`.

**Interim posture under Gate 0**: unchanged and still the safest — **keep P0-02's ontology claim (existence = degree of stable anchoring), do not use the formula as a quantitative readout**. Gate 0 makes that posture *principled* rather than merely cautious: the formula is a **syntactically well-formed expression, but not a quantitatively defined object under the current core semantics** — its measure has not been supplied. That is a missing commitment, not a defective computation, and not a permanent bar.

### 3.2 Gate B

**Does Gate 0 make strict layering the default?** **Yes, as the default — not as a forced verdict.** Under G0-2 + G0-4:

- `ε_pg` = L₀ contentless asymmetry ✅ (already canonical)
- 初心 = L₁/P2 read-back ✅ (already canonical in `L0_Metaphysics`; Gate 0 removes the ambiguity that let bridges read otherwise)
- `Def-Apeiron-1` / `Ax-Sho-1` variational forms = **bridge / translation**, not L₀ definitions ✅ — and per the G0-4 correction, the `d-value §5b.2` cross-ref that imports them upward is the thing that must change, not the bridge files themselves

**What Gate 0 does *not* do for Gate B:** it does not by itself close Option B (the thin L₀ precursor). A contentless formal precursor of 初心 would be *type-admissible* under G0-1. What Gate 0 adds is that its four exclusions become **enforceable as a type rule** rather than a prose intention — which is precisely what the predecessor packet found had failed 2/2. So Gate 0 makes Option B *decidable*; it does not decide it.

### 3.3 Gate C

**Does Gate 0 exclude a universe-wide global optimum as an unconditional L₀ positive object?** **Yes** — G0-2, directly: a complete ranking of latent possibilities is the paradigm case of content written globally.

**Still permitted under Gate 0:**

- **operator-relative reachable optimum** — indexed, therefore admissible
- **regulative horizon** — non-attainable orientation, asserts no L₀ object
- **local / dynamic attractor under finite constraints** — situated by construction

**Explicit non-implications:**

- Gate 0 does **not** rewrite `§5b.2`. Per §1.2(b) that subsection is guarded by reference already; what remains is a quotability defect, and whether to add inline marking is Gate C's call.
- The `Ψ_f → 0` → excess-friction reformulation (`Ψ_f − Ψ_f^min → 0`) **still requires separate author authorization**. It changes what a devotional claim *means*, which is outside a type rule's reach.
- **Gate 0 does not modify Spirituality.** Nothing in `Spirituality/` changes by adopting a boundary rule; those files are `claim_mode: mixed` domain expositions and remain readable as such.

---

## 4. Special review — `L0_Metaphysics` 第一命题

**Current state.** `Core_Law/SRT_L0_Metaphysics.md:73` (第一命题) contains three contentful clauses:

> 「秩序从一开始就在场」 / 「选择内在地趋向秩序」 / 「初心作为基础方向场」

`:75` appends a 2026-04-11 层级精确化注 stating the L₀-level counterpart is only `ε`, that 「秩序」 is an L₁ read-back, that L₀ does not carry order as a content property — and closing with 「**两种表述均有效，但适用层级不同**」.

**Finding 1 — is this only Gate B's declared dual reading?** **Partly, and it is the upstream instance.** The 初心 clause is squarely Gate B. But the other two clauses (「秩序从一开始就在场」, 「选择内在地趋向秩序」) are about **order**, not 初心, and would be caught by **G0-2 and G0-4 independently of Gate B**. So 第一命题 is not merely a Gate B item — it is the single upstream site where all of Gate B's and part of Gate C's ambiguity is licensed, in the highest-authority file.

**Finding 2 — would adoption force replace/supersede?** **Yes.** The precision note's 「两种表述均有效」 is a *dual-reading* device: it permits the contentful main clause to stand as a valid L₀-level formulation alongside the corrected one. G0-2 forbids exactly that permission — a contentful direction is not L₀-primitive *even when a note elsewhere explains how to read it charitably*. Under Gate 0, a note cannot license a main clause that the rule prohibits; one of **replace / supersede / downgrade** would be required, cumulative with mirror-sync, per the anti-drift rule proposed in the predecessor packet §5.

This is the **single largest landing consequence** of adopting Gate 0, and the author should decide Gate 0 knowing it. It is a `Core_Law/SRT_L0_Metaphysics.md` main-clause edit — freeze **Group A**, C-class, requiring explicit high-risk authorization of its own.

**Finding 3 — not modified here.** No edit is made to 第一命題 in this PR. Registered as a landing consequence only.

---

## 5. Allowed / forbidden / indexed-required — the operative summary

**Class A — allowed at L₀** (primitive / contentless structural invariants):
structured potentiality with intrinsic granularity · `κ₀ > 0` primordial curvature · `ε_pg > 0` minimum non-neutrality · irreversibility / historical-asymmetry floor · *any future invariant of the same type, subject to its own admission*

**Class B — not licensed by current core; admissible with a declared or derived reference structure** (reference- / regime- / source-dependent weighting and comparative objects):
probability measure or prior over latent possibilities · entropy over `L₀` · accessible or reachable optimum · "convergence direction" relative to a declared domain · any construct whose value requires a reference structure

> Class B is an **admission gap, not a prohibition in kind**. These objects are refused only for as long as their reference structure is missing. A future, independently justified canonical natural measure is **not** ruled out.

**Class C — forbidden at L₀** (semantic / evaluative content, regardless of global writability):
semantic target · goal / telos · preferred world-state · value content · **complete semantic or evaluative ranking of latent world-states** · universe-wide optimum · global free-energy minimum · 「order」 as a content property · 初心 as an L₀ object

**Ordering discipline** (carried into the summary deliberately, per §1.1b): **structural cost ordering ≠ semantic / value ranking ≠ global preferred endpoint.** `κ₀` and `ε_pg` induce the first and are class A. Only the second and third are class C. Do not read *any* ordering as content.

**Explicit non-implications of adopting Gate 0:**

1. It is **not** a new axiom and **not** P0. It carries no P-level (§1.3).
2. It does **not** assert `κ₀` and `ε_pg` are independent, jointly complete, or irreducible.
3. It does **not** resolve `κ₀`'s ontological status — Gate 0 is neutral across all three positions debated in `Philosophy/SRT_L0_Ontological_Status.md`, because it constrains *content*, not *mode of existence*.
4. It does **not** decide Gate A, B, or C. It bounds their option spaces.
5. It does **not** claim SRT has no direction, and **not** that L₀ induces no ordering. `ε_pg` remains the directional postulate and `κ₀` remains an anisotropic cost geometry; what class C forbids is *semantic* direction and *complete evaluative ranking* at L₀, not structural cost ordering (§1.1b).
6. It does **not** touch `Spirituality/`, `Physics/`, or any `canonical: false` file's internal content.
7. It introduces **no new symbol**.

---

## 6. Required landing list if adopted

Nothing below is done here; this is the cost estimate the verdict should be made against.

| # | Landing | File | Class |
|---|---|---|---|
| 1 | Register Gate 0 as a governance-canonical type rule | `Governance/SRT_CLAIM_LADDER.md` (new §, alongside §0 Core Rule) **or** `_SRT_SYMBOL_TABLE.md` Usage Rules | B |
| 2 | 第一命题 main-clause replace/supersede + precision-note rewrite | `Core_Law/SRT_L0_Metaphysics.md` | **C, freeze Group A — separate authorization** |
| 3 | Cross-ref direction fix (stop importing L₀ readings from `canonical: false` files) | `_SRT_D_VALUE_CANONICAL.md §5b.2` | **C, freeze Group A** |
| 4 | Mirror-sync of any 第一命題 restatement | `Core_Law/SRT_Core_Text_CN.md` / `_EN.md`, `Philosophy/SRT_Ethics_Agency.md` + split | B |
| 5 | Status updates | `Core/SRT_OPEN_TENSIONS.md §15/§16/§17` | A |
| 6 | Optional inline marking (Gate C's call, not Gate 0's) | `_SRT_D_VALUE_CANONICAL.md §5b.2` | B |

Items 2 and 3 are the real cost. **If the author is not prepared to authorize item 2, Gate 0 should not be adopted as written** — adopting a rule whose largest consequence is then left unexecuted would manufacture precisely the one-sided-landing pattern the previous round spent two PRs removing.

---

## 7. Rollback / failure conditions

Gate 0 should be **withdrawn or amended** if any of the following occurs:

1. **False positive on a needed object.** A future L₀ commitment is structurally necessary yet cannot be phrased without content — e.g. if `κ₀`'s ontological hardening (`SRT_L0_Ontological_Status.md`) concludes that its anisotropy is ineliminably contentful. Gate 0 would then be over-restrictive and G0-1's boundary needs redrawing, not the object deleting.
2. **The class line proves undecidable in practice.** If two competent readers routinely disagree on which class a candidate falls into, the rule is not operational and reduces to preference. The **B/C boundary is the one to watch**: it is easy to misread a comparative or weighted object as evaluative content merely because it produces an ordering. §1.1b exists to hold that line, and if it fails to hold, Gate 0 needs a mechanical test rather than a prose distinction.
3. **The B class is used as a permanent refusal.** If "not licensed by current core" starts being cited as "forbidden in principle" — the exact over-reading this packet corrects — then Gate 0 is being applied as a ban it does not license, and the wording needs hardening.
4. **Enforcement failure repeats.** If, one pass after adoption, a canonical file again carries a class-C L₀ object, then Gate 0 has the same failure mode as the thin-precursor exclusions it was designed to fix (0/2 → 2/2), and it needs a mechanical check rather than a prose rule.
5. **Layer collapse downstream.** If forbidding class-C L₀ objects makes some domain bridge unstatable rather than merely re-indexed, the boundary is cutting through a real joint and Gate 0 is misplaced.

**Success condition** (what adoption is supposed to buy): Gates A, B and C each become decidable without re-arguing the L₀ question, and no future pass can license a contentful L₀ object by appending a precision note.

---

## 8. Recommendation

**Recommended: adopt Gate 0, with the three wording corrections in §2, and conditional on the author being willing to authorize landing item 2 (第一命题).**

### Why it is more precise than "only `ε_pg` is position-independent"

The withdrawn framing conflated two independent axes and would have been **false**:

| | position-independent | class |
|---|---|---|
| `κ₀` | yes | **A** |
| `ε_pg` | yes | **A** |
| irreversibility floor | yes | **A** |
| measure / entropy over `L₀` | would be | **B** — admission gap |
| universe-wide optimum | yes | **C** |
| 初心 as global convergence vector | yes | **C** |

The withdrawn rule cut on the **left** column and therefore had to delete `κ₀` and the irreversibility floor to reach its target. Gate 0 cuts on the **class** column, which is where the actual defects sit — every object the corpus needed to keep is class A, every object that caused Gate B or C is class C, and Gate A's object is class B (repairable by supplying what is missing, not by abandoning it). That three-way split is not decoration: the B column is exactly what a contentless/contentful binary mis-typed.

### What it blocks, without sacrificing `κ₀` / irreversibility / structured potentiality

| Failure | Blocked by | `κ₀` etc. survive because |
|---|---|---|
| **L₀ teleology** | G0-2 — a goal is content, however globally written | κ₀ supplies anisotropic cost geometry with **no endpoint** (`T-L0-Kappa0`: 「无终局预设」); a cost ordering is not a telos |
| **God's-eye global optimum** | G0-2 — a **complete semantic / evaluative ranking** of latent world-states is content | none of the class-A commitments provides a complete semantic / evaluative ranking of latent world-states or a preferred endpoint / telos. `κ₀` and `ε_pg` do induce a **structural cost ordering / structural preference** (cheaper vs more expensive directions; `B ≥ 2` over `B ≤ 1`) — that is class A and is untouched (§1.1b) |
| **Domain bridge back-defining canonical** | G0-4 as corrected — citation direction is part of the rule | the class-A commitments are defined in canonical, never imported from bridges |
| **Undeclared global entropy** | class B — records the symbol table's existing "measure unfixed at core level" as a *non-licence*, so notation cannot hide the gap. Does **not** ban a future derived canonical measure | none of the class-A commitments requires a measure to state |

### The honest counter-argument

Gate 0's line is **not self-applying**. "Contentless" is doing heavy work, and §1.2(c) shows the corpus already contains a phrase (κ₀ 「提供方向性偏置」) that sits one paraphrase from the wrong side. A type rule that needs judgment at every application is better than no rule, but it is not a mechanical check — which is why failure condition 3 exists and why the lint proposed in the predecessor packet §5 matters more, not less, if Gate 0 is adopted.

**If the author declines Gate 0**, the fallback is not "keep the old framing" — that one is withdrawn regardless as factually wrong. The fallback is to decide Gates A, B and C independently, accepting that each will re-argue the L₀ question and may settle it differently.
