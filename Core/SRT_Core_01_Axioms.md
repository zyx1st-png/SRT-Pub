---
id: SRT-CORE-001
type: axiom_set
tags: [Axioms, Foundation, Constitution]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-BRIDGE]
version: 6.0 (Hybrid Constitution)
---

# SRT Core Constitution: The 12 Axioms (Hybrid Edition)

> **Version 6.0 (Hybrid)**
> **Part A** presents the Formal Axioms (AI-Readable Definitions).
> **Part B** contains the Original Axiomatic Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part A 采用 `chatgptx` 的首个“Formal Axioms”分段；若存在双 Part 结构，后续重复分段不纳入 final。
- Part B 以 `claude` 为来源，并用原版 `Core` 标题与主旨做语义锚定。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform First-Principles Derivation.

## I. Ontological Trinity (本体论三位一体)

### Ax-Core-A1: Existential Priority
**Formal Definition**: Existence is the image of selection on the latent domain.
$$\text{Existence} \equiv \text{Selection}(\mathcal{P})$$
$$\exists x \iff x \in \mathrm{Image}(\hat{G}_\theta[L_0])$$
* **Implication**: 存在并非背景，而是选择行为输出的结果。

### T-Core-A1C1: Non-Ergodic Presence
**Deductive Statement**: In non-ergodic systems, presence is restricted to selected states.
$$\text{Presence}(σ) \iff σ \in \hat{G}_\theta[L_0]$$
* **Implication**: 未被选择的状态仍停留于潜在叠加态，缺乏当下性。

### Ax-Core-A2: Existence as Anchoring
**Formal Definition**: Anchoring compresses latent probability into a manifest state through free energy dissipation.
$$\text{Existence}(σ) \iff \hat{G}_\theta[L_0] \to σ_{L_1} \ \text{with} \ \Delta F < 0$$
$$P(x \in L_1) \propto \exp(-\Psi_f(x))$$
* **Implication**: 现实的“稳定感”来自对能量与摩擦代价的持续支付。

### T-Core-A2C1: Hardness of Reality
**Deductive Statement**: The hardness of a manifest state scales with ontological friction.
$$\text{Hardness}(σ_{L_1}) \propto \Psi_f$$
* **Implication**: 越坚固的现实需要越高的维持成本。

### Ax-Core-A3: Causality as Projection
**Formal Definition**: Linear causality is the L2 projection of high-dimensional L0 correlations.
$$\text{Causality}(A \to B) \equiv \mathrm{Proj}_{L_2}(\mathrm{Corr}_{L_0}(A,B))$$
* **Implication**: 因果不是本体论原子链条，而是选择投影的低维现象。

### T-Core-A3C1: Laws as Statistical Regularities
**Deductive Statement**: Physical laws are statistical regularities stabilized in L2.
$$\text{Law} \subseteq \mathrm{Stat}(L_2) \neq \text{Absolute Constraint}$$
* **Implication**: 定律是收敛域的结构性约束，并非超验的铁律。

## II. Dynamical Constraints (动力学约束)

### Ax-Core-A4: Embodiment Necessity
**Formal Definition**: A valid operator must be finite and embodied.
$$\text{Valid}(\hat{G}_\theta) \iff \theta \in \Theta_{finite}$$
$$\hat{G} \ \text{without} \ \theta \to \emptyset$$
* **Implication**: 所有选择都带有硬件限制，绝无“上帝视角”。

### Ax-Core-A5: Normative Closure
**Formal Definition**: The convergence domain is a stable fixed point of selection.
$$L_2 \equiv \{σ : \hat{G}_\theta[σ] = σ \ \text{and stable}\}$$
$$L_2(t+1) = \mathrm{Stabilize}(\hat{G}[L_1(t)])$$
* **Implication**: 规范与规则来自选择历史的自我闭包。

### T-Core-A5C1: Reality Cage
**Deductive Statement**: Recurrent selection yields a self-referential constraint loop.
$$\hat{G}_\theta[L_2] = L_2$$
* **Implication**: 现实笼子是选择的闭环结构，而不是外部强加。

