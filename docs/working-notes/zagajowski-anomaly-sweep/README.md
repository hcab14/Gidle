# Zagajowski 1724 — anomaly sweep + gold-standard cross-reference

This folder is the working substrate for **§5 *Recurring anomalies in
the post-1516 Gidle cult*** of [`../../synthesis.md`](../../synthesis.md).

It has two layers of evidence:

1. **The original grep sweep** (15 hit-lists, table below). Recall-tuned
   regex searches against the OCR dump. These produced the candidate
   passages from which §5 was drafted.
2. **The gold-standard cross-reference**
   ([`claims-cross-reference.md`](claims-cross-reference.md)). For every
   line-anchored claim §5 actually cites, the cross-reference gives
   the page-image crop with red-rectangle overlay, the raw OCR, a
   fresh vision transcription preserving early-modern Polish/Latin
   orthography, the English translation, and uncertainty notes.

Use **layer 1** to verify that §5's *coverage* of the source is honest
(i.e. that nothing relevant was filtered out). Use **layer 2** to
verify that each *individual claim* in §5 is anchored in the actual
print.

## Key artefacts

| File | What it is | Status |
|---|---|---|
| [`claims-cross-reference.md`](claims-cross-reference.md) | Gold-standard per-claim entries (10 claims, with page-image crops, raw OCR, vision transcription, English translation, uncertainty notes). | **The main artefact of this folder.** |
| [`zagajowski-1724-ocr.txt`](zagajowski-1724-ocr.txt) | Full OCR dump (228 pages → 8250 lines) via `djvutxt`. Page separators `===== page0NNN =====` between pages. | Anchors every line citation in §5. |
| [`line-page-index.json`](line-page-index.json) | Maps every line in the OCR dump to its page-stem. | Used by `make-crop.py` to locate cited passages on the right page. |
| [`page-crops/`](page-crops/) | Wide JPG crops with red-rectangle overlays for each of the 10 line-anchored claims in §5. | LFS-tracked. |
| `0N-<topic>.txt` (×15) | Raw grep hit-lists from the original anomaly sweep. | Methodology audit trail. |

## The original grep sweep — file table

Line numbers below reference the OCR dump (`zagajowski-1724-ocr.txt`,
8250 lines). The DjVu sources live in
[`../../references/zagajowski-1724-skarb-wielki/`](../../references/zagajowski-1724-skarb-wielki/).

| File | Pattern (regex) | What it surfaces |
| --- | --- | --- |
| `01-light.txt` | `jasnoś\|światł\|blask\|łun[aą]\|świec\|światł\|promien` | Luminous / radiant phenomena |
| `02-odor.txt` | `woń\|wonn\|zapach\|aromat\|pachni\|pach[ln]\|smród\|smrod\|balsam` | Olfactory phenomena (incl. fragrant dust at l. 3076) |
| `03-sound.txt` | `głos\|usłysz\|szum\|huk\|brzęk\|dzwon\|stuk\|trąb\|hałas\|krzyk` | Auditory / voice phenomena |
| `04-apparition.txt` | `ukazał\|ukazała\|pokazała\|pokazał\|postać\|posta?wa\|zjawisk\|widzeni\|widział\|widziała\|persona\|widmo\|sen\|śnił\|śniła\|przyszła do` | Apparitions, visions, dream-figures |
| `05-aerial.txt` | `na niebie\|w powietrz\|wzniosła\|po powietrz\|nad ziemi\|nad mias\|nad domem\|niebo\|nad gł\|aer\|latając\|leciał` | Aerial / sky phenomena (incl. *„powietrze morowe”* = plague-air) |
| `06-subterr.txt` | `z ziemi\|spod ziemi\|podziemn\|jama\|jaski\|grot\|piwni\|stud[nz]i\|dół głęb\|grób\|grobu\|pieczar\|ja(mi\|me\|m)` | Subterranean / from-the-earth (well miracle at l. 7561) |
| `07-energy.txt` | `ogień\|płomień\|gor[ąa]czk\|gor[ąa]co\|spalon\|spalił\|opali\|por[aą]żo\|por[aą]żaj\|raził\|rażon\|piec[ze]\|piorun\|grzm\|elektr` | Burning / heat / shock effects |
| `08-motion.txt` | `znikł\|znikn\|znikał\|przeniosła si\|sama wróc\|sam wróc\|sama pow\|sam pow\|na pow.* się\|zjawi.* się\|samowoln` | Self-motion of objects, vanishing events |
| `09-weather.txt` | `burz[ay]\|grad\|piorun\|błyskawi\|grzm\|tęcza\|wicher\|mgł[ay]\|chmura\|grom` | Weather-related events |
| `10-paralysis.txt` | `sparal\|drętw\|skamien\|znieruchom\|nie mógł się ruszy\|stanęły\|skuł\|usch\|usycha\|porażon\|zmartwia\|martwy[a-z]*` | Sudden paralysis / immobilisation / tonic effects |
| `11-resurrection.txt` | `wskrzesz\|umarł.*ożył\|ożył\|martwych wskrz\|martwy[au] wsk\|zmartwychwsta` | Revivals from clinical death (very many) |
| `12-transparent.txt` | `przeźroczy\|przezrocz\|pajęczyn\|jak obło\|na kształ.*obło\|błyszcz\|świecąc.*posta\|wśród blasku` | Transparent / spiderweb-like / cloud-like figures |
| `15-possession.txt` | `czart\|czarta\|diabe[lł]\|opęt\|opęta\|wyszedł\|exorcy\|paf[lt]ego` | Possession / exorcism cases |
| `16-preserved.txt` | (composite `szwank\|szkod\|urazu\|krzywd\|porażon`) | Preservation-from-harm idioms |
| `17-contact.txt` | `proch.*z\|proch z\|olej\|woda.*omyć\|omyć\|umyć\|umycie\|maść\|woda z obraz` | Contact-mediated healing (dust, oil, wash-water) |

