"""Generiert die Detailseiten (Controller, Endpunkte, DTOs, Enums) der Referenz-Plugin-Doku.
Aufruf: python -I gen.py <plugin-repo> <zielordner> <hash> <revision> <manifest.json>
Das Manifest (Typen, Controller, Endpunkt-Pfade) wird von linkify.py gelesen."""
import os, re, sys, json, shutil

SRC, OUT, HASH, REV = sys.argv[1:5]
JAVA = os.path.join(SRC, 'src/main/java/at/letto/plugins')
CMT = f'<!-- generiert aus plugin-demo-java @ {HASH} (revision {REV}) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->'
EP = '<endpoint>'

def read(p): return open(p, encoding='utf-8-sig').read()

# ---------------------------------------------------------------- Javadoc
def jd_clean(t):
    t = re.sub(r'\{@code\s+([^}]*)\}', r'`\1`', t)
    t = re.sub(r'\{@link\s+([^}]*)\}', r'`\1`', t)
    return t

def jd_lines(block):
    out = []
    for l in block.split('\n'):
        l = l.strip()
        l = re.sub(r'^/\*\*\s?', '', l); l = re.sub(r'\*/$', '', l); l = re.sub(r'^\*\s?', '', l)
        out.append(l.rstrip())
    return out

def html2md(t):
    t = jd_clean(t)
    t = re.sub(r'<br\s*/?>', ' ', t, flags=re.I)
    t = re.sub(r'</?(b|i|p)>', '', t, flags=re.I)
    t = re.sub(r'\s+', ' ', t).strip()
    # verbleibende spitze Klammern außerhalb von Backticks maskieren
    parts = t.split('`')
    for i in range(0, len(parts), 2):
        parts[i] = parts[i].replace('<', '&lt;').replace('>', '&gt;')
    t = '`'.join(parts)
    return liquid(t.replace('|', '\\|'))

def liquid(t):
    return re.sub(r'\{\{(\w+)\}\}', r'{% raw %}{{\1}}{% endraw %}', t)

def parse_javadoc(block):
    """liefert (beschreibung, {tag: [texte]}) ; Zeilenumbrüche via <br> bleiben als \n"""
    lines = jd_lines(block)
    desc, tags, cur = [], [], None
    for l in lines:
        m = re.match(r'@(\w+)\s*(.*)', l)
        if m:
            cur = [m.group(1), m.group(2)]; tags.append(cur)
        elif cur: cur[1] += '\n' + l
        else: desc.append(l)
    return '\n'.join(desc).strip(), tags

def first_sentence(t):
    t = html2md(t)
    m = re.match(r'(.+?[.!])(\s|$)', t)
    return (m.group(1) if m else t).rstrip('.')

# ---------------------------------------------------------------- Endpoint-Konstanten
ep_src = read(os.path.join(JAVA, 'config/Endpoint.java'))
CONST = {}
for name, expr in re.findall(r'public static final String\s+(\w+)\s*=\s*([^;]+);', ep_src):
    CONST[name] = expr.strip()
def resolve(expr):
    res = ''
    for part in expr.split('+'):
        part = part.strip()
        if part.startswith('"'): res += part.strip('"')
        else:
            part = part.replace('Endpoint.', '')
            res += resolve(CONST[part])
    return res
SERVICEPATH = resolve(CONST['servicepath'])
def disp(path):  # /plugindemo -> /<endpoint>
    return '/' + EP + path[len(SERVICEPATH):] if path.startswith(SERVICEPATH) else path

# ---------------------------------------------------------------- DTOs / Enums
TYPES = {}   # name -> dict
def parse_class(path, kind):
    s = jd_clean(read(path))   # {@code ..} vorab ersetzen, sonst stören die Klammern beim Entfernen der Methodenrümpfe
    name = os.path.splitext(os.path.basename(path))[0]
    cm = re.search(r'(/\*\*(?:(?!\*/).)*\*/)\s*(?:@[\w()\s.,=",]*\s*)*public\s+(?:abstract\s+)?(class|enum)\s+' + name, s, re.S)
    cdoc = parse_javadoc(cm.group(1))[0] if cm else ''
    body = s[s.index('{', cm.end() if cm else 0) + 1:]
    if kind == 'dto':
        # Kommentare durch Platzhalter ersetzen, damit Klammern/Semikolons darin nicht stören
        comments = []
        def keep(m):
            comments.append(m.group(0)); return f' @@C{len(comments) - 1}@@ '
        body = re.sub(r'/\*.*?\*/', keep, body, flags=re.S)
        body = re.sub(r'//[^\n]*', '', body)
    # nur Text auf Klassenebene behalten (Methodenrümpfe und Initialisierer entfernen)
    flat, depth = [], 0
    for ch in (body if kind == 'dto' else ''):
        if ch == '{': depth += 1; continue
        if ch == '}':
            depth -= 1
            if depth < 0: break
            if depth == 0: flat.append(';')
            continue
        if depth == 0: flat.append(ch)
    if kind == 'dto': body = ''.join(flat)
    t = {'name': name, 'kind': kind, 'doc': cdoc, 'fields': [], 'consts': [], 'values': []}
    if kind == 'enum':
        # Werte bis zum ersten ';' oder Methodenbeginn
        m = re.match(r'(.*?)(;|\}\s*$)', body, re.S)
        part = m.group(1)
        items = re.findall(r'((?:/\*\*(?:(?!\*/).)*\*/\s*)?)(?://[^\n]*\n\s*)*([A-Za-z_]\w*)\s*(?:,|\s*$)', part, re.S)
        for doc, v in items:
            t['values'].append((v, html2md(parse_javadoc(doc)[0]) if doc else ''))
    else:
        for stmt in body.split(';'):
            # letzter Kommentar vor der Deklaration ist deren Doku
            docs = re.findall(r'@@C(\d+)@@', stmt)
            decl = re.sub(r'@@C\d+@@', ' ', stmt)
            decl = re.sub(r'@\w+(?:\([^)]*\))?', ' ', decl).strip()
            m = re.fullmatch(r'((?:(?:public|private|protected|static|final|transient|volatile)\s+)*)([\w<>\[\],\s.]+?)\s+(\w+)\s*(?:=\s*(.+))?', decl, re.S)
            if not m or '(' in m.group(2): continue
            mods, typ, fname, default = m.groups()
            doc = comments[int(docs[-1])] if docs and comments[int(docs[-1])].startswith('/**') else ''
            d = html2md(parse_javadoc(doc)[0]) if doc else ''
            typ = re.sub(r'\s+', ' ', typ.strip())
            entry = (fname, typ, (default or '').strip(), d)
            if 'static' in mods and 'final' in mods: t['consts'].append(entry)
            elif 'static' in mods: continue
            else: t['fields'].append(entry)
    TYPES[name] = t

