---
id: SRT-SYNTHESIS-TARGET-FREEZE-20260816
type: framework
status: frozen
claim_mode: governance
updated: 2026-08-16
record_stage: governance_decided
implementation_status: active
layer: meta
epistemic_layer: os
canonical: false
dependency:
  - SRT-MATERIAL-CLUSTER-BASELINE-PROBE-RESULTS-20260811
  - SRT-PH-IND01-ROUTING-TREATMENT-RESULTS-20260811
  - SRT-STATUS
related_files:
  - Operations/Audits/SRT_MATERIAL_CLUSTER_BASELINE_PROBE_RESULTS_2026-08-11.md
  - Operations/Audits/SRT_PH_IND01_ROUTING_TREATMENT_RESULTS_2026-08-11.md
  - AI/SRT_AI_Architecture_CompactCore.md
  - Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
  - STATUS.md
tags: [Governance, Freeze, Synthesis, Pipeline1, BoundedProbe, WIP]
---

# SRT Synthesis Target Freeze — 2026-08-16

## 0. Decision

2026-08-11 的材料簇 bounded baseline 已给出：

```text
AI            18/18 -> Case A / STOP
Neuroscience  18/18 -> Case A / STOP
Philosophy    17/18 -> narrow routing Case B
                 -> Route 8a treatment 18/18
                 -> STOP
```

因此，从 2026-08-16 起，以下对象**不得继续作为新 patch / hook 的默认 future landing target**：

```text
AI/SRT_AI_Architecture_CompactCore.md
Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
new Philosophy cluster synthesis created as a remedy for the tested material cluster
```

其中：

- `Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md` 当前不存在；**不得为了消除静态断链感而创建它**；
- `AI/SRT_AI_Architecture_CompactCore.md` 与 `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` 即使存在，也不得因为新材料 patch 数量增加而自动吸收；
- Philosophy 不创建新的 cluster synthesis 来修复已经被 Route 8a 关闭的 bounded retrieval 缺口。

## 1. Historical references

本 freeze **不要求批量重写历史 patch / hook**。

已有 `target_future_doc`、landing ledger 或 index 中的历史引用可保留，作为当时的工程规划记录。它们不得被 fresh session 解释成当前施工授权。

本规则只约束：

```text
new patch / hook created after 2026-08-16
```

## 2. New routing rule

新材料若仍有价值，优先按以下顺序落点：

```text
existing active owner
-> existing bridge / domain file
-> existing hardening index / hook ledger
-> no current landing target / parked with named trigger
```

不得因为：

```text
patch exists
hook pending
planned synthesis file missing
many patches share one target
```

就反推出：

```text
synthesis is needed
```

## 3. Reactivation gate

本 freeze 不是永久删除。只有出现以下任一条件，相关 synthesis target 才可重新授权：

1. 新的 **bounded baseline probe** 把对应 cluster 判为 Case B 或 Case C，并明确显示现有 owner / router 无法稳定承载该区分；
2. owner-level consistency audit 发现多个活跃 owner 对同一命题给出不可兼容答案，且局部修复不足；
3. 作者明确重新授权具名 synthesis 工作线。

重新授权时必须记录：

```text
trigger
scope
named target
exit condition
```

## 4. Convergence-phase WIP rule

当前进入 SRT Consolidation Phase。材料阅读可以继续，但新 hardening patch 只在以下三类情况新增：

1. 真正的新反例或 deletion / negative-control pressure；
2. 触发作者级裁决的边界问题；
3. 能直接形成 owner-level stable increment、且现有 patch / hook 无法承载的内容。

其他情况优先完成 SourceCard / Material Log / registry / index 所需留痕，或复用既有 patch / hook，不以新增编号作为进展指标。

下一阶段的主要治理指标是：

```text
owner-level contradiction down
pending hook backlog down
obsolete / parked / landed classification up
```

而不是 patch count up。