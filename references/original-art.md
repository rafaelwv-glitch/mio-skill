# Original art & registered external assets → ISO → constant generation

Use when the user uploads their own art **or registers a character generated outside Mio** ("register as asset", "use this character", "keep this style"). 1–4 images. For ≥ 5 images use `reference-pack.md`.

**Core rule:** the source image is the style **and** identity authority. Mio describes it, isolates it and keeps it — Mio does **not** translate it into a Mio default style, a cleaner commercial look, or a slimmer figure. No fallback to MOE / CEL00 / PAINT or any other library ID for a registered asset.

## 1. Read the source (write before generating anything)

### 1a. Rendering → `[STYLE-SOURCE]` (HOW it is painted)

Read only what is visible. One value per axis, concrete words:

| Axis | What to write | Example |
|---|---|---|
| line | weight, variation, colour, closure | thin even dark-brown lines, slight taper, lines broken at highlights |
| shading | type, number of tones, edge, depth | soft airbrushed multi-step gradient over a two-tone base, soft edges, light ambient occlusion in folds |
| gloss | level (matte / satin / soft-gloss / high-gloss), highlight shapes and where they sit | soft-gloss skin, small soft oval specular highlights on cheekbones, nose tip, shoulders, knees; glossy sheen bands on hair crown |
| rendering palette | saturation, temperature, shadow colour, line colour — **not** skin/hair/eye colours | warm, moderately saturated; shadows warm rose-brown; lines dark brown |
| eyes | shape, iris layers, highlight count/shape, lash rendering, gloss | large round, 3-band gradient iris, one large white highlight + two small dots, glassy wet sheen, thick dark upper lash line with flicks |
| hair | strand grouping, sheen type, edge | medium clumps with flyaway wisps, angel-ring sheen band, soft airbrushed tips |
| skin | finish, blush, highlights | smooth soft-gloss finish, diffuse pink blush on cheeks |
| medium | digital/traditional, texture, finish | clean digital, soft semi-painterly finish, slight soft focus |

**Rendering-fidelity tokens (glossy / PixAI-like sources).** Engines — Grok in particular — pull redraws toward a clean, flat, matte commercial anime look. When the source shows any of these, name them explicitly and keep them in every prompt:
- **gloss level** and **highlight shape** for skin, hair and eyes ("soft-gloss skin with small soft oval specular highlights", "glassy multi-layer eye highlights", "angel-ring sheen band");
- **gradient shading** depth ("soft airbrushed multi-step gradients, not flat two-tone cel");
- **eye highlight layers** (count and shape) and iris gradient bands;
- **finish** ("soft semi-painterly finish, slight soft focus").
Add one anti-flattening sentence: "Keep the source's glossy highlights and soft gradient depth; not flat, not matte, not simplified."

Full block (used for ISO generation and whenever the original is **not** attached):
```
[STYLE-SOURCE] EXT:<label> — line … · shading … · gloss … · rendering palette … · eyes … · hair … · skin … · medium …   (near: <library ID>, vocabulary only)
```
**Short form** (frames where the original rides along as a reference — keeps prompts short; with every lock in full, storyboard prompts easily pass 4,500–5,500 characters):
```
[STYLE-SOURCE·S] EXT:<label> — <line 3 words>, <shading 4 words>, <gloss + highlight shape>, <eye highlight layers>, <finish>
```
`[CANVAS-STYLE] EXT:<label>` = the rendering descriptors only. Every character on this canvas inherits it.

### 1b. Identity colours → `[IDENTITY-COLOURS]` (WHAT colour this person is)

```
[IDENTITY-COLOURS] skin light warm ivory (~#F3DCCB, shadow ~#D9B8A6) · hair ash-lavender (~#B8A9C9, highlight ~#DCD2E6) · eyes teal (~#2F8F8A, upper band deep green)
```
- Named colour first, approx hex second (engines read words better than hex).
- One block per character; re-injected verbatim in every frame, never shortened.
- Never put these colours into `[STYLE-SOURCE]` / `[CANVAS-STYLE]` — otherwise NPCs drift toward the main character's colouring.

### 1c. FACE / BODY / WARDROBE

- Hair length as a **measurable** landmark ("hair tips at the shoulder blades", "side strands to the collarbone"), not "long".
- Body silhouette as seen (soft curvy / athletic / slim) — the redraw must not slim it.
- **Image vs text:** visible traits come from the image. Traits only in the user's/bot text that the image doesn't show (freckles, coloured streaks, scars) → list in the Asset Check as `CONFLICT text-only: …`; added only on confirmation.

## 2. Check & adultify allowance

