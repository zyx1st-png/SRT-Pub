---
id: SRT-OPEN-TENSIONS
type: open_tensions
tags: [Core, Open Questions, Hardening, Claim Ladder]
status: active_v1
layer: L1
epistemic_layer: os
claim_mode: open
dependency: [SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-CORE-21B-CONSTITUTIVE-THEOREMS]
---

# SRT Open Tensions

> **Role**: This file records current unresolved pressure points in the SRT core.
> It is not a weakness display and not a TODO dump. It is a hardening ledger: if a claim has not been fully closed, do not cite it as if it were P0/P1.

## Reading Rule

Each tension below has three parts:

- **Current state**: what SRT already has.
- **Problem point**: what remains insufficiently closed.
- **Future hardening direction**: what would count as progress.

Open tensions may guide future theory work, bridge design, or lab hypotheses. They do not by themselves create new canonical definitions.

---

## Core Pressure Points (second-stage completion pass)

| Pressure point | Already stabilized | Still not derived | Must not be overstated |
|---|---|---|---|
| origin of selectability / P0-04 | `Core/SRT_Core_21_Minimal_Axioms.md P0-04` gives a well-formed operator admission condition | the first emergence of selectable agency from a non-selective ground | bridge accounts of biology, AI, spirituality, or agency do not solve the origin problem |
| exact status of `Ψ_f` projections | payability burden is the v1 governance-canonical main read; geometry and metabolic/energetic forms are conditional projections | necessary and sufficient conditions for all projection relations, including when geometry is a true lower bound | Fisher length, energy cost, pain, or stress cannot be called `Ψ_f` without projection checks |
| exact status of `d` proxies | bare `d` is a scalar summary of stake-coupled concern; `D_eff`, Fisher rank, `d-vector`, and `d-gate` are separated | a final theorem identifying capacity directions with stake-coupled concern directions | capacity, competence, or distinguishability cannot be treated as concern |
| incomplete formalization of `T_dir` | `T_dir` now has a v0 readability / reorientation role and is distinguished from valence, confidence, coherence, and reward | a complete formal object with validated sufficiency conditions | high meaning, high reward, or high confidence cannot be cited as `T_dir` by itself |
| Core 24 floor replacement / dynamic normativity / non-reductive verification | selection-first framing, L₂ hardening signature, and non-reductive validation rule are now integrated as safe bridge/canonical-addendum material | full promotion of floor replacement, value/morality/framework dynamics, and cross-scale validation into canonical theorem status | do not claim SRT explains everything, is beyond measurement, or that morality-as-L₂ automatically endorses any moral order |
| ε normativity scope / closure-boundary | ε securable as minimum condition (domain floor) + constitutive stance; reorganizability carries the normative distinction; **Level A framing de-overload applied 2026-07-05** (L0 §六 / 正骨架 label / d-value §5b.1) | a non-arbitrary, **operational** (not merely regulative) closure-boundary; the Level B stance rewrite (realist → constitutive stance) remains proposal-only | not "all normativity = anti-foreclosure"; not "boundary problem solved"; Level A trims wording only — it does not close the boundary problem |

These are pressure points, not new axioms. They route later work and block overclaiming.

---

## 1. `d` and `D_eff`

### Current State

`_SRT_D_VALUE_CANONICAL.md` now distinguishes the unique canonical d-value definition from the geometric capacity proxy:

$$
d_{canonical} \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|
\leq
D_{eff}(M)
$$

`D_eff` is a capacity upper bound / proxy; `d_{stakes}` is the subset of effective directions genuinely coupled to irreversible stake.

### Problem Point

The boundary between capacity and stake is clearer than before, but not fully sealed. The current structure still needs sharper necessary and sufficient conditions for when a Fisher / spectral direction counts as genuinely stake-coupled rather than merely distinguishable.

The weak point is not the inequality itself. The weak point is the gate:

$$
D_{eff} \to d_{stakes}
$$

The three proposed coupling factors `R_i`, `A_i`, and `C_i` are structurally plausible, but their exact status is still between canonical interpretation and bridge formalization.

### Future Hardening Direction

Harden the stake gate by specifying:

