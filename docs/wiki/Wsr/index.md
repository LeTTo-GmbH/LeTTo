# Wsr
## Plugin WSR

Zeichnet lineare elektrische Schaltungen und liefert auch das mathematische Modell in Form von Maxima-Befehlen.

### Definition der Schaltung
#### Schaltungselemente
Die Schaltung wird im Plugindialog über einen String(Zeichenkette) definiert, wobei folgende Zeichen definiert sind:

| Name              | Bedeutung                                                    | Symbol                                                          |
|-------------------|--------------------------------------------------------------|-----------------------------------------------------------------|
| R                 | Widerstand                                                   | <br>![ClipCapIt-181123-103129.PNG](ClipCapIt-181123-103129.PNG) |
| Z                 | komplexe Impedanz von der Frequenz unabhängig                | <br>![ClipCapIt-181123-103129.PNG](ClipCapIt-181123-103129.PNG) |
| C                 | Kondensator                                                  | <br>![ClipCapIt-181123-103156.PNG](ClipCapIt-181123-103156.PNG) |
| L                 | Induktivität                                                 | <br>![ClipCapIt-181127-205320.PNG](ClipCapIt-181127-205320.PNG) |
| LL                | Leerlauf oder Unterbrechung                                  | <br>![ClipCapIt-181127-091706.PNG](ClipCapIt-181127-091706.PNG) |
| KS                | Drahtbrücke oder Kurzschluss                                 | <br>![ClipCapIt-181127-091730.PNG](ClipCapIt-181127-091730.PNG) |
| DB                | Drahtbrücke ohne besondere Funktion                          | <br>![ClipCapIt-181127-091730.PNG](ClipCapIt-181127-091730.PNG) |
| U                 | Spannungsquelle                                              | <br>![ClipCapIt-181127-091816.PNG](ClipCapIt-181127-091816.PNG) |
| UR                | Spannungsquelle in Rückwärtsrichtung                         | <br>![ClipCapIt-181127-091844.PNG](ClipCapIt-181127-091844.PNG) |
| UW                | Wechselspannungsquelle                                       | <br>![ClipCapIt-181127-091904.PNG](ClipCapIt-181127-091904.PNG) |
| UWR               | Wechselspannungsquelle in Rückwärtsrichtung                  | <br>![ClipCapIt-181127-092800.PNG](ClipCapIt-181127-092800.PNG) |
| BAT               | Batterie als Spannungsquelle                                 | <br>![ClipCapIt-181127-100455.PNG](ClipCapIt-181127-100455.PNG) |
| BATR              | Batterie als Spannungsquelle in Rückwärtsrichtung            | <br>![ClipCapIt-181127-100522.PNG](ClipCapIt-181127-100522.PNG) |
| I                 | Stromquelle                                                  | <br>![ClipCapIt-181127-100611.PNG](ClipCapIt-181127-100611.PNG) |
| IR                | Stromquelle in Rückwärtsrichtung                             | <br>![ClipCapIt-181127-100715.PNG](ClipCapIt-181127-100715.PNG) |
| A                 | Amperemeter                                                  | <br>![ClipCapIt-181127-100748.PNG](ClipCapIt-181127-100748.PNG) |
| AR                | Amperemeter in Rückwärtsrichtung                             | <br>![ClipCapIt-181127-100829.PNG](ClipCapIt-181127-100829.PNG) |
| V                 | Voltmeter                                                    | <br>![ClipCapIt-181127-100902.PNG](ClipCapIt-181127-100902.PNG) |
| VR                | Voltmeter in Rückwärtsrichtung                               | <br>![ClipCapIt-181127-103105.PNG](ClipCapIt-181127-103105.PNG) |
| Par(R,R)          | Parallelschaltung von zwei Widerständen                      | <br>![ClipCapIt-181127-103152.PNG](ClipCapIt-181127-103152.PNG) |
| Ser(R,R)          | Serienschaltung von zwei Widerständen                        | <br>![ClipCapIt-181127-103220.PNG](ClipCapIt-181127-103220.PNG) |
| B(R1,R2,R3,R4,R5) | Brückenschaltung von 5 Bauelementen                          | <br>![ClipCapIt-181127-103314.PNG](ClipCapIt-181127-103314.PNG) |
| B(R)              | Brückenschaltung von 5 Widerständen mit verschiedenen Werten | <br>![ClipCapIt-181127-103314.PNG](ClipCapIt-181127-103314.PNG) |


Die Verschaltung der Bauelement erfolgt über die folgenden Operatoren:

