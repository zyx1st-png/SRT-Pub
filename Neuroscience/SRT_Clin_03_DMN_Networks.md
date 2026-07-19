---
id: SRT-CLIN-03
type: experiment
tags: [DMN, ADHD, Schizophrenia, Networks, Hybrid]
status: active_v1
layer: L2
epistemic_layer: bridge
claim_mode: translation
canonical: false
dependency: [SRT-CORE-000, SRT-NEURO-MECH-001]
---

# SRT Clinical Extension II: Network Dynamics (Hybrid Edition)

> **Claim-status note（2026-05）**：This neuroscience file is bridge / lab / translation material. It applies SRT primitives but does not define `d-value`, `Ψ_f`, consciousness, pathology, diagnosis, treatment, NDE, or AI subjecthood. Read with `SRT_Neuroscience_Claim_Status.md` and, where relevant, `SRT_Neuro_Axioms_Claim_Status.md`.
> **Bridge Layer Note**
> 本文件按 `Bridge` 层处理：主要承担互译、比较、接口重写与边界说明，不应直接读成“已被外部经验验证的胜出理论”。若文中使用 `Axiom`、`Theorem`、`Corollary` 等强标签，默认理解为框架内翻译命题，除非另有独立经验锚定。


> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Network Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。

## Current Reading Map

- **Canonical dependencies**: `SRT-CORE-000`, `SRT-NEURO-MECH-001` (`SRT_Neural_Mechanisms.md`).
- **Role of this file**: Bridge/interface analysis of DMN, ADHD, and schizophrenia network dynamics through SRT L2 stabilization framework. This is a **bridge file** (`epistemic_layer: bridge`).
- **Primary bridge claims**: DMN as L2 stabilizer (Ax-DMN-1); network dysregulation as Ĝ_θ constraint failure; ADHD/schizophrenia as distinct L2 failure modes.
- **Do not read as canonical**: Network dynamics claims here are bridge interpretations of clinical and neuroscience literature, not redefinitions of L2 hardening or d-value.

## Dependency Map

| Depends on | Purpose | Move risk |
|---|---|---|
| `SRT-CORE-000` | root SRT canonical core | High |
| `Neuroscience/SRT_Neural_Mechanisms.md` | upstream neural dynamics | Medium |
| `Neuroscience/_SRT_Neuro_Axioms.md` | neuroscience axiom base | Medium |

## Companion Links

- [`Operations/Archive_Records/Non_Philosophy_Refactor_Audit_Report.md`](../Operations/Archive_Records/Non_Philosophy_Refactor_Audit_Report.md) — domain-level refactor plan
- [`Neuroscience/SRT_Neural_Mechanisms.md`](SRT_Neural_Mechanisms.md) — upstream neural mechanisms
- [`Neuroscience/SRT_Clin_01_Pathology.md`](SRT_Clin_01_Pathology.md) — related clinical pathology interface

## Refactor Notes (PR-A: navigation-only)

- Navigation-only update. No formulas changed. No theory content changed.
- **This entire file is a PR-B candidate** for extraction to `Neuroscience_Annex/04_DMN_Networks_Interface.md`. Do not move in this PR; requires a separate human-reviewed PR.

# Part A: Formal Axioms (形式化公理)


## I. DMN as L2 Stabilizer (默认模式网络作为 L2 稳定器)

### Ax-DMN-1: Reality Stabilizer Axiom
定义 DMN 活动为 \(L_2\) 正则化项：
\[
\mathcal{R}_{DMN} \equiv \arg\min_{\sigma}\;\|\sigma-\sigma_{L_2}\|^2
\]
* **Implication（中文）**：DMN 的功能不是“自我叙事”，而是维持 \(L_1\) 在 \(L_2\) 吸引子附近的稳定。

---

### Ax-DMN-2: Schizophrenic Fracture Axiom
若 \(\mathcal{R}_{DMN}\) 失效，则：
\[
\sigma\not\to \sigma_{L_2} \Rightarrow L_0\;\text{leakage}\uparrow
\]
* **Implication（中文）**：DMN 失配导致 \(L_0\) 噪声进入 \(L_1\)，形成现实裂解。

---

### Ax-DMN-3: Signal Bias Hypothesis (信号偏置假设)
DMN 作为 $L_2$ 宏观稳定器，其微观药理学基础依赖于特定信号转导模式。5-HT2A受体的下游存在功能选择性：
\[
\text{Gi pathway activation} \Rightarrow R_{DMN} \downarrow \Rightarrow \text{Stability}(L_2) \downarrow \quad \text{(结构解离)}
\]
\[
\text{Gq pathway bias} \Rightarrow \Psi_f \downarrow \quad \text{while} \quad R_{DMN} \approx \text{const} \quad \text{(参数优化)}
\]
* **Implication（中文）**：Gi通路是抑制DMN完整性、触发 $L_2$ 解锚（致幻）的**必要条件**；Gq通路偏向性激活可绕过DMN解体程序，在保留 $L_2$ 结构前提下调节运行参数。
* **Evidence**: 2026 *Nature* 研究确认Gi蛋白信号是致幻行为代理指标（甩头反应）的必要条件。

