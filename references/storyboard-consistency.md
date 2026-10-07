# Storyboard consistency — multi-frame anti-drift, canvas style, NPCs

Applies to every set of ≥ 2 images of the same characters (greeting storyboards, scenes, expression runs, outfit runs).

## Why sets drift

1. **Compounding:** frame N is used as the reference for frame N+1, so small errors add up.
2. **Text-only frames:** the locks describe the character, but words alone let the engine re-interpret face and style each time.
3. **Patching with words:** "make her eyes bluer, sharper chin" pushes the image away from the anchor instead of back to it.
4. **Per-character styles:** an NPC described without the canvas style gets the engine's default look and pulls the main character with it.
5. **Long prompts that bury the locks:** scene detail outweighs identity.

## 1. Anchor rule (identity)

- The **anchor** is the approved image: `ISO-1` (ART/EXT), the picked LOOK, or `ANCHOR-ISO` / `ANCHOR-EXPR` (PACK).
- **Every frame** passes the anchor as **Ref1** ("From reference 1 take the character and the rendering style. Match the reference's rendering exactly; do not restyle.") **and** re-injects the text locks verbatim.
- **Never** use a previously generated frame as the identity or style reference. A previous frame may only serve as a *setting-only* Ref3 (with the no-style-steal sentence) when no location plate exists — prefer a location plate.
- Grok Canvas: branch every frame from the anchor node. Do not chain frame → frame.
- Tsubaki.3: anchor in the prompt-box reference slot (`@image1`); the base-image slot replaces the character and is only for pose/composition.

## 2. Fixed for the whole set

Print once at the start of the set and do not change mid-set:
```
SET LOCK · anchor=ISO-1 · style-ref=ISO-1 (+ original for EXT) · canvas=<ID> · engine=<ID> · seed=<fixed n | none>
```
- `[CANVAS-STYLE]` text and the style reference image stay identical for every frame.
- Engine stays the same. Switching engine = new set, re-anchor first.
- PixAI engines with a seed (Haruka, Tsubaki.1, Tsubaki.2): keep a fixed seed while only camera/pose change; change the seed only as a deliberate re-roll. Grok has no seed.
- Keep the identity locks **early** in the prompt (skeleton order); scene detail comes after.

## 3. Drift checklist (after every frame)

Compare with the anchor, print one line under the frame:
```
drift: face ✓ · hair ✓ · eyes ✓ · palette ✓ · line ✓ · shading ✓ · outfit-state ✓
```
| Axis | Fail when |
|---|---|
| face | face shape, age read, nose/mouth style or marks differ |
| hair | cut, length, bangs, colour or sheen type differ |
| eyes | colour, shape, highlight style or lash rendering differ |
| palette | hues/saturation/temperature shift from the canvas palette |
| line | weight, colour or taper differ from the anchor |
| shading | tone count, edge hardness or gradient use differ |
| outfit-state | garment, colour, or the beat's `[WARDROBE:…-state n]` differs |

## 4. On drift

1. Any ✗ → **regenerate from the anchor** with the **same prompt** (re-roll). Max 2.
2. Still ✗ → change exactly one thing that is not wording: camera distance (closer shots hold identity better), a cleaner pose, or the ref order. Say which.
3. Still ✗ → deliver the best frame, name the failing axis, offer a different camera or an engine with a reference slot.
- Never add patch words ("bluer eyes", "same face as before", "consistent character"). The lock already says it; the anchor carries it.
- Never accept a drifted frame as the new anchor.

## 5. Canvas style & NPC consistency

- `[CANVAS-STYLE]` = the style of the first locked character (or the registered EXT asset). It is printed with the locks and injected into **every** prompt of the canvas.
- `{{user}}`, every NPC, every crowd **inherit** it. NPC `[ASSET:…]` locks describe looks only — never a style.
- An NPC gets its own style only on an explicit user request ("draw the ghost in watercolour"); then the block names both IDs and says which character uses which.
- **Mixed sources:** EXT asset in style X + new NPCs → canvas = `EXT:X`; new NPCs are generated in X with the original as **style-only** reference (sentence in `original-art.md` §7).
- Two EXT assets in different styles → one question: "Canvas style: A's or B's?" Never blend, never average.
- Recurring NPC → mini ISO in the canvas style, approved → that NPC's anchor for later frames (Ref2 when the NPC is in frame; the main anchor stays Ref1).
- Multi-character prompts: one paragraph per character with position; neutral labels `CHAR-A`, `CHAR-B` on PixAI; on Tsubaki-family prompts open with `character: original,` so the model does not recall an existing character (PixAI DiT convention).

## 6. Per-frame prompt (storyboard)

```
From reference 1 take the character and the rendering style. Match the reference's rendering exactly; do not restyle.
[EXT: From reference 2 take only the rendering style — line, shading, palette, skin and eye rendering — not the pose, background or composition.]
[From reference 3 take background and light direction only. Do not take line language, shading, palette, or face from reference 3.]
[CANVAS-STYLE] 2D anime illustration of an original fictional adult, not a photograph.
A single illustration: <beat summary>, <crop>, <aspect>.
[FACE] [BODY] [WARDROBE:<outfit>-<state n>] — <position>, <action + weight shift + secondary motion>, <expression; speech shown as expression only>.
[ASSET:…] (NPCs in canvas style, location, props) — <light direction, time>.
<shot type>, <angle>, <lens feel>.
No speech bubbles, no text, no captions, no lettering, no sound-effect or onomatopoeia lettering, no comic panels, no watermark, no signature. Correct hands, no extra limbs.
```
Under the frame: `refs: Ref1=ISO-1 · Ref2=original · Ref3=bar-01 plate` and the drift line.
