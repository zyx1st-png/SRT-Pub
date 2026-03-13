#!/usr/bin/env python3
"""
SRT Knowledge Review Script - Pipeline 7
随机抽取 SRT 理论知识点，支持 JSON 输出和内容回写。

Usage:
  python srt_knowledge_review.py --count 3               # 抽取 3 个知识点并打印
  python srt_knowledge_review.py --count 3 --output-json # 输出 JSON 供 Claude 读取
  python srt_knowledge_review.py --list-domains          # 列出所有可用领域
  python srt_knowledge_review.py --writeback --patch-file /tmp/patch.json  # 回写
"""

import os
import re
import json
import random
import argparse
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

# ──────────────────────────────────────────────
# 配置
# ──────────────────────────────────────────────
SRT_ROOT = Path(__file__).parent.parent / "SRT"

# 纳入扫描的目录（相对于 SRT_ROOT）
THEORY_DIRS = [
    "Core",
    "Core_Law",
    "Physics",
    "Philosophy",
    "Neuroscience",
    "Spirituality",
    "AI",
]

# 排除规则
EXCLUDE_SUFFIXES = ["_CompactCore.md"]
EXCLUDE_DIR_PARTS = {"Split", "Annex", "Praxis_Split", "Operations", "Governance", "Glossary", ".venv", ".obsidian"}
EXCLUDE_DIR_SUFFIXES = ("_Split", "_Annex")
EXCLUDE_FILENAME_PATTERNS = [
    r".*Bridge\.md$",
    r".*_REGISTRY\.md$",
    r".*_SPLIT_PLAN\.md$",
    r".*CompactCore\.md$",
]

MIN_CONTENT_CHARS = 60  # 知识块最少字符数（过滤占位内容）


@dataclass
class KnowledgePoint:
    kp_id: str          # 唯一标识（自动生成或从文件中提取）
    doc_id: str         # 文件 frontmatter id
    file_path: str      # 相对于 SRT_ROOT 的路径
    line_start: int     # 1-based
    line_end: int       # 1-based, inclusive
    heading_level: int  # 2 or 3
    title: str          # heading text
    content: str        # 完整块内容（含 heading 行）
    domain: str         # Core / Physics / Philosophy / ...


# ──────────────────────────────────────────────
# 文件扫描与知识点提取
# ──────────────────────────────────────────────

def should_exclude(path: Path) -> bool:
    """判断文件是否应被排除"""
    # 排除目录组件
    for part in path.parts:
        if part in EXCLUDE_DIR_PARTS:
            return True
        if part.endswith(EXCLUDE_DIR_SUFFIXES):
            return True
    # 排除文件名模式
    for pat in EXCLUDE_FILENAME_PATTERNS:
        if re.match(pat, path.name):
            return True
    return False


def get_doc_id(lines: list[str]) -> str:
    """从 frontmatter 提取 id 字段"""
    in_frontmatter = False
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if line.strip() == "---":
                break
            m = re.match(r"^id:\s*(.+)$", line.strip())
            if m:
                return m.group(1).strip()
    return ""


def extract_knowledge_points(file_path: Path, domain: str) -> list[KnowledgePoint]:
    """从单个 .md 文件中提取 ### 级知识块"""
    try:
        text = file_path.read_text(encoding="utf-8")
    except Exception:
        return []

    lines = text.splitlines()
    doc_id = get_doc_id(lines)
    rel_path = str(file_path.relative_to(SRT_ROOT))

    points = []
    # 找到所有 ### 或 ## 标题行
    heading_lines = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#{2,3})\s+(.+)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            heading_lines.append((i, level, title))

    # 若无 ### 级标题，用 ## 级（部分文件只有二级标题）
    h3_count = sum(1 for _, lv, _ in heading_lines if lv == 3)
    target_level = 3 if h3_count >= 2 else 2

    target_headings = [(i, lv, t) for i, lv, t in heading_lines if lv == target_level]

    for idx, (line_idx, level, title) in enumerate(target_headings):
        # 块结束位置：下一个同级或更高级标题，或文件末尾
        if idx + 1 < len(target_headings):
            end_idx = target_headings[idx + 1][0] - 1
        else:
            end_idx = len(lines) - 1

        block_lines = lines[line_idx:end_idx + 1]
        # 去除末尾空行
        while block_lines and block_lines[-1].strip() == "":
            block_lines.pop()

        content = "\n".join(block_lines)
        # 过滤过短内容
        if len(content.strip()) < MIN_CONTENT_CHARS:
            continue

        # 提取知识点内嵌 ID（如 Ax-Core-A1、T-Core-A1C1、Def-Protocol-1 等）
        embedded_id = _extract_embedded_id(title)

        kp_id = embedded_id if embedded_id else f"{doc_id}::{_slugify(title)}"

        points.append(KnowledgePoint(
            kp_id=kp_id,
            doc_id=doc_id,
            file_path=rel_path,
            line_start=line_idx + 1,
            line_end=end_idx + 1,
            heading_level=level,
            title=title,
            content=content,
            domain=domain,
        ))

    return points


