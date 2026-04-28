---
id: SRT-NEURO-07-ANNEX-EVO-DEVO-INTERFACE
type: annex
tags:
  - Neuroscience
  - Annex
  - EvoDevo
  - Bioelectricity
  - Levin
  - ConvergentEvolution
  - Waddington
status: active_v1
layer: bridge
epistemic_layer: bridge
claim_mode: bridge
canonical: false
owner: Neuroscience/SRT_Neuro_07_Evo_Devo.md
dependency:
  - SRT-NEURO-07
  - Operations/PR_D_Batch2b_Neuro_07_PreExtraction_Audit.md
---

# Neuro 07 Annex: Evo-Devo Interface

> **Boundary Guardrail**
>
> This Annex is bridge/interface material. It does not define SRT Core primitives.
>
> `θ_morpho`, `Ĝ_devo`, and `L2^bioelectric` are defined in Part A of the owner file (Ax-BIO-2b, Ax-BIO-2, Ax-BIO-1) — not in this Annex.
>
> Levin bioelectric experiments do not redefine `Generativity_devo` or `Ψ_f(θ_morpho)`. `Φ_coupling` is used in §3.2 as a bridge proxy, not as a canonical SRT definition.
>
> Convergent evolution examples (García-Moreno, Zaremba, Kempynck) do not define `Ax-EVO-1/2/3`, `S_d`, `F_Bio` equivalence, or d-value universality. The SRT-internal formal argument (`S_d = {σ ∈ L_0^anatomical : d(Ĝ_σ) > 0}`, `F_Bio^{avian}(θ_DVR) ≅ F_Bio^{mammalian}(θ_neocortex)`) remains in §5.3–5.5 of the owner file.
>
> Waddington landscape is an analogical interface; it does not define `Ĝ_devo`, `L2^bioelectric`, or `L_2` attractor topology. The correspondence table entries are bridge mappings, not ontological identities.
>
> §3.2.4 (cancer mechanical window, 2026-03-16), §3.2.5 (Stentor learning, 2026-03-21), and all §6 (geometric regularity / Dehaene / symbolic compression) material remain outside this Annex.

**Owner file**: [`../Neuroscience/SRT_Neuro_07_Evo_Devo.md`](../Neuroscience/SRT_Neuro_07_Evo_Devo.md)

**Extracted in**: PR-D Batch 2b (2026-04-28)

**Extraction record**: [`../Operations/PR_D_Batch2b_Neuro_07_Evo_Devo_Extraction_Record.md`](../Operations/PR_D_Batch2b_Neuro_07_Evo_Devo_Extraction_Record.md)

---

## §3.2 Levin Experiments — Interface Material

### §3.2.1 双头涡虫实验

- **操作**：通过改变缝隙连接（调制 $\Phi_{\text{coupling}}$）改变涡虫的生物电模式
- **结果**：产生稳定的双头涡虫——这个表型可以遗传到后代，即使切除再生
- **SRT 解释**：生物电模式存储了"形态目标"（$\theta_{\text{morpho}}$），这个目标独立于基因组存在

> **Annex note**: `θ_morpho` (morphogenetic bioelectric parameter) is defined in the owner file (Ax-BIO-2b). The Levin experiment is a bridge application — it supports but does not define `θ_morpho`. `Φ_coupling` here is a bridge proxy for gap-junction-mediated coupling strength, not a canonical SRT definition.

---

### §3.2.2 青蛙眼睛移位实验

- **操作**：将眼睛移植到青蛙的尾部
- **结果**：青蛙能够通过尾部的眼睛看东西——神经找到了正确的目标
- **SRT 解释**：存在一个"解剖地图"指导神经生长，这个地图存储在生物电场中

> **Annex note**: The "anatomical map stored in bioelectric field" is a bridge-level description of `L2^bioelectric` guidance. `L2^bioelectric` is defined in the owner file (Ax-BIO-1). This experiment is a candidate empirical correlate, not a definition source.

---

### §3.2.3 癌症电学逆转实验

- **操作**：通过操纵离子通道改变癌细胞的生物电状态
- **结果**：癌细胞可以被"正常化"——恢复正常的细胞行为
- **SRT 解释**：癌症不仅是基因问题，更是 $\Phi_{\text{coupling}}$ 崩溃问题——恢复电学耦合可以恢复正常 $d$ 值

> **Annex note**: The `Φ_coupling` collapse / d-value restoration framing is a bridge interpretation applying SRT's cancer mechanism (defined in owner §3.4 and Ax-PATH-1/2). The canonical cancer-as-d-collapse claim remains in the owner file (§3.4). §3.2.4 (cancer mechanical window, 2026-03-16 empirical patch) stays in the owner file as a canonical empirical anchor.

---

## §5 Convergent Evolution — Empirical Basis

> **Source**: García-Moreno *et al.*, Zaremba *et al.*, Kempynck & Hecker, *Science* 387 (2025); 综述见 Tosches, *Science* 387 (2025); 科普报道见 Saplakoglu, *Quanta Magazine* (2025.04).

### §5.1 标准难题：回路趋同之谜

