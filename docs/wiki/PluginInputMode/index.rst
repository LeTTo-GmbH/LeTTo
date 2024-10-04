Mit dem Parameter '''input''' kann die Art der interaktiven Eingabe beim [[Plot]] Plugin durch den Schüler definiert werden.


{| class="wikitable" style="text-align: left; width: 100%;" 
| Parameter || Beschreibung ||  Beispieldefinition || charakteristisches Bild || Lösung
|-
| input=off || die interaktive Eingabe ist abgeschaltet, es funktioniert nur das Zoom || || ||
|-
| input=measure || Messwerkzeug für die Vermessung in einem karthesischen Koordinatensystem || || :[[Datei:ClipCapIt-201221-213115.PNG|300px]] || Punktematrix &lt;br&gt;[[-5.924,5.077],[5.107,-3.353]]
|-
| input=point || Eingabe eines einzigen Punktes || || :[[Datei:ClipCapIt-201221-213302.PNG|300px]] || Vektor &lt;br&gt; [2,9]
|-
| input=points || Eingabe von mehreren Punkten. Die Reihenfolge der Punkte ist dabei unwesentlich || || :[[Datei:ClipCapIt-201221-213745.PNG|300px]] || Punktematrix&lt;br&gt;[[2,9],[-5,-2],[10,-4]]
|-
| input=line || Eingabe einer Geraden gegeben durch zwei Punkte. || || :[[Datei:ClipCapIt-201221-214628.PNG|300px]] || Punktematrix [[0,-3],[5,7]] oder Gleichung y=-3+2*x je nach Lösungsfeld
|-
| input=hline || Eingabe einer horizontalen Geraden || U(t):=Us*sin(2*%pi*f*t)&lt;br&gt;U:-Us*1.2,Us*1.2,name=u(t)&lt;br&gt;t:0s,3/f&lt;br&gt;input=hline&lt;br&gt;w50h&lt;br&gt; :[[Datei:ClipCapIt-210930-155513.PNG|500px]] || :[[Datei:ClipCapIt-210930-154537.PNG|300px]] || Zahlenwert &lt;br&gt; 28V
|-
| input=vline || Eingabe einer vertikalen Geraden || U(t):=Us*sin(2*%pi*f*t)&lt;br&gt;U:-Us*1.2,Us*1.2,name=u(t)&lt;br&gt;t:0s,3/f&lt;br&gt;input=vline&lt;br&gt;w50h&lt;br&gt; :[[Datei:ClipCapIt-210930-155417.PNG|500px]] || :[[Datei:ClipCapIt-210930-155152.PNG|300px]] || Zahlenwert &lt;br&gt; 5.1ms
|-
| input=topoint(x,y) || Eingabe einer Linie von einem Startpunkt (x/y) zu einem einzugebenen Endpunkt || y(x):=y&lt;br&gt;x:0,6*T&lt;br&gt;y:0,m*1.2&lt;br&gt;input=topoint(0,a-b)&lt;br&gt;w50h :[[Datei:ClipCapIt-210930-160823.PNG|500px]]  ||  :[[Datei:ClipCapIt-210930-160737.PNG|300px]] || Vektor &lt;br&gt; [0.003,4.8]
|-
| input=toline(x,y) || Eingabe einer Geraden durch einen Startpunkt (x/y) und einen einzugebenen Punkt || input=toline(2,0) || :[[Datei:ClipCapIt-211103-203503.PNG|300px]] || Vektor &lt;br&gt; [6,8]
|-
| input=toarrow(x,y) || Eingabe eines Vektorpfeiles von einem Startpunkt (x/y) zu einem einzugebenen Endpunkt || input=toarrow(2,0) || :[[Datei:ClipCapIt-211103-201037.PNG|300px]] || Vektor &lt;br&gt; [6.4,4.2]
|-
| input=lines || Eingabe von mehreren Geraden für die Vermessung in Diagrammen. || || :[[Datei:ClipCapIt-201221-215336.PNG|300px]] || Punktematrix
|-
| input=arrow || Eingabe von mehreren Pfeilen. || || || Punktematrix
|-
| input=polyline || Eingabe von mehreren Punkten deren Reihenfolge stimmen muss ||  || || Punktematrix
|- 
| input=polygon || Eingabe von mehreren Punkten deren geschlossene Reihenfolge stimmen muss || :[[Datei:ClipCapIt-201221-225433.PNG|500px]] || :[[Datei:ClipCapIt-201221-222601.PNG|300px]] || Punktematrix &lt;br&gt; [[-5,-1],[-2,-1],[-2,-3],[-5,-3]]
|-
| input=function || Eingabe einer Funktion y=f(x) mit streng monoton steigendem x || :[[Datei:ClipCapIt-201221-225738.PNG|500px]] || :[[Datei:ClipCapIt-201221-222408.PNG|300px]]  || Punktematrix &lt;br&gt; [[-3,5],[-2,0],[-1,-3],[0,-4],[1,-3],[2,0],[3,5]]
|-
| input=mc(...) || Multiple Choice Eingabe auf Basis von Pixelkoordinaten || baseimage(0)&lt;br&gt;input=mc([301.2,521.1],[551.1,512],[697,470],[988.9,280.3],[905,220.1],[751.7,537.5],[631.4,641.5],[968.8,537.5],[666,347.8],[806.5,349.6],[1008,406.2])&lt;br&gt; :[[Datei:ClipCapIt-210930-162242.PNG|500px]] || :[[Datei:ClipCapIt-210930-162151.PNG|300px]] || Vektor aller angehakten Items &lt;br&gt; [0]
|-
| input=mcxy(...) || Multiple Choice Eingabe auf Basis des x-y-Koordinatensystems || input=mcxy(TP,P1,P2,P3,P4,P5,P6)&lt;br&gt;x:1.2*minx,1.2*maxx&lt;br&gt;y:1.2*miny,1.2*maxy&lt;br&gt;w50h&lt;br&gt; :[[Datei:ClipCapIt-210930-171143.PNG|500px]]  ||  :[[Datei:ClipCapIt-210930-170959.PNG|300px]] || Vektor aller angehakten Items &lt;br&gt; [0]
|-
|}

== siehe auch ==
[[Plot]] Plugin [[Plot#allgemeine_Parameter|allgemeine Parameter]]

[[Plot-Plugin graphische Multiple-Choice-Eingabe]]