for f in sorted(os.listdir(os.path.join(JAVA, 'dto'))):
    parse_class(os.path.join(JAVA, 'dto', f), 'dto')
for f in sorted(os.listdir(os.path.join(JAVA, 'enums'))):
    parse_class(os.path.join(JAVA, 'enums', f), 'enum')
NAMES = sorted(TYPES, key=len, reverse=True)
def refs(typ):
    return [n for n in TYPES if re.search(r'\b' + n + r'\b', typ)]

# ---------------------------------------------------------------- Controller
CONTROLLERS = []
for f in sorted(os.listdir(os.path.join(JAVA, 'controller'))):
    s = read(os.path.join(JAVA, 'controller', f)); cname = f[:-5]
    cm = re.search(r'(/\*\*(?:(?!\*/).)*\*/)\s*@RestController', s, re.S)
    cdoc = parse_javadoc(cm.group(1))[0] if cm else ''
    rm = re.search(r'@RequestMapping\(([^)]*)\)', s)
    base = resolve(rm.group(1)) if rm else ''
    tm = re.search(r'@Tag\([^)]*?description\s*=\s*((?:"[^"]*"\s*\+?\s*)+)', s, re.S)
    tag = ''.join(re.findall(r'"([^"]*)"', tm.group(1))) if tm else ''
    tag = re.sub(r'\s*\[JavaDoc\]\([^)]*\)', '', tag).strip()
    eps = []
    for m in re.finditer(r'(/\*\*(?:(?!\*/).)*?\*/)\s*((?:@\w+(?:\((?:[^()]|\([^()]*\))*\))?\s*|//[^\n]*\n\s*)+)public\s+([\w<>\[\], ]+?)\s+(\w+)\s*\(([^)]*)\)\s*\{', s, re.S):
        doc, annos, ret, meth, params = m.groups()
        mm = re.search(r'@(Get|Post|Put|Delete)Mapping\((.*?)\)\s*(?:$|@|//)', annos + '\n', re.S)
        if not mm: continue
        verb = mm.group(1).upper(); arg = mm.group(2)
        produces = ''
        pm = re.search(r'produces\s*=\s*MediaType\.(\w+)', arg)
        if pm: produces = {'TEXT_HTML_VALUE': 'text/html'}.get(pm.group(1), pm.group(1))
        vm = re.search(r'value\s*=\s*(\{[^}]*\}|[^,]+)', arg)
        varg = vm.group(1) if vm else arg
        paths = [base + resolve(p) for p in varg.strip('{} ').split(',') if p.strip()]
        # Rumpf
        depth, i = 1, m.end()
        while depth: depth += {'{': 1, '}': -1}.get(s[i], 0); i += 1
        body = s[m.end():i - 1]
        rt = re.match(r'ResponseEntity<(.*)>$', ret.strip()); rt = rt.group(1) if rt else ret.strip()
        req, rparams = None, []
        for p in [p.strip() for p in params.split(',') if p.strip()]:
            pm2 = re.match(r'@(RequestBody|RequestParam)\s+([\w<>\[\]]+)\s+(\w+)', p)
            if pm2:
                if pm2.group(1) == 'RequestBody': req = (pm2.group(2), pm2.group(3))
                else: rparams.append((pm2.group(2), pm2.group(3)))
        desc, tags = parse_javadoc(doc)
        jfields, pdocs, retdoc, throws = {}, {}, '', []
        for tg, txt in tags:
            if tg == 'param':
                pn, rest = (txt.split(None, 1) + [''])[:2]
                pdocs[pn] = rest
                for fl in re.findall(r'\b\w+\.(\w+)\s+([\w\[\]<>]+)\s*:\s*([^\n]*)', rest):
                    jfields[fl[0]] = (fl[1], html2md(fl[2]))
            elif tg == 'return': retdoc = txt
            elif tg == 'throws': throws.append(txt)
        used = sorted(set(re.findall(r'\b(?:r|dto)\.(?:get|is)(\w+)\(\)', body)))
        used = [u[0].lower() + u[1:] for u in used]
        calls = re.findall(r'createPluginService\([^;]*?\)\s*\.(\w+)\(', body, re.S)
        calls += re.findall(r'pluginService\s*\.(\w+)\(', body)
        cfg = re.findall(r'pluginConfiguration\.(\w+)\(', body)
        deleg = re.findall(r'apiController\.(\w+)\(', body)
        eps.append(dict(ctrl=cname, meth=meth, verb=verb, paths=paths, produces=produces, ret=rt, req=req, rparams=rparams,
                        desc=desc, jfields=jfields, pdocs=pdocs, retdoc=retdoc, throws=throws, used=used, calls=calls,
                        cfg=cfg, deleg=deleg, body=body))
    CONTROLLERS.append(dict(name=cname, doc=cdoc, base=base, tag=tag, eps=eps))
EPS = {(e['ctrl'], e['meth']): e for c in CONTROLLERS for e in c['eps']}
api_src = read(os.path.join(JAVA, 'controller/ApiController.java'))

def extern(path): return path.startswith(SERVICEPATH)
def reach(e): return 'extern über den Proxy' if extern(e['paths'][0]) else 'nur im Docker-Netzwerk'
def short(e): return first_sentence(e['desc']) if e['desc'] else first_sentence(e['retdoc'])

# ---------------------------------------------------------------- Plugin-API (PluginService)
ps = read(os.path.join(JAVA, 'plugin/PluginService.java'))
PAPI = []
for doc, sig in re.findall(r'(/\*\*(?:(?!\*/).)*?\*/)\s*(?://[^\n]*\n\s*)*(?:default\s+)?([\w<>\[\], .]+?\s+\w+\s*\([^)]*\))', ps, re.S):
    sig = re.sub(r'\s+', ' ', sig.strip())
    mn = re.search(r'(\w+)\s*\(', sig).group(1)
    PAPI.append((mn, sig, refs(sig)))

# ---------------------------------------------------------------- Zuordnung Typ -> Verwendungen
USAGE = {n: [] for n in TYPES}   # (key, rolle, pfad)
def walk(t, key, role, path, seen):
    USAGE[t].append((key, role, tuple(path)))
    if t in seen: return
    for fname, ftyp, _, _ in TYPES[t]['fields']:
        for u in refs(ftyp):
            if u not in seen | {t}:
                walk(u, key, role, path + [f'{t}.{fname}'], seen | {t})
