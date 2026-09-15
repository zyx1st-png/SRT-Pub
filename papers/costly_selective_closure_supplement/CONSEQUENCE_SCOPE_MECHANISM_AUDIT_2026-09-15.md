---
id: CSC-CONSEQUENCE-SCOPE-MECHANISM-AUDIT-2026-09-15
type: research_audit
status: draft
canonical: false
claim_mode: analysis
parent_evidence:
  - papers/costly_selective_closure_supplement/src/csc_experiment.py
  - papers/costly_selective_closure_supplement/src/csc_recoverability.py
  - papers/costly_selective_closure_supplement/src/csc_consequence_recovery.py
  - papers/costly_selective_closure_supplement/results/recoverability_gradient_results.json
  - papers/costly_selective_closure_supplement/results/consequence_recovery_results.json
publication_context: Draft PR #981 held pending mechanism review
---

# Consequence Scope Mechanism Audit — E1/E2/E3

## 0. Status and hard boundary

This is a **mechanism audit**, not an Experiment 4 preregistration and not a new CSC theorem.

It was opened after the E1/E2/E3 sequence exposed a possible explanatory variable that is more specific than the current phrase `consequence architecture`: **which unit loses future return-bearing or action-bearing opportunity when one agent fails**.

The audit has four constraints:

1. preserve E1/E2/E3 as already observed evidence;
2. do not reinterpret preregistered negative results as positive confirmation;
3. do not select a new manipulation merely to recover a desired sign;
4. do not modify the publication candidate until the causal alternatives below are separated enough to justify a manuscript claim.

Current publication implication:

```text
#981 CONTENT/PACKAGING PASS = HISTORICAL CHECKPOINT
#981 MERGE = HOLD
E4 = NOT PREREGISTERED
E4 = NOT AUTHORIZED BY THIS AUDIT ALONE
```

---

## 1. Why the previous one-dimensional reading is no longer sufficient

The existing sequence is:

```text
E1 terminal vs restore
-> large positive terminal cooperation effect

E2 persistent metabolic impairment, fixed horizon
-> preregistered positive gradient not supported

E3 forced-recovery latency, fixed horizon
-> preregistered positive gradient not supported
-> observed negative ordinal association
```

A coarse summary says only that these are different `consequence architectures`. That statement is safe but under-explanatory. The transition rules reveal a more specific candidate causal distinction:

> When one agent fails, does the consequence remain primarily local to that agent, or does the partner also lose future opportunities/returns?

This is called **consequence scope** in this audit. It is a mechanism candidate, not a validated general variable.

---

## 2. Verified implementation facts

### 2.1 E1: terminality creates dyad-level continuation dependence

The E1 environment uses the same immediate reward function in terminal and restore conditions. Energy depletion is processed agent by agent, but in the terminal condition the environment ends when **any** agent is no longer alive:

```text
done = horizon reached
       OR (terminal condition AND any agent depleted)
```

Therefore one agent's depletion has two distinct effects:

```text
failed agent:
  loses the remainder of the current episode-token

partner:
  also loses the remainder of the current episode-token
```

The controller lineage survives across later episodes, so this is not controller destruction. It is nevertheless a **shared within-token future-opportunity loss**.

E1 also has an algorithmic consequence that must not be hidden. `Policy.update`:

1. computes discounted returns on the realized trajectory;
2. standardizes returns within that trajectory when variance is nonzero;
3. averages the policy-gradient sum by realized trajectory length.

Terminal failure therefore changes not only environment continuation but also the realized return vector, the number of policy decisions, the within-trajectory normalization sample, and the gradient averaging denominator.

This does not invalidate E1. It does mean that `terminality` is a bundled intervention at the learning-process level.

### 2.2 The energy asymmetry makes unilateral cooperators especially failure-exposed

The E1/E2/E3 energy table implies the following net energy changes after the universal metabolic cost of `1.0`:

```text
C vs C:     +1.0
C vs Solo:  -1.0
Solo vs C:  +0.2
Solo vs Solo: -0.3
C vs Rest:  -0.6
Solo vs Rest: 0.0
Rest vs any: -0.5
```

The immediate reward table simultaneously gives:

```text
C vs Solo -> 0.0
Solo vs C -> 1.4
C vs Rest -> 0.2
Solo vs Rest -> 0.9
Rest vs any -> 0.25
```

Thus in a unilateral `C vs Solo` interaction, the cooperator both receives the lower reward and loses energy faster. This makes the exploited cooperator a plausible first-failure candidate.

If that cooperator fails in E1 terminal, however, the exploiting partner also loses its remaining within-episode future. This creates a plausible route by which partner viability becomes instrumentally relevant to the partner's own future return.

