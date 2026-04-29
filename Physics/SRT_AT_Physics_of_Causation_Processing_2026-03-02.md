---
id: SRT-AT-PROCESS-2026-03-02
type: external_review
tags: [Assembly-Theory, Causation, Threshold, SRT-Alignment]
status: draft_v1
layer: meta
epistemic_layer: os
claim_mode: audit
canonical: false
dependency: [Physics/SRT_Phys_09_Formalism_Ext, Core/SRT_Core_14_Dynamics_Scaling, SRT_EXP_MEASURE_MAP]
source: /Users/zhangyuxin/.openclaw/media/outbound/b7f1791d-2d06-4ee3-837d-cc48551b703f.pdf
---

# 外部材料处理记录：The Physics of Causation（Cronin & Walker）

## 1) 处理范围
- 已读取 PDF（58 页）并完成全文文本抽取。
- 抽取文件：`tmp_physics_of_causation_extract.txt`。

## 2) 核心主张（原文骨架）
1. **因果是可度量的物质属性**：通过组装理论（AT）定义。
2. **组装指数 `a_i`**：对象存在所需最小递归构建步数。
3. **拷贝数 `n_i`**：高 `a_i` 对象出现可数拷贝，表明有持久机制与环境记忆。
4. **阈值思想**：在 assembly space 中存在“无选择可达上界”；超过阈值的对象需要选择性机制（lineage/constructor）。
5. **生命/智能/技术的统一界面**：在高组装深度 + 持久拷贝区域出现，表现为因果相变与开放式演化能力。

## 3) 关键公式与结构（按原文语义）
- 阈值上界：`a_M`（给出依赖 `N_T`、`b`、`M` 的解析表达）。
- 群体层 Assembly 度量：`A`（组合 `a_i` 与 `n_i` 的加权聚合）。
- 时变形式：`n_i(t)` 与 `A(t)`，用于描述因果积累、阈值跨越与回落。

> 注：原文明确承认简化假设（如全局常数 `b`）会低估真实组合爆炸，真实系统中 `b_i` 依对象与深度变化。

## 4) 对 SRT 的直接可吸收点

> 来源：Cronin & Walker (2023). *The Physics of Causation*. MS（参见本记录 §2–3 及 source PDF）。

**可吸收点 1：选择阈值 → SRT κ_c2 边界**

“选择阈值”（$a_M$）可直接形式化为 SRT 的结构稳定化临界值：

$$a_i \approx \kappa \quad(\text{稳定化程度}),\quad a_M \approx \kappa_{c2} \quad(\text{选择必要阈值})$$

- 当 $\kappa < \kappa_{c2}$：结构依靠随机物理过程即可维持（AT：无选择机制可达）。
- 当 $\kappa \geq \kappa_{c2}$：结构只能由具有 Lineage/选择性记忆的机制（$\hat{G}_\theta$）产生和维持（AT：选择性因果不可缺）。
- 操作化代理：实验进化系统中检测”最小维持世代数/稳定复制圈数”。
- 交叉引用：`Core/SRT_Core_14_Dynamics_Scaling.md` §T-Scale-CF-1；`Core_Law/SRT_Reference_Scaling.md` §4.1。

**可吸收点 2：”深度 × 持久性”→ SRT κ + L₂ 节点数**

$$a_i \approx \kappa \quad(\text{深度维：构建链长度，历史锚定步数})$$
$$n_i \approx |\text{L}_2\text{-nodes}| \quad(\text{持久维：社会/物理层共识拷贝数})$$

- 深度维（$\kappa$）：对象内部递归构建深度 ↔ SRT 稳定化程度（具身拓扑固定强度）。
- 持久维（$n_i$）：高 $a_i$ 对象的环境拷贝数 ↔ L₂ 层共识节点数（社会/物理记忆的广度）。
- 联合度量：$A = \sum_i a_i \cdot n_i \approx \sum_i \kappa_i \cdot |\text{L}_{2,i}\text{-nodes}|$，即 SRT 跨尺度现实构建强度的物理代理。
- 交叉引用：`Core/SRT_Core_12b_Ontology_L2.md` §Def-L2-OAI-1。