Real-person photo → refuse. Under-age read → ask to adultify (mature face, 1:7) or stop.
**Allowed deviation when adultifying:** face maturity (defined jaw and cheekbones, slightly longer face) and body proportions toward 25 / 1:7 / head-to-hip > 1:3.5. **Nothing else changes:** identity colours, hair cut and length, eye colour, iris layers, highlight style and gloss, skin finish, build/silhouette, outfit and rendering stay as in the source. A mature face is not a licence for "smaller, flatter eyes" or a slimmer body.

## 3. Isolate (`ISO-1`, `ISO-2`)

**Preferred: edit, not redraw.** An edit keeps the pixels' rendering; a redraw re-interprets it.

Edit path (Grok edit · Tsubaki.3 NL edit · PixAI Reference Pro / Edit):
```
Remove the background, other people, props that are not worn, text and watermarks from reference 1.
Place the same character on a plain seamless light-grey studio backdrop.
Keep the character's face, hair colour and length, skin tone, eye colour and rendering, body proportions, outfit, line quality, shading, gloss and palette exactly as they are. Change nothing else.
No speech bubbles, no text, no captions, no lettering, no watermark, no signature.
```

**Unsuitable source pose** (sexualised, cropped, foreshortened, partly hidden, awkward): the ISO must be a neutral standing sheet, but identity and rendering still come from the source. Order:
1. **Pose edit** of the original: "Using reference 1, change only the pose to a neutral relaxed standing pose, full body, head to toe, and the background to plain light grey. Keep face, hair colour and length, skin tone, eyes, body proportions, outfit and the exact rendering — line, shading, gloss, palette — unchanged."
2. Only if the edit fails twice: **redraw** with the source as subject + style reference and "take the character and rendering from reference 1, **not its pose, camera angle or background**" (template below), plus the full `[STYLE-SOURCE]` and `[IDENTITY-COLOURS]`.
3. Either way, run the §4 check against the source; pose and background are the only allowed differences (plus the adultify allowance).

Redraw path (cropped source or failed edit):
```
Reference 1 is the source art: take the subject AND the rendering style from it, not its pose, camera angle or background.
Match the reference's rendering exactly — same line weight, shading, gloss and highlight shapes, eye and hair rendering, skin finish and medium. Do not restyle, do not beautify, do not convert to another anime style. Keep the source's glossy highlights and soft gradient depth; not flat, not matte, not simplified.
The character's appearance must be determined entirely by the reference image. Do not redesign the hair, outfit, facial features or body shape.
[STYLE-SOURCE] [IDENTITY-COLOURS] [FACE] [BODY] [WARDROBE]
Isolate the single adult fictional character. Plain seamless light-grey studio backdrop, neutral even white light.
Full body, head to toe, feet in frame, front or mild contrapposto, character-sheet clarity, the figure filling the frame height.
2D illustration, not a photograph. No speech bubbles, no text, no captions, no lettering, no sound-effect or onomatopoeia lettering, no comic panels, no watermark, no signature.
```
Use **neutral white light** for ISO sheets — warm or coloured light shifts skin and hair and the shift then propagates through every frame.
If the engine delivers landscape only (see `engines.md` → Grok Bot runtime), compose a two-view sheet: full body front on the left, bust close-up on the right, same character, no labels — then crop into `ISO-1` (full body) and `ANCHOR-FACE` (bust). The face anchor carries the eye and skin rendering at usable resolution. **Confirmed in testing:** the two-view sheet plus crop gives a usable ISO and ANCHOR-FACE.

## 4. Style- & identity-fidelity check (before the ISO is offered for approval)

Compare ISO with the original, axis by axis, and print:
```
fidelity: line ✓ · shading ✗ (flatter, less airbrush depth) · gloss ✗ (matte skin) · palette ✓ · skin-tone ✓ · hair-colour ✓ · hair-length ✓ · eyes ✗ (fewer highlight layers) · silhouette ✗ (slimmer) · medium ✓
```
Axes: line · shading · gloss · palette · skin-tone · hair-colour · hair-length · eyes (colour, highlight layers, lash rendering) · silhouette (build and proportions; must not get slimmer) · medium. Allowed differences: pose, background, adultify allowance (§2).

**Fidelity ladder** (one rung per retry; say which rung):
**Entry by axis:** identity axes (skin-tone, hair-colour, hair-length, eyes, silhouette) **skip F1 and start at F2** — an identical re-roll made identity worse in testing (skin tanned, hair shorter). Style axes start at F1. **Gloss on Grok** usually stops at satin: after F2, go to F4 if real PixAI-level gloss matters, or accept satin and say so (`engines.md` → Grok Bot runtime).