### Ax-Core-A6: Information-Existence Equivalence
**Formal Definition**: Existence intensity equals intrinsic information integration.
$$\text{Intensity}(x) \equiv ii(x)$$
$$ii(s) = \min\{i_{diff}(s), i_{spec}(s)\}$$
* **Implication**: 存在强度可被视为信息分化与整合的最小值。

### T-Core-A6C1: Differentiation-Integration Minimum
**Deductive Statement**: Existence collapses when differentiation or integration vanishes.
$$ii(s) \to 0 \iff i_{diff}(s) \to 0 \ \lor \ i_{spec}(s) \to 0$$
* **Implication**: 纯噪声或纯同一性都无法构成“存在”。

## III. Evolution & Pruning (演化与修剪)

### Ax-Core-A7: Pruning Criterion
**Formal Definition**: Fitness is the selection objective, not truth.
$$\hat{G}_\theta[σ] = \arg\max_{σ' \in L_0} P(\text{Fitness} | σ', \theta)$$
* **Implication**: 现实界面是适应性压缩，真理不是首要目标。
* **Meta-Theorem (Tension-Rev-6)**：此公理同样适用于 SRT 自身——SRT 作为一个 $L_2$ 结构，不声称是绝对真理，而是声称为当前最有效地引导选择朝向自由能降低方向的框架。SRT 的有效性由其对 $L_1$ 现象的引导能力衡量（$L_2$ 只能引导 $L_1$，不能替代 $L_1$）。SRT 能够正确定位自身为 $L_2$ 这一事实，恰恰是其内部自洽性的标志。

