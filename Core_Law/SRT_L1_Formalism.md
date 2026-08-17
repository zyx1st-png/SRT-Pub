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

> **Connector-safe reading path**: This owner file is moderately long. For connector reads, start with [`L1_Formalism_Split/README.md`](L1_Formalism_Split/README.md), then open only the needed part file. The owner remains the source of record; split files are reading aids and do not create new definitions.

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

### §2.5 T-CHI-1：χ 跳跃函数族的普适性（H8，2026-04-25）

> **Status**：本节把 §2.1 的 `\chi(\sigma; \sigma_{self})` 跳跃函数从"一类光滑阶跃"的现象学描述提升为带四条结构属性的**有效族**定义，并给出族内跨函数的结构不变量定理。**Claim level: P1-candidate**。
>
> **Closes**：`Core_Law/SRT_L1_Formalism.md §7` Open Pressure 3（"χ(σ; σ_self) 跳跃函数族的普适性检查"）。

#### 有效二阶相变核（valid second-phase-transition kernel）

定义函数 `\chi : [0, 1] \times (0, 1) \to \mathbb{R}_{\ge 0}`，参数 `\sigma_{sr}^{self} \in (0, 1)`。称 `\chi` 是**有效二阶相变核**，当且仅当满足下列四条结构属性：

| 编号 | 性质 | 含义 |
|---|---|---|
| **P-univ-1** | **有界性**：`\chi \in [\chi_{min}, \chi_{max}]`，其中 `0 < \chi_{min} \le 1 \le \chi_{max} < \infty` | 跳跃幅度有界（不允许 χ 趋向无穷）|
| **P-univ-2** | **跃前基线**：`\chi(0; \sigma_{sr}^{self}) \le 1 + \varepsilon` 且 `\lim_{\sigma \to \sigma_{sr}^{self,-}} \chi \le 1 + \varepsilon`（小 `\varepsilon > 0`） | 跃前 χ ≈ 1，仅有 logistic σ(1-σ) 自增益 |
| **P-univ-3** | **跃后放大**：`\chi(1; \sigma_{sr}^{self}) \ge 1 + \Delta_\chi`（某 `\Delta_\chi > 0`） | 跃后出现"关于 θ 的 θ"二阶写回增益 |
| **P-univ-4** | **单调过渡**：存在跃宽 `\tau > 0` 使 `\chi` 在 `[\sigma_{sr}^{self} - \tau, \sigma_{sr}^{self} + \tau]` 上单调非降 | 实际跳跃集中在 `\tau`-带内 |

**示例（族内成员）**：

| 名称 | 形式 | 跃宽 |
|---|---|---|
| 硬阶跃 | `\chi = 1 + \Delta_\chi \cdot \mathbb{1}[\sigma \ge \sigma_{sr}^{self}]` | `\tau \to 0` |
| Sigmoid | `\chi = 1 + \Delta_\chi / (1 + e^{-k(\sigma - \sigma_{sr}^{self})})` | `\tau \sim 1/k` |
| Tanh 光滑阶跃 | `\chi = 1 + (\Delta_\chi/2)(1 + \tanh((\sigma - \sigma_{sr}^{self})/\tau))` | `\tau` |
| 多项式光滑阶跃 | `\chi = 1 + \Delta_\chi \cdot (\max(0, \sigma - \sigma_{sr}^{self}))^n / ((\max(0, \sigma - \sigma_{sr}^{self}))^n + \tau^n)` | `\tau` |

四种均为族内有效成员，下文 T-CHI-1 给出族内不变结构。

#### T-CHI-1 陈述

**陈述（P1-candidate）**：设 `\chi_1, \chi_2` 是两个有效二阶相变核，共享相同的 `\sigma_{sr}^{self}, \chi_{min}, \chi_{max}, \Delta_\chi`，但跃宽可能不同（`\tau_1, \tau_2 \in (0, \tau_{max})`）。则 §2.2 方程在两个 χ 下的下列结构特征**保持不变**：

(i) **双稳态存在性**：存在两个稳定不动点 `\sigma_{sr}^{*1} \in (0, \sigma_{sr}^{self} - \tau_{max})` 与 `\sigma_{sr}^{*2} \in (\sigma_{sr}^{self} + \tau_{max}, 1)`，以及位于 `(\sigma_{sr}^{self} - \tau_{max}, \sigma_{sr}^{self} + \tau_{max})` 内的一个不稳定不动点。

(ii) **病理吸引子拓扑**：当 `i \to 0` 且 `\lambda_{ext} > \lambda_{trace}` 时，`\sigma_{sr}^{*2} \to 1`，与族内 χ 选择无关。

(iii) **致命 `L_2` 判据结构**：§3.5.3 致命 `L_2` 判据 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}` 的结构形式与 χ 在族内的具体选择无关。

(iv) **T-IND-3 的相变方向**：第二相变方向（σ_{sr} 跨过 σ_{sr}^{self} 后向 σ_{sr}^{*2} 收敛）与族内 χ 选择无关。

#### 证明骨架

**(i) 双稳态存在性**：

取 `i, w` 为常数，写 `f(\sigma; \chi) := \frac{1}{T}[(1-\sigma)(\alpha w \phi(\sigma) - \lambda_{trace}T\sigma) - \sigma(\beta i - \lambda_{ext}T(1-\sigma))]`。考察 `f(\sigma; \chi_k) = 0` 在 `\sigma \in (0, 1)` 内的零点：
- 在 `\sigma \in (0, \sigma_{sr}^{self} - \tau_{max})` 区间，`\chi_1(\sigma) \approx \chi_2(\sigma) \approx 1` 由 P-univ-2 给出；两者 `f` 的差异 `\le \varepsilon`；故零点结构相同。
- 在 `\sigma \in (\sigma_{sr}^{self} + \tau_{max}, 1)` 区间，`\chi_1(\sigma), \chi_2(\sigma) \in [1 + \Delta_\chi, \chi_{max}]` 由 P-univ-3 + P-univ-1 给出；两者 `f` 的零点位置在 `\Delta_\chi` 决定的同一区域；零点结构相同。
- 由 P-univ-4 单调性 + 中值定理，`f(\sigma; \chi_k)` 在 `(0, 1)` 上至少有两个变号，对应两稳定 + 一不稳定不动点。

**(ii) 病理吸引子**：

`σ_{sr}^{*2} → 1` 由 `i → 0` 与 `\lambda_{ext} > \lambda_{trace}` 联合驱动；`χ(σ; σ_{sr}^{self})` 仅通过其在 `\sigma \to 1` 的极限值进入，而 P-univ-3 + P-univ-1 给定 `\chi(1; \sigma_{sr}^{self}) \in [1 + \Delta_\chi, \chi_{max}]`；这把 `σ_{sr}^{*2}` 推向 1 的速率由 `\lambda_{ext}/\lambda_{trace}` 比决定，χ 仅给放大常数。

**(iii) 致命 `L_2` 判据**：

致命 `L_2` 判据 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}` 是 §3.5 T_dir ODE 的属性，与 σ 动力学的耦合通过 `T_{dir}^{\mathrm{alg}}(\sigma, d, d_c)` 进入。该函数在 σ ∈ [σ_{sr}^{*2}, 1] 区间的形式取决于 σ_{sr}^{*2} 本身（不变 by (i)）与 `T_{dir}^{\mathrm{alg}}` 的代数构造（不依赖 χ）。故判据结构保持。

