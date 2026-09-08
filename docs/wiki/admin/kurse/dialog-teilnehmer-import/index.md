# Dialog: Kursteilnehmer importieren

Der Teilnehmerimport liest eine CSV-Datei für den aktuell ausgewählten Kurs ein. Unterstützt werden die Spalten:

```text
Kennung;Nachname;Vorname;Email
```

Die E-Mail-Spalte ist optional. Encoding und Trennzeichen können im Dialog festgelegt werden. Nach Auswahl einer Datei werden die erkannten Teilnehmer als Vorschau angezeigt. Pflichtspalten bzw. unbrauchbare Daten führen zu einer Fehlermeldung und verhindern das Speichern.

Erst mit Bestätigung werden die eingelesenen Teilnehmer an die Kursverwaltung zurückgegeben und importiert.