- **F1** re-roll from the original, identical prompt (style axes only).
- **F2** re-roll once with the failing locks moved directly after the reference sentences and emphasised: "Skin tone, hair colour and length, eye rendering, gloss and body proportions exactly as in reference 1 — [IDENTITY-COLOURS] [STYLE-SOURCE gloss/shading fields]." (re-stating locks, not new adjectives)
- **F3** switch to the **edit path** (§3) — edit the original instead of generating.
- **F4** switch engine/slot: Tsubaki.3 prompt-box reference (`@image1`) or Reference Pro edit — the only rung that reliably reaches true PixAI-style gloss.
- **F5** show the best attempt, name the failing axes, ask.
Never accept a prettier but different style, a matte version of a glossy source, or a slimmer figure.

## 5. Lock

On approval: print `[CANVAS-STYLE]`, `[STYLE-SOURCE]`, `[IDENTITY-COLOURS]`, FACE / BODY / WARDROBE, `mode=ART`, `canvas=EXT:<label>`, note the anchors (`ANCHOR=ISO-1`, optional `ANCHOR-FACE`). No LOOKS slots unless the user asks for "variants".

## 6. Reference contract (Grok max 3 refs; same logic on Tsubaki.3 / Reference Pro)

| Ref | Role | Mandatory sentence |
|---|---|---|
| 1 | Anchor (approved ISO; `ANCHOR-FACE` for close-ups; original if no ISO yet) — **subject + style, always** | "From reference 1 take the character and the rendering style. Match the reference's rendering exactly; do not restyle." |
| 2 | **EXT assets:** the original source art — **style anchor**, every frame | "From reference 2 take only the rendering style — line, shading, gloss, palette, skin and eye rendering — not the pose, background or composition." |
| 2/3 | pose / outfit / composition sketch (optional) | "From reference N take the pose only." (or outfit only) |
| 3 | **`ANCHOR-FACE` whenever the face is medium-size or larger** (medium, cowboy, bust, close-up) | "From reference 3 take only her face, hair colour and eye rendering." |
| 3 | otherwise: setting / light mood (optional) | "From reference 3 take background and light direction only. Do not take line language, shading, palette, or face from reference 3." |

- Keep the original as Ref2 whenever a slot is free; drop the setting ref first (describe the setting in text) so ANCHOR-FACE and the original both fit. `EXT:` covers both the user's own art and characters generated elsewhere.
- **Tsubaki.3:** put identity/style refs in the **reference slot of the prompt box** (`@image1`, `@image2`). Never put the character in the **base image** slot — it keeps pose/composition/palette/texture but **replaces the character** (PixAI Tsubaki.3 guide).
- Never use a generated frame as Ref1 or as the style ref (see `storyboard-consistency.md`).
- Seed: only where the engine exposes it (PixAI Tsubaki.2/1, Haruka); Grok has none — do not invent one.

## 7. New characters in an EXT canvas

New NPCs / `{{user}}` next to a registered asset are drawn in the asset's rendering, with their **own** identity colours:
```
Every other person is drawn in exactly the same rendering style; do not take the face, hair, skin tone, outfit or identity of the woman from reference 1 or reference 2 for anyone else.
[CANVAS-STYLE] [ASSET:npc-01] (with its own skin/hair/eye colours) …
```
Once approved, that NPC's own ISO becomes its anchor; the original stays the style anchor.

## 8. Later-frame template

```
From reference 1 take the character and the rendering style. Match the reference's rendering exactly; do not restyle.
[From reference 2 take only the rendering style — line, shading, gloss, palette, skin and eye rendering — not the pose, background or composition.]   (EXT)
[From reference 3 take only her face, hair colour and eye rendering.]   (ANCHOR-FACE, face medium-size or larger; else the setting sentence)
Skin tone, hair colour, hair length, eye colour and body proportions exactly as in reference 1 and as listed in [IDENTITY-COLOURS]; the scene light does not change them.   (EXT: first attempt, every frame)
[CANVAS-STYLE] [STYLE-SOURCE·S] [IDENTITY-COLOURS] [FACE] [BODY] [WARDROBE] [ASSET…]
A single illustration. Change only: <pose / camera / setting / garment state as requested>.
<shot type>, <angle>. <action + weight shift + secondary motion>.
<location lock> — no other signs, boards, posters or written surfaces besides the locked ones.
Neutral white key light on the characters, <warm accents>; the light does not change her skin tone or hair colour.
2D illustration, not a photograph. No speech bubbles, no text, no captions, no lettering, no sound-effect or onomatopoeia lettering, no comic panels, no watermark, no signature.
```