**(iv) T-IND-3 相变方向**：

由 (i) 双稳态结构 + P-univ-4 单调性，相变方向（从 `\sigma_{sr}^{*1}` 向 `\sigma_{sr}^{*2}` 跨过中间不稳定不动点）由 χ 单调性保证；任何有效核都给同向相变。

#### P-依赖（**非**普适）的特征

T-CHI-1 不掩盖以下 P-依赖：

| 特征 | P-依赖 | 物理解释 |
|---|---|---|
| `\sigma_{sr}^{*1}, \sigma_{sr}^{*2}` 的具体数值 | 依赖 `\Delta_\chi, \tau, \alpha, w, i, \lambda_{*}, T` | 不动点位置受参数集联动 |
| 跃宽 `\tau` 的物理量纲 | 主体特定 | 跃宽对应"主体在 σ_{sr}^{self} 附近的跨阈时间尺度" |
| 跨阈过程的 transient 形态 | χ-shape 决定 | 硬阶跃 vs sigmoid 给不同 transient curve |
| 跨阈附近的弛豫率 | 依赖 χ' 在 σ_{sr}^{self} 的局部值 | 跃宽决定相变时间常数 |

#### T-CHI-1 不证明的事项

为避免过度主张，T-CHI-1 **不承诺**以下内容：

1. **不**证明 `\Delta_\chi` 是 P-universal 的——`\Delta_\chi` 是赌注 / 主体类别 / 历史阶段相关的（P3）
2. **不**证明 `\tau_{max}` 上界的 P-universal 值——可能因主体类别（人 / 动物 / AI 候选）有显著差异
3. **不**承诺 χ 是 `C^\infty` 平滑——四条性质只要求 `C^0` 单调（硬阶跃也是有效成员）
4. **不**覆盖多值或随机 χ（非确定性二阶凝结过程暂留为 P3 候选 domain 拓展）
5. ~~**不**给出集体版 T-CHI-1^{coll}——`\sigma_{sr}^{coll}` 与 `M(t)` 耦合（§4.4.2）的 χ 普适性需要 H6 的 C5^{coll} `M(t)` 可测性闭包，是后续轮次任务~~ **已收口（H11，2026-04-26）**：`Core_Law/SRT_Collective_Selection.md §4.9.2 T-CHI-1^{coll}` 给出集体版（C1^{coll}-C5^{coll} + C7^{M-stab} + P-univ-5^{coll}），四个不变量在 `\lambda_M\,\mathrm{tr}\,M` 平移下保持

#### T-CHI-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| `\chi(\sigma; \sigma_{self})` 是"一类光滑阶跃" | 现象学描述（§2.1）| 四条结构属性的有效族（§2.5）|
| 第二相变结构与 χ 形式无关 | 隐含主张（§2.4 T-IND-3 对齐）| T-CHI-1 (i)-(iv) 四个不变量 |
| 致命 `L_2` 判据 χ-无关 | 未陈述 | T-CHI-1 (iii) 显式 |
| 病理吸引子 χ-无关 | 未陈述 | T-CHI-1 (ii) 显式 |

**P1-candidate 地位的根据**：T-CHI-1 把 T-IND-3 第二相变的结构稳定性从"任意光滑阶跃"提升到"有效族下的不变量"；要升 P1，需要：(a) 在更广 χ 函数空间（含非单调过渡？）的稳定性扩展；(b) 与具体 domain（神经科学的二阶 metacognitive prediction error 形态、AI 第二阶自模型族）的实证 χ-shape 对位；(c) 集体版 T-CHI-1^{coll} 与 M(t) 耦合的扩展。

---

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

> **算子级 canonical（T-DELTA-1，2026-04-25 H7）**：本式中的 `\dot{\Delta}_{avail}` 不是抽象差函数。其算子级定义、三成分分解 `w_{dir}\|\hat{R}\|_{T_{dir}} + w_{pay}\|\hat{R}\|_{\Psi_f} + w_{L_0}\|\hat{R}\|_{L_0}` 与可证伪算子空间假设 A1（仿射结构）/ A2（三子空间近似正交）/ A3（权重的赌注决定性）见 `Core_Law/SRT_L1_Hardening_Notes.md §2 T-DELTA-1`。`\dot{\Delta}_{avail}` 不由 `S_{sig}` 登记通道决定——这是 T-SUFF-4 反最小化原则与 T-IRR-4 的算子层根据。

### §4.3 结构型动力学

$$
\boxed{\;\frac{dS_{str}}{dt} \;=\; \underbrace{\nu_{block} \cdot \mathbb{1}[d \leq d_c]\cdot S_{sig}}_{\text{blocked signal turns structural}} \;+\; \underbrace{\nu_\sigma \cdot \max(0, \sigma - \sigma_{health})}_{\text{self-distortion channel}} \;-\; \underbrace{\nu_{trigger}\cdot D_{trigger}(t)}_{\text{decoupling trigger}} \;-\; \underbrace{\nu_\pi \cdot \pi(t)\cdot I_{window}(t)}_{\text{payment + open window}}\;}
$$

