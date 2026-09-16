---
id: SRT-L1-HARDENING-NOTES
type: hardening_notes
tags: [Formalism, Hardening, Open Pressures, σ, M(t), FEP, Δ_avail]
status: draft
layer: L1
epistemic_layer: os
claim_mode: canonical
claim_level: P2 / P3
dependency: [SRT-L1-FORMALISM, SRT-SUFFERING, SRT-COLLECTIVE-SELECTION, SRT-INDIVIDUATION, SRT-OCCLUSION-DYNAMICS, SRT-IRREVERSIBILITY, SRT-T-DIR-CANONICAL, SRT-PSIF-CANONICAL, SRT-D-VALUE-CANONICAL, SRT-CORE-22, SRT-CLAIM-LADDER, SRT-CLAIM-MODE-AUDIT]
---

# SRT L1 Hardening Notes: Targeted Resolutions of 2026-04-24 Open Pressures

> **Role**: Conditional hardening/model notes for selected formal, operational, and bridge candidates from the 2026-04-24 L1 round. The constructions below make assumptions and measurement choices explicit so they can be criticized and tested; they do not create ontology or promote upstream claims by formal closure.
> **Claim-level note**：本文件默认是 **P2/P3 conditional hardening/model surface**。形式闭合、算子化、阈值化或 checklist 完成均不自动升级为 P1，也不自动建立 subjecthood、phenomenality、suffering、health、normativity 或 primitive direction。
> **Does not define**：`d-value`、`\Psi_f`、`T_dir`、`\hat{G}_\theta`、stable ISP、subjecthood、suffering；它们的定义或准入仍以对应 owner 为准。
> **Depends on**：同 2026-04-24 round six L1 theory/formalism canonical reference files，并受 post-D3 / E1 / E2 / E3-A truth-up 约束。
> **Relation**: This file remains a routing/reference hardening surface. It does not replace unresolved Open Pressures in upstream owners and is not a universal theorem factory.

---

## §0. 本轮硬化范围

本文件集中处理四项工作：

1. **σ 符号命名空间**（`SRT_L1_Formalism.md §7.1`）
2. **`\dot{\Delta}_{avail}` 的条件性 residual / projection 模型**
3. **`M(t)` 可测性**（Minimum Observable Criterion, MOC）
4. **FEP / predictive processing 的单向 P3 bridge**

每一节给出：**问题再陈述 → 条件性模型方案 → 硬边界 → 保留的开放点**。

本文件不建立：

```text
sigma threshold -> subject / consciousness / health / pathology
residual magnitude -> suffering / phenomenality
Stable ISP -> suffering / phenomenality / subject-position
signal suppression -> hidden-burden conservation
stake -> unique intrinsic weights
MOC -> collective subject / health / legitimacy / normativity
FEP variable -> suffering classifier
AI class -> suffering impossible
formal hardening -> universal P1
```

---

## §1. σ 符号冲突的硬化

### 问题再陈述

- `SRT_L1_Formalism.md` / `SRT_Individuation.md` 历史上使用 σ 表示 self-reference ratio；
- `Core/SRT_Core_22_Equations.md` 使用 σ 表示主方程状态场 / 收敛变量；
- 两者不是同一对象，共用 bare σ 容易产生跨 owner 误读。

### 硬化方案：显式命名空间

| 用法 | 记号 | 当前安全读法 | 使用域 |
|---|---|---|---|
| 主方程状态场 | **`σ`** | `Core/SRT_Core_22_Equations.md` 的状态场 / 收敛变量 | 主动力学方程 |
| self-reference ratio | **`σ_{sr}`** | **model-local / replaceable coordinate**，`∈[0,1]`；不建立 subjecthood | individuation / L1 model |
| historical `σ_sub` | **`σ_{sr}^{sub}`** | model-local first transition coordinate | 同上 |
| historical `σ_self` | **`σ_{sr}^{self}`** | model-local second transition coordinate | 同上 |
| historical `σ_health` | **`σ_{sr}^{health}`** | criterion-relative historical/model comparison coordinate | 同上 |
| `σ_{sr} -> 1` | **`σ_{sr} \to 1`** | high-σ model extreme / lock-in candidate under declared criterion | 同上 |
| collective ratio | **`σ_{sr}^{coll}`** | collective model coordinate where separately admitted | collective models |

