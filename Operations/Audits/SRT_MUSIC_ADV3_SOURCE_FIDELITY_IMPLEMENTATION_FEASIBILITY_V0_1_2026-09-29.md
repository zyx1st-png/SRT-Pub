---
id: SRT-MUSIC-ADV3-SOURCE-FIDELITY-IMPLEMENTATION-FEASIBILITY-V0-1-20260929
type: audit
status: active
canonical: false
layer: operations
epistemic_layer: os
claim_mode: source_fidelity_audit
created: 2026-09-29
updated: 2026-09-29
research_mode: U_to_TEST
root_question: Does the ADV-3A predictability x completion design remain implementable after checking the actual source paradigms and model interfaces?
comparative_claim: none
named_comparator: "Chander-Aslin local cadence adaptation; official IDyOM STM/LTM; Sears cadence expectancy; Smit cadence closure descriptions"
n_mode_triggered: false
priority: current_next_bounded_companion
dependency:
  - Operations/Audits/SRT_MUSIC_ADV3_SOURCE_OWNED_PREDICTION_TABLE_STIMULUS_LOGIC_V0_1_2026-09-29.md
  - Operations/Audits/SRT_MUSIC_E2_STRONG_BASELINE_ADVERSARIAL_PACKET_V0_1_2026-09-29.md
  - Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md
tags: [Music, ADV3, SourceFidelity, ImplementationFeasibility, Cadence, IDyOM, BayesianAdaptation, Completion]
---

# Music ADV-3 source-fidelity + implementation-feasibility audit v0.1

> Role: verify that the paper-only ADV-3 design does not ask source models or source experiments to do jobs they did not actually perform.
>
> Boundary: no experiment authorization, no preregistration, no SRT residual, no cross-domain promotion.

## 0. Executive verdict

~~~text
ADV-3A
= CONDITIONALLY IMPLEMENTABLE as a continuous crossed design;

clean categorical 2x2
= NOT YET ESTABLISHED;

key-conditioned K1/K2 version
= DEMOTED;

primary implementation
= trial-order / local-history adaptation
  x
  independently checked cadence closure;

standard IDyOM STM as session learner
= NOT VALID BY DEFAULT;

online Bayesian / local-probability learner
= REQUIRED first-line adaptation baseline;

Sears 2020 end-imminence
= EXPECTANCY comparator
!= post-event completion criterion;

experiment
= NO;

preregistration
= NO.
~~~

## 1. Chander–Aslin source fidelity

Source:
- Chander A, Aslin RN. 2023. Expectation adaptation for rare cadences in music: Item order matters in repetition priming. Cognition 240:105601. DOI 10.1016/j.cognition.2023.105601. PMCID PMC10501749.

### 1.1 What they actually manipulated

The study:
- used PACs and a modified deceptive-cadence family;
- held overall PAC/DC incidence at 50/50;
- manipulated **item order** so the local probability of DC changed through the experiment;
- used order schedules including 20/80 -> 80/20, 80/20 -> 20/80, and 50/50 -> 50/50;
- computed the current probability of a DC from all previous trials using maximum-likelihood estimation;
- collected prospective completion-confidence ratings before the cadence and retrospective expectation-match ratings after it.

Therefore the source directly supports:

~~~text
trial-by-trial expectation adaptation
to unfolding local cadence statistics.
~~~

It does **not** directly support:

~~~text
key identity
-> learned cadence probability mapping.
~~~

### 1.2 Important strength of the long-term prior

Chander–Aslin did not show that short-term statistics simply overwrite schematic PAC preference.

Their reported pattern includes:
- PACs remained favoured on average;
- DC expectedness increased faster under high local DC probability;
- PAC expectedness decreased somewhat as DC probability rose;
- prospective confidence only began to decline once the local DC probability rose to approximately 74%.

This is a direct warning against defining:

~~~text
"PAC is locally rare"
=
"PAC is absolutely low-predictability."
~~~

### 1.3 Consequence for ADV-3

The primary design should use:

~~~text
continuous current local probability / posterior expectedness
x
cadence closure type.
~~~