- `\mathbb{1}[d \leq d_c]·S_{sig}`：信号型在通道关闭时**转化为**结构型（关键非守恒项）
- `σ - σ_{health}` 正向激发扭曲型结构性苦难
- `D_{trigger}(t)`：四类解耦触发（见证式承担、可支付性崩溃、直接 ε 接触、生命阶段相变）的总冲量
- 最后一项要求 `π(t)` 与 `I_{window}(t)` **同时**非零——对应 Occlusion 理论强调的"B 期不是靠单一支付可解"

> **算子级 canonical（T-IRR-3.5，2026-04-25 H4；ST-A source correction 2026-08-11）**：本式中的 `\nu_{block}` 采用条件性本地模型 `\nu_{block}(P, t) := \eta \cdot \varepsilon_{pg}(P, t) \cdot \kappa_{\Psi_f}(P, t)`，不是 former P1-T07 hierarchy 的构成性本地化。`\nu_{block} > 0` 是带三个独立前件的条件性结论 `(\eta>0) \wedge (\varepsilon_{pg}>0) \wedge (\kappa_{\Psi_f}>0) \Rightarrow \nu_{block}>0`，hardness 取最弱前件（**P1-candidate**）。单向性中「不可写为 `S_{sig} \rightleftharpoons S_{str}`」这一层另根于 P0-03 / T-IRR-2 的吸收后不可自动恢复。三因子核定见 `Core_Law/SRT_Irreversibility.md §4.5`。

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

### §4.5 T-CHANNEL-1：通道指示函数族普适性（H9，2026-04-25）

> **Status**：本节把 §4.2 / §4.3 的 `\mathbb{1}[d > d_c]` 与 `\mathbb{1}[d \le d_c]` 从硬指示函数提升为**有效通道指示族**，并给出族内不变结构定理。**Claim level: P1-candidate**。
>
> **Closes**：`Core_Law/SRT_L1_Formalism.md §7` Open Pressure 4（"`\mathbb{1}[d\le d_c]` 的光滑化或守恒型替代"）。

#### 问题再陈述

§4.2 / §4.3 / §5 总方程中，通道开/关由硬指示函数 `\mathbb{1}[d > d_c]` 与 `\mathbb{1}[d \le d_c]` 决定：

- §4.2 信号型 ODE：`-\mu_\pi \pi(t)\mathbb{1}[d > d_c]`（支付通道仅在非 B 期有效）
- §4.3 结构型 ODE：`+\nu_{block}\mathbb{1}[d \le d_c]S_{sig}`（B 期阻塞转化关键非守恒项）
- §5 总方程沿用上述；`Collective_Selection §4.4.5` 同结构

硬指示函数在 `d = d_c` 处不可微，使（i）实证窗口（`d \approx d_c` 邻域）的方程不可解析，（ii）数值模拟可能产生人工 chatter，（iii）"边界附近的过渡"现象（如临床上的"濒临崩溃但尚未"状态）无法形式化。需把硬指示推广为**有效光滑族**，并验证 §4.2 / §4.3 的关键结构（T-SUFF-2 信号-结构两型分裂、T-SUFF-4 反最小化、T-IRR-3.5 单向性、致命 `L_2` 判据）在族内不变。

#### 有效通道指示族（valid channel-state indicator family）

定义函数 `\psi : \mathbb{R} \times \mathbb{R} \to [0, 1]`，参数 `d_c \in \mathbb{R}_{>0}`。称 `\psi` 是**有效闭合通道指示**（valid closed-channel indicator），当且仅当满足：

| 编号 | 性质 | 含义 |
|---|---|---|
| **Q-univ-1** | **左饱和**：`\lim_{d \to -\infty}\psi(d; d_c) = 1`；具体地 `d \le d_c - w_{tr}` 时 `\psi \ge 1 - \varepsilon` | B 期深度区域内通道完全关闭 |
| **Q-univ-2** | **右饱和**：`\lim_{d \to +\infty}\psi(d; d_c) = 0`；具体地 `d \ge d_c + w_{tr}` 时 `\psi \le \varepsilon` | 健康深度区域内通道完全开放 |
| **Q-univ-3** | **单调过渡**：`\psi(d; d_c)` 关于 `d` 非增；过渡集中在过渡宽 `w_{tr} > 0` 内 | 通道关闭单向、连续 |
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

**陈述（P1-candidate）**：设 `\psi_1, \psi_2` 是两个有效闭合通道指示，共享相同 `d_c, w_{tr}^{max}` 但具体光滑形态不同。则 §4.2 / §4.3 / §5 / `Collective_Selection §4.4.5` 在 `\psi_1, \psi_2` 替代下保持以下结构特征不变（modulo `O(w_{tr})` 修正）：

(i) **T-SUFF-2 信号-结构两型分裂**：`S_{sig}` / `S_{str}` 两个动力学子通道分离的结构定义保持；过渡宽 `w_{tr}` 内出现"混合通道"（部分阻塞 + 部分开放）的连续过渡，不破坏两型本身的存在性。

(ii) **T-SUFF-4 反最小化原则**：`S_{sig} \downarrow \Rightarrow S_{str} \uparrow$ 在 `\dot{\Delta}_{avail}` 守恒下成立的结构论证（§4.4 boxed equation）保持——证明仅依赖 `\psi + \bar{\psi} = 1`（通道总量守恒），与 `\psi` 具体形态无关。

(iii) **T-IRR-3.5 阻塞转化项的单向性**：`\nu_{block}\psi(d; d_c)S_{sig}$ 转 `S_{str}` 单向（不可自动双向化）的结论保持，因为单向性来自 P0-03 / T-IRR-2 的吸收后不可自动恢复，而非 `\psi` 的不连续性。

(iv) **致命 `L_2` 判据 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}`**（§3.5.3）：判据结构与 `\psi$ 选择无关，仅依赖 `\psi$ 在 `d \approx d_c$ 域的非零（保证 `\nu_{block}\psi$ 项有效）。

(v) **`\mathcal{F}_S$ 投影分裂（T-PROJ-1, §6.5 第 4 项）**：`\hat{R}` 在 `\bar{\psi}$ / `\psi$ 投影下分裂为 `S_{sig}$ / `S_{str}$ 两路的算子级一致性保持；C3 闭包条件（stable-ISP 紧性）保证投影积分有意义。

#### 证明骨架

**(i) T-SUFF-2 两型分裂**：

