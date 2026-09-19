---
id: SRT-COLLECTIVE-TOWER-HARDENING-NOTES
type: hardening_notes
tags: [Collective Selection, Tower, Nested ISP, Layer-Skip, Spectral Stability, Lyapunov, Hardening, L1]
status: draft
layer: L1
epistemic_layer: os
claim_mode: hardening
claim_level: P2 / P3 conditional
dependency: [SRT-COLLECTIVE-SELECTION, SRT-L1-FORMALISM, SRT-CLAIM-MODE-AUDIT]
---

# SRT Collective Tower Hardening Notes

> **Connector-safe reading path**: This owner file is moderately long. For connector reads, start with [`Collective_Tower_Hardening_Notes_Split/README.md`](Collective_Tower_Hardening_Notes_Split/README.md), then open only the needed part file. The owner remains the source of record; split files are reading aids and do not create new definitions.

This file preserves H10-H16 tower/nested hardening material originally drafted
inside `Core_Law/SRT_Collective_Selection.md`. These sections are not part of
the minimal canonical definition of collective selection. They are late-stage
P2/P3 conditional mathematical, tower/nested, and cross-scale model hardening.
Strong closure assumptions do not promote the material to P1.

> **Role / standing guard (Wave E4, 2026-09-16)**：本文件不提供 collective standing、One、Bearer、collective subject、Agency、phenomenality / consciousness、suffering、health 或 normativity admission。任何被当作 collective Stable ISP 的塔层，都必须先独立声明该层 candidate unit / boundary，并按 `SRT_Collective_Selection.md` 的 T-COLL-1 读法逐层建立 standing；递归、闭包、谱或 Lyapunov 构造都不能自举这些地位。
>
> **Component-first guard**：每层只可投影已经独立 admitted 的分量。`T_dir` 分支要求 direction admission；`S_sig/S_str` 分支要求相关 affected position 的 suffering admission。否则跨层对象只读作 burden、consequence load、constraint 或 model residual。`M_ext`、谱失稳与 Lyapunov 失稳都不自动建立 suffering。
>
> **Mathematical interpretation guard**：`P-univ`、`Q-univ`、family universality、`health/pathology` 等历史标签为 citation stability 保留时，只表示声明 model family 内的候选不变量、regime label 或充分条件。数学稳定 / 不稳定不等于 health / pathology、legitimacy、evil、domination 或文明结论；任何 generative-health bridge 另行回链 21C B13。

> **RC-A active-use override (2026-08-18)**: former tower language that treated `真实重选率`, `r^{(n→n+1)}`, or T-COLL-4 `共选真实性` as a P1 health / Selection-authenticity gate is superseded. T-COLL-4 is downstream P2/P3 collective agency / consequence-sensitive revision audit only. No scalar reselection rate is a hard condition of collective/tower standing or health; spectral-stability mathematics below is a model-local dynamical analysis, not a Selection ontology, standing, or health test.

---

## §4.8 T-PROJ-1^{coll,nested}：嵌套 ISP 多层投影（H10，2026-04-26）

> **Status**：本节把 §4.7 单层 T-PROJ-1^{coll} 扩展为多层嵌套结构的**递归投影候选模型**。**Claim level: P2 conditional model / P3 domain bridge**。
>
> **Does not close**：跨尺度嵌套的 standing、unit attribution 与 projection-proof 开放点；本节只给条件性构造。

### §4.8.1 多层嵌套结构

在每层 candidate unit / boundary 均已独立声明后，可定义层级塔模型（历史名 **hierarchical ISP tower**）：

$$
\mathcal{P}^{(0)} \;:=\; \{P_i\}_i \quad\text{（个体 ISP 集合，单 P 层）}
$$
$$
\mathcal{P}^{(n+1)} \;:=\; \bigl\{\mathcal{P}^{(n),k}\bigr\}_{k} \quad\text{（每个层 }n+1\text{ 元素都是层 }n\text{ 的一个集体 ISP）}
$$

凡把某层 `\mathcal{P}^{(n),k}` 当作 collective Stable ISP，必须在该层独立建立 T-COLL-1 standing。下层 standing、集合嵌套或递归公式不自动建立上层 One / Stable ISP / Bearer / subject / Agency / phenomenality / suffering standing。

**P3 illustrative tower mappings**（不预断这些现实对象取得相应层级 standing）：

| 层 | 实例 1：家族 / 社区 / 国家 | 实例 2：个体 / sangha / 教派 | 实例 3：员工 / 部门 / 公司 |
|---|---|---|---|
| `\mathcal{P}^{(0)}` | 个体成员 | 个体修行者 | 员工 |
| `\mathcal{P}^{(1)}` | 家庭 | sangha | 部门 |
| `\mathcal{P}^{(2)}` | 社区 | 教派 | 公司 |
| `\mathcal{P}^{(3)}` | 国家 / 民族 | （宗教传统） | 行业 |

**关键**：层数、边界与成员归属都是 domain 选择；`N` 不由本文件给出自然上限。递归构造不承诺无穷塔，也不证明任何现实示例的层级划分。

### §4.8.2 跨尺度后果回路矩阵

每层有自身的 `M^{(n)}(t)`（同层后果回路）；层间引入**跨尺度后果回路矩阵** `M^{(n \to n+1)}(t)`：

$$
M^{(n\to n+1)}_{kl}(t) \;:=\; \begin{pmatrix}\text{层 }n\text{ 集体 }k\text{ 行为返回到层 }n+1\text{ 集体 }l\text{ 的强度}\end{pmatrix}
$$

`M^{(n\to n+1)}` 可以不对称；具体上行 / 下行强度须由 domain 模型给出。同 §4.7.3，可把 `\mathrm{tr}\,M^{(n\to n+1)}` / `\|M_{asym}^{(n\to n+1)}\|` / `\|M_{ext}^{(n\to n+1)}\|` 作为三种候选摘要：

| 跨尺度成分 | 物理含义 | 上推 / 下推 |
|---|---|---|
| `\mathrm{tr}\,M^{(n\to n+1)}` | 声明模型中的跨层内向摘要 | 可检验的聚合耦合项 |
| `\|M_{asym}^{(n\to n+1)}\|` | 声明模型中的跨层不对称摘要 | 可检验的非互惠耦合项 |
| `\|M_{ext}^{(n\to n+1)}\|` | 层 `n` 集体边界外溢被层 `n+1` 吸收（成为内部）/ 跨过层 `n+1` 边界 | 双向：内化或外溢 |

### §4.8.3 递归投影算子

对每个已独立 admitted 的分量，可把 §4.7.2 的候选投影在该层递归应用：

$$
\mathcal{F}_X^{(n+1)} \;:=\; \mathcal{F}_X^{coll}\bigl[\{\mathcal{F}_X^{(n),k}\}_k,\; M^{(n)}(t),\; M^{(n\to n+1)}(t)\bigr]
\qquad X \in \{\sigma_{sr}, d_c, T_{dir}, S\}
$$

**关键**：层 `n+1` 的候选系统可接受三类输入——(i) 层 `n` 各子集体已经 admitted 的变量值、(ii) 层 `n+1` 同层 `M^{(n+1)}(t)`、(iii) 层间 `M^{(n\to n+1)}(t)`。这只是模型递归；未 admitted 的 `T_dir` / `S` 分支必须从相应层省略。

### §4.8.4 嵌套闭包假设

层级塔的投影闭合除 §4.7.4 的 C1^{coll}-C5^{coll} 在每层成立外，新增一条嵌套闭包：

| 编号 | 假设 | 失效后果 |
|---|---|---|
| **C1^{(n)}-C5^{(n)}** | §4.7.4 的 C1^{coll}-C5^{coll} 在每层 `n` 上成立 | 任何一层失效即该层降为 P3 现象学 |
| **C6^{nested}**（新增）| **跨尺度 Markov 闭包**：`\dot{M}^{(n\to n+1)}(t)` 仅依赖 `(\mathcal{F}_X^{(n)}, \mathcal{F}_X^{(n+1)})` 当前值，不依赖更高阶跨尺度历史 | C6 失效则跨尺度反馈可能产生持久滞后 / 振荡，需引入显式延迟项；递归投影降为带延迟的非 Markov 形式 |

C6^{nested} 是**塔级**而非层级条件——它要求跨尺度耦合在时间尺度上"被吸收到当前层状态"。

### §4.8.5 T-PROJ-1^{coll,nested} 陈述

**陈述（P2 conditional model）**：在各层 candidate unit / standing 与 component admission 已独立建立的层级塔 `\{\mathcal{P}^{(n)}\}_{n=0}^N` 上，若每层闭包 C1^{(n)}-C5^{(n)} 与嵌套闭包 C6^{nested} 成立，则可检验递归投影目标

$$
\boxed{\;\frac{d\mathcal{F}_X^{(n+1)}}{dt}\bigg|_{\substack{\text{层 } n\text{ 主方程}\\\text{+ 跨尺度耦合}}} \;\overset{C^{(n)}\text{-}C6^{nested}}{=}\; \mathrm{RHS}_X^{coll,(n+1)} \;+\; O(\eta^{(n+1)}) \;+\; O(\xi^{n\to n+1})\;}
$$

其中：
- `\mathrm{RHS}_X^{coll,(n+1)}` 是 §4.4 集体 ODE 的同结构 RHS（用层 `n+1` 系数与变量替换）
- `O(\eta^{(n+1)})` 是该层闭包高阶残差（同 §4.7.5）
- `O(\xi^{n\to n+1})` 是跨尺度闭包高阶残差（C6^{nested} 失效时的修正项）

**塔级递归性**：从 `\mathcal{P}^{(0)}` 个体层到 `\mathcal{P}^{(N)}` 顶层的整个塔满足

