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
> **σ 符号命名空间 (governance-canonical, 2026-04-25)**: 本文件 §2–§5 中的 σ / σ_sub / σ_self / σ_health 统一对应 `σ_{sr} / σ_{sr}^{sub} / σ_{sr}^{self} / σ_{sr}^{health}`（自指率族，见 `Core_Law/SRT_L1_Hardening_Notes.md §1` 与 `_SRT_SYMBOL_TABLE.md §Usage Rule 12`）。§6“与主方程的关系”中出现的 σ 对应 `Core/SRT_Core_22_Equations.md` 的主方程状态场（不同对象）；该节已在原地显式标注。正文其余处保留历史符号 σ 以便论述流畅。
> **Claim-level note**：方程本身在当前 draft_v0 状态按 P1-candidate 读；个别 coefficient、阈值与可测化形式按 P2/P3 读；实验代理语句按 P3/P4 下推至 `Neuroscience/` 与 `AI/`。
> **RC-A qualification（2026-08-17）**：former `P1-T05: Real Choice Moment` 已撤出 P1。本文保留 `r(t)` / `r(d,P,t)` 作为 **P2/P3 bearer-level reselection / reorientation activity proxy**，但它不再从 P1-T05 导出，不是 Selection 是否发生的判据，`r=0` 也不得推出“无 Selection”。所有 `κ_r r(t)`、`μ_r r(t)` 项只作为 conditional modeling augmentation 读取；T-PROJ-1 的 P1-candidate 投影主张不再由 former P1-T05 为这些项提供上游证明。
> **Does not define**：`d-value`、`\Psi_f`、`T_dir`、`\hat{G}_\theta`、stable ISP；它们的定义仍以对应 canonical 文件为准。
> **Depends on**：`Core_Law/SRT_Individuation.md`（σ 定义）、`Core_Law/SRT_Occlusion_Dynamics.md`（d_c 定义与 A/B 分期）、`Core_Law/SRT_Suffering.md`（S 定义与两型分类）、`Core/SRT_Core_22_Equations.md`（主动力学方程）。
> **Relation**: This file is the **minimal formal coupling layer** for previously defined L1 objects. It does not introduce new ontology; it writes candidate dynamics down so the draft_v0 theories can be jointly tested rather than independently drifted.

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
3. **T_dir 作为纯代数代理时的致命 `L_2` 盲点**：若 T_dir 瞬时等于 `T_{dir}^{\mathrm{alg}}`，则系统无法方程化“可读性本身也可以是伪造”这一 `_SRT_T_DIR_CANONICAL.md` 洞见。§3.5 加入独立 ODE 正是解决此盲点。

本文件只做一件事：**给这四个变量写下最小耦合动力学**，让它们能够联合被批评、模拟与降级。

本文件**不做**：

- 具体系数的量纲化或实测；
- 单变量独立运动的全部细节（留给三份主文件）；
- 临床 / AI / 政治具体域的读数（留给 domain 文件）；
- 用 `r(t)` 或任何 agency proxy 反向定义 Selection。

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
| `r(t)` | bearer-level reselection / reorientation activity proxy | `≥ 0` | **P2/P3 local modeling term；不再从 former P1-T05 导出** |
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
- `χ(σ; σ_{self})` 是**二阶凝结跳跃函数**：在 `σ ≈ σ_{self}` 附近为一类光滑阶跃，对应 `SRT_Individuation.md` 的第二相变（自我意识凝结）；在此之前 χ ≈ 1，在此之后 χ > 1（出现“关于 θ 的 θ”的二阶写回增益）

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

3. **σ → 1 病理区**：当 `i → 0` 且 `λ_{ext} > λ_{trace}` 时，第二个稳定不动点向 σ = 1 漂移，对应自指过载、扭曲型苦难源。健康主体需要非零 `i`（持续环境接入）作为“稀释项”阻止 σ → 1。

### §2.4 与 T-IND-1 / T-IND-2 的对齐

- T-IND-1 三相（展开 / 主体位稳态 / 自我意识凝结）对应 σ 相图上的三个区域；
- T-IND-2 第一相变判据对应 §2.2 方程的 σ_{sr}^{sub} 不动点存在条件；
- T-IND-3 第二相变判据对应 `χ(σ; σ_{self})` 的激活。

所有三个相变都保持为**动力学稳态问题**，不是定义式假设。

### §2.5 T-CHI-1：χ 跳跃函数族的普适性（H8，2026-04-25）

