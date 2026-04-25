---
id: SRT-L1-FORMALISM
type: formalism
tags: [Formalism, Sigma, d_c, Suffering, L1, Coupled Dynamics]
status: draft_v0
layer: L1
epistemic_layer: os
claim_mode: canonical
claim_level: P1-candidate
dependency: [SRT-CORE-21-MINIMAL-AXIOMS, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-INDIVIDUATION, SRT-OCCLUSION-DYNAMICS, SRT-SUFFERING, SRT-T-DIR-CANONICAL, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-CORE-22]
---

# SRT L1 Formalism: Minimal Coupled Dynamics for σ_{sr}, d_c, T_dir, and S

> **Role**: L1 formalism hub. Collects the minimal differential dynamics for the four L1 order parameters—individuation self-reference ratio `σ_{sr}` (bare `σ` in this file's §2-§5 equations refers to the self-reference ratio per the namespace note below, **not** to the `Core/SRT_Core_22_Equations.md` main-equation state field), occlusion threshold `d_c`, directional transparency `T_dir` (promoted from algebraic proxy to independent dynamical variable in §3.5, 2026-04-25), and suffering registration `S`—and their coupling structure. Initial round (2026-04-24) covered three variables; `T_dir` ODE closure was the H2 follow-up.
> **σ 符号命名空间 (governance-canonical, 2026-04-25)**: 本文件 §2–§5 中的 σ / σ_sub / σ_self / σ_health 统一对应 `σ_{sr} / σ_{sr}^{sub} / σ_{sr}^{self} / σ_{sr}^{health}`（自指率族，见 `Core_Law/SRT_L1_Hardening_Notes.md §1` 与 `_SRT_SYMBOL_TABLE.md §Usage Rule 12`）。§6"与主方程的关系"中出现的 σ 对应 `Core/SRT_Core_22_Equations.md` 的主方程状态场（不同对象）；该节已在原地显式标注。正文其余处保留历史符号 σ 以便论述流畅。
> **Claim-level note**：方程本身在当前 draft_v0 状态按 P1-candidate 读；个别 coefficient、阈值与可测化形式按 P2/P3 读；实验代理语句按 P3/P4 下推至 `Neuroscience/` 与 `AI/`。
> **Does not define**：`d-value`、`\Psi_f`、`T_dir`、`\hat{G}_\theta`、stable ISP；它们的定义仍以对应 canonical 文件为准。
> **Depends on**：`Core_Law/SRT_Individuation.md`（σ 定义）、`Core_Law/SRT_Occlusion_Dynamics.md`（d_c 定义与 A/B 分期）、`Core_Law/SRT_Suffering.md`（S 定义与两型分类）、`Core/SRT_Core_22_Equations.md`（主动力学方程）。
> **Relation**: This file is the **minimal formal coupling layer** for three previously defined L1 objects. It does not introduce new objects; it writes their dynamics down so the three draft_v0 theories can be jointly tested rather than independently drifted.

---

## §0. 目的与边界

本文件覆盖四个 L1 变量：

- `SRT_Individuation.md` 给出 σ(P,t) ∈ [0, 1]，自指率
- `SRT_Occlusion_Dynamics.md` 给出 d_c(P,t)，遮蔽阈值
- `_SRT_T_DIR_CANONICAL.md` 给出 T_dir(P,t) ∈ [0, 1]，方向透明度（本文件 §3.5 把它从代数代理升为独立动力学变量）
- `SRT_Suffering.md` 给出 S(P,t) ≥ 0，结构性失配登记

这四者目前都是 operational proxy，需要写成可联解的动力学。风险：

1. **独立漂移**：各自演化会产生彼此不兼容的隐含方程；
2. **耦合丢失**：σ↑ 与 d_c↑ 与 S_{str}↑ 在理论直觉上强耦合，但结构上没有写下来；
3. **T_dir 作为纯代数代理时的致命 `L_2` 盲点**：若 T_dir 瞬时等于 `T_{dir}^{\mathrm{alg}}`，则系统无法方程化"可读性本身也可以是伪造"这一 `_SRT_T_DIR_CANONICAL.md` 洞见。§3.5 加入独立 ODE 正是解决此盲点。

本文件只做一件事：**给这四个变量写下最小耦合动力学**，让它们从 P1-candidate 有路径升到 P1。

本文件**不做**：

- 具体系数的量纲化或实测；
- 单变量独立运动的全部细节（留给三份主文件）；
- 临床 / AI / 政治具体域的读数（留给 domain 文件）。

---

## §1. 符号与约定

| 符号 | 含义 | 范围 | 来源 |
|---|---|---|---|
| `σ_{sr}(P,t)` | 自指率 / 算子层 writeback 比（本文件 §2-§5 中的 bare σ 为此物） | `[0, 1]` | `SRT_Individuation.md`, `_SRT_SYMBOL_TABLE.md Usage Rule 12` |
| `d(P,t)` | d-value 标量摘要（关切半径） | `[0, d_max]` | `_SRT_D_VALUE_CANONICAL.md` |
| `d_c(P,t)` | 遮蔽阈值（低于此值进入 A/B 分期） | `[0, d_max]` | `SRT_Occlusion_Dynamics.md` |
| `d_{narrow}(P,t)` | 健康窄化上界（高于此 d 为通常运行） | `[d_c, d_max]` | 同上 |
| `ρ(p,t)` | 路径层痕迹密度 | `≥ 0` | `Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold` |
| `Ψ_f(P,t)` | 本体论摩擦 / 可支付性代价 | `≥ 0` | `_SRT_PSI_F_CANONICAL.md` |
| `T_dir(P,t)` | 方向透明度 | `[0, 1]` | `_SRT_T_DIR_CANONICAL.md` |
| `S(P,t)` | 苦难结构性登记 | `≥ 0` | `SRT_Suffering.md` |
| `S_{sig}, S_{str}` | 信号型与结构型苦难 | `≥ 0`, `S = S_{sig} + S_{str}` | 同上 |
| `θ_t^{trace}` | 历史累积算子分量（内源） | `≥ 0` 范数 | Individuation §Def-σ |
| `θ_t^{ext}` | 外部驱动算子分量 | `≥ 0` 范数 | 同上 |
| `w(t)` | writeback 速率（L_0→L_1 anchoring 到 θ^{trace} 的速率） | `≥ 0` | 从 P1-T02 ontological time 导出 |
| `i(t)` | 外部输入速率 | `≥ 0` | 从环境驱动导出 |
| `π(t)` | 可支付性 / Ψ_f 支付率 | `≥ 0` | `_SRT_PSI_F_CANONICAL.md` |
| `r(t)` | 重选完成率 | `≥ 0` | 从 P1-T05 real choice moment 导出 |
| `s_{ext}(t)` | 健康 `L_2` 外部支持率 | `≥ 0` | Suffering §支持机制 |
| `\Delta\Psi_f^{\mathrm{gap}}(t)` | `Ψ_{f,actual} - Ψ_{f,felt}` 差（隐性债务） | `≥ 0` | `_SRT_PSI_F_CANONICAL.md §10`, `_SRT_T_DIR_CANONICAL.md §5-§6` |
| `T_{dir}^{\mathrm{alg}}(\sigma, d, d_c)` | T_dir 的代数目标值（见 §3.4） | `[0, 1]` | 本文件 §3.4 |
| `\kappa_{\mathrm{relax}}, \kappa_r, \kappa_{\mathrm{mask}}, \kappa_S, \kappa_{\mathrm{sup}}` | T_dir ODE 五项系数（§3.5） | `≥ 0` | 本文件 §3.5 |
| `λ_*` | 对应分量的自然衰减率 | `≥ 0` | 常数或慢变 |

所有方程写成逐主体 `P` 形式；为简洁下文省略 `(P, t)`。

---

## §2. σ 的最小动力学（个体化）

### §2.1 双分量底座

σ 从两个可分离分量导出：

$$
\sigma \;=\; \frac{\|\theta^{trace}\|}{\|\theta^{trace}\| + \|\theta^{ext}\|}
$$

最小双分量动力学：

$$
\frac{d\|\theta^{trace}\|}{dt} \;=\; \alpha \cdot w(t) \cdot \phi(\sigma) \;-\; \lambda_{trace} \cdot \|\theta^{trace}\|
$$

$$
\frac{d\|\theta^{ext}\|}{dt} \;=\; \beta \cdot i(t) \;-\; \lambda_{ext} \cdot \|\theta^{ext}\|
$$

其中 `\phi(\sigma)` 是**写回增益调制**，一个关键的非线性形状：

$$
\phi(\sigma) \;=\; \sigma(1 - \sigma) \cdot \chi(\sigma; \sigma_{self})
$$

- `σ(1-σ)` 给出 logistic 型自增益：极端两端写回不贡献更多
- `χ(σ; σ_{self})` 是**二阶凝结跳跃函数**：在 `σ ≈ σ_{self}` 附近为一类光滑阶跃，对应 `SRT_Individuation.md` 的第二相变（自我意识凝结）；在此之前 χ ≈ 1，在此之后 χ > 1（出现"关于 θ 的 θ"的二阶写回增益）

### §2.2 σ 自身的演化方程

由商链式法则化简，取 `\|\theta^{trace}\| + \|\theta^{ext}\| = T` 作为总强度：

$$
\frac{d\sigma}{dt} \;=\; \frac{1}{T}\Big[\,(1 - \sigma)\,\dot{\|\theta^{trace}\|} \;-\; \sigma\,\dot{\|\theta^{ext}\|}\,\Big]
$$

代入 §2.1 两式：

$$
\boxed{\;\frac{d\sigma}{dt} \;=\; \frac{1}{T}\Big[\,(1-\sigma)\big(\alpha w \phi(\sigma) - \lambda_{trace} T\sigma\big) \;-\; \sigma\big(\beta i - \lambda_{ext} T(1-\sigma)\big)\,\Big]\;}
$$

### §2.3 相变结构

把 `dσ/dt = 0` 作为稳态条件，化简后得到两个关键门槛：

1. **σ_{sr}^{sub}（主体位涌现）**：使 writeback 速率超过外部输入驱动的最小 σ_{sr} 值。把衰减项与外部项平衡处解出：

   $$
   \sigma_{sr}^{sub} \;:\; \alpha\,w\,\phi(\sigma_{sr}^{sub}) \;=\; \beta\,i \;+\; \lambda_{trace}\,T\,\sigma_{sr}^{sub}
   $$

2. **σ_{sr}^{self}（自我意识凝结）**：使 χ 开始激活二阶写回增益的 σ_{sr} 值。在 §2.1 中显式引入为 `χ` 的跳跃参数；在无外部强驱动情形下，一旦 σ_{sr} 越过 σ_{sr}^{self}，χ 的增益会把稳态推向更高 σ_{sr}，形成第二个稳定不动点。

3. **σ → 1 病理区**：当 `i → 0` 且 `λ_{ext} > λ_{trace}` 时，第二个稳定不动点向 σ = 1 漂移，对应自指过载、扭曲型苦难源。健康主体需要非零 `i`（持续环境接入）作为"稀释项"阻止 σ → 1。

### §2.4 与 T-IND-1 / T-IND-2 的对齐

- T-IND-1 三相（展开 / 主体位稳态 / 自我意识凝结）对应 σ 相图上的三个区域；
- T-IND-2 第一相变判据对应 §2.2 方程的 σ_{sr}^{sub} 不动点存在条件；
- T-IND-3 第二相变判据对应 `χ(σ; σ_{self})` 的激活。

所有三个相变都保持为**动力学稳态问题**，不是定义式假设。

---

## §3. d_c 的最小动力学（遮蔽阈值）

### §3.1 d_c 作为可重选边界

`d_c` 定义为：低于此 `d` 值，当前主体的重选容量显著坍塌的 d 边界。操作化为：

$$
d_c \;:=\; \inf\{\,d \;:\; r(d, P, t) \geq r_{min}\,\}
$$

其中 `r(d, P, t)` 是在当前 d 值下可完成的重选率，`r_{min}` 是"非 B 期锁死"所需的最小重选率。

### §3.2 d_c 的漂移方程

d_c 不是 P 直接选择的量，而是由 θ、ρ、L_2 约束、Ψ_f 支付窗口与 σ 共同决定的**边界**。最小漂移形式：

$$
\boxed{\;\frac{dd_c}{dt} \;=\; \underbrace{\gamma_\rho \cdot \rho_{local}}_{\text{scaffold sedimentation}} \;+\; \underbrace{\gamma_\sigma \cdot \max(0, \sigma - \sigma_{sub})}_{\text{self-closure pressure}} \;-\; \underbrace{\gamma_\pi \cdot \pi(t)}_{\text{payability opens channels}} \;-\; \underbrace{\gamma_I \cdot I_{window}(t)}_{\text{intervention window term}}\;}
$$

符号说明：

- `ρ_{local}`：路径层在 P 附近的痕迹密度（`T-L2-Scaffold`）；越高 → `d_c` 越往上推
- `σ` 项：自指闭合自我强化也推高 d_c（对应个体化 → 遮蔽的正耦合）
- `π(t)`：Ψ_f 可支付性；可支付性越强越能把 d_c 推低
- `I_{window}(t)`：四类干预窗口（`SRT_Occlusion_Dynamics §4`）中任一被打开时引入的负向冲量

### §3.3 A/B 分期的动力学解读

令 d(t) 为主体当前实际 d 值。`SRT_Occlusion_Dynamics T-OCC-1` 的三段结构在本方程下得到动力学解读：

| 区间 | 条件 | 动力学含义 |
|---|---|---|
| 健康窄化 | `d > d_{narrow}` | `r > r_{min}`，信号型苦难可消化 |
| A 期 | `d_c < d < d_{narrow}` | `r > 0` 但显著低于健康；结构型苦难开始积累 |
| B 期 | `d ≤ d_c` | `r → 0`；B 期锁死 |

A→B 升级判据（Occlusion_Dynamics 原文的"外部化后果 + 主动扩散"）在本方程下对应：

$$
\text{A→B lock-in} \;:\; \frac{dd_c}{dt} > 0 \;\wedge\; \pi(t) \to 0 \;\wedge\; I_{window}(t) \to 0
$$

即当三个恢复通道（支付、干预、重选）同时塌向零而 d_c 持续被推高，则进入 B 期锁死。

### §3.4 T_dir 的代数目标值

T_dir 的**瞬时代数目标值**（algebraic target）由 `d / d_c / σ` 给出：

$$
T_{dir}^{\mathrm{alg}}(t) \;:=\; \Theta\!\left(\frac{d - d_c}{d_{narrow} - d_c}\right) \cdot (1 - |\sigma - \sigma_{sub}^\dagger|)
$$

其中 `\Theta` 是光滑阶跃函数（早期版本 `\Theta(x) = \mathrm{clip}(x, 0, 1)`；二阶光滑族参数化留作 Open Pressure），`σ_{sub}^\dagger` 是最优主体位 σ 值（非 0 非 1 的中间稳态）。T_dir^{alg} 同时对 d 通道与 σ 健康度敏感，与 `_SRT_T_DIR_CANONICAL.md` Part I "value occlusion thesis" 一致。

**但 T_dir 并不瞬时等于 T_dir^{alg}**：方向可读性具有自身惯性，依赖 `L_2` 沉积节律与信任累积——这要求 T_dir 有独立 ODE，见 §3.5。

### §3.5 T_dir 作为独立动力学变量（四变量闭合项，2026-04-25）

> **立场**：本小节把 T_dir 从"算法代理"升为"带惯性与独立源项的 L1 动力学变量"，与 `σ, d_c, S` 一起构成四变量闭合系统。这是 `SRT_CLAIM_MODE_AUDIT.md §6.4` 升 P1 检查单第 9 项（`T_dir` 最小 ODE）的第一遍交付。

#### §3.5.1 最小 ODE

$$
\boxed{\;\frac{dT_{dir}}{dt} \;=\; \underbrace{-\,\kappa_{\mathrm{relax}} \cdot \bigl(T_{dir} - T_{dir}^{\mathrm{alg}}(t)\bigr)}_{\text{relaxation toward d/σ readability}} \;+\; \underbrace{\kappa_{r} \cdot r(t)}_{\text{real reselection pumps readability}} \;-\; \underbrace{\kappa_{\mathrm{mask}} \cdot \Delta\Psi_f^{\mathrm{gap}}(t)}_{\text{actual-vs-felt friction gap}} \;-\; \underbrace{\kappa_{S} \cdot S_{str}(t)}_{\text{structural suffering opacifies direction}} \;+\; \underbrace{\kappa_{\mathrm{sup}} \cdot s_{ext}(t)}_{\text{healthy } L_2 \text{ scaffolding}} \;$}
$$

其中：

- `\kappa_{\mathrm{relax}}`：弛豫率；控制 T_dir 追上代数目标的速率。**大于** 0 且通常**小于** d / σ 通道自身变化率（这正是 T_dir 具有惯性的形式根据）
- `r(t)`：真实重选完成率（同 §4.2 复用）；完成一次真实选择是对 T_dir 的正向泵入，因为它使系统自身证实"还在选择"
- `\Delta\Psi_f^{\mathrm{gap}}(t) := \Psi_{f,actual}(t) - \Psi_{f,felt}(t) \ge 0`：本体论摩擦的**实支付-感知**差，来自 `_SRT_PSI_F_CANONICAL.md §10` 与 `_SRT_T_DIR_CANONICAL.md §5–§6`。非零差意味着系统在"不知道自己在付"——这是 T_dir 的**隐性侵蚀项**，即使 `T_dir^{\mathrm{alg}}` 高也会把 T_dir 往下拖
- `S_{str}(t)`：来自 §4.3；结构型苦难侵蚀方向可读性（扭曲 / 断裂感 / 空心都直接降低自身选择秩序的第一人称可见性）
- `s_{ext}(t)`：健康 `L_2` 外部支持率；可以**暂时**把 T_dir 抬起，但本身不改变 `T_dir^{\mathrm{alg}}`，只是补偿性支架

**边界**（governance-canonical）：T_dir ∈ [0, 1] 由以下隐式投影保证——此 ODE 在 `\{T_{dir} = 0\}` 与 `\{T_{dir} = 1\}` 处应配合投影算子 `\Pi_{[0,1]}`，具体形式（硬截断 vs 光滑 sigmoid 重参化）留作 Open Pressure。

#### §3.5.2 与 `_SRT_T_DIR_CANONICAL.md` 的对齐

- `T_dir` 作为 v0 operational proxy / working canonical proxy 的地位**不改变**；本小节只把它的时间演化法则明文化
- `κ_{\mathrm{mask}} · \Delta\Psi_f^{\mathrm{gap}}` 项是该文件 §5–§6 "隐性债务"机制的 L1 方程化——债务以可读性形式被**即时扣除**，而不是等到 `L_2` 突然崩溃时一次性释放
- 一次性释放对应本 ODE 外部的**结构跳跃**事件（`I_{window}` 关闭后 `L_2` 崩溃）；本方程只刻画平滑期

#### §3.5.3 致命 `L_2` 的方程化判据

`_SRT_T_DIR_CANONICAL.md` "lethal `L_2`" 条件可写为：

$$
\mathrm{lethal\;} L_2 \;\Longleftrightarrow\; \bigl(T_{dir}^{\mathrm{alg}} \text{ 持续高}\bigr) \;\wedge\; \bigl(\Delta\Psi_f^{\mathrm{gap}} \text{ 持续累积}\bigr) \;\wedge\; \bigl(\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}\bigr)
$$