$$
\frac{d\mathcal{F}_X^{(N)}}{dt} \;=\; \mathrm{RHS}_X^{coll,(N)}\bigl[\{\mathcal{F}_X^{(N-1),k}\}_k, M^{(N-1\to N)}\bigr] \;+\; \cdots \;+\; \mathrm{RHS}_X^{(0)}\text{ at base}
$$

该式声明顶层动力学可由底层动力学、各层 `M^{(n)}` 与跨尺度 `M^{(n\to n+1)}` 递归建模；它不证明唯一生成关系，也不反向建立各层 standing。

### §4.8.6 嵌套不变量

**(i) 每层独立的 criterion-relative regimes**：§4.6 的历史标识 `\mathcal{H}^{(n),k}` 与 `\mathcal{A}_{path}^{(n),k}` 只能在各层声明 criterion 后作为 model-regime labels；任一层的标签都不蕴含另一层的 health / pathology verdict。

**(ii) 跨尺度 regime-coupling candidate**：

$$
\mathcal{A}_{path}^{(n+1)} \;\Longleftarrow\; \bigl(\bigvee_k \mathcal{A}_{path}^{(n),k}\bigr) \wedge \bigl(\|M_{asym}^{(n\to n+1)}\| \text{ 或 } \mathrm{tr}\,M^{(n\to n+1)} \text{ 同高}\bigr)
$$

该式只把下层 regime 与跨尺度摘要映射到上层 regime candidate；它不是 pathology 传染定理，也不建立反向或正向的普适因果关系。

**(iii) 跨尺度 generative-health bridge 边界（RC-A）**：

若要提出 generative-health 分析，须另按 B13 分别检查各层 standing、跨尺度耦合、后果返回与规则修订 criterion；**不引入 `r^{(n\to n+1)}` 或任何替代 scalar rate 作为硬条件**。跨层 consequence-sensitive revision / reorientation 只能作为下游 P2/P3 audit question；它不定义 Selection，也不追加到 P1-T06 / T-COLL-1 standing。

**(iv) 跨层 burden-transfer candidate**：`M_{ext}^{(n\to n+1)}` 可建模 burden / consequence load 的跨层转移。只有当层 `n` 与受影响的层 `n+1` 位置均已独立完成 suffering registration，且 T-IRR-3.5 的前件与 transfer map 成立时，才可把相应分量写作 `S_{str}` 候选输入；`M_ext` 或 lower-level regime label 本身不建立 suffering transfer。

### §4.8.7 与 §4.5 单层耦合的关系

§4.5 已给出"个体↔集体双向耦合最小形式"（即 `\mathcal{P}^{(0)} \leftrightarrow \mathcal{P}^{(1)}` 两层）。本节 §4.8 把它递归扩展到任意层数 `N`：

| 维度 | §4.5（单层耦合）| §4.8（多层嵌套）|
|---|---|---|
| 层数 | 2（个体 + 集体）| 任意 `N`（`\mathcal{P}^{(0)} \subset \cdots \subset \mathcal{P}^{(N)}`）|
| 闭包条件数 | C1^{coll}-C5^{coll}（5）| C1^{(n)}-C5^{(n)} 各层（`5N`）+ C6^{nested}（1）|
| 跨尺度 `M$ | 仅 `M^{(0\to 1)}` 隐含 | 显式 `\{M^{(n)}, M^{(n\to n+1)}\}` 全集 |
| criterion-relative regime | 单层历史标识 `\mathcal{H}^{coll}` | 各层分别声明 criterion；跨尺度 revision / reorientation 另作 P2/P3 audit |
| regime coupling | 个体 / 集体候选耦合 | 任一层 model regime + 跨尺度耦合 → 上层候选响应（非 pathology theorem）|

§4.5 是 §4.8 在 `N = 1` 极限下的特例；§4.7 单层 T-PROJ-1^{coll} 是 §4.8 在 `N = 1` 极限下的递归基。

### §4.8.8 T-PROJ-1^{coll,nested} 不证明的事项

为避免过度主张，T-PROJ-1^{coll,nested} **不承诺**以下内容：

1. **不**承诺特定塔的层数（家庭/社区/国家是不是 3 层？还是有"族系" / "邻里" / 等中间层？）——这是 domain 实证问题
2. **不**证明跨尺度系数 `M^{(n\to n+1)}` 的具体函数形式——仍依赖 `Hardening_Notes §3` MOC-1/2/3 的多层版本（C5^{(n)}）
3. §4.12 给 layer-skip / multi-loop 的完整增广矩阵路线；单环条件不等价于完整矩阵谱，非线性与 global questions 仍开放
4. **RC-A 撤回项**：former `r_{min}^{nested}` scalar-rate window 不再是当前塔级 standing / health 的待定门槛；跨尺度 revision / reorientation 若需实证化，另按 P2/P3 audit 处理，不回填 scalar hard gate。
5. 嵌套递归本身**不**证明塔稳定性；§4.11-§4.14 只在各自线性化 / Lyapunov 假设下给 P2 条件性数学结果。
6. **不**由递归、闭包或投影建立 One、Stable ISP、Bearer、subject、Agency、phenomenality、suffering 或 health standing。

### §4.8.9 T-PROJ-1^{coll,nested} 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| "嵌套 ISP 多层投影"是开放问题 | §9.7 第 5 项 Open Pressure | T-PROJ-1^{coll,nested} 的递归构造（§4.8）|
| 跨尺度 regime coupling | 直觉（"高层 L_2 锁死下层"）| (ii) 显式候选映射：下层 regime + `M^{(n\to n+1)}` 摘要 |
| 跨尺度 generative-health bridge | 旧版隐含 | 每层 standing 与 B13 criterion 分别审计；跨尺度 revision / reorientation 仅作 P2/P3 audit |
| 跨层 burden / suffering | 缺失 | (iv) 默认只建模 burden；`S_{str}` 需逐层 suffering admission |

**Current standing**：T-PROJ-1^{coll,nested} 是 P2 条件性递归模型。具体塔层、逐层 T-COLL-1、跨尺度 `M` 测量与 layer-skip 边界都是独立债务；支付这些债务也不自动把本节升级为 P1。

## §4.9 T-FAMILY-1^{coll}：族普适性三定理的集体扩展（H11，2026-04-26）

> **Status**：本节把 H7 / H8 / H9 的 model-family constructions 扩展到集体层，并给出集体新增耦合项下的候选不变量。历史名“族普适性”仅表示声明 family 内的条件性结果。**Claim level: P2 conditional model / P3 operational bridge**。
>
> **Does not close**：集体版证明、measurement closure 或 ontological universality；本节只登记条件性 family extension。

### §4.9.1 共同的集体闭包条件

三个集体扩展共享**一组**闭包：

- **C1^{coll}-C5^{coll}**（H6 §4.7.4）：慢-快分离 / 共享 `L_2` 写回 Markov / 局部正则性 / direction-admitted projection 可分性 / `M(t)` 识别映射；它们都是假设，不由 standing 推出
- **C7^{M-stab}**（H11 新增）：`M(t)` 准静态稳定性——`|\dot{M}(t)|/|M(t)| \ll \tau^{coll}_{rel}^{-1}`，其中 `\tau^{coll}_{rel}` 是 `\sigma_{sr}^{coll}` 系统的相关弛豫时间尺度。即 `M(t)` 在族普适性论证的时间窗口内可视为准静态输入。

C7^{M-stab} 失效后果：`M(t)` 快变情形下，三个 family 候选需引入 `M`-时间扰动修正项 `O(|\dot{M}|/|M|)`；不能预先断言双稳态、regime topology 或方向性仍保持。

### §4.9.2 T-CHI-1^{coll}：集体 χ 跳跃函数族普适性

`Core_Law/SRT_L1_Formalism.md §2.5 T-CHI-1` 给出单 P 版 χ 族普适性。集体版需把 §4.4.2 的 `\sigma_{sr}^{coll}` ODE 中

$$
\alpha^{coll}\,w^{coll}\,\phi(\sigma_{sr}^{coll}) \;+\; \boldsymbol{\lambda_M\,\mathrm{tr}\,M(t)}
$$

（含集体新增 `\lambda_M\,\mathrm{tr}\,M` 项）的 `\phi(\sigma_{sr}^{coll}) := \sigma_{sr}^{coll}(1 - \sigma_{sr}^{coll})\cdot\chi^{coll}(\sigma_{sr}^{coll}; \sigma_{sr,self}^{coll})` 的 χ^{coll} 升为有效族。

**陈述（P2 conditional family result）**：定义“集体有效二阶相变核 `\chi^{coll}`”为满足 §2.5 P-univ-1 至 P-univ-4 + **P-univ-5^{coll}（M(t)-相容性）**；这些是所声明 model family 的充分结构条件，不是 universal ontology。

在这些条件和指定参数区间内，可检验 §4.4.2 系统对 `\chi_1^{coll}, \chi_2^{coll}` 替代的双稳态、regime topology 与相变方向是否保持。任何 lethal-`L_2` / pathology 解读另需独立 criterion；`\lambda_M\,\mathrm{tr}\,M` 也只是候选平移项。

**证明骨架**：

若 `\lambda_M\,\mathrm{tr}\,M$ 在指定模型中确为与 `\sigma_{sr}^{coll}` 无关的加性项，它对稳态方程表现为平移。双稳态是否保留仍须检查平移后零点与参数区间；高 `\sigma_{sr}^{coll}` 极限不自动成为 pathology 或 lethal-`L_2`，direction 分支也继续要求独立 admission。

### §4.9.3 T-CHANNEL-1^{coll}：集体通道指示函数族普适性