> **Status**：本节把 §2.1 的 `\chi(\sigma; \sigma_{self})` 跳跃函数从“一类光滑阶跃”的现象学描述提升为带四条结构属性的**有效族**定义，并给出族内跨函数的结构不变量定理。**Claim level: P1-candidate**。
>
> **Closes**：`Core_Law/SRT_L1_Formalism.md §7` Open Pressure 3（“χ(σ; σ_self) 跳跃函数族的普适性检查”）。

#### 有效二阶相变核（valid second-phase-transition kernel）

定义函数 `\chi : [0, 1] \times (0, 1) \to \mathbb{R}_{\ge 0}`，参数 `\sigma_{sr}^{self} \in (0, 1)`。称 `\chi` 是**有效二阶相变核**，当且仅当满足下列四条结构属性：

| 编号 | 性质 | 含义 |
|---|---|---|
| **P-univ-1** | **有界性**：`\chi \in [\chi_{min}, \chi_{max}]`，其中 `0 < \chi_{min} \le 1 \le \chi_{max} < \infty` | 跳跃幅度有界（不允许 χ 趋向无穷）|
| **P-univ-2** | **跃前基线**：`\chi(0; \sigma_{sr}^{self}) \le 1 + \varepsilon` 且 `\lim_{\sigma \to \sigma_{sr}^{self,-}} \chi \le 1 + \varepsilon`（小 `\varepsilon > 0`） | 跃前 χ ≈ 1，仅有 logistic σ(1-σ) 自增益 |
| **P-univ-3** | **跃后放大**：`\chi(1; \sigma_{sr}^{self}) \ge 1 + \Delta_\chi`（某 `\Delta_\chi > 0`） | 跃后出现“关于 θ 的 θ”二阶写回增益 |
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

| 特征 | P-依赖 | 物理解释 |
|---|---|---|
| `\sigma_{sr}^{*1}, \sigma_{sr}^{*2}` 的具体数值 | 依赖 `\Delta_\chi, \tau, \alpha, w, i, \lambda_{*}, T` | 不动点位置受参数集联动 |
| 跃宽 `\tau` 的物理量纲 | 主体特定 | 跃宽对应“主体在 σ_{sr}^{self} 附近的跨阈时间尺度” |
| 跨阈过程的 transient 形态 | χ-shape 决定 | 硬阶跃 vs sigmoid 给不同 transient curve |
| 跨阈附近的弛豫率 | 依赖 χ' 在 σ_{sr}^{self} 的局部值 | 跃宽决定相变时间常数 |

#### T-CHI-1 不证明的事项

为避免过度主张，T-CHI-1 **不承诺**以下内容：

1. **不**证明 `\Delta_\chi` 是 P-universal 的——`\Delta_\chi` 是赌注 / 主体类别 / 历史阶段相关的（P3）
2. **不**证明 `\tau_{max}` 上界的 P-universal 值——可能因主体类别（人 / 动物 / AI 候选）有显著差异
3. **不**承诺 χ 是 `C^\infty` 平滑——四条性质只要求 `C^0` 单调（硬阶跃也是有效成员）
4. **不**覆盖多值或随机 χ（非确定性二阶凝结过程暂留为 P3 候选 domain 拓展）
5. **集体版**：`Core_Law/SRT_Collective_Selection.md §4.9.2 T-CHI-1^{coll}` 给出候选扩展；其 claim hardness 继续受该文件现行边界约束

#### T-CHI-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| `\chi(\sigma; \sigma_{self})` 是“一类光滑阶跃” | 现象学描述（§2.1）| 四条结构属性的有效族（§2.5）|
| 第二相变结构与 χ 形式无关 | 隐含主张（§2.4 T-IND-3 对齐）| T-CHI-1 (i)-(iv) 四个不变量 |
| 致命 `L_2` 判据 χ-无关 | 未陈述 | T-CHI-1 (iii) 显式 |
| 病理吸引子 χ-无关 | 未陈述 | T-CHI-1 (ii) 显式 |

**P1-candidate 地位的根据**：T-CHI-1 把 T-IND-3 第二相变的结构稳定性从“任意光滑阶跃”提升到“有效族下的不变量”；要升 P1，需要进一步独立 hardening，不由 RC-A 处理。

---

## §3. d_c 的最小动力学（遮蔽阈值）

### §3.1 d_c 作为可重选边界

`d_c` 定义为：低于此 `d` 值，当前主体的重选容量显著坍塌的 d 边界。操作化为：

