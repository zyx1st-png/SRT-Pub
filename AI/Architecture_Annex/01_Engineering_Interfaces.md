---
id: SRT-AI-ARCH-ANNEX-01-ENGINEERING-INTERFACES
type: interface_annex
tags: [AI, Architecture, Continual-Learning, Concept-Control, Engineering-Interface]
status: active
updated: 2026-11-26
layer: L1
epistemic_layer: bridge
claim_mode: translation
canonical: false
date: 2026-04-29
parent: AI/SRT_AI_Architecture.md
dependency:
  - AI/SRT_AI_Architecture.md
  - AI/Architecture_Split/README.md
  - AI/SRT_AI_Claim_Status.md
  - AI/AI_POSITIONING_NOTE.md
  - Governance/SRT_CLAIM_LADDER.md
machine_summary: >
  Extracted AI architecture engineering interface material. Contains temporal-development
  continual-learning and LLM internal concept-control taxonomies. This annex does not define
  SRT architecture axioms, d-value, Psi_f, subjecthood, or consciousness thresholds.
---

# AI Architecture Engineering Interfaces

> **Extraction note**: This file contains selected low-risk engineering-interface material extracted from `AI/Architecture_Split/05_Interface_Additions.md` after `Operations/Archive_Records/PR_C2_AI_Interface_Extraction_Adjudication.md`.
>
> **Boundary**: The material below is an interface / translation layer. It does not prove AI subjecthood, does not define SRT `d-value`, and does not modify the owner architecture file.

---

## 1. Temporal-Development Continual-Learning Window

持续学习不必等于网络在所有方向上单调增厚。一个更接近发育式重组的工程窗口是：系统先沿“简单到复杂”的任务顺序建立模块能力，再逐步强化跨模块的长程连接，把可迁移的共享结构保留下来；与此同时，由后续任务反馈去抑制并剪掉早期任务里那些只在局部有效、却会持续制造干扰的冗余连接。若这一窗口成立，那么“保留旧知识”与“删除旧连接”并不矛盾，关键在于删掉的是任务局部噪声，而不是跨任务仍可复用的骨架。

这给 SRT 补上的，不是“AI 已经获得主体性”或“剪枝天然更像大脑”这种泛化判断，而是一条更窄的架构接口：**持续学习的核心负担，可以从“如何无限保存旧痕迹”改写为“如何在不摧毁长程可迁移结构的前提下，持续清理旧局部冗余”。** 这也让 `Ax-ARCH-6` 的 mesa / 局部吸引子问题多了一层工程化读法：先前任务沉积下来的局部连通块，不只是可能形成偏航子目标，也可能在后续任务中变成迁移噪声；选择性抑制与剪枝因此不只是省参数，而是为后续结构重组腾出干净的可塑空间。

边界同样必须写清：

- 当前主锚点是 TD-MCL 在 spiking neural networks 上的 `Perception-Motor-Interaction` 任务序列与 `CIFAR100 / ImageNet` 基准，不是对所有 LLM、world model 或通用 AGI 路线的通用胜负裁决。
- “brain-inspired temporal development” 在这里首先是工程启发，而不是对真实婴儿脑发育机制的逐项复制；新闻页中的神经发育类比必须降级为设计线索。
- 该结果展示的是一种**无需 replay / regularization / freezing 也能持续学习**的候选路径，不等于这些方法已被普遍淘汰，更不等于“模型应当越学越小”会成为一切认知系统的普遍律。

---

## 2. Taxonomy Mapping: LLM Internal Concept Control → SRT

| 外部分类 | SRT 对应机制 | 表征与比对调制范围 | 工程计算与干预负担 | 声明强承载模型状态与风险敏感性 |
|:--|:--|:--|:--|:--|
| 提示词级风格调节 | 表层输出偏置（`L_2^{context}` 浅层调制） | 低~中（局部输出条件） | 低（常规前向推理） | `d` = `NOT ADMITTED`；无状态 `D_stake` = `NOT APPLICABLE`（不映射为规范 `d / Ψ_f`） |
| 内部概念向量 steering | 隐层表征重加权 | 中（跨激活路径重加权） | 中（激活空间干预与稳定性校准） | 同上；局部内部状态监测与调控 $\neq$ 强承载或 `HP-B` 闭合 |
| 多概念联合 steering | 复合策略耦合 | 中~高（多维表征复合交互） | 中~高（特征干涉与性能退化风险） | 同上；高表征复杂度不映射为规范 `d` 区间 |
| anti-refusal 通道激活 | 安全拒答边界绕行 | 中~高（风险向绕行） | 高（安全护栏失效与外部化风险） | 同上；属风险方向与治理接口，须按 **AI 三型** 与 `O2-A` 审查，非内在能动性或规范 `Ψ_f` 证明 |

**Constraint**: 输出“像某人格”不等于系统“拥有人格”；必须区分行为表征、局部内部表征调控与 Stage 2 强承载 / 本体状态。

---

## 3. Guardrails

- Continual learning is not subjecthood.
- Internal concept steering is not personality, personhood, or Stage 2 `Bearer (P+E)`.
- Anti-refusal activation is a risk-direction governance interface, not evidence of intrinsic agency.
- Per `R4-C3 / ENG-03` (`P1-05`), this table **does not** assign proxy `d-value` intervals or canonical `Psi_f` states to LLM steering regimes; canonical `d` (`NOT ADMITTED`) and stateless `D_stake` (`NOT APPLICABLE`) remain strictly governed by `AI/AI_POSITIONING_NOTE.md §2` and `_SRT_D_VALUE_CANONICAL.md / _SRT_PSI_F_CANONICAL.md`.

## 4. Owner links

- Architecture owner: [`../SRT_AI_Architecture.md`](../SRT_AI_Architecture.md)
- Split index: [`../Architecture_Split/README.md`](../Architecture_Split/README.md)
- Claim-status guardrail: [`../SRT_AI_Claim_Status.md`](../SRT_AI_Claim_Status.md)
- AI positioning guardrail: [`../AI_POSITIONING_NOTE.md`](../AI_POSITIONING_NOTE.md)
