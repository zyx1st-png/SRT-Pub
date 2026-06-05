---
id: SRT-CORE-LAW-CORE-SYNC
type: governance
tags: [Governance, CrossCheck, CoreLaw, Core, Consistency]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
created: 2026-04-01
updated: 2026-06-05
---

# Core_Law/ ↔ Core/ 双向交叉检查协议

> **用途**：每次对 Core_Law/ 或 Core/ 任意一层做写入时，强制触发此协议。
> 目标：防止两层之间的系统性漂移，保持哲学锚点与形式化表达一致。

---

## 一、触发条件

以下任意一种情况发生，须执行本协议：

| 触发事件 | 检查方向 |
|---------|---------|
| 写入 `Core_Law/SRT_L0_Metaphysics.md` 任意词条 | → 检查 Core/ 对应形式化是否需更新 |
| 写入 `Core_Law/SRT_Core_Text_CN.md` 或 `Core_Law/SRT_Core_Text_CN_Euclid.md` 的主论证步骤 | → 检查 Core/ 对应方程/公理是否一致 |
| 写入 `Core/SRT_Core_22_Equations.md` 新方程 | → 检查 Core_Law/ 对应词条是否需补充 |
| 写入 `Core/SRT_Core_21_Formal_Axioms.md` 新公理 | → 检查 Core_Law/ L0 命题是否冲突 |
| 写入 `Core/SRT_Core_14_Dynamics_Scaling.md` 新内容 | → 检查 Core_Law/ 遮蔽/初心/真空期词条 |
| /srt-harden 会话产生写入决定 | → 双向检查 |

---

## 二、检查矩阵（已知映射关系）

| Core_Law/ 位置 | Core/ 对应位置 | 映射类型 |
|---------------|--------------|---------|
| L0_Metaphysics 遮蔽词条 | Core_14 §6（觉醒动力学）、Core_12b（L2滞后）、Core_13b（d值带宽）| 哲学描述 ↔ 形式机制 |
| L0_Metaphysics 具身词条 | Core_13a（κ_body双流耦合）、Reference_Dynamics §2（θ_binding）| 结构条件 ↔ 运作质量 |
| L0_Metaphysics 初心词条 | Core_14 §6.1（双盆地势能）| 方向场 ↔ 势能拓扑 |
| L0_Metaphysics 意识词条 | Core_13a（Ax-Op-02 Attention分解）、Core_14 §5（d值觉醒）| 候选窗口 ↔ 算子参数 |
| L0_Metaphysics 选择层级词条 | Core_22 Eq-Evo-03b（选择内再入通道）| 相变点 ↔ 方程架构 |
| Core_Text_CN family ⑦ / C2（势差 / 高阶意识候选窗口）| Core_22 Eq-Force-*（自由能/摩擦方程）| 哲学方向 ↔ 形式梯度 |
| Core_Text_CN family ⑧（遮蔽/真空期）| Core_14 §6.3（鞍结分叉）、Core_22 Eq-Evo-03（慢变量）| 干预逻辑 ↔ 分叉机制 |
| Reference_Axioms A1-A12 | Core_21 Ax-Core-A1-A12 | 直接对应，需保持编号一致 |
| Reference_Dynamics d/ρ/v定义 | Core_Bridge §0.1（符号寄存器）| 符号规范，需严格同步 |

---

## 三、检查步骤（每次写入后执行）

### 步骤 1：定位映射（1分钟）
根据上方矩阵，找到本次写入内容在另一层的对应位置。

### 步骤 2：一致性判断（5分钟）
对每个对应位置，判断以下三项：

- **方向一致**：两层描述的因果/结构方向是否相同？
- **条件一致**：一层的充要条件，另一层是否有相容表述？
- **无新增冲突**：本次写入是否引入了另一层没有对应的新承诺？

### 步骤 3：处理结论（二选一）

| 结论 | 行动 |
|------|------|
| 一致，无需改动 | 在写入记录中注明「跨层检查通过」|
| 存在张力或缺口 | 立即触发 `/srt-harden`（处理张力）或标记为「暂定锚 + 接口预留」|

---

## 四、冲突优先级规则

1. **Core_Law/ L0 形而上命题优先**：Core/ 的形式化不能违反 L0 四命题和五命题
2. **Core/ 精度可以上移修正 Core_Law/**：当 Core/ 的形式化更精确时，允许用其精度修正 Core_Law/ 的哲学表述（如本次 d值双参数修正）
3. **真实冲突须经 /srt-harden 钉住后再写入**：不允许「先写入、后硬化」

---

## 五、暂定锚登记表

当前已知暂定锚（写入了 Core_Law/ 但 Core/ 尚未形式化）：

| 概念 | Core_Law/ 位置 | Core/ 状态 | 优先级 |
|------|--------------|-----------|--------|
| 真空期（过渡态） | Core_Text_CN family ⑧、L0遮蔽词条 | Core_14 §6.3 已加限制注记，无正式定义 | 中 |
| A/B 相变临界值 $d_c$、$d_{\max}(\theta)$ | L0遮蔽词条 | Core_14 带宽方程有定性描述，无定量校准 | 低 |
| $\mathcal{M}_{meta}$ 函数形式 | Core_22 Eq-Evo-03b（已写入） | 标注 [H]，等 Philosophy/Ethics_Agency 对接 | 低 |
| 感知初心→本体论接近初心完整链 | L0初心词条（接口预留） | 未写入 | 中 |

---

## 六、与现有治理工具的关系

| 工具 | 本协议的关系 |
|------|------------|
| `Governance/SRT_Layer_Guard.md` | 互补：Layer_Guard 检查「写入了正确的层」；本协议检查「两层之间是否一致」|
| `Pipeline 4 / 周评` | 每周周评时执行一次完整扫描（见 §三），作为 Part A 的一个子项 |
| `/srt-harden` | 发现张力时的解决工具，不是预防工具 |
| `/srt-audit` | 单文件审计，可作为检查步骤 2 的辅助手段 |

---

## 七、更新规则

每次发现新的 Core_Law/ ↔ Core/ 映射关系，须更新第二节的映射矩阵。
每次消解一个暂定锚，须从第五节的登记表中移除，并在 Changelog 记录。