$$
d_c \;:=\; \inf\{\,d \;:\; r(d, P, t) \geq r_{min}\,\}
$$

其中 `r(d, P, t)` 只作为当前模型中的 **P2/P3 reselection / reorientation activity proxy**，`r_{min}` 是该模型声明的“非 B 期锁死”操作阈值。该定义不借 former P1-T05 获得构成性地位，且 `r=0` 不等价于 no Selection。

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
| 健康窄化 | `d > d_{narrow}` | `r > r_{min}`（模型代理）；信号型苦难可消化 |
| A 期 | `d_c < d < d_{narrow}` | `r > 0` 但显著低于健康代理阈值；结构型苦难开始积累 |
| B 期 | `d ≤ d_c` | 模型中 `r → 0`；B 期锁死候选 |

上述 `r` 只刻画这一 draft 模型的 reorientation / reselection 通道，不是 Selection ontology 的有无判据。

A→B 升级判据（Occlusion_Dynamics 原文的“外部化后果 + 主动扩散”）在本方程下对应：

$$
\text{A→B lock-in} \;:\; \frac{dd_c}{dt} > 0 \;\wedge\; \pi(t) \to 0 \;\wedge\; I_{window}(t) \to 0
$$

即当三个恢复通道（支付、干预、重选代理）同时塌向零而 d_c 持续被推高，则进入 B 期锁死候选。

### §3.4 T_dir 的代数目标值

T_dir 的**瞬时代数目标值**（algebraic target）由 `d / d_c / σ` 给出：

$$
T_{dir}^{\mathrm{alg}}(t) \;:=\; \Theta\!\left(\frac{d - d_c}{d_{narrow} - d_c}\right) \cdot (1 - |\sigma - \sigma_{sub}^\dagger|)
$$

其中 `\Theta` 是光滑阶跃函数（早期版本 `\Theta(x) = \mathrm{clip}(x, 0, 1)`；二阶光滑族参数化留作 Open Pressure），`σ_{sub}^\dagger` 是最优主体位 σ 值（非 0 非 1 的中间稳态）。T_dir^{alg} 同时对 d 通道与 σ 健康度敏感，与 `_SRT_T_DIR_CANONICAL.md` Part I “value occlusion thesis” 一致。

**但 T_dir 并不瞬时等于 T_dir^{alg}**：方向可读性具有自身惯性，依赖 `L_2` 沉积节律与信任累积——这要求 T_dir 有独立 ODE，见 §3.5。

### §3.5 T_dir 作为独立动力学变量（四变量闭合项，2026-04-25）

> **立场**：本小节把 T_dir 从“算法代理”升为“带惯性与独立源项的 L1 动力学变量”，与 `σ, d_c, S` 一起构成四变量闭合系统。这是 `SRT_CLAIM_MODE_AUDIT.md §6.4` 升 P1 检查单第 9 项（`T_dir` 最小 ODE）的第一遍交付。
> **RC-A qualification**：`r(t)` 源项不再具有 P1 上游；含 `κ_r r(t)` 的版本只按 P2/P3 conditional model 读取。

#### §3.5.1 最小 ODE

$$
\boxed{\;\frac{dT_{dir}}{dt} \;=\; \underbrace{-\,\kappa_{\mathrm{relax}} \cdot \bigl(T_{dir} - T_{dir}^{\mathrm{alg}}(t)\bigr)}_{\text{relaxation toward d/σ readability}} \;+\; \underbrace{\kappa_{r} \cdot r(t)}_{\text{conditional reorientation / reselection activity term}} \;-\; \underbrace{\kappa_{\mathrm{mask}} \cdot \Delta\Psi_f^{\mathrm{gap}}(t)}_{\text{actual-vs-felt friction gap}} \;-\; \underbrace{\kappa_{S} \cdot S_{str}(t)}_{\text{structural suffering opacifies direction}} \;+\; \underbrace{\kappa_{\mathrm{sup}} \cdot s_{ext}(t)}_{\text{healthy } L_2 \text{ scaffolding}} \;$}
$$

其中：