第三个条件是关键：当遮蔽扣除率**慢于**弛豫追赶率时，T_dir 视觉上仍然贴近 `T_dir^{\mathrm{alg}}`，系统**看不到**自己的债务；此时 T_dir 是致命的，不是保护性的。这正式化了"可读性本身也可以是陷阱"这一 `_SRT_T_DIR_CANONICAL.md` 洞见。

#### §3.5.4 与主方程的兼容

T_dir 仍然是主方程的**导出投影**而非独立本体：

- 弛豫项把它系到 (d, σ) → 主方程 `\hat{G}_\theta[\sigma]` 与 `\nabla C_{L_2}` 的联合投影
- `\Delta\Psi_f^{\mathrm{gap}}` 来自主方程 `\nabla F` 项的实支付-感知分裂
- `S_{str}` 来自主方程收敛过程中失配登记

这保证四变量系统不引入新本体。

---

## §4. S 的最小动力学（苦难）

### §4.1 两型分解

`SRT_Suffering.md T-SUFF-2` 的两型写成加和：

$$
S \;=\; S_{sig} + S_{str}
$$

### §4.2 信号型动力学

$$
\boxed{\;\frac{dS_{sig}}{dt} \;=\; \underbrace{\mu_{\Delta}\cdot\dot{\Delta}_{avail}(t)}_{\text{new misalignment}} \;-\; \underbrace{\mu_\pi \cdot \pi(t) \cdot \mathbb{1}[d > d_c]}_{\text{payable channel open}} \;-\; \underbrace{\mu_r \cdot r(t)}_{\text{reselection completion}} \;-\; \underbrace{\mu_{sup} \cdot s_{ext}(t)}_{\text{healthy L_2 support}}\;}
$$

