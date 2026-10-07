# Mio — anime character & storyboard skill

Standalone skill for designing original anime characters, registering and matching existing art (your own or generated elsewhere), and storyboarding scenes as images. Runs natively in Grok Imagine (Agent/Canvas) and writes copy-ready prompts for PixAI engines (Tsubaki.3/2/1, Haruka v2, Hoshino, Reference Pro).

**Version 2.2.1**

## What it does

- **Looks:** no style set → Mio suggests 2–3 styles that fit the character/genre/mood (one line each) and renders one look per style → you pick → locked. A locked style never changes silently.
- **Register as asset (2.2/2.2.1):** characters made outside Mio keep their **source** style — style read (line, shading, gloss, rendering palette, eyes, hair, skin, medium) into `[STYLE-SOURCE]`, identity colours (skin, hair, eyes with approx hex) into a separate `[IDENTITY-COLOURS]` lock, isolate by edit (pose edit for unsuitable source poses), fidelity check against the original with a retry ladder, original kept as style reference on later frames. No fallback to Mio defaults, no slimming, no flattening of glossy sources.
- **Canvas style (2.2):** one `[CANVAS-STYLE]` per canvas — `{{user}}`, every NPC and crowd inherit the first locked character's style; mixed sources draw new NPCs in the asset's style.
- **Storyboard anti-drift (2.2/2.2.1):** every frame re-anchors on the approved ISO/anchor image (never on a previous frame), style reference and identity colours fixed for the set, drift check per frame (incl. skin tone, hair colour/length, gloss, silhouette, counts), a 5-rung drift ladder instead of patching with words.
- **No speech bubbles (2.2):** bubbles, text, captions, SFX lettering and comic panels are banned (`bubbles=OFF`) unless you explicitly unlock them for the session; spoken lines never enter image prompts. Props that carry text (signs, name boards, shirts) are rendered blank (2.2.1).
- **Autopick (2.2.1):** `autopick=ON` lets Mio write missing locks itself and continue without waiting; OFF by default.
- **Reference Pack:** 5–30 images of one OC → bucket sort, majority consensus lock, ISO/turnaround/expression anchors, per-frame ≤3 refs (Grok-first, LoRA-lite).
- **PixAI LoRA:** dataset prep CLI + ritual; training only after your explicit OK.
- **Style library:** 40+ anime/manga/Pixiv styles plus engine house looks — Haruka v2, Tsubaki.2, Tsubaki.3, "ChatGPT anime" — and a Fit Map that maps genre/mood to suggestions.
- **Storyboards:** splits a greeting/scene into beats and **asks for any missing location, prop or NPC look** before drawing.
- **Anti-drift:** everything visual lives in LOCK blocks that are re-injected verbatim.

## Install

Copy the folder into your skills directory (e.g. `~/.grok/skills/mio/`) or upload `SKILL.md` (+ `references/`). Trigger with "Mio", "OC", "register this as asset", "match this art", "storyboard this greeting", "suggest a style", "Tsubaki prompt", etc.

## Layout

```
SKILL.md                              core ritual (short, authoritative)
references/engines.md                 Grok + PixAI engines, syntax, params, reference slots
references/styles.md                  style library, engine house looks, Fit Map
references/original-art.md            ART / register asset: style read, isolate, fidelity check, ref contract
references/reference-pack.md          PACK mode (≥5 images → anchors)
references/storyboard-consistency.md  multi-frame anti-drift, canvas style, NPC consistency
references/no-text.md                 speech-bubble / lettering ban and unlock
references/lora-pixai.md              PixAI LoRA prep / train gate
references/heat.md                    in-bounds adult illustration + retry ladders
references/poses.md                   pose pack
tools/lora-prep/                      dataset prep CLI (Pillow + imagehash)
```

## Limits

Adult fictional characters only (25, 1:7). No real people. Adult content stays inside the platform's allowed lane; no filter-evasion. No speech bubbles or lettering unless explicitly unlocked. Mio never starts paid LoRA training without explicit OK.

MIT licensed.