| Operator | Priorität | Bedeutung                                                                                                                                                      |
|----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *        | 15        | Parallelschaltung                                                                                                                                              |
| +        | 10        | Serienschaltung                                                                                                                                                |
| ?        |           | Wird nach einem Bauteil ein Fragezeichen gesetzt, so wird der Bauteil in der Angabe nicht angegeben und der Bauteilwert wird in der Schaltung nicht gezeichnet |


#### Zusammenschaltung von Zweipolen

| Schaltung                                                               | Bedeutung                                                | Beispiel           | Bild                                                            |
|-------------------------------------------------------------------------|----------------------------------------------------------|--------------------|-----------------------------------------------------------------|
| einzelner Zweipol als Serienschaltung                                   | Wird horizontal dargestellt und ohne Beistrich definiert | R+C                | <br>![ClipCapIt-181123-102901.PNG](ClipCapIt-181123-102901.PNG) |
| einzelner Zweipol als Parallelschaltung                                 | Wird horizontal dargestellt und ohne Beistrich definiert | R*C                | <br>![ClipCapIt-181127-210445.PNG](ClipCapIt-181127-210445.PNG) |
| senkrechter Zweipol                                                     | führt bei einigen Berechnungen noch zu Fehlern!          | ,R+C               | <br>![ClipCapIt-181123-103043.PNG](ClipCapIt-181123-103043.PNG) |
| Links offene Schaltung mit einer Eingangsspannung Ue und zwei Bauteilen | beginnt mit einem Komma                                  | ,R,C               | <br>![ClipCapIt-181127-210517.PNG](ClipCapIt-181127-210517.PNG) |
| Spannungsquelle mit zwei Bauteilen                                      |                                                          | U,R,C              | <br>![ClipCapIt-181127-210707.PNG](ClipCapIt-181127-210707.PNG) |
| Vierpol                                                                 |                                                          | ,R,C,,             | <br>![ClipCapIt-181127-210817.PNG](ClipCapIt-181127-210817.PNG) |
| Vierpol mit 3 Elementen                                                 |                                                          | ,R1,R2,R3,         | <br>![ClipCapIt-181127-210922.PNG](ClipCapIt-181127-210922.PNG) |
| Vierpol als T-Glied                                                     |                                                          | ,R1,R2,,R3,LL      | <br>![ClipCapIt-181127-211052.PNG](ClipCapIt-181127-211052.PNG) |
| Vierpol als Pi-Glied                                                    |                                                          | ,,R1,,R2,R3,,      | <br>![ClipCapIt-181127-211158.PNG](ClipCapIt-181127-211158.PNG) |
| Zweipol mit mehreren Elementen                                          |                                                          | ,R1,R2,R3,R4,R5,R6 | <br>![ClipCapIt-181127-211246.PNG](ClipCapIt-181127-211246.PNG) |


#### angezeigte Spannungen und Ströme
* Die angezeigten Ströme und Spannung können nach der Schaltungsdefinition durch einen Strichpunkt getrennt erfolgen. 
* Sie werden einfach durch Beistrich getrennt angegeben
Folgenden Definitionen sind hierbei möglich:

| Operator      | Beispiel | Bedeutung                                                                                                                                                        |
|---------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ohne Operator | UR1      | der Spannungspfeil für R1 wird gezeichnet                                                                                                                        |
| u             |          | alle Spannungs- und Strompfeile werden unterstrichen                                                                                                             |
| _             | UC1_     | Das Größensymbol wird in der Schaltung unterstrichen                                                                                                             |
| -             | Ue-      | Der Pfeil wird in der Schaltung nicht mehr gezeichnet                                                                                                            |
| !             | IC1!     | Der Absolutbetrag des berechneten Wertes wird zum Pfeil dazugeschrieben                                                                                          |
| ?             | UR1?     | Der Pfeil wird ohne Namen gezeichnet                                                                                                                             |
| &gt;          | UR1&gt;x | Der Index der Größe wird in Schaltung und Zeigerdiagramm ausgetauscht. In diesem Beispiel wird Ux statt UR1 geschrieben. In Maxima bleibt der Index unverändert. |
| :             | R1:Rx    | Ein Bauteilname kann umbenannt werden. Hier R1 auf Rx.                                                                                                           |

Die Operatoren _-!? können auch nach einer Änderung mit &gt; zusätzlich verwendet werden wie zB: UR4&gt;x!_ 
<br>![ClipCapIt-181127-212621.PNG](ClipCapIt-181127-212621.PNG)

