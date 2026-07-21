---
id: SRT-OPS-AUDIT-P1-T07-PROOF-HARDENING
type: audit_record
status: record_v0_1
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-07-17
source_of_truth: "origin/main @ 14c0d7f8 (post-#674 merge; Pass-2 branch base audit/p1-t07-proof-hardening)"
dependency:
  - SRT-GOV-SUB01-SUBTRACTIVE-AUDIT
  - SRT-OPS-AUDIT-CONCEPT-DELETION-PASS2-KAPPA-EPSILON
  - SRT-OPS-AUDIT-MAP-EPSILON-PG
tags: [Governance, ProofAudit, P1-T07, EpsilonPG, Reachability, Hazard]
---

# P1-T07 Proof Hardening Audit — Reachability, Cumulative Hazard, and ε_pg Independence

> **Status**: non-canonical Operations record. **Proof audit only.** It modifies no theorem, no axiom, no definition, no equation. It does not resolve the proof; it maps exactly where the current proof does and does not close, and hands options to a later controlled amendment PR. Prior Claude/ChatGPT statements about P1-T07 were treated as hypotheses; the only source of truth is `origin/main @ 14c0d7f8`. Archive/book files were read for context but are **not** used to establish anything about the canonical theorem.
>
> **Proof Audit 1.3 revision (2026-07-17)**: semantic-consistency cleanup. (a) `τ<∞` verdicts stratified by semantics — on a realized terminating history only **S1 pathwise** stability fails; **S2** fails only if `P(τ<∞)>0`, **S3** only if `P(τ=∞)=0`; no unconditional *process-level* stable-ISP verdict before the S1/S2/S3 choice (fixed in §0 Q5, §8, Proof Gate). (b) "Two exhaustive readings" → **three diagnostic branches** (theorem-false / circular / **recoverable-via-`K₀`** — the open B-lite/possible-R2 branch), marked diagnostic, not exhaustive. (c) Option A: ε-verdict now E-pending on `K₀` (no longer "keeps the headline only by making ε-dependence explicit"). (d) Option C: ε-premise verdict → E-pending, decided at the bridge. (e) "five corpus contradictions" → "four corpus findings, including the ε_pg source-direction circularity"; D5 → "candidate-neutral under one possible kernel definition"; map column renamed "global necessity / package role".
>
> **Proof Audit 1.2 revision (2026-07-17)**: consistency corrections. (a) positive-hazard logic clarified — the corpus doesn't *establish* positive hazard; *if* it holds at a surviving step, positive *eventual* termination follows; positive hazard at every step still ≠ a.s. termination. (b) Resolved the Q5 self-contradiction — "if `τ<∞` then not a stable ISP" is kept as true/derivable; what is **not** derivable is "neutral `P` terminates a.s., therefore not stable." (c) Uniform-δ reclassified from "pro-closure drift / actively dying" to **E — pending kernel** (may arise from unbiased geometry; stronger than necessary; absent from corpus). (d) Assumption-map "Necessary?" → **"Global necessity / package role"** with per-premise roles. (e) Option A regrounded on an independent neutral baseline `K₀` with `P_{K₀}(τ<∞)=1` via **alternative** packages A1/A2/A3 (not a simultaneous conjunction); ε-verdict withdrawn to E. (f) Option C lemma 2 fixed — P1-T06 yields **no** probabilistic survival; replaced by an S1/S2/S3 persistence lemma. (g) B-lite given a **comparative** anti-closure criterion (`P_K(τ>t) > P_{K₀}(τ>t)` or `h_t^K < h_t^{K₀}` on a non-null set) and marked a proposal, not a theorem.
>
> **Proof Audit 1.1 revision (2026-07-17)**: tightened the probability. (a) Replaced the unconditional "a.s. termination **iff** `Σh_t=∞`" with the deterministic product identity `P(τ>n)=∏(1-h_k)` and divergence as a **sufficient** condition (exact N&S flagged pending). (b) Added the stable-ISP **stochastic-semantics gap** S1/S2/S3 — P1-T07 is not a formal stochastic theorem until one is chosen. (c) Countermodels split by role: D1/D3/D6 refute the *inference* (not automatically S2 stable-ISP countermodels); D2/D4/D5 are *candidate* theorem countermodels pending perspective/history-bearing + an ε-neutral definition; removed "each satisfies the stated stable-ISP conditions." (d) **Withdrew** the unconditional ε-co-reference verdict: reachability / hazard-divergence / no-safe-class / recurrence are now **E — pending an independent neutral kernel**; only the askability prior is **C** and the define-neutral-by-survival move is **D/circular**. "clean R2 unreachable" → "not established, but possible in principle". (e) The strongest *unconditional* claim is only "if `τ<∞` then not a stable ISP." (f) Contradiction §6 narrowed to the ε_pg input/output circularity (the L₀/ISP level distinction is legitimate).

