# LTO-Dateiformat

Das `.lto`-Format ist das XML-Austauschformat von LeTTo für Fragen und Fragesammlungen. Es lehnt sich an
Moodle-XML an, enthält aber alle LeTTo-spezifischen Daten (Teilfragen, Datensätze, Maxima-Berechnungen,
Einheiten, Plugins, eingebettete Bilder). Exportiert und importiert werden `.lto`-Dateien vom
[Export-Service](../wiki/Export-Service/index.md).

* **Export:** Fragesammlung → Rechtsklick auf einen Ordner → „Kategorie exportieren“
  (alle Fragen und Unterordner, siehe [Ordnerverwaltung](../wiki/Ordnerverwaltung/index.md))
* **Import:** Rechtsklick auf den Zielordner → „Daten importieren“ → `.lto`-Datei wählen

Diese Seite beschreibt das Format Version 1 (`<letto mode="101">`) vollständig. Sie richtet sich an alle,
die `.lto`-Dateien mit eigenen Programmen oder mit KI-Unterstützung erzeugen oder auswerten wollen.

## Downloads

| Datei | Inhalt |
|---|---|
| [lto-v1.xsd](letto-lto/lto-v1.xsd) | XML-Schema (maschinenlesbare Grammatik) mit Kommentaren zu jedem Element |
| [validate_lto.py](letto-lto/validate_lto.py) | Prüfskript (Python 3, ohne Zusatzpakete) – prüft auch Regeln, die ein Schema nicht ausdrücken kann |
| [beispiele/](#beispiele) | Gültige Beispieldateien zum Importieren und als Vorlage |
| [letto-lto-skill.zip](/assets/download/letto-lto-skill.zip) | KI-Skill zum Erzeugen von Fragen (Claude, Claude Code, Codex, ChatGPT) – siehe [KI-Unterstützung](#ki-unterstützung) |
| [SKILL.md (GitHub)](https://github.com/LeTTo-GmbH/LeTTo/blob/master/docs/lto/letto-lto/SKILL.md) | KI-Kurzbeschreibung des Formats als einzelne Datei |

Prüfen einer Datei:

```bash
python validate_lto.py meine-fragen.lto
xmllint --noout --schema lto-v1.xsd meine-fragen.lto
```

## Aufbau

```
<?xml version="1.0" encoding="UTF-8"?>
<letto mode="101" databaseinfo="sql">       Wurzel, genau EIN Kindelement:
   <category>                                 Ordner mit Fragen und Unterordnern   oder
   <question type="MoodleClozeCalc">          eine einzelne Frage                  oder
   <subquestion>                              eine einzelne Teilfrage
</letto>

category
├─ name
├─ question*
│  ├─ Einzelfelder (id … changeLogMap, questionCommentMsg, questionCommentIcon)
│  ├─ text*            Fragetext und Feedbacks, je mit inhalt und file*
│  ├─ subquestion*     Teilfragen (Lücken) mit answer*
│  └─ dataset*         Datensätze (Zufallsvariablen)
└─ category*           Unterordner
```

Allgemeine Regeln:

* **Kodierung** UTF-8. Zeichen 0x01–0x08, 0x0B, 0x0C, 0x0E–0x1F werden beim Import entfernt.
* **Reihenfolge:** LeTTo schreibt alle Elemente in einer festen Reihenfolge (siehe Tabellen und Schema).
  Der Import liest die Einzelfelder einer Frage, Teilfrage, Antwort und eines Datensatzes unabhängig von der
  Reihenfolge, Erzeuger sollten sich aber an das Schema halten.
* **CDATA-Pflicht:** Alle Felder vom Typ *Text (CDATA)* liest der Import ausschließlich aus einem
  `<![CDATA[...]]>`-Abschnitt. `<name>Test</name>` ergibt einen leeren Namen. Leere Felder werden als
  `<feld/>` geschrieben. Ausnahme ist `category/name`, das auch ohne CDATA gelesen wird.
* **Zahlen, Booleans und Enum-Werte** stehen ohne CDATA im Element. Booleans: `true`/`false`
  (der Import akzeptiert auch `1`/`0`). Enum-Werte schreibt LeTTo als Zahl, der Import akzeptiert auch den Namen.
* **IDs** (`id`, `idUser`, Attribut `id`) stammen aus der Quelldatenbank und werden beim Import neu vergeben.
  Für neu erzeugte Dateien `0` verwenden.

## Wurzelelement `letto`

| Attribut | Wert | Bedeutung |
|---|---|---|
| mode | `101` | Formatversion (LETTO_XML_V1). Pflicht. |
| databaseinfo | `sql` | Herkunft, wird nicht ausgewertet |

Der Import liest nur das **erste** Kindelement. Neben `category`, `question` und `subquestion` wird beim
Import auch `test` akzeptiert und wie `category` behandelt; LeTTo exportiert dieses Element nicht.

## Kategorie `category`

| Element | Typ | Bedeutung |
|---|---|---|
| name | Text | Ordnername |
| question | Frage, mehrfach | Fragen des Ordners |
| category | Kategorie, mehrfach | Unterordner |

Beim Einlesen der Datei werden gleichnamige Unterordner desselben Ordners zusammengeführt, identische Fragen
nur einmal übernommen und gleichnamige Fragen eindeutig gemacht, indem `-1` angehängt bzw. die Endnummer
erhöht wird (`Name-1`, `Name-2`, …). Das betrifft nur den Inhalt der Datei; welche Fragen und Ordner
tatsächlich in den Zielordner übernommen werden, wird im Import-Dialog festgelegt.

## Frage `question`

Das Attribut `type` enthält den Fragetyp als Namen (z.B. `MoodleClozeCalc`) und dient nur der Lesbarkeit;
maßgeblich ist das Element `questionType`. Die Einzelfelder in Exportreihenfolge:

| Element | Typ | Standard | Bedeutung |
|---|---|---|---|
| id | Ganzzahl | 0 | ID in der Quelldatenbank |
| idUser | Ganzzahl | 0 | Ersteller in der Quelldatenbank |
| questionType | Enum [Fragetyp](#fragetyp-questiontype) | | Fragetyp, fast immer `22` |
| single | Enum [Lückentextmodus](#lückentextmodus-single) | 2 | Modus der Lückentextfrage, optional |
| name | Text (CDATA) | | Fragename, eindeutig im Ordner. Beim Import werden alle Zeichen außer Buchstaben (inkl. äöüß), Ziffern, Leerzeichen und `_ - ; : # ^ $ + * .` entfernt |
| punkte | Zahl | 1.0 | Maximale Punkte (bei Mehrfachberechnungsfragen Summe der Teilfragen) |
| penalty | Text | leer | Abzug je Fehlversuch im Rechen-/Hausübungsmodus, z.B. `0.3333333` – siehe [Bekannte Abweichungen](#bekannte-abweichungen-im-code) |
| hidden | Ganzzahl | 0 | 1 = versteckt |
| tag | Text (CDATA) | leer | Schlagworte |
| noAutoCorrect | Ganzzahl | 0 | 1 = Autokorrektur aus, 0 = globale Einstellung |
| usecase | Ganzzahl | 0 | 1 = Groß-/Kleinschreibung beachten |
| synchronize | Ganzzahl | 0 | 1 = mehrere Datensätze synchronisieren |
| shuffleAnswers | Enum [Antworten mischen](#antworten-mischen-shuffleanswers) | 1 | |
| answerNumbering | Text (CDATA) | `abc` | Nummerierung der Antworten |
| unitGradingType | Ganzzahl | 2 | 0 = nur Zahlenwert, 1 = Einheit wird umgerechnet aber nicht bewertet, 2 = Einheit wird bewertet |
| unitPenalty | Zahl | 0.1 | Abzug bei falscher Einheit (0..1), siehe [Einheit](../wiki/Einheit/index.md) |
| showUnits | Ganzzahl | 0 | 0 = Texteingabe, 1 = Mehrfachauswahl, 2 = Dropdown, 3 = Anzeige am Webserver |
| unitsLeft | Ganzzahl | 0 | 1 = Einheit links vom Wert |
| maxima | Text (CDATA) | leer | Maxima-Feld der Frage, siehe [Maxima-Feld](../wiki/BeispielsammlungEditieren/index.md#maxima-feld) |
| maximaAngabe | Text (CDATA) | | Automatisch erzeugtes Angabefeld. Wird nur exportiert, wenn kürzer als 10000 Zeichen und ohne Vorberechnung |
| responseFormat | Text (CDATA) | `editor` | Antwortformat für Freitext |
| responseFieldLines | Ganzzahl | 10 | Zeilen des Antwortfelds |
| attachments | Ganzzahl | 3 | Anzahl möglicher Anhänge |
| md5 | Text (CDATA) | leer | Prüfsumme, von LeTTo verwaltet |
| revNrServer, revNrLocal | Ganzzahl | | veraltet (SVN), werden ignoriert |
| units | Text (CDATA) | leer | Einheiten für Moodle |
| plugins | Text (CDATA) | leer | Plugin-Definitionen, z.B. `[PI Plugin1 Plot "..."]`, siehe [Plugins](../wiki/Plugins/index.md) |
| sendToParser | Boolean | false | true = Berechnung mit dem LeTTo-Parser statt Maxima |
| preCalc | Boolean | false | Vorberechnung mit eingesetzten Zahlenwerten |
| streng | Boolean | false | Frage nur ganz richtig oder ganz falsch |
| licenceKey | Text (CDATA) | leer | Lizenzschlüssel verschlüsselter Fragen |
| konstanteMitProzent | Boolean | true | Konstanten werden mit `%` geschrieben (`%pi`, `%e`, …) |
| useSymbolicMode | Boolean | false | Symbolischer Rechenmodus |
| addDocumentsPossible | Boolean | false | Schüler können Dokumente hochladen |
| info | Text (CDATA) | leer | Beschreibung der Funktionsweise der Frage |
| randomDataset | Boolean | false | Datensätze bei jedem Aufruf neu zufällig erzeugen |
| creationDate | Datum | leer | Erstellungsdatum `dd/MM/yyyy` |
| lastChange | Datum | leer | Datum der letzten Änderung `dd/MM/yyyy` |
| security | Text (CDATA) | leer | Geschützter Gültigkeits-/Lizenzstring |
| copyright | Text (CDATA) | leer | Copyright-Information |
| onRamp | Boolean | false | Nächste Teilfrage erst nach korrekter Abgabe der vorigen einblenden |
| jsonMap | Text (CDATA) | `{}` | JSON-Objekt mit Zusatzdaten (z.B. Kennlinien) |
| changeLogMap | Text (CDATA) | `{}` | JSON-Objekt mit Änderungsprotokoll |
| questionCommentMsg | Text (CDATA) | | Bearbeitungskommentar |
| questionCommentIcon | Enum | | Status des Kommentars: `WARNING`, `REVIEWED`, `PROCESSING`, `BLOCKED` |
| text | [Text](#text-text), mehrfach | | Fragetext, Feedbacks, Hinweise |
| subquestion | [Teilfrage](#teilfrage-subquestion), mehrfach | | Lücken der Frage |
| dataset | [Datensatz](#datensatz-dataset), mehrfach | | Zufallsvariablen |

## Text `text`

```xml
<text art="Questiontext" id="0" format="html">
   <inhalt><![CDATA[<p>Berechnen Sie $I = $ [Q0]</p>]]></inhalt>
   <file …>…</file>
</text>
```

Die Texte werden über ihre **Position** zugeordnet; das Attribut `art` ist nur informativ und wird beim
Import ignoriert:

| Position | art | Bedeutung |
|---|---|---|
| 1 | `Questiontext` | Fragetext (Angabe) |
| 2 | `general feedback` | Allgemeines Feedback, siehe [Feedback](../wiki/Feedback/index.md) |
| 3 | `correct feedback` | Feedback bei richtiger Antwort |
| 4 | `partially correct feedback` | Feedback bei teilweise richtiger Antwort |
| 5 | `incorrect feedback` | Feedback bei falscher Antwort |
| 6 | `grader info` | Information für Beurteiler |
| 7, 8 | leer | reserviert |
| ab 9 | `hint` | Hinweise |

LeTTo exportiert immer die ersten sechs Texte. Attribute: `id` (Ganzzahl), `format` (`html` oder leer).
Der Inhalt `inhalt` ist HTML in CDATA. Die Syntax des Fragetexts ist im
[Editor für den Angabetext](../wiki/EditorfürdenAngabetext/index.md) beschrieben; die wichtigsten Elemente:

| Syntax | Bedeutung |
|---|---|
| `[Q0]`, `[Q1]` … | Position der Teilfrage mit diesem Namen (Eingabefeld) |
| `$…$` | LaTeX-Formel |
| `{x}`, `{x,=mA}`, `{x,3}` | Wert des Datensatzes x (mit Einheit, erzwungener Einheit, gültigen Ziffern), siehe [Datensätze](../wiki/Datensätze/index.md) und [Zahlendarstellung](../wiki/Zahlendarstellung/index.md) |
| `{=y}`, `{=x+y}`, `{=y;=mV,3}` | Ergebnis aus dem Maxima-Feld bzw. berechneter Ausdruck |
| `[IMG0]`, `[LINK0 Text]` | Bild bzw. Download-Link auf die erste angehängte Datei, siehe [Dateien zur Frage](../wiki/DateienzurFrageverwalten/index.md) |
| `[PIG Plugin1 "…"]` | Plugin-Grafik, siehe [Plugins](../wiki/Plugins/index.md) |

### Datei `file`

Eine eingebettete Datei (meist ein Bild) gehört zu dem Text, in dem sie steht.

| Attribut | Bedeutung |
|---|---|
| filename | Dateiname inkl. Endung; die Endung bestimmt beim Import den Dateityp. Pflicht |
| id | ID in der Quelldatenbank |
| ext | Dateiendung |
| md5, filePath | Ablage im Bild-Service der Quelle, werden beim Import nicht verwendet |
| width | Breite, z.B. `50%` oder `300px`; ohne Einheit gelten Werte > 105 als Pixel, sonst Prozent |
| height | Höhe (derzeit ohne Wirkung) |
| title, alt, style | HTML-Attribute des Bildes |

Inhalt ist genau eines der Elemente:

* `base64` – Dateiinhalt Base64-codiert in CDATA (so exportiert LeTTo)
* `webPath` – URL in CDATA, von der die Datei beim Import geladen wird
* `inhalt` – veraltete Schreibweise für `base64`

Ein `file` ohne Inhalt (beim Export, wenn die Datei am Server fehlt) wird beim Import verworfen.

## Teilfrage `subquestion`

Eine Teilfrage ist eine Lücke im Fragetext und wird dort über `[Name]` platziert.

| Element | Typ | Standard | Bedeutung |
|---|---|---|---|
| id | Ganzzahl | 0 | |
| grade | Zahl | 1.0 | Punkte der Teilfrage |
| mode | Enum [Teilfragen-Modus](#teilfragen-modus-mode) | 4 | Art der Lücke |
| name | Text (CDATA) | | Name, im Fragetext als `[Name]`, üblich `Q0`, `Q1`, … |
| maxima | Text (CDATA) | leer | Maxima-Feld der Teilfrage; beginnt es mit `:`, rechnet der Parser |
| plugininfo | Text (CDATA) | leer | bei Modus PLUGIN: Plugin-Name, `:`, Parameter |
| plugininputimage | Text | | veraltet, wird ignoriert |
| einheit | Text (CDATA) | | veraltet: Einheit für alle Antworten ohne eigene Einheit (nur Import) |
| shuffleAnswers | Enum [Antworten mischen](#antworten-mischen-shuffleanswers) | 1 | |
| schwierigkeit | Enum [Bewertungsmodus](#bewertungsmodus-schwierigkeit) | 0 | |
| answer | [Antwort](#antwort-answer), mehrfach | | |

## Antwort `answer`

Alle Textfelder in CDATA. Die Bedeutung von `text`, `answer` und `maxima` hängt vom Modus der Teilfrage ab
(siehe [Lösung der Antwort](../wiki/BeispielsammlungEditieren/index.md)):

| Element | Typ | Standard | Bedeutung |
|---|---|---|---|
| id | Ganzzahl | 0 | |
| fraction | Zahl -100..100 | 0 | Anteil der Teilfragen-Punkte in Prozent; negativ = Abzug bei Auswahl |
| format | Text (CDATA) | `html` | Format des Antworttexts |
| text | Text (CDATA) | | Antwort-/Optionstext bzw. Lösung |
| feedback | Text (CDATA) | leer | Feedback zu dieser Antwort (HTML) |
| tolerance | Text (CDATA) | `1.0%` | [Toleranz](../wiki/BeispielsammlungEditieren/toleranz/index.md): `1%` relativ, `0.02` relativ, `a0.1` absolut, `0` exakt |
| correctAnswerFormat | Ganzzahl | 2 | 1 = Nachkommastellen, 2 = signifikante Stellen |
| correctAnswerLength | Ganzzahl | 5 | Stellenanzahl |
| maxima | Text (CDATA) | leer | Formel bzw. Variable des richtigen Ergebnisses |
| answer | Text (CDATA) | leer | Lösung / Zahlenwert des 1. Datensatzes / Zuordnungspartner |
| einheit | Text (CDATA) | leer | [Ziel-Einheit](../wiki/ZielEinheit/index.md), z.B. `A`, `=mA`, `?km/h`, `string`, `symbolfull` |

Belegung je Modus (aus LeTTo-Exporten):

| Modus | text | answer | maxima | fraction |
|---|---|---|---|---|
| CALCULATED | Lösung als Ausdruck der Datensätze, z.B. `U/R` | Ergebnis für Datensatz 1 mit Einheit, z.B. `52mA` | Variable des Maxima-Felds, z.B. `I` | 100 (weitere Antworten mit weniger Prozent für typische Fehler) |
| SINGLECHOICE | Optionstext | leer | leer | 100 für die richtige Option, sonst 0 |
| MULTICHOICE | Optionstext | leer | leer | richtige teilen sich 100, falsche negativ (z.B. -100) |
| TEXT | richtige Antwort | dieselbe in Anführungszeichen, z.B. `"gerade"` | optional | 100 |
| PLUGIN | Lösung für das Plugin | Lösung | Lösungsformel | 100 |

## Datensatz `dataset`

Ein Datensatz ist eine Zufallsvariable der Frage, siehe [Datensätze definieren](../wiki/Datensätzedefinieren/index.md).

| Element | Typ | Bedeutung |
|---|---|---|
| id | Ganzzahl | |
| status | Text (CDATA) | `shared`, `private` oder leer; wird beim Import nicht gelesen |
| name | Text (CDATA) | Variablenname |
| type | Text (CDATA) | `calculated` |
| distribution | Text (CDATA) | `uniform` |
| minimum, maximum | Text (CDATA) | kleinster / größter erzeugter Wert (SI) |
| decimals | Text (CDATA) | `3` oder `0` |
| itemcount | Ganzzahl | Anzahl der erzeugten Werte, üblich 40 |
| zahlenbereich | Text (CDATA) | Wertedefinition **in der Anzeigeeinheit**, z.B. `F2:5-230`, `I1-10`, `E12:1k-10k`, `2:3:15`, `1,2,5` |
| ziffern | Ganzzahl | gültige Ziffern bei der Werterzeugung |
| einheit | Text (CDATA) | Anzeigeeinheit, z.B. `ms` |
| items | Text (CDATA) | erzeugte Werte, durch `;` getrennt, **in SI-Basiseinheit** (10 ms → `0.01`) |

## Aufzählungen

### Fragetyp `questionType`

LeTTo verwendet praktisch nur die Mehrfachberechnungsfrage `22`; die Art jeder Lücke bestimmt der
[Teilfragen-Modus](#teilfragen-modus-mode). Siehe auch [Fragetypen](../wiki/Fragetypen/index.md).

| Wert | Name | Wert | Name |
|---|---|---|---|
| 10 | MoodleNumerical | 17 | MoodleEssay (Freitextfrage) |
| 11 | MoodleCalculated (Berechnungsfrage) | 18 | MoodleMatching (Zuordnungsfrage) |
| 12 | MoodleCalculated_Multi | 19 | MoodleCloze (Lückentextfrage) |
| 13 | MoodleCalculated_Simple | 20 | MoodleTrueFalse |
| 14 | MoodleMultichoice (Multiple-Choice-Frage) | 21 | MoodleRandomsMatch |
| 15 | MoodleShortAnswer | 22 | **MoodleClozeCalc (Mehrfachberechnungsfrage)** |
| 16 | MoodleDescription | 23 | LinkedQuestion |

### Teilfragen-Modus `mode`

| Wert | Name | Bedeutung |
|---|---|---|
| 0 | SINGLECHOICE | Auswahlliste, eine Antwort |
| 1 | TEXT | kurze Texteingabe, muss exakt stimmen |
| 2 | REGEXP | Texteingabe, geprüft mit regulärem Ausdruck (Java) |
| 3 | MULTICHOICE | Mehrfachauswahl |
| 4 | CALCULATED | berechneter Wert (Standard) |
| 5 | BOOLSCH | bewertet Eingaben anderer Teilfragen (Folgefehler), keine eigene Eingabe |
| 6 | PLUGIN | Bewertung durch ein Plugin |
| 7 | FREITEXT | Textfeld ohne automatische Korrektur |
| 8 | ZUORDNUNG | Zuordnung |
| 9 | IMAGE | Abgabe als Bild (Foto/Zwischenablage) |
| 10 | SCHIEBER | Schieberegler (Umfragen) |

Der Import akzeptiert auch die Namen; `SHORTANSWER` wird als `TEXT` gelesen.

### Lückentextmodus `single`

0 MultipleChoice, 1 SingleChoice, 2 Texteingabe, 3 DragAndDrop, 4 RegularExpression, 5 CaseSensitive.

### Antworten mischen `shuffleAnswers`

0 Nicht_mischen, 1 Mischen, 2 Nur_links_mischen, 3 Nur_rechts_mischen (2 und 3 für Zuordnungen),
4 Normal, 5 Streng, 6 Mild (4–6 für Bildabgaben).

### Bewertungsmodus `schwierigkeit`

0 Normal, 1 Streng, 2 Mild, 3 HundertProz – Bedeutung je Fragetyp siehe
[Beispielsammlung editieren](../wiki/BeispielsammlungEditieren/index.md).

## Beispiele

Alle Beispiele sind gültig nach Schema und Prüfskript und können direkt importiert werden:

* [01-berechnung-ohmsches-gesetz.lto](letto-lto/beispiele/01-berechnung-ohmsches-gesetz.lto) –
  Mehrfachberechnungsfrage mit zwei Datensätzen, Maxima-Feld und Einheiten
* [02-auswahl-und-text.lto](letto-lto/beispiele/02-auswahl-und-text.lto) –
  Single-Choice, Multiple-Choice mit negativer Bewertung und Texteingabe in einer Frage
* [03-kategorie-mit-unterordner.lto](letto-lto/beispiele/03-kategorie-mit-unterordner.lto) –
  Fragesammlung mit Unterordner

## KI-Unterstützung

Für das automatische Erzeugen von Fragen mit KI gibt es eine kompakte Formatbeschreibung als
**Skill** im offenen Agent-Skills-Format: [letto-lto-skill.zip](/assets/download/letto-lto-skill.zip).
Das Archiv enthält den Ordner `letto-lto` mit `SKILL.md` (Anleitung und Regeln), den Beispielen, dem Schema
und dem Prüfskript.

| Werkzeug | Einrichtung |
|---|---|
| Claude Code | Ordner `letto-lto` nach `~/.claude/skills/` (für alle Projekte) oder `.claude/skills/` im Projekt entpacken |
| Claude (claude.ai, Desktop) | Einstellungen → Fähigkeiten → Skill hochladen → ZIP auswählen |
| OpenAI Codex | Ordner `letto-lto` nach `~/.codex/skills/` entpacken |
| ChatGPT | Eigenes GPT bzw. Projekt anlegen und `SKILL.md` sowie die Beispieldateien als Wissen hochladen; als Anweisung z.B.: „Erzeuge LeTTo-Fragen als .lto-Datei streng nach SKILL.md.“ |

Danach genügt eine Anfrage wie „Erstelle 5 LeTTo-Rechenaufgaben zum Ohmschen Gesetz für die 1. Klasse HTL
als .lto-Datei“. Erzeugte Fragen werden mit dem Kommentarstatus „in Bearbeitung“ importiert und sollten
in der [Fragen-Vorschau](../wiki/Fragen-Vorschau/index.md) geprüft werden.

## Bekannte Abweichungen im Code

Diese Punkte betreffen das Verhalten von Export und Import, nicht das Format. Die ersten vier sind in
`letto-export` (Branch `version-1.3`) nach Revision 7045 behoben; Server mit älterem Export-Service zeigen
das beschriebene Verhalten noch:

* **penalty:** Der Export schreibt den Abzug als `<penalty>`, ältere Importe lesen nur `<abzug>`. Der Abzug
  geht dort bei Export und erneutem Import verloren. Jetzt werden beide Elemente gelesen.
* **Fehlende `break` im Import:** Ab `creationDate` fehlten in `XmlImport.parseQuestion` die `break`-Anweisungen.
  Jedes dieser Felder wurde zusätzlich in die nachfolgenden Felder gelesen. Fehlt `questionCommentMsg`, entsteht
  bei älteren Importen ein Kommentar mit dem Inhalt von `changeLogMap` (meist `{}`) und dem Status `PROCESSING`.
* **Datum:** `creationDate` und `lastChange` wurden immer leer exportiert (`XmlExport.XMLDate` verwarf das
  formatierte Datum).
* **licenceKey:** wurde als `<licenceKey >` mit Leerzeichen geschrieben; das ist gültiges XML und wird korrekt gelesen.
* **Kompetenzen** der Teilfragen (`ExportKompetenzSubquestionV1`) sind im DTO vorhanden, werden aber nicht exportiert.

## Quelle

Das Format ist im Projekt `letto-export` definiert:

* `exportservice/…/service/threads/XmlExport.java` – Schreiben
* `exportservice/…/service/threads/XmlImport.java` – Lesen
* `exportservice/…/xml/XMLfileLTO.java` – Wurzelelement und Formaterkennung
* `exportclient/…/dto/questions/*.java` – Datenklassen
* `tools/…/enums/*.java` (LeTTo-Server) – Aufzählungen

Das Schema wurde gegen 132 reale LeTTo-Exporte mit 1091 Fragen geprüft.