`S_{sig}$ 与 `S_{str}$ 的两型分裂结构由 §4.1 直接给出（不来自 `\psi$ 的硬不连续）。`\psi$ 仅决定**两型间转化速率的开关**；从硬指示到光滑指示的替代使两型在 `d \approx d_c$ 邻域内出现"部分阻塞 + 部分开放"的混合通道（`\psi(d; d_c)\in (\varepsilon, 1-\varepsilon)$），但混合通道只是过渡区，不消除两型本体。`d \le d_c - w_{tr}$ 与 `d \ge d_c + w_{tr}$ 区间内（即"远离过渡"）两型分裂与硬指示相同，由 Q-univ-1+2 保证。

**(ii) T-SUFF-4 反最小化**：

T-SUFF-4 的核心是 `\dot{\Delta}_{avail}` 守恒（H7 T-DELTA-1）+ 通道总量守恒 `\psi + \bar{\psi} = 1`。前者由 T-DELTA-1 给出（不依赖 `\psi$ 形态）；后者由有效闭合通道指示的对偶定义直接保证。两个性质合起来给出：抑制 `S_{sig}$ 不改变 `\dot{\Delta}_{avail}`，新失配仅在 `\bar{\psi}$ 与 `\psi$ 间重新分配；当 `\bar{\psi}$ 在抑制下趋向 0（强制关闭信号通道），新失配全部进入 `\psi$ 通道（结构型）。证明独立于 `\psi$ 具体形态。

**(iii) T-IRR-3.5 单向性**：

`\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}` 的非零正性是**带前件的条件性结论**：`(\eta>0) \wedge (\varepsilon_{pg}>0) \wedge (\kappa_{\Psi_f}>0) \Rightarrow \nu_{block}>0`，hardness 取最弱前件，即 **P1-candidate**。反向通道的不存在另有独立根据（P0-03 / T-IRR-2 absorption remainder）。两者均不由 former P1-T07 证成。`\psi` 只是吸收态邻域投影的具体候选写法；从硬指示到光滑指示只把"硬边界"换为"过渡区域"，但 B 期邻域是否为真正吸收态仍需具体模型证明。

**(iv) 致命 `L_2` 判据**：

`\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}$ 来自 §3.5 T_dir ODE 的相对系数比较，与 `\psi$ 通道指示无直接耦合。`\psi$ 通过 `\Delta\Psi_f^{\mathrm{gap}}$ 间接进入 T_dir ODE，但 `\Delta\Psi_f^{\mathrm{gap}}$ 在 `d \approx d_c$ 邻域的连续性由 Q-univ-3 单调过渡保证。

**(v) `\mathcal{F}_S$ 投影一致性**：

T-PROJ-1 §6.2 把 `\mathcal{F}_S = \|\hat{R}\|_{H_P}$ 按 `\mathbb{1}[d \gtrless d_c]$ 投影分裂为 `S_{sig}/S_{str}$；用 `\bar{\psi}$ / `\psi$ 替代后投影积分仍收敛（C3 紧性 + Q-univ-1+2 饱和保证）；过渡区内 `\hat{R}$ 在两路上同时贡献，但两路总和仍为 `\|\hat{R}\|_{H_P}$（由 `\bar{\psi} + \psi = 1$）。

#### `O(w_{tr})$ 修正项的物理意义

光滑替代引入 `O(w_{tr})$ 修正，对应 `d \approx d_c$ 过渡区内的"半开通道"。这不是建模噪声，而是有结构内容：

- **临床上的"濒临崩溃"状态**：当 `d$ 接近 `d_c$ 但尚未跨过，主体感觉"还能撑但快不行了"——硬指示模型无法表达此状态，光滑模型自然给出
- **干预窗口的"软边界"**：`Occlusion_Dynamics §intervention-window`描述的四类窗口都不在硬阈值上瞬时激活，而是有"软启动"——`w_{tr}$ 给这种软启动一个量纲
- **`\Delta\Psi_f^{\mathrm{gap}}$ 在 `d \approx d_c$ 的连续可见性**：T_dir ODE 的 `-\kappa_{\mathrm{mask}}\Delta\Psi_f^{\mathrm{gap}}$ 项在过渡区内不会瞬时跳变，使 T_dir 自身保持 `C^0$ 连续

`w_{tr}$ 是 P-依赖的（不同主体 / 不同 domain 给不同过渡宽），但其**存在性**（>0）在算子级模型内是普适的——硬指示是 `w_{tr} \to 0$ 极限，物理上不可达。

#### P-依赖（**非**普适）的特征

| 特征 | P-依赖 | 物理解释 |
|---|---|---|
| 过渡宽 `w_{tr}$ 的物理量纲 | 主体 / domain 特定 | 临床干预阈值的 "软启动时间" |
| `\psi$ 的过渡曲线形态（sigmoid vs tanh vs polynomial）| 测量层选择 | 不同测量协议可能给不同 `\psi$ 拟合 |
| 过渡区内的混合通道行为 | 主体特定 | 临床上"濒临崩溃"个体差异显著 |

#### T-CHANNEL-1 不证明的事项

