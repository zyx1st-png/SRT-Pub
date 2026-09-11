from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    s = p.read_text()
    if old not in s:
        raise RuntimeError(f"anchor not found in {path}: {old[:160]!r}")
    p.write_text(s.replace(old, new, 1))


# 21B — Stable ISP remains a stronger downstream standing criterion.
replace_once(
    "Core/SRT_Core_21b_Constitutive_Theorems.md",
    "version: v3",
    "version: v4",
)
replace_once(
    "Core/SRT_Core_21b_Constitutive_Theorems.md",
    "dependency: [SRT-CORE-21A-MINIMAL-AXIOMS, SRT-CLAIM-LADDER, SRT-CORE-12B]",
    "dependency: [SRT-CORE-21A-MINIMAL-AXIOMS, SRT-ONE-FORMATION, SRT-CLAIM-LADDER, SRT-CORE-12B]",
)
replace_once(
    "Core/SRT_Core_21b_Constitutive_Theorems.md",
    "P1-T06 therefore does not organize the ontology as `formed process -> Stable ISP -> subject-position`, and it does not decide the canonical owner or necessary-and-sufficient theorem for any thinner formed unity upstream of Stable ISP.",
    "P1-T06 therefore does not organize the ontology as `formed process -> Stable ISP -> subject-position`. The canonical semantic owner for the thinner upstream formation is `Core_Law/SRT_One_Formation.md`; P1-T06 still does not supply a necessary-and-sufficient theorem for One formation.",
)

# 21C B13 — bridge/stabilisation crosswalk, not One owner.
replace_once(
    "Core/SRT_Core_21c_Bridge_Hypotheses.md",
    "dependency: [SRT-CORE-21A-MINIMAL-AXIOMS, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL]",
    "dependency: [SRT-CORE-21A-MINIMAL-AXIOMS, SRT-ONE-FORMATION, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL]",
)
replace_once(
    "Core/SRT_Core_21c_Bridge_Hypotheses.md",
    "Structural stabilisation is therefore not microstate identity, continuous activity, a fixed point, or an attractor label.",
    "**R1 One-formation crosswalk (2026-09-11)**: B13's `formed process` is a broad bridge category, not the definition authority for `One` or `Selection-position`. One-specific formation semantics are owned by `Core_Law/SRT_One_Formation.md`. In particular, `One != structurally stable ISP automatically`; B13 continues to own stabilisation / generative-health distinctions only.\n\nStructural stabilisation is therefore not microstate identity, continuous activity, a fixed point, or an attractor label.",
)

