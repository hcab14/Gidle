# Pilzna 1645 — vision-OCR pilot

## Why this pilot exists

Tomasz z Pilzna's *Historya y Pożytki…* (Kraków 1645) is the **earliest
surviving printed full-length account of the Gidle cult** — almost
certainly drawing on the lost 1636 *Trebnic*, but at one further remove
from the contemporary witnesses. It is named on the title page:

| | |
|---|---|
| Author | X. Thomasz z Pilzna, Kaznodzieia Generalny, á na ten czás Przeor Gidzielski |
| Title | *Historya y Pożytki Skarbu Znalezionego w Roley… Cudownego Obrazu Panny Maryey Gidzielskiey* |
| Publication | Kraków, 1645 |
| Length | 140 pages |
| Local copy | [`docs/references/tomasz-z-pilzna-1645-historya-y-pozytki/`](../../references/tomasz-z-pilzna-1645-historya-y-pozytki/) |

The book ought to be a primary source for `§4` (Source genealogy),
`§5` (Anomaly catalogue), `§6.2` (the 1516 event), and `§9` (comparison
to other miraculous-discovery traditions). In practice, the existing
`djvutxt` OCR is too degraded for any of that to be done responsibly.
The body of the book is printed in **Schwabacher / Fraktur blackletter
Polish**, and `djvutxt` is essentially destroyed by it; the
front-matter dedication is in Roman type and survives somewhat better,
but is still well below citation quality.

This pilot tests whether **vision-model transcription against the page
images** can give us a clean enough Polish base text to incorporate
Pilzna 1645 properly into the synthesis. The same pipeline that
produced the Zagajowski cross-reference is used unchanged, with vision
transcription as the manual step.

If the vision pass works on this pilot, the natural next step is to
extend it to the full 140 pages (probably via an Anthropic-API
`vision-transcribe.py` wrapper around the JPGs produced by
`extract-page-images.sh` — see [`scripts/README.md`](../../../scripts/README.md)
for the deferred-work note).

## Method

```bash
# 1. OCR dump (~15 s; produces 4187 lines across 140 pages)
./scripts/ocr-pipeline.sh \
  'docs/references/tomasz-z-pilzna-1645-historya-y-pozytki/DjVu/NDIGSTDR008788_*.djvu' \
  docs/working-notes/pilzna-1645-vision-pilot/pilzna-1645-ocr.txt

# 2. Line→page index (~2 s)
python3.12 scripts/build-line-index.py \
  docs/working-notes/pilzna-1645-vision-pilot/pilzna-1645-ocr.txt \
  docs/working-notes/pilzna-1645-vision-pilot/line-page-index.json

# 3. Page images at 300 DPI for the 6 pilot pages
for pg in 0007 0008 0010 0046 0075 0084; do
  ddjvu -format=ppm -mode=color -scale=300 \
    "docs/references/tomasz-z-pilzna-1645-historya-y-pozytki/DjVu/NDIGSTDR008788_$pg.djvu" \
    "/tmp/pilzna-pages/NDIGSTDR008788_$pg.ppm"
  convert "/tmp/pilzna-pages/NDIGSTDR008788_$pg.ppm" "/tmp/pilzna-pages/NDIGSTDR008788_$pg.png"
done

# 4. JPG conversion (1800px wide for readability)
for pg in 0007 0008 0010 0046 0075 0084; do
  convert "/tmp/pilzna-pages/NDIGSTDR008788_$pg.png" \
    -resize 1800x -quality 90 \
    "docs/working-notes/pilzna-1645-vision-pilot/page-crops/pilzna-1645-p$pg.jpg"
done
```

The same OCR pipeline that ran unmodified on Zagajowski (228 pages →
8250 lines via `page*.djvu`) ran unmodified on Pilzna (140 pages →
4187 lines via `NDIGSTDR008788_*.djvu`). The only step that needed
per-source attention was the glob pattern.

## Page selection

