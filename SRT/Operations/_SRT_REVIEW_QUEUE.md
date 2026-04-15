---
id: SRT-REVIEW-QUEUE
type: log
tags: [ReviewQueue, Gaps, Tensions, HumanReview]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-DAILY-REVIEW-PIPELINE, SRT-EQ-HYP-MAP]
---

# SRT 待人工审查队列

> 由 Pipeline 6（每日自动审查）写入。人工处理后将条目移至"已处理"区并标注处理方式。
>
> **优先级定义**：
> - **High**：影响理论完备性或跨域对齐的缺口/张力
> - **Med**：格式不一致或局部定义偏离规范，不影响主干逻辑
> - **Low**：文档完整性问题（占位内容、缺失章节节点），不阻塞推理

---

## 待处理（Pending）

| 发现日期 | 来源文件 | 问题描述 | 建议处理方式 | 优先级 | 状态 |
|---------|---------|---------|------------|--------|------|
| 2026-04-01 | `Core_Law/SRT_Core_Text_CN.md` / `Core_Law/SRT_Core_Text_CN_Euclid.md` / `Core_Law/SRT_Selection_Argument.md` | 中文主论证入口的文本角色裁决与入口层同步已完成；当前剩余高优先级问题收缩为：Euclid 版是否正式进入 registry / canonical 入口，以及 `Selection_Argument` 在不扩枚举下是否还需进一步降负担 | 继续按 `Governance/SRT_CORE_TEXT_ADJUDICATION_2026-04.md` 执行最终裁决；若暂不扩 `claim_mode` 枚举，则重点处理 Euclid 是否正式入入口 | High | Pending |
| 2026-03-11 | `_SRT_VERTICAL_INTEGRATION.md §4.5` | 原 d_collective 聚合框架已升级：F_collective 景观优先性定理确立后，需实证测量 $D_{eff}(F_{collective})$ 的代理指标 | 进入实验设计阶段；在 `_SRT_EQ_HYP_MAP.md` 补 Eq-Multi-03 的 proxy 测量方案 | Med | Pending |
| 2026-03-16 | `_SRT_EQ_HYP_MAP.md` / `SRT_EXP_TEMPLATE.md` / `scripts/g2_wikimedia_open_data_mvp.py` | Eq-LDP-01 / Eq-LDP-02 已推进为 `Partial`，G2-2 开放数据 MVP、脚本骨架与首轮 sample run 已具备，但样本仍过小，尚不足以拟合稳定 surrogate `I_{SRT}^*` | 扩展 pageviews 时间窗与 mapped pages；将 recentchanges API / EventStreams 样本扩到多冲击窗口，再判断 surrogate 稳定性 | Med | Pending |
| 2026-03-02 | `Core/SRT_Core_01_Axioms.md` | A10/A11 Part B 缺乏标准化"实验钩"节 | 参照 A7/A8 格式补充 H-ID 实验钩节 | Med | Pending |
| 2026-03-02 | `_SRT_EQ_HYP_MAP.md` | 经济学 Bridge 和演化 Bridge 尚未建立 | 列入下一季度工作项 | Med | Pending |
| 2026-03-09 | `Operations/_SRT_DAILY_REVIEW_PIPELINE.md` | 检测到占位模式关键词样例（`[待填写]/[TODO]/[待补充]/[占位]/TBD`） | 标注为流程说明文本，后续在规则中加入“示例白名单”避免误报 | Med | Pending |
| 2026-03-09 | 多文件（26） | 命中 d-value 定义段落但未显式引用 `_SRT_D_VALUE_CANONICAL.md` | 作为文档治理批处理项，在周评中统一补 canonical 引用 | Med | Pending |

---

## 已处理（Resolved）

| 发现日期 | 处理日期 | 来源文件 | 问题描述 | 处理方式 | 处理人 |
|---------|---------|---------|---------|---------|--------|
| 2026-03-16 | 2026-03-16 | `_SRT_EQ_HYP_MAP.md` | 主映射矩阵仍含 2 条 `Status=Gap`（Eq-LDP-01 / Eq-LDP-02） | 已通过 hydrodynamic-limit / macroscopic-fluctuation / dense-crowd 一手文献将 Eq-LDP-01 与 Eq-LDP-02 推进为 `Partial`；High 缺口清零，后续转为 Med 的数据管线执行问题 | Agent |
| 2026-03-05 | 2026-03-16 | `_SRT_EQ_HYP_MAP.md` | 主映射矩阵含 3 条 `Status=Gap`（Eq-Select-Thermo / Eq-LDP-01 / Eq-LDP-02） | 已通过 `q(L_1)` 三代理 + 文献锚点将 Eq-Select-Thermo 推进为 `Partial`；High 缺口收缩为 Eq-LDP-01 / Eq-LDP-02 两条群体尺度桥接问题 | Agent |
| 2026-03-02 | 2026-03-11 | `_SRT_VERTICAL_INTEGRATION.md §4` | d_collective 聚合公式未形式化（方案 A/B/C/D 待实验选择） | 框架层已解决：集体景观优先性定理（§4.5）+Eq-Multi-01/02/03 将 d_collective 定义为 $D_{eff}(F_{collective})$，旧聚合方案 A-E 降为历史近似记录；实证测量 proxy 列为新 Med 项 | Agent |
| 2026-03-02 | 2026-03-02 | 多文件 | d-value 定义三处分裂 | 新建 `_SRT_D_VALUE_CANONICAL.md` 统一规范 | Agent |
| 2026-03-02 | 2026-03-02 | `Neuroscience/SRT_Neuro_10_Advanced_Models.md` | 感受-摩擦循环定义 (T1) | 加入单向因果链声明 | Agent |
| 2026-03-02 | 2026-03-02 | `Core/_SRT_Core_Bridge.md` | L₂ 语义漂移 (T2) | 添加 L₂ 热力学封闭条件 §1.3.3 | Agent |
| 2026-03-02 | 2026-03-02 | `AI/_SRT_AI_Bridge.md` | AI 屏障"永久 vs 可突破"歧义 (T3) | 添加双层区分（工程性 vs 原则性） | Agent |
| 2026-03-02 | 2026-03-02 | `Spirituality/_SRT_Spirit_Axioms.md` | Ω 拓扑极限与具身公理冲突 (T4) | 添加边界声明（热力学极限类比） | Agent |
