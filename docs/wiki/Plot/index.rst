Das Plot-Plugin dient zum Zeichnen von beliebigen Funktionsgraphen:
= Parameter-String =
* Der Parameter-String enthält alle Funktionen die geplottet werden sollen und Parameter, welche für alle Diagramme definiert werden sollen.
* Funktionen und Parameter sind durch '''Strichpunkt''' getrennt.
* Konfigurationsparameter können im Parameter-String oder im PIG-Tag angegeben werden

== normaler Funktionsplot (function) ==
Der Parameter '''function''' muss nicht angegeben werden, da er die Standardeinstellung für Plot ist.

mögliche Funktionsdefinitionen:
{| class="wikitable" style="text-align: left; width: 100%;" 
| Funktion || Beschreibung || Beispiel || Graph
|-
| f(x):= ''{Funktion in x}'' || Funktion in einer Variablen || f(x):=x^2 || 
:[[Datei:ClipCapIt-190416-172659.PNG|100px]]
|- 
| f(t):=[''{Funktion x(t)}'',''{Funktion y(t)}''] || parametrische Funktion || f(t):=[2*sin(t),2*cos(t)];t:0,2pi || 
:[[Datei:ClipCapIt-190416-172623.PNG|100px]]
|-
| f(x,y):=[[''{x1}'',''{y1}''],[''{x2}'',''{y2}''],...] || Linienzug aus Stützpunkten  || f(x,y):=[[0,0],[1,1],[2,0]] ||
:[[Datei:ClipCapIt-190416-172512.PNG|100px]]
|-
| f(x,y):=[''{x}'',''{y}''] || Punkt || f(x,y):=[3,4] || 
:[[Datei:ClipCapIt-190416-172349.PNG|100px]]
|-
| f(x,y):= ''{boolsche Funktion in x und y}'' || implizit deklarierte Funktion muss auf der rechten Seite ein boolsches Ergebnis haben! || f(x,y):=x*y&lt;3 || 
:[[Datei:ClipCapIt-190416-172124.PNG|100px]]
|-
| f(x,y):=''{Zeichenelement}''(''{Koordinaten durch Komma getrennt}'',''{parameter}''=''{wert}'') '''oder'''&lt;br&gt; ''{Zeichenelement}''(''{Koordinaten durch Komma getrennt}'',''{parameter}''=''{wert}'') || Zeichnet vordefiniert graphische Funktionen wie Linen,Punkte,Kreise,etc. || f(x,y):=line(1,3,5,-3,color=red,points,text=abc) '''oder'''&lt;br&gt; line(1,3,5,-3,color=red,points,text=abc) || 
:[[Datei:ClipCapIt-200507-075942.PNG|100px]]
|-
|}

=== Füllungen zwischen Graphen ===

Füllbereiche können zwischen zwei Funktionen eingefügt werden. 

Syntax:
{| class="wikitable" style="text-align: left; width: 100%;" 
| Füllungsdefinition|| Beschreibung || Beispiel || Graph
|-
| fill:''{Funktion1}'' '''&gt;''' ''{Funktion2}'' || Füllung des Bereichs wo die Funkion1 größer als die Funktion2 ist || y(x):=-0.1*x^2+7;y(x):=0.2*x+1;'''fill:ch1&gt;ch2,color=green''' || :[[Datei:ClipCapIt-190420-123342.PNG|100px]]
|-
| fill:''{Funktion1}'' '''&lt;''' ''{Funktion2}'' || Füllung des Bereichs wo die Funkion1 kleine als die Funktion2 ist || y(x):=-0.1*x^2+7;y(x):=0.2*x+1;'''fill:ch1&lt;ch2,color=green''' || :[[Datei:ClipCapIt-190420-123533.PNG|100px]]
|-
| fill:''{Funktion1}'' '''-''' ''{Funktion2}'' || Füllung des Bereichs zwischen Funkion1 und Funktion2 || y(x):=-0.1*x^2+7;y(x):=0.2*x+1;'''fill:ch1-ch2,color=green''' || :[[Datei:ClipCapIt-190420-123555.PNG|100px]]
|- 
|}

* Als Funktionsnamen kann der Name der Funktion, oder die Nummer der Funktion (ch1, ch2,...) verwendet werden
* Nach der Funktionsdefinition kann durch Beistrich getrennt die Füllung konfiguriert werden.

{| class="wikitable" style="text-align: left; width: 100%;" 
| Parameter || Beschreibung || Beispiel
|-
| color=''{Farbe}'' || [[Farben|Farbe]] der Füllung setzen || color=blue
|-
| size || Linienstärke der Füllungsumrandung || size=5
|-
| fill || Füllstärke (mit der Farbe der Linienfarbe) einer Füllung von der Graphenlinie bis zur Nulllinie 0..keine Füllung (Standard) 1..deckend gefüllt || fill=0.3
|}