for key, e in EPS.items():
    if e['req']:
        for t in refs(e['req'][0]): walk(t, key, 'Request', [], set())
    for t in refs(e['ret']): walk(t, key, 'Response', [], set())
OUTGOING = ('ausgehend', 'registerplugin')
for t in refs('ConfigServiceDto'): walk(t, OUTGOING, 'Request', [], set())
for t in refs('RegisterServiceResultDto'): walk(t, OUTGOING, 'Response', [], set())
IN_DTO = {n: [] for n in TYPES}
for t in TYPES.values():
    for fname, ftyp, _, _ in t['fields']:
        for u in refs(ftyp):
            if u != t['name']: IN_DTO[u].append((t['name'], fname))

# ---------------------------------------------------------------- Link-Helfer
# depth: Anzahl Ebenen unterhalb des Zielordners (1 = dtos/X, 2 = rest-schnittstelle/C/m ...)
def root(depth): return '../' * depth
def lt(n, depth):
    t = TYPES[n]; d = 'dtos' if t['kind'] == 'dto' else 'enums'
    return f'{root(depth)}{d}/{n}/index.md'
def le(key, depth): return f'{root(depth)}rest-schnittstelle/{key[0]}/{key[1]}/index.md'
def lc(c, depth): return f'{root(depth)}rest-schnittstelle/{c}/index.md'
def type_md(typ, depth):
    """Typstring mit Links, Generics maskiert"""
    toks = re.split(r'(\b(?:' + '|'.join(NAMES) + r')\b)', typ)
    out = ''
    for tk in toks:
        if tk in TYPES: out += f'[{tk}]({lt(tk, depth)})'
        else: out += tk.replace('<', '&lt;').replace('>', '&gt;')
    return out
def ep_label(key):
    if key == OUTGOING: return 'POST /config/auth/user/registerplugin (Setup-Service)'
    e = EPS[key]; return f'{e["verb"]} {disp(e["paths"][0])}'
def ep_link(key, depth):
    if key == OUTGOING:
        return f'[`POST /config/auth/user/registerplugin`]({root(depth)}build-deployment/index.md#registrierung-am-letto-server) (ausgehend, Setup-Service)'
    return f'[`{ep_label(key)}`]({le(key, depth)})'
def ep_short(key):
    if key == OUTGOING: return 'Registrierung des Plugin-Services am Setup-Service beim Start'
    return short(EPS[key])
def papi_link(mn, depth): return f'[`{mn}`]({root(depth)}plugin-api/index.md)'

def write(rel, text):
    p = os.path.join(OUT, rel, 'index.md')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8', newline='\n').write(text.rstrip() + '\n')

def nav(depth, extra):
    links = ' · '.join(f'[{t}]({u})' for t, u in extra)
    return '\n' + links + '\n'

