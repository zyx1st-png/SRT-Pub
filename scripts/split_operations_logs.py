#!/usr/bin/env python3
"""Split oversized Operations logs into connector-safe dated parts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
import re


ROOT = Path(__file__).resolve().parents[1]
OPERATIONS = ROOT / "Operations"

MATERIAL_LOG = OPERATIONS / "_SRT_MATERIAL_LOG.md"
MATERIAL_DIR = OPERATIONS / "Material_Log"

STATUS_HISTORY = OPERATIONS / "_SRT_STATUS_HISTORY.md"
STATUS_DIR = OPERATIONS / "Status_History"

MAX_PART_BYTES = 45_000

DATE_RE = re.compile(r"2026-\d{2}-\d{2}")


@dataclass
class PartFile:
    filename: str
    title: str
    count: int
    body_hash: str


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("frontmatter missing")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("frontmatter terminator missing")
    return text[: end + len("\n---\n")], text[end + len("\n---\n") :].lstrip("\n")


def chunk_items(items: list[str], prefix: str, max_bytes: int = MAX_PART_BYTES) -> list[tuple[str, list[str]]]:
    chunks: list[tuple[str, list[str]]] = []
    current: list[str] = []
    current_size = 0
    index = 1
    for item in items:
        item_size = len((item + "\n").encode("utf-8"))
        if current and current_size + item_size > max_bytes:
            chunks.append((f"{prefix}_Part{index:02d}.md", current))
            index += 1
            current = []
            current_size = 0
        current.append(item)
        current_size += item_size
    if current:
        chunks.append((f"{prefix}_Part{index:02d}.md", current))
    return chunks


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def split_material_log() -> list[PartFile]:
    text = MATERIAL_LOG.read_text(encoding="utf-8")
    if "role: split_master_index" in text:
        print("material log already split; skipping")
        return []

    frontmatter, body = split_frontmatter(text)
    start = body.index("## 台账记录")
    obs_marker = "\n---\n\n## 延后观察列表"
    obs_start = body.index(obs_marker)
    before_records = body[:start].rstrip()
    records_section = body[start:obs_start]
    after_records = body[obs_start:].lstrip("\n")

    lines = records_section.splitlines()
    preamble: list[str] = []
    rows: list[str] = []
    for line in lines:
        if line.startswith("| 2026-"):
            rows.append(line)
        else:
            preamble.append(line)

    groups: dict[str, list[str]] = {}
    for row in rows:
        match = DATE_RE.search(row)
        key = match.group(0)[:7] if match else "undated"
        groups.setdefault(key, []).append(row)

    parts: list[PartFile] = []
    table_header = [
        "| 日期 | 来源标题 / URL | 类型 | 审核结论 | 落点（文件 + 节位） | 融入状态 | 备注 |",
        "|-----|--------------|------|---------|-----------------|---------|------|",
    ]
    all_rows_text = "\n".join(rows) + "\n"

    for month in sorted(groups):
        chunks = chunk_items(groups[month], month)
        for filename, chunk_rows in chunks:
            part_title = f"Material Log {filename.removesuffix('.md')}"
            body_text = "\n".join(table_header + chunk_rows) + "\n"
            part_text = (
                "---\n"
                f"id: SRT-MATERIAL-LOG-{filename.removesuffix('.md').upper().replace('_', '-')}\n"
                "type: material_log_part\n"
                "status: active_v1\n"
                "layer: operations\n"
                "epistemic_layer: os\n"
                "claim_mode: evidence\n"
                "canonical: false\n"
                "source_log: Operations/_SRT_MATERIAL_LOG.md\n"
                "---\n\n"
                f"# {part_title}\n\n"
                f"> Split from `../_SRT_MATERIAL_LOG.md`; Pipeline 1 official state still routes through the root index and this dated part.\n\n"
                + body_text
            )
            write(MATERIAL_DIR / filename, part_text)
            parts.append(
                PartFile(
                    filename=filename,
                    title=part_title,
                    count=len(chunk_rows),
                    body_hash=sha(body_text),
                )
            )

    readme = [
        "---",
        "id: SRT-MATERIAL-LOG-SPLIT-INDEX",
        "type: operations_log_index",
        "status: active_v1",
        "layer: operations",
        "epistemic_layer: os",
        "claim_mode: evidence",
        "canonical: false",
        "---",
        "",
        "# Material Log Split Index",
        "",
        "> Purpose: keep Pipeline 1 material records connector-safe while preserving the root log as the official routing surface.",
        "",
        f"- Split source row SHA-256: `{sha(all_rows_text)}`",
        f"- Record rows: `{len(rows)}`",
        "",
        "| File | Rows | SHA-256 |",
        "|---|---:|---|",
    ]
    for part in parts:
        readme.append(f"| [{part.filename}]({part.filename}) | {part.count} | `{part.body_hash}` |")
    readme.append("")
    write(MATERIAL_DIR / "README.md", "\n".join(readme))

    root_lines = [
        frontmatter.replace("status: active_v1", "status: active_v1\nrole: split_master_index").rstrip(),
        "",
        before_records,
        "",
        "## 台账记录",
        "",
        "> Actual Pipeline 1 material records have been split into dated connector-safe files.",
        "> New material records should be appended to the current dated part, then this index should be updated if a new part is created.",
        "",
        "| Month / Part | File | Rows |",
        "|---|---|---:|",
    ]
    for part in parts:
        label = part.filename.removesuffix(".md")
        root_lines.append(f"| {label} | [Material_Log/{part.filename}](Material_Log/{part.filename}) | {part.count} |")
    root_lines.extend(["", after_records])
    write(MATERIAL_LOG, "\n".join(root_lines).rstrip() + "\n")
    return parts


def split_status_history() -> list[PartFile]:
    text = STATUS_HISTORY.read_text(encoding="utf-8")
    if "role: split_master_index" in text:
        print("status history already split; skipping")
        return []

    frontmatter, body = split_frontmatter(text)
    title = "# SRT 状态历史归档"
    title_idx = body.index(title)
    after_title = body[title_idx + len(title) :].lstrip("\n")

    markers: list[int] = []
    for match in re.finditer(r"(?m)^> \*\*", after_title):
        markers.append(match.start())
    for match in re.finditer(r"(?m)^---\n\n## ", after_title):
        markers.append(match.start())
    markers = sorted(set(markers))
    if not markers:
        raise ValueError("no status history block markers found")

    intro = after_title[: markers[0]].rstrip()
    blocks: list[str] = []
    for i, start in enumerate(markers):
        end = markers[i + 1] if i + 1 < len(markers) else len(after_title)
        blocks.append(after_title[start:end].strip())

    groups: dict[str, list[str]] = {}
    for block in blocks:
        match = DATE_RE.search(block)
        key = match.group(0)[:7] if match else "undated"
        groups.setdefault(key, []).append(block)

    parts: list[PartFile] = []
    all_blocks_text = "\n\n".join(blocks) + "\n"

    for month in sorted(groups):
        chunks = chunk_items(groups[month], month)
        for filename, chunk_blocks in chunks:
            part_title = f"Status History {filename.removesuffix('.md')}"
            body_text = "\n\n".join(chunk_blocks) + "\n"
            part_text = (
                "---\n"
                f"id: SRT-STATUS-HISTORY-{filename.removesuffix('.md').upper().replace('_', '-')}\n"
                "type: status_history_part\n"
                "status: active_v1\n"
                "layer: operations\n"
                "epistemic_layer: os\n"
                "claim_mode: evidence\n"
                "canonical: false\n"
                "source_log: Operations/_SRT_STATUS_HISTORY.md\n"
                "---\n\n"
                f"# {part_title}\n\n"
                f"> Split from `../_SRT_STATUS_HISTORY.md`; current status remains in `../STATUS.md`.\n\n"
                + body_text
            )
            write(STATUS_DIR / filename, part_text)
            parts.append(
                PartFile(
                    filename=filename,
                    title=part_title,
                    count=len(chunk_blocks),
                    body_hash=sha(body_text),
                )
            )

    readme = [
        "---",
        "id: SRT-STATUS-HISTORY-SPLIT-INDEX",
        "type: operations_log_index",
        "status: active_v1",
        "layer: operations",
        "epistemic_layer: os",
        "claim_mode: evidence",
        "canonical: false",
        "---",
        "",
        "# Status History Split Index",
        "",
        "> Purpose: keep historical status records connector-safe while preserving `../_SRT_STATUS_HISTORY.md` as the routing surface.",
        "",
        f"- Split source block SHA-256: `{sha(all_blocks_text)}`",
        f"- Blocks: `{len(blocks)}`",
        "",
        "| File | Blocks | SHA-256 |",
        "|---|---:|---|",
    ]
    for part in parts:
        readme.append(f"| [{part.filename}]({part.filename}) | {part.count} | `{part.body_hash}` |")
    readme.append("")
    write(STATUS_DIR / "README.md", "\n".join(readme))

    root_lines = [
        frontmatter.replace("status: active_v1", "status: active_v1\nrole: split_master_index").rstrip(),
        "",
        title,
        "",
        intro,
        "",
        "## Split History Parts",
        "",
        "> Historical status records have been split into connector-safe dated parts.",
        "> Current status remains in `../STATUS.md`.",
        "",
        "| Month / Part | File | Blocks |",
        "|---|---|---:|",
    ]
    for part in parts:
        label = part.filename.removesuffix(".md")
        root_lines.append(f"| {label} | [Status_History/{part.filename}](Status_History/{part.filename}) | {part.count} |")
    root_lines.append("")
    write(STATUS_HISTORY, "\n".join(root_lines).rstrip() + "\n")
    return parts


def main() -> None:
    material_parts = split_material_log()
    status_parts = split_status_history()
    print(f"material_parts={len(material_parts)}")
    print(f"status_history_parts={len(status_parts)}")


if __name__ == "__main__":
    main()
