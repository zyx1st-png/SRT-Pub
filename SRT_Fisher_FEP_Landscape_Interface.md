---
id: SRT-FISHER-FEP-LANDSCAPE-INTERFACE
type: framework
tags: [Fisher, FEP, Landscape, L0, L1, L2, Interface]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: bridge
claim_mode: canonical
dependency: [SRT-QUICKSTART, SRT-VERTICAL-INTEGRATION, SRT-CORE-22, SRT-PSIF-CANONICAL]
---

# SRT 中 Fisher 几何、能量景观与 FEP 的落位澄清
# Placement of Fisher Geometry, Energy Landscapes, and FEP in SRT

---

## 0. 目的

本文用于澄清一个容易混层的映射问题：

- 能量景观 / FEP 是否可以直接看成 `L₂`？
- Fisher 空间是否可以直接看成 `L₁`？
- `Ψ_f ≡ Fisher metric` 是否可以作为严格等号使用？

当前结论是：**这些对应可以作为启发式类比或局部形式投影，但不宜直接等同。**

原因在于：

- `L₀ / L₁ / L₂` 是 **SRT 的本体论域**
- Fisher 几何 / 能量景观 / FEP 是 **描述这些域之间过程的几何或动力学接口**
- `Ψ_f` 是 **信息论 / 组织性可支付负担**；Fisher–Rao metric 是该负担在平滑统计流形中的 **局部二阶信息几何投影**，不是与 `Ψ_f` 本身的裸恒等式

因此，更稳的做法不是“一一替代”，而是把它们放到 SRT 的不同箭头上。

---

## 1. 核心澄清（最短版）

### 不建议直接写成：

- `Fisher space = L₁`
- `energy landscape = L₂`
- `FEP = L₂`
- `Ψ_f ≡ g_F`（若按标量代价与度量张量的裸等号读取）

### 更准确的写法：

- **Fisher geometry**：主要刻画 `L₀ → L₁` 的局部可区分性 / 选择摩擦几何
- **L₁**：实际显现出来的事件、轨迹与当前现实切片
- **L₂**：由历史选择沉积而成的稳定约束域
- **energy / free-energy landscape**：`L₂` 的一种有效投影或低维表达
- **FEP**：某些组织化系统在 `L₁` 中、受 `L₂` 约束时的自维持更新律
- **`Ψ_f` 与 Fisher–Rao metric 的关系**：`Ψ_f` 的局部信息几何投影由 Fisher–Rao metric 诱导；严格写作应使用 `δΨ_f^{geom}=1/2 dθ^T g_F dθ + O(||dθ||^3)` 或路径泛函，而不是裸写 `Ψ_f = g_F`

最压缩的一句话是：

> **Fisher 属于 `L₀→L₁` 的生成几何，景观属于 `L₂` 对 `L₁` 的约束投影，FEP 属于 `L₁` 在 `L₂` 中的自维持动力学；`Ψ_f` 的 Fisher 读法是局部二阶投影，不是裸等号。**

---

## 2. 为什么不能直接等同

### 2.1 本体层级与描述接口不是同一类对象

`L₀ / L₁ / L₂` 回答的是：

- 什么是潜在域
- 什么是显现域
- 什么是收敛 / 沉积后的稳定约束域

而 Fisher / landscape / FEP 回答的是：

- 从可能到现实，这一步局部有多“难”
- 稳定约束如何以地形方式牵引后续更新
- 某些系统为什么会沿某种局部规则维持自身

所以这里的差别不是内容大小，而是**范畴差别**：

- 前者是 ontology
- 后者是 geometry / dynamics

---

### 2.2 L₁ 不是几何本身，而是几何上真实发生的显现

Fisher metric 给出的是：

\[
 ds^2 = d\theta^\top g_F(\theta) d\theta
\]

它描述的是：

- 邻近可选态之间的局部可区分性
- 哪些方向改一点就显现大变
- 哪些方向改很多，结果却几乎不变

因此它更接近：

> `L₀` 在趋向 `L₁` 实际化时所呈现出的局部选择几何

而 `L₁` 本身是：

- 已经发生的事件
- 已经显现的轨迹
- 当前现实的落点

所以：

