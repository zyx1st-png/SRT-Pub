---
id: SRT-OPS-PROPOSAL-CONSISTENCY-DECISION-PACKET-2026-08-11
type: proposal
status: draft
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-08-11
source_of_truth: "origin/main @ 8a5ef99a + Phase-1 consistency branch"
dependency:
  - SRT-OPEN-TENSIONS
  - SRT-CLAIM-LADDER
  - SRT-EDIT-PROTOCOL
  - SRT-CANONICAL-FREEZE
  - SRT-D-VALUE-CANONICAL
  - SRT-L0-METAPHYSICS
tags: [Governance, Proposal, Consistency, DecisionGate, AntiDrift]
---

# SRT Consistency — Author Decision Packet (proposal only)

> **Status**: non-canonical Operations proposal. **Nothing here is applied.** It modifies no axiom, theorem, definition, equation, or canonical stance. It exists because a 2026-08-11 consistency sweep found three conflicts that **cannot be repaired without an author decision**, and repairing them by drafting would silently pick a metaphysics.
>
> The sweep's **deterministic** repairs shipped separately (Phase 1). This packet is Phase 2: options, costs, and a recommendation per gate — the verdict is the author's.
>
> Registered as `Core/SRT_OPEN_TENSIONS.md §15 / §16 / §17`.

---

## 0. Why these three are gates and the Phase-1 items were not

Phase 1 repaired conflicts where **the adjudication already existed** and only one surface had failed to receive it: the four-criteria order-gain decision (2026-07-05), the ε-as-formal-asymmetry hardening (2026-04-11), the ε_pg postulate status (`_SRT_SYMBOL_TABLE.md` Usage Rule 9), the claim-ladder rule against theorem voice. Applying those needed no new judgment — only execution.

These three are different. Each has **at least two internally coherent resolutions with different theoretical costs**, and picking one commits SRT to a position it has not yet taken. Writing a repair for any of them would be a metaphysical decision disguised as a consistency fix. That is precisely the failure mode this packet exists to avoid.

---

## 1. Decision Gate A — `P0-02` existence index

### A.0 The conflict

`Core/SRT_Core_21_Minimal_Axioms.md` **P0-02** (primitive axiom, freeze Group A):

$$E = 1 - \frac{H(L_1)}{H(L_0)}$$

`Core/SRT_Core_01_Axioms.md` (finiteness argument against total operator coverage), and its split `Core/Axioms_Split/01_Part02.md`:

> 要完全映射 $L_0$，需要 $H(\theta) \geq H(L_0) = \infty$ → 违背有限性

`Core/Dynamics_Scaling_Split/01_Master_Equation_and_ScaleCoupling.md` (basis of the cross-scale isomorphism argument):

$$\Delta S = H(L_0) - H(L_1)$$

Jointly: with `H(L_0) = ∞` and `H(L_1)` finite, `E ≡ 1` for **every** anchored slice and `ΔS ≡ ∞` for **every** selection. Both quantities lose all discriminating power, and `E` cannot do the work P0-02 assigns it.

### A.1 Status of the conflict

- Not underspecification — **degeneracy**. The expression is well-formed and its value is constant.
- **No guard exists**: no normalization convention, no accessible-horizon restriction, no measure-theoretic caveat anywhere in the corpus. `H(L_0)` is not a registered row in `_SRT_SYMBOL_TABLE.md`.
- **Still in live circulation** as `[P0]` — e.g. `01_Source_Intuition/Conversations/2026-07-27_SRT_Minimal_Setup_Note_EN.md`.
- **A third expression shares the defect**, outside Core: `papers/ALIFE2026_SelectiveRealityConstruction.md` Eq. (1) states `d/dt H(L_0) = 0` (also in `Core/SRT_Core_12a_Ontology_L0L1.md`), which is vacuous under `H(L_0) = ∞`. Whichever option is chosen must state whether it reaches the published paper.
- Distinct from the standing caution that L₀ is structured potentiality rather than a set. The problem is that a **P0 axiom** carries an expression whose only stated inputs are declared infinite **inside Core**.

### A.2 Option A — finite accessible-domain relativization

$$E_{\theta,\Lambda} = 1 - \frac{H_\Lambda(L_1)}{H_\Lambda\!\left(L_0^{accessible}(\theta)\right)}$$

