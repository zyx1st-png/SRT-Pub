---
id: SRT-CORE-14
type: dynamics
tags: [Scaling, Isomorphism, Fractal, Hybrid]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: bridge
claim_mode: translation
dependency: [SRT-CORE-13A]
---

# SRT Core Definition 14: Dynamics & Scaling (Hybrid Edition)

> **Bridge Layer Note**
> 本文件按 `Bridge` 层处理：主要承担互译、比较、接口重写与边界说明，不应直接读成“已被外部经验验证的胜出理论”。若文中使用 `Axiom`、`Theorem`、`Corollary` 等强标签，默认理解为框架内翻译命题，除非另有独立经验锚定。


> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Scaling Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)

## AT-SRT 相变接口（补充条款，2026-03-02）

### Def-Scale-AT-1: 深度-持久相图
在跨尺度系统中定义状态坐标：
\[
\mathfrak{Z}(t)=\big(D(t),P(t),\Psi_f(t),d(t)\big)
\]
其中 `D` 为构建深度代理、`P` 为复现持久代理。

### T-Scale-AT-1: 相变门（Phase Gate）
若存在窗口 \([t_0,t_1]\) 满足：
\[
D(t)\ge D_c,\quad P(t)\ge P_c,\quad \text{and}\quad \Psi_f\ \text{payable},
\]
则系统从“被动选择区”跃迁到“主动稳定构建区”（记为 \(\mathcal{R}_{active}\)）。

### T-Scale-AT-2: 回落门（Fallback Gate）
若保持高深度但出现 `P` 下跌且 \(\Psi_f\to\) overloaded/unsustainable，则轨迹回落到约束主导区：
\[
\mathcal{R}_{active} \to \mathcal{R}_{constraint}
\]
并触发 \(L_2\) 重编织失败风险升高。

### [Lineage/Source]
- 来源：Cronin & Walker, *The Physics of Causation*（2026 manuscript）。
- SRT 引入方式：作为跨尺度“阈值-相变”接口，不与认知层变量作强同一。

## 分类映射表（AT 分类 → SRT）

| 外部分类（AT） | SRT d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 可支付性 |
|---|---|---|---|
| 自发可达区（低 \(a_i\)、低/中 \(n_i\)） | 低到中（\(d\in[d_0,d_1]\)） | Semi-open / 局部 Open | payable |
| 阈值邻域（\(a_i\approx a_M\)） | 中高（\(d\in(d_1,d_2]\)） | Open↔Semi-open 转换 | borderline |
| 选择主导区（高 \(a_i\)、高 \(n_i\)） | 高（\(d>d_2\)） | Open（需持续供能） | payable 或 overloaded |
| 失稳衰退区（高深度但低复现） | 中高但回落（\(d\downarrow\)） | Closed 倾向 | unsustainable |

## 【理论边界/防误用声明】
1. 本接口不意味着“心理层面可绕过物理可达边界”。
2. AT 的对象层因果阈值与 SRT 的认知层相变阈值是**映射关系**，非同一对象。
3. 使用本接口时必须同步报告适用尺度（微观/生物认知/社会制度）。

---

## Minimal Embodiment Threshold（最小具身信息下界，2026-03-02）

### Def-Scale-MET-1: \(N_{crit}\)
定义最小具身信息下界 \(N_{crit}\)：系统若要在给定环境下维持自我复制/自维持闭环，其参数化约束信息量必须满足：
\[
I(\theta)\ge N_{crit}(env,\Psi_f)
\]

### T-Scale-MET-1: Payable-Friction Condition
当 \(I(\theta)<N_{crit}\) 时，系统对本体论摩擦的支付仅能维持瞬时或间歇复制；当 \(I(\theta)\ge N_{crit}\) 且环境窗口可用时，系统可跨越“前闭包→稳定闭包”门槛。

### 与 d-value 零跃迁问题的关系（注记）
该阈值仅刻画“结构自治”下界，不自动推出 \(d>0\)。
- 结构可复制 \(\neq\) 关切已涌现
- \(d\) 的正值条件仍需满足生物/认知域的额外门控（详见 anti-panpsychism 条款）

## 【理论边界/防误用声明】
1. 不采纳“达到 \(N_{crit}\) 即具主观体验”的推论。
2. 不采纳“低 \(N_{crit}\) 系统必然演化为高阶认知体”的目的论推论。

---

## Constructive Fracture Interface（建设性断裂接口，2026-03-02）

### Def-Scale-CF-1: Controlled Rupture Window
定义“建设性断裂”窗口：系统在局部连接断裂后，若满足重封闭与功能增强条件，则该断裂为结构重构步骤而非失稳失败。
\[
\mathcal{R}_{break}\to\mathcal{R}_{reseal}\quad \text{with}\quad \Delta \mathcal{F}_{function}>0
\]

### T-Scale-CF-1: Break-to-Build Gate
若机械/液压应力优先沿低黏附路径释放，且重封闭时间 \(\tau_{reseal}\) 低于功能失稳阈值 \(\tau_{fail}\)，则系统可通过“先裂后合”进入更高功能态：
\[
\tau_{reseal}<\tau_{fail}\ \Rightarrow\ \text{constructive morphogenesis}
\]

