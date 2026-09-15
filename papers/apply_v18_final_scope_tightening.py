from pathlib import Path

p = Path(__file__).resolve().parent / 'CostlySelectiveClosure_v18_ArtificialLife_candidate.md'
t = p.read_text(encoding='utf-8')

replacements = [
    (
        'Artificial-life comparisons often treat mortality, persistent damage, and difficult recovery as if they lay on a common axis of failure consequence.',
        'Mortality, persistent damage, and difficult recovery can all be described informally as making failure more consequential, but it is not clear that they lie on a common ordered axis.',
        'abstract opening',
    ),
    (
        'The remaining comparative gap is narrower and more methodological. Artificial-life discussions often move between statements such as:',
        'The remaining comparative gap is narrower and more methodological. Cross-substrate artificial-life comparisons can involve statements such as:',
        'related-work framing',
    ),
]

for old, new, label in replacements:
    n = t.count(old)
    if n != 1:
        raise SystemExit(f'expected exactly one {label}; found {n}')
    t = t.replace(old, new, 1)

p.write_text(t, encoding='utf-8')
print('PASS: final scope framing tightened without changing evidence or claims')