## 0. The six core questions (answers up front)

1. **Does "nonzero probability at each step" imply almost-sure entry into `∅`?** **No.** Note the logic carefully: (a) the corpus does not *establish* positive per-step hazard at all (Step 3 asserts it); (b) *if* positive hazard holds at some surviving step, then positive **eventual** termination probability does follow (that step has positive probability of terminating); but (c) positive hazard **at every step** still does **not** imply *almost-sure* termination. (§3, §4)
2. **What minimal mathematical conditions are additionally required?** **Three *alternative* sufficient packages** (§4): **(A)** a uniform conditional hazard lower bound `h_t ≥ δ>0`; **(B)** divergent cumulative conditional hazard along every surviving history; **(C)** a Markov absorption package (all nonempty states transient / no other closed recurrent class). Each package internally implies reachability. The *exact* necessary-and-sufficient hazard theorem is flagged as **pending a stochastic-semantics choice** (S1/S2/S3, §2), not asserted here.
3. **Do these already exist in SRT definitions?** **No.** `A_t`, "ε-neutral", "continued selectability", and the stochastic transition itself are not formally defined at the level these premises need; the stable-ISP definition (P1-T06) is stated non-probabilistically and does not even fix which stability semantics (S1/S2/S3) is meant. (§2)
4. **Do these premises smuggle ε_pg back in?** **Undecided per premise (§5).** Only the *askability prior* is clearly ε-co-referential (C); *defining "neutral" directly by non-summable death hazard* is circular (D). Reachability / hazard-divergence / no-safe-class / recurrence **and the uniform-δ bound** are **E — pending an independently specified state-space geometry or neutral transition kernel**; they are *not* automatically ε_pg in disguise. (Uniform-δ is *stronger than necessary* and *absent from the corpus*, but it may arise from unbiased kernel geometry — not inherently a "pro-closure drift".)
5. **What can P1-T07 prove at most?** Two things must be separated, and the first is **semantics-relative**, not process-unconditional. **(i) True and derivable, per level**: on any realized history with `τ<∞`, that history enters the absorbing `∅` and no further selection is possible — so **S1 (pathwise) stability fails on that history**. At the *process* level, **S2** stability fails only when `P(τ<∞)>0`, and **S3** stability fails only when `P(τ=∞)=0`. Before S1/S2/S3 is chosen, **no unconditional process-level stable-ISP verdict may be issued** from `τ<∞`. **(ii) NOT derivable as written**: *neutral `P` terminates a.s., therefore neutral `P` is not stable* — because a.s. termination of a neutral process is exactly what Step 3 fails to establish. "Positive termination probability" is also **not** unconditional (it needs positive hazard at a surviving step). (§4, §8)
6. **Can ISP-level ε be derived independently of ε_pg?** **Not established — but not disproven.** Under the current corpus the anti-closure residue is **R4**. A clean **R2** (ε_pg dispensable) is **not established**, yet **remains possible in principle** if an independently defined neutral baseline kernel can be shown to absorb almost surely. (§5, §9)

## 1. Object

`Core/SRT_Core_21b_Constitutive_Theorems.md` **P1-T07** (canonical, claim_level P1). Statement: *for any stable ISP `P` under `L_0` irreversibility, `P` necessarily contains an ε-type anti-closure asymmetric bias.* Proof Sketch Step 3 (verbatim): *"Neutral `P` has nonzero probability of selecting into `A_{t*}=empty` at each step; over sufficient iterations, cumulative probability tends toward 1."*