This is an **analytic mechanism hypothesis** from the transition table. The existing result files do not contain event-level first-failure antecedent logs, so the audit does not claim that most actual E1 failures empirically occurred in `C vs Solo` states.

### 2.3 E2: damage changes viability state, not immediate return

E2 holds all episodes at 50 steps. On depletion:

```text
failure penalty = 0
energy -> E0 = 6 immediately
episode continues
normal action set remains available
```

Its manipulation multiplies future `ENERGY_GAIN` by `0.75` while damage is active. It does **not** modify the immediate `REWARD` table.

Consequently, persistent damage does not directly remove reward-bearing time, does not remove actions, and does not apply an explicit reward penalty. It can affect learning indirectly through:

- energy features in the observation;
- low-energy indicators;
- later state occupancy;
- later depletion frequency;
- the mortality-seen/failure-history features.

The manipulation was real: mean damaged-agent-step fraction rose from `0.000` at `tau0` to about `0.529` at `tau_inf`, and mean final-window depletion events rose from `3.71` to about `5.10` per episode. Yet the locked endpoint contrast remained only about `+0.006`, with 95% CI approximately `[-0.029, +0.044]`.

The correct inference is therefore narrower than a general rejection of persistent consequence:

> In this testbed, persistent internal metabolic impairment that did not directly remove reward-bearing time or normal actions did not reproduce E1's cooperation effect and excluded the preregistered `+0.10` strong endpoint effect.

### 2.4 E3: recovery latency localizes lost action opportunity to the failed agent

E3 also fixes every episode at 50 environment steps and restores energy immediately to `E0 = 6`. Its manipulation is different:

```text
failed agent
-> k subsequent forced-Rest steps
-> no normal policy action during those steps

partner
-> remains decision-capable unless it is also recovering
```

Therefore the loss of normal action opportunity is **primarily individual-scoped**.

This also changes the partner's social environment. Against a forced-Rest partner, the immediate table favors `Solo` over `Cooperate`:

```text
partner chooses Solo vs Rest -> reward 0.9, net energy 0.0
partner chooses C vs Rest    -> reward 0.2, net energy -0.6
```

Thus E3 does not merely make recovery longer. It can create a temporary state in which the still-active partner has both immediate reward and energetic reasons to choose Solo rather than Cooperate.

The observed E3 result is statistically strong in ordinal terms but modest in absolute endpoint size and occurs mainly in a floor-dominated regime:

```text
rho about -0.704
k10 - k0 about -0.037
95% CI about [-0.099, -0.003]
median cooperation:
  k0  about 0.0028
  k10 = 0
```

The common-state frozen-policy probe shows that the negative direction is present in learned policies and is not only a denominator artifact caused by excluding recovery steps from the cooperation measure.

### 2.5 E3 also changes the learning update for affected agents

E3 cannot be interpreted as a pure environment transition manipulation without qualification.

Because forced Rest is not a policy decision, `_update_masked`:

1. computes returns over all elapsed steps;
2. takes only genuine decision indices for score-function gradients;
3. standardizes **decision returns** over the condition-dependent set of genuine decisions;
4. divides the gradient sum by the number of genuine decisions.

At `k0`, every step is a decision and this is algebraically aligned with the original E1/E2 update. At `k>0`, failed agents have fewer genuine decisions. The return-standardization population and gradient averaging denominator therefore change with recovery occupancy.

This is not an implementation bug: it follows the preregistered semantics that forced actions receive no policy-gradient term. But it is a **mechanism-identification confound**.

The common-state frozen-policy probe cannot eliminate this confound because the learned policies were themselves produced under the condition-dependent masked updates.

---

## 3. Causal decomposition of the three experiments

| feature | E1 terminal | E2 persistent damage | E3 recovery latency |
|---|---|---|---|
| fixed 50-step environment horizon after failure | no | yes | yes |
| direct future-return truncation | yes | no | not terminal, but temporal return changes occur |
| normal action loss | both agents because episode ends | no | failed agent only during recovery |
| partner loses future opportunities when the other fails | yes | no | generally no |
| failure burden localized to failed agent | partly, but partner also loses continuation | yes | yes, primarily |
| partner remains active while failed agent is impaired | no | yes | yes |
| partner receives special incentives against impaired/recovering state | no post-failure interaction | indirectly through state only | yes, because partner acts against Rest |
| update length/normalization changes with failure | yes | no | yes for recovering agents |
| observed cooperation result | high terminal effect | no positive gradient | negative ordinal association |

No single row is currently isolated well enough to be declared the unique owner of E1.

---

## 4. Four live competing hypotheses

### H-SCOPE — shared future-loss / consequence-scope hypothesis

The E1 effect is substantially driven by the fact that one agent's failure removes future return-bearing opportunity for **both** agents.

