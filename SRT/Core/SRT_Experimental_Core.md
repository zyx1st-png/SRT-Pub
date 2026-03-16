---
id: SRT-EXP-CORE
type: experiment
tags: [Hypothesis, Falsification, Design, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-21, SRT-CORE-22]
---

# SRT Experimental Core: Hypotheses I (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Experimental Axioms (AI-Readable).
> **Part B** contains the Original Hypothesis Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)


## I. Ontological Detectability (本体论可检测性)

### Ax-Exp-01: Selection Beyond L₂ Determination (超越 L₂ 决定性的选择)
**Formal Definition**: If organism behavior is fully determined by brain $L_2$ patterns alone (without irreducible contribution from embodied $L_0$ interaction), SRT's $\hat{G}_\theta$ concept is redundant.
$$P(\text{Behavior}|\text{Brain}_{L_2}) < 1 \Rightarrow \exists \ \hat{G}_\theta^{embodied}$$
* **Implication（中文）**：大脑层面的因果闭合与 SRT 完全兼容——大脑作为 $L_2$ 天然因果封闭。需要检测的不是"大脑是否违反物理定律"，而是"有机体整体的选择行为是否仅由大脑 $L_2$ 模式决定，还是受到具身 $L_0$ 交互的不可约贡献"。
* **Falsification（证伪条件）**：若给定完整的大脑状态（突触权重 + 实时神经活动），有机体行为可被 100% 预测，且具身变量（内感受、代谢状态、环境交互）不提供额外预测信息，则 $\hat{G}_\theta$ 作为超越 $L_2$ 的概念失去必要性。

---

### T-Observer-Bias: Probabilistic Over-interpretation (观察者过度解读定理)
观察者 $\hat{G}_{obs}$ 在被观察对象中"发现"虚假意义的概率：
\[
P(\text{Over-interpret}) = \sigma\!\left(\alpha \cdot d_{obs} + \beta \cdot H(L_0^{target}) - \gamma \cdot E_{grounding}\right)
\]
- $d_{obs}$：观察者的寻找意义渴望（越高越容易过度解读）
- $H(L_0^{target})$：被观察对象的熵/随机性（越混乱越容易被投射）
- $E_{grounding}$：实验验证的接地能量（抑制项）

* **Implication（中文）**：解释了为何研究人员（高 $d_{obs}$）面对死鲑鱼fMRI噪声（高 $H$）且缺乏严谨基线（低 $E_{grounding}$）时，会产生高概率的解释性幻觉。

### Ax-Exp-02: Information Mass
**Formal Definition**: Information erasure carries energetic mass equivalence.
$$\Delta E \ge k_B T \ln 2 \quad (\text{Landauer–Vopson})$$
* **Implication**: 信息具有物理性，L1 不是纯语义层。

## II. Biological Signatures (生物学签名)

### Ax-Exp-03: Contextual Decoherence Weighting（情境退相干加权公理）

**Formal Definition**：生命系统通过具身参数 $\theta$ 构建特定的**热力学边界条件**，从而在与非生命惰性物质相同的量子态上产生统计显著不同的退相干通道权重：

$$P(\text{decoherence channel } k \mid \theta_{bio}) \neq P(\text{decoherence channel } k \mid \theta_{inert})$$

**机制链条（θ → 退相干偏置）**：

$$\theta_{bio} \xrightarrow{\text{encodes}} H_{env}^{(\theta)} \xrightarrow{\text{selects}} \text{decoherence channels} \xrightarrow{\text{amplifies}} L_1^{(\theta)}\text{ outcomes}$$

1. $\theta_{bio}$ 编码了生命系统的热力学边界结构（细胞膜电位、分子振动模式、代谢自由能梯度）；
2. 这些结构决定了系统-环境耦合哈密顿量 $H_{env}^{(\theta)}$ 的具体形式；
3. 不同的 $H_{env}^{(\theta)}$ 选择不同的退相干基（pointer basis），从而使特定 $L_1$ 显现态被优先放大（Quantum Darwinism 机制）。

