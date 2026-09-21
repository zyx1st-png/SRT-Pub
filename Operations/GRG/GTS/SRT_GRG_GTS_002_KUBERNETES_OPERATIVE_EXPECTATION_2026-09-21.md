---
id: SRT-GRG-GTS-002-KUBERNETES-OPERATIVE-EXPECTATION-20260921
type: grg_transformation_record
status: active
date: 2026-09-21
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Templates/SRT_GRG_GENERATIVE_TRANSFORMATION_RECORD_TEMPLATE_V0_2.md
  - Operations/GRG/Transfers/SRT_GRG_TR_X3B_01_KUBERNETES_NETWORKPOLICY_2026-09-21.md
  - Operations/GRG/NegativeControls/SRT_GRG_NEG_X3B_FORMAL_DECOUPLING_2026-09-21.md
  - Materials/2026/SRC_2026_09_21_Kubernetes_NetworkPolicy_Enforcement.md
tags: [GRG, GTS, X3b, Kubernetes, NetworkPolicy, M3, Absorbed]
---

# GTS-002 — Kubernetes NetworkPolicy: represented rule to operative connectivity constraint

## A. Identity

~~~text
GTS id = GTS-002
domain = software / distributed systems
surface = Kubernetes NetworkPolicy
legacy relation route = X3a / X3b
role = positive structural recurrence + M4-E0 absorption calibration
~~~

## B. Research question / objectification

Research question:

> When does a represented access rule become an operative generative condition on participant connectivity rather than remain a merely articulated specification?

Stabilized objectification:

~~~text
unit = Kubernetes pod / workload connectivity relation
rule object = NetworkPolicy resource
implementation = network plugin / controller support
outcome = allowed / denied traffic possibilities
grain = declared cluster/network-policy scope
~~~

Strongest reasonable horizontal baseline:

~~~text
ordinary Kubernetes networking practice already distinguishes
policy specification from actual enforcement implementation
and directly models changed connectivity.
~~~

What is reopened:

~~~text
the GRG question is not whether Kubernetes has policy enforcement;
it is whether the same generative burden recurs across objectifications:

represented expectation
+ operative embodiment
-> changed participant possibility relation.
~~~

## C. Source-native account

Kubernetes source-native topology:

~~~text
NetworkPolicy resource / rules
-> supporting network implementation
-> packet / connection filtering
-> changed pod connectivity possibilities
~~~

Near-miss:

~~~text
policy object present
+ no enforcing implementation
-> no NetworkPolicy traffic effect
~~~

The target domain owns this distinction explicitly.

## D. Generative-condition declaration

Candidate generative condition:

~~~text
operative enforcement relation coupling
policy specification to network implementation.
~~~

Why frame-like for this question:

~~~text
when enforcement is operative,
the reachable connectivity relation among pods changes.

when enforcement is absent,
the same represented policy does not change that reachability.
~~~

Expanded-state representability:

~~~text
YES.
A complete Kubernetes networking model can encode rule state,
plugin/controller state and connectivity state directly.
~~~

Vertical reading, if useful:

~~~text
the objectified policy document is not taken as the operative condition by default;
the formation of an operative rule-regime is separately paid.
~~~

## E. Bounded transformation

~~~text
C_t =
represented NetworkPolicy specification
+ cluster/network implementation context

G_t =
operative implementation/enforcement of the represented rule

C_(t+1) =
changed connectivity reachability:
some traffic relations become allowed / denied under the policy regime
~~~

Near-control:

~~~text
same/similar policy object
without enforcing implementation
-> no corresponding traffic constraint.
~~~

## F. History-input / reconstruction-output

History-input:

~~~text
not primary.
No historical inheritance claim is required.
~~~

Reconstruction-output:

~~~text
PAID at the declared local grain:

operative enforcement
-> changes the later connectivity / accessibility relation.
~~~

This is a current-condition reconstruction, not X4c inheritance.

## G. Locus / positionality

~~~text
local-locus formation = NOT REQUIRED
operative positionality = PARTIAL / SOURCE-LOCAL ONLY
~~~

Pods have different allowed/denied accessibility under the policy, but no canonical Selection-position inference is licensed.

## H. Composition

A minimal sequential dependency is source-native:

~~~text
represented rule
-> enforcement implementation
-> changed connectivity relation
~~~

Composition burden:

~~~text
the represented rule alone is insufficient;
the implementation output is load-bearing for the later accessibility constraint.
~~~

## I. Generative Prediction — P_G

Source-native discrimination:

~~~text
IF NetworkPolicy is represented
BUT no supporting implementation enforces it,
THEN the policy should not produce the claimed traffic effect.