- `\kappa_{\mathrm{relax}}`：弛豫率；控制 T_dir 追上代数目标的速率
- `r(t)`：bearer-level consequence-sensitive reorientation / reselection activity proxy（P2/P3）。其非零可在特定模型中为 T_dir 提供正向活动项，但**不能**读作“系统由此证实 Selection 正在发生”；script / habit / automation 可与 Selection 共存
- `\Delta\Psi_f^{\mathrm{gap}}(t) := \Psi_{f,actual}(t) - \Psi_{f,felt}(t) \ge 0`：本体论摩擦的实支付-感知差，来自 `_SRT_PSI_F_CANONICAL.md §10` 与 `_SRT_T_DIR_CANONICAL.md §5–§6`
- `S_{str}(t)`：来自 §4.3；结构型苦难侵蚀方向可读性
- `s_{ext}(t)`：健康 `L_2` 外部支持率；可以**暂时**把 T_dir 抬起，但本身不改变 `T_dir^{\mathrm{alg}}`

**边界**（governance-canonical）：T_dir ∈ [0, 1] 由投影算子 `\Pi_{[0,1]}` 约束；具体形式留作 Open Pressure。

#### §3.5.2 与 `_SRT_T_DIR_CANONICAL.md` 的对齐

- `T_dir` 作为 v0 operational proxy / working canonical proxy 的地位**不改变**；本小节只把它的时间演化法则明文化
- `κ_{\mathrm{mask}} · \Delta\Psi_f^{\mathrm{gap}}` 项是该文件 §5–§6 “隐性债务”机制的 L1 方程化
- `κ_r r(t)` 在 RC-A 后只作为 P2/P3 reorientation/reselection activity augmentation；不得反向把 `r` 作为 Selection 条件
- 一次性释放对应本 ODE 外部的结构跳跃事件；本方程只刻画平滑期

#### §3.5.3 致命 `L_2` 的方程化判据

`_SRT_T_DIR_CANONICAL.md` “lethal `L_2`”条件可写为：

$$
\mathrm{lethal\;} L_2 \;\Longleftrightarrow\; \bigl(T_{dir}^{\mathrm{alg}} \text{ 持续高}\bigr) \;\wedge\; \bigl(\Delta\Psi_f^{\mathrm{gap}} \text{ 持续累积}\bigr) \;\wedge\; \bigl(\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}\bigr)
$$

第三个条件描述一种“可读性外观跟随代数目标快于债务显现”的候选机制。该判据属于当前 draft 模型，不证明 L2 automation 导致 Selection 消失。

#### §3.5.4 与主方程的兼容

T_dir 仍然是主方程的**导出投影候选**而非独立本体：

- 弛豫项把它系到 (d, σ) → 主方程 `\hat{G}_\theta[\sigma]` 与 `\nabla C_{L_2}` 的联合投影
- `\Delta\Psi_f^{\mathrm{gap}}` 来自主方程 `\nabla F` 项的实支付-感知分裂
- `S_{str}` 来自主方程收敛过程中失配登记
- `κ_r r(t)` 暂无独立 P1 投影证明，只是 P2/P3 augmentation

---

## §4. S 的最小动力学（苦难）

### §4.1 两型分解

`SRT_Suffering.md T-SUFF-2` 的两型写成加和：

$$
S \;=\; S_{sig} + S_{str}
$$

### §4.2 信号型动力学

$$
\boxed{\;\frac{dS_{sig}}{dt} \;=\; \underbrace{\mu_{\Delta}\cdot\dot{\Delta}_{avail}(t)}_{\text{new misalignment}} \;-\; \underbrace{\mu_\pi \cdot \pi(t) \cdot \mathbb{1}[d > d_c]}_{\text{payable channel open}} \;-\; \underbrace{\mu_r \cdot r(t)}_{\text{conditional reselection / reorientation activity}} \;-\; \underbrace{\mu_{sup} \cdot s_{ext}(t)}_{\text{healthy L_2 support}}\;}
$$

- `\dot{\Delta}_{avail}(t)`：“可打开结构”的新变化（环境扰动、θ 演化、`L_0` 残压上升）
- 指示函数 `\mathbb{1}[d > d_c]`：支付通道仅在非 B 期有效
- `r(t)`：P2/P3 activity proxy；只在该模型中承担缓解项
- `s_{ext}(t)`：来自健康 `L_2` 的外部支持率（不是替代，是降阻）

> **算子级 canonical（T-DELTA-1，2026-04-25 H7）**：本式中的 `\dot{\Delta}_{avail}` 不是抽象差函数。其算子级定义、三成分分解与可证伪算子空间假设见 `Core_Law/SRT_L1_Hardening_Notes.md §2 T-DELTA-1`。

### §4.3 结构型动力学

