#!/usr/bin/env bash
# extract-page-images.sh — DjVu set → one PNG per page.
#
# Usage:
#   ./scripts/extract-page-images.sh '<glob-pattern>' <output-dir> [dpi]
#
# Examples:
#   ./scripts/extract-page-images.sh \
#     'docs/references/zagajowski-1724-skarb-wielki/page*.djvu' \
#     /tmp/zagajowski-pages 300
#
# Output: <output-dir>/<page-stem>.png for each input .djvu page.
# Default DPI: 300 (good for printed-text legibility; ~2500 px per page side).
#
# Output is intended for local pipeline use (cropping, OCR, vision-transcription).
# Do NOT commit the full page-image set — it can be regenerated from the DjVu sources.
# Only commit the targeted crops produced by make-crop.py.

set -euo pipefail

if [[ $# -lt 2 || $# -gt 3 ]]; then
    echo "Usage: $0 '<glob-pattern>' <output-dir> [dpi]" >&2
    exit 1
fi

PATTERN="$1"
OUTPUT_DIR="$2"
DPI="${3:-300}"

shopt -s nullglob
DJVU_FILES=($PATTERN)
if [[ ${#DJVU_FILES[@]} -eq 0 ]]; then
    echo "Error: no files matched pattern: $PATTERN" >&2
    exit 1
fi

IFS=$'\n' SORTED=($(sort <<<"${DJVU_FILES[*]}"))
unset IFS

mkdir -p "$OUTPUT_DIR"

FAILED=0
for f in "${SORTED[@]}"; do
    page_id=$(basename "${f%.djvu}")
    out="$OUTPUT_DIR/$page_id.png"
    if [[ -f "$out" ]]; then
        continue  # idempotent
    fi
    if ! ddjvu -format=ppm -mode=color -scale="$DPI" "$f" "$OUTPUT_DIR/$page_id.ppm" 2>/dev/null; then
        echo "[ddjvu failed for $page_id]" >&2
        FAILED=$((FAILED + 1))
        continue
    fi
    convert "$OUTPUT_DIR/$page_id.ppm" "$out"
    rm -f "$OUTPUT_DIR/$page_id.ppm"
done

PAGES=${#SORTED[@]}
EXTRACTED=$(ls "$OUTPUT_DIR"/*.png 2>/dev/null | wc -l)
echo "Page images extracted: $EXTRACTED / $PAGES (failed: $FAILED) in $OUTPUT_DIR"
