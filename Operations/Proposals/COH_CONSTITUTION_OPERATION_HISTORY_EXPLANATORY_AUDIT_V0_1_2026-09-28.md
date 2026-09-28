---
id: COH-EXPLANATORY-AUDIT-V0-1-20260928
type: proposal
status: active
canonical: false
layer: operations
epistemic_layer: os
claim_mode: method_proposal
created: 2026-09-28
updated: 2026-09-28
version: v0_1
tags: [Method, CrossDomain, Constitution, Operation, History, Explanation, Audit]
---

# Constitution–Operation–History Explanatory Audit v0.1

> A theory-neutral method for separating different explanatory burdens before comparing models, mechanisms, or domains.
>
> It does not assume any particular metaphysics and does not require SRT vocabulary.

## 0. Core question

Do not ask:

~~~text
What kind of thing is this concept?
~~~

Ask:

~~~text
Under the declared cut, scale and explanandum,
what explanatory job is this construct actually doing?
~~~

Every classification is indexed to:

~~~text
construct
+ explanandum
+ target cut
+ scale
+ timescale
+ source context.
~~~

## 1. Three primary explanatory burdens

### C — Constitution

Explains how an operative distinction, object, boundary, variable, candidate set, comparison relation or admissible state space becomes available or determinate.

Constitution must be split into two strengths:

~~~text
C-R = RELATIVE CONSTITUTION
      a higher-level object / boundary / pattern is generated
      within an already declared lower-level framework.

C-F = FRAMEWORK CONSTITUTION
      the variables / candidate dimensions / boundaries / comparison grammar
      used by the framework itself are generated or reorganized.
~~~

Hard guard:

~~~text
emergence of a higher-level object
!= automatically
generation of the framework's own primitive variables.
~~~

### O — Operation

Explains how a system works once the operative distinctions and state space are sufficiently declared.

Operation has at least three subtypes:

~~~text
O-S = current state / state estimation;
O-T = transition rule / dynamics / control relation;
O-G = current generator / grammar determining
      what distinctions, candidates or representations can presently be produced.
~~~

O-G can be deep and generative without becoming C-F automatically.

### H — Historical conditioning

Explains how a previously achieved organization changes later possibilities, transitions, costs, constraints, accessibility or response dispositions.

Require:

~~~text
prior organization
+ later participant / later transition
+ demonstrated later-effective difference.
~~~

Hard guard:

~~~text
past != historical conditioning;
stored != historical conditioning;
persistent != historical conditioning;
available as information != historical conditioning.
~~~

## 2. Orthogonal axis — Evidence / Access

Some items are not best treated as explanatory constructs at all.

Record separately:

~~~text
E-NONE       = not being used as evidence/access;
E-TRACE      = retained trace / record;
E-PROBE      = perturbation or measurement probe;
E-READOUT    = current observable readout;
E-RECON      = evidence used to reconstruct a latent process;
E-CARRIER    = evidence about a carrier of later-effective history.
~~~

This axis prevents mistakes such as:

~~~text
archive exists -> H;
observable item -> O;
hidden item -> C.
~~~

## 3. Step 0 — declare the cut

No verdict is valid until the target cut is explicit enough to audit.

Record:

~~~text
UNIT
BOUNDARY
GRAIN
EQUIVALENCE
STATE / CANDIDATE SPACE
COMPARISON RULE
TIMESCALE
OBSERVER / ACCESS RELATION
~~~

If the cut is intentionally underspecified, state that fact and lower confidence.

## 4. Nested-cut rule

The same physical or causal event can carry different burdens at different scales.

Example form:

~~~text
lower-scale declared variables -> ordinary operation;
same process -> formation of a higher-scale object.
~~~

Therefore:

~~~text
same event can be O at scale 1
and C-R at scale 2
without contradiction.
~~~

Never assign a scale-free permanent label to a named phenomenon.

## 5. Designed-framework rule

Some systems receive their framework from an external designer.

Distinguish:

~~~text
internal operation inside a supplied framework;
endogenous framework reconstitution;
external design / specification of the framework.
~~~

A software system executing a protocol does not thereby explain the constitution of the protocol's variable space.

## 6. Admission questions

### Q1 — presupposition