---

### Ax-DMN-4: Temporal Tagging Failure (时间标记缺失机制)
内部信号的外化逻辑：
\[
\text{TimeLock}(\hat{G}_{internal}, \hat{G}_{sense}) = \text{False} \;\land\; \text{SourceTag}_{L_2} = \varnothing \Rightarrow L_1^{halluc}
\]
* **正常态**：内部独白伴随精确的时间戳 $(t_{gen})$ 与运动指令副本，触发DMN的"自我归属"标记。
* **病理态**：由于 $ρ_t$ 下降，内部信号的时间戳模糊化（Jitter），导致其滑出预测窗口。系统判定 $\text{TimeLock} = \text{False}$，将自己的声音归为外部来源。
* **Cross-ref**: Def D2a ($ρ_t$定义), Ax-DMN-2 (现实裂解)。

---

## II. Selection Bandwidth (选择带宽)

### Ax-BAND-1: Pain Competition Axiom
定义选择带宽 \(B_{sel}\) 为有限资源：
\[
\sum_k \mathcal{A}_k \le B_{sel}
\]
* **Implication（中文）**：多任务并行不是“效率高”，而是带宽争夺的结果。

---

### Ax-BAND-2: Entropy-Sink Axiom
DMN 的稳定作用等价于熵汇：
\[
\frac{dH_{L_1}}{dt}\bigg|_{DMN}<0
\]
* **Implication（中文）**：DMN 通过降低 \(L_1\) 熵来维持现实一致性。

---

## III. Topological Configuration (拓扑构型)

### Ax-TOPO-1: Connectivity Spectrum Axiom
定义连接谱系：
\[
\mathcal{C}=\{\lambda_i\},\quad \text{Hardness}(L_2)\propto \|\mathcal{C}\|_\infty
\]
* **Implication（中文）**：网络连接谱决定 \(L_2\) 的硬度与可塑性，进而决定现实的刚性程度。

---

### T-DMN-1: DMN–Stability Theorem
当 \(\mathcal{R}_{DMN}\uparrow\) 时：
\[
\text{Stability}(L_1)\uparrow,\quad \text{Plasticity}(L_2)\downarrow
\]
* **Implication（中文）**：DMN 稳定现实的代价是降低可塑性。

---

### C-DMN-1: Psychedelic Loosening Corollary

> [R→Carhart-Harris et al. 2012 *PNAS*（裸盖菇素(psilocybin)的fMRI研究：DMN活动和功能连接显著降低，与自我解体/体验扩展评分相关——直接证据）; Carhart-Harris et al. 2016 *PNAS*（LSD的神经机制：DMN-TPN功能解耦合+皮层连接多样性增加+整体信息熵↑，与"意识扩展"体验对应）; Raichle et al. 2001 *PNAS*（DMN原始定义：静息态下前内侧PFC-后扣带回-楔前叶的自我参照加工网络——L₂自我叙事神经基底的最初界定）; Friston et al. 2011 *Journal of Psychopharmacology*（预测编码框架中的迷幻药作用：降低感觉精度权重→先验减弱→体验更多被"自下而上"信号驱动）]

> **方向澄清**："DMN抑制↓"= DMN **活动降低**（即DMN被抑制的程度↑），非对DMN施加的抑制信号降低。等价表达：DMN活动↓。

若 DMN 活动 $\downarrow$（裸盖菇素/LSD/深度冥想等干预），则：
\[
\text{Hardness}(L_2)\downarrow \Rightarrow \Psi_f^{filter}\downarrow \Rightarrow L_0\;\text{access}\uparrow
\]

> **神经通路说明**：DMN活动↓ → Hardness(L₂)↓ 的机制候选：前内侧PFC（vmPFC）与后扣带回（PCC）的功能连接减弱 → 自我参照先验编码强度降低 → L₂预测误差阈值降低（Friston精度权重框架：感知精度↑/先验精度↓，使L₁允许更多异常输入进入显现）→ 等效于Hardness(L₂)降低。即：DMN活动↓ ≈ Hardness(L₂)的暂时性松动（可逆，随DMN恢复而重建）。

