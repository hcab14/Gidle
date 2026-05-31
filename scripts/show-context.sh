#!/usr/bin/env bash
# show-context.sh — print N lines of context around a given line in an OCR dump.
#
# Usage:
#   ./scripts/show-context.sh <ocr-dump> <line-number> [context-lines]
#
# Example:
#   ./scripts/show-context.sh \
#     docs/working-notes/zagajowski-anomaly-sweep/zagajowski-1724-ocr.txt 3076 15
#
# Default context: 15 lines on each side. The target line is highlighted
# with ">>>" in the output.

set -euo pipefail

if [[ $# -lt 2 || $# -gt 3 ]]; then
    echo "Usage: $0 <ocr-dump> <line-number> [context-lines]" >&2
    exit 1
fi

OCR="$1"
LINE="$2"
CTX="${3:-15}"

if [[ ! -f "$OCR" ]]; then
    echo "Error: OCR file not found: $OCR" >&2
    exit 1
fi

START=$((LINE - CTX))
END=$((LINE + CTX))
[[ $START -lt 1 ]] && START=1

awk -v line="$LINE" -v s="$START" -v e="$END" '
    NR >= s && NR <= e {
        marker = (NR == line) ? " >>> " : "     "
        printf "%6d%s%s\n", NR, marker, $0
    }
' "$OCR"
