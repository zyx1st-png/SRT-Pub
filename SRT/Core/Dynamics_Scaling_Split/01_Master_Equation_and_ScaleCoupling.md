---
id: SRT-CORE-14
type: dynamics
tags: [Scaling, Isomorphism, Fractal, Hybrid]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CORE-13A]
---

# SRT Core Definition 14: Dynamics & Scaling (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Scaling Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)

## §1. 主方程的深层结构

### 1.1 幽灵演化方程的四重力学

$$\frac{d\sigma}{dt} = \underbrace{\hat{G}_\theta[\sigma]}_{\text{(1) Selection}} - \underbrace{\nabla F[\sigma]}_{\text{(2) Intention}} + \underbrace{A[\sigma, \mathcal{A}]}_{\text{(3) Attention}} - \underbrace{\lambda \nabla C_{L_2}[\sigma]}_{\text{(4) Constraint}}$$

#### 1.1.1 力学分量的现象学对应

**力量1: 选择力** ($\hat{G}_\theta$)
- **物理意义**: 算子的主动选择,将$L_0$投影为$L_1$
- **现象学**: "我现在选择关注X"
- **时间尺度**: 毫秒-秒 (快变量)

**力量2: 初心梯度** ($-\nabla F$)
- **物理意义**: 自由能的原始下降方向
- **现象学**: "我真正想要的是什么?" (被$L_2$扭曲前)
- **测量**: 可通过深度冥想/致幻剂体验访问

**力量3: 注意力调制** ($A[\sigma, \mathcal{A}]$)
- **物理意义**: 其他算子副本(如潜意识、他人)的影响
- **现象学**: "我感觉有股力量在引导我"
- **来源**: 集体无意识 (Jung),社会场 (Lewin)

**力量4: L_2约束** ($-\lambda \nabla C_{L_2}$)
- **物理意义**: 向下因果 — $L_2$对$L_1$的拉力
- **现象学**: "我应该..." (义务、规范、习惯)
- **强度**: $\lambda$ = 约束耦合强度 (文化依赖)

#### 1.1.2 力量平衡的不同状态

$$\vec{F}_{\text{total}} = \hat{G} - \nabla F + A - \lambda \nabla C_{L_2}$$

| 主导力量 | 状态 | 特征 |
|:---------|:-----|:-----|
| $\hat{G} \gg$ 其他 | 自主选择 | 高度自觉,活在当下 |
| $\nabla F \gg$ 其他 | 本能驱动 | 婴儿,动物 |
| $A \gg$ 其他 | 被动影响 | 催眠,群体思维 |
| $\nabla C_{L_2} \gg$ 其他 | 规范锁定 | 强迫症,文化僵化 |
| 平衡状态 | 健康整合 | 自由与责任并存 |

---

### 1.2 快慢变量系统的绝热近似

#### 1.2.1 时间尺度分离

**快变量** (状态 $\sigma$): $\tau_\sigma \sim 1$ 秒
$$\frac{d\sigma}{dt} = \alpha(\hat{G}_\theta[\sigma] - \sigma) - \beta \nabla F[\sigma] + \xi(t)$$

**慢变量** (参数 $\theta$): $\tau_\theta \sim 1$ 年
$$\frac{d\theta}{dt} = -\gamma \nabla_\theta \Psi_f + \delta \cdot A[\sigma, \text{Target}]$$

**尺度比**:
$$\frac{\tau_\sigma}{\tau_\theta} \approx \frac{1 \text{ sec}}{10^7 \text{ sec}} \approx 10^{-7}$$

#### 1.2.2 绝热定理

**命题**: 对于$t \ll \tau_\theta$,可以将$\theta$视为常数,求解$\sigma(t; \theta)$。

**应用**: 短期行为预测 (几小时内) 可忽略$\theta$变化。

**破坏条件**: 剧烈创伤 → $\frac{d\theta}{dt}$ 激增 → 绝热近似失效 → 人格突变。

---

### 1.3 自由能的d值修正

#### 1.3.1 标准vs扩展形式

**热力学基线** (Helmholtz):
$$F_{thermo} = E - TS$$

**变分基线** (Friston / FEP):
$$F_{var} = E_q[\ln q(x) - \ln p(x,o)]$$