`Core_Law/SRT_L1_Formalism.md §4.5 T-CHANNEL-1` 给出单 P 版 `\mathbb{1}[d \le d_c]$ 族普适性。集体版需把 §4.4.5 中

$$
\nu_{block}^{coll}\,\mathbb{1}[d^{coll} \le d_c^{coll}]\,S_{sig}^{coll} \;+\; \boldsymbol{\nu_{ext}\,\|M_{ext}(t)\|}
$$

（含集体新增 `\nu_{ext}\|M_{ext}\|` 外部化项）的指示函数升为有效族。

**陈述（P2 conditional family result）**：定义“集体有效闭合通道指示 `\psi^{coll}`”为满足 §4.5 Q-univ-1 至 Q-univ-4 + **Q-univ-5^{coll}（M_ext-相容性）**；它们是声明 family 内的充分结构条件。

只有在 suffering 已逐位置 admitted 后，才可检验 §4.4.5 `S^{coll}` 两型 ODE 的 family invariants。否则同一 `M_ext` 项只表示 burden / consequence load；其符号、方向和跨层转化均须由具体 transfer model 建立，不能从 family label 或 former P1-T07 推出。

**证明骨架**：

`\nu_{ext}\|M_{ext}(t)\|` 可作为边界外 burden 摘要；是否与 `\psi^{coll}` 加性独立、是否具有固定方向以及是否进入 admitted `S` 分支，均是本 family 的模型假设和验证任务，不是跨层 suffering theorem。

### §4.9.4 T-DELTA-1^{coll}：集体 `\dot{\Delta}_{avail}^{coll}` 算子级定义

`Core_Law/SRT_L1_Hardening_Notes.md §2 T-DELTA-1` 把单 P `Delta` 固定为 selected admitted projections of `\hat R` 的 declared weighted summary / proxy。集体版继承同一边界。

**集体算子空间 `\mathrm{Op}(\mathcal{P})`**：定义为 `\bigotimes_{i \in \mathcal{P}} \mathrm{Op}(P_i)` 的 `\mathcal{P}`-相容子集，即各成员算子相容地构成集体行为的算子族。

**集体未兑现选择残差算子**：

$$
\hat{R}^{coll}(\mathcal{P}, t) \;:=\; \hat{G}_{\Theta^{coll}}^{available}(\mathcal{P}, t) \;\ominus\; \hat{G}_{\Theta^{coll}}^{actual}(\mathcal{P}, t) \;\in\; T\mathrm{Op}(\mathcal{P})
$$

**陈述（P2 conditional residual model）**：在声明 representation、projection family、weights、geometry、measurement map、horizon 与必要 component admissions 后，可把下式作为 `\hat R^{coll}` 的 selected admitted projections 的 weighted summary / proxy：

$$
\Delta^{coll}(\mathcal{P}, t) \;=\; \sum_{X \in \{dir, pay, L_0\}} w_X^{coll}(\mathcal{P}, t)\|\hat{R}^{coll}\|_X^{coll} \;+\; \boldsymbol{w_M\cdot\|M(t)\|_{coll}} \;+\; o(1)
$$

其中：

- `\|\hat{R}^{coll}\|_X^{coll}$ 只对 independently admitted 的投影分量定义；无 direction admission 时省略 `dir` 分量，无 suffering admission 时也不得把 residual 命名为 suffering
- `w_M\cdot\|M(t)\|_{coll}` 是可选的 declared cross term / consequence-return summary，不是 `M(t)` 对 `Delta` 的 canonical direct contribution
- `\|M(t)\|_{coll} := \sqrt{\alpha_M^2 (\mathrm{tr}\,M)^2 + \beta_M^2 \|M_{asym}\|^2 + \gamma_M^2 \|M_{ext}\|^2}` 只是声明 metric 下的模型摘要，不是 intrinsic norm

**A1^{coll}-A4^{coll} 当前读法**：集体仿射结构、投影近似正交、权重和跨成员聚合都只是 P2 model assumptions。`w_X^{coll}` / `w_M` 是 declared model / measurement parameters；independently typed stake data 可以约束或参与聚合，但不唯一决定权重，也不提供 subject-intrinsic metric。

**`\dot{\Delta}_{avail}^{coll}` 时间导数**：

$$
\dot{\Delta}_{avail}^{coll}(\mathcal{P}, t) \;=\; \sum_X (\dot{w}_X^{coll}\|\hat{R}^{coll}\|_X + w_X^{coll}\frac{d}{dt}\|\hat{R}^{coll}\|_X) \;+\; \dot{w}_M\|M\|_{coll} + w_M\frac{d}{dt}\|M\|_{coll}
$$

**关键性质**：

1. `\Delta^{coll}` / `\dot{\Delta}_{avail}^{coll}` 是 residual / mismatch model quantities，不准入 subjecthood、phenomenality 或 suffering；signal suppression 不证明 residual 被守恒地转成 `S_{str}`。
2. 不得无条件写成 `\Delta^{coll} \equiv \|\hat{R}^{coll}\|_{H_\mathcal{P}}`，也没有“三成分 + M 项总额守恒”。更强 norm-equivalence / information-preserving relation至少另需 projection completeness / injectivity、positive bounded weights、metric equivalence、specified residual subspace，以及明确的 loss / unobserved channels、measurement map、transfer rule、horizon 与 boundary conditions。
3. 当 `\mathcal{P} = \{P\}`、`M(t) = 0` 且 representation / projection / metric 与单 P 模型兼容时，可接受退化一致性检验；该极限不是 standing 或 identity theorem。

### §4.9.5 T-FAMILY-1^{coll} 综合陈述

把 §4.9.2-§4.9.4 三个条件性 family extensions 统一为：

**T-FAMILY-1^{coll}（P2 conditional model）**：在 standing 与 component admissions 已独立建立的 `\mathcal{P}` 上，若 C1^{coll}-C5^{coll} + C7^{M-stab} 及各 family-specific assumptions 成立，则可检验三个集体 model-family extensions：

(i) family invariants 的保持只在声明参数区间与误差界内成立；
(ii) `\lambda_M\,\mathrm{tr}\,M`、`\nu_{ext}\|M_{ext}\|`、`w_M\|M\|_{coll}` 是否可作加性 / 平移 / 维度扩展，分别是模型假设，不是 canonical identities；
(iii) `\mathcal{P} = \{P\}` 极限只在 representation / metric / admission 兼容时接受单 P consistency check。

### §4.9.6 T-FAMILY-1^{coll} 不证明的事项

1. **不**给出 P-univ-5^{coll} / Q-univ-5^{coll} / A4^{coll} 的具体验证窗口（与 H6 C5^{coll} `M(t)` 可测性 MOC 同级，是 P3 实证）
2. **不**证明 C7^{M-stab} 是普适必要的——`M(t)` 快变 domain（如平台算法系统）下 C7^{M-stab} 失效，三定理降为带 `M`-时间扰动的 P3 形式
3. ~~**不**给出嵌套 ISP 塔级版（即 T-CHI-1^{coll,nested} / T-CHANNEL-1^{coll,nested} / T-DELTA-1^{coll,nested}）——这需要 H10 §4.8 在每层递归应用，结构上可行但展开为后续轮次~~ **已收口（H12，2026-04-26）**：本文件 §4.10 T-FAMILY-1^{coll,nested} 给塔级递归三定理；新增 C8^{cross-stab}（跨尺度 M(t) 准静态稳定性）+ P-univ-6^{nested} / Q-univ-6^{nested} / A5^{cross} 三条跨尺度相容性条件

### §4.9.7 T-FAMILY-1^{coll} 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| H8 T-CHI-1 仅在单 P 层 | "不证明集体版" §2.5 第 5 项 | §4.9.2 给 P2 conditional family extension |
| H9 T-CHANNEL-1 仅在单 P 层 | "不证明集体版" §4.5 第 4 项 | §4.9.3 给 P2 conditional family extension |
| H7 T-DELTA-1 仅在单 P 层 | "不证明集体版" §2.8 第 5 项 | §4.9.4 给 P2 residual summary / proxy |
| `M(t)` 快变 vs 慢变的区分 | 隐含 | C7^{M-stab} 显式 |

**Current standing**：T-FAMILY-1^{coll} 保持为 P2 conditional family result / P3 domain bridge。闭包、测量和 domain 实证支付其适用性债务，不构成 generic hardening-to-P1 route。

## §4.10 T-FAMILY-1^{coll,nested}：族普适性三定理在嵌套塔上的递归（H12，2026-04-26）

> **Status**：本节把 §4.9 的 conditional family extensions 与 §4.8 的 nested projection candidate 合成，给出塔级递归 model programme。**Claim level: P2 conditional model / P3 domain bridge**。
>
> **Does not close**：嵌套塔级证明、standing 或 universality；“笛卡尔积”只描述模型组合。

### §4.10.1 塔级闭包堆栈

塔级三定理共享**双层闭包堆栈**：