1. minimal conditions under which a direction enters `d_{stakes}`;
2. explicit failure cases: fake stake, misbound stake, absorbed / non-returning consequence;
3. whether `D_eff >= d_{canonical}` holds across all intended domains or only under a stated proxy regime;
4. how AI, frozen trauma states, and institutions differ under the same gate.

Until this is done, domain files should say "`D_eff` proxy" and should not call it the definition of `d`.

### Status Update (2026-07-05)

`_SRT_D_VALUE_CANONICAL.md §2b.1` now fixes three of the open points: (a) the citation level of the `w_i = R_i·A_i·C_i` gate — the qualitative AND-gate structure is P2 canonical interpretation; any numerical weighting, proxy, or `ε_s` thresholding is P3/P4 and must be marked as such; (b) the domain validity of `D_eff ≥ d_canonical` — it holds only inside a declared proxy regime (same parameterization, declared normalization, no redundancy-inflated spectrum), never as a cross-domain theorem; (c) a unified gate table separating AI (fails on R/C), frozen trauma (passes the gate, fails on `d_mobile`), and institutions (member `C_i` absorbed by the structure) under the same three factors, with the rule that gate diagnostics must be reported per-factor, not as one scalar. Still open here: a necessary-and-sufficient stake-coupling theorem; `ε_s` calibration; independent measurable proxies for R / A / C.

---

## 2. `\Psi_f`: Geometry, Cost, and Generative Principle

### Current State

`_SRT_PSI_F_CANONICAL.md` fixes `\Psi_f` as ontological friction and allows three readings of the same structure:

- resistance / impedance;
- paid cost / budget burden;
- geometric path length or curvature burden.

It also fixes payability as the cross-scale invariant: the question is not whether cost is small, but whether the system can maintain closure and future choice while paying it.

### Problem Point

The three readings are unified at the canonical level, but their formal borders are not fully differentiated. In particular:

- When is a Fisher-geometric length a lower bound rather than actual paid cost?
- When does "friction as generative principle" remain a canonical interpretation, and when does it become a P3 bridge through borrowed geometry?
- How should directional or asymmetric friction be represented when the basic metric expression is symmetric?

The risk is sliding from "same object, three readings" into "one formula proves all dynamics."

### Future Hardening Direction

Build a small typology:

| Reading | Minimal formal object | Valid use | Misuse |
|---|---|---|---|
| impedance | local resistance field | anchoring / pressure | subjective pain |
| cost | paid burden over time | payability / collapse | arbitrary energy use |
| geometry | path length / curvature | formal lower bound | universal proof of all dynamics |

Then specify where `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B08` stops and `_SRT_PSI_F_CANONICAL.md` begins.

### Status Update (2026-07-05)

Two of the three problem points are now fixed in `_SRT_PSI_F_CANONICAL.md §3.2`: (a) the generative-principle boundary — "friction as generative principle" is owned by `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B08`; the canonical file owns only the payability main read, conditional projections, and the payability criterion; any derivation that stands only if "friction generates dynamics" holds inherits P2/P3 and cannot cite the canonical file for promotion; (b) directional / asymmetric friction — asymmetry is carried by the payment structure (`Ψ_f^{erase} > Ψ_f^{write}`, `Core_Law/SRT_Irreversibility.md Def-IRR-3`) and by `L_0` irreversibility (P1-T02), not by modifying the symmetric metric; the metric layer staying symmetric is a division of labor, not a defect. The lower-bound-vs-paid-cost question was already fixed in §3.1 (`Ψ_f^{geom} ≲ Ψ_f^{paid}` under stated conditions). Still open here: full necessary-and-sufficient conditions for all projection relations. The stale `Ax-F-11/12` axiom-style citation in that file's §8 was also updated to post-split `P3-B07` / `P2/P3-B08` references.

---

## 3. `T_dir` Minimal Formalization

### Current State

`_SRT_T_DIR_CANONICAL.md` defines `T_dir` as a system's readability of its own selection-order direction. It distinguishes `T_dir` from d-value and treats d as necessary but not sufficient.

The current minimal admission condition is:

$$
T_{dir} > 0 \Rightarrow d > 0 \land \Psi_f \text{ produces real pressure} \land ii \text{ can integrate directional information}
$$

