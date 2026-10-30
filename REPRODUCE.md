# How this repository was made (Gabon)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Journal Officiel de la République Gabonaise, Droit gabonais: Constitution | <https://www.journal-officiel.ga/constitution> | 2026-10-29 | none published; legislation is public law |
| Journal Officiel de la République Gabonaise: Les codes, Code pénal (loi 006/2020) | <https://journal-officiel.ga/code-penal> | 2026-10-30 | none published; legislation is public law |
| Journal Officiel: loi 006/2020 (JO n°72 bis) | <https://journal-officiel.ga/4704-006-2020-/> | 2026-10-30 | none published; legislation is public law |
| Journal Officiel: loi 005/2021 (JO n°131) | <https://journal-officiel.ga/17697-005-2021/> | 2026-10-30 | none published; legislation is public law |
| Journal Officiel: Les codes, Code civil (1re partie, loi 15/72 consolidated) | <https://journal-officiel.ga/code-civil-1ere-et-2eme-partie> | 2026-10-30 | none published; legislation is public law |
| Journal Officiel: loi 004/2021 (JO n°131) | <https://journal-officiel.ga/17696-004-2021/> | 2026-10-30 | none published; legislation is public law |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution de la République gabonaise (loi n°3/91 du 26 mars 1991, modifiée jusqu'à la loi n°046/2020 du 11 janvier 2021) | 1 | 2021-01-11 to 2021-01-11 |
| `code-penal` | Code pénal de la République gabonaise (loi n°006/2020) | 2 | 2020-06-30 to 2021-09-16 |
| `code-civil` | Code civil de la République gabonaise, première partie: des personnes et de la famille (loi n°15/72) | 2 | 2017-08-03 to 2021-09-16 |

The build made 5 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 2 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futur`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 17 laws in the record.
- 8 tags.

## Dates

Each commit is dated at noon (Africa/Libreville) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution art. 114: the Constitution is published in the Journal Officiel and executed as a law of the Republic. No general commencement rule for amending laws was read; the one version here is dated by the latest amending law named in the source. https://www.journal-officiel.ga/constitution

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `bbf3fea886ea12619dedd51b8d1e52a0af3f1d619301d763b2505d6b178f4fdc` (930862 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

5 versions of 3 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- The only official text found online is the consolidated 1991 Constitution on journal-officiel.ga, last amended by loi n°046/2020 of 11 January 2021; it is a single 'oldest version available' dated 2021-01-11, the date of the last amending law.
- The page's per-article amendment notes (for example '(Loi n°047/2010 du 12 janvier 2011)') are left out of headings; the amending laws are listed as earlier laws, not credited per article.
- The 2024 Constitution (Journal Officiel n°47 bis, 19 December 2024) is not on the official site as text and is not included.
- The signature blocks after article 114 are left out.
- Code pénal: version 1 is the Code as published on journal-officiel.ga (Les codes, loi 006/2020 of 30 June 2020, Journal officiel n°72 bis spécial of the same day); it was checked equal, article by article, to the page of loi 006/2020 itself except two typographic differences (art. 75-7, 318). It is dated 2020-06-30, the day of promulgation and publication.
- Code pénal: version 2 (2021-09-16, Journal officiel n°131) is built by applying loi 005/2021 to version 1: the site does not publish a consolidated text. Each 'article nouveau' replaces the whole article; art. 256 'alinéa 1 nouveau' replaces the first paragraph; 'alinéa 2' of art. 173 and 271 is appended after the existing paragraphs; articles 223-4 bis, 234 bis, 257 bis and 291-1 to 291-6 are added. Loi 005/2021 art. 1 (new title of the law) changes no article.
- Code pénal and Code civil: headings (Livre, Titre, Chapitre, Section, Paragraphe) are left out; articles are the units. Typographic quotes and dashes were normalised.
- Code civil: the official site's page for the first part gives the text as completed by loi 009/2010 and modified by loi 003/2017, without a date for the consolidation; it is a single 'oldest version available' dated 2017-08-03, the date of the last law it names.
- Code civil: version 2 (2021-09-16) applies loi 004/2021 to that text: each 'article nouveau' replaces the whole article (art. 276 included, although the law's list says 'alinéa 3'), the articles added by its art. 3 are added, and its art. 5 repeals the second paragraph of art. 351 and all of art. 352. Its articles 699 and 700 belong to the second part of the Code (successions), which is not in this repository, and are not applied. Its art. 4 renames a heading, which is not recorded.
- Only the first part of the Code civil (articles 1 to 645, persons and family) is on the page; the second part and the Code de commerce were not found as text on the official site (OHADA Uniform Acts govern commercial law).

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
