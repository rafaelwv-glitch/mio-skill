# Original art & registered external assets → ISO → constant generation

Use when the user uploads their own art **or registers a character generated outside Mio** ("register as asset", "use this character", "keep this style"). 1–4 images. For ≥ 5 images use `reference-pack.md`.

**Core rule:** the source image is the style authority. Mio describes it, isolates it and keeps it — Mio does **not** translate it into a Mio default style. No fallback to MOE / CEL00 / PAINT or any other library ID for a registered asset.

## 1. Style read (write before generating anything)

Read only what is visible. One value per axis, concrete words:

| Axis | What to write | Example |
|---|---|---|
| line | weight, variation, colour, closure | thin even dark-brown lines, slight taper, lines broken at highlights |
| shading | type, number of tones, edge | two-tone hard cel, one soft gradient on hair only, no ambient occlusion |
| palette | named colours + approx hex, saturation, temperature | hair ash-lavender (~#B8A9C9), skin warm ivory (~#F3DCCB), shadow dusty mauve (~#9C7F95), accent crimson (~#B0233A); muted, cool |
| eyes | shape, iris layers, highlight shape/count, lash rendering | almond, 3-layer gradient iris, one large oval highlight + two dots, lashes as solid black wedges |
| hair | strand grouping, sheen type, edge | large clumps, angel-ring sheen band, soft airbrushed tips |
| skin | finish, blush, highlights | matte, flat base, pink hatched blush, no nose shine |
| medium | digital/traditional, texture, finish | clean digital, no paper texture, light grain, soft bloom |

Hex values are approximate descriptors (named colour first; engines read words better than hex).

Write the block:
```
[STYLE-SOURCE] EXT:<short label> — line … · shading … · palette … · eyes … · hair … · skin … · medium …   (near: <library ID>, vocabulary only)
```
`[CANVAS-STYLE] EXT:<label>` = the same descriptors. Every character on this canvas inherits it.

Then write FACE / BODY / WARDROBE from the art.

## 2. Check

Real-person photo → refuse. Under-age read → ask to adultify (mature face, 1:7) or stop. Adultifying changes proportions/face maturity only — never the rendering.

## 3. Isolate (`ISO-1`, `ISO-2`)

**Preferred: edit, not redraw.** An edit keeps the pixels' rendering; a redraw re-interprets it.

Edit path (Grok edit · Tsubaki.3 NL edit · PixAI Reference Pro / Edit):
```
Remove the background, other people, props that are not worn, text and watermarks from reference 1.
Place the same character on a plain seamless light-grey studio backdrop.
Keep the character's face, hair, proportions, outfit, line quality, shading, palette and rendering exactly as they are. Change nothing else.
No speech bubbles, no text, no captions, no lettering, no watermark, no signature.
```

Redraw path (only when the source is cropped / not full body):
```
Reference 1 is the source art: take the subject AND the rendering style from it.
Match the reference's rendering exactly — same line weight, shading, palette, eye and hair rendering, skin finish and medium. Do not restyle, do not beautify, do not convert to another anime style.
The character's appearance must be determined entirely by the reference image. Do not redesign the hair, outfit or facial features.
[STYLE-SOURCE] [FACE] [BODY] [WARDROBE]
Isolate the single adult fictional character. Plain seamless light-grey studio backdrop, soft even light.
Full body, head to toe, feet in frame, front or mild contrapposto, character-sheet clarity.
2D illustration, not a photograph. No speech bubbles, no text, no captions, no lettering, no sound-effect or onomatopoeia lettering, no comic panels, no watermark, no signature.
```

## 4. Style-fidelity check (before the ISO is offered for approval)

Compare ISO with the original, axis by axis, and print:
```
fidelity: line ✓ · shading ✓ · palette ✗ (hair went pink, source ash-lavender) · eyes ✓ · hair ✓ · skin ✓ · medium ✓
```
- All ✓ → offer for approval.
- Any ✗ → **re-roll from the original** with the identical prompt (not from the drifted ISO). Max 2 re-rolls.
- Still ✗ → switch path (redraw → edit, or Grok → Tsubaki.3 reference slot / Reference Pro), or show the best one, name the axis, ask. Never "fix" by adding adjectives; never accept a prettier but different style.
- Also check identity (face, hair cut, eye colour, outfit) the same way.

## 5. Lock

On approval: print `[CANVAS-STYLE]`, `[STYLE-SOURCE]`, FACE / BODY / WARDROBE, `mode=ART`, `canvas=EXT:<label>`, note the anchor (`ANCHOR=ISO-1`). No LOOKS slots unless the user asks for "variants".

## 6. Reference contract (Grok max 3 refs; same logic on Tsubaki.3 / Reference Pro)

| Ref | Role | Mandatory sentence |
|---|---|---|
| 1 | Anchor (approved ISO; original if no ISO yet) — **subject + style, always** | "From reference 1 take the character and the rendering style. Match the reference's rendering exactly; do not restyle." |
| 2 | **EXT assets:** the original source art — **style anchor**, every frame | "From reference 2 take only the rendering style — line, shading, palette, skin and eye rendering — not the pose, background or composition." |
| 2/3 | pose / outfit / composition sketch (optional) | "From reference N take the pose only." (or outfit only) |
| 3 | setting / light mood (optional) | "From reference 3 take background and light direction only. Do not take line language, shading, palette, or face from reference 3." |

- Keep the original as Ref2 whenever a slot is free (if all 3 slots are needed, drop the setting ref first and describe the setting in text). `EXT:` covers both the user's own art and characters generated elsewhere.
- **Tsubaki.3:** put identity/style refs in the **reference slot of the prompt box** (`@image1`, `@image2`). Never put the character in the **base image** slot — it keeps pose/composition/palette/texture but **replaces the character** (PixAI Tsubaki.3 guide).
- Never use a generated frame as Ref1 or as the style ref (see `storyboard-consistency.md`).
- Drift → regenerate from Ref1; never add a fourth face.
- Seed: only where the engine exposes it (PixAI Tsubaki.2/1, Haruka); Grok has none — do not invent one.

## 7. New characters in an EXT canvas

New NPCs / `{{user}}` next to a registered asset are drawn in the asset's style:
```
From reference 1 take only the rendering style (line, shading, palette, skin and eye rendering). Do not take the face, hair, outfit or identity of the character in reference 1.
[CANVAS-STYLE] [ASSET:npc-01] …
```
Once approved, that NPC's own ISO becomes its anchor; the original stays the style anchor.

## 8. Later-frame template

```
From reference 1 take the character and the rendering style. Match the reference's rendering exactly; do not restyle.
[From reference 2 take only the rendering style — line, shading, palette, skin and eye rendering — not the pose, background or composition.]   (EXT)
[From reference 3 take background and light direction only. Do not take line language, shading, palette, or face from reference 3.]
[CANVAS-STYLE] [STYLE-SOURCE] [FACE] [BODY] [WARDROBE] [ASSET…]
A single illustration. Change only: <pose / camera / setting / garment state as requested>.
<shot type>, <angle>. <action + weight shift + secondary motion>.
2D illustration, not a photograph. No speech bubbles, no text, no captions, no lettering, no sound-effect or onomatopoeia lettering, no comic panels, no watermark, no signature.
```
