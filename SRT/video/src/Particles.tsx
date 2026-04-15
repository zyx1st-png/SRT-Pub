import React, { useMemo } from 'react';
import { useCurrentFrame, useVideoConfig } from 'remotion';
import { COLORS } from './theme';

interface Particle {
  x: number;
  y: number;
  size: number;
  speed: number;
  phase: number;
  color: string;
  opacity: number;
}

const PARTICLE_COLORS = [
  COLORS.accent1,
  COLORS.accent2,
  COLORS.accent3,
];

export const Particles: React.FC<{ count?: number; fadeIn?: boolean }> = ({
  count = 60,
  fadeIn = true,
}) => {
  const frame   = useCurrentFrame();
  const { width, height, durationInFrames } = useVideoConfig();

  const particles = useMemo<Particle[]>(() => {
    const rng = (seed: number) => {
      const x = Math.sin(seed) * 43758.5453123;
      return x - Math.floor(x);
    };
    return Array.from({ length: count }, (_, i) => ({
      x:       rng(i * 7.1)  * width,
      y:       rng(i * 13.3) * height,
      size:    1.5 + rng(i * 3.7) * 3,
      speed:   0.15 + rng(i * 5.2) * 0.4,
      phase:   rng(i * 9.9) * Math.PI * 2,
      color:   PARTICLE_COLORS[Math.floor(rng(i * 2.3) * 3)],
      opacity: 0.25 + rng(i * 11.1) * 0.55,
    }));
  }, [count, width, height]);

  const globalAlpha = fadeIn
    ? Math.min(1, frame / 20)
    : Math.max(0, 1 - (frame - (durationInFrames - 20)) / 20);

  return (
    <svg
      style={{ position: 'absolute', inset: 0, width: '100%', height: '100%' }}
      width={width}
      height={height}
    >
      {particles.map((p, i) => {
        const dy    = Math.sin(frame * p.speed * 0.04 + p.phase) * 18;
        const pulse = 0.5 + 0.5 * Math.sin(frame * p.speed * 0.08 + p.phase);
        return (
          <circle
            key={i}
            cx={p.x}
            cy={p.y + dy}
            r={p.size * (0.85 + 0.15 * pulse)}
            fill={p.color}
            opacity={p.opacity * pulse * globalAlpha}
          />
        );
      })}
    </svg>
  );
};
