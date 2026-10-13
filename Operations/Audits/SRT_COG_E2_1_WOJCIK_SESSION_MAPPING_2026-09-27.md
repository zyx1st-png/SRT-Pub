---
id: SRT-COG-E2-1-WOJCIK-SESSION-MAPPING-20260927
type: audit
status: active
canonical: false
layer: operations
epistemic_layer: os
claim_mode: source_mapping
created: 2026-09-27
updated: 2026-09-27
research_mode: U
dependency:
  - Operations/Audits/SRT_COG_E2_1_WOJCIK_SOURCE_CODE_AUDIT_2026-09-27.md
tags: [Cognition, Wójcik, Dryad, SessionMapping, G0]
---

# COG-E2-1 — Dryad ↔ analysis-code session mapping

> **Purpose:** close preregistration gate G0 with a source-grounded mapping.
>
> **External code lock:** `m-j-wojcik/pfc_learning@48ada8054940f6a7ac26e8e83d150357a9f249d2`.

## 1. Source chain

Dryad README states:

- each ZIP is one experimental session;
- `m1` denotes Monkey 1;
- `ses24` denotes Session 24.

Nature Neuroscience Methods states:

- Monkey 1 = 25 daily sessions = 17 Experiment 1 + 8 Experiment 2;
- Monkey 2 = 25 daily sessions = 10 Experiment 1 + 15 Experiment 2;
- sessions are divided chronologically into learning stages.

The analysis repository `config.yml` contains:

- Womble = 17 Exp1 date-labelled sessions + 8 Exp2 date-labelled sessions;
- Wilfred = 10 Exp1 date-labelled sessions + 15 Exp2 date-labelled sessions;
- each list is chronological;
- `combine_session_lists(mode='stages')` splits the listed order.

This uniquely fixes:

~~~text
m1 = Monkey 1 = Womble
m2 = Monkey 2 = Wilfred

Dryad session ordinal
= ordinal position in the corresponding chronological code-session list.
~~~

No archive-size inference is used.

## 2. Complete mapping

| Dryad ID | code session ID | animal | experiment | basis |
|---|---|---|---|---|
| m1_ses1 | Wom20200910 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses2 | Wom20200911 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses3 | Wom20200914 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses4 | Wom20200915 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses5 | Wom20200916 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses6 | Wom20200917 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses7 | Wom20200918 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses8 | Wom20200921 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses9 | Wom20200922 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses10 | Wom20200923 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses11 | Wom20200924 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses12 | Wom20200925 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses13 | Wom20200928 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses14 | Wom20200929 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses15 | Wom20200930 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses16 | Wom20201001 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses17 | Wom20201002 | Monkey 1 / Womble | Exp1 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses18 | Wom20201005 | Monkey 1 / Womble | Exp2 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses19 | Wom20201006 | Monkey 1 / Womble | Exp2 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses20 | Wom20201007 | Monkey 1 / Womble | Exp2 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses21 | Wom20201008 | Monkey 1 / Womble | Exp2 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses22 | Wom20201009 | Monkey 1 / Womble | Exp2 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses23 | Wom20201012 | Monkey 1 / Womble | Exp2 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses24 | Wom20201013 | Monkey 1 / Womble | Exp2 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m1_ses25 | Wom20201014 | Monkey 1 / Womble | Exp2 | Dryad m1=Monkey 1; paper 17+8; config chronological Wom 17+8 |
| m2_ses1 | Wil20201020 | Monkey 2 / Wilfred | Exp1 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses2 | Wil20201021 | Monkey 2 / Wilfred | Exp1 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses3 | Wil20201022 | Monkey 2 / Wilfred | Exp1 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses4 | Wil20201023 | Monkey 2 / Wilfred | Exp1 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses5 | Wil20201026 | Monkey 2 / Wilfred | Exp1 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses6 | Wil20201027 | Monkey 2 / Wilfred | Exp1 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses7 | Wil20201028 | Monkey 2 / Wilfred | Exp1 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses8 | Wil20201029 | Monkey 2 / Wilfred | Exp1 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses9 | Wil20201102 | Monkey 2 / Wilfred | Exp1 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses10 | Wil20201103 | Monkey 2 / Wilfred | Exp1 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses11 | Wil20201104 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses12 | Wil20201106 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses13 | Wil20201109 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses14 | Wil20201110 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses15 | Wil20201111 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses16 | Wil20201112 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses17 | Wil20201113 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses18 | Wil20201116 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses19 | Wil20201117 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses20 | Wil20201118 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses21 | Wil20201119 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses22 | Wil20201120 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses23 | Wil20201123 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses24 | Wil20201124 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |
| m2_ses25 | Wil20201125 | Monkey 2 / Wilfred | Exp2 | Dryad m2=Monkey 2; paper 10+15; config chronological Wil 10+15 |

## 3. Boundary checks

The experiment transition is exactly where the independent source counts require it:

~~~text
m1_ses1..17  = Womble Exp1
m1_ses18..25 = Womble Exp2

m2_ses1..10  = Wilfred Exp1
m2_ses11..25 = Wilfred Exp2
~~~

This matches the paper's 17+8 and 10+15 partition and the code's two experiment-specific session lists.

## 4. G0 disposition

~~~text
G0 SESSION-ID MAPPING = PASS.
~~~

Execution adapter rule:

- downloaded archives retain original Dryad names;
- any extraction/rename layer must create date-labelled aliases/copies expected by the analysis code;
- the mapping table above is the only permitted ordinal adapter;
- do not infer or alter session identity from file size.

## 5. Next gate

~~~text
G1 = reproduce one source-owned E1 result
before any H1/H2/H3 inferential duel.
~~~
