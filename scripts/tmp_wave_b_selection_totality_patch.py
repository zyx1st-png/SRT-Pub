from pathlib import Path
import re


def replace_one(path: str, pattern: str, replacement: str, flags=re.S) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    new, n = re.subn(pattern, lambda _m: replacement, text, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f"{path}: expected exactly one match, got {n}: {pattern[:120]}")
    p.write_text(new, encoding="utf-8")
    print("patched", path, pattern[:80])


# Core 01
replace_one(
    "Core/SRT_Core_01_Axioms.md",
    r"## 元公理对（Meta-Axiom Pair）.*?\n---\n\n# Part A:",
    """## 元公理对（Meta-Axiom Pair）

> **2026-09-14 Selection-totality override**：本节只固定形式层如何服从当前 L0 / Spine。任何较早的 `κ₀`、`ε_pg`、`Align` 或 `Ĝ_θ` 强读法，都不得反向定义 primitive Selection。

**MA-1（选择一元生成 / Selection-totality）**：SRT 的 primitive 不是“潜在域 + 一个后来执行选择的算子”，而是 Selection 本身作为现实的生成方式。最低分析负担仍分为 O0（开放 / 非最大中性）与 S0（实际化），但两者是同一 primitive Selection 的共原初分面，不是两个机制。

```text
O0 before S0: NO
S0 before O0: NO
κ₀ causes first Selection: NO
ε_pg defines O0: NO
```

`κ₀`、`ε_pg` 与其他方向 / 代价结构可继续作为更强形式 realization 候选；它们相对于 primitive non-flatness 的必要性与继承关系另行裁决。

**MA-2（有限位置 / Bounded Positionality）**：primitive Selection 是有限位置索引的，但有限位置不等于已经形成的具身算子、One、Selection-position、Bearer 或主体。`Ĝ_θ`、`Align(θ,κ₀)`、d-value 等只在其各自已声明的 formed / formal / domain realization 中使用；它们不构成 primitive Selection 的先在视角者。

```text
finite positionality != prior operator entity;
finite positionality != formed evaluative standpoint;
formed operator perspective may be compared only under its declared model.
```

* **Cross-ref**: `Core_Law/SRT_L0_Metaphysics.md`; `Core/SRT_Core_21_Minimal_Axioms.md`; `Core_Law/SRT_Generative_Ontology_Spine.md`; `Core/SRT_Core_12a_Ontology_L0L1.md`.

---

# Part A:""",
)

replace_one(
    "Core/SRT_Core_01_Axioms.md",
    r"### Ax-Core-A1: Existential Priority.*?(?=### T-Core-A1C3:)",
    r"""### Ax-Core-A1: Selection-Actuality Identity
**Canonical Definition**: determinate manifest existence is the actuality aspect of Selection, not an ontically different product emitted by an operator acting on a prior warehouse.

```text
manifest existence
= Selection under determinate actuality.
```

Where a declared formal model uses `Ĝ_θ`, range / image notation is allowed only as a representation of realised actuality in that model. It is not the metaphysical definition of primitive Selection.

* **Implication**: “Selection precedes existence” is pedagogical ordering, not primitive chronology or a factory/product relation.

### T-Core-A1C1: Model-Relative Presence
**Scoped Statement**: in a declared non-ergodic model, current presence may be represented by the states realised / operative under that model's Selection map.

$$\text{Presence}_{M}(σ) \iff σ \in \mathrm{Realized}_{M}(\text{Selection})$$

This does **not** entail that every non-manifest alternative is a completed object stored in an absolute latent inventory. Selection-relative background / unexhausted openness is sufficient at the metaphysical level.

### T-Core-A1C2: Minimum Non-Flatness Boundary
**Canonical Boundary**: primitive Selection is not maximally indifferent / role-flat, but this minimum non-flatness does not by itself specify a continuation, non-self-erasure, option-count, value or moral gradient.

```text
primitive non-flatness: YES;
B >= 2 primitively preferred over B <= 1: NO;
continuation preference at O0: NO;
terminal Selection defective: NO;
ε_pg = O0 by definition: NO;
ε_pg as universal T_dir ground: NO.
```

Historical `ε_pg` proto-gradient formulas remain lineage / stronger-realization material unless separately re-established under their own owner. Their exact inheritance from primitive non-flatness is OPEN.

`T_dir` must therefore take any reference direction from an independently typed downstream relation; this theorem no longer supplies a universal hidden value direction.

""",
)