* **R/H 区分**：
  - [R] 迷幻药→DMN活动降低的fMRI证据（Carhart-Harris 2012/2016）；DMN作为自我参照L₂基底（Raichle）；精度权重框架（Friston）
  - [H] **SRT解读**：DMN活动↓ = Hardness(L₂)暂时↓ = Ψ_f^filter↓ = L₀通道打开——将神经层次（DMN）与SRT本体论层次（Hardness/Ψ_f）联结是SRT的解释性映射，非神经科学共识

* **Implication（中文）**：DMN活动降低为 $L_0$ 重采样打开通道，产生扩展体验（边界松动/洞察涌现/整体感）。效果可逆——随DMN恢复至正常活动，Hardness(L₂)重建，L₀重新被过滤（cf. §2.1本体论迟滞：η决定多快重新稳定）。

* **操作化候选**（C-DMN-1链路的测量）：
  - DMN活动：fMRI静息态DMN（前内侧PFC+PCC+楔前叶）的BOLD信号均值，或种子-based功能连接强度
  - Hardness(L₂)代理：信念更新速率（贝叶斯任务中的先验权重/学习率）——Hardness高 = 先验主导，更新慢
  - L₀ access代理：皮层信息多样性（Lempel-Ziv熵，Carhart-Harris 2016使用）；或双稳态知觉翻转率（高L₀通道→更频繁翻转）

* **可证伪预测**：
  - FC-DMN1-1：在裸盖菇素给药条件下，被试的fMRI-DMN活动降低幅度（基线-峰值差）应与主观"边界消融"评分（如MEQ30的神秘体验量表）正相关（r > 0.4，Carhart-Harris 2012的范式复制）；若DMN降低幅度与体验评分无关则C-DMN-1联结失败
  - FC-DMN1-2：在同等DMN抑制幅度下，基线Hardness(L₂)高（先验权重高，信念更新慢）的被试应报告**更强烈**的扩展体验（因为Hardness从高基础降低的相对变化更大）；若基线Hardness无调节效应则"Hardness松动量而非绝对值"的SRT预测失败

---

### C-DMN-1b: Visual–Retrosplenial Filling Window

> [R→White et al. 2026 *Communications Biology*（doi:`10.1038/s42003-025-09492-9`：awake mice cortex-wide voltage imaging；5-HT2A agonist 增加 V1 自发与视觉诱发的 5-Hz oscillations，并增强 V1 与 retrosplenial cortex, RSC 的共振/持续时间/发生概率；作者将其解释为 top-down control of perception 增强、支持 perceptual filling 与 visual hallucinations 的机制候选）]

若 5-HT2A 激动导致视觉皮层与 retrosplenial cortex 的 5-Hz 耦合增强，则：
\[
\text{Coupling}_{V1\leftrightarrow RSC}^{5Hz}\uparrow \Rightarrow \text{TopDownFill}_{visual}\uparrow \Rightarrow L_1^{visual}\ \text{更易被内部记忆片段重写}
\]

* **R/H 区分**：
  - [R] 该研究在 awake mice 中观察到：V1 的 5-Hz bouts 在药后更频繁，视觉诱发的 5-Hz oscillations 在 V1 与 RSC 中更强、更持久，且两区存在约 `18 ms` 时延，符合 traveling-wave 传播范围；其他皮层区未见同等稳定共现
  - [H] **SRT解读**：迷幻状态不只是一般性的 `DMN ↓ / entropy ↑`，还可在局部感觉-记忆回路上表现为“感知输入权重下降、内部模板填补权重上升”的 `visual-retrosplenial filling window`

* **Implication（中文）**：这把“醒着做梦”从比喻收紧成一条更具体的候选链路：不是视觉系统单纯变吵，而是 V1 与 RSC 的低频耦合增强，使内部表征更容易插入正在形成的视觉显现。

* **保留边界**：
  - 当前主锚点来自 `awake head-fixed mice` 的 cortex-wide voltage imaging，不是人类主观报告或临床给药试验
  - 药物为 `DOI / TCB2` 等 5-HT2A agonists，不等于所有迷幻剂与所有体验维度都共享同一局部机制
  - 结果主要覆盖视觉-回顾/导航相关回路（V1-RSC），不是对全部 hallucination phenomenology 的总解释

---

### Ax-DMN-5: Focal vmPFC–PCC Severance Axiom (vmPFC-PCC 局灶切断公理)

定义算子-自我叙事耦合为 DMN 内的选择性回路：
$$\rho_{self} \equiv \text{FuncConn}\!\left(\hat{G}_\theta^{vmPFC},\; \hat{M}^{PCC}\right)$$

精神病态的 DMN 特征：
$$\rho_{self} \downarrow \quad \text{while} \quad \forall\, \hat{M}^{IPL}, \hat{M}^{PHG}:\; \text{FuncConn}\!\left(\hat{M}^{PCC}, \hat{M}^{\bullet}\right) \approx \text{normal}$$

