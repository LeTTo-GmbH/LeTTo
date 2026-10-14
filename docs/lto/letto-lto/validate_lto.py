#!/usr/bin/env python3
"""
Prüft LeTTo-Austauschdateien (.lto, Format letto mode="101") auf Fehler, die einen Import
verhindern oder verfälschen würden. Benötigt nur die Python-Standardbibliothek.

Aufruf:   python validate_lto.py datei1.lto [datei2.lto ...]
Ergebnis: Exit-Code 0 = keine Fehler (Warnungen möglich), 1 = Fehler gefunden.

Geprüft wird u.a.:
  * Wurzel <letto mode="101"> mit genau einem Kind (category | question | subquestion)
  * erlaubte Elemente und deren Reihenfolge (wie lto-v1.xsd)
  * CDATA-Pflicht: diese Felder liest der LeTTo-Import nur aus <![CDATA[...]]>
  * Zahlen-, Boolean- und Enum-Werte
  * Platzhalter [Q0] im Fragetext <-> Teilfragen
  * Bewertung (fraction) je Teilfragen-Modus, Datensätze (Anzahl der Werte, Namen)
Das XML-Schema lto-v1.xsd liegt im selben Ordner und kann zusätzlich mit jedem
XSD-Validator (z.B. xmllint --schema lto-v1.xsd datei.lto) verwendet werden.
"""
import json
import re
import sys
from xml.dom import minidom
from xml.parsers.expat import ExpatError

# ---------------------------------------------------------------------------------------------
# Struktur: erlaubte Kindelemente in Reihenfolge. Typ-Kürzel:
#   C = Text, CDATA Pflicht   S = Text (CDATA optional)   I = Ganzzahl   D = Kommazahl
#   B = Boolean               E:<enum> = Enum             * = Element darf mehrfach vorkommen
#   ! = Pflichtelement        X = veraltet (Warnung)       sonst Name eines komplexen Typs
# ---------------------------------------------------------------------------------------------
QUESTION = [
    ("id", "I"), ("idUser", "I"), ("questionType", "E:questionType!"), ("single", "E:single"),
    ("name", "C!"), ("punkte", "D"), ("penalty", "S"), ("hidden", "I"), ("tag", "C"),
    ("noAutoCorrect", "I"), ("usecase", "I"), ("synchronize", "I"), ("shuffleAnswers", "E:shuffle"),
    ("answerNumbering", "C"), ("unitGradingType", "I"), ("unitPenalty", "D"), ("showUnits", "I"),
    ("unitsLeft", "I"), ("maxima", "C"), ("maximaAngabe", "C"), ("responseFormat", "C"),
    ("responseFieldLines", "I"), ("attachments", "I"), ("md5", "C"), ("revNrServer", "X"),
    ("revNrLocal", "X"), ("units", "C"), ("plugins", "C"), ("sendToParser", "B"), ("preCalc", "B"),
    ("streng", "B"), ("licenceKey", "C"), ("konstanteMitProzent", "B"), ("useSymbolicMode", "B"),
    ("addDocumentsPossible", "B"), ("info", "C"), ("randomDataset", "B"), ("creationDate", "DATE"),
    ("lastChange", "DATE"), ("security", "C"), ("copyright", "C"), ("onRamp", "B"),
    ("jsonMap", "JSON"), ("changeLogMap", "JSON"), ("questionCommentMsg", "C"),
    ("questionCommentIcon", "E:icon"), ("text", "TEXT*!"), ("subquestion", "SUBQUESTION*"),
    ("dataset", "DATASET*"),
]
SUBQUESTION = [
    ("id", "I"), ("grade", "D"), ("mode", "E:mode"), ("name", "C!"), ("maxima", "C"),
    ("plugininfo", "C"), ("plugininputimage", "X"), ("einheit", "X"), ("shuffleAnswers", "E:shuffle"),
    ("schwierigkeit", "E:schwierigkeit"), ("answer", "ANSWER*"),
]
ANSWER = [
    ("id", "I"), ("fraction", "D"), ("format", "C"), ("text", "C"), ("feedback", "C"),
    ("tolerance", "C"), ("correctAnswerFormat", "I"), ("correctAnswerLength", "I"), ("maxima", "C"),
    ("answer", "C"), ("einheit", "C"),
]
DATASET = [
    ("id", "I"), ("status", "C"), ("name", "C!"), ("type", "C"), ("distribution", "C"),
    ("minimum", "C"), ("maximum", "C"), ("decimals", "C"), ("itemcount", "I"),
    ("zahlenbereich", "C"), ("ziffern", "I"), ("einheit", "C"), ("items", "C"),
]
CATEGORY = [("name", "S!"), ("question", "QUESTION*"), ("category", "CATEGORY*")]
TEXT = [("inhalt", "C!"), ("file", "FILE*")]

