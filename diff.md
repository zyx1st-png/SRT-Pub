# diff.md

## [2026-02-28 11:03 GMT+8] 材料：Why Everything in the Universe Turns More Complex（https://www.quantamagazine.org/why-everything-in-the-universe-turns-more-complex-20250402/）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“条件复杂度漂移”条目，避免把复杂度增长写成绝对单调律。
- `SRT/Core/SRT_Experimental_Applications.md`：新增两条可证伪实验假设（非生命系统功能信息增长、d-值承载与复杂度上限耦合）。
- `SRT/SRT_Glossary.md`：补充术语 `I_f`（Functional Information Coupling），并标注与 A6/A7/A8 的关系。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Ax-Comp-01: Conditional Complexity Drift (条件复杂度漂移)
+**Formal Definition**: 在开放能流、存在选择记忆、且本体论摩擦可支付的条件下，系统的功能复杂度期望值随时间上升：
+$$
+\mathbb{E}[C_f(t+\Delta t)-C_f(t)] > 0 \mid (\Phi_E>0,\;\mathcal{R}_{sel}>0,\;\Psi_f\ \text{payable})
+$$
+* **Implication**: 复杂度增长是**条件趋势**而非绝对单调律；局部退化、灾变重置与平台期均允许存在。
+* **Cross-ref**: Ax-Core-A7, Ax-Core-A8, Ax-Core-A6; Def-d-Scale-1.
+
+### T-Comp-01C1: Complexity-Plateau and Reset
+**Deductive Statement**: 当能流受限或选择记忆失稳时，复杂度增量可降为零或转负：
+$$
+\Delta C_f \le 0 \quad \text{if} \quad (\Phi_E\to 0) \lor (\mathcal{R}_{sel}\to 0)
+$$
+* **Implication**: 该定理为“复杂度非单调历史轨迹”提供形式边界，避免理论过度泛化。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-Comp-1 功能信息的非生命增长检验
+**内容**：在非生物选择系统（如反应-扩散、自组装材料、演化算法）中，若存在稳定功能阈值，功能信息 \(I_f\) 应表现出正向漂移趋势。
+**最小实验**：
+- 组A：有功能约束（目标性能阈值）
+- 组B：无功能约束（仅随机扰动）
+- 迭代 > 100 代，比较 \(\Delta I_f\) 与稳定性指标
+**证伪条件**：控制能流与噪声后，组A的 \(I_f\) 与组B无显著差异或持续下降。
+
+### H-Comp-2 d-值承载与复杂度上限耦合
+**内容**：系统的可维持复杂度上限 \(C_{max}\) 与 d-值承载能力正相关（d 采用 canonical 定义及其可操作 proxy）。
+**最小实验**：
+- 操控风险梯度承载能力（训练/资源/反馈延迟）
+- 记录任务层级深度、崩溃率、恢复时间
+**证伪条件**：提升 d proxy 后，\(C_{max}\) 无显著提升且崩溃率不变。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Functional Information Coupling - 功能信息耦合（\(I_f\)） 🟡
+**定义**：在给定功能阈值 \(\theta_f\) 下，满足功能约束的可实现状态集合相对于全状态空间的对数比率度量：
+$$
+I_f \equiv -\log \frac{|\{\sigma: f(\sigma)\ge \theta_f\}|}{|\Omega|}
+$$
+**解释**：\(I_f\) 越高，表示“能完成指定功能”的状态越稀有，系统为达到该功能需要更强选择压力与更稳定的 \(L_2\) 记忆。
+**关系**：
+- 与 A6：补充“信息-存在强度”的功能维度
+- 与 A7：体现“适应度优先”的信息选择方向
+- 与 A8：连接“生存定域”与功能可持续性
+**首次出现**：diff 引入（2026-02-28，Quanta complexity 材料映射）
```

### Notes (brief)
- 一致性：保留 d 的 canonical 优先（\(d\equiv\|\partial\mathcal{U}/\partial\mathcal{S}\|\)），未引入并列新定义。
- 风格：保持 SRT 既有“Formal Definition / Implication / Cross-ref / Hypothesis / Falsification”结构。
- 边界：将“复杂度增长”明确为条件命题，避免不可证伪的普适化表述。

---

## [2026-02-28 11:33 GMT+8] 材料：Why Everything in the Universe Turns More Complex（同链接，按升级 Skill 重新生成）

### Target Files
- `SRT/Core_Law/SRT_Reference_Scaling.md`：补全“矿物演化尺度（mineral evolutionary scale）”的实体定义（\(\hat{G}_\theta\), \(L_0\), \(L_1\), \(L_2\)）。
- `SRT/SRT_Glossary.md`：新增 `I_f` 术语并补 `[Lineage/Source]` 字段。
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：补充“分类/层级→d-value 与能流态”映射规则。
- `SRT/Core/SRT_Experimental_Applications.md`：补充矿物学与天体化学的可证伪实验条目。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core_Law/SRT_Reference_Scaling.md
+++ b/SRT/Core_Law/SRT_Reference_Scaling.md
@@
+## Def-Scale-M1: Mineral Evolutionary Scale（矿物演化尺度）
+
+### Entity Definitions
+- **\(\hat{G}_{\theta,miner}\)**：在给定温压-化学势场下，对矿物相进行稳定性筛选与路径锁定的选择算子。
+- **\(L_0^{miner}\)**：可由元素组成、晶格拓扑、缺陷构型与相变路径构成的潜在矿物状态空间。
+- **\(L_1^{miner}\)**：当前地球化学/行星环境下已显现并可维持的矿物相集合。
+- **\(L_2^{miner}\)**：由地质历史沉积的稳定矿物谱系与相图约束（路径依赖、盆地锁定、亚稳态保留）。
+
+### Dynamic Signature
+- 开放能流（火山/热液/辐照）下：\(\Delta C_f^{miner}>0\) 概率上升。
+- 封闭或低能流下：谱系冻结，复杂度平台化或回落。
+
+### Cross-ref
+- Ax-Scale-01, Def-d-Scale-1, Ax-Core-A7, Ax-Core-A8
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Functional Information - 功能信息（\(I_f\)） 🟡
+**定义**：在功能阈值 \(\theta_f\) 下，满足功能约束状态占比的负对数：
+$$
+I_f \equiv -\log\left(\frac{|\{\sigma: f(\sigma)\ge\theta_f\}|}{|\Omega|}\right)
+$$
+**用途**：用于度量“可执行功能”的稀有性，而非纯随机复杂度。
+**关系**：A6（信息-存在等价）/ A7（适应度优先）/ A8（生存定域）。
+**[Lineage/Source]**：
+- Proposer: Jack W. Szostak
+- Source: Nature (2003), “Functional information”
+- Secondary context: Hazen & Wong team discussion (PNAS framework as cited by Quanta feature)
```