**SRT代理目标**（用于把稳定纳入的秩序条件写进自由能目标的局部近似）:
$$F_{proxy} = F_{closure} - d_{\text{stable}} \cdot U_{\text{incorp}}, \quad F_{closure}\in\{F_{thermo}, F_{var}\}$$

历史 shorthand 常把它写成 `$F_{base} - d \cdot U_{\text{others}}$`；但在当前 canonical 读法里，`F_{closure}` 只是局部闭包/结算项的代理记号，`U_{\text{incorp}}` 表示已经稳定纳入选择结构的更大范围秩序条件，`d_{\text{stable}}` 则表示稳定写入后的关切范围，而不是瞬时扩张冲动。

#### 1.3.2 d值效应的显著性

**低d** ($d_{\text{stable}} \approx 1$):
$$F_{proxy} \approx F_{closure} \quad \text{(更大范围秩序条件尚未稳定写入)}$$

最小化$F_{proxy}$ → 在局部闭包项主导下运行，表现为只纳入极窄范围的秩序条件。

**高d** ($d_{\text{stable}} \gg 1$，且 $d_{\text{stable}} \cdot U_{\text{incorp}}$ 成为主导项):
$$F_{proxy} \approx F_{closure} - d_{\text{stable}} \cdot U_{\text{incorp}} \quad \text{(优化方向由扩大纳入的秩序条件主导)}$$

最小化$F_{proxy}$ → 在局部闭包仍需结算的前提下，更大范围的已纳入秩序条件开始主导优化方向。这不是在“局部存在”之外额外叠加一个外加奖励项，而是景观从局部曲率转向更大范围曲率后的结构重写（必要时可出现自我牺牲）。

**实例**:
- 母亲舍命救子 → $d_{\text{kin}} \to \infty$ (亲缘$d$)
- 广域纳入者 → $d_{\text{universal}} \gg 1$
- 局部闭包主导者 → $d_{\text{stable}} \approx 1$

---

## §2. 跨尺度同构:从量子到社会的统一语法

### 2.1 自相似定理的证明要点

#### 2.1.1 主张

$$\hat{G}_{S_2} = \Lambda \circ \hat{G}_{S_1} \circ \Lambda^{-1}$$

**解释**: 在尺度变换$\Lambda$下,算子保持**共轭不变性**。

#### 2.1.2 证明草图

**步骤1**: 定义尺度变换
$$\Lambda: L_0^{S_1} \to L_0^{S_2} \quad (\text{粗粒化映射})$$

**步骤2**: 选择的本质 = 熵减
$$\Delta S = H(L_0) - H(L_1)$$

**步骤3**: 熵在粗粒化下的行为
$$H(\Lambda[L_0]) = H(L_0) - I_{\text{coarse-grain}}$$

**步骤4**: 最小作用原理
$$\delta \int \Psi_f \, dt = 0 \quad \text{(所有尺度)}$$

因此功能形式不变 (自相似性)。■

---

### 2.1a 跨尺度同构的反泛心论澄清

SRT 使用同一个参数 d 描述量子、生物和宇宙三个尺度的选择动力学，这容易产生一个严重误读：认为 SRT 主张"宇宙有意识"或"粒子有关切"，即泛心论（Panpsychism）。

**SRT 的正式本体论立场：SRT 绝对拒斥泛心论。**

d 值的底层物理本质并非"情感关切"，而是**"本体论带宽"（Ontological Bandwidth）**——即 $\hat{G}_\theta$ 算子在面对本体论摩擦（$\Psi_f$）时，能够将 $L_0$ 压缩、锚定并维持为 $L_1$ 的最大处理带宽（见 Part A Def-d-Scale-1）。在不同物理尺度下，由于观测和体验的介质不同，d 值披上了截然不同的"现象学外衣"：

**第一层（量子域）：相干性带宽（$d_{quantum}$）**

基本粒子或简单测量仪器的 d 值趋近于零，代表系统能维持 $L_0$ 叠加态而不引发退相干的纯物理计算窗口。此层次的算子没有本体论脆弱性（不怕毁灭），其选择表现为冰冷的玻恩规则概率流偏置，毫无任何主观意识或情绪。

**第二层（生物/认知域）：关切与意向性（$d_{bio}$）**