ENUMS = {
    "questionType": (range(10, 24), ["MoodleNumerical", "MoodleCalculated", "MoodleMultichoice",
                     "MoodleShortAnswer", "MoodleDescription", "MoodleEssay", "MoodleMatching",
                     "MoodleCloze", "MoodleTrueFalse", "MoodleRandomsMatch", "MoodleClozeCalc",
                     "LinkedQuestion"]),
    "single": (range(0, 6), ["MultipleChoice", "SingleChoice", "Texteingabe", "DragAndDrop",
               "RegularExpression", "CaseSensitive"]),
    "shuffle": (range(0, 7), ["Nicht_mischen", "Mischen", "Nur_links_mischen", "Nur_rechts_mischen",
                "Normal", "Streng", "Mild"]),
    "schwierigkeit": (range(0, 4), ["Normal", "Streng", "Mild", "HundertProz"]),
    "mode": (range(0, 11), ["SINGLECHOICE", "TEXT", "REGEXP", "MULTICHOICE", "CALCULATED", "BOOLSCH",
             "PLUGIN", "FREITEXT", "ZUORDNUNG", "IMAGE", "SCHIEBER"]),
    "icon": ([], ["WARNING", "REVIEWED", "PROCESSING", "BLOCKED"]),
}
MODE_NAMES = ENUMS["mode"][1]