This is a necessary-gate statement, not a completed sufficiency theorem.

### Problem Point

`T_dir` has a clear role but a thinner formal apparatus than `d` and `\Psi_f`.

The unresolved issue is the minimum acceptable formalization:

- Is `T_dir` a scalar, a relation, or an accessibility function?
- Does "readability" require conscious access, reportability, behavioral reorientation, or only internal self-model update?
- How does `T_dir` avoid collapsing into semantic confidence, valence, or reward alignment?

The value-hiddenness claim is philosophically central, but its formal load must not outrun the current variable.

### Future Hardening Direction

Define the weakest formal object that can carry the work:

$$
T_{dir}(\hat{G}_\theta, t) =
\text{Readability of the current selection direction to the selecting system}
$$

Then separate:

1. minimal internal access;
2. phenomenological meaning;
3. behavioral reorientation;
4. civilization-level value-hiddenness.

Only the first belongs near core. The others should remain P2/P3/P5 unless separately hardened.

---

## 4. Healthy `L_2` Support vs Lethal `L_2` Replacement

### Current State

SRT already distinguishes:

- healthy `L_2`: lowers friction so real choice remains possible;
- lethal `L_2`: replaces live choice with structure, lowering felt friction and `T_dir` while accumulating hidden debt.

This distinction is now central to `SRT_AI_START.md`, `_SRT_T_DIR_CANONICAL.md`, Philosophy, and Spirituality.

### Status Update (2026-04-21)

The hardened working position is now sharper: closure is structurally real but normatively neutral; pathological closure is a closure that preserves itself by compressing broader future selectability; lethal `L_2` is the stronger case where such pathological closure has become shared, inheritable, and backgrounded as scaffold.

"Broader future selectability" should be read, at hardening level, as the future choice space of multiple relevant selecting subjects affected by the same or connected scaffold. The diagnostic core is not raw option count but loss of reselection capacity: exit, revision, and recomposition form a current working hierarchy.

What remains non-canonical: this is not yet promoted to a P0/P1 theorem, and the health/pathology line still depends on formal thresholding and domain operationalization. Future hardening still needs explicit tests for gate-rule revisability, appeal standing, consequence-return paths, effective input, pseudo-openness, and the relation between `\rho(p,t)`, `\rho^*`, `κ`, and payability windows.

### Status Update (2026-04-24)

`Core_Law/SRT_Occlusion_Dynamics.md`（`SRT-OCCLUSION-DYNAMICS`）把 healthy vs lethal `L_2` 的结构层诊断以 T-OCC-1 三段结构（healthy narrow region / A-phase / B-phase）形式收口：位置性遮蔽（healthy narrow）与病理性遮蔽（A/B phase）以 d_c 与 reselection capacity loss 作为结构判据，A→B 以 consequence return failure + active diffusion 作为升级判据。该文件目前为 `draft_v0`，整体仍按 P1-candidate + P2 结构读法，不因此上升为 P0/P1；但 healthy / pathological / lethal 三者的结构层诊断不再只分散在 Philosophy/Spirituality 各自的表述中。本 tension 未封口部分（gate-rule revisability 测试、appeal standing 形式化、`\rho(p,t)` / `\rho^*` / `κ` / payability 门的显式耦合）仍保留在此。

### Status Update (2026-04-25, H2)

