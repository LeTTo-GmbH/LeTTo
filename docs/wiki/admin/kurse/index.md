# Kursverwaltung

Die Kursverwaltung wird in Installationen mit automatischer Verrechnung anstelle des klassischen Untis-Imports verwendet. Sie verwaltet Kurse eines Studienjahres und einer Abteilung sowie deren Vortragende und Teilnehmer.

## Filter und Kursliste

Zuerst werden **Abteilung** und **Studienjahr** gewählt. Zusätzlich kann nach einem Vortragenden und nach einem Teil des Kursnamens gefiltert werden. Die Kursliste zeigt Kursnummer, Bezeichnung sowie die Anzahl der Vortragenden und Teilnehmer.

## Kursdetails

Nach Auswahl eines Kurses erscheinen rechts die Kursdaten, Vortragenden und Teilnehmer. Die Kursnummer und Bezeichnung können über den [Bearbeitungsdialog](dialog-kurs-bearbeiten/index.md) geändert werden.

Vortragende können hinzugefügt oder geändert werden. Ein Vortragender kann nur gelöscht werden, wenn dies laut Backend zulässig ist; der letzte Vortragende eines Kurses kann nicht einfach entfernt werden. Teilnehmer werden über einen CSV-Import hinzugefügt.

## Neuer Kurs

**Neuen Kurs anlegen** öffnet den [Kursdialog](dialog-kurs-neu/index.md). Beim Anlegen werden Abteilung, Studienjahr und Hauptvortragender berücksichtigt.

## Teilnehmer importieren

Der [Teilnehmer-Importdialog](dialog-teilnehmer-import/index.md) erwartet eine CSV-Datei mit Kennung, Nachname, Vorname und optional E-Mail. Die Datei wird vor dem Speichern eingelesen und als Vorschau angezeigt.

## Kurs löschen

Beim Löschen ist eine Bestätigung erforderlich. Enthält der Kurs bereits Aktivitäten oder Beurteilungen, kann eine zusätzliche Sicherheitsabfrage notwendig sein.
