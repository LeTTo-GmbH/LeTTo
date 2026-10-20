# Datensätze / Einheiten anpassen
Der Dialog zur **Zuordnung von Einheiten und Wertebereichen zu Formelzeichen** kann aus dem [Kategorie-Baum](../../Ordnerverwaltung/index.md) über das [Kontext-Menü](../../Ordnerverwaltung/index.md#kontext-menü) aufgerufen werden.
Der Menüpunkt steht nur in Ordnern zur Verfügung, in denen Sie Änderungsrechte besitzen.

## Zweck
Wird in einer Frage ein neuer [Datensatz](../../../Berechnungen/Datensätze/index.md) angelegt, dann schlägt LeTTo anhand des Variablennamens
automatisch eine **Einheit** und einen **Wertebereich** vor. In diesem Dialog legen Sie fest, welche Vorschläge in einem Ordner gelten.

Beispiel: Ist für das Formelzeichen `R` die Einheit `Ohm` und der Wertebereich `E12:1k-100k` definiert, dann wird ein neuer
Datensatz `R1` automatisch mit der Einheit Ohm und mit Werten der Normreihe E12 zwischen 1kOhm und 100kOhm angelegt.

Die Einstellungen wirken nur beim **Anlegen neuer Datensätze**. Bereits bestehende Datensätze werden nicht verändert.

## Aufbau des Dialogs
**Einheiten verwenden:** Ist diese Checkbox nicht ausgewählt, dann werden neue Datensätze in diesem Ordner ohne physikalische Einheit angelegt.

Die Tabelle enthält für jedes Formelzeichen eine Zeile mit folgenden Spalten:

| Spalte         | Bedeutung                                                                                                                                         |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Formelzeichen  | Formelzeichen lt. SI-Einheitensystem, zB. `R` für Widerstand, `L` für Spule. Es gilt für alle Variablen, deren Name mit diesem Formelzeichen beginnt (`R` gilt also für `R1`, `R2`, `Ra`, ...). |
| EH             | Ist diese Checkbox ausgewählt, dann wird statt der Standard-Einheit lt. SI-System die Einheit aus der Spalte *Einheit* verwendet.                  |
| Einheit        | Einheit, die für dieses Formelzeichen in diesem Ordner verwendet wird. Nur sichtbar, wenn *EH* ausgewählt ist.                                     |
| Default-Werte  | Wertebereich, mit dem ein neuer Datensatz für dieses Formelzeichen belegt wird. Die Syntax ist unter [Datensätze definieren](../../../Berechnungen/Datensätzedefinieren/index.md) beschrieben. |
| X              | Löscht das Formelzeichen aus der Tabelle (nach einer Sicherheitsabfrage).                                                                         |

Die Werte in der Tabelle werden direkt durch Anklicken der Zelle bearbeitet.

Das Formelzeichen `default` hat eine besondere Bedeutung: Sein Wertebereich wird für alle Variablen verwendet, für die kein passendes Formelzeichen definiert ist.
Die Einheit solcher Variablen wird aus dem Variablennamen lt. SI-System ermittelt.

### Schaltflächen
* **Speichern:** Übernimmt die Tabelle für den aktuellen Ordner und schließt den Dialog.
* **Formelzeichen einfügen:** Fügt eine neue Zeile mit dem Platzhalter `Formelzeichen` und dem Wertebereich `I1-10` ein.
* **Abbrechen:** Schließt den Dialog ohne zu speichern.

## Vererbung
Die Definitionen können in jedem Ordner anders festgelegt werden. Hat ein Ordner keine eigenen Definitionen, dann gelten die
Einstellungen des nächsten übergeordneten Ordners. Ist auch dort nichts definiert, dann gilt die Standardeinstellung des Servers:

| Formelzeichen | Einheit | Default-Werte  |
|---------------|---------|----------------|
| default       |         | I1-10          |
| R             | Ohm     | E12:1k-100k    |
| L             | H       | 1m-100m        |
| C             | F       | E12:1n-100n    |