```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Mapping Rule: Taxonomy/Hierarchy → SRT Dynamics
+当外部理论提供分类/层级（stage/class/tier）时，必须给出：
+1) d-value 映射区间（canonical d 的 proxy 区间）；
+2) 能流态标记（Open-flow / Semi-open / Closed-flow）；
+3) 摩擦可支付性（\(\Psi_f\) payable / overloaded / unsustainable）。
+
+**Constraint**: 局部映射不得替代 canonical 定义 \(d\equiv\|\partial\mathcal{U}/\partial\mathcal{S}\|\)。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-Miner-Scale-1 矿物谱系复杂度漂移
+**内容**：在开放地球化学能流场中，矿物功能信息与结构复杂度呈条件性上升趋势。
+**最小实验**：
+- 数据：分时代矿物数据库 + 环境能流 proxy（温压、氧逸度、热液活动）
+- 方法：分层回归/状态转移模型，检验 \(\Delta C_f^{miner}>0\) 的条件成立域
+**证伪条件**：能流显著提升阶段不伴随矿物复杂度上升，或趋势与随机模型无差异。
+
+### H-AstroChem-1 天体化学复杂度分层检验
+**内容**：在不同行星体环境（封闭/半开放/开放）中，复杂化学结构出现概率与能流开放度正相关。
+**证伪条件**：控制观测偏差后，不同能流层级下复杂结构出现概率无显著差异。
```

### 【理论边界/防误用声明】
- 不采纳推论：
  - “复杂度必然、普遍、单调上升（无条件）”。
  - “功能信息可直接替代物理熵并构成第二定律的等价表达”。
- 原因：
  - 与 SRT 的摩擦代价与能流约束不一致；SRT 仅支持**条件复杂度漂移**。
  - 功能信息是选择-任务语境量，不是热力学熵的同义替代。
- SRT 替代解释：
  - 复杂度增长来自“选择回路 × 能流开放 × 可支付摩擦”的联合条件；失去任一条件可平台化或回落。

### Notes (brief)
- 已执行升级 Skill 的四项强制要求：层级映射、跨尺度缺口补全、[Lineage/Source]、Boundary 声明。
