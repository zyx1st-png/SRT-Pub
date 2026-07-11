"""Configuration, hashing, and deterministic seed helpers."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import yaml


def load_config(path: str | Path) -> dict:
    with Path(path).open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def stable_json_hash(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def sha256_tree(root: str | Path, patterns: tuple[str, ...] = ("*.py", "*.yaml", "*.md", "*.txt", "*.cjs", "*.json")) -> str:
    root = Path(root)
    excluded = {"outputs", "node_modules", "manifests"}
    paths = sorted({p for pattern in patterns for p in root.rglob(pattern) if not excluded.intersection(p.parts)})
    h = hashlib.sha256()
    for path in paths:
        h.update(str(path.relative_to(root)).encode() + b"\0")
        h.update(path.read_bytes() + b"\0")
    return h.hexdigest()