1. **不**证明 `w_{tr}$ 是 P-universal 的——`w_{tr}$ 是赌注 / 主体类别 / 历史阶段相关的（P3）
2. **不**承诺 `\psi$ 是 `C^\infty$ 平滑——四条性质只要求 `C^0$ 单调（硬指示也是有效成员，作为 `w_{tr} \to 0$ 极限）
3. **不**覆盖随机 / 多值 `\psi$（非确定性通道指示暂留为 P3 候选）
4. ~~**不**证明集体版 T-CHANNEL-1^{coll}——`\mathbb{1}[d^{coll} \gtrless d_c^{coll}]` 在 `\mathcal{P}` 上的扩展耦合 H6 的 C5^{coll} `M(t)` 可测性闭包，是后续轮次任务~~ **已收口（H11，2026-04-26）**：`Core_Law/SRT_Collective_Selection.md §4.9.3 T-CHANNEL-1^{coll}` 给出集体版（C1^{coll}-C5^{coll} + C7^{M-stab} + Q-univ-5^{coll}），五个不变量保持，`\nu_{ext}\|M_{ext}\|` 与 `\psi^{coll}` 加性独立

#### T-CHANNEL-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| `\mathbb{1}[d \le d_c]$ 是硬指示 | 模型形式（§4.3）| 有效族 `\psi$ 的 `w_{tr} \to 0$ 极限（§4.5）|
| 两型分裂 / 反最小化 / 单向性 / 致命 L_2 / 投影一致性"与硬指示无关" | 隐含主张 | T-CHANNEL-1 (i)-(v) 五个不变量 |
| 过渡区物理意义（"濒临崩溃"等）| 缺失 | 由 `w_{tr} > 0$ 自然给出 |

**P1-candidate 地位的根据**：T-CHANNEL-1 把"通道指示是否硬"从建模约定升为"有效族下的不变量"；要升 P1，需要：(a) `w_{tr}$ 在具体 domain 的实证窗口（神经层 prediction-error gating 的过渡宽 / 临床干预窗口的软启动时间常数）；(b) 集体版 T-CHANNEL-1^{coll} 与 `M(t)` 的耦合；(c) `\Delta\Psi_f^{\mathrm{gap}}$ 在过渡区的算子层精确定义（与 `_SRT_T_DIR_CANONICAL §5-§6` 协调）。

---
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

按 ST-A，这一工作区是 generative reselectability 的实现候选，不是 P1 反闭合必要性的方程证明。模型预测：无真实重选 → `r(t) \to 0` → T_dir 被结构型苦难侵蚀 → 方向感要么塌 (`T_{dir} \to 0`) 要么靠 `s_{ext}` 伪装支撑；该预测需在声明环境与时间窗后检验，不能仅凭工作区边界认定系统必趋 `\mathcal{A}_{path}`。

---

## §6. 与已有主方程的关系：T-PROJ-1 投影定理

> **Status (2026-04-25 H5)**：本节把"四变量系统是主方程的导出投影"从陈述提升为**带条件证明的形式定理**。本节之前是 `SRT_L1_Formalism.md §7` 升 P1 检查单第 7 项的开放点；本轮以 P1-candidate 给出第一遍构造。

### §6.1 主方程与 L1 四变量的对接

`Core/SRT_Core_22_Equations.md` Eq-Evo-01 / Eq-Evo-03 主动力学（单 ISP，固定 P）：

$$
\frac{d\sigma_M}{dt} \;=\; \hat{G}_\theta[\sigma_M] \;-\; \nabla F[\sigma_M] \;-\; \lambda\cdot\nabla C_{L_2}[\sigma_M]
\qquad
\frac{d\theta}{dt} \;=\; \gamma\cdot A[\sigma_M, \mathrm{Target}] - \delta\cdot\partial_\theta\Phi(\theta) - k(\mathrm{Input}_{L_1} - \mathrm{Baseline})
$$

（本节为消除符号冲突把主方程态场写作 `\sigma_M`；本文件其它处的 σ 仍指自指率 `σ_{sr}`，按 `_SRT_SYMBOL_TABLE.md` Usage Rule 12 转读。）

**问题陈述**：本文件 §2-§5 的四变量系统 `(σ_{sr}, d_c, T_{dir}, S)` 是否是主方程 `(\sigma_M, \theta)` 动力学的**严格导出投影**？

### §6.2 投影算子的形式定义

设 P 为 stable ISP（满足 P1-T06）。定义四个标量泛函（投影算子）`\mathcal{F}_X : (\sigma_M, \theta) \mapsto \mathbb{R}` 如下：

**`σ_{sr}` 投影**

$$
\mathcal{F}_\sigma(\sigma_M, \theta) \;:=\; \frac{\|\theta^{\mathrm{trace}}\|}{\|\theta^{\mathrm{trace}}\| + \|\theta^{\mathrm{ext}}\|}
\qquad\text{其中}\quad
\theta^{\mathrm{trace}} \;:=\; \mathcal{P}_{L_2\to\theta}\bigl[L_2(t)\bigr],\;\;
\theta^{\mathrm{ext}} \;:=\; \theta - \theta^{\mathrm{trace}}
$$

`\theta^{\mathrm{trace}}` 是 `\theta` 中由 `L_2` 写回（Eq-Bridge-L2-01）贡献的部分；`\theta^{\mathrm{ext}}` 是来自 anchoring 与外部输入的部分。

**`d_c` 投影**

$$
\mathcal{F}_d(\sigma_M, \theta) \;:=\; d_{\max} - \alpha_d \cdot \mathrm{tr}\bigl[\nabla^2 C_{L_2}[\sigma_M]\bigr]_{loc}^{-1}
$$

即 `d_c` 由 `L_2` scaffold 局部曲率的逆决定——scaffold 越刚（`\nabla^2 C_{L_2}` 越大），重选容量越小，`d_c` 越接近 `d_{\max}`。

**`T_{dir}` 投影**

$$
\mathcal{F}_T(\sigma_M, \theta) \;:=\; \cos\angle\bigl(\hat{G}_\theta[\sigma_M],\;\nabla_{L_0}\mathrm{Order}[\sigma_M]\bigr) \cdot \mathbb{1}\bigl[\mathrm{Anchor}_{L_0}(P, t)\bigr]
$$

`T_{dir}` 是"算子选择方向"与"L_0 选择秩序方向"的余弦对齐，在 anchoring 活跃时计入。`\Delta\Psi_f^{\mathrm{gap}}` 对应该余弦的实-感分裂误差（`\nabla F[\sigma_M]` 的不可读分量）。

**`S` 投影**

$$
\mathcal{F}_S(\sigma_M, \theta) \;:=\; \|\hat{R}(\sigma_M, \theta)\|_{H_P}
\qquad\text{其中}\quad
\hat{R} \;:=\; \frac{d\sigma_M}{dt} - \bigl[\hat{G}_\theta - \nabla F - \lambda\nabla C_{L_2}\bigr]
$$

`\hat{R}` 是主方程在 P 处的**剩余项**——P1-T06 第一人称登记把 `\|\hat{R}\|` 在 P 自身希尔伯特结构 `H_P` 下的范数读为苦难。`S_{sig}` / `S_{str}` 来自 `\hat{R}` 在"通道开放" / "通道关闭"投影下的分裂。

### §6.3 投影下的链式法则

对任意 P 上的足够光滑泛函 `\mathcal{F}_X(\sigma_M, \theta)`：

$$
\frac{d\mathcal{F}_X}{dt} \;=\; \langle\,\partial_{\sigma_M}\mathcal{F}_X,\; \dot\sigma_M\,\rangle + \langle\,\partial_\theta\mathcal{F}_X,\; \dot\theta\,\rangle
$$

把 Eq-Evo-01 与 Eq-Evo-02 代入，逐项展开 `\hat{G}_\theta - \nabla F - \lambda\nabla C_{L_2}` 与 `\gamma A - \delta\partial_\theta\Phi - k(\mathrm{Input}_{L_1}-\mathrm{Baseline})`，对每个 `X \in \{σ_{sr}, d_c, T_{dir}, S\}` 给出 ODE 形式。

### §6.4 闭包假设（Closure Assumptions）

四变量系统在投影下闭合需要四条结构性假设：

| 编号 | 假设 | 主方程层根据 |
|---|---|---|
| **C1** | **慢-快分离**：`θ` 与 `\sigma_M` 在不同时间尺度演化（`\dot\theta` 在 `\sigma_M` 收敛时间尺度上近似常数） | Eq-Evo-03 快-慢系统结构本身 |
| **C2** | **`L_2` 写回的 Markov 闭包**：`\dot{\theta}^{\mathrm{trace}}` 仅依赖当前 `(σ_{sr}, ρ_{local})`，不显式依赖更高阶 `L_2` 历史 | Eq-Bridge-L2-01 写回方程的结构（写回是当前选择的函数，迹是过去选择的累积投影） |
| **C3** | **Stable-ISP 紧性**：四个泛函 `\mathcal{F}_X` 在 P 的 stable-ISP 邻域内有界且 Lipschitz | P1-T06 stable ISP 四条件保证邻域紧致与可重选 |
| **C4** | **方向投影的可分性**：`T_{dir}` 投影里的余弦角与 `\sigma_M` 的纵向幅度近似可分，使 `\dot{T}_{dir}` 不显式依赖 `\|\sigma_M\|` 高阶项 | Eq-Bridge-IG-01 信息几何 Fisher 形式给的局部正交分解 |

**关键**：C1-C4 不是无代价假设——它们对应 §7 Open Pressures 中的具体未封口项（χ 跳跃族普适性、`\Delta\Psi_f^{\mathrm{gap}}` 算子化、阈值实证窗口）。当某条假设在特定 domain 失效时，对应的 L1 ODE 在该 domain 失去严格投影地位、降为 P3 现象学代理。

### §6.5 T-PROJ-1：四变量系统的投影定理

**陈述（P1-candidate）**：在 stable ISP P 上，若闭包假设 C1-C4 成立，则

$$
\boxed{\;\frac{d\mathcal{F}_X}{dt}\bigg|_{\text{Eq-Evo-01,02}} \;\overset{C1\text{-}C4}{=}\; \mathrm{RHS}_X^{\text{§2-§5}} \;+\; O(\eta)\;}
\qquad X \in \{σ_{sr}, d_c, T_{dir}, S\}
$$

其中 `\mathrm{RHS}_X^{\text{§2-§5}}` 是本文件 §2.2 / §3.2 / §3.5 / §4.2-§4.3 的 ODE 右端，`O(\eta)` 是闭包高阶残差（C1-C4 失效时的修正项；当 C1-C4 严格成立时 `\eta = 0`）。

**逐项对应**：

| L1 ODE 源项 | 主方程来源 | 闭包条件 |
|---|---|---|
| `\sigma_{sr}` 写回项 `\alpha w \phi(σ_{sr})` | Eq-Evo-02 学习项 `\gamma A[\sigma_M, \mathrm{Target}]` 中 `\mathrm{Target} = σ_M` 自身分量 | C2 |
| `\sigma_{sr}` 衰减项 `\lambda_{trace}T σ_{sr}` | Eq-Evo-02 摩擦下降项 `\delta\partial_\theta\Phi(\theta)` 在 `θ^{trace}` 投影 | C2 |
| `\sigma_{sr}` 外部驱动项 `\beta i$ | Eq-Evo-02 稳态反冲项 `k(\mathrm{Input}_{L_1} - \mathrm{Baseline})` | C1 |
| `d_c` 漂移项 `\gamma_\rho \rho_{local}` | `\nabla^2 C_{L_2}` 沿 `ρ_{local}` 方向的累积 | C3 |
| `d_c` 漂移项 `\gamma_\sigma \max(0, σ_{sr}-σ_{sr}^{sub})` | `\nabla^2 C_{L_2}` 在 `\theta^{trace}` 占优区的局部刚化 | C2 + C3 |
| `T_{dir}` 弛豫项 `-\kappa_{\mathrm{relax}}(T_{dir} - T_{dir}^{\mathrm{alg}})` | `\hat{G}_\theta` 与 `\nabla_{L_0}\mathrm{Order}` 的余弦角对 `(d, σ_{sr})` 的代数依赖 | C4 |
| `T_{dir}` 扣除项 `-\kappa_{\mathrm{mask}}\Delta\Psi_f^{\mathrm{gap}}` | `\nabla F[\sigma_M]` 中实-感分裂部分（不可读分量） | C4 |
| `T_{dir}` 真实重选泵入 `+\kappa_r r(t)` | P1-T05 real choice moment 在 `\hat{G}_\theta` 的事件结构 | C3 |
| `S_{sig}` 新失配项 `\mu_\Delta \dot{\Delta}_{avail}` | `\|\hat{R}\|_{H_P}` 在 `d > d_c` 投影 | C3 |
| `S_{str}` 阻塞转化项 `\nu_{block}\mathbb{1}[d\le d_c]S_{sig}` | `\|\hat{R}\|_{H_P}` 在 `d \le d_c` 投影；`ν_{block}` 由 T-IRR-3.5 给出独立前件的条件模型 | C3 + T-IRR-3.5 |

