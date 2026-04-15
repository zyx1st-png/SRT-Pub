/**
 * SRT Project — YouTube INTRO（中文版）
 * Duration: 5 s (150 frames @ 30 fps)
 * 与英文版动画完全一致，仅语言不同：
 *   "Project" → "项目"
 *   "Selection-Reality Theory" → "选择 · 现实 · 理论"
 */
import React from 'react';
import {
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
  Easing,
} from 'remotion';
import { COLORS, FONT } from './theme';
import { Particles } from './Particles';
import { Grid } from './Grid';

const easeOut = Easing.out(Easing.cubic);

export const IntroCN: React.FC = () => {
  const frame  = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const bgAlpha = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: 'clamp' });

  const srtScale = spring({
    frame: frame - 10,
    fps,
    config: { damping: 14, stiffness: 120, mass: 0.8 },
    durationInFrames: 30,
  });
  const srtOpacity = interpolate(frame, [10, 28], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeOut,
  });

  const pulse = frame > 50 ? 0.5 + 0.5 * Math.sin((frame - 50) * 0.12) : 0;

  const projX = interpolate(frame, [35, 60], [120, 0], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeOut,
  });
  const projOpacity = interpolate(frame, [35, 58], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeOut,
  });

  const subAlpha = interpolate(frame, [62, 88], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeOut,
  });

  const lineW = interpolate(frame, [70, 100], [0, 520], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeOut,
  });

  const fadeOut = interpolate(
    frame,
    [durationInFrames - 20, durationInFrames],
    [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeOut }
  );

  const masterAlpha = bgAlpha * fadeOut;

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        background: `radial-gradient(ellipse at 50% 45%, #0f0820 0%, ${COLORS.bg} 70%)`,
        overflow: 'hidden',
        position: 'relative',
        opacity: masterAlpha,
      }}
    >
      <Grid opacity={0.85} />
      <Particles count={55} fadeIn />

      <div
        style={{
          position: 'absolute',
          inset: 0,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 0,
        }}
      >
        {/* ── 标题行 ── */}
        <div
          style={{
            display: 'flex',
            alignItems: 'baseline',
            gap: 28,
            lineHeight: 1,
          }}
        >
          {/* "SRT" */}
          <span
            style={{
              fontFamily: FONT.title,
              fontSize: 200,
              fontWeight: 900,
              letterSpacing: '-0.03em',
              color: COLORS.white,
              opacity: srtOpacity,
              transform: `scale(${srtScale})`,
              display: 'inline-block',
              textShadow: [
                `0 0 ${20 + pulse * 30}px ${COLORS.accent1}`,
                `0 0 ${60 + pulse * 60}px ${COLORS.accent1}88`,
                `0 0 120px ${COLORS.accent2}44`,
              ].join(', '),
            }}
          >
            SRT
          </span>

          {/* "项目" — 从右滑入 */}
          <span
            style={{
              fontFamily: FONT.title,
              fontSize: 96,
              fontWeight: 300,
              letterSpacing: '0.1em',
              color: COLORS.accent2,
              opacity: projOpacity,
              transform: `translateX(${projX}px)`,
              display: 'inline-block',
              textShadow: `0 0 30px ${COLORS.accent2}88`,
            }}
          >
            项目
          </span>
        </div>

        {/* 分隔线 */}
        <div
          style={{
            width: lineW,
            height: 2,
            background: `linear-gradient(90deg, ${COLORS.accent1}, ${COLORS.accent2})`,
            borderRadius: 2,
            marginTop: 12,
            boxShadow: `0 0 12px ${COLORS.accent2}`,
          }}
        />

        {/* 副标题 */}
        <p
          style={{
            fontFamily: FONT.title,
            fontSize: 38,
            fontWeight: 300,
            letterSpacing: '0.28em',
            color: COLORS.dim,
            opacity: subAlpha,
            margin: '22px 0 0',
          }}
        >
          选择 · 现实 · 理论
        </p>
      </div>

      {/* 角落水印 */}
      <div
        style={{
          position: 'absolute',
          bottom: 48,
          right: 72,
          fontFamily: FONT.mono,
          fontSize: 22,
          color: COLORS.accent1,
          opacity: subAlpha * 0.6,
          letterSpacing: '0.1em',
        }}
      >
        srt-project
      </div>
    </div>
  );
};