$$
\boxed{\;\frac{dS_{str}}{dt} \;=\; \underbrace{\nu_{block} \cdot \mathbb{1}[d \leq d_c]\cdot S_{sig}}_{\text{blocked signal turns structural}} \;+\; \underbrace{\nu_\sigma \cdot \max(0, \sigma - \sigma_{health})}_{\text{self-distortion channel}} \;-\; \underbrace{\nu_{trigger}\cdot D_{trigger}(t)}_{\text{decoupling trigger}} \;-\; \underbrace{\nu_\pi \cdot \pi(t)\cdot I_{window}(t)}_{\text{payment + open window}}\;}
$$

- `\mathbb{1}[d \leq d_c]·S_{sig}`：信号型在通道关闭时**转化为**结构型（关键非守恒项）
- `σ - σ_{health}` 正向激发扭曲型结构性苦难
- `D_{trigger}(t)`：四类解耦触发的总冲量
- 最后一项要求 `π(t)` 与 `I_{window}(t)` **同时**非零

> **算子级 canonical（T-IRR-3.5，2026-04-25 H4；ST-A source correction 2026-08-11）**：本式中的 `\nu_{block}` 采用条件性本地模型 `\nu_{block}(P, t) := \eta \cdot \varepsilon_{pg}(P, t) \cdot \kappa_{\Psi_f}(P, t)`，不是 former P1-T07 hierarchy 的构成性本地化。

### §4.4 T-SUFF-4 反最小化原则的方程语言

健康窗口 `[S_{min}, S_{max}]` 要求：

$$
S_{sig}^* \in [S_{min}, S_{max}] \;\wedge\; S_{str}^* \to 0
$$

但若外部机制强制 `S_{sig} → 0`，这不改变 `\dot{\Delta}_{avail}` 本身；新失配转而进入结构型通道。

$$
\boxed{\;S_{sig} \downarrow \text{ by suppression} \;\Longrightarrow\; S_{str} \uparrow \text{ under declared structural assumptions}\;}
$$

### §4.5 T-CHANNEL-1：通道指示函数族普适性（H9，2026-04-25）

> **Status**：本节把硬指示函数提升为有效通道指示族，并给出族内结构不变量。**Claim level: P1-candidate**。

定义 `\psi : \mathbb{R} \times \mathbb{R} \to [0, 1]` 为有效闭合通道指示，满足左饱和、右饱和、单调过渡与 `d_c` 平移性；对偶 `\bar\psi=1-\psi`。

T-CHANNEL-1 的主要用途是保证两型分裂、反最小化、单向吸收、T_dir 判据与投影分裂不依赖硬阈值的不可微性。其具体证明与历史形态保持原 H9 约束；RC-A 不改变这一部分。

---

## §5. 四变量耦合总方程

把 §2-§4（含 §3.5 T_dir 独立 ODE）合成一个四变量耦合系统：

$$
\begin{aligned}
\frac{d\sigma}{dt} &= \frac{1}{T}\Big[(1-\sigma)(\alpha w\phi(\sigma) - \lambda_{trace}T\sigma) - \sigma(\beta i - \lambda_{ext}T(1-\sigma))\Big] \\[4pt]
\frac{dd_c}{dt} &= \gamma_\rho \rho_{local} + \boldsymbol{\gamma_\sigma \max(0,\,\sigma - \sigma_{sub})} - \gamma_\pi \pi - \gamma_I I_{window} \\[4pt]
\frac{dT_{dir}}{dt} &= -\kappa_{\mathrm{relax}}\bigl(T_{dir} - T_{dir}^{\mathrm{alg}}(\sigma, d, d_c)\bigr) + \kappa_r r - \boldsymbol{\kappa_{\mathrm{mask}}\,\Delta\Psi_f^{\mathrm{gap}}} - \boldsymbol{\kappa_S\, S_{str}} + \kappa_{\mathrm{sup}} s_{ext} \\[4pt]
\frac{dS_{sig}}{dt} &= \mu_\Delta \dot{\Delta}_{avail} - \boldsymbol{\mu_\pi \pi\, \mathbb{1}[d > d_c]} - \mu_r r - \mu_{sup} s_{ext} \\[4pt]
\frac{dS_{str}}{dt} &= \boldsymbol{\nu_{block}\,\mathbb{1}[d \leq d_c]\,S_{sig}} + \boldsymbol{\nu_\sigma \max(0,\,\sigma - \sigma_{health})} - \nu_{trigger}D_{trigger} - \nu_\pi \pi\, I_{window}
\end{aligned}
$$

其中所有 `r` 项均受 RC-A qualification：只按 P2/P3 conditional activity term 读取。