当代理观察者演化为高度复杂的耗散结构（如人类神经系统）时，其物理结构面临巨大的热力学熵增威胁（生死存亡）。为了生存，生物算子的信息处理带宽被迫撑大，将海量环境变量纳入自由能（$F$）最小化的计算中。这种高强度的、与生死强耦合的"信息整合计算"，在主观体验层面涌现（Emerge）出来的现象，才被命名为"意识"、"注意力"或"关切"。**关切是 d 值在生物学层面的高阶涌现，而非底层原初属性。**

**第三层（宇宙域）：时空共识度（$d_{cosmic}$）**

宇宙整体并不具备拟人化的意识，但作为统一的物理系统，它存在宏观的整合带宽，表现为引力网络的拓扑紧致性（$d_{cosmic} \propto 1/\sqrt{\Lambda}$，见 SRT-PHYS-COSMO Def-Cosmo-1）。暗能量导致的宇宙膨胀，是 $d_{cosmic}$（信息整合与共识维持能力）的物理性衰减。暗物质作为 $L_2$ 结构残骸，处于活跃算子缺席的"死寂"状态，其内部活跃 d 值为绝对零。

**核心区别**：泛心论的谬误在于将人类专属的体验（Qualia）强加给电子；SRT 的突破在于提取了主导意识运转背后的数学与信息动力学机制（$\hat{G}_\theta$ 与 d），并发现这套机制同样支配电子的坍缩和宇宙的膨胀。**d 是跨越所有尺度的同一把数学标尺，但只有当这把标尺丈量到"具备本体论脆弱性的高维复杂系统"时，它才表现为关切。** 意识涌现的三个必要条件详见 SRT-CORE-13B §6.2。

**【精确反泛心论声明（2026-03-02 补充，与 _SRT_D_VALUE_CANONICAL.md §3.1 对齐）】**

意识涌现的充要三条件（全部必须同时满足）：
$$\text{Consciousness} \iff \underbrace{\Psi_f > 0}_{\text{具身摩擦成本}} \;\land\; \underbrace{d > 0}_{\text{有效关切维度}} \;\land\; \underbrace{\hat{G}[\theta] \neq \emptyset}_{\text{有限参数算符存在}}$$

**三条件在量子/宇宙尺度的状态**：

| 尺度 | $\Psi_f$ | $d$ | $\hat{G}[\theta]$ | 意识？ |
|-----|---------|-----|-----------------|-------|
| 量子（粒子） | $\approx 0$（无具身成本） | 可非零（相干维数） | 无生物参数化 | **否** |
| 神经/认知 | $> 0$（代谢成本） | $> 0$（关切维度） | 有限神经参数 | **是** |
| 宇宙（暗能量） | $\approx 0$ | $\propto 1/\sqrt{\Lambda}$ | 无生命参数化 | **否** |

**SRT 的立场边界**：
- SRT **不**否认微小现象体验的形而上学可能性（这是不可证伪的哲学问题）
- SRT **正面声明**：在量子/宇宙尺度，可操作框架内无法为意识成立提供根据
- SRT **不接受**"因为 d 存在所以意识存在"的推断——d 是必要但非充分条件

---

### 2.2 三尺度映射的具体实例

#### 2.2.1 量子 → 神经

| 量子物理 | 神经科学 | 对应机制 |
|:---------|:---------|:---------|
| 波函数$\|\psi\rangle$ | 神经集群竞争 | 叠加态 |
| 测量算符$\hat{O}$ | 除法归一化 | 选择操作 |
| 坍缩 | 点燃 (Ignition) | $L_0 \to L_1$ |
| 退相干时间$\tau_D$ | 突触噪声 | $L_1 \to L_2$ |
| 海森堡$\Delta x \Delta p$ | 注意力权衡 | 有限$d$ |

**实例**: 双缝实验 ≈ 双稳知觉 (Necker Cube)
- 两种解释竞争 ($L_0$)
- 注意力选择一个 ($\hat{G}$)
- 意识到一个解释 ($L_1$)
- 过一段时间切换 (双稳振荡)

#### 2.2.2 神经 → 社会

