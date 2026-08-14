---
patch_id: PATCH-PHIL-PH-QUAL01-RESELECTIVE-QUALIA-GEOMETRY
origin: internal_theory_development
domain: philosophy_of_mind_consciousness_qualia
claim_level: P3-P4_bridge_hardening
canonical_status: non_canonical
status: active
target_documents:
  - Philosophy/Foundations_Annex/06_Qualia_Interface_Batch.md
  - Philosophy/SRT_HardProblem_Epistemology.md
  - Philosophy/SRT_Subjecthood_Threshold_Interface.md
  - Core/SRT_OPEN_TENSIONS.md
related_claims:
  - qualia_broad
  - relational_qualia_geometry
  - phenomenal_character
  - phenomenal_necessity
  - perspective_center_individuation
  - future_selectability
  - reselectability
  - bearer
  - consequence_return
  - concern_domain
  - d_value
  - T_dir
  - Psi_f_actual_felt
  - valence
  - pathological_foreclosure
tags:
  - qualia
  - consciousness
  - phenomenality
  - reselectability
  - quality_space
  - bearer
  - future_selectability
  - valence
  - d_value
  - T_dir
layer: operations
epistemic_layer: bridge
claim_mode: hardening
canonical: false
type: theory_hardening_patch
id: PATCH-PHIL-PH-QUAL01-RESELECTIVE-QUALIA-GEOMETRY
created: 2026-08-14
revised: 2026-08-14
---

# SRT Philosophy Patch PH-QUAL01: Reselective Qualia Geometry v0.2

> **Status**: P3/P4 philosophy-of-mind bridge hardening patch.
>
> **Canonical caution**: this file does **not** define qualia, consciousness, `d`, `T_dir`, `Psi_f`, bearer, subjecthood, or reselectability canonically. It does not claim that reselectability proves phenomenal presence. It does not close `PH-CONSC04`'s phenomenal-necessity / SRT-zombie pressure point. Its narrower task is to test whether SRT's existing account of **qualitative character** can be strengthened by adding a forward-facing, bearer-indexed constraint: how an event immediately rewrites the conditional structure of what the same bearer can select next.
>
> **Numbering note**: this is `PH-QUAL01`; no prior `PH-QUAL01` patch exists in the repository. The earlier draft was provisionally named `PH-QUAL02` and is superseded by this revision.

---

## 0. Why this patch exists

SRT already has several relevant pieces. This patch does not restart the qualia problem from zero.

### 0.1 Existing quality-space bridge

`Philosophy/Foundations_Annex/06_Qualia_Interface_Batch.md` places broad qualia mainly at `L1` and introduces the relational structure:

```text
Q_L1 = (E, Delta_ij)
```

where `Delta_ij` is experienced dissimilarity between experience items. The methodological point is that a consciousness theory should constrain phenomenal neighborhoods, clustering and deformation rather than only classify isolated experience labels.

### 0.2 Existing subjectivity decomposition

`PH-CONSC03` requires:

```text
Selector != Bearer != Concern Domain != Experiencer
```

and proposes, at bridge level, that structural bearing involves same-bearer consequence return, history-bearing writeback and non-trivial change in that bearer's future-selectability structure.

### 0.3 Existing hard-problem split

`PH-CONSC04` already distinguishes:

```text
HP-A = perspective-center individuation
HP-B = phenomenal necessity
```

Current SRT has substantial resources for HP-A, while HP-B remains open. In particular:

```text
structural bearing != phenomenal bearing proved
```

and a fully structurally specified `Z6` SRT-zombie remains a live pressure case.

### 0.4 Existing qualitative-character answer

`Philosophy/SRT_HardProblem_Epistemology.md §3.3` already gives a three-factor structural anchor for why one quale is this rather than another:

```text
qualitative character
~ f(L0 curvature direction x theta x L2_current)
```

This is an existing answer to qualitative specificity. It should not be overwritten or redescribed as absent.