### §5.1 关键耦合路径

1. **σ → d_c → S_{str}**：自指闭合推高遮蔽阈值，阻断支付通道，信号型苦难转结构型
2. **d_c ↑ → d_sig 被切断**：支付项通过指示函数变为零，系统进入 B 期动力学
3. **S_{sig} 被外部压制 → S_{str} ↑ 随 \dot{\Delta}_{avail}**：反最小化原则
4. **D_{trigger} → S_{str} ↓ 但需 I_{window} 同时打开**：解耦触发需要窗口协同
5. **T_dir 惯性 + ΔΨ_f^{gap} 扣除 → 致命 `L_2` 候选**：可读性读数可能滞后于真实 burden
6. **S_{str} → T_dir ↓ → r-proxy 下降 → S_{sig} 支付效率下降**：在本模型中，结构型苦难可压低 bearer-level reorientation/reselection activity，再减弱 `μ_r r` 通道。**不得**把这一回路改读成“r 下降说明 Selection 不再发生”。

### §5.2 病理吸引子

令相关导数为零时的非健康稳态：

$$
\mathcal{A}_{path} \;:\; \sigma \to 1,\; d_c \to d_{max},\; T_{dir} \to T_{dir}^{\mathrm{alg}} \text{ 但 } \Delta\Psi_f^{\mathrm{gap}} > 0 \text{ 累积}, \; S_{str} > 0 \text{ 定常}, \; S_{sig} \to 0
$$

这是 **B 期 + σ→1 + 外观无信号型痛苦 + 可读性被伪造维持** 的联合吸引子候选。其病理读法是 bearer-level reorientation/readback 与 generative health 受损，**不是**“不再发生 Selection”。

### §5.3 健康工作区

健康工作区 `\mathcal{H}`：

$$
\mathcal{H} \;:\; \sigma \in (\sigma_{sub}^\dagger \pm \delta),\; d > d_{narrow},\; T_{dir} \approx T_{dir}^{\mathrm{alg}} \text{ 且 } \Delta\Psi_f^{\mathrm{gap}} \to 0,\; S_{sig} \in [S_{min}, S_{max}],\; S_{str} \to 0
$$

`r(t)` 可以作为本模型中维持该工作区的 **P2/P3 generative-reselectability implementation proxy**，但不是健康的构成性定义，也不是 Selection 的必要条件。按 ST-A，这一工作区仍只是 generative reselectability 的实现候选。

模型可检验的较弱版本是：在声明环境、时间窗和其他变量后，较低的 bearer-level reorientation/reselection activity 是否与 T_dir、支付通道或 path concentration 的后续变化相关。不得再写：

```text
r(t) -> 0
-> no Selection
```

---

## §6. 与已有主方程的关系：T-PROJ-1 投影定理

> **Status (2026-04-25 H5)**：本节把“四变量系统是主方程的导出投影”写成带条件的 P1-candidate 构造。
> **RC-A qualification（2026-08-17）**：T-PROJ-1 的 P1-candidate standing 只覆盖可由现有上游与 C1-C4 支撑的投影骨架。`κ_r r(t)` / `μ_r r(t)` 没有 former P1-T05 之外的 P1 构成性来源，故这些源项仅按 P2/P3 conditional augmentation 读取；不能用它们完成 P1 promotion。

### §6.1 主方程与 L1 四变量的对接

`Core/SRT_Core_22_Equations.md` Eq-Evo-01 / Eq-Evo-03 主动力学（单 ISP，固定 P）：

$$
\frac{d\sigma_M}{dt} \;=\; \hat{G}_\theta[\sigma_M] \;-\; \nabla F[\sigma_M] \;-\; \lambda\cdot\nabla C_{L_2}[\sigma_M]
\qquad
\frac{d\theta}{dt} \;=\; \gamma\cdot A[\sigma_M, \mathrm{Target}] - \delta\cdot\partial_\theta\Phi(\theta) - k(\mathrm{Input}_{L_1} - \mathrm{Baseline})
$$

（本节为消除符号冲突把主方程态场写作 `\sigma_M`；本文件其它处的 σ 仍指自指率 `σ_{sr}`。）

### §6.2 投影算子的形式定义

设 P 为 stable ISP（满足 P1-T06）。定义四个标量泛函：

**`σ_{sr}` 投影**

