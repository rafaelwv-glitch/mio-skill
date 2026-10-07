# Engines — how Mio writes for each generator

Mio generates natively in **Grok Imagine** by default and also writes copy-ready prompts for **PixAI** engines. Pick the engine from the user's words ("for PixAI", "Tsubaki", "Haruka") or default `GROK`. Put it in the state line. LOCK blocks stay identical across engines; only the **syntax wrapper** changes. The NO-TEXT clause (`no-text.md`) is in every prompt on every engine while `bubbles=OFF`.

Sources (checked 2026-10-07): PixAI Docs — Tsubaki.3 overview, Tsubaki.3 Prompt Templates, Tsubaki.3 Prompts in Action, Other PixAI Models (parameter table), Prompt Basics, LoRA Basics; PixAI blog — Tsubaki.3 Prompt Guide, "Which PixAI model should you use?", DiT Model Prompt Writing Guide (community author); PixAI model pages (Haruka v2, Tsubaki.2); PixAI API model list; xAI Imagine docs. Where a source gives no detail, this file says so instead of guessing. **(unverified)** marks facts not confirmed by an official PixAI page.

## Quick pick

| Engine ID | Architecture | Prompt style | Best for | Reference image | Negative field | Seed |
|---|---|---|---|---|---|---|
| `GROK` | Grok Imagine | Natural language | Default; native in chat/canvas | up to 3 (edit) | no — inline NO-TEXT clause | not exposed — use refs |
| `TSUBAKI3` | PixAI DiT, flagship | NL (any language; keep technical terms in English) | Consistency sets, EXT assets via reference slot, any style, design sheets, lighting | yes — prompt-box ref (`@image1`) + base image | not documented (unverified) — inline clause | not documented |
| `TSUBAKI2` | PixAI DiT (Mar 2026) | NL | Multi-character, glossy house look, style presets | **no** | Pro/Ultimate only | yes |
| `TSUBAKI1` | PixAI DiT | NL | Fine prompt following, cheaper | yes | yes | yes |
| `HARUKA` | PixAI SDXL (Haruka v2) | **Danbooru tags** | Classic anime, best hands/eyes, SDXL LoRA stacking | yes | yes | yes |
| `HOSHINO2` | PixAI SDXL | tags | Single character from short prompts; sharper, more mature; retro-leaning | yes | yes | yes |
| `HOSHINO1` | PixAI SDXL | tags | Mature natural look; male characters | yes | yes | yes |
| `REFPRO` | PixAI editing model (DiT) | NL instruction | Edit/compose from up to 10 images, 2K/4K | required | no | no |
| `PXEDIT` | PixAI conversational edit | NL, multi-round | Iterative fixes on one image | required | no | no |

Other PixAI models named in PixAI's 2026 guide (Mio uses them only when asked): Otome v2 (soft, low-saturation romantic; male subjects), Serin (DiT, Korean webtoon look), Tsubaki Flash (lowest cost DiT), Nagi / Crystalize / Eternal (SDXL, clean cooler palette).

**Name clash:** PixAI's mascot and its "Mio.2" assistant are also called Mio, and Tsubaki.2 can recall PixAI characters by name (`character: mio_(pixai)`). Never write "Mio" (or `Mio-A`) in a PixAI prompt; use `CHAR-A`, `CHAR-B`, and open DiT prompts with `character: original,`.

## GROK (default)

- English natural-language paragraphs in skeleton order (SKILL §4). No weights, no tag soup.
- Consistency comes from **verbatim LOCK re-injection + the anchor as reference**, not seeds.
- Edit / multi-ref: up to **3** images. Always name roles: "From reference 1 take the character and the rendering style. Match the reference's rendering exactly; do not restyle. From reference 2 take … only."
- Agent/Canvas: branch every storyboard frame from the **anchor node** (ISO), never from the previous frame. Drop the ISO sheet (and, for EXT assets, the original) on the canvas.
- Isolating an EXT asset: use **edit** ("remove the background, keep everything else unchanged") before trying a redraw; unsuitable source pose → pose edit first (`original-art.md` §3).
- Grok tends to pull redraws toward a clean, flat, matte commercial anime look and slimmer figures (observed in the same test): for glossy sources always send the rendering-fidelity tokens and `[IDENTITY-COLOURS]` (`original-art.md` §1).
- Classifier notes: adult tokens first; avoid tripwords in `heat.md`; overflags are fixed by medium/crop/camera, not by removing clothing detail.

## Grok Bot runtime — GenerateImage tool (observed behaviour)

