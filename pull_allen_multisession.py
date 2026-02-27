from pathlib import Path
import csv
import argparse
from collections import defaultdict
import math


def bin_spikes(spike_times, T, dt):
    n = int(T / dt)
    counts = [0] * n
    for t in spike_times:
        if 0 <= t < T:
            i = int(t // dt)
            if 0 <= i < n:
                counts[i] += 1
    return counts


def zscore_map(d):
    vals = list(d.values())
    if not vals:
        return {k: 0.0 for k in d}
    m = sum(vals) / len(vals)
    v = sum((x - m) ** 2 for x in vals) / max(1, len(vals) - 1)
    s = math.sqrt(v) if v > 1e-12 else 1.0
    return {k: (x - m) / s for k, x in d.items()}


def build_bin_stimulus(stim_table, T, dt):
    n = int(T / dt)
    stim = ["unknown"] * n
    st = stim_table[["start_time", "stop_time", "stimulus_name"]].sort_values("start_time")
    rows = list(st.itertuples(index=False, name=None))

    j = 0
    for i in range(n):
        t = i * dt
        while j < len(rows) and rows[j][1] <= t:
            j += 1
        if j < len(rows) and rows[j][0] <= t < rows[j][1]:
            stim[i] = str(rows[j][2])
        else:
            stim[i] = "unknown"
    return stim


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n-sessions", type=int, default=5)
    p.add_argument("--units-per-session", type=int, default=5)
    p.add_argument("--max-seconds", type=float, default=600.0)
    p.add_argument("--dt", type=float, default=0.05)
    p.add_argument("--out", type=str, default="data/unified_srt_mtor_real_multi.csv")
    args = p.parse_args()

    from allensdk.brain_observatory.ecephys.ecephys_project_cache import EcephysProjectCache

    root = Path(__file__).resolve().parent
    cache_dir = root / "data" / "raw" / "allen" / "ecephys_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    manifest = cache_dir / "manifest.json"

    cache = EcephysProjectCache.from_warehouse(manifest=str(manifest))
    sessions = cache.get_session_table()

    session_ids = [int(x) for x in sessions.index[: args.n_sessions]]
    print(f"selected sessions: {session_ids}")

    all_rows = []

    for sidx, sid in enumerate(session_ids):
        print(f"loading session {sid} ...")
        session = cache.get_session_data(sid)
        units = list(session.units.index[: args.units_per_session])
        T = min(args.max_seconds, float(session.get_stimulus_table().stop_time.max()))
        n = int(T / args.dt)
        stim_by_bin = build_bin_stimulus(session.get_stimulus_table(), T, args.dt)

        for unit_id in units:
            counts = bin_spikes(session.spike_times[unit_id], T, args.dt)

            cutoff_train = int(0.70 * n)
            agg = defaultdict(list)
            for i in range(cutoff_train):
                agg[stim_by_bin[i]].append(counts[i])
            mean_by_stim = {k: (sum(v) / len(v)) for k, v in agg.items() if len(v) > 0}
            uz_map = zscore_map(mean_by_stim)

            for i, c in enumerate(counts):
                t = i * args.dt
                stim = stim_by_bin[i]
                u = uz_map.get(stim, 0.0)

                # session-level split to reduce leakage
                if sidx < int(0.6 * len(session_ids)):
                    split = "train"
                elif sidx < int(0.8 * len(session_ids)):
                    split = "valid"
                else:
                    split = "test"

                all_rows.append({
                    "dataset_id": "allen_vcnp_real_multi",
                    "subject_id": str(session.specimen_name),
                    "session_id": str(sid),
                    "circuit_id": str(unit_id),
                    "t_sec": round(t, 4),
                    "dt_sec": args.dt,
                    "spike_count": int(c),
                    "x_mtor_proxy": "",
                    "u_observer": round(float(u), 6),
                    "condition": stim,
                    "split": split,
                })

        print(f"session {sid} done; cumulative rows={len(all_rows)}")

    out = root / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "dataset_id","subject_id","session_id","circuit_id","t_sec","dt_sec",
        "spike_count","x_mtor_proxy","u_observer","condition","split"
    ]
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(all_rows)

    print(f"wrote {out}")
    print(f"total rows={len(all_rows)}")


if __name__ == "__main__":
    main()