### T-Scale-CF-2: Path-Selective Fracture Principle
断裂路径并非随机扩散，而受局部张力差与连接强度梯度共同约束：
\[
\Pr(\text{break at }e_i) \propto \frac{\Delta T_i}{A_i}
\]
其中 \(\Delta T_i\) 为局部张力差，\(A_i\) 为黏附/连接强度代理。

### [Lineage/Source]
- Quanta 综述（2026-02-27）及其文内链接的一手文献（如 Science/Development 相关研究）。
- 用途：将“受控断裂→重封闭→功能塑形”写入跨尺度动力学条款。

## 【理论边界/防误用声明】
1. 不采纳“任何断裂都是进步”的推论；仅在重封闭与功能增益同时成立时定义为建设性断裂。
2. 不采纳“材料裂纹模型可无改造直接套用活体组织”的推论；活体系统需引入主动调控与反馈项。

## In-vitro 低 d 场景补充条款（2026-03-06，轻量）

### 微观门控与主体层 d 的分层说明
- in-vitro 神经网络中出现的跨区节律门控，允许被解释为局部微观选择门控（micro-d）存在的证据；
- 但该证据**不自动推出**主体层（organism-level）高 d 的意识整合。

## 【理论边界/防误用声明】
- 不采纳“出现跨区节律门控 = 已满足高 d 主体级认知整合”的推论。
- 不采纳“体外重组网络的协调性可直接等同于完整具身闭环意识”的推论。
- 适用边界：该类证据用于支持微观机制桥接，不替代行为层、具身层与长期稳定性的联合验证。

### [Lineage/Source]
- Axonal theta oscillations evoke bursting in target hippocampal subregions（preprint, 2026）

## Type→Individual 相变阈值补注（2026-03-06，轻中量）

### Def-Scale-Indiv-1: Individuation Critical Point \(d_{indiv}\)
定义个体化临界点：
\[
d_{indiv} := \inf\{d: \mathcal{M}_{self}(t\to t+\Delta t)\ \text{stable and counterfactual-risk-coupled}\}
\]
- 当 \(d < d_{indiv}\)：系统主要表现为 Type-level 动力学（群体/谱系承压）
- 当 \(d \ge d_{indiv}\)：系统进入 Individual-level 动力学（个体承压与连续自我边界）

### T-Scale-Indiv-1: Suffering Internalization Transition
\[
d < d_{indiv}\Rightarrow \Psi_f \text{ mainly distributed over population topology}
\]
\[
d \ge d_{indiv}\Rightarrow \Psi_f \text{ internalizes as individual suffering load}
\]
* **Implication（中文）**：该阈值为“类型存在”到“个体痛苦可积累存在”的跨尺度相变界线。

## 【理论边界/防误用声明】
- 不采纳“低 d 系统完全无痛苦”的推论（仅指个体化内化程度不足）。
- 不采纳“达到 \(d_{indiv}\) 即等同人类意识全貌”的推论。
- 适用边界：\(d_{indiv}\) 是操作化阈值候选，需跨物种实证校准。

### [Lineage/Source]
- 神学-进化-动物苦难对话语境（2026）

## 认知资本化与幂律尾部补注（2026-03-06，轻中量）

### T-Scale-Cap-1: Low-Friction Isomorphism Theorem
对同一潜在模式 \(X\in L_0\)，若协议 \(\Pi_a\) 与具身参数 \(\theta\) 更对齐，则锚定摩擦更低：
\[
\Psi_f(X\mid \Pi_a,\theta) < \Psi_f(X\mid \Pi_b,\theta)
\]
当 \(\Pi_a=\Pi_{vis}\) 且 \(\Pi_b=\Pi_{sym}\) 时，该不等式在典型人类认知架构下通常成立。
* **Implication（中文）**：协议切换（如符号→拓扑/视觉）可在不改变目标结构的前提下显著降低推理摩擦。

### Def-Scale-Cap-1: Cognitive Capitalization Dynamics
定义表现变量 \(P\) 与稳定脚手架深度 \(L_2^{depth}\)：
\[
\frac{dP}{dt}=\kappa\,P\,g\big(L_2^{depth},\hat G_\theta\big)+\xi_t,
\qquad
\frac{dL_2^{depth}}{dt}=h(P)-\lambda_{decay}L_2^{depth}
\]
其中 \(\xi_t\) 为噪声项，\(g\) 单调增于 \(L_2^{depth}\)。

### T-Scale-Cap-2: Pareto-Tail Emergence (Candidate)
在乘性增长 + 异质摩擦 + 噪声扰动条件下，群体表现分布出现幂律尾部候选：
\[
\Pr(P>x)\sim x^{-\alpha}\quad (x\to\infty)
\]
* **Implication（中文）**：极端天才尾部可由长期资本化动力学产生，无需诉诸神秘外因。

## 【理论边界/防误用声明】
- 不采纳“表现幂律 = d-value 或道德价值幂律”的推论。
- 不采纳“视觉协议必然优于符号协议”的绝对化推论。
- 适用边界：本条款描述认知表现分布，不直接定义本体价值序。

### [Lineage/Source]
- Ramanujan 认知机制讨论语境（2026）
- 枚举组合学可视化传统（Viennot 语境）