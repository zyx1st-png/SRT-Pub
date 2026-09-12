#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "scripts/build_srt_context_bundles.py"
text = p.read_text(encoding="utf-8")

old = '''def parse_first_sources() -> list[str]:
    """解析 `SRT_AI_START.md` 中「当前 canonical 权威链」的有序清单。

    2026-08-29 的 AI_START 重构把原 §2 `First Sources` 改写为
    「Current formal/canonical sources remain historically authoritative
    until audited」区段；两者承担同一契约——按优先级列出当前登记的
    canonical 权威文件——因此这里按标题文字（而非章节号）定位，重构
    重新编号时不再断裂。
    """
    text = read_text("SRT_AI_START.md")
    m = re.search(r"^##\\s+\\d+\\.\\s+Current formal/canonical sources.*$", text, re.M)
    if m is None:
        fail("锚点缺失：SRT_AI_START.md 中找不到当前 canonical 权威链区段")
    start = m.start()
    nxt = re.search(r"^##\\s+", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    seen: list[str] = []
    # Only the numbered precedence list is unconditional. The prose immediately
    # below it names conditional sources such as OPEN_TENSIONS; treating every
    # backticked path in the section as a mandatory spine member defeats that
    # distinction and makes the budget contract depend on optional deep reads.
    numbered = re.findall(r"^\\d+\\.\\s+`([^`]+\\.md)`", text[start:end], re.M)
    for path in numbered:
        if path not in seen:
            seen.append(path)
    if not seen:
        fail("锚点缺失：SRT_AI_START.md §2 中解析不到任何路径")
    return seen
'''

new = '''def parse_authority_sources() -> list[str]:
    """从唯一完整 owner `CANONICAL_REGISTRY.md §C` 解析当前 citation-priority 路径。

    R2-A 起，runtime/bootstrap 文件只投影 Registry，不再维护第二份完整 authority chain。
    因此 context-bundle manifest 也必须直接读 Registry，而不能要求 `SRT_AI_START.md`
    重复一份 numbered list。这里保留 §C 的顺序，并把同一优先级行中的多个路径按出现
    顺序展开；非路径条目（domain claim-status files、split、原始长文）不强造为文件。
    """
    text = read_text("CANONICAL_REGISTRY.md")
    m = re.search(r"^##\\s+C\\.\\s+当前 canonical 引用优先级\\s*$", text, re.M)
    if m is None:
        fail("锚点缺失：CANONICAL_REGISTRY.md 中找不到 §C 当前 canonical 引用优先级")
    nxt = re.search(r"^##\\s+", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    section = text[m.end():end]

    seen: list[str] = []
    for line in section.splitlines():
        if not re.match(r"^\\d+\\.\\s+", line):
            continue
        for path in re.findall(r"`([^`]+\\.md)`", line):
            if path not in seen:
                seen.append(path)
    if not seen:
        fail("锚点缺失：CANONICAL_REGISTRY.md §C 中解析不到任何 .md 路径")
    return seen
'''

if old not in text:
    raise SystemExit("parse_first_sources anchor not found")
text = text.replace(old, new, 1)

text = text.replace('"Core_Law/SRT_L0_Metaphysics.md": ("定义源", "AI_START §2 First Sources 第 4 位"),',
                    '"Core_Law/SRT_L0_Metaphysics.md": ("定义源", "registry §C local-owner layer"),')
text = text.replace('"_SRT_SYMBOL_TABLE.md": ("定义源", "AI_START §2 First Sources；符号与记号的定义权"),',
                    '"_SRT_SYMBOL_TABLE.md": ("定义源", "symbol owner；Registry/local routing as applicable"),')
text = text.replace('first_sources = parse_first_sources()', 'first_sources = parse_authority_sources()')
text = text.replace('fs = "✓" if path in first_sources else "—"', 'fs = "✓" if path in first_sources else "—"')
text = text.replace('> 「registry 提及」「AI_START §2」两列是机械判定的事实。',
                    '> 「registry 提及」「Registry §C priority」两列是机械判定的事实。')
text = text.replace('| 文件 | 分类依据 | registry 提及 | AI_START §2 |',
                    '| 文件 | 分类依据 | registry 提及 | Registry §C priority |')
text = text.replace('**⚠ 高严重度：`SRT_AI_START.md` §2 First Sources 中有 {len(fs_broken)} 条路径',
                    '**⚠ 高严重度：`CANONICAL_REGISTRY.md` §C priority 中有 {len(fs_broken)} 条路径')

# There may be later prose labels mentioning First Sources; normalize them to the single source.
text = text.replace('First Sources', 'Registry §C priority')
text = text.replace('AI_START §2', 'Registry §C')

p.write_text(text, encoding="utf-8")
print("R2-A bundle authority source migrated to CANONICAL_REGISTRY §C")