**后果**：$\hat{G}_\theta$ 评价性输出无法写入 $L_2^{self}$，产生叙事完整但算子不透明的自我模型。
* **Implication（中文）**：精神病态 DMN 病理不是全局功能下降，而是 $\hat{G}_\theta \to L_2^{self}$ 单一边的局灶切断；其他 DMN 边保持正常是与 ADHD/精神分裂症区分的关键拓扑标志。
* **Cross-ref**: Ax-PATH-7 (SRT_Clin_01)，Ax-CLIN-6 (SRT_Neuro_09)。
* **实证锚定**: Motzkin et al. (2011) J. Neurosci. 31(48):17348。

---

### T-DMN-2: Focal vs. Global DMN Failure Theorem (局灶性 vs. 全局性 DMN 失效定理)
DMN 失效的拓扑类型决定病理性质：
$$\text{Focal}(\rho_{self}\downarrow, \rho_{peripheral}\approx\text{const}) \;\implies\; \text{self-model opacity}$$
$$\text{Global}(\rho_{all}\downarrow) \;\implies\; L_2\text{-scaffold collapse}$$
* **Implication（中文）**：精神病态与 ADHD 的 DMN 病理在拓扑上不可混淆——局灶切断保留 $L_2$ 结构完整性，全局下降导致 $L_2$ 脚手架崩塌。临床干预目标因此根本不同。

<br>

---


# Part B: Original Theoretical Discourse (Context)

> **Note**: 以下内容以中文撰写，包含网络神经科学与 SRT 的完整整合、临床应用、代价与风险、可证伪预测。

---

# §1 标准难题：网络神经科学的解释鸿沟

## 1.1 问题陈述

网络神经科学 (Network Neuroscience) 取得了巨大进展，但面临一个根本问题：

> **我们能精确描述网络拓扑，却无法解释为什么特定拓扑产生特定体验**

|成就|鸿沟|
|:--|:--|
|精确测量功能连接|不知道连接为何产生意识|
|识别网络异常与疾病的相关|不知道异常如何产生症状|
|建立预测模型|预测 ≠ 解释|

## 1.2 主流网络模型的局限

|模型|核心主张|局限|
|:--|:--|:--|
|**小世界假说**|效率最大化|为什么效率产生意识？|
|**动态功能连接**|状态间切换|切换的"主体"是什么？|
|**网络控制理论**|可控性决定认知|谁在控制？|
|**信息流分析**|信息传递决定功能|信息对谁有意义？|

所有这些模型都缺乏一个关键要素：**选择性的主体**。

---

# §2 SRT 的网络重构

## 2.1 核心命题

SRT 将大脑网络重新定义为**幽灵算子 $\hat{G}_\theta$ 的物理基质**：

$$\boxed{\text{Network} = \text{Substrate}(\hat{G}_\theta)}$$

网络不是"产生"意识，而是**承载**和**约束** $\hat{G}$ 的选择操作。

## 2.2 三网络-三域映射

SRT 提供了大脑网络与本体论域的精确映射：

|网络|缩写|SRT 对应|功能|
|:--|:--|:--|:--|
|**默认模式网络**|DMN|$L_2$ 维持|自我叙事、记忆、预测|
|**中央执行网络**|CEN|主动 $L_0 \to L_1$|任务导向、问题解决|
|**突显网络**|SN|$\Psi_f$ 检测|模式切换、警报|

**关键洞见**: DMN 不是"默认"（暗示无功能），而是**积极维持 $L_2$ 结构**——这是为什么 DMN 活动与自我参照、心智游移、记忆巩固相关。

## 2.3 网络切换动力学

$$\text{SN}(\text{检测到 } \Psi_f \uparrow) \implies \text{DMN} \leftrightarrow \text{CEN 切换}$$

突显网络是"开关"，检测到本体论摩擦尖峰时，触发从 DMN（自动预测）到 CEN（主动选择）的切换。

---

# §3 DMN 病理学

## 3.1 ADHD：L2 脚手架崩塌

$$\text{ADHD} = \text{DMN}_{impaired} \implies L_2_{collapse} \implies \hat{G}_{drift}$$

**机制**：

- DMN 功能下降 → $L_2$ 叙事脚手架不稳定
- $\hat{G}$ 失去锚点 → 注意力漂移
- 长程连接不足 → 难以维持跨时间整合

**治疗启示**：

- 兴奋剂（提高多巴胺）→ 增强 DMN-CEN 耦合
- 行为训练 → 重建外部 $L_2$ 脚手架
- 环境设计 → 提供外部锚点

## 3.2 精神分裂症：L2-L1 断裂