== gespiegelter Funktionsplot (functiony) ==
X und Y-Achse werden vertauscht! 

Beispiel:
&lt;pre&gt;
f(x):=x^2;x:-3,3;y:-3,3;f:size=5;functiony
&lt;/pre&gt;
:[[Datei:ClipCapIt-190416-172840.PNG|300px]]

== Bodediagramm (bode, bodeabs, bodearg) ==
{| class="wikitable" style="text-align: left; width: 100%;" 
| Funktion || Beschreibung || Beispiel || Graph
|-
| G(s):= ''{Funktion in s}'' || Laplace-transformierte || G(s):=1/(1+s);bode;s:0.01,100;abs:-60,20,size=4 || :[[Datei:ClipCapIt-190416-202517.PNG|200px]]
|-
| G(s):= ''{Funktion in s}'' || Laplace-transformierte mit Frequenz f  || G(s):=1/(1+s);bode;f:0.01,100;abs:-60,20,size=4 || [[Datei:ClipCapIt-190416-203122.PNG|200px]]
|-
| G(w):= ''{Funktion in w}'' || Fouriertransformierte mit Kreisfrequenz w || G(w):=1/(1+j*w);bode;w:0.01,100;abs:-60,20,size=4 || :[[Datei:ClipCapIt-190417-074431.PNG|200px]]
|-
| G(w):= ''{Funkion in w}'' || Fouriertransformierte mit Frequenz f || G(w):=1/(1+j*w);bode;f:0.01,100;abs:-60,20,size=4 || :[[Datei:ClipCapIt-190417-074615.PNG|200px]]
|-
| G(s):= ''{Funktion in s}'' || Nur Betragsfrequenzgang || G(s):=1/(1+0.01*s);bodeabs || :[[Datei:ClipCapIt-190417-074756.PNG|200px]]
|-
| G(s):= ''{Funktion in s}'' || Nur Betragsfrequenzgang || G(s):=1/(1+0.01*s);bodearg || :[[Datei:ClipCapIt-190417-074848.PNG|200px]]
|- 
|}

== Konfiguration von Achsen und Funktionen ==
Alle Konfigurationen zu Achsen und Funktionen beginnen mit dem Namen der Achse oder Funktion (Bsp: i(t) dann muss i:color=red --&gt; setzt die Farbe auf rot) gefolgt von einem Doppelpunkt und der durch Beistrich getrennten Parameterliste.

&lt;pre&gt;
Name:par1=wert1,par2=wert2,switch1,switch2
&lt;/pre&gt;

=== Name ===
{| class="wikitable" style="text-align: left; width: 100%;" 
| Name || Beschreibung || Beispiel || Name
|-
| Variable || Eine Variable, welche als Parameter einer Funktion auf einer Achse aufgetragen ist || f(x):=x^2+2*x || x
|-
| Funktion || Eine Funktion, welche auf einer Achse aufgetragen ist || f(x):=x^2+2*x || f
|-
| Absolutbetrag || Der Absolutbetrag einer komplexen Funktion || G(s):=1/(1+s);bode || abs
|-
| Argument || Das Argument einer komplexen Funktion || G(s):=1/(1+s);bode || arg
|}

=== Parameter ===
Wenn die '''ersten zwei Parameter''' aus Variablen und Datensätzen numerisch berechenbar sind, werden sie als '''Grenzen der Achsen''' verwendet. 

Weitere Parameter:
{| class="wikitable" style="text-align: left; width: 100%;" 
| Parameter || Beschreibung || Beispiel
|-
| color || [[Farben|Farbe]] des Graphen || color=red 
|-
| size || Linienstärke || size=5
|-
| style || [[Linienart]] setzen mit einem Definitionsstring der die Elemente Punkt,Minus,Unterstrich,Leerzeichen für die Definition der Linienart enthält || style=".-"
|-
| pointstyle || [[Punktstyle]] mit einem Definitionsstring für Start,Zwischen und Endpunkt durch Minus getrennt. || pointstyle=".-x-&gt;"
|-
| fill || Füllstärke (mit der Farbe der Linienfarbe) einer Füllung von der Graphenlinie bis zur Nulllinie 0..keine Füllung (Standard) 1..deckend gefüllt || fill=0.3
|-
| name || Beschriftungstext der Legende || name=abc
|-
| tex || Beschriftungstext der Legende als LaTeX Formel || tex=\alpha
|-
| eh   || Einheit die bei einem parametrischen Plot angezeigt werden soll || f(x,y):=[[1,2],[3,4]];y:0,3,eh=V
|- 
| grid || fixiert das Achsraster auf den angegebenen Wert || f(x):=x^2-3;x:-4,4,grid=1
|- 
| griddiv || setzt die Anzahl der Teilungen zwischen zwei Grid-Werte einer Achse || f(x):=x^2-3;x:-4,4,griddiv=2
|-
|}

