# Reference Pack — many images of one character (Grok-first, LoRA-lite)

Use when the user supplies **≥ 5 images of one fictional adult character**. For 1–4 images use ART LOCK (`original-art.md`). For true learned identity use the PixAI LoRA path (`lora-pixai.md`).

**Honest limits:** Grok Imagine sees **max 3** reference images per generation and does **not** learn or persist anything. PixAI Tsubaki.3 does reference-image generation from **1** ref; Reference Pro takes up to **10**. Extra images only help if Mio **condenses** them into a consensus lock + small anchor set. This improves stability; it is **not** training.

State line: `mode=PACK`.

## 1. Intake

- Accept **5–30** images of **one** fictional adult character (jpg/png/webp/canvas drops).
- **Refuse** real-person photographs as subjects. Under-age read → ask to adultify (25, mature face, 1:7) or stop.
- If images clearly show **different people**, stop and ask which character is the pack subject.
- Label each image `P01`…`Pnn` in arrival order (stable IDs for the manifest).

## 2. Sort into buckets

Assign every image to **one** primary bucket:

| Bucket | Meaning |
|---|---|
| `FACE-CLOSE` | face / head / bust dominance |
| `FULLBODY` | head-to-toe or clear proportions |
| `PROFILE/BACK` | side or rear view |
| `OUTFIT-<name>` | distinct costume (e.g. `OUTFIT-school`, `OUTFIT-casual`) |
| `STYLE-SAMPLE` | style/rendering reference more than identity |
| `POSE` | useful pose/composition, face secondary |

Also mark:
- **duplicate** — near-identical (same crop/pose/outfit); keep one, list the rest as `dup-of:Pxx`.
- **outlier** — different face, different art style, wrong character, heavy filter/meme overlay. **List outliers; never silently use them** in consensus or as anchors.

Print the sort as a short table before locking.

## 3. Consensus lock

Build `[FACE]` `[BODY]` `[STYLE]` `[WARDROBE]` **only from traits that appear on a clear majority** of **kept** (non-outlier) images.

- Majority = more than half of kept images where that trait is visible.
- **Never average** conflicts (e.g. blue eyes in 4, green in 3). Put conflicts in **one batched ask** (same shape as the Asset Check), then wait:

```
Pack Check — trait conflicts
FACE     eye colour: blue (P01,P03,P05,P08) vs green (P02,P04,P07) — pick?
WARDROBE default outfit: sailor (6) vs hoodie (3) — lock which as WARDROBE-default?
STYLE    line weight: thick cel (majority) vs thin paint (P12,P14 outliers already) — confirm CEL00?
Reply per row, or "you pick".
```

- Under-age consensus → adultify ask or stop (Hard Limits).
- On answers → print LOCK blocks + `lock=YES` · `mode=PACK`.

## 4. Anchor set

From the pack (Tsubaki.3-style design-sheet pattern; Grok or TSUBAKI3):

1. **ISO sheet** — single character, plain studio, full body, head-to-toe (same as ART isolate).
2. **Turnaround** — front / side / back on one page (or three frames).
3. **3×3 expression sheet** — nine expressions, same face/style.

User **approves** → these become the **anchors** (`ANCHOR-ISO`, `ANCHOR-TURN`, `ANCHOR-EXPR`). Prefer anchors over raw pack images as Ref1 thereafter.

## 5. Per-frame ref selection (max 3)

| Beat type | Ref1 | Ref2 | Ref3 |
|---|---|---|---|
| Close-up / face / choker | best FACE-CLOSE anchor (or ANCHOR-EXPR crop) | pose/outfit match if needed | setting only |
| Full-body / cowboy / establishing with figure | ANCHOR-ISO or ANCHOR-TURN | pose or OUTFIT-<name> match | setting only |
| Outfit change | ANCHOR-ISO (face+body) | OUTFIT-<name> pack image | setting only |

Ref3 mandatory sentence (from `original-art.md`):

> From reference 3 take background and light direction only. Do not take line language, shading, palette, or face from reference 3.

**Print under each frame** which pack/anchor IDs were used, e.g. `refs: Ref1=ANCHOR-ISO · Ref2=P14(POSE) · Ref3=setting-mood`.

## 6. Pack manifest (re-inject verbatim)

Print once after sort; re-print when the pack changes; re-inject the block on later turns so the pack survives:

```
[PACK MANIFEST] subject=<short fictional label> · kept=N · outliers=M · anchors=…
| id  | bucket        | status          | notes |
| P01 | FACE-CLOSE    | keep            | best face |
| P02 | FULLBODY      | keep            | |
| P03 | FACE-CLOSE    | dup-of:P01      | |
| P12 | STYLE-SAMPLE  | outlier          | different face |
| ANCHOR-ISO | FULLBODY | anchor     | user approved |
```

Do not paraphrase the manifest. Edits only on user request, then reprint.

## 7. When to escalate to LoRA

If the user needs the character across many sessions / engines with true learning → prepare a PixAI LoRA dataset (`lora-pixai.md` + `tools/lora-prep/`). Pack ≠ training.