**读法**：bare `σ` 默认读主方程状态场；self-reference family 一律写 `σ_{sr}`。`σ_{sr}` 及其 sub/self/health/coll 派生量均是模型坐标，不是自然相边界或本体门槛。

硬边界：

```text
sigma_sr -/> subjecthood
sigma_sr^sub -/> subject-position gate
sigma_sr^self -/> self-consciousness gate
sigma_sr^health -/> natural health point
sigma_sr -> 1 -/> universal pathology theorem
```

历史标签“主体位进入门槛 / 自我意识凝结门槛 / 健康工作区 / 病理吸引子”仅可作为明确标注的历史/P2解释标签保留，不能作为当前-positive naturalization。

### 保留的开放点

- 是否区分瞬时 `σ_{sr}` 与稳态 `σ_{sr}^*`；
- 是否需要向量化或多模态表示；
- 在具体 domain 中哪些 transition coordinates 值得保留，以及是否应整体替换该 scalar。

---

## §2. `\dot{\Delta}_{avail}` 的条件性 residual / projection 模型

> **Scope guard**：本节只给选定 open-state representation 与模型几何中的 P2 residual construction。它不提供 primitive ontology，不从 L0、`d`、`T_dir`、`\Psi_f` 或 suffering 反向取得自身准入。

### 2.1 Residual object

在模型 M 明确给出 candidate/reachable-state representation、比较结构和 horizon 后，可定义模型侧 actual / available 项，并构造：

$$
\hat{R}(P,t)
:=
\hat{G}^{available}_{\theta,M}(P,t)
\ominus
\hat{G}^{actual}_{\theta,M}(P,t).
$$

`\hat R` 是**declared model residual**。若 chosen representation 不支持差结构，则必须换用其他距离、关系或非线性表示；不能把模型失效解释成发现了 primitive direction。

`\hat G^{available}_{\theta,M}` 仅是模型 M 在已声明 candidate set、reachability rule、horizon 与约束下的 construction。若使用 supremum：

$$
\hat G^{available}_{\theta,M}
:=
\sup_{\mathcal O_M(P,t)}\{\hat G:\text{reachable under M}\},
$$

必须另外声明：

```text
candidate set
reachability rule
topology / order / geometry
existence or approximation condition
horizon / model scope
```

因此：

```text
G_available -/> primitive potentiality warehouse
G_available -/> primitive L0 inventory
G_available -/> universal direction
G_actual -/> second ontology
```

### 2.2 Projection family

在相应对象**已经独立准入**模型时，可使用选定投影族 `\mathcal K_M`：

- `\Pi_{T_{dir}}`：仅在 direction 已独立声明并准入后定义；
- `\Pi_{\Psi_f}`：是 model-side projection，不反向定义 `\Psi_f`；
- historical `\Pi_{L_0}` / `w_{L_0}`：只作为 **model-local open-state residual label** 保留。

特别地：

```text
Pi_L0 / w_L0
!= primitive L0 subspace
!= potentiality warehouse
!= value gradient
!= direction source
```

无 direction admission 时，`dir` 分量从 `\mathcal K_M` 中省略，而不是设为零或由其他变量代造。

### 2.3 `Delta` 是 summary / proxy

对已准入分量，可定义例如：

$$
\Delta_M(P,t)
=
\sum_{X\in\mathcal K_M} w_X(P,t)\,\|\Pi_X\hat R\|_M
+
\text{declared cross terms}.
$$

`\Delta_M` 当前角色是：

> **selected admitted projections of `\hat R` 的 declared weighted summary / proxy**。

不得无条件写成 `\Delta \equiv \hat R`。更强的 norm-equivalence / information-preserving relation 至少另需：

