from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected one match in {path}, got {count}: {old[:120]!r}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


# Registry frontmatter dependency truth-up.
replace_once(
    "CANONICAL_REGISTRY.md",
    "dependency: [SRT-INDEX, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-CROSS-DOMAIN-MATRIX, SRT-CORE-22]",
    "dependency: [SRT-INDEX, SRT-GENERATIVE-ONTOLOGY-SPINE, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-CROSS-DOMAIN-MATRIX, SRT-CORE-22]",
)

# Register the new cross-owner spine before local definition owners.
marker = "## A. 核心定义层（Definitions）\n\n"
entry = """## A. 核心定义层（Definitions）

### 0. Generative Ontology Spine — 跨 owner 生成主轴
- 主锚点：`Core_Law/SRT_Generative_Ontology_Spine.md`
- id：`SRT-GENERATIVE-ONTOLOGY-SPINE`
- layer：L0-L1 / epistemic：os / status：active / version：v0 / claim-mode：canonical
- 角色：固定当前 SRT 的**跨层生成顺序、非同一性与 OPEN gate**，作为旧 canonical 清洗和后续本体研究的第一路由；它不替代各局部 owner 的详细定义。
- 当前 trunk：`minimum non-neutrality / pre-object difference -> subjectless Selection -> manifestation + relative backgrounding -> active verticalization -> recurrent localized vertical organization -> One / Selection-position`。
- 当前 Bearer gate：已形成的 `One / Selection-position + P prospective self-indexing + E same-One prospective exposure -> Bearer`，按 semantic / architectural canonical 读取；不是跨所有实现域的形式化或实证 N&S theorem。
- typed layering：One-level endogenous perspective、A1/A2/A3 anticipation 分层须保留；`all Ones automatically perspective-bearing` 仍未建立。
- supersession：旧文件若在**跨层推论**上与本 spine 冲突，旧推论转为 cleanup / retyping target；局部数学或语义内容在不冲突范围内继续有效。
- 硬边界：history/writeback 不作为 verticality 的本体来源；Stable ISP 不作为 One 的形成源；`sigma_sr` / d / T_dir / Psi_f 不得反向生成 One / Bearer / subject；Bearer 不按定义等同于承担 / concern / subject / experiencer。
- OPEN：精确 L0 primitive decomposition、One-level perspective 普遍充分性、Bearer↔承担、Bearer→concern/d、agency、positive subject gate、cognition、phenomenality、collective subject sufficiency、new Level、Level 2 均未由本文件自动关闭。
- 引用规则：涉及当前**生成顺序、跨 owner 层级关系、旧 canonical 是否越权**时先回链本文件；随后再进入 L0、One Formation、P1-T06、d / Psi_f / T_dir 等局部 owner。

"""
replace_once("CANONICAL_REGISTRY.md", marker, entry)