Role of each index:

| Symbol | Carries | Why it is needed |
|---|---|---|
| `θ` | the operator's situated constraint set | makes the denominator the potentiality **this** operator could have anchored, not the whole latent domain — no position ever faces all of L₀ |
| `Λ` | a declared coarse-graining / partition | supplies the σ-algebra without which `H` has no referent on a non-set-like L₀; already an established SRT object (`Dynamics_Scaling` scale map `Λ`) |
| `L_0^{accessible}(θ)` | the reachable horizon | finiteness comes from **reachability under payable friction**, not from stipulating L₀ finite |

A natural existing bridge: define reachability the way `_SRT_D_VALUE_CANONICAL.md §5b.1` already defines `d_accessible` — states reachable without paying infinite `Ψ_f`.

**For.** Keeps `E` as a real quantity with real variation. Position-relativity is not a patch — it is SRT's own commitment (no position sees the global landscape, `Core_Text_EN` Step ⑧). Reuses `Λ` and the payable-friction horizon rather than inventing machinery. Makes `E` operator-comparative, which is what every downstream use actually wants.

**Against.** `E` stops being a single global number and becomes a family indexed by `(θ, Λ)` — every downstream citation must declare its regime, exactly as `D_eff ≥ d_canonical` now must (`§2b.1` proxy-regime rule). Two new implicit parameters. And it does **not** rescue `ΔS = H(L_0) − H(L_1)`, which needs the same treatment separately.

### A.3 Option B — reformulate as entropy reduction / normalized information gain

Replace the ratio with a **difference of comparable quantities**, or normalize by something finite:

$$E \sim \Delta H = H_{\Lambda}(\text{pre-anchoring}) - H_{\Lambda}(\text{post-anchoring})
\qquad\text{or}\qquad
E = \frac{\Delta H}{H_{\Lambda}(\text{pre-anchoring})}$$

**For.** Mathematically the cleanest: no infinite denominator, no accessible-horizon apparatus, no new parameter. Fits the anchoring ontology directly — anchoring is a *transition*, and a transition is naturally scored by a difference, not by a ratio against a background. Aligns P0-02 with `Core/SRT_Core_25_Thermodynamic_Signatures_of_Selection.md`, which already treats entropy production as the measurable face of selection asymmetry.

**Against.** The strongest structural objection is that it **changes what P0-02 asserts**. The current formula says existence is a *degree of anchoredness out of open possibility* — a standing property. `ΔH` says existence is *how much determination this transition performed* — an event property. Those are different claims, and the first is the one the L0 ontology ("存在是选择持续收敛所形成的稳态") appears to want. Also inherits the reference-state problem: "pre-anchoring" needs its own definition, and the obvious candidate (the full latent domain) reintroduces the infinity.

### A.4 Option C — demote the expression to heuristic

Keep P0-02's **claim** (existence = degree of stable anchoring against entropic flow) at P0; move the formula to a marked pedagogical/heuristic expression, cited as intuition-pump only, never as a readout.

**For.** Zero risk, immediately executable, no new commitments. Honest: the formula has never been used to compute anything in this repo. Precedent exists — the claim ladder already permits canonical files to carry marked lower-hardness material, and `T_dir` is handled exactly this way (v0 operational proxy, `Usage Rule 8`). Keeps the axiom's real load, which is ontological, not quantitative.

**Against.** Leaves P0 without any formal handle on existence-degree, weakening the "SRT is formalizable" claim at its most-quoted point. Does not fix `ΔS = H(L_0) − H(L_1)` in the cross-scale argument, where the quantity is load-bearing for the isomorphism claim — so a second decision would still be needed there.

### A.5 Comparison