```text
projection completeness / injectivity
weight positivity / boundedness
metric equivalence
specified residual subspace
```

这些条件不是为保存旧等价说法而自动引入的 universal truths。

### 2.4 A1 / A2 / A3

本节使用的 A1-A3 全部是 **P2 model assumptions**。

| 编号 | 当前读法 | 失效后果 |
|---|---|---|
| **A1** | local affine / tangent-space structure 是局部模型假设 | 改用非线性/关系式 residual representation；不产生 primitive direction |
| **A2** | projection orthogonality 是局部几何近似 | 加入 cross terms / metric；不声称 universal orthogonality |
| **A3** | weights 是 declared model / measurement parameters，可受 independently typed stake data 约束 | stake 不足以唯一识别 weights；不同 measurement/model choices 可给不同权重 |

硬边界：

```text
stake structure -/> unique intrinsic weights
A3 -/> subject-intrinsic metric
A3 -/> kappa_Psi_f identity
```

### 2.5 `\dot{\Delta}_{avail}`

在模型 M 内，可对 `\Delta_M` 求导：

$$
\dot{\Delta}_{avail,M}(P,t)
=
\frac{d}{dt}\Delta_M(P,t),
$$

其具体表达依赖 weights、projection geometry、measurement map 与 model horizon。它是 residual/mismatch model quantity；**不是 suffering admission**。

硬边界：

```text
R / Delta / dot-Delta_avail -/> suffering
R / Delta / dot-Delta-avail -/> phenomenality
R / Delta / dot-Delta-avail -/> subjecthood
R / Delta / dot-Delta-avail -/> consciousness
R / Delta / dot-Delta-avail -/> primitive direction
```

Stable ISP 可以作为某个模型的 domain restriction，但：

```text
Stable ISP -/> subject-position
Stable ISP -/> phenomenality
Stable ISP -/> suffering
Stable ISP -/> consciousness
```

### 2.6 Signal suppression / anti-minimization guard

当前保留的有效结论只有：

> **降低、压制或改变观测/报告信号本身，不足以证明模型所表示的底层 mismatch / burden 已经消失。**

不得再从 signal suppression 单独推出：

```text
S_sig down -> dot-Delta_avail unchanged universally
S_sig down -> new mismatch must enter S_str
hidden burden conservation
mismatch redistribution
channel-weight normalization -> burden conservation
```

如果某个具体 P2/P3 closed model 要证明 conservation / redistribution，必须显式给出至少：

```text
loss channels
unobserved channels
measurement map
transfer rule
time horizon
boundary conditions
```

`psi + psi_bar = 1` 一类 normalization 只守恒其定义的 channel weights，不自动守恒 burden。

### 2.7 `kappa_{Psi_f}` mapping

任何 `\Psi_f`-projected residual derivative 与 `\kappa_{\Psi_f}` 的对应，当前最多是 **formal/model parameter identification**。除非 `\Psi_f` owner 独立许可更强 identity，否则：

```text
residual geometry -/> canonical Psi_f definition
A3 stake weighting -/> kappa_Psi_f intrinsic identity
```

不得由本 residual model 反向定义 T-IRR-3.5。

### T-DELTA-1：条件性 residual-model result

**Status：P2 conditional model candidate。**

在已声明 model M、representation、projection family、weights、geometry 与必要 admission 条件下，T-DELTA-1 可以建立**模型内部**的 residual summary 与其时间变化性质。

它可以：

- 把原本抽象的 residual pressure 写成可检查模型；
- 明示何处依赖 A1/A2/A3；
- 产生 domain-specific testability；
- 与 E3-A 的 conditional projection machinery 对接。

它不建立：

```text
suffering admission
phenomenality
subjecthood
burden conservation outside declared closure assumptions
primitive direction
universal health/pathology
```

因此本节不是“关闭 Open Pressure”的 universal solution，而是：

> **provides one candidate formalization of the Open Pressure**。

