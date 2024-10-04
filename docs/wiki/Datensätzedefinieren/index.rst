Siehe auch [[Datensätze|Einführung zu Datensätzen]], [[Editor für den Angabetext#Datensätze und Variable]]

Jede Variable, die im Angabetext in geschwungenen Klammern eingesetzt werden kann, wird über einen Datensatz definiert.

==Erstellung aus dem [[Editor für den Angabetext|Editor]]==
Wenn im Text der Frage in geschwungenen Klammern eine Variablenbezeichnung verwendet wird, dann ist die Variable mit Klick der rechten Maustaste --&gt; '''Datensatz einfügen'''
:[[Datei:ClipCapIt-200304-202515.PNG]]
vom Benutzer anzulegen.

'''TIPP:''' 
Drücken Sie im Fragentext unmittelbar nach dem Variablennamen die '''F2'''-Taste. Es wird die Variable in geschwungenen Klammern gesetzt und der Datensatz in der Datensatzliste angelegt. Aus der Variabel x wird {x}.

Drücken Sie im Fragentext unmittelbar nach dem Variablennamen die '''F3'''-Taste wird die Variable ebenfalls in geschwungenen Klammern gesetzt und der Datensatz in der Datensatzliste angelegt. Der Fragentext wird um die Mathematikmodusdarstellung von LaTeX ergänzt. Aus der Variabel x wird $x={x}$.

Aus dem Variablennamen wird laut SI-Einheitensystem die entsprechende SI-Einheit zugeordnet.
Die Wertebereiche und die Einheiten können aber in jeder [[Ordnerverwaltung|Kategorie]] eigens definiert und überschrieben werden.

==Erstellung / Änderung über den Datensatz-Bereich==
:[[Datei:ClipCapIt-180620-222938.PNG|250px]]
:[[Datei:ClipCapIt-180831-181125.PNG|thumb|120px|Kontext-Menü der Datensatz-Tabelle]]
Die Tabelle zur Definition der Datensätze enthält drei Spalten:
* DS: Name der Variable
* Werte: Definition des Wertebereiches und des Types der Variable
* EH: Einheit der Variable

Über das Kontext-Menüs (rechte Maustaste) dieser Datensatz-Tabelle können auch neue Variablen hinzugefügt und bestehende gelöscht werden. Weiters können auch Datensätze mit vordefinierten Werten aus einer Datei importiert werden.
:[[Datei:ClipCapIt-180831-181504.PNG|400px]]

==Name der Variablen (Datensatz-Name)==

Folgende Namenskonventionen sind für die Variablenbezeichnung einzuhalten:
* Der Namen muss mit einem Buchstaben beginnen.
* Datensätze dürfen keine Sonderzeichen enthalten!
* Erlaubt sind Zeichen, Ziffern und der Unterstrich _

==Definition der Werte==

Es gibt zwei Varianten einen Wertebereich zu definieren:

* Nur durch die Angabe eines gültigen Bereiches:  zB.:1-10,E12:1k-10k
* Durch einen Typbezeichner gefolgt von einem gültigen Bereich:   zB.: C:1-10

Folgende Typbezeichner sind möglich:

{| class="wikitable"
|  Bezeichner 	||  Beschreibung 	||    Beispiel
|-
|  I:           ||  Ganzzahl 	||  I:10-20
|-
| V[Dimension]: ||  Vektor      ||  V3:1-10
|-
| M[Zeilen]x[Spalten]: || Matrix der Dimension [Zeilen]x[Spalten]  ||  M3x3:1-10
|-
| M[Dimension]: || Matrix der Dimension [Dimension]x[Dimension] mit einer Determinante ungleich Null ||  M3:1-10
|-
| P[Grad]:      ||  Polynom der Ordnung [Grad] in der Variablen s '''Noch nicht realisiert''' ||  P3:1-10
|-
| B[Zählergrad],[Nennergrad]: 	||  Polynombruch in der Variablen s mit definiertem Zählergrad und Nennergrad '''Noch nicht realisiert''' ||  B2,3:1-20
|-
| C: 	        || komplexe Zahl mit zufälligem Winkel zwischen 0° und 360°    || C:1-10
|-
|               || komplexe Zahl mit Betrag und Winkel in Grad                 || C:1-10arg10-90
|-
|               || komplexe Zahl mit Realteil und Imaginärteil (j als imaginäre Einheit)	               || C:1-10j1-10
|-
|               || komplexe Zahl mit Realteil und Imaginärteil 	    (i als imaginäre Einheit)	           || C:1-10i1-10
|-
| F[ziffern]: 	|| Gleitkommazahl mit einer definierten Anzahl gültiger Ziffern || F3:5-9
|-
| [ziffern]: 	|| Gleitkommazahl aus einem Bereich mit einer definierten Anzahl von äquidistanten Werten || 5:2-9
|-
| S: 	        || Zeichenketten durch Beistrich getrennt. Ein Beistrich muss mit einem Backslash verblockt werden!|| S:rot,grün,blau
|-
| R: 	        || Regulärer Ausdruck: Erzeugt einen String auf den der reguläre Ausdruck trifft. || R:[a-m]x?[^B]+
|-
| R[stellen]: 	|| Regulärer Ausdruck erzeugt einen String mit "stellen" Zeichen || R5:.+
|-
| R[minstellen]-[maxstellen]: || Regulärer Ausdruck mit einen Stellenanzahl von "minstellen" bist "maxstellen" || R5-8:[a-z]+\d+
|-
| sI:wert,wert,wert || erzeugt Ganzzahl-Datensätze aus den angegebenen Werten, wobei die Reihenfolge der Werte wie angegeben beibehalten wird! (Zahlenbereiche sind hier nicht erlaubt!!) || sI:5,78,2,-5,4
|-
| sF:wert,wert,wert || erzeugt Gleitkomma-Datensätze aus den angegebenen Werten, wobei die Reihenfolge der Werte wie angegeben beibehalten wird! (Zahlenbereiche sind hier nicht erlaubt!!) || sF:34.5,3.4,6,5,-43.4
|-
| sS:wert,wert,wert || erzeugt String-Datensätze aus den angegebenen Werten, wobei die Reihenfolge der Werte wie angegeben beibehalten wird! (Zahlenbereiche sind hier nicht erlaubt!!) Ein Beistrich muss mit einem Backslash verblockt werden! || sS:Hut,Kappe,Hose
|-
| Startwert:Schrittweite:Endwert || erzeugt Werte zwischen Startwert und Endwert mit einem Abstand von Schrittweite zwischen den Werten || 2:0.1:5
|}
	
===Bereichsdefinitionen===
Folgende Bereichsdefinitionen sind möglich:
	
{| class="wikitable"
| Beschreibung    ||	Beispiel
|-
| Zahl            ||	45
|-
| Zahl mit Einheitenvielfachen ||	15k
|-
| mehrere Zahlen, durch Beistrich getrennt ||  34,15k,24.4m
|-
| Zahlenbereich mittels Bindestrich  ||	3-15
|-
| Ganzzahl-Bereiche     || I3-15
|-
| Eine bestimmte Anzahl von Werten aus einem Zahlenbereich ||	13:45-130
|-
| Werte einer arithmetischen Folge ||	2:3:15 || 2,5,8,11,14
|-
| Werte einer geometrischen Folge ||	3*2:100 || 3,6,12,24,48,96
|-
| Normreihe 	        || E12:10k-80k || 10k,12k,15k,22k,27k,33k,39k,47k,56k,68k
|-
| Dezimale Reihe 	|| D2:10-600 || 10,50,100,500
|}

Mögliche Normreihen mit logarithmisch verteilten Werten pro Dekade: E3,E6,E12,E24,E48

Mögliche dezimale Reihen mit gleicheverteilten Werten pro Dekade: D2, D5, D10, D20, D40

Mögliche Einheitenvielfache: m,u,n,p,f,a,k,M,G,T

==Einheiten==

* Als [[Einheit]] kann jede gültige SI Einheit angegeben werden
* Beginnt die Einheit mit einem Gleichheitszeichen, so wird die Einheit bei der Darstellung der Variable in der angegebenen Form und mit dem angegebenen Prefix erzwungen.
* Als Sondereinheiten sind zulässig
{| class="wikitable"
|    dB  || Dezibel
|+
|    % 	 || Prozent
|+
|    ppm || parts per million
|+
|    ° 	 || Grad
|+
|    € 	 || Euro
|+
|    $ 	 || Dollar
|}

* Bei komplexen Zahlen kann durch Beistrich getrennt die Darstellung der komplexen Zahl definiert werden. Folgende Darstellungsvarianten sind zulässig:
{| class="wikitable"
|    karti 	|| karthesische Darstellung mit "i" als komplexen Operator (1+2i)
|+
|    kartj 	|| karthesische Darstellung mit "j" als komplexen Operator (1+2j)
|+
|    poldeg 	|| Polarkoordinaten Darstellung in Grad 2arg30°
|+
|    polrad 	|| Polarkoordinaten Darstellung in Radianten 2arg0.2
|+
|    polideg 	|| Exponentialdarstellung mit "i" als komplexen Operator und Winkel in Grad 1*e^20°i
|+
|    polirad 	|| Exponentialdarstellung mit "i" als komplexen Operator und Winkel in Radiant 1*e^0.2i
|+
|    poljdeg 	|| Exponentialdarstellung mit "j" als komplexen Operator und Winkel in Grad 1*e^20°j
|+
|    poljrad 	|| Exponentialdarstellung mit "j" als komplexen Operator und Winkel in Radiant 1*e^0.2j
|}

