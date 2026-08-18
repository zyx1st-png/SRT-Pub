from pathlib import Path
import subprocess


def replace_exact(path: str, old: str, new: str, count: int = 1) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    found = text.count(old)
    if found != count:
        raise SystemExit(f"{path}: expected {count} matches, found {found}: {old[:120]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")
    print(f"REPLACED {path}: {found}")


tower = "Core_Law/SRT_Collective_Tower_Hardening_Notes.md"
tower_p1 = "Core_Law/Collective_Tower_Hardening_Notes_Split/00_Part01.md"
tower_p2 = "Core_Law/Collective_Tower_Hardening_Notes_Split/01_Part02.md"

old_intro = """This file preserves H10-H16 tower/nested hardening material originally drafted
inside `Core_Law/SRT_Collective_Selection.md`. These sections are not part of
the minimal canonical definition of collective selection. They are late-stage
hardening material: P1-candidate only under strong closure assumptions, with
P2/P3 operational debt wherever closure, measurability, or stability conditions
are not yet specified.
"""
new_intro = old_intro + """
> **RC-A active-use override (2026-08-18)**: former tower language that treated `真实重选率`, `r^{(n→n+1)}`, or T-COLL-4 `共选真实性` as a P1 health / Selection-authenticity gate is superseded. T-COLL-4 is downstream P2/P3 collective agency / consequence-sensitive revision audit only. No scalar reselection rate is a hard condition of collective/tower standing or health; spectral-stability mathematics below must not be read as a Selection ontology test.
"""
replace_exact(tower, old_intro, new_intro)
replace_exact(tower_p1, old_intro, new_intro)

old_hard = """**(iii) 跨尺度健康的额外硬条件**：

$$
\\mathcal{H}^{(n+1)} \\text{ 要求}：\\quad \\bigl(\\forall k:\\; \\mathcal{P}^{(n),k} \\in \\mathcal{H}^{(n),k}\\bigr) \\;\\wedge\\; r^{(n\\to n+1)}(t) > r_{min}^{nested} > 0
$$

其中 `r^{(n\\to n+1)}` 是跨尺度真实重选率：层 `n+1` 在层 `n` 子集体之间能进行真实重选的频率（即上层不锁死下层 / 下层不绑架上层）。这是 T-COLL-4 共选真实性判据在跨尺度上的递归扩展。
"""
new_hard = """**(iii) 跨尺度健康的附加审计边界（RC-A）**：

层 `n+1` 的健康分析仍需分别检查各层 `\\mathcal{H}^{(n),k}` standing，以及跨尺度耦合、后果返回与结构性外部化；但**不再引入 `r^{(n\\to n+1)}` 或任何替代 scalar rate 作为硬条件**。跨层 consequence-sensitive revision / reorientation 只能作为下游 P2/P3 audit question；它不定义 Selection，也不追加到 P1-T06 / T-COLL-1 standing。
"""
replace_exact(tower, old_hard, new_hard)
replace_exact(tower_p1, old_hard, new_hard)

old_table = "| 健康判据 | 单层 `\\mathcal{H}^{coll}` | 塔级递归 `\\{\\mathcal{H}^{(n)}\\}` + 跨尺度 `r^{(n\\to n+1)} > r_{min}^{nested}` |"
new_table = "| 健康判据 | 单层 `\\mathcal{H}^{coll}` | 塔级递归 `\\{\\mathcal{H}^{(n)}\\}`；跨尺度 revision / reorientation 另作 P2/P3 audit，不设 scalar-rate 硬门 |"
replace_exact(tower, old_table, new_table)
replace_exact(tower_p1, old_table, new_table)

old_prop1 = "1. **健康塔的硬条件**：`\\mathcal{H}^{tower} \\Rightarrow \\rho(\\mathcal{T}_{loop}) < 1 - \\delta_{stab}`（带正间隔 `\\delta_{stab} > 0$，对应 T-COLL-4 共选真实性的塔级递归形式）"
new_prop1 = "1. **健康塔的动力学必要条件候选**：`\\mathcal{H}^{tower} \\Rightarrow \\rho(\\mathcal{T}_{loop}) < 1 - \\delta_{stab}`（带正间隔 `\\delta_{stab} > 0$）。RC-A 后该谱条件只承担塔级反馈稳定性角色，不再映射为 T-COLL-4 / Selection-authenticity 判据。"
replace_exact(tower, old_prop1, new_prop1)
replace_exact(tower_p2, old_prop1, new_prop1)