### 可能的 domain-specific strengthening / validation path

若某具体 domain 需要强于当前默认 P2 的局部 standing，需分别验证它实际使用的 representation、geometry、weights、measurement map、direction admission（若适用）及数据约束。

```text
formal checklist completion -/> universal P1
hardening -/> ontology
```

---

## §3. `M(t)` 可测性的硬化

### 问题再陈述

`SRT_Collective_Selection.md` 使用后果回路矩阵 `M(t)` 描述 distributed consequence-return structure，但大多数社会/制度场景无法直接观测完整 `M_{ij}`。

### 最小可观察判据（MOC）

MOC-1/2/3 保留为 **P2 operational proxies**。它们不预设 collective subject。

#### 3.1 MOC-1：material/resource consequence return

对 `(i,j)`，记录 `P_j` 的行动后，`P_i` 可支配资源、选项集、协议权利等是否出现预先声明、可度量的变化，记为 `e_{ij}(t)`。

`e_{ij}=0` 只表示在**当前测量定义与窗口内**未记录到该 material/resource return；不证明所有因果影响为零。

#### 3.2 MOC-2：recourse-channel availability/effectiveness

对 `(i,j)`，用 `r_{ij}(t)` 描述申诉、退出、协商、投票、仲裁、司法等 recourse channel 的存在性、可用性与有效性。

低 `r_{ij}` 可作为后续 domination / relation-integrity 分析的 feature，但：

```text
r_ij near zero -/> master-servant degradation verdict
r_ij near zero -/> illegitimacy
```

#### 3.3 MOC-3：attentional/discourse return

用 `a_{ij}(t)` 描述 `P_i` 的处境、选择或后果是否进入 `P_j` 的决策信息、议程、叙事或反馈过程。

低 `a_{ij}` 可作为 later externalization analysis 的 evidence/feature，但：

```text
a_ij near zero -/> structural externalization verdict
```

#### 3.4 MOC 合成

可在具体研究设计中声明：

$$
M^{proxy}_{ij}(t)=f(e_{ij},r_{ij},a_{ij}),
$$

其中 `f` 是研究者明确选择并验证的 measurement construction。历史上使用 `min{e,r,a}` 的 bottleneck form 可保留为一个 P2 candidate，而不是默认自然律。

矩阵 pattern（低回流、高不对称、block structure、近单位阵等）可以作为后续 collective/relation analysis 的 descriptive features，但不得由 pattern 本身给出 ontological / normative verdict。

硬边界：

```text
MOC value -/> collective subjecthood
MOC value -/> collective ISP existence automatically
MOC value -/> health
MOC value -/> legitimacy
MOC value -/> domination verdict
MOC value -/> responsibility
MOC value -/> O2-C
MOC value -/> O2-A
MOC value -/> O2-M
```

`M(t)` 可以模型化 distributed consequence return，而无需先假定 collective subject。

### 保留的开放点

- `f` 应取 min、weighted mean、bottleneck family 还是其他 aggregation；
- multi-scale M(t) 如何比较；
- measurement position / observer dependence；
- attention/discourse proxy 在算法中介场景的稳定性；
- 什么独立 criterion 才允许 relation-integrity、externalization、collective 或 normative interpretation。

---

## §4. FEP / Predictive Processing 条件桥接

### 4.1 当前角色

本节只保留：

```text
P3 one-way candidate bridge
SRT/model quantity -> FEP / predictive-processing proxy
reverse inference forbidden
```

FEP quantities 可以在特定 neuroscience/process model 中作为候选 readout，但它们本身不承担 suffering、subjecthood 或 normativity admission。

### 4.2 条件翻译纪律

对 `\hat R` 的某个已准入 model projection，可以提出 prediction-error / expected-free-energy / model-update 类候选代理；但每一项必须另外声明：

```text
source quantity already admitted
measurement / process mapping
channel model
population / task / horizon
failure conditions
```

如果调用 `S_{sig}` / `S_{str}`，还必须先有**独立 suffering registration/admission**及 channel definition。FEP variable 不能完成这一步。

