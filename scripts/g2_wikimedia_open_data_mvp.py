#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path


PAGEVIEWS_API = (
    "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
    "{project}/{access}/{agent}/{article}/{granularity}/{start}/{end}"
)
EVENTSTREAM_URL = "https://stream.wikimedia.org/v2/stream/recentchange"
MEDIAWIKI_API = "https://{host}/w/api.php"
USER_AGENT = "SRT-G2-OpenData-MVP/0.1 (local research script)"


def normalize_title(title: str) -> str:
    return title.strip().replace(" ", "_")


def load_topic_mapping(path: Path) -> dict[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    inverse: dict[str, str] = {}
    for topic, pages in data.items():
        if not isinstance(pages, list):
            raise ValueError(f"topic {topic!r} must map to a list of page titles")
        for page in pages:
            title = normalize_title(str(page))
            if title in inverse and inverse[title] != topic:
                raise ValueError(f"page {title!r} assigned to multiple topics")
            inverse[title] = topic
    if not inverse:
        raise ValueError("topic mapping is empty")
    return inverse


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def parse_api_timestamp(raw: str, is_end: bool) -> str:
    if len(raw) == 8:
        return raw + ("23" if is_end else "00")
    if len(raw) == 10:
        return raw
    raise ValueError("timestamps must be YYYYMMDD or YYYYMMDDHH")


def pageviews_timestamp_to_iso(raw: str) -> str:
    stamp = dt.datetime.strptime(raw, "%Y%m%d%H").replace(tzinfo=dt.timezone.utc)
    return stamp.isoformat().replace("+00:00", "Z")


def floor_to_hour_iso(ts: dt.datetime) -> str:
    ts = ts.astimezone(dt.timezone.utc).replace(minute=0, second=0, microsecond=0)
    return ts.isoformat().replace("+00:00", "Z")


def floor_to_day_iso(ts: dt.datetime) -> str:
    ts = ts.astimezone(dt.timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    return ts.isoformat().replace("+00:00", "Z")


def parse_event_time(payload: dict) -> dt.datetime:
    meta = payload.get("meta") or {}
    if isinstance(meta, dict) and meta.get("dt"):
        raw = meta["dt"].replace("Z", "+00:00")
        return dt.datetime.fromisoformat(raw).astimezone(dt.timezone.utc)
    timestamp = payload.get("timestamp")
    if isinstance(timestamp, str):
        raw = timestamp.replace("Z", "+00:00")
        return dt.datetime.fromisoformat(raw).astimezone(dt.timezone.utc)
    if payload.get("timestamp") is not None:
        return dt.datetime.fromtimestamp(int(payload["timestamp"]), tz=dt.timezone.utc)
    raise ValueError("event has no usable timestamp")


def entropy(probs: list[float]) -> float:
    out = 0.0
    for p in probs:
        if p > 0:
            out -= p * math.log(p)
    return out


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def request_json(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        },
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.load(resp)


def request_json_with_params(base_url: str, params: dict[str, str]) -> dict:
    url = base_url + "?" + urllib.parse.urlencode(params)
    return request_json(url)


def cmd_fetch_pageviews(args: argparse.Namespace) -> int:
    topic_by_title = load_topic_mapping(Path(args.mapping))
    start = parse_api_timestamp(args.start, is_end=False)
    end = parse_api_timestamp(args.end, is_end=True)

    rows: list[dict] = []
    for title, topic in sorted(topic_by_title.items()):
        article = urllib.parse.quote(title, safe="")
        url = PAGEVIEWS_API.format(
            project=args.project,
            access=args.access,
            agent=args.agent,
            article=article,
            granularity=args.granularity,
            start=start,
            end=end,
        )
        payload = request_json(url)
        for item in payload.get("items", []):
            rows.append(
                {
                    "timestamp": pageviews_timestamp_to_iso(item["timestamp"]),
                    "timestamp_raw": item["timestamp"],
                    "topic": topic,
                    "page": title,
                    "project": item.get("project", args.project),
                    "views": int(item["views"]),
                }
            )
        if args.sleep_seconds:
            time.sleep(args.sleep_seconds)

    write_csv(
        Path(args.out),
        ["timestamp", "timestamp_raw", "topic", "page", "project", "views"],
        rows,
    )
    print(f"wrote {len(rows)} pageview rows to {args.out}")
    return 0


def cmd_aggregate_pageviews(args: argparse.Namespace) -> int:
    rows = read_csv_rows(Path(args.input))
    topic_views: dict[tuple[str, str], int] = defaultdict(int)
    total_views: dict[str, int] = defaultdict(int)
    for row in rows:
        key = (row["timestamp"], row["topic"])
        views = int(row["views"])
        topic_views[key] += views
        total_views[row["timestamp"]] += views

    out_rows: list[dict] = []
    for timestamp, total in sorted(total_views.items()):
        topics = sorted(topic for ts, topic in topic_views if ts == timestamp)
        for topic in topics:
            views = topic_views[(timestamp, topic)]
            rho = views / total if total else 0.0
            out_rows.append(
                {
                    "timestamp": timestamp,
                    "topic": topic,
                    "views": views,
                    "total_views": total,
                    "rho": f"{rho:.8f}",
                }
            )

    write_csv(Path(args.out), ["timestamp", "topic", "views", "total_views", "rho"], out_rows)
    print(f"wrote {len(out_rows)} rho rows to {args.out}")
    return 0


def iter_sse_payloads(url: str, seconds: int, max_events: int | None) -> list[dict]:
    deadline = time.monotonic() + seconds
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "text/event-stream",
            "User-Agent": USER_AGENT,
        },
    )
    payloads: list[dict] = []
    with urllib.request.urlopen(req, timeout=60) as resp:
        event: dict[str, str] = {}
        for raw in resp:
            if time.monotonic() >= deadline:
                break
            line = raw.decode("utf-8", errors="replace").rstrip("\n")
            if not line:
                data = event.get("data")
                if data:
                    try:
                        payloads.append(json.loads(data))
                    except json.JSONDecodeError:
                        pass
                    if max_events and len(payloads) >= max_events:
                        break
                event = {}
                continue
            if line.startswith(":"):
                continue
            field, _, value = line.partition(":")
            event[field] = value.lstrip()
    return payloads


