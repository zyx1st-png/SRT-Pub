---
id: SRT-OPS-PROPOSAL-GATEB-SHOSHIN-LAYER-2026-08-12
type: proposal
status: draft
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-08-12
source_of_truth: "origin/main @ c2f6a7a0 (post #784 Gate 0 landing, post #788 ST-A/EX-A)"
dependency:
  - SRT-OPEN-TENSIONS
  - SRT-CLAIM-LADDER
  - SRT-L0-METAPHYSICS
  - SRT-D-VALUE-CANONICAL
  - SRT-SYMBOL-TABLE
  - SRT-CORE-21B-CONSTITUTIVE-THEOREMS
  - SRT-OPS-PROPOSAL-GATE0-L0-CONTENTLESS-STRUCTURALITY-2026-08-11
tags: [Governance, Proposal, GateB, Shoshin, L0, DecisionGate]
---

# Gate B — Layer Assignment of 初心 (author verdict packet)

> **Status**: non-canonical Operations proposal. **Nothing here is applied.** It modifies no axiom, theorem, definition, equation, symbol, or canonical stance. It executes no Gate. It proposes no edit to `Spirituality/` or `Physics/`.
>
> **Object**: the residual open question in `Core/SRT_OPEN_TENSIONS.md §16`, as narrowed by Gate 0 (`Governance/SRT_CLAIM_LADDER.md §0A`, adopted 2026-08-11).
>
> **Scope discipline**: Gate B is **not** "what is 初心". It is one type question — *may anything answering to 初心 sit at bare `L_0`, and if so what?* Its value content, phenomenology, and domain use are out of scope and stay where they are.

---

## 0. Re-verification — Gate B's premises moved twice since it was framed

Gate B was framed on 2026-08-11 against `main @ 8a5ef99a`. Two later merges changed its inputs. **Both must be on the table before the verdict.**

### 0.1 Gate 0 landed (#784) — the question is now narrower

Gate 0 settled that a **contentful** 初心 is **class C** and inadmissible as a bare `L_0` primitive, and closed the citation-direction leak at `_SRT_D_VALUE_CANONICAL.md §5b.2`. `Core_Law/SRT_L0_Metaphysics.md` 第一命题 was rewritten so its main clause no longer licenses an `L_0`-level 初心 reading.

So Gate B is **no longer** "is 初心 L₀ or L₁". That part is decided. What remains is exactly one question, stated in §2.

### 0.2 ST-A landed (#788) — it removes one specific motivation for Option B

This is the input that did not exist when Gate B's options were written.

`Core/SRT_Core_21b_Constitutive_Theorems.md` now records:

> **Former P1-T07: Unconditional Constitutive Asymmetry Claim (Demoted by ST-A)** … the former unconditional statement — "every stable ISP necessarily contains an anti-closure `ε` bias" — is **no longer a P1 theorem**.

and, decisively for Gate B:

> **`ε_pg` boundary**: `ε_pg` remains an `L_0` structural postulate and scalar seed. **ST-A does not derive an ISP-level anti-closure direction from it, nor from irreversibility alone.**

**Why this matters — stated narrowly.** One motivation for a "thin L₀ precursor of 初心" was that `ε_pg` grounds a directional bias which L₁ then reads back as 初心, so something at `L_0` must be doing the directing. ST-A **removes that specific `ε_pg` → ISP-level-anti-closure-direction motivation**: the step is now an explicitly underived conditional candidate (`Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`), not a theorem.

**What ST-A does and does not do here:**

- It does **not** prove that no distinct precursor can exist.
- It **removes one previously assumed derivation**, and therefore **weakens the current positive case** for adding an `L_0` commitment — the work such an object was imagined to underwrite is work SRT has now declined to claim.
- If a future explanatory gap **and** a T5-passing candidate appear, **Gate B can be reopened** (§9).

### 0.3 What did *not* change

