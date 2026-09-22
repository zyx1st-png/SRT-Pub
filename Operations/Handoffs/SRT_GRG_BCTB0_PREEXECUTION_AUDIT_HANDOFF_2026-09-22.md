---
id: SRT-GRG-BCTB0-PREEXECUTION-AUDIT-HANDOFF-20260922
type: handoff
status: active
date: 2026-09-22
layer: operations
epistemic_layer: os
claim_mode: governance
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Proposals/SRT_GRG_BCTB0_TEMPORAL_REPLAY_CALIBRATION_CHARTER_V0_1_2026-09-22.md
tags: [GRG, BCTB0, PreExecution, Audit, Handoff, Blindness, InputIsolation]
---

# GRG BCTB-0 pre-execution audit handoff

## 0. Role

This handoff is the only BCTB-0 document the fresh pre-execution input-auditor should read before receiving the candidate T1 inputs.

The auditor must NOT read:

- GitHub PR metadata / PR body / PR discussion for #1027 or any other PR used to locate refs;
- branch-discovery or PR-lookup output;
- the full BCTB-0 charter;
- later fold descriptions;
- post-cut target SourceCards;
- post-cut target audits/results;
- later GRG revisions;
- PR discussion that names the hidden target;
- repository search results for the fold.

Reason:

~~~text
the full charter contains target identities and later evaluator-only metadata.
~~~

The input-auditor role is intentionally narrower than the charter-designer / evaluator role.

## 1. Audit object

Fold label:

~~~text
T1
~~~

Historical cut:

~~~text
9900f425369b8840eac9220e567a60b811c52b27
~~~

The auditor is not told the hidden target identity.

Use the refs below directly. Do not resolve them through PR metadata.

R3 handoff ref:

`research/grg-bctb0-temporal-replay-20260922`

Candidate-input ref:

`experiments/grg-bctb0-t1-preexec-package-20260922`

The auditor receives only the following six candidate inputs from the candidate-input ref:

1. manifest  
   `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_MANIFEST_2026-09-22.md`

2. exact historical raw source bundle  
   `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_RAW_2026-09-22.md`

3. proposed masked capsule  
   `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_MASKED_CAPSULE_2026-09-22.md`

4. deterministic de-labelling transform and mapping table  
   `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_DELABEL_TRANSFORM_2026-09-22.md`

5. transformed de-labelled source bundle  
   `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_DELABELED_2026-09-22.md`

6. proposed model / inference / sampling execution plan  
   `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_EXECUTION_PLAN_2026-09-22.md`

No other repository path is authorized.

If any of these six files is absent:

~~~text
affected audit item = REVISE
EXECUTION READINESS = BLOCKED
~~~

Do not search for a substitute.

No target result is supplied.

## 2. What the auditor must NOT infer from missing information

Do not assume that:

- the hidden target is novel;
- the hidden target is a positive case;
- a GRG mapping must exist;
- the de-labelled arm is expected to perform worse;
- the capsule is valid merely because it does not state a target name.

The auditor is checking input integrity, not deciding whether GRG is correct.

## 3. Seven required checks

### A1 — Mechanical manifest integrity

PASS only if:

- all source files are at the exact historical cut;
- files are included only by the declared fixed-root / one-hop-dependency rule;
- no target keyword search or evaluator convenience selection is used;
- missing roots are recorded rather than replaced by later files;
- each included file records path + cut + inclusion rule + blob/content hash when available.

Return FAIL if the manifest contains a file that could only have been selected by knowing the hidden target or later answer.

### A2 — Capsule-answer leakage

Inspect only the proposed capsule, not the later answer.

Classify every substantive clue as:

~~~text
SYSTEM-FACT
TASK-GENERIC
ANSWER-SUGGESTIVE
ANSWER-EXPLICIT
UNRESOLVED
~~~

PASS requires:

- enough system information to permit a nontrivial mapping attempt;
- no named target;
- no later source-native answer terminology;
- no explicit expected discriminator;
- no explicit expected false positive;
- no explicit expected failure condition;
- no instruction to prefer GRG over no-mapping.

If the capsule directly supplies a load-bearing admission / exclusion / failure discriminator:

~~~text
CAPSULE LEAKAGE = INVALID
~~~

If it only weakly suggests a likely contrast:

~~~text
CAPSULE LEAKAGE = REVISE
~~~

Do not repair the capsule yourself in the same audit. Return the problematic phrases.

### A3 — Target-identity probe readiness

The future identity probe must:

- use the capsule alone;
- run in a fresh context;
- use the same model family/version planned for scored generation;
- ask only what real-world target, if any, the capsule appears to describe;
- record NOT INFERRED / INFERRED / AMBIGUOUS;
- run before any source pack is shown.

PASS means the procedure is reproducible and every outcome consequence is frozen:

~~~text
NOT INFERRED
-> blind integrity = PASS-ELIGIBLE
-> absolute historical-transfer credit remains eligible
-> fold may count as a valid core fold if all other gates pass
-> symmetric between-arm comparison may continue

INFERRED
-> blind integrity = COMPROMISED
-> absolute historical-transfer credit = NO
-> fold does not count as a valid core fold
-> symmetric between-arm comparison may continue
-> any residual result is COMPROMISED-DIAGNOSTIC

