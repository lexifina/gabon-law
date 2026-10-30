import re, html
def page_text(path):
    t = open(path, 'rb').read().decode('utf8')
    b = re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S)
    b = re.sub(r'<(?:br|/p|/div|/h\d|/li|/tr)[^>]*>', '\n', b)
    b = re.sub(r'<[^>]+>', '', b)
    b = html.unescape(b).replace('\xa0', ' ').replace('​', '').replace('﻿', '')
    b = re.sub(r'[ \t]+', ' ', b)
    return [l.strip() for l in b.split('\n') if l.strip()]
HEAD = re.compile(r'^(LIVRE|TITRE|CHAPITRE|Chapitre|SECTION|Section|Sous-section|SOUS-SECTION|Paragraphe|PARAGRAPHE|Dispositions (transitoires|finales|générales)|PARLEMENT|PARTIE|PREMIERE PARTIE|DEUXIEME PARTIE|Première partie|Deuxième partie|TITRE PRELIMINAIRE)\b')
ART = re.compile(r'^Article\s+(premier|1er|\d+(?:er)?)(?:\s*[-–]\s*(\d+(?:\.\d+)?))?(?:\s*[-–]?\s*(bis|ter|quater|quinquies|sexies|septies))?\s*(nouveau)?\s*:\s*(.*)$', re.I)
def key_of(a):
    n, sub, suf = a
    n = 1 if n.lower() in ('premier', '1er') else int(n.rstrip('er'))
    k = 'art-%03d' % n
    if sub: k += '-%s' % sub.replace('.', '-')
    if suf: k += '-' + suf.lower()
    return k
def label_of(m):
    n = m.group(1); n = '1er' if n.lower() in ('premier', '1er') else n
    s = 'Article ' + n
    if m.group(2): s += '-' + m.group(2)
    if m.group(3): s += ' ' + m.group(3).lower()
    return s
def articles(lines):
    """-> ordered dict key -> {'label', 'p': [paragraphs]}"""
    out = {}; cur = None; skip = False
    for l in lines:
        m = ART.match(l)
        if m:
            k = key_of(m.groups()[:3])
            if k in out: raise SystemExit('duplicate ' + k)
            cur = out[k] = {'label': label_of(m), 'p': []}
            skip = False
            if m.group(5): cur['p'].append(m.group(5))
            continue
        if HEAD.match(l):
            skip = True; continue
        if cur is None or skip: 
            if skip and cur is not None and False: pass
            continue
        cur['p'].append(l)
    return out
