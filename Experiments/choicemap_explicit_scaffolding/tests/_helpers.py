from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.utils import load_config

CONFIG = load_config(ROOT / "configs" / "smoke.yaml")