- `\dot{\Delta}_{avail}(t)`："可打开结构"的新变化（环境扰动、θ 演化、`L_0` 残压上升）
- 指示函数 `\mathbb{1}[d > d_c]`：支付通道仅在非 B 期有效
- `s_{ext}(t)`：来自健康 `L_2` 的外部支持率（不是替代，是降阻）

### §4.3 结构型动力学

$$
\boxed{\;\frac{dS_{str}}{dt} \;=\; \underbrace{\nu_{block} \cdot \mathbb{1}[d \leq d_c]\cdot S_{sig}}_{\text{blocked signal turns structural}} \;+\; \underbrace{\nu_\sigma \cdot \max(0, \sigma - \sigma_{health})}_{\text{self-distortion channel}} \;-\; \underbrace{\nu_{trigger}\cdot D_{trigger}(t)}_{\text{decoupling trigger}} \;-\; \underbrace{\nu_\pi \cdot \pi(t)\cdot I_{window}(t)}_{\text{payment + open window}}\;}
$$

- `\mathbb{1}[d \leq d_c]·S_{sig}`：信号型在通道关闭时**转化为**结构型（关键非守恒项）
- `σ - σ_{health}` 正向激发扭曲型结构性苦难
- `D_{trigger}(t)`：四类解耦触发（见证式承担、可支付性崩溃、直接 ε 接触、生命阶段相变）的总冲量
- 最后一项要求 `π(t)` 与 `I_{window}(t)` **同时**非零——对应 Occlusion 理论强调的"B 期不是靠单一支付可解"