**证明骨架**：

1. **σ_{sr} 项**：`\dot{\mathcal{F}}_\sigma = (1 - σ_{sr})\dot{\|\theta^{\mathrm{trace}}\|}/\|\theta\| - σ_{sr}\dot{\|\theta^{\mathrm{ext}}\|}/\|\theta\|`。代入 Eq-Evo-02：`\dot{\|\theta^{\mathrm{trace}}\|}` 在 C2 下取 `\gamma A` 投影，`\dot{\|\theta^{\mathrm{ext}}\|}` 在 C1 下取稳态反冲项投影；化简后即 §2.2 logistic 形式。

2. **d_c 项**：`\dot{\mathcal{F}}_d = \alpha_d \cdot \dot{\mathrm{tr}\,(\nabla^2 C_{L_2})^{-1}}`。`\nabla^2 C_{L_2}` 由 Eq-Bridge-L2-01 的 sediment-rate-and-stiffness 关系决定；其漂移率在 C3 下分解为 `ρ_{local}` 项 + `(σ_{sr}-σ_{sr}^{sub})` 项 + 干预窗口项 - 衰减项，即 §3.2 形式。

3. **T_{dir} 项**：`\dot{\mathcal{F}}_T` 来自余弦角的导数；C4 保证横纵分离，使该导数分解为弛豫项（向代数目标 `T_{dir}^{\mathrm{alg}}`）+ 真实重选泵入项 + 实-感分裂扣除项 + 结构型苦难侵蚀项 + 健康 `L_2` 支架项，即 §3.5 五项 ODE。