`κ₀` retains its status and its class-A admission. The `κ₀` / `ε_pg` dependency and independence relation remains deferred (`_SRT_SYMBOL_TABLE.md` Usage Rule 15, GOV-SUB01 Pass 2) and **is not touched here**.

---

## 1. Bounded provenance audit (current `main @ c2f6a7a0`)

Scope-limited to the files that carry a 初心 layer commitment. **No repo-wide sweep.**

| Site | Authority | What it says now | Gate-0 class | State |
|---|---|---|---|---|
| `Core_Law/SRT_L0_Metaphysics.md` 初心词条 + 正骨架 | theory-canonical anchor, **freeze A** | 初心 is an **L1 concept**, outside L0's term adjudication; L0 commits only to `ε` | — | **correct, post-#784** |
| `Core_Law/SRT_L0_Metaphysics.md` 第一命题 | same | rewritten: L₀ carries `κ₀`/`ε`/irreversibility as **contentless** asymmetries; does **not** commit to 初心 as content | — | **correct, post-#784** |
| `_SRT_SYMBOL_TABLE.md` `ε_pg` row | governance-canonical | scalar seed, no inherent direction; **ST-A**: does not by itself yield an ISP-level direction | **A** | **correct, post-#788** |
| `_SRT_D_VALUE_CANONICAL.md §5b.2` cross-ref | theory-canonical anchor, **freeze A** | provenance-only, citation-direction guard; `Ax-Sho-1`/`Def-Apeiron-1` marked bridge/translation, may not back-define `L_0` | — | **correct, post-#784** |
| **`_SRT_D_VALUE_CANONICAL.md §5b.1` 规范表述** | theory-canonical anchor, **freeze A** | still contains `d ↑ ⇒ 局部最优 → 全局最优 ⇒ ⟨v, Shoshin⟩ > 0` and 「初心（**全局收敛向量**）」 | **C-shaped** | **residual — see §1.1** |
| `Spirituality/SRT_Spirit_05_Shoshin.md` `Ax-Sho-1` | `claim_mode: mixed` | 初心 as negative gradient of a long-horizon free-energy functional | **C** (as an L₀ claim) | bridge; **out of scope** |
| `Physics/SRT_Phys_08_Ontology_Ext.md` `Def-Apeiron-1` | `claim_mode: translation`, `canonical: false` | 初心 as `argmin ∫F`; 「$L_0$ 的内在属性」 | **C** (as an L₀ claim) | translation; **out of scope** |

### 1.1 One residual, recorded not fixed

`§5b.1`'s **normative expression** still writes 初心 as a **global convergence vector** inside a freeze-Group-A canonical file:

$$d \uparrow \;\Rightarrow\; \text{局部最优} \to \text{全局最优} \;\Rightarrow\; \langle v, \text{Shoshin} \rangle > 0$$

Three things must be kept apart here, and only the third is Gate B's:

1. **Is it guarded?** Yes. §5b.1's own Level-A clause (2026-07-05) states the 「全局最优」 reading depends on the unresolved closure-boundary and is 「不是一个位置无关的宇宙级最小值」, and scopes that reading over §5b.1 and §5b.2. So this is **not an unguarded claim**.
2. **Is the "global optimum" terminology settled?** No — that is **Gate C** (`§17`), still open.
3. **Does it assert an L₀-level 初心?** **No.** It is a claim about `d`-expansion alignment at the selection-dynamics layer, not about what `L_0` contains. It therefore does **not** violate Gate 0 and is **not** Gate B's to fix.

**Recorded so the next pass does not mistake it for a Gate B残留.** If the author wants the vector phrasing narrowed, that is a Gate C landing item, not this one.

---

## 2. The residual question, stated exactly

> **Is a strictly *contentless* formal precursor of 初心 admissible at bare `L_0` under Gate 0 class A — and if so, what is its relation to `ε_pg`?**

Everything else in §16 is decided. Note what the question is **not**: it is not whether 初心 is meaningful, not whether the L₁ read-back is legitimate (it is), and not whether Spirituality or Physics may use their variational forms (they may, as bridge/translation).