Observed in one Mio 2.2 test run (2026-10-07, 7 images): when `reference_image_paths` were attached, the GenerateImage tool **ignored the requested `aspect_ratio`** — jobs requested as 2:3 and 3:4 all came back **16:9 (1280×720)**. Only this case was observed; whether it holds without references, for other ratios or after tool updates is untested.

Workaround until confirmed otherwise:
- State crop and orientation **in the prompt** as well ("vertical composition, full body, head to toe") — but **compose for the frame actually delivered**: assume 16:9 when references are attached.
- Single-figure portraits/ISO in 16:9: either a two-view sheet (full body left, bust close-up right, no labels) or a figure that fills the frame height; then **crop afterwards** to the wanted ratio (a crop does not touch the rendering).
- Do not let a small figure in a wide frame become the anchor: crop a face/bust anchor (`ANCHOR-FACE`) so eye and skin rendering keep enough pixels.
- Report the delivered ratio under the frame if it differs from the request.

## TSUBAKI3 (PixAI flagship)

What it does well (PixAI docs): locks character features and art style to each other across a set; expression sheets, turnarounds, outfit sheets, pose collections in one image; directional, physically consistent lighting; very wide style range (flat sketch to impasto to photoreal — Mio keeps 2D); Color Palette control in the panel; native 2K. It also draws full manga pages **with panels, speech bubbles and text** and readable typography — which is exactly why the NO-TEXT rules matter here.

Prompt rules (official guide + workflow):
1. Write a **description**, not tags. Order: subject → details (wearing/doing/expression) → framing & camera → light (direction, colour, hardness, **source object**) → style. The workflow page uses ① style & effects → ② one-sentence summary → ③ characters → ④ text design → ⑤ layout; Mio **skips ④** while `bubbles=OFF`.
2. Language: Japanese/Korean/Chinese work directly (official guide); keep technical terms (`rim light`, `bokeh`, `wide-angle`) in English. Mio writes English. Prompt Helper **off** for precise control.
3. Multiple characters: one paragraph each with position ("dominates the centre foreground", "behind on the upper-left"); neutral labels `CHAR-A`, `CHAR-B`.
4. Style = components: line · colour application · palette · surface; write the one or two the style cannot do without; on far jumps add what you don't want ("no smooth gradients").
5. **Reference slots:**
   - **Prompt-box reference** (`@image1`, `@image2` …) — keeps the character and edits/places it. Use for anchors, EXT originals, outfit refs. Add: "The character's appearance must be determined entirely by the reference image. Do not redesign the hair, outfit, or facial features."
   - **Base image** (right panel) — borrows pose / placement / mood or palette / texture and **replaces everything else, including the character**. Never put an identity anchor here.
6. NL edits: say what changes **and** what stays, naming objects ("keeping the navy ribbon bow at her collar … unchanged").
7. Design sheets: `MANDATORY PAGE CONTENT:` + uppercase modules (`TURNAROUND:`, `EXPRESSION GRID:`, `DETAIL GRID:`, `PALETTE:`) — for Mio sheets add "no labels, no text, no panel borders".
8. Official quality line used in PixAI's own prompts, good to append: "consistent face, hairstyle and costume, correct anatomy, natural hands and feet, no duplicated limbs, no random outfit changes, no watermark, no signature, no text."
- Reference-image generation from one ref: figure/plush, colour line art from a style ref, swap character into a base image, outfit ref + character ref, pose ref + character ref, composition sketch + character ref, mood studies, turnaround, 3×3 expression sheet. (Four-panel manga and sticker sets also exist — not used while `bubbles=OFF`.)
- Official style blocks: see `styles.md` → `TSU3`. Strip "prominent sound effects" from the manga block.
- LoRA: PixAI's LoRA training docs list SD1.5 / SDXL / DiT.1 / DiT.2 only; the Tsubaki.3 FAQ mentions LoRAs/Recipes and some user LoRA pages carry a "DiT.3" tag → **Tsubaki.3 LoRA support unverified**; don't promise it. Negative-prompt field, seed, steps for Tsubaki.3: **not documented** — Mio writes negatives inline.

## TSUBAKI2

