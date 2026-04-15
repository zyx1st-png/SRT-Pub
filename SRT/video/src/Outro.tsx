/**
 * SRT Project — YouTube OUTRO
 * Duration: 7 s (210 frames @ 30 fps)
 *
 * Timeline:
 *  0–20   Fade in from black
 * 15–50   "感谢观看" fades + slides up
 * 45–80   Divider line draws
 * 72–110  "SRT Project" logo appears (spring)
 * 100–140 Three CTA icons slide in staggered
 * 140–190 Hold (YouTube end-screen zone)
 * 190–210 Fade to black
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
const easeIn  = Easing.in(Easing.cubic);

/** A single CTA badge */
const CTABadge: React.FC<{
  icon: string;
  label: string;
  color: string;
  delay: number;
  frame: number;
  fps: number;
}> = ({ icon, label, color, delay, frame, fps }) => {
  const s = spring({
    frame: frame - delay,
    fps,
    config: { damping: 16, stiffness: 140, mass: 0.7 },
    durationInFrames: 28,
  });
  const opacity = interpolate(frame, [delay, delay + 20], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: easeOut,
  });

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: 12,
        opacity,
        transform: `translateY(${(1 - s) * 40}px)`,
      }}
    >
      {/* Circle icon */}
      <div
        style={{
          width: 88,
          height: 88,
          borderRadius: '50%',
          border: `2.5px solid ${color}`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: 38,
          boxShadow: `0 0 24px ${color}66`,
          background: `${color}11`,
        }}
      >
        {icon}
      </div>
      <span
        style={{
          fontFamily: FONT.title,
          fontSize: 26,
          fontWeight: 400,
          color: COLORS.dim,
          letterSpacing: '0.12em',
          textTransform: 'uppercase',
        }}
      >
        {label}
      </span>
    </div>
  );
};

export const Outro: React.FC = () => {
  const frame  = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  // ── Master alpha ──────────────────────────────────────────
  const fadeIn  = interpolate(frame, [0, 20], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeOut,
  });
  const fadeOut = interpolate(
    frame,
    [durationInFrames - 20, durationInFrames],
    [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeIn }
  );
  const masterAlpha = fadeIn * fadeOut;

  // ── "感谢观看" ────────────────────────────────────────────
  const thankY = interpolate(frame, [15, 48], [30, 0], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeOut,
  });
  const thankAlpha = interpolate(frame, [15, 48], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeOut,
  });

  // ── Divider line ──────────────────────────────────────────
  const lineW = interpolate(frame, [48, 78], [0, 600], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeOut,
  });

  // ── "SRT Project" ─────────────────────────────────────────
  const logoScale = spring({
    frame: frame - 72,
    fps,
    config: { damping: 13, stiffness: 110, mass: 0.9 },
    durationInFrames: 36,
  });
  const logoAlpha = interpolate(frame, [72, 96], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: easeOut,
  });

  // ── Subtle pulse ──────────────────────────────────────────
  const pulse = frame > 110
    ? 0.5 + 0.5 * Math.sin((frame - 110) * 0.1)
    : 0;

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        background: `radial-gradient(ellipse at 50% 60%, #0d0520 0%, ${COLORS.bg} 68%)`,
        overflow: 'hidden',
        position: 'relative',
        opacity: masterAlpha,
      }}
    >
      <Grid opacity={0.6} />
      <Particles count={45} fadeIn={false} />

      {/* ── Centre card ── */}
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
        {/* Thanks */}
        <p
          style={{
            fontFamily: FONT.title,
            fontSize: 68,
            fontWeight: 300,
            letterSpacing: '0.25em',
            color: COLORS.dim,
            margin: 0,
            opacity: thankAlpha,
            transform: `translateY(${thankY}px)`,
          }}
        >
          感谢观看
        </p>

        {/* Divider */}
        <div
          style={{
            width: lineW,
            height: 2,
            background: `linear-gradient(90deg, ${COLORS.accent3}, ${COLORS.accent1}, ${COLORS.accent2})`,
            borderRadius: 2,
            margin: '28px 0 32px',
            boxShadow: `0 0 16px ${COLORS.accent1}88`,
          }}
        />

        {/* SRT Project logo */}
        <div
          style={{
            display: 'flex',
            alignItems: 'baseline',
            gap: 18,
            opacity: logoAlpha,
            transform: `scale(${logoScale})`,
          }}
        >
          <span
            style={{
              fontFamily: FONT.title,
              fontSize: 110,
              fontWeight: 900,
              letterSpacing: '-0.03em',
              color: COLORS.white,
              textShadow: [
                `0 0 ${16 + pulse * 24}px ${COLORS.accent1}`,
                `0 0 ${48 + pulse * 48}px ${COLORS.accent1}66`,
              ].join(', '),
            }}
          >
            SRT
          </span>
          <span
            style={{
              fontFamily: FONT.title,
              fontSize: 52,
              fontWeight: 300,
              letterSpacing: '0.2em',
              color: COLORS.accent2,
              textTransform: 'uppercase',
              textShadow: `0 0 24px ${COLORS.accent2}88`,
            }}
          >
            Project
          </span>
        </div>

        {/* CTA badges */}
        <div
          style={{
            display: 'flex',
            gap: 80,
            marginTop: 58,
          }}
        >
          <CTABadge
            icon="🔔"
            label="订阅"
            color={COLORS.accent3}
            delay={100}
            frame={frame}
            fps={fps}
          />
          <CTABadge
            icon="👍"
            label="点赞"
            color={COLORS.accent1}
            delay={115}
            frame={frame}
            fps={fps}
          />
          <CTABadge
            icon="💬"
            label="留言"
            color={COLORS.accent2}
            delay={130}
            frame={frame}
            fps={fps}
          />
        </div>
      </div>

      {/* Bottom watermark */}
      <div
        style={{
          position: 'absolute',
          bottom: 44,
          left: 0,
          right: 0,
          textAlign: 'center',
          fontFamily: FONT.mono,
          fontSize: 20,
          color: COLORS.accent1,
          opacity: logoAlpha * 0.5,
          letterSpacing: '0.15em',
        }}
      >
        Selection-Reality Theory  ·  srt-project
      </div>
    </div>
  );
};