### 0.5 The remaining opportunity

Those three factors are primarily **retrospective / current-state constraints**:

```text
what L0 direction is accessed
+ how theta filters it
+ how current historical anchoring receives it
```

The reselectability line adds a distinct **forward-facing question**:

> After the event is anchored at this bearer-position, how does that very event immediately rewrite the conditional structure of what this bearer can still attend to, approach, avoid, remember, reopen, compare or select next?

The candidate contribution is therefore not:

```text
reselectability -> consciousness
```

and not:

```text
reselectability replaces the existing three-factor qualia account
```

but:

> **Reselective deformation is a candidate fourth interface that links the existing qualitative-character anchor to the bearer's changed future accessibility.**

---

## 1. Hard-problem namespace: preserve HP-A / HP-B and add HP-C

This patch adopts the namespace already established by `PH-CONSC04`.

### HP-A — perspective-center individuation

Question:

> How does a persistent, history-bearing, consequence-bearing perspective center become individuated?

This includes much of the structural burden behind ownership / `for-me` attribution.

### HP-B — phenomenal necessity

Question:

> Why could a fully individuated, stake-bearing, history-bearing perspective center not be phenomenally empty?

This remains open.

### HP-C — qualitative character

New label introduced by this patch for an already partially treated burden:

> Given phenomenal presence, why does an event have this qualitative organization rather than another, with this phenomenal neighborhood, intensity profile and temporal organization?

`HP-C` does **not** mean SRT previously lacked a qualitative-character account. `SRT_HardProblem_Epistemology §3.3` already supplies the three-factor anchor. `PH-QUAL01` asks whether that account gains discriminating content when linked to immediate future-selectability rewrite.

Guardrails:

```text
HP-A != HP-B != HP-C
```

```text
for-me-ness / ownership work in §5
= extension of HP-A
not a new proof of HP-B
```

```text
reselective qualia geometry
!= proof of phenomenal necessity
```

---

## 2. Existing three-factor anchor plus a forward-facing fourth interface

Let the existing qualitative-character anchor be compressed as:

```text
A_q(t)
= current structural anchoring of q
~ (L0-access direction, theta, L2_current)
```

`A_q(t)` is only expository shorthand in this patch, not a new repository symbol.

The new question is what the event does **at the moment it is incorporated into the bearer**.

### 2.1 `Omega_B` lineage and scope

`PH-CONSC03` and `PH-CONSC04` already use indexed `Omega_B(t)` as bridge-level notation for the future choice/action/state structure reachable by candidate bearer `B`.

This patch inherits that notation rather than redeclaring a new object. It does **not** use bare `Omega`, and it does not request symbol-table promotion.

### 2.2 Avoiding retrospective determination

The earlier draft used:

```text
Omega_B(t) -> Omega_B(t + dt)
```

which can be misread as making what `q_t` felt like depend on what actually happens later. That reading is rejected here.

Use an event-local transition instead:

```text
Omega_B(t^-)
-> [event q_t is borne / incorporated]
-> Omega_B(t^+)
```

where:

- `t^-` means the conditional reachable structure immediately before the event update;
- `t^+` means the conditional reachable structure immediately after the event update;
- neither term denotes the later realized path;
- later behavior does not retroactively constitute the original phenomenal event.

The relevant object is therefore an **immediate state-conditioned rewrite of counterfactual accessibility**, not hindsight about what the bearer eventually chose.

### 2.3 Test-local reselective deformation profile

To avoid crowding the `D_*` namespace used by `D_eff` and related quantities, this revision replaces the earlier `D^B_q` mnemonic with:

```text
RDef_B(q_t): Omega_B(t^-) -> Omega_B(t^+)
```

`RDef_B(q_t)` is plain test-local notation for a **reselective deformation profile**. It is not canonical, not a scalar, and not related by definition to `D_eff`.

Candidate profile dimensions may include independently operationalized changes in:

