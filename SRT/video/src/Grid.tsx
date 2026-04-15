import React from 'react';
import { useCurrentFrame } from 'remotion';
import { COLORS, W, H } from './theme';

/** Animated perspective grid — gives a "quantum field" look */
export const Grid: React.FC<{ opacity?: number }> = ({ opacity = 1 }) => {
  const frame = useCurrentFrame();

  // Slowly shift the grid downward to suggest movement through a field
  const shift = (frame * 0.8) % 80;

  const lines: React.ReactNode[] = [];

  // Horizontal lines — perspective converge toward horizon at 60% height
  for (let i = 0; i <= 14; i++) {
    const t   = i / 14;
    const y   = H * 0.6 + (t - 0.5) * H * 1.2 + shift * (t - 0.5);
    const w   = 60 + t * (W - 120);
    const x   = (W - w) / 2;
    const alpha = (0.06 + t * 0.06) * opacity;
    lines.push(
      <line
        key={`h${i}`}
        x1={x} y1={y}
        x2={x + w} y2={y}
        stroke={COLORS.accent1}
        strokeWidth="1"
        opacity={alpha}
      />
    );
  }

  // Vertical lines — radiate from vanishing point
  const vp = { x: W / 2, y: H * 0.6 };
  for (let i = 0; i <= 20; i++) {
    const t  = i / 20;
    const bx = W * t;
    const alpha = (0.04 + 0.04 * Math.sin(t * Math.PI)) * opacity;
    lines.push(
      <line
        key={`v${i}`}
        x1={vp.x} y1={vp.y}
        x2={bx}   y2={H}
        stroke={COLORS.accent2}
        strokeWidth="0.8"
        opacity={alpha}
      />
    );
  }

  return (
    <svg
      style={{ position: 'absolute', inset: 0 }}
      width={W}
      height={H}
      viewBox={`0 0 ${W} ${H}`}
    >
      {lines}
    </svg>
  );
};
