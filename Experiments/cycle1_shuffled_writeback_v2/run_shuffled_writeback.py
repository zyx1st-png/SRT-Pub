"""One preregistered formation-time routing probe; Python standard library only.

Candidate and ordinary baseline use independently written transition code.
No copy/replacement/same-state experiment or optional seed/metric selection.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import random
from statistics import mean

HERE = Path(__file__).resolve().parent


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def candidate_step(h, x, evidence, route, alpha, rho):
    if evidence is not None:
        h = [(1 - alpha) * old + alpha * evidence[source]
             for old, source in zip(h, route)]
    x = [rho * old + (1 - rho) * hist for old, hist in zip(x, h)]
    return h, x


def ordinary_step(q, z, evidence, route, alpha, rho):
    # Ordinary prediction-error update, independently implemented in place.
    for j in range(len(q)):
        if evidence is not None:
            error = evidence[route[j]] - q[j]
            q[j] += alpha * error
        z[j] += (1 - rho) * (q[j] - z[j])
    return q, z


def score(state, signs):
    return mean((1 + s * x) / 2 for s, x in zip(signs, state))


def state_graph(n, alpha, rho, formation):
    # Edges for the simultaneous state map, excluding manipulated evidence input.
    keep = 1 - alpha if formation else 1.0
    return [(i, i, keep) for i in range(n)] + [
        (i, n + i, (1 - rho) * keep) for i in range(n)
    ] + [(n + i, n + i, rho) for i in range(n)]


def quantile(sorted_values, p):
    position = (len(sorted_values) - 1) * p
    lo = math.floor(position)
    hi = math.ceil(position)
    return sorted_values[lo] + (position - lo) * (
        sorted_values[hi] - sorted_values[lo])


def one_seed(seed, cfg):
    n, steps, probe = cfg['loci'], cfg['formation_epochs'], cfg['probe_epochs']
    alpha, rho = cfg['alpha'], cfg['rho']
    env_rng, route_rng = random.Random(seed), random.Random(100000 + seed)
    signs = [1] * (n // 2) + [-1] * (n // 2)
    env_rng.shuffle(signs)
    evidence = [[cfg['signal'] * s + env_rng.uniform(
        -cfg['noise_halfwidth'], cfg['noise_halfwidth']) for s in signs]
        for _ in range(steps)]
    shuffled = []
    for _ in range(steps):
        route = list(range(n))
        route_rng.shuffle(route)
        shuffled.append(route)
    outputs = {}
    for arm in ('O', 'D'):
        h, x, q, z = ([0.0] * n for _ in range(4))
        curves, baseline_curves = [], []
        counts = [0] * n
        max_error = 0.0
        schedule = []
        for t in range(steps + probe):
            if t == steps:
                formed_h = h.copy()
                x, z = [0.0] * n, [0.0] * n
            route = list(range(n)) if arm == 'O' or t >= steps else shuffled[t]
            tokens = evidence[t] if t < steps else None
            if tokens is not None:
                # Bijection: no dropped/duplicated evidence or fewer destination writes.
                assert sorted(route) == list(range(n))
                assert sorted(tokens[j] for j in route) == sorted(tokens)
                counts = [v + 1 for v in counts]
                schedule.append(route)
            h, x = candidate_step(h, x, tokens, route, alpha, rho)
            q, z = ordinary_step(q, z, tokens, route, alpha, rho)
            max_error = max(max_error, *(abs(a - b) for a, b in zip(h + x, q + z)))
            assert all(-1 <= v <= 1 for v in h + x)
            if t >= steps:
                u = t - steps + 1
                assert h == formed_h  # Probe contains no new history/learning evidence.
                assert max(abs(v - (1 - rho**u) * hist)
                           for v, hist in zip(x, formed_h)) < cfg['baseline_tolerance']
            curves.append(score(x, signs))
            baseline_curves.append(score(z, signs))
        assert counts == [steps] * n
        assert max_error < cfg['baseline_tolerance'], 'Implementation mismatch, not SRT effect'
        outputs[arm] = {
            'primary': mean(curves[steps:]),
            'ordinary_primary': mean(baseline_curves[steps:]),
            'max_baseline_state_error': max_error,
            'history_at_challenge': formed_h,
            'writes_per_locus': counts,
            'routing_sha256': digest(json.dumps(schedule).encode()),
            'descriptive_curve': curves,
        }
    # Conservation of aggregate EMA input, not equality of source-specific information.
    assert abs(sum(outputs['O']['history_at_challenge']) -
               sum(outputs['D']['history_at_challenge'])) < cfg['baseline_tolerance']
    return {'seed': seed, 'signs': signs,
            'evidence_sha256': digest(json.dumps(evidence).encode()), **outputs}


def run():
    cfg = json.loads((HERE / 'config.json').read_text())
    n, alpha, rho = cfg['loci'], cfg['alpha'], cfg['rho']
    assert n % 2 == 0
    # Engineering validation is performed before simulations.
    graphs = {arm: [state_graph(n, alpha, rho, formation)
                   for formation in (True, False)] for arm in ('O', 'D')}
    assert graphs['O'] == graphs['D']
    rows = [one_seed(seed, cfg) for seed in cfg['seeds']]
    differences = [r['O']['primary'] - r['D']['primary'] for r in rows]
    ordinary_differences = [r['O']['ordinary_primary'] - r['D']['ordinary_primary']
                            for r in rows]
    rng = random.Random(cfg['bootstrap_seed'])
    bootstrap = sorted(mean(rng.choices(differences, k=len(rows)))
                       for _ in range(cfg['bootstrap_resamples']))
    ci = [quantile(bootstrap, p) for p in cfg['ci_quantiles']]
    max_error = max(r[a]['max_baseline_state_error'] for r in rows for a in ('O', 'D'))
    positive = ci[0] > cfg['positive_ci_lower_bound']
    result = {
        'config': cfg,
        'config_sha256': digest((HERE / 'config.json').read_bytes()),
        'runner_sha256': digest(Path(__file__).read_bytes()),
        'engineering_topology_gate': 'PASS',
        'state_graph_sha256': digest(json.dumps(graphs['O']).encode()),
        'matching_checks': 'PASS: bijective writes, count, exposure, bounded state, probe history preservation',
        'summary': {
            'O_primary_mean': mean(r['O']['primary'] for r in rows),
            'D_primary_mean': mean(r['D']['primary'] for r in rows),
            'paired_mean_difference': mean(differences),
            'paired_bootstrap_95_ci': ci,
            'ordinary_paired_mean_difference': mean(ordinary_differences),
            'max_baseline_state_error': max_error,
            'analytic_expected_difference': .5 * cfg['signal'] * (1 - (1 - alpha)**cfg['formation_epochs'])
                * mean(1 - rho**u for u in range(1, cfg['probe_epochs'] + 1)),
            'positive_primary_rule': positive,
        },
        'verdict': 'C — GENERIC RECURRENCE RESULT' if positive else 'B — NO EFFECT',
        'SRT_distinctiveness': 'NO',
        'full_recurrence_collapse_gate': 'NOT SURVIVED: exact ordinary dynamics mapping',
        'rows': rows,
    }
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, help='Required unless --check is supplied')
    parser.add_argument('--check', type=Path, help='Recompute and compare exact stored JSON')
    args = parser.parse_args()
    if (args.output is None) == (args.check is None):
        parser.error('Use exactly one of --output or --check')
    report = run()
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + '\n'
    if args.check:
        assert json.loads(args.check.read_text()) == report, 'Reference mismatch'
        print('Reference reproduction: PASS')
    else:
        args.output.write_text(rendered)
    print(json.dumps({k: v for k, v in report.items() if k != 'rows'}, indent=2, ensure_ascii=False))