# Core 12a
replace_one(
    "Core/SRT_Core_12a_Ontology_L0L1.md",
    r"> \*\*Part B\*\* contains the Original Theoretical Discourse \(Human-Readable Context\)\.\n",
    "> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).\n\n> **Selection-totality formal-scope override（2026-09-14）**：本文件现在是 L0/L1 的**形式 / realization 接口**，不是第二形而上 owner。`L_0/L_1` 可在具名模型中表现为域、流形、状态空间或 phase regime，但这些数学对象不得反向定义 primitive Selection。`L_0^{abs}` 的“绝对潜在源 / 可能性仓库”旧读法在形而上强度上 superseded；`Ĝ_θ != primitive Selection`。\n",
    flags=0,
)

replace_one(
    "Core/SRT_Core_12a_Ontology_L0L1.md",
    r"## I\. L_0: The Latent Domain \(潜在域\).*?(?=### Ax-L0-Bootstrap:)",
    r"""## I. L_0 / L_1: Model-Facing Selection Aspects

### Ax-L0-01: Open-Aspect Formalization
**Canonical formal boundary**: `L_0` notation at this layer denotes a declared formal rendering of Selection's open / non-preclosed aspect relative to a determinate manifestation or model cut. It does not denote a universally required warehouse of completed possible objects.

A domain may choose a state space such as a Hilbert space, moduli space, graph / computational space, manifold or other formal domain when that mapping is independently justified. Such spaces are **realization models**, not the identity of primitive L0.

```text
formal L0-model != primitive Selection itself;
formal L0-model != absolute inventory of preformed outcomes.
```

### Ax-L0-02: Non-Exhaustion of Selection Openness
No finite determinate manifestation, formed position or formal projection exhausts the open generative aspect of Selection. This is a non-exhaustion boundary, not a claim that all future forms pre-exist as completed latent objects.

### T-L0-01: Novelty Without Preformation
New manifest structures are actualising Selection under concrete constraints. They need not pre-exist as completed patterns in an absolute latent source, and they are not generated from an unconstrained nothing.

The primitive actualisation burden remains with P0-01; domain theories specify realization conditions rather than derive the primitive from a prior non-selective mechanism.

### Ax-L0-03: Conditional Differential-Topology Realization
A declared `L_0^{rel}` model **may** use a differential manifold, cost geometry, attractor landscape or other anisotropic structure to represent constraints on realizations.

For such a model one may write, for example:

$$L_0^{rel,M}=(M,\nabla,\mathcal{S})$$

provided the model, metric / measure and interpretation are declared. This is **not** a universal theorem that primitive Selection lives inside a prior differential manifold, and no such gradient alone causes first actualisation.

""",
)

replace_one(
    "Core/SRT_Core_12a_Ontology_L0L1.md",
    r"### T-L0-02: Phase-Anchor Theorem.*?(?=### Def-L0-PreAnchored:)",
    r"""### T-L0-02: Conditional Stabilization-Phase Model

`κ` may be used in a declared formal realization as a stabilization coordinate for Selection organization. Phase-transition language such as `κ_c1` / `κ_c2`, spectral gaps and fixed points is therefore **model-conditional**. It does not define universal births of L1/L2 as separate substances and does not establish consciousness thresholds by itself.

```text
kappa phase map = stronger realization model;
!= primitive ontology definition;
!= universal consciousness switch.
```

### T-L0-Kappa0: Conditional Anisotropy Floor

`κ₀` is retained as a stronger formal candidate for models that posit a nonzero anisotropy / curvature floor:

$$\exists\,\kappa_0>0 : R(L_0^{rel,M})\geq\kappa_0$$

within a **declared model M**.

Canonical boundary:

```text
κ₀ != definition of O0;
κ₀ != hidden cause of primitive Selection;
κ₀ != proof that a specific Selection occurs;
κ₀ necessity relative to Selection-totality = OPEN.
```

Any `Psi_f` floor, critical-threshold or cheaper-path consequences derived from `κ₀` are conditional consequences of that stronger model, not primitive theorems.

### T-L0-NonStatic: Conditional History / Geometry Co-Evolution

In models that encode prior Selection efficacy as changing geometry, a history-dependent parameter such as

$$\kappa(t)=\kappa_0+\int_0^t\mathcal{F}[\hat G_\theta(\tau),\kappa(\tau)]d\tau$$

may represent changing accessibility / cost structure. The ontological reading is **not** “Selection writes into a separate L0 substance”; it is a formal representation of prior Selection remaining effective in later Selection conditions. Entropy balances, curvature accumulation and coupled `κ/θ` equations remain scoped hypotheses requiring declared state space and measure.

### Formal-stage scope guard

All following constructs such as `PreAnchored`, `Swampland`, Platonic attractor or similar L0-stage vocabulary are **model / bridge constructs** unless independently promoted. They may organize a declared realization but must not be cited as the universal primitive ontology or as proof of a prior possibility warehouse.

""",
)

