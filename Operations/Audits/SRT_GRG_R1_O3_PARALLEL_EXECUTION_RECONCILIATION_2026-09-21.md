---
id: SRT-GRG-R1-O3-PARALLEL-EXECUTION-RECONCILIATION-20260921
type: audit
status: active
date: 2026-09-21
layer: operations
epistemic_layer: os
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Audits/SRT_GRG_R1_O3_CAUSAL_MEDIATION_RESULT_2026-09-21.md
  - Operations/Audits/SRT_GRG_R1_O3_V0_3_CAUSAL_MEDIATION_RESULT_2026-09-21.md
  - Operations/Audits/SRT_GRG_R1_O3_V0_1_PREEXECUTION_VALIDITY_AUDIT_2026-09-21.md
tags: [GRG, GRGR1, O3, Reconciliation, ParallelExecution, Provenance, NullReplication]
---

# GRG-R1 O3 parallel-execution reconciliation

## 0. Purpose

Two O3 workstreams advanced in parallel from different repository baselines.

They converged on the same primary verdict but left one provenance conflict:

~~~text
trunk workstream:
  O3 v0.1 one-time spectral transplant = EXECUTED / O3-CAUSAL-NULL

parallel #1001 workstream:
  stale-branch pre-execution audit stated v0.1 had not executed
~~~

The second statement was locally true only relative to what that stale branch had seen when the audit was written. It is false as a global trunk execution claim after reconciliation.

This audit resolves the execution history without deleting either record.

## 1. Authoritative first O3 execution

The first completed O3 run is owned by:

~~~text
Experiments/grg_r1_o3_causal_mediation/O3_CAUSAL_MEDIATION_PROTOCOL_v0_1.md

Operations/Audits/
SRT_GRG_R1_O3_CAUSAL_MEDIATION_RESULT_2026-09-21.md
~~~

Design:

~~~text
fresh S/D donors
-> history-associated recurrent eigenvalue scaffold

fresh naive recipients
-> one-time pre-training S scaffold / D scaffold / intact
-> common source-domain learning
~~~

Primary result:

~~~text
O3-CAUSAL-NULL

median C_SD = 0.001575
median C_S0 = 0.002794

mean C_SD = -0.000030
mean C_S0 = 0.004394

95% CI mean C_SD = [-0.003182, 0.003168]
95% CI mean C_S0 = [-0.000015, 0.008896]
~~~

Interpretation already landed on trunk:

~~~text
O1 spectral imprint PASS
does not entail
O3 causal mediation PASS.
~~~

## 2. Status of the stale-branch v0.1 pre-execution audit

The later file:

~~~text
Operations/Audits/
SRT_GRG_R1_O3_V0_1_PREEXECUTION_VALIDITY_AUDIT_2026-09-21.md
~~~

was created on a parallel branch that had not yet incorporated the already-completed trunk O3 execution.

Its global execution-history statements are therefore superseded:

~~~text
"v0.1 execution = DO NOT RUN"
"SUPERSEDED BEFORE OUTCOME GENERATION"
"No O3 recipient outcome was generated"
~~~

Do not use those statements to erase or invalidate the authoritative trunk v0.1 result.

The design criticisms in that audit remain useful as retrospective limitations:

- extraction/transplant eigen-rank identity was weaker than intended;
- complex-eigenvalue reconstruction required taking the real part;
- S and D interventions were not parameter-distance matched.

Those points motivate a stricter robustness design. They do not mean the first execution did not occur.

## 3. What #1001 actually adds

PR #1001 should be read as a stricter independent robustness execution, not as the first O3 execution.

Its final valid protocol is:

~~~text
Experiments/grg_r1_o3_causal_mediation/
O3_CAUSAL_MEDIATION_PROTOCOL_v0_3.md
~~~

Key changes relative to the first trunk run:

~~~text
real singular-spectrum intervention
+
repeated resets through early learning
+
fresh recipients 400..411
+
equal-magnitude D-history spectral-direction control
+
baseline-centered learning-gain AUC
+
source/base domain only
~~~