- candidate admission / exclusion;
- attentional priority;
- action affordance accessibility;
- memory encoding / retrieval weighting;
- counterfactual evaluation;
- approach / avoidance policy availability;
- recoverability / reopening;
- concern weighting;
- self-reorientation availability.

The list is a measurement menu, not permission to fit an arbitrary post-hoc distance.

### 2.4 Fourth-interface proposal

The safe bridge is:

```text
existing qualitative anchoring A_q(t)
+ immediate bearer-indexed RDef_B(q_t)
-> candidate richer constraint on HP-C
```

More explicitly:

> **The existing three-factor anchor constrains what kind of experience is instantiated at the current bearer-position; the reselective interface asks whether the same event's immediate rewrite of future accessibility supplies additional, forward-facing structure that helps explain and predict phenomenal relations.**

This is an extension, not a replacement.

---

## 3. Temporal thickness without retrocausality

A lived event can still be temporally thick without being determined from the future.

Safe sequence:

```text
past history / L2_current
-> present anchoring and bearing
-> immediate counterfactual-accessibility rewrite
-> later memory / re-objectification
```

`PH-MEM01` supports a compatible memory-side bridge: retained history can alter the conditions under which later objects, judgments and alternatives become accessible. `NEURAL25` similarly treats memory as historical selection bias at a neuroscience bridge level.

Therefore later history may change:

```text
how q_t is remembered
how q_t is categorized
which aspects of q_t become reportable
how q_t is re-objectified at t+n
```

without licensing:

```text
later history retroactively changes what q_t originally was like at t
```

This distinction should be preserved in any future reconsolidation / trauma / memory work.

---

## 4. Reselective Qualia Structure Hypothesis

### Claim PH-QUAL01-A — bounded similarity bridge

For a bearer already admitted as a serious phenomenal candidate, and **within a declared regime where actual consequence structure is not strongly masked from the bearer**, experienced dissimilarity may show incremental covariance with independently estimated similarity of immediate reselective deformation profiles.

Reuse the annex notation:

```text
Delta_ij
~
Dist(RDef_B(q_i), RDef_B(q_j))
```

where:

- `Delta_ij` is the same experienced-dissimilarity relation already used by `Def-Phil-Qualia-3`;
- `Dist` must be declared **before** confirmatory testing from a bounded metric/model family;
- `RDef_B` must be estimated independently of `Delta_ij` rather than reverse-engineered from subjective similarity;
- sensory-feature distance, task structure and report demands must be explicit covariates / controls;
- success requires **incremental out-of-sample prediction**, not merely a fitted correlation.

This replaces the unfalsifiable reading in which an unspecified distance and an open-ended deformation list could always be chosen after the fact.

### 4.1 What would count as support

A useful result would have the form:

```text
sensory / task baseline
+ preregistered RDef predictors
-> reliable incremental prediction of Delta_ij
```

across held-out stimuli, sessions or participants.

### 4.2 What would count against the bridge

The claim is weakened if, in the declared non-masking regime:

1. preregistered deformation predictors add no out-of-sample information beyond low-level sensory / task features;
2. phenomenal neighborhoods remain stable while independently measured immediate accessibility rewrites vary strongly;
3. deformation-profile neighborhoods remain stable while phenomenal similarity systematically reorganizes;
4. any apparent relation disappears under cross-validation or a matched sensory control.

Large, reproducible dissociations are not to be redescribed away by changing `Dist` after seeing the data.

---

## 5. Empirical anchor: quality-space data and a non-trivial dissociation requirement

The existing qualia annex already points to:

- Fleming & Shea (2024), *Quality space computations for consciousness*;
- Hirao et al. (2025), a neuroimaging dataset using sequential color-qualia similarity judgments with report and no-report conditions.

`PH-QUAL01` does not treat those sources as proof of SRT. They provide a concrete way to stop the hypothesis from remaining purely verbal.

### 5.1 Test A1 — lock the phenomenal geometry first