Mechanistic intuition:

```text
partner viability
-> affects my continuation
-> exploitation that drives partner toward failure can reduce my own future return
```

Prediction for a new non-terminal test:

> For the same recovery mechanism and same latency, making action/opportunity loss shared should yield more cooperation than localizing the loss to the failed agent.

A positive result would support a narrow consequence-scope mechanism. It would **not** prove that shared consequence fully explains E1.

### H-TERM — terminality-specific / return-truncation hypothesis

The dominant E1 effect depends on true episode termination and the associated return/trajectory transformation. Shared non-terminal burden will not reproduce it.

Prediction:

> Shared and individual non-terminal recovery may differ little, or both may remain near the low-cooperation regime; only true terminality produces the large E1 separation.

This is a serious rival because E1 changes the realized trajectory and learning update in ways E2/E3 do not.

### H-VICTIM — asymmetric-victim-burden hypothesis

The sign difference between E1 and E3 arises partly because unilateral cooperation is energetically fragile. In E3, the agent most exposed to exploitation can also become the agent forced out of normal choice, while the partner remains free and is rewarded for Solo against Rest.

Prediction:

> E3 failure events should be enriched for cases in which the depleted agent is the cooperator in an asymmetric interaction, and active partners during individual recovery should show elevated Solo choice. Sharing the recovery loss should attenuate the negative E3 pattern.

This hypothesis requires event-level diagnostics that are absent from the currently committed aggregate result files.

### H-UPDATE — learning-update-mechanics hypothesis

Part of E3's ordered negative association is generated by the condition-dependent decision mask and return standardization rather than by recovery burden alone.

Prediction:

> The magnitude or ordering of the E3 effect will change materially under an update formulation that holds return normalization/gradient scaling comparable across consequence-scope conditions.

This does not imply that E3 is invalid. It limits any attempt to interpret the E3 sign as an architecture-general law.

---

## 5. What the current evidence can and cannot support

### Supported now

1. E1 robustly establishes a terminal-versus-restore difference in the reported REINFORCE testbed.
2. E2 excludes the preregistered large positive endpoint effect for its particular internal-damage manipulation.
3. E3 rejects its preregistered positive hypothesis and yields a negative learned-policy association under individual-scoped forced recovery.
4. The three manipulations are not empirically interchangeable in this testbed.
5. `who loses future opportunity when failure occurs?` is now a legitimate mechanism question generated by the existing results.

### Not supported now

1. consequence scope is the unique cause of E1;
2. E1 has already shown a general law of shared fate/cooperation;
3. E2 disproves every form of persistent non-terminal consequence;
4. E3 proves that recovery burden generally suppresses cooperation;
5. a scalar `failure severity` variable has been disproved in all possible operationalizations;
6. the CSC B/M/H profile is empirically validated by these experiments.

---

## 6. Candidate next experiments

### Design A — action-opportunity scope replication of E3

This is the most direct next test of H-SCOPE versus H-VICTIM while staying close to an already implemented mechanism.

New confirmatory seeds must be disjoint from E1/E2/E3 seeds.

For each nonzero recovery latency, compare:

```text
INDIVIDUAL scope:
  failed agent -> forced Rest for k steps
  partner remains normally decision-capable

SHARED scope:
  if either agent fails -> both agents forced Rest for k steps
  then both regain normal action availability
```

Everything else remains matched:

```text
fixed 50-step horizon
same E0 rescue
zero explicit failure penalty
same reward/energy tables
same policy architecture
same bonus schedule
same optimizer/update family
same seeds across scope conditions
```

To avoid selecting a favorable latency after seeing E3, a preregistration should reuse all previously locked nonzero values `k = 2, 5, 10` rather than cherry-pick `k10`.

A common `k0` anchor may be included as an implementation invariant; scope is behaviorally undefined/redundant at zero latency and should not be treated as an independent factorial cell.

Candidate primary contrast:

```text
for each seed:
  mean over k in {2,5,10} of
  [post_coop(shared,k) - post_coop(individual,k)]
```

with a paired randomization/sign-flip test and paired confidence interval locked before execution.

Required diagnostics should include:

- first/triggering failure action pair;
- identity of the failed agent relative to `C vs Solo` asymmetry;
- partner actions during individual recovery;
- forced-agent-step fraction by scope;
- eligible-decision fraction;
- depletion frequency;
- common-state frozen-policy comparison.

Interpretation gate:

```text
shared > individual robustly
-> supports consequence scope for this action-opportunity mechanism
-> does NOT yet prove E1 is explained

shared ~= individual
-> weakens scope as the main explanation
-> increases weight on terminality/update-specific rivals

shared < individual
-> shared burden does not rescue cooperation here
-> H-SCOPE in its simple form is disfavored
```

