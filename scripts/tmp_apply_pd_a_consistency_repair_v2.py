from pathlib import Path

# Reuse the already-frozen owner/§13 patch from v1, correcting its accidental trailing character.
base_path = Path('/tmp/pd_a_base.py')
base = base_path.read_text(encoding='utf-8')
if not base.endswith('encoding="utf-8")n'):
    raise SystemExit('unexpected v1 helper ending')
base = base[:-1]
exec(compile(base, str(base_path), 'exec'))

# 4) Historical Pass-1 audit: make the former extra gate explicitly historical and add post-PD-A read-back.
p1 = Path('Operations/Audits/SRT_SELECTION_IRREDUCIBILITY_RIVAL_TEST_2026-08-16.md')
text = p1.read_text(encoding='utf-8')
old = '> **Residue gate**: `Core/SRT_OPEN_TENSIONS.md §13` currently allows a formal GOV-SUB01 residue label for `selection` only after at least one qualifying exhibit is produced against the reduced vocabulary: differential counterfactual (`E_cf`), differential intervention (`E_int`), an executed real-choice/script divergence the reduced vocabulary cannot carry, or a demonstrable `E_phen / E_norm` loss. Pass 1 produces none of those exhibits. Therefore **formal GOV-SUB01 residue remains `UNASSIGNED`**. All `R* / N* / P` references below are analysis-level **candidate readings only**, not attached residue labels.\n'
new = '> **Residue gate (historical at execution time)**: when this audit was executed, `Core/SRT_OPEN_TENSIONS.md §13` imposed an additional exhibit gate before a formal GOV-SUB01 residue label could be attached to `selection`: differential counterfactual (`E_cf`), differential intervention (`E_int`), an executed real-choice/script divergence the reduced vocabulary could not carry, or a demonstrable `E_phen / E_norm` loss. Pass 1 produced none of those exhibits, so **formal GOV-SUB01 residue was correctly recorded as `UNASSIGNED`** and all `R* / N* / P` references below remained candidate readings.\n>\n> **Post-PD-A read-back (2026-08-17)**: PD-A later retires that extra D2/exhibit gate because direct D2 is not a P0-admission requirement. This does **not** retroactively attach a residue label. The historical `UNASSIGNED` verdict remains controlling until a post-PD-A re-adjudication explicitly applies GOV-SUB01 `§8.1`, completes relevant Step-5 compensation tests and Step-6 perturbation robustness, reruns the mandatory anti-laundering checks, and records a new label rationale. See `Core/SRT_OPEN_TENSIONS.md §13`.\n'
if old not in text:
    raise SystemExit('Pass1 residue gate marker missing')
text = text.replace(old, new, 1)
text = text.replace('does not satisfy the §13 residue gate because no external counterfactual/interventional divergence was executed', 'did not satisfy the then-current §13 residue gate because no external counterfactual/interventional divergence was executed')
text = text.replace('§13 currently imposes an additional exhibit gate', 'the then-current §13 imposed an additional exhibit gate')
p1.write_text(text, encoding='utf-8')

# 5) Historical Pass-1.5 audit: preserve historical execution but prevent retroactive residue promotion.
p15 = Path('Operations/Audits/SRT_SELECTION_IRREDUCIBILITY_PASS1_5_JOINT_REMOVAL_2026-08-16.md')
text = p15.read_text(encoding='utf-8')
marker = '> **Hard boundary**: this pass does not modify `P0-01`, `P1-T05`, the CG protocol, or any canonical definition. It does not assign a formal GOV-SUB01 residue to `selection`.\n'
insert = marker + '>\n> **Post-PD-A read-back (2026-08-17)**: PD-A separates P0 admission from downstream D2 and retires the former extra §13 D2/exhibit gate. This historical pass is **not** retroactively upgraded: it did not execute the full declared perturbation sweep or a post-PD-A residue re-adjudication. Its no-formal-residue disposition therefore remains in force until the current `Core/SRT_OPEN_TENSIONS.md §13` re-adjudication rule is satisfied.\n'
if marker not in text:
    raise SystemExit('Pass1.5 hard-boundary marker missing')
text = text.replace(marker, insert, 1)
p15.write_text(text, encoding='utf-8')

# 6) Compact PD-A author decision record.
packet = Path('Operations/SRT_PD_A_P0_D2_BOUNDARY_AUTHOR_DECISION_PACKET_2026-08-17.md')
if packet.exists():
    raise SystemExit('PD-A packet already exists')
