# Berechnungen: Einbau der Funktionsreferenz

Das Paket enthält 451 einzelne Beschreibungsseiten: 396 Funktionen, 37 Operatoren, 15 Konstanten und 3 Klammerarten. Hinzu kommen die angepasste Hauptseite, die alphabetische Funktionsübersicht und 28 Themenübersichten.

## Einbau

1. ZIP in ein temporäres Verzeichnis entpacken.
2. Den enthaltenen Ordner `wiki/Berechnungen` mit dem gleichnamigen Ordner im GitHub-Pages-Repository zusammenführen. Die Datei `wiki/Berechnungen/index.md` wird dabei durch die neue Übersicht ersetzt.
3. Bereits vorhandene Bilder und andere Dateien im Wiki-Verzeichnis beibehalten. Der Ordner wird ergänzt, nicht zuvor gelöscht.
4. Änderungen committen und die vorhandene GitHub-Pages-Veröffentlichung durchführen.

Die Dateien im Paket liegen bereits unter `wiki/Berechnungen`. Wird das ZIP unmittelbar im Repository-Stamm entpackt, ist keine zusätzliche Verschiebung der Markdown-Dateien notwendig. `README.md`, `Hinweise-zum-Quellcode.md`, `Pruefbericht.md` und `Seitenverzeichnis.csv` sind Begleitdateien und müssen nicht auf die Website übernommen werden.

## Struktur und Links

- `wiki/Berechnungen/index.md`: bestehender allgemeiner Artikel und Tabellen mit Links zu sämtlichen Detailseiten. Die lange Parameterreferenz wurde entfernt und auf die Detailseiten übertragen.
- `wiki/Berechnungen/func/index.md`: alphabetische Übersicht aller Funktionen.
- `wiki/Berechnungen/func/<thema>/<funktion>/index.md`: eine Seite je Funktionsname; mehrere Aufrufvarianten stehen gemeinsam auf dieser Seite.
- `wiki/Berechnungen/operatoren/<infix|prefix|suffix>/<operator>/index.md`: eine Seite je Operator und Position. Die unterschiedlichen Bedeutungen von `+`, `-` und `%` bleiben so getrennt.
- `wiki/Berechnungen/konstanten/<name>/index.md`: Konstanten.
- `wiki/Berechnungen/klammern/<klammerart>/index.md`: Klammerarten.

Auch Aliasnamen haben eigene Seiten mit Rückverweis zur verwandten Funktion. Groß-/Kleinschreibungsvarianten haben kollisionsfreie Verzeichnisnamen, damit das Repository auch auf Windows ausgecheckt werden kann.

Die relative Linkschreibweise mit `index.md` entspricht der angelieferten Seite. Der bereits vorhandene Aufbau und die Verarbeitung durch die GitHub-Pages-Seite werden weiterverwendet; es sind keine neuen Plugins oder JavaScript-Dateien erforderlich.

## Bilder und Demobeispiele

Die Anhänge enthalten keine Bilddateien. Vorhandene Bildverweise wurden auf den Detailseiten relativ auf ihre bisherigen Speicherorte unter `wiki/Berechnungen` angepasst. Daher müssen die entsprechenden Bilder im bestehenden Repository erhalten bleiben. Die Übersicht behält ebenfalls ihre bisherigen Bildverweise.

Alle vorhandenen Demo-IDs wurden übernommen. Die Linkpfade auf den tiefer liegenden Detailseiten wurden entsprechend angepasst. Die Zieldatei `demobsp.html` sowie andere Wiki-Kapitel sind Bestandteile des bestehenden Repositorys und nicht Teil dieses Pakets. Die Erreichbarkeit der Demoanwendung wurde nicht online getestet.

Ein verbleibender `/notimplemented/index.md`-Verweis betrifft die **Fragendefinition** im Abschnitt Ergebnisvorschau, keine Funktion. Dieser unverwandte Verweis wurde beibehalten, weil dessen tatsächliche Zielseite aus den Anhängen nicht hervorgeht.

## Revision und Änderungsdatum

Bei 63 Funktionen enthält die Übersicht eine belegte Einführungsrevision; diese wurde übernommen. Für andere Elemente ist die Revision ausdrücklich als nicht ermittelbar bezeichnet. Die mitgelieferten Java-Dateien enthalten keine vollständige Versionsgeschichte.

Als letzte Änderung der neu erstellten Dokumentationsseiten ist der 06.10.2026 angegeben. Dieses Datum bezeichnet die Dokumentation, nicht die letzte Codeänderung. Ein nicht belegtes Änderungsdatum der Implementierung wird nicht erfunden.

## Inhaltliche Grundlage

Die Beschreibungen übernehmen die ursprüngliche Übersicht und sämtliche 394 Einträge der detaillierten Parameterreferenz. Zusätzlich wurden `float` und `mathe`, die nur in der Kurzliste stehen, aufgenommen. Java-Implementierungen wurden für Parameterprüfungen, zusätzliche Aufrufvarianten und ausgewählte Randfälle herangezogen. Bekannte Widersprüche zwischen Hilfe und Implementierung werden auf den betroffenen Seiten erläutert; siehe auch `Hinweise-zum-Quellcode.md`.

Dies ist eine Dokumentationsänderung. Es wurden keine Java-Quelldateien verändert. Eine Ausführung aller LeTTo-Funktionen war mit dem isolierten Funktionspaket ohne Registrierung und weitere Projektabhängigkeiten nicht möglich. Beispiele stammen aus der gelieferten Referenz oder wurden anhand des Codes bzw. der beschriebenen mathematischen Operation ergänzt.