class Report:
    def __init__(self, filename):
        self.filename = filename
        self.errors, self.warnings = [], []

    def error(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")


def elements(node):
    return [c for c in node.childNodes if c.nodeType == c.ELEMENT_NODE]


def content(node):
    """Liefert (text, hat_cdata, hat_text_ausserhalb_cdata)."""
    cdata = "".join(c.data for c in node.childNodes if c.nodeType == c.CDATA_SECTION_NODE)
    text = "".join(c.data for c in node.childNodes if c.nodeType == c.TEXT_NODE)
    if cdata:
        return cdata, True, bool(text.strip())
    return text, False, bool(text.strip())


def check_simple(rep, where, el, kind):
    value, has_cdata, has_text = content(el)
    if elements(el):
        rep.error(where, "darf keine Kindelemente enthalten")
        return value
    if kind == "C":
        if has_text and not has_cdata:
            rep.error(where, "Inhalt muss in <![CDATA[...]]> stehen – der Import liest sonst einen leeren Wert")
        elif has_text:
            rep.error(where, "Text außerhalb des CDATA-Abschnitts wird ignoriert")
        return value
    v = value.strip()
    if kind == "S" or kind == "X":
        return value
    if kind == "I":
        if not re.fullmatch(r"-?\d+", v):
            rep.error(where, f"Ganzzahl erwartet, gefunden '{v}'")
    elif kind == "D":
        if not re.fullmatch(r"-?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?", v):
            rep.error(where, f"Zahl erwartet, gefunden '{v}'")
    elif kind == "B":
        if v not in ("true", "false", "1", "0"):
            rep.error(where, f"true/false erwartet, gefunden '{v}'")
    elif kind == "DATE":
        if v and not re.fullmatch(r"\d{2}/\d{2}/\d{4}", v):
            rep.error(where, f"Datum dd/MM/yyyy oder leer erwartet, gefunden '{v}'")
    elif kind == "JSON":
        if has_text and not has_cdata:
            rep.error(where, "Inhalt muss in <![CDATA[...]]> stehen")
        try:
            if not isinstance(json.loads(value or "{}"), dict):
                raise ValueError
        except ValueError:
            rep.error(where, "JSON-Objekt erwartet (z.B. {})")
    elif kind.startswith("E:"):
        numbers, names = ENUMS[kind[2:]]
        if not ((v.isdigit() and int(v) in numbers) or v in names):
            allowed = (f"{numbers.start}..{numbers.stop - 1} oder " if numbers else "") + ", ".join(names)
            rep.error(where, f"ungültiger Wert '{v}', erlaubt: {allowed}")
    return value


def check_sequence(rep, where, node, spec):
    """Prüft erlaubte Elemente, Reihenfolge, Pflichtelemente und Einzel-Werte. Liefert dict name->[elemente]."""
    order = {name: i for i, (name, _) in enumerate(spec)}
    kinds = dict(spec)
    found, last = {}, -1
    for el in elements(node):
        name = el.tagName
        if name not in order:
            rep.error(where, f"unbekanntes Element <{name}>")
            continue
        kind = kinds[name]
        if order[name] < last:
            rep.error(where, f"<{name}> steht an falscher Position (Reihenfolge siehe lto-v1.xsd)")
        if name in found and "*" not in kind:
            rep.error(where, f"<{name}> darf nur einmal vorkommen")
        last = max(last, order[name])
        found.setdefault(name, []).append(el)
        if kind == "X":
            rep.warn(where, f"<{name}> ist veraltet und wird ignoriert")
    for name, kind in spec:
        base = kind.rstrip("*!")
        if kind.endswith("!") and name not in found:
            rep.error(where, f"Pflichtelement <{name}> fehlt")
        if name in found and (base in ("C", "S", "I", "D", "B", "X", "DATE", "JSON") or base.startswith("E:")):
            check_simple(rep, f"{where}/{name}", found[name][0], base)
    return found


def text_of(found, name):
    return content(found[name][0])[0] if name in found else ""


def check_answer(rep, where, node, mode):
    found = check_sequence(rep, where, node, ANSWER)
    try:
        fraction = float(text_of(found, "fraction") or "0")
    except ValueError:
        fraction = 0.0
    if not -100 <= fraction <= 100:
        rep.error(where + "/fraction", "muss zwischen -100 und 100 liegen")
    if mode == "CALCULATED" and not text_of(found, "maxima").strip():
        rep.warn(where, "Berechnungs-Teilfrage ohne <maxima> (Variable bzw. Formel des Ergebnisses)")
    if mode in ("SINGLECHOICE", "MULTICHOICE") and not text_of(found, "text").strip():
        rep.warn(where + "/text", "Auswahl-Antwort ohne Antworttext")
    return fraction


def check_subquestion(rep, where, node):
    found = check_sequence(rep, where, node, SUBQUESTION)
    raw = text_of(found, "mode").strip() or "4"
    mode = MODE_NAMES[int(raw)] if raw.isdigit() and int(raw) < len(MODE_NAMES) else raw.upper()
    name = text_of(found, "name").strip()
    where = f"{where}[{name}]"
    answers = found.get("answer", [])
    fractions = [check_answer(rep, f"{where}/answer[{i + 1}]", a, mode) for i, a in enumerate(answers)]
    if not answers and mode not in ("FREITEXT", "IMAGE", "ZUORDNUNG"):
        rep.warn(where, f"Teilfrage im Modus {mode} ohne Antwort")
    if mode == "SINGLECHOICE" and fractions and max(fractions) < 100:
        rep.warn(where, "Single-Choice ohne Antwort mit fraction 100")
    if mode == "MULTICHOICE" and fractions:
        positive = sum(f for f in fractions if f > 0)
        if abs(positive - 100) > 1:
            rep.warn(where, f"Multiple-Choice: Summe der positiven fractions ist {positive:g}, erwartet 100")
    grade = text_of(found, "grade").strip() or "1"
    if mode in ("CALCULATED", "TEXT", "REGEXP") and fractions and max(fractions) < 100 and float(grade) != 0:
        rep.warn(where, "keine Antwort mit fraction 100 – volle Punkte sind nicht erreichbar")
    return name, mode


def check_dataset(rep, where, node):
    found = check_sequence(rep, where, node, DATASET)
    name = text_of(found, "name").strip()
    where = f"{where}[{name}]"
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name):
        rep.error(where + "/name", "Datensatzname muss mit einem Buchstaben beginnen (Buchstaben, Ziffern, _)")
    items = [x for x in text_of(found, "items").split(";") if x.strip()]
    if items:
        for x in items:
            if not re.fullmatch(r"\s*-?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?\s*", x):
                rep.warn(where + "/items", f"Wert '{x.strip()}' ist keine Zahl in SI-Basiseinheit")
                break
    else:
        rep.warn(where, "keine Werte in <items> – die Werte (40 Stück, SI-Einheit) sollten mitgeliefert werden")
    return name


def check_text(rep, where, node, index):
    found = check_sequence(rep, where, node, TEXT)
    for i, f in enumerate(found.get("file", [])):
        fw = f"{where}/file[{i + 1}]"
        if not f.getAttribute("filename"):
            rep.error(fw, "Attribut filename fehlt")
        kids = elements(f)
        if not kids:
            rep.warn(fw, "Datei ohne Inhalt wird beim Import verworfen")
        for k in kids:
            if k.tagName not in ("base64", "webPath", "inhalt"):
                rep.error(fw, f"unbekanntes Element <{k.tagName}>")
            else:
                check_simple(rep, f"{fw}/{k.tagName}", k, "C")
    return text_of(found, "inhalt")