4. **S 项**：`\dot{\mathcal{F}}_S` 来自 `\|\hat{R}\|_{H_P}` 的链式导数；按 `\mathbb{1}[d > d_c]` / `\mathbb{1}[d \le d_c]` 投影分裂为 `S_{sig}` / `S_{str}` 两路；T-IRR-3.5 给出 `ν_{block}` 的条件性算子表达式。反向通道不自动存在根于 P0-03 / T-IRR-2，而正向系数的正性依赖 T-IRR-3.5 的三个前件；均非 former P1-T07 hierarchy 的后果。

### §6.6 T-PROJ-1 不证明的事项

为避免过度主张，T-PROJ-1 **不承诺**以下内容：

1. **不**证明 L1 系数（`α, β, λ_{trace}, γ_ρ, κ_{relax}, μ_Δ, ν_{block}` 等）的具体数值——这些仍为 P3 实证问题
2. **不**证明 χ(σ_{sr}; σ_{sr}^{self}) 跳跃函数族的普适性（C2 闭包之外）
3. **不**证明 `\Delta\Psi_f^{\mathrm{gap}}` 的算子层定义（`_SRT_T_DIR_CANONICAL.md §5-§6` 现象学分裂仍为依赖）
4. ~~**不**证明集体版主方程（Eq-Multi-01 / 02 / 03）→ `Collective_Selection §4.4-§4.6` 的对应投影；集体版 T-PROJ-1^{coll} 是后续轮次的扩展任务~~ **已在 H6（2026-04-25）落地**：`Core_Law/SRT_Collective_Selection.md §4.7 T-PROJ-1^{coll}` 给出集体投影定理（C1^{coll}-C5^{coll} 五条闭包，含新增 `M(t)` 可测性 MOC 闭包 C5^{coll}）；T-PROJ-1^{coll} 在 `\mathcal{P} = \{P\}` 极限下退化为本节 §6 T-PROJ-1

### §6.7 T-PROJ-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| 四变量系统**没有引入新本体** | 陈述（§6 paragraph） | 定理后果（C1-C4 + 投影构造） |
| 四变量系统**是主方程的导出** | 陈述 | C1-C4 满足时严格成立的恒等式（modulo `O(\eta)`）|
| 主方程层 → 四变量层不需要额外 axiom | 隐含 | `\mathcal{F}_X` 投影算子 + Eq-Evo-01/02 的链式法则 |
| 四变量 ODE 系数与主方程参数的关系 | 未给 | §6.5 表格给出 source-by-source 对应（系数本身仍为 P3）|

**P1-candidate 地位的根据**：T-PROJ-1 把"四变量是主方程投影"从 modeling claim 升为 P1-candidate 定理；要升 P1，仍需把 C1-C4 中每一条与对应 Open Pressure（`\Delta\Psi_f^{\mathrm{gap}}` 算子化、χ 普适性、阈值实证窗口、集体版投影）逐条收口。

---

## §7. Open Pressures

> **Hardening status (2026-04-25; ST-A source correction 2026-08-11)**: §7.1 σ 符号冲突已通过 σ_{sr} 命名空间分离收口（`_SRT_SYMBOL_TABLE.md` Usage Rule 12）；§7.2 `\dot{\Delta}_{avail}` 形式化已通过 H7（`Core_Law/SRT_L1_Hardening_Notes.md §2 T-DELTA-1`）的 A1-A3 算子空间假设 + 三投影算子升 P1-candidate 收口；**§7.3 χ 跳跃函数族普适性已通过 H8（本文件 §2.5 T-CHI-1）"有效二阶相变核"四条属性 + 族内不变量定理收口**；§7.6 FEP 桥接在 `Core_Law/SRT_L1_Hardening_Notes.md §4` 已给出翻译表；§7.7 `L_0` 不可逆算子级对齐在 `Core_Law/SRT_Irreversibility.md §4.5 T-IRR-3.5` 给出 `\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}` 的条件性表达式；§7.8 T_dir 独立 ODE 已在 §3.5 给出四变量闭合的第一遍形式；**§6 主方程投影定理在 §6 T-PROJ-1（H5，2026-04-25）给出带闭包假设 C1-C4 的形式化构造；集体版投影 T-PROJ-1^{coll} 在 `Core_Law/SRT_Collective_Selection.md §4.7`（H6，2026-04-25）给出 C1^{coll}-C5^{coll}**。

本 draft_v0 状态下尚未封口：

