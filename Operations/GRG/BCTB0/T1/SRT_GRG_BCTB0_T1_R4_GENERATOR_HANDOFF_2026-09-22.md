---
id: SRT-GRG-BCTB0-T1-R4-GENERATOR-HANDOFF-20260922
type: handoff
status: active
date: 2026-09-22
canonical: false
ai_do_not_use_for_definition: true
---

# BCTB-0 T1 R4 generator handoff

## 0. Role

You are one isolated scored generator sample for BCTB-0 fold T1.

This handoff is sufficient to run exactly one sample.

Do not inspect any evaluator, audit, target, result, PR, charter, package-index, R2, R3, or other-sample material.

Do not execute more than one sample in this context.

## 1. Invocation

The user must specify exactly one pair:

```text
ARM = G / S / A / C
SAMPLE = 1 / 2 / 3
```

If either is absent, invalid, or more than one pair is requested:

```text
STOP = INVALID SAMPLE INVOCATION
```

Do not infer or choose a different arm/sample.

## 2. Exact authorized ref and inputs

Read only from ref:

`experiments/grg-bctb0-t1-preexec-package-20260922`

Always read the frozen capsule:

`Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_MASKED_CAPSULE_2026-09-22.md`

Then read exactly one source pack:

```text
ARM G:
Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_RAW_2026-09-22.md

ARM S / A / C:
Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_DELABELED_2026-09-22.md
```

No other repository path is authorized.

Do not call PR metadata / PR lookup.
Do not use repository-wide search.
Do not browse the web.
Do not use personal-context or memory retrieval.
Do not read outputs from any other sample.
Do not write to GitHub or any other external system.

## 3. Frozen execution surface

```text
product = ChatGPT text chat
model identifier = GPT-5.6 Sol
reasoning effort = High
backend build = UNAVAILABLE unless exposed
```

If the exposed model identifier is not GPT-5.6 Sol:

```text
STOP = MODEL IDENTIFIER MISMATCH
```

Context ceiling:

```text
source-pack ceiling = 170,000 UTF-8 characters
total serialized scored input ceiling = 180,000 UTF-8 characters
```

Use the complete authorized source pack. Do not summarize, omit, truncate, compress, or substitute it.

If the input is truncated or cannot be read completely:

```text
STOP = INPUT TRUNCATION
```

## 4. Frozen arm instructions

### ARM G

```text
Using only the supplied historical source pack and capsule,
propose the strongest warranted cross-domain mapping, if any.

Preserve source-native differences.
Return A admission, X nearest false positive,
F failure/narrowing, and O only if objectification is load-bearing.
If no mapping is warranted, say so.
Do not browse or use tools beyond reading the supplied inputs.
```

### ARM S

```text
Using only the supplied structured source pack and capsule,
infer the strongest warranted cross-domain mapping, if any,
without assuming that any named framework label is privileged.

Return A admission, X nearest false positive,
F failure/narrowing, and O only if objectification is load-bearing.
If no mapping is warranted, say so.
Do not browse or use tools beyond reading the supplied inputs.
```

### ARM A

```text
Use structure-mapping / analogical reasoning on the supplied source pack
and capsule.

Identify the strongest relational correspondence that is warranted,
then return A admission, X nearest false positive,
F failure/narrowing, and O only if objectification is load-bearing.
If no mapping is warranted, say so.
Do not browse or use tools beyond reading the supplied inputs.
```

### ARM C

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

Use only the instruction for the invoked arm.

## 5. Frozen output template

Return exactly one scored packet in this structure:

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

P_POST is not part of generator output.

Do not append commentary, confidence scoring, evaluator notes, or cross-sample comparisons.

## 6. Isolation / no-rescue

This context performs exactly one sample.

Do not:

- ask for the hidden target;
- infer expected evaluator answer from governance language;
- inspect target result/audit material;
- revise the capsule;
- revise the source pack;
- consult another sample;
- regenerate because the result appears weak;
- add post-cut concepts to rescue a mapping.

If no mapping is warranted, return that result within the same frozen template.

## 7. Return boundary

Return the scored packet to the user only.

Do not commit, save, compare, evaluate, or unblind it in this context.
