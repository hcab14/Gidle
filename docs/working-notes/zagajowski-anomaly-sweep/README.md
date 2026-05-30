# Zagajowski 1724 — anomaly sweep

This folder holds the raw `grep` hit-lists used to populate the
**§5 *Recurring anomalies in the post-1516 Gidle cult*** section of
[`../../synthesis.md`](../../synthesis.md). Each file is the line-numbered
output of a `grep -ni -E '<pattern>'` against the OCR text-dump of
Zagajowski's *Skarb wielki* (Kraków 1724), produced via `djvutxt` over
the 242-page DjVu set in
[`../../references/zagajowski-1724-skarb-wielki/`](../../references/zagajowski-1724-skarb-wielki/).

Line numbers reference the flat-text dump (8250 lines). Page numbers
inside the OCR are best located by searching for the
`===== page0NNN =====` separators that `djvutxt` inserts between pages.

## Files

| File | Pattern (regex) | What it surfaces |
| --- | --- | --- |
| `01-light.txt` | `jasnoś\|światł\|blask\|łun[aą]\|świec\|światł\|promien` | Luminous / radiant phenomena |
| `02-odor.txt` | `woń\|wonn\|zapach\|aromat\|pachni\|pach[ln]\|smród\|smrod\|balsam` | Olfactory phenomena (incl. fragrant dust at l. 3076) |
| `03-sound.txt` | `głos\|usłysz\|szum\|huk\|brzęk\|dzwon\|stuk\|trąb\|hałas\|krzyk` | Auditory / voice phenomena |
| `04-apparition.txt` | `ukazał\|ukazała\|pokazała\|pokazał\|postać\|posta?wa\|zjawisk\|widzeni\|widział\|widziała\|persona\|widmo\|sen\|śnił\|śniła\|przyszła do` | Apparitions, visions, dream-figures |
| `05-aerial.txt` | `na niebie\|w powietrz\|wzniosła\|po powietrz\|nad ziemi\|nad mias\|nad domem\|niebo\|nad gł\|aer\|latając\|leciał` | Aerial / sky phenomena (incl. "powietrze morowe" = plague-air) |
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

```bash
# 1) Re-OCR the DjVu set into a flat text dump
cd docs/references/zagajowski-1724-skarb-wielki
for f in page*.djvu; do
  echo "===== ${f%.djvu} ====="
  djvutxt "$f"
done > /tmp/zagajowski-1724-full.txt

# 2) Re-run the sweep (each line below = one of the files above)
grep -ni -E 'jasnoś|światł|blask|łun[aą]|świec|światł|promien' \
    /tmp/zagajowski-1724-full.txt > 01-light.txt
# … etc., see the table above for the full set of patterns
```

The patterns deliberately tolerate the OCR's frequent letter-swaps in
old-spelling Polish (long-s for `f`, broken diacritics, etc.). They are
intended for **recall**, not precision — expect ~5-10% false positives
in each file, mostly from `niebezpieczeństwo` (matches `niebo`) or
`oświecony` (matches `świat`).

## What's missing

- **Tomasz z Pilzna 1645** OCR is too degraded for systematic mining
  (see `/tmp/tomasz-pilzna-1645-full.txt`); only a handful of its
  patterns survive the OCR, and even named entities like *Gidle* and
  *Panna* turn up as `Gidcl/kley` and `Panno pr5enaew«t#`. A clean
  re-OCR or hand transcription is open task #7 in `synthesis.md`.
- **Trebnic 1636** is not digitised at all — see `synthesis.md` §
  *Visiting BJ* for the in-person plan.