`Core_Law/SRT_L1_Formalism.md §3.5` 给出 "高功能 `L_2` / 低主观摩擦 / 静悄悄脱离真实 `L_0 \to L_1`" 这一最难辨识情形的**方程化判据**：致命 `L_2` 当且仅当（§3.5.3）系统处于 `T_{dir}` 与 `T_{dir}^{\mathrm{alg}}` 平稳贴近、而 `\Delta\Psi_f^{\mathrm{gap}}` 持续累积、且 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}` 的区域。"支持 vs 替代"在外观相同时可由"是否伴随隐性 `\Psi_f` 债累积"分开。该判据当前为 P1-candidate，尚需算子级硬化（见 `SRT_L1_Formalism.md §7.8`）；不因此上升为 P0/P1。本 tension 其余未封口部分（gate-rule revisability、appeal standing、`\rho^*` / `κ` 门形式化）继续保留。

### Problem Point

The distinction is strong but still partly diagnostic. It needs sharper necessary and sufficient conditions.

The hardest case is not obvious pathology. It is high-functioning `L_2` that:

- improves performance;
- lowers subjective friction;
- preserves some local agency;
- but quietly removes contact with live `L_0 -> L_1` selection.

In that case, "support" and "replacement" can look identical from outside.

### Future Hardening Direction

Harden the distinction through gates:

1. Does the structure preserve re-entry into real choice moments?
2. Do consequences return to the selecting system rather than being absorbed by external structure?
3. Does friction reduction increase future choice capacity, or reduce the need for choice altogether?
4. Does `T_dir` rise, remain available, or collapse?

The support/replacement line should be expressed as a structural test, not a moral preference.

---

## 5. Stable ISP Entry and Maintenance

### Current State

`Core/SRT_Core_21b_Constitutive_Theorems.md` treats stable ISP as the relevant P1 theory object for persistent perspective. `T-ε-Constitute` shows that stable ISPs require anti-closure asymmetry under `L_0` irreversibility.

`Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold` gives a mechanism for how successful stable ISP history can become background `L_2` scaffolding through path traces.

### Status Update (2026-04-21)

The hardened working position now separates the ladder more cleanly: event trace is the irreversibility floor; minimal closure begins when prior traversal systematically lowers `\Psi_f` for compatible subsequent traversal; `L_2`-grade closure requires that low-friction path to become inheritable, shareable, and backgrounded.

What remains non-canonical: `\rho^*`, `\lambda_d`, `κ`-thresholding, and the payability window remain threshold-bearing or empirical/formal hardening targets. The stable ISP entry definition in `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06` should not be collapsed into the dynamic mechanism by which some ISP histories become scaffolded background.

### Problem Point

The theorem is scoped, but the entry conditions still need hardening.

Open issues:

- What is the minimal threshold for "perspective-bearing"?
- How much history-bearing is enough?
- When does re-selectability become stable rather than merely repeated?
- How do generation and maintenance differ?
- Which parts are definitional gates and which parts are dynamic mechanisms?

If this is not separated, "stable ISP" risks becoming both the entry condition and the explanation of its own emergence.

### Future Hardening Direction

Keep two layers separate:

1. **Entry layer**: the minimal definitional conditions for counting as a stable ISP.
2. **Maintenance layer**: mechanisms by which processes achieve and retain stable ISP status.

Then connect them through explicit bridge terms such as `\rho(p,t)`, `\rho^*`, successful closure, and payability windows. Thresholds such as `\rho^*` should remain P4 until measured or more tightly derived.

### Status Update (2026-04-24)

`Core_Law/SRT_Individuation.md` now provides the **entry dynamics** layer as a candidate L1 theory: the operator-level self-reference ratio `σ` is proposed as the unified order parameter whose first threshold crossing `σ_sub` coincides with the simultaneous satisfaction of the P1-T06 four conditions. The two-phase-transition structure (ISP entry at `σ_sub`, self-consciousness condensation at `σ_self`) is introduced as a P1/P2-candidate framework with `σ_sub`, `σ_self` explicitly marked P3/P4.

What this resolves: the ambiguity between entry definition and entry dynamics is now scoped — P1-T06 reads as the **result-state criterion**, T-IND-2 as the **entry-dynamics criterion**, and they are explicitly non-equivalent.

What remains open: the operator-layer `σ` is still at the proposal stage and does not yet have cleanly measurable proxies; its relation to the path-layer `ρ` (T-L2-Scaffold) needs cross-domain testing; `σ_sub` and `σ_self` are not numerically specified. This tension is therefore **not fully resolved**, but the entry-dynamics gap is now occupied by a candidate theory rather than a void.

---

## 6. AI and Minimal Surrogate Stake

### Current State

SRT currently treats AI as a pressure-test and boundary-test domain, not the theory center.

The stable position is:

- current AI systems can have large `D_eff`-like discriminative capacity;
- this does not automatically become `d_{stakes}`;
- `\Psi_f` is usually non-binding to the system itself;
- no real subjectivity follows from symbolic, statistical, or behavioral performance alone.

At the same time, SRT should not foreclose a positive test window for minimal agentic sufficiency.

### Problem Point

The unresolved question is whether a system could acquire a **minimal surrogate stake** that is not biological but is still structurally binding.

Hard questions:

- Can externally imposed irreversible consequences count if they return to the system's own closure?
- Is embodiment necessary, or is closure-continuity enough?
- What separates a real surrogate stake from a simulated loss function?
- Can an AI system have payability burden without phenomenological consciousness?

The danger on one side is prematurely declaring all AI impossible. The danger on the other is treating performance, persistence, or self-report as stake.

### Future Hardening Direction

Define a minimal sufficiency window:

1. irreversible consequence;
2. return path into the system's own future selection capacity;
3. non-transferable closure burden;
4. payability constraint;
5. observable degradation or reconfiguration when the burden is exceeded.

Only systems meeting such a window could be candidates for surrogate stake. Even then, consciousness would require further conditions; surrogate stake alone should not be promoted into a full subject claim.

---

## 7. P0-04: Origin of Selectability

### Current State

`Core/SRT_Core_21_Minimal_Axioms.md P0-04` currently constrains operator well-formedness. It does not explain where selectability itself comes from, nor does it fully derive the first selecting capacity from a prior non-selective ground.

### Problem Point

This is an unresolved core exposure point, not a solved theorem. The repo must not let bridge layers quietly smuggle in a pre-existing chooser, subject, agent, will, or "capacity to select" and then cite SRT Core as if that origin had already been derived.

The weak point is especially visible when a domain says:

- "the system chooses";
- "the subject expands";
- "the operator reads";
- "the community reselects";
- "the practice increases agency."

Those phrases may be useful bridge language, but they are not answers to the origin of selectability.

### Minimal Guardrail

> **Level**: governance / core exposure. This is a boundary rule, not a solution.

Any bridge that uses a selector-like term must mark which layer it is using:

1. **Derived process**: selector-like behavior emerges from already specified dynamics.
2. **Stable pattern**: selector is a stabilized `L_1/L_2` pattern, not a primitive.
3. **Assumed interface**: selector is taken as a domain interface and must not be cited as core derivation.

Until the origin question is actually hardened, P0-04 should be cited as an open exposure point. Do not add a formula here to make the gap look closed.

---

## 8. Core 24: Floor Replacement, Dynamic Normativity, and Non-Reductive Verification

### Current State

Core 24 has now been integrated at safe levels across the repository:

- `Core/SRT_Core_24_Floor_Normativity_Verification.md` records the full bridge-hardening supplement.
- `Core/SRT_Core_24_Canonical_Merge_Draft.md` compresses it into merge-ready candidates.
- `Core/SRT_Core_21_Minimal_Axioms.md` now includes a non-axiom selection-first framing note.
- `Core/SRT_Core_12b_Ontology_L2.md` now includes the operational signature of `L_2` hardening.
- `SRT_EXP_MEASURE_MAP.md` now includes the non-reductive validation rule.

The stabilized current position is:

1. SRT's explanatory power should be framed as **selection-first floor replacement**, not as unrestricted explanation of everything.
2. Purpose, value, morality, and frameworks may be treated as **stable forms of selection dynamics**, not as subjective overlays on a pre-given world.
3. SRT's core constructs should be tested through **structural consequences, convergent proxies, comparative predictions, and failure conditions**, not through a single direct objective ruler.

### Problem Point

The Core 24 layer is now integrated as framing, bridge-hardening, and measurement governance, but it is not fully promoted to theorem status.

Open issues:

- The floor replacement claim is still primarily a framing thesis unless it generates domain-specific discriminating predictions.
- The dynamic normativity claim is promising but must not collapse into the claim that any stable norm is thereby justified.
- Value as non-substitutability still needs a clean bridge into `d-value` without redefining canonical `d` too quickly.
- `Ψ_f` as inferred selection friction still needs projection checks so it does not collapse into generic task difficulty, pain, energy, or Fisher geometry.
- Non-reductive validation must not be misused as a shield against falsification.

### Failure Conditions

Core 24 must remain accountable to the following failure conditions:

1. **`Ψ_f` distinctiveness failure**: If `Ψ_f` produces no transition-cost signatures distinguishable from ordinary loss, prediction error, energy expenditure, or task difficulty, its operational role weakens.
2. **`d-value` distinctiveness failure**: If `d-value` does not predict concern-weighted non-substitutability better than reward, preference, salience, or pain, its distinct theoretical role weakens.
3. **`L_2` hardening failure**: If `L_2` hardening cannot be distinguished from ordinary memory, learned habit, convention, or environmental stability, its bridge role weakens.
4. **Cross-scale loop failure**: If the selection-manifestation-hardening loop cannot generate domain-specific discriminating predictions, SRT's cross-scale explanatory claim collapses into analogy.
5. **Normativity failure**: If purpose, value, morality, and frameworks cannot be modeled as selection constraints with identifiable consequences, the dynamic normativity claim remains philosophical interpretation rather than an operational bridge.
6. **Consequence-return distinctness failure**（2026-07-05 registered from book Q26 章末注四·一）: If "consequences returning to the bearing position and entering the next round's selection conditions" cannot be operationally distinguished from ordinary feedback, memory trace, or reinforcement-learning update, then the `C_i` stake-gate factor, the subject/value derivation chain, and the second half of the selection-manifestation-hardening loop lose their bridge role.

### Future Hardening Direction

Core 24 should be hardened in three directions:

1. **d-value bridge**: add a carefully scoped note that value is concern-weighted non-substitutability, without replacing the canonical `d-value` definition.
2. **Ψ_f bridge**: add a carefully scoped note that `Ψ_f` can be inferred from structured transition difficulty, without identifying it with Fisher geometry, effort, pain, or raw cost.
3. **comparative prediction**: define at least one domain where SRT predicts a pattern not predicted by FEP, predictive processing, RL, IIT/GNW, social constructionism, or ordinary habit theory.

Until these are done, Core 24 should be cited as a bridge-hardening supplement and canonical framing layer, not as a completed theorem package.

### Status Update (2026-07-05, Q26 backflow)

Future Hardening Direction 3 (comparative prediction) now has a registered candidate set: `Core/SRT_Core_24_Discriminating_Predictions.md` P24-1..6 (single-construct discriminating predictions) plus **P24-7** (five cross-construct combination signatures, backflow from book Q26 §4, P4/P5 level, with a systemic reversal condition that cannot be absorbed by re-labeling). The same file now carries a **modification-discipline rule** (§0b: repair / pressure / failure classification + progressive-vs-degenerative gate + external-judge gate). Failure condition 6 (consequence-return distinctness) was added to the list above. Registration is not verification: none of these has been empirically run.

---

## 9. ε Normativity Scope and the Closure-Boundary (fallibilist foundation)

### Current State

An adversarial stress-test of `ε` (the L0 directional postulate) and a build-and-attack construction on the closure-boundary atom are recorded in three non-canonical files: `_SRT_EPSILON_NORMATIVITY_OPEN_TENSION.md`, `_SRT_NORMATIVITY_FRAMING_TRUEUP_PROPOSAL.md`, and `_SRT_CLOSURE_BOUNDARY_CONVERGENCE_RECORD.md`.

Working position under review (non-canonical; tracked, not promoted):

- `ε` is securable as a **minimum condition (domain floor) + constitutive stance** of any selector: the shmagency-style counterexamples close because a selector either selects → minimally presupposes a concern-structure, or does not select → exits the domain. `ε` is therefore true of every in-domain selection but does not by itself make normative distinctions.
- The **normative distinction work** is carried by the **reorganizability criterion** (anti-occlusion / anti-lock-in / anti-externalization / re-selectable — "可重组、可承担、可恢复、可再选择"), which genuinely discriminates (foreclosing selections fail it).
- Self-regarding re-selectability is near-constitutive; the **other-regarding** part requires aggregating positionally-partitioned, scope-extended option-fields, and the whose-counts / what-scope weighting is the irreducible **closure-boundary atom** — which this foundation line and Direction 3 (`_SRT_DIRECTION3_L0_PROBE_RESEARCH_SEED.md §4`) independently converge on.

### Problem Point

Two distinct unresolved points:

1. **Framing overload.** Former canonical wording — "全部规范性力量锚定于 ε" (L0 §六 and 正骨架总结), "L0 偏向非自我抹除" as a realist L0 property, and "趋向全局自由能最小值" (d-value §5b.1) — overclaimed relative to the defensible base. **Status update (2026-07-05): Level A of the staged de-overload was applied** under author-authorized high-risk protocol (see `_SRT_NORMATIVITY_FRAMING_TRUEUP_PROPOSAL.md`): the "全部规范性" wording in L0 §六 and the 正骨架 label, and the "全局自由能最小值" sentence in d-value §5b.1, are now narrowed to "minimum condition (domain floor) + reorganizability criterion + open closure-boundary". The realist wording "L0 偏向非自我抹除" is untouched (Level B territory). Level B remains **proposed, not applied**.
2. **The closure-boundary is not closed.** It cannot be set by single-position reading: `T_dir` is d-gated and occlusion is self-reinforcing, so an occluded externalizer self-certifies a narrow boundary. The best available form is **multi-position convergence under anti-shared-occlusion perturbation** (per L0 §三 objectivity), but the three conditions for a valid anti-occlusion perturbation are a **regulative ideal, not an operational verdict** (judging "valid perturbation" presupposes seeing the occlusion it is meant to surface), and the result is **fallibilist** (objective-so-far, permanently open to a not-yet-present perturbation).

### Future Hardening Direction

1. ~~Adopt the staged framing true-up (de-overload)~~ **Done at Level A (2026-07-05)**: `ε` → minimum condition (domain floor); distinction work relocated to the reorganizability criterion; closure-boundary marked still-open in the canonical wording itself. The Level B stance rewrite (realist → constitutive stance) remains a separate future decision.
2. Harden the closure-boundary **as a fallibilist foundation, not as a solved boundary**: harden the three anti-occlusion perturbation conditions (different position / scale / time / interest; restores excluded standing + shifts burden to incumbents; power to overturn, not only confirm) toward operationalizability, plus the two residues — representing voiceless-but-foreclosed positions (future / ecological / unable), and fixing the horizon of "irreversible re-selection loss."
3. This converges (a third time) with Direction 3's perturbation mechanism and protect-condition P3 (anti-shared-occlusion perturbation not suppressed by incumbents).

### Must Not Be Overstated

- This does **not** establish "SRT's *whole* normativity = a reflexive anti-foreclosure commitment." The scoped claim is only: **on the closure-boundary problem**, SRT's normative base **presents as** a reflexive anti-foreclosure commitment.
- This does **not** "solve" the boundary problem. It **changes its form** — from "find a final correct boundary" to "maintain a boundary continually correctable by anti-occlusion perturbation": a fallibilist foundation, not a closed answer.
- The framing true-up **Level A was applied 2026-07-05** under `Governance/SRT_EDIT_PROTOCOL.md` plus the L0 freeze high-risk cross-check (author-authorized); **Level B remains proposed, not applied** — the realist stance wording and its rewrite stay a separate future decision.

---

## Standing Rule

If a domain file uses one of these tensions, it should mark the claim level:

- use **P2** for current canonical interpretation;
- use **P3** for bridge mapping;
- use **P4** for operational or threshold hypotheses;
- avoid P0/P1 unless the tension has been separately closed in core/canonical files.

---

## 10. Closure / Compatibility Hardening Note (2026-04-21)

A hardened working position has now been written into:

- `Core/SRT_Closure_Compatibility_Hardening.md`

This note fixes the following distinctions at L1 hardening level:

1. primitive asymmetry vs historical asymmetry;
2. event trace vs historical asymmetry;
3. repetition as common path, closure as essence, and `κ`-threshold crossing as criterion;
4. minimal closure vs L2-grade closure;
5. operational compatibility vs `ε`-constrained deep compatibility;
6. normatively neutral closure vs pathological closure vs lethal `L_2`.

**Important status note**:
These results should be treated as hardened working conclusions, not yet as automatically promoted P0/P1 canonical primitives. The remaining open pressure point is not the distinction itself, but the quantitative and threshold layer:

- exact `κ` thresholding;
- bridge relation between `κ`, `\rho(p,t)`, and payability windows;
- domain-specific operationalization of compatibility and future-choice compression.

---

## 11. Order-Gain Criterion: three → four (RESOLVED 2026-07-05, option 3)

> **Resolution (2026-07-05, author decision)**: adopted **option 3** — order-gain (`秩序增益`) expands from three criteria to **four**: 可延续 / 可协调 / **不外包** / 可再选择. The new criterion 不外包 (consequence-return-channel integrity) is now a distinct load-bearing pillar, sourced in `Core_Law/SRT_Core_Text_CN.md`'s ε+F+M+U minimal closure as "ε on the consequence-return axis" (the second face of F: consequences displaced to other positions, parallel to F's time-face carrying 可延续). Landed across the theory layer: `Core_Law/SRT_Selection_Argument.md §7b.2` (canonical source), `Core_Law/SRT_Core_Text_CN.md`, `_SRT_D_VALUE_CANONICAL.md §5b.1a` (aligned with the `C_i` consequence-return factor), `Core_Law/SRT_L0_Metaphysics.md` 秩序增益词条, `Core_Law/SRT_Constitution_Seven_Theses.md`, `Philosophy/SRT_Ethics_Agency.md`, `Core/SRT_Core_22_Equations.md` Eq-Evo-03c, `Core/Dynamics_Scaling_Annex/13`, both glossaries, and the two bridges. The analysis below is retained as the adjudication record.

### Current State

`Core_Law/SRT_Selection_Argument.md §7b` fixes the order-gain (`秩序增益`) test as three criteria: **可延续 / 可协调 / 可再选择** (sustainable / coordinable / re-selectable), presented as the operational projection of 初心 ("能维持更多存在持续存在的动态平衡").

### Problem Point

A whole-book vocabulary reconciliation (`03_Bridges/SRT_Book_Vocabulary_Theory_Sync_Bridge_2026-07-05.md`) found that the book's crystallized direction test (`附录_术语表` Q22 方向三问; Q26 §3) uses a **different middle criterion**: **自耗 / 外包 / 锁死** (self-consumption / outsourcing / lock-in). The outer axes align (自耗↔¬可延续, 锁死↔¬可再选择), but the middle axis does not coincide:

- theory 可协调 = whether difference can be organized into coexistence;
- book 外包 = whether consequence falls on positions with no feedback channel.

These can come apart: a system can coordinate difference well yet still outsource cost to voiceless positions (future generations, ecology, the unable-to-appeal); or return all consequences yet suppress difference. The book moved the second load-bearing pillar of "direction" toward **consequence-return-channel integrity** — consistent with the book's 后果回流 spine and with the `C_i` consequence-return factor in `_SRT_D_VALUE_CANONICAL.md §2b`. The theory canonical still reads it as **coordination of difference**. This is not a wording difference; it is a difference in the content of the criterion.

### Resolution (adopted 2026-07-05)

Three candidate resolutions were on the table:

1. **Two faces of one axis**: outsourcing is the operationalization of ¬可协调; add one sentence to `§7b` — low risk.
2. **Book is sharper; theory follows**: replace 可协调 with 不外包 — C-class edit, middle criterion swapped.
3. **【ADOPTED】 Two independent criteria; direction is four**: 可延续 / 可协调 / 不外包 / 可再选择.

**Author chose option 3.** Rationale: 可协调 (differences coexist) and 不外包 (consequences return to bearers) genuinely come apart, so each earns a distinct pillar; 不外包 unifies with the whole-book 后果回流 spine and the `C_i` factor. It fits the ε+F+M+U minimal closure cleanly — F ("no position sees all consequences") has two faces, consequences displaced in time (→可延续) and consequences displaced to other positions (→不外包), so adding 不外包 gives F its own criterion rather than bundling it into 可延续. The change is now landed (see the Resolution note at the top of this section for the full file list). What remains open is only the empirical/threshold layer shared with §4 (operational tests for when a consequence counts as genuinely "outsourced to a no-feedback position" vs. legitimately borne elsewhere).
