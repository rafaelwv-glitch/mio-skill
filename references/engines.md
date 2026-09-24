# Engines — how Mio writes for each generator

Mio generates natively in **Grok Imagine** by default and also writes copy-ready prompts for **PixAI** engines. Pick the engine from the user's words ("for PixAI", "Tsubaki", "Haruka") or default `GROK`. Put it in the state line. LOCK blocks stay identical across engines; only the **syntax wrapper** changes.

Sources: PixAI Docs (models overview, Tsubaki.3 overview / templates / workflow, prompt basics & advanced, model parameters, editing models, LoRA basics; checked 2026-09-24), xAI Imagine docs, community prompt reviews. Where a doc gives no detail (e.g. Hoshino), this file says so instead of guessing.

## Quick pick

| Engine ID | Architecture | Prompt style | Best for | Reference image | Seed |
|---|---|---|---|---|---|
| `GROK` | Grok Imagine (Aurora) | Natural language | Default; native in chat/canvas | up to 3 (edit) | not exposed — use refs |
| `TSUBAKI3` | PixAI DiT, flagship (2026) | NL, English best | Consistency, design sheets, manga pages, lighting, text/layout | yes (ref-image generation + NL edit) | — |
| `TSUBAKI2` | PixAI DiT (Mar 2026) | NL | Multi-character, detail, 35+ style presets | no | yes |
| `TSUBAKI1` | PixAI DiT | NL | Fine prompt following, cheaper | yes | yes |
| `HARUKA` | PixAI SDXL (Haruka v2) | **Danbooru tags** | Classic anime, best hands/eyes, SDXL LoRA stacking | yes | yes |
| `HOSHINO2` | PixAI SDXL | tags | Retro anime look from short prompts | yes | yes |
| `HOSHINO1` | PixAI SDXL | tags | Mature, natural look; male characters; artist tags | yes | yes |
| `REFPRO` | PixAI editing model | NL instruction | Edit/compose from up to 10 images, 2K/4K | required | no |
| `PXEDIT` | PixAI conversational edit | NL, multi-round | Iterative fixes on one image | required | no |

## GROK (default)

- Write English natural-language paragraphs in skeleton order (SKILL §4). No weights, no tag soup.
- Consistency comes from **verbatim LOCK re-injection + reference images**, not seeds.
- Edit / multi-ref: up to **3** images. Always name roles: "From reference 1 take the subject and style. From reference 2 take the pose only. From reference 3 take background and light direction only."
- Agent/Canvas: prefer branching a node over a fresh text-only generation; drop the ISO sheet on the canvas as the anchor.
- Classifier notes: adult tokens first; avoid tripwords listed in `heat.md`; overflags are fixed by medium/crop/camera, not by removing clothing detail.

## TSUBAKI3 (PixAI flagship)

What it does well (PixAI docs): locks character features and art style to each other across a set; expression sheets, turnarounds, outfit sheets and pose collections in one image; directional, physically consistent lighting; full manga pages with panels, screentones and bubbles; typography and layout; photoreal *and* anime in one model (Mio keeps 2D); Color Palette control in the panel.

Prompt rules from the official workflow:
1. **English**, Prompt Helper **off** for precise control.
2. **Fixed order:** ① style & effects → ② one-sentence content summary → ③ character description (look, pose, position) → ④ text design (only if text) → ⑤ layout (bg, negative space).
3. **Name characters** when more than one: `Mio-A`, `Mio-B` … and give each its own paragraph with position ("dominates the center foreground", "behind on the upper-left").
4. Embedded text format: `title:「…」`, never label in the same language as the text.
5. Design sheets: `MANDATORY PAGE CONTENT:` then uppercase module labels (`TURNAROUND:`, `EXPRESSION GRID:`, `DETAIL GRID:`, `PALETTE:`). Flat style section for sheets.
6. Reuse the **character file** (Mio's LOCK blocks) untouched; swap only style and summary between images.
7. Manga: script first, check continuity, then prompt: style → summary → character → setting continuity → panel layout → panel content. Restate continuity (same outfit, same room, same time) on every page.

Reference-image generation (single ref is enough): turn into figure/plush, colour line art from a style ref, swap character into a base image (keeps composition/camera/light), outfit ref + character ref, pose ref + character ref, composition sketch + character ref, 4-panel manga from one ref, 2×2 mood studies, sticker sets, 3×3 expression sheet, front/side/back turnaround.

NL edit phrasing: say what to change **and** what to keep — "Change the @image1 character's hair from white to pale pink", "Replace the black top with a white shirt while keeping the bow, jacket, skirt and all other elements unchanged."

Official style blocks (copy as the ① style section; details in `styles.md`): flat colouring (design sheet), stronger linework, general manga monochrome, fine manga lines, cel anime screencap, realistic backgrounds, 3D-render look, ukiyo-e, GALGAME/visual-novel CG, pixel art, lighting/lens, detail richness, high-contrast chiaroscuro.

## TSUBAKI2

- NL prompts; formula Subject + Action + Scene (+ Mood + Style for polish).
- **Style presets** (35+) in the panel — same prompt, different preset. Mio names the intended look in text and may suggest a preset, but never relies on a preset name it has not seen.
- **Modes** Lite / Standard / Pro / Ultimate are different sub-models (texture differs, not just speed). Custom **negative prompts only in Pro/Ultimate**.
- Seed supported; no reference image; no sampler/CFG/steps.
- Multi-character: keeps characters distinct better than SDXL — still one paragraph per character.

## HARUKA (v2, SDXL)

- **Tag-based**, comma-separated Danbooru tags. Translate LOCK blocks into tags; keep order: quality → subject count → character tags → outfit → pose → camera → setting → light.
- Quality head (Illustrious-family convention): `masterpiece, best quality, very aesthetic, absurdres`.
- Subject: `1girl, solo, adult, mature female` (then features). For two: `1girl, 1boy`.
- Emphasis syntax: `(token:1.2)`; keep weights 1.1–1.4.
- LoRA: architecture must match (SDXL LoRA only). Copy the trigger word. Start at weight **0.7**; stacking → character ~0.8, style ~0.5. One LoRA to test, then add.
- Params: steps default 28; sampler Euler a (explore) or DPM++ 2M Karras (sharp); **CFG 5** balanced, 6–7 strict; fix seed to iterate; VAE PPPAnimix for clean anime.
- Reference strength: 0.1–0.3 keep, 0.3–0.5 style transfer, 0.5–0.7 sketch-to-finish.
- Negative (only terms not in the prompt): `lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, text, watermark, signature, blurry, worst quality, low quality, jpeg artifacts, photorealistic, 3d` + `child, loli, teen`.
- Tools: Face Fix, HiRes detail, Variation, Upscale available.

## HOSHINO v1 / v2 (SDXL)

PixAI docs only say: v2 = retro anime aesthetic from simple prompts; v1 = mature natural look, male characters, artist tags. Use HARUKA syntax. Mio does not use living-artist tags as a requirement.

## REFPRO / PXEDIT (editing)

- No LoRA, no negatives, no params — images + instruction only.
- REFPRO: up to 10 inputs, composition of several refs, 2K/4K, aspect 16:9 … 5:4. Good for ISO sheets, outfit swaps, panel rebuilds.
- PXEDIT: multi-round chat edits on one image; fix text/hands without rerolling.
- Instruction form: "[Change X] while keeping [face, hair, outfit, style, composition] unchanged."

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
| monochrome manga | `monochrome, greyscale, manga, screentones, lineart` |