# Reference Axioms
replace_one(
    "Core_Law/SRT_Reference_Axioms.md",
    r"> \*\*Status\*\*: L1 Formal Axioms \| \*\*Version\*\*: 1\.0\n",
    "> **Status**: L1 Formal Axioms | **Version**: 1.0\n> **Selection-totality compatibility（2026-09-14）**：本文件是形式 / 接口层，不得反向定义 primitive Selection。`Ĝ_θ` 只在具名 operator realization 中使用；`L_0/L_1/L_2` 是可形式化的 Selection 分面 / regime，不是三个先在物质域。A6-A12 等历史高承诺条目保留其研究 lineage，但不得以本文件位置自动获得 primitive proof load。\n",
    flags=0,
)

replace_one(
    "Core_Law/SRT_Reference_Axioms.md",
    r"### A1 选择优先性 \(Existential Priority\).*?(?=### A2 )",
    """### A1 选择—实际性同一接口 (Selection / Actuality Interface)

primitive Selection 的形而上意义由 L0 owner 固定；本接口只给出形式读法：

```text
Existence_actual
:= Selection 的 determinate-manifest aspect.
```

当一个具名模型采用 `Ĝ_θ` 时，可以用其 realized range 表示当前显现，但这只是模型表达，不意味着存在是一个先在算子从绝对潜在库存中输出的第二种材料。

**推论 A1-C1（模型相对）**：在具名非遍历模型中，presence 可限制于该模型已实际化 / operative 的状态；未显现部分只需按 Selection-relative background / unexhausted openness 处理，不要求 completed latent-object inventory。

---

""",
)

replace_one(
    "Core_Law/SRT_Reference_Axioms.md",
    r"### A4 具身必要性 \(Embodiment Necessity\).*?(?=### A5 )",
    r"""### A4 具身算子有限性 (Embodied Operator Finitude)

任何**已形成 / 具身的 operator realization** `Ĝ_θ` 都必须声明有限参数、接口与作用域；不存在由该形式算子获得的无位置 God-view。

$$\hat G_\theta : S_M\to S_M,\quad \theta\in\Theta_M$$

但：

```text
formed / embodied G-hat finitude
!= primitive Selection requires a prior embodied chooser.
```

primitive finite positionality 比一个具体 `θ`-operator 更薄。

---

""",
)

replace_one(
    "Core_Law/SRT_Reference_Axioms.md",
    r"### A5 规范闭包 \(Normative Closure\).*?(?=### A6 )",
    r"""### A5 历史约束与稳定化实现 (Historical Constraint / Stabilization Realizations)

一般 L2-side 负担是：先前 Selection 的差异在后来 Selection 中保持实际约束效力。固定点 / attractor 只是这一负担的**强 realization 类**之一。

在声明的模型中可以定义：

$$L_{2,M}^{fp}:=\{\sigma:\hat G_\theta[\sigma]=\sigma\ \text{and stable under }M\}$$

但：

```text
L2-side historical efficacy
!= universally a fixed-point substance;
fixed point != normativity / legitimacy automatically.
```

“现实笼子”可作为强迟滞 / 锁定 realization 的解释性名称，不是 L2 的普遍定义。

---

### A6-A12 Selection-totality scope guard

A6-A12 中的信息、适应度、生存、全息、延续、脆弱性与跨尺度命题属于 hybrid / bridge / high-commitment lineage。除非其各自 owner 另有当前 claim-level 授权，它们：

```text
不得定义 primitive Selection；
不得恢复 absolute latent warehouse；
不得把 survival / continuation 写成 primitive value；
不得把 consciousness / agency 反投射到 primitive Selection。
```

""",
)

