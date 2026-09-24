# Changelog

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

Prior history (1.0–1.9): see the `grok-mio-skill` repository.
- Greeting-recommended styles marked ★ (SEMIGLOSS, GAMECG).
