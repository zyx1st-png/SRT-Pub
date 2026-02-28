#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1] / "SRT"
SYMBOLS = ROOT / "_SRT_SYMBOL_TABLE.md"

REQUIRED_TOKENS = ["L_0", "L_1", "L_2", "\\Psi_f"]
ALT_GHOST_TOKENS = ["\\hat{G}_\\theta", "\\hat{G}"]


def main() -> int:
    if not SYMBOLS.exists():
        print("[MISSING] SRT/_SRT_SYMBOL_TABLE.md")
        return 1

    txt = SYMBOLS.read_text(errors="ignore")
    missing = [t for t in REQUIRED_TOKENS if t not in txt]
    if not any(t in txt for t in ALT_GHOST_TOKENS):
        missing.append("\\hat{G} or \\hat{G}_\\theta")

    if missing:
        print("Symbol governance check failed:")
        for m in missing:
            print(f"- missing canonical token: {m}")
        return 1

    print("Symbol governance check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