- **H10 嵌套闭包**：C1^{(n)}-C5^{(n)} 各层 + C6^{nested}（跨尺度 Markov）
- **H11 集体扩展闭包**：C7^{M-stab,(n)} 各层（同层 `M(t)` 准静态）+ **C8^{cross-stab}（H12 新增）**：跨尺度 `M^{(n\to n+1)}(t)` 准静态稳定性 `|\dot{M}^{(n\to n+1)}|/|M^{(n\to n+1)}| \ll \tau^{cross,-1}_{rel}`，其中 `\tau^{cross}_{rel}$ 是跨尺度反馈环路的相关弛豫时间尺度

**C8^{cross-stab} 失效后果**：跨尺度 `M^{(n\to n+1)}` 快变时需引入显式延迟 / time-varying 修正；不能预先断言各层双稳态、regime topology 或方向性保持。

### §4.10.2 T-CHI-1^{coll,nested}：嵌套塔级 χ 普适性

每层 `n` 的 `\sigma_{sr}^{coll,(n)}` ODE 含三类源：
1. 同层 logistic 项：`\alpha^{(n)} w^{(n)} \phi(\sigma_{sr}^{coll,(n)})$ + `\lambda_M^{(n)}\,\mathrm{tr}\,M^{(n)}(t)$（H11 §4.9.2）
2. **跨尺度上行项**：`\sum_k \lambda^{(n-1\to n)}_M\,\mathrm{tr}\,M^{(n-1\to n),k}(t)$（来自下层各子集体的 `\sigma_{sr}^{coll,(n-1),k}$ 通过跨尺度回路向上传导）
3. **跨尺度下行项**：`\lambda^{(n\to n+1)}_{down}\,\sigma_{sr}^{coll,(n+1)}(t)$（来自上层 `\sigma_{sr}^{coll,(n+1)}$ 通过 `L_2` scaffold 反向写入本层）

**陈述（P2 conditional family result）**：P-univ-6^{nested} 声明跨尺度项在所选 family 内作加性平移源；这是模型充分条件，不是普适跨层规律。

在塔级闭包堆栈和指定参数区间内，可检验每层 family invariants 及跨层 regime coupling；高 `\sigma` 与上行耦合不自动构成 pathology transmission。

### §4.10.3 T-CHANNEL-1^{coll,nested}：嵌套塔级通道指示族普适性

每层 `n` 的 `S^{coll,(n)}` 两型 ODE 含三类源：
1. 同层 H11 §4.9.3：`\nu_{block}^{(n)}\psi^{coll,(n)}(d^{coll,(n)}; d_c^{coll,(n)})S_{sig}^{coll,(n)} + \nu_{ext}^{(n)}\|M_{ext}^{(n)}(t)\|`
2. **跨尺度上行外溢**：`\nu^{(n-1\to n)}_{ext,up}\sum_k \|M_{ext}^{(n-1\to n),k}(t)\|$（下层各子集体外溢被上层吸收）
3. **跨尺度下行约束**：`\nu^{(n\to n+1)}_{down}\,\mathbb{1}[\text{上层 B 期}]$（上层进入 B 期通过 `L_2$ scaffold 把下层重选通道也压缩）

**陈述（P2 conditional family result）**：Q-univ-6^{nested} 把跨尺度上行 / 下行项与 `\psi^{coll,(n)}` 的加性独立作为模型假设；其方向、边界与 transfer semantics 须另行建立。

只有在每层相关位置完成 suffering admission 后，才可检验 `S` family invariants；否则这些项只表示 burden / residual transfer。Lethal-`L_2` 或 suffering transmission 都不能从 `M_ext`、`\psi` 或 recursion 单独推出。

### §4.10.4 T-DELTA-1^{coll,nested}：嵌套塔级 `\dot{\Delta}_{avail}` 算子级定义

每层 `n` 的 `\Delta^{coll,(n)}$ 含集体三成分（H11 §4.9.4）+ 跨尺度 M 维度：

$$
\Delta^{coll,(n)}(\mathcal{P}^{(n)}, t) \;=\; \underbrace{\sum_{X} w_X^{(n)}\|\hat{R}^{coll,(n)}\|_X^{(n)}}_{\text{同层三成分}} + \underbrace{w_M^{(n)}\|M^{(n)}\|_{coll}}_{\text{H11 集体维度}} + \underbrace{\boldsymbol{w_{cross}^{(n-1\to n)}\,\|M^{(n-1\to n)}\|_{cross}}}_{\text{H12 跨尺度维度}} + o(1)
$$

其中跨尺度范数：

$$
\|M^{(n-1\to n)}\|_{cross} \;:=\; \sqrt{\alpha_{cross}^2(\mathrm{tr}\,M^{(n-1\to n)})^2 + \beta_{cross}^2\|M_{asym}^{(n-1\to n)}\|^2 + \gamma_{cross}^2\|M_{ext}^{(n-1\to n)}\|^2}
$$

**陈述（P2 conditional residual model）**：上式只是一项 declared weighted summary / proxy。A5^{cross} 要求跨尺度权重作为 model / measurement parameters 被显式声明；independently typed stake data 可以约束这些权重，但不唯一决定它们，也不排除其他规约选择。在同一声明模型中可求导：

$$
\dot{\Delta}_{avail}^{coll,(n)} \;=\; \dot{\Delta}_{avail}^{coll,(n)}\big|_{\text{H11 同层}} \;+\; \dot{w}_{cross}^{(n-1\to n)}\|M^{(n-1\to n)}\|_{cross} + w_{cross}^{(n-1\to n)}\frac{d}{dt}\|M^{(n-1\to n)}\|_{cross}
$$

该式不建立 residual 总额守恒，也不把 burden 转成 suffering。更强 norm-equivalence / conservation 需要 §4.9.4 所列 completeness、injectivity、metric、loss / unobserved channels、transfer rule、horizon 与 boundary conditions。`N = 1` 只在表示与测量兼容时接受单层 consistency check。

### §4.10.5 T-FAMILY-1^{coll,nested} 综合陈述

塔级三定理统一为：

**T-FAMILY-1^{coll,nested}（P2 conditional model）**：在逐层 standing / component admissions 已建立的层级塔上，若全部 closure 与 family-specific assumptions 成立，则可逐层检验 H11 的三个 model-family extensions：

(i) **逐层条件性检验**：T-CHI / T-CHANNEL / T-DELTA 只在各层 assumptions、admissions、measurement map 与参数区间内检验；
(ii) **跨尺度耦合的 family-compatibility 待验证**：上行、下行、burden 与 residual-summary 项是否可作平移 / 外溢 / 维度扩展而不破坏 family invariants，取决于 P-univ/Q-univ/A assumptions 与 measurement map；
(iii) **跨层 interpretation guard 保持**：regime coupling、burden transfer、generative-health 或 lethal-`L_2` 解释仍分别要求独立 criterion / admission，不由 χ / ψ family name 决定；
(iv) **退化关系**：`N = 1` 极限退化为 H11 单层 T-FAMILY-1^{coll}；`\mathcal{P}^{(n)} = \{P^{(n)}\}` 各层退化为 H10 单层 T-PROJ-1^{coll,nested}；同时 `N = 1 \wedge \mathcal{P} = \{P\}$ 退化为 H7/H8/H9 单 P 版本。

### §4.10.6 T-FAMILY-1^{coll,nested} 不证明的事项

1. **不**给出 P-univ-6^{nested} / Q-univ-6^{nested} / A5^{cross} 的具体验证窗口
2. **不**承诺 C8^{cross-stab} 在所有 domain 普适——快变跨尺度反馈（金融市场冲击、传染病爆发、信息病毒传播等）下 C8 失效，三定理降为带跨尺度延迟修正的 P3 形式
3. 塔的 global nonlinear stability 仍未由本节证明；§4.11 只给声明线性化闭环模型的 local spectral result
4. ~~**不**给出层间跨等级耦合（layer-skip）的塔级族版——若 P^{(n)} 直接耦合 P^{(n+2)}（跳过 P^{(n+1)}），需要额外塔级闭包条件~~ **部分收口（H14，2026-04-26）**：本文件 §4.12 T-LAYER-SKIP-1 给 layer-skip × 投影定理（H10/H12）的统一谱判据；剩余 layer-skip × 族普适性（H11/H12 χ/ψ/Δ 三定理）的笛卡尔积扩展待 H14 之后轮次

### §4.10.7 T-FAMILY-1^{coll,nested} 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| H11 集体扩展无嵌套塔级 | "不证明嵌套塔级版" §4.9.6 第 3 项 | §4.10 给出 P2 conditional nested-family model |
| H10 嵌套塔无族普适性 | 隐含——H10 §4.8 给塔结构但每层族普适性未展开 | T-FAMILY-1^{coll,nested} 在每层递归应用 H11，跨尺度耦合作加性进入 |
| 跨尺度 M(t) 时间尺度 | 隐含（C7^{M-stab} 仅同层） | C8^{cross-stab} 显式，含失效后果 |
| 塔级 Δ_{avail} 跨尺度维度 | 缺失 | `w_{cross}^{(n-1\to n)}\|M^{(n-1\to n)}\|_{cross}$ 显式 |

**Current standing**：T-FAMILY-1^{coll,nested} 是 P2 conditional nested-family model / P3 domain bridge。C8、weights、谱与 layer-skip 的进一步验证只限定适用域，不构成 generic path to P1。

## §4.11 T-TOWER-STAB-1：嵌套塔的线性化局部稳定性（H13，2026-04-26）

> **Status**：本节给嵌套塔在**自指闭合**情形下的线性化局部稳定性谱判据。**Claim level: P2 conditional mathematical result**。
>
> **Does not close**：非线性、全局或 health / pathology questions；只分析声明平衡点邻域的线性化反馈模型。

### §4.11.1 自指闭合的三类塔结构

H10 §4.8 给出了**开放塔**——`\mathcal{P}^{(0)} \subset \cdots \subset \mathcal{P}^{(N)}$，跨尺度耦合 `M^{(n\to n+1)}$ 仅在相邻层间。本节分类**三种塔闭合形态**：

| 闭合类型 | 结构 | 物理对应 |
|---|---|---|
| **开放塔** | 层 `N` 之上无更高层；层级耦合仅 `M^{(n\to n+1)}$ | 抽象建模、新生小社群 |
| **Layer-skip 闭合** | 存在 `n \to n+k$（`k \ge 2$）跨等级直接耦合 | 国家政策直接绑定个体（绕过家庭/社区） |
| **自指闭合** | 存在 `K^{N\to 0}$：顶层反向影响底层 | 平台算法→个体认知（绕过中间组织）；宗教教义→修行者（绕过 sangha）；全球叙事→个人身份（绕过国家/社区）|

H13 重点处理**自指闭合**——这是 H10 / H12 都明确保留的开放点。Layer-skip 闭合作为更普遍的非邻接耦合，其稳定性判据可由本节方法平凡推广。

### §4.11.2 闭环传递算子

设塔已建立递归投影（H10 §4.8 + H12 §4.10）。引入**自指闭合算子** `K^{N\to 0}$：