> **L₁ 是“走出来的那一步”，Fisher 是“这一步附近的路感与阻力结构”。**

---

### 2.3 `Ψ_f` 不是 Fisher 张量本身，而是由 Fisher 张量诱导的局部代价 / 路径泛函

Fisher–Rao metric 是一个度量张量 \(g_F\)，而 `Ψ_f` 在 SRT 中是 payability burden、局部标量代价或路径泛函。二者范畴不同，不能直接写成严格裸等式。

在可微统计流形 \(p(x\mid\theta)\) 上，KL 散度有局部二阶展开：

\[
D_{KL}(p_\theta\parallel p_{\theta+d\theta})
=
\frac12 d\theta^\top g_F(\theta)d\theta
+O(\|d\theta\|^3)
\]

因此 SRT 中最稳的 Fisher 表达是：

\[
\delta\Psi_f^{geom}
=
\frac12 d\theta^\top g_F(\theta)d\theta
+O(\|d\theta\|^3)
\]

或路径形式：

\[
\Psi_f^{geom}[\gamma]
=
\int_\gamma \sqrt{g^F_{ij}(\theta)\dot\theta^i\dot\theta^j}\,dt
\]

这意味着：

> **Fisher metric 不是 `Ψ_f` 本身，而是 `Ψ_f` 在统计流形投影中的局部二阶几何结构。**

---

### 2.4 L₂ 比景观更厚，景观只是其有效切片

`L₂` 在 SRT 中不仅包含稳定性，还包含：

- 历史沉积
- 滞后（hysteresis）
- 规范性与制度性
- 多主体收敛后的惯性结构

而常见的能量 / 自由能景观通常只给出一个标量函数：

\[
V(x) \quad \text{or} \quad F(x)
\]

它表达的是：

- 哪些状态更“低”
- 哪些盆地更稳定
- 哪些方向更容易被牵引

因此更稳的说法是：

> **能量景观不是整个 `L₂`，而是 `L₂` 约束域在某组状态变量上的有效投影。**

---

### 2.5 FEP 是更新原则，不是整个 L₂

FEP 的核心工作是描述：

- 某类已经组织化的系统
- 如何在给定约束下维持自身
- 为什么会沿局部下降方向更新

因此它更像：

> **组织化主体在 `L₁` 中、受 `L₂` 牵引时的一种局部动力学规则**

而不是 `L₂` 本身。

换句话说：

- `L₂` 更接近“稳定约束场”
- FEP 更接近“系统在这个约束场中如何继续运动”

---

## 3. 三箭头结构（推荐固定写法）

与其做静态的一一对应，不如固定成 SRT 的三段结构：

### A. `L₀ → L₁`

**主题**：生成 / 实际化 / 局部选择

**最合适的接口**：Fisher geometry

**它刻画的内容**：

- 局部可区分性
- 选择摩擦的几何投影
- 哪个方向更自然
- 选择参数微扰如何放大为显现差异

**推荐公式**：

\[
\delta\Psi_f^{geom}
=
\frac12 d\theta^\top g_F(\theta)d\theta
+O(\|d\theta\|^3)
\]

---

### B. `L₁ → L₂`

**主题**：沉积 / 稳定化 / 滞后

**最合适的语言**：SRT 自身的历史沉积论述

**它刻画的内容**：

- 反复发生的选择如何变成习惯、规范、吸引子、制度
- 当前现实如何硬化为后续现实的约束条件

这一步是 SRT 的原生任务，不能被 Fisher 或 FEP 单独取代。

---

### C. `L₂ → L₁`

**主题**：回牵 / 塑形 / 自维持更新

**最合适的接口**：energy landscape / free-energy landscape / FEP

**它刻画的内容**：

- 稳定约束如何回牵新的显现
- 哪些状态更容易被维持
- 某些组织化系统如何在这片约束地形中继续更新

---

## 4. 三者之间的关系式（谨慎表述）

在适用场景下，可以用如下关系帮助读者建立直觉：

\[
\dot{\theta} \sim - g_F^{-1}(\theta)\, \nabla_\theta F_{eff}
\]

其中：

- \(g_F(\theta)\) 提供局部 Fisher 几何
- \(F_{eff}\) 提供有效景观或目标地形
- 更新轨迹发生在组织化系统的实际运动中

