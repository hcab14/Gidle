#!/usr/bin/env python3.12
"""make-crop.py — produce a wide page crop with red-rectangle overlay.

Given a line range in an OCR dump, locate the corresponding page image,
estimate the on-page region of the cited text (via Tesseract bboxes +
linear interpolation), draw a red rectangle around it, and save a wide
JPG crop preserving full page-width and adding vertical padding above
and below for paragraph context.

If the cited line range spans multiple pages, multiple output files are
produced with `-p1`, `-p2`, ... suffixes.

Usage::

    python3.12 scripts/make-crop.py \\
      --line-index <line-index.json> \\
      --pages-dir <pages-dir> \\
      --first-line <N> --last-line <M> \\
      --output <output.jpg> \\
      [--label '<short label>'] \\
      [--pad-px 300] [--quality 95]

Note on accuracy: the red rectangle is an *orientation heuristic*, not
pixel-perfect. The point is to let a reader find the cited passage
within the page's full visual context. The crop always preserves enough
context (full width + padding) that the cited passage is recoverable
even if the rectangle is off by a few lines.
"""

import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw
import pytesseract


def find_page_block(line_index: dict, line_no: int) -> dict | None:
    for block in line_index["pages"]:
        if block["first_line"] <= line_no <= block["last_line"]:
            return block
    return None


def estimate_highlight_box(
    image: Image.Image,
    page_block: dict,
    first_line: int,
    last_line: int,
) -> tuple[int, int, int, int]:
    """Estimate (left, top, right, bottom) of the highlighted region."""
    page_first = page_block["first_line"]
    page_last = page_block["last_line"]
    page_span = max(1, page_last - page_first + 1)

    top_frac = (first_line - page_first) / page_span
    bot_frac = (last_line - page_first + 1) / page_span
    top_frac = max(0.0, min(1.0, top_frac))
    bot_frac = max(0.0, min(1.0, bot_frac))

    width, height = image.size

    text_top, text_bot = 0, height
    try:
        data = pytesseract.image_to_data(
            image,
            lang="pol+lat",
            output_type=pytesseract.Output.DICT,
        )
        text_ys = [
            (data["top"][i], data["top"][i] + data["height"][i])
            for i in range(len(data["text"]))
            if data["text"][i].strip()
        ]
        if text_ys:
            text_top = min(t for t, _ in text_ys)
            text_bot = max(b for _, b in text_ys)
    except Exception:
        pass

    text_span = max(1, text_bot - text_top)
    est_top = int(text_top + top_frac * text_span)
    est_bot = int(text_top + bot_frac * text_span)
    if est_bot - est_top < 30:
        est_bot = est_top + 30

    margin = max(10, width // 40)
    return (margin, est_top, width - margin, est_bot)


def render_crop(
    image_path: Path,
    page_block: dict,
    first_line: int,
    last_line: int,
    output_path: Path,
    pad_px: int = 300,
    quality: int = 95,
) -> None:
    image = Image.open(image_path).convert("RGB")
    left, top, right, bottom = estimate_highlight_box(
        image, page_block, first_line, last_line
    )

    annotated = image.copy()
    draw = ImageDraw.Draw(annotated)
    draw.rectangle([left, top, right, bottom], outline="red", width=5)

    crop_top = max(0, top - pad_px)
    crop_bot = min(image.height, bottom + pad_px)
    cropped = annotated.crop((0, crop_top, image.width, crop_bot))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(output_path, "JPEG", quality=quality)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--line-index", required=True, type=Path)
    ap.add_argument("--pages-dir", required=True, type=Path)
    ap.add_argument("--first-line", required=True, type=int)
    ap.add_argument("--last-line", required=True, type=int)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--label", default="")
    ap.add_argument("--pad-px", type=int, default=300)
    ap.add_argument("--quality", type=int, default=95)
    args = ap.parse_args()

    if args.last_line < args.first_line:
        print("Error: --last-line must be >= --first-line", file=sys.stderr)
        return 1

    with args.line_index.open("r", encoding="utf-8") as fh:
        line_index = json.load(fh)

    page_blocks = [
        b for b in line_index["pages"]
        if b["first_line"] <= args.last_line and b["last_line"] >= args.first_line
    ]
    if not page_blocks:
        print(
            f"Error: lines {args.first_line}-{args.last_line} not found in line index",
            file=sys.stderr,
        )
        return 1

    if len(page_blocks) == 1:
        block = page_blocks[0]
        page_path = args.pages_dir / f"{block['page_id']}.png"
        if not page_path.is_file():
            print(f"Error: page image not found: {page_path}", file=sys.stderr)
            return 1
        render_crop(
            page_path, block, args.first_line, args.last_line, args.output,
            pad_px=args.pad_px, quality=args.quality,
        )
        print(
            f"Crop: {args.output} "
            f"(page {block['page_id']}, lines {args.first_line}-{args.last_line})"
        )
    else:
        stem, suffix = args.output.stem, args.output.suffix
        for i, block in enumerate(page_blocks, start=1):
            page_path = args.pages_dir / f"{block['page_id']}.png"
            if not page_path.is_file():
                print(f"Warning: page image not found, skipping: {page_path}", file=sys.stderr)
                continue
            line_lo = max(args.first_line, block["first_line"])
            line_hi = min(args.last_line, block["last_line"])
            out_p = args.output.with_name(f"{stem}-p{i}{suffix}")
            render_crop(
                page_path, block, line_lo, line_hi, out_p,
                pad_px=args.pad_px, quality=args.quality,
            )
            print(
                f"Crop: {out_p} "
                f"(page {block['page_id']}, lines {line_lo}-{line_hi})"
            )

    return 0


if __name__ == "__main__":
    sys.exit(main())