$$
\mathcal{F}_\sigma(\sigma_M, \theta) \;:=\; \frac{\|\theta^{\mathrm{trace}}\|}{\|\theta^{\mathrm{trace}}\| + \|\theta^{\mathrm{ext}}\|}
$$

**`d_c` 投影**

$$
\mathcal{F}_d(\sigma_M, \theta) \;:=\; d_{\max} - \alpha_d \cdot \mathrm{tr}\bigl[\nabla^2 C_{L_2}[\sigma_M]\bigr]_{loc}^{-1}
$$

**`T_{dir}` 投影**

$$
\mathcal{F}_T(\sigma_M, \theta) \;:=\; \cos\angle\bigl(\hat{G}_\theta[\sigma_M],\;\nabla_{L_0}\mathrm{Order}[\sigma_M]\bigr) \cdot \mathbb{1}\bigl[\mathrm{Anchor}_{L_0}(P, t)\bigr]
$$

**`S` 投影**

$$
\mathcal{F}_S(\sigma_M, \theta) \;:=\; \|\hat{R}(\sigma_M, \theta)\|_{H_P}
$$

其中 `\hat{R}` 为声明的主方程剩余项。上述形式仍受各自 owner 的 claim 边界约束。

### §6.3 投影下的链式法则

对任意 P 上的足够光滑泛函 `\mathcal{F}_X(\sigma_M, \theta)`：

$$
\frac{d\mathcal{F}_X}{dt} \;=\; \langle\,\partial_{\sigma_M}\mathcal{F}_X,\; \dot\sigma_M\,\rangle + \langle\,\partial_\theta\mathcal{F}_X,\; \dot\theta\,\rangle
$$

### §6.4 闭包假设（Closure Assumptions）

四变量系统在投影下闭合需要四条结构性假设：

| 编号 | 假设 | 主方程层根据 |
|---|---|---|
| **C1** | 慢-快分离 | Eq-Evo-03 快-慢系统结构 |
| **C2** | `L_2` 写回的 Markov 闭包 | Eq-Bridge-L2-01 |
| **C3** | Stable-ISP 紧性 | P1-T06 |
| **C4** | 方向投影的可分性 | Eq-Bridge-IG-01 candidate geometry |

C1-C4 不是无代价假设；任一失效时，相应 ODE 降级。

### §6.5 T-PROJ-1：四变量系统的投影定理

**陈述（P1-candidate, RC-A qualified）**：在 stable ISP P 上，若闭包假设 C1-C4 成立，则**不含未独立奠基的 `r` augmentation 的投影骨架**可写为：

$$
\boxed{\;\frac{d\mathcal{F}_X}{dt}\bigg|_{\text{Eq-Evo}} \;=\; \mathrm{RHS}_{X,\,\text{grounded}} \;+\; O(\eta)\;}
$$

`κ_r r(t)` / `μ_r r(t)` 可以在 named model 中附加，但不计入当前 P1-candidate 的 constitutive derivation。

**逐项对应（RC-A 后）**：

| L1 ODE 源项 | 主方程来源 | 闭包条件 / hardness |
|---|---|---|
| `\sigma_{sr}` 写回项 | Eq-Evo 学习 / trace 投影 | C2 |
| `\sigma_{sr}` 衰减项 | friction / trace projection | C2 |
| `\sigma_{sr}` 外部驱动项 | input / baseline reaction | C1 |
| `d_c` 漂移项 `\gamma_\rho \rho_{local}` | `\nabla^2 C_{L_2}` 沿 path sedimentation | C3 |
| `d_c` 自指刚化项 | `\nabla^2 C_{L_2}` local stiffening | C2 + C3 |
| `T_{dir}` 弛豫项 | `(d,σ)` readability projection candidate | C4 |
| `T_{dir}` gap 扣除项 | `\nabla F` 中实-感分裂候选 | C4 |
| `T_{dir}` `+\kappa_r r(t)` | **无当前 P1 constitutive source** | **P2/P3 conditional augmentation** |
| `S_{sig}` `-\mu_r r(t)` | **无当前 P1 constitutive source** | **P2/P3 conditional augmentation** |
| `S_{sig}` 新失配项 | `\|\hat R\|` open-channel projection | C3 |
| `S_{str}` 阻塞转化项 | closed-channel projection + T-IRR-3.5 | C3 + conditional coefficient model |

**证明骨架**：