Use pairwise color-qualia similarity judgments to estimate `Delta_ij` **without using future-selectability variables to construct the phenomenal target**.

Where the Hirao dataset supports the required trial-level structure, its report / no-report design can be used to check whether candidate relations survive obvious report-demand confounds.

### 5.2 Test A2 — build the deformation predictor independently

Estimate a bounded `RDef` proxy from measures that are conceptually downstream of the event but assessed as the **immediate post-event state update**, for example:

- change in subsequent candidate discrimination thresholds;
- attention allocation to competing candidates;
- memory weighting for near-neighbor alternatives;
- action / categorization affordance shifts;
- counterfactual accessibility or switching costs.

If an existing dataset does not contain enough of these variables, it should be used to lock the stimulus set / phenomenal geometry and motivate a matched follow-up experiment rather than pretending an unavailable variable was measured.

### 5.3 Non-triviality criterion

The key test is not that two nearby colors both feel similar and cause similar downstream processing. That can be a trivial consequence of sensory similarity.

At least one confirmatory analysis should seek a dissociation such as:

```text
matched / near-matched sensory feature distance
but different learned history, stake, context or action relevance
-> different RDef profiles
-> corresponding shift in Delta_ij
```

or the reverse control:

```text
changed sensory feature distance
but experimentally stabilized action / history / concern structure
-> does Delta_ij follow sensory geometry alone or retain RDef-linked structure?
```

Only such incremental / dissociation results would materially strengthen the SRT-specific bridge.

---

## 6. Ownership / for-me-ness is an HP-A extension, not HP-C or HP-B

The earlier draft placed ownership inside the phenomenal-character bucket. This revision corrects that taxonomy.

A bearer-indexed event can have a stronger **structural ownership basis** when:

1. a candidate bearer `B` has already been provisionally individuated under an independent boundary / continuity criterion;
2. the event's consequences return to that same candidate unit;
3. history-dependent writeback persists in that unit;
4. the event changes that unit's immediate future-accessibility structure;
5. the relevant update cannot be trivially transferred / reset while preserving the declared bearer-identity criterion.

Candidate route:

```text
independently bounded bearer candidate
+ same-bearer consequence return
+ history writeback
+ immediate future-accessibility rewrite
-> stronger structural basis for ownership / for-me attribution
```

### 6.1 Anti-circularity guard

Do **not** reason:

```text
B is the bearer because consequences close on B
and
consequences close on B because B is the bearer
```

`PH-IND02` explicitly treats selective closure as a precursor rather than a bearer definition and requires dynamic boundary investigation before bearer attribution. `P1-T06` / Stable-ISP work supplies a separate continuity-side constraint.

Therefore the order is:

```text
candidate organization
-> independently declared provisional boundary / identity criterion
-> consequence-return audit
-> history / future-selectability audit
-> stronger bearer candidate
-> phenomenal ownership remains separately assessed
```

### 6.2 Resetability must not be judged from hindsight

“Not fully resettable” is not a fact discovered only after observing the future. It must be evaluated relative to a declared identity / continuity / reset protocol:

```text
Would resetting / copying / offloading preserve the same candidate bearer
under the criterion declared before the test?
```

This remains a bridge-level discriminator, not a metaphysical identity theorem.

Guardrail:

```text
structural basis for for-me-ness
!= phenomenal presence proved
```

---

## 7. Phenomenal dimensions that the bridge may constrain

### 7.1 Qualitative character

The new contribution is not:

```text
red = one RDef profile
blue = another RDef profile
```

as a reductive identity.

Rather:

> Given the existing `L0-access x theta x L2_current` anchor, different experiences may also differ systematically in the immediate accessibility rewrites they induce in the same bearer.

### 7.2 Phenomenal similarity

Phenomenal neighborhood may partly covary with similarity of those preregistered immediate deformation profiles, subject to the controls in §4–§5.

### 7.3 Intensity

