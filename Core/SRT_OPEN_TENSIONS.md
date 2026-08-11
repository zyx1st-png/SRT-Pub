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
| selection irreducibility / competitor-vocabulary deletion (§13) | Claim Ladder: `selection` is a P0 primitive axiom (P0-01); GOV-SUB01 §8.1 defines the (not-yet-run) deletion test | whether asymmetric constraint + reachable-set change + irreversible writeback + payability + bearer-specific consequence return can replace the `selection` primitive with no lost difference | GOV-SUB01 residue status **unassigned** (no deletion test run); must not be presented as a proven-irreducible ontological ultimate; representational substitutability under broad refit ≠ role absence |
| `P0-02` existence index vs `H(L_0)=∞` (§15) | P0-02's *claim* (existence = degree of stable anchoring out of open possibility) is unaffected | a well-defined quantity: with `H(L_0)=∞` declared in `Core/SRT_Core_01_Axioms.md`, `E = 1 - H(L_1)/H(L_0)` is identically 1 and `ΔS = H(L_0)-H(L_1)` identically ∞ | do not cite `E` or that `ΔS` as a quantitative readout; **no normalization has been adopted** — Decision Gate A is open, no file may pick one unilaterally |
| layer assignment of 初心 (§16) | L0 anchor is explicit and repeated: 初心 is L1, L0 commits only to `ε`, §七.11 rejects pre-set goals in L₀ | whether a thin L₀ formal precursor is admissible at all | a freeze-Group-A canonical anchor currently imports an L₀-level reading from a `canonical: false` translation file; **Decision Gate B open** — do not resolve by editing either side |
| "global optimum" four senses (§17) | Level A de-overload applied 2026-07-05 to d-value §5b.1 | one term for four objects (universe-wide / operator-relative reachable / regulative ideal / finite-constraint attractor); §5b.2 never narrowed; `Ψ_f→0` reads as degenerate in Core and as optimum in Spirituality | **Decision Gate C open**; the 2026-08-11 pass changed no §5b.2 wording and no Spirituality framing |

These are pressure points, not new axioms. They route later work and block overclaiming. §15-§17 additionally carry **author-decision gates**: they are registered here so that no downstream file resolves them by drafting, and the options live in `Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md`.

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

### Status Update (2026-08-11) — partially resolved, ledger was stale

The first question above ("is `T_dir` a scalar, a relation, or an accessibility function?") **has in fact been answered at v0 level**, and this section had not recorded it:

- `_SRT_T_DIR_CANONICAL.md` Def-T-1 / §3.1 fixes `T_dir` as a **scalar-valued readability × reorientation functional**, `T_{dir}^{v0} := \mathcal{R}_{self}(\operatorname{Dir}(\Delta\hat{G}_\theta,t)) \cdot \mathcal{A}_{reorient}(\operatorname{Dir}(\Delta\hat{G}_\theta,t))`, explicitly labelled **v0 operational proxy**, not a completed ontological foundation.
- `Core_Law/SRT_L1_Formalism.md §3.5` (2026-04-25) promotes `T_dir` from algebraic proxy to an **independent dynamical variable** with a five-term ODE (relaxation / real-reselection pump / `\Delta\Psi_f^{gap}` deduction / `S_{str}` erosion / `s_{ext}` scaffolding), with `T_dir ∈ [0,1]` carried as a **governance-canonical** range.

So the form question is **partially resolved**: scalar-valued functional with a v0 dynamical law. What remains open and keeps this tension live:

1. **Sufficiency conditions** — the admission condition in §3 above is still a necessary gate, not a sufficiency theorem. Unchanged.
2. **Projection form** — `SRT_L1_Formalism.md §3.5.1` leaves the `[0,1]` projection operator `\Pi_{[0,1]}` (hard cutoff vs smooth sigmoid reparameterization) explicitly open.
3. **Semantic closure** — `\mathcal{R}_{self}` and `\mathcal{A}_{reorient}` are named roles, not independently specified objects; the four-way separation (minimal internal access / phenomenological meaning / behavioral reorientation / value-hiddenness) is still not formally cut.
4. **Operator-level hardening** — `SRT_L1_Formalism.md §7.8` still lists this as pending; the lethal-`L_2` criterion built on the ODE stays P1-candidate.