IF implementation enforces it,
THEN allowed / denied connectivity should change according to the source-native policy semantics.
~~~

This discrimination is real and testable.

But it is NOT a new GRG prediction in Kubernetes.

## J. Generative Order admission

Order id:

~~~text
O-K8S-NP-OPERATIVE
~~~

GO1 formation / operation:

~~~text
PASS when policy + supporting enforcement implementation
are actually operative.
~~~

GO2 structural articulation:

~~~text
PASS:
represented policy
+ enforcement channel
+ changed allowed / denied connectivity relation.
~~~

GO3 generative efficacy:

~~~text
PASS:
removing / lacking enforcement changes whether the policy constrains connectivity.
~~~

GO4 scope:

~~~text
relation = pod/workload network accessibility
locus / position = policy-relevant participant endpoints
scale = declared cluster/network-policy scope
horizon = while the policy + enforcing implementation remain operative
~~~

GO5 failure / dissolution:

~~~text
policy unsupported / enforcement implementation absent or decoupled
-> claimed operative order fails / is hollow.
~~~

Order admission:

~~~text
PASS for the source-native operative NetworkPolicy regime.
~~~

## K. Generative Expectation — E_G

Primary counterfactual transformation:

~~~text
remove / decouple enforcement
while represented policy remains.
~~~

Relative to:

~~~text
O-K8S-NP-OPERATIVE
~~~

classification:

~~~text
E_G = HOLLOW / DESTROY the operative policy order,
depending on whether some operative channel remains.
~~~

Reason:

~~~text
the representation remains,
but the dependency that makes it alter participant connectivity is removed.
~~~

This E_G is functional/order-relative.

It does not imply moral legitimacy of the policy.

## L. Cross-objectification gain

Independent realizations:

~~~text
A. institutional / irrigation:
rules-in-use + monitoring / sanctions
-> actual participant option constraints

B. Internet standards:
implemented protocol/interface
-> interoperability possibilities

C. Kubernetes:
represented policy + enforcement implementation
-> connectivity possibilities
~~~

Shared GTS burden:

~~~text
represented/shared expectation
!= operative constraint

operative embodiment / implementation
-> participant possibility relation changes.
~~~

XG1 independent source-native grounding:

~~~text
PASS
~~~

XG2 shared burden survives mechanism change:

~~~text
PASS
~~~

XG3 admission / exclusion / failure constraints survive:

~~~text
PASS
negative control = formal structure decoupled from activity.
~~~

XG4 no flattening:

~~~text
PASS:
Kubernetes networking mechanism remains source-native;
GRG does not own CNI/controller semantics.
~~~

XG5 prospective discrimination:

~~~text
candidate distinction = specification vs enforcement.
~~~

M4-E0 absorption check:

~~~text
ABSORBED.
Kubernetes ordinary mature practice explicitly owns
the same specification-versus-enforcement distinction.
~~~

Cross-objectification verdict:

~~~text
STRUCTURAL-PASS / M3-side burden
PROSPECTIVE-PASS = NO
M4 = NO / ABSORBED
~~~

## M. Measurement / proxy bridge

~~~text
policy object presence
!= operative enforcement

observable connectivity effect
is part of the source-native implementation evidence.
~~~

No speculative hidden bridge is required.

## N. Mature-neighbor pressure

Source-native Kubernetes practice is itself the strongest target-domain comparator.

Outcome:

~~~text
INHERIT target-domain distinction
DOMAIN-OWNED mechanism
ABSORB prospective novelty claim
~~~

## O. Evidence / maturity

~~~text
source fidelity = PASS
negative control = PASS
semantic invariance across domains = PASS
legacy X3b maturity = M3 PASS
M4 = NO / ABSORBED
scientific distinctiveness = NOT ESTABLISHED
~~~

## P. Revision

No relation retirement is required.

Revision pressure:

~~~text
keep operative-vs-articulated distinction;
do not mistake structural recurrence for target-domain novelty.
~~~

## Q. GTS reconciliation verdict

Compared with the old X3b relation/transfer records, GTS adds four useful constraints:

1. it forces the strongest horizontal / mature-practice comparator into the same record;
2. GO1-GO5 distinguish an actually operative order from a formal rule object;
3. E_G can classify decoupling as hollowing without moralizing;
4. the same record carries both M3 structural gain and M4-E0 absorption instead of treating them as competing verdicts.

~~~text
GTS reconciliation = PRODUCTIVE
legacy X3b / transfer provenance = RETAIN
M4 = NO / ABSORBED
canonical consequence = NONE
~~~