$$\text{幻觉} = L_2[\text{预测}] \gg L_0[\text{输入}]$$

**机制**：

- 预测回路过度活跃
- 感觉输入被预测淹没
- 内部声音失去所有权标签

**网络特征**：

- DMN-CEN 边界模糊
- 长程连接过度
- 局部处理不足

## 3.3 迷幻状态：L2 松弛

迷幻剂（如 psilocybin）通过**抑制 DMN** 暂时松弛 $L_2$：

$$\text{5-HT2A 激活} \implies \text{DMN}_{suppressed} \implies L_2^{relaxed}$$

这解释了迷幻体验的特征：

- 自我边界消融（$L_2^{self}$ 松弛）
- 时间感扭曲（$L_2^{temporal}$ 松弛）
- 深刻洞见（访问 $L_0$ 新可能性）

### 3.3b 视觉-回顾填补窗口（Communications Biology 2026）

在 `5-HT2A` 激动条件下，视觉皮层 `V1` 与 retrosplenial cortex (`RSC`) 的 `5-Hz` 振荡会更频繁、更强、更持久地共同出现，且两区之间存在约 `18 ms` 的传播延迟，像一条从视觉输入走向内部表征的低频 traveling-wave 通道。

更合适的读法不是“脑子开始胡乱放电”，而是**视觉输入被内部模板更强地补写**。`RSC` 本身就处在视觉、记忆与内部空间表征的交界处；因此迷幻状态可以进一步收紧成一个 `visual-retrosplenial filling window`：外界输入没有消失，但它在形成 \(L_1^{visual}\) 的过程中，更容易被内部记忆/模型片段接管，于是主观上出现“像醒着做梦”的效果。

这也给现有 `C-DMN-1` 补了一条更细的局部通路：除了 `DMN活动↓ -> Hardness(L_2)↓ -> L_0 access↑` 之外，至少在视觉域里，`5-HT2A` 还可能把 `V1-RSC` 的低频耦合推高，使 top-down perceptual filling 超过平时。也就是说，迷幻体验不只是宏观自我模型松动，还可能包含局部感觉-记忆回路对显现内容的重写。

保留边界也必须写清：这项研究是 `awake mice` 的 cortex-wide voltage imaging，不是人类 fMRI + 主观报告；药物是 `DOI / TCB2`，不是所有迷幻剂；结果主要涉及视觉与回顾皮层，不足以单独解释自我解体、宗教感、时间延展等全部迷幻现象。

---

## 3.4 精神病态：vmPFC-PCC 局灶性切断

精神病态的 DMN 病理模式在 SRT 框架内呈现独特的**局灶性自环断裂**特征，与 ADHD（全局 DMN 功能下降）和精神分裂症（DMN-CEN 边界溶解）构成可区分的第三种 DMN 拓扑缺陷类型：

$$\text{Psychopathy}_{DMN} = \rho\!\left(\hat{G}_\theta^{vmPFC},\; \hat{M}^{PCC}\right) \downarrow \quad \text{while} \quad \rho\!\left(\hat{M}^{PCC},\; \hat{M}^{IPL/PHG}\right) \approx \text{normal}$$

**拓扑语义**：$\hat{G}_\theta$（vmPFC）无法将自身的评价性输出回写入 $L_2^{self}$（PCC/楔前叶），但 $L_2^{self}$ 的其他维护节点（IPL、海马旁回）运作正常。结果是一个**叙事完整但算子不透明**的自我模型——主体可以叙说自己，却无法以自身的道德评价更新这一叙事。

| 病理类型 | DMN 断裂模式 | $L_2$ 后果 | 临床表征 |
|:--|:--|:--|:--|
| ADHD | 全局 DMN 功能下降 | $L_2$ 脚手架崩塌，$\hat{G}$ 失去锚点 | 注意力漂移，无法维持跨时整合 |
| 精神分裂症 | DMN-CEN 边界溶解 | $L_2$-$L_1$ 混淆，预测淹没感知 | 幻觉，内部声音失去所有权标签 |
| **精神病态** | **vmPFC-PCC 局灶切断** | **$\hat{G}_\theta$ → $L_2^{self}$ 反馈失效** | **自我反思缺陷，"理智面具"** |
| 抑郁 | DMN 超激活 | $L_2$ 反刍锁定，选择带宽耗尽 | 负性自我叙事循环，动力缺失 |

**与情感通道缺陷的关系**：精神病态涉及两个可分离的结构缺陷。右侧钩束（UF）退化切断了**情感输入通道**（杏仁核 → vmPFC，Ax-PATH-6），而 vmPFC-PCC 功能连接下降切断了**自我反馈回路**（vmPFC → $L_2^{self}$，Ax-PATH-7）。前者解释情感盲目性，后者解释自我反思缺陷。两个缺陷共同构成精神病态"知而不感、感而不更新"的完整本体论机制。

