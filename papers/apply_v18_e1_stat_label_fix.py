from pathlib import Path

p = Path(__file__).resolve().parent / 'CostlySelectiveClosure_v18_ArtificialLife_candidate.md'
t = p.read_text(encoding='utf-8')

old_methods = '''The two regimes use the same programmed immediate reward function, observation features, base energy dynamics, policy architecture, schedule, and seeds. A matched depletion penalty of `2.0` is applied in the main comparison. Because the terminal transition ends the future return stream of that episode and changes subsequent state occupancy, termination does not merely relabel the same trajectory; those changes are part of the intervention.'''
new_methods = '''The two regimes use the same programmed immediate reward function, observation features, base energy dynamics, policy architecture, schedule, and seeds. A matched depletion penalty of `2.0` is applied in the main comparison. Because the terminal transition ends the future return stream of that episode and changes subsequent state occupancy, termination does not merely relabel the same trajectory; those changes are part of the intervention.\n\nThe historical Experiment 1 result files were analysed with a two-sided **two-sample label-permutation test** using 20,000 resamples: the terminal and restore outcomes were pooled, regime labels were permuted, and the difference in group means was recomputed. Although the same 30 seeds were run in both regimes, that historical test does not exploit the matched-seed pairing. For v18, the already committed outcomes are therefore also subjected to a two-sided **paired sign-flip sensitivity analysis** on per-seed differences. This sensitivity analysis is post-hoc, involves no retraining or replacement of the historical result, and is reported separately rather than retroactively relabelling the original Experiment 1 analysis.'''

old_main = '''After the cooperation bonus is withdrawn, mean mutual cooperation is `0.548` in the terminal condition and `0.0367` in the restore condition across 30 paired seeds. The paired difference is approximately `0.511`, with the two-sided paired sign-flip permutation test at the 20,000-resample resolution floor (`p < 0.0001`). The auxiliary simulated-stake condition averages `0.0725`, remaining much closer to restore than terminal.'''
new_main = '''After the cooperation bonus is withdrawn, mean mutual cooperation is `0.548` in the terminal condition and `0.0367` in the restore condition across 30 matched seeds. The historical two-sided two-sample label-permutation test gives a mean difference of `0.51115` and reaches the 20,000-resample resolution floor (`p = 0.0000499975`). Because the design used matched seeds, the v18 evidence audit additionally applies the post-hoc paired sign-flip sensitivity analysis to the same fixed outcomes. It reaches the same resampling floor (`p = 0.0000499975`): 24 of 30 paired differences are positive, 2 are exactly zero, and 4 are negative. The paired analysis is a sensitivity check, not a preregistered Experiment 1 analysis and not a replacement for the historical test. The auxiliary simulated-stake condition averages `0.0725`, remaining much closer to restore than terminal.'''

old_zero = '''The zero-penalty ablation retains the main separation: post-withdrawal cooperation is approximately `0.50` under terminal failure and `0.05` under restoration (`p < 0.0001`). Thus the main result cannot be attributed solely to the manually specified depletion penalty.'''
new_zero = '''The zero-penalty ablation retains the main separation: post-withdrawal cooperation is approximately `0.50` under terminal failure and `0.05` under restoration. Its historical two-sample label-permutation p-value is again at the 20,000-resample floor (`p = 0.0000499975`). The same post-hoc paired sign-flip sensitivity analysis also gives `p = 0.0000499975`, with 25 of 30 paired differences positive. Thus the main separation cannot be attributed solely to the manually specified depletion penalty, and its statistical direction is unchanged when the matched-seed structure is used as a sensitivity analysis.'''

old_data = '''The reproduction package contains the Experiment 1 code and fixed result files, the preregistrations and first confirmatory result artifacts for Experiments 2 and 3, statistical procedures, invariant tests, and figure-generation assets. Experiment 2 and Experiment 3 preserve their first confirmatory outcomes and their preregistration provenance; no unfavorable result was replaced by a tuned rerun.'''
new_data = '''The reproduction package contains the Experiment 1 code and fixed result files, the preregistrations and first confirmatory result artifacts for Experiments 2 and 3, statistical procedures, invariant tests, and figure-generation assets. Experiment 2 and Experiment 3 preserve their first confirmatory outcomes and their preregistration provenance; no unfavorable result was replaced by a tuned rerun. The script `costly_selective_closure_supplement/audit_e1_paired_sensitivity.py` reproduces the v18 paired-sensitivity audit directly from the committed Experiment 1 and zero-penalty JSON files without retraining agents or altering the historical two-sample label-permutation results.'''

for old, new, label in [
    (old_methods, new_methods, 'E1 methods paragraph'),
    (old_main, new_main, 'main E1 paragraph'),
    (old_zero, new_zero, 'zero-penalty paragraph'),
    (old_data, new_data, 'data availability paragraph'),
]:
    n = t.count(old)
    if n != 1:
        raise SystemExit(f'expected exactly one {label}; found {n}')
    t = t.replace(old, new, 1)

p.write_text(t, encoding='utf-8')
print('PASS: E1 statistical labels corrected transparently in Methods, Results, and Data/Code Availability')