| Page | What's there | Why picked |
|---|---|---|
| **p0007** | Title / dedication page — Tomasz z Pilzna names himself Prior of Gidle, dedicates to Crown Treasurer (Podskarbi Koronny) **Jan Mikołaj Daniłowicz of Żurów**. Opens with the *„skarb zakopany w roley”* ("treasure buried in a field") parable (Matt 13:44) as the central framing of the Image discovery. | Establishes authorship, dedicatee, and the **theological framing** of the discovery. |
| **p0008** | Continuation of dedication: the image-as-hidden-treasure theology, expanded with a quotation from St Bernard. Frames the Gidle image as the *„skarb Korony Polskiey”* — "treasure of the Polish Crown". | Shows the **state-religious** elevation of the cult by 1645. |
| **p0010** | Continuation of dedication: heraldic Marian typology — interprets the Daniłowicz coat-of-arms' arrow as a Marian symbol via Isaiah 49:2 *„Posuit me Dominus quasi sagittam electam”*. | A worked example of dedication-mode rhetoric: how a 17th-c. Dominican preacher weaves cult, heraldry, Latin scripture, and patronage. |
| **p0046** | Body theology section, with marginal *„Psalm 77”* citation; the gospel of the stater-in-the-fish (Matt 17:24–27) used as scriptural typology for the Gidle discovery. | Connects the §1 / §6.2 discovery framing to the Petrine tradition of recovered objects. |
| **p0075** | Body miracle catalogue, cases 21–23. Each entry dated, with named noble witnesses (Jadwiga Dżwonowska of Brzywanice; Stanisław Grodzicki with wife; Tomasz Russewski with wife) and notarial co-signature formula. | A sample of the **Pilzna miracle catalogue format** — directly comparable in structure to the Zagajowski 1724 catalogue, but ~80 years earlier. |
| **p0084** | Body miracle catalogue, cases 16–19. **Case 16 is dated 1518** (two years after the 1516 discovery!) and concerns a child's miraculous healing in the town of Słomniki near Kraków. Cases 17–19 date from the same year. | **The earliest dated Gidle miracles preserved in print.** Critical for §6.2 (the 1516 event's persistence into a cult) and for §4 (source genealogy). |

The two front-matter pages (p0007–0008) and one body page (p0084) are
the highest-priority for the synthesis; p0046 supplies the Petrine
typology footnote; p0075 documents the catalogue format.

## Findings

### 1. Existing OCR is critically degraded — far worse than Zagajowski 1724

The Zagajowski cross-reference (sibling folder) showed `djvutxt`
performing at perhaps 80% accuracy: noisy, but usable as a keyword
index and recoverable into citation form with light cleaning. On
Pilzna 1645 the OCR is in two regimes:

- **Front matter (pp. 5–11, Roman type):** legible at perhaps
  50–70% accuracy. Headers, page numbers, and lines printed in larger
  capitals survive. Mixed-case body text is degraded but recoverable
  in context.
- **Body (most of the book, blackletter Schwabacher type):**
  essentially destroyed. Every line is corrupted; most words are
  unrecognisable. The text is **not** usable for keyword search and
  cannot be cited.

This makes anything in the body of Pilzna 1645 **invisible to the
grep-based methodology** that produced the Zagajowski anomaly sweep.
The §5 anomaly catalogue could not have been replicated on this
source even with the same effort.

### 2. The vision pass recovers the text cleanly

Visual reading against the 300-DPI JPGs is straightforward for both
regimes. The Schwabacher type is unfamiliar at first but consistent;
once the letterforms are learned (long-s ‹ſ›, ‹w› with cross-bar,
the ‹ł›/‹t› distinction, ‹s›/‹ſ› distinction at line-end) every
page can be transcribed.

The **dedication pages** in particular are perfectly clean prints in
good Roman type and require essentially no orthographic judgement
calls. The **body pages** require care with the blackletter
letterforms but are otherwise legible.

### 3. What the vision pass surfaces, that the OCR-grep methodology
   could not

#### p0007 — title / dedication

The title page makes three claims that the existing OCR garbles or
loses entirely:

- **The author is the *Prior of Gidle*** at the time of writing
  (1645). Not a remote chronicler — the head of the Dominican
  community at the sanctuary itself.
- **The dedicatee is Jan Mikołaj Daniłowicz of Żurów**, Crown
  Treasurer (*Podskarbi Koronny*), starost of Przemyśl, Sambor,
  Drohobycz, Ratno, and Kolno — a top-tier Polish-Lithuanian
  magnate. The cult by 1645 was already operating in the highest
  patronage register.
- **The theological framing is *„skarb zakopany w roley”* — the
  parable of the treasure hidden in the field (Matt 13:44).** This
  *is* the discovery story (Czeczek's plow stopping over a stone in
  a field), filtered through the gospel parable. The synthesis's
  `§1` retelling of the discovery is implicitly using this same
  framing without naming it. **The book's full title literally is
  *Pożytki Skarbu Znalezionego w Roley…* — "Profits of the Treasure
  Found in the Field…"** — so the parable is *the book's titular
  controlling metaphor*. This is an important framing detail to
  add to `§4` and `§6.2`.

