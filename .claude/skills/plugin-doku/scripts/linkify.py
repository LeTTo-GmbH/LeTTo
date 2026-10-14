"""Verlinkt Erwähnungen von DTOs, Enums, Controllern und Endpunkten in allen Seiten des Zielordners.
Aufruf: python -I linkify.py <zielordner> <manifest.json>"""
import os, re, sys, json

OUT, MAN = sys.argv[1:3]
man = json.load(open(MAN))
TYPES = man['types']                      # name -> dto|enum
CTRLS = man['controllers']
EPATHS = {}                               # anzeigepfad -> "Ctrl/meth"
EPMETH = {}                               # (ctrl, meth) -> True
for key, paths in man['endpoints'].items():
    c, m = key.split('/')
    EPMETH[(c, m)] = True
    for p in paths:
        # der reine Servicepfad ist mehrdeutig (Proxy-Präfix vs. Hilfeseite) und wird nicht verlinkt
        if p.rstrip('/') != '/<endpoint>': EPATHS.setdefault(p, key)
BARE_SKIP = {'Score'}                     # gewöhnliches Wort, nur in Backticks verlinken

def target(rel_page, kind, name):
    """relativer Link von der Seite (Pfad relativ zu OUT, Ordner) auf ein Ziel"""
    depth = 0 if rel_page in ('', '.') else rel_page.count('/') + 1
    up = '../' * depth
    if kind == 'type': return f'{up}{"dtos" if TYPES[name] == "dto" else "enums"}/{name}/index.md'
    if kind == 'ctrl': return f'{up}rest-schnittstelle/{name}/index.md'
    if kind == 'ep': return f'{up}rest-schnittstelle/{name}/index.md'

def self_of(rel_page):
    parts = rel_page.split('/')
    if parts[0] in ('dtos', 'enums') and len(parts) == 2: return ('type', parts[1])
    if parts[0] == 'rest-schnittstelle' and len(parts) == 2: return ('ctrl', parts[1])
    if parts[0] == 'rest-schnittstelle' and len(parts) == 3: return ('ep', parts[1] + '/' + parts[2])
    return None

NAME_RE = '|'.join(sorted(list(TYPES) + CTRLS, key=len, reverse=True))

def resolve_code(code):
    """Backtick-Inhalt -> (kind, ziel) oder None"""
    if code in EPATHS: return ('ep', EPATHS[code])
    m = re.fullmatch(r'(' + NAME_RE + r')((?:\.\w+)*)(\(\))?', code)
    if not m: return None
    n, member = m.group(1), m.group(2)
    if n in CTRLS:
        meth = member[1:].split('.')[0] if member else ''
        if meth and (n, meth) in EPMETH: return ('ep', f'{n}/{meth}')
        return ('ctrl', n)
    return ('type', n)

def process_text(seg, rel, me):
    # Backtick-Spans
    out, pos = [], 0
    for m in re.finditer(r'`([^`]+)`', seg):
        out.append(bare(seg[pos:m.start()], rel, me))
        r = resolve_code(m.group(1))
        if r and r != me: out.append(f'[{m.group(0)}]({target(rel, *r)})')
        else: out.append(m.group(0))
        pos = m.end()
    out.append(bare(seg[pos:], rel, me))
    return ''.join(out)

def bare(text, rel, me):
    def rep(m):
        n = m.group(1)
        if n in BARE_SKIP: return n
        kind = 'ctrl' if n in CTRLS else 'type'
        if (kind, n) == me: return n
        return f'[{n}]({target(rel, kind, n)})'
    # keine Treffer in URLs/Pfaden (vorher / . oder Buchstabe, nachher .html)
    return re.sub(r'(?<![\w/.\-\[])(' + NAME_RE + r')(?![\w.\-]*\.html)(?![\w\]])', rep, text)

LINK = re.compile(r'\[[^\]]*\]\([^)]*\)|<!--.*?-->|https?://\S+|\{% raw %\}.*?\{% endraw %\}')

def liquid(line):
    return re.sub(r'(?<!\{% raw %\})\{\{(\w+)\}\}', r'{% raw %}{{\1}}{% endraw %}', line)

for dirpath, _, files in os.walk(OUT):
    if 'index.md' not in files: continue
    rel = os.path.relpath(dirpath, OUT).replace('\\', '/')
    rel = '' if rel == '.' else rel
    me = self_of(rel)
    p = os.path.join(dirpath, 'index.md')
    lines = open(p, encoding='utf-8').read().split('\n')
    res, fence = [], False
    for i, line in enumerate(lines):
        if line.startswith('```'): fence = not fence; res.append(line); continue
        if fence: res.append(line); continue
        line = liquid(line)
        if line.startswith('#') or line.startswith('<!--'): res.append(line); continue
        out, pos = [], 0
        for m in LINK.finditer(line):
            out.append(process_text(line[pos:m.start()], rel, me)); out.append(m.group(0)); pos = m.end()
        out.append(process_text(line[pos:], rel, me))
        res.append(''.join(out))
    open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(res))
print('linkify ok')
