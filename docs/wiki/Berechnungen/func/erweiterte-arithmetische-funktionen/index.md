# erweiterte arithmetische Funktionen

[Zurück zu Berechnungen](../../index.md) · [Alle Funktionen](../index.md)

| Funktion | Beschreibung |
| --- | --- |
| [cnewton](cnewton/index.md) | Bestimmt eine komplexe Nullstelle einer Funktion nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der komplexe Startwert. DEMO-Beispiel |
| [cnewtonall](cnewtonall/index.md) | Bestimmt alle komplexen Nullstellen einer Funktion mit einem Betrag des Funktionsparameters kleiner als ein definierter Wert nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der maximale Betrag des Funktionsparameters. Das Ergebnis ist immer ein Vektor mit den Nullstellen. DEMO-Beispiel |
| [interpol](interpol/index.md) | Interpolationsfunktion zwischen mehreren Stützpunkten in einem Koordinatensystem.  interpol(WerteX,WerteY,x) DEMO-Beispiel |
| [newton](newton/index.md) | Bestimmt eine Nullstelle einer Funktion nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der Startwert. DEMO-Beispiel |
| [newtonall](newtonall/index.md) | Bestimmt alle Nullstellen einer Funktion mit einem Betrag des Funktionsparameters kleiner als ein definierter Wert nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der maximale Betrag des Funktionsparameters. Das Ergebnis ist immer ein Vektor mit den nach aufsteigendem Funktionswert sortierten Nullstellen. DEMO-Beispiel |
| [numdif](numdif/index.md) | numerisches Differenzieren einer Funktion "funktion" nach einer Variablen "Variable" an der Stelle "position" mit einer Differenz der Variablen von "differenz"  numdif(position,funktion,Variable,differenz) DEMO-Beispiel |
| [numint](numint/index.md) | numerische Integration  numint(untereGrenze,obereGrenze,funktion,Variable) numint(untereGrenze,obereGrenze,funktion,Variable,punkteAnzahl) DEMO-Beispiel |
| [periodic](periodic/index.md) | Erzeugt aus einer beliebigen Funktion zwischen 0 und Periodendauer eine periodische Funktion  periodic(Variable,Periodendauer,Funktion) periodic(Variable,Periodendauer,Funktionsperiodendauer,Funktion) DEMO-Beispiel |
| [pulse](pulse/index.md) | Rechteckfunktion: pulse(x,x0) ist gleich 1 für x0 < x < x0 + 1, sonst 0pulse(x,x0,L) ist gleich 1 für x0 < x < x0 + L, sonst 0!300px-Pulse.png DEMO-Beispiel |
| [ramp](ramp/index.md) | Rampenfunktion: ramp(x,x0) Rampe von x0 < x < x0 + 1ramp(x,x0,L) Rampe von x0 < x < x0 + L!300px-Funktion_ramp.png DEMO-Beispiel |
| [sigma](sigma/index.md) | Sprungfunktion: sigma(x) liefert 0 für x<0 und 1 für x>=0 DEMO-Beispiel |
| [solve](solve/index.md) | löst eine Gleichung oder ein Gleichungssystem nach einer oder mehrerer Variablen DEMO-Beispiel |
| [solvevalue](solvevalue/index.md) | löst eine Gleichung oder ein Gleichungssystem nach einer Variablen und liefert genau die erste Lösung wenn sie numerisch berechenbar ist DEMO-Beispiel |