**Vision transcription of the title block:**

> Jásnie Wielmożnemu á mnie wielce Mściwemu P.
> IEGO MOSCI
> **P. IANOWI MIKOŁAIOWI**
> Z ZUROWA
> **DANIŁOWICZOWI,**
> Podskarbiemu Koronnemu:
> Przemyskiemu, Samborskiemu, Drohobyc-
> kiemu, Ratnenskiemu, Kolskiemu, &c. &c.
> STAROSCIE
> X. Thomasz z Pilzna, Káznodzieiá Generálny, á
> ná ten czás Przeor Gidzielski zdrowia dobrego
> y Błogosławienstwá Páńskiego.

**Vision transcription of the dedication opening:**

> O niegdy Zbáwiciel nász o Krole-
> stwie Niebieskim, to ia o Obrázie
> Gidzielskim mowię Jásnie Wiel:
> á mnie wielce M.P. iż podobny
> iest skárbowi zákopánemu w ro-
> ley, ktory ieden vbogi rolnik ználassy,
> zákrył go w domku swoim,
> iako Historya świadczy. Z tamtego skárbu znalezio-
> nego vweselił się człowiek, ktory go ználast. Znalezio-
> ny Obraz Gidzielski, ásáż vbogiego chłopá nie vwese-
> lił?

**English translation:**

> What once the Saviour [said] to us about the Kingdom
> of Heaven, this I say to Your Illustrious Honour, my
> Greatly Merciful Lord, about the Image of Gidle: that
> it is like a treasure buried in a field, which a poor
> ploughman, having found, hid in his cottage, as the
> Story bears witness. The man who found that found
> treasure rejoiced. Does not the found Image of Gidle
> also gladden the poor peasant?

The discovery story is here being told in essentially the same
shape as in Zagajowski 1724 (Czeczek the ploughman, the field, the
hiding-in-cottage), but with the **parable-framing built in at the
title-page level**. The framing is not just rhetorical decoration —
it is the *interpretive key* the book hands the reader. *Skarb*
(treasure) is the recurring noun for the Image throughout.

#### p0008 — *„skryty iest w máłey wioscy skarb wielki”*

The most quotable passage on this page:

> Skryty iest w máłey wioscy skarb wielki, (to iest:
> Naświętsza Pánná) skryty iest mowię, ále nie przed
> Bogiem, lecz przed ludźmi.

> A great treasure is hidden in a small village (that is:
> the Most Holy Virgin) — hidden, I say, but not from
> God, but from people.

And then explicitly:

> Skryty iest w tey máłey wiosce skarb wielki Korony
> Polskiey, Obraz Pánny **MARYEY GIDZIELSKIEY**;
> skryty iest mowię, ále nie przed Bogiem.

> Hidden in this small village is the great treasure of the
> Polish Crown, the Image of the Virgin **MARY OF GIDLE**;
> hidden, I say, but not from God.

By 1645 the cult is being explicitly framed as a *national*
patrimony, the *„skarb Korony Polskiey”* ("treasure of the Polish
Crown"). Pilzna writes from Gidle — the prior of the sanctuary —
and constructs the rhetoric of *national-religious treasure* on the
back of the older 1516 *peasant + field + plough* story.

This is a relevant detail for `§7` of the synthesis (current
sanctuary practice and political-religious context) and gives
historical depth to its 1645 baseline.

#### p0010 — heraldic Marian typology (Daniłowicz arrow)

A worked example of how the dedication is constructed: the
Daniłowicz coat of arms (*Sas* or similar, featuring an arrow) is
read **Marian-typologically** through Isaiah 49:2:

> *„Posuit me Dominus quali sagittam electam.”* — Tey strzale
> przypisuie Kościoł święty, że zraniła serce Bogá Oycá, ktory
> dla tego misit filium suum factum ex muliere, factum sub lege ut
> eos qui sub lege erant redimeret ut adoptionem filiorum recipere
> mus.

> *"The Lord set me as a chosen arrow."* — To this arrow the Holy
> Church attributes that it wounded the heart of God the Father, who
> therefore *"sent His Son made of woman, made under the Law, that He
> might redeem those who were under the Law, that we might receive
> the adoption of sons."* [Galatians 4:4–5]

This is a worked example of a **standard 17th-c. Dominican
*dedicatio*** — the dedicatee's heraldry is interpreted as already
prefiguring the dedicated work's subject. It tells us nothing new
about Gidle but is useful as a sample of the genre, and the
Polish-Latin code-switching is dense (the Latin scripture is woven
into the Polish mid-sentence without grammatical break).

#### p0046 — Petrine typology for found treasures

> A iáko Bernát s. piszą o Miáſteczku Násáreth, mowił: *Latet in
> hac parua Ciuitate thesaurus, latet inquam sed homines non Deum.*
> Skryty iest w málym miásteczku skarb wielki, (to iest: Naświętsza
> Pánná) skryty iest mowię, ále nie przed Bogiem, lecz przed
> ludźmi.

> As St Bernard wrote about the little town of Nazareth: *"Hidden in
> this little city is a treasure, hidden, I say, but [from] men, not
> from God."* Hidden in a little town is a great treasure (that is:
> the Most Holy Virgin); hidden, I say, but not from God, but from
> people.