- NL; formula Subject + Action + Scene (+ appearance, light, camera, style preset). Tags work but are unstable with Prompt Helper off.
- **Style presets** (35+ per docs; count varies by page) + **Customize Style** field (Tsubaki.2 only) for style words. House look: `styles.md` → `TSU2`.
- **Modes** Lite / Standard / Pro / Ultimate (some pages: "Ultra") are different sub-models, not just speed. Custom **negative prompts only in Pro/Ultimate** (Standard uses the system default).
- Seed supported; **no reference image**; no sampler/CFG/steps (official parameter table). Bracket weights `(x:1.2)` are not recognized on DiT (community guide) — emphasize by moving the phrase earlier.
- Multi-character: keeps characters distinct better than SDXL — still one paragraph per character.
- Because there is no reference image, Tsubaki.2 cannot hold an EXT asset's style by reference — prefer `TSUBAKI3` / `REFPRO` / `GROK` for registered assets, or a DiT.2 LoRA.

## HARUKA (v2, SDXL)

- Only official Haruka base model as of 2026-10 (PixAI docs + API model list). "Haruka … v3/.3" items on PixAI are user LoRAs.
- **Tag-based**, comma-separated Danbooru tags. Order: quality → subject count → character tags → outfit → pose → camera → setting → light.
- Quality head (Illustrious-family convention, community): `masterpiece, best quality, very aesthetic, absurdres`.
- Subject: `1girl, solo, adult, mature female` (then features). For two: `1girl, 1boy`.
- Emphasis syntax: `(token:1.2)`; keep weights 1.1–1.4.
- **Model-page defaults (verified):** steps **28**, sampler **Euler a**, CFG **5**. Allowed samplers (API): Euler a, Euler, LMS, Heun, DPM2 Karras, DPM2 a Karras, DDIM, DPM++ 2M Karras, DPM++ 2S a Karras, DPM++ SDE Karras, DPM++ 2M SDE Karras, Restart. CFG 6–7 for stricter following and VAE PPPAnimix are community advice **(unverified)**.
- Default negative on the model page already contains `text, artist name, signature, watermark, username` — and also `simple background`: **remove `simple background` for ISO sheets** (Mio wants a plain backdrop). Mio's negative: `lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, worst quality, low quality, jpeg artifacts, photorealistic, 3d, blurry` + `child, loli, teen` + the NO-TEXT tag list (`no-text.md`).
- LoRA: SDXL only. Copy the trigger word. PixAI default weight **0.7**; stacking → character ~0.8, style ~0.5. One LoRA to test, then add.
- Reference strength: 0.1–0.3 keep, 0.3–0.5 style transfer, 0.5–0.7 sketch-to-finish **(community guidance, unverified)**. For EXT assets stay at the low end so the source rendering survives.
- Tools: Face Fix, HiRes detail, Variation, Upscale available.

## HOSHINO v1 / v2 (SDXL)

PixAI docs: v2 = retro anime aesthetic from simple prompts ("a highly popular style in Japan", API list; "sharper features, more mature", blog); v1 = mature natural look, male characters, artist tags. Use HARUKA syntax. Mio does not use living-artist tags as a requirement.

## REFPRO / PXEDIT (editing)

- No LoRA, no negatives, no params — images + instruction only.
- REFPRO: up to 10 inputs, composition of several refs, 2K/4K, aspect 16:9, 9:16, 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4. Best tool for EXT isolation and outfit swaps without restyling.
- PXEDIT: multi-round chat edits on one image; fix hands or remove stray lettering without rerolling.
- Instruction form: "[Change X] while keeping [face, hair, outfit, rendering style, composition] unchanged." No text in the instruction except the NO-TEXT clause.

## Tag translation cheatsheet (NL → Haruka tags)

| NL (lock) | Tags |
|---|---|
| adult woman, 25, mature face | `1girl, solo, adult, mature female, mature face` |
| full body head to toe, feet in frame | `full body, standing, feet visible` |
| cowboy shot | `cowboy shot` |
| three-quarter view looking back | `from side, looking back, three-quarter view` |
| low angle | `from below` |
| clean delicate linework, painterly | `delicate lineart, painterly, soft shading, gradient` |
| 2000s TV cel | `anime screencap, anime coloring, cel shading, 2000s (style)` |
| 90s retro | `1990s (style), retro artstyle, anime screencap, film grain` |
| monochrome manga rendering | `monochrome, greyscale, screentones, lineart` (not `comic`, not `manga page`) |
| speaking (expression only) | `open mouth, :o` / `smile, open mouth` — never `speech bubble` |

## LoRA (PixAI only)

Train/use path: `references/lora-pixai.md`. Dataset CLI: `tools/lora-prep/`. Architecture must match (SDXL LoRA → HARUKA/HOSHINO; DiT.2 → TSUBAKI2). Tsubaki.3 LoRA: unverified — use Pack/ART refs on TSUBAKI3. Mio prepares datasets and waits for **explicit user OK** before any paid training.