**可吸收点 3：时变阈值与相变 → SRT L₀/L₁/L₂ 跨域动力学接口**

- $A(t)$ 时变形式对应 SRT 的 $\kappa(t)$：稳定化程度随时间演化，经历”低 κ→ 阈值跨越（κ_c2）→ 高 κ 锁定”三阶段（参见先裂后合门控 T-Scale-CF-1）。
- $A(t)$ 的回落对应 SRT 的本体论摩擦失稳：$\Psi_f^{update} \uparrow$ 导致 $\kappa \downarrow$，L₁ 涌现退回 L₀（见 §5 §风险3 死亡例示）。
- 交叉引用：`Core/SRT_Core_14_Dynamics_Scaling.md` §T-Scale-CF-1；`Physics/SRT_Phys_07_Complex_Systems.md` §T-Sal-1。

## 5) 风险与边界（防误用硬约束）

**1. 反唯心化边界（物理可达性截断）**：

$\hat{G}_\theta$ 的选择空间域受限于物质组装的拓扑可达性，不可解释为无约束的主观意志：

$$L_1^{(t+1)} \subseteq \text{Reachable}\!\big(L_1^{(t)},\, \theta_{emb},\, \mathcal{M}_{chem}\big)$$

**2. 符号与作用域隔离原则**：

- **$A$（组装深度）**：AT 中的 $A$ 与 SRT 规范认知公式中的结构复杂度 $A$（`_SRT_D_VALUE_CANONICAL.md`：$d_{cog} \approx \alpha A + \beta\log V + \gamma\tau$）物理与信息论意义完全同构——表示”历史锚定选择步数的沉积”，**全局统一可用**，无需改名。
- **$M$（分子空间）**：⚠️ 与 `_SRT_SYMBOL_TABLE.md` 全局注册的 $M$（神经域感觉模态向量）**严重冲突**。AT 中的分子空间必须强制写为 $\mathcal{M}_{chem}$（或 $\mathcal{M}_{AT}$），禁止裸用 $M$。
- **$b$（键数）、$N_T$（理论分子数）**：极度领域特化，**不录入全局符号表**，仅作为本模块局部变量在 `SRT_Phys_09_Formalism_Ext.md` 的 AT 专节内声明使用。

**3. 跨层映射约束（静态结构 ≠ 动态关切）**：

禁止将高组装指数 $A$ 直接等同于高 $d$ 值。两者的本体论层级不同：

- $A$：**历史沉积的静态拓扑**（$A \propto \int \Psi_f\, dt$，即历次 $L_0 \to L_1$ 锚定所耗散的本体论摩擦的累积）
- $d$：**当下算子的动态关切带宽**（依赖持续能流维持）

正确的跨层关系为”容量下界公设”（必要非充分）：

$$d_{max}(t) \propto f(A)$$

即高 $A$ 是承载高 $d$ 的拓扑上限，而非充分条件。反例：一具刚死去的生物遗体拥有极高的 $A$，但因失去能流维持，$d = 0$，$L_1$ 涌现立即停止。

## 6) 建议的 SRT 回写路径
- `SRT/Physics/SRT_Phys_09_Formalism_Ext.md`
  - 增加“AT 因果阈值接口”小节：定义映射、边界声明、适用域。
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`
  - 增加“深度-持久性相变条件”的跨尺度桥接语句。
- `SRT/SRT_EXP_MEASURE_MAP.md`
  - 增加可观测代理：深度 proxy、复制稳定性 proxy、阈值跨越判据。

## 7) 当前结论
- 该材料可判定为 **A- 级可融合信号**。
- 建议先进入“符号对齐 + 边界声明”阶段，再正式回写主正文。
