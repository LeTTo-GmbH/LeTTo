# Fragen in Aktivität gruppieren

Mit einer **Fragengruppe** wird aus mehreren Fragen einer Aktivität bei jedem Versuch nur eine festgelegte Anzahl
**zufällig ausgewählt**. So bekommen die Schüler unterschiedliche Fragen – zB. werden aus fünf gleichwertigen Fragen
zu einem Thema für jeden Schüler zwei gezogen.

## Voraussetzungen

* Die Aktivität muss sich im Modus **Testbearbeitung** befinden (Link „Aktivität zur Bearbeitung festlegen“, siehe
  [Beispiele zu Test hinzufügen](../BeispielezuTesthinzufügen/index.md)). Die Fragen der Aktivität werden dann in der
  Frageliste angezeigt.
* Die Fragen, die gruppiert werden sollen, sind bereits in der Aktivität enthalten.

## Fragengruppe anlegen

1. In der Frageliste der Aktivität die Fragen markieren, aus denen ausgewählt werden soll
   (mehrere Fragen mit **Strg**- bzw. **Shift**-Klick).
2. Rechtsklick auf eine der markierten Fragen und **„Fragen in Aktivität gruppieren“** wählen.
3. Im Dialog **„Gruppierung von Fragen“** eingeben, **wie viele Fragen** aus dieser Gruppe in einem Versuch verwendet
   werden, und mit **OK** bestätigen.

Die Anzahl muss **kleiner** sein als die Anzahl der markierten Fragen – sonst gäbe es nichts auszuwählen.
Keine der markierten Fragen darf bereits zu einer anderen Fragengruppe gehören.

Gruppierte Fragen werden in der Frageliste mit einem eigenen Symbol gekennzeichnet; aufeinanderfolgende Gruppen
erhalten abwechselnd unterschiedliche Symbole, damit man sie unterscheiden kann.

## Anzahl ändern oder Gruppe aufheben

Rechtsklick auf eine Frage der Gruppe:

* **„Anzahl an Fragen der Gruppe ändern“** – öffnet denselben Dialog mit der aktuellen Anzahl. Sind mehrere Fragen
  markiert, müssen alle zur selben Gruppe gehören.
* **„Gruppierung aufheben“** – die Fragen bleiben in der Aktivität, werden aber wieder alle verwendet.

## Wirkung bei der Durchführung

* Beim Start eines Versuchs werden aus jeder Fragengruppe **zufällig** so viele Fragen gezogen, wie für die Gruppe
  eingestellt ist. Fragen ohne Gruppe werden immer verwendet.
* Ist in den Einstellungen der Aktivität **„Fragen mischen“** aktiv, wird zusätzlich die Reihenfolge aller Fragen
  zufällig festgelegt.
* Die Fragengruppe sollte **vor dem Start der Aktivität** festgelegt werden. Bei bereits gestarteten Versuchen werden
  fehlende Fragen beim nächsten Öffnen ergänzt; die schon gezogenen Fragen bleiben unverändert.

## Punkte

Die **Gesamtpunkte** der Aktivität zählen für eine Fragengruppe **Anzahl × Punkte der ersten Frage der Gruppe**.
Damit alle Schüler gleich viele Punkte erreichen können, sollten **alle Fragen einer Gruppe dieselbe Punktezahl** haben.

## Siehe auch

* [Beispiele zu Test hinzufügen](../BeispielezuTesthinzufügen/index.md)
* [Test anlegen](../Testanlegen/index.md)
* [Test-Ergebnisse](../Test-Ergebnisse/index.md)