def check_question(rep, where, node, names_in_category):
    found = check_sequence(rep, where, node, QUESTION)
    qname = text_of(found, "name").strip()
    where = f"{where}[{qname}]"
    removed = set(re.sub(r"[a-zA-ZöäüÖÄÜß0-9_\-;:#^$+*\s.]", "", qname))
    if removed:
        rep.warn(where, f"Zeichen {''.join(sorted(removed))} werden beim Import aus dem Fragenamen entfernt")
    if qname in names_in_category:
        rep.warn(where, "Fragename kommt im Ordner doppelt vor – der Import benennt in '-1' um")
    names_in_category.add(qname)
    texts = [check_text(rep, f"{where}/text[{i + 1}]", t, i) for i, t in enumerate(found.get("text", []))]
    if found.get("text") and found["text"][0].getAttribute("art") not in ("", "Questiontext"):
        rep.warn(where, "der erste <text> ist immer der Fragetext (art wird beim Import ignoriert)")
    subquestions = [check_subquestion(rep, f"{where}/subquestion", s) for s in found.get("subquestion", [])]
    sq_names = [n for n, _ in subquestions]
    ds_names = [check_dataset(rep, f"{where}/dataset", d) for d in found.get("dataset", [])]
    for dup in {n for n in sq_names if sq_names.count(n) > 1}:
        rep.error(where, f"Teilfragenname '{dup}' ist doppelt")
    for dup in {n for n in ds_names if ds_names.count(n) > 1}:
        rep.error(where, f"Datensatzname '{dup}' ist doppelt")
    questiontext = texts[0] if texts else ""
    qtype = text_of(found, "questionType").strip()
    if qtype in ("22", "MoodleClozeCalc"):
        # Bei der Mehrfachberechnungsfrage wird jede Lücke über [Name] im Fragetext platziert
        for n, mode in subquestions:
            if n and mode != "BOOLSCH" and f"[{n}]" not in questiontext:
                rep.warn(where, f"Teilfrage '{n}' wird im Fragetext nicht mit [{n}] platziert")
        for tag in re.findall(r"\[(Q\d+)\]", questiontext):
            if tag not in sq_names:
                rep.error(where, f"Platzhalter [{tag}] im Fragetext hat keine Teilfrage")
    return qname


def check_category(rep, where, node):
    found = check_sequence(rep, where, node, CATEGORY)
    where = f"{where}[{text_of(found, 'name').strip()}]"
    names = set()
    for q in found.get("question", []):
        check_question(rep, f"{where}/question", q, names)
    sub = [text_of(check_sequence(Report(''), '', c, CATEGORY), "name").strip() for c in found.get("category", [])]
    for dup in {n for n in sub if sub.count(n) > 1}:
        rep.warn(where, f"Unterordner '{dup}' doppelt – wird beim Import zusammengeführt")
    for c in found.get("category", []):
        check_category(rep, f"{where}/category", c)


def check_file(filename):
    rep = Report(filename)
    try:
        doc = minidom.parse(filename)
    except (ExpatError, OSError) as ex:
        rep.error("XML", f"nicht lesbar bzw. nicht wohlgeformt: {ex}")
        return rep
    root = doc.documentElement
    if root.tagName != "letto":
        rep.error("letto", f"Wurzelelement muss <letto> sein, gefunden <{root.tagName}>")
        return rep
    if root.getAttribute("mode") != "101":
        rep.error("letto", 'Attribut mode="101" fehlt oder ist falsch')
    kids = elements(root)
    if len(kids) != 1:
        rep.error("letto", f"genau ein Kindelement erwartet, gefunden {len(kids)} (der Import liest nur das erste)")
    for k in kids[:1]:
        if k.tagName == "category":
            check_category(rep, "category", k)
        elif k.tagName == "question":
            check_question(rep, "question", k, set())
        elif k.tagName == "subquestion":
            check_subquestion(rep, "subquestion", k)
        else:
            rep.error("letto", f"unerwartetes Kindelement <{k.tagName}>")
    return rep


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(argv) < 2:
        print(__doc__)
        return 2
    failed = False
    for filename in argv[1:]:
        rep = check_file(filename)
        status = "FEHLER" if rep.errors else "OK"
        print(f"{status}: {filename}  ({len(rep.errors)} Fehler, {len(rep.warnings)} Warnungen)")
        for e in rep.errors:
            print(f"  FEHLER   {e}")
        for w in rep.warnings:
            print(f"  WARNUNG  {w}")
        failed |= bool(rep.errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
