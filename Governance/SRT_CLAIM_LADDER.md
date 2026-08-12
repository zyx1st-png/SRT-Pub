---
id: SRT-CLAIM-LADDER
type: governance
tags: [Governance, Claim Ladder, Canonical, Bridge, Lab, Manifesto]
status: active_v1_1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CANONICAL-FREEZE, SRT-EDIT-PROTOCOL, SRT-CANONICAL-REGISTRY]
---

# SRT Claim Ladder

> **Purpose**: This file defines proposition-level hardness. File role and claim role are related but not identical: a canonical file may contain bridge claims, and a bridge file may quote primitive axioms. The claim level must be explicit whenever hardness matters.

## 0. Core Rule

Never let a lower-hardness claim wear the voice of a higher-hardness claim.

In particular, domain files must not present P3/P4/P5 claims as if they were P0/P1.

---

## 0A. Gate 0 — L₀ Contentless Structurality Boundary

> **Status**: governance-canonical **type / boundary rule**. Adopted 2026-08-11.
> **This file is the single primary authority for Gate 0.** `_SRT_SYMBOL_TABLE.md` Usage Rule 16 is a cross-reference for symbol users and does not restate the rule's content.
> **Gate 0 carries no P-level.** It is **not** a P0 axiom, **not** a P1 theorem, **not** a physics claim, and **not** a new ontological quantity. §0 governs the *hardness* a claim may wear; §0A governs the *kind* of object that may sit at L₀. The two are orthogonal.
> **Adjudication record**: `Operations/Proposals/SRT_GATE0_L0_CONTENTLESS_STRUCTURALITY_DECISION_2026-08-11.md`.

### The rule

**A contentful direction, goal, optimum, value, or semantic order is not primitive at L₀ merely because it can be written globally.** L₀ may carry universal, position-independent **structural** invariants; it may not carry semantic or evaluative content, and a global notation does not convert the second into the first.

### The three classes

| Class | Nature | Members currently admitted / named | Admission at bare L₀ |
|---|---|---|---|
| **A** | primitive / contentless structural | structured potentiality (with intrinsic granularity) · `κ₀` · `ε_pg` · irreversibility floor | **allowed** |
| **B** | reference- / regime- / source-dependent weighting or comparative object | probability measure or prior over latent possibilities · entropy over `L₀` · reachable / accessible comparative quantities · any construct whose value requires a reference structure | **admission gap** — see below |
| **C** | semantic / evaluative / contentful | semantic target · good / value · telos · 「order」 as content · 初心 as a global contentful direction · universe-wide preferred world-state · global semantic or evaluative optimum | **not admissible as a bare L₀ primitive** |

**Class A is open, not closed.** The listed members are those currently committed; the class does not assert they are independent, jointly complete, or irreducible, and a future invariant of the same type must pass its own admission. (The `κ₀` / `ε_pg` dependency-graph audit remains deferred — `_SRT_SYMBOL_TABLE.md` Usage Rule 15.)

**Class B is an admission gap, not a prohibition in kind.** The rule is:

> Current core does not license such an object unless its required reference structure is **stated or independently derived**.

This must **not** be written as "L₀ forbids a natural measure." A future, independently justified canonical natural measure remains open. Gate 0's function here is only to stop global notation from hiding a missing commitment.

### Ordering discipline

**Structural cost ordering ≠ semantic / value ranking ≠ preferred endpoint / telos.**

`κ₀` induces an anisotropic cost geometry (some directions are cheaper) and `ε_pg` induces a two-class structural preference (`B ≥ 2` over `B ≤ 1`). **Both produce an ordering and both remain class A.** What class C forbids is a *complete semantic or evaluative ranking of latent world-states* and any *preferred endpoint*. Do not read any ordering as content — that misreading would come for `κ₀` and `ε_pg`, which Gate 0 exists in part to protect.

### Declaration requirement for situated / contentful objects

A situated or contentful object must **declare the reference structures its content actually depends on**.

Ordinarily required at minimum:

- a finite operator / position;
- a declared admissible or reachable domain.

Required **conditionally, when and only when the object depends on them**:

- historical constraints — only when the object is history-dependent;
- a probability measure — only when probability or entropy is used;
- a payability / reachability horizon — when claiming reachable- or accessibility-relative quantities;
- any other index the construct depends on.

These are **typing / admission requirements, not a sufficient construction recipe.** Satisfying them makes an object well-posed; it does not make any particular content correct. History is deliberately *not* universally required: a first situated manifestation may arise before any `L_2` historical sediment exists (`Core_Law/SRT_L0_Metaphysics.md` Ax-L0-Bootstrap; `Core/SRT_Core_12a` T-L0-Kappa0).

### Read-back rule

「order」, 「初心 / original intention」, 「good」, and 「global convergence」 may exist as **L₁/P2 read-back, regulative language, or domain bridge** — but may not back-define L₀.

**"Back-define" includes the indirect route**: a canonical anchor may not import an L₀-level reading of these terms by cross-referencing a `canonical: false` bridge or translation file. **Direction of citation is part of this rule**, not a separate courtesy.