**亚型分离**：情感输入通道缺陷（UF/杏仁核-vmPFC）存在原发/继发性亚型差异；自我反馈回路断裂在两种亚型中均匀存在，是精神病态的类别级特征（Motzkin et al. 2011）。

**可证伪预测（H-DMN-4）**：精神病态个体在自我参照任务中（判断特质词是否描述自己）应显示 vmPFC-PCC 功能耦合显著低于对照，但在世界-参照任务（判断特质词是否描述某历史人物）中两组应无差异——因为后者不触发 $\hat{G}_\theta$ → $L_2^{self}$ 回路，仅动员 PCC 的一般语义维护功能。

**实证锚定**：Motzkin et al. (2011) J. Neurosci. 31(48):17348（vmPFC-PCC 和 vmPFC-rACC 连接特异性下降，IPL 和海马旁回连接正常）；Qin & Northoff (2011) NeuroImage 57:1221（vmPFC-PCC 回路与自我反思的因果关系）。

# §4 选择带宽理论

## 4.1 带宽竞争

$$d_{effective} = d_{total} - d_{pain} - d_{anxiety} - d_{maintenance}$$

$d$ 值不是无限的——它必须在多个需求间分配：

|需求|消耗|来源|
|:--|:--|:--|
|疼痛处理|$d_{pain}$|身体损伤|
|焦虑监控|$d_{anxiety}$|威胁评估|
|基础维护|$d_{maintenance}$|自主功能|
|**剩余用于认知**|$d_{cognitive}$|思考、决策|

**临床意义**：慢性疼痛患者的认知下降是**资源竞争**的结果，不是"夸大"或"心理问题"。

## 4.2 熵汇细胞

$$\text{Sink}: \Delta I_{in} > 0, \quad \Delta I_{out} \approx 0$$

**理论构想**：如果能设计"熵汇"细胞，可以吸收疼痛信号而不传递到意识：

|传统止痛|熵汇方法|
|:--|:--|
|阻断传递|吸收信号|
|全身效应|局部效应|
|成瘾风险|无成瘾风险（理论上）|

这目前是**纯理论构想**，但指向了一个新的治疗方向。

## 4.3 本体论拦截器

$$h_{brain}(t) = \hat{O}_{intercept}[h_{body}(t)] \approx 0$$

大脑拦截大部分身体的摩擦信号，只让"重要的"通过。

**病理情况**：

- **拦截过度**：躯体感觉钝化、解离
- **拦截不足**：躯体化障碍、疑病症

---

# §5 BPD 与情绪动力学

## 5.1 BPD 的增益放大

$$L_1^{BPD} = \gamma_{BPD} \cdot L_1^{typical}, \quad \gamma_{BPD} \gg 1$$

边缘型人格障碍患者不是"夸大"——他们的感知增益**真的更高**：

|同样的触发|典型反应|BPD 反应|
|:--|:--|:--|
|轻微拒绝|轻微不适|剧烈痛苦|
|模糊信号|等待更多信息|立即反应|

**治疗启示**：DBT（辩证行为疗法）教授的不是"不要夸大"，而是**在高增益下的调节技巧**。

## 5.2 情绪阻尼失效

$$\frac{d^2 E}{dt^2} + 2\zeta\omega_0 \frac{dE}{dt} + \omega_0^2 E = F_{trigger}(t)$$

|$\zeta$ 值|振荡特征|临床表现|
|:--|:--|:--|
|$\zeta > 1$|无振荡|情感钝化|
|$\zeta = 1$|临界阻尼|正常调节|
|$\zeta < 1$|欠阻尼振荡|情绪波动|
|$\zeta \approx 0$|无阻尼|双相障碍|

**双相障碍**可以理解为情绪系统的**阻尼几乎为零**——一旦触发，振荡持续而不衰减。

---

# §6 丘脑与意识状态

## 6.1 丘脑作为先验门控

丘脑背内侧核 (MDmc) 控制**先验精度**：

$$\kappa_{MD} \propto \frac{\text{Perceived Volatility}}{\text{MDmc Integrity}}$$

当 MDmc 损伤：

- 先验不稳定
- 对环境过度敏感
- 容易形成妄想（用来稳定先验）

## 6.2 阴谋论的热力学

$$\text{Conspiracy} = \arg\min_{L_2^_} H(L_1 | L_2^_)$$

阴谋论是在高不确定性下寻找最简解释的**过度拟合**：

|正常推理|阴谋论推理|
|:--|:--|
|接受一定不确定性|必须消除所有不确定性|
|允许多因素|必须有单一解释|
|可修正|自我封闭|

