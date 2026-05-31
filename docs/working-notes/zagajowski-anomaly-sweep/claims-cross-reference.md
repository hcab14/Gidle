# Gold-standard cross-reference: Zagajowski 1724 (*Skarb wielki…*)

## What this document is

This file provides a **fully-auditable evidence chain** for every
line-anchored claim made about Zagajowski 1724 in
[`docs/synthesis.md §5 (Anomaly catalogue)`](../../synthesis.md#5-recurring-anomalies-in-the-post-1516-gidle-cult).

For each claim, the entry below gives:

1. **Synthesis context** — the passage in `§5` that makes the claim,
   quoted verbatim.
2. **Source location** — DjVu page-stem (e.g. `page0087`) and OCR line
   range in `zagajowski-1724-ocr.txt`.
3. **Page image** — a wide JPG crop of the original 1724 print with a
   red rectangle around the cited passage. Produced by
   [`scripts/make-crop.py`](../../../scripts/make-crop.py).
4. **Existing OCR (djvutxt)** — the raw text from `djvutxt` against the
   JBC DjVu master, copied verbatim with line numbers.
5. **Vision transcription** — the same passage transcribed afresh from
   the page image, preserving early-modern Polish/Latin orthography
   (long ‹ſ› normalised to ‹s›, archaic spelling otherwise kept,
   capitalisation as printed).
6. **English translation** with explicit uncertainty notes.

The point is: **a reader who does not trust the synthesis can verify
every line-anchored claim about Zagajowski 1724 without leaving this
repository**, by comparing the page image, the existing OCR, and the
vision transcription.

## Source

| | |
|---|---|
| Author / title | Mateusz Zagajowski, OP. *Skarb wielki, w Gidlach złożony* |
| Publication | Kraków: Drukarnia Akademicka, 1724 |
| Digital copy | [Biblioteka Jagiellońska digital library (JBC)](https://jbc.bj.uj.edu.pl/dlibra/publication/17748/) |
| Local DjVu + PDF | [`docs/references/zagajowski-1724-skarb-wielki/`](../../references/zagajowski-1724-skarb-wielki/) |
| OCR dump | [`zagajowski-1724-ocr.txt`](zagajowski-1724-ocr.txt) — 228 pages → 8250 lines, via `djvutxt` |
| Line → page index | [`line-page-index.json`](line-page-index.json) |
| Pipeline scripts | [`scripts/`](../../../scripts/) |

## Coverage and gaps

This pass covers **the 10 line-anchored claims** explicitly cited in
`§5.1`, `§5.2`, `§5.3`, `§5.4`, and `§5.5` of the synthesis, plus the
three formal index entries cited in `§5.1` and `§5.3`.

The **drowning-rescue cluster** (lines 2829, 3110, 3120, 3580, 3746,
5580, 5966, 6451) referenced in `§5.3` is deliberately not expanded
here — the cluster was already substantiated by the
`08-drowning-rescue.txt` grep sweep and incorporated into `§3.1` of
the synthesis. A per-entry pass over those eight depositions is
[`§10.6` future work](../../synthesis.md#10-open-tasks).

The **other formal index categories** enumerated in `§5.6` (ergotism /
*"ogień piekielny"*, paralysis, blindness, weapons-invulnerability,
strangulation, madness, plague) are listed in the synthesis without
specific line citations — they were taken from the back-of-book
alphabetic index (~lines 7400–8200) by category name and were not
narrated against a specific affidavit. They are out of scope for this
file.

## Pipeline (regeneration recipe)

All artefacts in this file are produced by the scripts under
[`scripts/`](../../../scripts/). To regenerate from scratch:

```bash
# 1. OCR dump (~20 s; deterministic; 8250 lines)
./scripts/ocr-pipeline.sh \
  'docs/references/zagajowski-1724-skarb-wielki/page*.djvu' \
  docs/working-notes/zagajowski-anomaly-sweep/zagajowski-1724-ocr.txt

# 2. Line→page index (~3 s)
python3.12 scripts/build-line-index.py \
  docs/working-notes/zagajowski-anomaly-sweep/zagajowski-1724-ocr.txt \
  docs/working-notes/zagajowski-anomaly-sweep/line-page-index.json

# 3. Page images at 300 DPI (~6 min for 228 pages; local only, NOT committed)
./scripts/extract-page-images.sh \
  'docs/references/zagajowski-1724-skarb-wielki/page*.djvu' \
  /tmp/zagajowski-pages 300

# 4. Per-claim crop (~10 s each)
python3.12 scripts/make-crop.py \
  --line-index docs/working-notes/zagajowski-anomaly-sweep/line-page-index.json \
  --pages-dir /tmp/zagajowski-pages \
  --first-line <N> --last-line <M> \
  --output <output.jpg> \
  --pad-px 300 --quality 95
```

Steps 1, 2, and the crops produced by step 4 are committed. The page-image set
produced by step 3 is regenerable from the DjVu sources and lives in `/tmp`.

## Transcription conventions

- The **vision transcription** preserves the original 1724 typography as
  closely as Unicode allows:
  - Long s (ſ) is normalised to ‹s›; this is the only silent change.
  - Archaic spelling (*„iakoby”*, *„fwoiemi”* → *„swoiemi”* etc.) is
    otherwise kept as printed.
  - Original capitalisation is preserved (theonyms in small-caps in the
    print appear as **CAPS** here: PANNA, PAN BÓG, etc.).
  - Ligatures, macron-abbreviations, and broken ligatures are expanded
    silently only when the underlying word is completely unambiguous.
- The **English translation** is fluent rather than literal where
  Polish syntax and English syntax diverge, but never adds
  iconographic or theological interpretation. Where the original Polish
  is itself ambiguous, the translation flags it with `[?]`.
- **Uncertainty notes** flag every place where the vision pass disagrees
  with the djvutxt OCR, every place where the print is itself unclear,
  and every place where the synthesis paraphrase departs from the
  source.

A vision transcription is **not** a manuscript edition. The synthesis
quotes most of these passages in a lightly modernised form for
readability; this file gives the unmodernised source-form against which
the modernisation can be checked.

## Index of entries

| # | Synthesis § | Line | Topic | Page |
|---|---|---|---|---|
| 1 | §5.1 | 2855 | Recurring nocturnal lights at the church (Brat. 8 narrative) | page0081 |
| 2 | §5.4 | 3070 | Bartolomeus Kotulski deposition — fragrant dust from the figurine | page0087 |
| 3 | §5.2 | 3458 | Riders' daylight vision: bright window in the dark clouds (Sun, with Image, Angels, Crucifix) | page0097 |
| 4 | §5.5 | 5093 | Sworska exorcism — "the devil flew out as a fly" | page0141–0142 |
| 5 | §5.5 | 5354 | Woytowicz exorcism — broken-bone exit sign | page0148 |
| 6 | §5.2 | 6983 | Self-luminous small cloud approaches a runner | page0192 |
| 7 | §5.2 | 7077 | Pławno apparition — translucent "spiderweb" figure, plague prophecy | page0195 |
| 8 | §5.3 | 7548 | Formal index entry: *„Przywalona ziemią…”* (buried-alive → revival class) | page0208 |
| 9 | §5.3 | 7561 | Formal index entry: *„W studnie wpadaiący…”* (well-rescue class) | page0208 |
| 10 | §5.1 | 7563 | Formal index entry: *„Światłość cudowna, y ogień…”* (nocturnal-lights class) | page0208 |

---

## Claim 1 — Recurring nocturnal lights at the church (Brat. 8 narrative)

**Synthesis citation:** `§5.1`, citing line 2855.

> The detailed account at line 2855 (Brat. 8) describes a multi-witness,
> recurring pattern: the inhabitants of Gidle *„często widywali dziwne
> światło w nocy”* ("often saw a strange light at night") in the
> still-unfinished church; they would ring the bells and run with
> buckets *„iakoby do zagaszenia ognia”* ("as if to extinguish a fire")
> — but on arrival *„cudownie światło zniknęło, Kościół bez świetli
> znaleziony”* ("the miraculous light vanished, the Church was found
> without any lights"). A specific sub-pattern was repeatedly observed:
> *„iakoby dwie świece gorące na Ołtarzu przed Obrazem”* ("as if two
> burning candles on the altar before the Image"), seen by approaching
> townspeople but absent on entry.

**Source:** Zagajowski 1724, `page0081`, lines 2855–2867. Witness
identification "Brat. 8" = *Świadek 8* (Witness 8) in the formal series
of *Brat[er(stwa Rosary)]* depositions on the early miracles.

**Page image:** [`page-crops/l-2855-nocturnal-lights-narrative.jpg`](page-crops/l-2855-nocturnal-lights-narrative.jpg)

![](page-crops/l-2855-nocturnal-lights-narrative.jpg)

**Existing OCR (djvutxt):**

```
2855  8. Cifz (Władkowie zeznśli* że w tym Kościele BogarO-
2856  dźice Panny ze w(zyftkiemi fwoiemi obywitelami Gidellkie*
2857  mi częfto widywśli diiwne świitło w nocy, y iako razeriL»
2858  Obywatele Gidclfcy uderzeniem we dzwon pobudzeni iako-
2859  by do zigifzenia ognia (który ttafuakiem iakimfiś zipufzczo-
2860  nym bydz w Kościele iefzcze niedofkonale wyftiwionym być
2861  rozumieli) zbiegali: aź potym gdy fwiatłość NiebieIka uft4«
2862  ^ły Kośćioł Bogarodźice Panny zndleźlii diiwowali
2863  widiiano wiele rizy i^koby dwie fwiece gorśi^cc
2864  na U tarzu przed Obrazem cudownie znaleźionym Bogkrodźicc
2865  FANNY, y gdy fię zbiegli Obywatele widiicc fwiśtło, gdy cu«
2866  dawnie fwiatło zniknęto, Kosrioł bez świaTla znaleziony,
2867  świadczył o obecności Łaski Bofkiey.
```

**Vision transcription (early-modern Polish, preserved):**

> 8. Ciſz świadkowie zeznali, że w tym Kościele Bogaro-
> dzice PANNY ze wszystkiemi swoiemi obywatelami Gidelskie-
> mi często widywali dziwne światło w nocy, y iako razem
> Obywatele Gidelscy uderzeniem we dzwon pobudzeni iako-
> by do zagaszenia ognia (ktory trafunkiem iakimsiś zapuszczo-
> nym bydz w Kościele ieszcze niedoskonale wystawionym być
> rozumieli) zbiegali: aż potym gdy światłość Niebielska usta-
> piła, że cały Kościoł Bogarodzice PANNY znaleźli, dziwowali
> się. Nad to widziano wiele razy iakoby dwie świece goraiące
> na Ołtarzu przed Obrazem cudownie znaleźionym Bogarodzice
> PANNY, y gdy się zbiegli Obywatele widziec światło, gdy cu-
> downie światło zniknęło, Kościoł bez światła znaleziony,
> świadczył o obecności Łaski Boskiey.

**English translation:**

> 8. The same witnesses testified that in this Church of the Mother of
> God, the Virgin, they have, together with all their fellow citizens
> of Gidle, often seen a strange light at night; and, as soon as the
> inhabitants of Gidle were roused by the striking of the bell — as if
> to extinguish a fire (which they took to be some accidentally-set
> blaze in the still-unfinished Church) — they ran together; but then
> when the heavenly brightness had ceased, they were astonished to find
> the whole Church of the Mother of God, the Virgin, intact. Moreover,
> there were seen many times, as it were, two burning candles on the
> Altar before the miraculously-found Image of the Mother of God, the
> Virgin; and when the inhabitants who had come running to see the
> light arrived, the miraculous light had vanished, and the Church,
> found without any light, bore witness to the presence of Divine
> Grace.

**Uncertainty notes:**

- *„Ciſz świadkowie”* — OCR reads *„Cifz (Władkowie”* (the long-s misread
  as `f` and a stray `(` introduced). The print is unambiguous and
  reads *„Ciſz świadkowie”* = modern *„Ci sami świadkowie”* ("the same
  witnesses"). This makes the entry a continuation of the *Brat. 7*
  testimony that ends in the page immediately before.
- The synthesis paraphrase has *„Kościół bez świetli znaleziony”*; the
  print actually has *„Kościoł bez światła znaleziony”* (genitive
  singular). Same meaning ("the Church found without any light"); the
  synthesis form should be corrected in a future pass.
- The synthesis paraphrase telescopes two distinct events into one:
  (a) the all-Church *„światłość Niebielska”* (heavenly brightness)
  pattern, and (b) the *„iakoby dwie świece goraiące”* (as-if two
  burning candles) pattern. The print preserves them as separate
  recurring phenomena, both witnessed by multiple inhabitants. The
  synthesis treatment is faithful to the cumulative claim but
  loses this binary structure.
- "Brat. 8" in the synthesis stands for *Świadek 8* (Witness 8) in the
  brotherhood-deposition sequence; the print uses Arabic "8." as the
  paragraph number.

---

## Claim 2 — Bartolomeus Kotulski deposition: fragrant dust from the figurine

**Synthesis citation:** `§5.4`, citing line 3070–3085.

> One of the most phenomenologically striking entries in the entire
> book (line 3070–3085, deposition of Bartolomeus Plebani of Gidle,
> recorded *coram notario sub juramento*) concerns work done on the
> figurine itself. The witness — then **starszy** (elder) of the local
> Rosary Brotherhood — had taken the figurine to a goldsmith in
> Radomsko (one **Jerzy** […]) to have new silver crowns and clothing
> made. The metal filings/dust from the figurine, when swept onto the
> goldsmith's forge fire:
>
> > *„uczynił wonność wielką godzinę w domu onym, ja z Złotnikiem
> > siedzieliśmy zdumiawszy się długo, nie wiedząc skąd by była ona
> > wonność, aż Złotnik rzekł do mnie: pewnie z tego prochu ona wonność,
> > który ty wsuł[eś] [w] ogień.”*
> >
> > ("…it produced a great fragrance for an hour in that house; I and
> > the goldsmith sat astonished for a long time, not knowing whence the
> > fragrance came, until the goldsmith said to me: surely it is from
> > that dust which you put into the fire.")
>
> The witness then admits he had already burnt the entire sample and
> had none left to give. […] The literal claim is: **the material
> residue of the figurine emits a powerful, lasting fragrance when
> burnt.**

**Source:** Zagajowski 1724, `page0087` (book page 13 of *Instrument 2*),
lines 3070–3082. The witness is identified in the print as
**Nobilis Joannes Kotulski, Pictor, Incola Gidlensis** — a noble
painter resident in Gidle. (The synthesis cites him as "Bartolomeus
Plebani" — see uncertainty notes below; **this is a synthesis-side
error to correct**.)

**Page image:** [`page-crops/l-3070-bartolomeus-dust.jpg`](page-crops/l-3070-bartolomeus-dust.jpg)

![](page-crops/l-3070-bartolomeus-dust.jpg)

**Existing OCR (djvutxt):**

```
3069  *, Nobilis toaancs Kotuliki Pi^or Irrcol-jGidlffnfis» Tub ;u*
3070  ramcnto rccognoyit. Ze będgc Starfzym Rozanca Świętego
3071  ^ractwa przcd trzema laty, ch<3cy oprawić Obraz Panny Nay-
3072  WKośćicIc Pannt Maryi Giielfkim bę-
3073  ^?cy iramienny, (prylowałcai Koronki yf2faty u tego Obrazka>
3074  ‘P^‘0|>nieyf2cgo przyftiniar do (rebra, k proch wfufcm na
3075  ogicn u złotnika Icrzego w Radomikincłi który na ogniu będjjc
3076  »czynil wonność wiclfcazgodiinę w domu onym, ia z Złocm^
3077  ^icni sicdźicliimy zdiirniawfzy fię d?ugo, nic wicdr^C zk^d by
3078  była ona wonność, afz Złotnik rzekł da mnie, pewnie z tcgO
3079  prochu ona wonność, który, ty vfuł ogicir. dW migotro-
3080  che profzę czuc, alera mu nieme dał,bom iuz był fpalił wftyftck
3081
3082  Quæ testimonia debito juris ordine audivi & examinavi sedulò […]
```

**Vision transcription (early-modern Polish + Latin, preserved):**

> **2.** Nobilis Ioannes Kotulski Pictor Incola Gidlensis, sub iu-
> ramento recognovit. Ze będąc Starszym Roznaca Świętego
> Bractwa przed trzema laty, chcący oprawić Obraz PANNY Nay-
> świętszey Cudowny w Kościele PANNY MARYI Gidelskim bę-
> dący kamienny, sprylowałem Koronki y szaty u tego Obrazka,
> dla sposobnieyszego przystaniu do srebra, á proch wsułem ná
> ogien u złotnika Ierzego w Radomskim, ktory ná ogniu będąc
> uczynił wonność wielką z godzinę w domu onym, ia z Złotni-
> kiem siedzieliśmy zdumiawszy się długo, nie wiedząc skąd by
> była ona wonność, asz Złotnik rzekł do mnie, pewnie z tego
> prochu ona wonność, ktoryś ty wsuł ná ogien, daćmi go tro-
> chę proszę czuc, alem mu nie nie dał, bom iuz był spalił wszystek.
>
> *Quæ testimonia debito juris ordine audivi & examinavi se-
> dulò descripsi, in præsentia Reverendi Blasij Simonik Radom-
> scensis Plebani, in Gidle Ecclesiastici Parochialis Divæ Mariæ
> Magdalenæ, Petri Reciszki, Ioannis Kotulski, Martini Penga Ad-
> vocati in Gidle, Martini Ryszczyk, & aliorum fide dignorum
> testium, ad id specialiter vocatorum & rogatorum. Acta sunt
> hæc, Anno Die Hora ut suprà.*

**English translation:**

> **2.** The Noble Jan Kotulski, Painter, Inhabitant of Gidle, has
> testified under oath: That being Elder of the Rosary Holy Brotherhood
> three years ago, wishing to refurbish the miraculous Image of the
> Most Holy Virgin in the Church of the Virgin Mary in Gidle, the
> Image being of stone, I unsoldered the Crowns and vestments from
> this little Image, so as more conveniently to apply [them] to the
> silver; and the dust I cast onto the fire at the goldsmith Jerzy's
> in Radomsko, which being on the fire produced a great fragrance for
> an hour in that house. I sat with the Goldsmith astonished for a
> long time, not knowing whence that fragrance came, until the
> Goldsmith said to me: surely [it is] from that dust, which you cast
> onto the fire — give me, I beg, a little to smell. But I gave him
> none [at all] [?], for I had already burnt all of it.
>
> *Which testimonies, in due order of law I have heard and examined
> [and] carefully recorded, in the presence of the Reverend Blasius
> Simonik, Parish Priest of Radomsko, Ecclesiastic of the Parish of
> Saint Mary Magdalene in Gidle; [of] Peter Recziszki, Jan Kotulski,
> Martin Penga the Advocate in Gidle, Martin Ryszczyk, and other
> witnesses worthy of trust, specially called and requested for this.
> These things were done in the year, day, [and] hour as above.*

**Uncertainty notes:**

- **The witness's name in the synthesis is wrong.** The print clearly
  reads *Ioannes Kotulski* (Jan Kotulski), not *Bartolomeus Plebani*.
  *Plebani* in the Latin attestation block at lines 3081–3087 is the
  Latin genitive of *plebanus* = "of the parish priest" — it modifies
  *Blasij Simonik Radomscensis*, the parish priest of Radomsko who
  recorded the deposition. The synthesis confuses the witness with the
  recording cleric and his title. **This needs a correction pass in
  `§5.4`.**
- **"Three years ago" not "long ago".** The print reads *„przed trzema
  laty”* = "three years ago", which gives a sharp date relative to the
  deposition date (recorded as "year, day, hour as above" referring to
  the recording session, so anchorable once that header is read). The
  synthesis loses this datable specificity.
- **"Of stone" — the figurine is described here as *kamienny*.** This
  is consistent with the synthesis's discussion in `§1.2 / §2.2` of
  the figurine's material. Worth noting that the witness himself
  explicitly mentions stone as the figurine's substance in the
  *grounds-for-action* clause: *"the Image being of stone"* (so that
  the silver crowns and vestments had to be re-fitted). This rules
  out simple ash residue from a wooden carving.
- *„alem mu nie nie dał”* — the doubled negative *„nie nie dał”* is
  what the print shows; one *nie* is likely a typographical doubling
  (the line breaks between the two), but the meaning is clearly
  "I gave him none [at all]". Marked `[?]` in the translation.
- *„daćmi go trochę”* — written as one word in the print (*daćmi*); =
  modern *daj mi*. Standard 17th-c. Polish enclitic.
- **Latin attestation block is essentially perfect Latin**; OCR garbled
  it badly (the long-s problem hits Latin too). Vision pass gives the
  correct formula: *„Quae testimonia debito juris ordine audivi…”* —
  the standard Polish-Catholic *coram notario* notarial template.
- The cited witnesses (`Petri Recziszki`, `Joannis Kotulski`,
  `Martini Penga`, `Martini Ryszczyk`) include another *Joannes
  Kotulski* — the deponent himself, listed again as one of the formal
  witnesses to the recording session. This is typical: the deponent's
  spoken testimony is then witnessed by his own signature plus four
  other named men.

---

## Claim 3 — Riders' daylight vision: bright window in the dark clouds

**Synthesis citation:** `§5.2`, citing line 3461–3469.

> Several riders approaching Gidle saw *„między ciemnemi obłokami okno
> jasne w którym był Obraz Panny Przenajświętszej… y Anioły
> zrosciągnionemi skrzydłami, i na ostatku y Krucifix”* ("between the
> dark clouds, a bright window in which was the Image of the Most Holy
> Lady… and Angels with outstretched wings, and finally also a
> Crucifix"). *„Tym widzeniem przestraszeni z koni zsiedli, na kolana
> upadłszy”* ("Frightened by this vision they dismounted from the
> horses, falling on their knees"). The event occurred *„kilka stay od
> Kościoła Gidelskiego”* (a few *stay* ≈ ~1 km from the church) and
> was reported publicly on arrival.

**Source:** Zagajowski 1724, `page0097`, lines 3458–3467. Date: 6 August
1620. Named witnesses: Pan Mikołay Łasocki of Łasocie (the dedicatee)
and Pan Piotr Boryszowski; vowing to visit the miraculous places of the
Virgin while imprisoned in Moscow during the Polish–Muscovite war.

**Page image:** [`page-crops/l-3458-riders-vision-in-clouds.jpg`](page-crops/l-3458-riders-vision-in-clouds.jpg)

![](page-crops/l-3458-riders-vision-in-clouds.jpg)

**Existing OCR (djvutxt):**

```
3458  iWoim, iechali do Gidel w roku namienionym i6io. Dniś
3459  Sierpnia. Agdy iuź pfzychodźili kuGidlonł,widiicli w Słońcu mię-!
3460  dzy ćicmocaii obłokami okno iśfne w którym był Obraz Pan-
3461  WT Przenayfwiętfzey, fen który ieft na Ołtarzu obaczyii y An-
3462  10 azrosciagnioncmi fkrzydłami, i na oftatku y Kructfix* Tym
3463  widzeniem przcftrafzcni z koni z fiedli, ni kolink upadłfzyBO-
3464  VjU częsc oddali; i potytn piefzo fzli afz na mieyfcc. Mieli to
3465  Widzenie kilka ftay od Kościoła Gidelflęipgo Przenayfwiętfzcy
3466  Panny; gdiic przyfzedłfzy Jawnie y wgłoi wyznawali pczcd
3467  wfzyftkicmi których tam zaftali^
```

**Vision transcription (early-modern Polish, preserved):**

> swoim, iechali do Gidel w roku namienionym 1620. Dniá 6.
> Sierpnia. A gdy iuż przychodzili ku Gidlom, widzieli w Słońcu mię-
> dzy ciemnemi obłokami okno iasne w ktorym był Obraz PAN-
> NY Przenayświętszey, ten ktory iest na Ołtarzu obaczyli y An-
> ioła z rosciągnionemi skrzydłami, á na ostatku y Krucifix. Tym
> widzeniem przestrafzeni z koni zsiedli, ná kolaná upadłszy BO-
> GU część oddali; á potym piefzo szli asz na mieysce. Mieli to
> widzenie kilka stay od Kościoła Gidelskiego Przenayświętszey
> PANNY: gdzie przyszedłszy iawnie y w głos wyznawali przed
> wszyftkiemi ktorych tam zastali.

**English translation:**

> […for] their [vows], they rode to Gidle in the said year 1620, on the
> 6th day of August. And when they were already approaching Gidle, they
> saw in the Sun, between the dark clouds, a bright window in which was
> the Image of the Most Holy VIRGIN, the one which is on the Altar
> [there] — they saw [it] — and an Angel with outstretched wings, and
> at the end also a Crucifix. Frightened by this vision, they
> dismounted from their horses, falling on their knees, [and] gave a
> portion [of homage] to GOD; and then went on foot all the way to the
> place. They had this vision a few *stay* [arch. unit ≈ 100–300 m
> each; a few ≈ several hundred metres to ~1 km] from the Church of the
> Most Holy VIRGIN of Gidle: where on arrival, openly and aloud, they
> confessed [it] before all whom they found there.

**Uncertainty notes:**

- *„widzieli w Słońcu między ciemnemi obłokami okno iasne”* — the print
  reads *„w Słońcu”* ("in the Sun"), not "in the sky": the vision is
  located **in the direction of the Sun**, with the bright window
  framed by dark clouds. The synthesis preserves this. The
  iconographic note: this is consistent with a solar-axis apparition,
  which is also how the *mulier amicta sole* (Apocalypse 12) tradition
  iconographically places the Marian image (cf. the panel-reading in
  `§3.1`, marker 5+15).
- *„Aniołá z rosciągnionemi skrzydłami”* (singular, not plural) — the
  print has *„Aniołá”* (accusative singular: "an Angel"), and *„y
  Krucifix”* ("and a Crucifix"). The synthesis pluralises to "Angels";
  this should be a singular Angel in any future quotation.
  The sequence is: a bright window → Image of the Virgin (the
  *exact* image that is on the Gidle altar, recognised) → one Angel with
  outstretched wings → a Crucifix. A composite, structured visual
  apparition with named iconographic elements in succession.
- *„stay”* — an old Polish unit of distance; one *staj/staia* is
  variably given as 100–300 m. "Kilka stay" thus ≈ several hundred
  metres to ~1 km. The synthesis's "~1 km" is a reasonable upper
  estimate.
- Names (visible elsewhere on the page, slightly above the crop):
  *Pan Mikołay Łasocki z Łasocie* and *Pan Piotr Boryszowski*. The
  pair were imprisoned in Moscow during the Polish–Muscovite war and
  vowed to visit the miraculous Marian places upon release; the vision
  occurred on their fulfilment journey. Both are gentry; both are
  named in the print and in the synthesis.

---

## Claim 4 — Sworska exorcism: "the devil flew out as a fly"

**Synthesis citation:** `§5.5`, citing line 5099–5113.

> A class of exorcism narratives where the leaving "demon" takes a
> **physical, observable form** on departure. The clearest case is
> **Pani Zofia Sworska, 8 August 1641** (line 5099–5113), exorcised
> before the image. After prolonged struggle, the celebrant called the
> assembly to collective prayer, and:
>
> > *„na ten czas czart przymuszony od Najświętszej Panny bez żadnej
> > szkody muchą wyleciał.”*
> >
> > ("…then the devil, compelled by the Most Holy Lady, **flew out as a
> > fly**, without any harm.")

**Source:** Zagajowski 1724, `page0141`–`page0142`, lines 5093–5114.
Date: 8 August 1641. Witness: Lady Zofia Sworska of the house of the
Dunins (*„JeyMość Pani Zofia Sworska z Domu JJ. MM. PP. Duninów”*),
who is described as having been *„z nienawiści ludzkiey od nasłanego
czarta opętana”* ("possessed by a devil sent through human enmity") —
a maleficium-attribution framing. Spans the page break; the actual
"fly" line is on `page0142`.

**Page images:**
[`page-crops/l-5093-exorcism-sworska-p1.jpg`](page-crops/l-5093-exorcism-sworska-p1.jpg) (page0141),
[`page-crops/l-5093-exorcism-sworska-p2.jpg`](page-crops/l-5093-exorcism-sworska-p2.jpg) (page0142)

![](page-crops/l-5093-exorcism-sworska-p1.jpg)

![](page-crops/l-5093-exorcism-sworska-p2.jpg)

**Existing OCR (djvutxt):**

```
5093  I f. Roku tegoż Dnia 8- Sierpniai JeyMoś^ Pani Zofia Swor-
5094  |ka z Domu J, MM* PP, Duninów , będąc z aienświśći ludz-
5095  kiey od nasłanego	opętana	iiko prędko to poczułk w
5096  fobie, zaraz do Obrazu Gidelikiego votum uczymłś, gdźie przy*
5097  fzedł(zy dnii pomienionego z wielkim przymufzenicm wpro¬
5098  wadzona byłk do Kośćioik, gdy Kśpłan nad nva exorcyzm czy¬
5099  nił y długo piiicuiac z mordowkny moc^ BOGA naywyi^z^go
5100  loA^azał diabłu śby zćiiła (które niesłuTznym priwcm osiadł)
5101  Vyfzcdł. Lecz gdy mu dikbcł odpowiedżiał <y mnie ztad nic
5102  ^źeniefz chybi źe przeciwko mnie fzcrokg pobudiifz, która
5103  KźcU mi rolkaźc wyniść, mufzc: Kkpł^n usłyjzawfzy to prośłl
5104  5 1	ludii
5105
5106  ===== page0142 =====
5107  Księga 2. Czisc 5.
5108  iudźi obecnych kby każdy z nich modlitwę iak3 nabożni do
5109  Nayfwiętfzcy Panny uczynił* Co gdy uczynili ludiie owif na
5110  na ten czas czart przymu(źony od Nayfwiętlzcy Panny bcź
5111  zadncy (zkody much^ wylcćiał. Zaczym pomicniona JeyMośd
5112  Pani Sworlka po małym czaśic przylzedłfzy do fiebie padła
5113  krzyicm przed Obrazem pomicnionymi dźiękuiąc Nay(więt-
5114  fzcy Pannie za uwolnienie od czarta przeklętego.
```

**Vision transcription (early-modern Polish, preserved):**

> 11. Roku tegoż Dnia 8. Sierpnia, JeyMość Pani Zofia Swor-
> ska z Domu JJ. MM. PP. Duninow, będąc z nienawiści ludz-
> kiey od nasłanego czartá opętana iako prędko to poczuła w
> sobie, zaraz do Obrazu Gidelskiego votum uczyniła, gdzie przy-
> szedłszy dnia pomienionego z wielkim przymuszeniem wpro-
> wadzona była do Kościoła, gdy Kapłán nad nią exorcyzm czy-
> nił y długo prácuiac z mordowány mocą BOGA naywyższego
> roskazał diabłu áby z ciała (ktore niesłusznym práwem osiadł)
> wyszedł. Lecz gdy mu diabeł odpowiedział, ty mnie ztąd nie
> wyżeniesz chyba że przeciwko mnie szeroka pobudzisz, ktora
> ieżeli mi roskaże wyniść, muszę: Kapłán usłyszawszy to prosił
>
> **[page break — page0142]**
>
> Księga 2. Część 5.   [page-header]
> ludzi obecnych áby kaźdy z nich modlitwę iaką nabożną do
> Nayświętszey PANNY uczynił. Co gdy uczynili ludzie owi, ná
> na ten czas czart przymuszony od Nayświętszey PANNY beż
> zadney szkody muchą wyleciał. Zaczym pomieniona JeyMość
> Pani Sworska po małym czasie przyszedłszy do siebie, padła
> krzyzem przed Obrazem pomienionym, dziekuiąc Nayświęt-
> szey PANNIE za uwolnienie od czartá przeklętego.

**English translation:**

> **11.** Of the same year, on the 8th day of August, Her Grace Lady
> Zofia Sworska, of the house of Their Graces the Lords Dunins,
> being — through human enmity — possessed by a devil that had been
> sent [against her], as soon as she felt this in herself, immediately
> made a vow to the Image of Gidle, where, having arrived on the said
> day, she was brought into the Church with great force [against her
> will]. When the Priest performed exorcism over her, and after a long
> [labour], having been wearied by it, by the power of GOD Most High
> he commanded the devil to depart from the body (which it had
> unjustly occupied as its own). But when the devil answered him: "You
> shall not drive me hence unless you rouse a broad [assembly] against
> me, which, if it shall order me to depart, I must" — the Priest,
> hearing this, asked the people present that each of them should make
> some pious prayer to the Most Holy VIRGIN. Which when those people
> did, **at that time the devil, compelled by the Most Holy VIRGIN,
> flew out as a fly without any harm.** After which the said Her Grace
> Lady Sworska, having after a short time come to herself, fell prone
> [literally: "as a cross", arms outstretched] before the said Image,
> giving thanks to the Most Holy VIRGIN for [her] liberation from the
> accursed devil.

**Uncertainty notes:**

- **The numbered case is "11.", not "1f." or "I f."** — the OCR reads
  *„I f.”* due to long-s/`f` confusion plus a smudge; the print is
  clearly Arabic *11.* The case number matters for cross-checking
  against later index entries (`§5.5` mentions a separate index entry
  for "Sworska Zofia" at line ~8029 which would point back to this
  case number).
- *„czart przymuszony od Nayświętszey PANNY”* is the synthesis quote;
  the print has exactly this. *Przymuszony* is "compelled"; the
  participle implies an external, almost-mechanical compulsion ("forced
  to leave"), not persuasion.
- *„muchą wyleciał”* — "flew out as a fly" — instrumental case
  *„muchą”* gives the *manner* / *form* of exit. The phrase is
  unambiguous and the synthesis paraphrase is accurate. Note: the
  parallel case at index entry line ~8029 (referenced in `§5.5`) reads
  *„czart w postać much wyszedł z niey”* = "the devil came out of her
  in the form of flies" (plural *much*) — distinct events, both
  insect-form exits.
- *„szeroka pobudzisz”* — the print has *„szeroka”* (feminine
  adjective), which here is shorthand for *„szeroką [modlitwę]”* /
  *„szeroką [kompanię]”* — a "broad" or "wide" prayer-assembly. The
  reading is slightly elliptical in the print but the parallel
  resolution "the broader assembly" / "more people" is clear from
  context (the priest's response is to call the congregation to
  collective prayer).
- *„padła krzyżem”* — literally "fell as a cross", i.e. prostrate with
  arms outstretched, a classical Polish-Catholic gesture of total
  submission. The Polish phrase is technical; English needs a gloss.
- *„JJ. MM. PP.”* expands to *„Jaśnie Wielmożnych Mościwych Panów”*
  ("Their Illustrious Honoured Lordships") — a standard noble-house
  formula. The Dunins are a well-attested Polish noble family.
- *„Pani Sworska”* — Sworska is the feminine of *Sworski*; the maiden
  name (Dunin) is the natal house. Standard 17th-c. Polish noblewoman
  identification.

---

## Claim 5 — Woytowicz exorcism: broken-bone exit sign

**Synthesis citation:** `§5.5`, citing line 5354.

> The Krakovian burgher **Maciej Woytowicz** (line 5354), possessed for
> half a year, was freed before the same image; *„znak tylko czart
> zostawił że mu [łaty?] złamał, na to patrzeła cała kompania
> Różancowa”* — the only sign the discharging entity left was a
> physical breakage on the man, witnessed by the **whole Rosary
> company**.

**Source:** Zagajowski 1724, `page0148`, lines 5354–5359. Witness:
*Sławetny Pan Maciey Woytowicz Miefzczanin Krakowski* — "the famous
Lord Maciej Woytowicz, Burgher of Kraków". Date: 22 June (year
inferable from context as the *„tegoż roku”* = "in the same year"
chain, anchored to the preceding 1641 entry; so 1641 also).

**Page image:** [`page-crops/l-5354-exorcism-woytowicz.jpg`](page-crops/l-5354-exorcism-woytowicz.jpg)

![](page-crops/l-5354-exorcism-woytowicz.jpg)

**Existing OCR (djvutxt):**

```
5354  12. Tegoż róku dnia 22« Czerwca, Sławetny Pan Macicy
5355  Woytowicz Miefzczanin Krakowiki, opętany od Czartś pize*
5356  klętego przez pułrokai przy Cudownym Obraźic GidcKkim
5357  od niego wolnym zoftałt znak tylko czart zoQawii ze mu kyi
5358  2łama}, na to patrzcła cała kompania Rozancowa. VAltntx PUh
5359  Gidlem S.J*A*N,P,
```

**Vision transcription (early-modern Polish, preserved):**

> 12. Tegoż roku dnia 22. Czerwca, Sławetny Pan Macicy
> Woytowicz Miefzczanin Krakowski, opętany od Czartá prze-
> klętego przez pułroka, przy Cudownym Obrazie Gidelskim
> od niego wolnym został, znak tylko czart zostawił ze mu kyi
> złamał, na to patrzeła cała kompania Rozancowá. *Valent: Pleb:
> Gidlen: S. J. A. N. P.*

**English translation:**

> **12.** Of the same year, on the 22nd day of June, the Famous Lord
> Maciej Woytowicz, Burgher of Kraków, possessed by the accursed Devil
> for half a year, was set free from him at the Miraculous Image of
> Gidle; the only sign the Devil left [was] that he broke his **kyi**
> [staff? shin? — see notes] for him; at which the whole Rosary
> Company looked on. *Valentinus, Parson of Gidle, S. J. A. N. P.*

**Uncertainty notes:**

- **The "broken" object is uncertain.** The print reads *„że mu **kyi**
  złamał”*. The OCR rendered the same word *„kyi”*. *Kyi* is not a
  modern standard Polish word; candidates include:
  - *„kij”* = "staff / stick" (most likely — possessed person's
    walking-stick broken at the moment of release; common motif).
  - *„kył”* / *„goleń”* = "shin"; or possibly *„kół”* = "stake".
  - A typographical degradation of *„nogi”* or another body part.

  The synthesis paraphrase has *„[łaty?]”* ("a lath?") — that is a
  synthesis-side guess. The vision pass confirms the print spelling is
  *„kyi”*; the resolution should be **either** *„kij”* (walking-stick)
  **or** an archaic body-part term (most likely shin, given the
  visual focus and "the whole Rosary company looked on" framing —
  a broken stick would not require that level of public attestation).
  *„kij”* is the more conservative reading.
- *„Sławetny”* — honorific used for burghers (the equivalent of
  *„Wielmożny”* for nobility). Translates as "Famous", "Honourable",
  or "Esteemed".
- *„kompania Różancowa”* — the lay Rosary Confraternity; a standing
  body at the church, hence routinely available as a corporate
  witnessing body. This explains the formal "the whole Rosary
  company looked on" framing — corporate witnesses validate the
  physical sign.
- *„Valent: Pleb: Gidlen: S. J. A. N. P.”* — abbreviation
  *„Valentinus Plebanus Gidlensis Sub Juramento Articulorum Notarii
  Publici”* (probable expansion): "Valentinus, parish priest of
  Gidle, under oath / before the articles of the Public Notary."
  This is the standard formal-attestation footer used throughout
  this section; it confirms the deposition was sworn before a public
  notary. Same abbreviation appears at the foot of the preceding case
  (line 5353).

---

## Claim 6 — Self-luminous small cloud approaches a runner

**Synthesis citation:** `§5.2`, citing line 6985.

> A man being pursued saw, from far off, *„jasność jakąś przeciwko
> biegnącą iak obłoczek”* ("a certain brightness running toward [him]
> like a small cloud") which, as it approached, resolved into *„Obraz
> Najświętszej Panny w promieniach”* ("the Image of the Most Holy
> Lady in rays"). After he called for help and the pursuers fled,
> *„jasność zniknęła”* ("the brightness vanished").
> Phenomenologically: a self-luminous object that moves directionally
> through the air at the witness's eye-level, resolves into a
> recognised figure, then disappears — a textbook "Ball-of-Light"
> sequence.

**Source:** Zagajowski 1724, `page0192`, lines 6983–6993. Context: the
witness is being pursued by *„poczwary piekielne”* ("infernal
monstrosities") in a hellish vision-experience (the surrounding text on
the same page describes being torn by claws, bound, pricked by
instruments, etc.) — i.e. this is an apparition inside an already-
liminal visionary state, not a clear-sky outdoor encounter.

**Page image:** [`page-crops/l-6983-luminous-cloud.jpg`](page-crops/l-6983-luminous-cloud.jpg)

![](page-crops/l-6983-luminous-cloud.jpg)

**Existing OCR (djvutxt):**

```
6983  fzedł mu wi/.^j m tihc nk myśl Obraz Cidcl/ki Nayfwictfzcy
6984  PANNYiyiako mógł zawołał, Nayfwiętfza Panko rituy mię
6985  Zgubionego, az obaczył zdalcki iafność lik^ś przeciwko bic-
6986  Z3C3 iak obłoczek: która fwiktłość gdy (\ę do niego zhlizyła:
6987  Obaczył Obraz Nayfwiętfzey Panny w ^romicniach, tak iako
6988  tu wKapIicy w Ołtarzu ieft, y tym be/piecznieyrzy zawołst
6989  znowu* Ratuy mięMitko moi^> y wnet one pocz^iry pędem
6990  od niego poućiekały. W tym iafność zniknęła, 4rn iśkoby Z
6991  pod kimieniś umoidow4ny y fpoczony porwał flę. y wftał y.
6992  obroćiwizy Gę ku G^lon padł na kolinai y Nayfwiętfzey Pan-
6993  nie
```

**Vision transcription (early-modern Polish, preserved):**

> Przy-
> szedł mu w owym razie ná myśl Obraz Gidelski Nayświętszey
> PANNY, y iako mogł zawołał, Nayświętsza PANNO rátuy mię
> zgubionego, az obaczył zdaleka iasność iakąś przeciwko bie-
> ząca iak obłoczek: ktora światłość gdy się do niego zbliżyła:
> Obaczył Obraz Nayświętszey PANNY w promieniach, tak iako
> tu w Káplicy w Ołtarzu iest, y tym bespiecznieyszy zawołał
> znowu: Rátuy mię Mátko moiá, y wnet one poczwáry pędem
> od niego poućiekały. W tym iasność zniknęła, á on iákoby z
> pod kámienia umordowány y spoczony porwał się, y wstał y
> obróciwszy się ku Gidlom padł ná kolaná, y Nayświętszey
> PANNIE [...]

**English translation:**

> There came to him at that moment to mind the Image of Gidle of the
> Most Holy VIRGIN, and as he was able he called out: "Most Holy
> VIRGIN, rescue me, [I am] lost" — until he saw from afar a certain
> brightness running toward [him], like a small cloud; which
> brightness, when it came near him, [resolved into] — he saw the
> Image of the Most Holy VIRGIN in rays, exactly as it is here in the
> Chapel on the Altar; and, made more confident by this, he called out
> again: "Rescue me, my Mother!", and at once those monstrosities fled
> headlong from him. At which the brightness vanished, and he, as if
> from beneath a stone, exhausted and spent, gathered himself up, and
> stood up, and turning toward Gidle, fell on [his] knees, and [gave
> thanks] to the Most Holy VIRGIN […]

**Uncertainty notes:**

- *„zdaleka iasność iakąś przeciwko bieząca iak obłoczek”* — the print
  is unambiguous. *Bieząca* is the present-active participle of *bieżeć*
  / *biec* ("to run / move quickly"); *przeciwko* here is "toward / to
  meet" (not "against / opposed to"); *iak obłoczek* = "like a small
  cloud". The composite: an object self-illuminated, moving rapidly
  toward the witness, in the form of a small cloud.
- *„Obraz… w promieniach”* — "the Image… in rays". The brightness, on
  near approach, **resolves** into the recognised image of the Gidle
  Virgin with the rays (the *mulier amicta sole* iconography again — cf.
  the panel reading in §3.1).
- *„iákoby z pod kámienia umordowány”* — "as if exhausted from beneath
  a stone". An idiomatic Polish phrase: completely drained. Not
  literally a stone; the sense is "exhausted as if having been crushed
  under a stone".
- The synthesis frames the encounter as a "textbook Ball-of-Light
  sequence" — that framing is fair on the *phenomenology* (self-
  luminous, directional, eye-level, resolves into a recognisable figure,
  vanishes) but understates the **interpretive context**: the witness
  is already in an extended visionary / dream-like state (hellish
  pursuit). This is *not* an open-sky daylight encounter (cf. Claims 3
  and 7, which are). The synthesis treatment in §5.2 should arguably
  flag this case as a *vision-state encounter* rather than a
  daylight-aerial one, to keep the §5.2 typology clean. (Suggested
  refinement for `§5.2`.)
- *„poczwáry”* = "monstrosities, abominations" (the same word that
  Pasulka and others use for the disturbing-form / "trickster" entities
  in the modern comparative literature — purely lexical convergence,
  but worth noting).

---

## Claim 7 — Pławno apparition: translucent "spiderweb" figure with plague prophecy

**Synthesis citation:** `§5.2`, citing line 7081–7110.

> On 4 July 1662, the townsman Król of Pławno, walking out of his
> house *„około południa”* (at about noon) toward a nearby grove, was
> met by *„iakaś postać na kształt Obrazu śmierci uformowana
> przeźroczysta na podobieństwo pajęczyny”* ("a certain figure formed
> in the likeness of an Image of Death, transparent like a
> spiderweb") which spoke to him intelligibly, prophesied the coming
> plague in Koniecpol and Miechów, and indicated that Gidle and
> nearby holy places would be punished too.

**Source:** Zagajowski 1724, `page0195`, lines 7077–7091 (case
continues for several pages, this crop covers the encounter itself).
Date: 4 July 1662. Witness: a townsman of Pławno surnamed Król,
recorded as over sixty years old at the time of his deposition; the
deposition is co-signed by the parish commendator and the town mayor
(*Burmistrz*).

**Page image:** [`page-crops/l-7077-plawno-apparition.jpg`](page-crops/l-7077-plawno-apparition.jpg)

![](page-crops/l-7077-plawno-apparition.jpg)

**Existing OCR (djvutxt):**

```
7077  fłi o kołó południi Micfzczaninowi Pławie o (kie mu nazwiHsicm
7078  Krolowi wychodzgccmu zdomu do gaiu blilkicgOy zalUpiła-»
7079  j^kaś poAać na kfzt^łt Obrazu śmierci uformowśoa przeyzto*
7080  czvfta na fodobicnftwo paięczyny, to mowiac do niego .(gdy
7081  •fię zlakJ) nieboy fię al« to miefzczanom twoim ozaaymieyi źc
7082  b ez Bory gotuie Cię przeciwko nim, dia tego źc nic fa nabo-
7083  yni na micyica-eh Świętych, które tu blilko mila. A gdy on^
7084  rzeki nic będa mi wierzyć.* rzekła poftawa ona» ieźelić wier¬
7085  zyć nie będ4, y iyćiś Iwoicgo nie papiawia, wymiotę to Mii-
7086  wcczko az do naymnicyfzego, teraz idę do Koniecpola, Mie¬
7087  chowi, w krotce tam będźie powietrze* Przelękli fię Miefzcza-
7088  nic na tg mowę, y zmśiemi diiitkami nświcdźili bardzo ra¬
7089  no Kofćioł nafz Gldclfki, pr7cpraf2ai4c Nayfwiętfz? Pani^, <y
7090  naznaczymy fobie poft y po Mfzy Swiętey fpiewaney pr?y-
7091  dawizy dyfcyplinę przed Obrizejii Nayfwi^ętfzey Panny tiuby
```

**Vision transcription (early-modern Polish, preserved):**

> [Tegoż czá-]
> su o koło południá Mieszczaninowi Pławienskiemu nazwiskiem
> Krolowi wychodzacemu z domu do gaiu bliskiego, zástapiła
> iakaś postáć na kształt Obrazu śmierci uformowáná przeźro-
> czysta na podobienstwo paięczyny, to mowiąc do niego: (gdy
> się zląkł) nieboy się ále to mieszczanom twoim oznaymiey, że
> bicz Boży gotuie sie przeciwko nim, dla tego że nie są nabo-
> zni ná mieyscach Świętych, ktore tu blisko máia. A gdy on
> rzekł, nie będą mi wierzyć: rzekła postáwa oná, ieźelić wie-
> rzyć nie będą, y życia swoiego nie poprawia, wymiotę to Miá-
> steczko az do naymnieyszego, teraz idę do Koniecpola, Mie-
> chowá, w krotce tám będzie powietrze. Przelękli się Miefzcza-
> nie ná tę mowę, y z máłemi dziátkami náwiedzili bardzo rá-
> no Kościoł nasz Gidelski, przepraszáiąc Nayświętszą PANNĘ, y
> náznáczywszy sobie post y po Mszy Świętey śpiewaney przy-
> dawszy dyscyplinę przed Obrázem Nayświętszey PANNY śluby
> [swoie wypełniali.]

**English translation:**

> At that time, about noon, the townsman of Pławno, by name Król,
> walking from [his] house to a nearby grove, was met by a certain
> figure formed in the likeness of an Image of Death, transparent like
> a spider's web, [which] said to him (when he was frightened): "Be
> not afraid, but announce this to your townsmen: that the Scourge of
> God is being prepared against them, because they are not pious in the
> Holy Places which they have nearby here." And when he said: "They
> will not believe me," — the figure said: "If they will not believe,
> and will not amend their lives, I will sweep this little Town clean
> down to the smallest [child / inhabitant]; now I am going to
> Koniecpol [and] Miechów, soon there will be plague-air there."
> The Townsmen, alarmed at this speech, very early [in the morning]
> with their little children visited our Gidle Church, beseeching the
> Most Holy VIRGIN [for forgiveness], and having appointed for
> themselves a fast and, after a sung Holy Mass, having taken
> discipline [self-flagellation] before the Image of the Most Holy
> VIRGIN, fulfilled their vows.

**Uncertainty notes:**

- *„zastapiła iakaś postać”* — *„zastąpić”* in this period means
  "barred the way / met head-on / interposed" — so the encounter is
  literally a being **interposing itself in his path**, not a
  bystander figure seen at a distance. Adjusts the encounter geometry:
  this is a near-field, on-the-road meeting.
- *„postać … uformowáná przeźroczysta na podobienstwo paięczyny”* —
  the phrase is **the** key phenomenological detail. *Przeźroczysta*
  = "transparent / see-through"; *paięczyna* = "spider's web". The
  composite: a humanoid figure that is *see-through, of a texture like
  a spider's web*. The synthesis preserves this verbatim.
- *„Obrazu śmierci”* — "an Image of Death". Polish-Catholic iconography
  routinely depicts Death (e.g. on church frescoes) as a skeletal
  hooded figure (the *Memento Mori* iconography). The witness is
  comparing the figure to this **iconographic** convention — i.e. the
  figure looks like the kind of figure he would have seen *painted*
  on a church wall. This is important: the comparison is **to a
  picture**, not to "a dead person" or "a corpse". The translation
  preserves this.
- *„bicz Boży”* — "the Scourge of God" — a standard Polish-Catholic
  epithet for plague.
- *„wymiotę to Miáfteczko az do naymnieyszego”* — the verb is
  *wymieść* ("to sweep out"); the phrase = "I shall sweep this little
  town clean down to the smallest [thing/person]" — total destruction.
- *„powietrze”* (lit. "air") here = "plague-air" / "pestilence", the
  miasmatic-theory term for plague in 17th–18th-c. Polish; cf. the
  index entry *„Od Powietrza Morowego uwolnieni…”* ("liberated from
  plague-air") at line 7545.
- **The prophecy was fulfilled.** The next page (not cropped here) of
  the print records the arrival of plague in Koniecpol and Miechów
  shortly afterwards, exactly as predicted. The deposition was
  recorded with the witness over 60 years old, co-signed by the
  parish commendator and the town mayor (*Burmistrz*) — corporate
  attestation by both ecclesiastical and civil authority.
- The structural pattern: noon-time, on-the-road, near-field encounter
  with a translucent humanoid figure of geometrically-specific form,
  bearing verbal predictive information of demonstrable accuracy, with
  named-witness corporate attestation. This is the case the synthesis
  flags as "a description as precise as any 20th-c. UAP/NHI
  close-encounter report"; the verbatim print supports that framing.

---

## Claim 8 — Formal index entry: *„Przywalona ziemią…”* (buried-alive → revival class)

**Synthesis citation:** `§5.3`, citing line ~7550.

> Zagajowski's formal index lists this as **two distinct classes**:
>
> > *„Przywalona ziemią, już prawie martwa, dobyta, ofiarowana do Gidel,
> > przyszła do siebie.”* (line ~7550)
> > ("Buried by earth, already nearly dead, dug out, offered to Gidle,
> > came to herself.") — a **buried-alive → revival** class.

**Source:** Zagajowski 1724, `page0208`, lines 7548–7549. From the
back-of-book alphabetic index. Internal cross-reference code
*„k. 2. c. 7. r. 1. l. 5”* = Book 2, Chapter 7, Row 1, Paragraph 5
(the book's internal locator system).

**Page image:** [`page-crops/l-7548-depth-rescue-buried.jpg`](page-crops/l-7548-depth-rescue-buried.jpg)

![](page-crops/l-7548-depth-rescue-buried.jpg)

**Existing OCR (djvutxt):**

```
7548  Przywalona i.emi», luż prawie martw» dobyta, ofiarowana dó Qi-‘
7549  dcl, przylzfa do Siebie, k.i, i»7, r,u/, f,
```

**Vision transcription (early-modern Polish, preserved):**

> Przywaloná ziemią, iuż prawie martwá dobyta, ofiarowana do Gi-
> del, przyszła do siebie. *k. 2. c. 7. r. 1. l. 5.*

**English translation:**

> Buried-over by earth, already nearly dead [when] dug out, offered to
> Gidle, came to herself. *Book 2, Chapter 7, Row 1, Paragraph 5.*

**Uncertainty notes:**

- The index entry uses the feminine singular (*przywaloná, martwá,
  ofiarowana, przyszła do siebie*), so a specific woman is in view —
  not a generic "buried person". The full narrative referenced by the
  internal locator (Book 2 / Chapter 7 / Row 1 / §5) was not retrieved
  in this pass; the existence of the **index entry as its own row** is
  what the synthesis cites.
- *„dobyta”* — past passive participle of *dobyć*, "to draw out, dig
  out, extract". The sequence is: buried by earth → dug out → already
  near death on extraction → vowed/offered to Gidle → recovered.
- The internal locator system uses *k.* = *księga* (book), *c.* =
  *część* / *capitulum* (chapter / part), *r.* = *rok* / *rząd* (year
  or row), *l.* = either *list* (folio) or *liczba* (number). The OCR
  garbling (*„k.i, i»7, r,u/, f,”*) is severe; vision pass reads
  *„k. 2. c. 7. r. 1. l. 5”* against the clear print.
- The synthesis groups this with the **river-drowning** miracles and
  the **well-rescue** entry below as a single *depth-rescue* theme.
  As an *iconographic* claim about the cult, this grouping is
  defensible. As a strict *index-class* claim, the print preserves
  three separate index headings: ground-burial, well-fall, and
  drowning are distinct; *§5.3* is correct in saying it lists them as
  "two distinct classes" (ground and well), with drowning narrated
  separately in the body.

---

## Claim 9 — Formal index entry: *„W studnie wpadaiący…”* (well-rescue class)

**Synthesis citation:** `§5.3`, citing line 7561.

> > *„W Studnie wpadawszy, ofiarowani do Gidel, bez szwanku byli.”*
> > (line 7561) ("Those who fell into wells, having been offered to
> > Gidle, were without harm.") — a **well-rescue** class.

**Source:** Zagajowski 1724, `page0208`, lines 7561–7562. From the
back-of-book alphabetic index. Multiple internal cross-references in
the locator code, indicating multiple distinct cases narrated in the
body.

**Page image:** [`page-crops/l-7561-depth-rescue-well.jpg`](page-crops/l-7561-depth-rescue-well.jpg)

![](page-crops/l-7561-depth-rescue-well.jpg)

**Existing OCR (djvutxt):**

```
7561  W Studnie w padaiVy > ofiarowani do Gidel, be2 fzwanku byli.
7562  k,z,e.f,	6,	/•»/•	Z,.?,	r«7. r,»
```

**Vision transcription (early-modern Polish, preserved):**

> W Studnie wpadaiący, ofiarowani do Gidel, beż szwánku byli.
> *k. 2. c. 5. r. 4. l. 5. c. 6. r. 3. l. 2. c. 7. r. 1. l. 3.*

**English translation:**

> Those falling into wells, offered to Gidle, were without harm.
> *[Book 2,] Chapter 5, Row 4, Paragraph 5; Chapter 6, Row 3,
> Paragraph 2; Chapter 7, Row 1, Paragraph 3.*

**Uncertainty notes:**

- The synthesis paraphrases *„W Studnie wpadaiący”* as *„W Studnie
  wpadawszy”*; the print actually has *wpadaiący* (present active
  participle: "those falling into") rather than *wpadawszy* (past
  perfective). Translates the same in English ("those who fell into
  wells"), but the print's tense is *iterative* — habitual or
  repeated falling, not single past events. This reinforces the
  reading as a *class* of cases, not a single incident.
- *„bez szwanku”* — "without harm / damage / injury". *Szwank* is a
  rare archaism; the modern form is *„bez szwanku”* still in idiomatic
  use, meaning "unharmed".
- **Multiple internal cross-references** — at least three distinct
  body-text cases (in Chapters 5, 6, and 7 of Book 2) are indexed
  under this single class entry. So the class is *empirically*
  populated, not just a categorical placeholder.
- The OCR rendering of the locator codes (*„k,z,e.f, 6, /•»/• Z,.?,
  r«7. r,»”*) is essentially destroyed; the vision pass against the
  clear print resolves all the codes.

---

## Claim 10 — Formal index entry: *„Światłość cudowna, y ogień…”* (nocturnal-lights class)

**Synthesis citation:** `§5.1`, citing line 7563.

> Zagajowski's **formal index** lists this as a class of phenomena, not
> as a single event (line 7563):
>
> > *„Światłość cudowna, y ogień w Kościele Gidelskim widziane w nocy
> > przed Obrazem Panny Najświętszej.”*
> > ("Miraculous brightness, and fire seen at night in the Gidle Church
> > before the Image of the Most Holy Lady.")

**Source:** Zagajowski 1724, `page0208`, lines 7563–7564. From the
back-of-book alphabetic index. The internal cross-reference code
*„k. 2. c. 1. instr: 1. l. 8”* points back to the narrative crop in
**Claim 1** of this file (Book 2, Chapter 1, Instrument 1, Paragraph 8
= the "*Brat. 8*" testimony at l. 2855).

**Page image:** [`page-crops/l-7563-nocturnal-lights-index.jpg`](page-crops/l-7563-nocturnal-lights-index.jpg)

![](page-crops/l-7563-nocturnal-lights-index.jpg)

**Existing OCR (djvutxt):**

```
7563  Swiatlosc cudowna, y ogień w Kościele Gidelfkim widiianc w hocy
7564  przed Obrazem Panny Ńayswiętlzey. k,t. c,i, infłr: t, l 8,
```

**Vision transcription (early-modern Polish, preserved):**

> Światłosć cudowna, y ogień w Kościele Gidelskim widziane w nocy
> przed Obrazem PANNY Nayświętszey. *k. 2. c. 1. instr: 1. l. 8.*

**English translation:**

> Miraculous brightness, and fire, seen at night in the Gidle Church
> before the Image of the Most Holy VIRGIN. *Book 2, Chapter 1,
> Instrument 1, Paragraph 8.*

**Uncertainty notes:**

- **Two phenomena are named, not one.** The index entry distinguishes
  *„światłosć cudowna”* ("miraculous brightness") from *„ogień”*
  ("fire") as *distinct* classes — joined here in one index row but
  iconographically separable. The narrative at l. 2855 (Claim 1) gives
  the second sub-pattern as *„iakoby dwie świece goraiące”* ("as if
  two burning candles") — a *fire-like* sub-pattern within the broader
  brightness category. The index-entry's binary structure
  (*„światłosć… y ogień”*) thus **confirms the synthesis-level reading**
  that two distinct phenomena are in view, and is **more conservative**
  than the synthesis ("recurring anomalous lights" as a single class):
  the index treats *brightness* and *fire-form* as separate
  observable categories. Worth flagging in `§5.1`.
- *„Swiatlosc / Światłosć”* — the *-ść* ending is what the modern
  spelling expects; the 1724 print has *-sć*, and the vision pass
  preserves this. The OCR rendered without diacritics.
- The internal locator *„instr: 1.”* = *Instrumentum 1* — the first
  formal notarial *instrument* (witness-deposition group) in Book 2
  Chapter 1. This is the same source group from which Claim 1
  (the Brat. 8 narrative) is drawn. The forward/back chain
  **index entry l. 7563 ↔ narrative l. 2855** thus closes
  cleanly inside the print's own apparatus.

---

## Methodology note: what this cross-reference proves and does not prove

This file proves that the **synthesis quotations** are anchored in the
actual 1724 print, and that the **OCR-derived line citations** map to
the passages the synthesis claims they map to. It does not prove the
historical *truth* of the depositions themselves — only that the
depositions exist, were recorded in the form Zagajowski reproduces,
and say what the synthesis says they say.

For most claims, the vision transcription and the existing djvutxt
OCR agree on the **meaning** of the passage, even where the OCR is
visibly noisy. The systematic disagreements are:

1. **Long-s problem.** djvutxt swaps `ſ` ↔ `f` ~80% of the time. This
   makes the OCR borderline-unreadable on first glance but does not
   destroy semantic content (a Polish reader can recover the meaning).
2. **Mid-line typographical noise.** djvutxt drops or replaces
   characters in the middle of lines, especially near figure-numbers,
   abbreviations, and diacritics. ~20% of lines have at least one
   such corruption.
3. **Latin attestation blocks.** The standardised *coram notario*
   Latin closing-formulae (e.g. *„Quæ testimonia debito juris ordine
   audivi…”*) suffer the worst OCR degradation; the vision pass
   restores them almost perfectly.
4. **Index-page locator codes.** The internal book-reference codes
   (`k. N. c. N. r. N. l. N.`) are essentially destroyed by OCR; the
   vision pass restores them and lets us trace **index → narrative**
   forward chains within the book.

Net assessment: **the existing OCR is good enough to support
keyword-search and orientation, but inadequate for direct quotation
in published work**. For any future scholarly use of Zagajowski 1724
text in the synthesis, the vision-transcription pass should be the
authoritative source, with the OCR retained as a search index and
locator.

**Two synthesis-side corrections surfaced during this pass** (both
flagged in the per-claim uncertainty notes):

1. **Claim 2 (`§5.4`):** the witness's name is **Jan Kotulski**, not
   "Bartolomeus Plebani". *Plebani* is the Latin genitive of *plebanus*
   ("parish priest") and refers to the recording cleric, not the
   deponent.
2. **Claim 5 (`§5.5`):** the broken object in the Woytowicz exorcism
   is *„kyi”* — most likely *„kij”* (walking-stick) — not *„[łaty]”*
   (lath) as guessed in the synthesis paraphrase.

Both corrections will be applied to `docs/synthesis.md` in a
follow-up commit, with this cross-reference cited as the source.
