# Punkte-Mengen-Funktionen

[Zurück zu Berechnungen](../../index.md) · [Alle Funktionen](../index.md)

| Funktion | Beschreibung |
| --- | --- |
| [pvabs](pvabs/index.md) | Bestimmt den Betrag eines Punktes oder aller Ortsvektoren zu den Punkten. DEMO-Beispiel |
| [pvarg](pvarg/index.md) | Bestimmt den Winkel eines Punktes oder aller Ortsvektoren zu den Punkten. DEMO-Beispiel |
| [pvcompare](pvcompare/index.md) | Vergleicht einen Referenz-Linienzug mit einem eingegebenen Linienzug unter Berücksichtigung der Toleranz. Die Toleranz stellt eine relative Tolerenz bezogen auf den Bereich zwischen MinXY und MaxXY da, wobei eine Toleranz von 0.1 gleichbedeutend 10 Prozent bezogen auf Max-Min ist (Mit dem String "a0.1" könnte man auch ein absolute Toleranz von 0.1 für x und y realisieren)  pvcompare(Referenz,Eingabe) pvcompare(Referenz,Eingabe,Toleranz) pvcompare(Referenz,Eingabe,MinX,MaxX,MinY,MaxY)  pvcompare(Referenz,Eingabe,MinX,MaxX,MinY,MaxY,Toleranz) DEMO-Beispiel |
| [pvdistance](pvdistance/index.md) | Bestimmt die Abstände als Vektoren zwischen den Punkten. pvdistance([A,B,C]) liefert [AB,BC,CA] DEMO-Beispiel |
| [pvequals](pvequals/index.md) | Prüft ob zwei Punktevektoren gleich sind. Die Genauigkeit wird als dritter Parameter angegeben, oder bei einem Antwortfeld von der Antworttoleranz genommen. Prozentangaben der Genauigkeit beziehen sich auf die Breite bzw. Höhe des Punktefeldes im karthesischen Koordinatensystem. DEMO-Beispiel |
| [pvforeachline](pvforeachline/index.md) | Führt für jedes Punktepaar eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion DEMO-Beispiel |
| [pvfunc](pvfunc/index.md) | Erzeugt aus einer Funktionen in einer Variablen (x-Achse) eine Punktmatrix der Funktionswerte (y-Achse). pvfunc(funktion,variable,minx,maxx,deltax) DEMO-Beispiel |
| [pvget](pvget/index.md) | Liefert einen Punkt der Punkteliste. DEMO-Beispiel |
| [pvgetx](pvgetx/index.md) | Bestimmt die x-Koordinate eines Punktes oder aller Punkte. DEMO-Beispiel |
| [pvgety](pvgety/index.md) | Bestimmt die y-Koordinate eines Punktes oder aller Punkte. DEMO-Beispiel |
| [pvhasline](pvhasline/index.md) | Prüft ob sich eine Linie innerhalb des Punktefeldes von Linien befindet. Die Genauigkeit kann wie bei pvequals als dritter Parameter angegeben werden. DEMO-Beispiel |
| [pvhaspoint](pvhaspoint/index.md) | Prüft ob sich ein Punkt innerhalb des Punktefeldes befindet. Die Genauigkeit kann wie bei pvequals als dritter Parameter angegeben werden. DEMO-Beispiel |
| [pvinsert](pvinsert/index.md) | Fügt einen Punkt in die Punktemenge ein DEMO-Beispiel |
| [pvinsertlast](pvinsertlast/index.md) | Fügt am Ende der Punktemenge einen Punkt ein DEMO-Beispiel |
| [pvline](pvline/index.md) | Bestimmt die Geradengleichung einer Geraden durch das n-te Punktepaar DEMO-Beispiel |
| [pvlineabs](pvlineabs/index.md) | Bestimmt aus dem n-ten Punktepaar den Absolutbetrag des Abstandes. DEMO-Beispiel |
| [pvlinearg](pvlinearg/index.md) | Bestimmt aus dem n-ten Punktepaar den Winkel der Strecke zur x-Achse DEMO-Beispiel |
| [pvlined](pvlined/index.md) | Bestimmt den Schnittpunkt einer Geraden durch das n-te Punktepaar mit der y-Achse DEMO-Beispiel |
| [pvlinek](pvlinek/index.md) | Bestimmt die Steigung der zugehörigen Geraden dem n-ten Punktepaar DEMO-Beispiel |
| [pvlines](pvlines/index.md) | Bestimmt die Anzahl der Linien bzw. Punktepaare eines Punktevektors. |
| [pvpoints](pvpoints/index.md) | Bestimmt die Anzahl der Punkte DEMO-Beispiel |
| [pvrect](pvrect/index.md) | Liefert aus einer Punktewolke ein Rechteck als zwei Eckpunkte links-unten und rechts-oben. |
| [pvremove](pvremove/index.md) | Löscht einen Punkt aus der Punktemenge DEMO-Beispiel |
| [pvsort](pvsort/index.md) | Sortiert die Punkte zuerst nach steigender x-Koordinate und bei gleicher x-Koordinate nach steigender y-Koordinate. |
| [pvsortabs](pvsortabs/index.md) | Sortiert die Punkte nach steigendem Absolutbetrag des Ortsvektors DEMO-Beispiel |
| [pvsortarg](pvsortarg/index.md) | Sortiert die Punkte nach steigendem Winkel des Ortsvektors (-pi bis pi) DEMO-Beispiel |
| [pvsortlineabs](pvsortlineabs/index.md) | Sortiert Punktepaare nach steigendem Betrag der Linienlänge. DEMO-Beispiel |
| [pvsortlinearg](pvsortlinearg/index.md) | Sortiert Punktepaare nach steigendem Winkel der Linienrichtung. DEMO-Beispiel |
| [pvsortlinex](pvsortlinex/index.md) | Sortiert Punktepaare nach steigender x-Koordinate der kleineren x-Koordinate des Paares. DEMO-Beispiel |
| [pvsortliney](pvsortliney/index.md) | Sortiert Punktepaare nach steigender y-Koordinate der kleineren y-Koordinate des Paares. DEMO-Beispiel |
| [pvsortx](pvsortx/index.md) | Sortiert die Punkte nach steigender x-Koordinate DEMO-Beispiel |
| [pvsorty](pvsorty/index.md) | Sortiert die Punkte nach steigender y-Koordinate DEMO-Beispiel |
| [pvunion](pvunion/index.md) | hängt mehrere Punktevektoren zu einem größereren Punktevektor zusammen DEMO-Beispiel |
| [pvvect](pvvect/index.md) | Bestimmt einen Vector aus dem n-te Punktepaar DEMO-Beispiel |