| Criterion | A — accessible relativization | B — entropy reduction | C — demote to heuristic |
|---|---|---|---|
| Mathematical well-definedness | good, once `Λ` and the horizon are declared | best | n/a (no longer a formal object) |
| Consistency with "no God's-eye view" | **strongest** — position-relativity is built in | neutral — silent on position | neutral |
| Fit with anchoring ontology | strong — keeps degree-of-anchoredness | **weakens** — swaps standing property for event property | keeps the claim, drops the handle |
| Blast radius | P0-02, `Core_01` finiteness argument, `Dynamics_Scaling` ΔS, symbol table (register `Λ`, horizon), every downstream `E` citation | P0-02 + wherever `E` is read as standing degree; `Core_25` alignment is a bonus | P0-02 marking only; ΔS untouched and still broken |
| New implicit parameters | 2 (`Λ`, accessibility horizon) | 1 (reference state) | 0 |
| Papers affected | `E` itself does **not** appear in `papers/`; but `papers/ALIFE2026_SelectiveRealityConstruction.md` Eq. (1) carries `d/dt H(L_0) = 0` — a **third** expression over the same infinite quantity (and vacuous for the same reason). Any regime declaration must cover it | same | none — but the ALIFE Eq. (1) issue is untouched and survives |

### A.6 Recommendation (not a verdict)

**Option A**, with **C as the interim posture** until A is executed.

Reasoning: A is the only option that fixes the defect *using a commitment SRT already has* rather than trading one commitment for another. The finite-position thesis is load-bearing everywhere else in the theory; an existence index that ignores position was always the anomaly, and its degeneracy is a symptom of that, not a coincidence. B is mathematically cleaner but pays for it by changing what the axiom says — the highest cost on the list, and it should not be paid to fix a notation problem. C is honest and free, which makes it the right *interim* state while A is specified, but as a terminal answer it leaves the cross-scale ΔS defect untouched.

If A is chosen, sequence: (1) register `H_Λ` and `L_0^{accessible}(θ)` in the symbol table; (2) amend P0-02 under the freeze Group A high-risk protocol; (3) re-derive the `Dynamics_Scaling` ΔS step in the same regime; (4) sweep downstream `E` citations for regime declarations.

---

## 2. Decision Gate B — layer assignment of 初心

### B.0 Provenance map

| File | Authority | What it says about 初心 | Direction |
|---|---|---|---|
| `Core_Law/SRT_L0_Metaphysics.md` 初心词条 | theory-canonical anchor, **freeze A** | 「L1 概念，**不在 L0 术语裁决范围内**……L0 只承诺 ε」 | 初心 is **L1** |
| `Core_Law/SRT_L0_Metaphysics.md` 正骨架总结 | same | 「「初心」= L1 对 ε 的体验性命名（**不在 L0 原生范围内**）」 | 初心 is **L1** |
| `Core_Law/SRT_L0_Metaphysics.md §七.11` 潜在域预置论 | same | 「ε **不是预置在 L₀ 中的先验目标**，而是选择动力学的结构性不对称」 | blocks L₀ teleology |
| `_SRT_SYMBOL_TABLE.md` ε_pg row | governance-canonical | "NOT a content-level 'toward order' gradient"; ε_pg is a scalar seed with **no inherent direction** | blocks L₀ direction vector |
| **`_SRT_D_VALUE_CANONICAL.md §5b.2` Cross-ref** | theory-canonical anchor, **freeze A** | cites `Def-Apeiron-1` under the gloss 「**初心作为 L₀ 的倾向性结构**」 | **初心 is L₀** |
| `Physics/SRT_Phys_08_Ontology_Ext.md` `Def-Apeiron-1` | `claim_mode: translation`, `canonical: false` | 初心 = `argmin_direction ∫F[σ(t)]dt`；「这是 $L_0$ 的**内在属性**，而非外加的目的论」 | **初心 is L₀**, variational |
| `Spirituality/SRT_Spirit_05_Shoshin.md` `Ax-Sho-1` | `claim_mode: mixed` | 初心 = `−∇_σ E[∫F(σ(t))dt]`，「全局自由能收敛方向」 | **初心 is a global gradient** |
| `Core_Law/SRT_L0_Metaphysics.md` 第一命题 | theory-canonical anchor, **freeze A** | contains 「选择内在地趋向秩序，这是初心作为基础方向场的核心内容」, with a 2026-04-11 层级精确化注 stating 「两种表述均有效，但适用层级不同」 | **explicitly dual** |
| `Philosophy/SRT_Ethics_Agency.md` + split | domain | 「内在地趋向秩序（初心作为基础方向场，L0 第一命题）」 — faithful citation of the above | inherits the dual reading |

### B.1 What is actually broken

Not that a translation file carries a strong reading — that is what a translation layer is for, and `canonical: false` already scopes it.