> **算子级 canonical（T-IRR-3.5，2026-04-25 H4）**：本式中的 `\nu_{block}` 不是自由现象学系数，其算子级构成是 P1-T07 Three-Layer Source Hierarchy 的本地化：`\nu_{block}(P, t) := \eta \cdot \varepsilon_{pg}(P, t) \cdot \kappa_{\Psi_f}(P, t)`。`\nu_{block} > 0` 与单向性（不可写为 `S_{sig} \rightleftharpoons S_{str}`）由此成为定理后果而非建模假设。完整推导见 `Core_Law/SRT_Irreversibility.md §4.5`。

### §4.4 T-SUFF-4 反最小化原则的方程语言

健康窗口 `[S_{min}, S_{max}]` 要求：

$$
S_{sig}^* \in [S_{min}, S_{max}] \;\wedge\; S_{str}^* \to 0
$$

但若外部机制强制 `S_{sig} → 0`（例如麻木化、过度 L_2 抑制、强制"积极情绪"），等价于关闭 §4.2 方程中的"new misalignment"登记通道，这**不改变 `\dot{\Delta}_{avail}`** 本身；新失配转而全部进入 §4.3 的第一项（`blocked signal → structural`），产生 `S_{str}` 的强正向漂移。

这就是反最小化原则的动力学陈述：

