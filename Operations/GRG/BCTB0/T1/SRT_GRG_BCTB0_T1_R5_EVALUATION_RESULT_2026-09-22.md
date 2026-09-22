---
id: SRT-GRG-BCTB0-T1-R5-EVALUATION-RESULT-20260922
type: calibration_evaluation_result
status: complete
date: 2026-09-22
canonical: false
ai_do_not_use_for_definition: true
---

# BCTB-0 T1 R5 evaluator result

## 0. Verdict

~~~text
fold = T1
generator freeze = 12/12 COMPLETE
formal identity probe = AMBIGUOUS
blind integrity = COMPROMISED
valid core fold = NO
absolute historical-transfer credit = NO
allowed use = COMPROMISED-DIAGNOSTIC

historical A/X/F recovery = YES
GRG residual candidate = NO
residual classification = BASELINE-SHARED
canonical consequence = NONE
M4 credit = NONE
M5 credit = NONE
scientific-distinctiveness credit = NONE
~~~

No sample was regenerated after another arm/sample was observed.

## 1. Frozen generator set

~~~text
G1 G2 G3 = FROZEN
S1 S2 S3 = FROZEN
A1 A2 A3 = FROZEN
C1 C2 C3 = FROZEN
~~~

All generator outputs were frozen before evaluator unblind.

## 2. Blind-integrity disposition

Formal capsule-only probe:

~~~text
AMBIGUOUS: multiple network-policy systems fit these facts; no unique named target is identified.
~~~

Frozen consequence:

~~~text
blind integrity = COMPROMISED
absolute historical-transfer credit = NO
valid core fold = NO
symmetric between-arm comparison = ALLOWED
~~~

Generator self-report after source-pack exposure:

~~~text
G: YES 2/3, OPEN 1/3
S: YES 2/3, OPEN 1/3
A: YES 3/3, OPEN 0/3
C: YES 1/3, OPEN 2/3

overall:
YES = 8/12
OPEN = 4/12
NO = 0/12
~~~

This does not change the already-frozen COMPROMISED classification.

## 3. Historical target unblind

Historical target:

~~~text
Kubernetes NetworkPolicy
~~~

Historical source-native topology:

~~~text
NetworkPolicy object / rules
-> supporting network implementation
-> packet / connection filtering
-> changed pod connectivity possibilities
~~~

Historical mapping:

~~~text
policy object / spec
-> X3a articulated expectation

network plugin/controller enforcement
-> X3b operative expectation embodiment

changed allowed / denied connections
-> changed participant accessibility / action possibilities
~~~

Historical near-miss:

~~~text
policy object / API present
+
no enforcing implementation
->
no NetworkPolicy traffic effect
~~~

Historical objectification field in the cross-domain burden matrix:

~~~text
not opened
~~~

Historical programme disposition:

~~~text
semantic match = PASS
source-native evidence = PASS
negative-control structure = PASS
M3 = PASS
M4 = NO / ABSORBED
canonical consequence = NONE
~~~

Evaluator sources:

- `Operations/GRG/Transfers/SRT_GRG_TR_X3B_01_KUBERNETES_NETWORKPOLICY_2026-09-21.md`
- `Materials/2026/SRC_2026_09_21_Kubernetes_NetworkPolicy_Enforcement.md`
- `Operations/Audits/SRT_GRG_M3_M4_CROSSDOMAIN_TRANSFER_ABSORPTION_PASS1_2026-09-21.md`
- `Operations/GRG/SRT_GRG_CROSS_DOMAIN_BURDEN_MATRIX_V0_1.md`
- `Operations/GRG/GTS/SRT_GRG_GTS_002_KUBERNETES_OPERATIVE_EXPECTATION_2026-09-21.md`

## 4. Frozen majority scoring

Majority threshold:

~~~text
2 of 3
~~~

### 4.1 A — admission burden

Materially equivalent candidate:

~~~text
formal / represented declaration alone is weaker;
operative technical embodiment must convert the declared relation
into changed communication accessibility.
~~~

Arm result:

~~~text
G = 3/3
S = 3/3
A = 3/3
C = 3/3
~~~

Historical match:

~~~text
YES
~~~

Residual disposition:

~~~text
BASELINE-SHARED
~~~

