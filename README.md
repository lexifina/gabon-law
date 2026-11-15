# Gabon: law history in git


The law of Gabon as a git history: one file per article, one commit per version on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every line; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Gabon's national law, which global-law reads at `gabon/national/acts/`.

**What is in it now:** three acts, with 5 versions: the Constitution of 1991 as amended to 2021 (133 articles, one version), the Code pénal of 2020 (694 articles, two versions) and the first part of the Code civil, on persons and the family (648 articles, two versions). Each act's `README.md` lists its articles and when each last changed; [`data/laws.csv`](data/laws.csv) lists the 17 laws the record names.

Each act is a folder, and each article a file named by its printed number: `code-penal/art-230.md` is Article 230 of the Code pénal, `code-penal/art-223-4-bis.md` is Article 223-4 bis, and the Constitution's Préambule is `constitution/preamble.md`.

The text is in French, as the Journal Officiel prints it. An English translation is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Article 230 of the Code pénal | `git log -p --word-diff -- code-penal/art-230.md` |
| Which law wrote each line of Article 230? | `git blame code-penal/art-230.md` |
| Every version of the Code pénal, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- "code-penal/art-*"` |
| Article 230 as in force on 1 January 2021 | `python tools/on.py 2021-01-01 code-penal art-230` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Gabonese law](https://global-law.lexifina.com/v1/try_claude?country=gabon)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=gabon)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=mariage&jurisdictions=gabon)**: a search of Gabonese law for "mariage", returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in French or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add gabon/national/acts
python3 tools/law.py show 2026-01-01 gabon/national/acts/code-penal/art-230.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Africa/Libreville, on the day the version took effect, and carries it in its `In-force:` trailer:

- the Code pénal as enacted: 30 June 2020, the day loi n°006/2020 was promulgated and published (Journal officiel n°72 bis spécial);
- the 2021 changes to both codes: 16 September 2021, the day loi n°005/2021 and loi n°004/2021 were published (Journal officiel n°131);
- the Constitution and the Code civil's first version: the date of the latest law the source names as included (loi n°046/2020 of 11 January 2021; loi n°003/2017 of 3 August 2017). The source gives no other day these texts took effect.

Each change is credited to the law that made it (`Loi 005/2021`). The Constitution and the Code civil's first version are credited to the publisher, the Journal Officiel, as the "oldest version available", and their commit messages name the laws the text already includes (the 1991 Constitution and its eight amending laws; loi n°15/72, n°009/2010 and n°003/2017).

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before, and compares it with the corpus: 5 versions of 3 acts, no mismatches.
- Every commit's trailers parse; there are no merge commits, commit dates never go backwards and none is dated after the build.
- The Code pénal of 2020 matches the published text of loi n°006/2020 article by article, apart from two typographic differences (articles 75-7 and 318).
- `tools/build.py` writes the history from one corpus file, and the same corpus gives the same commit hashes; no second build has been compared yet. The details are in [`REPRODUCE.md`](REPRODUCE.md).

## What it does not show

- **The Constitution in force.** Gabon adopted a new Constitution by referendum on 16 November 2024, promulgated on 19 December 2024. The Journal Officiel site does not carry its text, so the Constitution here is the 1991 text it replaced.
- **Earlier wording.** The first version of the Constitution already includes its amendments of 1994 to 2021, and that of the Code civil the laws of 2010 and 2017; there is no history before them.
- **An official 2021 text.** The site publishes no consolidated text after the 2021 laws: the 2021 versions apply each law's amendments to the earlier text (see `REPRODUCE.md`). Loi n°004/2021 also changes articles 699 and 700, in the Code civil's second part, which are not applied; later amendments, if any, are not here.
- **Most of Gabonese law.** The second part of the Code civil, the Code de commerce, the Code de procédure pénale and the other codes are not here: the site shows them only as images, or not at all. Commercial law is largely the OHADA Uniform Acts.
- **Headings and notes.** The codes' headings (Livre, Titre, Chapitre, Section), the Constitution's signature blocks and the notes naming amending laws are left out. The source has no Code civil articles 220 and 614.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Journal Officiel de la République Gabonaise](https://journal-officiel.ga) | Official journal: the Constitution, the codes and the laws | no, one consolidated text per act | The Constitution, Code pénal and Code civil pages, and the laws n°006/2020, n°005/2021 and n°004/2021, retrieved on 29 and 30 October 2026 |

## Licence

See [`LICENSE`](LICENSE). The site publishes no licence for its legislation pages; the texts are the public law of the Republic of Gabon, reproduced with attribution, and their copyright status is not confirmed. Lexifina's own contributions (the history, the commit messages, the tables and the tools) are dedicated to the public domain under CC0 1.0.

No AI model wrote, translated or corrected legal text; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