# ---------------------------------------------------------------- manuelle Ergänzungen
SEE_ALSO = {
    ('ApiExternOpenController', 'pluginList'): [('ApiController', 'pluginList')],
    ('ApiExternOpenController', 'pluginGeneralInfoList'): [('ApiController', 'pluginGeneralInfoList')],
    ('ApiExternOpenController', 'pluginGeneralInfo'): [('ApiController', 'pluginGeneralInfo')],
    ('ApiExternOpenController', 'reloadPluginDto'): [('ApiController', 'reloadPluginDto'), ('ApiController', 'setConfigurationData')],
    ('ApiController', 'pluginList'): [('ApiExternOpenController', 'pluginList'), ('ApiController', 'pluginGeneralInfoList')],
    ('ApiController', 'pluginGeneralInfoList'): [('ApiExternOpenController', 'pluginGeneralInfoList'), ('ApiController', 'pluginGeneralInfo')],
    ('ApiController', 'pluginGeneralInfo'): [('ApiExternOpenController', 'pluginGeneralInfo'), ('ApiController', 'pluginGeneralInfoList')],
    ('ApiController', 'getHtml'): [('ApiController', 'loadPluginDto')],
    ('ApiController', 'getAngabe'): [('ApiController', 'generateDatasets'), ('ApiController', 'modifyAngabe')],
    ('ApiController', 'generateDatasets'): [('ApiController', 'getVars'), ('ApiController', 'getAngabe')],
    ('ApiController', 'getVars'): [('ApiController', 'generateDatasets')],
    ('ApiController', 'getMaxima'): [('ApiController', 'parserPlugin')],
    ('ApiController', 'getImage'): [('ApiController', 'getImageUrl'), ('ApiController', 'getImageTemplates'), ('ApiController', 'loadPluginDto')],
    ('ApiController', 'getImageUrl'): [('ApiController', 'getImage'), ('ApiController', 'loadPluginDto')],
    ('ApiController', 'getImageTemplates'): [('ApiController', 'getImage')],
    ('ApiController', 'parserPlugin'): [('ApiController', 'parserPluginEinheit'), ('ApiController', 'getMaxima')],
    ('ApiController', 'parserPluginEinheit'): [('ApiController', 'parserPlugin')],
    ('ApiController', 'score'): [('ApiController', 'loadPluginDto'), ('ApiController', 'renderPluginResult')],
    ('ApiController', 'modifyAngabe'): [('ApiController', 'modifyAngabeTextkomplett')],
    ('ApiController', 'modifyAngabeTextkomplett'): [('ApiController', 'modifyAngabe')],
    ('ApiController', 'updatePluginstringJavascript'): [('ApiController', 'loadPluginDto')],
    ('ApiController', 'loadPluginDto'): [('ApiController', 'score'), ('ApiController', 'reloadPluginDto'), ('ApiController', 'renderLatex')],
    ('ApiController', 'renderLatex'): [('ApiController', 'renderPluginResult'), ('ApiController', 'loadPluginDto')],
    ('ApiController', 'renderPluginResult'): [('ApiController', 'score'), ('ApiController', 'renderLatex')],
    ('ApiController', 'configurationInfo'): [('ApiController', 'setConfigurationData'), ('ConfigHttpController', 'configHttp'), ('ApiController', 'getConfiguration')],
    ('ApiController', 'setConfigurationData'): [('ApiController', 'configurationInfo'), ('ApiExternOpenController', 'reloadPluginDto'), ('ApiController', 'getConfiguration')],
    ('ApiController', 'getConfiguration'): [('ApiController', 'configurationInfo'), ('ApiController', 'setConfigurationData')],
    ('ApiController', 'reloadPluginDto'): [('ApiExternOpenController', 'reloadPluginDto'), ('ApiController', 'loadPluginDto'), ('ApiController', 'configurationInfo')],
    ('ConfigHttpController', 'configHttp'): [('ApiController', 'configurationInfo'), ('ApiController', 'setConfigurationData'), ('ApiExternOpenController', 'reloadPluginDto'), ('ApiController', 'getConfiguration')],
    ('InfoController', 'ping'): [('InfoController', 'pingopen')],
    ('InfoController', 'pingopen'): [('InfoController', 'ping')],
    ('InfoController', 'info'): [('InfoController', 'infoOpen'), ('InfoController', 'version')],
    ('InfoController', 'infoOpen'): [('InfoController', 'info')],
    ('InfoController', 'version'): [('InfoController', 'info')],
}
EP_NOTES = {
    ('ApiController', 'configurationInfo'): [
        'Legt eine Konfigurationssitzung (`PluginConfigurationConnection`) an bzw. aktualisiert sie; ohne `configurationID` erzeugt der Service eine zufällige ID (30 Zeichen).',
        'Der Controller setzt `configurationUrl` auf `<letto.plugin.uri.extern>/<endpoint>/open/confighttp?typ=<typ>&configurationID=<id>` (URL-codiert).',
        'Bei jedem Zugriff werden Sitzungen entfernt, deren letzter Zugriff länger als `timeout` Sekunden zurückliegt.',
        'Kann das Plugin nicht erzeugt werden, wird ein leeres `PluginConfigurationInfoDto` geliefert (kein 404).'],
    ('ApiController', 'setConfigurationData'): [
        'Ruft `setConfigurationData` des Plugins auf und ergänzt im Ergebnis `configurationID`, `typ`, `name`, `config`, `tagName` sowie ein `pluginDto` (über `loadPluginDto` mit leeren Parametern).',
        'Der Controller setzt `pluginDtoUri` auf den externen Endpunkt `/<endpoint>/api/open/reloadplugindto` und `pluginDtoToken` auf einen Leerstring.',
        'Ohne gültige Sitzung enthält das Ergebnis `errorMsg = "cannot find connection or plugin"`.'],
    ('ApiController', 'getConfiguration'): [
        'Fehler werden nicht als HTTP-Status, sondern im Text gemeldet: `@Error:cannot find connection or plugin` bzw. `@Error: error during configuration of plugin`.'],
    ('ApiController', 'reloadPluginDto'): [
        'Sucht die Sitzung zur `configurationID`, erzeugt das Plugin mit der übergebenen `config` neu und aktualisiert damit die Sitzung (`changeConfig`), sodass `getconfiguration` danach die neue Konfiguration liefert.',
        'Das `PluginDto` wird mit der in der Sitzung gespeicherten Frage (`pluginQuestionDto`) erzeugt, `q` aus dem Request wird ignoriert.'],
    ('ApiController', 'pluginGeneralInfo'): ['Der Request-Body ist der Plugin-Typ als reiner String (kein JSON-Objekt).'],
    ('ApiExternOpenController', 'pluginGeneralInfo'): ['Der Request-Body ist der Plugin-Typ als reiner String (kein JSON-Objekt).'],
    ('ApiController', 'getImageUrl'): [
        'Das Bild wird über `parseDrawParams` und `paint` erzeugt und im Image-Service des Plugins gespeichert (Verzeichnis `letto.pathPlugins` + Servicepfad); `imageUrl` und `imageInfoDto.url` enthalten die öffentliche URL.',
        'Der LeTTo-Server ruft diesen Endpunkt vor `image` auf. Liefert er keine URL oder schlägt er fehl, verwendet der Server das Base64-Bild von `image`.',
        'Kann das Bild nicht gespeichert werden, steht die Meldung in `error`.'],
    ('ApiController', 'getImageTemplates'): ['Die Antwort ist ein Array von String-Arrays: [0] beschreibender Text, [1] PIG-Tag, [2] Hilfetext.'],
    ('ConfigHttpController', 'configHttp'): [
        'Die Seite bindet `' + EP + '/open/js/jquery-3.6.0.min.js` und den Quelltext aller lokalen JavaScript-Libraries des Plugins (`javascriptLibrariesLocal()`) ein.',
        'Sie enthält `<div id="configform_div">`, das versteckte Feld `.configform_config` mit der aktuellen Konfiguration und das `PluginConfigDto` als JSON in `<script id="pluginConfigDto">`.',
        'Anschließend wird die Konfigurations-Methode des Plugins (`javaScriptMethode` aus `PluginConfigurationInfoDto`) mit dem JSON-String aufgerufen. Der Methodenname muss ein gültiger JavaScript-Bezeichner sein.',
        'Fehlt im `PluginConfigDto` die `pluginDtoUri`, wird sie auf den externen `reloadplugindto`-Endpunkt gesetzt.'],
    ('HelpController', 'help'): ['Die Seite stammt aus `src/main/resources/help/index.html`; `{{servicepath}}`, `{{name}}` und `{{version}}` werden beim Start einmalig ersetzt.'],
    ('InfoController', 'ping'): ['Wird vom Docker-Healthcheck (`scripts/healthcheck.sh`) aufgerufen; erwartet wird genau `pong`.'],
    ('InfoController', 'info'): ['Die Informationen werden beim ersten Aufruf ermittelt und danach zwischengespeichert (Startzeit, Laufzeit usw. ändern sich daher nicht mehr).'],
    ('InfoController', 'infoOpen'): ['Die Informationen werden beim ersten Aufruf ermittelt und danach zwischengespeichert.'],
}
ERRORS = {
    'plugin': '404 Not Found, wenn der Plugin-Typ nicht registriert ist oder das Plugin nicht erzeugt werden kann („Plugin vom Typ … kann nicht erzeugt werden").',
}
DTO_NOTES = {
    'PluginConfigurationConnection': ['**Interne Klasse, wird nicht über REST übertragen.** Sie hält im Plugin-Service den Zustand einer Konfigurationssitzung; `PluginConfiguration` speichert die Sitzungen nach `configurationID`.',
                                      'Der Konstruktor erzeugt eine zufällige ID (30 Zeichen), wenn keine `configurationID` übergeben wird, und legt ein `PluginConfigDto` mit Größe 800×600 an.',
                                      '`changeConfig(config, pluginService)` setzt Konfiguration und Plugin-Instanz neu und holt `configurationInfo` vom Plugin.'],
    'PluginDto': ['Konstruktor `PluginDto(params, pluginService, q, nr)`: setzt `tagName = <frageId>_<name>_<nr>`, übernimmt `size=` aus den Parametern und erzeugt das Bild – zuerst über `getImageUrl`, sonst als `data:image/png;base64,…` über `getImageDto`; `width`/`height` kommen danach vom Plugin.',
                  'Konstruktor `PluginDto(params, name, nr, idQuestion)`: nur Tag-Name und Größe.',
                  '`toJson()` liefert das DTO als JSON.'],
    'PluginConfigDto': ['Konstruktoren mit `params` übernehmen `size=<B>x<H>` bzw. `size=<N>` aus den durch Komma getrennten Parametern.'],
    'JavascriptLibrary': ['Konstruktoren: `(path)` lokale Ressource, `(name, jscode, true)` Quelltext (Modus `JAVASCRIPT`), `(server, path)` bzw. `(server, pathlocal, pathGlobal)` externe Library (Modus `SERVER`).',
                          '`loadPath(localServer)` liefert den Ladepfad je nach Modus; `equals(lib)` vergleicht Modus, Name und ggf. Serverpfad.'],
    'ToleranzDto': ['Der Standardkonstruktor erzeugt eine relative Toleranz von `1e-10`.', '`relativ()` / `absolut()` prüfen den Modus.'],
    'VarHashDto': ['`getString(key)` liefert den Textwert einer Variablen (oder `""`), `getCalcErgebnisDto(key)` deren Wert (oder `null`).', '`toString()` liefert `name=wert,…`.'],
    'CalcErgebnisDto': ['`toString()` liefert je nach `type` den JSON-String (`CALCULATE`), den String (`STRING`) bzw. `error`.'],
    'ImageInfoDto': ['`lifetimeOutdated()` prüft, ob `lifetime` überschritten ist.'],
    'ConfigServiceDto': ['`htmlServiceStartTime()` / `htmlLastRegistrationTime()` formatieren die Zeitpunkte für die Anzeige.',
                         'Das Demo übergibt in `programmingLanguage` die Java-Version (`serverStatus.getJavaVersion()`).'],
    'PluginGeneralInfo': ['Das Feld `useVarsMaxima` heißt in `BasePlugin` und `PluginConfigurationInfoDto` `useMaximaVars`. Der Name ist Teil der REST-Schnittstelle und wird vom LeTTo-Server so gelesen – er darf nicht angeglichen werden.'],
    'PluginRenderLatexRequestDto': ['`mode` lässt sich derzeit nicht auswerten: Der LeTTo-Server übergibt `TexPrintMode.toString()`, und diese Klasse hat kein eigenes `toString()` – das Plugin erhält nur einen Objekt-Bezeichner wie `at.letto.tools.tex.TexPrintMode@6d06d69c`.'],
    'PluginQuestionDto': ['`clone()` liefert eine flache Kopie.'],
    'ServiceInfoDTO': ['Im Demo bleibt `endpoints` leer und `jarLibs` ist `null`.'],
}
ENUM_NOTES = {
    'Score': ['Neue Werte dürfen nur hinten angefügt werden (Kommentar im Code).',
              '`getScoreTexColor()` liefert die LaTeX-Farbe des Status, `htmlColor(text)` formatiert HTML-Text farbig (grün richtig, gelb teilweise, rot falsch, magenta Angabe-/Systemfehler).'],
    'SHOWPOTENZ': ['`parse(s)` liest den Wert ohne Beachtung der Groß-/Kleinschreibung, liefert `null` bei unbekanntem Namen.'],
}
GROUPS = [
    ('Request-DTOs', ['PluginRequestDto', 'LoadPluginRequestDto', 'PluginAngabeRequestDto', 'PluginParserRequestDto', 'PluginEinheitRequestDto',
                      'PluginScoreRequestDto', 'PluginRenderResultRequestDto', 'PluginRenderLatexRequestDto', 'PluginUpdateJavascriptRequestDto',
                      'PluginConfigurationInfoRequestDto', 'PluginSetConfigurationDataRequestDto', 'PluginConfigurationRequestDto']),
    ('Frage und Variablen', ['PluginQuestionDto', 'PluginSubQuestionDto', 'VarHashDto', 'VarDto', 'CalcErgebnisDto', 'CalcParamsDto', 'ToleranzDto', 'PluginMaximaCalcModeDto']),
    ('Plugin-Informationen', ['PluginGeneralInfo', 'PluginGeneralInfoList', 'JavascriptLibrary']),
    ('Darstellung und Bilder', ['PluginDto', 'PluginRenderDto', 'ImageBase64Dto', 'ImageUrlDto', 'ImageInfoDto', 'PluginImageResultDto']),
    ('Bewertung', ['PluginAnswerDto', 'PluginScoreInfoDto']),
    ('Datensätze', ['PluginDatasetDto', 'PluginDatasetListDto']),
    ('Konfiguration', ['PluginConfigurationInfoDto', 'PluginConfigDto']),
    ('Service und Registrierung', ['ConfigServiceDto', 'RegisterServiceResultDto', 'ServiceInfoDTO', 'AdminInfoDto']),
    ('Intern', ['PluginConfigurationConnection']),
]
grouped = {n for _, l in GROUPS for n in l}
missing = [n for n, t in TYPES.items() if t['kind'] == 'dto' and n not in grouped]
if missing: GROUPS.append(('Sonstige', missing))

