from pathlib import Path
import re


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def replace_line_prefix(path, prefix, new_line):
    lines = read(path).splitlines()
    idx = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(idx) != 1:
        raise SystemExit(f"{path}: prefix {prefix!r} expected 1 line, found {len(idx)}")
    lines[idx[0]] = new_line
    write(path, "\n".join(lines) + "\n")
    print("LINE", path, prefix)


def replace_block(path, start, end, new_block):
    text = read(path)
    a = text.count(start)
    b = text.count(end)
    if a != 1 or b < 1:
        raise SystemExit(f"{path}: block markers start={a} end={b} for {start!r}")
    i = text.index(start)
    j = text.index(end, i)
    text = text[:i] + new_block.rstrip() + "\n\n" + text[j:]
    write(path, text)
    print("BLOCK", path, start)


def insert_after_once(path, needle, addition):
    text = read(path)
    if addition.strip() in text:
        return
    if text.count(needle) != 1:
        raise SystemExit(f"{path}: insert marker expected 1, found {text.count(needle)}")
    write(path, text.replace(needle, needle + addition, 1))
    print("INSERT", path)


tower = "Core_Law/SRT_Collective_Tower_Hardening_Notes.md"
p1 = "Core_Law/Collective_Tower_Hardening_Notes_Split/00_Part01.md"
p2 = "Core_Law/Collective_Tower_Hardening_Notes_Split/01_Part02.md"

intro_marker = "are not yet specified.\n"
guard = "\n> **RC-A active-use override (2026-08-18)**: former tower language that treated `真实重选率`, `r^{(n→n+1)}`, or T-COLL-4 `共选真实性` as a P1 health / Selection-authenticity gate is superseded. T-COLL-4 is downstream P2/P3 collective agency / consequence-sensitive revision audit only. No scalar reselection rate is a hard condition of collective/tower standing or health; spectral-stability mathematics below must not be read as a Selection ontology test.\n"
for path in (tower, p1):
    insert_after_once(path, intro_marker, guard)

new_hard = """**(iii) 跨尺度健康的附加审计边界（RC-A）**：

层 `n+1` 的健康分析仍需分别检查各层 `\\mathcal{H}^{(n),k}` standing，以及跨尺度耦合、后果返回与结构性外部化；但**不再引入 `r^{(n\\to n+1)}` 或任何替代 scalar rate 作为硬条件**。跨层 consequence-sensitive revision / reorientation 只能作为下游 P2/P3 audit question；它不定义 Selection，也不追加到 P1-T06 / T-COLL-1 standing。"""
for path in (tower, p1):
    replace_block(path, "**(iii) 跨尺度健康的额外硬条件**：", "**(iv) 致命 `L_2` 的塔级刻画**：", new_hard)

for path in (tower, p1):
    replace_line_prefix(
        path,
        "| 健康判据 | 单层 `\\mathcal{H}^{coll}` |",
        "| 健康判据 | 单层 `\\mathcal{H}^{coll}` | 塔级递归 `\\{\\mathcal{H}^{(n)}\\}`；跨尺度 revision / reorientation 另作 P2/P3 audit，不设 scalar-rate 硬门 |",
    )

for path in (tower, p2):
    replace_line_prefix(
        path,
        "1. **健康塔的硬条件**：",
        "1. **健康塔的动力学必要条件候选**：`\\mathcal{H}^{tower} \\Rightarrow \\rho(\\mathcal{T}_{loop}) < 1 - \\delta_{stab}`（带正间隔 `\\delta_{stab} > 0`）。RC-A 后该谱条件只承担塔级反馈稳定性角色，不再映射为 T-COLL-4 / Selection-authenticity 判据。",
    )
    replace_line_prefix(
        path,
        "3. **健康-病理判据的塔级对偶**：",
        "3. **RC-A jurisdiction guard**：`\\rho(\\mathcal{T}_{loop}) < 1` 只表示该线性化反馈环路在给定模型下收敛；它**不等价于**任何“真实重选率”关系，也不得据此推出 T-COLL-4、collective agency 或 Selection authenticity。",
    )
    replace_line_prefix(
        path,
        "| T-COLL-4 共选真实性的塔级递归 |",
        "| T-COLL-4 与塔级谱判据 | 旧版曾映射到单层 T-COLL-4 | **RC-A 后撤销该真实性映射**；谱稳定性只保留为塔级动力学判据，T-COLL-4 另属 P2/P3 collective agency / revision audit |",
    )

