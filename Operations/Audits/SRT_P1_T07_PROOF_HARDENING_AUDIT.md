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

## 0. The six core questions (answers up front)

1. **Does "nonzero probability at each step" imply almost-sure entry into `∅`?** **No.** It does not even imply positive *eventual* termination without a reachability premise, and it never implies *almost-sure* termination. (§3, §4)
2. **What minimal mathematical conditions are additionally required?** Empty-state reachability **plus** one of: a uniform hazard lower bound (`h_t ≥ δ>0`), or divergence of the conditional cumulative hazard (`Σ h_t = ∞` a.s., via Lévy's conditional Borel–Cantelli), or an irreducible-to-absorbing recurrence structure with no neutral closed class avoiding `∅`. (§4)
3. **Do these already exist in SRT definitions?** **No.** `A_t`, "ε-neutral", "continued selectability", and the stochastic transition itself are not formally defined at the level these premises need; the stable-ISP definition (P1-T06) is stated non-probabilistically. (§2)
4. **Do these premises smuggle ε_pg back in?** **Yes, or plausibly yes, for the load-bearing ones.** The reachability / no-safe-neutral-class / hazard-divergence premises are co-referential with ε_pg's branching bias (`B≥2 ≻ B≤1`); the uniform-δ premise is a mis-directed pro-closure drift. (§5)
5. **What can P1-T07 prove at most?** At most **positive termination probability** (given reachability at some step). **Not** almost-sure termination, **not** finite expected termination time, **not**, therefore, "P terminates ⇒ not a stable ISP". (§4)
6. **Can ISP-level ε be derived independently of ε_pg?** **Not established.** Every route that closes the proof imports an ε-like premise or is analytic; the corpus itself scopes the honest version as *local, postulate-grade* (`L0_Metaphysics §六`). (§5, §9)

## 1. Object

`Core/SRT_Core_21b_Constitutive_Theorems.md` **P1-T07** (canonical, claim_level P1). Statement: *for any stable ISP `P` under `L_0` irreversibility, `P` necessarily contains an ε-type anti-closure asymmetric bias.* Proof Sketch Step 3 (verbatim): *"Neutral `P` has nonzero probability of selecting into `A_{t*}=empty` at each step; over sufficient iterations, cumulative probability tends toward 1."*

## 2. Formal reconstruction of the current proof

To test Step 3 we must make the implicit stochastic model explicit. The theorem does not supply one; the following is the **minimal** charitable formalization.

- **Reachable-selection set** `A_t`: the set of selections available to `P` at step `t`. `A_t = ∅` is the terminal/absorbing configuration (P1-T06 cond. 1 requires `A_t ≠ ∅` to select).
- **Absorbing terminal** `∅`: by `L_0` irreversibility (`SRT_Irreversibility.md` Def-IRR / T-IRR-2), `A_{t*}=∅ ⇒ ∀t>t*` no `Ĝ_θ` yields a new selection. **Absorbing is well-defined and canonical.**
- **History filtration** `H_t` = σ-algebra of the process up to `t`.
- **Conditional death hazard**: `h_t := P(A_{t+1}=∅ \mid H_t,\ A_t ≠ ∅)`.
- **Stable ISP** (P1-T06 result-state criterion): iterative (`A_t≠∅` each `t`), perspective-bearing, history-bearing (writeback `A_t → A_{t+1}`), **re-selectable (continues selecting across steps)**.
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

Even granting `h_t > 0` for **all** `t` (proposition 3, itself unstated), a.s. termination does **not** follow. By **Lévy's conditional Borel–Cantelli lemma**, for events adapted to `H_t`, `{A_{t+1}=∅ \text{ i.o.}} = {Σ_t P(A_{t+1}=∅\mid H_t) = ∞}` a.s. Termination is a.s. **iff** the conditional cumulative hazard diverges. If `Σ_t h_t < ∞` — which is fully compatible with every `h_t > 0` — the survival probability `∏_t (1-h_t) > 0`, so `P(P` never terminates`) > 0`. On those paths `P` keeps selecting forever and **is** a stable ISP. Hence "neutral ⇒ terminates ⇒ not stable ISP" fails on a positive-probability set.

Moreover neutrality does not even give proposition (3): a neutral process may have `h_t = 0` (it simply never drifts toward `∅`). "No anti-closure bias" ≠ "positive closure bias."

## 4. Four proof versions

### Version A — Uniform hazard lower bound (`h_t ≥ δ > 0`)
- **Yields**: a.s. termination *and* finite expected time (`P(survive to t) ≤ (1-δ)^t → 0`, `E[τ] ≤ 1/δ`). **Sufficient.**
- **Where does δ come from?** Nowhere in the corpus. Worse, it is a **uniform positive drift *toward* `∅`** — a *pro-closure* assumption. Neutrality (absence of anti-closure bias) does not supply a positive death drift. So Version A does not model "ε-neutral"; it models "actively dying," which begs the result in the wrong direction.
- **ε-status**: not ε (it is anti-ε); but illegitimate as a model of neutrality → **category D/E** (mis-assumption).

### Version B — Divergent cumulative hazard (`Σ h_t = ∞`)
- **Yields**: a.s. termination (via Lévy), **no** finite-expected-time guarantee. **Sufficient for the theorem's needs.**
- **Requires**: a conditional/martingale structure (Lévy applies to conditional probabilities, so it is available), plus the substantive claim that a neutral `P` has non-summable death hazard.
- **Is this weaker than ε_pg?** The divergence claim is precisely "neutrality cannot keep `Σ h_t < ∞`", i.e. "neutral dynamics cannot sustain non-self-erasure indefinitely." That is the **contrapositive of ε_pg's `B≥2 ≻ B≤1` branching bias**. So it is **not** obviously weaker — it restates ε_pg's content as a hazard-divergence premise. **Category C** (local projection of ε_pg).

### Version C — Finite/countable recurrent system, `∅` reachable & absorbing
- Model neutral `P` as a Markov chain on reachable-set configurations, `∅` absorbing.
- **Yields**: a.s. absorption **iff** every recurrent class either is `{∅}` or communicates with `∅` — i.e. **there is no neutral closed communicating class avoiding `∅`**.
- **The load-bearing premise is exactly "no safe neutral class."** Nothing in P1-T06/T07 forbids one (Countermodel D2/D5). Asserting its absence is asserting that neutrality cannot form a self-sustaining non-`∅` cycle — again **ε_pg's non-self-erasure claim**. **Category C/D.**

### Version D — Countermodels (each a valid stochastic/transition system)
| # | Countermodel | Terminates a.s.? | Blocked by which formal condition? |
|---|---|---|---|
| D1 | `h_t = 2^{-t}` (all `h_t>0`, `Σh_t = 1 < ∞`) | **No** — survival prob `∏(1-2^{-t}) ≈ 0.29 > 0` | none in P1-T06/T07 |
| D2 | Neutral closed 2-cycle `{a,b}`, both `≠∅`, `∅` unreachable from it | **No** | none — no reachability premise |
| D3 | `∅` reachable but only with total probability `<1` (transient toward a safe region) | **No** | none — no recurrence premise |
| D4 | Infinite non-terminating trajectory retaining `A_t≠∅` (e.g. random walk on ℕ with reflecting 0-neighbourhood) | **No** | none — no hitting guarantee |
| D5 | Deterministic period-2 orbit, `h_t=0` ∀t | **No** | none — determinism is "neutral" (no *bias*) yet survives |
| D6 | Hazard decays to 0 (`h_t ↓ 0`, `Σh_t<∞`): long-run survival stays positive | **No** | none |

**For each countermodel**: it satisfies irreversibility (`∅` absorbing is respected — it is simply never reached), and it satisfies the *stated* stable-ISP conditions (it keeps selecting). Whether it counts as **"ε-neutral"** cannot be decided, because ε-neutral is undefined. Two exhaustive readings:
- If ε-neutral = "no active anti-closure maintenance / no hazard lower bound", then **D1–D6 are ε-neutral and survive ⇒ P1-T07 is false as stated.**
- If ε-neutral is defined so as to exclude D1–D6 (e.g. "has non-summable death hazard"), then that exclusion **is** the ε-bias ⇒ **P1-T07 is analytic/circular** (it assumes the hazard structure it concludes).

Either horn blocks an unconditional proof.

## 5. Is ε_pg hidden in the premises?

Classify each candidate closing premise (A=truly independent, B=weaker than ε_pg, C=local projection of ε_pg, D=renamed ε-like primitive, E=undecidable):

| Premise | Classification | Reason |
|---|---|---|
| `∅` absorbing | **A (independent)** | pure irreversibility; but insufficient alone |
| `∅` reachable (proposition 2) | **C** | "neutral dynamics can always reach self-erasure" is the negation of ε_pg's `B≥2` favouring; co-referential |
| `h_t ≥ δ > 0` (Version A) | **D/E** | a *pro-closure* drift; not a model of neutrality — mis-assumption |
| `Σ h_t = ∞` (Version B) | **C** | = "neutrality cannot sustain non-self-erasure", contrapositive of ε_pg branching bias |
| "no safe neutral closed class" (Version C) | **C/D** | = ε_pg's non-self-erasure necessity, restated as a topology-of-chain premise |
| persistence / askability prior | **C** | `L0_Metaphysics §六`: "any position that can accumulate/remember/ask must **locally** satisfy non-self-erasure" — this **is** local ε, and the file says it proves only *local* ε, not global |

**Verdict**: the premises that would make Step 3 valid are, for the load-bearing ones, **co-referential with ε_pg** (branching / non-self-erasure), or illegitimate (Version A). The proof cannot be closed by a premise that is demonstrably ε-independent. Therefore **ε_pg-independence at the ISP level is not established**, and the strong reading in which P1-T07 *derives* ε from irreversibility alone is unsupported.

## 6. Corpus contradictions found (recorded, not resolved)

1. **Postulate vs theorem-consequence.** `Core_Law/SRT_L0_Metaphysics.md:202`: "ε 是公设，不可被升格为定理" (ε is a **postulate**, must **not** be upgraded to a theorem). `Core_Law/SRT_Irreversibility.md:240`: "ε_pg > 0：由 P1-T07 反证法保证" (ε_pg>0 is **guaranteed by** P1-T07's proof-by-contradiction). These are contradictory on whether ε_pg is an input postulate or a derived consequence.
2. **Circular dependency.** P1-T07 bridge relation step 1 uses ε_pg ("existence of asymmetry") as an **input**; `Irreversibility.md:240` uses P1-T07 as the **source** of `ε_pg>0`. ε_pg is both premise and conclusion of the same argument.
3. **Local vs global.** `L0_Metaphysics:202` explicitly scopes the askability argument as proving only **locally-valid ε**, "不能推广到全局 L0" — yet P1-T07/T-IRR-3 state the necessity without that locality qualifier.
4. **Undefined primitive.** "ε-neutral" is load-bearing in the proof but has **no formal definition** in the canonical corpus.
5. **Non-probabilistic definition, probabilistic proof.** P1-T06 defines stable ISP without any transition-probability structure; P1-T07 Step 3 silently introduces one (`h_t`), so the proof's object is not the definition's object.

## 7. Collective version — T-COLL-3

`Core_Law/SRT_Collective_Selection.md §5 T-COLL-3` proof (line 498) is **explicitly "与 P1-T07 同构" (isomorphic to P1-T07)**: collective neutrality ⇒ `A_𝒫(t)` has nonzero probability of collapsing to `∅` ⇒ absorbing ⇒ not a stable collective ISP.

- **Same proof shape** ⇒ **inherits the identical Step-3 gap.**
- **No independent collective reachability/hazard premise** is supplied.
- It defines `σ_sr^coll → 1 ⇔ ε^coll → 0` (line 504) — again defining neutrality by the closure condition (same circularity, lifted).
- **Individual vs collective termination** are structurally distinguished (T-IRR-2 "集体终止") but the *proof* does not use that distinction to add a premise.
- **Cannot** serve as independent support for P1-T07: an isomorphic copy of the same invalid inference is not corroboration.

## 8. What the theorem CAN stand on (unconditionally)

- The **absorbing** character of `∅` under irreversibility — solid.
- **Positive termination probability** given reachability at some step — solid but weak (compatible with positive survival probability, so it does **not** yield "not a stable ISP").
- The **local, conditional** statement: *a process that maintains a non-summable death hazard under neutral dynamics terminates a.s.* — solid, but this is Version B with its premise made explicit, and the premise is ε-co-referential.

Everything stronger (a.s. termination for *all* neutral stable-ISP candidates; ε-independence) is **not** currently proven.

## 9. Decision gates

### P1-T07 Proof Gate
- **Is the stated theorem valid?** **Not as proved.** The statement may be *true under an added premise*, but the current Proof Sketch does not establish it.
- **Is the current Proof Sketch valid?** **No** — Step 3 is a non-sequitur (§3); it conflates six distinct propositions (§2).
- **Strongest unconditionally supported conclusion**: `∅` is absorbing; neutral `P` has *positive* termination probability given reachability. **Not** a.s. termination.
- **Minimal sufficient assumption set**: reachability of `∅` **and** (uniform `h_t≥δ` **or** `Σh_t=∞` a.s.) **and** no neutral closed class avoiding `∅`.
- **Uniform hazard needed?** Sufficient but illegitimate as a neutrality model (Version A).
- **Cumulative-hazard divergence enough?** Yes (with Lévy), and it is the honest minimal premise — but it is ε-co-referential.
- **Valid countermodels exist?** **Yes** (D1–D6), each blocking the unconditional claim.
- **Confidence**: **high** that the current proof is invalid as written (this is standard probability); **medium** on the exact minimal premise set; **medium** on the ε-co-reference classification (interpretive).
- **GO / NO-GO for a theorem-amendment proposal**: **GO** — the evidence supports a controlled amendment PR (options in `Operations/Proposals/SRT_P1_T07_HARDENING_OPTIONS.md`). **NO-GO** for editing P1-T07 in this pass.

### ε_pg Independence Gate
- **Can P1-T07 stand independent of ε_pg?** **Not established.** Every closing premise is ε-co-referential (§5) or illegitimate.
- **Which premises may be hidden ε?** reachability, `Σh_t=∞`, "no safe neutral class", askability-persistence — all category C/D.
- **GOV-SUB01 residue for the anti-closure role (conditional)**:
  - under the current (invalid) proof: **R4** (removal masked by an unstated, ε-co-referential premise);
  - if hardened via Version B/C: **P** (the closing premise is an ε-grade postulate, not an ε-independent derivation) — *not* R2;
  - a clean **R2** (ε_pg dispensable, role carried by an ε-independent structure) is **not** currently reachable on the evidence.
- **What is still missing**: a formal definition of ε-neutral that is **not** the closure condition itself, plus a reachability/recurrence premise with an **ε-independent** justification. Absent both, the R2 reading is unsupported.

### Collective Gate
- **Does T-COLL-3 close independently?** **No.**
- **Does it inherit the same gap?** **Yes** (isomorphic proof, no independent premise).
- **Can it corroborate P1-T07?** **No** — same invalid inference cannot support itself.

## 10. Recommendation (not executed)

Proceed to a **controlled theorem-amendment proposal** (see the Proposals file), which does **not** edit canonical text this pass. Route the missing formal `ε-neutral` definition and the reachability premise to the proof layer. Log the five corpus contradictions (§6) for governance; do not "fix" them by wording.

**Canonical-invariance statement**: this pass modified no canonical/theory file. It created three non-canonical files (this report + one assumption map + one proposals memo). No theorem, axiom, definition, equation, or claim status was changed.
