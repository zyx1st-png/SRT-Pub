# SRT Video Workflows

This folder now contains both the Remotion branding assets and the bilingual post-production workflow that used to live in another project.

## What Lives Here

- `src/`: Remotion intro/outro compositions
- `out/`: rendered branding clips reused by the post-production pipeline
- `scripts/`: subtitle extraction, dubbing, subtitle burn-in, and final assembly scripts

## Branding Clips

Render the reusable intros/outros from this folder:

```bash
cd /Users/zhangyuxin/.openclaw/workspace/SRT/video
npm run render:intro
npm run render:intro-cn
npm run render:outro
npm run render:outro-en
```

The dual-language pipeline reuses these defaults:

- English intro: `video/out/intro.mp4`
- Chinese intro: `video/out/intro_cn.mp4`
- Chinese outro: `video/out/outro.mp4`
- English outro: `video/out/outro_en.mp4`

## Dual-Language Pipeline

Supported entrypoint:

```bash
cd /Users/zhangyuxin/.openclaw/workspace/SRT/video
./run_dual_language_pipeline.sh \
  --video /absolute/path/to/source.mp4 \
  --chinese-srt /absolute/path/to/translated.zh.srt
```

If you omit `--chinese-srt`, the pipeline now auto-generates:

- `*.zh.contextual.srt`
- `*.zh.polished.srt`
- `*.zh.spoken.srt`

The dubbing step then uses the generated `spoken` version by default.

Equivalent raw `uv` command:

```bash
uv run \
  --with faster-whisper \
  --with pydub \
  --with opencv-python \
  --with pillow \
  --with numpy \
  --with edge-tts \
  python /Users/zhangyuxin/.openclaw/workspace/SRT/video/scripts/video_dual_language_pipeline.py \
  --video /absolute/path/to/source.mp4 \
  --chinese-srt /absolute/path/to/translated.zh.srt
```

Outputs go to `video/pipeline_out/` by default unless `--output-dir` is set.

Automatic translation uses an OpenAI-compatible chat endpoint. Set one of:

- `SRT_VIDEO_TRANSLATE_API_KEY`
- `OPENAI_API_KEY`
- or pass a custom env var name via `--translate-api-key-env`

Optional overrides:

- `SRT_VIDEO_TRANSLATE_MODEL`
- `SRT_VIDEO_TRANSLATE_BASE_URL`

## Workflow Notes

- English subtitle extraction is automatic via `faster-whisper`.
- Chinese translation can now be automatic if you omit `--chinese-srt`.
- The translation flow is staged as `contextual -> polished -> spoken` so you still get intermediate subtitle assets.
- Chinese dubbing is generated from that translated `.srt`.
- Final outputs include English and Chinese `mp4`, `srt`, and `mp3`.

## Helper Scripts

- `transcribe_video_fw.py`: English transcription to `srt/txt/json`
- `translate_subtitles.py`: staged subtitle translation via an OpenAI-compatible API
- `align_dub.py`: timestamp-aligned TTS dubbing
- `burn_bilingual_subs.py`: Chinese-only or bilingual subtitle burn-in
- `finalize_en_intro_outro_clean.py`: clean English main clip and assemble intro/outro
- `finalize_cn_intro_outro.py`: title-card and Chinese finalization helper
- `video_dual_language_pipeline.py`: top-level end-to-end workflow