def javadoc_url(fq): return f'`/{EP}/open/javadoc/{fq.replace(".", "/")}.html`'

def notes_md(lst): return '\n'.join('* ' + liquid(n) for n in lst)

# ---------------------------------------------------------------- Endpunkt-Seiten
for c in CONTROLLERS:
    for e in c['eps']:
        key = (e['ctrl'], e['meth']); D = 3
        L = [f'# {e["verb"]} {disp(e["paths"][0]).replace("<", "&lt;").replace(">", "&gt;")}', CMT, '']
        L += ['| | |', '|---|---|',
              f'| Controller | [{c["name"]}](../index.md) |',
              f'| Java-Methode | `{e["meth"]}` |',
              f'| HTTP-Methode | {e["verb"]} |',
              f'| Pfad | ' + '<br>'.join(f'`{disp(p)}`' for p in e['paths']) + ' |',
              f'| Erreichbarkeit | {reach(e)} |']
        if e['produces']: L.append(f'| Content-Type | `{e["produces"]}` |')
        if e['req']: L.append(f'| Request-Body | {type_md(e["req"][0], D)} |')
        for t, n in e['rparams']: L.append(f'| Query-Parameter | `{n}` ({t}) |')
        if not e['req'] and not e['rparams']: L.append('| Request | – |')
        L.append(f'| Response | {type_md(e["ret"], D)} |')
        L += ['', '## Beschreibung', '']
        if e['desc']:
            for para in re.split(r'<br>\s*', e['desc']):
                if para.strip(): L.append(html2md(para))
                L.append('')
        else: L += ['im Code nicht dokumentiert', '']
        # Request
        if e['req'] or e['rparams']:
            L += ['## Request', '']
            if e['req'] and refs(e['req'][0]):
                dto = refs(e['req'][0])[0]; t = TYPES[dto]
                used = set(e['used']) | set(e['jfields'])
                if e['deleg']:
                    tgt = ('ApiController', e['deleg'][0])
                    used = set(EPS[tgt]['used']) | set(EPS[tgt]['jfields'])
                L += [f'Body: [{dto}]({lt(dto, D)})', '', '| Feld | Typ | ausgewertet | Bedeutung |', '|---|---|---|---|']
                for fname, ftyp, _, fdoc in t['fields']:
                    d = e['jfields'].get(fname, (None, ''))[1] or fdoc
                    L.append(f'| `{fname}` | {type_md(ftyp, D)} | {"ja" if fname in used else "nein"} | {d} |')
                L.append('')
            elif e['req']:
                pd = e['pdocs'].get(e['req'][1], '')
                L += [f'Body: `{e["req"][0]}` – {html2md(pd) if pd else "im Code nicht dokumentiert"}', '']
            for t_, n in e['rparams']:
                L.append(f'* `{n}` ({t_}): {html2md(e["pdocs"].get(n, "")) or "im Code nicht dokumentiert"}')
            if e['rparams']: L.append('')
        # Response
        L += ['## Response', '', f'Typ: {type_md(e["ret"], D)}', '']
        if e['retdoc']: L += [html2md(e['retdoc']), '']
        if e['produces'] == 'text/html': L += ['Die Antwort ist eine HTML-Seite.', '']
        # Ablauf
        L += ['## Ablauf im Service', '']
        if e['deleg']:
            tgt = ('ApiController', e['deleg'][0])
            L.append(f'* Delegiert an [`{ep_label(tgt)}`]({le(tgt, D)}) (`ApiController.{e["deleg"][0]}`).')
        if e['calls']:
            L.append('* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: ' +
                     ', '.join(papi_link(m, D) for m in dict.fromkeys(e['calls'])) + '.')
        other = [m for m in dict.fromkeys(e['cfg']) if m not in ('createPluginService',)]
        if other: L.append('* Verwendet `PluginConfiguration`: ' + ', '.join(f'`{m}`' for m in other) + '.')
        if e['body'].count('return ResponseEntity.ok("pong")'): L.append('* Liefert fest den Text `pong`.')
        if 'PLUGIN_VERSION' in e['body'] and not e['calls']: L.append('* Liefert die Konstante `PluginConfiguration.PLUGIN_VERSION`.')
        for n in EP_NOTES.get(key, []): L.append('* ' + liquid(n))
        if L[-1] == '': L.append('* im Code nicht dokumentiert')
        L.append('')
        # Fehler
        errs = []
        if 'createPluginService(' in e['body'] or (e['deleg'] and 'createPluginService(' in EPS[('ApiController', e['deleg'][0])]['body']): errs.append(ERRORS['plugin'])
        if 'NOT_FOUND, "Plugin-Typ' in e['body'] or (e['deleg'] and e['deleg'][0] == 'pluginGeneralInfo'): errs.append('404 Not Found, wenn der Plugin-Typ nicht registriert ist.')
        if 'notFound()' in e['body'] or (e['deleg'] and e['deleg'][0] == 'reloadPluginDto'): errs.append('404 Not Found ohne Body, wenn zur `configurationID` keine gültige Sitzung existiert.')
        if 'HttpStatus.NOT_FOUND).body' in e['body']: errs.append('404 Not Found, wenn die Konfigurations-Sitzung fehlt oder abgelaufen ist.')
        if 'INTERNAL_SERVER_ERROR' in e['body']: errs.append('500 Internal Server Error, wenn das Plugin keine gültige Konfigurations-Methode angibt.')
        L += ['## Fehlerfälle', '']
        L += [f'* {x}' for x in dict.fromkeys(errs)] or ['* keine eigenen Fehlerfälle im Code']
        L.append('')
        # Beispiel
        if e['req'] and refs(e['req'][0]):
            dto = refs(e['req'][0])[0]
            ex = {}
            for fname, ftyp, _, _ in TYPES[dto]['fields']:
                if ftyp in ('String',): ex[fname] = f'<{fname}>'
                elif ftyp in ('int', 'long', 'double'): ex[fname] = 0
                elif ftyp == 'boolean': ex[fname] = False
                elif ftyp.endswith('[]'): ex[fname] = []
                else: ex[fname] = {'…': f'{ftyp}'}
            L += ['## Beispiel-Request', '', 'JSON-Gerüst aus den Feldern des DTOs, Werte sind Platzhalter:', '', '```json', json.dumps(ex, ensure_ascii=False, indent=2), '```', '']
        # Siehe auch
        sa = SEE_ALSO.get(key, [])
        if sa:
            L += ['## Siehe auch', '']
            for k in sa: L.append(f'* [`{ep_label(k)}`]({le(k, D)}) – {ep_short(k)}')
            L.append('')
        L.append(nav(D, [(c['name'], '../index.md'), ('REST-Schnittstelle', '../../index.md'), ('Referenz-Plugin (Java)', '../../../index.md')]))
        write(f'rest-schnittstelle/{c["name"]}/{e["meth"]}', '\n'.join(L).replace('<endpoint>', EP))