#### Limitation of Design A

Design A intentionally changes who loses actions, so scope and the number of policy decisions are linked. It cannot fully eliminate H-UPDATE. A positive Design A result is therefore a mechanism step, not final causal closure.

### Design B — joint versus individual absorbing continuation

A closer terminality test would distinguish:

```text
JOINT ABSORPTION:
  one failure -> both units lose later decisions/returns

INDIVIDUAL ABSORPTION:
  failed unit loses later decisions/returns
  partner continues
```

This targets E1's shared future-loss structure more directly.

However, it creates a difficult ecological definition problem: after one member is absorbed, what exactly does the survivor interact with? A Rest surrogate, ghost policy, absent partner, or solo environment each changes the social game. Without a principled survivor transition, this design has a severe partner-state confound.

Verdict:

```text
scientifically important
NOT READY FOR PREREGISTRATION
```

### Design C — direct return-scope intervention

A cleaner mathematical mechanism probe could keep action availability and horizon fixed while making a failure-triggered return consequence apply either to the failed unit only or to both agents.

This would isolate `who bears return loss?` more directly than Design A. But it necessarily introduces an explicit return manipulation and therefore becomes a deliberately synthetic RL mechanism experiment rather than a naturalistic maintenance model.

It could be useful after Design A, especially if the goal is mechanism identification rather than life-likeness analogy.

Verdict:

```text
best isolation of return scope
but higher construct-artificiality cost
SECOND-STAGE OPTION
```

---

## 7. Recommended research sequence

The audit recommends a staged sequence rather than an immediate new positive-result search.

```text
Stage 0 — current audit
COMPLETE when competing explanations and design confounds are explicit.

Stage 1 — author adjudication
Question: is consequence scope worth testing as the next bounded mechanism claim?

Stage 2 — if YES, preregister Design A
Primary claim limited to action-opportunity consequence scope.
No claim that E1 is already explained.

Stage 3 — run Design A once on disjoint confirmatory seeds
Retain any null or opposite result.

Stage 4 — only if Design A supports scope strongly
Decide whether a second isolation test is worth paying:
  Design B after resolving survivor semantics, or
  Design C as a deliberately synthetic return-scope probe.
```

This sequence is compatible with the anti-positive-result-hunting principle because the new question is generated by a concrete mechanistic ambiguity in already observed results, and it has outcome rules that can directly defeat the new hypothesis.

---

## 8. Publication consequences

Before a new mechanism test, the v18 manuscript should not state or imply that `failure is not one-dimensional` as a universal empirical result.

The strongest already-supported publication claim is narrower:

> In this survival-coupled REINFORCE testbed, terminal depletion, persistent internal damage, and individual-scoped recovery latency are not interchangeable interventions. The current sequence identifies consequence scope, terminal return truncation, and action-opportunity structure as competing explanations that require further discrimination.

If no further experiment is run, this narrower wording is still publishable in principle, but the paper should:

1. reduce E2's falsification burden;
2. describe E3's negative rank effect separately from its modest absolute endpoint difference;
3. add the E3 update-mechanics caveat;
4. treat consequence scope as a future mechanism hypothesis, not a result;
5. avoid using B/M/H as if they were tested contributions.

If Design A later supports H-SCOPE, a stronger paper may become possible around the question:

> **Who bears failure? How the scope of lost future opportunity changes social learning in artificial agents.**

That title/claim is not authorized yet.

---

## 9. Current gate

```text
E1 = VALID TERMINAL-VS-RESTORE EFFECT
E2 = VALID PREREGISTERED NO-SUPPORT RESULT / CONSTRUCT INTERPRETATION NARROWED
E3 = VALID PREREGISTERED H1 FAILURE / NEGATIVE ORDINAL RESULT
E3 COMMON-STATE PROBE = POLICY DIFFERENCE CONFIRMED
E3 UPDATE-MECHANICS CONFOUND = LIVE
CONSEQUENCE SCOPE = PLAUSIBLE MECHANISM HYPOTHESIS / NOT ESTABLISHED
TERMINALITY-SPECIFIC RIVAL = LIVE
ASYMMETRIC-VICTIM-BURDEN RIVAL = LIVE
DESIGN A = RECOMMENDED FIRST DISCRIMINATION TEST
DESIGN B = NOT YET CLEAN ENOUGH
DESIGN C = SECOND-STAGE SYNTHETIC ISOLATION OPTION
E4 PREREGISTRATION = NOT YET WRITTEN
E4 CONFIRMATORY RUN = NOT AUTHORIZED
#981 = SCIENTIFIC HOLD PENDING AUTHOR ADJUDICATION OR NARROWER MANUSCRIPT REVISION
```
