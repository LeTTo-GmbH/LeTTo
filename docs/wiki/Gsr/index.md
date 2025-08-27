# Gsr
## Plugin GSR

* Zeichnet lineare elektrische Schaltungen für Gleichspannung.
* Besteht die Schaltung nur aus linearen Elementen, dann liefert das Plugin auch das mathematische Modell in Form von Maxima-Befehlen.

siehe auch: [Plugins](../Plugins/index.md)

### Definition der Schaltung
#### Schaltungselemente
Die Schaltung wird im Plugindialog über einen String(Zeichenkette) definiert, wobei folgende lineare Bauteile definiert sind:

| Name              | Bedeutung                                                    | Symbol                                                          |
|-------------------|--------------------------------------------------------------|-----------------------------------------------------------------|
| R                 | Widerstand                                                   | <br>![ClipCapIt-181123-103129.PNG](ClipCapIt-181123-103129.PNG) |
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


Folgende Bauteile, welche nicht mit Maxima berechnbar sind, sind ebenfalls definiert:

| Name | Bedeutung                       | Symbol                                                          |
|------|---------------------------------|-----------------------------------------------------------------|
| D    | Diode                           | <br>![ClipCapIt-190220-101437.PNG](ClipCapIt-190220-101437.PNG) |
| DR   | Diode in Rückwärtsrichtung      | <br>![ClipCapIt-190220-101453.PNG](ClipCapIt-190220-101453.PNG) |
| ZD   | Zenerdiode                      | <br>![ClipCapIt-190220-101512.PNG](ClipCapIt-190220-101512.PNG) |
| ZDR  | Zenerdiode in Rückwärtsrichtung | <br>![ClipCapIt-190220-101527.PNG](ClipCapIt-190220-101527.PNG) |
| LED  | LED                             | <br>![ClipCapIt-190220-101538.PNG](ClipCapIt-190220-101538.PNG) |
| LEDR | LED in Rückwärtsrichtung        | <br>![ClipCapIt-190220-101552.PNG](ClipCapIt-190220-101552.PNG) |
| Lamp | Glühbirne                       | <br>![ClipCapIt-190220-101611.PNG](ClipCapIt-190220-101611.PNG) |
| X    | Glühbirne                       | <br>![ClipCapIt-190220-101611.PNG](ClipCapIt-190220-101611.PNG) |
| NTC  | NTC-Widerstand                  | <br>![ClipCapIt-190220-101631.PNG](ClipCapIt-190220-101631.PNG) |
| PTC  | PTC-Widerstand                  | <br>![ClipCapIt-190220-101643.PNG](ClipCapIt-190220-101643.PNG) |
| VDR  | VDR-Widerstand                  | <br>![ClipCapIt-190220-101658.PNG](ClipCapIt-190220-101658.PNG) |
| S    | Schalter als Schließer          | <br>![ClipCapIt-190220-101721.PNG](ClipCapIt-190220-101721.PNG) |
| O    | Schalter als Öffner             | <br>![ClipCapIt-190220-101709.PNG](ClipCapIt-190220-101709.PNG) |


Die Verschaltung der Bauelement erfolgt über die folgenden Operatoren:

| Operator | Priorität | Bedeutung         |
|----------|-----------|-------------------|
| *        | 15        | Parallelschaltung |
| +        | 10        | Serienschaltung   |


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

| Operator      | Beispiel | Bedeutung                                                                                                                                  |
|---------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ohne Operator | UR1      | der Spannungspfeil für R1 wird gezeichnet                                                                                                  |
| _             | UR1_     | Das Größensymbol wird in der Schaltung unterstrichen                                                                                       |
| -             | Ue-      | Der Pfeil wird in der Schaltung nicht mehr gezeichnet                                                                                      |
| !             | IR1!     | Der berechneten Wert wird zum Pfeil dazugeschrieben. Die Wert ist nur verfügbar, wenn er auch im Maxima-Feld berechnet wurde!              |
| ?             | UR1?     | Der Pfeil wird ohne Namen gezeichnet                                                                                                       |
| &gt;          | UR1&gt;x | Der Indizes der Größe wird ausgetauscht. In diesem Beispiel wird Ux statt UR1 geschrieben. In Maxima bleibt der Index unverändert.         |
| :             | R1:Rx    | Ein Bauteilname kann umbenannt werden. Hier R1 auf Rx. Dies hat keinen Einfluss auf die Maxima-Berechnung, hier bleibt der Namen erhalten. |

Die Operatoren _-!? können auch nach einer Änderung mit &gt; zusätzlich verwendet werden wie zB: UR4&gt;x!_ 
<br>![ClipCapIt-181127-212621.PNG](ClipCapIt-181127-212621.PNG)

#### Beispiele