The four cells remain a useful visualization, but the empirical model should not require that PAC cross an arbitrary absolute probability threshold.

The hard requirement becomes:

> the same PAC-like closing event must show a predeclared, independently verified **shift in expectedness as local history changes**, while its completion / closure status remains stable.

This is stronger and more source-faithful than demanding an absolute “low-P PAC.”

## 2. IDyOM source fidelity

Official implementation coordinate:
- mtpearce/idyom
- mtpearce/idyom-tutorial, tutorial-script.lisp.

The official tutorial describes the Short-Term Model as:

~~~text
learning incrementally through each melody
from an initially empty state.
~~~

Therefore:

~~~text
standard STM
!= automatic cross-trial session-memory model.
~~~

If each cadence phrase is presented as a separate melody / item, a vanilla STM run cannot simply be assumed to carry the participant's preceding trial history.

### 2.1 Allowed uses

IDyOM remains useful for:
- long-term / corpus expectation;
- within-item melodic information content / entropy;
- combined LTM + STM where the represented stream matches the model's memory scope;
- stimulus screening under a declared encoding.

### 2.2 Not allowed without explicit implementation work

Do not write:

~~~text
IDyOM will model the Chander-style local session adaptation.
~~~

unless one of the following is specified and validated:
- trials are encoded as one continuous stream with justified boundary handling;
- memory is explicitly persisted across items;
- a modified / wrapper implementation provides session-level online updating;
- another online learner is used for the session-level probability and IDyOM is retained for long-term schematic pressure.

### 2.3 Fair baseline consequence

For ADV-3A the statistical baseline should be split:

~~~text
B_online
= online Bayesian / rolling local-probability learner
  over the actual trial sequence;

B_long
= corpus / schematic expectation
  from IDyOM LTM, tonal-statistical or related model.
~~~

A combined baseline may use both.

## 3. Sears 2020 source fidelity

Source:
- Sears DRW, Spitzer J, Caplin WE, McAdams S. Expecting the end: Continuous expectancy ratings for tonal cadences. Psychology of Music 48(3):358-375. DOI 10.1177/0305735618803676.

The dependent variable was a continuous rating of:

> how strongly the listener expected the **end of the excerpt to be imminent**.

This is highly relevant to prospective closure expectation.

It is not identical to:

~~~text
after hearing the terminal cadence,
does this now feel complete / able to stop?
~~~

Therefore:

~~~text
Sears end-imminence
= prospective expectancy comparator;

Sears end-imminence
!= direct post-event completion validation.
~~~

## 4. Completion / openness source fidelity

Smit et al. 2020 review and stimulus definitions describe:
- authentic cadences as stable / resolved;
- half cadences as unresolved / unstable;
- deceptive cadences as leaving harmonic closure relatively open.

However, their measured outcomes were arousal and valence, not a direct post-event completion scale.

Therefore cadence taxonomy can provide an **independent structural anchor**, but ADV-3 still requires a separate completion manipulation check.

Required future distinction:

~~~text
structural cadence class
!= measured felt completion;
prospective end-imminence
!= post-event completion.
~~~

## 5. Revised primary implementation — ADV-3A'

### 5.1 Trial-order schedule

Use PAC and DC items in a sequence whose local statistics vary over time while global incidence remains approximately matched.

Source-faithful schedule family:

~~~text
Schedule S1:
20% DC / 80% PAC
-> 80% DC / 20% PAC

Schedule S2:
80% DC / 20% PAC
-> 20% DC / 80% PAC

Schedule S0:
50% DC / 50% PAC
-> 50% DC / 50% PAC
~~~

Exact trial counts remain unfrozen.

### 5.2 Primary predictability variable

Do not reduce predictability to the schedule label.

Use a continuous trial-level quantity:

~~~text
q_t
= online estimated probability of the upcoming cadence class
  from the preceding trial history.
~~~

Candidate first-line implementation:
- maximum-likelihood local-history estimate, matching the Chander–Aslin descriptive analysis;
- Bayesian posterior estimate with declared prior / forgetting rule as a robustness model.

