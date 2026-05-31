# `scripts/` — reusable pipeline for archival-source cross-referencing

A small set of source-agnostic scripts for turning a digitised primary
source (DjVu page set + line-anchored claims) into a fully-auditable
evidence chain: OCR dump → line→page index → wide page-image crops with
red-rectangle overlays → gold-standard cross-reference markdown.

These were built for the Zagajowski 1724 `§5` cross-reference work but
are designed to drop straight onto any future DjVu/PDF source (Trebnic
1636 once BJ photos exist; additional Marian-apparition case studies;
any 17th–18th-c. printed Polish or Latin source).

## Pipeline stages

| Stage | Script | What it does |
|---|---|---|
| 1. OCR text | `ocr-pipeline.sh` | DjVu set → flat text dump with `===== <page-stem> =====` separators |
| 2. Page→images | `extract-page-images.sh` | DjVu set → one PNG per page (300 DPI default) |
| 3. Line→page index | `build-line-index.py` | OCR dump → JSON mapping every line number to a page-stem |
| 4. Crop with overlay | `make-crop.py` | Line range + page image → wide JPG crop with red-rectangle highlight |
| 5. Context helper | `show-context.sh` | Print N lines of OCR around any cited line for quick inspection |

Stages 1–4 are deterministic; rerun the same command, get the same
output. Stage 5 is interactive.

## End-to-end example — adding cross-reference entries for a new source

Assume you've added a digitised source under `docs/references/<source-name>/`
containing `page*.djvu` files and a parallel working-notes folder
`docs/working-notes/<source-name>-xref/`:

```bash
# 1. Build the OCR dump (committed; ~500 KB plain text)
./scripts/ocr-pipeline.sh \
  'docs/references/<source-name>/page*.djvu' \
  docs/working-notes/<source-name>-xref/<source-name>-ocr.txt

# 2. Extract page images (local-only — do NOT commit)
./scripts/extract-page-images.sh \
  'docs/references/<source-name>/page*.djvu' \
  /tmp/<source-name>-pages 300

# 3. Build the line→page index (committed; small JSON)
python3.12 scripts/build-line-index.py \
  docs/working-notes/<source-name>-xref/<source-name>-ocr.txt \
  docs/working-notes/<source-name>-xref/line-page-index.json

# 4. For each line-anchored claim in your synthesis, make a crop:
python3.12 scripts/make-crop.py \
  --line-index docs/working-notes/<source-name>-xref/line-page-index.json \
  --pages-dir /tmp/<source-name>-pages \
  --first-line 3070 --last-line 3085 \
  --output docs/working-notes/<source-name>-xref/page-crops/l-3070-bartolomeus-dust.jpg \
  --label bartolomeus-dust \
  --pad-px 300 --quality 95

# 5. (Optional) quick check on a line in the OCR dump:
./scripts/show-context.sh \
  docs/working-notes/<source-name>-xref/<source-name>-ocr.txt 3076 15
```

The page-image extraction (stage 2) is intentionally local-only: a full
300-DPI image set for a 200-page book is ~500 MB, which doesn't belong
in git LFS. The targeted crops produced by stage 4 are what get committed
(~50–150 KB each at JPG q95).

## What to commit vs. regenerate

| Artefact | Commit? | Reason |
|---|---|---|
| `<source>-ocr.txt` | **Yes** | Anchors every line number cited in synthesis; small (~500 KB-1 MB plain text). Without it, line citations are bare integers pointing at nothing. |
| `line-page-index.json` | **Yes** | Tiny; needed by `make-crop.py`; documents the dump→page mapping deterministically. |
| `page-crops/*.jpg` | **Yes** (LFS) | The gold-standard visual proof for each cited claim. |
| `claims-cross-reference.md` | **Yes** | The human-readable artefact tying everything together. |
| `/tmp/<source>-pages/*.png` | **No** | Regenerable from the DjVu source via stage 2. ~500 MB for a typical book. |

## Tooling prerequisites

- `djvutxt`, `ddjvu` — from `djvulibre-bin` (Ubuntu/Debian)
- `tesseract` with `pol` and `lat` language packs — `tesseract-ocr`, `tesseract-ocr-pol`, `tesseract-ocr-lat`
- `convert`, `identify` — from `imagemagick`
- Python ≥ 3.10 with `Pillow` and `pytesseract` (`pip install pillow pytesseract`)

## Anthropic API integration (future)

The vision-transcription step (page-crop image → original-orthography
Polish + English translation + uncertainty notes) is currently done
interactively in-chat. A `vision-transcribe.py` wrapper around the
Anthropic SDK is the next natural addition; the JPG crops produced by
stage 4 are already in the right format to feed to such a wrapper. See
`docs/working-notes/zagajowski-anomaly-sweep/pilzna-1645-vision-pilot/`
for the empirical baseline on Polish 17th-c. material.
