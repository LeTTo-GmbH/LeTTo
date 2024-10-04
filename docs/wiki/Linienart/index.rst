Die Linienart im [[Plot]]-Plogin wird über den '''style''' Wert der als String definiert ist angegeben. 

= Zeichen für die Definition der Linienart =

{| class="wikitable" style="text-align: left; width: 100%;" 
| Zeichen || Beschreibung || Beispiel || Graph
|-
| . (Punkt) || kurzer Strich bzw. Punkt || line(-6,-3,6,9,style=".",size=8);line(-6,-6,6,6,style="2.",size=8);line(-6,-9,6,3,style="6.",size=8) || 
:[[Datei:ClipCapIt-200520-085034.PNG|100px]]
|- 
| - (Minus) || mittlerer Strich || line(-6,-3,6,9,style="-",size=8);line(-6,-6,6,6,style="-",size=3);line(-6,-9,6,3,style="9-",size=3) || 
:[[Datei:ClipCapIt-200520-085211.PNG|100px]]
|- 
| - (Unterstrich) || langer Strich || line(-6,-3,6,9,style="_",size=8);line(-6,-6,6,6,style="_",size=3);line(-6,-9,6,3,style="9_",size=3) || 
:[[Datei:ClipCapIt-200520-085402.PNG|100px]]
|- 
|  (Leerzeichen) || Zwischenraum || line(-6,-3,6,9,style=". .",size=8);line(-6,-6,6,6,style=". ",size=8);line(-6,-9,6,3,style="- ",size=3) || 
:[[Datei:ClipCapIt-200520-085610.PNG|100px]]
|- 
| r || abgerundete Enden || line(-6,-3,6,9,style=".r",size=8);line(-6,-6,6,6,style="-r",size=8);line(-6,-9,6,3,style="-r",size=3) || 
:[[Datei:ClipCapIt-200520-085759.PNG|100px]]
|- 
| s || rechteckige Enden || line(-6,-3,6,9,style=".s",size=8);line(-6,-6,6,6,style="-s",size=8);line(-6,-9,6,3,style="-s",size=3) || 
:[[Datei:ClipCapIt-200520-090048.PNG|100px]]
|- 
| R || abgerundete äußere Ecken || rect(-8,-8,8,8,style="R",size=18);rect(-6,-6,6,6,style="R",size=8) || 
:[[Datei:ClipCapIt-200520-182106.PNG|100px]]
|- 
| B || angefaste äußere Ecken || rect(-8,-8,8,8,style="B",size=18);rect(-6,-6,6,6,style="B",size=8) || 
:[[Datei:ClipCapIt-200520-182305.PNG|100px]]
|-
| 0..9 (Ziffer) || setzt den automatischen Leerraum zwischen zwei Linien (0:extrem kurz 9:lang). Der Wert kann auch mehrmals angegeben werden. || line(-6,-3,6,9,style="1-4-9-",size=5);line(-6,-6,6,6,style="1--9--",size=4);line(-6,-9,6,3,style="1-.",size=4) || 
:[[Datei:ClipCapIt-200520-183040.PNG|100px]]
|-
|}

= Beispiele =

{| class="wikitable" style="text-align: left; width: 100%;" 
| Beispiel || Code || Graph
|-
| -. || line(-7,2,7,2,style="-.",size=3) || [[Datei:ClipCapIt-200522-112437.PNG|300px]]
|-
| _. || line(-7,2,7,2,style="_.",size=3) || [[Datei:ClipCapIt-200522-112628.PNG|300px]]
|-
| s1___9_. || line(-7,2,7,2,style="s1___9_.",size=1) || [[Datei:ClipCapIt-200522-113643.PNG|300px]]
|-
| . || line(-7,2,7,2,style=".",size=3) || [[Datei:ClipCapIt-200522-112715.PNG|300px]]
|-
| 2. || line(-7,2,7,2,style="2.",size=3) || [[Datei:ClipCapIt-200522-113028.PNG|300px]]
|-
| 9. || line(-7,2,7,2,style="9.",size=3) || [[Datei:ClipCapIt-200522-113134.PNG|300px]] 
|-
| - || line(-7,2,7,2,style="-",size=3) || [[Datei:ClipCapIt-200522-112817.PNG|300px]]
|-
| _.. || line(-7,2,7,2,style="_..",size=3) || [[Datei:ClipCapIt-200522-112928.PNG|300px]]
|- 
| 9_2.9. || line(-7,2,7,2,style="9_2.9.",size=3) || [[Datei:ClipCapIt-200522-113301.PNG|300px]]
|-
|}