---

## 3. Gate 0 makes this decidable — the class-A admission test

Gate 0's class A is **open**: "a future invariant of the same type must pass its own admission." Before this, Option B's exclusions were a prose intention. Gate 0 converts them into a checkable admission. A candidate thin precursor `π₀` would have to clear all five:

On the two existing formulations: `Def-Apeiron-1` and `Ax-Sho-1` **do not qualify as bare-`L_0` candidates** — their global / variational forms carry content or reference commitments incompatible with bare class-A admission. That is **not** because variational syntax is forbidden in itself.

| # | Admission condition | Rationale |
|---|---|---|
| **T1** | **No hidden teleology or undeclared reference structure in a functional representation.** A functional representation is **not disqualifying by mathematical form alone**. It fails class-A admission if it encodes a preferred endpoint, a complete semantic/evaluative ranking, or requires an **undeclared** class-B reference structure. | Gate 0 forbids content and undeclared reference structure, not variational syntax. |
| **T2** | **No preferred endpoint.** `π₀` must not designate a target state, attractor, or limit toward which selection tends. | Class C: preferred endpoint. |
| **T3** | **No complete ranking.** `π₀` may induce a *structural cost ordering* (Gate 0 permits this — `κ₀` and `ε_pg` both do), but not a complete semantic or evaluative ranking of latent world-states. | Gate 0 ordering discipline. |
| **T4** | **No reference structure required.** If `π₀` needs a measure, horizon, or index to have content, it is class **B**, not class A, and is not an `L_0` primitive at all. | Class B/A boundary. |
| **T5** | **Non-redundancy.** Does `π₀` perform a **non-redundant structural role** not already carried by the current class-A commitments (`L_0` granularity, `κ₀`, `ε_pg`)? | Class A is a set of commitments, not synonyms. |

**T1–T4 fix the admissible type boundary; T5 is where any specific candidate is actually weighed.** Note what this test can and cannot do — see §5.1.

---

## 4. Option A — strict layering

