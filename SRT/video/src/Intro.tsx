/**
 * SRT Project — YouTube INTRO
 * Duration: 5 s (150 frames @ 30 fps)
 *
 * Timeline:
 *  0–15   Background + grid fade in
 * 10–35   "SRT" logo springs in (scale + opacity)
 * 35–65   "Project" slides in from right
 * 60–90   Subtitle "Selection-Reality Theory" fades in
 * 90–130  Glow pulse + hold
 * 130–150 Fast fade-out to black
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

export const Intro: React.FC = () => {
  const frame  = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  // ── Background & Grid ─────────────────────────────────────
  const bgAlpha = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: 'clamp' });

  // ── "SRT" logo ────────────────────────────────────────────
  const srtScale = spring({
    frame: frame - 10,
    fps,
    config: { damping: 14, stiffness: 120, mass: 0.8 },
    durationInFrames: 30,
  });
  const srtOpacity = interpolate(frame, [10, 28], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: easeOut,
  });

  // Subtle glow pulse after logo arrives
  const pulse = frame > 50
    ? 0.5 + 0.5 * Math.sin((frame - 50) * 0.12)
    : 0;

  // ── "Project" word ────────────────────────────────────────
  const projX = interpolate(frame, [35, 60], [120, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: easeOut,
  });
  const projOpacity = interpolate(frame, [35, 58], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: easeOut,
  });

  // ── Subtitle ──────────────────────────────────────────────
  const subAlpha = interpolate(frame, [62, 88], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: easeOut,
  });

  // ── Accent line under title ────────────────────────────────
  const lineW = interpolate(frame, [70, 100], [0, 520], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: easeOut,
  });

  // ── Final fade out ─────────────────────────────────────────
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
      {/* Grid */}
      <Grid opacity={0.85} />

      {/* Particles */}
      <Particles count={55} fadeIn />

      {/* Centre content */}
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
        {/* ── Title row ── */}
        <div
          style={{
            display: 'flex',
            alignItems: 'baseline',
            gap: 28,
            lineHeight: 1,
          }}
        >
          {/* "SRT" — large, glowing */}
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

          {/* "Project" — slides in */}
          <span
            style={{
              fontFamily: FONT.title,
              fontSize: 96,
              fontWeight: 300,
              letterSpacing: '0.18em',
              color: COLORS.accent2,
              opacity: projOpacity,
              transform: `translateX(${projX}px)`,
              display: 'inline-block',
              textTransform: 'uppercase',
              textShadow: `0 0 30px ${COLORS.accent2}88`,
            }}
          >
            Project
          </span>
        </div>

        {/* ── Accent line ── */}
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

        {/* ── Subtitle ── */}
        <p
          style={{
            fontFamily: FONT.title,
            fontSize: 38,
            fontWeight: 300,
            letterSpacing: '0.22em',
            color: COLORS.dim,
            opacity: subAlpha,
            margin: '22px 0 0',
            textTransform: 'uppercase',
          }}
        >
          Selection-Reality Theory
        </p>
      </div>

      {/* Corner watermark */}
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
