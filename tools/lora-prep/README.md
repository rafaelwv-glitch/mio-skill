# lora-prep — PixAI LoRA dataset helper

Prepares a folder of images for PixAI **Train your own LoRA**. Dedupe, optional square pad, resize, PNG export, per-image captions, `manifest.csv`. Does **not** upload or start training.

## Requirements

```
pip install -r requirements.txt
```

- Python 3.10+
- Pillow (required)
- imagehash (recommended; without it, dedupe is skipped with a warning)
- Optional: `--tagger path/to/wd14.onnx` plus a `wd14_tagger` / `tagger` / `mio_tagger` module exposing `tag(path, model_path=...)`. If missing, tagging is skipped silently.

## Usage

```
python prep.py INPUT_DIR OUTPUT_DIR --trigger "oc01 adult woman, long silver hair, blunt bangs, red eyes"
```

Useful flags:

| Flag | Default | Meaning |
|---|---|---|
| `--size` | 1024 | Longest side cap |
| `--square` | off | Pad to square (no crop) |
| `--caption-template "..."` | empty | Extra text after trigger |
| `--min` | 10 | Warn if fewer images kept |
| `--tagger PATH` | none | Optional ONNX tagger |

Filename hints (stem prefixes) append short caption bits: `face_*`, `full_*`, `back_*`, `profile_*`, `side_*`, `expr_*`, `pose_*`, `outfitX_*`.

Outputs in `OUTPUT_DIR`:

- `*.png` + matching `*.txt` captions (`trigger` + template + hints)
- `manifest.csv` — file, hash, kept/dropped, reason, WxH, out_file
- `summary.txt`

## After prep

See `references/lora-pixai.md`: pick architecture, confirm trigger, then **user** starts training in PixAI (Models → Train your own LoRA). Mio never spends credits itself.
