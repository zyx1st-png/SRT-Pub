#!/usr/bin/env python3
from pathlib import Path
import runpy
import sys

# Temporary PR-local shim: the current generator is build_srt_context_bundles.py
# and writes by default. Ignore the legacy --write spelling used by the refresh job.
sys.argv = [str(Path(__file__).with_name("build_srt_context_bundles.py"))]
runpy.run_path(sys.argv[0], run_name="__main__")