Intensity must not be identified with stimulus magnitude, `Psi_f`, `d` or total option loss.

Candidate predictors include:

- breadth of immediate candidate reprioritization;
- persistence of writeback;
- attentional capture;
- stake coupling;
- recoverability burden;
- degree to which the update reaches multiple action / memory / concern dimensions.

But the repository's `Psi_f_actual / Psi_f_felt` split is a live warning: a system can bear accumulating actual cost while registering little of it. Therefore:

```text
phenomenal intensity
cannot be assumed to track actual structural burden monotonically
```

Any intensity model must specify whether it predicts felt / registered burden, actual burden, or their divergence.

### 7.4 Temporal thickness

Temporal thickness is read as:

```text
historically conditioned present event
+ immediate rewrite of conditional future accessibility
```

not as future facts reaching backward to constitute the present.

### 7.5 Ineffability — positional difference first, compression second

This patch inherits `SRT_HardProblem_Epistemology §3.4` rather than replacing it.

Primary source:

```text
internal selection / bearing position
!= external re-objectification position
```

An external description is another selection and objectification event, not a transparent copy of the original internal event.

Secondary source:

```text
L1 high-dimensional lived structure
-> lossy L2 linguistic / conceptual compression
```

Therefore:

> Ineffability may be intensified by the high dimensionality of a bearer-specific reselective deformation profile, but compression is secondary to the more basic positional / re-objectification difference.

Do not write:

```text
ineffability = lossy compression
```

---

## 8. Valence and reselectability are orthogonal enough to require a 2 x 2

Central guard:

```text
Valence != Reselectability != Reselectability health
```

The important claim is not inversion but partial orthogonality.

| | Long-horizon reselection preserved / expanded | Long-horizon foreclosure |
|---|---|---|
| **Negative valence** | acute protective pain: local narrowing may preserve bodily / action capacity | chronic trauma / maladaptive pain: protective closure fails to reopen |
| **Positive valence** | curiosity / insight: exploratory or inferential alternatives may open | addiction / habit capture: positive reward can stabilize narrowing and repeated lock-in |

This table makes four distinct points:

1. negative valence does not imply pathological foreclosure;
2. positive valence does not imply healthy expansion;
3. local option count is not reselectability health;
4. long-horizon reopening / recoverability must be measured separately from reported valence.

### Test B becomes operational

Within each valence sign, compare conditions matched as closely as possible for reported valence but differing in later reopening / accessibility:

```text
negative: protective acute pain vs persistent maladaptive lock
positive: curiosity / insight vs addictive / habitual capture
```

The bridge predicts that valence matching will not erase differences in reselective geometry.

---

## 9. Pain, trauma and addiction: use the existing actual / felt split

### 9.1 Acute pain

Do not write:

```text
pain = Psi_f
pain = d
pain = T_dir
pain = low reselectability
```

A safer bridge reading is:

> Acute pain can be modeled as a high-priority phenomenal event that sharply reprioritizes the same bearer's near-term candidate space under bodily stake, often producing local narrowing that protects longer-horizon capacity.

### 9.2 Trauma / chronic maladaptive pain

Candidate pathology:

```text
protective local closure
-> history-bearing writeback
-> overgeneralized candidate exclusion
-> reduced recoverability / reopening
-> persistent foreclosure
```

The key variable is failure to reopen, not negative valence alone.

### 9.3 Addiction / lethal-L2 crosswalk

The existing `T_dir` / lethal-L2 line already treats addiction-like dynamics as a case in which attractive or low-felt-cost trajectories can coexist with worsening underlying structural debt.

`_SRT_PSI_F_CANONICAL.md §10` explicitly allows:

```text
Psi_f_actual >= Psi_f_felt
```

with hidden debt when the system does not register the cost it is actually paying.

This is a **live boundary condition and potential falsifier** for a naive version of Claim PH-QUAL01-A:

```text
felt phenomenal profile
need not mirror actual long-horizon future-selectability damage
```

