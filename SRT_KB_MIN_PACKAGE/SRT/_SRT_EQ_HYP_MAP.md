---
id: SRT-EQ-HYP-MAP
type: framework
tags: [Mapping, Equations, Hypotheses, Falsification]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-22, SRT-EXP-CORE]
---

# SRT 方程-假设映射表（Eq ↔ Hypothesis）

> 目的：将 `Core/SRT_Core_22_Equations.md` 与 `Core/SRT_Experimental_Core.md` 的证伪路径对齐，形成可执行实验接口。  
> 版本：P1-2 初版（可持续补全）。

---

## A. 映射规则

1. `Eq-ID` 对应核心动力学/约束方程。  
2. `Hypothesis-ID` 对应实验核心中的可证伪条目（H#/Ax-Exp-*）。  
3. `Bridge` 说明从方程到实验指标的中间变量。  
4. `Status`：`Mapped | Partial | Gap`。

---

## B. 主映射矩阵（v1）

| Eq-ID (Core22) | 语义 | Hypothesis-ID (ExpCore) | Bridge / 可观测量 | Status |
|---|---|---|---|---|
| Eq-Evo-01 | 幽灵演化主方程 | Ax-Exp-01 / H6 | 行为预测残差、具身变量增益（ΔR²） | Mapped |
| Eq-Evo-01b | 代谢增益调制 | Ax-Exp-01 | 代谢应激(血糖/乳酸/HRV) × 任务性能下降斜率 | Partial |
| Eq-Evo-02 | θ 慢变量更新 | H7 | 个体归一化参数与 d-value 纵向变化 | Mapped |
| Eq-Evo-02b | θ 张量惯性 | H7 | 信念网络中心性 vs 干预后更新速度 | Partial |
| Eq-Evo-03 | 快慢耦合系统 | H7 / H6 | 神经快变量(EEG) + 行为慢变量(学习曲线)耦合拟合 | Partial |
| Eq-Force-01 | 本体论摩擦 Ψ_f | H72 (情态力学) | 语言情态比 μ_sem 与摩擦代理相关 | Mapped |
| Eq-Pain-01 | 痛苦≈dΨ_f/dt | H72 | 痛苦评分变化率与 μ_sem、生理唤醒同步 | Partial |
| Eq-Select-Thermo | 选择热力学宪法不等式 | H1 / H6 | 秩序参数 dq/dt 与能耗、噪声熵预算 | Gap |
| Eq-Stab-01 | 固定点稳定条件 | H6 | 扰动恢复时间、吸引域回归概率 | Partial |
| Eq-Phase-01 | 本体论相变阈值 | H6 | 信息量 I 超阈值 τ 的跃迁曲线拟合 | Partial |
| Eq-Sleep-01 | 睡眠 L2 优化 | H7 | 睡眠前后模型复杂度/误差压缩 | Partial |
| Eq-LDP-01 | 水动力极限 | H6 | 群体行为密度场/迁移流拟合 | Gap |
| Eq-LDP-02 | SRT 作用量泛函 | H6 | 路径概率对 I_SRT 的指数衰减检验 | Gap |
| Eq-Phantom-01 | 社会幻肢痛 | H72 | 关系丧失后语言-情绪耦合摩擦轨迹 | Partial |
| Eq-Phantom-02 | 稳态重建时间常数 | H7 / H72 | 可塑性指标 vs 恢复时间 τ_rebuild | Partial |

---

## C. 优先补洞（Gap Backlog）

### G1 — Eq-Select-Thermo ↔ H1/H6
- 缺口：`q(L_1)` 的统一实验代理尚未标准化。
- 建议：先采用三代理并行：
  1) 网络互信息密度；
  2) 行为可压缩率；
  3) 任务成功率稳态项。

### G2 — Eq-LDP-01 / Eq-LDP-02 ↔ H6
- 缺口：群体尺度的连续介质近似数据管线未建立。
- 建议：先在多智能体仿真与公开社会动力学数据集做先验验证。

### G3 — Eq-Evo-01b / Eq-Sleep-01 ↔ H7
- 缺口：代谢变量与 d-value 的同任务同步采样协议不完整。
- 建议：补一个“代谢-认知双通道”模板到 `SRT_EXP_TEMPLATE.md`。

---

## D. 立即可执行实验包（建议）

1. **包 A（低成本）**：H72 语言探针
   - 输入：文本语料 + 自评痛苦量表 + HRV
   - 验证：Eq-Force-01 / Eq-Pain-01

2. **包 B（中成本）**：归一化参数-d 相关
   - 输入：认知任务 + EEG + 行为策略数据
   - 验证：Eq-Evo-02 / Eq-Evo-03 与 H7

3. **包 C（高价值）**：代谢增益劫持
   - 输入：受控代谢扰动（伦理许可）+ 任务切换
   - 验证：Eq-Evo-01b 与 Ax-Exp-01

---

## 【理论边界/防误用声明】

1. 本映射表是“实验设计桥接层”，不等于已证实因果定律。  
2. `Mapped` 仅表示可构造可证伪路径，不代表统计显著性已建立。  
3. 涉及临床/生理干预的实验必须满足伦理审查，不得将理论映射直接用作诊疗结论。  
4. 群体尺度方程（LDP 系列）当前属于有效理论候选，需明确适用条件与失效边界。