## How to regenerate

The pipeline scripts now live under [`../../../scripts/`](../../../scripts/).
Full reproduction recipe:

```bash
# 1. OCR dump (~20 s, deterministic)
./scripts/ocr-pipeline.sh \
  'docs/references/zagajowski-1724-skarb-wielki/page*.djvu' \
  docs/working-notes/zagajowski-anomaly-sweep/zagajowski-1724-ocr.txt

# 2. Re-run the 15-pattern grep sweep (one of the lines below per file)
grep -ni -E 'jasnoś|światł|blask|łun[aą]|świec|światł|promien' \
    docs/working-notes/zagajowski-anomaly-sweep/zagajowski-1724-ocr.txt \
    > docs/working-notes/zagajowski-anomaly-sweep/01-light.txt
# … etc., see the table above for the full pattern set

# 3. (For the gold-standard layer) line→page index
python3.12 scripts/build-line-index.py \
  docs/working-notes/zagajowski-anomaly-sweep/zagajowski-1724-ocr.txt \
  docs/working-notes/zagajowski-anomaly-sweep/line-page-index.json

# 4. (For the gold-standard layer) extract 300-DPI page images locally
./scripts/extract-page-images.sh \
  'docs/references/zagajowski-1724-skarb-wielki/page*.djvu' \
  /tmp/zagajowski-pages 300

# 5. (For the gold-standard layer) per-claim wide crops
python3.12 scripts/make-crop.py \
  --line-index docs/working-notes/zagajowski-anomaly-sweep/line-page-index.json \
  --pages-dir /tmp/zagajowski-pages \
  --first-line <N> --last-line <M> \
  --output docs/working-notes/zagajowski-anomaly-sweep/page-crops/l-<N>-<label>.jpg
```

The grep patterns deliberately tolerate the OCR's frequent letter-swaps
in old-spelling Polish (long-s ↔ `f`, broken diacritics, etc.). They are
recall-tuned, not precision-tuned — expect ~5–10% false positives in
each file, mostly from `niebezpieczeństwo` (matches `niebo`) or
`oświecony` (matches `świat`). The gold-standard cross-reference at
`claims-cross-reference.md` filters these down to the 10 actually-cited
passages.

## OCR vs. vision transcription — quality note

Layer 1 (the grep sweep) relies on the existing `djvutxt` OCR, which on
this 1724 Roman-type print is roughly 80% accurate: enough to support
keyword search, marginal for direct quotation. Layer 2 (the cross-
reference) is built against fresh **vision transcription** from the
page-image crops, preserving early-modern orthography.

Systematic OCR failure modes documented in
[`claims-cross-reference.md` — methodology note](claims-cross-reference.md#methodology-note-what-this-cross-reference-proves-and-does-not-prove):
long-s ↔ `f` (~80% of the time), mid-line character drops in noisy
areas, Latin attestation blocks badly degraded, internal book-locator
codes (`k. N. c. N. r. N. l. N.`) almost entirely destroyed. The
vision pass recovers all of these.

## Other sources

- **Tomasz z Pilzna 1645** — printed mostly in blackletter Schwabacher,
  for which `djvutxt` is essentially destroyed. See the sibling pilot
  folder [`../pilzna-1645-vision-pilot/`](../pilzna-1645-vision-pilot/)
  for a 6-page vision-transcription demonstration, plus an analysis of
  which Pilzna content is currently unrecoverable from the grep
  approach used here.
- **Trebnic 1636** — not digitised; planning notes in `synthesis.md`
  §10.3 (the *Visiting BJ* appendix).
