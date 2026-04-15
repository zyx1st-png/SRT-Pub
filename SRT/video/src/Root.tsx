import React from 'react';
import { Composition } from 'remotion';
import { Intro }   from './Intro';
import { IntroCN } from './IntroCN';
import { Outro }   from './Outro';
import { OutroEN } from './OutroEN';
import { FPS, W, H } from './theme';

export const Root: React.FC = () => (
  <>
    {/* ── 开头 ── */}
    <Composition
      id="SRTIntro"
      component={Intro}
      durationInFrames={150}   // 5 s  英文版
      fps={FPS} width={W} height={H}
    />
    <Composition
      id="SRTIntroCN"
      component={IntroCN}
      durationInFrames={150}   // 5 s  中文版
      fps={FPS} width={W} height={H}
    />

    {/* ── 结尾 ── */}
    <Composition
      id="SRTOutro"
      component={Outro}
      durationInFrames={210}   // 7 s  中文版
      fps={FPS} width={W} height={H}
    />
    <Composition
      id="SRTOutroEN"
      component={OutroEN}
      durationInFrames={210}   // 7 s  英文版
      fps={FPS} width={W} height={H}
    />
  </>
);
