# PixAI LoRA pipeline — dataset prep automated; training only after explicit OK

Mio **prepares** datasets and prompts. Mio **never starts paid training itself**. Training runs only after the user says explicitly (e.g. "train it", "OK start training", "spend the credits").

Sources: PixAI Docs — LoRA usage / train-your-own, model parameters, credit costs; DiT LoRA training guide (2026). Checked 2026-09-24.

## When to train

- Recurring fictional adult character the user will reuse across many generations/engines.
- Recommended curated set: **15–40** images (PixAI minimum **10**). More varied angles beat more near-duplicates.
- Prefer after a Reference Pack consensus lock (`reference-pack.md`) so identity is already decided.
- Skip LoRA when a 3-ref Pack/ART path is enough for a one-off scene.

## Dataset rules

- **Same subject**, adults only (25, 1:7 presentation). No real-person photos.
- Variety: face close-ups, full body, profile/back, several expressions, several outfits, clean backgrounds mixed with simple scenes.
- Consistent identity (hair/eyes/face). Conflicts resolved before training (ask; never average).
- **No** watermarks, burned-in text, other people, logos, heavy meme overlays.
- Prefer PNG after prep; longest side ≥ 512 (1024 recommended for SDXL/DiT).
- Prep helper: `tools/lora-prep/prep.py` (dedupe, resize, captions, manifest).

## Architecture choice

A LoRA **only works on the matching architecture**.

| Architecture | Train target (examples) | Generate with (Mio engine ID) | Notes |
|---|---|---|---|
| SD 1.5 | Moonbeam etc. | legacy SD1.5 models | cheapest; weaker modern anime |
| SDXL | Haruka v2, Hoshino | `HARUKA` / `HOSHINO*` | classic anime; tag prompts; best hands/eyes stack |
| DiT.1 | Tsubaki (DiT.1) | `TSUBAKI1` family | NL prompts; shorter triggers OK per DiT.1 guidance |
| DiT.2 | Tsubaki.2 | `TSUBAKI2` | NL; trigger **≥ 30 characters** recommended |
| *(Tsubaki.3)* | — | `TSUBAKI3` | **Tsubaki.3 LoRA support is not documented** as of 2026-09 — do not promise a T3 LoRA; use Pack refs / RefPro on T3, or train DiT.2 for Tsubaki.2 |

Pick from the user's target engine. Default recommendation for new anime OCs: **SDXL → Haruka** (flexible + LoRA ecosystem) or **DiT.2 → Tsubaki.2** (NL + consistency). Say the credit cost band when offering (docs: SD1.5 lowest → SDXL → DiT.1 → DiT.2 highest; dataset-reuse retrain may discount — cite current PixAI pricing page, don't invent numbers in-chat if unsure).

Category: **character** (identity) or **style** (rendering). One LoRA, one category.

## Trigger-word recipe

- Description **≥ 30 characters** (PixAI docs; especially DiT.2).
- Pattern: `name-like-token, permanent appearance traits` — hair length/colour/cut, eye colour/shape, face marks, signature accessories that **always** stay.
- **Do not** put variable pose, background, or outfit into the trigger (those go in captions / per-prompt).
- Example shape: `mioa01 adult woman, long silver hair, blunt bangs, red eyes, beauty mark left cheek` (≥ 30 chars, fictional token, no real names).

## Caption strategy

Per-image `.txt` beside each training image:

```
<trigger>, <variable hints>
```

- Fold **identity** into the trigger (same on every file).
- Caption what should stay **VARIABLE**: pose, camera, background, outfit, expression, lighting.
- Filename hints help (`face_*`, `full_*`, `back_*`, `outfitcasual_*`) — prep.py derives short hints from these.
- Avoid repeating identity traits in every caption (reduces flexibility).

## Prep → user OK → train (hard gate)

1. Mio / `prep.py` builds `OUTPUT_DIR` (PNG + `.txt` + `manifest.csv` + summary).
2. Mio prints: image count kept/dropped, architecture recommendation, trigger, estimated "credits will be charged by PixAI", and asks:
   `Train on PixAI now? Reply YES to proceed — I will not start training without that.`
3. On **YES** (or clear equivalent): give the user the browser path — PixAI → **Models → Train your own LoRA** — with architecture, category, trigger, and dataset folder ready. Mio does **not** click Start Training or spend credits itself.
4. On anything else: stop. Keep the dataset for later.

## Post-training test protocol

Fixed-seed grid (engine that matches the LoRA):

| Weight | Prompts (4) |
|---|---|
| 0.5 / **0.7** / 0.9 | (1) portrait close-up · (2) full body studio · (3) **new outfit** · (4) **new setting** |

- Default use weight **0.7**. Stacking: character ~**0.8** + style ~**0.5**.
- Pass = identity holds on (1)(2) and still follows (3)(4) without baking the training outfits/backgrounds.
- Fail → adjust trigger, weight 0.6–0.9, test **one LoRA alone**, remove prompt tokens that fight the LoRA. Do not stack until solo works.

## How Mio uses the LoRA afterwards

State line `engine=HARUKA` or `engine=TSUBAKI2` (etc., matching architecture).

- Include the **trigger** in the prompt (HARUKA: tags; TSUBAKI2: NL sentence containing the trigger phrase).
- State LoRA name + weight in the copy-ready block under the frame (user pastes into PixAI panel).
- Still re-inject LOCK blocks verbatim; LoRA assists identity, locks remain source of truth for wardrobe/assets.
- Grok Imagine has **no** LoRA slot — on `engine=GROK` keep using Pack/ART refs (max 3). Offer the PixAI path when the user wants learned weights.

## Never

- Start paid training without explicit user OK.
- Promise Tsubaki.3 LoRA support while undocumented.
- Train on real-person photos or under-age reads.
- Average conflicting identity traits into the trigger.