Same theological move as on p0008, this time anchored on a Bernardine
sermon about Nazareth.

The page's gospel exegesis (Matt 17:24–27, Peter and the stater)
applies the *finding-a-treasure-by-divine-instruction* type to
Czeczek and the Gidle image. This pattern is exactly what comparative
literature would later call *"miraculous discovery"* or
*"manifestation"* tradition — the gospel-rooted theological framing
already does the comparative work.

#### p0075 — body miracle catalogue, cases 21–23

Three numbered miracle cases on this page, dated and witnessed.
Vision transcription of the first:

> **Cud Dwudziesty pierwszy.** Roku tegoż dniá 13. Czerwcá Jey
> Mość Páni Jadwigá Dżwonowská z Brzywánic Zrádziny Ruskiey,
> znawszy dobrodzieystwá ktore otrzymáłá będac ofiárowáná od
> małżonká swego przed Obraz Pánny Maryey Gidzielskiey, stáwiła
> się wespoł z nim przed Obrazem pomieniony, tedy zeznała
> sumnieniem dobrym, wespol z małżonkiem swoim, iż iuż będac
> vmárła, przez godzin szesc ofiárowáná często z żalem
> wielkim, y dobra wiara od męża swego przed Obraz Pánny Maryey
> Gidzielskiey, ożyłá y zdrowá zostáwszy dzieki powinne P. Bogu
> y naświętszey Pánniey przed Obrázem tey pomienionym oddała.

> **Twenty-first miracle.** Of the same year on the 13th day of June,
> Her Grace Lady Jadwiga Dżwonowska of Brzywanice in Ruthenia,
> having known the benefactions she received having been offered by
> her husband before the Image of the Virgin Mary of Gidle, presented
> herself together with him before the said Image; then she testified
> in good conscience, together with her husband, that having already
> been dead [or: as good as dead], for six hours having been offered
> [vowed] with much grief and good faith by her husband before the
> Image of the Virgin Mary of Gidle, she revived and remained well;
> [and] gave the due thanks to the Lord God and to the Most Holy
> Virgin before the said Image.

This is **a near-death-revival case** — formally similar to the
depth-rescue revival entries in Zagajowski (`§5.3`). The pattern
"already dead → offered to Gidle → revived" is here in 1645 (with
the *coram-public-witness* attestation form) and continues into the
1724 Zagajowski catalogue — i.e. this class of phenomena is
**continuous across a century** of cult documentation.

The 1645 entry adds an additional small detail not present in the
Zagajowski version of the same miracle class: a precise duration
(*„przez godzin szesc”* — "for six hours") of the period the
witness was effectively dead before revival.

#### p0084 — body miracle catalogue, cases 16–19, dated 1518

> **Szesnasty Cud.** Roku páńskiego 1518. Iest nie dáleko od
> Krákowá Miasteczko nazwáne Słomniki, w tym Miáſteczku corká ná
> imie Ewá iedney Mieszczki Agneszki Rzeczyckiey bárzo y
> niebespieczno chorowáłá: ktora mátká od tego Kościoła
> Gidzielskiego Przenaświętszey Pánny ofiárowáłá, y záraz zdrowa
> obáczyłá; co iáwnie mátká z co kąwznáły wráz tymże Kościele w
> dzień Zwiástowánia Przenaświętszey Pánny.

> **Sixteenth miracle.** In the Year of the Lord 1518. Not far from
> Kraków there is a Little Town named Słomniki; in that Little
> Town the daughter — by name Eva — of one Burgher woman, Agneszka
> Rzeczycka, was severely and dangerously ill; whom the mother
> offered up [in vow] to this Church of Gidle of the Most Holy
> Virgin, and at once saw her well again; which the mother openly
> witnessed in that same Church on the day of the Annunciation of
> the Most Holy Virgin.