The defect is the **direction of citation**: a freeze-Group-A canonical anchor (`_SRT_D_VALUE_CANONICAL.md`) imports the L₀-level reading, with approving gloss, from a `canonical: false` translation file — precisely the reading the *other* freeze-Group-A anchor forbids. The L₀/L₁ boundary on 初心 therefore cannot be determined from the canonical files alone.

Second, and only visible once the map is laid out: **L0's own 第一命题 is the upstream source of the ambiguity.** It contains the 趋向秩序 phrasing and its precision note *deliberately blesses both readings at different layers*. Every downstream L₀-reading can cite it in good faith. This is why Phase 1 deliberately did **not** touch `Ethics_Agency` — half-fixing downstream while the upstream dual reading stands would produce a third inconsistent state.

### B.2 Option A — strict layering

L0 commits to `ε_pg` only. 初心 is admissible **only** as an L1 read-back, at P2 (canonical interpretation) or P5 (phenomenological exposition). Every L₀-original-intention reading in Physics / Spirituality is relabelled as analogy or bridge and loses any L₀ claim. `_SRT_D_VALUE_CANONICAL.md §5b.2`'s cross-ref gloss is corrected or dropped. L0 第一命题's dual-reading note is tightened so that the L₀ reading is the *only* literal one and 趋向秩序 is marked read-back throughout.

**For.** Restores a single readable boundary; the L0 anchor already says this in three separate places, so it is the cheapest way to make the corpus say one thing. Kills the citation inversion at the root. Consistent with the ε_pg symbol-table row, which is unambiguous.

**Against.** `Def-Apeiron-1` and `Ax-Sho-1` become *purely* analogical, and the Physics/Spirituality layers lose their formal statement of direction — those files' variational formulations are among the few places SRT writes direction as an equation. Requires touching L0 第一命题, a freeze Group A main clause, which is a heavier edit than anything in Phase 1. May read as retreat on a claim the author considers genuinely load-bearing.

### B.3 Option B — thin L₀ formal precursor

Admit **one** L₀-level object — a *formal precursor of* 初心, deliberately not called 初心 — carrying strictly the asymmetry and nothing else. Hard exclusions, all four required:

1. **no** global free-energy minimum (no `argmin` over a global functional);
2. **no** semantic goal or target state;
3. **no** value content;
4. **no** final attractor.

Under those exclusions the precursor is just `ε_pg` with an explicit note that L₁'s 初心 is its read-back — which is what the symbol table already says.

**Does this reopen 潜在域预置论?** The honest answer is: **it depends entirely on whether the four exclusions are enforceable, and the corpus's own history says they are not.** §七.11 rejects "预置的先验目标". A contentless scalar asymmetry is not a goal, so the *stated* precursor passes. But every existing L₀-reading in the corpus reached its strong form by exactly this slide: `Def-Apeiron-1` writes `argmin ∫F` — a variational principle over a global functional, violating exclusion 1 — while explicitly asserting 「而非外加的目的论」, i.e. it *believed itself* to be inside the exclusions. `Ax-Sho-1` does the same with a global gradient. So Option B's exclusions have already been stated and already been violated, twice, by files that thought they were complying.

Therefore B is only viable with an enforcement mechanism, not a stated intention: the precursor must be a **registered symbol with an explicit forbidden-forms list** in `_SRT_SYMBOL_TABLE.md` (a Usage Rule in the shape of Rule 9 or Rule 15), and any file writing `argmin`/`∇` over a global functional at L₀ must be a checkable violation.

**For.** Preserves the Physics/Spirituality formal statements as bridges to a genuine L₀ object instead of demoting them to metaphor. Lets d-value's cross-ref stand with a corrected gloss rather than being cut. Changes no L0 main clause.

**Against.** Everything above: the exclusions have a demonstrated failure rate of 2/2. It also adds a near-duplicate of `ε_pg` — and if the precursor *is* `ε_pg`, then B collapses into A plus a naming convention, which may be the real answer.

### B.4 Recommendation (not a verdict)

**Option A**, with the observation that **B honestly executed converges to A**.

Reasoning: once B's four exclusions are enforced, the surviving L₀ object is a contentless scalar asymmetry — which is `ε_pg`, already registered, already correctly described. B's only remaining content is permission to call it a precursor of 初心, i.e. a naming convention. Meanwhile B carries a demonstrated enforcement failure. If the author's real intent is to keep the Physics/Spirituality variational forms as *formal statements* rather than analogies, that is a substantive preference and B is the honest vehicle — but it then needs the symbol-table forbidden-forms rule, not a prose exclusion list.