def cmd_sample_recentchanges(args: argparse.Namespace) -> int:
    topic_by_title = load_topic_mapping(Path(args.mapping)) if args.mapping else None
    allowed_wikis = set(args.wikis.split(",")) if args.wikis else None

    payloads = iter_sse_payloads(EVENTSTREAM_URL, args.seconds, args.max_events)
    kept: list[dict] = []
    for payload in payloads:
        wiki = payload.get("wiki")
        if allowed_wikis and wiki not in allowed_wikis:
            continue
        if not args.include_bots and payload.get("bot"):
            continue
        title = normalize_title(str(payload.get("title", "")))
        if topic_by_title is not None and title not in topic_by_title:
            continue
        kept.append(payload)

    out = Path(args.out)
    ensure_parent(out)
    with out.open("w", encoding="utf-8") as fh:
        for payload in kept:
            fh.write(json.dumps(payload, ensure_ascii=False) + "\n")
    print(f"captured {len(kept)} recentchange events to {args.out}")
    return 0


def cmd_fetch_recentchanges_api(args: argparse.Namespace) -> int:
    topic_by_title = load_topic_mapping(Path(args.mapping)) if args.mapping else None
    host = args.host
    base_url = MEDIAWIKI_API.format(host=host)

    end = dt.datetime.now(dt.timezone.utc)
    start = end - dt.timedelta(minutes=args.minutes_back)
    rcstart = end.strftime("%Y-%m-%dT%H:%M:%SZ")
    rcend = start.strftime("%Y-%m-%dT%H:%M:%SZ")

    rows: list[dict] = []
    titles = sorted(topic_by_title) if topic_by_title else [None]

    for tracked_title in titles:
        params = {
            "action": "query",
            "format": "json",
            "formatversion": "2",
            "list": "recentchanges",
            "rcprop": "title|timestamp|ids|sizes|flags",
            "rctype": "edit|new",
            "rcnamespace": "0",
            "rclimit": str(args.limit),
            "rcstart": rcstart,
            "rcend": rcend,
        }
        if tracked_title is not None:
            params["rctitle"] = tracked_title

        while True:
            payload = request_json_with_params(base_url, params)
            batch = payload.get("query", {}).get("recentchanges", [])
            for item in batch:
                title = normalize_title(str(item.get("title", "")))
                if topic_by_title is not None and title not in topic_by_title:
                    continue
                rows.append(
                    {
                        "title": title,
                        "timestamp": item.get("timestamp"),
                        "revid": item.get("revid"),
                        "old_revid": item.get("old_revid"),
                        "type": item.get("type"),
                        "wiki": host,
                        "topic": topic_by_title.get(title, "") if topic_by_title else "",
                    }
                )
                if len(rows) >= args.max_rows:
                    break
            if len(rows) >= args.max_rows:
                break
            cont = payload.get("continue", {})
            if not cont:
                break
            params.update({k: str(v) for k, v in cont.items()})
        if len(rows) >= args.max_rows:
            break

    rows = rows[: args.max_rows]
    out = Path(args.out)
    ensure_parent(out)
    with out.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"captured {len(rows)} recentchanges-api events to {args.out}")
    return 0