=== Schalter ===
Schalter haben keinen Wert, sondern werden nur aktiv wenn sie angegeben werden.

{| class="wikitable" style="text-align: left; width: 100%;" 
| Schalter|| Beschreibung 
|-
| fill || Setzt die Füllstärke auf 0.3 wie wenn fill=0.3 gesetzt ist
|-
| name= || löscht die Legendenbeschriftung 
|- 
| 1000 || setzt die Anzahl der berechneten Werte auf 1000 
|-
| log || Ändert die Skala der Achse auf eine logarithmische Skala
|-
| dB || Ändert die Skala der Achse auf eine dB-Skala
|}

=== Beispiele ===
&lt;pre&gt;
x:-4,5,color=red,size=4
arg:color=blue
&lt;/pre&gt;

== allgemeine Parameter ==

{| class="wikitable" style="text-align: left; width: 100%;" 
| Parameter || Beschreibung || Beispiel
|-
| all=off || Schaltet alle Achsen und Gitter ab. &lt;br&gt; mögliche Modi sind: x,y,on,off || g(x):x+4;g;y:-10,10;all=off
|-
| grid=[mode] ||	Setzt die Darstellungsart des Hauptgitters! &lt;br&gt; mögliche Modi sind: x,y,all,off || g(x):x+4;g;y:-10,10;grid=off
|-
| helpgrid=[mode]	|| Setzt die Darstellungsart des Hilfsgitters! &lt;br&gt; mögliche Modi sind: x,y,all,off || 
|-
| axis=[mode] || Setzt die Darstellungsart der Achsen &lt;br&gt; mögliche Modi sind: x,y,all,off ||
|-
| legend=[mode] || Setzt die Darstellungsart der Achsenbeschriftung &lt;br&gt;mögliche Modi sind: x,y,all,off ||
|-
| numbers=[mode] || Setzt die Darstellungsart der Zahlen bei den Achsen &lt;br&gt; mögliche Modi sind: x,y,all,off || 
|-
| cursor=[mode] || Setzt die [[Plot-Plugin Cursor Darstellung | Darstellungsart des Cursors]] bei der Eingabe. &lt;br&gt; mögliche Modi sind: cnum(Standard),off,on,pixel,numbers,carg,crel,point,pnum,parg,all,hline,hnum,vline,vnum  || 
|-
| input=[mode] || Setzt die [[Plugin Input Mode|Art der Eingabe]] für die '''Mausbedienung''' des Plugins. &lt;br&gt; mögliche Modi sind: off, measure, point, line, hline, vline, toline(x,y),topoint(x,y),toarrow(x,y), lines, arrow, points, polyline, polygon, function, mc(), mcxy() || 
|-
| inputcounter=[anzahl] || Definiert die Anzahl der Punkte, die ein Schüler bei der Eingabe mindestens setzen muss. Ist nur aktiv wenn die Lösung als Funktion oder Gleichung angegeben wurde. || 
|-
| inputcolor=[farbe] || Setzt die Zeichenfarbe für Schülereingaben || inputcolor=blue
|-
| bgcolor=[farbe] || Setzt die Hintergrundfarbe || bgcolor=lightgray
|-
| gridcolor=[farbe] || Setzt die Farbe des Hauptgitters || gridcolor=black
|-
| helpgridcolor=[farbe] || Setzt die Farbe des Hilfsgitters || helpgridcolor=black
|-
| legendcolor=[farbe] || Setzt die Farbe der Achslegende || legendcolor=black
|-
| numbercolor=[farbe] || Setzt die Farbe des Zahlenbeschriftungen || numbercolor=black
|-
| axiscolor=[farbe] || Setzt die Farbe der Achsen || axiscolor=black
|-
| w[breite][Auflösung] || Breite und [[Plot-Plugin Auflösung|Auflösung]] des Bildes setzen. || w80, w80h, wh, wl, ws, w70h, w90s, w50l, w30H, w70L, w100S, w30-300, w40-800x600
|-
| size=[Auflösung] || Setzt die Bildgröße in Pixel. Siehe [[Plot-Plugin Auflösung|Auflösung]] || size=800, size=800x600
|-
| ae &lt;br&gt; achseinheit || Einheit bei den Achslegenden || 
|-
| showparams=off || Schaltet die Anzeige der Parameterwerte einer Parameterfunktion aus (on/off) || f(t):[cos(t),sin(t)];showparams=off
|- 
| htext=[text] || Zeigt den angegebenen Text als Achs-Legende auf der horizontalen Achse an || htext=U1
|-
| vtext=[text] || Zeigt den angegebenen Text als Achs-Legende auf der vertikalen Achse an || vtext=U1
|-
| htex=[text] || Zeigt den angegebenen Text als Achs-Legende auf der horizontalen Achse mit LaTeX Formelsatz an || htex=\alpha
|-
| vtex=[text] || Zeigt den angegebenen Text als Achs-Legende auf der vertikalen Achse mit LaTeX Formelsatz an || vtex=\alpha
|-
| point(f) || Zeichnet die durch Punkte gegebene Funktion nur aus den Stützpunkten || f(x,y):[[0,a],[a,b]];point(f)
|-
| line(f) || Zeichnet die durch Punkte gegebene Funktion als Liniezug (Standard) || f(x,y):[[0,a],[a,b]];line(f)
|-
| vect(f) || Zeichnet die durch Punkte gegebene Funktion als Vectorkette || f(x,y):[[0,a],[a,b]];vect(f) 
|-
| ort(f) || Zeichnet die durch Punkte gegebene Funktion aus einzelnen Ortsvektoren || f(x,y):[[0,a],[a,b]];ort(f)
|-
| linepoint(f) || Zeichnet die durch Punkte gegebene Funktion als Linienzug mit Stützpunkten || f(x,y):[[0,a],[a,b]];linepoint(f)
|-
| view=x1,y1,x2,y2 || Setzt den sichtbaren Bereich bezüglich des normal quadratischen Zeichenfensters auf das angegebene Rechteck (x1,y1)(x2,y2). Die Angabe von x1,x2,y1,y2 erfolgt mittels Ganzzahlen als Prozentwerte wobei links oben 0,0 und rechts unten 100,100 liegen. Die Standardeinstellung ist somit view=0,0,100,100&lt;br&gt; Prozentwerte sind größer als 100 und auch negativ möglich! || f(x):=sin(x);x:0,2pi;view=10,0,60,70 :[[Datei:ClipCapIt-200527-101423.PNG|100px]]
|}

