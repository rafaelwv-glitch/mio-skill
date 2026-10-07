# Changelog

## 2.2.1 — 2026-10-07
Fixes from a real test run (EXT asset + 4-frame greeting storyboard on Grok).
- **Identity colours separated from the style palette:** new `[IDENTITY-COLOURS]` lock per character (skin, hair, eyes; named + approx hex), re-injected verbatim every frame, never shortened; `[STYLE-SOURCE]`/`[CANVAS-STYLE]` keep only the rendering palette, so NPCs no longer drift toward the main character's colouring. Hair length as a measurable landmark in FACE.
- **Explicit fidelity/drift axes:** skin-tone, hair-colour, hair-length, eyes (colour/highlight layers), gloss, silhouette (must not get slimmer), counts. **Adultify allowance:** only face maturity and proportions toward the Hard Limits may change. **Fidelity ladder** F1–F5 (re-roll → emphasised locks → edit path → engine/slot switch → ask) and **drift ladder** R1–R5 (regen with IDENTITY-COLOURS emphasised once → reference-only edit of the anchor → targeted correction edit → remove the cause, e.g. warm light / crowded frame → deliver & report).
- **Rendering-fidelity tokens:** new `gloss` axis; glossy/PixAI-like sources must name gloss level, highlight shapes, gradient shading depth and eye highlight layers, plus an anti-flattening sentence. Short form `[STYLE-SOURCE·S]` for frames where the original rides along (prompts were reaching ~5,000 characters).
- **Unsuitable source poses:** sexualised/cropped/awkward source → pose edit of the original first ("change only the pose and background"), redraw only if that fails; check against the source with pose/background as the only allowed differences. ISO sheets use neutral white light.
- **Grok Bot GenerateImage (observed):** with reference images attached, requested 2:3/3:4 came back 16:9 (1280×720); compose for the delivered frame, two-view ISO sheet + crop, crop a face anchor (`ANCHOR-FACE`). Documented in `engines.md` as observed behaviour only.
- **`autopick=ON|OFF`** session flag in the state line: Mio writes missing locks itself and continues without waiting; OFF by default; never overrides Hard Limits, `bubbles=OFF` or user-stated facts.
- **Text props recipe** (`no-text.md` §6): signs, name boards, shirts, packets, screens rendered blank or with abstract unreadable marks; the words go in chat, never in the prompt (not even negated).
- Also: scene light must not recolour identity ("the light does not change her skin tone or hair colour"); counts locked as "exactly N"; `{{user}}` default gets an outfit; new **PARTIAL** asset class for half-described NPCs; image-vs-text rule for FACE (text-only traits become an Asset Check conflict); slot-to-beat mapping when a fixed number of images covers more beats; canonical NPC sentence for multi-person frames.