Which units, variables, boundaries and comparison relations must already exist for the construct to be defined?

### Q2 — constitution

Does the construct make any of those presupposed distinctions themselves part of the explanandum?

### Q3 — relative vs framework constitution

If something new forms, is it:

~~~text
new object/pattern inside a fixed framework -> C-R
or
change to the framework's own variables/candidate dimensions/grammar -> C-F?
~~~

### Q4 — current operation

Is the construct primarily about current state, transition dynamics or current generative grammar?

### Q5 — historical conditioning

Does a prior achieved organization materially alter a later transition or possibility structure?

### Q6 — persistence control

Could the item persist or remain readable while having no effect on later transitions?

If YES, persistence alone is insufficient for H.

### Q7 — removal test

Remove the higher-level object labels and current candidate menu.

Ask:

~~~text
Does the explanatory burden still concern how those distinctions arise? -> C pressure
Does the construct lose its target because the framework was required? -> O pressure
Does prior structure still alter later response? -> H pressure
~~~

### Q8 — current-state-matched history test

Can two systems have similar current readout but respond differently later because of different histories?

If YES, that is strong H evidence.

### Q9 — evidence-role test

Is the item itself explanatory, or merely a trace/readout/probe used to infer another construct?

### Q10 — falsifier

State what source evidence would change the classification.

## 7. Allowed verdicts

Primary explanatory verdicts:

~~~text
C-R
C-F
C-R<->O
C-F<->O
O-S
O-T
O-G
O<->H
H
MIXED
NOT-APPLICABLE
UNDETERMINED
~~~

`NOT-APPLICABLE` means the item is being used only as evidence/access or bookkeeping, not as an explanatory construct in the current question.

`UNDETERMINED` means the evidence is insufficient.

Do not confuse them.

## 8. Comparison rule

Before claiming that one framework absorbs, replaces, duplicates or outperforms another, compare the same burden.

Examples:

~~~text
O-T success does not automatically answer C-F;
H evidence does not automatically answer current O-T;
C-R emergence does not automatically answer C-F framework genesis.
~~~

Cross-burden comparisons are allowed only when the bridge itself is the target.

## 9. Frequent category errors

~~~text
generative model -> C-F                [invalid shortcut]
hidden state -> C                     [invalid shortcut]
phase transition -> C-F               [invalid shortcut]
self-organization -> C-F              [invalid shortcut]
memory trace -> H                     [invalid shortcut]
old rule/document -> H                [invalid shortcut]
current stability -> H                [invalid shortcut]
observable output -> O                [invalid shortcut]
new higher-level pattern -> no lower framework assumed [invalid shortcut]
~~~

## 10. Minimal examples

~~~text
Bayesian inference over fixed hidden states -> O-S / O-T
parameter learning within fixed model family -> O-T or O-G
structure learning adding/removing modeled relations -> O-G, possibly C-R
representation-basis redefinition -> C-F candidate
Turing pattern formation from fixed PDE variables -> C-R at pattern scale, O-T at field scale
metaplasticity where prior priming changes later response -> H
archived transcript used to infer latent process -> NOT-APPLICABLE + E-RECON
binding precedent currently applied -> O-T
old precedent constraining successor court -> H
new legal category formed in case of first impression -> C-R or C-F depending declared legal framework
~~~

## 11. Confidence

~~~text
HIGH   = source-native role explicit; cut and scale clear; multiple questions converge
MEDIUM = role supported but nested cut / bridge interpretation remains
LOW    = sparse source support or unresolved cut
~~~

Confidence applies to classification, not truth of the theory.

## 12. Promotion requirement

Do not treat v0.1 as a general method until:

~~~text
1. blind cross-domain calibration is run;
2. domains include at least one physical, biological, cognitive/neural, institutional and engineered case;
3. producing-model labels remain hidden until blind verdicts freeze;
4. disagreements are classified;
5. cases that only restate source-native distinctions are separated from cases where the audit adds new clarity;
6. the method's failure cases are recorded.
~~~

## 13. Current status

~~~text
theory-neutral proposal = ACTIVE
cross-domain seed = PENDING
independent blind validation = PENDING
general-method claim = NOT ESTABLISHED
~~~