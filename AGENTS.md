# AGENTS.md

Project conventions for AI agents on the Gidle case study. Extends
(does not override) `~/.cursor/rules/site-environment.mdc`.

Read `README.md` and `docs/synthesis.md` first — the project's
framing, methodology, sources, and open questions live there.
Secondary documentation: `docs/references/README.md` catalogues
primary sources with snapshot dates and canonical URLs;
`docs/working-notes/` holds methodology notes and regeneration
recipes (e.g. the grep-sweep that §5 of the synthesis was built
from).

## The two rules that matter most

### 1. Polish translations: always present both languages

For every primary-source Polish passage you quote or paraphrase:

- Give the **Polish original verbatim** (with the archaic-Polish
  typography preserved: *„…"* low/high quotes, original spelling
  including long-s, original diacritics).
- Give an **English translation** alongside it.
- Flag any uncertain word or phrase explicitly (e.g. *"[unclear:
  OCR reads X, possibly Y]"*).

Neither the user nor the AI is a fluent Polish reader; the user
will check translations against the original, and the AI is
expected to push back when a user translation looks off. Mutual
cross-checking is the working pattern. **Do not** silently
translate without showing the Polish source text.

### 2. Citations: ask before you guess

If you are not sure of a bibliographic, biographical, or
institutional detail — chapter title, year, page range, PhD
institution, founder list, exact title of a work — **ask the user
or run a `WebSearch` check**, do not infer from adjacent knowledge.

Hallucinated citations already caught in earlier sessions: a
non-existent "Hacking Heaven" chapter in *American Cosmic*, the
wrong PhD institution for Pasulka, a padded SOL Foundation founder
list. Each got fixed before commit, but only because a fact-check
was run. Always run the fact-check.

If a primary source is hard to access (digital library blocked,
catalogue down, scan unclear), say so and ask, rather than fill
in.

## Calibration — what the AI did, and didn't, do reliably

For a future AI session calibrating its own confidence on this
project: in the session that built this repo, the AI handled the
mechanical bulk — source discovery and download from Polish
digital libraries, the OCR pipeline, the 15-category grep sweep
across 8,250 lines of Zagajowski 1724, first-pass drafting of
§§3, 5, 6, 8, 9 of the synthesis, the bibliography, the 17-marker
annotated panel, and `WebSearch`-based self-fact-checking (which
caught three of its own hallucinations before commit).

On the same evidence, the AI was *not* reliable for:

- **Exhaustive visual reading** of a dense artefact — the user
  caught the axe, the cylinder, the sun + moon iconography, and
  the right-bottom topographic vignette, each materially
  important.
- **Citation accuracy without verification** — all three caught
  hallucinations (the *American Cosmic* "Hacking Heaven" chapter,
  Pasulka's PhD institution, the SOL Foundation founder list)
  would have shipped silently without a `WebSearch` pass. See
  Rule 2.
- **Polish translation without cross-check** — OCR-degraded
  archaic Polish reads at maybe 80–90% accuracy on first pass.
  See Rule 1.
- **Observation-tier claims without the primary source open** —
  first-pass paraphrases drift; only line-numbered quotation
  against the OCR (and, eventually, against the DjVu page) is
  trustworthy.

The intended posture is neither over-confidence (committing
without `WebSearch`, smoothing over poor OCR, paraphrasing without
the source open) nor under-confidence (refusing a hard sweep or
treating a degraded source as unreadable). The user is willing to
do verification and corrective re-readings, and expects the AI to
attempt the difficult moves.

## A few smaller conventions

- **Don't commit unless explicitly asked.** Project rhythm is
  draft → show → revise → commit.
- **Use `AskQuestion` for delicate authorial decisions** (framing,
  voice, what to include) rather than guessing. The user
  demonstrated this pattern by selecting one of five offered
  framings for the README's *How this project started* section;
  that's the intended pattern.
- **`§8.4` of `docs/synthesis.md`** is the project's methodological
  covenant: structural pattern-matching across the comparative
  literature is licensed; importing modern causal/ontological
  vocabulary ("UFO event", "NHI", etc.) into the historical
  sources is not. Re-read it before touching §9.
- **Visible retractions are a transitional convention**, not the
  end state. When you correct a prior reading, label the
  retraction in place; the eventual goal is a self-consistent
  document with retractions reabsorbed.
- **The README's *On AI collaboration* section is intentional** —
  the project has a stated dual purpose (the case study itself,
  plus a worked example of AI-assisted archival reading). Do not
  silently strip or dial down that section.
- **Don't silently revert what looks like a user edit.** Check the
  git log or ask.