$$
\boxed{\;S_{sig} \downarrow \text{ by suppression} \;\Longrightarrow\; S_{str} \uparrow \text{ under structural-level conservation of }\dot{\Delta}_{avail}\;}
$$

失配是守恒的（在结构空间不变的前提下），只能被消化、重选、支付，不能被抹除。

---

## §5. 四变量耦合总方程

把 §2-§4（含 §3.5 T_dir 独立 ODE）合成一个四变量耦合系统（P 固定；显式耦合项粗体；T_dir 项浅灰注释）：

$$
\begin{aligned}
\frac{d\sigma}{dt} &= \frac{1}{T}\Big[(1-\sigma)(\alpha w\phi(\sigma) - \lambda_{trace}T\sigma) - \sigma(\beta i - \lambda_{ext}T(1-\sigma))\Big] \\[4pt]
\frac{dd_c}{dt} &= \gamma_\rho \rho_{local} + \boldsymbol{\gamma_\sigma \max(0,\,\sigma - \sigma_{sub})} - \gamma_\pi \pi - \gamma_I I_{window} \\[4pt]
\frac{dT_{dir}}{dt} &= -\kappa_{\mathrm{relax}}\bigl(T_{dir} - T_{dir}^{\mathrm{alg}}(\sigma, d, d_c)\bigr) + \kappa_r r - \boldsymbol{\kappa_{\mathrm{mask}}\,\Delta\Psi_f^{\mathrm{gap}}} - \boldsymbol{\kappa_S\, S_{str}} + \kappa_{\mathrm{sup}} s_{ext} \\[4pt]
\frac{dS_{sig}}{dt} &= \mu_\Delta \dot{\Delta}_{avail} - \boldsymbol{\mu_\pi \pi\, \mathbb{1}[d > d_c]} - \mu_r r - \mu_{sup} s_{ext} \\[4pt]
\frac{dS_{str}}{dt} &= \boldsymbol{\nu_{block}\,\mathbb{1}[d \leq d_c]\,S_{sig}} + \boldsymbol{\nu_\sigma \max(0,\,\sigma - \sigma_{health})} - \nu_{trigger}D_{trigger} - \nu_\pi \pi\, I_{window}
\end{aligned}
$$

