from pathlib import Path

p = Path(__file__).resolve().parent / 'CostlySelectiveClosure_v18_ArtificialLife_candidate.md'
t = p.read_text(encoding='utf-8')

old_main = '''After the cooperation bonus is withdrawn, mean mutual cooperation is `0.548` in the terminal condition and `0.0367` in the restore condition across 30 paired seeds. The paired difference is approximately `0.511`, with the two-sided paired sign-flip permutation test at the 20,000-resample resolution floor (`p < 0.0001`). The auxiliary simulated-stake condition averages `0.0725`, remaining much closer to restore than terminal.'''
new_main = '''After the cooperation bonus is withdrawn, mean mutual cooperation is `0.548` in the terminal condition and `0.0367` in the restore condition across 30 matched seeds. The historical Experiment 1 result file was analysed with a two-sided **two-sample label-permutation test** that pooled the terminal and restore outcomes before permuting regime labels; the mean difference is `0.51115` and the 20,000-resample p-value is `0.0000499975`. Because the design used matched seeds, the v18 evidence audit additionally applied a two-sided **paired sign-flip sensitivity analysis** to the 30 per-seed differences without retraining or replacing the historical result. It reached the same resampling floor (`p = 0.0000499975`): 24 of 30 paired differences were positive, 2 were exactly zero, and 4 were negative. This paired analysis is a post-hoc statistical sensitivity check, not part of a preregistered Experiment 1 analysis. The auxiliary simulated-stake condition averages `0.0725`, remaining much closer to restore than terminal.'''

old_zero = '''The zero-penalty ablation retains the main separation: post-withdrawal cooperation is approximately `0.50` under terminal failure and `0.05` under restoration (`p < 0.0001`). Thus the main result cannot be attributed solely to the manually specified depletion penalty.'''
new_zero = '''The zero-penalty ablation retains the main separation: post-withdrawal cooperation is approximately `0.50` under terminal failure and `0.05` under restoration. Its historical two-sample label-permutation p-value is again at the 20,000-resample floor (`p = 0.0000499975`). The same post-hoc paired sign-flip sensitivity analysis also gives `p = 0.0000499975`, with 25 of 30 paired differences positive. Thus the main separation cannot be attributed solely to the manually specified depletion penalty, and its statistical direction is unchanged when the matched-seed structure is used as a sensitivity analysis.'''

for old, new, label in [(old_main, new_main, 'main E1 paragraph'), (old_zero, new_zero, 'zero-penalty paragraph')]:
    n = t.count(old)
    if n != 1:
        raise SystemExit(f'expected exactly one {label}; found {n}')
    t = t.replace(old, new, 1)

p.write_text(t, encoding='utf-8')
print('PASS: E1 statistical labels corrected transparently')