## 2.2 — 2026-10-07
- **Register as asset / external art:** 7-axis style read (line, shading, palette in named colours + approx hex, eyes, hair, skin, medium) into a new `[STYLE-SOURCE] EXT:<label>` lock; source style is kept, no fallback to MOE/CEL00/PAINT or any library default; isolate by **edit** first; reference always passed as subject + style with "Match the reference's rendering exactly; do not restyle."; style-fidelity check against the original before approval with a re-roll-from-original rule; the original rides along as style reference (Ref2) on later frames; Tsubaki.3 reference-slot vs base-image guidance. (`original-art.md`, `reference-pack.md`)
- **Storyboard anti-drift:** new `references/storyboard-consistency.md` — every frame re-anchors on the approved anchor image as Ref1; never a previous generated frame as identity/style reference; SET LOCK (anchor, style ref, canvas, engine, seed) fixed for the set; per-frame drift line (face, hair, eyes, palette, line, shading, outfit-state); regenerate from anchor, never patch with words.
- **No speech bubbles:** new Hard Limit + `references/no-text.md` — no bubbles, text, captions, SFX/onomatopoeia lettering or comic panels; verbatim NO-TEXT clause in every skeleton and template; PixAI negative tag list; bubble trigger-word list (manga page, comic panel, dialogue, quoted lines …); greeting speech becomes expression/gesture only; state-line flag `bubbles=OFF`, ON only by explicit user unlock for the session; strip "prominent sound effects" from PixAI's manga block.
- **Styles & flexibility:** the "only MOE/CEL00/PAINT defaults" rule is replaced by a **Fit Map** — with no style set, Mio proposes 2–3 fitting styles (one line each) and renders one look per style; fallback KEYVIS/PAINT/CEL00; still never switches a locked style silently. New engine house looks `HARUKA2`, `TSU2`, `TSU3`, `GPTANIME` ("ChatGPT anime", Ghibli-adjacent); new Pixiv styles `ATSUNURI`, `GLOSSREAL`, `SUISAI`, `FLATLINE`, `RIMLIGHT`, `YUMEKAWA`, `KUUKI`, `NEONPOP`, `BRUSHSOFT`; effect `+WARM`.
- **Canvas style / NPC consistency:** new `[CANVAS-STYLE]` lock — style of the first locked character (or registered asset) applies to every character on the canvas incl. `{{user}}`, NPCs and crowds; NPC locks never carry a style; own style per NPC only on explicit ask; mixed sources draw new NPCs in the asset's style (style-only reference); two assets in different styles → ask once, never blend. State line gains `canvas=`.
- **Engines (re-checked 2026-10-07):** Tsubaki.3 reference slots (prompt-box ref keeps the character; base image replaces it), multilingual prompts, official quality line, LoRA/negative/seed marked unverified; Tsubaki.2 Customize Style, preset count discrepancy, Ultimate/Ultra naming, no bracket weights on DiT; Haruka v2 verified defaults (28 steps, Euler a, CFG 5), only official Haruka base is v2, remove `simple background` from negatives for ISO sheets; other PixAI models listed; neutral `CHAR-A/B` labels and `character: original,` instead of `Mio-A` (PixAI's mascot is also named Mio).
- State line: `Mio 2.2 · lock · mode · canvas · bubbles · assets · beats · engine`.

## 2.1 — 2026-09-24
- **Reference Pack (`mode=PACK`):** intake 5–30 images of one fictional adult; bucket sort; majority consensus locks; conflict ask (never average); ISO + turnaround + 3×3 expression anchors; per-frame ≤3 ref selection; pack manifest re-inject. Detail: `references/reference-pack.md`.
- **ART vs PACK precedence:** PACK when ≥5 images of one character; ART when 1–4.
- **PixAI LoRA path:** `references/lora-pixai.md` (when to train, dataset rules, architecture table, trigger/caption, test grid, hard gate — no paid training without explicit user OK). Note: Tsubaki.3 LoRA support undocumented.
- **tools/lora-prep:** `prep.py` CLI (dedupe, resize, captions, manifest) + README + requirements.
- State line modes: `LOOKS|ART|PACK`. Never-list: average conflicting traits; start paid training without explicit OK.

## 2.0 — 2026-09-24
Standalone rewrite (split from the `grok-mio-skill` / bot-stack lineage, v1.9).
- Separated from bot-card tooling: no card/situation/world coupling, no owner data.
- Prime directives: concise + anti-drift (LOCK blocks verbatim, ask-don't-improvise, one change per retry).
- **Asset Gate:** one scan → LOCKED / DEFINED / MISSING / CROWD; asset IDs in the session registry; pronoun resolution; garment states as WARDROBE locks per beat; "you pick" needs confirm; one batched ask.
- **Engines:** Grok default + PixAI Tsubaki.3/2/1, Haruka v2, Hoshino, Reference Pro/Edit with per-engine syntax and params.
- **Style library:** 30+ styles with IDs; only MOE / CEL00 / PAINT are defaults.
- Original-art path and reference contract carried over from 1.9.
- Short state line: `Mio 2.0 · lock · mode · assets · beats · engine`.
- Greeting-recommended styles marked ★ (SEMIGLOSS, GAMECG).

Prior history (1.0–1.9): see the `grok-mio-skill` repository.