The repeated-reset structure is closer to the maintenance burden exposed by the Bowler source-fidelity audit, while the D-history direction provides a materially stronger geometry control.

## 4. Second O3 result

Owner:

~~~text
Operations/Audits/
SRT_GRG_R1_O3_V0_3_CAUSAL_MEDIATION_RESULT_2026-09-21.md
~~~

Result:

~~~text
O3-CAUSAL-NULL

valid recipients = 12/12

median C_SD = -0.002745
median C_SI =  0.010806

mean C_SD = -0.006542
mean C_SI =  0.014748

95% CI mean C_SD = [-0.038720, 0.016612]
95% CI mean C_SI = [-0.017672, 0.051086]
~~~

Parameter-distance matching succeeded to numerical tolerance:

~~~text
max singular-displacement mismatch = 1.78e-15
max recurrent Frobenius mismatch = 9.54e-7
~~~

Thus the stricter control does not rescue S-history-specific causal mediation.

## 5. Joint interpretation

The two executions are not numerically identical replications and should not be pooled as if they shared one preregistration.

They are better classified as:

~~~text
O3-A:
one-time S-vs-D eigen-scaffold transplant
-> NULL

O3-B / robustness:
maintained repeated S scaffold
vs equal-magnitude D-history singular direction
-> NULL
~~~

Their common directional conclusion is robust:

~~~text
history-associated recurrent spectral structure
can be reproducibly identified,

but the tested S-history spectral scaffold/direction
does not show stable specific causal superiority
over credible alternative-history controls
on the source-domain learning outcome.
~~~

Therefore:

~~~text
toy RNN spectral family:
R1a retained imprint = PASS
R1b maintained scaffold = experimentally manipulable
R1c history-specific causal re-entry = NOT PAID / NULL
R1d prospective transfer = BLOCKED
~~~

## 6. Stronger STOP condition

The second NULL materially strengthens the existing stop rule.

Do not now tune:

- top-k mode count;
- eigenvalue / singular-value ranking;
- recipient task;
- reset frequency;
- history centroids;
- thresholds;
- new transfer target

to seek a positive RNN spectral result.

A future RNN R1c route would require a materially different source-native causal object and a new independent rationale.

## 7. Bowler boundary

Neither toy NULL refutes Bowler et al.

Bowler remains source-native positive pressure for:

~~~text
structured experience
-> recurrent operator organization
-> maintained early-training spectral scaffold
-> altered later learning regime.
~~~

The toy results instead block the shortcut:

~~~text
Bowler has a positive spectral intervention
therefore
any history-classifiable spectral scaffold in a toy RNN
is GRG-R1 causal O.
~~~

That inference is not licensed.

## 8. HKB parallel route

Live main independently selected HKB human bimanual coordination dynamics as the next non-RNN R1c candidate.

Current HKB state:

~~~text
source close-read = PASS
protocol reconstruction = PASS
measurement / normalization guard = PASS / revised
public raw trajectory access = NO-GO / NOT LOCATED
current authorized raw-data route = NOT ESTABLISHED
existing-data access request package = PREPARED
request actually sent = NO
new human experiment = NO
simulation-as-confirmation = NO
R1d / O4 = BLOCKED
~~~

The RNN O3 robustness NULL neither supports nor refutes HKB.

HKB existing-data access remains the live programme gate.

## 9. Final reconciliation

~~~text
authoritative first O3 execution = trunk v0.1 NULL
parallel stale-branch "v0.1 not executed" claim = SUPERSEDED
stale audit design criticisms = RETAIN AS RETROSPECTIVE LIMITATIONS

#1001 v0.3 = independent stricter robustness O3 NULL

RNN spectral R1c = STOP
RNN O4 = BLOCKED

HKB existing-data access = LIVE NEXT GATE

canonical edit = NO
new Level = NO
scientific distinctiveness = NOT ESTABLISHED
winner-style strongest-neighbor audit = DO NOT REOPEN
~~~