# Individuation — downstream subject-position model; sigma does not back-define formation.
replace_once(
    "Core_Law/SRT_Individuation.md",
    "dependency: [SRT-L0-METAPHYSICS, SRT-CORE-21-MINIMAL-AXIOMS, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-CORE-12B-ONTOLOGY-L2, SRT-PSIF-CANONICAL, SRT-D-VALUE-CANONICAL]",
    "dependency: [SRT-L0-METAPHYSICS, SRT-CORE-21-MINIMAL-AXIOMS, SRT-ONE-FORMATION, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-CORE-12B-ONTOLOGY-L2, SRT-PSIF-CANONICAL, SRT-D-VALUE-CANONICAL]",
)
replace_once(
    "Core_Law/SRT_Individuation.md",
    "本文件是 L1 层的相变理论，填补 L0（选择无主语）与 P1-T06（稳定 ISP 作为持续视角中心）之间的过渡空洞。",
    "本文件是 L1 层的主体位 / 自我意识相变模型，位于 `Core_Law/SRT_One_Formation.md` 已固定的 formed `One / Selection-position` 之后。",
)
replace_once(
    "Core_Law/SRT_Individuation.md",
    "它承担的是**从无主语选择到载视角选择的动力学说明**",
    "它承担的是**从已形成 One / Selection-position 到更强 subject-position / self-consciousness 候选的动力学说明**",
)
replace_once(
    "Core_Law/SRT_Individuation.md",
    "- **Role**: L1 theory of how subjectless selection condenses into perspective-bearing selection; extension (not replacement) of P1-T06 Stable ISP entry conditions.",
    "- **Role**: L1 subject-position / self-consciousness dynamics downstream of `SRT-ONE-FORMATION`; not the owner of One formation and not the definition of Stable-ISP entry.",
)
replace_once(
    "Core_Law/SRT_Individuation.md",
    "- **Depends on**: L0 metaphysics (subjectless selection, position, irreversibility), P1-T06 (Stable ISP / continued selectability), 21C B13 (ST-A conditional generative reselectability), T-L2-Scaffold (path trace).",
    "- **Depends on**: L0 metaphysics (subjectless Selection, finite position, irreversibility), `SRT-ONE-FORMATION` (formed One / Selection-position), P1-T06 (Stable ISP / continued-selectability standing), 21C B13 (ST-A conditional generative reselectability), T-L2-Scaffold (path trace).",
)
replace_once(
    "Core_Law/SRT_Individuation.md",
    "- **Do not change**: Three-phase structure, self-consciousness as condensate (not as innate property), ε/κ₀ roles without explicit cross-check with L0.\n\n---",
    "- **Do not change**: Three-phase structure, self-consciousness as condensate (not as innate property), ε/κ₀ roles without explicit cross-check with L0.\n\n> **R1 owner boundary (2026-09-11)**: `Core_Law/SRT_One_Formation.md` canonically owns active vertical formation, `One`, and ontological `Selection-position`. The `σ_{sr}` family, `σ_{sr}^{sub}`, and T-IND-2 may not be used to define those upstream objects or to override P1-T06 standing. Legacy body phrases that call `σ_{sr}^{sub}` an \"ISP entry\" coordinate remain model-local subject-transition language pending the separate R2 individuation / measurement reconstruction; this R1 landing does not adjudicate the exact subject threshold.\n\n---",
)

# Collective — higher-order One does not bypass T-COLL-1.
replace_once(
    "Core_Law/SRT_Collective_Selection.md",
    "dependency: [SRT-CORE-21-MINIMAL-AXIOMS, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-INDIVIDUATION, SRT-OCCLUSION-DYNAMICS, SRT-SUFFERING, SRT-L1-FORMALISM, SRT-T-DIR-CANONICAL, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL]",
    "dependency: [SRT-CORE-21-MINIMAL-AXIOMS, SRT-ONE-FORMATION, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-INDIVIDUATION, SRT-OCCLUSION-DYNAMICS, SRT-SUFFERING, SRT-L1-FORMALISM, SRT-T-DIR-CANONICAL, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL]",
)
replace_once(
    "Core_Law/SRT_Collective_Selection.md",
    "> **Does not define**：`d-value`、`\\Psi_f`、`T_dir`、stable ISP、Selection occurrence 或 agency；它们的定义与判定仍以对应 canonical / downstream owner 为准。",
    "> **Does not define**：`One / Selection-position`、`d-value`、`\\Psi_f`、`T_dir`、stable ISP、Selection occurrence 或 agency；它们的定义与判定仍以对应 canonical / downstream owner 为准。",
)
replace_once(
    "Core_Law/SRT_Collective_Selection.md",
    "> **RC-A boundary (2026-08-18)**：former P1-T05 / Real Choice Moment 不再承担集体 Selection 或 collective-ISP 的定义权。T-COLL-1 的 stable-ISP extension 回链 P1-T06；脚本、制度自动化、投票或共识本身既不能证明更强 agency，也不能反推“没有 Selection”。",
    "> **RC-A boundary (2026-08-18)**：former P1-T05 / Real Choice Moment 不再承担集体 Selection 或 collective-ISP 的定义权。T-COLL-1 的 stable-ISP extension 回链 P1-T06；脚本、制度自动化、投票或共识本身既不能证明更强 agency，也不能反推“没有 Selection”。\n> **R1 One-formation boundary (2026-09-11)**：`Core_Law/SRT_One_Formation.md` owns `One / Selection-position`. Relation-level or higher-order One language does **not** establish collective ISP automatically; T-COLL-1 remains the separate collective Stable-ISP standing gate. Shared `L_2`, `M(t)`, or collective `σ_{sr}^{coll}` therefore do not back-define One formation.",
)