`L_0` commits to `κ₀`, `ε_pg`, granularity and irreversibility. 初心 exists **only** as L₁/P2 read-back, regulative language, or domain bridge. No `L_0` precursor is admitted. Physics and Spirituality keep their variational forms **as bridge/translation** — unchanged internally, simply not L₀-defining (already true post-#784).

**For.**

- It is what the L0 anchor already says, in three places, and what #784 landed.
- Nothing currently needs an extra `L_0` object. Post-ST-A this is stronger than it was: the directional work a precursor was imagined to do is work SRT has **explicitly declined to derive** (§0.2).
- Zero new commitments, zero new enforcement surface.

**Against.**

- Physics/Spirituality variational forms become *purely* bridge — some may feel that under-describes a claim they take to be structural.
- It leaves the read-back asymmetry unexplained at `L_0`: if L₁ reliably reads back a direction, one may want an `L_0` story for *why that read-back is stable*.

  **Option A does not claim that `ε_pg` plus the amplification conditions already establish the stability of the read-back.** Its narrower claim is that **the current core has not established an explanatory gap that requires an additional `L_0` object**. If such a gap is later demonstrated, §16 should reopen (§9).

  The distinction is load-bearing: **absence of a demonstrated explanatory gap ≠ completed explanation by existing mechanisms.** Option A rests on the first, and asserts nothing about the hardness of `ε_pg` or of the amplification conditions — post-ST-A that hardness is itself not claimed (§0.2).

---

## 5. Option B — admit a thin contentless precursor

Admit exactly one additional class-A object `π₀`, deliberately **not** called 初心, passing T1–T5.

### 5.1 What the admission test can and cannot establish

**T1–T4 determine the admissible *type boundary*; they do not exhaustively enumerate class A.** Gate 0 states class A is **open, not closed**, and nothing in T1–T4 rules out a future contentless structural invariant, relation, or geometry of a **different type** from the ones currently committed. **T5 therefore cannot prove that no distinct precursor could ever exist.** It asks a narrower question: does any *specified* candidate perform a non-redundant structural role not already carried by the current class-A commitments?

**The current evidence, stated as such:**

- **No such candidate is presently specified in SRT.**
- The two existing Shoshin / Apeiron formulations **do not qualify as bare-`L_0` candidates** (§3).
- The obvious scalar non-neutrality role is **already occupied by `ε_pg`** — 「formal asymmetry favouring configurations with `B ≥ 2` over `B ≤ 1`… scalar seed, no inherent direction」.

**Therefore there is currently no positive warrant for adding another `L_0` commitment.** That is a verdict on the present candidate set, not a proof of impossibility.

**The honest steelman.** One could argue `π₀` should capture *the stability of the read-back* rather than the asymmetry itself — "the property of `L_0` in virtue of which the L₁ read-back converges across positions." Two responses, neither of which is a proof of impossibility:

- convergence across positions is already `L0_Metaphysics §三`'s **objectivity** criterion — a commitment SRT holds, not an additional `L_0` object;
- post-ST-A, SRT no longer claims the ISP-level direction is derived at all, so there is at present no established convergence for `π₀` to underwrite. If that changes, so does this assessment.

**For.** Would let `Def-Apeiron-1` and `Ax-Sho-1` be bridges *to a real `L_0` object* rather than to a read-back.

**Against.** Everything above, plus: with no candidate specified, adopting it would add an `L_0` commitment and an enforcement surface without a stated structural role to justify either.

---

## 6. Comparison

| Criterion | A — strict layering | B — thin precursor |
|---|---|---|
| Consistency with current canonical | **already the stated position** (L0 anchor ×3, post-#784 第一命题) | requires a new class-A admission |
| Class-A admission status | n/a — posits nothing | **no qualifying candidate currently specified** (§5.1) |
| Post-ST-A motivation | **strengthened** — the directional work is not claimed | **weakened** — one motivating inference was withdrawn (not refuted in principle) |
| Ontological commitment delta | **0** — adds no `L_0` object | **+1** object + 1 enforcement surface |
| Landing blast radius | **minimal but non-zero** — §16 ledger update + one freeze-Group-A clarification in the 初心 词条; no new symbol, no domain edit | symbol table, L0 anchor, claim ladder §0A class-A list |
| Existing formulations as bare-`L_0` candidates | n/a | neither `Ax-Sho-1` nor `Def-Apeiron-1` qualifies (content / reference commitments, **not** variational syntax) |
| Effect on Physics / Spirituality | none (bridge status already correct) | would upgrade their referent — the only real gain |

---

## 7. Recommendation

**Adopt Option A, and close §16 as a current-admission verdict:**

> **No additional `L_0` precursor of 初心 is currently admitted or required.** Under the present core, 初心 remains an L₁/P2 read-back; no distinct class-A precursor is added. A future candidate would require a **new Gate-0 admission** showing a non-redundant structural role.

Three things jointly favour A — none of them a proof of impossibility:

1. **Minimum ontological commitment.** Adding an `L_0` object is a real commitment; the default is not to add one absent warrant.
2. **Absence of a *demonstrated* explanatory gap.** Nothing currently in the corpus needs a precursor to state what it states — and post-ST-A the directional work it was imagined to underwrite is not claimed (§0.2). This is **not** the claim that existing mechanisms already complete the explanation (§4); it is the claim that no gap requiring an additional `L_0` object has been demonstrated.
3. **Absence of a T5-passing candidate.** None is presently specified (§5.1).

This is deliberately **weaker** than the argument an earlier draft of this packet made. That draft claimed T1–T4 leave "no room" for a third object and that Gate B therefore "decides itself." That over-reaches: Gate 0 states class A is **open, not closed**, so the admission test cannot establish that no distinct precursor could ever exist. §16 can close on the current candidate set **without** upgrading "no qualifying candidate today" into "no candidate is logically possible."

**What adopting A does *not* do:**

1. It does **not** demote 初心. It stays a full L₁/P2 object with its phenomenology, its read-back role, and its domain use intact.
1b. It does **not** assert that a precursor is impossible — only that none is **currently admitted or required**. §16 closes as a current-admission verdict with reopen conditions, not as a proof.
2. It does **not** modify `Spirituality/` or `Physics/`. Their forms remain valid **as bridge/translation** — which is what they already are post-#784.
3. It does **not** resolve the `κ₀` / `ε_pg` dependency relation (GOV-SUB01 Pass 2).
4. It does **not** touch Gate C. §5b.1's global-convergence-vector phrasing and the "global optimum" terminology remain Gate C's (§1.1).
5. It does **not** close class A generally. A future *different* class-A candidate may still be proposed; what closes is the **初心-precursor** question specifically.

**If the author instead wants Option B**, the packet's position is that it cannot be adopted *as currently stated*, because no candidate `π₀` has been specified. It should be re-proposed with a candidate that names explicitly what structural role it performs that the current class-A commitments do not (T5). Absent that, adopting B would register a commitment with no specified content.

---

## 8. Required landing list if Option A is adopted

Deliberately small — most of Gate B already landed with Gate 0.

| # | Landing | File | Class |
|---|---|---|---|
| 1 | Mark §16 **`RESOLVED — Option A / no additional precursor currently admitted`**, with the reopen conditions of §9 carried explicitly in the section | `Core/SRT_OPEN_TENSIONS.md` | A |
| 2 | One clause in the 初心 词条: **no additional `L_0` precursor of 初心 is currently admitted or required**; `L_0` commits to `ε_pg` and `κ₀`; 初心 remains an L₁/P2 read-back; a future candidate would need a new Gate-0 admission showing a non-redundant structural role | `Core_Law/SRT_L0_Metaphysics.md` | **B/C — freeze Group A, needs its own authorization** |

**Not on the list**, and deliberately so:

- any `Spirituality/` or `Physics/` edit; any §5b.1 / §5b.2 wording change; any symbol addition;
- **any line in Gate 0 §0A recording this as precedent.** §0A is a *general* type rule; a Gate B verdict that depends on the **current candidate set** should not be written back into the general authority. If the precedent is worth keeping, its home is `Core/SRT_OPEN_TENSIONS.md §16` or this decision record.

---

## 9. Rollback / failure conditions

Option A should be **reopened** if:

1. **A T5-passing candidate appears.** Someone specifies a contentless `L_0` object that demonstrably does work `ε_pg` does not — the direct refutation of §5.
2. **ST-A is reversed.** If a later pass re-establishes the `ε_pg` → ISP-level-direction derivation as a theorem, Option B's motivation returns and §0.2's argument weakens.
3. **The read-back proves unstable without an `L_0` ground.** If the L₁ 初心 read-back turns out to require an `L_0` underwriter that `ε_pg` plus objectivity cannot supply, the gap is real and A is under-committed.
4. **Bridge unstatability.** If treating `Def-Apeiron-1` / `Ax-Sho-1` as bridges makes some domain claim unstatable rather than merely re-indexed, the layering cut is in the wrong place.

**Success condition:** §16 closes without any file needing an `L_0`-level 初心, and Physics/Spirituality continue to say what they said, at bridge level, unchanged.

---

## 10. Boundary of this packet

- Modifies **no** axiom, theorem, definition, equation, threshold, symbol, or canonical stance.
- Adopts **no** option — §7 is an argument, not a verdict, and no file may cite this packet as having settled §16.
- Executes **no** Gate. Gate C (§17) and the `κ₀`/`ε_pg` dependency remain untouched and open.
- Does **not** authorize any edit to `Spirituality/`, `Physics/`, `_SRT_D_VALUE_CANONICAL.md`, or `Core_Law/SRT_L0_Metaphysics.md`. Landing item 2 above is a freeze-Group-A edit requiring separate authorization even if Option A is adopted.
- Gate A (§15) is **already resolved** by the author's EX-A decision (#788) and is referenced here only as context.
