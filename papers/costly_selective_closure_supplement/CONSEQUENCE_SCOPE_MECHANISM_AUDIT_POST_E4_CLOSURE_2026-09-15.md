---
id: CSC-CONSEQUENCE-SCOPE-MECHANISM-AUDIT-POST-E4-CLOSURE-2026-09-15
type: research_audit_closure
status: complete
canonical: false
claim_mode: adjudication
parent_audit: papers/costly_selective_closure_supplement/CONSEQUENCE_SCOPE_MECHANISM_AUDIT_2026-09-15.md
e4_adjudication: papers/costly_selective_closure_supplement/EXPERIMENT4_CONSEQUENCE_SCOPE_ADJUDICATION.md
publication_context: Draft PR #981 remains on scientific hold pending E1-E4 reconstruction
---

# Consequence-Scope Mechanism Audit — Post-E4 Closure

Date closed: 2026-09-15

## 1. Purpose

The pre-E4 mechanism audit identified four live explanations for the E1/E2/E3 sequence:

```text
H-SCOPE  = shared future-opportunity / consequence scope
H-TERM   = terminality / return-truncation-specific effect
H-VICTIM = asymmetric burden on an exploited cooperator
H-UPDATE = condition-dependent policy-update mechanics
```

That audit recommended a bounded Design-A discriminator before any manuscript claim escalation. Experiment 4 then preregistered and executed exactly that action-opportunity scope test.

This closure records how E4 changes the audit. It does not modify the publication manuscript and does not alter canonical SRT.

## 2. E4 result that closes the audit question

E4 compared the same non-terminal forced-recovery mechanism under:

```text
INDIVIDUAL scope:
  only the failed agent loses normal action choice for k steps

SHARED scope:
  one agent's failure makes both agents lose normal action choice for k steps
```

with `k = 2,5,10`, confirmatory seeds `101..130`, fixed 50-step episodes, zero explicit failure penalty, immediate `E0=6` rescue, a fixed-horizon policy-update rule, and a common 2,000-state frozen-policy endpoint.

The first and only confirmatory execution produced:

```text
mean(shared - individual), collapsed over latency = +0.0299836682
95% paired bootstrap CI                           = [+0.0119520663, +0.0538730310]
two-sided paired sign-flip p                      = 0.0001499925
```

The preregistered support rule passed. The preregistered strong-support gate `mean >= +0.10` failed.

Locked verdict:

```text
E4 = OUTCOME B — POSITIVE BUT MODEST H-SCOPE SUPPORT
```

The collapsed scope contrast was positive in 29 of 30 seeds. The effect is directionally broad but practically modest and right-skewed.

## 3. Audit hypotheses after E4

### H-SCOPE

```text
status = SUPPORTED / MODEST
```

Consequence scope is no longer merely a plausible mechanism hypothesis. Under the tested non-terminal action-opportunity mechanism, changing who bears failure-triggered loss of normal action opportunity measurably changes learned cooperation.

Allowed claim:

> Consequence scope is an empirically relevant mechanism variable in this testbed.

Not allowed:

- consequence scope fully explains E1;
- shared fate universally produces cooperation;
- the E4 effect is large;
- CSC as a whole is validated.

### H-TERM

```text
status = STILL LIVE FOR E1 MAGNITUDE
```

E4 weakens the strongest terminality-only rival, because a non-terminal scope manipulation did produce a stable policy-level difference.

But E4's effect is about `+0.030`, far smaller than the original E1 terminal-versus-restore separation. E4 therefore does not explain away terminality, return truncation, realized trajectory length, or other terminal-transition effects.

Safe inference:

> Scope contributes, but terminality-specific mechanisms remain plausible contributors to the much larger E1 effect.

### H-VICTIM

```text
status = MIXED / PARTIAL
```

During INDIVIDUAL recovery the still-active partner strongly preferred Solo to Cooperate, confirming a real unilateral post-failure exploitation window.