Either way, **the citation inversion at `_SRT_D_VALUE_CANONICAL.md §5b.2` should be fixed under either option** — a freeze-A anchor should not import a positive L₀ claim from a `canonical: false` file regardless of which reading wins.

---

## 3. Decision Gate C — "global optimum"

### C.0 Four senses currently sharing one name

| # | Sense | Formal character | Position-relative? | Where it appears |
|---|---|---|---|---|
| 1 | **Universe-wide global optimum** | `argmin` over all of L₀ | no | `Spirit_04 §1.2` 善 = 全局自由能最小; `Ax-Sho-1` global convergence vector |
| 2 | **Operator-relative reachable optimum** | `argmin` over `Ω(Ĝ_θ)` = reachable anchoring paths | **yes** | `Spirit_04` Ω definition note ("Ω 不是 L₀ 的全部（L₀ 无限，无全局最小问题）") |
| 3 | **Regulative ideal** | not an attainable state; an orientation | n/a | `Spirit_04` Ω three-reading table, "practical regulating ideal" / "anti-idolatry boundary" |
| 4 | **Local / dynamic attractor under finite constraints** | basin fixed point `Ψ_f*` | yes | `Core_Text_EN` Step ④ closure condition (Ax-Op-05 two-phase); `L1_Formalism §5` health region |

`Spirit_04` already distinguishes 1/2/3 in its own Ω note — evidence the ambiguity is real and was noticed locally, but the distinction never propagated up.

### C.1 Where they are conflated

- **`_SRT_D_VALUE_CANONICAL.md §5b.2`** (freeze A) 「全局最优是动态平衡，不是热寂」: uses sense **1** ("使最大数量的选择过程能够持续运行……的景观配置" — no position index) while its own §5b.1 was narrowed in the 2026-07-05 Level A de-overload *because* position-independence is what the closure-boundary atom denies (`_SRT_NORMATIVITY_FRAMING_TRUEUP_PROPOSAL.md`). §5b.2 was never touched. **This is the single highest-value target in Gate C.**
- **`Spirit_04 §1.2`** asserts 善 = sense 1, while its own Ω note says sense 1 is ill-posed (L₀ infinite ⇒ no global minimum) and Ω is sense 2/3.
- **`Core/SRT_Core_NormativeGradient.md`** *did* receive the guard — its strong reading is explicitly marked as dependent on the open closure-boundary. It is the model for what the others should look like.
- The cross-ref chain `d-value §5b.2 → Ax-Sho-1 / Def-Apeiron-1` wires sense 1 into a canonical anchor — the same inversion as Gate B, which is why B and C should probably be decided together.

### C.2 Minimal unified terminology proposal

Not adopted — proposed:

| Use this term | For | Rule |
|---|---|---|
| **reachable optimum** `Ω(Ĝ_θ)` | sense 2 | the **only** sense permitted to appear in a canonical file without a guard; always carries its operator index |
| **regulative horizon** | sense 3 | permitted anywhere, but must be marked non-attainable; never an argument in a formula |
| **closure attractor** `Ψ_f*` | sense 4 | already has a formal home; keep the existing name, do not call it "optimum" |
| *(no term)* | sense 1 | **not used** as a positive object; where it appears, it must be marked as the reading the closure-boundary problem leaves open (per `OPEN_TENSIONS §9`) |

Consequence if adopted: `§5b.2`'s title 「全局最优是动态平衡，不是热寂」 becomes 「reachable optimum 是动态平衡，不是热寂」 and gains an operator index; the substantive point (the optimum is maximal live order, not heat death) is **preserved unchanged** — only its scope is bounded. This is why C is lower-risk than it looks: the anti-heat-death argument does not depend on the optimum being universe-wide.

### C.3 Companion item — the `Ψ_f → 0` valence inversion