Therefore the similarity claim is scoped to declared regimes where strong actual/felt masking is not independently indicated. A later theory may predict an interaction with masking; it may not simply redefine every mismatch as support.

---

## 10. Relation to canonical `d`

Canonical `d` remains the scalar summary of stake-coupled concern / irreversible-risk sensitivity. This patch does not redefine it.

Keep:

```text
d != qualia intensity
d != qualia richness
d != information capacity
d != consciousness level
d > threshold != phenomenality proof
```

The existing qualia annex also carries a legacy / bridge-side consciousness-entry condition involving `d > d_UAL`. Read it only as a **necessary-gate style condition inside that interface**, not as a sufficiency theorem for phenomenality.

The useful PH-QUAL01 role is narrower:

> `d` can help identify which discriminable directions are genuinely stake-coupled when constructing a deformation profile; it does not turn the profile into experience.

---

## 11. Relation to `T_dir`

`T_dir` is not qualia and not valence.

Its current v0 role concerns whether a system can read back and use its own selection direction for reorientation.

Thus:

```text
strong causal deformation
!= high T_dir
```

because a system can be strongly pushed by a direction it cannot adequately read or reorient around.

Conversely:

```text
explicit direction report
!= phenomenal-structure proof
```

`T_dir` can become a useful moderator when testing whether an immediate accessibility rewrite is internally readable, but it is not part of the definition of qualia.

---

## 12. Relation to `Psi_f`: actual burden, felt burden and a predicted dissociation

This patch does not identify felt pain, discomfort or intensity with canonical `Psi_f`.

Safe relation:

```text
Psi_f-related burden
may contribute to consequence structure
whose same-bearer writeback changes future accessibility
```

But §10 of `_SRT_PSI_F_CANONICAL.md` requires a split in pathological / L2-masking regimes:

```text
Psi_f_actual >= Psi_f_felt
```

This produces an important empirical pressure:

> If phenomenal character or intensity tracks the bearer's registered state while actual structural debt accumulates outside that registration, phenomenal geometry can systematically diverge from actual future-selectability damage.

That is not an embarrassment to be hidden. It is a discriminating boundary condition.

Do not write:

```text
Psi_f = pain
Psi_f = phenomenal intensity
high Psi_f automatically creates qualia
low felt cost = low actual cost
```

---

## 13. Weak bridge versus strong constitutive proposal

### 13.1 Weak bridge — current load-bearing claim

```text
Within a declared non-masking regime,
phenomenal similarity may show preregistered, incremental covariance
with independently estimated similarity of immediate bearer-indexed
reselective deformation profiles.
```

**Claim-ladder status:** P3 bridge candidate.

This is the part that can earn or lose support through discriminating analysis.

### 13.2 Strong constitutive proposal — explicitly unresolved

```text
[H] Qualitative character is the first-person mode of a concern-weighted,
history-bearing reselective deformation of a bearer.
```

**Claim-ladder status:** P4 candidate.  
**Annotation:** `[H]` marks a constitutive / metaphysical proposal; it is not a new claim-ladder level and must not be written as `P4/H`.

### 13.3 Current result of Test E: not passed

Run the deletion question now, not later:

```text
Delete only:
"qualitative character is the first-person mode of RDef"

Keep:
- bearer indexing
- history writeback
- immediate accessibility deformation
- relational geometry
- valence/reselectability dissociations
- trauma/addiction dynamics
- all behavioral / structural predictions
```

Current result:

> **No independently specified structural or predictive target has yet been shown to disappear.**

The main explanatory gains listed in this patch can presently be carried by the weak structural bridge without the constitutive identity sentence.

Therefore:

```text
Test E status = NOT PASSED
strong constitutive proposal = philosophical compression / open hardening target
not explanatory closure
```

Promotion requires either:

1. an independently specified explanatory target that is lost under deletion; or
2. a discriminating consequence unavailable to a purely structural reselective account; or
3. a non-circular argument showing why the identity is constitutively necessary.