However, E4 failure triggers were dominated by mutual-Solo states rather than by `failed C vs partner Solo`. The stronger claim that the programme is mainly explained by exploited cooperators being selectively burdened is therefore not supported.

### H-UPDATE

```text
status = SPECIFIC E3 CONFOUND WEAKENED
```

E4 used fixed-horizon return normalization and fixed `/50` gradient scaling, with forced actions omitted only from score-function gradients. The positive scope result survived under this anti-confound rule.

Therefore E4 cannot be assigned to the specific E3 decision-count-dependent normalization/scaling mechanism. Algorithm-specific effects in general remain possible.

## 4. What the full E1-E4 sequence now supports

The evidence sequence is now:

```text
E1
terminal depletion vs cheap restore
-> large cooperation difference

E2
persistent internal metabolic impairment without direct action/time loss
-> preregistered positive generalization not supported

E3
individual-scoped forced-recovery latency
-> preregistered positive prediction not supported
-> negative ordinal learned-policy association

E4
shared vs individual scope of the same non-terminal recovery burden
-> preregistered positive scope contrast supported
-> effect modest, not large
```

The sequence supports four bounded conclusions:

1. the E1 effect is real within the original REINFORCE testbed;
2. failure manipulations that appear intuitively 'more consequential' are not interchangeable;
3. **who bears failure-triggered future action-opportunity loss matters independently** under the E4 mechanism;
4. consequence scope alone is insufficient to explain the magnitude of E1.

## 5. What the sequence still does not support

The evidence does not establish:

1. a universal one-dimensional or multidimensional law of failure;
2. a universal monotonic relationship between consequence severity and cooperation;
3. that terminality is reducible to consequence scope;
4. that shared consequence is sufficient for cooperation;
5. that persistent damage is behaviorally irrelevant in general;
6. that the full CSC B/M/H framework is experimentally validated;
7. that the agents should be called alive.

## 6. Publication-level implication

The pre-E4 audit warned that the broad title/claim `Failure Is Not One-Dimensional` exceeded the available evidence. E4 does not restore that broad formulation.

Instead, the E1-E4 sequence now justifies a more specific evidence-led framing around **failure consequence scope**:

> In this survival-coupled multi-agent testbed, learned cooperation depends not only on whether failure occurs or how recovery is delayed, but also on which agents lose future normal action opportunity when failure occurs.

A stronger but still bounded question for the revised paper is:

> **Who bears failure? How consequence scope interacts with terminality and recovery architecture in survival-coupled artificial agents.**

The publication should treat CSC as the conceptual origin of the question, not as a framework validated by these experiments.

## 7. Research stop rule

The audit does **not** recommend an immediate E5.

Reason:

- E4 answered the first discriminator proposed by the audit;
- the remaining E1 magnitude gap is scientifically real but no longer blocks a publishable bounded claim;
- additional mechanism experiments risk turning the paper into an open-ended RL decomposition programme rather than a coherent ALife article.

Further experiments should be reviewer-driven or motivated by a new independently specified question, not by a desire to raise the E4 effect toward the E1 magnitude.

## 8. Closure gate

```text
PRE-E4 AUDIT = COMPLETE / PRESERVED AS HISTORICAL ANALYSIS
E4 DESIGN-A DISCRIMINATOR = EXECUTED ONCE / VALID
E4 RESULT = OUTCOME B
H-SCOPE = DETECTABLE / MODEST SUPPORT
H-TERM = STILL LIVE FOR E1 MAGNITUDE
H-VICTIM = MIXED / NOT DOMINANTLY ESTABLISHED
H-UPDATE = SPECIFIC E3 SCALING CONFOUND WEAKENED
E5 = NOT REQUIRED BEFORE MANUSCRIPT RECONSTRUCTION
#981 = SCIENTIFIC HOLD UNTIL E1-E4 MANUSCRIPT RECONSTRUCTION
CANONICAL SRT = UNCHANGED
```

Next justified action:

```text
open a separate publication-reconstruction branch
re-center the article on E1-E4 evidence and consequence scope
then perform an independent reviewer-pressure test
```
