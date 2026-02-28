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
