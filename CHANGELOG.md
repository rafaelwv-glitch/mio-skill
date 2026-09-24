# Changelog

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