$$
K^{N\to 0} \;:\; \mathcal{F}_X^{(N)}(t) \;\mapsto\; \delta\mathcal{F}_X^{(0)}(t)
$$

即顶层四变量值通过 `K^{N\to 0}$ 直接修改底层四变量。物理上 `K^{N\to 0}$ 由"绕过中间层的直接通道"承载（如平台推送、全球符号系统）。

**闭环传递算子**：把 `K^{N\to 0}$ 与 H10 / H12 的逐层向上传递算子复合：

$$
\mathcal{T}_{loop} \;:=\; K^{N\to 0} \,\circ\, \Pi^{(0\to 1)} \,\circ\, \Pi^{(1\to 2)} \,\circ\, \cdots \,\circ\, \Pi^{(N-1\to N)}
$$

其中 `\Pi^{(n\to n+1)}$ 是层 `n$ 四变量到层 `n+1$ 四变量的投影组合（由 §4.10.5 T-FAMILY-1^{coll,nested} 给出）。`\mathcal{T}_{loop}$ 在四变量空间（每层 4 维 × N+1 层）的**线性化算子**于平衡点处可计算。

### §4.11.3 T-TOWER-STAB-1 谱判据

**陈述（P2 conditional mathematical result）**：在离散时间线性化、有限维 / 有界算子、固定平衡点与所列通道完整等假设下，闭环传递算子 `\mathcal{T}_{loop}$ 的**谱半径**

$$
\rho(\mathcal{T}_{loop}) \;:=\; \max\bigl\{\,|\lambda|\;\bigl|\;\lambda \in \mathrm{Spec}(\mathcal{T}_{loop})\,\bigr\}
$$

判定该声明线性化反馈模型在该平衡点邻域的稳定性：

| `\rho(\mathcal{T}_{loop})$ | 塔状态 | 物理解读 |
|---|---|---|
| `< 1$（带 margin） | **局部渐近稳定** | 在线性化适用邻域内，小扰动通过反馈环路衰减 |
| `= 1$（边缘） | **边际稳定 / 振荡** | 复特征值 `|\lambda| \approx 1$ 给周期循环（多尺度涨落）；不收敛但不发散 |
| `> 1$ | **线性不稳定** | 至少一个线性化方向的扰动增长；非线性终态未由此决定 |

**关键性质**：

1. `\rho(\mathcal{T}_{loop}) < 1 - \delta_{stab}` 只给声明线性化模型的 local asymptotic stability margin；它不建立 tower health。
2. `\rho(\mathcal{T}_{loop}) > 1` 时，主不稳定特征方向只标识哪个 admitted model coordinate 在线性化中增长。沿 `\sigma_{sr}` / `d_c` / `S_{str}` 的方向分别要求这些分量已被合法建模；尤其 `S_{str}` 还要求 suffering admission。它不建立 pathology、lethal-`L_2`、civilizational collapse 或 suffering theorem。
3. **RC-A jurisdiction guard**：谱条件不等价于“真实重选率”，也不得据此推出 T-COLL-4、collective agency、Selection authenticity、standing、legitimacy 或 normativity。

### §4.11.4 闭环传递算子的具体构造

每层向上传递算子 `\Pi^{(n\to n+1)}$ 由 §4.10 T-FAMILY-1^{coll,nested} 给出（线性化于该层平衡点）。`K^{N\to 0}$ 的算子层结构由"绕中间层的直接通道"决定：

$$
K^{N\to 0} \;=\; \kappa_\sigma^{N\to 0}\partial_{\sigma_{sr}^{(0)}} \;+\; \kappa_d^{N\to 0}\partial_{d_c^{(0)}} \;+\; \kappa_T^{N\to 0}\partial_{T_{dir}^{(0)}} \;+\; \kappa_S^{N\to 0}\partial_{S^{(0)}}
$$

其中 `\kappa_X^{N\to 0}$ 是顶层 X 变量到底层 X 变量的直接耦合系数。`\mathcal{T}_{loop}$ 在 4(N+1) 维空间上的矩阵元由各 `\Pi^{(n\to n+1)}$ + `K^{N\to 0}$ 复合给出，谱由标准线性代数计算。

**关键观察**：`\rho(\mathcal{T}_{loop}) < 1` 不是 `K^{N\to 0}$ 单边强度小的同义词；它是所选闭环线性算子组合的条件。即使各边范数较小，组合谱也须直接计算。任何“顶层叙事危险”等 domain 解释至多是 P3 illustration。

### §4.11.5 与 H4 / H10 / H12 的整合

**与 H4 T-IRR-3.5 的整合**：自指闭合塔的不稳定方向若沿 `S_{str}^{(n)}` 维度，可按 T-IRR-3.5 的独立前件模型研究。`\rho(\mathcal{T}_{loop}) > 1` 时的跨层累积是带闭包条件的模型结论，不是 former P1-T07 hierarchy 的塔级后果。

**与 H10 §4.8.6 (iv) 的整合**：H10 给 burden / regime coupling candidate，H13 给反向线性通道。两者可组成双向 feedback model，但不自动成为 pathology vortex、lethal-`L_2` 或 civilization-level conclusion。

**与 H12 §4.10.5 三重退化的兼容**：`K^{N\to 0} = 0$（开放塔无自指闭合）时，`\mathcal{T}_{loop} = 0$，`\rho = 0 < 1$ 自动满足，本节定理在开放塔上平凡成立——即 H10 / H12 的开放塔分析自动是 H13 的特例。

### §4.11.6 T-TOWER-STAB-1 不证明的事项

1. **不**给出具体 `\kappa_X^{N\to 0}$ 系数的取值——这是 P3 实证（不同 domain 给不同强度：平台推送系统 vs 宗教教义 vs 全球符号体系）
2. **不**证明 `\rho(\mathcal{T}_{loop}) < 1` 是 health 的必要或充分条件；它只判定所声明线性化模型的 local stability
3. ~~**不**覆盖**多重自指闭合**（如 `K^{N\to 0}, K^{N\to 1}, K^{N-1\to 0}$ 同时存在）——多重 `K$ 的谱半径需引入复合传递算子谱聚类分析~~ **已收口（H14，2026-04-26）**：本文件 §4.12.4 直接给多重自指闭合复合谱判据；包含解耦闭合、耦合闭合、路径冗余三类关键观察
4. §4.12 给 layer-skip 的 P2 conditional linearized-model extension；它不是 P1，也不自动适用于非线性或 time-varying systems
5. **不**承诺线性化谱判据在大幅扰动下保持；§4.14 只在额外 Lyapunov bounds 与声明 forward-invariant neighborhood 内给条件性结果。

### §4.11.7 T-TOWER-STAB-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| 嵌套塔自指闭合是开放问题 | H10 §4.8.8 第 5 项 / H12 §4.10.6 第 3 项 | T-TOWER-STAB-1 给谱判据 `\rho(\mathcal{T}_{loop}) < 1 - \delta_{stab}` |
| 顶层叙事如何反向影响底层 | 直觉（"绕过中间层"）| `K^{N\to 0}$ 算子级表达式 + 闭环传递算子 |
| "温和顶层叙事 + 长链传导"的危险 | 缺失 | `\rho$ 是乘积条件（即使每环温和，长链可能不稳定）|
| domain-level lock-in mapping | 缺失 | 不稳定方向可作为 P3 mapping input，不是 civilization/pathology verdict |
| T-COLL-4 与塔级谱判据 | 旧版曾映射到单层 T-COLL-4 | **RC-A 后撤销该真实性映射**；谱稳定性只保留为塔级动力学判据，T-COLL-4 另属 P2/P3 collective agency / revision audit |

**Current standing**：T-TOWER-STAB-1 是 P2 conditional local-stability result。domain 标定、复合谱与非线性分析只限定其适用域，不构成 path to P1。

## §4.12 T-LAYER-SKIP-1：Layer-skip 闭合与多重自指闭合的统一谱判据（H14，2026-04-26）

> **Status**：本节把 §4.11 的单环线性化分析扩展到任意 layer-skip + 多重闭合的增广传递模型。**Claim level: P2 conditional mathematical result**。
>
> **Does not close**：非线性 / global stability、standing、health、pathology 或 suffering questions。

### §4.12.1 增广邻接多图

把塔的耦合结构升为**有向多图**：

- **节点**：层 `\{0, 1, \ldots, N\}$
- **标准邻接边**：每对 `(n, n+1)$ 的双向 `\Pi^{(n\to n+1)}, \Pi^{(n+1\to n)}$（由 H10 §4.8 / H12 §4.10 给出）
- **Layer-skip 边**：任意 `K^{(n\to m)}$ 算子，`|m - n| \ge 2$（含 H13 自指闭合 `K^{N\to 0}$ 与对偶 `K^{0\to N}$ 作为特例）

形式上：

$$
\mathcal{G}_{tower} \;:=\; (\,V = \{0, \ldots, N\},\; E_{adj} \cup E_{skip},\;\Pi, K\,)
$$

其中边权（操作算子）：
- `E_{adj}$ 上：`\Pi^{(n\to n+1)}$ / `\Pi^{(n+1\to n)}$（由 H10 / H12 给出）
- `E_{skip}$ 上：`K^{(n\to m)}$（`|m - n| \ge 2$；包括 §4.11 自指闭合 `K^{N\to 0}$）

