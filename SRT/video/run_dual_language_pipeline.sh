#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

uv run \
  --with faster-whisper \
  --with pydub \
  --with opencv-python \
  --with pillow \
  --with numpy \
  --with edge-tts \
  python "$ROOT_DIR/scripts/video_dual_language_pipeline.py" "$@"