### What Gate 0 does not do

It does not decide Gate A, Gate B, or Gate C (`Core/SRT_OPEN_TENSIONS.md §15 / §16 / §17`) — it bounds their option spaces. It does not resolve `κ₀`'s ontological status, and is neutral across the positions in `Philosophy/SRT_L0_Ontological_Status.md`, because it constrains *content*, not *mode of existence*. It introduces no symbol.

---

## 1. Claim Levels

| Level | Name | Definition | Allowed Voice |
|---:|---|---|---|
| P0 | Primitive axiom | A minimal SRT axiom without which the core grammar fails. It does not depend on a domain bridge, empirical threshold, or external theory. | "SRT assumes..."; "Within SRT, this is primitive..."; "Without this, the framework does not stand..." |
| P1 | Constitutive theorem | A claim treated as following from the SRT core structure. It is not primitive, but it is internally constitutive once P0 is granted. | "SRT entails..."; "Constitutively..."; "Given the core axioms..." |
| P2 | Canonical interpretation | A stable interpretive reading used across SRT, but not a primitive or theorem. It organizes meaning and usage. | "SRT reads this as..."; "Canonical interpretation..."; "Use this as the default reading..." |
| P3 | Bridge mapping | A mapping between SRT and another theory, domain, model, or scale. It may be useful and strong, but it depends on an interface. | "maps to..."; "can be modeled as..."; "bridge claim..."; "under this mapping..." |
| P4 | Lab hypothesis | A testable, measurable, empirical, or threshold-bearing claim. It may generate predictions or operational proxies. | "hypothesis..."; "candidate proxy..."; "to be tested..."; "under these measurement conditions..." |
| P5 | Phenomenological / companion exposition | A lived, pedagogical, literary, praxis, or companion explanation. It may be valuable but does not bear core-theory proof load. | "as exposition..."; "phenomenologically..."; "companion reading..."; "helps describe..." |

---

## 2. Relation to File Roles

File roles and claim levels do not automatically determine each other.

| File role | Typical claim levels | Rule |
|---|---|---|
| canonical | P0-P2, with occasional marked P3/P4 | Must mark mixed lower-hardness claims clearly |
| compact core | P1-P3 | May summarize P0/P1 but should link to canonical sources |
| bridge | P2-P4 | Must not silently upgrade mappings into axioms |
| lab | P4 | Must keep measurement/proxy conditions visible |
| navigation / registry / index | usually no substantive claim level | Should route to sources, not define theory |
| companion / praxis / public exposition | P5 plus quoted P0-P2 | Must distinguish explanation from definition |

The same file may mix P-levels. If it does, mark the level at least at section level. Inline marking is preferred for high-risk statements.

---

## 2A. `claim_mode: manifesto`

A `manifesto` claim mode authorizes worldview-level rhetorical compression while keeping the claim ladder load-bearing. It exists so that SRT can have a public-facing front-edge document without inviting silent P3-as-P0 inflation.

**Scope**: applies to files under `Manifesto/` and to any first-screen reference block in `README.md` that quotes a manifesto center sentence.

**Allowed**:

- Restate already-canonical P0/P1/P2 claims in slogan, compressed, or metaphorical form.
- Place P0 (hard) and P3 (bridge) claims in the same paragraph or center sentence, **provided the paragraph itself carries inline claim-level tags distinguishing them**.
- Bilingual parallel passages (e.g., Chinese + English) where the non-Chinese line is a rhetorical mirror, not an independent assertion.

**Forbidden**:

- Introducing any new P0 or P1 claim. New claims must first pass through `Core/`, `Core_Law/`, or `Governance/` promotion before a manifesto may quote them.
- Hiding P3/P4 hardness behind P0-style phrasing. Bridge claims must remain bridge claims even in slogan form.
- Coining new symbols, operators, or domain names. Manifestos only reference symbols already registered in `_SRT_SYMBOL_TABLE.md`.
- Single-file deferred footers as a substitute for inline tagging.

**Inline tag rule**:

- Every reversal proposition, center sentence, and free-standing assertion paragraph must carry an inline claim tag in `[P0-XX]` / `[P1, canonical]` / `[P2, canonical]` / `[P3, bridge]` / `[P3, conjectural]` / `[P4, speculative]` / `[P5, exposition]` form.
- Tags must appear in the same line or paragraph as the claim, not in a separate footnote section.
- When a center sentence compresses (a) P0 + (b) P3, the two halves must be sub-labeled `(a)` and `(b)` and tagged separately at least once in the file.

**Frontmatter requirement**:

A manifesto-mode file's YAML frontmatter must include:

- `claim_mode: manifesto`
- `audience: human_public`
- `manifesto_version: vX.Y`
- `anchored_claims:` — explicit list of canonical anchor IDs (e.g., `P0-01`, `P3-B07`, `PSI-F-CANONICAL`) the manifesto draws from
- `last_review: YYYY-MM-DD`
- `review_window_until: YYYY-MM-DD` — date for the next mandated reception review

**Versioning and trace**:

Any change to a manifesto's center sentence (Layer A / Layer B / Layer C) must be logged as a separate `Operations/` entry on the day of the change.

