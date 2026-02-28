# diff.md

> 用途：持续记录“外部材料 -> SRT 分析映射 -> 理论/实验引入”的增量 diff。
> 规则：每次新增一个小节；保持原文风格与格式；显式标注引入时间与材料标题/链接。

---

## [2026-02-28 10:44 GMT+8] 材料：工作流需求定义（用户指令）

### A. 本次建立的执行协议（无正文材料输入，先建框架）

- 输入：用户提供文本或链接。
- 输出：仅输出可落地的“增量 diff 内容”，并追加到本文件新小节。
- 分析主线：
  1. **SRT 相关度评估**（核心/中等/弱相关）
  2. **理论映射**（L_0/L_1/L_2, \hat{G}_\theta, d, \Psi_f, F, ii 等）
  3. **理论引入**（新增定义、推论、边界条件、反例约束）
  4. **实验引入**（可证伪假设、proxy 指标、最小实验设计）
  5. **一致性校验**（与 canonical 定义、术语和既有公理对齐）

### B. 统一输出模板（后续每次沿用）

```markdown
## [YYYY-MM-DD HH:mm GMT+8] 材料：<标题>（<链接或来源标识>）

### 1) 相关度评估
- 结论：核心相关 / 中等相关 / 弱相关
- 理由：...

### 2) 理论映射（SRT）
- 概念映射：...
- 方程/变量映射：...
- 与既有条目关系：...

### 3) 理论引入（建议写入）
- 引入项 T1：...
- 引入项 T2：...
- 适用边界：...

### 4) 实验引入（可证伪）
- 假设 Hx：...
- 指标与 proxy：...
- 最小实验：...
- 反证条件：...

### 5) 一致性与风格对齐
- 与 canonical d 定义对齐：通过 / 需修订
- 术语与符号对齐：通过 / 需修订
- 风格一致性：通过 / 需修订（说明）

### 6) 建议写入位置（文件级）
- `SRT/...`：新增/修改建议
```

### C. 备注

- 当前小节仅为协议初始化，不含外部材料实质映射。
- 下一条你给材料后，我将直接在本文件**新增下一小节**并给出正式 diff 内容。

---

## [2026-02-28 10:47 GMT+8] 材料：Why Everything in the Universe Turns More Complex（https://www.quantamagazine.org/why-everything-in-the-universe-turns-more-complex-20250402/）

### 1) 相关度评估
- 结论：**核心相关**。
- 理由：材料讨论“复杂度随时间上升”“功能信息驱动选择”“生物演化是更一般选择律的特例”，与 SRT 的 A7（适应度优先）、A8（生存概率定域）、A6（信息-存在强度）及 L_0/L_1/L_2 结构高度同构。

### 2) 理论映射（SRT）
- 概念映射：
  - 文中“复杂度增长趋势” → SRT 中 L_2 的累积固化与可行结构扩张。
  - “functional information（Szostak）” → SRT 的 \(ii\) 与可行动选择权重的耦合量。
  - “selection beyond biology” → \(\hat{G}_\theta\) 在多尺度（物理/生物/社会）的同构选择。
- 方程/变量映射：
  - 复杂度上升可写为趋势关系：\(\partial C/\partial t > 0\)（条件性，不作绝对单调）。
  - 与 A7 对齐：\(\hat{G}_\theta[\sigma]=\arg\max P(\mathrm{Fitness}|\sigma,\theta)\)。
  - 与 canonical d 对齐：复杂结构维持要求更高风险梯度承载，\(d\equiv\|\partial\mathcal{U}/\partial\mathcal{S}\|\) 上升时可支持更高功能层级。
- 与既有条目关系：
  - 对齐：`SRT/Core/SRT_Core_01_Axioms.md`（A6/A7/A8）
  - 对齐：`SRT/Core/SRT_Core_14_Dynamics_Scaling.md`（跨尺度同构）
  - 对齐：`SRT/D_VALUE_ALIGNMENT.md`（d 的 canonical 优先）

### 3) 理论引入（建议写入）
- 引入项 T1（条件复杂度律，建议新增到 Core Dynamics）：
  - **Ax-Comp-01 (Conditional Complexity Drift)**：在开放能流且存在可复制选择回路时，系统的功能复杂度期望值随时间上升：
  \[
  \mathbb{E}[C_f(t+\Delta t)-C_f(t)]>0 \mid (\Phi_E>0,\;\mathcal{R}_{rep}>0,\;\Psi_f\;\text{可支付})
  \]
- 引入项 T2（功能信息耦合项）：
  - 定义 \(I_f\) 为“达成功能阈值 \(\theta_f\) 的可实现状态密度对数比”，并将其并入 A6 的信息强度叙述，避免“复杂=随机”误读。
- 适用边界：
  - 不主张全宇宙全时段单调上升；局部可出现退化、重置、灾变回落。
  - 复杂度上升需能流与选择记忆，不满足时不成立。

### 4) 实验引入（可证伪）
- 假设 H-Comp-1：在非生物耗散系统中，若存在稳定功能约束，功能信息 \(I_f\) 的时间趋势显著为正。
  - 指标与 proxy：结构多样性指数、可重复功能达成率、稳态恢复时间。
  - 最小实验：对比“有功能约束 vs 无功能约束”的反应-扩散/材料自组装系统，跟踪 100+ 代迭代。
  - 反证条件：控制噪声与能流后，\(I_f\) 无显著上升或系统性下降。
- 假设 H-Comp-2：在任务生态中，提高风险梯度承载能力（d proxy 上升）可提升可维持复杂度上限。
  - 指标与 proxy：\(d\) 行为 proxy、任务层级深度、崩溃率。
  - 反证条件：d proxy 提升与复杂度上限无关。

### 5) 一致性与风格对齐
- 与 canonical d 定义对齐：**通过**（仅用 canonical 作定义，局部量为 proxy）。
- 术语与符号对齐：**通过**（L_0/L_1/L_2, \hat{G}_\theta, \Psi_f, ii）。
- 风格一致性：**通过**（采用“命题-方程-边界-证伪”结构）。

### 6) 建议写入位置（文件级）
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“Conditional Complexity Drift”小节。
- `SRT/Core/SRT_Experimental_Applications.md`：新增 H-Comp-1 / H-Comp-2。
- `SRT/SRT_Glossary.md`：新增术语“Functional Information Coupling (I_f)”。