#### Beispiele

| Definition                                        | Schaltung                                                                   |
|---------------------------------------------------|-----------------------------------------------------------------------------|
| ,R,C,,R,LL;IC1&gt;p,UR1!,Ua_,Ue-                  | <br>![ClipCapIt-181127-213036.PNG](ClipCapIt-181127-213036.PNG) |
| U,R,R,A;UR1,UR2,IR1&gt;1,IA1-                     | <br>![ClipCapIt-181127-213202.PNG](ClipCapIt-181127-213202.PNG) |
| U,R,R,A;UR1,UR2,IR1&gt;1,IA1-,A1:.,R2:Rx,URx&gt;x | <br>![ClipCapIt-181127-213502.PNG](ClipCapIt-181127-213502.PNG) |
| ,R,R;Ue?,Ie-,UR1?,UR2&gt;a                        | <br>![ClipCapIt-181127-213912.PNG](ClipCapIt-181127-213912.PNG) |
| ,R,C?,,                                           | <br>![300px-ClipCapIt-190322-142038.PNG](300px-ClipCapIt-190322-142038.PNG) |


### Datensätze
* Das Plugin erstellt automatisch beim Beenden des Plugin-Editors die benötigten Datensätze
* Für alle Bauteilwert darf aktuell nur ein reeller und kein komplexer Wert verwendet werden
* Für Bauteile kann man den zugehörigen Datensatz löschen und durch eine Berechnung in Maxima überschreiben (Der Datensatz wird aber dann aktuell jedesmal wenn man in den Plugin-Dialog wechselt neu angelegt -&gt; Bug)

### Verwendung des Plugins in der Frage
#### Einfügen von Angabewerten
Im Frageeditor kann man mit der rechten Maustaste und Plugin-Angabe die Angabe für alle generierten Datensätze in den Fragetext einfügen lassen.
<br>![ClipCapIt-181127-214344.PNG](ClipCapIt-181127-214344.PNG)
Wird später das Plugin verändert wird dieser Test **nicht automatisch** nachgeführt. Er muss dann entweder gelöscht und neu eingefügt, oder händisch angepasst werden.

Beispiel:

| Schaltung                                                       | Angabe                                               |
|-----------------------------------------------------------------|------------------------------------------------------|
| <br>![ClipCapIt-181127-214655.PNG](ClipCapIt-181127-214655.PNG) | $U_{Q1}={UQ1}$, $R_{1}={R1}$, $C_{1}={C1}$ , $f={f}$ |

#### Einfügen von Graphiken
Eine Graphik kann durch das Plugin-Tag 
<pre>
[PIG pluginname "typ parameter&#92;"/](PIG pluginname "typ parameter&#92;"/)
</pre>
im Fragetext eingefügt werden. Dies erfolgt entweder direkt über die Eingabe des Textes oder über die rechte Maustaste im Fragetext-Editor.

Folgende Parameter können angegeben werden:


| Graphiktyp     | typ parameter   | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Beispiel                                                             |
|----------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Schaltung      | keine Parameter |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | &#91;PIG plugin1&#93;                                              |
| Schaltung      | S W,w20         | W,werte..Werte der Bauteile drucken<br> w20..Breite in Prozent des Bildschirms<br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | &#91;PIG plugin1 "S W,w60&#92;"/&#93;       |
| Bodediagramm   | BODE UR1,W,w20  | erster Parameter ist die Ausgangs-Spannung oder der Ausgangs-Strom <br> weitere Parameter durch Komma getrennt<br> O..Frequenzachse Kreisfrequenz<br> B,BF..Betragsfrequenzgang mit Frequenzachse in Hz<br> BO..Betragsfrequenzgang mit Frequenzachse als Kreisfrequenz <br> W,WF..Winkelfrequenzgang mit Frequenzachse in Hz<br> WO..Winkelfrequenzgang mit Frequenzachse als Kreisfrequenz<br> w50..Breite in Prozent des Bildschirms                                                                                                                                                                                                                                                                                 | &#91;PIG plugin1 "bode UC2"/&#93;               |
| Zeigerdiagramm | ZD w40          | Parameter durch Komma getrennt<br> U Zeigerdiagramm der Spannungen<br> I Zeigerdiagramm der Ströme<br> UI Zeigerdiagramm der Ströme und Spannungen<br> UR1 erzwingt das Zeichnen der Spannung UR1<br> IC1 erzwingt das Zeichnen des Stromes IC1<br> u unterstreicht alle Ströme und Spannungen<br> UR1? zeichnet den Zeiger ohne Beschriftung<br> UR1/ die Beschriftung erfolgt auf der anderen Seite des Zeigers<br> UR2- Die Spannung wird nicht gezeichnet<br> P(UR1,UR2,IC1) nur die angegebenen Spannungen und Ströme werden gezeichnet<br> w50 Breite in Prozent des Bildschirms <br> noscale keine Angabe über die Größe der Spannungen und Ströme<br> nolegend keine Beschriftung der Spannungen und Ströme<br> | &#91;PIG plugin1 "zd UI,w50"/&#93;            |
| Ortskurve      | OK UC1,w20      | erster Parameter ist die Ausgangs-Spannung oder der Ausgangs-Strom <br> weitere Parameter durch Komma getrennt<br> w50..Breite in Prozent des Bildschirms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | &#91;PIG plugin1 "ok UC2,w40&#92;"/&#93; |