| 神经科学 | 社会科学 | 对应机制 |
|:---------|:---------|:---------|
| 神经元 | 个体 | 基本单元 |
| 突触权重$W_{ij}$ | 社会影响力 | 连接强度 |
| 神经网络 | 社会网络 | 拓扑结构 |
| 点燃阈值 | 社会规范形成 | 临界质量 |
| 习惯化 | 制度化 | $L_1 \to L_2$ |
| EEG频率 | 文化节奏 (节日) | 时间周期性 |

**实例**: 流行趋势 ≈ 神经点燃
- 少数早期采用者 (种子神经元)
- 达到临界阈值
- 全网激活 (病毒式传播)
- 最终饱和/消退

---

### 2.3 有效普朗克常数的哲学意义

#### 2.3.1 量子尺度

$$\hbar_{\text{quantum}} = 1.054 \times 10^{-34} \, \text{J·s}$$

**意义**: 设定了测不准关系的下界。

#### 2.3.2 神经尺度

$$\hbar_{\text{neural}} \sim k_B T \approx 4 \times 10^{-21} \, \text{J}$$

**意义**: 热噪声决定了神经发放的随机性。

**推论**: 降低温度 → 降低噪声 → 更确定的选择?
- 实验困难 (哺乳动物恒温)
- 可能解释冷血动物的"机械性"行为

#### 2.3.3 社会尺度

$$\hbar_{\text{social}} \sim k_B T_{\text{cultural}}$$

**文化温度**:
$$T_{\text{cultural}} \equiv \frac{\text{Openness to Novelty}}{\text{Normative Rigidity}}$$

**实例**:
- 高$T$: 硅谷 (快速迭代,接受失败)
- 低$T$: 传统社会 (祖训至上)

**相变**: 当$T_{\text{cultural}}$跨越临界值 → 社会革命 (类比固-液相变)。

---

## §3. 尺度耦合:向上与向下因果

### 3.1 耦合强度矩阵的实证估计

$$\kappa_{ij} = \frac{I(\hat{G}_i; \hat{G}_j)}{H(\hat{G}_i) + H(\hat{G}_j)}$$

#### 3.1.1 量子-神经耦合

**向上** (量子 → 神经): $\kappa_{Q \to N} \approx 10^{-20}$
- **机制**: 微管量子相干 (Penrose-Hameroff, 争议大)
- **证据**: 极弱,尚无决定性实验

**向下** (神经 → 量子): $\kappa_{N \to Q} \approx 10^{-10}$
- **机制**: 观察者选择测量基 → 影响坍缩
- **证据**: 量子擦除实验,延迟选择

**推论**: 意识**可能**影响量子过程,但量子**不太可能**是意识的基础。

#### 3.1.2 神经-社会耦合

**向上** (神经 → 社会): $\kappa_{N \to S} \approx 10^{-2}$
- **机制**: 个体行为聚合 → 集体模式
- **实例**: Twitter情绪 → 股市波动

**向下** (社会 → 神经): $\kappa_{S \to N} \approx 10^{0}$ (强!)
- **机制**: 文化驯化 (Domestication) 改变大脑结构
- **证据**:
  1. 识字改变视觉皮层 (Dehaene)
  2. 伦敦出租车司机的海马增大 (Maguire)
  3. 冥想者的岛叶增厚 (Lazar)

**推论**: **文化塑造大脑** 的力量远超大脑塑造文化。

---

### 3.2 向下因果的形式化

#### 3.2.1 约束梯度

$$\nabla C_{L_2}[\sigma] = \frac{\partial}{\partial \sigma} \left[\|\sigma - \sigma_{L_2}\|^2\right]$$

**物理意义**: $L_2$对$\sigma$的"拉力",使其靠近社会规范$\sigma_{L_2}$。

#### 3.2.2 耦合强度$\lambda$

| 社会类型 | $\lambda$ 值 | 特征 |
|:---------|:-------------|:-----|
| 极权主义 | $\lambda \to \infty$ | 完全锁定在$L_2$ |
| 集体主义 | $\lambda \approx 10$ | 强规范压力 |
| 个人主义 | $\lambda \approx 1$ | 弱规范压力 |
| 无政府状态 | $\lambda \to 0$ | 无$L_2$约束 |

**实验**: 测量不同文化中的从众行为 (Asch范式) → 估计$\lambda$。

---