### 5.3 Primary completion variable

Use:
- cadence class as the structural factor;
- separate post-event completion / “could stop here now” manipulation check.

Do not use:
- Sears end-imminence rating as the completion measure;
- statistical expectedness as the completion definition.

### 5.4 Crossed-design criterion

The design no longer requires four perfect absolute bins.

It requires enough overlap so that:

~~~text
PAC trials occur across meaningfully different q_t values
AND
DC trials occur across meaningfully different q_t values
AND
PAC remains more closing than DC on the independent completion check.
~~~

This supports estimating:

~~~text
local expectedness effect
+
closure effect
+
their interaction / nonlinear relation
~~~

without redefining either factor from the final E2 outcome.

## 6. Revised Cell-C criterion

Old idealized criterion:

~~~text
C = absolutely low predictability + high completion.
~~~

Source-fidelity correction:

~~~text
C-separation
= PAC-like closing items encountered under a local history
  that makes them significantly less expected than the same PAC-like items
  under the opposite local history,
  while completion remains high.
~~~

Important:

~~~text
C-separation
!= PAC must become less likely than DC in absolute terms.
~~~

If PAC expectedness barely shifts under local-history manipulation, the design still fails.

## 7. Implementation-feasibility gates

### IF-1 local-history effect

Independent expectedness check must show a predeclared PAC/DC expectedness shift with local history.

If not:

~~~text
ADV-3A' = FAIL.
~~~

### IF-2 completion preservation

PAC/DC completion contrast must remain independently detectable after local adaptation.

If not:

~~~text
construct separation = FAIL.
~~~

### IF-3 no explicit contingency dependence

The local-history effect should not require participants to explicitly verbalize an experimenter-imposed rule.

If explicit strategy is necessary:

~~~text
result level
= explicit learned prediction;
not pre-object orientation evidence.
~~~

### IF-4 baseline memory scope

Every comparator must receive the information its theory / implementation is allowed to use.

Do not compare:
- a session-aware candidate model
against
- a reset-at-each-item baseline

and call the difference an E2 residual.

### IF-5 completion validity

Post-event completion must be validated independently from prospective end-imminence.

## 8. Fair baseline architecture after source-fidelity correction

~~~text
B*
=
B_online
+ B_long
+ B_close
+ B_tension
+ B_boundary.
~~~

Where:

~~~text
B_online
= trial-history Bayesian / local-probability learner;

B_long
= IDyOM LTM / corpus tonal statistics / schematic expectation;

B_close
= cadence-class / tonal-stability / implication-closure predictors;

B_tension
= Farbood / TenseMusic / tonal-tension family;

B_boundary
= phrase / event-segmentation predictor.
~~~

The exact ensemble architecture is not frozen.

Complexity / leakage / held-out controls remain mandatory.

## 9. Current feasibility verdict

The source-fidelity audit changes the route from:

~~~text
"Can a clean four-bin 2x2 be manufactured?"
~~~

to:

~~~text
"Can online expectedness be moved independently enough
from cadence closure
to estimate their distinct and joint effects?"
~~~

This is a meaningful contraction, not a failure.

Current verdict:

~~~text
ADV-3A'
= CONDITIONALLY VIABLE PAPER DESIGN;

absolute 2x2
= NOT REQUIRED / NOT ESTABLISHED;

session adaptation
= EMPIRICALLY PLAUSIBLE;

full prior reversal
= NOT ESTABLISHED;

completion manipulation
= REQUIRES independent validation;

SRT residual
= NONE;

experiment
= NO;

preregistration
= NO.
~~~

## 10. Next allowed move

Paper-only synthetic feasibility:

1. instantiate S1 / S2 / S0 schedules;
2. compute q_t with an online local-history / Bayesian learner;
3. test whether PAC and DC each occupy a useful range of q_t;
4. test sensitivity to stronger vs weaker schematic priors;
5. predefine a minimum separation criterion before any human data;
6. do not simulate completion from the same expectedness model.

Only after that:

~~~text
consider whether an independent FR-ADV / prereg-preparation package is warranted.
~~~