# ---------------------------------------------------------------- Controller-Seiten
REACH_C = {'ApiController': 'nur im Docker-Netzwerk (`http://letto-<endpoint>.nw-letto:8080/open/...`)',
           'ApiExternOpenController': 'extern über den Proxy', 'ConfigHttpController': 'extern über den Proxy',
           'HelpController': 'extern über den Proxy', 'InfoController': 'teils intern, teils extern (siehe Tabelle)'}
C_NOTES = {'ApiController': ['Für jede Anfrage wird mit `typ`, `name` und `config` eine neue Plugin-Instanz erzeugt; kann der Typ nicht erzeugt werden, antwortet der Endpunkt mit 404.',
                             'Die Endpunkte für den Konfigurationsdialog (`configurationinfo`, `setconfigurationdata`, `getconfiguration`, `reloadplugindto`) arbeiten mit einer Sitzung, die über die `configurationID` identifiziert wird.'],
           'ApiExternOpenController': ['Alle Endpunkte delegieren an den gleichnamigen Endpunkt des [ApiController](../ApiController/index.md).'],
           'InfoController': ['Der Controller hat keinen gemeinsamen Basispfad; `/ping`, `/info` und `/version` sind nur im Docker-Netzwerk erreichbar.']}
for c in CONTROLLERS:
    D = 2
    L = [f'# {c["name"]}', CMT, '']
    if c['doc']: L += [html2md(c['doc']), '']
    if c['tag'] and html2md(c['tag']) != html2md(c['doc']): L += [f'Swagger: {html2md(c["tag"])}', '']
    L += ['| | |', '|---|---|', f'| Klasse | `at.letto.plugins.controller.{c["name"]}` |',
          f'| Basispfad | {"`" + disp(c["base"]) + "`" if c["base"] else "–"} |', f'| Erreichbarkeit | {REACH_C.get(c["name"], "")} |',
          f'| JavaDoc | {javadoc_url("at.letto.plugins.controller." + c["name"])} |', '']
    L += ['## Endpunkte', '', '| Methode | Pfad | Request | Response | Beschreibung |', '|---|---|---|---|---|']
    for e in c['eps']:
        rq = type_md(e['req'][0], D) if e['req'] else (', '.join(f'`{n}`' for _, n in e['rparams']) or '–')
        L.append(f'| {e["verb"]} | [`{disp(e["paths"][0])}`]({e["meth"]}/index.md) | {rq} | {type_md(e["ret"], D)} | {short(e)} |')
    L.append('')
    if C_NOTES.get(c['name']): L += ['## Hinweise', '', notes_md(C_NOTES[c['name']]), '']
    L.append(nav(D, [('REST-Schnittstelle', '../index.md'), ('Referenz-Plugin (Java)', '../../index.md')]))
    write(f'rest-schnittstelle/{c["name"]}', '\n'.join(L))