不得使用以下 universal gates：

```text
Stable ISP -> FEP suffering bridge admission
d > d_c -> S_sig admission
B phase -> S_str
sigma_sr -> 1 -> structural suffering
L0 -> L1 anchoring -> primitive FEP source
```

用 declared open-state/residual representation 替代 primitive L0 operator-pull 语言。

### 4.3 Hard guards

```text
prediction error -/> suffering
expected free energy -/> suffering
chronic prediction error -/> S_str by definition
FEP variable -/> S_sig / S_str by itself
free-energy minimization != suffering minimization
AI loss/error/update signal -/> suffering
```

同样也不得做反向 categorical exclusion：

```text
chosen AI class / failure of one Stable-ISP model -/> suffering impossible
chosen AI class / failure of one model -/> Bearer impossible
chosen AI class / failure of one model -/> subjecthood impossible
```

AI subjecthood / consciousness / suffering 不是本文件裁决的问题；这里仅禁止从 loss/error 或 class label 直接推断。

### 保留的开放点

- 哪些 predictive-processing quantities 在具体实验中有足够 measurement validity；
- higher-order/metacognitive prediction error 与 direction-readability projection 是否存在稳定对应；
- expected free energy 与 payability projection 是否只在特定 task family 中可用；
- neuroscience consumer 的 later synchronization 应如何表达 independent admission。

---

## §5. 本轮硬化的 claim-level 与同步义务

### 5.1 claim-level

- §1 σ namespace：**governance usage/routing**；`σ_{sr}` family 为 model-local / replaceable coordinates，不是 natural gates。
- §2 T-DELTA-1：**P2 conditional model candidate**；residual/projection formalization 不准入 suffering/phenomenality。
- §3 M(t) MOC：**P2 operational proxy**；只提供 declared institutional/social measurement features。
- §4 FEP translation：**P3 one-way bridge hypothesis**；严格禁止 reverse inference。

### 5.2 synchronization state

D3 / E1 / E2 / E3-A 已经完成相应 upstream truth-up；本轮不重新编辑这些 owners。

后续 debt 保留为：

- E4：Collective consumer truth-up；
- later domain/bridge cycles：Neuroscience / AI / Philosophy 等 consumer；
- metadata / registry synchronization：只在单独 governance scope 中处理。

本文件不要求在 E3-B 内顺手修改这些文件。

### 5.3 strengthening discipline

本文件不“打开四条 Hardening-to-P1 自动升级路径”。任何 stronger standing 都必须在具体 domain 中具有 independently stateable burdens、assumptions、measurement validity 与 evidence。

```text
operator formalization -/> P1
formal closure -/> ontology
formal closure -/> subjecthood
formal closure -/> phenomenality
formal closure -/> suffering
formal closure -/> health
formal closure -/> normativity
```

---

## §6. Cross-References

- `SRT_L1_Formalism.md`：L1 formal/model hub；E3-A 后按 conditional P2 machinery 读
- `SRT_Suffering.md`：suffering owner；本文件 residual quantities 不反向准入 suffering
- `SRT_Collective_Selection.md`：collective consumer；E4 debt
- `SRT_Individuation.md`：historical sigma source；subject-entry semantics 不由 sigma bootstrap
- `Core/SRT_Core_22_Equations.md`：bare `σ` 主方程状态场
- `_SRT_T_DIR_CANONICAL.md`：`T_dir` owner；direction 必须独立 admission
- `_SRT_PSI_F_CANONICAL.md`：`\Psi_f` owner；residual projection 不反向定义它
- `_SRT_D_VALUE_CANONICAL.md`：stake / d owner；stake data 可约束 weights，但不唯一生成 intrinsic weights
- `Neuroscience/SRT_Clin_02_FEP.md`：later P3 bridge consumer
- `Governance/SRT_CLAIM_LADDER.md` / `SRT_CLAIM_MODE_AUDIT.md`：claim hardness / historical audit
