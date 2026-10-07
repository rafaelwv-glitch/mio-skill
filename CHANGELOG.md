# Changelog

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