def cmd_aggregate_recentchanges(args: argparse.Namespace) -> int:
    topic_by_title = load_topic_mapping(Path(args.mapping))
    counts: dict[tuple[str, str], int] = defaultdict(int)
    pages_per_bin: dict[tuple[str, str], set[str]] = defaultdict(set)
    totals: dict[str, int] = defaultdict(int)

    with Path(args.input).open("r", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            payload = json.loads(line)
            title = normalize_title(str(payload.get("title", "")))
            topic = topic_by_title.get(title)
            if topic is None:
                continue
            event_time = parse_event_time(payload)
            if args.bin_granularity == "daily":
                stamp = floor_to_day_iso(event_time)
            else:
                stamp = floor_to_hour_iso(event_time)
            key = (stamp, topic)
            counts[key] += 1
            pages_per_bin[key].add(title)
            totals[stamp] += 1

    out_rows: list[dict] = []
    for stamp, total in sorted(totals.items()):
        topics = sorted(topic for ts, topic in counts if ts == stamp)
        for topic in topics:
            edits = counts[(stamp, topic)]
            j_val = edits / max(args.bin_hours, 1)
            out_rows.append(
                {
                    "timestamp": stamp,
                    "topic": topic,
                    "edits": edits,
                    "unique_pages": len(pages_per_bin[(stamp, topic)]),
                    "total_edits": total,
                    "J": f"{j_val:.8f}",
                    "bin_granularity": args.bin_granularity,
                }
            )

    write_csv(
        Path(args.out),
        ["timestamp", "topic", "edits", "unique_pages", "total_edits", "J", "bin_granularity"],
        out_rows,
    )
    print(f"wrote {len(out_rows)} J rows to {args.out}")
    return 0


def cmd_build_trajectories(args: argparse.Namespace) -> int:
    rho_rows = read_csv_rows(Path(args.rho_csv))
    j_rows = read_csv_rows(Path(args.j_csv))

    rho_map: dict[str, dict[str, float]] = defaultdict(dict)
    j_map: dict[str, dict[str, float]] = defaultdict(dict)
    topics: set[str] = set()

    for row in rho_rows:
        rho_map[row["timestamp"]][row["topic"]] = float(row["rho"])
        topics.add(row["topic"])
    for row in j_rows:
        j_map[row["timestamp"]][row["topic"]] = float(row["J"])
        topics.add(row["topic"])

    timestamps = sorted(set(rho_map) & set(j_map))
    topics_sorted = sorted(topics)
    window = args.window_hours
    trajectories: list[dict] = []

    for start_idx in range(0, max(len(timestamps) - window + 1, 0), window):
        window_stamps = timestamps[start_idx : start_idx + window]
        if len(window_stamps) < window:
            continue

        rho_start = {topic: rho_map[window_stamps[0]].get(topic, 0.0) for topic in topics_sorted}
        rho_end = {topic: rho_map[window_stamps[-1]].get(topic, 0.0) for topic in topics_sorted}
        j_total = {
            topic: sum(j_map[stamp].get(topic, 0.0) for stamp in window_stamps)
            for topic in topics_sorted
        }
        start_topic = max(rho_start, key=rho_start.get)
        end_topic = max(rho_end, key=rho_end.get)
        flow_topic = max(j_total, key=j_total.get)

        h_start = entropy(list(rho_start.values()))
        h_end = entropy(list(rho_end.values()))
        delta_h = h_end - h_start
        if delta_h > args.entropy_eps:
            h_label = "entropy_up"
        elif delta_h < -args.entropy_eps:
            h_label = "entropy_down"
        else:
            h_label = "entropy_flat"

        path_label = f"{start_topic}->{end_topic}|{h_label}|flow:{flow_topic}"
        trajectories.append(
            {
                "window_start": window_stamps[0],
                "window_end": window_stamps[-1],
                "path_label": path_label,
                "dominant_topic_start": start_topic,
                "dominant_topic_end": end_topic,
                "peak_flow_topic": flow_topic,
                "entropy_start": round(h_start, 6),
                "entropy_end": round(h_end, 6),
                "entropy_delta": round(delta_h, 6),
                "rho_start": rho_start,
                "rho_end": rho_end,
                "j_total": j_total,
            }
        )

    out = Path(args.out)
    ensure_parent(out)
    out.write_text(json.dumps(trajectories, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {len(trajectories)} trajectories to {args.out}")
    return 0


def cmd_summarize_paths(args: argparse.Namespace) -> int:
    trajectories = json.loads(Path(args.input).read_text(encoding="utf-8"))
    counter = Counter(item["path_label"] for item in trajectories)
    total = sum(counter.values()) or 1
    out_rows = [
        {
            "path_label": label,
            "count": count,
            "frequency": f"{count / total:.8f}",
        }
        for label, count in counter.most_common()
    ]
    write_csv(Path(args.out), ["path_label", "count", "frequency"], out_rows)
    print(f"wrote {len(out_rows)} path classes to {args.out}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Minimal Wikimedia open-data pipeline for SRT G2-2 coarse-grained rho/J/path observables."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    fetch = subparsers.add_parser("fetch-pageviews", help="Fetch raw pageviews for mapped pages.")
    fetch.add_argument("--mapping", required=True, help="JSON file mapping topics to page titles.")
    fetch.add_argument("--start", required=True, help="YYYYMMDD or YYYYMMDDHH")
    fetch.add_argument("--end", required=True, help="YYYYMMDD or YYYYMMDDHH")
    fetch.add_argument("--project", default="en.wikipedia.org")
    fetch.add_argument("--access", default="all-access")
    fetch.add_argument("--agent", default="all-agents")
    fetch.add_argument("--granularity", default="daily", choices=["daily", "monthly"])
    fetch.add_argument("--sleep-seconds", type=float, default=0.0)
    fetch.add_argument("--out", required=True)
    fetch.set_defaults(func=cmd_fetch_pageviews)

    agg_views = subparsers.add_parser("aggregate-pageviews", help="Aggregate raw pageviews into rho_k(t).")
    agg_views.add_argument("--input", required=True)
    agg_views.add_argument("--out", required=True)
    agg_views.set_defaults(func=cmd_aggregate_pageviews)

    sample = subparsers.add_parser("sample-recentchanges", help="Sample live recentchange events to NDJSON.")
    sample.add_argument("--seconds", type=int, default=300)
    sample.add_argument("--max-events", type=int, default=None)
    sample.add_argument("--mapping", help="Optional JSON topic mapping to keep only tracked pages.")
    sample.add_argument("--wikis", help="Comma-separated wiki ids, e.g. enwiki,zhwiki")
    sample.add_argument("--include-bots", action="store_true")
    sample.add_argument("--out", required=True)
    sample.set_defaults(func=cmd_sample_recentchanges)

    recent_api = subparsers.add_parser(
        "fetch-recentchanges-api",
        help="Fetch recent changes from the MediaWiki Action API as NDJSON.",
    )
    recent_api.add_argument("--mapping", help="Optional JSON topic mapping to keep only tracked pages.")
    recent_api.add_argument("--host", default="en.wikipedia.org")
    recent_api.add_argument("--minutes-back", type=int, default=1440)
    recent_api.add_argument("--limit", type=int, default=500)
    recent_api.add_argument("--max-rows", type=int, default=5000)
    recent_api.add_argument("--out", required=True)
    recent_api.set_defaults(func=cmd_fetch_recentchanges_api)

    agg_changes = subparsers.add_parser("aggregate-recentchanges", help="Aggregate raw recentchange NDJSON into J_k(t).")
    agg_changes.add_argument("--input", required=True)
    agg_changes.add_argument("--mapping", required=True)
    agg_changes.add_argument("--bin-hours", type=int, default=1)
    agg_changes.add_argument("--bin-granularity", default="hourly", choices=["hourly", "daily"])
    agg_changes.add_argument("--out", required=True)
    agg_changes.set_defaults(func=cmd_aggregate_recentchanges)

    build = subparsers.add_parser("build-trajectories", help="Fuse rho/J hourly series into windowed path objects.")
    build.add_argument("--rho-csv", required=True)
    build.add_argument("--j-csv", required=True)
    build.add_argument("--window-hours", type=int, default=24)
    build.add_argument("--entropy-eps", type=float, default=0.02)
    build.add_argument("--out", required=True)
    build.set_defaults(func=cmd_build_trajectories)

    summary = subparsers.add_parser("summarize-paths", help="Count path labels and estimate path frequencies.")
    summary.add_argument("--input", required=True)
    summary.add_argument("--out", required=True)
    summary.set_defaults(func=cmd_summarize_paths)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("aborted by user", file=sys.stderr)
        return 130
    except Exception as exc:  # pragma: no cover - CLI error path
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