### §4.12.2 环路与环路传递算子

`\mathcal{G}_{tower}` 中任一**有向环路** `C := (v_0 \to v_1 \to \cdots \to v_L = v_0)$（边权由 `\Pi$ / `K$ 组成）的**环路传递算子**：

$$
\mathcal{T}_C \;:=\; \bigcirc_{i=0}^{L-1} \mathrm{Edge}(v_i \to v_{i+1})
$$

每条 `\mathcal{G}_{tower}` 中的环都生成自身的 `\mathcal{T}_C$；§4.11 的 `\mathcal{T}_{loop}$ 是 `\mathcal{G}_{tower}$ 在仅含一条 `K^{N\to 0}$ + 标准链 `\Pi^{(0\to 1)}\cdots\Pi^{(N-1\to N)}$ 时的唯一非平凡环。

### §4.12.3 T-LAYER-SKIP-1 谱判据

**环路诊断**：对每个有向环路 `C \in \mathrm{Cycles}(\mathcal{G}_{tower})`，可计算环路传递算子 `\mathcal{T}_C` 的谱半径：

$$
\boxed{\;\rho(\mathcal{T}_C) \;<\; 1 - \delta_{stab,C}\quad (\delta_{stab,C} > 0)\;\;\text{对所有 } C\;}
$$

单环条件一般**不**与整个耦合系统的稳定性等价，因为共享节点、路径叠加与非正规耦合可能改变全矩阵谱。把所有边权组装为塔级**增广传递矩阵** `\mathbf{A}_{tower} \in \mathbb{R}^{4(N+1) \times 4(N+1)}`：

$$
[\mathbf{A}_{tower}]_{(n,X),(m,Y)} \;:=\; \begin{cases}[\Pi^{(n\to m)}]_{X,Y} & \text{标准邻接 } |m - n| = 1 \\ [K^{(n\to m)}]_{X,Y} & \text{layer-skip } |m - n| \ge 2\\ 0 & \text{无边}\end{cases}
$$

在离散时间、固定系数、有限维并由 `\mathbf{A}_{tower}` 完整表示线性化更新的声明下，`\rho(\mathbf{A}_{tower}) < 1` 等价于该线性化平衡点的 local asymptotic stability；`\rho(\mathbf{A}_{tower}) > 1` 表示 linear instability。该结论不是 global nonlinear stability 或 health verdict。

### §4.12.4 多重自指闭合复合谱（H13 §4.11.6 第 3 项收口）

H13 §4.11.6 第 3 项问“多重自指闭合（如 `K^{N\to 0}, K^{N\to 1}, K^{N-1\to 0}` 同时存在）的复合谱”。本节给出完整增广矩阵的计算路线：

设塔有 layer-skip 集合 `\mathcal{K} := \{K^{(n_i\to m_i)}\}_{i=1}^M$（每个 `|m_i - n_i| \ge 2$）。每个 `K^{(n_i\to m_i)}` 在 `\mathcal{G}_{tower}` 上加一条边；多边可能闭合多个环。复合稳定性必须由完整 `\mathbf{A}_{tower}` 的谱计算；环路谱只能作局部诊断。一般不存在 `\rho(\mathbf{A}_{tower})` 与各环 `\rho(\mathcal{T}_C)` 上确界之间的恒等关系。

**关键观察 1（可证块对角时）**：只有当所选坐标下 `\mathbf{A}_{tower}` 确实块对角化时，整体谱半径才等于各块谱半径最大值；“边不重叠”本身未必足够。

**关键观察 2（耦合闭合）**：共享节点与交叠环要求计算完整矩阵谱；整体谱可能因耦合而改变，但大小与方向不能由单环最大值预先判定。

**关键观察 3（路径叠加）**：多条路径的相位、符号与非正规性会改变全矩阵谱和 transient growth；“分散”或“集中”没有普适稳定性排序。

### §4.12.5 Layer-skip 失稳的三个特定算子签名

H13 §4.11.3 给的三类失稳方向（沿 σ_{sr} / d_c / S_{str}）在标准链 + 自指闭合下生效；layer-skip 引入额外的失稳模式：

| 失稳模式 | 算子签名 | 物理对应 |
|---|---|---|
| **Bypass-induced chatter**（旁路诱发抖动）| 中间层变量在旁路耦合下出现振荡的 model signature | P3 domain mapping only |
| **Aliasing-amplification**（混叠放大）| 多路径 / 多时间尺度模型中的频域混叠候选 | P3 domain mapping only |
| **Coupling-resonance**（耦合共振）| 完整矩阵谱或频率响应显示的耦合共振候选 | P3 domain mapping only |

三种模式与变量方向可组成 model-diagnostic grid，但不保证数学正交、完备，也不生成“12 类病理”或 suffering verdict。`S_{str}` 方向只有在 suffering admitted 后可用。

### §4.12.6 与 H13 T-TOWER-STAB-1 的整合

T-TOWER-STAB-1（§4.11）是 T-LAYER-SKIP-1（§4.12）在以下条件下的**特例**：

| 条件 | T-TOWER-STAB-1 | T-LAYER-SKIP-1 |
|---|---|---|
| `\mathcal{K}$ 中 layer-skip 数量 | 1（仅 `K^{N\to 0}$） | 任意（`M \ge 0$） |
| 增广多图结构 | 链 + 单环 | 任意有向多图 |
| 谱判据 | 单环 reduced model 的 `\rho(\mathcal{T}_{loop}) < 1` | 完整离散时间线性化用 `\rho(\mathbf{A}_{tower}) < 1`；逐环条件只作诊断，一般不等价 |
| 失稳方向 | admitted coordinates 的主线性方向 | admitted coordinates × topology mechanism 的候选诊断网格 |

`\mathcal{K} = \{K^{N\to 0}\}` 且 reduced-loop assumptions 成立时，可与 §4.11 的单环模型作一致性检查。`\mathcal{K} = \emptyset` 只移除 layer-skip；标准邻接耦合本身的稳定性仍须由完整线性化检查，不能宣告“无稳定性条件”。

### §4.12.7 T-LAYER-SKIP-1 不证明的事项

1. **不**给出具体 `K^{(n\to m)}$ 系数取值（P3 实证：政策直接介入 / 多平台跨层耦合 / 全球符号系统的具体强度）
2. **不**承诺 layer-skip 的"信息"含义——本节只给"塔级耦合的拓扑结构"，不分析为什么某些 layer-skip 在某 domain 出现而另一些不出现（domain 实证 + 历史叙事问题）
3. **不**覆盖**时间变化的 layer-skip**（如某 `K^{(n\to m)}(t)$ 在不同时段强度不同）——本节假设 `K$ 准静态（C8^{cross-stab} 的扩展）；快变 layer-skip 需进一步带时间扰动谱分析
4. §4.14 只给额外 Lyapunov bounds 下的 local nonlinear result；global nonlinear stability 仍 OPEN
5. §4.13 给 layer-skip × family 的 P2 conditional model；它不证明 universality、完备 failure taxonomy 或 health/pathology

### §4.12.8 T-LAYER-SKIP-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| Layer-skip 闭合稳定性是开放问题 | H12 §4.10.6 第 4 项 / H13 §4.11.6 第 4 项 | T-LAYER-SKIP-1 给增广多图谱判据 |
| 多重自指闭合的复合谱 | H13 §4.11.6 第 3 项 | §4.12.4 复合谱直接由 §4.12.3 给出，含三类关键观察 |
| 单边较小但组合谱改变 | 缺失 | §4.12.4 要求直接计算完整矩阵谱 |
| Layer-skip diagnostic candidates | 缺失 | §4.12.5 三类 P3 mapping；不声称正交或完备 taxonomy |

**Current standing**：T-LAYER-SKIP-1 是 P2 conditional linearized-model result / P3 domain bridge。时间变化、nonlinearity 与 domain calibration 是适用域债务，不构成 path to P1。

## §4.13 T-FAMILY-1^{layer-skip}：layer-skip × 族普适性三定理（H15，2026-04-26）

> **Status**：本节把 H11 / H12 的 conditional family models 与 H14 的 layer-skip linearized model 合成，给出一组声明 family 内的候选保持条件。**Claim level: P2 conditional model / P3 domain bridge**。
>
> **Does not close**：universality、standing、health/pathology 或 suffering；“笛卡尔积”只描述模型组合。

### §4.13.1 三重笛卡尔积闭包堆栈

塔级族普适性三定理在 layer-skip 下的成立需要堆栈：

