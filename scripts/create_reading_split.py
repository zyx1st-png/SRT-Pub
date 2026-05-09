#!/usr/bin/env python3
"""Create connector-safe reading shards for a long Markdown owner file."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import argparse
import hashlib
import os
import re
import shutil


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MAX_BYTES = 40_000


@dataclass
class Part:
    index: int
    title: str
    content: str
    filename: str


def rel(path: Path, start: Path) -> str:
    return os.path.relpath(path, start).replace(os.sep, "/")


def md_target(target: str) -> str:
    return target.replace(" ", "%20")


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    return text[: end + 5], text[end + 5 :].lstrip("\n")


def frontmatter_value(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", frontmatter, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip().strip('"').strip("'")


def extract_main_title(body: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return fallback


def block_title(block: str, fallback: str) -> str:
    match = re.search(r"^#{1,3}\s+(.+)$", block, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return fallback


def markdown_blocks(body: str) -> list[str]:
    lines = body.splitlines(keepends=True)
    blocks: list[str] = []
    current: list[str] = []
    heading_re = re.compile(r"^#{1,3}\s+")
    for line in lines:
        if heading_re.match(line) and current:
            blocks.append("".join(current).strip() + "\n")
            current = [line]
        else:
            current.append(line)
    if current:
        blocks.append("".join(current).strip() + "\n")
    return [block for block in blocks if block.strip()]


def split_large_block(block: str, max_body_bytes: int) -> list[str]:
    if len(block.encode("utf-8")) <= max_body_bytes:
        return [block]
    paragraphs = re.split(r"(\n\s*\n)", block)
    out: list[str] = []
    current = ""
    for piece in paragraphs:
        if not piece:
            continue
        if current and len((current + piece).encode("utf-8")) > max_body_bytes:
            out.append(current.strip() + "\n")
            current = piece
        else:
            current += piece
    if current.strip():
        out.append(current.strip() + "\n")

    line_safe: list[str] = []
    for item in out:
        if len(item.encode("utf-8")) <= max_body_bytes:
            line_safe.append(item)
            continue
        line_current = ""
        for line in item.splitlines(keepends=True):
            if line_current and len((line_current + line).encode("utf-8")) > max_body_bytes:
                line_safe.append(line_current.strip() + "\n")
                line_current = line
            else:
                line_current += line
        if line_current.strip():
            line_safe.append(line_current.strip() + "\n")
    return line_safe


def build_parts(body: str, max_bytes: int) -> list[Part]:
    max_body_bytes = int(max_bytes * 0.82)
    blocks: list[str] = []
    for block in markdown_blocks(body):
        blocks.extend(split_large_block(block, max_body_bytes))

    parts: list[Part] = []
    current: list[str] = []
    current_size = 0
    for block in blocks:
        block_size = len(block.encode("utf-8"))
        if current and current_size + block_size > max_body_bytes:
            content = "\n".join(current).strip() + "\n"
            idx = len(parts)
            parts.append(
                Part(
                    index=idx,
                    title=block_title(content, f"Part {idx:02d}"),
                    content=content,
                    filename=f"{idx:02d}_Part{idx + 1:02d}.md",
                )
            )
            current = [block]
            current_size = block_size
        else:
            current.append(block)
            current_size += block_size

    if current:
        content = "\n".join(current).strip() + "\n"
        idx = len(parts)
        parts.append(
            Part(
                index=idx,
                title=block_title(content, f"Part {idx:02d}"),
                content=content,
                filename=f"{idx:02d}_Part{idx + 1:02d}.md",
            )
        )
    return parts


def write_part(part: Part, source: Path, split_dir: Path, split_id: str) -> None:
    source_link = rel(source, split_dir)
    text = "\n".join(
        [
            "---",
            f"id: {split_id}-PART-{part.index:02d}",
            "type: reading_shard",
            "tags: [Split, Navigation, Longform, ConnectorSafety]",
            "status: active_v1",
            "layer: meta",
            "epistemic_layer: os",
            "claim_mode: evidence",
            "canonical: false",
            f"source_owner: {source_link}",
            "---",
            "",
            f"# Part {part.index:02d}: {part.title}",
            "",
            f"> Source owner: [`{source_link}`]({md_target(source_link)})",
            ">",
            "> Reading-aid guardrail: this shard is a connector-safe navigation copy. It does not create new definitions, new claim status, or independent authority.",
            "",
            part.content.rstrip(),
            "",
        ]
    )
    (split_dir / part.filename).write_text(text, encoding="utf-8")


def write_readme(
    source: Path,
    split_dir: Path,
    split_id: str,
    source_id: str,
    title: str,
    parts: list[Part],
) -> None:
    source_link = rel(source, split_dir)
    rows = []
    for part in parts:
        path = split_dir / part.filename
        digest = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
        rows.append(
            f"| {part.index:02d} | [`{part.filename}`]({part.filename}) | {part.title} | {path.stat().st_size} | `{digest}` |"
        )
    readme = "\n".join(
        [
            "---",
            f"id: {split_id}",
            "type: index",
            "tags: [Split, Navigation, Longform, ConnectorSafety]",
            "status: active_v1",
            "layer: meta",
            "epistemic_layer: os",
            "claim_mode: evidence",
            "canonical: false",
            f"dependency: [{source_id}]",
            "---",
            "",
            f"# {title} Split Index",
            "",
            f"- 原始总文（保留，不删内容）：[`{source_link}`]({md_target(source_link)})",
            "- 本目录只承担连接器安全读取、导航与局部检索；不创建新的定义权或 claim status。",
            "- 修改正文含义时仍以 owner 文件与上游 canonical / governance 文件为准。",
            "",
            "| Part | File | Starts with | Bytes | SHA-256 prefix |",
            "|---:|---|---|---:|---|",
            *rows,
            "",
        ]
    )
    (split_dir / "README.md").write_text(readme, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("split_dir")
    parser.add_argument("--id", required=True)
    parser.add_argument("--title")
    parser.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    source = Path(args.source)
    if not source.is_absolute():
        source = ROOT / source
    split_dir = Path(args.split_dir)
    if not split_dir.is_absolute():
        split_dir = ROOT / split_dir
    if not source.is_file():
        raise SystemExit(f"source not found: {source}")
    if split_dir.exists():
        if not args.force:
            raise SystemExit(f"split dir already exists: {split_dir}")
        shutil.rmtree(split_dir)
    split_dir.mkdir(parents=True)

    text = source.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(text)
    source_id = frontmatter_value(frontmatter, "id") or source.stem.upper().replace(" ", "-")
    title = args.title or extract_main_title(body, source.stem)
    parts = build_parts(body, args.max_bytes)
    for part in parts:
        write_part(part, source, split_dir, args.id, )
    write_readme(source, split_dir, args.id, source_id, title, parts)
    largest = max((split_dir / part.filename).stat().st_size for part in parts)
    print(f"source={source.relative_to(ROOT)}")
    print(f"split_dir={split_dir.relative_to(ROOT)}")
    print(f"parts={len(parts)}")
    print(f"largest_part={largest}")


if __name__ == "__main__":
    main()
