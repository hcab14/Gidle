#!/usr/bin/env bash
# ocr-pipeline.sh — DjVu set → flat OCR text dump with page separators.
#
# Usage:
#   ./scripts/ocr-pipeline.sh '<glob-pattern>' <output-file>
#
# Examples:
#   ./scripts/ocr-pipeline.sh \
#     'docs/references/zagajowski-1724-skarb-wielki/page*.djvu' \
#     docs/working-notes/zagajowski-anomaly-sweep/zagajowski-1724-ocr.txt
#
#   ./scripts/ocr-pipeline.sh \
#     'docs/references/tomasz-z-pilzna-1645-historya-y-pozytki/DjVu/NDIGSTDR008788_*.djvu' \
#     docs/working-notes/pilzna-1645-vision-pilot/pilzna-1645-ocr.txt
#
# Output format: each page is preceded by a separator of the form
#   ===== <page-stem> =====
# where <page-stem> is the filename without .djvu (e.g. "page0042" or
# "NDIGSTDR008788_0042"). Line numbers in the resulting file are stable
# and can be used as canonical citation anchors (e.g. "l. 3070" in synthesis.md).

set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "Usage: $0 '<glob-pattern>' <output-file>" >&2
    echo "  Quote the glob pattern to prevent premature shell expansion." >&2
    exit 1
fi

PATTERN="$1"
OUTPUT_FILE="$2"

# Resolve glob pattern (quoted in the argv, expanded here)
shopt -s nullglob
DJVU_FILES=($PATTERN)
if [[ ${#DJVU_FILES[@]} -eq 0 ]]; then
    echo "Error: no files matched pattern: $PATTERN" >&2
    exit 1
fi

# Sort for deterministic page order (DjVu glob expansion is filesystem-order on some systems)
IFS=$'\n' SORTED=($(sort <<<"${DJVU_FILES[*]}"))
unset IFS

mkdir -p "$(dirname "$OUTPUT_FILE")"
: > "$OUTPUT_FILE"  # truncate

FAILED=0
for f in "${SORTED[@]}"; do
    page_id=$(basename "${f%.djvu}")
    echo "===== $page_id =====" >> "$OUTPUT_FILE"
    # djvutxt emits a trailing form-feed (\f) at the end of each page;
    # strip it so the next page's separator stays on its own line and
    # remains anchorable in regex searches.
    if ! djvutxt "$f" 2>/dev/null | tr -d '\f' >> "$OUTPUT_FILE"; then
        echo "[djvutxt failed for $page_id]" >> "$OUTPUT_FILE"
        FAILED=$((FAILED + 1))
    fi
done

LINES=$(wc -l < "$OUTPUT_FILE")
PAGES=${#SORTED[@]}
echo "OCR dump written: $OUTPUT_FILE"
echo "  Pages processed: $PAGES (failed: $FAILED)"
echo "  Lines of output: $LINES"