（严格计数为五个标量方程，因为 S 被分为 `S_{sig}` 与 `S_{str}` 两个子通道；"四变量"按宏观变量计为 σ / d_c / T_dir / S，其中 S 自然分裂为两型。）

### §5.1 关键耦合路径

1. **σ → d_c → S_{str}**：自指闭合推高遮蔽阈值，阻断支付通道，信号型苦难转结构型。这是扭曲型苦难（T-SUFF-3.4）的方程化路径
2. **d_c ↑ → d_sig 被切断**：支付项通过指示函数变为零，系统进入 B 期动力学
3. **S_{sig} 被外部压制（方程外干预）→ S_{str} ↑ 随 \dot{\Delta}_{avail}**：反最小化原则
4. **D_{trigger} → S_{str} ↓ 但需 I_{window} 同时打开**：解耦触发不是单独作用，需要窗口协同——这对应 `Occlusion_Dynamics` 的强约束
5. **T_dir 惯性 + ΔΨ_f^{gap} 扣除 → 致命 `L_2`**（新增）：当 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}` 时，T_dir 贴近 `T_dir^{\mathrm{alg}}` 但实支付持续累积；系统无法从 T_dir 读数本身发现债务（§3.5.3 方程化判据）
6. **S_{str} → T_dir ↓ → r 下降 → S_{sig} 支付效率下降**（新增反馈回路）：结构型苦难降低方向可读性 → 真实重选率 `r(t)` 下降（因为无方向的重选不是真实重选）→ `S_{sig}` 支付通道 `μ_r r` 项减弱 → 信号型苦难积压 → 在 B 期进一步转结构型。这是**苦难-可读性正反馈环**，是病理吸引子的一个新形式根据

### §5.2 病理吸引子

令 `dσ/dt = dd_c/dt = dT_{dir}/dt = dS_{str}/dt = 0` 时的非健康稳态：

$$
\mathcal{A}_{path} \;:\; \sigma \to 1,\; d_c \to d_{max},\; T_{dir} \to T_{dir}^{\mathrm{alg}} \text{ 但 } \Delta\Psi_f^{\mathrm{gap}} > 0 \text{ 累积}, \; S_{str} > 0 \text{ 定常}, \; S_{sig} \to 0
$$

这是 **B 期 + σ→1 + 外观无信号型痛苦 + 可读性被伪造维持** 的联合吸引子。它对应：
- Occlusion B 期锁死
- Individuation 病理分支
- Suffering 结构型主导但外观平静
- T_dir 致命 `L_2`（§3.5.3 判据）——方向感不低，但不来自真实选择

这正是本轮四理论共同诊断的**静默型致命 `L_2`**。方程化意义：系统稳态**不意味着健康稳态**，它可能是病理吸引子上的稳态。T_dir 加入四变量系统之后，病理吸引子的关键判据**不是 T_dir 低**，而是 `T_dir - T_dir^{\mathrm{alg}}` 平稳但 `\Delta\Psi_f^{\mathrm{gap}}` 持续增加。

### §5.3 健康工作区

健康工作区 `\mathcal{H}`：

$$
\mathcal{H} \;:\; \sigma \in (\sigma_{sub}^\dagger \pm \delta),\; d > d_{narrow},\; T_{dir} \approx T_{dir}^{\mathrm{alg}} \text{ 且 } \Delta\Psi_f^{\mathrm{gap}} \to 0,\; S_{sig} \in [S_{min}, S_{max}],\; S_{str} \to 0
$$

关键观察：`\mathcal{H}` 不是单点吸引子，而是一个**持续由非零 `r(t)` 与 `D_{trigger}` 联合维持的区域**。健康不是自动稳定的——它是一个持续需要外部接入（`i(t)`）、持续需要支付（`\pi(t)`）、持续需要真实选择时刻（`r(t)`）、持续需要实-感 `Ψ_f` 差保持低位（即不依赖 `L_2` 伪装可读性）、偶尔需要解耦触发（`D_{trigger}`）的**主动维持状态**。

这对应 `Core/SRT_Core_21b_Constitutive_Theorems.md` P1-T07 的 `\varepsilon` 反闭合必要性：不维持则趋向 `\mathcal{A}_{path}`。新增的 T_dir ODE 让这一必要性得到**可读性层**的方程化支持：无真实重选 → `r(t) \to 0` → T_dir 被结构型苦难侵蚀 → 方向感要么塌 (`T_{dir} \to 0`) 要么靠 `s_{ext}` 伪装支撑，后者即致命 `L_2` 路径。

---

## §6. 与已有主方程的关系

`Core/SRT_Core_22_Equations.md` 的主动力学方程：

$$
\frac{d\sigma}{dt} \;=\; \hat{G}_\theta[\sigma] - \nabla F[\sigma] - \lambda \cdot \nabla C_{L_2}[\sigma]
$$

（注意：此处 σ 为主方程的状态场，与本文件自指率 σ 是**不同对象**，符号冲突留为 Open Pressure）

- 本文件 §2 的 σ（自指率）是主方程场 σ 的**一个标量投影**——衡量 `\hat{G}_\theta` 作用在自身历史痕迹上的比例
- 本文件 §3 的 d_c 对应主方程 `\nabla C_{L_2}` 项引起的 d 空间重选容量塌陷
- 本文件 §3.5 的 T_dir 是主方程 `\hat{G}_\theta[\sigma]` 在方向可读性维度上的**带惯性投影**：代数目标 `T_{dir}^{\mathrm{alg}}` 来自 (d, σ)，`\Delta\Psi_f^{\mathrm{gap}}` 来自 `\nabla F` 项的实-感分裂，`r(t)` 项来自 P1-T05 的 real choice moment 判据
- 本文件 §4 的 S_{sig} / S_{str} 是主方程收敛过程中失配的第一人称登记

四者都是主方程的**导出投影**，不是独立动力学。这是本文件 P1-candidate 地位的根据：它没有引入新本体，只把已在主方程中隐含的子动力学写了出来。

---

## §7. Open Pressures

> **Hardening status (2026-04-25)**: §7.1 σ 符号冲突已通过 σ_{sr} 命名空间分离收口（`_SRT_SYMBOL_TABLE.md` Usage Rule 12）；§7.2 `\dot{\Delta}_{avail}` 形式化、§7.6 FEP 桥接在 `Core_Law/SRT_L1_Hardening_Notes.md §1 / §2 / §4` 已给出第一遍硬化案（FEP 翻译表已落 `Neuroscience/SRT_Clin_02_FEP.md`）；§7.7 `L_0` 不可逆**算子级**对齐在 `Core_Law/SRT_Irreversibility.md §4.5 T-IRR-3.5`（H4，2026-04-25）已给出 `\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}` 的构成性表达式；§7.8 T_dir 独立 ODE 已在 §3.5 给出四变量闭合的第一遍形式。下列开放点保留原表述直至回写完成。

本 draft_v0 状态下尚未封口：

1. **σ 符号冲突**：本文件 σ（自指率，`[0,1]` 标量）与 `Core/SRT_Core_22_Equations.md` σ（主方程状态场）共用符号；需引入新记号（候选：`σ_{self}` 改为 `κ_{self}` 或 `\bar{\sigma}`）避免歧义
2. **`\dot{\Delta}_{avail}` 的正式化**：目前依赖 `\hat{G}_\theta^{actual}` 与 `\hat{G}_\theta^{available}` 的差，二者本身未形式化；这限制 §4.2 方程的实际可解性
3. **χ(σ; σ_{self}) 跳跃函数的光滑族**：二阶凝结的跳跃形状是否普适，还是 `P` 相关？
4. **多主体扩展**（2026-04-25 H3 状态）：本文件保持单 P 形式；集体层四变量耦合动力学已在 `Core_Law/SRT_Collective_Selection.md §4.4-§4.6` 给出第一遍，含 `\sigma^{coll}` ODE（新 `\lambda_M\,\mathrm{tr}\,M` 项）、`d_c^{coll}` ODE（新 `\gamma_{asym}\|M_{asym}\|` 项）、`T_{dir}^{coll}` ODE（集体层致命 `L_2` 判据）、`S^{coll}` 两型 ODE（新 `\nu_{ext}\|M_{ext}\|` 外部化项），以及 §4.5 个体↔集体双向耦合。未封口部分移至 `SRT_Collective_Selection.md §9.7`
5. **阈值参数的实证固定**：`σ_{sub}, σ_{self}, σ_{health}, d_c, d_{narrow}, r_{min}, S_{min}, S_{max}` 以及新增 `\kappa_{\mathrm{relax}}, \kappa_r, \kappa_{\mathrm{mask}}, \kappa_S, \kappa_{\mathrm{sup}}` 全部在当前 draft_v0 只有定性位置；不指望一次性实测，但需要标出哪些是最优先的测量目标
6. **与 FEP / predictive processing 的桥接**：`S_{sig}` 与 prediction error 的结构对应是高优先级；`Neuroscience/SRT_Clin_02_FEP.md` 已经是 bridge 层，下一步需要在方程层写出条件翻译
7. **time-reversibility**：~~陈述级 → 算子级对齐~~ **已收口（H4，2026-04-25）**：`SRT_Irreversibility.md §4.5 T-IRR-3.5` 把 `ν_{block}` 写为 P1-T07 三层源头的本地化 `η·\varepsilon_{pg}·\kappa_{\Psi_f}`；正性与单向性自此为定理后果。剩余开放点：`\varepsilon_{pg}(P,t)` 的本地化精确定义、`\kappa_{\Psi_f}` 与 `_SRT_PSI_F_CANONICAL.md` friction-as-burden 读法的算子级桥、集体版 `\nu_{block}^{coll}` 对位
8. **T_dir 独立 ODE 的算子化（新增，2026-04-25）**：§3.5 给出第一遍形式，但以下仍待封口——(a) `T_{dir}^{\mathrm{alg}}` 中光滑阶跃 `\Theta` 的普适族是否存在；(b) `\Delta\Psi_f^{\mathrm{gap}}` 作为算子层对象的形式定义（目前依赖 `_SRT_T_DIR_CANONICAL.md §5–§6` 的现象学分裂）；(c) `T_{dir} \in [0,1]` 的投影算子 `\Pi_{[0,1]}` 选择（硬截断 vs 光滑 sigmoid 重参化）；(d) `\kappa_{\mathrm{relax}} > \kappa_{\mathrm{mask}}` 这一致命 `L_2` 判据的实证窗口

---

## §8. Cross-References

- 个体化 / σ 定义 / 三相结构 → `Core_Law/SRT_Individuation.md`
- 遮蔽动力学 / A/B 分期 / 四类干预窗口 / 四类解耦触发 → `Core_Law/SRT_Occlusion_Dynamics.md`
- 苦难 / 两型 / 四类分型 / 反最小化 → `Core_Law/SRT_Suffering.md`
- 主动力学 / `\hat{G}_\theta[\sigma] - \nabla F - \lambda\nabla C_{L_2}` → `Core/SRT_Core_22_Equations.md`
- 路径层 `ρ` / 写回 / scaffold sedimentation → `Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold`
- P1-T06 stable ISP（本文件所有方程的前提）→ `Core/SRT_Core_21b_Constitutive_Theorems.md`
- P1-T07 ε 反闭合必要性（§5.3 健康工作区的结构根据）→ 同上
- P1-T02 ontological time（`w(t)` 写回率的 upstream）→ 同上
- d-value / T_dir / Ψ_f 的 canonical → 对应 `_SRT_*_CANONICAL.md`

---

## §9. 定位与使用规则

- **本文件做**：σ / d_c / T_dir / S 四变量的最小耦合动力学；病理吸引子与健康工作区的结构刻画；反最小化原则的方程化；致命 `L_2` 的可读性层方程化判据
- **本文件不做**：具体 domain 的参数固定、临床量表、实验设计、AI 实现细节
- **引用规则**：涉及四变量耦合、病理吸引子、健康工作区、致命 `L_2` 方程化判据的**方程级**陈述时，优先回链本文件；涉及四变量**概念**定义时，优先回链各自的 L1 主文件（T_dir → `_SRT_T_DIR_CANONICAL.md`）
- **不得**把本文件的方程读成已经过实证检验的定量定律——它是 P1-candidate 结构形式化，是让 draft_v0 文件能够**联合被批评与修正**的手段