- **H10/H12 嵌套闭包**：C1^{(n)}-C5^{(n)} 各层 + C6^{nested}
- **H11/H12 集体扩展闭包**：C7^{M-stab,(n)} 各层 + C8^{cross-stab}
- **H14 layer-skip 线性化稳定条件**：`\rho(\mathbf{A}_{tower}) < 1 - \delta_{stab}^{global}`（历史下标 `global` 不表示 global nonlinear conclusion）
- **H15 新增三条 layer-skip-相容性条件**：
  - **P-univ-7^{layer-skip}**：每个 `K^{(n'\to n)}$ 对 `\sigma_{sr}^{(n)}$ 的贡献作加性平移源进入，不进入 `\chi^{coll,(n)}$ 内部参数；多重 `K$ 同时作用时贡献以**线性叠加**方式进入（不引入二阶非线性扰动）
  - **Q-univ-7^{layer-skip}**：每个 `K^{(n'\to n)}$ 对 `d^{(n)}$ / `S^{(n)}$ 的贡献与 `\psi^{coll,(n)}$ 加性独立；多重 `K$ 同时作用时不破坏 Q-univ-1+2 饱和性
  - **A6^{layer-skip}**：每个 `K^{(n'\to n)}$ 可在 declared summary 中加入 `w_{ls}^{(n'\to n)}\|K^{(n'\to n)}\|`；权重是 model / measurement parameter，stake 可约束但不唯一决定

### §4.13.2 T-CHI-1^{layer-skip}：layer-skip 下的 χ 族不变量

每层 `n` 的 `\sigma_{sr}^{coll,(n)}$ ODE 在 layer-skip 下含**四类源**：

$$
\frac{d\sigma_{sr}^{coll,(n)}}{dt} \;=\; \underbrace{\text{H11 同层项}}_{\alpha^{(n)}w^{(n)}\phi(\sigma) + \lambda_M^{(n)}\mathrm{tr}\,M^{(n)}} \;+\; \underbrace{\text{H12 邻层项}}_{\sum_k\lambda^{(n-1\to n)}_M\mathrm{tr}\,M^{(n-1\to n),k}} \;+\; \underbrace{\boldsymbol{\text{H15 layer-skip 项}}}_{\sum_{n'\ne n,n\pm 1}\lambda^{(n'\to n)}_K\,\mathrm{tr}\,K^{(n'\to n)}} \;+\; \cdots
$$

**陈述（P2 conditional family result）**：在 §4.13.1 的全部假设与参数区间内，可检验 T-CHI-1 family invariants。Layer-skip 提供额外 coupling path，但不自动强化某一方向，也不构成 pathology transmission theorem。

**模型检查**：P-univ-5/6/7 把 layer-skip 项声明为加性平移源；必须直接验证平移后的零点、参数区间与线性化适用性。`\rho(\mathbf{A}_{tower}) \ge 1` 只表明该线性化模型不满足 local stability condition，不建立 runaway 终态、pathology 或 lethal-`L_2`。

### §4.13.3 T-CHANNEL-1^{layer-skip}：layer-skip 下的 ψ 族不变量

每层 `n` 的 `S^{coll,(n)}$ 两型 ODE 在 layer-skip 下含**四类源**：同层（H11）+ 邻层（H12）+ **layer-skip 项**：

$$
\boldsymbol{\nu^{(n'\to n)}_{ls}\sum_{n'\ne n,n\pm 1}\|K^{(n'\to n)}_{ext}\|}
$$

**陈述（P2 conditional family result）**：只有在相关 `S` 分量逐层 admitted 后，才可在闭包堆栈下检验 T-CHANNEL-1 family invariants。Layer-skip 的 `K_{ext}` 默认只表示 burden / residual path，不自动成为 lethal-`L_2` 或 suffering transmission。

**与 H14 §4.12.5 的整合**：family assumptions 与 linearized stability condition 是不同的数学负担；一方成立不推出另一方，也不共同定义 tower health。

### §4.13.4 T-DELTA-1^{layer-skip}：layer-skip 下的 Δ 算子级

每层 `n` 的 `\Delta^{coll,(n)}$ 在 layer-skip 下含**四个维度**：同层三成分 + H11 集体维度 + H12 跨尺度维度 + **新增 layer-skip 维度**：

$$
\Delta^{coll,(n)} \;=\; \cdots \;+\; \underbrace{\boldsymbol{\sum_{n'\ne n, n\pm 1}w_{ls}^{(n'\to n)}\|K^{(n'\to n)}\|_{ls}}}_{\text{H15 layer-skip 维度}} \;+\; o(1)
$$

其中：

$$
\|K^{(n'\to n)}\|_{ls} \;:=\; \sqrt{\alpha_{ls}^2(\mathrm{tr}\,K)^2 + \beta_{ls}^2\|K_{asym}\|^2 + \gamma_{ls}^2\|K_{ext}\|^2}
$$

**陈述（P2 conditional residual model）**：在 A1^{coll}-A6^{layer-skip} 的 declared representation 下，上式可作 selected admitted residual projections 的 weighted summary / proxy，时间导数可包含相应 layer-skip 项。它不建立总额守恒、suffering conversion 或 `\Delta \equiv \hat R`；更强关系继续要求 §4.9.4 的 completeness、injectivity、metric、loss-channel 与 transfer assumptions。

### §4.13.5 T-FAMILY-1^{layer-skip} 综合陈述

**T-FAMILY-1^{layer-skip}**：在层级塔 `\{\mathcal{P}^{(n)}\}_{n=0}^N$ 上含任意 layer-skip 集合 `\mathcal{K}$（包括多重自指闭合），若 §4.13.1 三重笛卡尔积闭包堆栈成立，则：

(i) **family invariants 的条件性检验**：各项只在声明 family、admission、参数区间与误差界内成立
(ii) **layer-skip compatibility 待验证**：只有 P-univ/Q-univ/A assumptions 与 measurement map 在该模型成立时，才可把它作为额外耦合源而保持相应 family invariants
(iii) **跨层 burden / regime coupling** 只提供模型路径；不自动成为 pathology、lethal-`L_2` 或 suffering transmission
(iv) **family 与谱条件分别支付**：`\rho(\mathbf{A}_{tower}) < 1` 只判定声明线性化模型的 local stability，不赋予 family ontological universality
(v) **多重退化关系**：`\mathcal{K} = \emptyset$ → H12 T-FAMILY-1^{coll,nested}；进一步 `N=1$ → H11 T-FAMILY-1^{coll}；`N=1 \wedge \mathcal{P}=\{P\}$ → H7/H8/H9 单 P 版

### §4.13.6 与 H14 model-diagnostic grid 的条件性对位

H14 §4.12.5 的 variable-direction × topology-mechanism 组合可作 model-diagnostic grid。下表保留历史对应，但每行都只是候选 failure mode，不是 pathology / suffering verdict：

| 历史诊断标签 | 候选 family failure mode |
|---|---|
| 沿 σ_{sr} × bypass | T-CHI-1 (i) 双稳态被中间层 σ chatter 破坏 |
| 沿 σ_{sr} × aliasing | T-CHI-1 (ii) regime attractor 在频域受混叠路径扰动 |
| 沿 σ_{sr} × resonance | T-CHI-1 (i) 双稳态 + (iv) 相变方向被共振环路逆转 |
| 沿 d_c × bypass | T-CHANNEL-1 (i) 两型分裂被中间层 d_c chatter 破坏 |
| 沿 d_c × aliasing | T-CHANNEL-1 (ii) 反最小化在混叠路径下出现伪反例 |
| 沿 d_c × resonance | T-CHANNEL-1 (iii) 单向性被共振环路逆转（罕见但可能：极端嵌套 K 配置）|
| 沿 S_{str} × bypass | T-CHANNEL-1 (iv) 致命 L_2 判据被旁路绕过 |
| 沿 S_{str} × aliasing | T-DELTA-1 (1) Δ_{avail} 不由登记通道决定的论证被混叠扰动 |
| 沿 S_{str} × resonance | declared residual summary 在共振环路下失去原 measurement interpretation |
| 沿 T_{dir} × bypass | T-CHANNEL-1 (v) 投影分裂在 bypass 旁路下出现非投影分量 |
| 沿 T_{dir} × aliasing | T-CHI-1 (iii) 致命 L_2 在频域混叠下被错误诊断 |
| 沿 T_{dir} × resonance | T-DELTA-1 (3) 退化关系在共振下不收敛 |

该表只帮助定位哪项 family assumption 或 measurement interpretation 可能失效；它不提供完备分类、health/pathology 结论或 suffering admission。

### §4.13.7 T-FAMILY-1^{layer-skip} 不证明的事项

1. **不**给出 P-univ-7^{layer-skip} / Q-univ-7^{layer-skip} / A6^{layer-skip} 的具体验证窗口
2. **不**承诺族不变量与谱稳定的耦合是**充分必要**——本节给"谱稳定 ⟹ 族动力学有效"的必要方向；反向（族静态有效 ⟹ 谱稳定）不成立
3. **不**覆盖**多重族失效叠加**——若两类失效模式（如 σ × bypass 与 d_c × resonance）同时发生，§4.13.6 表给单类破坏路径，未分析叠加效应
4. **不**给出**时间变化 layer-skip × 族普适性**——准静态假设保留（与 H14 §4.12.7 第 3 项相同限制）
5. §4.14 只给额外 Lyapunov assumptions 下的 P2 local-stability result；它不把 family + spectrum + dissipation + boundedness 提升为 P1 或 tower-health condition

### §4.13.8 T-FAMILY-1^{layer-skip} 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| Layer-skip × family model 是开放问题 | H14 §4.12.7 第 5 项 | §4.13 给 P2 conditional family model |
| 族不变量与谱稳定的关系 | 隐含独立 | §4.13.5 (iv) 显式耦合：动力学有效性以谱稳定为前提 |
| diagnostic-grid failure paths | H14 给 topology candidates | §4.13.6 给 family-assumption failure candidates |
| Layer-skip 维度在 Δ 中的位置 | 缺失 | §4.13.4 `w_{ls}^{(n'\to n)}\|K^{(n'\to n)}\|_{ls}$ 显式 |

**Current standing**：T-FAMILY-1^{layer-skip} 是 P2 conditional family model / P3 domain bridge。P-univ/Q-univ/A6 保持 family-scoped；后续实证与 Lyapunov 分析不构成 generic path to P1。

## §4.14 T-LYAPUNOV-1：塔的条件性局部非线性稳定性（H16，2026-04-26）

> **Status**：本节给塔级动力学的 Lyapunov candidate 与条件性 local nonlinear-stability result；它不把线性化谱判据自动升级为 global guarantee。**Claim level: P2 conditional mathematical result**。
>
> **Does not close**：global basin、large-disturbance、health/pathology 或 P1 standing。若要 global / domain-global conclusion，必须另行给出覆盖该 domain 的 forward invariance、coercive bounds 与 derivative inequality。

### §4.14.1 Lyapunov 候选框架

塔的候选状态只包含逐层 independently admitted 的分量；下式保留历史五分量写法，未 admitted 的 `T_dir` 或 `S` 分量必须省略：

$$
x \;:=\; \bigl(\sigma_{sr}^{(n)}, d_c^{(n)}, T_{dir}^{(n)}, S_{sig}^{(n)}, S_{str}^{(n)}\bigr)_{n=0}^N \;\in\; \mathbb{R}^{5(N+1)}
$$

声明平衡点 `x^* := \{x^{*,(n)}\}_{n=0}^N`。历史标签 `\mathcal{H}^{(n)}` 至多表示 criterion-relative model regime，不建立 health。

**Lyapunov 候选函数**：

$$
\boxed{\;V_{tower}(x) \;:=\; \sum_{n=0}^N V^{(n)}(x^{(n)}) \;+\; \sum_{(n,m)\in E_{adj} \cup E_{skip}} V^{(n,m)}_{coupling}(x^{(n)}, x^{(m)})\;}
$$

其中**每层项**：

$$
V^{(n)}(x^{(n)}) \;:=\; w_\sigma^{(n)}(\sigma_{sr}^{(n)} - \sigma_{sr}^{*,(n)})^2 + w_d^{(n)}(d_c^{(n)} - d_c^{*,(n)})^2 + w_T^{(n)}(T_{dir}^{(n)} - T_{dir}^{*,(n)})^2 + w_{S}^{(n)}\bigl[(S_{sig}^{(n)})^2 + (S_{str}^{(n)})^2\bigr]
$$

**耦合项**（沿 `\mathcal{G}_{tower}$ 每条边）：

$$
V^{(n,m)}_{coupling}(x^{(n)}, x^{(m)}) \;:=\; w_{coup}^{(n,m)}\sum_{X}\bigl(x_X^{(n)} - \mathrm{lift}^{(m\to n)}(x_X^{(m)})\bigr)^2
$$

其中 `\mathrm{lift}^{(m\to n)}` 是层 `m` 到层 `n` 的 declared reference mapping。A5^{cross} / A6^{layer-skip} 与 independently typed stake data 可以约束它，但不唯一决定它，也不赋予“健康预期”语义。

### §4.14.2 充分条件 N1-N3

N1-N3 是候选验证条件，但单靠它们不能证明 `V_{tower}` 为 Lyapunov 函数：

| 编号 | 条件 | 含义 / 与已有结构的对应 |
|---|---|---|
| **N1（耦合算子有界性）** | 所有 `\Pi^{(n\to m)}, K^{(n\to m)}$ 是 `\mathrm{Op}(\mathcal{P})$ 上的有界线性算子；`\sup_{(n,m)}\|\Pi^{(n\to m)}\|_{op} \le M_{\Pi}$，`\sup_{(n,m)}\|K^{(n\to m)}\|_{op} \le M_K$（有限常数） | 把 H10 / H12 / H14 的代数结构升为度量结构；耦合不会"突然爆炸" |
| **N2（条件性耗散界）** | 若 `S` 已逐层 admitted，可在声明邻域内检验原速率不等式；否则用 burden / residual terms 重写 | model-local derivative-bound candidate；不是 suffering admission 或 T-IRR 普适强化 |
| **N3（谱 margin + 非线性余项界）** | `\rho(\mathbf{A}_{tower}) < 1 - \delta_{nonlinear}$ 加声明邻域内的高阶余项界 | 支持局部分析；不单独保证 trajectory 不离开该邻域 |

**关键观察**：N1 / N2 / N3 只提供候选检查路线：
- N1 ↔ H10 跨尺度耦合 + H14 layer-skip 耦合的有界性公理化
- N2 ↔ 在 suffering admitted 时对相关速率项提出局部 bound
- N3 ↔ H14 / H15 线性化谱条件加局部非线性余项 bound

### §4.14.3 T-LYAPUNOV-1 陈述

**陈述（P2 conditional mathematical result）**：在声明的 forward-invariant neighborhood 内，若 N1 / N2 / N3 成立，并且 `V_{tower}` 被独立验证为相对于 `x^*` 正定、具有该邻域内所需上下界，且其导数满足下式，则可得到该平衡点在此邻域内的 local exponential stability：

$$
\boxed{\;V_{tower}(x^*) = 0,\quad V_{tower}(x) > 0\text{ for }x \ne x^*,\quad \dot{V}_{tower}(x) \le -\alpha V_{tower}(x)\text{ for some }\alpha > 0\;}
$$

对从该 forward-invariant neighborhood 内出发的初始扰动，可在所验证 bounds 下得到相应指数衰减估计。这里没有对任意 `x_0` 的 global claim，也不把稳定平衡点称为 healthy。

### §4.14.4 验证义务

**Step 1（每层 `\dot{V}^{(n)} \le 0$ 单层贡献）**：

把 H10 / H12 各层 ODE 代入 `\dot{V}^{(n)}` 后，必须在声明邻域内证明而非假定每层独立项具有足够负定部分：

$$
\dot{V}^{(n)}\big|_{\text{independent}} = -\alpha^{(n)}\bigl[(\sigma_{sr}^{(n)} - \sigma_{sr}^{*,(n)})^2 + \cdots\bigr] + \text{交叉项}
$$

§4.4-§4.6 的弛豫项只提供候选来源；其符号、系数与交叉项是否足以给出负定界，必须逐模型验证。

**Step 2（N2 控制 `S_{str}$ 累积项）**：

仅在 `S` 已 admitted 的模型中，N2 才可用于检查 `S`-相关贡献是否非正。该不等式是 local model assumption，不是 global anti-minimization principle，也不证明 burden 守恒或 suffering transfer。

**Step 3（N3 控制耦合项）**：

`\dot{V}^{(n,m)}_{coupling}` 含交叉路径产生的二次项；必须显式证明 N1 / N3 给出的 bounds 足以让负定部分支配这些项。线性谱 margin 本身不提供该非线性结论。

**Step 4（综合给 `\dot{V}_{tower} \le -\alpha V_{tower}$）**：

只有在 Step 1-3 的 bounds 均在同一 forward-invariant neighborhood 成立时，才可选择正的 `\alpha` 并得到该邻域内的指数衰减率；否则本节只保留 Lyapunov candidate programme。

### §4.14.5 与 H4 / H10-H15 的最终统一

T-LYAPUNOV-1 与既有定理的关系：

| 既有定理 | T-LYAPUNOV-1 中的角色 |
|---|---|
| H4 T-IRR-3.5（ν_block 条件模型 / P0-03 absorption remainder） | suffering admitted 时 N2 的条件性模型输入；不是自动的速率或 transfer theorem |
| H10 T-PROJ-1^{coll,nested}（嵌套递归投影） | V^{(n)} 各层项的结构来源 |
| H12 T-FAMILY-1^{coll,nested}（conditional family recursion） | 提供待声明的 model terms；权重仍是 measurement/model parameters |
| H13 T-TOWER-STAB-1（自指闭合谱判据） | N3 谱判据条件的具体形式 |
| H14 T-LAYER-SKIP-1（layer-skip 增广多图谱判据） | N3 在含 layer-skip 拓扑下的具体形式 |
| H15 T-FAMILY-1^{layer-skip}（family + spectrum） | 为局部 Lyapunov candidate 提供待验证的 model terms；不自动升级为 nonlinear theorem |

**最终统一的结构主张**：

$$
\boxed{\;\text{declared local mathematical stability} \;\Longleftarrow\; \text{(family assumptions)} \;\wedge\; \text{(spectral/nonlinear bounds)} \;\wedge\; \text{(conditional derivative bound)} \;\wedge\; \text{(operator boundedness)}\;}
$$

该式只在 §4.14.3 的 forward-invariant neighborhood、positive-definiteness 与 derivative bounds 均已证明时给 local mathematical stability。任一条件失效只表示本证明路线失败，不自动对应 health / pathology。Generative-health 解释必须另经 21C B13。

### §4.14.6 T-LYAPUNOV-1 不证明的事项

1. **不**承诺 `V_{tower}$ 是**唯一**有效 Lyapunov 函数——其他形式可能也工作；本节给一个具体候选
2. **不**给出**全局吸引域**；只对已经声明并验证 forward-invariant 的邻域给 local exponential result
3. **不**覆盖多重平衡点；“不同文化 / 制度”只能作为 P3 domain mapping，不使用 healthy-attractor 预断
4. **不**给出 `V_{tower}$ 系数 `w_X^{(n)}, w_{coup}^{(n,m)}$ 的具体最优选择——仅承诺存在性，最优化属 P3 实证
5. **不**覆盖**非光滑动力学**（即 `\mathbb{1}[d \le d_c]$ 在 `d = d_c$ 处不可微）——需用 H9 T-CHANNEL-1 光滑族近似把硬指示替换为 `\psi^{coll,(n)}$；非光滑极限的 Lyapunov 处理留作后续

### §4.14.7 T-LYAPUNOV-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| 线性化与非线性 | H13 / H14 / H15 线性化 | T-LYAPUNOV-1 给额外 bounds 下的 local nonlinear result |
| family assumptions + 谱稳定 | H15 条件性耦合 | T-LYAPUNOV-1 把它们列为共同验证义务 |
| mathematical stability condition | 多个独立条件 | §4.14.5 boxed 公式：只在 §4.14.3 前件下成立 |
| conditional derivative bound | H4 提供候选方向 | N2 只作 suffering-admitted model 的 local bound candidate |

**Current standing**：T-LYAPUNOV-1 是 P2 conditional local nonlinear-stability result / P3 domain bridge。Global conclusions remain OPEN unless a declared forward-invariant domain, coercive bounds and derivative inequality are actually supplied; no generic path to P1 or health follows.