# Reference Ontology
replace_one(
    "Core_Law/SRT_Reference_Ontology.md",
    r"## §1 三域结构 \(The Triadic Ontology\).*?(?=### §1\.4 κ)",
    r"""## §1 Selection 的三类模型分面 (Triadic Model Aspects)

> **本节定位（2026-09-14）**：`L_0/L_1/L_2` 继续作为强有用的形式坐标，但它们不再被本文件定义成三个独立本体容器。L0 形而上意义由 `SRT_L0_Metaphysics.md` 与 Generative Ontology Spine 控制。

### §1.1 L₀ — Open / Non-Preclosed Aspect

**定义 O1**：在一个声明模型 `M` 中，`L_0^M` 表示相对于当前 determinate manifestation 尚未被该 model-cut 穷尽 / 封闭的可达或生成状态结构。

```text
L0^M = model-relative openness / accessibility construct;
!= absolute warehouse of completed possible objects.
```

历史记号 `L_0^{abs}` 不再作为 positive canonical primitive source。若旧桥接或比较文献继续使用它，只能表示“任何有限形式模型都不能穷尽 primitive Selection openness”的极限性速记，不能承载集合库存、全信息量或先在容器证明。

**定义 O1b（相对可达域）**：`L_0^{rel,M}(t)` 可以继续作为给定 formed operator / constraints 时的可访问状态空间：

$$L_0^{rel,M}(t+1)=f_M(L_1^M(t),\hat G_\theta,\text{constraints})$$

它是模型构造，不是 primitive ontology。

---

### §1.2 L₁ — Determinate Manifest Aspect

**定义 O2**：`L_1^M(t)` 表示 Selection 在模型 `M` 中的 determinate manifest / operative slice。

若采用 operator realization，可写：

$$L_1^M(t)=\mathrm{Realized}_M(\hat G_\theta, t)$$

而不是把该式读成 prior operator 产生 ontically different existence。迟滞、门控、单纯复形、topological-hole 等公式均为更强 realization / observation models。

---

### §1.3 L₂ — Retained Historical-Efficacy Aspect

**定义 O3**：`L_2` 的一般负担是先前 Selection 的差异继续实际约束后来 Selection。

```text
L2-side
= retained / sedimented historical efficacy of prior Selection.
```

固定点、attractor、迟滞累积、hardness 与可塑性阈值是某些强 stabilization models，不是普遍 ontology definition。对一个声明模型可以另定义 `L_{2,M}^{fp}` 等子类。

---

""",
)

replace_one(
    "Core_Law/SRT_Reference_Ontology.md",
    r"### §1\.4 κ — 稳定化程度参数 \(Stabilization Degree\).*?(?=\*\*定义 O3d \(稳定化程度\)\*\*)",
    """### §1.4 κ — 条件性稳定化参数 (Conditional Stabilization Degree)

> `κ` 是强 realization / model coordinate，不是 primitive Selection 的阶段计。它只在一个已声明的 `L_0^{rel,M}` / operator model 中有定义。`κ_c1/κ_c2`、spectral-gap、fixed-point 等相变解释不得被写成 L1/L2 作为独立本体物质的 universal birth theorem；意识对应尤其需要独立 bridge / empirical gate。

""",
)

# Reference Dynamics
replace_one(
    "Core_Law/SRT_Reference_Dynamics.md",
    r"> \*\*依赖\*\*: SRT_Reference_Axioms\.md \(符号规范\)\n",
    "> **依赖**: SRT_Reference_Axioms.md (符号规范)\n> **Selection-totality scope override（2026-09-14）**：本文件只描述 formed / embodied / domain-level Selection realizations。`Ĝ_θ != primitive Selection`；attention、intentional vector、survival gating、agency 与 embodied parameters 都是更强组织或模型性质，不得反向定义 subjectless primitive Selection。\n",
    flags=0,
)

replace_one(
    "Core_Law/SRT_Reference_Dynamics.md",
    r"### §1\.1 基本定义.*?(?=\*\*定义 D2a \(时间分辨率\)\*\*)",
    r"""### §1.1 基本定义

**定义 D1**：在一个声明的 model / formed realization 中，Ghost Operator `Ĝ_θ` 是对 Selection organization 的参数化形式载体：

$$\hat G_\theta:S_M\to S_M,\quad \theta\in\Theta_M$$

Hard guard:

```text
G-hat_theta != primitive Selection;
formal operator != prior chooser;
state space S_M != absolute possibility warehouse.
```

### §1.2 形成后注意力分解（formed-operator decomposition）

旧句“Ghost Operator 的本质是 Fundamental Attention”在 universal / primitive 强度上 **superseded**。对具有注意、分辨率或意向结构的 formed / embodied operator，可使用条件性分解：

$$\hat G_\theta^M\approx\mathrm{Attention}_M(\mathrm{Scope},\mathrm{Resolution}_s,\mathrm{Resolution}_t,\mathrm{Vector})$$

这些分量属于模型 `M` 的形成后结构：

| 分量 | 允许读法 | 禁止反推 |
|---|---|---|
| Scope / d | formed concern / selection scope proxy | primitive Selection 已有 d / Concern |
| spatial / temporal resolution | embodied model resolution | primitive Selection 需要知觉 |
| Vector | domain-specific directional / action signal | primitive Selection 自带 intention / goal |

后续 D2a、agency、survival gate、somatic binding 等公式均按此 formed / domain scope 读取。

""",
)

for path in [
    "Core/SRT_Core_01_Axioms.md",
    "Core/SRT_Core_12a_Ontology_L0L1.md",
    "Core_Law/SRT_Reference_Axioms.md",
    "Core_Law/SRT_Reference_Ontology.md",
    "Core_Law/SRT_Reference_Dynamics.md",
]:
    text = Path(path).read_text(encoding="utf-8")
    if "Selection-totality" not in text:
        raise SystemExit(f"{path}: Selection-totality marker missing after patch")
