# Original art → ISO → constant generation

Use when the user uploads or drops their own art and wants it matched.

## Steps

1. **Read, don't generate yet.** Write FACE / BODY / STYLE / WARDROBE from the art. STYLE = nearest ID from `styles.md` + 4–6 tokens you can *see* (line weight, shading type, palette, skin finish, eye rendering).
2. **Check.** Real-person photo → refuse. Under-age read → ask to adultify (mature face, 1:7) or stop.
3. **Isolate** (1–2 images, `ISO-1`, `ISO-2`):

```
Reference 1 is the user's original art: take the subject and the rendering style from it.
Isolate the single adult fictional character from reference 1. Remove background, other people, props that are not worn, text, watermarks.
Plain seamless studio backdrop, soft even light, light grey.
[FACE] [BODY] [WARDROBE] [STYLE]
Full body, head to toe, feet in frame, front or mild contrapposto, character-sheet clarity.
Keep the exact face, hair, proportions, outfit, line quality, shading and palette of reference 1.
2D illustration, not a photograph. No text.
```

4. **Lock** on approval: print blocks, `mode=ART`, note which ISO is the anchor. No three-slot looks unless the user asks for "variants".

## Reference contract (Grok max 3 refs; same logic on Tsubaki.3 / RefPro)

| Ref | Role | Mandatory sentence |
|---|---|---|
| 1 | ISO (or original if no ISO yet) — **subject + style, always** | "From reference 1 take the character and the rendering style." |
| 2 | pose / outfit / composition sketch (optional) | "From reference 2 take the pose only." (or outfit only) |
| 3 | setting / light mood (optional) | "From reference 3 take background and light direction only. Do not take line language, shading, palette, or face from reference 3." |

- Prefer the ISO over the original as Ref1 (cleaner subject). The original stays on the canvas as source of truth, not as a second style ref.
- LOCK blocks go into the same prompt as the reference sentences.
- Drift → regenerate from Ref1; never add a fourth face.
- Seed: use only if the engine exposes it (PixAI Tsubaki.2/1, Haruka); Grok has none — do not invent one.

## Later-frame template

```
From reference 1 take the character and the rendering style.
[From reference 2 take the pose only.]
[From reference 3 take background and light direction only. Do not take line language, shading, palette, or face from reference 3.]
[STYLE] [FACE] [BODY] [WARDROBE] [ASSET…]
Change only: <pose / camera / setting / garment state as requested>.
<shot type>, <angle>. <action + weight shift + secondary motion>.
2D illustration, not a photograph. No text, no watermark.
```