发育神经科学的一个核心谜题：

**回路趋同之谜**：鸟类的背侧室脊（DVR）与哺乳类的新皮层（neocortex）在解剖学上截然不同——新皮层有六层有序结构，DVR 只是"无地标的神经元球"。但鸟类却展现出与灵长类相当的认知能力（乌鸦计数、鹦鹉计划、山雀追踪数万颗种子的位置）。一个 10 克大脑的鸟类完成的认知任务，相当于拥有 400 克大脑的黑猩猩（Güntürkün）。这些相似回路是从 3.2 亿年前的共祖继承的，还是独立演化的？

> **Annex note**: This problem framing is external cognitive science context. The SRT interpretation of circuit convergence as topological necessity of `S_d` under `L_0` constraints is in the owner file (§5.3 — `S_d = {σ ∈ L_0^anatomical : d(Ĝ_σ) > 0}`).

---

### §5.2 实证基础

2025 年 2 月发表于 *Science* 的三项独立研究利用**单细胞 RNA 测序**（scRNA-seq）给出了迄今最明确的答案：

#### §5.2.1 García-Moreno 团队

- **方法**：追踪鸡、小鼠、壁虎的 pallium 内神经元在胚胎各阶段的生成时间与成熟位置
- **发现**：成熟回路**跨物种惊人相似**（证实 Karten），但发育路径**完全不同**——回路在不同时间、不同顺序、不同脑区构建（证实 Puelles）
- **结论**：相似回路 ≠ 共祖遗传，而是独立组装

#### §5.2.2 Zaremba 团队

- **方法**：构建迄今最完整的鸟类 pallium 细胞图谱，与蜥蜴和小鼠进行跨物种比较
- **发现**：新皮层与 DVR 由**相似回路但不同细胞类型**构建——"你可以用不同的细胞类型构建相同的回路"
- **关键发现**：鸟类中，不同胚胎区域的细胞可以成熟为相同类型的成年神经元——"前脑的惊人重组"（Güntürkün）

#### §5.2.3 Kempynck & Hecker 团队

- **方法**：利用深度学习比较小鼠、鸡、人类的基因组调控元件
- **发现**：共享的 DNA 片段影响新皮层/DVR 的发育 → 相似的**遗传工具箱**在不同物种中被独立部署
- **补充**：抑制性神经元（调节信号的沉默神经元）跨鸟类和哺乳类保守

> **Annex note**: These three studies are pure external empirical content. The SRT-internal interpretation — `S_d` attractor topology (§5.3), `F_Bio` functional equivalence (`F_Bio^{avian}(θ_DVR) ≅ F_Bio^{mammalian}(θ_neocortex)`, §5.4), and d-value universality (`d > 0 ⟺ effective L_0 → L_1 selection`, §5.5) — remains in the owner file. These external findings support Ax-EVO-3 (convergent intelligence) but do not define it.

---

## §8 Waddington Landscape Interface

### §8.1 经典 Waddington 景观

Conrad Waddington 在 1940 年代提出了著名的"表观遗传景观"隐喻：

- **山谷 (Chreods)**：发育的稳定路径
- **山脊**：发育路径之间的能量屏障
- **滚动的球**：细胞的发育状态

### §8.2 SRT 重新诠释

|景观特征|SRT 对应|深层含义|
|:--|:--|:--|
|山谷|$L_2$ 吸引子|物种典型形态作为选择收敛点|
|山脊|$L_0$ 中的高自由能屏障|形态转换的能量代价|
|滚动的球|$\hat{G}_\theta$ 的当前选择状态|细胞正在经历的选择过程|
|景观本身|形态空间 $L_0^{\text{anatomical}}$|所有可能发育路径的相空间|

**SRT 的独特贡献**：

1. Waddington 景观是**动态的**——它本身在演化中被塑造
2. 球不是"被动滚动"，而是**主动导航**——细胞群体作为 $\hat{G}^{\text{collective}}$ 在选择路径
3. "到达谷底"不是终点，而是 $L_1 \to L_2$ 固化的开始

> **Annex note**: The correspondence table `✓` entries are analogical bridge mappings, not ontological identities. `L_2` attractor topology is defined in Core_Law and owner Part A — not by the Waddington reinterpretation. `Ĝ_devo` is defined in owner Part A (Ax-BIO-2). `Generativity_devo ∝ 1/Ψ_f(θ_morpho)` is defined in owner Part A (Ax-BIO-3). The three "SRT unique contributions" above are bridge-level interpretive claims that apply already-defined concepts, not new definitions.

---

> **Note**: §3.2.4 (cancer mechanical window, 2026-03-16 patch), §3.2.5 (Stentor single-cell learning, 2026-03-21 patch), and all §6 (geometric regularity / Dehaene / symbolic compression) content were not extracted. §3.2.4 and §3.2.5 are dated canonical empirical anchors and remain in the owner file. §6 (§6.3–6.5 contain SRT-internal `d_symbolic`, `η_compress`, and `Ψ_f ∝ 1/η_compress` claims) requires separate adjudication before extraction.
