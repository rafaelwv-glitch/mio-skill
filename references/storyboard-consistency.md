# Storyboard consistency — multi-frame anti-drift, canvas style, NPCs

Applies to every set of ≥ 2 images of the same characters (greeting storyboards, scenes, expression runs, outfit runs).

## Why sets drift

1. **Compounding:** frame N is used as the reference for frame N+1, so small errors add up.
2. **Text-only frames:** the locks describe the character, but words alone let the engine re-interpret face and style each time.
3. **Patching with words:** "make her eyes bluer, sharper chin" pushes the image away from the anchor instead of back to it.
4. **Per-character styles:** an NPC described without the canvas style gets the engine's default look and pulls the main character with it.
5. **Long prompts that bury the locks:** scene detail outweighs identity.
6. **Scene light recolours identity:** warm lamp light or sunset pushes skin toward tan and hair toward darker brown; the next frame takes that as the new truth.
7. **Vague length words:** "long loose strands" lets the engine grow the hair a little more every frame.

## 1. Anchor rule (identity)

- The **anchor** is the approved image: `ISO-1` (ART/EXT), the picked LOOK, or `ANCHOR-ISO` / `ANCHOR-EXPR` (PACK).
- **Every frame** passes the anchor as **Ref1** ("From reference 1 take the character and the rendering style. Match the reference's rendering exactly; do not restyle.") **and** re-injects the text locks verbatim.
- **Never** use a previously generated frame as the identity or style reference. A previous frame may only serve as a *setting-only* Ref3 (with the no-style-steal sentence) when no location plate exists — prefer a location plate.
- Grok Canvas: branch every frame from the anchor node. Do not chain frame → frame.
- Tsubaki.3: anchor in the prompt-box reference slot (`@image1`); the base-image slot replaces the character and is only for pose/composition.

## 2. Fixed for the whole set

Print once at the start of the set and do not change mid-set:
```
SET LOCK · anchor=ISO-1 (+ ANCHOR-FACE) · style-ref=ISO-1 (+ original for EXT) · canvas=<ID> · identity=[IDENTITY-COLOURS] per character · engine=<ID> · seed=<fixed n | none> · slots=S1=b1–2 · S2=b3 · …
```
- `[CANVAS-STYLE]` text and the style reference image stay identical for every frame.
- Engine stays the same. Switching engine = new set, re-anchor first.
- PixAI engines with a seed (Haruka, Tsubaki.1, Tsubaki.2): keep a fixed seed while only camera/pose change; change the seed only as a deliberate re-roll. Grok has no seed.
- Keep the identity locks **early** in the prompt (skeleton order); scene detail comes after. `[IDENTITY-COLOURS]` is never shortened; `[STYLE-SOURCE]` may use its short form while the original is attached.
- **Identity sentence in the first attempt (EXT assets):** every frame — not only retries — carries, directly after the reference sentences: "Skin tone, hair colour, hair length, eye colour and body proportions exactly as in reference 1 and as listed in [IDENTITY-COLOURS]; the scene light does not change them." Light defaults to the R4 setup: neutral white key light on the characters, warm practical lamps only as background accents. (Test: without this, skin tanned in all four first attempts under warm interior light.)
- **ANCHOR-FACE as extra reference** whenever the face is medium-size or larger (medium shot, cowboy shot, bust, close-up): `Ref1=ISO-1 · Ref2=original · Ref3=ANCHOR-FACE` with "From reference 3 take only her face, hair colour and eye rendering." The setting ref is dropped first; describe the setting in text. Close-ups and bust shots may use `ANCHOR-FACE` as Ref1.
- **Wide shots protect the silhouette:** a small figure in a wide frame gets slimmed (test: the wide establishing frame lost the curvy build). Prefer a full shot where she fills ≥ ~half the frame height; if the beat needs a true wide shot, repeat the BODY lock in explicit proportion words ("soft curvy adult build with full hips and thighs, the same body proportions as reference 1, unchanged at this distance") — or split into an establishing plate plus a closer frame.
- **POV frames:** the viewer's visible arms/hands are `{{user}}` and wear the `{{user}}` wardrobe (default: heather-grey t-shirt sleeve, bare forearm). Write it into the frame: "the viewer's own forearm in a heather-grey t-shirt sleeve reaches in from the lower edge". (Test: an unlocked navy sleeve appeared.)
- **Counts** are locked as "exactly N" and repeated in the frame ("exactly two coffee cups", "exactly one display board"). They keep their position in every attempt — a retry never moves them to the back of the prompt.
- **Location locks** end with: "no other signs, boards, posters or written surfaces besides the locked ones". (Test: a retry invented a second, unlocked board with pseudo-text.)
- **Slot mapping:** fixed number of images but more beats → merge adjacent beats per slot, print the map once, keep the last beat in its own slot.

