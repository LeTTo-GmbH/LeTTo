---
name: letto-lto
description: Erzeugt Fragen und Fragesammlungen für die Lernplattform LeTTo als importierbare .lto-Dateien (XML, letto mode="101") – Rechenaufgaben mit Zufallsdatensätzen und Einheiten, Single-/Multiple-Choice, Texteingabe, Freitext. Verwenden, wenn LeTTo-Fragen, eine LeTTo-Fragesammlung oder eine .lto-Datei erstellt, geändert oder geprüft werden sollen.
---

# LeTTo-Fragen im .lto-Format erzeugen

LeTTo (https://letto.at) ist eine Lernplattform für Mathematik, Naturwissenschaften und Technik.
Fragen werden als `.lto`-Datei (XML) exportiert und importiert: im Fragesammlungs-Baum über
Rechtsklick auf einen Ordner → „Daten importieren“. Diese Anleitung beschreibt alles, was du zum
Erzeugen gültiger Dateien brauchst. Menschliche Doku: https://doc.letto.at/lto/

Dateien in diesem Skill-Ordner:
- `beispiele/*.lto` – vollständige, gültige Vorlagen. **Kopiere deren Aufbau**, statt frei zu formulieren.
- `validate_lto.py` – Prüfskript (nur Python-Standardbibliothek): `python validate_lto.py datei.lto`
- `lto-v1.xsd` – XML-Schema für XSD-Validatoren.

## Arbeitsablauf

1. **Klären**: Thema, Schulstufe, Anzahl der Fragen, Sprache, Ordnerstruktur, Fragearten.
   Ohne Angabe: Deutsch, Rechenaufgaben mit Zufallswerten, wo das Thema es zulässt.
2. **Jede Frage planen**: Angabetext, Teilfragen (Lücken), Variablen mit Wertebereich und Einheit,
   Formeln, Musterlösung. Rechne die Lösung für den ersten Datensatz selbst nach.
3. **XML schreiben** nach den Vorlagen und den Regeln unten.
4. **Prüfen**: `python validate_lto.py datei.lto` ausführen (falls du Code ausführen kannst) und alle
   FEHLER beheben. Ohne Codeausführung: Checkliste am Ende durchgehen.
5. **Ausgeben**: eine Datei pro Frage (`<letto><question>`) oder eine Sammlung (`<letto><category>`),
   UTF-8, Endung `.lto`. Weise darauf hin, die Datei in LeTTo zu importieren und in der Vorschau zu testen.

## Harte Regeln (sonst scheitert oder verfälscht der Import)

1. **Wurzel**: `<?xml version="1.0" encoding="UTF-8"?>` dann `<letto mode="101" databaseinfo="sql">`
   mit **genau einem** Kind: `<category>`, `<question>` oder `<subquestion>`.
2. **CDATA-Pflicht**: Alle Textfelder (in der Vorlage mit `<![CDATA[...]]>`) MÜSSEN als CDATA
   geschrieben werden. Der Import liest bei ihnen nur CDATA – `<name>Test</name>` ergibt einen
   **leeren** Namen. Leere Felder als `<feld/>`. Ausnahme: Zahlen, Booleans und Enum-Felder ohne CDATA.
   Der Text darf `]]>` nicht enthalten.
3. **Reihenfolge**: Elemente exakt in der Reihenfolge der Vorlage (= Exportreihenfolge).
4. **Texte nach Position**: Jede Frage hat genau sechs `<text>`-Elemente in dieser Reihenfolge:
   Fragetext, allgemeines Feedback, Feedback richtig, Feedback teilweise richtig, Feedback falsch,
   Info für Beurteiler. Das Attribut `art` ist nur Kosmetik – zählt wird die Position.
5. **IDs**: alle `<id>`, `<idUser>` und `id="…"`-Attribute auf `0` setzen (LeTTo vergibt neue).
6. **Nicht befüllen** (leer lassen oder weglassen): `maximaAngabe`, `md5`, `licenceKey`, `security`,
   `creationDate`/`lastChange` (leer: `<creationDate></creationDate>`).
   **Immer setzen**: `<questionCommentMsg><![CDATA[KI-generiert – bitte prüfen]]></questionCommentMsg>` und
   `<questionCommentIcon>PROCESSING</questionCommentIcon>` – markiert die Frage in LeTTo als „in Bearbeitung“
   (ohne diese Felder setzen ältere LeTTo-Versionen beim Import einen Kommentar „{}“).
7. **Namen**: Fragenamen innerhalb eines Ordners eindeutig (sonst hängt der Import „-1“ an) und nur aus
   Buchstaben (inkl. äöüß), Ziffern, Leerzeichen und `_ - ; : # ^ $ + * .` – alle anderen Zeichen
   (Klammern, Komma, `/`, `?`, `–`) entfernt der Import.
   Teilfragen heißen `Q0`, `Q1`, … in Reihenfolge. Datensatz-/Variablennamen: Buchstabe am Anfang, dann
   Buchstaben/Ziffern; im Maxima-Feld **kein Unterstrich**.
8. **Platzhalter**: Jede Teilfrage steht genau einmal als `[Q0]`, `[Q1]` … im Fragetext. Kein `[Qn]` ohne Teilfrage.
9. **Fragetyp**: Verwende immer `<questionType>22</questionType>` und `type="MoodleClozeCalc"`
   („Mehrfachberechnungsfrage“). Die Art jeder Lücke legt `subquestion/mode` fest.
   `<punkte>` = Summe der `grade` der Teilfragen.
10. `<penalty/>` leer lassen (ältere LeTTo-Versionen lesen den Abzug beim Import nicht ein).
11. **CDATA-Inhalte nicht einrücken**: Alles zwischen `<![CDATA[` und `]]>` wird wörtlich übernommen.
    Mehrzeilige Inhalte (Maxima-Feld, HTML) beginnen jede Zeile ohne XML-Einrückung.

## Aufbau

```
letto (mode="101")
└─ category                     Ordner: name, dann question*, dann category*
   ├─ name                      CDATA
   ├─ question*                 siehe Vorlage beispiele/01-…
   │  ├─ (Einzelfelder)         questionType, single, name, punkte, …, maxima, …
   │  ├─ text ×6                <text art=".." id="0" format="html"><inhalt><![CDATA[HTML]]></inhalt></text>
   │  ├─ subquestion*           id, grade, mode, name, maxima, plugininfo, shuffleAnswers, schwierigkeit, answer*
   │  │  └─ answer*             id, fraction, format, text, feedback, tolerance, correctAnswerFormat,
   │  │                         correctAnswerLength, maxima, answer, einheit
   │  └─ dataset*               id, status, name, type, distribution, minimum, maximum, decimals,
   │                            itemcount, zahlenbereich, ziffern, einheit, items
   └─ category*                 Unterordner (gleicher Aufbau)
```

Einzelfelder der Frage in Reihenfolge mit empfohlenen Werten (Standardwerte von LeTTo):

| Element | Wert | Bedeutung |
|---|---|---|
| id, idUser | 0 | |
| questionType | 22 | Mehrfachberechnungsfrage |
| single | 2 bei reinen Rechenaufgaben, sonst 0 | Lückentextmodus; die Art jeder Lücke bestimmt trotzdem `subquestion/mode` |
| name | CDATA | Fragename |
| punkte | z.B. 2.0 | Summe der Teilfragen-grades |
| penalty | leer | |
| hidden | 0 | |
| tag | CDATA oder leer | Schlagworte |
| noAutoCorrect, usecase, synchronize | 0 | |
| shuffleAnswers | 1 | Antworten mischen |
| answerNumbering | CDATA `abc` | |
| unitGradingType | 2 | 2 = Einheit muss stimmen, 0 = nur Zahlenwert |
| unitPenalty | 0.1 | Abzug bei falscher Einheit (0..1) |
| showUnits, unitsLeft | 0 | |
| maxima | CDATA | Berechnungen der Frage (siehe unten) |
| responseFormat | CDATA `editor` | |
| responseFieldLines, attachments | 10, 3 | |
| md5, units, plugins | leer | |
| sendToParser | false | false = Maxima rechnet, true = LeTTo-Parser |
| preCalc | false | |
| streng | false | true = nur ganz richtig/ganz falsch |
| licenceKey | leer | |
| konstanteMitProzent | true | Konstanten mit %: `%pi`, `%e`, `%mu0` … |
| useSymbolicMode | false | |
| addDocumentsPossible | false | true = Schüler dürfen Dateien hochladen |
| info | CDATA | kurze Beschreibung der Frage (für Lehrende) |
| randomDataset | false | |
| creationDate, lastChange | leer | |
| security, copyright | leer | |
| onRamp | false | true = nächste Teilfrage erst nach richtiger Antwort |
| jsonMap, changeLogMap | CDATA `{}` | |
| questionCommentMsg | CDATA `KI-generiert – bitte prüfen` | Bearbeitungskommentar |
| questionCommentIcon | PROCESSING | Status: PROCESSING, REVIEWED, WARNING, BLOCKED |

## Teilfragen (Lücken)

`<grade>` = Punkte der Teilfrage (Standard 1.0), `<shuffleAnswers>1</shuffleAnswers>`,
`<schwierigkeit>0</schwierigkeit>` (0 Normal, 1 Streng, 2 Mild, 3 HundertProz), `<maxima/>` und
`<plugininfo/>` meist leer. `fraction` = Prozent der Teilfragen-Punkte für diese Antwort (-100..100).

| mode | Name | Antworten befüllen |
|---|---|---|
| 4 | CALCULATED – Berechnung | **eine** Antwort: `fraction` 100, `maxima` = Variable/Formel aus dem Maxima-Feld (z.B. `I`), `text` = Lösung als Ausdruck der Datensätze (z.B. `U/R`), `answer` = Ergebnis für Datensatz 1 mit Einheit (z.B. `52mA`), `einheit` = Ziel-Einheit (z.B. `A`), `tolerance` z.B. `1%`. Weitere Antworten mit kleinerer fraction für typische Fehler möglich (eigene `maxima`). |
| 0 | SINGLECHOICE – Auswahlliste | eine Antwort pro Option: `text` = Optionstext, richtige Option `fraction` 100, andere 0. Kein LaTeX. |
| 3 | MULTICHOICE – Mehrfachauswahl | eine Antwort pro Option: richtige Optionen teilen sich 100 (z.B. 2× 50), falsche Optionen negativ (üblich -100, mildere Abzüge wie -50 erlaubt). `text` = Optionstext, `$LaTeX$` erlaubt. |
| 1 | TEXT – kurze Texteingabe | `text` = richtige Antwort, `answer` = dieselbe in Anführungszeichen (`"Sperrschicht"`), fraction 100. Muss exakt eingegeben werden. |
| 2 | REGEXP | `text`/`answer` = regulärer Ausdruck (Java-Syntax), fraction 100. |
| 7 | FREITEXT – Aufsatz | eine Antwort mit fraction 100, Felder leer; manuelle Korrektur. Musterlösung ins allgemeine Feedback. |
| 5 | BOOLSCH | bewertet andere Teilfragen (Folgefehler); wird nicht platziert. Nur auf ausdrücklichen Wunsch. |
| 6 | PLUGIN, 8 ZUORDNUNG, 9 IMAGE, 10 SCHIEBER | nur auf ausdrücklichen Wunsch und nach Vorlage einer echten LeTTo-Exportdatei. |

Bei allen Antworten zusätzlich (`tolerance` ist bei Auswahl-Lücken bedeutungslos, `1%` stehen lassen):
`<format><![CDATA[html]]></format>`, `<feedback/>` (oder CDATA-HTML),
`<correctAnswerFormat>2</correctAnswerFormat>`, `<correctAnswerLength>5</correctAnswerLength>`.

## Fragetext (HTML in CDATA)

- HTML mit `<p>`, `<br>`, `<b>`, `<i>`, `<strong>`, `<em>`, `<ul>/<ol>/<li>`, `<table>…`, `<h2>`, `<pre>`, `<span>`.
  Andere Tags entfernt LeTTo. Umlaute direkt (UTF-8) oder als HTML-Entity.
- Lücken: `[Q0]`, `[Q1]` … an die Stelle, wo das Eingabefeld erscheinen soll, z.B. `$I = $&nbsp;[Q0]`.
- Formeln in LaTeX zwischen `$…$`; ein echtes Dollarzeichen als `\$`.
- Variablenwerte einsetzen: `{U}` (Wert mit Einheit, optimales Vielfaches), `{U,=mV}` (Einheit erzwingen),
  `{U,3}` (3 gültige Ziffern). Ergebnis einer Rechnung: `{=P}` oder `{=U*I}`; mit Format `{=P;=mW,3}`.
  Funktioniert auch innerhalb von `$…$`: `$R = {R}$`.
- Eckige Klammern, die kein LeTTo-Tag sind, bleiben normal stehen.
- Feedback-Texte (Position 2–5) ebenfalls HTML; im allgemeinen Feedback eignet sich ein Lösungsweg
  mit `{=…}`-Werten.

## Maxima-Feld der Frage

Berechnet aus den Datensätzen die Ergebnisse; eine Anweisung pro Zeile, keine `;` nötig:
```
I : U/R
P : U*I
```
- Zuweisung `name : ausdruck` (`::` = ohne Vereinfachung); Kommentar `//`.
- Variablennamen ohne Unterstrich. Datensätze sind automatisch als Variablen verfügbar.
- Variablennamen dürfen grundsätzlich wie Einheiten heißen (z.B. `T` in echten LeTTo-Fragen). Im Zweifel
  eindeutige Namen wie `t1`, `sw`, `h0` statt `s`, `h`, `min` verwenden.
- Konstanten mit `%` (tragen ihre Einheit): `%pi`, `%e`, `%i`, `%g` = 9.81 m/s², `%c0` Lichtgeschwindigkeit,
  `%mu0`, `%epsilon0`, `%Qe` Elementarladung, `%k` Boltzmann, `%NA` Avogadro, `%h` Planck. Funktionen wie in Maxima:
  `sqrt`, `sin`, `cos`, `tan`, `asin`, `exp`, `log`, `abs`, …
- Werte mit Einheit direkt: `U0 : 230V`, `f : 50Hz`; zusammengesetzte Einheiten in Hochkomma: `v : 3'm/s'`.

## Datensätze (Zufallsvariablen)

Jede Variable der Angabe ist ein `<dataset>`. LeTTo speichert **40 Werte in SI-Basiseinheit** und
weist sie zufällig den Schülern zu; angezeigt wird mit der Einheit aus `<einheit>`.

| Element | Inhalt |
|---|---|
| name | Variablenname, z.B. `U` |
| status | leer |
| type / distribution | `calculated` / `uniform` |
| zahlenbereich | Definition (siehe unten) **in der Anzeigeeinheit**, z.B. `F2:5-230` (V) oder `I1-10` (h) |
| einheit | Anzeigeeinheit, z.B. `V`, `mA`, `Ohm`, `ms`, `km/h` |
| items | 40 Werte, `;`-getrennt, **in SI-Basiseinheit** (10 ms → `0.01`, 4,7 kΩ → `4700`) |
| itemcount | 40 |
| minimum / maximum | kleinster / größter Wert aus items (SI) |
| decimals | `3` (wird von LeTTo nicht mehr ausgewertet) |
| ziffern | gültige Ziffern der Werte, z.B. 2 bei `F2:…`, 12 bei Folgen und Listen |

Beispiel mit Umrechnung: `zahlenbereich` = `I30-130`, `einheit` = `km/h` → `items` in m/s
(`36.11111111111;8.333333333333;…`, ca. 12 gültige Ziffern); `zahlenbereich` = `5:5:60`, `einheit` = `min`
→ `items` in s (`300;600;…`). „Datensatz 1“ ist immer der erste Wert in `items`.

`zahlenbereich`-Syntax: `3-15` Bereich, `I3-15` Ganzzahlen, `F3:10-500` Gleitkomma mit 3 gültigen
Ziffern, `2:3:15` arithmetische Folge (2,5,8,11,14), `13:45-130` 13 Werte im Bereich,
`E12:1k-10k` Normreihe (E3/E6/E12/E24/E48), `34,15k,24.4m` Liste. Vielfache: p n u m k M G.
Erzeuge die 40 `items` selbst passend zum `zahlenbereich` (Listen zyklisch wiederholen) und
wähle Bereiche so, dass die Ergebnisse realistisch sind und nicht durch 0 geteilt wird.

## Einheiten, Ziel-Einheit, Toleranz

- Werte mit Einheit ohne Leerzeichen: `52mA`, `4.7kOhm`, `10ms`, `230V`. Dezimalpunkt, kein Komma.
  Ohm als `Ohm`, Grad als `°`, Prozent als `%`. Einheiten mit Rechenzeichen in Hochkomma: `29'km/h'`,
  `9.81'm/s^2'` – im Maxima-Feld, in `answer` und in `einheit` (`'m/s'`). Einheiten aus einem Symbol mit
  Vorsatz (`km`, `ms`, `kOhm`) brauchen keine Hochkomma.
- Gängige Einheiten: s, min, h, m, km, g, kg, t, N, J, W, Pa, bar, V, A, Ohm, F, H, Hz, Upm (Umdrehungen pro
  Minute), °, %, Euro. Vollständige Liste: https://doc.letto.at/wiki/Einheit/
- `answer` der Berechnungsantwort: Ergebnis für Datensatz 1 in der Ziel-Einheit mit 5 gültigen Ziffern,
  z.B. `75.833km`, `41.07'm/s'`.
- `answer/einheit` (Ziel-Einheit): `A` = gleiche Dimension (Schüler darf mA, kA … eingeben);
  `=mA` = genau diese Einheit; `?km/h` = diese Einheit mit beliebigem Vorsatz; leer = wie das Ergebnis.
  Für Text-Ergebnisse `string`, für symbolische Ergebnisse (Formel als Antwort) `symbolfull`.
- `tolerance`: `1%` relativ (Standard für Rechenaufgaben), `a0.01` absolut in SI-Einheit,
  `0` exakt. Bei Ergebnis 0 immer absolute Toleranz verwenden.

## Bilder (optional)

Eine Datei gehört zu einem `<text>` und folgt nach `<inhalt>`:
```xml
<text art="Questiontext" id="0" format="html">
   <inhalt><![CDATA[<p>[IMG0]</p><p>Bestimmen Sie … [Q0]</p>]]></inhalt>
   <file filename="schaltung.png" id="0" ext="png" width="50%" height="50" title="" alt="Schaltung" style="">
      <base64><![CDATA[iVBORw0KGgo…]]></base64>
   </file>
</text>
```
Im Text wird die erste Datei mit `[IMG0]` eingebunden, die zweite mit `[IMG1]` usw.
Erfinde keine Base64-Daten; ohne echte Bilddatei die Frage ohne Bild formulieren.

## Checkliste vor der Ausgabe

- [ ] Wurzel `letto mode="101"`, genau ein Kind, UTF-8.
- [ ] Alle Textfelder als CDATA, Reihenfolge wie Vorlage, sechs `<text>` pro Frage.
- [ ] Alle IDs 0; Fragenamen pro Ordner eindeutig.
- [ ] Jede Teilfrage `Qn` genau einmal im Fragetext, Platzhalter und Teilfragen passen zusammen.
- [ ] `punkte` = Summe der `grade`.
- [ ] Single-Choice: genau eine Antwort mit 100; Multiple-Choice: positive fractions ergeben 100.
- [ ] Rechenaufgaben: jede Variable als Dataset mit 40 Werten in SI, Formeln im Maxima-Feld,
      `answer` = nachgerechnetes Ergebnis für Datensatz 1 mit Einheit, sinnvolle Toleranz und Ziel-Einheit.
- [ ] `python validate_lto.py datei.lto` meldet keine FEHLER.

## Hinweise

- Einige Felder berechnet LeTTo im Editor selbst (`answer` und `text` der Berechnungsantwort,
  `minimum`/`maximum`, die Datensatzwerte). Ob der Import sie neu berechnet, ist nicht garantiert –
  liefere sie deshalb vollständig und korrekt, genau so wie LeTTo exportiert.
- Für ungewöhnliche Fragearten (Plugins, Zuordnung, Bildabgabe) zuerst eine echte Exportdatei aus
  LeTTo als Vorlage anfordern.
- Format-Version und Quelle: LeTTo `letto-export`, Klassen `XmlExport`/`XmlImport`.
