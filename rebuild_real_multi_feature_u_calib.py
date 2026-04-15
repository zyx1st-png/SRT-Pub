from pathlib import Path
import csv
import math
from collections import defaultdict

SESSION_IDS = [715093703, 719161530, 721123822, 732592105, 737581020]
UNITS_PER_SESSION = 5
DT = 0.05
MAX_T = 600.0

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "unified_srt_mtor_real_multi_featureu_calib.csv"
MANIFEST = ROOT / "data" / "raw" / "allen" / "ecephys_cache" / "manifest.json"


def bin_spikes(spike_times, T, dt):
    n = int(T / dt)
    counts = [0] * n
    for t in spike_times:
        if 0 <= t < T:
            i = int(t // dt)
            if 0 <= i < n:
                counts[i] += 1
    return counts


def safe_float(x, default=0.0):
    try:
        return float(x)
    except Exception:
        return default


def build_bin_meta(stim_table, T, dt):
    n = int(T / dt)
    cond = ["0"] * n
    stim_name = ["unknown"] * n
    ori = [0.0] * n
    sf = [0.0] * n
    tf = [0.0] * n
    ctr = [0.0] * n

    cols = ["start_time", "stop_time", "stimulus_condition_id", "stimulus_name", "orientation", "spatial_frequency", "temporal_frequency", "contrast"]
    st = stim_table[cols].sort_values("start_time")
    rows = list(st.itertuples(index=False, name=None))

    j = 0
    for i in range(n):
        t = i * dt
        while j < len(rows) and rows[j][1] <= t:
            j += 1
        if j < len(rows) and rows[j][0] <= t < rows[j][1]:
            cond[i] = str(int(rows[j][2])) if rows[j][2] is not None else "0"
            stim_name[i] = str(rows[j][3])
            ori[i] = safe_float(rows[j][4], 0.0)
            sf[i] = safe_float(rows[j][5], 0.0)
            tf[i] = safe_float(rows[j][6], 0.0)
            ctr[i] = safe_float(rows[j][7], 0.0)

    return cond, stim_name, ori, sf, tf, ctr


def bin_feat(x, step):
    return f"{round(x/step)*step:.2f}"


def zscore_from_stats(v, m, s):
    return (v - m) / s if s > 1e-12 else 0.0


def main():
    from allensdk.brain_observatory.ecephys.ecephys_project_cache import EcephysProjectCache

    cache = EcephysProjectCache.from_warehouse(manifest=str(MANIFEST))

    # pass1: collect TRAIN-session global means by feature bin across all units
    # train sessions are first 3 ids (session-level split)
    train_session_set = set(SESSION_IDS[: int(0.6 * len(SESSION_IDS))])

    by_cond = defaultdict(list)
    by_ori = defaultdict(list)
    by_sf = defaultdict(list)
    by_tf = defaultdict(list)
    by_ctr = defaultdict(list)

    session_cache = {}

    for sid in SESSION_IDS:
        session = cache.get_session_data(sid)
        units = list(session.units.index[:UNITS_PER_SESSION])
        T = min(MAX_T, float(session.get_stimulus_table().stop_time.max()))
        n = int(T / DT)
        cond, sname, ori, sf, tf, ctr = build_bin_meta(session.get_stimulus_table(), T, DT)
        session_cache[sid] = (session, units, T, n, cond, sname, ori, sf, tf, ctr)

        if sid not in train_session_set:
            continue

        cutoff = int(0.7 * n)
        for unit_id in units:
            counts = bin_spikes(session.spike_times[unit_id], T, DT)
            for i in range(cutoff):
                y = counts[i]
                by_cond[cond[i]].append(y)
                by_ori[bin_feat(ori[i], 15.0)].append(y)
                by_sf[bin_feat(sf[i], 0.02)].append(y)
                by_tf[bin_feat(tf[i], 1.0)].append(y)
                by_ctr[bin_feat(ctr[i], 0.1)].append(y)

    def stats_map(tab):
        out = {}
        for k, v in tab.items():
            if not v:
                continue
            m = sum(v) / len(v)
            var = sum((x - m) ** 2 for x in v) / max(1, len(v) - 1)
            s = math.sqrt(var)
            out[k] = (m, s if s > 1e-12 else 1.0)
        return out

    st_cond = stats_map(by_cond)
    st_ori = stats_map(by_ori)
    st_sf = stats_map(by_sf)
    st_tf = stats_map(by_tf)
    st_ctr = stats_map(by_ctr)

    fields = [
        "dataset_id","subject_id","session_id","circuit_id","t_sec","dt_sec",
        "spike_count","x_mtor_proxy","u_observer","condition","split"
    ]

    rows_out = []

    for sidx, sid in enumerate(SESSION_IDS):
        session, units, T, n, cond, sname, ori, sf, tf, ctr = session_cache[sid]

        for unit_id in units:
            counts = bin_spikes(session.spike_times[unit_id], T, DT)
            for i, y in enumerate(counts):
                t = i * DT
                key_ori = bin_feat(ori[i], 15.0)
                key_sf = bin_feat(sf[i], 0.02)
                key_tf = bin_feat(tf[i], 1.0)
                key_ctr = bin_feat(ctr[i], 0.1)

                m, s = st_cond.get(cond[i], (0.0, 1.0)); zc = zscore_from_stats(y, m, s)
                m, s = st_ori.get(key_ori, (0.0, 1.0)); zo = zscore_from_stats(y, m, s)
                m, s = st_sf.get(key_sf, (0.0, 1.0)); zs = zscore_from_stats(y, m, s)
                m, s = st_tf.get(key_tf, (0.0, 1.0)); zt = zscore_from_stats(y, m, s)
                m, s = st_ctr.get(key_ctr, (0.0, 1.0)); zr = zscore_from_stats(y, m, s)

                u = 0.45 * zc + 0.20 * zo + 0.15 * zs + 0.10 * zt + 0.10 * zr

                cond_key = f"cid:{cond[i]}|ori:{key_ori}|sf:{key_sf}|tf:{key_tf}|ct:{key_ctr}"

                if sidx < int(0.6 * len(SESSION_IDS)):
                    split = "train"
                elif sidx < int(0.8 * len(SESSION_IDS)):
                    split = "valid"
                else:
                    split = "test"

                rows_out.append({
                    "dataset_id": f"allen_vcnp_real_multi|{sname[i]}",
                    "subject_id": str(session.specimen_name),
                    "session_id": str(sid),
                    "circuit_id": str(unit_id),
                    "t_sec": round(t, 4),
                    "dt_sec": DT,
                    "spike_count": int(y),
                    "x_mtor_proxy": "",
                    "u_observer": round(float(u), 6),
                    "condition": cond_key,
                    "split": split,
                })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows_out)

    print(f"wrote {OUT}")
    print(f"rows={len(rows_out)}")


if __name__ == "__main__":
    main()
