from pathlib import Path


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def replace_line_prefix(path, prefix, new_line):
    lines = read(path).splitlines()
    idx = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(idx) != 1:
        raise SystemExit(f"{path}: prefix {prefix!r} expected 1, found {len(idx)}")
    lines[idx[0]] = new_line
    write(path, "\n".join(lines) + "\n")
    print("LINE", path, prefix)


def replace_exact(path, old, new, count=1):
    text = read(path)
    found = text.count(old)
    if found != count:
        raise SystemExit(f"{path}: expected {count} occurrences, found {found}: {old!r}")
    write(path, text.replace(old, new))
    print("EXACT", path, old[:80])


def insert_after(path, needle, addition):
    text = read(path)
    if addition.strip() in text:
        return
    if text.count(needle) != 1:
        raise SystemExit(f"{path}: insertion marker expected 1, found {text.count(needle)}")
    write(path, text.replace(needle, needle + addition, 1))
    print("INSERT", path)


tower = "Core_Law/SRT_Collective_Tower_Hardening_Notes.md"
split = "Core_Law/Collective_Tower_Hardening_Notes_Split/00_Part01.md"
for path in (tower, split):
    replace_line_prefix(
        path,
        "4. **不**给出 `r_{min}^{nested}` 的实证窗口",
        "4. **RC-A 撤回项**：former `r_{min}^{nested}` scalar-rate window 不再是当前塔级 standing / health 的待定门槛；跨尺度 revision / reorientation 若需实证化，另按 P2/P3 audit 处理，不回填 scalar hard gate。",
    )
    replace_line_prefix(
        path,
        "| 跨尺度健康硬条件 | 隐含 |",
        "| 跨尺度健康硬条件 | 旧版隐含 | **RC-A 撤回 scalar-rate 硬门**：每层 standing / health 分别审计；跨尺度 revision / reorientation 仅作 P2/P3 audit |",
    )
    replace_exact(
        path,
        "**P1-candidate 地位的根据**：T-PROJ-1^{coll,nested} 把\"多层嵌套\"从开放问题升为递归投影定理。要升 P1：(a) 具体塔的层数与 T-COLL-1 各层验证；(b) 跨尺度 `M^{(n\\to n+1)}` 的 MOC 多层版本；(c) `r_{min}^{nested}` 实证窗口；(d) 跨层耦合（layer-skip）的边界条件。",
        "**P1-candidate 地位的根据（RC-A sync）**：T-PROJ-1^{coll,nested} 把\"多层嵌套\"从开放问题升为递归投影构造候选。若讨论其更高 claim standing，仍需：(a) 具体塔的层数与 T-COLL-1 各层验证；(b) 跨尺度 `M^{(n\\to n+1)}` 的 MOC 多层版本；(c) 跨层耦合（layer-skip）的边界条件。former `r_{min}^{nested}` 不再属于升级条件。",
    )

ops = "Operations/SRT_CROSS_SCALE_GENERATIVE_EMERGENCE_AUDIT_2026-07-12.md"
insert_after(
    ops,
    "> **执行基线**：`c47d6b35989f9af09daa132dc9ce64c9b21c0679`（= main HEAD，PR #659 合并点）。所有 SHA、覆盖判断以此基线为准；后续任何目标文件被新 PR 更新，须重跑对应行。\n",
    "\n> **RC-A supersession note (2026-08-18)**：本文件是 2026-07-12 coverage snapshot；其中把 tower-level `r^{(n→n+1)}` / `真实重选率` 记作现行 P1-candidate hardening 的行，已被 RC-A Phase-0 后续裁决 supersede。当前 tower owner 已删除 scalar-rate hard gate；跨尺度 consequence-sensitive revision / reorientation 仅属 P2/P3 audit，不得把本审计的旧“已有”判断当作现行 authority。\n",
)
replace_line_prefix(
    ops,
    "| 上层不锁死下层 / 下层不捕获上层 |",
    "| 上层不锁死下层 / 下层不捕获上层 | `Collective_Tower_Hardening_Notes.md` 当前以跨尺度耦合、后果返回与 P2/P3 revision / reorientation audit 表述；former scalar `r^{(n→n+1)}` hard gate 已由 RC-A 删除 | P2/P3 audit + P1-candidate tower dynamics | **RC-A 后需分层读取**——方向性风险仍有审计价值，但 scalar reselection-rate 不是当前 hard condition |",
)
replace_line_prefix(
    ops,
    "- **`Collective_Tower_Hardening_Notes.md`**（blob `d544080b5789`",
    "- **`Collective_Tower_Hardening_Notes.md`**（本文件原基线 blob `d544080b5789`；RC-A superseded 2026-08-18）：原基线曾以 `r^{(n→n+1)}` 表述“上层不锁死下层/下层不绑架上层”。当前 owner 已删除该 scalar-rate hard gate，保留跨尺度耦合 / 后果返回分析，并把 consequence-sensitive revision / reorientation 限于 P2/P3 audit。故本行旧“已有 P1-candidate hardening”判断不再作为现行覆盖证据。",
)

# Remove accidentally tracked runtime inventory; final inventory is an artifact only.
inv = Path("rca-final-review-strengthened-inventory.txt")
if inv.exists():
    inv.unlink()
    print("DELETE", inv)

# Fail loud on active stale positive assertions targeted in this pass.
for path in (tower, split):
    text = read(path)
    for stale in [
        "| 跨尺度健康硬条件 | 隐含 | (iii) 显式：每层健康 + 跨尺度 `r^{(n\\to n+1)} > r_{min}^{nested}` |",
        "(c) `r_{min}^{nested}` 实证窗口",
        "4. **不**给出 `r_{min}^{nested}` 的实证窗口——这是 P3/P4",
    ]:
        if stale in text:
            raise SystemExit(f"stale tower assertion remains: {path}: {stale}")

text = read(ops)
for stale in [
    "| 上层不锁死下层 / 下层不捕获上层 | `Collective_Tower_Hardening_Notes.md` line 133：跨尺度真实重选率 `r^{(n→n+1)}` | P1-candidate hardening | **已有** |",
    "已含\"上层不锁死下层/下层不绑架上层\"（`r^{(n→n+1)}`）。**本轮不修改**（Phase G3 → 不改）。",
]:
    if stale in text:
        raise SystemExit(f"stale coverage assertion remains: {stale}")

print("final RC-A derivative cleanup v3 complete")