def _extract_embedded_id(title: str) -> str:
    """从标题中提取标准 SRT ID（如 Ax-Core-A1、T-Core-A1C1、Def-Protocol-1）"""
    m = re.match(r"^([A-Za-z][\w\-]+)[\s:：]", title)
    if m:
        candidate = m.group(1)
        # 判断是否像 SRT ID（含连字符且非全小写普通单词）
        if "-" in candidate and re.search(r"[A-Z0-9]", candidate):
            return candidate
    return ""


def _slugify(text: str) -> str:
    """生成简单 slug"""
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "_", text.strip())
    return text[:40]


def index_all_knowledge_points(domain_filter: Optional[str] = None) -> list[KnowledgePoint]:
    """扫描所有理论目录，返回所有知识点列表"""
    all_points = []
    for domain_dir in THEORY_DIRS:
        if domain_filter and domain_dir.lower() != domain_filter.lower():
            continue
        base = SRT_ROOT / domain_dir
        if not base.exists():
            continue
        for md_file in sorted(base.rglob("*.md")):
            if should_exclude(md_file):
                continue
            points = extract_knowledge_points(md_file, domain_dir)
            all_points.extend(points)
    return all_points


# ──────────────────────────────────────────────
# 抽样
# ──────────────────────────────────────────────

def sample_knowledge_points(
    count: int = 3,
    domain_filter: Optional[str] = None,
    seed: Optional[int] = None,
) -> list[KnowledgePoint]:
    """随机抽取 N 个知识点"""
    all_points = index_all_knowledge_points(domain_filter)
    if not all_points:
        return []
    if seed is not None:
        random.seed(seed)
    count = min(count, len(all_points))
    return random.sample(all_points, count)


# ──────────────────────────────────────────────
# 输出（人类可读）
# ──────────────────────────────────────────────

DIVIDER = "─" * 60

def print_knowledge_points(points: list[KnowledgePoint]) -> None:
    total = len(points)
    for i, kp in enumerate(points, 1):
        print(f"\n{DIVIDER}")
        print(f"【知识点 {i}/{total}】")
        print(f"📍 来源：{kp.file_path}  (行 {kp.line_start}–{kp.line_end})")
        print(f"🏷️  ID：{kp.kp_id}  |  领域：{kp.domain}")
        print(DIVIDER)
        print(kp.content)
        print(DIVIDER)


# ──────────────────────────────────────────────
# JSON 输出（供 Claude 程序化读取）
# ──────────────────────────────────────────────

def output_json(points: list[KnowledgePoint]) -> None:
    data = [asdict(kp) for kp in points]
    print(json.dumps(data, ensure_ascii=False, indent=2))


# ──────────────────────────────────────────────
# 回写
# ──────────────────────────────────────────────

@dataclass
class PatchEntry:
    kp_id: str
    file_path: str       # 相对于 SRT_ROOT
    line_start: int
    line_end: int
    new_content: str     # 替换后的完整块内容（含 heading 行）


