---
id: SRT-PP-ALIGNMENT
type: guide
tags: [PredictiveProcessing, FEP, Mapping]
status: draft_v1
dependency: [SRT-CORE-14, SRT-REF-ONTOLOGY, SRT-AI-01]
---

# SRT × Predictive Processing 对接指南（简版）

## 1) 核心映射

| PP/FEP 概念 | SRT 对应 | 说明 |
|:--|:--|:--|
| Generative model | \(\hat G_\theta\) + \(L_2\) 先验 | 预测模板来自算子参数与收敛协议 |
| Prediction error | \(\Psi_f^{pred}\) 代理 | 误差是局部摩擦密度可观测代理 |
| Variational free energy | \(\mathcal F_{SRT}=Complexity-Accuracy\) | 与维持成本最小化耦合 |
| Hyperpriors | \(\Pi_{hyper}\subset\theta\) | 深层先验协议层 |
| Markov blanket | 具身边界 \(B_{MB}\) | 与脆弱性/闭包条件绑定 |

## 2) 三条判据

1. **存在判据**：
\[
\text{Exist}_{L_1}(X)\iff \Psi_f^{maint}(X)<\infty
\]

2. **连续性判据（生命-心智）**：
\[
\arg\min \mathcal F_{SRT}\Longleftrightarrow\arg\min \Psi_f^{maint}
\]

3. **AI 边界判据**：
\[
d>0\Rightarrow \mathcal V_{MB}>0\ \land\ \text{prediction failure induces physical risk}
\]

## 3) 常见误读与纠正

- “受控幻觉 = 一切主观任意” → 错。受控来自反馈约束与可支付代价。
- “预测成功 = 绝对真理” → 错。预测保证可维持性，不保证全域同构。
- “有马尔可夫毯形式 = 有意识” → 错。还需不可逆脆弱性与 d 值关切。
- “知觉内容 = 大脑内部预测模型内容” → 错。此为典型 **Category Error**：把“整体具身主体-环境关系层”的知觉事件，误缩减为“脑内子系统”的统计交易。
- “现实是受控幻觉”可作本体论结论 → 错。SRT 仅接受其**模型论弱式**：
  \[
  \Psi_f^{pred}\approx \text{error-signal proxy under }\hat G_\theta
  \]
  即预测误差是现实约束的局部代理，不是“现实可被任意内模替换”的许可。

> 注：参考 Evan Thompson (IAI, 2026-03-09) 对 PP 过度形而上化的批判；本指南采纳“具身-关系实在”解释路径，与 Gibson 式 affordance 视角一致。

## 【理论边界/防误用声明】
- 本文仅提供 SRT 与 PP/FEP 的术语对接，不替代具体实验设计与统计验证。
- 任何跨尺度外推必须声明 \(\theta,\rho,d\) 条件，禁止无条件泛化。
