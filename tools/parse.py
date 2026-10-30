import json, re, html, hashlib, pathlib
here = pathlib.Path(__file__).parent
raw = (here / '.cache' / 'constitution.html').read_bytes()
sha = hashlib.sha256(raw).hexdigest()
t = raw.decode('utf8', 'replace')
t = re.sub(r'<(script|style).*?</\1>', '', t, flags=re.S)
t = re.sub(r'<br\s*/?>|</p>|</div>|</li>|</h\d>', '\n', t)
t = html.unescape(re.sub(r'<[^>]+>', '', t))
lines = [re.sub(r'[ \t\xa0]+', ' ', l).strip() for l in t.split('\n')]
lines = [l for l in lines if l]


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r' +', ' ', s)


i0 = lines.index('PREAMBULE')
i1 = next(i for i, l in enumerate(lines) if l.startswith('Fait à Libreville'))
body = lines[i0:i1]
ROM = {'PRELIMINAIRE': 0, 'PREMIER': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11, 'XII': 12}
out = {}
cur = None


def add(key, label, kind, head):
    global cur
    assert key not in out, key
    cur = {'label': label, 'kind': kind, 'lines': [head]}
    out[key] = cur


for l in body:
    m = re.match(r'^Article (Premier|\d+)([a-z]?)\b', l)
    if l == 'PREAMBULE':
        add('preamble', 'Préambule', 'preamble', '# Préambule')
    elif l.startswith('TITRE '):
        k = re.match(r'TITRE (\S+)', l).group(1)
        add('titre-%02d' % ROM[k], l.split(':')[0].strip().capitalize(), 'chapter', '# ' + norm(l))
    elif m:
        n = 1 if m.group(1) == 'Premier' else int(m.group(1))
        suf = m.group(2)
        key = f'art-{n:03d}' + (f'-{suf}' if suf else '')
        add(key, f'Art. {n}{suf}', 'art', '# ' + ('Article Premier' if n == 1 else f'Article {n}{suf}'))
    else:
        cur['lines'].append(norm(l))
units = {k: {'label': u['label'], 'kind': u['kind'], 'text': '\n'.join(u['lines']) + '\n'} for k, u in out.items()}
amend = [('loi-1-94', 'Loi n°1/94', '1994-03-18'), ('loi-18-95', 'Loi n°18/95', '1995-09-29'),
         ('loi-1-97', 'Loi n°1/97', '1997-04-22'), ('loi-14-2000', 'Loi n°14/2000', '2000-10-11'),
         ('loi-13-2003', 'Loi n°13/2003', '2003-08-19'), ('loi-047-2010', 'Loi n°047/2010', '2011-01-12'),
         ('loi-001-2018', 'Loi n°001/2018', '2018-01-12'), ('loi-046-2020', 'Loi n°046/2020', '2021-01-11')]
U = 'https://www.journal-officiel.ga/constitution'
laws = {'loi-3-91': {'label': 'Loi n°3/91', 'title': 'Constitution de la République gabonaise (loi du 26 mars 1991)', 'kind': 'law', 'enacted': '1991-03-26', 'published': None, 'url': U, 'temporary_until': None, 'restores': None, 'note': None}}
for k, l, d in amend:
    laws[k] = {'label': l, 'title': f'Loi portant révision de la Constitution, {l} du {d}', 'kind': 'law', 'enacted': d, 'published': None, 'url': U, 'temporary_until': None, 'restores': None, 'note': None}
corpus = {
    'country': {'code': 'GA', 'name': 'Gabon', 'slug': 'gabon', 'lang': 'fr', 'tz': 'Africa/Libreville', 'future_branch': 'futur',
                'publisher': {'name': 'Journal Officiel de la République Gabonaise (journal-officiel.ga)', 'email': 'journal-officiel@journal-officiel.invalid'},
                'default_in_force_rule': {'text': "Constitution art. 114: the Constitution is published in the Journal Officiel and executed as a law of the Republic. No general commencement rule for amending laws was read; the one version here is dated by the latest amending law named in the source.", 'source': U},
                'licence_note': "Text from the Journal Officiel de la République Gabonaise (www.journal-officiel.ga), the official gazette site. No licence is published on the site; Gabonese legislation is public law."},
    'sources': [{'name': 'Journal Officiel de la République Gabonaise, Droit gabonais: Constitution', 'url': U, 'retrieved': '2026-10-29', 'requests': 1,
                 'licence': 'none published; legislation is public law', 'notes': f'One page, sha256 {sha[:16]}. robots.txt: none found.'}],
    'laws': laws,
    'acts': [{'slug': 'constitution', 'short': 'Const.',
              'title': "Constitution de la République gabonaise (loi n°3/91 du 26 mars 1991, modifiée jusqu'à la loi n°046/2020 du 11 janvier 2021)", 'url': U,
              'first_law': None, 'earlier_laws': ['loi-3-91'] + [a[0] for a in amend],
              'versions': [{'from': '2021-01-11', 'source_url': U, 'sha256': sha, 'units': units, 'credits': {},
                            'note': "The consolidated text the Journal Officiel site prints, with the amendments of 1994, 1995, 1997, 2000, 2003, 2011, 2018 and 2021 already applied and no earlier version. This Constitution was replaced by the Constitution adopted by referendum on 16 November 2024 and promulgated on 19 December 2024, which the site's page does not carry; this text is therefore historical."}]}],
    'applies': [],
    'decisions': ["The only official text found online is the consolidated 1991 Constitution on journal-officiel.ga, last amended by loi n°046/2020 of 11 January 2021; it is a single 'oldest version available' dated 2021-01-11, the date of the last amending law.",
                  "The page's per-article amendment notes (for example '(Loi n°047/2010 du 12 janvier 2011)') are left out of headings; the amending laws are listed as earlier laws, not credited per article.",
                  "The 2024 Constitution (Journal Officiel n°47 bis, 19 December 2024) is not on the official site as text and is not included.",
                  "The signature blocks after article 114 are left out."],
    'ai_use': ['none']}
(here / 'corpus.json').write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
print(len(units), 'units')
