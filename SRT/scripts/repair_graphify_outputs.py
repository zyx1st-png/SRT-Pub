from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from graphify.analyze import god_nodes
from graphify.build import build_from_json


def safe_base(title: str) -> str:
    return (
        title.replace("/", "-")
        .replace(" ", "_")
        .replace(":", "-")
        .replace("|", "-")
        .replace("\\", "-")
    )


def allocate_filenames(titles: list[str]) -> dict[str, str]:
    used: Counter[str] = Counter()
    mapping: dict[str, str] = {}
    for title in sorted(set(titles)):
        base = safe_base(title) or "untitled"
        used[base] += 1
        suffix = "" if used[base] == 1 else f"__{used[base]}"
        mapping[title] = f"{base}{suffix}"
    return mapping


def md_link(title: str, mapping: dict[str, str]) -> str:
    target = f"{mapping[title]}.md"
    return f"[{title}](<{target}>)"


def community_article(
    graph,
    cid: int,
    node_ids: list[str],
    label: str,
    community_labels: dict[int, str],
    title_map: dict[str, str],
) -> str:
    source_files = sorted({graph.nodes[n].get("source_file", "") for n in node_ids} - {""})
    label_counts: Counter[str] = Counter()
    confidence: Counter[str] = Counter()
    cross_links: Counter[str] = Counter()

    for nid in node_ids:
        for neighbor in graph.neighbors(nid):
            edge = graph.edges[nid, neighbor]
            confidence[edge.get("confidence", "EXTRACTED")] += 1
            neighbor_label = graph.nodes[neighbor].get("label", neighbor)
            label_counts[neighbor_label] += 1
            neighbor_cid = graph.nodes[neighbor].get("community")
            if neighbor_cid is not None and neighbor_cid != cid:
                cross_links[community_labels.get(neighbor_cid, f"Community {neighbor_cid}")] += 1

    top_concepts = []
    for nid in sorted(node_ids, key=lambda n: graph.degree(n), reverse=True):
        node_label = graph.nodes[nid].get("label", nid)
        if node_label == label or node_label in top_concepts:
            continue
        top_concepts.append(node_label)
        if len(top_concepts) == 20:
            break

    lines = [
        f"# {label}",
        "",
        f"> Community page · {len(node_ids)} nodes · {len(source_files)} source files",
        "",
        "## Key Concepts",
        "",
    ]

    if top_concepts:
        for concept in top_concepts:
            lines.append(f"- {md_link(concept, title_map)}")
    else:
        lines.append("- No standout concept labels found")

    lines += ["", "## Cross-Community Links", ""]
    if cross_links:
        for other, count in cross_links.most_common(12):
            lines.append(f"- {md_link(other, title_map)} ({count} shared connections)")
    else:
        lines.append("- No strong cross-community links detected")

    if source_files:
        lines += ["", "## Source Files", ""]
        for src in source_files[:30]:
            lines.append(f"- `{src}`")

    total_edges = sum(confidence.values()) or 1
    lines += ["", "## Audit Trail", ""]
    for level in ("EXTRACTED", "INFERRED", "AMBIGUOUS"):
        count = confidence.get(level, 0)
        pct = round(count / total_edges * 100)
        lines.append(f"- {level}: {count} ({pct}%)")

    lines += ["", "---", "", f"*Part of the repaired graphify wiki. Start at [index](index.md).*"]
    return "\n".join(lines) + "\n"


def label_article(
    graph,
    label: str,
    node_ids: list[str],
    community_labels: dict[int, str],
    title_map: dict[str, str],
) -> str:
    source_files = sorted({graph.nodes[n].get("source_file", "") for n in node_ids} - {""})
    communities = []
    seen_communities = set()
    related: dict[str, Counter[str]] = defaultdict(Counter)
    confidence: Counter[str] = Counter()

    for nid in node_ids:
        cid = graph.nodes[nid].get("community")
        if cid is not None:
            community_label = community_labels.get(cid, f"Community {cid}")
            if community_label not in seen_communities:
                seen_communities.add(community_label)
                communities.append(community_label)

        for neighbor in graph.neighbors(nid):
            edge = graph.edges[nid, neighbor]
            neighbor_label = graph.nodes[neighbor].get("label", neighbor)
            if neighbor_label == label:
                continue
            related[edge.get("relation", "related_to")][neighbor_label] += 1
            confidence[edge.get("confidence", "EXTRACTED")] += 1

    lines = [
        f"# {label}",
        "",
        f"> Concept page · {len(node_ids)} graph node(s) · {sum(graph.degree(n) for n in node_ids)} total connections",
        "",
    ]

    if communities:
        lines += ["## Communities", ""]
        for community_label in communities:
            lines.append(f"- {md_link(community_label, title_map)}")
        lines.append("")

    if source_files:
        lines += ["## Source Files", ""]
        for src in source_files[:20]:
            lines.append(f"- `{src}`")
        lines.append("")

    lines += ["## Connections by Relation", ""]
    if related:
        for relation in sorted(related):
            lines.append(f"### {relation}")
            for neighbor_label, count in related[relation].most_common(20):
                lines.append(f"- {md_link(neighbor_label, title_map)} ({count})")
            lines.append("")
    else:
        lines.append("- No outgoing connections captured")
        lines.append("")

    total_edges = sum(confidence.values()) or 1
    lines += ["## Audit Trail", ""]
    for level in ("EXTRACTED", "INFERRED", "AMBIGUOUS"):
        count = confidence.get(level, 0)
        pct = round(count / total_edges * 100)
        lines.append(f"- {level}: {count} ({pct}%)")

    lines += ["", "---", "", f"*Part of the repaired graphify wiki. Start at [index](index.md).*"]
    return "\n".join(lines) + "\n"


