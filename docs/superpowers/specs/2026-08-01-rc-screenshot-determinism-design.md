# RC Screenshot Determinism Design

## Problem

The father-son render regression compares against three 1920x1080 screenshots that were recorded while Ren'Py was fullscreen on a 1920x1200 display. The testcase does not set a physical window size. A clean save starts windowed at the game's native 1280x720 resolution, so the first comparison fails on size before the RC suite can finish.

## Selected design

Normalize the father-son render testcase to the configured game resolution before it opens the fixture:

```renpy
$ renpy.set_physical_size((config.screen_width, config.screen_height))
pause 0.3
assert eval (renpy.get_physical_size() == (config.screen_width, config.screen_height))
```

Regenerate all three revision-tagged reference screenshots at 1280x720. Extend the existing Python asset contract so it rejects both a missing normalization call and any future reference image whose dimensions differ from 1280x720.

This is preferable to forcing fullscreen, which still depends on the host display, or resizing images during comparison, which can hide real layout changes.

## Verification

The regression must demonstrate both failure modes:

- RED: the Python contract fails against the current 1920x1080 references and missing normalization call.
- GREEN: the focused Ren'Py testcase passes from a brand-new savedir and from a savedir seeded with fullscreen preferences.
- The complete Ren'Py suite then passes from a brand-new savedir, followed by lint and the existing Python/release gates.

## Asset impact

No shipping art, music, sound effect, UI asset, video, or animation changes. Only three non-shipping test reference PNGs are re-recorded; the game's two WebP CG files remain byte-identical.