*(诠释框架：本公理基于**退相干理论**（Zurek 2003）与量子达尔文主义，不预设哥本哈根诠释的"意识导致坍缩"，不承诺 Orch-OR（Penrose-Hameroff）的微管量子相干假说。"选择偏置"是热力学-几何结构导致的统计效应，非神秘的意识-量子耦合。)*

**可测量预测（Falsifiable Prediction）**：

在相同量子初态 $|\psi_0\rangle$ 下，生命与非生命介质的退相干时间 $\tau_{dec}$ 与通道分布存在系统性差异：

$$\tau_{dec}^{(bio)} \neq \tau_{dec}^{(inert)}, \quad \Delta P_{channel} > \delta_{min}$$

证伪条件：在受控温度与电磁隔离环境中，生物组织与同质量同温度无机物的量子退相干统计无显著差异（$p > 0.05$，效应量 $< 0.1$）。

### Ax-Exp-04: Bioelectric Software
**Formal Definition**: Morphogenesis is controlled by L2 bioelectric fields rather than DNA alone.
$$\text{Form} = \hat{G}_{body}[\text{Bioelectric Pattern}]$$
* **Implication**: 形态发生受 L2 结构性场约束而非仅基因决定。

## III. Cognitive & Linguistic Probes (认知与语言探针)

### Ax-Exp-05: Normalization–d Correlation
**Formal Definition**: Divisive normalization parameters correlate with d-value.
$$\mathrm{Corr}(\theta_{norm}, d) > 0$$
* **Implication**: 归一化参数是 d 值的可测代理。

### Ax-Exp-06: Modal Mechanics Probe
**Formal Definition**: Modal verb distributions reflect ontological friction levels.
$$\mu_{sem} = \frac{\sum w_i \cdot \mathrm{Freq}(\text{必须/不能/应该})}{\sum w_j \cdot \mathrm{Freq}(\text{可以/可能/想要})}$$
* **Implication**: 语言中的情态结构可作为 Ψ_f 的统计指标。

<br>

---


# Part B: Original Hypotheses (Context)

> **Note**: The following sections contain the detailed experimental designs and falsification conditions.


# 2.1 H1：信息-质量-能量等效

信息具有质量。根据Vopson的质量-能量-信息等效原理，被擦除的信息位应产生额外能量释放。
$$ m_{bit} = k_BT \ln(2)/c^2 \approx 3.19 \times 10^{-38} \text{kg} $$

# 2.2 H2：量子坍缩的上下文偏置

活细胞内的量子测量统计应与惰性系统不同。

# 2.2a H60：生物电作为选择的生理软件

生物电模式（跨膜电压梯度）应作为形态发生的"生理软件"发挥作用。

# 2.6 H6：因果非封闭

如果世界是显性因果封闭的——即物理定律完全决定所有事件，意识对物理无统计可检测影响，不存在任何形式的目的论偏置——则SRT被证伪。

# 3.1 H7：归一化参数与d值相关

除法归一化参数的个体差异应与d值（选择考量范围）测量相关。

# 3.7 H72：情态力学——Ψ_f的语言学探针

个体语言中的情态动词使用模式反映其本体论摩擦（Ψ_f）水平。
$$ μ_{sem} = \frac{\sum w_i · \text{Freq}(必须/不能/应该)}{\sum w_j · \text{Freq}(可以/可能/想要)} $$
* **操作化补注**: H72 不预测“零 \(Ψ_f\) 最优”，而预测语言代理应与系统所处的摩擦区间相关：低负载可支付、中高负载可支付、边界可支付或过载。实验上应尽量把 proxy 分成预算侧、负荷侧与塌缩侧三类联合读取。

### Formalization Summary (形式化概述)

本文档的形式化实验公理围绕 SRT 核心算子的可检测性展开：

1. **Selection Beyond L2 Determination (Ax-Exp-01)**:
   $$P(\text{Behavior}|\text{Brain}_{L_2}) < 1 \Rightarrow \exists \ \hat{G}_\theta^{embodied}$$
   含义：若有机体行为无法仅由大脑 $L_2$ 模式完全预测，则存在具身选择算子 $\hat{G}_\theta^{embodied}$ 的不可约贡献。这是 SRT 选择概念的核心可证伪接口。