**AI session boundary**:

Manifesto files are human-first entries. They are **not** part of the AI session bootstrap defined in `AGENTS.md §Session Start`. AI agents read manifesto material only when the task involves user-facing framing.

**Relation to existing modes**:

- `claim_mode: manifesto` is rhetorically less constrained than `canonical` but governance-wise more constrained than `mixed`: it authorizes compression in exchange for mandatory inline tagging.
- It does not grant manifestos any authority over canonical files. Canonical files always outrank manifesto restatements.

---

## 3. Level-Specific Tests

### P0 Test

A statement can be P0 only if:

1. Removing it breaks SRT's core grammar.
2. It does not require empirical data to become meaningful.
3. It does not borrow authority from another theory.
4. It is not more cleanly derivable from other SRT claims.

Failure of any condition means demote.

### P1 Test

A statement can be P1 only if:

1. Its premises are already P0 or accepted P1.
2. The derivation path is stated or obvious from the formal context.
3. Its negation would break the SRT structure or carry a high internal contradiction cost.

If it depends on a domain mapping or threshold, it is not P1.

### P2 Test

A statement can be P2 when:

1. SRT repeatedly uses it as a stable interpretation.
2. It clarifies the meaning of core terms.
3. It does not by itself claim external validation.

P2 may be canonical in practice without becoming P0/P1.

### P3 Test

A statement is P3 when it says that an SRT structure maps onto another theory, domain, or scale.

Typical markers:

- "physics-scale realization"
- "AI analogue"
- "neuroscience implementation"
- "Fisher / information-theory expression"
- "spirituality / praxis reading"

P3 can be strong. It is still not a primitive axiom.

### P4 Test

A statement is P4 when it involves:

- thresholds
- empirical proxies
- measurable predictions
- falsification conditions
- operational criteria
- lab or field validation

P4 should name its measurement boundary whenever possible.

### P5 Test

A statement is P5 when its main function is:

- human orientation
- lived description
- metaphor
- companion exposition
- practice guidance
- pedagogical compression

P5 may be important for understanding, but it cannot carry proof load.

---

## 4. Mixed Files

A file may contain different P-levels if one of the following is true:

1. The frontmatter declares `claim_mode: mixed`.
2. The file has a claim-level map near the top.
3. Each major section marks its level.

Recommended section prefix:

- `P0-Ax`
- `P1-T`
- `P2-Interp`
- `P3-Bridge`
- `P4-Hyp`
- `P5-Companion`

For older files, a short header block is enough:

```md
> Claim-level note: this file is mainly P3 bridge. It quotes P0/P1 claims but does not define them.
```

---

## 5. Promotion and Demotion

### Promotion

A claim may be promoted only when the missing support is explicit:

- P4 -> P3: empirical proxy becomes a stable bridge mapping.
- P3 -> P2: mapping becomes a stable SRT interpretation not dependent on the external domain.
- P2 -> P1: interpretation is shown to follow from the core structure.
- P1 -> P0: only in rare cases where the theorem is discovered to be primitive and non-derivable.

Promotions touching P0/P1 must cross-check:

1. `_SRT_SYMBOL_TABLE.md`
2. `CANONICAL_REGISTRY.md`
3. the relevant core/canonical file

### Demotion

Demotion is not deletion. It means:

- the claim remains available;
- its proof burden is lowered;
- its voice becomes more honest;
- domain files lose permission to quote it as primitive.

This is the default response to ambiguity.

---

## 6. Domain Rule

Domain files may support, test, interpret, or expose SRT. They may not reverse-define the SRT core.

Minimum header for domain main files:

```md
> Role: [bridge / companion / praxis / domain exposition]
> Claim level: mainly P3/P4/P5, with explicit back-links to P0/P1 sources.
> Does not define: primitive axioms, d-value, Ψ_f, T_dir, L0/L1/L2, or real choice moment.
> Depends on: [canonical files]
```

If a domain file needs a new P0/P1 claim, it must be moved or mirrored into the appropriate core/canonical file through the edit protocol.

---

## 7. Citation Rules

When citing a claim:

- Cite P0/P1 claims from core/canonical files.
- Cite P2 interpretations with the phrase "canonical interpretation" when hardness matters.
- Cite P3 mappings with the phrase "bridge" or "mapping."
- Cite P4 claims with the phrase "hypothesis," "proxy," or "candidate criterion."
- Cite P5 material as exposition, not evidence.

Forbidden citation pattern:

> "Because the AI file says X, SRT's primitive axiom is X."

Allowed citation pattern:

> "The AI file uses X as a P3 bridge mapping back to the P0/P1 core in..."

---

## 8. Current Immediate Application

`Core/SRT_Core_21_Formal_Axioms.md` has been split into:

- `Core/SRT_Core_21_Minimal_Axioms.md` — P0
- `Core/SRT_Core_21b_Constitutive_Theorems.md` — P1
- `Core/SRT_Core_21c_Bridge_Hypotheses.md` — P2/P3/P4

This split changes epistemic placement, not the underlying intended theory.