# ---------------------------------------------------------------- Verwendungen
def usage_md(n, D):
    L = []
    rows = {}
    paths = {}
    for key, role, path in USAGE[n]:
        paths.setdefault((key, role), set()).add(path)
    for (key, role), ps in paths.items():
        best = min(ps, key=lambda p: (len(p), p))
        r = role if not best else f'{role} über ' + ' → '.join(f'`{p}`' for p in best)
        if len(ps) > 1: r += ' (und 1 weiterer Weg)' if len(ps) == 2 else f' (und {len(ps) - 1} weitere Wege)'
        rows.setdefault(key, []).append(r)
    L += ['## Verwendet in Endpunkten', '']
    if rows:
        L += ['| Endpunkt | Rolle | Beschreibung |', '|---|---|---|']
        order = sorted(rows, key=lambda k: (k == OUTGOING, [c['name'] for c in CONTROLLERS].index(k[0]) if k != OUTGOING else 0,
                                           [e['meth'] for e in next(c for c in CONTROLLERS if c['name'] == k[0])['eps']].index(k[1]) if k != OUTGOING else 0))
        for k in order:
            L.append(f'| {ep_link(k, D)} | {"<br>".join(rows[k])} | {ep_short(k)} |')
    else: L.append('wird in keinem Endpunkt verwendet')
    L.append('')
    L += ['## Verwendet in DTOs', '']
    if IN_DTO[n]:
        for d, f in IN_DTO[n]: L.append(f'* [{d}]({lt(d, D)}) – Feld `{f}`')
    else: L.append('in keinem DTO als Feldtyp verwendet')
    L.append('')
    pa = [(m, s) for m, s, r in PAPI if n in r]
    L += ['## Verwendet in der Plugin-API', '']
    if pa:
        for m, s in pa: L.append(f'* {papi_link(m, D)}: `{s}`')
    else: L.append('nicht direkt in `PluginService` verwendet')
    L.append('')
    return L

# ---------------------------------------------------------------- DTO-Seiten
for n, t in TYPES.items():
    if t['kind'] != 'dto': continue
    D = 2
    L = [f'# {n}', CMT, '', html2md(t['doc']) if t['doc'] else 'im Code nicht dokumentiert', '',
         '| | |', '|---|---|', f'| Klasse | `at.letto.plugins.dto.{n}` |', f'| JavaDoc | {javadoc_url("at.letto.plugins.dto." + n)} |', '']
    if t['consts']:
        L += ['## Konstanten', '', '| Konstante | Typ | Wert | Bedeutung |', '|---|---|---|---|']
        for fname, ftyp, dv, d in t['consts']:
            L.append(f'| `{fname}` | {type_md(ftyp, D)} | `{dv}` | {d} |')
        L.append('')
    L += ['## Felder', '']
    if t['fields']:
        L += ['| Feld | Typ | Standard | Bedeutung |', '|---|---|---|---|']
        for fname, ftyp, dv, d in t['fields']:
            dv = dv if dv and len(dv) < 60 else ('' if not dv else 'siehe Code')
            L.append(f'| `{fname}` | {type_md(ftyp, D)} | {"`" + dv + "`" if dv and dv != "siehe Code" else dv} | {d or "im Code nicht dokumentiert"} |')
    else: L.append('keine Felder')
    L.append('')
    if DTO_NOTES.get(n): L += ['## Hinweise', '', notes_md(DTO_NOTES[n]), '']
    L += usage_md(n, D)
    L.append(nav(D, [('DTOs', '../index.md'), ('Referenz-Plugin (Java)', '../../index.md')]))
    write(f'dtos/{n}', '\n'.join(L))

# ---------------------------------------------------------------- Enum-Seiten
for n, t in TYPES.items():
    if t['kind'] != 'enum': continue
    D = 2
    L = [f'# {n}', CMT, '', html2md(t['doc']) if t['doc'] else 'im Code nicht dokumentiert', '',
         '| | |', '|---|---|', f'| Enum | `at.letto.plugins.enums.{n}` |', f'| JavaDoc | {javadoc_url("at.letto.plugins.enums." + n)} |', '',
         '## Werte', '', '| Wert | Bedeutung |', '|---|---|']
    for v, d in t['values']: L.append(f'| `{v}` | {d or "im Code nicht dokumentiert"} |')
    L.append('')
    if ENUM_NOTES.get(n): L += ['## Hinweise', '', notes_md(ENUM_NOTES[n]), '']
    L += usage_md(n, D)
    L.append(nav(D, [('Enums', '../index.md'), ('Referenz-Plugin (Java)', '../../index.md')]))
    write(f'enums/{n}', '\n'.join(L))