packet.write_text('''---
id: SRT-PD-A-P0-D2-BOUNDARY-AUTHOR-DECISION-20260817
type: author_decision_record
status: active
record_stage: author_decision_landed
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: author_decision_P0_boundary
canonical: false
date: 2026-08-17
dependency:
  - SRT-CLAIM-LADDER
  - SRT-CORE-21A-MINIMAL-AXIOMS
  - SRT-OPEN-TENSIONS
  - SRT-GOV-SUB01-SUBTRACTIVE-AUDIT
  - SRT-CORE-24-DISCRIMINATING-PREDICTIONS
tags: [AuthorDecision, PDA, P0, D2, EmpiricalDiscrimination, Fruitfulness, AntiImmunization]
---

# PD-A — P0 / Empirical Discrimination Boundary

> **Author decision (2026-08-17): A.** Keep `P0-01` as SRT's explicit Selection-first primitive. Direct D2/D3 rival discrimination is not a P0 admission condition; scientific distinctiveness must be earned downstream at P3/P4.

## 1. What PD-A decides

PD-A separates two proof burdens:

```text
P0 architecture
= coherence + non-redundancy + derivational fruitfulness

P3/P4 science
= operationalized prediction + frozen bounded rival + D2/D3
```

Allowed:

- `Within SRT, Selection is primitive.`
- a D2-positive workline supports the empirical fruitfulness of that specific derivation / workline.

Forbidden:

- `experiments prove Selection is ontologically primitive`;
- using P0 status as evidence of empirical irreducibility;
- using `D2 = 0` from one workline as an automatic P0 falsification;
- using one D2-positive workline as architecture-wide empirical superiority.

## 2. GOV-SUB01 residue after PD-A

The pre-PD-A `OPEN_TENSIONS §13` added a D2/exhibit gate on top of GOV-SUB01. PD-A retires that **extra** gate because D2 is not a P0-admission condition.

Retirement is not retroactive promotion. Pass 1 / Pass 1.5 remain formally `UNASSIGNED` until a post-PD-A re-adjudication:

1. applies GOV-SUB01 `§8.1` to primitive Selection deletion;
2. completes relevant Step-5 joint-removal / minimum-set tests;
3. executes Step-6 perturbation robustness before a robust label;
4. reruns hidden-reparameterization, target-laundering, bearer-relocation, short-horizon and scale-collapse checks;
5. explicitly records and reversibility-tests a residue label.

D2 remains required for **scientific discrimination claims**, not for every possible GOV-SUB01 residue label.

## 3. Anti-immunization / evidence symmetry

A PD-A workline is `mature` only if, before outcome inspection, it freezes:

- an independently motivated middle-level consequence;
- a bounded rival state/update/calibration family and revision / complexity cost;
- a common intervention and observable;
- symmetric failure criteria;
- a terminal disposition (`spec-stage NO-GO`, D2-negative/rival-equivalent, or D2-positive).

Dataset swaps or rephrasings of one derivation do not count as independent worklines.

Governance trigger, not statistical theorem:

- **negative**: 3 independent mature D2-negative / rival-equivalent worklines spanning at least 2 distinct middle-level consequences force a P0-01 fruitfulness / redundancy review before a fourth substantially similar mature workline;
- **positive**: architecture-level empirical-fruitfulness language requires at least 2 independent D2-positive worklines grounded in distinct middle-level consequences; one positive remains local.

`Core/SRT_OPEN_TENSIONS.md §13` owns the scoreboard and review trigger. Any change to P0 remains author-gated.

Historical A2 / P24 NO-GO results are relevant pressure evidence but are not automatically back-counted because they were not all frozen under this maturity contract. Count at adoption: `0`.

## 4. Research order

```text
P0/P1
-> non-circular middle-level consequence
-> deletion / replacement audit
-> P3/P4 operationalization
-> frozen bounded rival
-> D2/D3
```

A downstream D2 can make SRT scientifically fruitful without turning P0 into an observed variable.

## 5. Scope / stop rule

PD-A adds no symbol, equation, ontology layer, Selection subtype, or empirical result. It does not change Core 24's established D2 count (`0`).

Do not reopen direct-D2-as-P0-admission without a new author decision. Do not treat PD-A as immunity from review: the mandatory negative trigger above is part of the decision.
''', encoding='utf-8')

# 7) STATUS: add only compact RC-A / PD-A pointers and update date; bundle regen will absorb the high-sensitivity edit.
status = Path('STATUS.md')
text = status.read_text(encoding='utf-8')
text = text.replace('updated: 2026-08-16', 'updated: 2026-08-17', 1)
text = text.replace('> **最后更新**：2026-08-16', '> **最后更新**：2026-08-17', 1)
status_marker = '- **2026-08-16 synthesis target freeze**：继承 2026-08-11 bounded probe 的 Case A / STOP 与 Philosophy Route 8a closure，新的 patch / hook 不再默认指向 AI CompactCore、Neuroscience N1–N13、Neural Mechanisms CompactCore 或为已测 Philosophy cluster 新建 synthesis。历史 target 引用保留为工程记录，不代表当前施工授权。复活条件仅为：新的 bounded probe 转为 Case B/C、owner-level contradiction 无法局部修复，或作者明确重新授权。见 `Operations/SRT_SYNTHESIS_TARGET_FREEZE_2026-08-16.md`。\n'
status_insert = status_marker + '- **2026-08-17 RC-A**：former `P1-T05: Real Choice Moment` 已从 P1 降为 P2/P3 Agency / Automation Guard；`Selection != Agency`，script / habit / gradient / L2 automation 不得反推“没有 Selection”。P1-T06 Stable ISP 保留。裁决/同步记录见 `Operations/Audits/SRT_RC_A_P1_T05_DEMOTION_DERIVATIVE_SYNC_2026-08-17.md`。\n- **2026-08-17 PD-A**：P0-01 保留为 Selection-first primitive，但 direct D2/D3 不是 P0 准入条件；科学区分力必须在 P3/P4 以冻结 bounded rival 的 D2/D3 支付。旧 §13 额外 exhibit gate 退役但不追溯升级 residue；3 条成熟独立 null/rival-equivalent 工作线（至少 2 个中层推导）将强制重开 P0-01 fruitfulness/redundancy review。裁决见 `Operations/SRT_PD_A_P0_D2_BOUNDARY_AUTHOR_DECISION_PACKET_2026-08-17.md`。\n'
if status_marker not in text:
    raise SystemExit('STATUS insertion marker missing')
text = text.replace(status_marker, status_insert, 1)
status.write_text(text, encoding='utf-8')