== Ortskurve (ortskurve) ==
Zeichnet die '''Frequenzgangsortskurve''' einer Funktion im Laplacebereich mit dem '''Laplaceoperator s''' oder einer Fouriertransformierten mit der '''Kreisfrequenz w'''.

Beispiel:
&lt;pre&gt;
G(s):=1/(1+0.01*s);ortskurve;ReG:-1,1;ImG:-1,1;G:size=4,color=blue
&lt;/pre&gt;
:[[Datei:ClipCapIt-190417-075639.PNG|300px]]

== zeichnen in ein vordefiniertes Bild ==
* Ein Bild welches in der [[Dateien_zur_Frage_verwalten|Bildliste]] einer Frage existiert kann als Hintergrundbild für eine Zeichnung verwendet werden. Für das Bild IMG0 verwende:
&lt;pre&gt;
baseimage(0)
&lt;/pre&gt;

* Die Bildgröße wird direkt als Basis für das Koordinatensystem verwendet 
* Der Koordinatenursprung liegt links oben
* Die positive x-Achse zeigt nach rechts
* Die positive y-Achse zeigt nach unten

== vordefinierte graphische Funktionen ==

Für das einfache Zeichnen von beliebigen Elementen sind graphische Grundelemente vordefiniert. Diese Elemente können auch ein einigen anderen Plugins wie [[Wsr]], [[Gsr]], [[Dsr]], [[Graph]], [[DigiGraph]] und [[Elektronik]] durch Strichpunkt getrennt verwendet werden.

=== Definition ===
===== Definition als Funktion =====
&lt;pre&gt;
{name}({parameter1},{parameter2}):={zeichenelement}({parameter},{parameter},{parameter},...)
&lt;/pre&gt;

Wie zum Beispiel:
&lt;pre&gt;
f(x,y):=line(-3,-4,8,2,textsize=4,textcolor=red,pointcolor=black,"HALLO")
&lt;/pre&gt;

ANMERKUNG: falls eine weitere Funktion in der Zeichenebene mit nicht-Standard-Achsvariablen (x,y) verwendet wird sollten die Achsvariablen der anderen Funktion für parameter1 und parameter2 verwendet werden, damit wird dann in das vorhandene Achsensystem gezeichnet

Wie zum Beispiel:
[[Datei:Line-sin.png|mini]]
&lt;pre&gt;
u(t):=20V*sin(2*%pi*50Hz*t)
f(t,u):=line(5ms,-5V,15ms,20V,textsize=1,textcolor=red,pointcolor=black,"HALLO")
u:-30V,30V
t:0ms,20ms
&lt;/pre&gt;

===== direkte Definition des Zeichenelementes ohne Funktion =====
Da hier der Funktionsname und die Parameter nicht definiert sind werden als '''Parameter immer x und y''' verwendet und der Funktionsname ist gleich wie der Zeichenelementname.
&lt;pre&gt;
{zeichenelement}({parameter},{parameter},{parameter},...)
&lt;/pre&gt;