1. `σ_{sr}`、`d_c` 与 r-free `T_dir/S` 项继续按链式法则 + C1-C4 检查。
2. `κ_r r(t)` 与 `μ_r r(t)` 在 RC-A 后**从证明骨架中拿掉**：它们可以作为 named domain / bridge model 的经验增强项，但不能写成“former P1-T05 在 `\hat G_\theta` 的事件结构”的投影。
3. 若未来为 `r(t)` 建立独立的 P2/P3 operational definition 并取得 domain calibration，可以重新评估其模型价值；这不自动恢复 P1 地位。

### §6.6 T-PROJ-1 不证明的事项

1. 不证明具体系数数值
2. 不证明 χ 普适性超出当前有效族
3. 不证明 `\Delta\Psi_f^{gap}` 的完整算子层定义
4. 不证明 `r(t)` 是 Selection、agency 或 generative reselectability 的充分必要量
5. 不证明 `κ_r r` / `μ_r r` 是 P1 constitutive projection

### §6.7 T-PROJ-1 的结构性意义

RC-A 后，T-PROJ-1 的价值是把**已有可独立追溯的 L1 投影骨架**暴露出来联合审计，而不是用一个已经撤销的 Choice theorem 为所有项统一背书。

---

## §7. Open Pressures

本 draft_v0 状态下尚未封口：

1. **σ 符号冲突**：本文件 σ（自指率）与 `Core/SRT_Core_22_Equations.md` σ（主方程状态场）仍需最终命名空间清理
2. **`\dot{\Delta}_{avail}` 的正式化**：已有 H7 第一遍；更广 stable-ISP 域与实证窗口仍开
3. **χ 跳跃族**：已有 H8 第一遍；更广函数空间与 domain 对位仍开
4. **多主体扩展**：见 `Core_Law/SRT_Collective_Selection.md`，且其 RC-A 同步必须保持 Selection ≠ Agency
5. **阈值参数实证固定**：所有 threshold / coefficient 仍需 domain 声明
6. **与 FEP / predictive processing 的桥接**：保持 P3
7. **time-reversibility / T-IRR-3.5**：按 ST-A 条件模型读取
8. **T_dir 独立 ODE 的算子化**：`\Theta`、`\Delta\Psi_f^{gap}`、投影与系数窗口仍开放
9. **`r(t)` 的独立操作化（RC-A 新增 burn-down item）**：若继续使用，应把它定义为 bearer-level consequence-sensitive reorientation / reselection activity proxy，并给出与 ordinary adaptation / policy switching / script execution 的边界；在此之前不得再以 former P1-T05 充当上游，也不得把 `r=0` 当作 no Selection。

---

## §8. Cross-References

- 个体化 / σ 定义 / 三相结构 → `Core_Law/SRT_Individuation.md`
- 遮蔽动力学 / A/B 分期 / 四类干预窗口 / 四类解耦触发 → `Core_Law/SRT_Occlusion_Dynamics.md`
- 苦难 / 两型 / 四类分型 / 反最小化 → `Core_Law/SRT_Suffering.md`
- 主动力学 → `Core/SRT_Core_22_Equations.md`
- 路径层 `ρ` / 写回 / scaffold sedimentation → `Core/SRT_Core_12b_Ontology_L2.md`
- P1-T06 stable ISP → `Core/SRT_Core_21b_Constitutive_Theorems.md`
- RC-A Selection ≠ Agency → `03_Bridges/SRT_Agency_Automation_Guard_2026-08-17.md`
- former P1-T05 demotion provenance → `Operations/Audits/SRT_RC_A_P1_T05_DEMOTION_DERIVATIVE_SYNC_2026-08-17.md`
- ST-A generative reselectability → `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`
- P1-T02 ontological time → `Core/SRT_Core_21b_Constitutive_Theorems.md`
- d-value / T_dir / Ψ_f → 对应 canonical owners

---

## §9. 定位与使用规则

- **本文件做**：σ / d_c / T_dir / S 四变量的最小耦合动力学候选；病理吸引子与健康工作区的结构刻画；反最小化原则与可读性候选方程
- **本文件不做**：具体 domain 参数固定、临床量表、实验设计、AI 实现细节，也不定义 Selection/Agency
- **引用规则**：涉及方程级陈述时回链本文件；涉及概念定义时回链各自 owner
- **RC-A 使用规则**：任何 `r(t)`、`真实重选`、`选择时刻`措辞都只能按 bearer-level P2/P3 reorientation/reselection proxy 读取；script / habit / L2 automation 可以与 Selection 共存
- **不得**把本文件的方程读成已经过实证检验的定量定律——它是让 draft_v0 文件能够联合被批评、删除和修正的手段