| Definition                                        | Schaltung                                                       |
|---------------------------------------------------|-----------------------------------------------------------------|
| U,R,R,A;UR1,UR2,IR1&gt;1,IA1-                     | <br>![ClipCapIt-181127-213202.PNG](ClipCapIt-181127-213202.PNG) |
| U,R,R,A;UR1,UR2,IR1&gt;1,IA1-,A1:.,R2:Rx,URx&gt;x | <br>![ClipCapIt-181127-213502.PNG](ClipCapIt-181127-213502.PNG) |
| ,R,R;Ue?,Ie-,UR1?,UR2&gt;a                        | <br>![ClipCapIt-181127-213912.PNG](ClipCapIt-181127-213912.PNG) |


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

| Schaltung                                                       | Angabe                                     |
|-----------------------------------------------------------------|--------------------------------------------|
| <br>![ClipCapIt-181127-214655.PNG](ClipCapIt-181127-214655.PNG) | $U_{Q1}={UQ1}$, $R_{1}={R1}$, $C_{1}={C1}$ |

#### Einfügen von Graphiken
Eine Graphik kann durch das Plugin-Tag 
<pre>
[PIG pluginname "typ parameter"/](PIG pluginname "typ parameter"/)
</pre>
im Fragetext eingefügt werden. Dies erfolgt entweder direkt über die Eingabe des Textes oder über die rechte Maustaste im Fragetext-Editor.

Folgende Parameter können angegeben werden:


| Graphiktyp | typ parameter   | Beschreibung                                                                       | Beispiel                                         |
|------------|-----------------|------------------------------------------------------------------------------------|--------------------------------------------------|
| Schaltung  | keine Parameter |                                                                                    | [PIG plugin1]                                    |
| Schaltung  | S W,w20         | W,werte..Werte der Bauteile drucken<br> w20..Breite in Prozent des Bildschirms<br> | [PIG plugin1 "S W,w60"/](PIG plugin1 "S W,w60"/) |


#### Zeichenelemente des Plot-Plugins
Durch Strichpunkt getrennt können auch die [Zeichenelemente](../Plot/index.md#vordefinierte-graphische-funktionen-) des Plot-Plugins eingefügt werden.

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

automatische eingefügt werden. Dieses Tag kann auch über die rechte Maustaste im Maximafeld eingefügt werden.
Das PIM-Tag wird vor der Maxima-Berechnung automatisch durch die Formeln des Plugins ersetzt.

Folgende Variablen werden im Maxima-Feld definiert und können für das Ergebnis 
verwendet werden:

| Variable | Beschreibung                                                    |
|----------|-----------------------------------------------------------------|
| UR1      | Spannung am Widerstand R1                                       |
| IC1      | Strom im Kondensator C1                                         |
| Rges     | Gesamtwiderstand wenn die Schaltung als Zweipol darstellbar ist |
| Ue       | Gesamtspannung am Eingang eines Zweipols oder Vierpols          |
| Ie       | Gesamtstrom am Eingang eines Zweipols oder Vierpols             |


Werden in der Schaltung **Induktivitäten oder Kapazitäten** verwendet werden alle Ströme und Spannungen im Laplace-Bereich 
und im Gleichstromarbeitspunkt berechnet.

| Variable | Beschreibung                                                   | Ergebnistyp          |
|----------|----------------------------------------------------------------|----------------------|
| UR1      | Spannung am Widerstand R1 im Laplace-Bereich als Funktion in s | Übertragungsfunktion |
| IC1      | Strom im Kondensator C1 im Laplace-Bereich als Funktion in s   | Übertragungsfunktion |
| dcUR1    | Gleichspannung am Widerstand R1 im Arbeitspunkt                | Gleichspannung       |
| dcIL1    | Gleichstrom in der Induktivität L1 im Arbeitspunkt             | Gleichstrom          |


Werden in der Schaltung **Schalter** verwendet, so werden alle notwendigen Größen für **Schaltvorgänge** berechnet.

| Variable | Beschreibung                                                                                     | Ergebnistyp          |
|----------|--------------------------------------------------------------------------------------------------|----------------------|
| dcUR1    | Gleichspannung am Widerstand R1 vor der Betätigung des Schalters                                 | Gleichspannung       |
| UR1      | Spannung am Widerstand R1 vor dem Betätigen des Schalters im Laplace-Bereich als Funktion von s  | Übertragungsfunktion |
| npUR1    | Spannung am Widerstand R1 direkt nach dem Betätigen des Schalters                                | Momentanwert         |
| infUR1   | Gleichspannung am Widerstand R1 nach unendlich langer Zeit nach dem Betätigung des Schalters     | Gleichspannung       |
| sUR1     | Spannung am Widerstand R1 nach dem Betätigen des Schalters im Laplace-Bereich als Funktion von s | Übertragungsfunktion |


[Plugins](../Plugins/index.md)