old_prop3 = "3. **健康-病理判据的塔级对偶**：`\\rho(\\mathcal{T}_{loop}) < 1$ ⟺ **顶层叙事在底层可被真实重选的速率 ≥ 顶层叙事被反向写回底层的速率**——这是 T-COLL-4 共选真实性 `r > r_{min}$ 在塔级 + 自指闭合下的递归同构。"
new_prop3 = "3. **RC-A jurisdiction guard**：`\\rho(\\mathcal{T}_{loop}) < 1$ 只表示该线性化反馈环路在给定模型下收敛；它**不等价于**任何“真实重选率”关系，也不得据此推出 T-COLL-4、collective agency 或 Selection authenticity。"
replace_exact(tower, old_prop3, new_prop3)
replace_exact(tower_p2, old_prop3, new_prop3)

old_meaning = "| T-COLL-4 共选真实性的塔级递归 | 单层（§6 T-COLL-4） | 塔级（顶层叙事可被底层真实重选 vs 反向写回的速率比） |"
new_meaning = "| T-COLL-4 与塔级谱判据 | 旧版曾映射到单层 T-COLL-4 | **RC-A 后撤销该真实性映射**；谱稳定性只保留为塔级动力学判据，T-COLL-4 另属 P2/P3 collective agency / revision audit |"
replace_exact(tower, old_meaning, new_meaning)
replace_exact(tower_p2, old_meaning, new_meaning)

# Political Rights: re-scope T-COLL-4 to downstream audit.
pr = "Philosophy/SRT_Political_Rights.md"
old_pr = "> **Canonical Collective Selection Layer (2026-04-24)**：本文把投票读为 d 倾向后验验证、把制度读为三层（公检法 / 监督 / 授权）结构——这些在结构层回链 `Core_Law/SRT_Collective_Selection.md`（`SRT-COLLECTIVE-SELECTION`）。按 T-COLL-4 共选真实性判据，投票不自动是共选（需同时满足 `A_{\\mathcal{P}}` 真实扩展、`M(t)` 对称、非脚本化）；制度是集体 ISP 的**器官**不是主体。本文件保留权利与授权的规范性 P2/P3/P4 论述，但集体 ISP 条件、三类退化判据与共选真实性判据不在本文件重复定义。"
new_pr = "> **Canonical Collective Selection Layer (2026-04-24; RC-A sync 2026-08-18)**：本文把投票读为 d 倾向后验验证、把制度读为三层（公检法 / 监督 / 授权）结构——这些在结构层回链 `Core_Law/SRT_Collective_Selection.md`（`SRT-COLLECTIVE-SELECTION`）。投票本身不证明 collective agency；T-COLL-4 仅可作为 downstream consequence-sensitive revision / agency audit input，`A_{\\mathcal{P}}`、`M(t)` 返回与非脚本化等信号不得反向定义 Selection 或追加为 T-COLL-1 的硬条件。制度是集体 ISP 的**器官**不是主体。本文件保留权利与授权的规范性 P2/P3/P4 论述，但集体 ISP standing 与三类退化判据不在本文件重复定义。"
replace_exact(pr, old_pr, new_pr)

# Spirituality: remove T-COLL-4 as a necessary healthy-community condition; guard legacy phrase.
sp = "Spirituality/SRT_Spirituality_Community_and_Sangha.md"
old_sp = "> **Canonical Collective Selection Layer**: 本文所说\"共同体\"不是自动的集体 ISP。按 `Core_Law/SRT_Collective_Selection.md`（`SRT-COLLECTIVE-SELECTION`）：健康共同体需同时满足 T-COLL-1 四条件、T-COLL-3 集体 ε 反闭合维持、T-COLL-4 真实共选判据；\"共同体变新地板\"对应**收编型退化**（`σ^{coll} → 1`）；\"不托举他者苦难、让伤痛外溢\"对应**主从型退化**（`M(t)` 不对称）。结构层判据以 canonical 为准，本文只做共同体现象学。"
new_sp = "> **Canonical Collective Selection Layer / RC-A active-use override (2026-08-18)**: 本文所说\"共同体\"不是自动的集体 ISP。结构 standing 回链 `Core_Law/SRT_Collective_Selection.md`（`SRT-COLLECTIVE-SELECTION`）：T-COLL-1 / P1-T06 承担 collective-ISP standing；ST-A 条件化的 T-COLL-3 与降级后的 T-COLL-4 不得被追加为每个健康共同体或每个 Selection occurrence 的硬条件。T-COLL-4 仅作 downstream collective agency / consequence-sensitive revision audit。本文后文若沿用\"真实选择时刻\"，只表示 praxis / freedom 层对实质修订、重取向空间的 legacy shorthand，不定义 Selection ontology。\"共同体变新地板\"对应**收编型退化**（`σ^{coll} → 1`）；\"不托举他者苦难、让伤痛外溢\"对应**主从型退化**（`M(t)` 不对称）。结构层判据以 canonical 为准，本文只做共同体现象学。"
replace_exact(sp, old_sp, new_sp)