2. **Information Mass (Ax-Exp-02)**:
   $$\Delta E \ge k_B T \ln 2$$
   含义：信息擦除携带兰道尔下界能量代价，确立 $L_1$ 的物理实在性——信息不是纯语义抽象，而是具有质量-能量等效性的本体论实体。

3. **Normalization-d Correlation (Ax-Exp-05)**:
   $$\mathrm{Corr}(\theta_{norm}, d) > 0$$
   含义：除法归一化参数 $\theta_{norm}$ 与 d-value 正相关，提供从神经计算参数到 SRT 选择开放性的可测代理桥接。

4. **Modal Mechanics Probe (Ax-Exp-06)**:
   $$\mu_{sem} = \frac{\sum w_i \cdot \mathrm{Freq}(\text{必须/不能/应该})}{\sum w_j \cdot \mathrm{Freq}(\text{可以/可能/想要})}$$
   含义：语言中义务型情态词与可能型情态词的加权频率比 $\mu_{sem}$，作为本体论摩擦 $\Psi_f$ 水平的语言学统计代理。

### Mechanism Explanation (机制解释)

本文档的实验假设从不同尺度探测 SRT 核心算子 $\hat{G}_\theta$、摩擦 $\Psi_f$ 与 d-value 的经验签名：

- **$\hat{G}_\theta$ 的可检测性机制**：Ax-Exp-01 将检测焦点从"大脑是否违反物理定律"转移到"具身变量（内感受、代谢状态、环境交互）是否提供超出 $L_2$ 脑状态的预测信息"。若 $P(\text{Behavior}|\text{Brain}_{L_2}) = 1$，则 $\hat{G}_\theta$ 概念冗余，SRT 被证伪。T-Observer-Bias 进一步约束实验者自身的 $d_{obs}$ 偏置，防止过度解读噪声为意义信号。

- **$\Psi_f$ 的多模态代理**：本体论摩擦 $\Psi_f$ 通过三条独立通道获得可测代理：(a) 物理层的兰道尔能量下界（Ax-Exp-02），确认信息操作具有不可约耗散代价；(b) 生物层的量子坍缩偏置（Ax-Exp-03）与生物电模式（Ax-Exp-04），检测 $\theta$ 参数对物理基底的选择偏置效应；(c) 语言层的情态力学探针（Ax-Exp-06），将 $\Psi_f$ 水平映射为高义务/低自由度的情态分布 $\mu_{sem}$。

- **d-value 的操作化路径**：d-value 作为选择考量范围（scope of selection consideration）的度量，通过除法归一化参数 $\theta_{norm}$（Ax-Exp-05）获得神经计算层面的可操作代理。高 d 对应更宽的归一化池（更开放的信息整合），低 d 对应窄化的局部竞争（更封闭的选择空间）。

- **跨尺度一致性约束**：各假设并非孤立检验，而是构成联合约束网络——若 $\hat{G}_\theta$ 可检测（Ax-Exp-01），则其 $\theta$ 参数应同时在归一化相关（Ax-Exp-05）和情态分布（Ax-Exp-06）上留下一致签名。任何单一通道的异常需经其他通道交叉验证。

## 【理论边界/防误用声明】

1. 本文档用于理论解释与建模组织，不应替代独立实证、工程验证或专业判断。  
2. 任何公式或命题都依赖操作化定义、测量条件与语境边界，不得脱离边界做绝对化推断。  
3. 涉及临床、社会治理、伦理与部署决策时，必须结合风险评估与人类监督机制。

## H-Quant-Boundary-Stress：经典-量子边界应力测试（新增，2026-03-06）

### 假设
当系统被维持在高相干 \(L_0\)-主导区并逼近边界阈值时，维持该态所需代价出现超线性上升：
\[
\Psi_f^{maint}(\tau, m, \ell) \uparrow\uparrow\ \text{near}\ \tau_c(m,\ell)
\]
并伴随自发锚定概率升高：
\[
P_{anchor} = \sigma\big(\Psi_f^{maint} - \Psi_f^{cap}\big)
\]