Bodediagramm und Ortskurve werden grundsätzlich als Verhältnis von 
angegebener Ausgangsspannung oder Ausgangsstrom zur Eingangsspannung
oder zum Eingangsstromg berechnet.<br>

#### Zeichenelemente des Plot-Plugins
Durch Strichpunkt getrennt können auch die [Zeichenelemente vordefinierte graphische funktionen](../Plot/index.md#vordefinierte-graphische-funktionen) des Plot-Plugins eingefügt werden.

Das Koordinatensystem des Bildschirmfensters hat den Nullpunkt links unten.

Die positive horizontale Achse geht von links nach rechts von 0 bis 100 und bei Schaltungen von 0 bis zur Schaltungsbreite wobei ein Widerstand eine Länge von 3 hat.

Die postitive vertikale Achse reicht unten nach oben und beginnt unten bei 0. Der maximale Wert ist abhängig vom Seitenverhältnis des Fensters.

Beispiele:

| Plugin-Definition | PIG-Tag                                                                                                      | Bild                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| ,R,R,,R,LL;Ia     | S w,w50;loop(2.5,1.5,0.6,tex="I");loop(7.5,1.5,0.6,tex="II");circle(5,4,0.3,color=red);text(5,4.7,tex="III") | <br>![200px-ClipCapIt-200603-133148.PNG](200px-ClipCapIt-200603-133148.PNG) |


#### Maximafeld
Im Maximafeld kann ein Satz von Berechnungsformeln für das Plugin über den Tag

<pre>
[pluginname/](PIM)
</pre>

automatische eingefügt werden. Dieses Tag kann auch über die rechte Maustaste im Maximafeld eingefügt werden. D
Das PIM-Tag wird vor der Maxima-Berechnung automatisch durch die Formeln des Plugins ersetzt.

Folgende Variablen werden im Maxima-Feld definiert und können für das Ergebnis 
verwendet werden:

| Variable | Beschreibung                                           | Ergebnistyp               |
|----------|--------------------------------------------------------|---------------------------|
| UR1      | Spannung am Widerstand R1                              | Polynombruch im s-Bereich |
| IC1      | Strom im Kondensator C1                                | Polynombruch im s-Bereich |
| cUS1     | Spannung an der Serienschaltung S1 als komplexe Zahl   | komplexe Zahl             |
| absUS1   | Absolutbetrag der komplexen Spannung US1               | double                    |
| argUP1   | Winkel der komplexen Spannung UP1                      | double                    |
| reUR1    | Realteil der komplexen Spannung UR1                    | double                    |
| imUC1    | Imaginärteil der komplexen Spannung UC1                | double                    |
| cSR1     | komplexe Scheinleistung am Bauteil R1                  | komplexe Zahl             |
| SR1      | Absolutbetrag der Scheinleistung am Bauteil R1         | double                    |
| argSR1   | Winkel der Scheinleistung am Bauteil R1                | double                    |
| PR1      | Wirkleistung am Bauteil R1                             | double                    |
| QR1      | Blindleistung am Bauteil R1                            | double                    |
| Zges     | Gesamtimpedanz wenn als Zweipol darstellbar            | Polynombruch in s         |
| Ue       | Gesamtspannung am Eingang eines Zweipols oder Vierpols | Polynombruch in s         |
| Ie       | Gesamtstrom am Eingang eines Zweipols oder Vierpols    | Polynombruch in s         |
| cZges    | komplexe Gesamtimpedanz                                | komplexe Zahl             |



[Plugins](../Plugins/index.md)

