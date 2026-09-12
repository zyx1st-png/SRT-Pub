#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "scripts/build_srt_context_bundles.py"
text = p.read_text(encoding="utf-8")

new_func = '''def parse_authority_sources() -> list[str]:
    """从唯一完整 owner `CANONICAL_REGISTRY.md §C` 解析当前 citation-priority 路径。

    R2-A 起，runtime/bootstrap 文件只投影 Registry，不再维护第二份完整 authority chain。
    因此 context-bundle manifest 也必须直接读 Registry。这里保留 §C 的顺序，并把同一
    优先级行中的多个路径按出现顺序展开；非路径条目不强造为文件。
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
pattern = r"def parse_first_sources\(\) -> list\[str\]:\n.*?(?=^def \w+\()"
text, n = re.subn(pattern, lambda _m: new_func, text, count=1, flags=re.M | re.S)
if n != 1:
    raise SystemExit(f"parse_first_sources function boundary replacement failed: {n}")

text = text.replace('"Core_Law/SRT_L0_Metaphysics.md": ("定义源", "AI_START §2 First Sources 第 4 位"),',
                    '"Core_Law/SRT_L0_Metaphysics.md": ("定义源", "registry §C local-owner layer"),')
text = text.replace('"_SRT_SYMBOL_TABLE.md": ("定义源", "AI_START §2 First Sources；符号与记号的定义权"),',
                    '"_SRT_SYMBOL_TABLE.md": ("定义源", "symbol owner；Registry/local routing as applicable"),')
text = text.replace('parse_first_sources()', 'parse_authority_sources()')
text = text.replace('First Sources', 'Registry §C priority')
text = text.replace('AI_START §2', 'Registry §C')
p.write_text(text, encoding="utf-8")

# Synchronize the builder tests with the Registry-owned authority contract.
tp = ROOT / "scripts/test_build_context_bundles.py"
test = tp.read_text(encoding="utf-8")
test = test.replace('parse_first_sources', 'parse_authority_sources')
test = test.replace('first_sources', 'authority_sources')
test = test.replace('First Sources', 'Registry §C authority sources')
test = test.replace('First Source', 'Registry §C authority source')

test = test.replace('''    check("Registry §C authority sources 解析非空", len(authority_sources) >= 10, f"got {len(authority_sources)}")
    check("registry 提及解析非空", len(mentioned) >= 50, f"got {len(mentioned)}")
''', '''    check("Registry §C authority sources 解析非空", len(authority_sources) >= 10,
          f"got {len(authority_sources)}")
    check("Registry §C 把 generative spine 放在 local owners 之前",
          authority_sources.index("Core_Law/SRT_Generative_Ontology_Spine.md")
          < authority_sources.index("Core_Law/SRT_L0_Metaphysics.md"))
    check("registry 提及解析非空", len(mentioned) >= 50, f"got {len(mentioned)}")
''', 1)

# The SPINE bundle is explicitly curated/budgeted, not the complete closure of Registry §C.
# Replace any legacy "all authority files must be in SPINE" assertion with an order-projection check.
projection_block = '''    projected_authority = [p for p in authority_sources if p in B.SPINE]
    projected_positions = [B.SPINE.index(p) for p in projected_authority]
    check("Registry §C authority projection 顺序与 SPINE 一致",
          projected_positions == sorted(projected_positions),
          f"projection={projected_authority}")
'''
legacy_projection_pattern = (
    r"    missing_(?:fs|authority) = \[p for p in authority_sources\n"
    r"(?:.*\n){1,3}?"
    r"    check\([^\n]*SPINE[^\n]*\)\n"
)
test, replaced = re.subn(
    legacy_projection_pattern,
    lambda _m: projection_block,
    test,
    count=1,
    flags=re.M,
)
if replaced != 1:
    raise SystemExit(f"legacy SPINE completeness assertion replacement failed: {replaced}")

tp.write_text(test, encoding="utf-8")

print("R2-A bundle authority source + tests migrated to CANONICAL_REGISTRY §C")
