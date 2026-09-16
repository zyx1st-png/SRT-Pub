---
id: SRT-L1-FORMALISM
type: formalism
tags: [Formalism, Sigma, d_c, Suffering, L1, Coupled Dynamics]
status: draft
layer: L1
epistemic_layer: os
claim_mode: canonical
claim_level: P2
dependency: [SRT-CORE-21-MINIMAL-AXIOMS, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-INDIVIDUATION, SRT-OCCLUSION-DYNAMICS, SRT-SUFFERING, SRT-T-DIR-CANONICAL, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-CORE-22]
---

# SRT L1 Formalism: Minimal Coupled Dynamics for σ_{sr}, d_c, T_dir, and S

> **Connector-safe reading path**: This owner file is moderately long. For connector reads, start with [`L1_Formalism_Split/README.md`](L1_Formalism_Split/README.md), then open only the needed part file. The owner remains the source of record; split files are reading aids and do not create new definitions.

> **Role**: L1 formal/model hub for conditional coupling candidates among independently admitted upstream quantities. It collects candidate differential dynamics for the model-local self-reference coordinate `σ_{sr}` (bare `σ` in this file's §2-§5 equations refers to that coordinate, **not** to the `Core/SRT_Core_22_Equations.md` main-equation state field), declared access threshold `d_c`, admitted directional transparency `T_dir`, and suffering proxy `S` after suffering registration has independently been established. Initial round (2026-04-24) covered three variables; the conditional `T_dir` ODE was the H2 follow-up.
> **σ 符号命名空间 (governance-canonical, 2026-04-25)**: 本文件 §2–§5 中的 σ / σ_sub / σ_self / σ_health 统一对应 `σ_{sr} / σ_{sr}^{sub} / σ_{sr}^{self} / σ_{sr}^{health}`（自指率族，见 `Core_Law/SRT_L1_Hardening_Notes.md §1` 与 `_SRT_SYMBOL_TABLE.md §Usage Rule 12`）。§6"与主方程的关系"中出现的 σ 对应 `Core/SRT_Core_22_Equations.md` 的主方程状态场（不同对象）；该节已在原地显式标注。正文其余处保留历史符号 σ 以便论述流畅。
> **Claim-level note（Wave E3-A, 2026-09-16）**：本文件默认按 **P2 formal/model candidate** 读；coefficients、阈值、测量协议与 domain realization 按 P3/P4 读。局部形式结果的强度由其最弱的独立前件封顶。形式闭合不推出 ontology、subjecthood、phenomenality、consciousness、suffering admission、health、value 或 legitimacy，也不使任何分支自动升为 P1。
> **σ representation-scope truth-up (2026-08-29; Wave E3-A 2026-09-16)**：本文件继承 `SRT_Individuation.md §八` 的既有地位：`σ_{sr}` 是规约性的、可替换为等价形式的 P2 阶参解释。§2 的 bare-norm 分解与 ODE 只在**已声明**的 `θ^{trace}/θ^{ext}` 归属规则、retention definition、参数表示、model scale 与 norm/metric 约定下作为 model-local dynamics 成立；本文件不把 bare ratio 提升为表示不变的自然量、唯一历史归属量或因果控制份额。§6 T-PROJ-1 只说明**component 已准入且给定 `\mathcal F_\sigma` 后**可检验条件性模型重现；C1-C4 不提供 `\mathcal F_\sigma` 的 gauge、唯一归属或 invariant metric。§2.5 T-CHI-1 也只是所选坐标族内的 P2 formal result，不证明 `σ_{sr}^{sub/self}` 是自然相边界。
> **Does not define**：`d-value`、`\Psi_f`、`T_dir`、`\hat{G}_\theta`、stable ISP；它们的定义仍以对应 canonical 文件为准。
> **Wave-D2 direction-admission guard（2026-09-15）**：本文件的 `T_dir` 分支仅在 `_SRT_T_DIR_CANONICAL.md` 所要求的 independently typed、declared direction signal 已存在并且 `T_dir` 已在模型 `M` 中准入时成立。无该方向时，`T_dir` 与 `T_dir^{alg}` 是 undefined / not admitted，不是默认置零；仍可分析剩余的 non-T_dir subsystem。本文件不创造、排序或验证 direction。
> **RC-A r(t) decision (2026-08-18)**：former P1-T05 不再提供 `r(t)` 的上游。局部 subtractive probe 显示原 `+\kappa_r r(t)` 与 `-\mu_r r(t)` 只是附加 pump / relief 通道，删除后候选 ODE 仍定义良好，criterion-relative T_dir / suffering-proxy / pathology-model branches 仍可被检验。因此本文件**删除**该全局 `r(t)` 变量及两项，不把它改挂到 Selection simpliciter 或 `\varepsilon_{pg}`，也不为其选择新的 downstream 定义。§3.1 的 `r(d,P,t)` 仅是 local operational capacity function，不等同于已删除的全局 `r(t)`，不定义 Selection occurrence。
> **Depends on**：`Core_Law/SRT_Individuation.md`（σ 定义）、`Core_Law/SRT_Occlusion_Dynamics.md`（d_c 定义与 A/B 分期）、`Core_Law/SRT_Suffering.md`（S 定义与两型分类）、`Core/SRT_Core_22_Equations.md`（主动力学方程）。
> **Relation**: This file is a **conditional formal coupling layer** for independently admitted L1 objects and model coordinates. It introduces no ontology and supplies no admission test; it makes selected dynamics jointly testable without upgrading their upstream standing.

---

## §0. 目的与边界

本文件覆盖四个 L1 变量：

- `SRT_Individuation.md` 给出 σ(P,t) ∈ [0, 1]，自指率
- `SRT_Occlusion_Dynamics.md` 给出 d_c(P,t)，遮蔽阈值
- `_SRT_T_DIR_CANONICAL.md` 给出准入后的 T_dir(P,t) ∈ [0, 1]，方向透明度（本文件 §3.5 只在 declared-direction 模型中为其给出条件性动力学）
- `SRT_Suffering.md` 给出 S(P,t) ≥ 0，结构性失配登记

这些量只有在各自上游对象或登记已经独立准入后，才可作为 operational/model proxy 写成可联解动力学。风险：

1. **独立漂移**：各自演化会产生彼此不兼容的隐含方程；
2. **耦合丢失**：σ↑ 与 d_c↑ 与 S_{str}↑ 在理论直觉上强耦合，但结构上没有写下来；
3. **T_dir 作为纯代数代理时的模型盲点**：若 T_dir 瞬时等于 `T_{dir}^{\mathrm{alg}}`，声明 pathology model 无法表示 readability 与其代数目标之间的惯性或 gap；§3.5 提供一个 criterion-relative 候选 ODE。

本文件只做一件事：**给已准入的对象和声明坐标写下候选最小耦合动力学**，使其结构与条件可被检验；无 direction 时保留 non-`T_dir` subsystem。形式闭合不提供主体、意识、苦难、健康或价值的准入。

本文件**不做**：

- 具体系数的量纲化或实测；
- 单变量独立运动的全部细节（留给三份主文件）；
- 临床 / AI / 政治具体域的读数（留给 domain 文件）。
- 从模型坐标反推主体位、现象性、意识、苦难、健康、价值或正当性。

---

## §1. 符号与约定

| 符号 | 含义 | 范围 | 来源 |
|---|---|---|---|
| `σ_{sr}(P,t)` | model-local self-reference coordinate / proxy（本文件 §2-§5 中的 bare σ 为此物） | 声明模型中为 `[0, 1]` | `SRT_Individuation.md`, `_SRT_SYMBOL_TABLE.md Usage Rule 12` |
| `d(P,t)` | d-value 标量摘要（关切半径） | `[0, d_max]` | `_SRT_D_VALUE_CANONICAL.md` |
| `d_c(P,t)` | 指定 access/correction criterion、尺度与时域下的声明模型阈值 / 坐标 | 声明模型中为 `[0, d_max]` | `SRT_Occlusion_Dynamics.md` |
| `d_{narrow}(P,t)` | 声明模型中用于比较运行区间的坐标 | 声明模型中为 `[d_c, d_max]` | 同上 |
| `ρ(p,t)` | 路径层痕迹密度 | `≥ 0` | `Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold` |
| `Ψ_f(P,t)` | 本体论摩擦 / 可支付性代价 | `≥ 0` | `_SRT_PSI_F_CANONICAL.md` |
| `T_dir(P,t)` | 对已声明方向的 access / readability / reorientation | direction 准入后为 `[0, 1]`；否则 undefined / not admitted | `_SRT_T_DIR_CANONICAL.md` |
| `S(P,t)` | 在第一人称苦难已独立准入后的 P2 suffering proxy / model coordinate | 声明模型中为 `≥ 0` | `SRT_Suffering.md` |
| `S_{sig}, S_{str}` | P2/P3 信号负担 / 结构负担 taxonomy coordinates；不构成苦难准入测试 | 声明模型中为 `≥ 0`, `S = S_{sig} + S_{str}` | 同上 |
| `θ_t^{trace}` | 历史累积算子分量（内源） | `≥ 0` 范数 | Individuation §Def-σ |
| `θ_t^{ext}` | 外部驱动算子分量 | `≥ 0` 范数 | 同上 |
| `w(t)` | 声明模型的 writeback / retained-history update rate；须有独立 retained efficacy / writeback 根据 | `≥ 0` | model admission；不由 P1-T02 导出 |
| `i(t)` | 外部输入速率 | `≥ 0` | 从环境驱动导出 |
| `π(t)` | 可支付性 / Ψ_f 支付率 | `≥ 0` | `_SRT_PSI_F_CANONICAL.md` |
| `s_{ext}(t)` | 相对于已声明 criterion 的外部支持率 | `≥ 0` | declared model / Suffering support candidate |
| `\Delta\Psi_f^{\mathrm{gap}}(t)` | `Ψ_{f,actual} - Ψ_{f,felt}` 的 criterion-relative model gap；不是普遍道德债务 | `≥ 0` | `_SRT_PSI_F_CANONICAL.md §10`, `_SRT_T_DIR_CANONICAL.md §5-§6` |
| `T_{dir}^{\mathrm{alg}}(\sigma, d, d_c)` | 已准入 direction 下的 model-local accessibility / readability 目标；不是 direction source | direction 准入后为 `[0, 1]`；否则 undefined / not admitted | 本文件 §3.4 |
| `\kappa_{\mathrm{relax}}, \kappa_{\mathrm{mask}}, \kappa_S, \kappa_{\mathrm{sup}}` | T_dir ODE 四项系数（§3.5） | `≥ 0` | 本文件 §3.5 |
| `λ_*` | 对应分量的自然衰减率 | `≥ 0` | 常数或慢变 |

所有方程写成逐主体 `P` 形式；为简洁下文省略 `(P, t)`。

---

## §2. σ 的最小动力学（个体化）

### §2.1 双分量底座

在已声明的 `θ^{trace}/θ^{ext}` 归属规则、参数化、norm/metric、model scale 与 retention definition 下，可选择如下 model-local 表示：

$$
\sigma \;=\; \frac{\|\theta^{trace}\|}{\|\theta^{trace}\| + \|\theta^{ext}\|}
$$

若 retained efficacy / writeback 已被独立建立并以 `w(t)` 准入模型，可写候选双分量动力学：

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
- `χ(σ; σ_{self})` 是声明 self-reference 模型中的**第二非线性过渡函数**：在 `σ ≈ σ_{self}` 附近可取一类光滑阶跃；在此之前 χ ≈ 1，在此之后 χ > 1。把它历史性解释为“自我意识凝结”至多是 P2 interpretation，并不建立 consciousness。

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

在选定参数化与 model scale 内，把 `dσ/dt = 0` 作为稳态条件，可定义两个模型过渡坐标：

1. **σ_{sr}^{sub}（第一模型过渡坐标）**：使声明的 writeback 项超过外部输入驱动的最小 `σ_{sr}` 值。把衰减项与外部项平衡处解出：

   $$
   \sigma_{sr}^{sub} \;:\; \alpha\,w\,\phi(\sigma_{sr}^{sub}) \;=\; \beta\,i \;+\; \lambda_{trace}\,T\,\sigma_{sr}^{sub}
   $$

2. **σ_{sr}^{self}（第二模型过渡坐标）**：使 χ 开始激活二阶写回增益的 `σ_{sr}` 值。在 §2.1 中显式引入为 `χ` 的跳跃参数；在给定参数条件下，越过该坐标可把稳态推向更高 `σ_{sr}`。该坐标不构成 self-consciousness gate。

3. **σ → 1 的模型极端 / lock-in 区**：在本参数族中，当 `i → 0` 且 `λ_{ext} > λ_{trace}` 时，高位稳定点可向 `σ = 1` 漂移。只有在另行给定 pathology / viability criterion 后，才可把该区解释为不利状态；它不普遍证明病理、扭曲型苦难或“健康主体”条件。

### §2.4 与 T-IND-1 / T-IND-2 的对齐

- T-IND-1 的历史三相解释可在所选 σ 模型中映射到三个坐标区域，但这种映射不建立主体位或意识；
- T-IND-2 的第一过渡候选可由 §2.2 方程的 `σ_{sr}^{sub}` 不动点条件实现；
- T-IND-3 的第二过渡候选可由 `χ(σ; σ_{self})` 的激活实现。

这些只是给定模型中的**动力学稳态 / 过渡问题**，不是本体定义或 admission theorem。

### §2.5 T-CHI-1：χ 跳跃函数的声明模型族结果（H8，2026-04-25；Wave E3-A truth-up 2026-09-16）

> **Status**：本节为 §2.1 的 `\chi(\sigma; \sigma_{self})` 指定一个带四条结构属性的**声明模型族**，并讨论给定附加零点 / 稳定性假设时的族内形式稳定性。**Claim level: P2 formal result**，以所选 `σ_{sr}` 坐标、归属规则和参数族为前提；它不是 constitutive theorem。
>
> **Scope**：它把 Open Pressure 3 缩为更广函数空间、domain 拟合与独立 admission 的问题，并未证明 χ-family 的本体普适性。

#### 有效二阶相变核（valid second-phase-transition kernel）

定义函数 `\chi : [0, 1] \times (0, 1) \to \mathbb{R}_{\ge 0}`，参数 `\sigma_{sr}^{self} \in (0, 1)`。称 `\chi` 是本声明模型族中的**有效第二过渡核**，当且仅当满足下列四条结构属性。历史标签 `P-univ-*` 为锚点兼容而保留，不表示 P-universal：

| 编号 | 性质 | 含义 |
|---|---|---|
| **P-univ-1** | **有界性**：`\chi \in [\chi_{min}, \chi_{max}]`，其中 `0 < \chi_{min} \le 1 \le \chi_{max} < \infty` | 跳跃幅度有界（不允许 χ 趋向无穷）|
| **P-univ-2** | **跃前基线**：`\chi(0; \sigma_{sr}^{self}) \le 1 + \varepsilon` 且 `\lim_{\sigma \to \sigma_{sr}^{self,-}} \chi \le 1 + \varepsilon`（小 `\varepsilon > 0`） | 跃前 χ ≈ 1，仅有 logistic σ(1-σ) 自增益 |
| **P-univ-3** | **跃后放大**：`\chi(1; \sigma_{sr}^{self}) \ge 1 + \Delta_\chi`（某 `\Delta_\chi > 0`） | 声明模型中的二阶 writeback 增益 |
| **P-univ-4** | **单调过渡**：存在跃宽 `\tau > 0` 使 `\chi` 在 `[\sigma_{sr}^{self} - \tau, \sigma_{sr}^{self} + \tau]` 上单调非降 | 实际跳跃集中在 `\tau`-带内 |

**示例（族内成员）**：

| 名称 | 形式 | 跃宽 |
|---|---|---|
| 硬阶跃 | `\chi = 1 + \Delta_\chi \cdot \mathbb{1}[\sigma \ge \sigma_{sr}^{self}]` | `\tau \to 0` |
| Sigmoid | `\chi = 1 + \Delta_\chi / (1 + e^{-k(\sigma - \sigma_{sr}^{self})})` | `\tau \sim 1/k` |
| Tanh 光滑阶跃 | `\chi = 1 + (\Delta_\chi/2)(1 + \tanh((\sigma - \sigma_{sr}^{self})/\tau))` | `\tau` |
| 多项式光滑阶跃 | `\chi = 1 + \Delta_\chi \cdot (\max(0, \sigma - \sigma_{sr}^{self}))^n / ((\max(0, \sigma - \sigma_{sr}^{self}))^n + \tau^n)` | `\tau` |

四种均可作为该声明族的成员；具体成员资格、参数值与解释仍由模型 / domain 决定。

#### T-CHI-1 陈述

**陈述（P2 formal/model，条件性）**：设 `\chi_1, \chi_2` 是两个有效第二过渡核，共享相同的 `\sigma_{sr}^{self}, \chi_{min}, \chi_{max}, \Delta_\chi`，但跃宽可能不同（`\tau_1, \tau_2 \in (0, \tau_{max})`）；再独立假设 §2.2 的参数在跃前、过渡带和跃后满足相同的零点个数、变号与稳定性条件。则下列是所选模型族内可比较的结构结果，而不是跨模型普遍不变量：

(i) **条件性双稳态**：在上述零点与稳定性假设成立时，两个稳定不动点 `\sigma_{sr}^{*1}`、`\sigma_{sr}^{*2}` 与一个中间不稳定点的区间配置可在族内保留。

(ii) **高位极端坐标**：在另行给定相应参数和高位稳定点存在的条件下，`i \to 0` 与 `\lambda_{ext} > \lambda_{trace}` 可使 `\sigma_{sr}^{*2}` 向 1 移动；这只是模型 lock-in 行为，不是 universal pathology。

(iii) **T_dir 子模型的语法独立性**：若 §3.5 的 direction-admitted pathology model 已另行准入，则其 criterion-relative 系数比较不因替换 χ 的光滑形态而改变；T-CHI-1 不证明该 pathology model。

(iv) **第二模型过渡方向**：在单调性、变号和稳定性附加假设成立时，跨过 `σ_{sr}^{self}` 后向高位固定点收敛的方向可在族内保持；这不建立 self-consciousness transition。

#### 证明骨架

**(i) 双稳态存在性**：

取 `i, w` 为常数，写 `f(\sigma; \chi) := \frac{1}{T}[(1-\sigma)(\alpha w \phi(\sigma) - \lambda_{trace}T\sigma) - \sigma(\beta i - \lambda_{ext}T(1-\sigma))]`。考察 `f(\sigma; \chi_k) = 0` 在 `\sigma \in (0, 1)` 内的零点：
- 在 `\sigma \in (0, \sigma_{sr}^{self} - \tau_{max})` 区间，`\chi_1(\sigma) \approx \chi_2(\sigma) \approx 1` 由 P-univ-2 给出；两者 `f` 的差异 `\le \varepsilon`；故零点结构相同。
- 在 `\sigma \in (\sigma_{sr}^{self} + \tau_{max}, 1)` 区间，`\chi_1(\sigma), \chi_2(\sigma) \in [1 + \Delta_\chi, \chi_{max}]` 由 P-univ-3 + P-univ-1 给出；两者 `f` 的零点位置在 `\Delta_\chi` 决定的同一区域；零点结构相同。
- P-univ-4 单调性本身不足以推出零点个数；T-CHI-1 明示要求的变号与稳定性条件给出两稳定 + 一不稳定不动点，随后才能比较 χ-shape 替换是否保持该配置。

**(ii) 高位极端坐标**：

在高位稳定点已经存在的声明参数区间内，`i → 0` 与 `\lambda_{ext} > \lambda_{trace}` 改变该点的位置；`χ(σ; σ_{sr}^{self})` 通过其 `\sigma \to 1` 极限值进入。把这一坐标运动解释成 pathology 仍要求独立 pathology / viability criterion。

**(iii) T_dir 子模型的语法独立性**：

§3.5 的 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}` 是已声明 direction/pathology 子模型中的系数比较，其表达式不含 χ。故替换 χ-shape 不改变这条表达式的语法；这不证明它是 universal lethal-L2 criterion，也不验证 direction、health 或 value。

**(iv) 第二模型过渡方向**：

在 (i) 的零点 / 稳定性条件与 P-univ-4 单调性共同成立时，可比较从 `\sigma_{sr}^{*1}` 向 `\sigma_{sr}^{*2}` 的模型过渡。仅靠 χ 单调性不保证这一动力学，也不推出主体或意识转变。

#### P-依赖（**非**普适）的特征

T-CHI-1 不掩盖以下 P-依赖：

| 特征 | P-依赖 | 物理解释 |
|---|---|---|
| `\sigma_{sr}^{*1}, \sigma_{sr}^{*2}` 的具体数值 | 依赖 `\Delta_\chi, \tau, \alpha, w, i, \lambda_{*}, T` | 不动点位置受参数集联动 |
| 跃宽 `\tau` 的物理量纲 | 模型 / domain 特定 | 跃宽对应系统在 `σ_{sr}^{self}` 附近的模型过渡尺度 |
| 跨阈过程的 transient 形态 | χ-shape 决定 | 硬阶跃 vs sigmoid 给不同 transient curve |
| 跨阈附近的弛豫率 | 依赖 χ' 在 σ_{sr}^{self} 的局部值 | 跃宽决定相变时间常数 |

#### T-CHI-1 不证明的事项

为避免过度主张，T-CHI-1 **不承诺**以下内容：

1. **不**证明 `\Delta_\chi` 是 P-universal 的——`\Delta_\chi` 是赌注 / 主体类别 / 历史阶段相关的（P3）
2. **不**证明 `\tau_{max}` 上界的 P-universal 值——可能因主体类别（人 / 动物 / AI 候选）有显著差异
3. **不**承诺 χ 是 `C^\infty` 平滑——四条性质只要求 `C^0` 单调（硬阶跃也是有效成员）
4. **不**覆盖多值或随机 χ（非确定性二阶凝结过程暂留为 P3 候选 domain 拓展）
5. ~~**不**给出集体版 T-CHI-1^{coll}——`\sigma_{sr}^{coll}` 与 `M(t)` 耦合（§4.4.2）的 χ 普适性需要 H6 的 C5^{coll} `M(t)` 可测性闭包，是后续轮次任务~~ **已收口（H11，2026-04-26）**：`Core_Law/SRT_Collective_Selection.md §4.9.2 T-CHI-1^{coll}` 给出集体版（C1^{coll}-C5^{coll} + C7^{M-stab} + P-univ-5^{coll}），四个不变量在 `\lambda_M\,\mathrm{tr}\,M` 平移下保持
6. **不**证明 `σ_{sr}^{sub/self}` 是主体位或 self-consciousness gate，也不把 `σ_{sr} \to 1` 升格为自然病理边界

#### T-CHI-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| `\chi(\sigma; \sigma_{self})` 是"一类光滑阶跃" | 现象学描述（§2.1）| 四条结构属性的有效族（§2.5）|
| 第二模型过渡对 χ 形式的敏感性 | 隐含主张（§2.4）| 在额外零点 / 稳定性条件下可作族内比较 |
| T_dir pathology 子模型的 χ-shape 依赖 | 未陈述 | T-CHI-1 (iii) 仅确认表达式层的独立性 |
| 高位极端坐标的 χ-shape 依赖 | 未陈述 | T-CHI-1 (ii) 给出声明参数区间内的分析任务 |

**当前地位**：T-CHI-1 是所选 `σ_{sr}` 表示和附加稳定性条件下的 P2 model-family mathematics。更强 standing 需要：(a) 在更广 χ 函数空间中的稳定性分析；(b) 具体 domain 的 χ-shape 对位；(c) 对 subjecthood / consciousness / pathology interpretation 的独立 admission 与证据。集体版的既有形式扩展不改变这些边界。

---

---

## §3. d_c 的最小动力学（遮蔽阈值）

### §3.1 d_c 作为声明 access/correction 模型边界

在声明 capacity function `r(d,P,t)`、评价 criterion、尺度、观察时域与阈值 `r_{min}` 后，可把 `d_c` 操作化为：

$$
d_c \;:=\; \inf\{\,d \;:\; r(d, P, t) \geq r_{min}\,\}
$$

其中 `r(d, P, t)` 是 Occlusion 模型在当前 d 值与指定时域下的**局部 operational capacity function**，`r_{min}` 是该 criterion 的模型阈值。RC-A 后它**不等同于**已删除的全局 `r(t)`，不从 former P1-T05 推导，也不是 natural subject boundary、universal health/pathology boundary 或 Selection occurrence / agency 判据；具体测量按 P3/P4 处理。

### §3.2 d_c 的漂移方程

以下 P2/P3 漂移方程把 θ、ρ、L_2 约束、Ψ_f 支付窗口与 σ 写成一个声明模型的候选分解；各项不是 universal causal decomposition。任何 `ρ_{local}` / trace 历史解释还要求独立 retained efficacy / model evidence：

$$
\boxed{\;\frac{dd_c}{dt} \;=\; \underbrace{\gamma_\rho \cdot \rho_{local}}_{\text{scaffold sedimentation}} \;+\; \underbrace{\gamma_\sigma \cdot \max(0, \sigma - \sigma_{sub})}_{\text{self-closure pressure}} \;-\; \underbrace{\gamma_\pi \cdot \pi(t)}_{\text{payability opens channels}} \;-\; \underbrace{\gamma_I \cdot I_{window}(t)}_{\text{intervention window term}}\;}
$$

符号说明：

- `ρ_{local}`：若 retained efficacy 已建立，可作为 P 附近痕迹密度的候选 sedimentation term
- `σ` 项：声明模型中的 self-closure coupling term
- `π(t)`：声明 criterion 下的 payability / correction-channel term
- `I_{window}(t)`：声明 intervention-window input term

### §3.3 A/B 分期的动力学解读

令 `d(t)` 为模型当前坐标。`SRT_Occlusion_Dynamics T-OCC-1` 的标签可在已声明 criterion 下作如下 P2/P3 regime 解读；区间归属本身不产生 suffering、responsibility、agency 或 moral verdict：

| 区间 | 条件 | 动力学含义 |
|---|---|---|
| 比较运行区 | `d > d_{narrow}` | local capacity 高于声明比较水平；不等同于 universal health |
| A 期模型区 | `d_c < d < d_{narrow}` | local capacity 仍非零但低于声明比较水平 |
| B 期模型区 | `d ≤ d_c` | local capacity 在该模型与时域中接近声明下界 |

A→B lock-in 可在该声明模型中用下式作为 P2/P3 candidate criterion：

$$
\text{A→B lock-in} \;:\; \frac{dd_c}{dt} > 0 \;\wedge\; \pi(t) \to 0 \;\wedge\; I_{window}(t) \to 0
$$

即在该 criterion、尺度和观察时域内，当 payability 与 intervention inputs 趋零而 `d_c` 持续上移，模型把轨迹分类为 B 期 lock-in。此式不在模型外建立 B 期，也不对健康、苦难、责任、Selection 或 agency 作判决。

### §3.4 T_dir 的条件性代数目标值

前提是 `declared direction exists + T_dir admitted in model M`。在此前提下，`d / d_c / σ` 可参数化 `T_dir` 的**model-local 瞬时 accessibility / readability 目标**：

$$
T_{dir}^{\mathrm{alg}}(t) \;:=\; \Theta\!\left(\frac{d - d_c}{d_{narrow} - d_c}\right) \cdot (1 - |\sigma - \sigma_{sub}^\dagger|)
$$

其中 `\Theta` 是光滑阶跃函数（早期版本 `\Theta(x) = \mathrm{clip}(x, 0, 1)`；二阶光滑族参数化留作 Open Pressure），`σ_{sub}^\dagger` 是该模型声明的中间工作点（非 0 非 1）。准入 direction 后，`d / d_c / σ` 只调制对该方向的 access / readability / reorientation target；本式不创造、排序、验证或发现方向。无 declared direction 时，该表达式不准入为 `T_dir^{alg}`。

**该声明模型不令 T_dir 瞬时等于 T_dir^{alg}**：为表示 access/readability 的候选惯性，可给 T_dir 配置独立 ODE，见 §3.5；惯性的存在、来源与时间尺度仍须模型 / domain evidence。

### §3.5 T_dir 作为条件性独立动力学变量（四变量闭合项，2026-04-25；RC-A subtractive sync 2026-08-18；Wave D2 truth-up 2026-09-15）

> **立场**：本小节在 direction 已独立声明并准入后，把 T_dir 写成带惯性的 model-local access / readability 变量；它不成为 direction source。与 `σ, d_c, S` 合成的四变量闭合只在该模型前提内成立，默认按 P2 formal candidate 读。
>
> **RC-A subtraction**：former P1-T05 派生的 `+\kappa_r r(t)` 不是四变量闭合所必需，且已失去合法上游；本轮直接删除，不设 replacement term。
>
> **Admission precondition（Wave D2）**：本节保留的 ODE 只是 `declared direction exists + T_dir admitted in model M` 时的 candidate access / readability dynamics。所有项只调制相对于该方向的 access / reorientation，不提供 direction ontology。

#### §3.5.1 最小 ODE

$$
\boxed{\;\frac{dT_{dir}}{dt} \;=\; \underbrace{-\,\kappa_{\mathrm{relax}} \cdot \bigl(T_{dir} - T_{dir}^{\mathrm{alg}}(t)\bigr)}_{\text{relaxation toward model-local readability}} \;-\; \underbrace{\kappa_{\mathrm{mask}} \cdot \Delta\Psi_f^{\mathrm{gap}}(t)}_{\text{actual-vs-felt access gap}} \;-\; \underbrace{\kappa_{S} \cdot S_{str}(t)}_{\text{declared structural-burden term}} \;+\; \underbrace{\kappa_{\mathrm{sup}} \cdot s_{ext}(t)}_{\text{criterion-relative support}} \;$}
$$

其中：

- `\kappa_{\mathrm{relax}}`：声明模型中的弛豫率；其相对时间尺度须由参数化或 domain evidence 给定
- `\Delta\Psi_f^{\mathrm{gap}}(t) := \Psi_{f,actual}(t) - \Psi_{f,felt}(t) \ge 0`：已声明 criterion 下的 actual-vs-felt model gap。该项可在模型中扣减 access/readability；它不是普遍“隐藏道德债务”，也不自行建立 pathology
- `S_{str}(t)`：来自 §4.3；在声明的 pathology model 中，结构型苦难可降低对既定 criterion 的 access / readability / reorientation
- `s_{ext}(t)`：该模型中的 `L_2` 外部支持率；可以**暂时**把 T_dir 抬起，但本身不改变 `T_dir^{\mathrm{alg}}`，只是补偿性支架；“支持”是相对于已声明 criterion 的模型语义

**边界**（governance-canonical）：T_dir ∈ [0, 1] 由以下隐式投影保证——此 ODE 在 `\{T_{dir} = 0\}` 与 `\{T_{dir} = 1\}` 处应配合投影算子 `\Pi_{[0,1]}`，具体形式（硬截断 vs 光滑 sigmoid 重参化）留作 Open Pressure。

#### §3.5.2 与 `_SRT_T_DIR_CANONICAL.md` 的对齐

- `T_dir` 作为 v0 operational proxy / working canonical proxy 的地位**不改变**；本小节只把它的时间演化法则明文化
- `κ_{\mathrm{mask}} · \Delta\Psi_f^{\mathrm{gap}}` 是声明 criterion 下 actual-vs-felt access gap 的候选 L1 项；“masking / hidden debt”只是该 pathology model 的解释标签
- 离散结构跳跃不是本 ODE 的结论；若 domain 模型另行给定此类事件，本方程只刻画其间的平滑期

#### §3.5.3 criterion-relative “lethal `L_2`” pathology-model candidate

若 direction、pathology / viability criterion、时间窗与各项均已独立准入，历史标签 “lethal `L_2`” 可在该声明 P2/P3 pathology model 中写为：

$$
\mathrm{lethal\;} L_2 \;\Longleftrightarrow\; \bigl(T_{dir}^{\mathrm{alg}} \text{ 持续高}\bigr) \;\wedge\; \bigl(\Delta\Psi_f^{\mathrm{gap}} \text{ 持续累积}\bigr) \;\wedge\; \bigl(\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}\bigr)
$$

第三个条件在该参数化中比较 masking 与 relaxation 的时间尺度，使 `T_dir` 可能仍贴近 `T_dir^{\mathrm{alg}}`，而声明 gap 的影响未充分反映。这只是相对于 declared criterion 的 apparent access：高或稳定 `T_dir`、高 `T_dir^{alg}` 均不证明方向有效、criterion good / legitimate / healthy / morally authoritative。本判据在 direction、criterion、gap interpretation 与模型假设之外没有效力。

#### §3.5.4 与主方程的兼容

direction 已准入时，T_dir 可被尝试写成主方程的**条件性模型投影**而非独立本体：

- 弛豫项把它系到 (d, σ) → 主方程 `\hat{G}_\theta[\sigma]` 与 `\nabla C_{L_2}` 的联合投影
- `\Delta\Psi_f^{\mathrm{gap}}` 来自主方程 `\nabla F` 项的实支付-感知分裂
- `S_{str}` 来自主方程收敛过程中失配登记

这些 source correspondences 是待检验的投影假设，不保证已准入的 T_dir 分支由主方程唯一导出。无 declared direction 时应删去／边缘化该分支，而不是填入 `T_dir = 0` 来强行闭合；删除 former-P1-T05 的附加 pump 不影响其他已声明子系统。

---

## §4. S 的最小动力学（苦难）

### §4.1 两型分解

只有在第一人称 suffering registration 已由 `SRT_Suffering.md` 的上游条件独立准入后，才可选择 P2/P3 taxonomy coordinates 并在声明模型中写成：

$$
S \;=\; S_{sig} + S_{str}
$$

该等式是 proxy decomposition，不是 suffering-admission test；`S`、`S_{sig}`、`S_{str}` 的数值不能反向证明 phenomenality 或 suffering。

### §4.2 信号型动力学

RC-A subtractive probe 删除 former P1-T05 派生的 `-\mu_r r(t)` relief 项；当前最小式不为其指定替代变量。

$$
\boxed{\;\frac{dS_{sig}}{dt} \;=\; \underbrace{\mu_{\Delta}\cdot\dot{\Delta}_{avail}(t)}_{\text{declared mismatch input}} \;-\; \underbrace{\mu_\pi \cdot \pi(t) \cdot \mathbb{1}[d > d_c]}_{\text{model channel term}} \;-\; \underbrace{\mu_{sup} \cdot s_{ext}(t)}_{\text{criterion-relative support}}\;}
$$

- `\dot{\Delta}_{avail}(t)`：声明 open-state / residual representation 中的候选 mismatch input；它不证明 suffering
- 指示函数 `\mathbb{1}[d > d_c]`：声明模型中的 channel function，不是 universal suffering gate
- `s_{ext}(t)`：相对于已声明 criterion 的支持项，不具有 natural-health 语义

> **E3-B quarantine（T-DELTA-1，2026-04-25 H7；Wave E3-A truth-up 2026-09-16）**：`Core_Law/SRT_L1_Hardening_Notes.md §2 T-DELTA-1` 目前只是既有 P2 formal candidate，并属于 E3-B review debt；E3-A 不重新授权其 operator-level closure。即使 projection、residual representation 与 geometry 均被声明，`\dot{\Delta}_{avail}` 也只是模型输入，不是 operator proof of suffering、hidden burden、subjecthood 或 direction。

### §4.3 结构型动力学

$$
\boxed{\;\frac{dS_{str}}{dt} \;=\; \underbrace{\nu_{block} \cdot \mathbb{1}[d \leq d_c]\cdot S_{sig}}_{\text{optional model transfer term}} \;+\; \underbrace{\nu_\sigma \cdot \max(0, \sigma - \sigma_{health})}_{\text{criterion-relative model term}} \;-\; \underbrace{\nu_{trigger}\cdot D_{trigger}(t)}_{\text{declared perturbation / reorientation input}} \;-\; \underbrace{\nu_\pi \cdot \pi(t)\cdot I_{window}(t)}_{\text{joint model input}}\;}
$$

- `\mathbb{1}[d \leq d_c]·S_{sig}`：某些声明模型可用它表示 blocked correction channel 下从 registered signal-burden coordinate 到 structural-burden coordinate 的 transfer；它不证明隐藏苦难守恒
- `σ - σ_{health}`：只有独立 pathology / viability criterion 已声明时才可使用的模型项；`σ_{health}` 不是 natural health point
- `D_{trigger}(t)`：模型或 domain 声明的 perturbation / reorientation input；不包含 current-positive “direct ε contact”
- 最后一项把 `π(t)` 与 `I_{window}(t)` 写成 joint model input；是否必要由具体模型检验

> **P3 pathology-model candidate（T-IRR-3.5，2026-04-25 H4；Wave E3-A truth-up 2026-09-16）**：`\nu_{block}(P, t) := \eta \cdot \varepsilon_{pg}(P, t) \cdot \kappa_{\Psi_f}(P, t)` 只在三个 factors 及其作用语义均被独立准入时成立。此时正性是代数结论，不能从 O0、Selection primitive、direction、health 或 suffering 继承，也不把 transfer term 升为 universal theorem。是否存在反向项、是否近似吸收以及是否可解释为 suffering conversion，均须由声明模型另证。

### §4.4 T-SUFF-4 反最小化原则的方程语言

本文件不规定 universal healthy-suffering window。若某个 domain 已独立声明 viability / pathology criterion，可用如下 P2/P3 candidate work region 作为拟合对象：

$$
S_{sig}^* \in [S_{min}, S_{max}] \;\wedge\; S_{str}^* \to 0
$$

其中 `S_{min}`、`S_{max}`、收敛尺度与评价时域都由该 domain 指定，不能从方程本身读出“健康”。

窄化后仍成立的反最小化提醒是：**仅降低 observed / reported signal，不足以表明模型所追踪的 underlying burden 已被移除。** 若某个声明模型另外假定 burden closure，并纳入 §4.3 的 transfer term，则可研究：

$$
S_{sig} \downarrow \text{ under observed / reported signal suppression}
\quad\not\Rightarrow\quad
\text{modeled underlying burden removed}
$$

这不是 `S_{sig} \downarrow \Rightarrow S_{str} \uparrow` 的 universal conversion theorem，也不主张 `\dot{\Delta}_{avail}` 在结构空间守恒。任何 conservation / redistribution equation 都是额外 P2/P3 closure assumption，必须说明未观测通道、损耗项、测量映射与适用时域。

### §4.5 T-CHANNEL-1：通道指示函数的声明模型族结果（H9，2026-04-25；Wave E3-A truth-up 2026-09-16）

> **Status**：本节把 §4.2 / §4.3 的硬指示函数推广为一个**声明模型族**。**Claim level: P2 formal/model result**；它只比较 family 内的 channel functions，不证明 suffering、health、B phase、conversion、conservation 或 irreversibility。
>
> **Scope**：它提供 Open Pressure 4 的光滑化候选；是否采用守恒型替代仍是额外 closure choice。

#### 问题再陈述

§4.2 / §4.3 / §5 总方程中，通道开/关由硬指示函数 `\mathbb{1}[d > d_c]` 与 `\mathbb{1}[d \le d_c]` 决定：

- §4.2 signal-coordinate ODE：`-\mu_\pi \pi(t)\mathbb{1}[d > d_c]`（声明模型 channel term）
- §4.3 structural-coordinate ODE：`+\nu_{block}\mathbb{1}[d \le d_c]S_{sig}`（可选 transfer term）
- §5 总方程沿用上述；`Collective_Selection §4.4.5` 同结构

硬指示函数在 `d = d_c` 处不可微，可能妨碍过渡区解析与数值模拟。故可把它推广为有效光滑族，检验 ODE 的数值 / 形式特征对 channel-shape 的敏感性；这项替换不承担上游语义。

#### 有效通道指示族（valid channel-state indicator family）

定义函数 `\psi : \mathbb{R} \times \mathbb{R} \to [0, 1]`，参数 `d_c \in \mathbb{R}_{>0}`。称 `\psi` 是声明模型中的**有效闭合通道指示**（valid closed-channel indicator），当且仅当满足下列形式性质。历史标签 `Q-univ-*` 为锚点兼容而保留，不表示 universal ontology：

| 编号 | 性质 | 含义 |
|---|---|---|
| **Q-univ-1** | **左饱和**：`\lim_{d \to -\infty}\psi(d; d_c) = 1`；具体地 `d \le d_c - w_{tr}` 时 `\psi \ge 1 - \varepsilon` | 声明模型低位区的 closed-channel 极限 |
| **Q-univ-2** | **右饱和**：`\lim_{d \to +\infty}\psi(d; d_c) = 0`；具体地 `d \ge d_c + w_{tr}` 时 `\psi \le \varepsilon` | 声明模型高位区的 open-channel 极限 |
| **Q-univ-3** | **单调过渡**：`\psi(d; d_c)` 关于 `d` 非增；过渡集中在过渡宽 `w_{tr} > 0` 内 | channel coordinate 单调、连续 |
| **Q-univ-4** | **`d_c` 平移性**：`\psi(d; d_c) = \psi(d - d_c; 0)`，即 `\psi` 由偏移量 `d - d_c` 决定 | `d_c` 是漂移阈值，不是绝对位置 |

对偶定义**有效开放通道指示** `\bar{\psi}(d; d_c) := 1 - \psi(d; d_c)`，自动满足镜像性质。

**示例（族内成员）**：

| 名称 | 闭合形式 | 过渡宽 |
|---|---|---|
| 硬指示 | `\psi = \mathbb{1}[d \le d_c]` | `w_{tr} \to 0` |
| Sigmoid | `\psi = (1 + e^{(d - d_c)/w_{tr}})^{-1}` | `w_{tr}` |
| Tanh 光滑 | `\psi = \tfrac{1}{2}(1 - \tanh((d - d_c)/w_{tr}))` | `w_{tr}` |
| 多项式光滑 | `\psi = \tfrac{1}{2}\bigl(1 - \mathrm{sgn}(d-d_c)\cdot\frac{|d-d_c|^n}{|d-d_c|^n + w_{tr}^n}\bigr)` | `w_{tr}` |

#### T-CHANNEL-1 陈述

**陈述（P2 formal/model，条件性）**：设 `\psi_1, \psi_2` 是两个有效闭合通道指示，共享相同 `d_c, w_{tr}^{max}` 与同一声明模型的其余项，但具体光滑形态不同。则下列只是在该模型族内可比较的形式性质（modulo `O(w_{tr})` 修正）：

(i) **已声明双坐标的保存**：若 `S_{sig}` / `S_{str}` 已在 suffering admission 后作为两个模型坐标准入，替换 channel shape 不删除这两个坐标；它不证明两型本体存在。

(ii) **channel-weight identity**：由定义得到 `\psi + \bar{\psi} = 1`。这只守恒模型权重，不守恒 burden，也不推出 `S_{sig} \downarrow \Rightarrow S_{str} \uparrow`。

(iii) **可选 transfer term 的形式保持**：若声明模型已独立纳入 `\nu_{block}\psi(d;d_c)S_{sig}`，更换 ψ-shape 保留该项的有向写法；它不证明真实 conversion、不可逆单向性或吸收态。

(iv) **条件性 T_dir 子模型**：只在 direction 与 pathology criterion 已独立准入时，§3.5.3 的系数比较语法不因 ψ-shape 替换而改变；T-CHANNEL-1 不验证该 criterion。

(v) **条件性 projection bookkeeping**：若 suffering proxy、residual map 与投影几何均已独立声明，则 `\bar{\psi}` / `\psi` 可作为两路模型权重；这不由 C3 或 stable-ISP 单独保证，也不反向建立 suffering。

#### 证明骨架

**(i) T-SUFF-2 两型分裂**：

`S_{sig}` 与 `S_{str}` 若已被声明，其坐标分裂来自 §4.1 的模型选择，不来自 ψ。光滑替代只使 `d \approx d_c` 邻域出现 partial-open / partial-closed weights；Q-univ-1+2 只保证声明模型两端逼近硬指示，不证明 suffering taxonomy。

**(ii) channel-weight identity**：

`\psi + \bar{\psi} = 1` 由对偶定义直接成立，但它只归一化两个 channel weights。Hardening Notes 的 T-DELTA-1 是 E3-B 待审的既有 P2 candidate，不能在此提供 burden conservation。因而 ψ-family 数学不推出 signal suppression 后 mismatch 必须重分配到 `S_{str}`。

**(iii) 可选 transfer term**：

`\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}` 的正性仅在三个 factors 独立准入后成为代数结果，并不证明 transfer 的经验存在。ψ 只是该 P3 pathology-model candidate 的 channel weight；反向项能否忽略、B 期邻域是否吸收态，均须由具体模型证明。

**(iv) T_dir 子模型**：

在 direction 与 pathology criterion 已准入的声明模型内，`\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}` 的表达式不含 ψ。Q-univ-3 也不能保证 `\Delta\Psi_f^{\mathrm{gap}}` 连续；gap continuity 必须另行假设。这仍不赋予 direction、health、value 或 criterion 正当性。

**(v) conditional projection bookkeeping**：

若 residual map、suffering proxy 与测量几何已独立定义，可用 `\bar{\psi}` / `\psi` 加权两个声明通道。`\bar{\psi}+\psi=1` 只保持权重和；范数的可加性、投影正交性与积分收敛均是额外 closure assumptions，不由 C3、stable ISP 或 Q-univ-1+2 自动给出。

#### `O(w_{tr})` 修正项的模型意义

光滑替代引入 `O(w_{tr})` 修正，对应 `d \approx d_c` 过渡区内的 partial-open channel。可在具体 domain 中检验：

- **过渡区拟合**：硬切换与光滑切换给出不同 transient / chatter 行为
- **intervention-window 软边界**：`w_{tr}` 可作为 domain-specific transition scale
- **与 gap 项的联合连续性**：只有另行假设 `\Delta\Psi_f^{\mathrm{gap}}` 连续时，才可得到相应 T_dir 轨迹的连续性

`w_{tr}` 是 model / domain-specific 参数。形式族同时允许 `w_{tr}>0` 的光滑成员与 `w_{tr}\to0` 的硬指示极限；本文件不声称硬极限在物理上不可达。

#### P-依赖（**非**普适）的特征

| 特征 | P-依赖 | 物理解释 |
|---|---|---|
| 过渡宽 `w_{tr}` 的物理量纲 | model / domain 特定 | 声明阈值的 transition scale |
| `\psi` 的过渡曲线形态（sigmoid vs tanh vs polynomial）| 测量层选择 | 不同测量协议可能给不同 `\psi` 拟合 |
| 过渡区内的混合通道行为 | model / domain 特定 | 需由测量与 domain evidence 判定 |

#### T-CHANNEL-1 不证明的事项

1. **不**证明 `w_{tr}` 是 P-universal 的——`w_{tr}` 是赌注 / 主体类别 / 历史阶段相关的（P3）
2. **不**承诺 `\psi` 是 `C^\infty` 平滑——四条性质只要求 `C^0` 单调（硬指示也是有效成员，作为 `w_{tr} \to 0` 极限）
3. **不**覆盖随机 / 多值 `\psi`（非确定性通道指示暂留为 P3 候选）
4. ~~**不**证明集体版 T-CHANNEL-1^{coll}——`\mathbb{1}[d^{coll} \gtrless d_c^{coll}]` 在 `\mathcal{P}` 上的扩展耦合 H6 的 C5^{coll} `M(t)` 可测性闭包，是后续轮次任务~~ **已收口（H11，2026-04-26）**：`Core_Law/SRT_Collective_Selection.md §4.9.3 T-CHANNEL-1^{coll}` 给出集体版（C1^{coll}-C5^{coll} + C7^{M-stab} + Q-univ-5^{coll}），五个不变量保持，`\nu_{ext}\|M_{ext}\|` 与 `\psi^{coll}` 加性独立
5. **不**证明 universal health region、B phase、signal-to-structural conversion、burden conservation、anti-minimization theorem 或 irreversible single direction
6. **不**从 residual / channel projection 反向准入 suffering；Hardening Notes 的 operator claims 仍属 E3-B debt

#### T-CHANNEL-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| `\mathbb{1}[d \le d_c]` 是硬指示 | 模型形式（§4.3）| 有效族 `\psi` 的 `w_{tr} \to 0` 极限（§4.5）|
| 已声明双坐标 / transfer term 对 ψ-shape 的敏感性 | 隐含主张 | T-CHANNEL-1 给出族内形式比较，不建立上游语义 |
| 过渡区模型意义 | 缺失 | `w_{tr}>0` 提供可拟合的软切换候选 |

**当前地位**：T-CHANNEL-1 是声明 channel-function family 内的 P2 formal/model result。更强 domain standing 需要独立 suffering admission、阈值 / 测量协议、transfer / loss closure 与数据；集体版的既有形式扩展不改变这些边界。

---
---

## §5. 四变量耦合总方程

当各 component model 已独立准入、suffering registration 已建立，并且 `declared direction exists + T_dir admitted in model M` 时，可把 §2-§4 合成一个 P2 候选四变量耦合系统（P 固定；显式耦合项粗体）：

$$
\begin{aligned}
\frac{d\sigma}{dt} &= \frac{1}{T}\Big[(1-\sigma)(\alpha w\phi(\sigma) - \lambda_{trace}T\sigma) - \sigma(\beta i - \lambda_{ext}T(1-\sigma))\Big] \\[4pt]
\frac{dd_c}{dt} &= \gamma_\rho \rho_{local} + \boldsymbol{\gamma_\sigma \max(0,\,\sigma - \sigma_{sub})} - \gamma_\pi \pi - \gamma_I I_{window} \\[4pt]
\frac{dT_{dir}}{dt} &= -\kappa_{\mathrm{relax}}\bigl(T_{dir} - T_{dir}^{\mathrm{alg}}(\sigma, d, d_c)\bigr) - \boldsymbol{\kappa_{\mathrm{mask}}\,\Delta\Psi_f^{\mathrm{gap}}} - \boldsymbol{\kappa_S\, S_{str}} + \kappa_{\mathrm{sup}} s_{ext} \\[4pt]
\frac{dS_{sig}}{dt} &= \mu_\Delta \dot{\Delta}_{avail} - \boldsymbol{\mu_\pi \pi\, \mathbb{1}[d > d_c]} - \mu_{sup} s_{ext} \\[4pt]
\frac{dS_{str}}{dt} &= \boldsymbol{\nu_{block}\,\mathbb{1}[d \leq d_c]\,S_{sig}} + \boldsymbol{\nu_\sigma \max(0,\,\sigma - \sigma_{health})} - \nu_{trigger}D_{trigger} - \nu_\pi \pi\, I_{window}
\end{aligned}
$$

（严格计数为五个标量方程，因为声明的 S proxy 被分为 `S_{sig}` 与 `S_{str}` 两个模型坐标；“四变量”按宏观变量计为 σ / d_c / T_dir / S。该分解并非自然分类定理。）

无 direction 准入时，不得为了闭合而填入 `T_dir = 0`；应删去／边缘化 T_dir 方程及相关项，分析剩余已声明的 non-T_dir subsystem。

### §5.1 关键耦合路径

1. **σ → d_c coupling candidate**：声明模型把 self-reference coordinate 的高位部分写入 `d_c` 漂移；这不建立 occlusion 或 suffering
2. **d_c → channel weight**：模型 channel function 随 `d-d_c` 改变；B 标签只在 declared criterion 下使用
3. **optional S transfer path**：只有额外 transfer / loss closure 成立时，registered `S_{sig}` 才可影响 `S_{str}`；signal suppression 本身不推出该路径
4. **perturbation / window inputs**：`D_{trigger}`、`I_{window}` 与 `π` 的联合作用是待检验 model coupling
5. **conditional T_dir pathology candidate**：在 direction 与 criterion 已准入后，可比较 T_dir relaxation 与 gap term；它不验证 direction、health、value 或 legitimacy

former P1-T05 所提供的 `S_{str} → T_dir ↓ → r ↓ → S_{sig}` feedback path 已删除；本轮不以新的 downstream rate 替代它。

### §5.2 声明 pathology model 的吸引子候选

仅当 pathology / viability criterion、suffering proxy 与 direction 都已独立准入时，可研究下列联合稳态候选：

$$
\mathcal{A}_{path} \;:\; \sigma \to 1,\; d_c \to d_{max},\; T_{dir} \to T_{dir}^{\mathrm{alg}} \text{ 但 } \Delta\Psi_f^{\mathrm{gap}} > 0 \text{ 累积}, \; S_{str} > 0 \text{ 定常}, \; S_{sig} \to 0
$$

在该声明 pathology model 中，以上只是 B-regime、high-σ coordinate、低 observed signal coordinate 与 apparent readability 的联合候选。是否存在该吸引子须由参数、稳定性与时域分析证明；是否应称为 pathology / “lethal `L_2`”由独立 criterion 决定。稳态不自动等同于 health，但该提醒也不能从方程反向定义 health、suffering 或 moral debt。

### §5.3 criterion-relative candidate work region

在 direction、suffering proxy 与 viability criterion 都已准入的声明模型中，可定义 criterion-relative candidate work region `\mathcal{H}`：

$$
\mathcal{H} \;:\; \sigma \in (\sigma_{sub}^\dagger \pm \delta),\; d > d_{narrow},\; T_{dir} \approx T_{dir}^{\mathrm{alg}} \text{ 且 } \Delta\Psi_f^{\mathrm{gap}} \to 0,\; S_{sig} \in [S_{min}, S_{max}],\; S_{str} \to 0
$$

`\mathcal{H}` 只是由外部接入 `i(t)`、可支付性 `\pi(t)`、声明 gap 与 perturbation inputs 参数化的模型区域；它是否可达、稳定或有利仍须另证。“健康”只相对于已声明 criterion，T_dir 不验证它；无 direction 准入时省略含 T_dir 的分支。

按 ST-A，该工作区至多是 generative reselectability 的实现候选，不是 P1 反闭合必要性的方程证明；更强的 consequence-sensitive rule revisability 仍需由 21C B13 独立审计，不能从 `\mathcal{H}` 或 Selection occurrence 直接推出。

---

## §6. 与已有主方程的关系：T-PROJ-1 投影定理

> **Status (2026-04-25 H5; RC-A source correction 2026-08-18; Wave E3-A truth-up 2026-09-16)**：本节把“已准入 component models 可由一个选择的主方程投影重现”写成**条件性 P2 模型结果**。它不从 Core22 反向准入任何 component；含 `T_dir` 的版本另要求 direction admission，含 `S` 的版本另要求 suffering registration 与 suffering proxy admission。无 direction 时只保留已定义的投影子集。former P1-T05 的 `r(t)` 投影项已因上游撤销而删除。

### §6.1 主方程与 L1 四变量的对接

`Core/SRT_Core_22_Equations.md` Eq-Evo-01 / Eq-Evo-03 主动力学（单 ISP，固定 P）：

$$
\frac{d\sigma_M}{dt} \;=\; \hat{G}_\theta[\sigma_M] \;-\; \nabla F[\sigma_M] \;-\; \lambda\cdot\nabla C_{L_2}[\sigma_M]
\qquad
\frac{d\theta}{dt} \;=\; \gamma\cdot A[\sigma_M, \mathrm{Target}] - \delta\cdot\partial_\theta\Phi(\theta) - k(\mathrm{Input}_{L_1} - \mathrm{Baseline})
$$

（本节为消除符号冲突把主方程态场写作 `\sigma_M`；本文件其它处的 σ 仍指自指率 `σ_{sr}`，按 `_SRT_SYMBOL_TABLE.md` Usage Rule 12 转读。）

**问题陈述**：在各 component model 已独立准入后，能否选择投影与 closure assumptions，使本文件 §2-§5 的声明子系统由主方程 `(\sigma_M, \theta)` 重现？若无 direction 准入，省略 `T_{dir}`；若 suffering 未独立准入，省略 `S`。不得用零填充代替缺失对象。

### §6.2 投影算子的形式定义

设 P 已由上游独立建立为 stable ISP，并且相应 component models 已准入。可选择四个标量泛函（投影算子）`\mathcal{F}_X : (\sigma_M, \theta) \mapsto \mathbb{R}` 如下；这些选择不是由 P1-T06 自动给出：

**`σ_{sr}` 投影**

$$
\mathcal{F}_\sigma(\sigma_M, \theta) \;:=\; \frac{\|\theta^{\mathrm{trace}}\|}{\|\theta^{\mathrm{trace}}\| + \|\theta^{\mathrm{ext}}\|}
\qquad\text{其中}\quad
\theta^{\mathrm{trace}} \;:=\; \mathcal{P}_{L_2\to\theta}\bigl[L_2(t)\bigr],\;\;
\theta^{\mathrm{ext}} \;:=\; \theta - \theta^{\mathrm{trace}}
$$

在独立 trace/ext attribution rule、retention definition、writeback efficacy、参数化与 metric 已声明时，`\theta^{\mathrm{trace}}` 可表示模型归于 retained writeback 的部分，`\theta^{\mathrm{ext}}` 表示其余声明分量；Core22 不保证该分解唯一或自然。

**`d_c` 投影**

$$
\mathcal{F}_d(\sigma_M, \theta) \;:=\; d_{\max} - \alpha_d \cdot \mathrm{tr}\bigl[\nabla^2 C_{L_2}[\sigma_M]\bigr]_{loc}^{-1}
$$

这是 `d_c` 的一个声明投影候选：只有在局部曲率、可逆性与尺度关系另行成立时，scaffold 刚度才可映射到该模型坐标。它不建立 natural threshold。

**`T_{dir}` 投影**

$$
\mathcal{F}_T(\sigma_M, \theta) \;:=\; \mathrm{Dir}(\Delta\hat{G}_\theta,t) \cdot R_{self}(P,t) \cdot A_{reorient}(P,t)
$$

这里的 `\mathrm{Dir}(\Delta\hat{G}_\theta,t)` 必须先由模型相对于已声明 direction 给出；`R_{self}` 与 `A_{reorient}` 只限制该方向的自我相关可读性与重定向接入。若没有已声明 direction，`\mathcal{F}_T` 未定义并从投影族中省略，而不是取零。`d`、`d_c`、`σ_{sr}` 与 `L_0` 标签均不生成、排序或正当化该方向；`\Delta\Psi_f^{\mathrm{gap}}` 只在同一已声明方向下表示实—感接入误差。

**`S` 投影**

$$
\mathcal{F}_S(\sigma_M, \theta) \;:=\; \|\hat{R}(\sigma_M, \theta)\|_{H_P}
\qquad\text{其中}\quad
\hat{R} \;:=\; \frac{d\sigma_M}{dt} - \bigl[\hat{G}_\theta - \nabla F - \lambda\nabla C_{L_2}\bigr]
$$

`\hat{R}` 是主方程在 P 处的**模型剩余项**。只有第一人称 suffering 已独立准入，且 residual-to-suffering map、`H_P` metric 与测量解释均另行声明时，才可把 `\|\hat{R}\|` 作为 `S` proxy；P1-T06 不提供这一步。`S_{sig}` / `S_{str}` 也只是额外声明的 weighted decomposition，不由 residual norm 自动产生。

### §6.3 投影下的链式法则

对任意 P 上的足够光滑泛函 `\mathcal{F}_X(\sigma_M, \theta)`：

$$
\frac{d\mathcal{F}_X}{dt} \;=\; \langle\,\partial_{\sigma_M}\mathcal{F}_X,\; \dot\sigma_M\,\rangle + \langle\,\partial_\theta\mathcal{F}_X,\; \dot\theta\,\rangle
$$

把 Eq-Evo-01 与 Eq-Evo-02 代入，逐项展开 `\hat{G}_\theta - \nabla F - \lambda\nabla C_{L_2}` 与 `\gamma A - \delta\partial_\theta\Phi - k(\mathrm{Input}_{L_1}-\mathrm{Baseline})`。direction 已准入时，对每个 `X \in \{σ_{sr}, d_c, T_{dir}, S\}` 给出 ODE 形式；否则只对已定义的 non-`T_{dir}` 投影分量应用链式法则。

### §6.4 闭包假设（Closure Assumptions）

四变量系统在投影下闭合需要四条结构性假设：

| 编号 | 假设 | 主方程层根据 |
|---|---|---|
| **C1** | **慢-快分离**：`θ` 与 `\sigma_M` 在不同时间尺度演化（`\dot\theta` 在 `\sigma_M` 收敛时间尺度上近似常数） | 额外 model assumption；Core22 形式提供候选分解但不保证尺度分离 |
| **C2** | **`L_2` 写回的 Markov 闭包**：`\dot{\theta}^{\mathrm{trace}}` 仅依赖当前 `(σ_{sr}, ρ_{local})`，不显式依赖更高阶 `L_2` 历史 | 额外 retained-efficacy / writeback assumption；不由 P1-T02 或 Core22 自动提供 |
| **C3** | **局部正则性假设**：已准入的泛函 `\mathcal{F}_X` 在声明邻域内有界且 Lipschitz | 额外 model assumption；P1-T06 不保证 compactness、metric 或 Lipschitz 性 |
| **C4** | **条件性方向投影的可分性**：在 direction 已独立声明并准入后，`\mathrm{Dir}(\Delta\hat{G}_\theta,t)` 与 `\sigma_M` 的纵向幅度近似可分，使 `\dot{T}_{dir}` 不显式依赖 `\|\sigma_M\|` 高阶项 | 声明模型中的局部几何假设；Eq-Bridge-IG-01 可提供一种 realization，但不生成方向 |

**关键**：C1-C4 是有代价的 P2/P3 model assumptions，对应 §7 的 χ-family stability、`\Delta\Psi_f^{\mathrm{gap}}` 表示、阈值与测量窗口等开放项。当某条假设失效时，对应 ODE 只保留现象学代理地位。

### §6.5 T-PROJ-1：四变量系统的投影定理

**陈述（条件性形式 / 模型结果，默认按 P2 读）**：在 stable ISP P、各 component model 与相应投影都已独立准入后，若 direction / suffering 等分支各自满足 admission，且闭包假设 C1-C4 成立，则所选投影可在误差项内重现声明 subsystem：

$$
\boxed{\;\frac{d\mathcal{F}_X}{dt}\bigg|_{\text{Eq-Evo-01,02}} \;\overset{C1\text{-}C4}{=}\; \mathrm{RHS}_X^{\text{§2-§5}} \;+\; O(\eta)\;}
\qquad X \in \{σ_{sr}, d_c, T_{dir}, S\}
$$

其中 `\mathrm{RHS}_X^{\text{§2-§5}}` 是本文件 §2.2 / §3.2 / §3.5 / §4.2-§4.3 的 ODE 右端，`O(\eta)` 是闭包高阶残差（C1-C4 失效时的修正项；当 C1-C4 严格成立时 `\eta = 0`）。

若无 direction 准入，从 `X` 与 `\mathrm{RHS}_X` 中省略 `T_{dir}`；若无 suffering admission，同样省略 `S`。这些情形不是把缺失对象或投影设为零。

**逐项对应**：

| L1 ODE 源项 | 主方程来源 | 闭包条件 |
|---|---|---|
| `\sigma_{sr}` 写回项 `\alpha w \phi(σ_{sr})` | Eq-Evo-02 学习项 `\gamma A[\sigma_M, \mathrm{Target}]` 中 `\mathrm{Target} = σ_M` 自身分量 | C2 |
| `\sigma_{sr}` 衰减项 `\lambda_{trace}T σ_{sr}` | Eq-Evo-02 摩擦下降项 `\delta\partial_\theta\Phi(\theta)` 在 `θ^{trace}` 投影 | C2 |
| `\sigma_{sr}` 外部驱动项 `\beta i` | Eq-Evo-02 稳态反冲项 `k(\mathrm{Input}_{L_1} - \mathrm{Baseline})` | C1 |
| `d_c` 漂移项 `\gamma_\rho \rho_{local}` | `\nabla^2 C_{L_2}` 沿 `ρ_{local}` 方向的累积 | C3 |
| `d_c` 漂移项 `\gamma_\sigma \max(0, σ_{sr}-σ_{sr}^{sub})` | `\nabla^2 C_{L_2}` 在 `\theta^{trace}` 占优区的局部刚化 | C2 + C3 |
| `T_{dir}` 弛豫项 `-\kappa_{\mathrm{relax}}(T_{dir} - T_{dir}^{\mathrm{alg}})` | 相对于已声明 direction 的 `\mathrm{Dir}(\Delta\hat{G}_\theta,t) R_{self} A_{reorient}` 的条件性接入动力学；`(d,d_c,σ_{sr})` 只调制接入 | C4 + direction admission |
| `T_{dir}` 扣除项 `-\kappa_{\mathrm{mask}}\Delta\Psi_f^{\mathrm{gap}}` | `\nabla F[\sigma_M]` 中实-感分裂部分（不可读分量） | C4 |
| `S_{sig}` mismatch input `\mu_\Delta \dot{\Delta}_{avail}` | suffering 与 residual map 均已准入后的候选 weighted projection | C3 + suffering/proxy admission；T-DELTA-1 为 E3-B debt |
| `S_{str}` optional transfer term `\nu_{block}\mathbb{1}[d\le d_c]S_{sig}` | 声明 suffering model 中的候选 weighted projection | C3 + independently admitted P3 T-IRR-3.5 model |

former P1-T05 的 `+\kappa_r r(t)` / `-\mu_r r(t)` 不再属于 `RHS_X`，也不再声称存在主方程投影来源。

**证明骨架**：

1. **σ_{sr} 项**：在 trace/ext attribution、metric、retention 与 writeback assumptions 已独立准入后，`\dot{\mathcal{F}}_\sigma = (1 - σ_{sr})\dot{\|\theta^{\mathrm{trace}}\|}/\|\theta\| - σ_{sr}\dot{\|\theta^{\mathrm{ext}}\|}/\|\theta\|`。再施加 C1-C2，才可化为 §2.2 的选定形式；这不证明 σ 的自然性。

2. **d_c 项**：`\dot{\mathcal{F}}_d = \alpha_d \cdot \dot{\mathrm{tr}\,(\nabla^2 C_{L_2})^{-1}}`。只有另行准入 local curvature-to-capacity map、retained efficacy 与 §3.2 的 source decomposition 后，才可把其漂移写成 `ρ_{local}`、`(σ_{sr}-σ_{sr}^{sub})` 与 window terms；C3 本身不提供这些对应。

3. **T_{dir} 项**：仅在 direction admission 成立时，`\dot{\mathcal{F}}_T` 来自已声明方向下的 readability / reorientation-access 泛函；C4 保证局部可分，使该导数分解为弛豫项（向条件性代数目标 `T_{dir}^{\mathrm{alg}}`）+ 实—感接入扣除项 + 结构型苦难调制项 + 声明模型中的 `L_2` 支架项，即 RC-A subtractive sync 后的 §3.5 四项 ODE。该推导不生成、排序或验证方向；无 direction 时本项省略。

4. **S 项**：只有 suffering registration、residual-to-suffering proxy、metric 与双坐标分解均已独立准入后，才可对 `\dot{\mathcal{F}}_S` 使用链式法则并以 channel functions 加权。T-IRR-3.5 只提供三个 factors 已准入时的 P3 coefficient candidate；它不证明 conversion、single direction 或 suffering。

### §6.6 T-PROJ-1 不证明的事项

为避免过度主张，T-PROJ-1 **不承诺**以下内容：

1. **不**证明 L1 系数（`α, β, λ_{trace}, γ_ρ, κ_{relax}, μ_Δ, ν_{block}` 等）的具体数值——这些仍为 P3 实证问题
2. **不**证明 χ(σ_{sr}; σ_{sr}^{self}) 跳跃函数族的普适性（C2 闭包之外）
3. **不**证明 `\Delta\Psi_f^{\mathrm{gap}}` 的算子层定义（`_SRT_T_DIR_CANONICAL.md §5-§6` 现象学分裂仍为依赖）
4. ~~**不**证明集体版主方程（Eq-Multi-01 / 02 / 03）→ `Collective_Selection §4.4-§4.6` 的对应投影；集体版 T-PROJ-1^{coll} 是后续轮次的扩展任务~~ **已在 H6（2026-04-25）落地**：`Core_Law/SRT_Collective_Selection.md §4.7 T-PROJ-1^{coll}` 给出集体投影定理（C1^{coll}-C5^{coll} 五条闭包，含新增 `M(t)` 可测性 MOC 闭包 C5^{coll}）；T-PROJ-1^{coll} 在 `\mathcal{P} = \{P\}` 极限下退化为本节 §6 T-PROJ-1
5. **不**证明 `\mathcal F_\sigma` 的 trace/ext 分解唯一、bare norm 跨等价参数化不变、或其数值等于因果控制份额；这些是所选 σ 表示本身的额外负担，不由 C1-C4 提供。
6. **不**证明 `σ_{sr}^{sub/self}` 是 subjecthood / consciousness gates，`σ_{health}` 是 natural health point，或 `σ_{sr}\to1` 是 universal pathology
7. **不**证明 `d_c/d_{narrow}` 是 natural thresholds，也不由 A/B regime 建立 suffering、agency、responsibility 或 Selection occurrence
8. **不**准入 suffering，不把 residual norm、channel weights 或 `\dot{\Delta}_{avail}` 变成 first-person registration 的证明
9. **不**生成 primitive direction，也不从高 `T_dir` / `T_dir^{alg}` 推出 health、goodness、value 或 legitimacy

### §6.7 T-PROJ-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| 条件性四变量系统不承担本体准入 | 陈述（§6 paragraph） | 只有 component 先独立 admission，投影才可作模型重现 |
| 四变量系统与主方程的关系 | “条件性导出”陈述 | 选定 projection + closure assumptions 下的模型重现（modulo `O(\eta)`）|
| 主方程层 → 四变量层需要哪些额外条件 | 隐含 | `\mathcal{F}_X` 投影算子 + direction admission + C1-C4 + Eq-Evo-01/02 的链式法则 |
| 四变量 ODE 系数与主方程参数的关系 | 未给 | §6.5 表格给出 source-by-source 对应（系数本身仍为 P3）|

**当前地位**：T-PROJ-1 是 component-first admission、选定 projection 与 C1-C4 下的 P2 conditional model result。它不能把表示、主体位、意识、苦难、自然阈值、primitive direction 或闭包条件反向升级为 P1。更强 domain standing 需要分别固定投影几何、admission、criterion、measurement 与误差界；Hardening Notes 的 operator-level claims 仍属 E3-B review debt。

---

## §7. Open Pressures

> **Hardening status (Wave E3-A truth-up 2026-09-16)**: σ namespace separation remains. Hardening Notes 中的 T-DELTA-1、operator-level residual decomposition 与 FEP hardening 只作为既有 P2 candidates / E3-B review debt，不为本文件提供 suffering、hidden-burden、subjecthood 或 direction 的证明。T-CHI-1 与 T-CHANNEL-1 现为声明模型族内的 P2 formal results；`\nu_{block}` 现为独立前件下的 P3 pathology-model candidate。T_dir ODE 与含它的 T-PROJ-1 均要求 direction admission。Former P1-T05 派生的全局 `r(t)` 及两项保持删除。

当前 draft 状态下尚未封口：

1. **σ 符号冲突**：本文件 σ（自指率，`[0,1]` 标量）与 `Core/SRT_Core_22_Equations.md` σ（主方程状态场）共用符号；需引入新记号（候选：`σ_{self}` 改为 `κ_{self}` 或 `\bar{\sigma}`）避免歧义
2. **`\dot{\Delta}_{avail}` 与 residual mapping**：Hardening Notes §2 T-DELTA-1 是既有 P2 candidate / E3-B review debt。projection set、open-state representation、geometry、operator closure 与 residual-to-suffering map 都未由 E3-A 封口；A1-A3、domain window 与 source-by-source 对位仍待审。
3. **χ-family 的稳定性与解释**：T-CHI-1 只在所选 `σ_{sr}` 坐标、零点 / 稳定性附加条件与声明参数族内成立。更广 χ 空间、domain shape、trace attribution，以及 subjecthood / consciousness / pathology interpretation 均保持开放。
4. **多主体扩展**（2026-04-25 H3 状态）：本文件保持单 P 形式；集体层四变量耦合动力学已在 `Core_Law/SRT_Collective_Selection.md §4.4-§4.6` 给出第一遍；former-P1-T05 的平行 `r^{coll}` 通道已于 RC-A sync 删除。未封口部分仍在 `SRT_Collective_Selection.md §9`
5. **阈值 / criterion / 测量的实证固定**：`σ_{sub}, σ_{self}, σ_{health}, d_c, d_{narrow}, r_{min}, S_{min}, S_{max}` 以及 `\kappa_*` 全部只是 model/domain coordinates；尚须明确 criterion、尺度、时域、测量映射与 evidence。它们不是 subject、consciousness、health、pathology、suffering 或 Selection gates。
6. **与 FEP / predictive processing 的桥接**：`S_{sig}` 与 prediction error 的结构对应是高优先级；`Neuroscience/SRT_Clin_02_FEP.md` 已经是 bridge 层，下一步需要在方程层写出条件翻译
7. **transfer / reversibility model**：`ν_{block}=η·\varepsilon_{pg}·\kappa_{\Psi_f}` 只是在 factors 独立准入后的 P3 candidate。transfer existence、反向项、loss channels、B-regime 吸收性与 suffering interpretation 均待具体模型证明。
8. **T_dir 独立 ODE 的模型闭包**：仍待——(a) `T_{dir}^{\mathrm{alg}}` 的 Θ-family；(b) gap 的表示与测量；(c) `[0,1]` 投影；(d) criterion-relative coefficient window。任何结果都不能生成 direction 或 health/value standing。

---

## §8. Cross-References

- 个体化 / σ 定义 / 三相结构 → `Core_Law/SRT_Individuation.md`
- 遮蔽动力学 / A/B 分期 / 四类干预窗口 / 四类解耦触发 → `Core_Law/SRT_Occlusion_Dynamics.md`
- 苦难 / 两型 / 四类分型 / 反最小化 → `Core_Law/SRT_Suffering.md`
- 主动力学 / `\hat{G}_\theta[\sigma] - \nabla F - \lambda\nabla C_{L_2}` → `Core/SRT_Core_22_Equations.md`
- 路径层 `ρ` / 写回 / scaffold sedimentation → `Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold`
- P1-T06 stable ISP（仅提供上游 standing；不自动给出本文件的 metric、writeback、projection、suffering 或 closure）→ `Core/SRT_Core_21b_Constitutive_Theorems.md`
- former P1-T07 demotion / absorption remainder → 同上
- ST-A generative reselectability / conditional anti-closure candidate（§5.3 工作区的解释层）→ `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`
- P1-T02 occurrence non-equivalence（不提供 `w(t)`、retained history 或 durable writeback）→ 同上
- d-value / T_dir / Ψ_f 的 canonical → 对应 `_SRT_*_CANONICAL.md`

---

## §9. 定位与使用规则

- **本文件做**：在 component-first admission 后，提供 σ / d_c / suffering proxy 与准入后 T_dir 的 P2 conditional coupling candidates、model-family analysis 与 projection/testability programme
- **本文件不做**：固定 domain 参数、临床量表、实验设计或 AI 实现；不定义 ontology、subjecthood、phenomenality、consciousness、suffering admission、Selection occurrence、agency、health、value 或 legitimacy
- **引用规则**：涉及声明模型的四变量方程、criterion-relative attractor/work-region candidate 或 channel-family 数学时可回链本文件；涉及变量定义、admission 或上游 standing 时必须回链各 owner（T_dir → `_SRT_T_DIR_CANONICAL.md`）
- **不得**把本文件的方程读成实证定量定律、自然阈值或 P1 theorem，也不得以代数闭合反向升级任何模型前件；它们用于联合批评、拟合与修正
