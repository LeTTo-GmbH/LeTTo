"""Prüft die Doku des Python-Referenz-Plugins gegen den Code.
Aufruf (vom LeTTo-Repo-Root): python -I .claude/skills/plugin-doku-python/scripts/check.py [../plugin-demo-python]

Prüft:
  1. jeder Endpunkt aus app/main.py kommt in rest-schnittstelle/index.md vor
  2. jedes Pydantic-Modell kommt in dtos/index.md vor
  3. Feldvergleich Python-Modelle <-> Java-DTOs (aus den generierten Java-Doku-Seiten) – Abweichungen müssen in dtos/index.md stehen
  4. jede CONF_*-Konstante kommt in plugin-api/index.md vor
  5. alle relativen Links und Bilder der Python-Seiten existieren, kein ungeschütztes <…> oder {{…}}
  6. Quell-Commit im Kommentar jeder Seite
Exit-Code 1 bei Fehlern."""
import os, re, subprocess, sys

SRC = sys.argv[1] if len(sys.argv) > 1 else '../plugin-demo-python'
DOC = 'docs/wiki/Plugins/referenz-plugin-python'
JAVA_DTOS = 'docs/wiki/Plugins/referenz-plugin-java/dtos'
main = open(os.path.join(SRC, 'app/main.py'), encoding='utf-8').read()
def page(rel): return open(os.path.join(DOC, rel, 'index.md'), encoding='utf-8').read()
errors, notes = [], []

# ---- Konstanten für Pfade
consts = dict(re.findall(r'^(\w+)(?:\s*:\s*\w+)?\s*=\s*f?"([^"]*)"', main, re.M))
sp = re.search(r'CONF_STANDARD_SERVICEPATH\s*=\s*"([^"]+)"', main).group(1)
def expand(expr):
    expr = expr.strip()
    if expr.startswith(('f"', '"')):
        s = expr[expr.index('"') + 1:-1]
        s = s.replace('{SERVICEPATH}', '<servicepath>')
        return re.sub(r'\{(\w+)\}', lambda m: expand(consts.get(m.group(1), '')) if m.group(1) in consts else m.group(0), s)
    if expr in consts:
        return expand('f"' + consts[expr] + '"')
    return expr

# ---- 1. Endpunkte
routers = {'app': ''}
for name, prefix in re.findall(r'^(\w+)\s*=\s*APIRouter\(prefix=(\w+)\)', main, re.M):
    routers[name] = expand(prefix)
mounts = [expand(m) for m in re.findall(r'include_router\(mount_internal_open\(([^)]+)\)\)', main)]
routes = []
for router, path in re.findall(r'@(\w+)\.(?:get|post|put|delete)\(\s*([^,)]+)', main):
    path = expand(path) if not path.strip().startswith('"') else path.strip().strip('"')
    path = path.replace('{SERVICEPATH}', '<servicepath>')
    if router == 'r':
        routes += [m + path for m in mounts]
    else:
        routes.append(routers.get(router, '') + path)
rest = page('rest-schnittstelle')
for r in sorted(set(routes)):
    r = r.replace(sp, '<servicepath>')
    # Pfade unter <servicepath>/open sind in der Doku über /open beschrieben
    probe = r.replace('<servicepath>/open/', '/open/', 1) if r.startswith('<servicepath>/open/') else r
    if f'`{r}`' not in rest and f'`{probe}`' not in rest and r.rstrip('/') + '/' not in rest:
        errors.append(f'Endpunkt fehlt in rest-schnittstelle: {r}')
print(f'Endpunkte im Code: {len(set(routes))}')

# ---- 2./3. Modelle
models = {}
for m in re.finditer(r'^class (\w+)\(BaseModel\):\n((?:    .*\n|\n)*?)(?=^\S)', main, re.M):
    models[m.group(1)] = [f for f in re.findall(r'^    (\w+):', m.group(2), re.M) if f != 'model_config']
dtos = page('dtos')
for n in models:
    if f'`{n}`' not in dtos: errors.append(f'Modell fehlt in dtos: {n}')
for n, fields in sorted(models.items()):
    p = os.path.join(JAVA_DTOS, n, 'index.md')
    if not os.path.exists(p):
        notes.append(f'{n}: keine Java-DTO-Seite'); continue
    s = open(p, encoding='utf-8').read()
    sec = s.split('## Felder')[1].split('\n## ')[0] if '## Felder' in s else ''
    jf = set(re.findall(r'^\| `(\w+)` \|', sec, re.M))
    alias = set(re.findall(r'alias="(\w+)"', main))
    pf = set(fields)
    extra, miss = sorted(pf - jf), sorted(jf - pf - alias)
    extra = [e for e in extra if not (e.endswith('_value') and e[:-6] in alias)]
    if extra or miss:
        line = f'{n}: nur Python {extra}, fehlt in Python {miss}'
        notes.append(line)
        # Felder nur in Python müssen einzeln genannt sein; fehlende Java-Felder reichen als Vermerk in der Übersichtszeile
        for f in extra:
            if f'`{f}`' not in dtos: errors.append(f'Feldabweichung nicht in dtos dokumentiert: {n}.{f}')
        row = re.search(r'^\| `' + n + r'` \|.*\| (.*) \|$', dtos, re.M)
        if miss and (not row or row.group(1).strip() == '–'):
            errors.append(f'{n}: Java-Felder {miss} fehlen in Python, Übersichtszeile in dtos nennt keine Abweichung')
print(f'Pydantic-Modelle: {len(models)}')

# ---- 4. CONF-Konstanten
api = page('plugin-api')
for c in sorted(set(re.findall(r'^(CONF_\w+)\s*=', main, re.M))):
    if c not in api: errors.append(f'Konstante fehlt in plugin-api: {c}')

# ---- 5./6. Links, Maskierung, Kommentar
head = subprocess.run(['git', '-C', SRC, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
for d, _, fs in os.walk(DOC):
    if 'index.md' not in fs: continue
    p = os.path.join(d, 'index.md'); s = open(p, encoding='utf-8').read()
    code = re.sub(r'```.*?```', '', s, flags=re.S)
    for l in re.findall(r'\]\(([^)#\s:]+\.(?:md|png|jpg|gif|svg))(?:#[^)]*)?\)', code):
        if not os.path.exists(os.path.normpath(os.path.join(d, l))): errors.append(f'kaputter Link: {p} -> {l}')
    txt = re.sub(r'<!--.*?-->', '', re.sub(r'`[^`]*`', '', code))
    for m in re.findall(r'<(?!br>|!--)[a-zA-Z][^>]*>', txt): errors.append(f'ungeschütztes {m} in {p}')
    if re.search(r'(?<!% raw %\})\{\{', s): errors.append(f'ungeschütztes {{{{ in {p}')
    m = re.search(r'plugin-demo-python @ (\w+)', s)
    if not m: errors.append(f'Quell-Kommentar fehlt: {p}')
    elif head and m.group(1) != head: notes.append(f'{p}: Kommentar {m.group(1)}, Plugin-Repo ist auf {head}')

for n in notes: print('Hinweis:', n)
for e in errors: print('FEHLER:', e)
print('OK' if not errors else f'{len(errors)} Fehler')
sys.exit(1 if errors else 0)