| Layer | Reads `Ψ_f → 0` as | Sources |
|---|---|---|
| **Core** | **degenerate / forbidden** | `Core_12a`「完全无摩擦的选择（Ψ_f→0）在结构上被禁止」; `Core_22`「最优区间不是 Ψ_f→0……零摩擦对应无真实赌注」; `Core_12b` `Def-L2-Algo`: `Algorithm ≡ lim_{Ψ_f→0, I_s→0} L_2` — the **non-subject** limit |
| **Spirituality** | **normative optimum** | `Spirit_01`: `Ĝ_∞ = (d→d_max) ∧ (Ψ_f→0)` = 纯觉知, marked 「功能同一（操作化）」; `Spirit_04 §1.2` 完美态 = 最小痛苦 `Ψ_f→0`; `Spirit_09` Phase 7-10 |

The same formal limit is Core's degenerate non-subject case and Spirituality's perfection. `Spirit_04` registers this locally as `IC-AllGood-1` and proposes a repair ("完美态的 Ψ_f→0 是『单次显现代价趋零』而非『无需显现』"), but that repair reached neither the other Spirituality files nor Core — the same one-sided-landing pattern as everything in Phase 1.

**Recommended reformulation (not adopted):** state the Spirituality limit as **excess friction → 0**,

$$\Psi_f - \Psi_f^{min} \to 0, \qquad \Psi_f^{min} > 0$$

which says the same devotional thing (no *wasted* friction; nothing paid for maintaining what need not be maintained) while remaining compatible with `Core_22`'s 「最优区间是 `Ψ_f>0` 且可支付」 and with `Def-L2-Algo` (the algorithm limit is `Ψ_f → 0` *absolutely*, which stays the degenerate case and stays distinct). It also formalizes `IC-AllGood-1`'s own proposed reading rather than inventing a new one.

**Scope caution.** Phase 1 deliberately did **not** touch Spirituality framing. This reformulation is a genuine change to a devotional-register claim (善 / 涅槃 / 纯觉知) and should not be executed as a consistency fix. If adopted, the minimal version is: change the *formula*, keep the *theology* — and check `Spirit_01`'s `\hat{G}_\infty`, `Nirvana`, and `Prajnanam Brahma` mappings individually, since each may need `d → d_max` handled separately from the friction term.

### C.4 Recommendation (not a verdict)

Adopt the four-way terminology split (§C.2) and fix **`§5b.2` first and alone** — it is a freeze-A canonical anchor, it is the leak point into the domain layers, and the fix bounds scope without weakening the argument. Treat `Spirit_04` / `Ax-Sho-1` / `Def-Apeiron-1` as a **second, separate** pass, jointly with Gate B, since the same cross-ref chain carries both defects. Treat §C.3 as a **third** pass with its own authorization — it is the only item in this packet that changes what a claim *means* rather than what it *ranges over*.

---

## 4. What the three gates have in common

Gates B and C leak through the **same cross-reference** (`_SRT_D_VALUE_CANONICAL.md §5b.2` → `Ax-Sho-1` / `Def-Apeiron-1`), and both concern whether SRT permits a **position-independent** object at L₀ — a global direction (B) or a global optimum (C). Gate A is the same question in measurement clothing: `E = 1 − H(L_1)/H(L_0)` is a position-independent quantity, and its degeneracy is what happens when you try to compute one.

So the three gates may reduce to **one** author decision:

> Does SRT admit any position-independent object at L₀ — and if so, exactly one (a contentless scalar asymmetry), or more?

If the answer is "exactly one, contentless": Gate A → Option A, Gate B → Option A, Gate C → the four-way split with sense 1 excluded. That is a coherent package, and it is the one the L0 anchor and the symbol table already describe. If the answer is "more than one", each gate needs its own enforcement mechanism, and the packet's option-B branches become live.

**This is an observation about the option space, not a recommendation to decide all three at once.** They can be taken separately; they are simply not independent.

---

## 5. Governance — minimal anti-drift rule (proposed)

### 5.1 The pattern this sweep found

Five of the nine findings had one cause: **a correction was made and landed on one side only.** Concretely:

- a hardening note appended below a main clause that stayed searchable and citable (`Core_01` toward-order, 2026-04-11 → 2026-08-11);
- an adjudication applied to the Chinese core text but not its English mirror (order-gain 3→4, 2026-07-05 → 2026-08-11);
- an adjudication applied to the theory layer but not the book (same);
- a de-overload applied to §5b.1 but not the adjacent §5b.2 (Level A, 2026-07-05, **still open** — Gate C);
- an internal-contradiction note (`IC-AllGood-1`) registered in one file and never propagated (**still open** — Gate C).