# Registry — new owner plus corrected downstream routing.
owner_section = """### 13. SRT One Formation（One / Selection-position 形成层 owner）
- 主文件：`Core_Law/SRT_One_Formation.md`
- id：`SRT-ONE-FORMATION`
- layer：L1 / epistemic：os / status：draft_v0 / claim-mode：canonical / claim-level：P1-candidate
- 说明：薄层 canonical semantic owner，固定 `subjectless Selection -> active vertical organization -> One / Selection-position` 的形成语义；verticality 是 Selection-generated / regenerated 的非平坦组织，不是被动历史沉积；One 只按 D4a 强度固定为 localized、lineage-relative、processual formed unity，其持续为 Selection-mediated recurrent reconstitution；`Selection-position_t` 是同一 continuing One 的 time-local operative from-where
- 与 P1-T06 的关系：本文在形成层上游；P1-T06 仍只负责更强 Stable ISP standing。`One != Stable ISP`，且 P1-T06 不反向定义 One
- 与 Individuation / Bearer 的关系：formed Selection-position 不自动推出 perspective-bearing subject-position、Bearer、first-person bearing、consciousness 或 phenomenality；`σ_{sr}` / `d` / `T_dir` 不得反向定义 One
- 与 Collective 的关系：higher-order / relation-level One 不自动成为 collective ISP；T-COLL-1 保持独立 standing gate
- 引用规则：涉及 active vertical formation、One、pre-subject ontological Selection-position、history/verticality typing 与 One/Stable-ISP/subject/Bearer 分界时，优先回链本文件

"""
replace_once(
    "CANONICAL_REGISTRY.md",
    "### 13a. SRT 个体化理论（主体涌现 + 自我意识凝结）",
    owner_section + "### 13a. SRT 个体化理论（主体涌现 + 自我意识凝结）",
)
replace_once(
    "CANONICAL_REGISTRY.md",
    "L1 相变理论，填补 L0（选择无主语）与 P1-T06 Stable ISP 之间的过渡空洞；",
    "L1 主体位 / 自我意识相变模型，位于 `SRT-ONE-FORMATION` 已形成 One / Selection-position 之后；",
)
replace_once(
    "CANONICAL_REGISTRY.md",
    "- 与 P1-T06 的关系：本文件是 ISP 的**进入动力学候选**；P1-T06 是 ISP 的**结果状态判据**（continued selectability）。`σ_{sr}<1` 不单独证明该结果，更不证明 21C B13 的 generative reselectability",
    "- 与 One Formation / P1-T06 的关系：本文件只承担下游 subject-position / self-consciousness 动力学候选；`SRT-ONE-FORMATION` owns formed One / Selection-position，P1-T06 owns stronger Stable-ISP standing。`σ_{sr}` / `σ_{sr}^{sub}` 不定义 One，也不单独证明 Stable ISP 或 21C B13 的 generative reselectability",
)
replace_once(
    "CANONICAL_REGISTRY.md",
    "3. `_SRT_D_VALUE_CANONICAL.md` / `_SRT_PSI_F_CANONICAL.md` / `_SRT_T_DIR_CANONICAL.md` / `_SRT_CROSS_DOMAIN_MATRIX.md` / `Core/SRT_Core_21_Formal_Axioms.md` / `Core/SRT_Core_22_Equations.md`（找规范定义与跨域用法）",
    "3. `_SRT_D_VALUE_CANONICAL.md` / `_SRT_PSI_F_CANONICAL.md` / `_SRT_T_DIR_CANONICAL.md` / `_SRT_CROSS_DOMAIN_MATRIX.md` / `Core_Law/SRT_One_Formation.md` / `Core/SRT_Core_21_Formal_Axioms.md` / `Core/SRT_Core_22_Equations.md`（找规范定义、形成层 owner 与跨域用法）",
)
replace_once(
    "CANONICAL_REGISTRY.md",
    "- `Open tensions` → `Core/SRT_OPEN_TENSIONS.md`",
    "- `Open tensions` → `Core/SRT_OPEN_TENSIONS.md`\n- `One / Selection-position formation` → `Core_Law/SRT_One_Formation.md`",
)

print("PR942 bounded crosswalk edits applied")
