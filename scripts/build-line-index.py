#!/usr/bin/env python3.12
"""build-line-index.py — parse an OCR dump and produce a line→page index.

Reads an OCR text file produced by ocr-pipeline.sh (which inserts
`===== <page-stem> =====` markers between pages) and writes a JSON file
mapping every line number in the dump to the page-stem that line belongs
to.

Output JSON schema::

    {
      "source": "<input-path>",
      "total_lines": 8250,
      "pages": [
        {"page_id": "page0001", "first_line": 2, "last_line": 35},
        {"page_id": "page0002", "first_line": 37, "last_line": 71},
        ...
      ],
      "line_to_page": {"3070": "page0095", ...}
    }

Usage::

    python3.12 scripts/build-line-index.py <ocr-dump> <output-json>
"""

import json
import re
import sys
from pathlib import Path

SEPARATOR_RE = re.compile(r"^[\s\f]*=====\s+(\S+)\s+=====\s*$")


def build_index(ocr_path: Path) -> dict:
    pages: list[dict] = []
    line_to_page: dict[str, str] = {}
    current_page: str | None = None
    current_first: int | None = None
    last_content_line: int | None = None

    with ocr_path.open("r", encoding="utf-8", errors="replace") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.rstrip("\n")
            m = SEPARATOR_RE.match(line)
            if m:
                # Close out the previous page block
                if current_page is not None and current_first is not None:
                    pages.append({
                        "page_id": current_page,
                        "first_line": current_first,
                        "last_line": last_content_line or current_first,
                    })
                current_page = m.group(1)
                current_first = lineno + 1  # content begins on the next line
                last_content_line = None
                continue
            if current_page is not None:
                line_to_page[str(lineno)] = current_page
                last_content_line = lineno

    # Close out the final page
    if current_page is not None and current_first is not None:
        pages.append({
            "page_id": current_page,
            "first_line": current_first,
            "last_line": last_content_line or current_first,
        })

    return {
        "source": str(ocr_path),
        "total_lines": len(line_to_page),
        "page_count": len(pages),
        "pages": pages,
        "line_to_page": line_to_page,
    }


def main() -> int:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <ocr-dump> <output-json>", file=sys.stderr)
        return 1

    ocr_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    if not ocr_path.is_file():
        print(f"Error: OCR dump not found: {ocr_path}", file=sys.stderr)
        return 1

    index = build_index(ocr_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=2)

    print(f"Line index written: {out_path}")
    print(f"  Total lines indexed: {index['total_lines']}")
    print(f"  Pages found: {index['page_count']}")
    if index["pages"]:
        print(
            f"  First page: {index['pages'][0]['page_id']} "
            f"(lines {index['pages'][0]['first_line']}–{index['pages'][0]['last_line']})"
        )
        print(
            f"  Last page:  {index['pages'][-1]['page_id']} "
            f"(lines {index['pages'][-1]['first_line']}–{index['pages'][-1]['last_line']})"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