''VORSICHT'': falls in der Zeichenebenen nicht x und y bei den Achsen verwendet werden wird dadurch eine weitere y-Achse mit dem Bereich -10..10 hinzugefügt. In diesem Fall ist die funktionale Schreibweise f(x,y):=funktionsname... zu bevorzugen, wobei dann statt x und y die vorandenen Achsvariablen zu verwenden sind!

Wie zum Beispiel:
&lt;pre&gt;
line(-3,-4,8,2,textsize=4,textcolor=red,pointcolor=black,"HALLO")
&lt;/pre&gt;

===== Beschreibung der Parmeter =====

* name : Name der Funktion, welche wie eine normale parametrische Funktion verwendet werden kann
* parameter1 : Name der Funktionsvariablen auf der horizontalen Achse
* parameter2 : Name der Funktionsvariablen auf der verzikalen Achse
* zeichenelement: Name des Zeichenelementes wie line,point,vect,etc.
* parameter : Die Parameter  beginnen immer mit den Funktionskoordinaten, welche in Anzahl und Art von dem Zeichenelement abhängig sind. Danach können in beliebiger Reihenfolge Parameter angegeben werden welche die Funktion parametrieren wie etwa textcolor,color,points,fill,etc.

==== Verwendung im PIG-Tag ====
Alle voerdefinierten Elemente können auch durch Strichpunkt getrennt im PIG-Tag angegeben werden.

Ein Anführungszeichen " muss bei der Verwendung im PIG-Tag im Definitionsstring mit einem Backslash verblockt werden.
&lt;pre&gt; [PIG Plugin2 "text(2,2,tex=\"\alpha\")"/] &lt;/pre&gt;

=== definierte Zeichenelemente ===