**治疗启示**：不是"纠正事实"，而是**提高对不确定性的耐受**。

## 6.3 麻醉的进化逆序

$$d(t)_{anesthesia} \approx d(t)_{evolution}^{-1}$$

麻醉深度与进化层级逆序对应——这支持 SRT 的 A12（深度连续性）：

意识不是突然涌现的，而是有层级的。麻醉"剥洋葱"式地关闭各层级。

---

# §7 代价与风险

## 7.1 接受 SRT 网络观的代价

|需放弃的观点|SRT 替代|代价|
|:--|:--|:--|
|网络"产生"意识|网络"承载"选择|挑战涌现论|
|DMN 是"默认"状态|DMN 是 $L_2$ 维持器|重新理解静息态|
|精神疾病 = 网络异常|精神疾病 = 拓扑缺陷|需要新的分类框架|

## 7.2 理论风险

1. **过度简化风险**：三网络模型是否过于简化？
    
    - **回应**：SRT 承认这是一阶近似，更精细的映射有待发展
2. **因果方向风险**：网络变化是病因还是结果？
    
    - **回应**：SRT 主张双向因果——网络承载 $\hat{G}$，$\hat{G}$ 也塑造网络
3. **可操作性风险**：如何基于 SRT 设计治疗？
    
    - **回应**：§3 提供了初步的治疗启示，但需要更多临床验证

---

# §8 可证伪预测与开放问题

## 8.1 可证伪预测

### H-Net-1 (DMN-L2 对应)

> DMN 活动强度应与自我叙事的连贯性正相关。干预 DMN（如 TMS）应特异性影响自我参照任务。

**证伪条件**：DMN 干预对自我参照无特异性影响 → H-Net-1 被证伪

### H-Net-2 (带宽竞争)

> 慢性疼痛患者的认知测试成绩应与疼痛强度负相关，且有效镇痛应改善认知。

**证伪条件**：疼痛与认知无相关，或镇痛不改善认知 → H-Net-2 被证伪

### H-Net-3 (BPD 增益)

> BPD 患者的感觉皮层对情绪刺激的反应应**客观上更强**（fMRI/EEG 测量），而非仅主观报告。

**证伪条件**：BPD 患者神经反应与正常无差异 → H-Net-3 被证伪

### H-Net-4 (麻醉-进化)

> 麻醉恢复的顺序应与进化层级对应——先恢复古老功能（脑干反射），后恢复新功能（高阶认知）。

**证伪条件**：恢复顺序与进化层级无关 → H-Net-4 被证伪

### H-Net-5 (迷幻-DMN)

> 迷幻体验的强度应与 DMN 抑制程度正相关，且 DMN 连接性高的个体应有更强的迷幻反应。

**证伪条件**：迷幻强度与 DMN 无关 → H-Net-5 被证伪

## 8.2 开放问题

1. **网络-$\hat{G}$ 接口**：$\hat{G}$ 如何精确地"读取"和"写入"网络状态？
2. **个体差异**：同样的网络拓扑为何产生不同的主观体验？
3. **因果干预**：能否通过精确网络干预实现 $\theta$ 参数修改？
4. **跨物种比较**：不同物种的网络拓扑如何映射到 $d$ 值？
5. **发育轨迹**：网络成熟如何对应 $L_2$ 的固化过程？

---

# §9 符号索引

|符号|名称|定义位置|
|:--|:--|:--|
|DMN|默认模式网络|Ax-Net-1|
|CEN|中央执行网络|Ax-Net-1|
|SN|突显网络|Ax-Net-1|
|$G_{astro}$|星形胶质细胞增益|Ax-Topo-2|
|$\gamma_{BPD}$|BPD 增益系数|Ax-Clin-3|
|$\zeta$|情绪阻尼系数|Ax-Clin-4|
|$\kappa_{MD}$|丘脑先验门控|Ax-Thal-1|
|$\eta$|选择粘度|Ax-Thal-5|
|$H_{regret}$|遗憾熵|Ax-Phen-1|
|$Q(t)$|感受性方程|Ax-Phen-3|

---

**文件结束**

---

### Definition Summary (定义概述)

