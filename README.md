# Mio — anime character & storyboard skill

Standalone skill for designing original anime characters, matching your own art, and storyboarding scenes as images. Runs natively in Grok Imagine (Agent/Canvas) and writes copy-ready prompts for PixAI engines (Tsubaki.3/2/1, Haruka v2, Hoshino, Reference Pro).

## What it does

- **Looks:** three default looks (soft moe, 2000s cel, painterly) → you pick → locked.
- **Your art:** extracts face/style, isolates the figure on a clean sheet, keeps later images on-model with a strict reference contract.
- **Style library:** 30+ anime/manga styles (90s cel, OVA, manhwa, manga monochrome, gacha, VN CG, cinematic sky, …) — used only when you ask.
- **Storyboards:** splits a greeting/scene into beats and **asks for any missing location, prop or NPC look** before drawing.
- **Anti-drift:** everything visual lives in LOCK blocks that are re-injected verbatim.

## Install

Copy the folder into your skills directory (e.g. `~/.grok/skills/mio/`) or upload `SKILL.md` (+ `references/`). Trigger with "Mio", "OC", "match this art", "storyboard this greeting", "90s style", etc.

## Layout

```
SKILL.md                  core ritual (short, authoritative)
references/engines.md     Grok + PixAI engines, syntax, params
references/styles.md      style library (IDs, tokens)
references/original-art.md ISO + reference contract
references/heat.md        in-bounds adult illustration + retry ladders
references/poses.md       pose pack
```

## Limits

Adult fictional characters only (25, 1:7). No real people. Adult content stays inside the platform's allowed lane; no filter-evasion.

MIT licensed.
