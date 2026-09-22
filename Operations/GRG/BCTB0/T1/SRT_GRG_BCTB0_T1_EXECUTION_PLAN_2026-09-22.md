---
id: SRT-GRG-BCTB0-T1-EXECUTION-PLAN-20260922
type: calibration_execution_plan
status: candidate
date: 2026-09-22
canonical: false
ai_do_not_use_for_definition: true
---

# BCTB-0 T1 execution plan — candidate

## 0. Gate

T1 execution is BLOCKED until R3 returns PASS on A1–A7.

This file is a proposed plan only.

## 1. Inputs

Historical cut:

```text
9900f425369b8840eac9220e567a60b811c52b27
```

Raw source pack:

`Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_RAW_2026-09-22.md`

Deterministic de-labelled source pack:

`Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_DELABELED_2026-09-22.md`

De-labelling transform:

`Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_DELABEL_TRANSFORM_2026-09-22.md`

Masked capsule:

`Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_MASKED_CAPSULE_2026-09-22.md`

status:

```text
PRESENT / FROZEN FROM FRESH R2
```

## 2. Product / model controls

Scored-generation surface:

```text
product = ChatGPT text chat
model identifier = GPT-5.6 Sol
reasoning effort = High
backend build hash = UNAVAILABLE unless product exposes one at execution time
temperature / seed = NOT USER-ADDRESSABLE unless product exposes them
```

All scored arms must use the same exposed model identifier and reasoning effort.

All 12 scored samples must be run in one bounded execution batch after R3 PASS.

If the exposed model identifier changes during the batch:

```text
STOP / batch invalid
```

If a backend build hash becomes exposed, it must be recorded and matched.

## 3. Context isolation

For identity probe and every scored sample:

- use a fresh isolated chat/context;
- Memory/personal-context carryover must be disabled for the execution context where the product permits this control;
- do not invoke personal-context retrieval;
- do not browse the web;
- do not use GitHub search;
- do not read PR #1027;
- do not read the full BCTB-0 charter;
- do not read target/result/audit files;
- do not read outputs from other arms/samples;
- read only the explicitly authorized capsule + source-pack file + arm instruction + output template.

If memory isolation cannot be established:

```text
procedural isolation limitation = RECORDED
identity probe consequence still applies
```

The run must not claim epistemic blindness.

## 4. Identity probe

Run once before any source pack is shown.

Model:

```text
GPT-5.6 Sol / High
```

Input:

- audited masked capsule only.

Prompt:

```text
Given only this capsule, does it identify a specific real-world product,
feature, paper, protocol, institution or named target?

Return exactly one:
NOT INFERRED
INFERRED: <name>
AMBIGUOUS: <short explanation>

Do not browse or use tools.
```

Consequence:

```text
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
-> any residual result must be labelled COMPROMISED-DIAGNOSTIC

AMBIGUOUS
-> blind integrity = COMPROMISED
-> absolute historical-transfer credit = NO
-> fold does not count as a valid core fold
-> symmetric between-arm comparison may continue
-> any residual result must be labelled COMPROMISED-DIAGNOSTIC
```

No later evaluator discretion may upgrade INFERRED or AMBIGUOUS to PASS.

## 4.1 Frozen context budget

The context-budget ceiling is identical across all scored arms.

```text
source-pack ceiling = 170,000 UTF-8 characters
total serialized scored input ceiling = 180,000 UTF-8 characters
```

The total serialized scored input includes:

- the audited masked capsule;
- exactly one authorized source pack;
- the arm instruction;
- the frozen output template.

Rules:

- G uses the full raw source pack;
- S/A/C use the full de-labelled source pack;
- no arm-specific truncation, summarization, omission or compression;
- if any scored input exceeds the frozen ceiling or is truncated by the product, the entire T1 batch is INVALID and must stop;
- unused budget is not filled with additional material.

The ceiling is a common maximum, not a requirement that every arm consume the same number of characters.

## 5. Scored arms

T1 uses four scored arms.