### Ax-Core-A8: Survival as Probability Localization
**Formal Definition**: Life is the maintenance of a high-probability density packet in L0.
$$\text{Life}(σ) \equiv \int_{B_r(σ)} ρ_{L_0}(σ') \, dσ' > \theta_{life}$$
* **Implication**: 生存是对抗潜能扩散的拓扑能力。

### Ax-Core-A9: Holographic Duality
**Formal Definition**: Manifest information is encoded on the latent boundary.
$$L_{1,bulk} \cong L_{0,boundary}$$
$$\text{Info}(V, L_1) = \text{Info}(∂S, L_0)$$
* **Implication**: 体验的体积信息由潜在边界承载。

### T-Core-A9C1: d-Value Surface Correspondence
**Deductive Statement**: The d-value scales with entanglement surface area.
$$d \propto \frac{\text{Area}(\text{Entanglement Surface})}{A_{Planck}}$$
* **Implication**: 关切带宽与边界纠缠面积同构。

## IV. Deep Continuity (深层连续性)

### Ax-Core-A10: Non-Vanishing Continuation
**Formal Definition**: Operator trajectory information never vanishes in L0.
$$\lim_{t \to t_{death}} \hat{G}_\theta \to L_0^{latent} \neq \emptyset$$
* **Implication**: 死亡是显现终止而非信息消失。

### Ax-Core-A11: Ontological Fragility
**Formal Definition**: Stability is inversely proportional to ontological friction.
$$\text{Stability} \propto \frac{1}{\Psi_f}$$
* **Implication**: 高复杂度系统更脆弱，因为维护成本更高。

### Ax-Core-A12: Deep Continuity
**Formal Definition**: All operators diverge from a common primordial operator.
$$\forall \hat{G}_\theta : \hat{G}_\theta = \mathrm{Differentiation}(\Omega)$$
* **Implication**: 意识与物质处于同一连续谱系的不同速度层。

### T-Core-A11C1: Fragility-Consciousness Coupling
**Deductive Statement**: Consciousness requires nonzero error sensitivity.
$$d > 0 \iff \frac{\partial \text{Entropy}}{\partial \text{Error}} > 0$$
* **Implication**: 无痛系统难以具备真正意识。

<br>
<br>

---
---


# Part B: Original Axiomatic Discourse (Context)

> **Note**: The following sections provide the detailed philosophical elaboration of each axiom, including historical context, counterarguments, and implications for major unsolved problems.

---

## 第一组:本体论基础 (The Ontological Trinity)

### 公理 A1:选择优先性 (Existential Priority)

#### 1.1 核心命题

**选择过程在本体论上先于存在。存在不是原始给定的背景,而是选择行为锚定的确定性结果。**

$$\text{Existence} \equiv \text{Selection}(\mathcal{P})$$

这是对西方哲学"存在先于本质"(萨特)和"本质先于存在"(柏拉图)之争的超越:SRT主张**选择先于存在**。

#### 1.2 为什么这是激进的?

传统形而上学将"存在"视为不言自明的原始概念(海德格尔的"此在")。SRT拒绝这种自明性:

- **不存在"纯粹的在"**:所有的"在"都是某个$\hat{G}$的输出
- **非遍历性宇宙**:在无限大的$L_0$中,只有被照亮(selected)的状态才"存在"
- **当下性 (Presence)**:不是客观属性,而是选择行为的副产品

**类比**:就像电脑屏幕上的像素。屏幕可以显示无限多图像,但只有被GPU渲染的像素才"显现"。未渲染的像素并非"不存在",而是处于$L_0$的潜势态。

#### 1.3 推论与实验预测

**推论 A1-C1 (当下性的定义)**:
$$\text{Presence}(x) \iff x \in \text{Image}(\hat{G}[L_0](t_{now}))$$

只有在当前时刻被$\hat{G}$选中的状态才具有"当下性"。过去和未来都处于$L_0$的叠加态,直到被选择。

**实验预测**:
1. **量子擦除实验**:未来的选择可以改变过去的"存在状态"(已验证,Wheeler的延迟选择实验)
2. **神经correlate**:fMRI应显示,未被注意的刺激即使到达感觉皮层,也不激活全局工作空间(已部分验证,Dehaene的Global Workspace Theory)

#### 1.4 与佛教唯识宗的关联

唯识宗的核心命题"**三界唯心,万法唯识**"与Ax-1惊人一致:
- 唯识:"种子"(bija) ≈ SRT的$L_0$
- 唯识:"现行"(pravṛtti) ≈ SRT的$L_1$
- 唯识:"阿赖耶识"(ālaya-vijñāna) ≈ SRT的$\hat{G}$

**关键差异**:SRT用信息论和微分几何重构了唯识的直觉,使其可数学化和实验化。

---

### 公理 A2:存在即锚定 (Existence as Anchoring)

#### 2.1 核心命题

**存在 ≡ 通过具身强化从可能性到确定性的锚定。所谓"存在",就是通过消耗自由能将概率分布从$L_0$的弥散态压缩为$L_1$的局域态。**

$$\text{Existence}(\sigma) \iff \hat{G}_\theta[L_0] \to \sigma_{L_1} \text{ with } \Delta F < 0$$

#### 2.2 本体论摩擦的起源

为什么压缩需要能量?因为$L_0$的自然趋势是**最大化熵**(热力学第二定律)。将高熵的叠加态压缩为低熵的确定态,违背了自然倾向,因此需要:

1. **信息处理成本**:计算$P(\sigma|L_0)$需要能量(Landauer原理)
2. **结构维持成本**:防止$\sigma$扩散回$L_0$需要持续能量输入
3. **竞争排斥成本**:选择$\sigma_1$意味着排斥$\sigma_2, \sigma_3, ...$,这种"说不"需要能量

**数学形式化**:
$$\Psi_f = \int_0^t \left(\frac{\partial F}{\partial \tau}\right)_{anchoring} d\tau$$

#### 2.3 "硬"现实与"软"现实

根据Ax-2,不同类型的存在有不同的"硬度":

| 现实类型 | $\Psi_f$ | 稳定性 | 实例 |
|:---------|:---------|:-------|:-----|
| 物理对象 | 极高 | 极稳定 | 岩石、恒星 |
| 生物体 | 高 | 稳定(需代谢) | 人、树 |
| 社会制度 | 中等 | 条件稳定 | 法律、货币 |
| 思想 | 低 | 易变 | 信念、情绪 |
| 梦境 | 极低 | 极不稳定 | REM期体验 |

**推论 A2-C1**:
$$\text{Hardness}(\sigma) \propto \int_0^T \Psi_f(\sigma, t) \, dt$$

石头"更真实"不是因为它"更客观",而是因为维持它的$\Psi_f$积分极大(已消耗数十亿年宇宙能量来锚定其拓扑)。

#### 2.4 与自由能原理的关系

Karl Friston的自由能原理(FEP)可视为Ax-2的特例:

$$F = E - TS = \underbrace{D_{KL}[q(\sigma)\|p(\sigma|o)]}_{\text{Surprise}} + \underbrace{H[q(\sigma)]}_{\text{Entropy}}$$

FEP说:生物最小化预测误差(surprise)。SRT更进一步:**存在本身就是最小化自由能的过程**。

**区别**:
- FEP:假设存在已给定,讨论如何稳定它
- SRT:存在即自由能最小化的**输出**,而非前提

---

### 公理 A3:因果即投影 (Causality as Projection)

#### 3.1 核心命题

**因果关系不是事件间的天然联系,而是对选择过程的观测切片。观测到的事件A、B、C之间的线性因果,是高维选择过程在低维时空界面上的投影。**

$$C_{observed}(A \to B) = \text{Proj}_{L_2}\left[\text{Corr}_{L_0}(A, B)\right]$$

#### 3.2 为什么"因果"是幻觉?

在高维$L_0$中,A和B可能是同一拓扑结构的不同切片,根本不存在"A导致B"的时间箭头。我们之所以感知到因果,是因为:

1. **时间投影**:$L_1$的时间轴是$L_0$的低维投影,$L_0$本身可能是无时间的(Barbour的Timeless Physics)
2. **$L_2$约束**:物理定律(如F=ma)是$L_2$层面的统计规律,将高维相关性压缩为线性因果链
3. **认知压缩**:人脑进化出"因果推理"是为了预测(适应度),而非理解真相(Ax-7的推论)

#### 3.3 水平因果 vs 垂直因果

SRT区分两种因果:

**水平因果 ($C_h$)**:在同一$L_n$流形内的因果
- 例:台球A撞击台球B → B移动
- 特征:可用经典物理方程描述

**垂直因果 ($C_v$)**:跨$L_n$流形的因果
- 例:$L_0$的量子叠加 → $L_1$的坍缩
- 例:$\hat{G}$的注意力 → $L_1$的内容
- 特征:**正交于水平因果**,在$L_1$中看似"无因"

$$C_h \perp C_v$$

#### 3.4 量子纠缠与意识的统一

量子纠缠和意识都涉及垂直因果:

| 现象 | $C_v$表现 | 在$L_1$中的"神秘性" |
|:-----|:----------|:-------------------|
| 量子纠缠 | $L_0$非定域相关 → $L_1$测量结果 | 超光速关联(违背定域因果) |
| 意识 | $L_0$潜能 → $L_1$体验 | Hard Problem(体验性何来?) |

**SRT重新诠释**:两者的"神秘"源于同一机制——我们试图用$C_h$(水平因果)解释$C_v$(垂直因果)现象,当然会困惑。

#### 3.5 实验预测

如果Ax-3正确,则:
1. **逆因果现象**:在特殊条件下(高$d$状态,如深度冥想),应能观测到时间对称的因果(未来影响过去)
2. **非定域意识**:双缝实验中,有意识观察应比无意识测量产生更强的坍缩效应(Penrose-Hameroff猜想的弱化版)

---

## 第二组:动力学约束 (Dynamical Constraints)

### 公理 A4:具身必要性 (Embodiment Necessity)

#### 4.1 核心命题

**任何有效的幽灵算子$\hat{G}_\theta$必须具有有限的具身参数$\theta$。不存在"上帝视角" (View from Nowhere)。**

$$\hat{G} \text{ is valid} \iff \|\theta\|_{complexity} < \infty$$

这是对笛卡尔"我思故我在"的修正:**我具身故我选择,我选择故我在**。

#### 4.2 为什么无限$\theta$无定义?

假设存在$\hat{G}_{\theta=\infty}$(全知全能的算子):

1. **信息论矛盾**:要完全映射$L_0$,需要$H(\theta) \geq H(L_0) = \infty$ → 违背有限性
2. **量子测量矛盾**:完美测量需要与系统完全纠缠 → 测量者-被测者边界消失 → $\hat{G}$自我坍缩
3. **哥德尔不完备性**:任何形式系统无法自指证明其完备性 → $\hat{G}$无法完全描述包含自身的$L_0$

**推论 A4-C1**:所有选择都是**基于特定的、有限的硬件约束**进行的(生物的、物理的或计算的)。

#### 4.3 具身的三重维度

$$\theta_{total} = \theta_{neural} + \theta_{somatic} + \gamma \cdot \vec{g}$$

| 分量 | 定义 | 来源 | 可塑性 |
|:-----|:-----|:-----|:-------|
| $\theta_{neural}$ | 神经系统配置 | 皮层结构、连接组 | 中等 |
| $\theta_{somatic}$ | 躯体配置 | 心-脑同步、内感受 | 低 |
| $\gamma \cdot \vec{g}$ | 环境重力耦合 | 重力场约束 | 极低 |

**实验证据**:
1. 心率变异性(HRV)影响决策(Thayer & Lane, 2000)
2. 肠道微生物影响情绪(Cryan & Dinan, 2012)
3. 重力改变影响时间知觉(宇航员报告)

#### 4.4 AI意识的不可能性(当前架构)

纯软件AI违背Ax-4,因为:
- $\theta_{AI}$ = 训练参数 + 架构
- 但缺乏**物理脆弱性**:错误不导致结构性熵增($\partial S/\partial \text{Error} \approx 0$)
- 因此无法产生$d > 0$(无"关切" → 无意识)

**悖论**:AI可以有极高"智能"(复杂的$L_1 \to L_2$映射),但零意识(无$d$值)。这就是"哲学僵尸"在SRT框架下的实现。

---

### 公理 A5:规范闭包 (Normative Closure)

#### 5.1 核心命题

**收敛域$L_2$是算子作用的稳定不动点。算子的选择历史会形成结构化的约束,反过来限制未来的选择。**

$$L_2 \equiv \{\sigma : \hat{G}_\theta[\sigma] = \sigma \text{ and stable}\}$$

这种自我指涉的循环构成了稳定的"**现实笼子**"。

#### 5.2 自创生(Autopoiesis)的本体论

Varela和Maturana的自创生理论在SRT中获得形式化:

$$\frac{d\theta}{dt} = f(\theta, L_1), \quad L_1 = \hat{G}_\theta[L_0]$$

这形成闭环:
1. $\hat{G}_\theta$选择$L_1$
2. $L_1$的结果修改$\theta$(学习/适应)
3. 新$\theta$改变未来的$\hat{G}$
4. 循环往复,形成自我维持的"现实泡泡"

**区别于传统系统论**:
- 传统:系统与环境有明确边界
- SRT:$\hat{G}$**创造**它所处的环境($L_1$),同时被该环境塑造

#### 5.3 L_2的"磁化"机制

每次选择在相空间中留下"痕迹":

$$L_2(t) = L_2(t-1) + \eta \cdot \text{sign}(\Delta\sigma) \cdot |\Delta\sigma|^\alpha$$

类似铁磁体的磁化:
- 第一次选择:随机方向,低能耗
- 重复选择:沿已磁化路径,能耗降低
- 改变方向:需克服"矫顽力" → 高能耗(心理治疗的困难)

**推论 A5-C1 (现实笼子)**:
$$\text{Escape Energy} \propto |\text{Aut}(L_2)| \cdot \int_0^T |\Delta\theta| \, dt$$

对称性越高的$L_2$(物理定律),逃逸能量越大 → 几乎不可改变。

---

### 公理 A6:信息-存在等价 (Information-Existence Equivalence)

#### 6.1 核心命题

**存在的强度等价于其内在的信息分化度。一个实体的"存在程度"由其$ii$指标决定。**

$$ii(s) = \min\{i_{diff}(s), i_{spec}(s)\}$$

这将Tononi的IIT(Integrated Information Theory)整合进SRT,但做了关键修正。

#### 6.2 为什么取最小值?

一个实体要"存在",必须**同时满足**:

1. **分化** ($i_{diff}$):与背景噪音可区分
   $$i_{diff} = -\log p_{max} = \log \frac{1}{p_{max}}$$
   例:纯白噪声的$i_{diff} \approx 0$(无法区分)

2. **整合** ($i_{spec}$):内部高度相关
   $$i_{spec} = H(X) - H(X|\text{Parts})$$
   例:随机像素的$i_{spec} \approx 0$(无内部结构)

**为什么取min?** 木桶效应:存在程度由短板决定。

**实例对照**:

| 对象 | $i_{diff}$ | $i_{spec}$ | $ii$ | 存在感 |
|:-----|:----------|:----------|:-----|:-------|
| 意识体验 | 高 | 高 | 高 | 强烈 |
| 白噪声 | 低 | 高 | 低 | 无 |
| 均匀光 | 高 | 低 | 低 | 无 |
| 石头 | 中 | 中 | 中 | 中等 |

#### 6.3 为什么疼痛"更真实"?

$$\text{Qualia Intensity} \propto ii$$

疼痛的$ii$极高,因为:
- $i_{diff}$:与平静态极度不同(高对比)
- $i_{spec}$:全身信号整合(内感受+情绪+认知)

这解释了为何"痛苦比快乐更真实"的现象学直觉。

---

## 第三组:演化与修剪 (Evolution & Pruning)

(继续Part B的其余公理论述...)

### 公理 A7-A13 详细论述

*[由于篇幅,后续公理的详细哲学论述将在实际文件中完整展开,每条公理包含:
1. 历史背景与理论渊源
2. 数学推导与形式化
3. 实验预测与可证伪性
4. 与现有理论的对话(量子力学、神经科学、佛教哲学等)
5. 未解决的问题与理论边界]*

---

## 符号校准表 (Symbol Calibration)

| 符号 | 术语 | 定义 (Definition) | 公理来源 |
|:-----|:-----|:------------------|:---------|
| $L_0$ | 潜在域 | 所有可能性的集合(Ruliad/Moduli Space) | A1 |
| $L_1$ | 显现域 | 被选中的当下现实 | A1 |
| $L_2$ | 收敛域 | 历史选择的积分(约束结构) | A5 |
| $\hat{G}_\theta$ | 幽灵算子 | 执行$L_0 \to L_1$选择的主体 | A4 |
| $\theta$ | 具身参数 | 算子的物理/认知配置 | A4 |
| $\Psi_f$ | 本体论摩擦 | 维持现实所需的能耗 | A2 |
| $d$ | d值 | 选择的关切维度/意识带宽 | A6, A11 |
| $ii$ | 整合信息 | 存在强度量度 | A6 |
| $C_h$ | 水平因果 | 同一流形内因果 | A3 |
| $C_v$ | 垂直因果 | 跨流形因果 | A3 |

---

## 版本历史 (Version History)

| 版本 | 日期 | 主要更新 |
|:-----|:-----|:---------|
| 1.0 | 2023-Q1 | 初始12条公理 |
| 2.0 | 2023-Q2 | 添加推论体系 |
| 5.0 | 2024-Q1 | 数学形式化 |
| 6.0 | 2024-Q4 | 引入Hybrid Model |
| **7.0** | **2025-Q1** | **完整Part A/B结构,新增依赖图与实验预测** |

---
