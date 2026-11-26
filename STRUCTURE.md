# Structure

Un dossier par type de texte, puis par année ; un dossier par texte ; un fichier par article.

| Dossier | Contenu |
| --- | --- |
| `constitution/` | la Constitution en vigueur (2024) : `preambule.md`, `art-001.md` … `art-173.md`, `signatures.md`, `index.md` ; la Constitution de 1991 dans l'historique git |
| `codes/<code>/` | les codes consolidés : `codes/code-penal/`, `codes/code-civil/` (1re partie) |
| `lois/<année>/<numéro>-<objet>/` | lois, lois organiques, lois référendaires, lois-programmes, décrets-lois, chartes |
| `ordonnances/<année>/<numéro>-<objet>/` | ordonnances |
| `decrets/<année>/<mois>/<numéro>-<objet>/` | décrets (par mois : moins de 1 000 entrées par dossier) |
| `arretes/<année>/<mois>/<numéro>-<objet>/` | arrêtés et arrêtés interministériels |
| `autres/<année>/<nature>-<numéro>-<objet>/` | délibérations, décisions de caractère général, règlements, conventions, accords, instruments de ratification |
| `journal-officiel/<année>/<numéro>/sommaire.md` | le sommaire de chaque numéro, avec un lien vers chaque texte repris |

Dans le dossier d'un texte : `index.md` (intitulé, nature, numéro, date, autorité, numéro du Journal officiel, source, plan), `preambule.md` (intitulé et visas), `art-NNN.md` (un article ; `art-012-bis.md`, `art-unique.md`), `signatures.md`, ou `texte.md` pour un texte sans articles. Au-delà de 900 articles, les articles sont rangés dans `articles-0000/`, `articles-0500/`, …

## Commits

Un commit par texte publié, daté à midi, heure de Libreville (UTC+1), du jour de publication du numéro du Journal officiel (`Published:`, `Date-basis: JO publication`) ; l'auteur est le texte (`Décret 0463/PR/MAEDR`), le committer Lexifina. Trailers : `Law`, `Kind`, `Enacted` (date du texte), `Published`, `Date-basis`, `Source`.

## Non repris

Récépissés, communiqués, procès-verbaux, avis, autorisations, arrêtés et décisions individuels, errata et rectificatifs, circulaires : ils restent cités dans le `sommaire.md` du numéro avec la mention « non repris ». Les décisions de la Cour constitutionnelle sont dans un dépôt de jurisprudence distinct.
