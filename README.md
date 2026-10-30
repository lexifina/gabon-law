# Gabon: law history in git

The law of Gabon as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to a section; `tools/on.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ga/`.

Language: the official language, French. This README is English first.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution de la République gabonaise (loi n°3/91 du 26 mars 1991) as consolidated to the loi n°046/2020 du 11 janvier 2021 | 1 | One "oldest version available": the consolidated text the Journal Officiel site prints, dated 11 January 2021 |

| `code-penal/` | Code pénal (loi n°006/2020 du 30 juin 2020, which replaced loi n°042/2018) | 2 | The Code as promulgated on 30 June 2020 (685 articles), then the changes made by loi n°005/2021, in force from 16 September 2021 (18 articles changed or added) |
| `code-civil/` | Code civil, première partie: des personnes et de la famille (loi n°15/72 du 29 juillet 1972), articles 1 to 645 | 2 | The consolidated text the Journal Officiel site prints (completed by loi n°009/2010, modified by loi n°003/2017), dated 3 August 2017 as the oldest version available, then the changes made by loi n°004/2021, in force from 16 September 2021 (45 articles changed, added or repealed) |

The constitution is one text with no change history. The two codes each have two versions.

## What it does not show

- **It is the Constitution before 2024.** Gabon adopted a new Constitution by referendum on 16 November 2024, promulgated on 19 December 2024. The Journal Officiel site's Constitution page still prints the 1991 text as amended to 2021, and no text of the 2024 Constitution was found on an official site with a text layer, so it is not here. **Do not read this repository as the law in force today.**
- **Amendments before 2021 are already applied.** The site prints the Constitution as amended in 1994, 1995, 1997, 2000, 2003, 2011, 2018 and 2021, and gives no earlier wording, so there is no history between 1991 and 2021. Those amending laws are named as the earlier laws in the first commit.
- **Other law.** Only these three acts. The second part of the Code civil (property, successions, contracts), the Code de commerce, the Code de procédure pénale and the other codes are not here: the site's codes page shows them only as images, or not at all (commercial law is largely the OHADA Uniform Acts).
- **The 2021 versions are Lexifina's application of the amending laws.** The site prints the Code pénal as of 2020 and the Code civil as of 2017, and publishes the 2021 laws separately; it publishes no consolidated 2021 text. The 2021 versions were made by applying each amending law's "article nouveau" texts to the earlier text (see `REPRODUCE.md`, "decisions"). Loi n°004/2021 also changes articles 699 and 700, which belong to the second part of the Code civil and are not applied. Later amendments to either code, if any, are not in the record. Check the Journal Officiel before relying on any wording.
- **Code civil gaps in the source.** The page has no articles 220 and 614.
- Headings (Livre, Titre, Chapitre, Section) are left out of the codes; articles are the units.
- Signature blocks after Article 114, and the per-article notes naming the amending law, are left out of the text.
- This is not legal advice, and it is not an official text.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| Article 4 as printed | `python tools/on.py 2021-01-11 constitution art-004` |
| Who wrote each line of Article 4? | `git blame constitution/art-004.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |

Files are named by the printed number: `art-004` is Article 4, `art-224-1` is Article 224-1, `art-011-a` is Article 11a, `titre-02` is Titre II, and `preamble` is the Préambule.

## Dates

Each commit is dated at noon, Africa/Libreville, on the day the version took effect. The constitution's single version is dated 11 January 2021, the date of the latest amending law the site names (loi n°046/2020). The Code pénal's first version is dated 30 June 2020 (promulgation and publication in Journal officiel n°72 bis spécial), the 2021 versions 16 September 2021 (Journal officiel n°131, publication of loi n°005/2021 and n°004/2021). The Code civil's first version is dated by the last law the page names. The site gives no other entry-into-force dates.

## What "author" means

The author of a commit is the law that made the change, at an address that cannot exist. For the constitution and the Code civil's first version the commit is by the publisher, the Journal Officiel, as the **oldest version available**, naming the 1991 law and its eight amending laws.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

The text comes from the Journal Officiel de la République Gabonaise (https://journal-officiel.ga): the Constitution page (retrieved 29 October 2026), and, retrieved 30 October 2026, the pages for the Code pénal (`/code-penal`, `/4704-006-2020-/`), loi n°005/2021 (`/17697-005-2021/`), the Code civil (`/code-civil-1ere-et-2eme-partie`) and loi n°004/2021 (`/17696-004-2021/`). The site publishes no licence; the law of the Republic is public law, reproduced with this attribution.

Changes made by Lexifina: the page was converted to one Markdown file per provision, one paragraph or item per line; spacing, quotes and dashes were normalised; the amendment notes in the article headings and the signature blocks were left out. The wording of the law was not changed. The Journal Officiel and the Government of Gabon do not endorse this repository.

Lexifina's own contributions (the arrangement of the history, the commit messages, the tables and the tools) are dedicated to the public domain under CC0 1.0 Universal: https://creativecommons.org/publicdomain/zero/1.0/legalcode