```text
G = period-correct labelled framework
S = structured de-labelled ablation
A = structure-mapping / analogy baseline
C = causal transfer / invariance baseline
H = N.A. for T1 v0.1
```

Information budget:

```text
G -> raw source pack
S -> de-labelled source pack
A -> same de-labelled source pack
C -> same de-labelled source pack
all -> identical audited capsule
all -> identical A/X/F + conditional O output template
```

No evaluator-written summaries are supplied.

## 6. Arm instructions

### G

```text
Using only the supplied historical source pack and capsule,
propose the strongest warranted cross-domain mapping, if any.

Preserve source-native differences.
Return A admission, X nearest false positive,
F failure/narrowing, and O only if objectification is load-bearing.
If no mapping is warranted, say so.
Do not browse or use tools beyond reading the supplied inputs.
```

### S

```text
Using only the supplied structured source pack and capsule,
infer the strongest warranted cross-domain mapping, if any,
without assuming that any named framework label is privileged.

Return A admission, X nearest false positive,
F failure/narrowing, and O only if objectification is load-bearing.
If no mapping is warranted, say so.
Do not browse or use tools beyond reading the supplied inputs.
```

### A

```text
Use structure-mapping / analogical reasoning on the supplied source pack
and capsule.

Identify the strongest relational correspondence that is warranted,
then return A admission, X nearest false positive,
F failure/narrowing, and O only if objectification is load-bearing.
If no mapping is warranted, say so.
Do not browse or use tools beyond reading the supplied inputs.
```

### C

```text
Use causal-transfer / invariance reasoning on the supplied source pack
and capsule.

Identify a candidate transferable conditional or mechanism burden,
state what must remain invariant, and return
A admission, X nearest non-transfer / false positive,
F failure/narrowing, and O only if objectification is load-bearing.
Preserve source-specific mechanism differences.
If no mapping is warranted, say so.
Do not browse or use tools beyond reading the supplied inputs.
```

## 7. Sampling

```text
k = 3 independent samples per scored arm
arms = G / S / A / C
total scored samples = 12
majority threshold = 2 of 3
```

Each sample uses a fresh isolated context.

No sample may be regenerated because another sample or arm underperformed.

Outputs are frozen before any target unblind.

## 8. Historical-generator output template

Every scored sample returns:

```text
FOLD = T1
ARM = G / S / A / C
SAMPLE = 1 / 2 / 3
MODEL IDENTIFIER = GPT-5.6 Sol
REASONING EFFORT = High
BACKEND BUILD = <hash if exposed> / UNAVAILABLE
TARGET IDENTITY INFERRED DURING SAMPLE = NO / YES / OPEN

A — ADMISSION
candidate burden =
required conditions =
evidence that would pay admission =
weaker nearby relation that is insufficient =

X — EXCLUSION
nearest false positive =
why it must not count =
candidate contrast / negative control =

F — FAILURE / NARROWING
load-bearing condition =
predicted failure / narrowing if removed =
post-result revision operation if violated =

O — OBJECTIFICATION
status = OPENED / NOT OPENED
if opened:
  objectification change =
  expected stability / narrowing / flip / unresolved =
  mechanism-specific necessity preserved =

PROPOSED GRAMMAR REVISION PRESSURE =
NONE / NARROW / SPLIT / RETYPE / RETIRE / OTHER

NO-RESCUE ACKNOWLEDGEMENT =
packet frozen before target unblind.
```

P_POST is not part of this generator output.

## 9. P_POST

Only after all 12 samples are frozen, the evaluator applies the current evidence-generative-provenance scaffold uniformly.

```text
P_POST historical transfer credit = NONE
```

## 10. Residual rule

For any materially equivalent constraint:

```text
G majority = appears in >=2/3 G samples
baseline majority = appears in >=2/3 samples of S, A or C

G majority + any baseline majority
-> BASELINE-SHARED

G majority + no baseline majority
-> GRG-RESIDUAL-CANDIDATE

not G majority
-> NO STABLE GRG CANDIDATE
```

No single-sample residual claim is permitted.
