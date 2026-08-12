---
id: SRT-EXISTENCE-AUTHOR-DECISION-PACKET-20260811
type: framework
status: frozen
claim_mode: governance
updated: 2026-08-11
record_stage: author_decided_and_landed
implementation_status: landed
author_decision: EX-A
decision_date: 2026-08-11
layer: meta
epistemic_layer: os
canonical: false
related_files:
  - Core/SRT_Core_21_Minimal_Axioms.md
  - Core/SRT_Core_21b_Constitutive_Theorems.md
  - Core/SRT_Core_21c_Bridge_Hypotheses.md
  - Core_Law/SRT_L0_Metaphysics.md
  - Core_Law/SRT_Reference_Axioms.md
  - Core_Law/SRT_Reference_Ontology.md
  - Core/SRT_OPEN_TENSIONS.md
  - Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md
  - Operations/_SRT_REVIEW_QUEUE.md
---

# 作者裁决包：Existence、Anchoring Persistence 与 Stable ISP

## 作者裁决记录（2026-08-11）

作者选择：**EX-A — Actuality／Persistence／Stable-ISP 三层分离**。

已落地：

- `P0-01` 承担存在准入的最低层：一个 determinate `L_1` event 已经发生；
- `P0-02` 只承担 anchoring persistence：该事件是否留下有效痕迹、获得维持条件并继续约束后续转移；
- stable ISP identity 保留在 `P1-T06 / ST-A`：同一视角与历史承载过程跨声明扰动范围被反复重构，并保持 continued selectability；
- 旧式 `E = 1-H(L_1)/H(L_0)` 从 P0 撤下，只在 `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B14` 作为历史启发式保留；
- EX-A 不采用 `H(L_0^{abs})`、accessible-horizon 归一化、概率测度或量化 existence index；未来模型级读出须另过 P3 测量门。

本文件是 author-decision record，不是定义源。Canonical 口径以已落地 owner 文件为准。

## 1. 本次只处理的连接

> 一个事件实际发生
> → 它是否因此必然持续存在，并进一步成为 stable ISP。

本轮不重审 PC-A、AM-A、PHR-A 或 ST-A，不把持续性写成事件现实化的原因，也不推进主体、意识、伦理、合法性或统一物理命题。

## 2. 地板检验

### 2.1 负担标注

| 判断句 | 标签 | 结论 |
|---|---|---|
| “一个 determinate `L_1` event 已发生。” | **D / P0-01** | 这是 manifest actuality；不以持续时长为准入条件 |
| “该事件留下痕迹并约束后续转移。” | **S** | 需要指定 trace carrier、因果效力与时间窗；不是事件发生的同义反复 |
| “该结构获得维持条件并持续。” | **C + S** | 需要环境、维护机制、扰动范围与 replacement control；不由一次发生自动推出 |
| “持续结构就是同一个 stable ISP。” | **S / 当前不成立** | 还需历史／视角承载、recurrent reconstitution 与 continued selectability |
| “存在强度可由旧 `E` 式量化。” | **O / 未获许可** | 缺少域、分割、测度、有限性与时间窗；只能保留为历史启发式 |

### 2.2 裸句测试

去掉“凝结”“扎根”“从虚无中站住”等比喻后，可保留的裸句是：

> 事件现实性是一次 determinate transition 已发生；锚定持续性是该事件的结果在后续时间中仍具有效痕迹、维持条件与约束效力；stable ISP 则进一步要求同一视角与历史承载过程跨声明扰动范围被反复重构并保持可继续选择。三者不得互相替代。

### 2.3 连接判决

```text
manifest actuality -> historical occurrence                         🟢
historical occurrence -> effective trace                            🟡 需 carrier / efficacy / horizon
effective trace -> maintained persistence                           🔴 不自动成立
maintained persistence -> stable ISP identity                       🔴 不自动成立
old entropy ratio -> quantitative existence or persistence readout  🔴 未定义
```

因此，“发生即永久持续”与“持续即 stable ISP”都不能作为强连接保留。EX-A 通过分层保住三个不同问题，而不制造一个表面统一、实际跨层的 existence 指标。

## 3. Canonical 落点

- `Core/SRT_Core_21_Minimal_Axioms.md P0-01/P0-02`：actuality／persistence 边界；
- `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06`：stable ISP；
- `Core/SRT_Core_21c_Bridge_Hypotheses.md B14`：旧式的历史启发式与未来模型级测量前件；
- `Core_Law/SRT_L0_Metaphysics.md`：L0 本体论叙述的三层同步；
- `Core/SRT_OPEN_TENSIONS.md §15`：语义 gate 销账，剩余熵形式化债务继续登记。

## 4. 推理护栏

1. 瞬时事件可以是真实事件；未持续不等于从未发生。
2. 后来失去锚定不抹除更早的发生史，受 P0-03 约束。
3. 持续存在不自动建立 structural stability、stable ISP identity 或 generative health。
4. 旧 `E` 式不得作为经验读出，不得代入 `L_0^{abs}`，也不得以 EX-A 名义补一个未裁决的归一化。
5. EX-A 不推出 subjecthood、consciousness、moral status、legitimacy 或任何伦理结论。

## 5. 停驻条件

量化 anchoring-persistence readout 只有在具名 P3 工作线同时声明以下对象时才可复活：相对／可访问域、outcome partition 或 sigma-algebra、概率测度、必要的有限／非零条件、事件边界与比较时间窗。此前不构成 canonical 待办。