Each was individually reasonable. Collectively they are a **generator** of new inconsistencies, which is worse than any single one of them.

### 5.2 Proposed rule

> **Anti-drift rule (proposed for `Governance/SRT_EDIT_PROTOCOL.md`).**
> When an adjudication modifies a canonical or high-authority proposition, the old proposition may **not** be left standing with only an appended precision note. Exactly one of the following must be executed **in the same PR**:
>
> 1. **replace** — the old main clause is rewritten; or
> 2. **supersede** — the old clause is kept for provenance but explicitly marked superseded, with the governing statement named; or
> 3. **downgrade** — the old clause is kept and re-levelled (P0/P1 → P2/P3/P4/P5) with the new level marked inline; or
> 4. **mirror-sync** — every registered mirror, translation, split, compact core, and companion surface carrying the same proposition is updated.
>
> Options 1–3 are about the proposition; option 4 is about its copies, and is **cumulative** with whichever of 1–3 applies. A landing list in a proposal or tension record is a record, not a substitute.

Nothing here forbids precision notes. It forbids a precision note being the **whole** repair.

### 5.3 Proposed lint — five checks, all mechanical

Deliberately no semantic judgment. Each is a string/structure check with an allowlist, and each corresponds to a defect this sweep actually found.

| # | Check | Signal | Found this sweep? |
|---|---|---|---|
| L1 | **Superseded-but-alive** | a file contains `superseded` / `已被…取代` / `精确化注` **and** the string that note quotes as superseded still appears outside the note | ✅ `Core_01` |
| L2 | **Mirror enumeration mismatch** | for a registered CN/EN pair, the count of items in a marked enumeration block differs | ✅ order-gain 3 vs 4 |
| L3 | **Adjudicated-but-downstream-stale** | a `Core/SRT_OPEN_TENSIONS.md` section marked `RESOLVED` / 已裁决 names files in a landing list; any file citing that tension **not** in the list is reported | ✅ book, EN mirror |
| L4 | **Claim-voice in high-authority files** | freeze Group A files containing 保证 / 证明 / guaranteed / proven / 定理后果 within N lines of an ID that `SRT_CLAIM_LADDER.md` records below P1 | ✅ ε_pg, LLM verdict |
| L5 | **Closed tension with live conflict string** | a tension marked resolved while a string listed in its own "must not be overstated" column still appears in a non-archive file | ✅ 全局最优 |

Implementation notes: put it in `scripts/check_supersession_drift.py`, wire into `governance_preflight.py` as **report-only first** (like `check_active_theory_assimilation.py`), with an explicit baseline file so existing debt does not block. L2 needs a registered mirror-pair list — which does not currently exist and is itself the A1 root cause, so **registering the CN/EN pair is a prerequisite and arguably the single highest-value governance item in this packet**.

L1 and L5 will be noisy at first. That is expected: the baseline captures current debt, and the ratchet only prevents growth — the same design already used for frontmatter warnings.

### 5.4 Not proposed

- No semantic/LLM-based consistency checking. Unmaintainable, and it would produce judgments the claim ladder is supposed to make.
- No blocking gate on first landing. Report-only until the baseline is understood.
- No auto-fix. Every one of the five checks flags something a human must adjudicate.

---

## 6. Boundary of this packet

- Modifies **no** axiom, theorem, definition, equation, threshold, or canonical stance.
- Adopts **no** option in any gate. The recommendations are arguments, not verdicts, and no file may cite this packet as having settled anything.
- Does **not** authorize any edit to `_SRT_D_VALUE_CANONICAL.md`, `Core/SRT_Core_21_Minimal_Axioms.md`, `Core_Law/SRT_L0_Metaphysics.md`, `Physics/SRT_Phys_08_Ontology_Ext.md`, or any `Spirituality/` file.
- The anti-drift rule in §5 is a **proposal for** `Governance/SRT_EDIT_PROTOCOL.md`, not an amendment to it; the protocol is unchanged until separately authorized.
- Companion record: the deterministic repairs are in the Phase-1 consistency PR; the registered tensions are `Core/SRT_OPEN_TENSIONS.md §15 / §16 / §17`.