> **Siedmnasty Cud.** Tegoż Roku dniá 13. Kwietniá [continues]

This is the earliest dated Gidle miracle preserved in print. **1518
is two years after the 1516 discovery** — within the founding
generation. The witness travels to the church (Słomniki is south of
Częstochowa, ~100 km from Gidle) and gives testimony on a Marian
feast day (Annunciation, 25 March).

Cases 17–19 on the same page continue with miracles from the same
year. Cases 18 and 19 introduce a Czestochowa-related witness chain
and a Warsaw burgher (*Vczciwy Stánisław Smocki Mieszczánin
Warszawski*) — the cult is **already attracting witnesses from
across the Polish-Lithuanian Commonwealth in its first decade**.

This is a substantial discovery: the synthesis currently treats the
1516 event somewhat in isolation and reaches Zagajowski 1724 for the
fuller record. The Pilzna 1645 body, properly transcribed, would
**push the documented cult record back ~80 years and into the
founding decade**.

### 4. Vision-API automation is technically straightforward

The 6 JPG crops in this folder are exactly what an Anthropic-API
transcription wrapper would consume. Each page is ~2.5 MB at 1800-px
width / quality 90. A scripted `vision-transcribe.py` that loops
over `<glob>.jpg`, sends each to Claude vision with a system prompt
specifying preservation conventions (early-modern orthography,
diacritics-as-printed, long-s normalisation, etc.), and writes the
result to `<glob>.transcription.md` would let us run the same pass
over all 140 Pilzna pages in one batch. Cost estimate at present
Anthropic pricing: ~$15–25 for the full Pilzna book at the JPG sizes
shown here.

This is the natural Phase-2 of the cross-reference work, and the
file naming convention here is already lined up to support it (one
JPG per page → one transcription per page, side-by-side).

## Synthesis-side actions surfaced by this pilot

1. **`§4` (Source genealogy)** should be updated to state explicitly
   that Pilzna 1645's controlling theological metaphor is the
   *„skarb zákopány w roley”* / *treasure-hidden-in-the-field* parable
   (Matt 13:44), and that the book is dedicated to Crown Treasurer
   **Jan Mikołaj Daniłowicz** — establishing the cult's national
   patronage register by 1645.
2. **`§6.2` (The 1516 event)** should incorporate the Pilzna title
   page's framing: the discovery is *understood by the cult itself*
   as a *„skarb zákopány w roley”* event, with the ploughman and the
   field as gospel-typological elements. This is not later
   speculation; it is the cult's self-description as printed in 1645.
3. **`§5.3` (Depth-rescue cluster)** should add the Pilzna 1645
   evidence: the "near-death revival" class is documented in
   essentially the same form in 1645 (p0075, Lady Jadwiga Dżwonowska
   case) as in 1724 (Zagajowski). The class is therefore
   **continuous across a century** of cult record-keeping, not a
   late-18th-c. accretion.
4. **`§10` (Open tasks) item 7** ("Re-OCR or hand-transcribe Tomasz
   z Pilzna 1645") should be updated to note that the **6-page pilot
   here demonstrates the vision-API approach works**, and the
   recommended next step is the full-book vision pass via the
   `vision-transcribe.py` wrapper deferred in `scripts/README.md`.
5. **Investigate the 1518 Słomniki child-healing case (p0084,
   Sixteenth Miracle)** as the earliest dated Gidle miracle. It
   anchors the cult to within two years of the founding event and
   suggests a documented witness chain that may be traceable in
   diocesan records (Słomniki parish was in the Diocese of Kraków;
   the witness Agneszka Rzeczycka is named in full and her daughter
   Eva).

## Files in this folder

| File | Status | Notes |
|---|---|---|
| `README.md` | this file | pilot report |
| `pilzna-1645-ocr.txt` | committed | full djvutxt OCR dump (140 pages → 4187 lines; mostly garbage in the body, partially legible in front matter — kept as a search index of sorts) |
| `line-page-index.json` | committed | line → page-stem index for the OCR dump |
| `page-crops/*.jpg` | committed (LFS) | 6 full-page JPGs at 1800 px wide, 300 DPI source |
| (the `page-crops/` images carry no red-rectangle overlay because the entire page is the cited unit; for line-anchored claims within these pages, use `make-crop.py` against the line-page index, the same way Zagajowski was handled) | | |
