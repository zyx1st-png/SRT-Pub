from pathlib import Path

p = Path(__file__).resolve().parent / 'CostlySelectiveClosure_v18_ArtificialLife_candidate.md'
t = p.read_text(encoding='utf-8')
old = 'costly_selective_closure_supplement/figures/figure1_design_v17.svg'
new = 'costly_selective_closure_supplement/figures/figure1_design_v18.svg'
count = t.count(old)
if count != 1:
    raise SystemExit(f'expected exactly one old Figure 1 reference; found {count}')
t = t.replace(old, new, 1)
p.write_text(t, encoding='utf-8')
print('PASS: switched candidate to figure1_design_v18.svg')