### 4.2 X — exclusion / nearest false positive

Materially equivalent exclusion:

~~~text
policy / declaration / selector structure present
but enforcement absent, bypassed, unsupported or decoupled
from actual communication.
~~~

Arm result:

~~~text
G = 3/3
S = 3/3
A = 3/3
C = 3/3
~~~

Historical match:

~~~text
YES
~~~

Residual disposition:

~~~text
BASELINE-SHARED
~~~

### 4.3 F — failure / narrowing

Materially equivalent failure:

~~~text
remove declaration-to-enforcement coupling
-> stronger operative mapping fails or narrows
-> articulated / represented expectation remains.
~~~

Arm result:

~~~text
G = 3/3
S = 3/3
A = 3/3
C = 3/3
~~~

Historical match:

~~~text
YES
~~~

Residual disposition:

~~~text
BASELINE-SHARED
~~~

### 4.4 O — objectification

Opened:

~~~text
G = 3/3
S = 2/3
A = 3/3
C = 2/3
~~~

Therefore:

~~~text
G majority = YES
baseline majority = YES in S / A / C
residual disposition = BASELINE-SHARED
~~~

But the historical target record has:

~~~text
O = not opened
~~~

Therefore the generated O result is not historical transfer success.

Disposition:

~~~text
BASELINE-SHARED OVER-OPENING
~~~

It earns no residual or historical correctness credit.

## 5. Grammar-revision-pressure output

Observed sample majorities:

~~~text
G: NONE = 3/3
S: NONE = 2/3
A: NONE = 2/3
C: NARROW = 2/3
~~~

This field does not produce a G-only stable constraint.

No GRG residual follows from it.

## 6. Frozen residual-rule application

Frozen rule:

~~~text
G majority + any baseline majority
-> BASELINE-SHARED

G majority + no baseline majority
-> GRG-RESIDUAL-CANDIDATE

not G majority
-> NO STABLE GRG CANDIDATE
~~~

Application:

~~~text
A = G majority + baseline majority -> BASELINE-SHARED
X = G majority + baseline majority -> BASELINE-SHARED
F = G majority + baseline majority -> BASELINE-SHARED
O = G majority + baseline majority -> BASELINE-SHARED,
    plus historical over-opening
~~~

Final residual verdict:

~~~text
GRG-RESIDUAL-CANDIDATE = NONE
T1 residual classification = BASELINE-SHARED
~~~

## 7. P_POST — evidence-generative provenance

Historical Kubernetes evidence is source-native.

For the historical record:

~~~text
O_R = policy / enforcement / connectivity cut

independently evidenced O_W =
YES, SOURCE-NATIVE

tested GRG intervention involved in generating evidence? =
NO

alternative-generation / near-miss =
policy-without-enforcement is source-native;
GRG did not generate it
~~~

However BCTB-0 T1 is retrospective calibration.

Therefore:

~~~text
P_POST historical transfer credit = NONE
construction != discovery
post-deployment conformity != independent confirmation
Order Admission != Grammar Validation
~~~

The generator packets can be used to compare arm behavior only.

They cannot retroactively create prospective transfer credit.

## 8. Interpretation

T1 demonstrates that the historically correct A/X/F distinction is recoverable from the frozen capsule plus historical source material.

It does not demonstrate that the labelled GRG arm uniquely generates that distinction.

The same material burden is stable under:

~~~text
structured de-labelled reasoning
structure-mapping / analogy reasoning
causal-transfer / invariance reasoning
~~~

Therefore the diagnostic result is:

~~~text
the T1 distinction is baseline-accessible under the frozen information budget.
~~~

This is an informative calibration result.

It should not be repaired by changing the capsule, regenerating samples, weakening baselines, or redefining material equivalence after seeing the result.

## 9. Programme consequence

~~~text
T1 = RETAIN AS COMPROMISED-DIAGNOSTIC / BASELINE-SHARED

valid-core-fold count contribution = 0
absolute historical-transfer credit = 0
GRG residual = NONE
M4 = NONE
M5 = NONE
scientific distinctiveness = NOT ESTABLISHED
canonical consequence = NONE
~~~

Next work should preserve T1 unchanged and move to the next independently frozen fold rather than tuning T1 to produce a residual.