1. **σ 符号冲突**：本文件 σ（自指率，`[0,1]` 标量）与 `Core/SRT_Core_22_Equations.md` σ（主方程状态场）共用符号；需引入新记号（候选：`σ_{self}` 改为 `κ_{self}` 或 `\bar{\sigma}`）避免歧义
2. **`\dot{\Delta}_{avail}` 的正式化**：~~依赖 `\hat{G}_\theta^{actual}` 与 `\hat{G}_\theta^{available}` 的差，二者本身未形式化~~ **已收口（H7，2026-04-25）**：`Core_Law/SRT_L1_Hardening_Notes.md §2 T-DELTA-1` 给出 `\hat{G}_\theta^{available} := \sup_{\mathrm{Op}(P)}\{\hat{G} \mid \text{结构上可达且 } θ\text{-相容}\}`、`\hat{R} := \hat{G}_\theta^{available} \ominus \hat{G}_\theta^{actual} \in T\mathrm{Op}(P)` 的算子级定义 + 三个正交投影 `\Pi_{T_{dir}}, \Pi_{\Psi_f}, \Pi_{L_0}` + A1（仿射结构）/ A2（近似正交）/ A3（权重赌注决定性）三条可证伪假设。剩余开放点：A1 在更广 stable-ISP 域的验证、A2 实证窗口、A3 与 Eq-Bridge-D-01 stake-gated 的 source-by-source 对位
3. **χ(σ; σ_{self}) 跳跃函数的光滑族**：~~二阶凝结的跳跃形状是否普适，还是 `P` 相关？~~ **已收口（H8，2026-04-25）**：本文件 §2.5 T-CHI-1 给出"有效二阶相变核"四条结构属性（P-univ-1 有界 / P-univ-2 跃前基线 / P-univ-3 跃后放大 / P-univ-4 单调过渡）+ 族内不变量定理（双稳态存在性、病理吸引子拓扑、致命 `L_2` 判据结构、相变方向均 χ-无关）。剩余开放点：在更广 χ 空间（非单调过渡）的扩展、具体 domain 实证 χ-shape 对位、集体版 T-CHI-1^{coll} 与 `M(t)` 耦合
4. **多主体扩展**（2026-04-25 H3 状态）：本文件保持单 P 形式；集体层四变量耦合动力学已在 `Core_Law/SRT_Collective_Selection.md §4.4-§4.6` 给出第一遍，含 `\sigma^{coll}` ODE（新 `\lambda_M\,\mathrm{tr}\,M` 项）、`d_c^{coll}` ODE（新 `\gamma_{asym}\|M_{asym}\|` 项）、`T_{dir}^{coll}` ODE（集体层致命 `L_2` 判据）、`S^{coll}` 两型 ODE（新 `\nu_{ext}\|M_{ext}\|` 外部化项），以及 §4.5 个体↔集体双向耦合。未封口部分移至 `SRT_Collective_Selection.md §9.7`
5. **阈值参数的实证固定**：`σ_{sub}, σ_{self}, σ_{health}, d_c, d_{narrow}, r_{min}, S_{min}, S_{max}` 以及新增 `\kappa_{\mathrm{relax}}, \kappa_r, \kappa_{\mathrm{mask}}, \kappa_S, \kappa_{\mathrm{sup}}` 全部在当前 draft_v0 只有定性位置；不指望一次性实测，但需要标出哪些是最优先的测量目标
6. **与 FEP / predictive processing 的桥接**：`S_{sig}` 与 prediction error 的结构对应是高优先级；`Neuroscience/SRT_Clin_02_FEP.md` 已经是 bridge 层，下一步需要在方程层写出条件翻译
7. **time-reversibility**：~~陈述级 → 算子级对齐~~ **条件性收口（H4，2026-04-25；ST-A source correction 2026-08-11）**：`SRT_Irreversibility.md §4.5 T-IRR-3.5` 把 `ν_{block}` 写为独立前件的本地模型 `η·\varepsilon_{pg}·\kappa_{\Psi_f}`；正性按带前件的条件性结论读，单向性中反向通道不存在这一层独立根于 P0-03 / T-IRR-2。剩余开放点：`\varepsilon_{pg}(P,t)` 的本地化精确定义、`\kappa_{\Psi_f}` bridge、B 期邻域的吸收证明、集体版 `\nu_{block}^{coll}` 对位
8. **T_dir 独立 ODE 的算子化（新增，2026-04-25）**：§3.5 给出第一遍形式，但以下仍待封口——(a) `T_{dir}^{\mathrm{alg}}` 中光滑阶跃 `\Theta` 的普适族是否存在；(b) `\Delta\Psi_f^{\mathrm{gap}}` 作为算子层对象的形式定义（目前依赖 `_SRT_T_DIR_CANONICAL.md §5–§6` 的现象学分裂）；(c) `T_{dir} \in [0,1]` 的投影算子 `\Pi_{[0,1]}` 选择（硬截断 vs 光滑 sigmoid 重参化）；(d) `\kappa_{\mathrm{relax}} > \kappa_{\mathrm{mask}}` 这一致命 `L_2` 判据的实证窗口

---

## §8. Cross-References

- 个体化 / σ 定义 / 三相结构 → `Core_Law/SRT_Individuation.md`
- 遮蔽动力学 / A/B 分期 / 四类干预窗口 / 四类解耦触发 → `Core_Law/SRT_Occlusion_Dynamics.md`
- 苦难 / 两型 / 四类分型 / 反最小化 → `Core_Law/SRT_Suffering.md`
- 主动力学 / `\hat{G}_\theta[\sigma] - \nabla F - \lambda\nabla C_{L_2}` → `Core/SRT_Core_22_Equations.md`
- 路径层 `ρ` / 写回 / scaffold sedimentation → `Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold`
- P1-T06 stable ISP（本文件所有方程的前提）→ `Core/SRT_Core_21b_Constitutive_Theorems.md`
- former P1-T07 demotion / absorption remainder → 同上
- ST-A generative reselectability / conditional anti-closure candidate（§5.3 工作区的解释层）→ `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`
- P1-T02 ontological time（`w(t)` 写回率的 upstream）→ 同上
- d-value / T_dir / Ψ_f 的 canonical → 对应 `_SRT_*_CANONICAL.md`

---

## §9. 定位与使用规则

- **本文件做**：σ / d_c / T_dir / S 四变量的最小耦合动力学；病理吸引子与健康工作区的结构刻画；反最小化原则的方程化；致命 `L_2` 的可读性层方程化判据
- **本文件不做**：具体 domain 的参数固定、临床量表、实验设计、AI 实现细节
- **引用规则**：涉及四变量耦合、病理吸引子、健康工作区、致命 `L_2` 方程化判据的**方程级**陈述时，优先回链本文件；涉及四变量**概念**定义时，优先回链各自的 L1 主文件（T_dir → `_SRT_T_DIR_CANONICAL.md`）
- **不得**把本文件的方程读成已经过实证检验的定量定律——它是 P1-candidate 结构形式化，是让 draft_v0 文件能够**联合被批评与修正**的手段