# Political Philosophy: remove dangling r-coll and reframe freedom / later shorthand.
pp = "Philosophy/SRT_Political_Philosophy.md"
old_pp_head = "> **Canonical Collective Selection Layer (2026-04-24; ST-A correction 2026-08-11)**：本文涉及\"多主体共同现实选择\"、合法性、反支配、结构性不公、危机决断与民主等 P2/P3 政治哲学读法，结构层回链 `Core_Law/SRT_Collective_Selection.md`。T-COLL-1、三类退化、ST-A 条件性 T-COLL-3 与 T-COLL-4 不在本文件重新定义。集体四变量 ODE、`r^{coll}(t)>r^{coll}_{min}`、申诉／轮替／异议通道、`M(t)` 或 `ΔR_future` 只能提供 generative-reselectability 与外部化风险的候选审计信号；它们不自动构成合法性的必要充分条件，也不能从结构稳定直接推出规范正当性。具体制度判断继续按 P3/P4 读。"
new_pp_head = "> **Canonical Collective Selection Layer (2026-04-24; ST-A correction 2026-08-11; RC-A sync 2026-08-18)**：本文涉及\"多主体共同现实选择\"、合法性、反支配、结构性不公、危机决断与民主等 P2/P3 政治哲学读法，结构层回链 `Core_Law/SRT_Collective_Selection.md`。T-COLL-1、三类退化、ST-A 条件性 T-COLL-3 与降级后的 T-COLL-4 不在本文件重新定义。集体四变量 ODE、申诉／轮替／异议通道、`M(t)` 或 `ΔR_future` 只能提供 generative-reselectability、consequence-sensitive revision 与外部化风险的候选审计信号；它们不自动构成 Selection、collective agency 或合法性的必要充分条件，也不能从结构稳定直接推出规范正当性。具体制度判断继续按 P3/P4 读。本文若保留旧版“真实选择时刻”措辞，只能按 downstream freedom / agency shorthand 读取，不得反向定义 Selection ontology。"
replace_exact(pp, old_pp_head, new_pp_head)

old_free = "> **自由 = 真实选择时刻被保留，以及主体能以可实现方式进入共同现实塑造过程。**\n\n因此：\n\n- 没有真实选择时刻，选项再多也可能不自由\n- 只有私人生活自由、没有公共进入权，也是不完整自由\n- 被迫在别人已经写好的 `L_2` 里做微调，不算完整自由"
new_free = "> **自由（P2/P3 政治规范性读法）= 主体保有可后果敏感地修订 / 重取向其行动，并以可实现方式进入共同现实塑造过程的空间。**\n\n因此：\n\n- 形式选项再多，若实质修订 / 重取向空间被预先锁死，仍可能不自由\n- 只有私人生活自由、没有公共进入权，也是不完整自由\n- 被迫在别人已经写好的 `L_2` 里做微调，不算完整自由"
replace_exact(pp, old_free, new_free)
replace_exact(pp, "- 形式在，真实选择时刻消失", "- 形式在，实质修订 / 重取向空间消失")

# Fail-loud targeted stale patterns after repair.
for path, forbidden in {
    tower: ["真实重选率", "r^{(n\\to n+1)}(t) > r_{min}^{nested}", "共选真实性 `r > r_{min}`", "顶层叙事可被底层真实重选 vs"],
    tower_p1: ["真实重选率", "r^{(n\\to n+1)}(t) > r_{min}^{nested}"],
    tower_p2: ["共选真实性 `r > r_{min}`", "顶层叙事可被底层真实重选 vs"],
    pr: ["按 T-COLL-4 共选真实性判据"],
    sp: ["健康共同体需同时满足 T-COLL-1 四条件、T-COLL-3 集体 ε 反闭合维持、T-COLL-4 真实共选判据"],
    pp: ["自由 = 真实选择时刻被保留", "`r^{coll}(t)>r^{coll}_{min}`", "形式在，真实选择时刻消失"],
}.items():
    text = Path(path).read_text(encoding="utf-8")
    for needle in forbidden:
        if needle in text:
            raise SystemExit(f"stale pattern remains in {path}: {needle}")

print("RC-A final-review exact repair complete")