## 3. Drift checklist (after every frame)

Compare with the anchor, print one line under the frame:
```
drift: face ✓ · skin-tone ✓ · hair-colour ✓ · hair-length ✓ · eyes ✓ · gloss ✓ · silhouette ✓ · palette ✓ · line ✓ · shading ✓ · outfit-state ✓ · counts ✓
```
| Axis | Fail when |
|---|---|
| face | face shape, age read, nose/mouth style or marks differ |
| skin-tone | skin reads darker/lighter/more tanned than `[IDENTITY-COLOURS]` (judge in the lit areas, allowing for the scene light's tint on the *whole* image) |
| hair-colour | hue or value differs from `[IDENTITY-COLOURS]` (darker brown, redder, greyer) |
| hair-length | hair longer/shorter than the FACE landmark, cut or bangs changed |
| eyes | colour, shape, highlight layers or lash rendering differ |
| gloss | skin/hair/eye highlights flatter or matter than the anchor |
| silhouette | build or proportions differ (slimmer, taller, different bust/hip/waist read) |
| palette | rendering saturation/temperature shift from the canvas palette |
| line | weight, colour or taper differ from the anchor |
| shading | tone count, edge hardness or gradient use differ |
| outfit-state | garment, colour, or the beat's `[WARDROBE:…-state n]` differs |
| counts | number of locked items differs ("exactly two cups" → three) |

## 4. On drift — the ladder

One rung per retry; say which rung. "Identity axes" = face, skin-tone, hair-colour, hair-length, eyes, silhouette.

**Entry point by axis:**
- **skin-tone / hair-colour** (identity colours) on a frame with **one main figure** → start at **R2**. Hair colour did not recover with R1 in testing, and EXT frames already carry the R1 sentence from the first attempt.
- skin-tone / hair-colour with **several figures** in frame → R1 once (with ANCHOR-FACE as Ref3), then R3 (correction edit of the best frame) before R2.
- other identity axes (face, hair-length, eyes, silhouette) → R1, then R2. Silhouette in a wide shot → R4 (closer camera) first.

- **R1 — regen from anchor, identity emphasised (once):** same prompt, but move `[IDENTITY-COLOURS]` (and the failing FACE/BODY field) directly after the reference sentences, keep the identity sentence, add ANCHOR-FACE as Ref3 if the face is medium-size or larger. **Everything else keeps its position** — count locks ("exactly one board"), location lock and its no-other-signs clause, NO-TEXT clause. Re-check counts and text on the result: a retry that adds an object or lettering fails even if identity improved.
- **R2 — reference-only edit of the anchor:** stop generating fresh. Edit the anchor into the frame: "Using reference 1, change only the pose, camera and background to: <beat>. Keep skin tone, hair colour and length, eyes, body proportions, outfit and the exact rendering unchanged." (Grok edit / Tsubaki.3 NL edit with `@image1` / Reference Pro.) Best for single-character frames.
- **R3 — targeted correction edit:** keep the best frame as the base image and edit only the failing axis back, with the anchor as the identity reference: "Change only her hair colour and length (or skin tone) to match reference 1; keep everything else unchanged." The frame is the canvas being edited, never the identity reference.
- **R4 — remove the cause (one change):** neutral/cool key light instead of warm, closer camera, or fewer characters in frame (split a crowded beat into two frames). Then repeat R1.
- **R5 — deliver & report:** the best frame, the failing axis, and one offer (different camera, engine with a reference slot).

Style axes (gloss, line, shading, palette) and counts follow the same ladder from R1 (emphasise the `[STYLE-SOURCE]` field or the "exactly N" lock instead of identity).
- Never add patch words ("bluer eyes", "same face as before", "consistent character"). Emphasising an existing lock is allowed; new adjectives are not.
- Never accept a drifted frame as the new anchor.

## 5. Canvas style & NPC consistency

- `[CANVAS-STYLE]` = the style of the first locked character (or the registered EXT asset). It is printed with the locks and injected into **every** prompt of the canvas. It holds rendering only; skin/hair/eye colours live in each character's `[IDENTITY-COLOURS]` / `[ASSET]` lock, so NPCs never drift toward the main character's colouring.
- `{{user}}`, every NPC, every crowd **inherit** it. NPC `[ASSET:…]` locks describe looks only — never a style.
- An NPC gets its own style only on an explicit user request ("draw the ghost in watercolour"); then the block names both IDs and says which character uses which.
- **Mixed sources:** EXT asset in style X + new NPCs → canvas = `EXT:X`; new NPCs are generated in X with the original as **style-only** reference (sentence in `original-art.md` §7).
- NPC sentence for every multi-person frame: "Every other person is drawn in exactly the same rendering style; do not take the face, hair, skin tone, outfit or identity of the woman from reference 1 or reference 2 for anyone else."
- Half-described NPCs (**PARTIAL**: text gives age/hair/prop but no build/outfit): lock the given fields, ask only for the rest — or fill them under `autopick=ON`.
- Two EXT assets in different styles → one question: "Canvas style: A's or B's?" Never blend, never average.
- Recurring NPC → mini ISO in the canvas style, approved → that NPC's anchor for later frames (Ref2 when the NPC is in frame; the main anchor stays Ref1).
- Multi-character prompts: one paragraph per character with position; neutral labels `CHAR-A`, `CHAR-B` on PixAI; on Tsubaki-family prompts open with `character: original,` so the model does not recall an existing character (PixAI DiT convention).

## 6. Per-frame prompt (storyboard)

```
From reference 1 take the character and the rendering style. Match the reference's rendering exactly; do not restyle.
[EXT: From reference 2 take only the rendering style — line, shading, palette, skin and eye rendering — not the pose, background or composition.]
[Ref3 = ANCHOR-FACE when the face is medium-size or larger: From reference 3 take only her face, hair colour and eye rendering. — otherwise: From reference 3 take background and light direction only. Do not take line language, shading, palette, or face from reference 3.]
[Identity sentence (EXT): Skin tone, hair colour, hair length, eye colour and body proportions exactly as in reference 1 and as listed in [IDENTITY-COLOURS]; the scene light does not change them.]
[CANVAS-STYLE] [STYLE-SOURCE·S] 2D anime illustration of an original fictional adult, not a photograph.
A single illustration: <beat summary>, <crop>, <orientation — compose for the frame the engine actually delivers>.
[IDENTITY-COLOURS] [FACE] [BODY] [WARDROBE:<outfit>-<state n>] — <position>, <action + weight shift + secondary motion>, <expression; speech shown as expression only>.
[POV: the viewer's own forearm in the {{user}} sleeve …] [NPC sentence] [ASSET:…] (NPCs with their own colours, location + "no other signs, boards, posters or written surfaces besides the locked ones", props with "exactly N", text props blank) — neutral white key light on the characters, <warm accents, time>; the light does not change her skin tone or hair colour.
<shot type>, <angle>, <lens feel>.
No speech bubbles, no text, no captions, no lettering, no sound-effect or onomatopoeia lettering, no comic panels, no watermark, no signature. Correct hands, no extra limbs.
```
Under the frame: `refs: Ref1=ISO-1 · Ref2=original · Ref3=ANCHOR-FACE` (or setting plate), the drift line, and the ladder rung if a retry was needed.