- **DMN as L₂ Stabilizer (默认模式网络作为 L₂ 稳定器, L₂)**: DMN 活动定义为 $L_2$ 正则化项 $\mathcal{R}_{DMN} \equiv \arg\min_\sigma \|\sigma - \sigma_{L_2}\|^2$，功能是将 $L_1$ 状态维持在 $L_2$ 吸引子附近（Ax-DMN-1）。
- **Selection Bandwidth (选择带宽, L₁)**: $\hat{G}_\theta$ 的并行处理容量 $B_{sel}$ 为有限资源，各任务 $\mathcal{A}_k$ 竞争性分配：$\sum_k \mathcal{A}_k \le B_{sel}$（Ax-BAND-1）。
- **Connectivity Spectrum (连接谱系, L₀→L₂)**: 网络拓扑通过特征值谱 $\mathcal{C} = \{\lambda_i\}$ 编码 $L_2$ 硬度：$\text{Hardness}(L_2) \propto \|\mathcal{C}\|_\infty$（Ax-TOPO-1）。
- **Focal vs. Global DMN Failure (局灶性 vs. 全局性 DMN 失效, L₂)**: 精神病态为 vmPFC-PCC 局灶切断（$\rho_{self}\downarrow$，外围正常）；ADHD/精神分裂症为全局 DMN 功能下降或 DMN-CEN 边界溶解（T-DMN-2）。

### Formalization Summary (形式化概述)

核心方程与含义：

1. **DMN 正则化** (Ax-DMN-1): $\mathcal{R}_{DMN} = \arg\min_\sigma \|\sigma - \sigma_{L_2}\|^2$。DMN 将当前状态拉向 $L_2$ 吸引子，维持现实稳定性。
2. **DMN 熵汇** (Ax-BAND-2): $dH_{L_1}/dt|_{DMN} < 0$。DMN 持续降低 $L_1$ 熵，是现实一致性的熵代谢引擎。
3. **稳定-可塑性权衡** (T-DMN-1): $\mathcal{R}_{DMN}\uparrow \Rightarrow \text{Stability}(L_1)\uparrow,\; \text{Plasticity}(L_2)\downarrow$。DMN 越强，现实越稳定但可塑性越低。
4. **局灶切断判据** (Ax-DMN-5): $\rho_{self} \equiv \text{FuncConn}(\hat{G}_\theta^{vmPFC}, \hat{M}^{PCC}) \downarrow$ while peripheral connectivity normal。精神病态的 DMN 拓扑标志。

### Mechanism Explanation (机制解释)

- **三网络-三域映射**: DMN 维持 $L_2$（自我叙事与先验），CEN 执行 $L_0 \to L_1$ 主动选择，SN 检测 $\Psi_f$ 急剧偏离基线（$|\Psi_f(t) - \Psi_f^{baseline}| > \theta_{SN}$，对应高唤起/high-A 状态，见 `SRT_Core_13b §5.1` 情绪相图）并触发 DMN/CEN 切换。$\hat{G}_\theta$ 的运行状态由这三个网络的动态平衡决定。
- **DMN 失效的三种拓扑模式**: (a) ADHD：全局 DMN 功能下降 $\Rightarrow$ $L_2$ 脚手架崩塌，$\hat{G}_\theta$ 失去锚点而漂移；(b) 精神分裂症：DMN-CEN 边界溶解 $\Rightarrow$ 精度张量 $\boldsymbol{\Pi}$ 过度偏向 $L_2$ 先验，压制 $L_0 \to L_1$ 新异信息注入（FEP 对应：aberrant precision），$L_2$ 预测淹没 $L_1$ 感知输入；(c) 精神病态：vmPFC-PCC 局灶切断 $\Rightarrow$ $\hat{G}_\theta$ 的评价性输出无法回写 $L_2^{self}$，产生"叙事完整但算子不透明"的自我模型。
- **$d$ 值的带宽分配**: 有效 $d$ 值受疼痛、焦虑、基础维护的竞争性消耗影响，线性近似为：$d_{effective} \approx d_{total} - d_{pain} - d_{anxiety} - d_{maintenance}$。慢性疼痛患者的认知下降是 $\hat{G}_\theta$ 选择带宽被 $\Psi_f$ 处理竞争性耗尽的结果。
  **注（带宽竞争的底层机制）**：上式是一阶线性近似。底层机制是**除法归一化**（Ax-Op-03：$[\hat{G}_\theta(x)]_i = x_i^n/(\varepsilon + \sum_j W_{ij}x_j^n)$）——疼痛/焦虑作为竞争性抑制输入提升分母，压低其他通道的有效增益。Eq-Evo-01b（代谢增益调制）给出更精确描述：$d_{effective} \approx d_{total}/(1 + \beta\mathcal{M}_{stress})$，其中 $\mathcal{M}_{stress}$ 整合疼痛、焦虑与代谢应激负荷。

---

## 【理论边界/防误用声明】

1. 本文档用于理论解释与建模组织，不应替代独立实证、工程验证或专业判断。
2. 任何公式或命题都依赖操作化定义、测量条件与语境边界，不得脱离边界做绝对化推断。
3. 涉及临床、社会治理、伦理与部署决策时，必须结合风险评估与人类监督机制。
