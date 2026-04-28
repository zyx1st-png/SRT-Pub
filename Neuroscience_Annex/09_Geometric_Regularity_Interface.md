---
id: SRT-NEURO-07-ANNEX-GEOMETRIC-REGULARITY-INTERFACE
type: annex
tags:
  - Neuroscience
  - Annex
  - GeometricRegularity
  - Dehaene
  - SymbolicCompression
  - MDL
  - fMRI
  - MEG
status: active_v1
layer: bridge
epistemic_layer: bridge
claim_mode: bridge
canonical: false
owner: Neuroscience/SRT_Neuro_07_Evo_Devo.md
dependency:
  - SRT-NEURO-07
  - Operations/PR_D0_6_Neuro_07_Geometric_Regularity_Adjudication.md
  - Operations/PR_D_Batch2c1_Neuro_07_Geometric_Annotation_Conversion_Record.md
---

# Neuro 07 Annex: Geometric Regularity Interface

> **Boundary Guardrail**
>
> This Annex is bridge/interface material. It does not define SRT Core primitives.
>
> Geometric regularity / Dehaene / Sablé-Meyer empirical content does not define `η_compress`, `Ψ_f`, `d_symbolic`, or `Ĝ_θ^{ventral/dorsal}`.
>
> `η_compress = I(L_1;L_0)/H(L_1)` and `Ψ_f(σ) ∝ 1/η_compress(σ)` remain owner-file formal claims in [`Neuroscience/SRT_Neuro_07_Evo_Devo.md`](../Neuroscience/SRT_Neuro_07_Evo_Devo.md) §6.4.
>
> `d > d_symbolic` remains an owner-file d-value threshold claim in §6.5.
>
> `Ĝ_θ^{ventral}` and `Ĝ_θ^{dorsal}` remain owner-file formal operator specializations in §6.3.
>
> The `→ SRT interpretation` notes below are owner cross-references, not definitions. They were converted from inline formula citations in PR-D Batch 2c-1 (PR #56) as a prerequisite for safe extraction.
>
> §6.3–§6.5 remain outside this Annex.

**Owner file**: [`../Neuroscience/SRT_Neuro_07_Evo_Devo.md`](../Neuroscience/SRT_Neuro_07_Evo_Devo.md)

**Extracted in**: PR-D Batch 2c-2 (2026-04-29)

**Adjudication record**: [`../Operations/PR_D0_6_Neuro_07_Geometric_Regularity_Adjudication.md`](../Operations/PR_D0_6_Neuro_07_Geometric_Regularity_Adjudication.md)

**Annotation conversion record**: [`../Operations/PR_D_Batch2c1_Neuro_07_Geometric_Annotation_Conversion_Record.md`](../Operations/PR_D_Batch2c1_Neuro_07_Geometric_Annotation_Conversion_Record.md)

**Extraction record**: [`../Operations/PR_D_Batch2c2_Neuro_07_Geometric_Regularity_Extraction_Record.md`](../Operations/PR_D_Batch2c2_Neuro_07_Geometric_Regularity_Extraction_Record.md)

---

## §6 Geometric Regularity / Symbolic Compression — External Interface

> **Source**: Sablé-Meyer, Bhatt *et al.*, "A geometric shape regularity effect in the human brain", *eLife* 13 (2025), e106464; 基于 Dehaene *et al.* (2022), Sablé-Meyer *et al.* (2021, 2022) 的行为学前序工作。

### §6.1 标准难题：为什么人类能"看见"几何规则？

认知人类学的核心发现：

**几何规则性之谜**：远在书写发明之前，人类最早的图形产品就是高度规则的非具象几何符号——平行线、锯齿、三角网格。全球各文化在绘画、建筑、装饰中自发使用对称、平行等几何规则性。即使没有接受过西方正规教育的群体（如纳米比亚的 Himba 族），也能直觉地感知点、线及其组合成规则形状的方式。然而，狒狒不展现几何规则性效应，黑猩猩不能将具象图片的学习迁移到几何线条图。

**核心问题**：如果几何规则性感知不是教育的产物，那么它在大脑中的**神经基础**是什么？为什么人类拥有而其他灵长类缺乏这种能力？

> **Annex note**: This is external cognitive anthropology problem framing. The SRT answer — layered selection architecture (`Ĝ_θ^{ventral/dorsal}`), `η_compress` as compression efficiency, and `d_symbolic` threshold — is in the owner file §6.3–§6.5.

---

### §6.2 实证基础：fMRI/MEG 双通路证据

Dehaene 团队通过 fMRI（成人和 6 岁儿童）和 MEG（成人）记录了人脑在感知简单几何形状（三角形、四边形、六边形）时的神经活动：

#### §6.2.1 双重编码系统

| 通路 | 时间 | 脑区 | 计算模型 | 跨物种保守性 |
|:--|:--|:--|:--|:--|
| **腹侧通路** | 早期（~100-200ms）| 枕颞区 | CNN 可解释 | 人类与非人灵长类同源 |
| **背侧-前额通路** | 晚期（>200ms）| IPS + ITG + 前额 | 仅符号化几何特征模型可解释 | **人类独有** |

#### §6.2.2 关键发现

> **[R]** 以下5条发现均来自 Dehaene 团队 fMRI/MEG 实验（Dehaene et al. 2022/2023, *Science*；Amalric & Dehaene 2019；Meyer et al. 2025, *Nature Neuroscience*）。SRT 解释见 owner §6.3–6.5。

1. **规则性效应** **[R]**：几何规则性越高（如正方形 > 矩形 > 任意四边形），IPS/ITG/前额区的调制越强。→ SRT interpretation: see owner §6.4 (`η_compress`, `Ψ_f` relationship). This empirical finding supports the owner-file interpretation that geometric regularity can serve as an operational proxy for compression efficiency; it does not define `η_compress` or `Ψ_f`.
2. **压缩编码** **[R]**：大脑活动与**最小描述长度**（MDL，Rissanen 1978; Grünwald 2007）成比例 → 规则形状 = 更高压缩效率。→ SRT interpretation: see owner §6.4 (`η_compress` as neural implementation; MDL as one operational proxy for `Ψ_f`). The empirical finding is brain activity tracking MDL; the SRT formula remains defined in the owner file.
3. **CNN 失败** **[R]**：卷积神经网络可解释早期视觉反应（腹侧 L₁ 生成），但完全无法捕获后期背侧-前额信号。→ SRT interpretation: see owner §6.3 (`Ĝ_θ^{dorsal}` as symbolic selection / ontological transition). The empirical finding is CNN failure on late dorsal-prefrontal signals; the SRT operator-specialization claim remains in the owner file.
4. **发育先天性** **[R]**：6 岁儿童在相同 IPS/ITG 位置显示几何形状激活 → 先于正规教育。**混淆因素注**：6 岁前已有大量非正式几何暴露（积木、环境中的直线）；"先天性"的更强证据应来自：① 文化剥夺对照（Himba 族数据已部分支持）；② 先天盲后复明者（视觉经验受限）的几何激活检验。
5. **人类皮层扩展** **[R]**：人类相对于非人灵长类，**顶叶区的皮层面积扩展最大**（Meyer et al. 2025）。→ SRT interpretation: see owner §6.5 (`d_symbolic` threshold; parietal expansion as embodied hardware condition). This empirical finding supports the owner-file interpretation but does not define `d_symbolic` or the d-value threshold.

**证伪方向（§6.2.2 实验发现层）**：
- 若训练后的 CNN 变体（整合符号推理模块）能捕获后期背侧-前额信号（预测 MEG 晚期分量），则 "CNN 失败 → 本体论跃迁必需" 的推论被削弱（允许连续架构模拟符号化通路）。注：SRT 对此推论的理论来源在 owner §6.3。
- 若 Himba 族等缺乏正式几何教育的群体缺乏背侧-前额激活（仅腹侧），则"先天性"主张需修订（激活是教育诱发的，而非进化内置的）。

---

> **Note**: §6.3 (SRT layered selection architecture: `Ĝ_θ^{ventral}`, `Ĝ_θ^{dorsal}`), §6.4 (`η_compress = I(L_1;L_0)/H(L_1)`, `Ψ_f(σ) ∝ 1/η_compress(σ)`), and §6.5 (`d > d_symbolic ⇒ symbolic selection pathway`, d-value species table) were not extracted. These sections contain SRT-internal formal operator specializations, the canonical Ψ_f formula, and the canonical d-value threshold. They remain in the owner file at [`../Neuroscience/SRT_Neuro_07_Evo_Devo.md`](../Neuroscience/SRT_Neuro_07_Evo_Devo.md) §6.3–§6.5.