{| class="wikitable" style="text-align: left; width: 100%;" 
| Funktion || Beschreibung || Beispiel || Graph
|-
| line(x1,y1,x2,y2) || Zeichnet eine Line vom Startpunkt x1/y1 zum Endpunkt x2/y2 || line(-3,-6,8,5) || 
:[[Datei:ClipCapIt-200507-082039.PNG|100px]]
|-
| arrow(x1,y1,x2,y2) || Zeichnet einen Pfeil vom Startpunkt x1/y1 zum Endpunkt x2/y2 || arrow(-3,-6,8,5) || 
:[[Datei:ClipCapIt-200507-084749.PNG|100px]]
|-
| dimension(x1,y1,x2,y2) || Zeichnet eine Bemaßung vom Startpunkt x1/y1 zum Endpunkt x2/y2 || dimension(-3,2,8,5,textsize=3) || 
:[[Datei:ClipCapIt-200507-084855.PNG|100px]]
|-
| hdimension(x1,y1,x2,y2,y) || Zeichnet eine horizontale Bemaßung mit Maßlinien. || hdimension(2,2,6,-3,4) || 
:[[Datei:ClipCapIt-200603-120304.PNG|100px]]
|-
| vdimension(x1,y1,x2,y2,x) || Zeichnet eine horizontale Bemaßung mit Maßlinien. || vdimension(2,2,6,-3,8) || 
:[[Datei:ClipCapIt-200603-120342.PNG|100px]]
|-
| rdimension(x1,y1,r) || Zeichnet eine Radius-Bemaßung. || circle(2,4,3);rdimension(2,4,3) ||
:[[Datei:ClipCapIt-200603-123717.PNG|100px]]
|-
| rdimension(x1,y1,r,alpha) || Zeichnet eine Radius-Bemaßung am Positionswinkel alpha ||  circle(2,4,1.88);rdimension(2,4,1.88,-30°) || 
:[[Datei:ClipCapIt-200603-123806.PNG|100px]]
|-
| point(x1,y1) || Zeichnet einen Punkt am Punkt x1/y1 || point(-3,-6,"A",textsize=2) ||  
:[[Datei:ClipCapIt-200507-085057.PNG|100px]]
|-
| drawpoint(x1,y1) || Zeichnet einen Punkt am Punkt x1/y1 || drawpoint(-3,-6,"A",textsize=2) ||  
:[[Datei:ClipCapIt-200507-085057.PNG|100px]]
|-
| circle(x1,y1,r) || Zeichnet einen Kreis mit dem Radius r und dem Mittelpunkt x1/y1 || circle(2,3,5) || 
:[[Datei:ClipCapIt-200507-085121.PNG|100px]]
|-
| oval(x1,y1,rx,ry) || Zeichnet eine Ellipse mit der Halbachse rx auf der x-Achse und der Halbachse ry auf der y-Achse || oval(2,3,5,3) || 
:[[Datei:ClipCapIt-200507-085150.PNG|100px]]
|-
| arc(x1,y1,r,start,arg) || Zeichnet einen Kreisbogen mit dem Mittelpunkt x1,y1 dem Radius r von einem Startwinkel start (rad) mit einer Winkelbogen von arg ||  arc(2,3,3,180°,-220°,pointstyle="O-&gt;") || 
:[[Datei:ClipCapIt-200603-073709.PNG|110px]]
|-
| loop(x1,x2,r) || Zeichnet einen Kreisbogen mit 250° und Pfeil mit Mittelpunkt x1,y1 und Radius r. Mit dem Parameter '''reverse''' zeigt der Pfeil in die Gegenrichtung. || loop(2,3,1,tex="\alpha")&lt;br&gt;loop(2,3,1,tex="\alpha",reverse) || 
:[[Datei:ClipCapIt-200603-073927.PNG|100px]] &lt;br&gt;
:[[Datei:ClipCapIt-200608-112003.PNG|100px]]
|-
| rect(x1,y1,x2,y2) || Zeichnet ein Rechteck mit den zwei Eckpunkten x1/y1 und x2/y2 || rect(-3,-6,8,2) || 
:[[Datei:ClipCapIt-200507-085242.PNG|100px]]
|-
| rectc(x1,y1,b,h) || Zeichnet ein Rechteck mit dem Mittelpunkt x1/y1, Breite b und Höhe h || rectc(2,4,8,5) || 
:[[Datei:ClipCapIt-200507-085309.PNG|100px]]
|-
| text(x1,y1,text) || Zeichnet einen Text mit Mittelpunk x1/y1 || text(-3,4,"ABC") ||
:[[Datei:ClipCapIt-200507-085400.PNG|100px]]   
|-
| drawpoints([[x1,y1],[y2,y2],[x3,y3]]) || Zeichnet die Punkte welche in der Matrix definiert sind. || drawpoints([[2,2],[8,5],[3,-5],[8,2]]) || 
:[[Datei:ClipCapIt-211102-142806.PNG|100px]]
|-
| drawline([[x1,y1],[y2,y2],[x3,y3]]) || Zeichnet die Punkte welche in der Matrix definiert sind paarweise als Linien. || drawline([[2,2],[8,5],[3,-5],[8,2]]) ||  
:[[Datei:ClipCapIt-211102-142728.PNG|100px]]
|-
| drawvect([[x1,y1],[y2,y2],[x3,y3]]) || Zeichnet die Punkte welche in der Matrix definiert sind paarweise als Pfeile. || drawvect([[2,2],[8,5],[3,-5],[8,2]]) ||  
:[[Datei:ClipCapIt-211102-143050.PNG|100px]]
|-
| drawlines([[x1,y1],[y2,y2],[x3,y3]]) || Zeichnet die Punkte welche in der Matrix definiert sind paarweise als Geraden. || drawlines([[2,2],[8,5],[3,-5],[8,2]]) ||  
:[[Datei:ClipCapIt-211102-142916.PNG|100px]]
|-
| vect([[x1,y1],[y2,y2],[x3,y3]]) || Zeichnet Ortsvektoren die Punkte welche in der Matrix definiert sind. || vect([[2,2],[8,5],[3,-5]])  ||
:[[Datei:ClipCapIt-200507-085508.PNG|100px]]
|-
| polyline([[x1,y1],[y2,y2],[x3,y3]]) || Verbindet die  Punkte welche in der Matrix definiert sind durch eine Linie. || polyline([[2,2],[8,5],[3,-5]]) ||
:[[Datei:ClipCapIt-200507-085536.PNG|100px]]
|-
| polygon([[x1,y1],[y2,y2],[x3,y3]]) || Verbindet die Punkte welche in der Matrix definiert zu einer geschlossenen Linie. || polygon([[2,2],[8,5],[3,-5]]) ||
:[[Datei:ClipCapIt-200507-085558.PNG|100px]]
|- 
| legend(position,beschriftung,beschriftung) || Zeichnet eine Legenden-Box an die angegebene Position (1,2,3,4)|| f(x):5*sin(x);x:0,2pi;legend(1,alpha+beta,"Parabel");g(x):=x^2-3;legend=off || 
:[[Datei:ClipCapIt-200513-104711.PNG|100px]]
|-
| legend(x,y,beschriftung,beschriftung) || Zeichnet eine Legenden-Box an die angegebene Position (Werte zwischen 0 und 1) || f(x):5*sin(x);x:0,2pi;legend(0.2,0.6,alpha+beta,"Parabel",size=3);g(x):=x^2-3 ||
:[[Datei:ClipCapIt-200513-105042.PNG|100px]]
|-
| image(x1,y1,x2,y2,nr) || Zeichnet ein Bild aus der Bildliste der Frage in das Rechteck mit den Eckpunkten (x1,y1) und (y2,y2). Die Nummer entspricht der IMG-Nummer in der Bildliste der Frage. || image(-6,-6,8,6,0) || 
:[[Datei:ClipCapIt-200622-120054.PNG|100px]]
|-
| imgfunc(function) || Zeichnet eine Funktion, welche im Maximfeld definiert wurde. || maxima: f1:line(1,2,3,4)&lt;br&gt; imgfunc(f1) || 
:[[Datei:ClipCapIt-200608-155302.PNG|100px]]
|- 
| imgif(bedingung,function1,function2) || Zeichnet je nachdem ob eine Bedingung erfüllt (function1) oder nicht erfüllt (function2) die entsprechende Funktion. || imgif(y!=0,line(1,2,3,4),rect(1,2,3,4)) || 
:[[Datei:ClipCapIt-200608-152824.PNG|100px]]
|-
| imgfor(variable,first,second,last,function) || Zeichnet eine Funktion mit einer Schleife mehrmals. || imgfor(x,-4,-3,4,line(x,1,x+4,6)) ||
:[[Datei:ClipCapIt-200608-152751.PNG|100px]]
|-
| boxplot(uw,uq,m,oq,ow,pos,height) || Zeichnet einen Boxplot. pos und height sind optional.  || boxplot(-6,-3,1,2,4);boxplot(-4,-2,1,2,5,3,2);boxplot([[Berechnungen#Mengen-Funktionen|setboxplot]]([1,2,3,4,5,6]),-4,text="Hallo") || 
:[[Datei:ClipCapIt-201002-172706.PNG|100px]]
|-
|}

=== Konfigurations-Parameter ===

{| class="wikitable" style="text-align: left; width: 100%;" 
| Parameter|| Beschreibung || Beispiel || Graph
|-
| size= || Strichstärke und Pfeilgröße || dimension(-3,2,6,7,size=1);dimension(-3,0,6,5,size=2);dimension(-3,-2,6,3,size=3) || 
:[[Datei:ClipCapIt-200507-131807.PNG|100px]]
|- 
| style= || [[Linienart]] setzen mit einem Definitionsstring der die Elemente Punkt,Minus,Unterstrich,Leerzeichen für die Definition der Linienart enthält || line(-4,-5,8,8,style="_.",size=2) || 
:[[Datei:ClipCapIt-200519-170022.PNG|100px]]
|-
| color= || Linienfarbe || dimension(-3,2,6,7,color=red);dimension(-3,0,6,5,color=green);dimension(-3,-2,6,3,color=blue) || 
:[[Datei:ClipCapIt-200507-115058.PNG|100px]]
|- 
| textcolor= || Textfarbe || dimension(-3,2,6,7);dimension(-3,0,6,5,textcolor=red);dimension(-3,-2,6,3,textcolor=green) || 
:[[Datei:ClipCapIt-200507-131736.PNG|100px]]
|- 
| bgcolor= || Hintergrundfarbe von Text || dimension(-3,2,6,7);dimension(-3,0,6,5,bgcolor=red);dimension(-3,-2,6,3,bgcolor=green) || 
:[[Datei:ClipCapIt-200512-155301.PNG|100px]]
|- 
| pointcolor= || Punktfarbe || line(-3,2,6,7);line(-3,0,6,5,pointcolor=red);line(-3,-2,6,3,pointcolor=green) || 
:[[Datei:ClipCapIt-200507-132044.PNG|100px]]
|- 
| fillcolor= || Füllfarbe || circle(2,4,4,fillcolor=red) || 
:[[Datei:ClipCapIt-200507-132416.PNG||100px]]
|- 
| fill= || Füllgrad als Wert zwischen 1 und 255 || circle(-4,4,4,fill=20);circle(4,4,4,fill=100);circle(4,-4,4,fill=255) ||
:[[Datei:ClipCapIt-200507-132642.PNG|100px]]
|- 
| fill || Schaltet die Füllung mit einem Standardfüllgrad ein || circle(2,4,4,fill)|| 
:[[Datei:ClipCapIt-200612-074140.PNG|100px]]
|-
| fillunder || Füllt eine Polyline von y=0 bis zur Polylinie || polyline([[-8,2],[-2,6],[3,-6],[7,5],[9,5]],color=red,fillunder) || 
:[[Datei:ClipCapIt-200612-074250.PNG|100px]]
|-
| stairs || Zeichnet eine Polylinie als Treppenfunktion mit horizontalen Treppenstufen || polyline([[-8,2],[-2,6],[3,-6],[7,5],[9,5]],stairs) || 
:[[Datei:ClipCapIt-200612-074344.PNG|100px]]
|-
| points || Zeichnet die Bezugspunkt des Elements als Punkte ein || rectc(-4,4,4,4,points);rectc(4,4,4,4,pointcolor=red) || 
:[[Datei:ClipCapIt-200507-132914.PNG|100px]] 
|- 
| text || definiert einen Text, der zu dem graphischen Element geschrieben wird. Statt text="abc" kann auch direkte "abc" geschrieben werden. Formeln werden im LaTeX Formelsatz geschrieben. || line(-3,2,6,7,text="abc");line(-3,0,6,5,"efg");line(-3,-2,6,3,text=2*4mm) || 
:[[Datei:ClipCapIt-200507-133453.PNG|100px]]
|- 
| tex= || definiert einen Text, der zu dem graphischen Element als LaTeX Formelsatz interpretiert wird. || line(-3,2,6,7,tex=\alpha);line(-3,0,6,5,tex="\alpha_x");line(-3,-2,6,3,text=2*4'mm2') || 
:[[Datei:ClipCapIt-200512-160018.PNG|100px]]
|- 
| textangle= || definiert den Schriftwinkel des Textes wobei immer um den Textbezugspunkt rotiert wird || line(-3,2,6,7,text="abc");line(-3,0,6,5,"efg",textangle=90°);line(-3,-2,6,3,text=2*4mm,textangle=180°) || 
:[[Datei:ClipCapIt-200507-133818.PNG|100px]]
|- 
| textangleabs= || definiert den Schriftwinkel des Textes bezüglich des Koordinatensystems wobei immer um den Textbezugspunkt rotiert wird || line(-3,2,6,7,text="abc",textangleabs);line(-3,0,6,5,"efg",textangleabs=45°);line(-3,-2,6,3,text=2*4mm,textangleabs=90°) || [[Datei:ClipCapIt-200522-160645.PNG|100px]]
|- 
| textposition= || definiert die vertikale Position des Text-Bezugspunktes || line(-3,2,6,7,text="abc");line(-3,0,6,5,"efg",textposition=0.4);line(-3,-2,6,3,text=2*4mm,textposition=-0.3) ||
:[[Datei:ClipCapIt-200507-133751.PNG|100px]]
|- 
| textsize= || definiert die Schriftgröße als Faktor (Standard=2) || line(-3,2,6,7,text="abc");line(-3,0,6,5,"efg",textsize=1);line(-3,-2,6,3,text=2*4mm,textsize=3)  || 
:[[Datei:ClipCapIt-200507-134222.PNG|100px]]
|-
| unit= || Setzt die Einheit einer Bemaßung auf die angegebenen Einheit und dividiert durch den Zahlenwert wenn er nicht gleich 1 ist. ||
dimension(-3cm,2cm,6cm,7cm,unit=1cm); dimension(-3cm,0cm,6cm,5cm,unit=2cm)
|| :[[Datei:ClipCapIt-200522-170352.PNG|100px]]
|-
| unitnorm= || Dividiert den Zahlenwert durch die angegebene Einheit. || dimension(-3cm,2cm,6cm,7cm,unitnorm=1cm); dimension(-3cm,0cm,6cm,5cm,unitnorm=2cm) || 
:[[Datei:ClipCapIt-200522-170544.PNG|100px]]
|- 
| underline || unterstreicht den Text ||  rect(-3,2,6,7,text="Abc",underline, textcolor=red) || 
:[[Datei:ClipCapIt-200507-134408.PNG|100px]]
|- 
| center || zentriert den Text horizontal und vertikal ||  text(-3,2,6,7,text="Text Demo",center,points,pointcolor=red) || 
:[[Datei:ClipCapIt-200512-160358.PNG|100px]]
|- 
| hcenter || zentriert den Text horizontal ||  text(-3,2,6,7,text="Text Demo",hcenter,points,pointcolor=red) || 
:[[Datei:ClipCapIt-200512-160358.PNG|100px]]
|- 
| vcenter || zentriert den Text vertikal ||  text(-3,2,6,7,text="Text Demo",vcenter,points,pointcolor=red) || 
:[[Datei:ClipCapIt-200512-160358.PNG|100px]]
|- 
| left || schreibt den Text linksbündig ||  text(-3,2,6,7,text="Text Demo",left,points,pointcolor=red) || 
:[[Datei:ClipCapIt-200512-160555.PNG|100px]]
|- 
| right || schreibt den Text rechtsbündig ||  text(-3,2,6,7,text="Text Demo",right,points,pointcolor=red) || 
:[[Datei:ClipCapIt-200512-160644.PNG|100px]]
|- 
| top || schreibt den Text nach oben bündig ||  text(-3,2,6,7,text="Text Demo",top,points,pointcolor=red) || 
:[[Datei:ClipCapIt-200512-160740.PNG|100px]]
|- 
| bottom || schreibt den Text nach unten bündig ||  text(-3,2,6,7,text="Text Demo",bottom,points,pointcolor=red) || 
:[[Datei:ClipCapIt-200512-160801.PNG|100px]]
|- 
| back || Zeichnet das Zeichenelement im Hintergrund || image(-6,-6,8,6,0,back) || 
:[[Datei:ClipCapIt-200622-120418.PNG|100px]]
|}

= siehe auch =
* [[Plugins]]
* [[Linienart]]
* [[Punktstyle]]
* [[Plugin_Input_Mode|interaktive Eingabe]]
* [[Plot-Plugin Cursor Darstellung]]

[[Category:Plugins]]