Until then, the strong sentence must not be cited as an established SRT solution to HP-B or HP-C.

---

## 14. Falsification / discrimination program

### Test A — phenomenal geometry beyond sensory geometry

Use the two-stage design in §5:

1. estimate `Delta_ij` independently;
2. preregister a bounded `RDef` model family;
3. control sensory-feature and task distances;
4. test incremental out-of-sample prediction;
5. include at least one sensory / history / action-relevance dissociation.

**Failure:** no incremental prediction or unstable post-hoc metric dependence.

### Test B — 2 x 2 valence / long-horizon reselection dissociation

Use the §8 four-cell structure and test whether matched-valence conditions differ in reopening / recoverability geometry.

**Failure:** once valence and obvious task features are matched, the proposed reselective dimensions contribute no stable discrimination.

### Test C — local compression versus global preservation

Compare acute protective narrowing with chronic unreopened narrowing.

Prediction:

```text
similar local narrowing
but different reopening trajectories
```

should distinguish protective closure from pathological foreclosure.

### Test D — ownership / bearer consequence, split into two arms

The earlier generic instruction to “match systems while varying same-bearer consequence return” was not operationally adequate. Use two explicitly different arms.

#### D1 — human ownership dissociation arm

Use human paradigms or clinical / quasi-experimental conditions in which representation / perceptual content and felt ownership can dissociate, for example carefully selected bodily-ownership manipulations or depersonalization / derealization phenomena.

Measure separately:

- represented content;
- ownership / for-me reports;
- history writeback;
- immediate accessibility changes;
- continuity / consequence-return proxies.

This arm can test ownership structure but cannot cleanly manipulate bearer identity itself.

#### D2 — artificial-system negative-control arm

Reuse `PH-CONSC04`'s `Z4` / `Z6` logic.

Artificial systems can vary:

- persistent same-instance writeback;
- reset / copy / outsourcing conditions;
- self-model / report content;
- future-policy accessibility.

But the dependent variables here are **behavioral / architectural / report readouts only**.

Do not infer:

```text
artificial RDef difference -> phenomenality difference
```

The arm is a negative control for representational sufficiency, not a consciousness assay.

### Test E — constitutive deletion

Current result is already recorded in §13.3:

```text
NOT PASSED
```

Keep it open until a genuine explanatory residue is identified.

### Test F — actual / felt divergence

Predefine a masking / debt regime using measures independent of the phenomenal similarity target.

Prediction:

```text
low-masking regime:
Delta_ij may track preregistered immediate RDef geometry incrementally

high-masking / lethal-L2-like regime:
phenomenal / felt structure may decouple from actual long-horizon structural damage
```

A useful theory must predict the boundary rather than fit both outcomes post hoc.

---

## 15. What this bridge can currently claim

### Current plausible gain

The weak bridge may help SRT:

- connect its existing three-factor qualitative anchor to forward accessibility;
- turn quality-space talk into a discriminating reselectability analysis;
- separate phenomenal similarity from mere sensory-feature similarity;
- type ownership as an HP-A problem rather than smuggling it into HP-B;
- model pain / trauma / addiction without equating valence with health;
- predict actual / felt divergence under L2 masking;
- preserve historical thickness without retrocausal constitution;
- state exactly where the constitutive hypothesis currently fails its own deletion test.

### Still open

It does not establish:

- why phenomenal presence exists at all;
- why `Z6` is impossible;
- why a structural bearer must be an experiencer;
- why one physical / computational realization must instantiate one specific quale;
- that `RDef` explains more than neighboring embodied / enactive / predictive frameworks;
- a universal metric over deformation profiles;
- a necessary-and-sufficient bearer boundary.

---

## 16. Compatibility constraints

Read this patch under all of the following guards:

```text
HP-A != HP-B != HP-C
```

```text
Selector != Bearer != Concern Domain != Experiencer
```