# Replace citation priority so the spine controls cross-owner ordering before local owners.
old_priority = """1. `CANONICAL_REGISTRY.md`（找入口）
2. `Governance/SRT_CLAIM_LADDER.md` / `Governance/SRT_CLAIM_MODE_AUDIT.md`（判断命题硬度与降级状态）
3. `_SRT_D_VALUE_CANONICAL.md` / `_SRT_PSI_F_CANONICAL.md` / `_SRT_T_DIR_CANONICAL.md` / `_SRT_CROSS_DOMAIN_MATRIX.md` / `Core_Law/SRT_One_Formation.md` / `Core/SRT_Core_21_Formal_Axioms.md` / `Core/SRT_Core_22_Equations.md`（找规范定义、形成层 owner 与跨域用法）
4. `Core/SRT_Core_21_Minimal_Axioms.md` / `Core/SRT_Core_21b_Constitutive_Theorems.md` / `Core/SRT_Core_21c_Bridge_Hypotheses.md`（按 P-level 找 Core_21 正文）
5. domain claim-status files（防止 bridge / public / clinical / spirituality / AI / physics overclaim）
6. `Core/SRT_Core_14_Dynamics_Scaling.md` / `Core_Law/SRT_Reference_Dynamics.md` / `AI/SRT_AI_01_Ontology.md`（找展开与跨域解释；not final definitions）
7. `Core/SRT_OPEN_TENSIONS.md`（确认未封口问题）
8. 各 split 目录（找导航与局部阅读）
9. 原始长文（找历史展开与全量语境）"""
new_priority = """1. `CANONICAL_REGISTRY.md`（找入口）
2. `Core_Law/SRT_Generative_Ontology_Spine.md`（判断跨 owner 生成顺序、非同一性、OPEN gate 与旧 canonical 是否越权）
3. `Governance/SRT_CLAIM_LADDER.md` / `Governance/SRT_CLAIM_MODE_AUDIT.md`（判断命题硬度与降级状态）
4. `Core_Law/SRT_L0_Metaphysics.md` / `Core_Law/SRT_One_Formation.md` / `_SRT_D_VALUE_CANONICAL.md` / `_SRT_PSI_F_CANONICAL.md` / `_SRT_T_DIR_CANONICAL.md` / `_SRT_CROSS_DOMAIN_MATRIX.md` / `Core/SRT_Core_21_Formal_Axioms.md` / `Core/SRT_Core_22_Equations.md`（找兼容于 spine 的局部定义、形成 owner、形式与跨域用法）
5. `Core/SRT_Core_21_Minimal_Axioms.md` / `Core/SRT_Core_21b_Constitutive_Theorems.md` / `Core/SRT_Core_21c_Bridge_Hypotheses.md`（按 P-level 找 Core_21 正文；不得反向覆盖 spine 的跨层顺序）
6. domain claim-status files（防止 bridge / public / clinical / spirituality / AI / physics overclaim）
7. `Core/SRT_Core_14_Dynamics_Scaling.md` / `Core_Law/SRT_Reference_Dynamics.md` / `AI/SRT_AI_01_Ontology.md`（找展开与跨域解释；not final definitions）
8. `Core/SRT_OPEN_TENSIONS.md`（确认未封口问题）
9. 各 split 目录（找导航与局部阅读）
10. 原始长文（找历史展开与全量语境）"""
replace_once("CANONICAL_REGISTRY.md", old_priority, new_priority)

# Add spine to the compact owner rollup.
replace_once(
    "CANONICAL_REGISTRY.md",
    "本轮 governance-canonical 抽离 v1 暂定以下四者为主干用法：\n- `d-value` → `_SRT_D_VALUE_CANONICAL.md`",
    "本轮 governance-canonical 抽离 v1 与 2026-09-11 spine landing 后，主干用法优先包含：\n- `Generative ontology cross-owner order` → `Core_Law/SRT_Generative_Ontology_Spine.md`\n- `d-value` → `_SRT_D_VALUE_CANONICAL.md`",
)

# Freeze: make the spine an explicit protected canonical anchor.
replace_once(
    "Governance/SRT_CANONICAL_FREEZE.md",
    "以下文件默认不做无明确授权的正文重写：\n\n- `Core_Law/SRT_L0_Metaphysics.md`",
    "以下文件默认不做无明确授权的正文重写：\n\n- `Core_Law/SRT_Generative_Ontology_Spine.md`\n- `Core_Law/SRT_L0_Metaphysics.md`",
)

replace_once(
    "Governance/SRT_CANONICAL_FREEZE.md",
    "- 若必须改正文，需明确标注为高风险编辑\n",
    "- 若必须改正文，需明确标注为高风险编辑\n- 跨 owner 的生成顺序、非同一性与 OPEN gate 以 `Core_Law/SRT_Generative_Ontology_Spine.md` 为当前优先路由；旧 anchor 的局部定义只在与该 spine 兼容的范围内继续有效，冲突的跨层推论进入 cleanup / retyping，而不是自动反向约束当前 reconstruction\n",
)

print("generative ontology spine routing landed")