# ---------------------------------------------------------------- Übersichten
L = ['# DTOs des Referenz-Plugins', CMT, '',
     '* Paket `at.letto.plugins.dto`; die DTOs werden als JSON übertragen, Feldnamen im JSON entsprechen den Java-Feldnamen.',
     '* Getter/Setter und Konstruktoren erzeugt Lombok.',
     '* Jede Seite listet die Felder und alle Endpunkte, in denen das DTO direkt oder verschachtelt vorkommt.',
     '* Die Enums sind unter [Enums](../enums/index.md) beschrieben.', '']
for g, names in GROUPS:
    L += [f'## {g}', '', '| DTO | Beschreibung | Endpunkte |', '|---|---|---|']
    for n in names:
        if n not in TYPES: continue
        cnt = len({k for k, _, _ in USAGE[n]})
        L.append(f'| [{n}]({n}/index.md) | {first_sentence(TYPES[n]["doc"]) if TYPES[n]["doc"] else "im Code nicht dokumentiert"} | {cnt} |')
    L.append('')
L.append(nav(1, [('Referenz-Plugin (Java)', '../index.md')]))
write('dtos', '\n'.join(L))

L = ['# Enums des Referenz-Plugins', CMT, '', '* Paket `at.letto.plugins.enums`; Enums werden in JSON als Name des Werts übertragen.', '',
     '| Enum | Beschreibung | Werte |', '|---|---|---|']
for n, t in TYPES.items():
    if t['kind'] == 'enum':
        L.append(f'| [{n}]({n}/index.md) | {first_sentence(t["doc"])} | {", ".join("`" + v + "`" for v, _ in t["values"])} |')
L.append(nav(1, [('Referenz-Plugin (Java)', '../index.md')]))
write('enums', '\n'.join(L))

L = ['# REST-Schnittstelle des Referenz-Plugins', CMT, '',
     '* Alle Pfade sind in `at.letto.plugins.config.Endpoint` definiert. `<endpoint>` steht für den Endpoint-Pfad des Plugins (im Demo `' + SERVICEPATH[1:] + '`).',
     '* Request- und Response-Bodies sind JSON. Die Datenklassen sind unter [DTOs](../dtos/index.md) und [Enums](../enums/index.md) beschrieben.',
     '* Die Swagger-UI des laufenden Services liegt unter `/<endpoint>/swagger-ui.html`; die Beschreibungen dort stammen aus der JavaDoc.',
     '* Jeder Endpunkt hat eine eigene Seite mit Request-Feldern, Ablauf, Fehlerfällen und Querverweisen.', '',
     '## Controller', '', '| Controller | Basispfad | Erreichbarkeit | Endpunkte | Zweck |', '|---|---|---|---|---|']
for c in CONTROLLERS:
    L.append(f'| [{c["name"]}]({c["name"]}/index.md) | {"`" + disp(c["base"]) + "`" if c["base"] else "–"} | {REACH_C.get(c["name"], "")} | {len(c["eps"])} | {first_sentence(c["doc"])} |')
L += ['', '## Alle Endpunkte', '', '| Methode | Pfad | Controller | Request | Response | Beschreibung |', '|---|---|---|---|---|---|']
for c in CONTROLLERS:
    for e in c['eps']:
        rq = type_md(e['req'][0], 1) if e['req'] else (', '.join(f'`{n}`' for _, n in e['rparams']) or '–')
        L.append(f'| {e["verb"]} | [`{disp(e["paths"][0])}`]({c["name"]}/{e["meth"]}/index.md) | [{c["name"]}]({c["name"]}/index.md) | {rq} | {type_md(e["ret"], 1)} | {short(e)} |')
L += ['', '## Konfigurationssitzung', '',
      '* [configurationinfo](ApiController/configurationInfo/index.md) muss vor [setconfigurationdata](ApiController/setConfigurationData/index.md), '
      '[getconfiguration](ApiController/getConfiguration/index.md), [reloadplugindto](ApiController/reloadPluginDto/index.md) und '
      '[confighttp](ConfigHttpController/configHttp/index.md) aufgerufen werden.',
      '* Die `configurationID` muss für jeden Konfigurationsdialog eindeutig sein und dient an den offenen Endpunkten als Authentifizierung.',
      '* Die Sitzung wird nach `timeout` Sekunden ohne Zugriff entfernt.', '',
      '## Registrierung am Setup-Service (ausgehend)', '',
      '| Methode | Pfad am Setup-Service | Request | Response | Authentifizierung |', '|---|---|---|---|---|',
      f'| POST | `/config/auth/user/registerplugin` | {type_md("ConfigServiceDto", 1)} | {type_md("RegisterServiceResultDto", 1)} | Basic Auth (`letto.user.user.name` / `letto.user.user.password`) |',
      '', 'Siehe [Build und Deployment](../build-deployment/index.md#registrierung-am-letto-server).', '',
      '## Hinweise', '',
      '* `EXTERN_API` (`/<endpoint>/auth/user`) wird bei der Registrierung als externe URI (`uriExtern`) an das Setup-Service gemeldet; '
      'ein Controller für eine authentifizierte externe API ist im Demo nicht implementiert.',
      nav(1, [('Referenz-Plugin (Java)', '../index.md')])]
write('rest-schnittstelle', '\n'.join(L))

# ---------------------------------------------------------------- Manifest für Linkify/Prüfung
manifest = {'types': {n: t['kind'] for n, t in TYPES.items()},
            'controllers': [c['name'] for c in CONTROLLERS],
            'endpoints': {f'{e["ctrl"]}/{e["meth"]}': [disp(p) for p in e['paths']] for e in EPS.values()},
            'papi': [m for m, _, _ in PAPI]}
json.dump(manifest, open(sys.argv[5], 'w'), indent=1)
print('controller', len(CONTROLLERS), 'endpoints', len(EPS), 'dtos', sum(t['kind'] == 'dto' for t in TYPES.values()),
      'enums', sum(t['kind'] == 'enum' for t in TYPES.values()))