### 可测代理
- 相干时间 \(\tau\)
- 维持功率/能耗 \(P_{hold}\)
- 质量/尺度参数 \((m,\ell)\)
- 退相干速率与读出阈值差 \((\tau_{decoh}^{-1}-\tau_{read}^{-1})\)

### 可证伪判据
- 若在跨平台复现实验中，\(P_{hold}\) 与相干维持不出现边界超线性项，且无额外耗散残差，则“\(\Psi_f\) 边界应力代理”假设不成立。
- 若额外耗散项可被标准噪声模型完全解释，则本假设降级为“无新增信息”。

## 【理论边界/防误用声明】
1. 该模板不预设对标准量子力学的否定；仅用于检测是否存在额外可重复耗散结构。
2. 任何“异常”必须先通过噪声谱、仪器漂移、数据筛选偏差三重审计。
3. 未达复现标准前，不得将单次结果升格为本体论结论。

### [Lineage/Source]
- 冷原子/量子光学边界实验语境（访谈信息接口）


## H-Exp-Precision-01：高分辨率单事件优先准则（2026-03-07）

> **[R]** 贝叶斯最优实验设计（Chaloner & Verdinelli 1995, Box & Hill 1967）的"最大化信息增益"原则为R基础；**[H]** 以下准则特化于 SRT 高阶动力学参数（θ相变阈值、Ψ_f临界点、高阶模态）的识别语境，并提出具体策略比较框架。

**SRT 特有适用条件**：当目标参数 θ 处于或接近相变临界区（∂B_chaos 附近，§11.3）时，后验分布极窄且呈强非高斯形态——低精度观测仅能采样噪声分布，无法区分信号与系统误差。此时高精度单次观测的 ΔI 收益显著超过低精度多次观测。

### 假设
在高阶动力学参数识别任务中，提升单次锚定精度（SNR 与模态分辨率）通常比增加低质量样本数更高效：
\[
\Delta \mathcal{I}_{single-high} > \Delta \mathcal{I}_{many-low}
\]
（在总预算相同且目标参数相同的前提下）

### 实验设计要点
1. 明确目标参数集（如高阶模态、相变阈值、微弱耦合项）；
2. 固定总预算，比较两策略：
   - A：少量高精度观测（高 SNR、低噪声、强校准）
   - B：大量低精度观测（低 SNR、高异质噪声）
3. 以参数后验收缩率与可证伪判据达成速度为主指标。

### 可测指标
- **后验体积收缩**：$\Delta V_{posterior} = V_{prior} - V_{posterior}$（对数体积差：$\Delta V \approx -\Delta \mathcal{I}$，即信息增益与后验收缩等价：$\Delta\mathcal{I} \approx \text{KL}(p_{post}\|p_{prior})$）
- **模态可分辨度**：$\mathcal{R}_{mode} \equiv \frac{\Delta\mu_{mode}}{\sigma_{noise}}$（两模态均值之差除以噪声标准差，类 SDT $d'$）；策略A vs B 比较：若 $\mathcal{R}_{mode}^A > \mathcal{R}_{mode}^B$ 而预算相同，则A优。
- **单位预算信息增益**：$\Delta \mathcal{I}/\$$ = 信息增益/预算（操作化候选：KL散度/实验成本）

### 可证伪判据
- 若在多任务复现实验中，策略 B 系统性优于策略 A（在等预算下后验收缩更快且更稳），则本准则被证伪或仅适用于窄域任务。
- **[H-追加]** 若参数已远离相变临界区（θ 处于宽稳定吸引盆内部），则策略A/B差异消失（ΔI_single-high ≈ ΔI_many-low），准则退化为标准功效分析建议（即准则的适用性本身是 θ 位置的函数）。

## 【理论边界/防误用声明】
1. 该准则不否定大样本统计学，仅用于“高阶弱信号参数识别”场景的策略选择。  
2. 不采纳“单次漂亮结果即可跳过复现”的推论；高分辨率事件仍需跨平台验证。  
3. 任何高 SNR 结果必须通过仪器系统误差与分析管线偏差审计。