## 2. Formal reconstruction of the current proof

To test Step 3 we must make the implicit stochastic model explicit. The theorem does not supply one; the following is the **minimal** charitable formalization.

- **Reachable-selection set** `A_t`: the set of selections available to `P` at step `t`. `A_t = ∅` is the terminal/absorbing configuration (P1-T06 cond. 1 requires `A_t ≠ ∅` to select).
- **Absorbing terminal** `∅`: by `L_0` irreversibility (`SRT_Irreversibility.md` Def-IRR / T-IRR-2), `A_{t*}=∅ ⇒ ∀t>t*` no `Ĝ_θ` yields a new selection. **Absorbing is well-defined and canonical.**
- **History filtration** `H_t` = σ-algebra of the process up to `t`.
- **Conditional death hazard**: `h_t := P(A_{t+1}=∅ \mid H_t,\ A_t ≠ ∅)`.
- **Stable ISP** (P1-T06 result-state criterion): iterative (`A_t≠∅` each `t`), perspective-bearing, history-bearing (writeback `A_t → A_{t+1}`), **re-selectable (continues selecting across steps)** — all stated **non-probabilistically**.
- **Stochastic semantics of "stable" — undetermined by P1-T06.** With `τ := inf{t : A_t = ∅}`, P1-T06 does not decide which of these "stable ISP" requires:
  - **S1 — pathwise stability**: `A_t ≠ ∅` for all `t` on a *realized* history (`τ = ∞` on that path);
  - **S2 — almost-sure stability**: `P(τ = ∞) = 1`;
  - **S3 — positive-survival stability**: `P(τ = ∞) > 0`.
  These are genuinely different objects, and **P1-T07 cannot be a formal stochastic theorem until one is chosen** — both the theorem's truth and the status of every countermodel depend on the choice.
- **ε-neutral**: **not formally defined anywhere in the corpus** (grep across `Core/`, `Core_Law/`: used in P1-T07 proof and `Irreversibility.md §3/§4/§4.5`, never defined). The only quasi-definition is by contrast (`Irreversibility.md:167`): ε-anti-closure ISPs are "those with nonzero long-run probability of not entering the absorbing state"; so ε-neutral reads as its negation.
- **Irreversibility**: `∅` is absorbing (above). This governs *what happens after* `∅`, not *whether* `∅` is reached.

**Six distinct propositions that Step 3 conflates** (none entails the next without added premises):

1. `∅` is **absorbing** — ✅ canonical (irreversibility).
2. `∅` is **reachable** from current states under neutral dynamics — ❓ unstated.
3. `∅` carries **positive per-step hazard** (`h_t>0`) — ❓ unstated; not entailed by neutrality.
4. **cumulative hazard diverges** (`Σ h_t = ∞` a.s.) — ❓ unstated.
5. **hitting probability = 1** (a.s. termination) — the proof needs this.
6. **expected hitting time finite** — a stronger claim the proof gestures at ("over sufficient iterations").

Step 3 asserts (5) [and flirts with (6)] from (3). That inference is invalid.

## 3. The gap, precisely

Even granting `h_t > 0` for **all** `t` (proposition 3, itself unstated), a.s. termination does **not** follow.

**Deterministic (pre-given) hazard.** Survival is exactly `P(τ > n) = ∏_{k≤n}(1 - h_k)`. Since for `h_k ∈ [0,1)` one has `∏_k (1-h_k) > 0 ⟺ Σ_k h_k < ∞`, a strictly positive per-step hazard is **compatible with positive survival forever**. Concretely, `h_t = 2^{-t}` (`t ≥ 1`, every `h_t > 0`) gives `∏_{t≥1}(1 - 2^{-t}) ≈ 0.2888 > 0`, so `P(τ = ∞) > 0` despite `h_t > 0` at every step.