```text
PERS-1 != PERS-2 != PERS-3
```

```text
structural bearing != phenomenal bearing proved
```

```text
capacity / distinguishability != canonical d
```

```text
valence != T_dir
```

```text
Psi_f_actual may diverge from Psi_f_felt
```

```text
option count != reselectability
```

```text
later realized future != constituent of q_t at t
```

```text
reselective qualia geometry != solved hard problem
```

Any future promotion that violates one of these guards requires explicit cross-file repair and governance review.

---

## 17. Integration targets

This patch does not directly rewrite owner / canonical-facing documents. A separate integration hook records the landing order.

### 17.1 `Philosophy/Foundations_Annex/06_Qualia_Interface_Batch.md`

Future integration should:

- cross-reference PH-QUAL01 after `Def-Phil-Qualia-3`;
- reuse `Delta_ij` rather than introduce a competing phenomenal-distance symbol;
- add the incremental-prediction / sensory-control requirement;
- retain the existing quality-space literature anchors.

### 17.2 `Philosophy/SRT_HardProblem_Epistemology.md`

Future synthesis should:

- preserve `PH-CONSC04`'s HP-A / HP-B split;
- add `HP-C` only as the qualitative-character label;
- treat reselective deformation as a forward-facing fourth interface to the existing §3.3 three-factor anchor;
- preserve §3.4's positional-difference-first, compression-second account of ineffability;
- reconcile any stronger legacy bearing/phenomenality wording with `PH-CONSC04` rather than letting PH-QUAL01 silently decide HP-B.

### 17.3 `Philosophy/SRT_Subjecthood_Threshold_Interface.md`

Future integration should:

- use `PH-IND02` / continuity constraints to establish a provisional bearer candidate before applying same-bearer deformation tests;
- keep ownership as HP-A support;
- never use `RDef` to bootstrap subjecthood or phenomenality circularly.

### 17.4 `Core/SRT_OPEN_TENSIONS.md`

Future integration may note PH-QUAL01 as an HP-C bridge candidate while preserving:

```text
Stable ISP natural boundary / phenomenal necessity = open
```

The strong `[H]` constitutive proposal must remain visibly unresolved because Test E is currently not passed.

---

## 18. One-paragraph abstract

SRT already constrains qualitative specificity through the current `L0-access x theta x L2_current` anchor and already separates perspective-center individuation (HP-A) from phenomenal necessity (HP-B). PH-QUAL01 adds a narrower HP-C bridge: once phenomenality is independently in play, the qualitative relations among experiences may receive additional forward-facing constraint from the **immediate, bearer-indexed rewrite of conditional future accessibility** produced when an event is incorporated. This rewrite is defined at `t^- -> t^+`, not by whatever future path later happens, so the proposal does not make present experience retroactively depend on later behavior. The weak P3 claim is empirically risky only when `RDef` is preregistered independently of phenomenal similarity and must add out-of-sample prediction beyond sensory/task geometry. Valence, `d`, `T_dir` and `Psi_f` remain non-identical to qualia; `Psi_f_actual / Psi_f_felt` divergence supplies a live masking boundary. The stronger `[H]` identity claim remains a P4 candidate and explicitly **fails the current deletion test**: no independent explanatory target has yet been shown to disappear when the first-person identity sentence is removed.

---

## 19. Compact statements

### Preferred current formulation

> **在既有的“L0 接入方向 × 具身参数 θ × 当前历史锚定”之外，感受质的关系结构还可能受一个前瞻性接口约束：一次体验被这个持续承担者纳入时，会即时改变它接下来还能怎样注意、比较、行动、记忆、重新打开路径与再次选择。**

### Stronger formulation — open `[H]` proposal only

> **感受可能是这种 bearer-indexed 再选择形变的第一人称形态。**

Current governance note:

```text
strong formulation:
Test E = NOT PASSED
status = P4 candidate + [H] annotation
not canonical
not HP-B closure
```
