# References

Local copies (and pointers) of the sources cited in `docs/synthesis.md`.
All material is either public-domain or scholarly open access; cite the
originals, not these copies, in any external use.

## Local files

| File | Source | What it is |
| --- | --- | --- |
| [`zagajowski-1724-skarb-wielki/`](./zagajowski-1724-skarb-wielki/) | Cyfrowa Biblioteka Diecezjalna w Sandomierzu | The full 1724 first edition of Zagajowski's *Skarb wielki…* as a 228-page indirect-multipage DjVu (228 page files + dictionary chunks + the main index `17748.djvu`). Public domain. Open the main `17748.djvu` in any DjVu viewer (`djview4`, `okular`, `evince` with DjVu support, etc.). |
| [`cholewinski-2015-dzieje-sanktuarium.pdf`](./cholewinski-2015-dzieje-sanktuarium.pdf) | KUL / *Roczniki Teologiczne* | Łukasz Cholewiński (2015), the peer-reviewed article that grounds the relief-panel re-dating (1651 altar / 1670 gilding) on the Dominican Archive in Kraków. |
| [`dominikanie-gidle-historia.html`](./dominikanie-gidle-historia.html) | gidle.dominikanie.pl | Snapshot of the sanctuary's own *Historia* page. Quotes Trebnica 1636 verbatim and identifies the relief as a *dawne antepedium*. |
| [`dominikanie-gidle-figurka.html`](./dominikanie-gidle-figurka.html) | gidle.dominikanie.pl | Snapshot of the sanctuary's *Figurka MB* page (the original prompt URL of the whole investigation). |
| [`fundacja-hereditas-figurka-mb-gidelskiej.html`](./fundacja-hereditas-figurka-mb-gidelskiej.html) | cudaregionu.fundacja-hereditas.pl | Fundacja Hereditas blog post: notes the 7.5 cm height, the *medieval* stylistic affinity, and the 1669–1670 Garlicki altar dating. |
| [`wikipedia-pl-bazylika-gidle.html`](./wikipedia-pl-bazylika-gidle.html) | pl.wikipedia.org | Polish Wikipedia article on the basilica; useful for the 1640–1655 construction range, heritage register numbers, and the 1998 *bazylika mniejsza* designation. |

Snapshots taken **2026-05-30**.

## Sources not (yet) available locally

### Jerzy Trebnica (Trebnic) OP — *Historya o Cudownym Obrazie Przenaswiętszey Panny Mariey, który jest w Gidlach* (1636)

The **earliest** written account; quoted in extenso on the Dominicans' history page. No digital edition has been located. Likely holdings to check:

- Archiwum Klasztoru OO. Dominikanów w Krakowie (the order's central archive).
- Biblioteka Jagiellońska, Kraków — old-prints catalogue.
- Biblioteka Narodowa, Warszawa — *Polona* digital library (worth searching periodically; it may eventually be digitized).
- KARO / FBC federated search across Polish digital libraries.

### Modern Polish monographs

- **K. Walaszczyk**, *Sanktuarium Matki Bożej Gidelskiej*, Radomsko: Muzeum Radomszczańskie, 1993.
- **K. Żukiewicz OP**, *Matka Boska Gidelska*, Radomsko: Muzeum Radomszczańskie, 2011 (reprint of an earlier work).

Both cited heavily by Cholewiński 2015. Likely held at Biblioteka Narodowa and major university libraries; no open digital edition known.

### Internal Dominican archival material

- **R. Świętochowski OP**, *„W 450 rocznicę wyorania cudownego posążka Matki Boskiej Gidelskiej”*, Kraków 1966 — typescript in the Dominican Archive in Kraków (ADK).
- **ADK, Liber Consiliorum Conventus Gidlensis** — building contracts with Jan Buszt (1632) and Fryderyk Laipet (1644).
- **ADK, Księga wydatków klasztoru (1625–1857), sygn. Gi 81** — the 1630 Speyzer altar contract.
- **ADK, Akta dotyczące budynków kościoła OO. Dominikanów w Gidlach (1630–1953), sygn. Gi 18** — main-altar contract for the 1796 Schreiber reconstruction.

Accessible by appointment at Archiwum Polskiej Prowincji Dominikanów, ul. Stolarska 12, Kraków.

## Canonical URLs (in case the snapshots go stale)

- Sanctuary main page: <https://gidle.dominikanie.pl/>
- Sanctuary history: <https://gidle.dominikanie.pl/klasztor/historia/>
- Sanctuary on the figurine: <https://gidle.dominikanie.pl/sanktuarium/figurka-mb/>
- Zagajowski 1724 (Sandomierz dLibra): <https://bc.bdsandomierz.pl/dlibra/publication/1071/edition/1028>
  - Direct ZIP: <https://bc.bdsandomierz.pl/Content/1028/download/>
- Cholewiński 2015 (TNKUL): <https://ojs.tnkul.pl/index.php/rt/article/download/8607/8286/>
- Fundacja Hereditas figurine page: <http://cudaregionu.fundacja-hereditas.pl/2021/11/15/figurka-matki-bozej-gidelskiej/>
- Wikipedia (PL) basilica: <https://pl.wikipedia.org/wiki/Bazylika_Wniebowzi%C4%99cia_Naj%C5%9Bwi%C4%99tszej_Maryi_Panny_w_Gidlach>

## Suggested viewers / extraction tools

- **DjVu** (Zagajowski 1724): `sudo apt install djvulibre-bin djview4` then `djview4 docs/references/zagajowski-1724-skarb-wielki/17748.djvu`. To convert a few pages to PDF: `ddjvu -format=pdf page0010.djvu page0010.pdf`.
- **HTML snapshots**: open directly in a browser, or use `pandoc -f html -t plain` for a clean text dump.