def write_index(
    wiki_dir: Path,
    communities: dict[int, list[str]],
    community_labels: dict[int, str],
    graph,
    title_map: dict[str, str],
) -> None:
    gods = god_nodes(graph, top_n=10)
    lines = [
        "# Knowledge Graph Index",
        "",
        "> Repaired graphify wiki with working Markdown links.",
        "",
        f"**{graph.number_of_nodes()} nodes · {graph.number_of_edges()} edges · {len(communities)} communities**",
        "",
        "- [Graph Report](../GRAPH_REPORT.md)",
        "- [Interactive Graph](../graph.html)",
        "- [Raw Graph JSON](../graph.json)",
        "",
        "---",
        "",
        "## Communities",
        "",
    ]

    for cid, node_ids in sorted(communities.items(), key=lambda item: -len(item[1])):
        label = community_labels.get(cid, f"Community {cid}")
        lines.append(f"- {md_link(label, title_map)} — {len(node_ids)} nodes")

    lines += ["", "## God Nodes", ""]
    for node in gods:
        lines.append(f"- {md_link(node['label'], title_map)} — {node['edges']} connections")

    lines += ["", "---", "", "*Generated from the current graphify outputs.*", ""]
    (wiki_dir / "index.md").write_text("\n".join(lines))


def update_report(
    report_path: Path,
    communities: dict[int, list[str]],
    community_labels: dict[int, str],
    title_map: dict[str, str],
) -> None:
    if not report_path.exists():
        return

    text = report_path.read_text()
    start = text.find("## Community Hubs (Navigation)")
    end = text.find("\n## God Nodes", start)
    if start == -1 or end == -1:
        return

    lines = [
        "## Community Hubs (Navigation)",
        "- [Wiki Index](wiki/index.md)",
    ]
    for cid, node_ids in sorted(communities.items(), key=lambda item: -len(item[1])):
        label = community_labels.get(cid, f"Community {cid}")
        lines.append(f"- [{label}](<wiki/{title_map[label]}.md>) — {len(node_ids)} nodes")

    replacement = "\n".join(lines)
    report_path.write_text(text[:start] + replacement + text[end:])


def main() -> None:
    root = Path(".")
    out_dir = root / "graphify-out"
    wiki_dir = out_dir / "wiki"
    legacy_dir = out_dir / "wiki_legacy"
    graph_path = out_dir / "graph.json"
    report_path = out_dir / "GRAPH_REPORT.md"
    labels_path = out_dir / "community_labels.json"
    manifest_path = wiki_dir / "_manifest.json"
    existing_md = {p.name: p for p in wiki_dir.glob("*.md")} if wiki_dir.exists() else {}

    graph_data = json.loads(graph_path.read_text())
    graph = build_from_json(graph_data)
    graph.graph["hyperedges"] = graph_data.get("hyperedges", [])

    communities: dict[int, list[str]] = defaultdict(list)
    label_nodes: dict[str, list[str]] = defaultdict(list)
    for node in graph_data["nodes"]:
        cid = node.get("community")
        if cid is not None:
            communities[int(cid)].append(node["id"])
        label_nodes[node.get("label", node["id"])].append(node["id"])

    labels_raw = json.loads(labels_path.read_text()) if labels_path.exists() else {}
    community_labels = {int(k): v for k, v in labels_raw.items()}
    for cid in communities:
        community_labels.setdefault(cid, f"Community {cid}")

    all_titles = list(label_nodes) + list(community_labels.values())
    title_map = allocate_filenames(all_titles)

    wiki_dir.mkdir(parents=True, exist_ok=True)
    written_files = {"index.md"}

    for cid, node_ids in communities.items():
        title = community_labels[cid]
        content = community_article(graph, cid, node_ids, title, community_labels, title_map)
        filename = f"{title_map[title]}.md"
        (wiki_dir / filename).write_text(content)
        written_files.add(filename)

    for title, node_ids in label_nodes.items():
        content = label_article(graph, title, node_ids, community_labels, title_map)
        filename = f"{title_map[title]}.md"
        (wiki_dir / filename).write_text(content)
        written_files.add(filename)

    write_index(wiki_dir, communities, community_labels, graph, title_map)
    update_report(report_path, communities, community_labels, title_map)

    manifest = {
        "community_pages": {label: f"{title_map[label]}.md" for label in community_labels.values()},
        "label_pages": {label: f"{title_map[label]}.md" for label in label_nodes},
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))

    stale_files = [name for name in existing_md if name not in written_files]
    if stale_files:
        legacy_dir.mkdir(parents=True, exist_ok=True)
        for name in stale_files:
            existing_md[name].rename(legacy_dir / name)

    print(
        json.dumps(
            {
                "community_pages": len(community_labels),
                "label_pages": len(label_nodes),
                "stale_files_moved": len(stale_files),
                "index": str(wiki_dir / "index.md"),
                "report": str(report_path),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
