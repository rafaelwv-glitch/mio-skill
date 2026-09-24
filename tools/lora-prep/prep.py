#!/usr/bin/env python3
"""Mio LoRA dataset prep for PixAI. Dedupe, resize, caption, manifest. No training."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("ERROR: Pillow is required. pip install Pillow", file=sys.stderr)
    sys.exit(1)

try:
    import imagehash
except ImportError:
    imagehash = None  # type: ignore

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
HASH_THRESHOLD = 6  # perceptual near-dupe cutoff
TINY_PX = 512


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Prepare a PixAI LoRA dataset: dedupe, resize, caption, manifest."
    )
    p.add_argument("input_dir", type=Path, help="Folder of jpg/png/webp images")
    p.add_argument("output_dir", type=Path, help="Output folder (created if missing)")
    p.add_argument(
        "--trigger",
        required=True,
        help='Trigger text (>=30 chars recommended), e.g. "oc01 adult woman, long silver hair, red eyes"',
    )
    p.add_argument("--size", type=int, default=1024, help="Max longest side (default 1024)")
    p.add_argument(
        "--square",
        action="store_true",
        help="Pad to square with neutral fill (no crop). Off by default.",
    )
    p.add_argument(
        "--caption-template",
        default="",
        help="Extra caption text appended after trigger (before filename hints)",
    )
    p.add_argument("--min", type=int, default=10, dest="min_keep", help="Warn if fewer kept (default 10)")
    p.add_argument(
        "--tagger",
        default=None,
        help="Optional path to WD14-style ONNX tagger; skipped if missing/unloadable",
    )
    p.add_argument(
        "--hash-size",
        type=int,
        default=8,
        help="imagehash phash size (default 8)",
    )
    return p.parse_args()


def collect_images(input_dir: Path) -> list[Path]:
    files = []
    for p in sorted(input_dir.iterdir()):
        if p.is_file() and p.suffix.lower() in IMAGE_EXTS:
            files.append(p)
    return files


def filename_hints(stem: str) -> str:
    s = stem.lower()
    hints: list[str] = []
    rules = [
        (r"^face[_-]?", "close-up face"),
        (r"^full[_-]?", "full body"),
        (r"^back[_-]?", "from behind"),
        (r"^profile[_-]?", "profile view"),
        (r"^side[_-]?", "side view"),
        (r"^expr[_-]?", "expression focus"),
        (r"^pose[_-]?", "dynamic pose"),
        (r"^outfit([a-z0-9]+)?[_-]?", None),  # special
    ]
    for pat, hint in rules:
        m = re.search(pat, s)
        if not m:
            continue
        if hint is not None:
            hints.append(hint)
        else:
            raw = m.group(1) or ""
            if raw:
                hints.append(f"wearing outfit {raw}")
            else:
                hints.append("outfit focus")
    # outfitX_ mid-name
    m2 = re.search(r"outfit([a-z0-9]+)", s)
    if m2 and not any(h.startswith("wearing outfit") or h == "outfit focus" for h in hints):
        hints.append(f"wearing outfit {m2.group(1)}")
    return ", ".join(hints)


def pad_to_square(im: Image.Image, fill=(200, 200, 200)) -> Image.Image:
    w, h = im.size
    side = max(w, h)
    if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
        base = Image.new("RGBA", (side, side), fill + (255,))
        im = im.convert("RGBA")
    else:
        base = Image.new("RGB", (side, side), fill)
        im = im.convert("RGB")
    base.paste(im, ((side - w) // 2, (side - h) // 2))
    return base


def resize_longest(im: Image.Image, size: int) -> Image.Image:
    w, h = im.size
    longest = max(w, h)
    if longest <= size:
        return im
    scale = size / float(longest)
    nw, nh = max(1, int(round(w * scale))), max(1, int(round(h * scale)))
    return im.resize((nw, nh), Image.Resampling.LANCZOS)


def try_tagger(tagger_path: str | None, image_path: Path) -> str:
    if not tagger_path:
        return ""
    path = Path(tagger_path)
    if not path.exists():
        return ""
    # Optional WD14-style ONNX: load only if onnxruntime + a thin wrapper exist.
    # Fail soft — never abort the prep run.
    try:
        # Placeholder hook: if user points at a .onnx file we acknowledge and skip
        # unless a companion tagger module is importable.
        import importlib

        mod = None
        for name in ("wd14_tagger", "tagger", "mio_tagger"):
            try:
                mod = importlib.import_module(name)
                break
            except ImportError:
                continue
        if mod is None or not hasattr(mod, "tag"):
            return ""
        tags = mod.tag(str(image_path), model_path=str(path))
        if isinstance(tags, (list, tuple)):
            return ", ".join(str(t) for t in tags)
        return str(tags) if tags else ""
    except Exception:
        return ""


def main() -> int:
    args = parse_args()
    inp: Path = args.input_dir
    out: Path = args.output_dir

    if not inp.is_dir():
        print(f"ERROR: input_dir not a directory: {inp}", file=sys.stderr)
        return 2

    out.mkdir(parents=True, exist_ok=True)

    if imagehash is None:
        print("WARN: imagehash not installed — skipping perceptual dedupe. pip install imagehash")

    trigger = args.trigger.strip()
    if len(trigger) < 30:
        print(
            f"WARN: trigger is {len(trigger)} chars; PixAI recommends >= 30 "
            "(especially DiT.2 / Tsubaki.2)."
        )

    files = collect_images(inp)
    if not files:
        print(f"ERROR: no jpg/png/webp in {inp}", file=sys.stderr)
        return 2

    rows: list[dict] = []
    kept_hashes: list[tuple[object, str]] = []  # (hash, kept_out_name)
    kept_count = 0
    dropped_count = 0
    warnings: list[str] = []

    for src in files:
        reason = ""
        status = "kept"
        phash_str = ""
        w = h = 0
        try:
            with Image.open(src) as im:
                im.load()
                w, h = im.size
                work = im.convert("RGBA") if im.mode in ("RGBA", "LA", "P") else im.convert("RGB")
                if imagehash is not None:
                    ph = imagehash.phash(work, hash_size=args.hash_size)
                    phash_str = str(ph)
                    dup_of = None
                    for prev_h, prev_name in kept_hashes:
                        if ph - prev_h <= HASH_THRESHOLD:
                            dup_of = prev_name
                            break
                    if dup_of is not None:
                        status = "dropped"
                        reason = f"duplicate of {dup_of} (phash distance <= {HASH_THRESHOLD})"
                        dropped_count += 1
                        rows.append(
                            {
                                "file": src.name,
                                "hash": phash_str,
                                "status": status,
                                "reason": reason,
                                "width": w,
                                "height": h,
                                "out_file": "",
                            }
                        )
                        print(f"DROP  {src.name} — {reason}")
                        continue

                if max(w, h) < TINY_PX:
                    warnings.append(f"{src.name}: very small ({w}x{h}), < {TINY_PX}px")
                ar = max(w, h) / max(1, min(w, h))
                if ar >= 3.0:
                    warnings.append(f"{src.name}: extreme aspect ratio {w}x{h} ({ar:.1f}:1)")

                if args.square:
                    work = pad_to_square(work)
                work = resize_longest(work, args.size)
                if work.mode == "RGBA":
                    # Flatten soft for PixAI-friendly PNG without alpha surprises
                    bg = Image.new("RGB", work.size, (200, 200, 200))
                    bg.paste(work, mask=work.split()[-1])
                    work = bg
                else:
                    work = work.convert("RGB")

                out_name = f"{src.stem}.png"
                # Avoid collisions
                n = 1
                while (out / out_name).exists():
                    out_name = f"{src.stem}_{n}.png"
                    n += 1
                out_path = out / out_name
                work.save(out_path, format="PNG", optimize=True)

                hints = filename_hints(src.stem)
                parts = [trigger]
                if args.caption_template.strip():
                    parts.append(args.caption_template.strip())
                if hints:
                    parts.append(hints)
                extra_tags = try_tagger(args.tagger, out_path)
                if extra_tags:
                    parts.append(extra_tags)
                caption = ", ".join(parts)
                (out / f"{Path(out_name).stem}.txt").write_text(caption + "\n", encoding="utf-8")

                if imagehash is not None:
                    kept_hashes.append((ph, out_name))
                kept_count += 1
                rows.append(
                    {
                        "file": src.name,
                        "hash": phash_str,
                        "status": "kept",
                        "reason": "",
                        "width": w,
                        "height": h,
                        "out_file": out_name,
                    }
                )
                print(f"KEEP  {src.name} -> {out_name} ({work.size[0]}x{work.size[1]})")
        except Exception as e:
            status = "dropped"
            reason = f"unreadable: {e}"
            dropped_count += 1
            rows.append(
                {
                    "file": src.name,
                    "hash": "",
                    "status": status,
                    "reason": reason,
                    "width": w,
                    "height": h,
                    "out_file": "",
                }
            )
            print(f"DROP  {src.name} — {reason}")

    # manifest.csv
    man_path = out / "manifest.csv"
    with man_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["file", "hash", "status", "reason", "width", "height", "out_file"]
        )
        writer.writeheader()
        writer.writerows(rows)

    summary_lines = [
        f"input: {inp}",
        f"output: {out}",
        f"trigger: {trigger}",
        f"scanned: {len(files)}",
        f"kept: {kept_count}",
        f"dropped: {dropped_count}",
        f"size_cap: {args.size}",
        f"square_pad: {args.square}",
        f"dedupe: {'phash' if imagehash else 'skipped (no imagehash)'}",
        f"min_target: {args.min_keep}",
    ]
    if kept_count < args.min_keep:
        msg = f"WARN: only {kept_count} images kept (min {args.min_keep}). Add more varied angles before training."
        warnings.append(msg)
        print(msg)
    for wmsg in warnings:
        if not wmsg.startswith("WARN:"):
            print(f"WARN: {wmsg}")
        summary_lines.append(f"WARN: {wmsg}" if not wmsg.startswith("WARN:") else wmsg)

    summary_path = out / "summary.txt"
    summary_path.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    print("---")
    print(f"Wrote {man_path.name}, {summary_path.name}; kept={kept_count} dropped={dropped_count}")
    print("Mio never starts paid training — wait for explicit user OK (see references/lora-pixai.md).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