pr = "Philosophy/SRT_Political_Rights.md"
replace_line_prefix(
    pr,
    "> **Canonical Collective Selection Layer (2026-04-24)**",
    "> **Canonical Collective Selection Layer (2026-04-24; RC-A sync 2026-08-18)**：本文把投票读为 d 倾向后验验证、把制度读为三层（公检法 / 监督 / 授权）结构——这些在结构层回链 `Core_Law/SRT_Collective_Selection.md`（`SRT-COLLECTIVE-SELECTION`）。投票本身不证明 collective agency；T-COLL-4 仅可作为 downstream consequence-sensitive revision / agency audit input，`A_{\\mathcal{P}}`、`M(t)` 返回与非脚本化等信号不得反向定义 Selection 或追加为 T-COLL-1 的硬条件。制度是集体 ISP 的**器官**不是主体。本文件保留权利与授权的规范性 P2/P3/P4 论述，但集体 ISP standing 与三类退化判据不在本文件重复定义。",
)

sp = "Spirituality/SRT_Spirituality_Community_and_Sangha.md"
replace_line_prefix(
    sp,
    "> **Canonical Collective Selection Layer**:",
    "> **Canonical Collective Selection Layer / RC-A active-use override (2026-08-18)**: 本文所说“共同体”不是自动的集体 ISP。结构 standing 回链 `Core_Law/SRT_Collective_Selection.md`（`SRT-COLLECTIVE-SELECTION`）：T-COLL-1 / P1-T06 承担 collective-ISP standing；ST-A 条件化的 T-COLL-3 与降级后的 T-COLL-4 不得被追加为每个健康共同体或每个 Selection occurrence 的硬条件。T-COLL-4 仅作 downstream collective agency / consequence-sensitive revision audit。本文后文若沿用“真实选择时刻”，只表示 praxis / freedom 层对实质修订、重取向空间的 legacy shorthand，不定义 Selection ontology。“共同体变新地板”对应**收编型退化**（`σ^{coll} → 1`）；“不托举他者苦难、让伤痛外溢”对应**主从型退化**（`M(t)` 不对称）。结构层判据以 canonical 为准，本文只做共同体现象学。",
)

pp = "Philosophy/SRT_Political_Philosophy.md"
replace_line_prefix(
    pp,
    "> **Canonical Collective Selection Layer (2026-04-24; ST-A correction 2026-08-11)**",
    "> **Canonical Collective Selection Layer (2026-04-24; ST-A correction 2026-08-11; RC-A sync 2026-08-18)**：本文涉及“多主体共同现实选择”、合法性、反支配、结构性不公、危机决断与民主等 P2/P3 政治哲学读法，结构层回链 `Core_Law/SRT_Collective_Selection.md`。T-COLL-1、三类退化、ST-A 条件性 T-COLL-3 与降级后的 T-COLL-4 不在本文件重新定义。集体四变量 ODE、申诉／轮替／异议通道、`M(t)` 或 `ΔR_future` 只能提供 generative-reselectability、consequence-sensitive revision 与外部化风险的候选审计信号；它们不自动构成 Selection、collective agency 或合法性的必要充分条件，也不能从结构稳定直接推出规范正当性。具体制度判断继续按 P3/P4 读。本文若保留旧版“真实选择时刻”措辞，只能按 downstream freedom / agency shorthand 读取，不得反向定义 Selection ontology。",
)

new_free = """> **自由（P2/P3 政治规范性读法）= 主体保有可后果敏感地修订 / 重取向其行动，并以可实现方式进入共同现实塑造过程的空间。**

因此：

- 形式选项再多，若实质修订 / 重取向空间被预先锁死，仍可能不自由
- 只有私人生活自由、没有公共进入权，也是不完整自由
- 被迫在别人已经写好的 `L_2` 里做微调，不算完整自由"""
replace_block(pp, "> **自由 = 真实选择时刻被保留", "### 4.2 平等：", new_free + "\n\n")
replace_line_prefix(pp, "- 形式在，真实选择时刻消失", "- 形式在，实质修订 / 重取向空间消失")

# Fail-loud on the exact stale claims identified by the final review.
checks = {
    tower: ["跨尺度真实重选率", "r^{(n\\to n+1)}(t) > r_{min}^{nested}", "共选真实性 `r > r_{min}`", "顶层叙事可被底层真实重选 vs"],
    p1: ["跨尺度真实重选率", "r^{(n\\to n+1)}(t) > r_{min}^{nested}"],
    p2: ["共选真实性 `r > r_{min}`", "顶层叙事可被底层真实重选 vs"],
    pr: ["按 T-COLL-4 共选真实性判据"],
    sp: ["健康共同体需同时满足 T-COLL-1 四条件、T-COLL-3 集体 ε 反闭合维持、T-COLL-4 真实共选判据"],
    pp: ["自由 = 真实选择时刻被保留", "`r^{coll}(t)>r^{coll}_{min}`", "形式在，真实选择时刻消失"],
}
for path, needles in checks.items():
    text = read(path)
    for needle in needles:
        if needle in text:
            raise SystemExit(f"stale claim remains in {path}: {needle}")

print("RC-A final-review repair v2 complete")