def apply_patches(patch_file: str, dry_run: bool = False) -> list[str]:
    """
    读取 patch JSON 文件，将修改写回源文件。
    patch JSON 格式：
    [
      {
        "kp_id": "...",
        "file_path": "Core/SRT_Core_01_Axioms.md",
        "line_start": 73,
        "line_end": 78,
        "new_content": "### Ax-Core-A1: ..."
      },
      ...
    ]
    返回已修改的文件列表。
    """
    with open(patch_file, encoding="utf-8") as f:
        patches = json.load(f)

    # 按文件分组，同一文件的 patch 一起处理
    by_file: dict[str, list[dict]] = {}
    for p in patches:
        fp = p["file_path"]
        by_file.setdefault(fp, []).append(p)

    modified_files = []

    for rel_path, file_patches in by_file.items():
        abs_path = SRT_ROOT / rel_path
        if not abs_path.exists():
            print(f"[WARN] 文件不存在，跳过：{rel_path}")
            continue

        lines = abs_path.read_text(encoding="utf-8").splitlines(keepends=True)

        # 从后往前替换（避免行号偏移）
        file_patches_sorted = sorted(file_patches, key=lambda x: x["line_start"], reverse=True)

        for patch in file_patches_sorted:
            start = patch["line_start"] - 1  # 转为 0-based
            end = patch["line_end"]          # 切片 end（exclusive）
            new_lines = patch["new_content"].splitlines(keepends=False)
            # 确保每行以换行符结尾
            new_lines_with_nl = [l + "\n" for l in new_lines]

            lines[start:end] = new_lines_with_nl
            print(f"[PATCH] {rel_path} 行 {patch['line_start']}–{patch['line_end']} → {len(new_lines)} 行")

        if not dry_run:
            abs_path.write_text("".join(lines), encoding="utf-8")
            modified_files.append(rel_path)
            print(f"[WRITE] {rel_path}")

    return modified_files


# ──────────────────────────────────────────────
# 工具函数：列出领域统计
# ──────────────────────────────────────────────

def list_domains() -> None:
    """列出每个领域的知识点数量"""
    all_points = index_all_knowledge_points()
    domain_counts: dict[str, int] = {}
    for kp in all_points:
        domain_counts[kp.domain] = domain_counts.get(kp.domain, 0) + 1

    print("\n SRT 知识点领域统计")
    print(DIVIDER)
    total = 0
    for domain in THEORY_DIRS:
        count = domain_counts.get(domain, 0)
        total += count
        print(f"  {domain:<20} {count:>4} 个知识点")
    print(DIVIDER)
    print(f"  {'合计':<20} {total:>4} 个知识点")


# ──────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="SRT Knowledge Review Pipeline 7 — 随机抽取知识点 / 回写优化内容"
    )
    parser.add_argument("--count", "-n", type=int, default=3, help="抽取知识点数量（默认 3）")
    parser.add_argument("--domain", "-d", type=str, default=None,
                        help="限定领域（Core / Physics / Philosophy / Neuroscience / Spirituality / AI / Core_Law）")
    parser.add_argument("--seed", type=int, default=None, help="随机种子（用于复现）")
    parser.add_argument("--output-json", action="store_true", help="输出 JSON 格式（供 Claude 读取）")
    parser.add_argument("--list-domains", action="store_true", help="列出各领域知识点统计")
    parser.add_argument("--writeback", action="store_true", help="执行回写模式")
    parser.add_argument("--patch-file", type=str, default=None, help="patch JSON 文件路径（--writeback 时必须）")
    parser.add_argument("--dry-run", action="store_true", help="dry-run 模式：只打印不写文件")

    args = parser.parse_args()

    if args.list_domains:
        list_domains()
        return

    if args.writeback:
        if not args.patch_file:
            print("[ERROR] --writeback 需要 --patch-file 参数")
            return
        modified = apply_patches(args.patch_file, dry_run=args.dry_run)
        if modified:
            print(f"\n✅ 已修改 {len(modified)} 个文件：")
            for f in modified:
                print(f"  - {f}")
        return

    # 默认：抽样并输出
    points = sample_knowledge_points(
        count=args.count,
        domain_filter=args.domain,
        seed=args.seed,
    )

    if not points:
        print("[WARN] 未找到知识点，请检查 SRT_ROOT 路径和目录配置")
        return

    if args.output_json:
        output_json(points)
    else:
        print_knowledge_points(points)


if __name__ == "__main__":
    main()