**General (predictable) hazard.** Divergence of the cumulative conditional hazard **along every surviving history** is a *sufficient* condition for a.s. termination, under the appropriate predictable-hazard / compensator formulation (`Σ_t h_t = ∞` a.s. ⇒ `∏_t(1-h_t) = 0` a.s. ⇒ `τ < ∞` a.s.). This pass does **not** assert an unconditional "iff": the exact necessary-and-sufficient characterization — random hazards, the compensator of `𝟙[τ ≤ t]`, and the measure-theoretic meaning of "along surviving histories" — requires fuller probabilistic formalization and is **flagged as pending**.

The upshot for Step 3 is unchanged: "nonzero per-step hazard" does not yield a.s. termination. Moreover neutrality does not even give proposition (3): a neutral process may have `h_t = 0` (it simply never drifts toward `∅`). "No anti-closure bias" ≠ "positive closure bias."

## 4. Proof versions: three *alternative* sufficient packages (A/B/C) + countermodels (D)

Versions A, B, C are **not** a single conjunction; each is an **independent sufficient package** for a.s. termination, and each **internally implies reachability** (so reachability need not be added separately). They differ in strength and in what they presuppose.

### Version A — Uniform conditional hazard lower bound (`h_t ≥ δ > 0`)
*Implies reachability (positive per-step hazard at every surviving step).*
- **Yields**: a.s. termination *and* finite expected time (`P(survive to t) ≤ (1-δ)^t → 0`, `E[τ] ≤ 1/δ`). **Sufficient.**
- **Where does δ come from?** Nowhere in the corpus, and it is **stronger than necessary** (Packages B/C need no uniform bound).
- **ε-status**: **E — pending a neutral-kernel interpretation.** A uniform `δ` is **not** intrinsically a "pro-closure drift": it can arise from *unbiased* kernel geometry (e.g. a fixed escape probability to a boundary at each step, with no directional bias between `B≥2` and `B≤1`). It is neither established as ε nor established as ε-independent — simply absent from the corpus; if supplied, its ε-status depends on the kernel.

