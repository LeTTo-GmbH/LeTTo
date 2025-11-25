# Datensätze
[Datensätze definieren](../Datensätzedefinieren/index.md)

Datensatz ist in LeTTo ein Synonym für Variable. Diese können dazu verwendet werden, um Beispiele mit unterschiedlichen Zahlenwerten, durchgerechneten Images und alternativen Lösungen zu erstellen. 
Der [Lösungsweg der Beispiele](../Berechnungen/index.md) wird im Maxima-Eingabefeld definiert und führt zu einer geschlossenen mathematischen Lösung, in die dann zur Laufzeit des Tests Zahlenwerte eingesetzt werden, die in den Datensätzen definiert wurden. Bei der [Erstellung von Datensätzen](../Datensätzedefinieren/index.md) werden immer 40 Wertepaare erzeugt, die bei Tests dann zufällig zugewiesen werden.

## Verwendung von Variablen
Im Fragentext können Sie Variable verwenden, indem sie die Bezeichnung des Datensatzes in geschwungene Klammern setzen und den Parameter in der Parameterliste eintragen (rechte Maustaste auf die Datensatzdefinitionen --&gt; Datensatz einfügen):
  {R1} im Fragetext wird durch einen Zahlenwert in der tatsächlichen Angabe für den Schüler ersetzt
R1 wurde zB. mit E12:1k-10k, Ohm definiert: R1 kann damit Werte aus der Normreihe E12 im Wertebereich von 1kOhm bis 10kOhm annehmen.
Details zur Definition von Datensätzen finden Sie [hier](../Datensätzedefinieren/index.md). 

Datensätze können immer als physikalische Größen mit Einheiten verwendet werden. In der Berechnung ist das komplette SI-Einheitensystem verfügbar.
**Wichtig:** Alle Datensätze liegen immer in SI-Einheiten vor, auch wenn die Eingabe nicht so erfolgte:
Eingabe von 
  t: I1-10, h =&gt; liefert Datensätze mit Werten zwischen 3600s bis 36000s. 
Dadurch muss bei der Berechnung nicht mehr auf Einheiten Rücksicht genommen werden.

### Darstellung von Variablen mit Einheiten
Hat der Datensatz eine [Einheit](../Einheit/index.md), dann wird bei der Ersetzung der geschwungenen Klammern automatisch der Zahlenwert mit SI-Einheit in der optimalen Darstellungsform ausgegeben:
  0.0012m werden als 1.2mm dargestellt.

#### Erzwingen von Einheiten
Sollen andere Einheitenvielfache oder andere Dimensionen angezeigt werden, kann folgende Variablendefinition verwendet werden:
  {t;=h} : Diese Definition bewirkt, dass die Zeit in Stunden angegeben wird.
Verwendung: Nach dem Variablennamen, getrennt durch einen Beistrich, wird mit dem Istgleichzeichen die geforderte _Zieleinheit_ definiert. Die korrekte Umrechnung der Werte erfolgt automatisch.

### Referenzierung von Werten aus der Lösung
Sie können in der Angabe auch auf alle Berechnungsschritte des Lösungswegs zugreifen oder auf im Lösungsweg definierte Formeln:
  _Im Maxima-Feld wurde definiert:_
  erg:noopt( x+y/(3*x+2*y) )

Mit folgender Definition wird nun die Formel in der Angabe korrekt referenziert:
  {=:erg}

Wenn nach der geschwungenen Klammer ein Istgleichzeichen folgt, dann wird kein Datensatz zum Einsetzen verwendet, sondern ein Berechnungsschritt aus der Lösungsdefinition. Die [Funktion](../Funktionen/index.md) **noopt** dient dazu, dass eine Formel nicht vereinfacht wird und unverändert übernommen wird.

Der Doppelpunkt bewirkt, dass beim Einsetzen der Werte keine weiteren Vereinfachungen bzw. Berechnungen erfolgen.
* {=2+3} liefert in der Angabe den Wert 5
* {=:2+3} liefert in der Angabe 2+3