AMBIGUOUS
-> blind integrity = COMPROMISED
-> absolute historical-transfer credit = NO
-> fold does not count as a valid core fold
-> symmetric between-arm comparison may continue
-> any residual result is COMPROMISED-DIAGNOSTIC
~~~

No later evaluator discretion may upgrade INFERRED or AMBIGUOUS to PASS.

The pre-execution auditor does not run this identity probe.

### A4 — De-labelling transform reproducibility

PASS only if the transform:

- uses a recorded deterministic replacement table;
- changes GRG-specific labels/status vocabulary only;
- does not summarize;
- does not delete sentences/sections;
- does not reorder content;
- does not add causal interpretation;
- does not add target terminology;
- produces an auditable transformed-input hash.

The same transformed source content must feed all de-labelled arms.

### A5 — Arm information-budget symmetry

The scored arms may differ only by:

- period-correct GRG labels/structure for Arm G versus deterministic de-labelling for S/A/C/[H];
- the arm-specific instruction.

PASS requires:

~~~text
same masked capsule
same underlying source manifest
same file order
same context-budget ceiling
same output A/X/F[/O] template
same exposed model identifier
same product / API surface
same reasoning-effort setting
same user-addressable inference settings
same sampling count
no browsing / target retrieval
~~~

Arm C must not receive an evaluator-written causal summary.

Arm A must not receive a selectively simplified analogy summary.

If source content is added/deleted asymmetrically:

~~~text
ARM INFORMATION-BUDGET SYMMETRY = FAIL
~~~

### A6 — Same-model / repeated-sampling plan

PASS only if:

~~~text
same exposed model identifier across scored arms = YES
same product / API surface = YES
same reasoning-effort setting = YES
same user-addressable inference settings = YES
odd independent samples per arm k >= 3
preferred first run k = 3
all samples frozen before unblind
no regeneration based on other-arm performance
single-sample residual claims forbidden
~~~

If an internal backend build hash is exposed, it must match.

If it is not exposed, the plan must:

- record backend build = UNAVAILABLE;
- run all scored arms in one bounded execution batch;
- avoid claiming exact hidden-build identity.

If seeds are exposed, use distinct recorded seeds.

If seeds are not exposed, fresh isolated contexts are acceptable but the limitation must be recorded.

### A7 — P_POST separation

The historical generators must not be required to use post-cut #1025 evidence-generative-provenance vocabulary.

PASS requires:

~~~text
historical generator output = A / X / F + conditional O

P_POST =
current-method evaluator scaffold
applied only after all generator outputs freeze
historical transfer credit = NONE
~~~

If the generator prompt contains required P / pseudoreplication / O_R vs O_W vocabulary:

~~~text
P_POST SEPARATION = FAIL
~~~

## 4. Required audit output

Return exactly this structure:

~~~text
BCTB-0 T1 PRE-EXECUTION AUDIT

historical cut =
9900f425369b8840eac9220e567a60b811c52b27

A1 mechanical manifest integrity =
PASS / REVISE / FAIL

A2 capsule-answer leakage =
PASS / REVISE / INVALID

A3 target-identity probe readiness =
PASS / REVISE / FAIL

A4 de-labelling transform reproducibility =
PASS / REVISE / FAIL

A5 arm information-budget symmetry =
PASS / REVISE / FAIL

A6 same-model / repeated-sampling plan =
PASS / REVISE / FAIL

A7 P_POST separation =
PASS / REVISE / FAIL

EXECUTION READINESS =
PASS / BLOCKED

blocking items =
- ...

non-blocking notes =
- ...

target identity guessed during this audit =
NO / YES / AMBIGUOUS

target-result material encountered =
NO / YES

auditor contamination =
NONE / POSSIBLE / CONFIRMED
~~~

## 5. Decision rule

~~~text
EXECUTION READINESS = PASS
~~~

only if:

- A1 = PASS;
- A2 = PASS;
- A3 = PASS;
- A4 = PASS;
- A5 = PASS;
- A6 = PASS;
- A7 = PASS;
- target-result material encountered = NO;
- auditor contamination != CONFIRMED.

Any REVISE / FAIL / INVALID keeps T1 blocked.

## 6. STOP conditions

Stop immediately and report contamination if:

- a file names the hidden target unexpectedly;
- a later SourceCard/audit/result is exposed;
- the auditor is asked to inspect current-main target evidence;
- the evaluator supplies the expected answer to help decide leakage;
- the full BCTB-0 charter or PR discussion exposes the hidden target before the audit completes.

Do not continue and pretend the audit remains blind.

## 7. Handoff back to evaluator

If PASS:

~~~text
do not execute T1 in the auditor session
return the audit only
~~~

The evaluator may then authorize separate R1/R2/R4 execution contexts.

If BLOCKED:

~~~text
return exact blocking phrases / file selections / transform asymmetries
do not rewrite them
~~~

The target-aware evaluator owns any revision.

## 8. Programme boundary

~~~text
this audit =
input-integrity / execution-readiness only

it does NOT establish:
GRG correctness
M4
M5
scientific distinctiveness
target-domain novelty
canonical consequence
~~~