这条式子可读作：

> **景观给出“往哪边低”，Fisher 给出“在这个统计空间里怎么走才自然”，而实际走出来的就是 `L₁` 中的更新轨迹。**

注意：这是一种 **bridge-level** 写法，用于局部动力学接口；不应反过来把它当作 SRT 全体本体论的替代物，也不应把 \(g_F\) 当作 `Ψ_f` 的完整定义。

---

## 5. 推荐对外表述

### 版本 A（最短）

> 在 SRT 中，Fisher 几何不等于 `L₁`，而是主要刻画 `L₀→L₁` 的局部选择几何；`Ψ_f` 的 Fisher 读法不是 `Ψ_f = g_F`，而是 `Ψ_f` 的局部二阶信息几何投影由 Fisher–Rao metric 诱导；能量景观也不等于整个 `L₂`，而是 `L₂` 作为稳定约束域的一种有效投影；FEP 则描述组织化系统在 `L₂` 约束下于 `L₁` 中的自维持更新。

### 版本 B（中文压缩）

> **Fisher 属于生成前沿，景观属于稳定地形，FEP 属于地形中的更新规则；`Ψ_f` 的 Fisher 表达是局部二阶代价投影，不是裸恒等式。**

### 版本 C（英文压缩）

> **Fisher geometry belongs primarily to the generative interface from `L₀` to `L₁`; the Fisher reading of `Ψ_f` is a local second-order information-geometric projection, not a bare identity; energy landscapes are effective projections of `L₂`; FEP characterizes self-maintaining updates within `L₁` under `L₂` constraints.**

---

## 6. 与现有仓库表述的兼容方式

本文不否定仓库中关于“集体景观优先性”或“自由能景观”的现有写法，而是做一个更细的层级澄清：

1. 若某文把景观写成结构上“更原初”，应理解为：**在该局部 bridge 框架下，景观被当作组织化约束的有效起点**。
2. 这不等于在 SRT 全局本体论中，`L₂ = landscape`。
3. 同理，若某文把 Fisher 与选择成本紧密绑定，应理解为：**Fisher 给出局部可区分性与选择摩擦的几何表达**。
4. 这不等于在 SRT 全局本体论中，`L₁ = Fisher space`，也不等于 `Ψ_f = g_F` 的裸恒等式。

因此，仓库中的更稳读法应是：

- **ontology**：`L₀ / L₁ / L₂`
- **payability burden**：`Ψ_f`
- **local information geometry**：Fisher–Rao metric induced projection of `Ψ_f`
- **effective constraint picture**：landscape
- **local update rule**：FEP

五者互相连接，但不应被压扁成同一层。

---

## 7. 建议固定下来的四句话

1. **Fisher 主要描述现实生成前沿的局部几何。**
2. **`Ψ_f` 的 Fisher 表达是局部二阶信息几何投影，不是 `Ψ_f ≡ g_F` 的裸等号。**
3. **L₂ 不是景观图本身，而是景观图所压缩表达的稳定约束域。**
4. **FEP 不是选择本身的普遍本体论，而是某些组织化系统在既有约束场中的自维持动力学。**

---

## 8. 结论

因此，针对“能量景观和 FEP 能否看成 SRT 的 `L₂`，Fisher 空间能否看成 `L₁`，以及 `Ψ_f ≡ Fisher metric` 能否作为严格恒等式”这一问题，当前仓库更推荐的规范答案是：

> **可以把这种说法当成启发式类比或内部速记，但在正式写作中应改写为：Fisher 刻画 `L₀→L₁` 的局部选择几何，`Ψ_f` 的 Fisher 读法是由 Fisher–Rao metric 诱导的局部二阶信息几何代价或路径泛函，景观刻画 `L₂` 对 `L₁` 的有效约束投影，FEP 刻画组织化系统在该约束下的局部更新动力学。**

这样可以同时保留：

- SRT 的本体层级清晰性
- `Ψ_f` 的 payability 主读
- Fisher 的几何角色
- 景观的有效约束角色
- FEP 的局部动力学角色

避免把 ontology、cost、metric 和 dynamics 混成一层。
