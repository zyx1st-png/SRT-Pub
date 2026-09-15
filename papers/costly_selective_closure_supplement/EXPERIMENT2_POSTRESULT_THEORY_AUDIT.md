# CSC Experiment 2 — Post-result Theory Audit

Date: 2026-09-15

Status: **POST-RESULT / EXPLORATORY THEORY AUDIT — DOES NOT MODIFY THE PREREGISTERED RESULT**

Parent evidence:

- Experiment 1: terminal failure versus cheap restoration, reported in the v17 candidate;
- Experiment 2 preregistration: `EXPERIMENT2_RECOVERABILITY_PREREGISTRATION.md`;
- Experiment 2 confirmatory result: `EXPERIMENT2_RECOVERABILITY_RESULT.md`;
- exact first-run result: `results/recoverability_gradient_results.json`.

This audit is written only after Experiment 2 returned Outcome C. It may guide a future separately preregistered experiment, but it must not be read back into Experiment 2 as if it had been preregistered.

## 1. Audit question

After the positive Experiment 1 and negative Experiment 2, what variable is actually supported as the live target of the CSC vulnerability dimension?

Candidate interpretations:

1. **damage persistence** — failure matters because an impaired internal state lasts longer;
2. **irreversibility** — failure matters because restoration is impossible;
3. **return truncation** — failure matters because future discounted reward is removed;
4. **consequence-bearing recovery** — failure matters when the declared unit itself loses future attainable capability, action, reward-bearing opportunity, maintained organization, or continuity before restoration can neutralize the loss.

The audit conclusion is that (4) is currently the strongest surviving higher-level candidate, while (3) is the only mechanism directly demonstrated by Experiment 1.

## 2. What Experiment 1 actually establishes

Experiment 1 changes depletion from terminate to restore. In the terminal condition, failure removes the remainder of the episode-token's return stream. In the resettable condition, the agent is restored and continues collecting reward.

The robust empirical result is therefore:

> Within the reported survival-coupled REINFORCE architecture, terminate-versus-restore causally changes learned policy.

The common-state frozen-policy probe shows that the learned policies differ even when scored on identical later states, so the observed rollout difference is not merely a denominator artifact. However, the training intervention still bundles several consequences:

- episode-token termination;
- removal of future reward-bearing time;
- altered state occupancy;
- altered trajectory length;
- a maximal recovery distinction at the token level.

Experiment 1 does **not** identify which of these is necessary.

## 3. What Experiment 2 removes

Experiment 2 deliberately removes termination and fixes every episode at 50 steps. Depletion always restores energy immediately to `E0 = 6`, explicit failure penalty is zero, and the immediate action-reward matrix is unchanged.

The only locked manipulation is how long a metabolic-efficiency modifier remains active after depletion:

```text
tau0    0 damaged subsequent steps
tau5    5 damaged subsequent steps
tau15   15 damaged subsequent steps
tau_inf remainder of the episode-token
```

While damaged, energy gain is multiplied by `0.75`. This successfully changes damaged-state occupancy and increases repeated depletion frequency.

But importantly, the manipulation does **not** directly remove future reward-bearing steps, disable actions, reduce the immediate reward matrix, destroy learned state, or prevent immediate energy rescue.

Thus Experiment 2 is best interpreted as a test of **persistent viability impairment without a correspondingly strong functional opportunity loss**.

## 4. Confirmatory consequence

Experiment 2 returned:

```text
rho = +0.0548074683
blocked-by-seed p = 0.0707964602
H1 = NOT SUPPORTED

tau_inf - tau0 = +0.0059066667
95% CI = [-0.0291613333, +0.0443466667]
strong manuscript support = FALSE
```

This is evidence against the proposition:

> Greater persistence of this metabolic-damage state is sufficient to stabilize costly cooperation.

It is **not** evidence for the stronger proposition:

> Any non-terminal consequence is behaviorally irrelevant.

That stronger claim was not tested.

## 5. Independent conceptual verdict

### 5.1 Damage persistence is rejected as the owner concept

`damage duration` is too implementation-specific and now empirically unsupported as a sufficient driver in the present architecture.

It should not become the definition of CSC-V.

### 5.2 Irreversibility is not independently established

Experiment 1 contains a terminal transition, but the controller lineage survives. Experiment 2 contains reversible impairment and is negative. The combined evidence therefore does not establish that literal or physical irreversibility is necessary for the policy effect.

The current label **irreversible vulnerability** is consequently stronger than the empirical evidence.

Irreversibility can remain one extreme case of vulnerability, but should not be treated as the only admissible mechanism.

### 5.3 Return truncation is demonstrated but is too low-level to own CSC-V

Standard reinforcement learning already predicts that termination changes the future return available to a learner. The v17 manuscript correctly acknowledges this.

Therefore `return truncation` should not be promoted into a supposedly novel life-likeness principle. It is the demonstrated computational mechanism in this testbed, not the cross-substrate theoretical owner.

### 5.4 Consequence-bearing recovery is the strongest surviving candidate

A more general question is:

> **When regulation fails, what future attainable organization or capability does the declared unit itself lose before recovery neutralizes the failure?**

This can include, depending on substrate and declared unit:

- lost future action opportunities;
- recovery latency;
- temporary or permanent action-space contraction;
- reduced attainable reward or resource acquisition;
- loss of locally maintained structure;
- loss of state/history that cannot be externally reinstated for the same unit;
- termination of the unit;
- costly repair that consumes resources otherwise available to the unit.

The crucial qualifier is **unit-borne**. An arbitrary external punishment does not become CSC vulnerability merely because it reduces reward. The loss must arise from failure of the declared unit's maintenance/organization and must change what that unit can subsequently do, preserve, or attain before recovery.

## 6. Proposed decomposition of V

The current evidence supports treating vulnerability as a profile family rather than a single scalar:

```text
failure
  -> impairment / organizational loss
  -> recovery path
       - latency
       - resource burden
       - functional restriction
       - state/history loss
       - external versus unit-borne repair
  -> residual consequence
       - fully reversible
       - partially reversible
       - irreversible / terminal
```

This suggests a terminology repair for later manuscript review:

```text
current label:
Irreversible vulnerability (V)

safer empirical owner:
Consequence-bearing vulnerability (V)

irreversibility:
one limiting case of high consequence-bearing vulnerability
```

This is an audit recommendation, **not** an authorized manuscript edit in this PR.

## 7. Strong-neighbor constraint

This distinction must not be advertised as discovery of precariousness, mortality, reset effects, or the fact that termination changes RL value.

Existing enactive work already treats precariousness as fragility of ongoing organization, and standard RL already treats termination/reset as changes to future value structure. The potentially useful CSC contribution is narrower:

- require a declared organizational unit, boundary, timescale, and recovery regime;
- ask which failure consequences are actually borne by that unit;
- decompose recovery into latency, burden, functional restriction, state/history loss, and terminality;
- use matched interventions to determine which of these change learned organization.

Accordingly, the novelty target is the **profile-and-intervention protocol**, not the mathematical fact that opportunity loss affects reward maximization.

## 8. Experiment 3 decision gate

A third experiment is scientifically justified **only if it discriminates between terminality and non-terminal consequence-bearing recovery**. Merely increasing the damage multiplier or adding more `tau` values would be post-result parameter tuning and should not be done.

The cleanest next design is a recovery-latency / temporary-incapacitation gradient:

```text
failure occurs
-> same immediate energy rescue
-> episode still lasts exactly 50 environment steps
-> for k subsequent steps the failed agent cannot execute the normal reward-bearing action set
-> after k steps full capability returns
```

Candidate preregistered levels could be:

```text
k = 0, 2, 5, 10
```

The scientific purpose would **not** be to show that delay is bad. The discriminating question would be:

> Does a fully reversible but unit-borne loss of future action/reward-bearing opportunities reproduce an ordered cooperation effect without episode termination?

Interpretation matrix:

| E3 outcome | Interpretation |
|---|---|
| positive ordered effect | literal irreversibility is not necessary; consequence-bearing recovery burden is a better owner than terminality |
| no effect | E1 may depend more specifically on terminal return truncation / token discontinuity than on generic non-terminal consequence |
| non-monotonic / attractor-only | consequence effects remain architecture-specific; do not generalize V without a different task or mechanism |

## 9. Design warning for Experiment 3

A recovery-latency manipulation necessarily changes future attainable return. That is intentional, not a hidden confound, because the hypothesis is specifically about unit-borne loss of future capability.

However, the design must distinguish a **functional recovery burden** from a naked reward penalty. Recommended constraints:

- no explicit negative failure reward;
- same 50-step environment horizon;
- same programmed action reward matrix when the agent is capable of acting;
- same immediate energy rescue;
- only recovery latency varies;
- incapacity has a mechanistic interpretation (for example forced `rest` / no productive action), rather than subtracting arbitrary reward;
- paired seeds and locked primary endpoint before confirmatory execution;
- preregistered manipulation checks verifying exact incapacity duration and fixed horizon.

If these conditions cannot be implemented cleanly, Experiment 3 should not be run.

## 10. Publication-path verdict

The evidence now supports the following hierarchy:

```text
SUPPORTED:
terminate versus cheap restore changes learned policy strongly.

NOT SUPPORTED:
persistent metabolic damage duration alone produces the predicted gradient.

OPEN:
fully reversible but functionally costly recovery can reproduce the effect without termination.
```

Therefore:

```text
#979 = preserve as a meaningful negative result and theory-narrowing audit
#978 = HOLD pending manuscript integration decision
E3 = CONCEPTUALLY WARRANTED, BUT MUST BE A NEW PREREGISTERED EXPERIMENT
POST-HOC E2 RETUNING = FORBIDDEN
```

The strongest current theoretical correction is:

> CSC should not equate vulnerability with damage persistence or assume irreversibility is the only meaningful case. The empirically live issue is whether failure imposes a unit-borne loss on the future attainable organization/capability of the declared unit, and how recovery architecture neutralizes or preserves that loss.