### Version B — Divergent cumulative hazard along surviving histories (`Σ h_t = ∞`)
*Implies reachability (a summable-to-∞ hazard cannot be identically zero).*
- **Yields**: a.s. termination (predictable-hazard / compensator argument), **no** finite-expected-time guarantee. **Sufficient.**
- **Requires**: a predictable/martingale structure (available), plus the substantive claim that a neutral `P` has non-summable death hazard.
- **Is this ε_pg in disguise?** **Undecided — E pending a neutral-kernel definition.** The divergence premise *could* be read as "neutrality cannot sustain non-self-erasure" (the contrapositive of ε_pg's `B≥2 ≻ B≤1` bias), **or** it could follow from an *independently specified* neutral transition kernel / state-space geometry. Whether it collapses into ε_pg depends on how "neutral" is defined (still open). Not auto-classified as ε.

### Version C — Markov absorption package (`∅` reachable & absorbing; no other closed recurrent class)
*Bundles reachability and "no safe neutral class."*
- Model neutral `P` as a Markov chain on reachable-set configurations, `∅` absorbing.
- **Yields**: a.s. absorption when every nonempty state is transient / there is **no closed recurrent class avoiding `∅`**.
- **Is the "no safe neutral class" premise ε_pg?** **Undecided — E pending the topology/model.** Nothing in P1-T06/T07 forbids a safe class (Countermodels D2/D5), so the premise is *load-bearing and unstated*; but it *could* be supplied by an independently defined kernel geometry rather than by ε_pg. Not auto-classified as ε.

### Version D — Countermodels (each a valid stochastic/transition system)
| # | Countermodel | Terminates a.s.? | Blocked by which formal condition? |
|---|---|---|---|
| D1 | `h_t = 2^{-t}` (all `h_t>0`, `Σh_t = 1 < ∞`) | **No** — survival prob `∏(1-2^{-t}) ≈ 0.29 > 0` | none in P1-T06/T07 |
| D2 | Neutral closed 2-cycle `{a,b}`, both `≠∅`, `∅` unreachable from it | **No** | none — no reachability premise |
| D3 | `∅` reachable but only with total probability `<1` (transient toward a safe region) | **No** | none — no recurrence premise |
| D4 | Infinite non-terminating trajectory retaining `A_t≠∅` (e.g. random walk on ℕ with reflecting 0-neighbourhood) | **No** | none — no hitting guarantee |
| D5 | Deterministic period-2 orbit, `h_t=0` ∀t | **No** | none — **candidate-neutral under one possible kernel definition** (no *bias* term), yet survives |
| D6 | Hazard decays to 0 (`h_t ↓ 0`, `Σh_t<∞`): long-run survival stays positive | **No** | none |

All six respect irreversibility (`∅` is absorbing — simply never reached). They play **two distinct roles** (not interchangeable):

- **Refuting the Step-3 *inference*** — **D1, D3, D6** have `h_t > 0` at every step yet `P(τ=∞) > 0` (survival positive but *not* a.s.). They **refute "nonzero per-step hazard ⇒ a.s. termination."** They do **not** automatically constitute stable-ISP *countermodels* under **S2** (a.s. stability), since under S2 a process with `P(τ<∞) > 0` is not stable; under **S3** (positive-survival) they would be.
- **Candidate *theorem* countermodels** — **D2, D4, D5** have `P(τ=∞) = 1` (deterministic / closed non-`∅` class), so they are **S2-stable (survive a.s.)**. They are candidate countermodels to the theorem **only if** (i) the perspective-bearing / history-bearing conditions of P1-T06 (conds. 2–3) are supplied and satisfied, **and** (ii) "ε-neutrality" is independently defined so they qualify as neutral. Neither is pinned down, so they remain **candidates**, not confirmed countermodels.

Whether any `D_i` counts as **"ε-neutral"** cannot be decided, because ε-neutral is undefined. **Three diagnostic branches** for a future definition (diagnostic, **not** a proven-exhaustive classification of all possible neutral definitions):

1. **Theorem-false branch**: an independently specified neutral definition *includes* a surviving countermodel (e.g. D2/D5 under a weak "no active anti-closure maintenance" reading) ⇒ **P1-T07 is false under the chosen semantics**.
2. **Circular branch**: neutrality is defined directly by the survival/hazard *outcome* (e.g. "has non-summable death hazard") ⇒ the exclusion **is** the ε-bias ⇒ **P1-T07 is analytic/circular**.
3. **Recoverable branch (open — B-lite / possible-R2)**: a neutral baseline kernel `K₀` is *independently* defined (kernel property, not survival outcome) and **shown** to absorb a.s. ⇒ the theorem may be **recoverable without ε_pg**, with anti-closure identified comparatively against `K₀`.

Branches 1 and 2 block an *unconditional* proof; branch 3 is the constructive escape route, currently unbuilt.

## 5. Is ε_pg hidden in the premises?

Classify each candidate closing premise (A=truly independent, B=weaker than ε_pg, C=local projection of ε_pg, D=renamed ε-like primitive, E=undecidable):

| Premise | Classification | Reason |
|---|---|---|
| `∅` absorbing | **A (independent)** | pure irreversibility; but insufficient alone |
| `∅` reachable (proposition 2) | **E — pending source** | could be an independently specified state-space geometry / neutral kernel, **or** a projection of ε_pg's `B≥2` favouring; not decidable without the neutral-kernel definition |
| `h_t ≥ δ > 0` (Version A) | **E — pending kernel** | stronger than necessary and absent from the corpus; **not** intrinsically pro-closure — may arise from unbiased kernel geometry |
| `Σ h_t = ∞` (Version B) | **E — pending neutral-kernel definition** | may restate ε_pg's non-self-erasure, **or** may follow from an independent kernel; depends on the (still open) definition of "neutral" |
| "no safe neutral closed class" (Version C) | **E — pending topology/model** | load-bearing and unstated, but **could** be supplied by an independent kernel geometry rather than by ε_pg |
| recurrence / irreducibility | **E — pending model** | a structural chain property; not intrinsically ε |
| persistence / askability prior | **C** | `L0_Metaphysics §六`: "any position that can accumulate/remember/ask must **locally** satisfy non-self-erasure" — this **is** local ε; the file scopes it to *local* ε only |
| defining "neutral" directly by non-summable death hazard | **D / circular** | assumes the very hazard structure the theorem concludes |

**Verdict**: only the askability prior (**C**) and the define-neutral-by-survival move (**D/circular**) are settled as ε-entangled. The load-bearing *structural* premises — reachability, hazard divergence, no-safe-class, recurrence, and the uniform-δ bound — are **E: not decidable without an independently specified neutral baseline kernel / state-space geometry**. Therefore **ε_pg-independence at the ISP level is not established — but it is not disproven either.** A **clean R2 is not established in the current corpus; it remains possible in principle if an independently defined neutral baseline kernel can be shown to absorb almost surely** (see Proposals Option B-lite).

## 6. Corpus contradictions found (recorded, not resolved)

> **Not a contradiction (legitimate design):** the two-level distinction — `ε_pg` (L₀) as a **structural postulate** vs ISP-level `ε` as a **proposed structural corollary** — is a coherent layering, not an inconsistency. The finding below is narrower.

1. **Circular dependency on ε_pg (the precise contradiction).** `Core_Law/SRT_Irreversibility.md:240` states `ε_pg > 0` is **guaranteed by P1-T07**'s proof-by-contradiction, while P1-T07's own bridge relation (step 1) already takes **`ε_pg` existence as an input**. So the L₀ postulate is made a *consequence* of a theorem that *assumes* it — ε_pg is both premise and conclusion of one argument. (`L0_Metaphysics:202` independently insists ε "不可被升格为定理" / must not be upgraded to a theorem, siding against the Irreversibility:240 reading.)
2. **Local vs global.** `L0_Metaphysics:202` explicitly scopes the askability argument as proving only **locally-valid ε**, "不能推广到全局 L0" — yet P1-T07 / T-IRR-3 state the necessity without that locality qualifier.
3. **Undefined primitive.** "ε-neutral" is load-bearing in the proof but has **no formal definition** in the canonical corpus.
4. **Non-probabilistic definition, probabilistic proof, undetermined semantics.** P1-T06 defines stable ISP without any transition-probability structure and without fixing S1/S2/S3 (§2); P1-T07 Step 3 silently introduces a stochastic model (`h_t`). The proof's object is not (yet) the definition's object.

## 7. Collective version — T-COLL-3

`Core_Law/SRT_Collective_Selection.md §5 T-COLL-3` proof (line 498) is **explicitly "与 P1-T07 同构" (isomorphic to P1-T07)**: collective neutrality ⇒ `A_𝒫(t)` has nonzero probability of collapsing to `∅` ⇒ absorbing ⇒ not a stable collective ISP.

- **Same proof shape** ⇒ **inherits the identical Step-3 gap.**
- **No independent collective reachability/hazard premise** is supplied.
- It defines `σ_sr^coll → 1 ⇔ ε^coll → 0` (line 504) — again defining neutrality by the closure condition (same circularity, lifted).
- **Individual vs collective termination** are structurally distinguished (T-IRR-2 "集体终止") but the *proof* does not use that distinction to add a premise.
- **Inherits the S1/S2/S3 ambiguity too** (§2): "stable collective ISP" is likewise not fixed to a stochastic-stability semantics, so the collective statement is no more formally closed than the single-ISP one.
- **Cannot** serve as independent support for P1-T07: an isomorphic copy of the same invalid inference is not corroboration.

## 8. What the theorem CAN stand on (unconditionally)

- The **absorbing** character of `∅` under irreversibility — solid, unconditional.
- **The only unconditional consequence about stability is history-level, not process-level**: on any realized history with `τ < ∞`, that history enters the absorbing `∅` and selection cannot continue — **S1 (pathwise) stability fails on that history**. At the process level, **S2 fails only if `P(τ<∞)>0`** and **S3 fails only if `P(τ=∞)=0`** — so before S1/S2/S3 is chosen, no unconditional process-level stable-ISP verdict follows from `τ<∞`. And this is a conditional on termination *occurring*; it says nothing about *whether* it occurs.
- **"Positive termination probability" is NOT unconditional** — it requires reachability (an unstated premise), so it is not part of the unconditional base.
- **Conditional statements** (each with an explicit, currently-unjustified premise): Versions A / B / C each yield a.s. termination; whether their premises are ε-co-referential is **open** (§5), not settled.

Everything stronger (a.s. termination for *all* neutral stable-ISP candidates; ε-independence) is **not** currently proven, and cannot be stated as a stochastic theorem until S1/S2/S3 is chosen.

## 9. Decision gates

### P1-T07 Proof Gate
- **Is the current Proof Sketch valid?** **No — high confidence.** Step 3 is a non-sequitur (§3, standard probability); it conflates six distinct propositions (§2).
- **Is the *theorem* (statement) true?** **Unresolved.** It may be true under an added premise and a chosen semantics; the current text neither proves nor refutes it.
- **Exact necessary/sufficient hazard theorem?** **Pending a stochastic-semantics choice (S1/S2/S3, §2).** Not stated this pass.
- **Strongest unconditional conclusion**: `∅` is absorbing; and on any realized history with `τ<∞`, **S1 (pathwise) stability fails on that history** — process-level (S2/S3) verdicts require the semantics choice and the relevant probability (`P(τ<∞)>0` / `P(τ=∞)=0`). **Not** a.s. termination; **not** even unconditional positive termination probability; **no** unconditional process-level stable-ISP verdict.
- **Sufficient packages** (alternatives, §4): **A** uniform `h_t≥δ`; **B** divergent cumulative hazard on surviving histories; **C** Markov absorption (no other closed recurrent class). All three are absent from the corpus and their ε-status is **E — pending a neutral-kernel definition** (none is settled ε, none settled ε-independent).
- **Valid countermodels?** **Yes** to the *inference* (D1/D3/D6 refute Step 3); **candidate** countermodels to the *theorem* (D2/D4/D5) pending semantics + an ε-neutral definition.
- **Confidence**: **high** the proof is invalid as written; **medium** on the sufficient-package set; **low-to-medium** on whether those premises are ε-entangled.
- **GO / NO-GO for a theorem-amendment proposal**: **GO** (options in `Operations/Proposals/SRT_P1_T07_HARDENING_OPTIONS.md`). **NO-GO** for editing P1-T07 this pass.

### ε_pg Independence Gate
- **Can P1-T07 stand independent of ε_pg?** **Not established — and not disproven.**
- **Which premises *may* be hidden ε?** Only the askability prior is settled ε (**C**); defining "neutral" by non-summable hazard is circular (**D**). Reachability / hazard-divergence / no-safe-class / recurrence are **E — pending an independently specified neutral kernel / geometry** (§5), not automatically ε.
- **GOV-SUB01 residue for the anti-closure role**:
  - under the current (invalid) proof: **R4**;
  - **R2 is not established in the current corpus**, but **remains possible in principle** if an independently defined neutral baseline kernel can be shown to absorb almost surely (Proposals Option B-lite);
  - a **P** reading applies only if the closing premise turns out to be an ε-grade postulate — which is one of the open branches, not a settled verdict.
- **What is still missing**: (i) a choice of S1/S2/S3; (ii) a formal ε-neutral definition that is **not** the survival/closure outcome; (iii) an ε-independent justification (or refutation) of the reachability/absorption premise.

### Collective Gate
- **Does T-COLL-3 close independently?** **No.**
- **Does it inherit the same gap?** **Yes** (isomorphic proof, no independent premise) — **plus** the same S1/S2/S3 semantic ambiguity.
- **Can it corroborate P1-T07?** **No** — an isomorphic copy of the same invalid inference cannot support itself.

## 10. Recommendation (not executed)

Proceed to a **controlled theorem-amendment proposal** (see the Proposals file), which does **not** edit canonical text this pass. Route the missing formal `ε-neutral` definition and the reachability premise to the proof layer. Log the four corpus findings, including the ε_pg source-direction circularity (§6), for governance; do not "fix" them by wording.

**Canonical-invariance statement**: this pass modified no canonical/theory file. It created three non-canonical files (this report + one assumption map + one proposals memo). No theorem, axiom, definition, equation, or claim status was changed.
