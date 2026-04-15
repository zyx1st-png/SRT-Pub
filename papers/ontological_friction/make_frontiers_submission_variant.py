from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'paper_ontological_friction.md'
OUT = ROOT / 'paper_ontological_friction_frontiers_submission.md'
FIG_CAP = ROOT / 'frontiers_figure_captions.md'

src = SRC.read_text(encoding='utf-8')
fig_caps = FIG_CAP.read_text(encoding='utf-8').strip()
fig_caps = re.sub(r"^# Figure Captions\s*\n+", "", fig_caps)

fig_callouts: list[str] = []
table_blocks: list[str] = []

fig_re = re.compile(
    r"\n\*\*Figure (\d+)\.\*\*.*?\n\n!\[Figure \1\]\([^\n]+\)\{[^\n]+\}\n",
    re.S,
)

def replace_fig(m: re.Match[str]) -> str:
    num = m.group(1)
    fig_callouts.append(num)
    return f"\n*Insert Figure {num} near here.*\n"

body = fig_re.sub(replace_fig, src)


def extract_table_blocks(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^\*\*Table (\d+)\..*\*\*$", line)
        if not m:
            out.append(line)
            i += 1
            continue

        num = m.group(1)
        caption = line
        j = i + 1
        while j < len(lines) and lines[j].strip() == '':
            j += 1
        table_lines: list[str] = []
        while j < len(lines) and lines[j].startswith('|'):
            table_lines.append(lines[j])
            j += 1
        if not table_lines:
            out.append(line)
            i += 1
            continue

        table_blocks.append('\n'.join([caption, ''] + table_lines))
        out.extend(['', f'*Insert Table {num} near here.*', ''])
        i = j
    return '\n'.join(out)

body = extract_table_blocks(body)

# Collapse excess blank lines but preserve markdown section spacing.
body = re.sub(r'\n{4,}', '\n\n\n', body).strip() + '\n\n'

appendix = '## Figure Captions\n\n' + fig_caps + '\n\n## Tables\n\n' + '\n\n'.join(table_blocks).strip() + '\n'

OUT.write_text(body + appendix, encoding='utf-8')

print(f'Wrote {OUT.name}')
print(f'Figure callouts: {", ".join(fig_callouts)}')
print(f'Tables moved: {len(table_blocks)}')