Citation rule unchanged: `_SRT_SYMBOL_TABLE.md` Usage Rule 8 still governs — `T_dir` is a v0 operational proxy and must not be cited as a completed formal object. The change here is only that "no formal object exists yet" is no longer an accurate description of the repo state.

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

### Source-Intuition Testimony (non-resolving, added 2026-07-10)

Two source-intuition choice-traces register direct intuitive testimony on this exposure point. Testimony is not derivation; it does not move P0-04 toward resolution. It is logged here only so the exposure point's intuitive-pressure record does not stay empty.

- `01_Source_Intuition/SRT_FIRST_INTUITION_SELECTION_BEFORE_EXISTENCE_CHOICE_TRACE_2026-07-09.md` P2: "selection is prior to the subject; the subject is only a later-stage form the selection structure develops into." This restates the P0-04 exposure rather than closing it — it says the chooser is downstream, not where the first selecting capacity itself comes from.
- `01_Source_Intuition/SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md` P2-01: "selection as the minimal non-neutral maintenance of a lucky openness" (the author's own words: "选择是对于幸运产生的最小非中立的维持"). "Lucky" is an intuitive name for the non-selective ground P0-04 asks about; it does not derive selectability from it.

Neither testimony should be read as narrowing the three-way guardrail above (derived process / stable pattern / assumed interface); both remain compatible with all three and do not by themselves pick one.

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

### Open Tension (2026-07-12, cross-scale generative-emergence writeback)

The 2026-07-12 book writeback round (`Operations/SRT_CROSS_SCALE_GENERATIVE_EMERGENCE_WRITEBACK_PLAN_2026-07-12.md`, Phase-A audit `..._AUDIT_2026-07-12.md`, source trace `01_Source_Intuition/SRT_CROSS_SCALE_SELECTION_PROXY_TRACE_2026-07-12.md`) introduced three book-side exposition-candidate names: **协调性关闭 / coordinated closure**, **参与式退让 / participatory yielding**, **选择代理层 / selection proxy layer**. Their relation to existing theory objects is a **candidate mapping / to-be-verified relation, NOT an identity or alias** — and the mapping itself carries residual open tension:

- *coordinated closure* is **structurally adjacent to, but not equal to**, `Core_Law/SRT_Reference_Scaling.md` **Def-Scale-PCC-1 (Primordial Constraint Closure)**. PCC is defined in the origin-of-life register (sustainable metabolic flow, `P_in > P_diss + P_maint`, payability); it does **not** currently define "multiple units mutually constraining and closing local optionality so as to generate macro-scale degrees of freedom." That generative step is not yet formalized in canonical.
- *participatory yielding* is **adjacent to, but not equal to**, shared-`L_2`-field formation (`Core_Law/SRT_Collective_Selection.md` Def-C-1). Def-C-1 defines only that a path trace `ρ(p,t)` is visible to and affects multiple `P_i`; it does **not** define "each unit reduces its independent optionality" as the formation cost. That reduction step is a candidate, not a defined object.
- *selection proxy layer* is **adjacent to** `Collective_Selection.md` T-COLL-1「制度是集体 ISP 的器官非主体」 composed with `L_2` scaffold, but "a background that begins to handle a class of repeated selections for later units" is likewise not itself a defined canonical object.

Canonical verdict for this round is **H-A (no canonical amendment)** — but for the reason that the candidate relation is **not yet ripe for canonical**, NOT because it is already covered. These three names carry no new symbols, must not enter the symbol table, and must not be promoted to canonical until the mapping above is verified. **New open item registered**: whether the generative step (independent local optionality ↓ → coordinated closure → macro effective selectability ↑, with residual causality retained) can be given a domain-discriminating formalization that connects to PCC / Def-C-1 / T-COLL-1 without collapsing into any of them — this is distinct from, and upstream of, Failure Condition 4 above (which concerns whether the whole loop yields discriminating predictions).

---

## 9. ε Normativity Scope and the Closure-Boundary (fallibilist foundation)

### Current State

An adversarial stress-test of `ε` (the L0 directional postulate) and a build-and-attack construction on the closure-boundary atom are recorded in three non-canonical files: `_SRT_EPSILON_NORMATIVITY_OPEN_TENSION.md`, `90_Backstage/Incubation/_SRT_NORMATIVITY_FRAMING_TRUEUP_PROPOSAL.md`, and `_SRT_CLOSURE_BOUNDARY_CONVERGENCE_RECORD.md`.

Working position under review (non-canonical; tracked, not promoted):

- `ε` is securable as a **minimum condition (domain floor) + constitutive stance** of any selector: the shmagency-style counterexamples close because a selector either selects → minimally presupposes a concern-structure, or does not select → exits the domain. `ε` is therefore true of every in-domain selection but does not by itself make normative distinctions.
- The **normative distinction work** is carried by the **reorganizability criterion** (anti-occlusion / anti-lock-in / anti-externalization / re-selectable — "可重组、可承担、可恢复、可再选择"), which genuinely discriminates (foreclosing selections fail it).
- Self-regarding re-selectability is near-constitutive; the **other-regarding** part requires aggregating positionally-partitioned, scope-extended option-fields, and the whose-counts / what-scope weighting is the irreducible **closure-boundary atom** — which this foundation line and Direction 3 (`_SRT_DIRECTION3_L0_PROBE_RESEARCH_SEED.md §4`) independently converge on.

### Problem Point

Two distinct unresolved points:

1. **Framing overload.** Former canonical wording — "全部规范性力量锚定于 ε" (L0 §六 and 正骨架总结), "L0 偏向非自我抹除" as a realist L0 property, and "趋向全局自由能最小值" (d-value §5b.1) — overclaimed relative to the defensible base. **Status update (2026-07-05): Level A of the staged de-overload was applied** under author-authorized high-risk protocol (see `90_Backstage/Incubation/_SRT_NORMATIVITY_FRAMING_TRUEUP_PROPOSAL.md`): the "全部规范性" wording in L0 §六 and the 正骨架 label, and the "全局自由能最小值" sentence in d-value §5b.1, are now narrowed to "minimum condition (domain floor) + reorganizability criterion + open closure-boundary". The realist wording "L0 偏向非自我抹除" is untouched (Level B territory). Level B remains **proposed, not applied**.
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

### Landing-scope correction (2026-08-11)

The 2026-07-05 landing list above was a **theory-layer** list. Two surfaces were outside it and kept the superseded three-criteria reading for 13 months' worth of reads:

1. **`Core_Law/SRT_Core_Text_EN.md` (English mirror of the CN core text).** Step ⑩ still enumerated three criteria *and* carried its own minimality claim — "the three together form the minimal cover, irreducible" — in direct mutual exclusion with the CN side's 「四者合取构成最小覆盖，不可再省」. This file has **no frontmatter and appears in no registry, index, or freeze list**, so nothing bound it to the CN source; that absence is the mechanism, not an oversight by any single pass. **Synced 2026-08-11**, with a mirror-status header naming CN as governing and `SRT_Selection_Argument.md §7b.2` as the adjudicating source for this criteria set.
2. **Book drafts `Q22_方向.md` / `Q23_共同体.md`.** The book not only kept three questions, it **bound the canonical term 可协调 to mean 不外包** — Q22 wrote 「可协调（不外包）」 and headed its second question 「有没有外包？（可协调性）」; Q23 §4 labelled its return-channel question 「共同可协调」 and glossed 「查协调通道」. That identification is exactly what `SRT_Selection_Argument.md §7b.2` explicitly forbids (「②可协调与③不外包不同一，也不可互相替代」). **Corrected 2026-08-11**: the book keeps its three-question compressed diagnostic interface (自耗／外包／锁死), but the interface is now explicitly marked as *not* the theory-layer criteria set, with the mapping registered in `Q22` 章末注八 (自耗→可延续, 外包→不外包, 锁死→可再选择, 可协调 held as a separate criterion that surfaces at the multi-position scale in Q23).

`03_Bridges/SRT_Book_Vocabulary_Theory_Sync_Bridge_2026-07-05.md §5` had listed 「分歧悬空死法」 (book and canonical drifting apart if the mid-axis were never adjudicated) as the failure mode this bridge most needed to prevent. The drift did occur — but in a form that file did not anticipate: **not un-adjudicated, but adjudicated and landed on one side only**. That failure shape is now the target of the anti-drift rule proposed in `Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md §5`.

---

## 12. Entropy as a De-Selection Reading (open, registered 2026-07-10)

### Current State

`Core/SRT_Core_25_Thermodynamic_Signatures_of_Selection.md` treats thermodynamic irreversibility and entropy production as an **empirical signature** of selection: `H_P` (production entropy) is a possible readout of selection asymmetry, not identical to `\Psi_f`. This is a bridge-level, measurement-facing reading — entropy production is evidence *that* a selection-like asymmetry occurred.

### Problem Point

A source-intuition choice-trace (`01_Source_Intuition/SRT_FIRST_INTUITION_SELECTION_BEFORE_EXISTENCE_CHOICE_TRACE_2026-07-09.md`, P13) proposes a different-altitude reading: entropy is not a signature *of* selection but a **statistical portrait of what remains after selection, boundary-maintenance, and scaffolding are abstracted away** — "熵是对'将世界的选择剔除后'的运转规律总结" (CT-20260709-20/21). This is not a restatement of the Core_25 bridge; it is a claim about where entropy sits relative to selection *in principle* (de-selection reading), not merely how entropy can be measured.

The trace's own follow-up question (CT-21) is unresolved and must travel with the tension: is this an **ontological absence** claim (selection is genuinely not present in what entropy tracks) or a **theoretical abstraction** claim (statistical mechanics, as a modeling choice, abstracts selection out even though it is present)? These have different physical commitments — the first risks colliding with standard statistical mechanics; the second does not. The trace does not adjudicate between them.

A companion trace (`01_Source_Intuition/SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md`, P2-14) independently proposes the dual/complementary formulation: "selection is a generative resynchronization of randomness" (a construction reading, additive) against P13's "entropy is the de-selection portrait" (a subtraction reading). The two are registered together because they describe the same boundary from opposite directions and should not be hardened as two separate concepts.

### Minimal Guardrail

> **Level**: source-intuition pressure, not a resolved theorem.

- Do not cite P13 or P2-14 as showing SRT is an anti-entropy or entropy-reversing theory.
- Do not treat P13 as superseding or correcting `Core/SRT_Core_25`'s measurement-facing reading — the two operate at different altitudes (ontological positioning vs. empirical projection) until a bridge explicitly reconciles them.
- Do not present the ontological-absence / theoretical-abstraction distinction as resolved in either direction.
- If hardened into a bridge, the bridge must state which of the two readings (or a scoped combination) it adopts, and must cross-check against `Core_Law/SRT_L0_Metaphysics.md`'s existing randomness argument ("pure randomness would not produce stable structure; a constrained determinization process is what SRT calls selection") to avoid introducing an uncredited new primitive.

---

## 13. Selection Irreducibility / Competitor-Vocabulary Deletion Test (open, registered 2026-07-16, GOV-SUB01 Pass 1)

### Current State

- `Core/SRT_Core_21_Minimal_Axioms.md P0-01` fixes selection as primitive: existence is the image of selection (`∃x ⟺ x ∈ Range(Ĝ)`). `P0-04` separately exposes the origin of selectability as open (see §7 above).
- `Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md §8.1` defines the subtractive test for this primitive: remove the word and primitive role of `selection`, retaining only asymmetric constraint, reachable-set restriction, history dependence, cost, and consequence return.
- Two registers must be kept separate, and neither may borrow the other's authority:
  - **Claim Ladder register**: `selection` is currently a **P0 primitive axiom** (`P0-01`). That is its epistemic-rank registration and is unchanged by this pass.
  - **GOV-SUB01 residue register**: **unassigned.** No actual deletion test (`M^{-selection}`) has been executed, so no residue label (`R2` / `R4` / `N1` / `N2`) may be attached. A residue label is earned only by running the K=0 / limited-K / broad-K tests below — it is never asserted in advance.

### Problem Point

The unresolved question (GOV-SUB01 §8.1 required form):

> Using only asymmetric constraint, reachable-set change, irreversible writeback, payability, and bearer-specific consequence return — and deleting the `selection` primitive — what explanatory, counterfactual, experimental, or interventional difference does SRT actually lose?

Until this produces a concrete difference the competitor vocabulary cannot reconstruct, `selection` must **not** be presented as a **proven-irreducible ontological ultimate**. Its `P0` axiom status records that SRT *treats* selection as primitive; it does not certify that no competitor vocabulary could reconstruct selection's role. Asserting that it cannot is exactly the overreach GOV-SUB01 §0 and §10 warn against ("survives removal testing ≠ primitive ≠ ontologically fundamental") — and, symmetrically, attaching a residue label (`N1`/`N2`/`R*`) before the deletion test is run is the same error in reverse.

Two guardrails on how the test may be run:

1. **Refit-budget relativity (GOV-SUB01 §3, §7.4).** A `broad K` replacement that reconstructs SRT behavior in non-selection vocabulary shows *representational substitutability*, not *absence of the underlying role*. Do not count a variable as removed when its function was merely moved into initialization, a loss term, a prior, preprocessing, or a renamed construct.
2. **Distinctness from §7.** §7 (P0-04) asks where selectability *comes from*; this tension asks whether the selection *primitive can be dissolved* into non-selection vocabulary without loss. These are distinct exposures and must not be conflated or cited as one closing the other.

### Future Hardening Direction

A future deletion pass may attach a residue label to `selection` only if it exhibits at least one of the following against the reduced vocabulary (GOV-SUB01 §4 evaluation vector):

1. a counterfactual SRT discriminates that the reduced vocabulary cannot (`E_cf`);
2. an intervention whose predicted effect differs under a selection framing vs. a pure asymmetric-constraint framing (`E_int`);
3. an experiment where a real choice moment (`Core/SRT_Core_21b_Constitutive_Theorems.md P1-T05`) and script execution / gradient following diverge in a way the reduced vocabulary cannot label;
4. a phenomenological or normative distinction (`E_phen` / `E_norm`) — bearer-specific consequence return, directional self-readability — the reduced vocabulary demonstrably fails to carry.

Absent such a result, domain, book, and public files must **not** present `selection` as "proven irreducible." They may cite its current **P0 primitive-axiom** status (per `Governance/SRT_CLAIM_LADDER.md`) but must not attach any GOV-SUB01 residue label to it. This tension introduces no new symbol and does not change `P0-01` or `P0-04`. Any residue classification, if reached, comes only from an executed deletion test — never asserted in advance and never read off the axiom status.

---

## 14. Selection-Event Threshold Operationalization (open, registered 2026-08-06)

### Current State

- `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T05` fixes **real choice moment** as a live `L_0 -> L_1` anchoring event whose result genuinely constrains the future selection space, and lists what does *not* qualify (script execution, habit replay, gradient following, `L_2` label optimization).
- `03_Bridges/SRT_Choice_Generation_Conditions_2026-08-04.md` (T-D, P2-P3) supplies the positive side P1-T05 does not carry: five functional conditions — difference manifestation (`CG-0`), non-equivalent registration (`CG-1`), path efficacy (`CG-2`), consequence bearing (`CG-3`), historical efficacy (`CG-4`) — plus a three-tier threshold structure (candidate formation / process unfolding / event standing).
- `Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md` grades each condition (`DMF` 0-3, `NER` 0-4, `PEF` 0-4, `CBP` 0-4, `HEF` 0-4) and sets audit-default minima `DMF-2 / NER-2 / PEF-2 / CBP-2 / HEF-3` under a non-compensation rule.
- Compact discrimination layer: `03_Bridges/SRT_Selection_Event_CompactCore.md`.

### Problem Point

The bridge's own conclusion states that "effective strength at the relevant scale" still requires domain operationalization, and the protocol states that its minima are **audit defaults, not a cross-domain necessary-and-sufficient theorem**. Three exposures follow:

1. **Threshold status.** `DMF-2 / NER-2 / PEF-2 / CBP-2 / HEF-3` have no derivation from P0/P1 and no cross-domain calibration. They are currently conventions that make audits comparable, not established thresholds. They must not be cited as SRT-derived criteria.
2. **Discriminating gain unproven.** Degradation trigger 1 of the bridge is that ordinary causal transition, constraint, and path dependence may already explain every case the `CG` conditions explain. No executed test yet shows a case where the `CG` reading yields a counterfactual or interventional difference that the reduced vocabulary cannot produce. This exposure is the same shape as, but distinct from, §13: §13 asks whether the `selection` primitive dissolves into competitor vocabulary; §14 asks whether the five-gate *event criterion* adds discriminating power over plain causal description.
3. **Relation to P1-T05 unformalized.** Whether the five gates are necessary conditions for a real choice moment, sufficient conditions, or merely a correlated audit surface is not established. The bridge explicitly declines to reduce P1-T05 to the five conditions.

### Future Hardening Direction

Progress would be at least one of:

1. a case where a `CG`-based verdict and a plain causal-transition verdict **diverge**, with the divergence confirmed by intervention rather than by relabeling;
2. a domain-specific derivation or calibration of one minimum threshold from independently motivated constraints, replacing the audit-default convention;
3. a formal statement of the P1-T05 ↔ `CG-0..CG-4` relation (necessary / sufficient / neither), with the failure conditions of that statement made explicit;
4. an executed negative control in which a system passing all five gates is independently judged not to have made a selection, forcing a threshold or condition revision.

Until then, `CG-0..CG-4`, the graded ladders, and the minima remain **P2-P3 audit apparatus**. They may not be presented as canonical criteria for selection, subjecthood, consciousness, freedom, `L_2`, or generative health, and passing all five gates licenses only the phrase "bounded selection-event candidate." This tension introduces no new symbol and does not change P1-T05.

---

## 15. `P0-02` Existence Index vs. `H(L_0) = ∞` (open, registered 2026-08-11)

### Current State

- `Core/SRT_Core_21_Minimal_Axioms.md` **P0-02** (primitive axiom, freeze Group A) gives existence-as-anchoring the compact form `E = 1 - H(L_1)/H(L_0)`.
- `Core/SRT_Core_01_Axioms.md` (and its split `Core/Axioms_Split/01_Part02.md`) states, in the finiteness argument against total operator coverage, `H(\theta) \geq H(L_0) = \infty`.
- `Core/Dynamics_Scaling_Split/01_Master_Equation_and_ScaleCoupling.md` uses `\Delta S = H(L_0) - H(L_1)` as the entropy-reduction basis of the cross-scale isomorphism argument.

### Problem Point

Taken together at face value these are jointly degenerate, not merely underspecified. With `H(L_0) = \infty` and `H(L_1)` finite, `E \equiv 1` for **every** anchored slice and `\Delta S \equiv \infty` for **every** selection: both quantities lose all discriminating power, and `E` cannot do the work P0-02 assigns it (degree of stable anchoring out of open possibility).

No normalization convention, accessible-horizon restriction, or measure-theoretic guard exists anywhere in the corpus; `H(L_0)` is not a registered row in `_SRT_SYMBOL_TABLE.md`. The formula is still in live circulation as `[P0]` (e.g. `01_Source_Intuition/Conversations/2026-07-27_SRT_Minimal_Setup_Note_EN.md`).

This is distinct from the general "L₀ is structured potentiality, not a set" caution: the issue is that a P0 axiom carries an expression whose only stated inputs are declared infinite elsewhere in Core.

### Status

**Author decision required — not adjudicated here.** Candidate resolutions (finite accessible-domain relativization / entropy-reduction reformulation / demotion of the expression to heuristic) with their respective costs are laid out in `Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md` **Decision Gate A**. No option has been adopted, and this tension does **not** license any file to pick one unilaterally. Until a gate verdict lands, cite P0-02's *claim* (existence = degree of stable anchoring) rather than its *formula*, and do not use `E` or `\Delta S = H(L_0) - H(L_1)` as a quantitative readout.

---

## 16. Layer Assignment of 初心 / "Original Intention" (open, registered 2026-08-11)

### Current State

- `Core_Law/SRT_L0_Metaphysics.md` is explicit and repeated: 「初心」is an **L1 concept**, outside L0's term-adjudication scope; L0 commits only to `ε`; §七.11 (潜在域预置论) rejects reading `ε` as a pre-set a priori goal in L₀.
- `_SRT_D_VALUE_CANONICAL.md §5b.2` Cross-ref (theory-canonical anchor, freeze Group A) nonetheless cites `Physics/SRT_Phys_08_Ontology_Ext.md` **Def-Apeiron-1** under the gloss 「初心作为 L₀ 的倾向性结构」.
- `Physics/SRT_Phys_08_Ontology_Ext.md` Def-Apeiron-1 (`claim_mode: translation`, `canonical: false`) states 初心 = `\arg\min_{\text{direction}} \int_0^\infty F[\sigma(t)]dt` and calls it 「$L_0$ 的内在属性」.
- `Spirituality/SRT_Spirit_05_Shoshin.md` Ax-Sho-1 (`claim_mode: mixed`) defines 初心 as the negative gradient of a long-horizon free-energy functional.

### Problem Point

The defect is **not** that a translation-layer file carries a strong reading — that is what a translation layer is for, and its `canonical: false` marking already scopes it. The defect is the **direction of citation**: a freeze-Group-A canonical anchor imports the L₀-level reading, with approving gloss, from a `canonical: false` translation file — precisely the reading the other freeze-Group-A anchor forbids. That is a claim-level inversion inside the canonical layer, and it makes the L₀/L₁ boundary on 初心 unreadable from the canonical files alone.

A related but separate item, **not** treated here: `Core_Law/SRT_L0_Metaphysics.md` 第一命题 itself contains 「选择内在地趋向秩序」 with a 2026-04-11 层级精确化注 declaring **both** readings valid at different layers. That is an explicitly declared dual reading, not an unrepaired residue, and it is left untouched pending the same gate.

### Status

**Author decision required — not adjudicated here.** Two framed options (strict layering vs. a thin L₀ formal precursor), with an analysis of whether the second reopens 潜在域预置论, are in `Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md` **Decision Gate B**, together with the full provenance map of every file that gives 初心 an L₀ reading. No canonical stance was changed in the 2026-08-11 consistency pass.

---

## 17. "Global Optimum" — Four Senses Running Under One Name (open, registered 2026-08-11)

### Current State

The 2026-07-05 Level A normativity de-overload (§9 above) narrowed the 「趋向全局自由能最小值」 sentence in `_SRT_D_VALUE_CANONICAL.md §5b.1`. The rationale recorded in `90_Backstage/Incubation/_SRT_NORMATIVITY_FRAMING_TRUEUP_PROPOSAL.md` was that 「"全局最优"的位置无关性正是闭包边界原初所否定的」.

### Problem Point

The narrowing was applied to §5b.1 only. The **adjacent subsection in the same canonical file**, §5b.2「全局最优是动态平衡，不是热寂」, was left untouched and still positively characterizes 全局自由能最小值 as a landscape configuration — i.e. it is the subsection that actually carries the position-independent global-optimum ontology the de-overload's own rationale rejects.

Downstream landing was likewise partial: `Core/SRT_Core_NormativeGradient.md` did receive the guard (its strong reading is marked as dependent on the open closure-boundary); `Spirituality/SRT_Spirit_04_Synthesis.md` (善 = 全局自由能最小) and `Spirituality/SRT_Spirit_05_Shoshin.md` Ax-Sho-1 did not.

Underneath the wording sits a genuine ambiguity: at least four different objects currently share the name — universe-wide global optimum, operator-relative reachable optimum, regulative ideal, and local/dynamic attractor under finite constraints. `Spirit_04` itself already carries an Ω three-reading table that separates some of these, which is evidence the ambiguity is real rather than imagined.

### Related: `\Psi_f \to 0` valence inversion

The same cluster carries a second inconsistency. Core treats the `\Psi_f \to 0` limit as **degenerate**: `Core/SRT_Core_12a_Ontology_L0L1.md` states frictionless selection is 「在结构上被禁止」; `Core/SRT_Core_22_Equations.md` states 「最优区间不是 `Ψ_f→0`……零摩擦对应无真实赌注」; `Core/SRT_Core_12b_Ontology_L2.md` Def-L2-Algo uses that very limit to define the algorithm as an extreme `L_2` state with no historical embodiment. Spirituality treats the same limit as the **normative optimum** (`SRT_Spirit_01_Religion_Ontology.md` `\hat{G}_\infty = (d \to d_{max}) \wedge (\Psi_f \to 0)` as 纯觉知, 「功能同一（操作化）」; `SRT_Spirit_04_Synthesis.md` 完美态; `SRT_Spirit_09_Praxis.md` Phase 7-10). `Spirit_04` registers this locally as `IC-AllGood-1` and proposes a reading (per-manifestation cost → 0, not "no manifestation needed"), but that repair propagated to neither the other Spirituality files nor Core.

### Status

**Author decision required — not adjudicated here.** A four-sense terminology separation and a recommended (but not adopted) reformulation of the Spirituality limit as **excess friction** `\Psi_f - \Psi_f^{min} \to 0` are in `Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md` **Decision Gate C**. The 2026-08-11 pass changed no Spirituality framing and no §5b.2 wording.
