Im Angabetext und bei der [[ZielEinheit]] einer Lösung kann die Zahlendarstellung durch ein Zahlenformat durch einen Beistrich getrennt angegeben werden. Bei einer Berechnenden Anzeige {= } sollte man einen '''Strichpunkt''' verwenden!

z.B:
&lt;pre&gt;{x;a2}
{y,4}
{=153;F3}   

Bei konstanten Werten oder berechneten Werten kann der Beistrich als Listentrenner interpretiert werden. Es wird empfohlen den Strichpunkt zu verwenden.
&lt;/pre&gt;

== Ergebniseingabe bei Antwortfeldern ==
Für die Schülereingabe kann die Eingabe durch ein Gleichheitszeichen vor dem Zahlenformat in der [[ZielEinheit]] der Teilantwort einer Frage erzwungen werden!

== Zahlenformate ==
Für die Zahlendarstellung sind folgende Zahlenformate definiert:
{| class="wikitable" style="text-align: left; width: 100%;
| Format || Bedeutung || Beispiel || Wert || Ausgabe
|-
| || ohne Angabe wird die Zahl ab 10^5 bzw. 10^-5 als Gleitkommazahl mit 14 gültigen Ziffern dargestellt || {x} || 12345.34&lt;br&gt;123456.43 || 12345.34 &lt;br&gt; 1.2345643e5
|-
| ,{ziffern} || maximale Anzahl gültiger Ziffern&lt;br&gt;auch hier wird ab 10^5 bzw. 10^-5 auf Gleitkommadarstellung umgestellt || {x,3} || 1451.34 &lt;br&gt; 1234567.23 || 1450 &lt;br&gt; 1.23e6
|-
| ,d{ziffern} || Kommazahl mit einer maximalen Anzahl gültiger Ziffern  || {x,d3}&lt;br&gt;{x,d8} || 203.2 || 203&lt;br&gt;203.2
|-
| ,D{ziffern} || Kommazahl mit einer fixen Anzahl gültiger Ziffern || {x,D3}&lt;br&gt;{x,D8} || 203.2 || 203&lt;br&gt;203.20000
|-
| ,r{ziffern} || Kommazahl in normaler oder Gleitkommadarstellung mit einer maximalen Anzahl gültiger Ziffern || {x,r3}&lt;br&gt;{x,r8} || 203.2 || 203&lt;br&gt;203.2
|-
| ,R{ziffern} || Kommazahl in normaler oder Gleitkommadarstellungmit einer fixen Anzahl gültiger Ziffern || {x,R3}&lt;br&gt;{x,R8} || 203.2 || 203&lt;br&gt;203.20000
|-
| ,a{ziffern} || Kommazahl mit einer maximalen Anzahl von Nachkommastellen || {x,a1} &lt;br&gt; {x,a3} || 1451.34 || 1451.3 &lt;br&gt;1451.34
|-
| ,A{ziffern} || Kommazahl mit einer fixen Anzahl von Nachkommastellen || {x,A1} &lt;br&gt; {x,A3} || 1451.34 || 1451.3 &lt;br&gt;1451.340
|-
| ,A0 || Ganzzahl ohne Gleitkommadarstellung || {x,A0} || 1451.34 &lt;br&gt; 123456789012.2345 || 1451 &lt;br&gt;123456789012
|-
| ,e{ziffern} || Exponentialschreibweise Gleitkommazahl mit einer maximalen Anzahl gültiger Ziffern || {x,e3}&lt;br&gt;{x,e8} || 1451.34 || 1.45e3&lt;br&gt;1.45134e3
|-
| ,E{ziffern} || Exponentialschreibweise Gleitkommazahl mit einer fixen Anzahl Ziffern || {x,E3}&lt;br&gt;{x,E8} || 1451.34 || 1.45e3&lt;br&gt;1.4513400e3
|-
| ,t{ziffern} || technische Exponentialschreibweise (Potenzen sind Vielfache von 3) Gleitkommazahl mit einer maximalen Anzahl gültiger Ziffern || {x,t3}&lt;br&gt;{x,t8} || 14513.4 || 14.5E3&lt;br&gt;14.5134E3
|-
| ,T{ziffern} || technische Exponentialschreibweise (Potenzen sind Vielfache von 3) Gleitkommazahl mit einer fixen Anzahl Ziffern || {x,T3}&lt;br&gt;{x,T8} || 14513.4 || 14.5E3&lt;br&gt;14.513400E3
|-
| ,f{ziffern} || Gleitkommazahl mit einer maximalen Anzahl gültiger Ziffern || {x,f3}&lt;br&gt;{x,f8} || 1451.34 || 1.45*10^3&lt;br&gt;1.45134*10^3
|-
| ,F{ziffern} || Gleitkommazahl mit einer fixen Anzahl Ziffern || {x,F3}&lt;br&gt;{x,F8} || 1451.34 || 1.45*10^3&lt;br&gt;1.4513400*10^3
|-
| ,Z{ziffern} || gekürzter Bruch aus einer Dezimalzahl mit einer definierten Anzahl von gültigen Ziffern || {x,Z4} || 203.2 || 1016/5
|-
| ,einheit    || es wird nur die Einheit '''ohne Zahlenwert''' dargestellt || {=x,einheit} || 32V/m || V/m
|}

===für Vektoren, Matrizen und Mengen können weiters folgende Parameter angegeben werden===
{| class="wikitable" style="text-align: left; width: 100%;
| Format || Bedeutung || Beispiel || Wert || Ausgabe
|-
| ,line || gibt den Vektorn in einer Zeile an || {x,line} || [2,3,4] || (2&amp;#x007C;3&amp;#x007C;4)
|-
| ,input || gibt den Vektorn so an, wie er auch eingegeben werden kann || {x,input} || [2,3,4] || [2,3,4]
|-
| ,set || gibt eine Menge mit Mengenklammern an || {x,set} || [2,3,4] || {2,3,4}
|-
| ,list || gibt eine Menge ohne Klammern an || {x,list} || [2,3,4] || 2,3,4
|-
| ,frac || stellt eine Menge mit 2 oder 3 Elementen als Bruch oder gemischten Bruch dar || {x,frac} || [2,3,4] || 2 3/4
|}

===für allgemeine Funtionen können folgende Parameter angegeben werden===
{| class="wikitable" style="text-align: left; width: 100%;
| Format || Bedeutung || Beispiel || Wert || Ausgabe
|-
| ;term || lässt alle Malzeichen zwischen Variablen und Zahlenwerten weg. || {=x^2*y+2*x^2*y^3;term} ||  || x²y+2x²y³
|-
|}

=== für Polynome und gebrochen rationale Funktionen mit numerischen Koeffizienten in einer Variablen können folgende Parameter angegeben werden===
siehe auch [[Berechnungen#Polynome]]
{| class="wikitable" style="text-align: left; width: 100%;
| Format  || Bedeutung
|-
| ;pnPN   || Pole und Nullstellen mit 1 bei der kleinsten Potenz der Polynomvariablen. 
|-
| ;pnPN1  || Pole und Nullstellen mit 1 bei der höchsten Potenz der Polynomvariablen.
|-
| ;pnF1   || Faktordarstellung mit 1 bei der niedrigsten Potenz der Polynomvariable in Zähler und Nenner und steigenden Potenzen
|-
| ;pnF1F  || Faktordarstellung mit 1 bei der niedrigsten Potenz der Polynomvariable in Zähler und Nenner und fallende Potenzen
|-
| ;pnFn   || Faktordarstellung mit 1 bei der höchsten Potenz der Polynomvariable in Zähler und Nenner und steigenden Potenzen
|-
| ;pnFnF  || Faktordarstellung mit 1 bei der höchsten Potenz der Polynomvariable in Zähler und Nenner und fallende Potenzen
|-
| ;pnF1i  || Faktordarstellung mit negativen Potenzen mit 1 bei der niedrigsten Potenz der Polynomvariable in Zähler und Nenner und steigenden Potenzen
|-
| ;pnF1Fi || Faktordarstellung mit negativen Potenzen mit 1 bei der niedrigsten Potenz der Polynomvariable in Zähler und Nenner und fallende Potenzen
|-
| ;pnFni  || Faktordarstellung mit negativen Potenzen mit 1 bei der höchsten Potenz der Polynomvariable in Zähler und Nenner und steigenden Potenzen
|-
| ;pnFnFi || Faktordarstellung mit negativen Potenzen mit 1 bei der höchsten Potenz der Polynomvariable in Zähler und Nenner und fallende Potenzen
|-
| ;pnN1   || Faktordarstellung mit 1 bei der niedrigsten Potenz der Polynomvariable im Nenner und steigenden Potenzen
|-
| ;pnN1F  || Faktordarstellung mit 1 bei der niedrigsten Potenz der Polynomvariable im Nenner und fallende Potenzen
|-
| ;pnZ1   || Faktordarstellung mit 1 bei der niedrigsten Potenz der Polynomvariable im Zähler und steigenden Potenzen
|-
| ;pnZ1F  || Faktordarstellung mit 1 bei der niedrigsten Potenz der Polynomvariable im Zähler und fallende Potenzen
|-
| ;pnNn   || Faktordarstellung mit 1 bei der höchsten Potenz der Polynomvariable im Nenner und steigenden Potenzen
|-
| ;pnNnF  || Faktordarstellung mit 1 bei der höchsten Potenz der Polynomvariable im Nenner und fallende Potenzen
|-
| ;pnZn   || Faktordarstellung mit 1 bei der höchsten Potenz der Polynomvariable im Zähler und steigenden Potenzen
|-
| ;pnZnF  || Faktordarstellung mit 1 bei der höchsten Potenz der Polynomvariable im Zähler und fallende Potenzen
|-
| ;pnN1i  || Faktordarstellung mit negativen Potenzen mit 1 bei der niedrigsten Potenz der Polynomvariable im Nenner und steigenden Potenzen
|-
| ;pnN1Fi || Faktordarstellung mit negativen Potenzen mit 1 bei der niedrigsten Potenz der Polynomvariable im Nenner und fallende Potenzen
|-
| ;pnZ1i  || Faktordarstellung mit negativen Potenzen mit 1 bei der niedrigsten Potenz der Polynomvariable im Zähler und steigenden Potenzen
|-
| ;pnZ1Fi || Faktordarstellung mit negativen Potenzen mit 1 bei der niedrigsten Potenz der Polynomvariable im Zähler und fallende Potenzen
|-
| ;pnNni  || Faktordarstellung mit negativen Potenzen mit 1 bei der höchsten Potenz der Polynomvariable im Nenner und steigenden Potenzen
|-
| ;pnNnFi || Faktordarstellung mit negativen Potenzen mit 1 bei der höchsten Potenz der Polynomvariable im Nenner und fallende Potenzen
|-
| ;pnZni  || Faktordarstellung mit negativen Potenzen mit 1 bei der höchsten Potenz der Polynomvariable im Zähler und steigenden Potenzen
|-
| ;pnZnFi || Faktordarstellung mit negativen Potenzen mit 1 bei der höchsten Potenz der Polynomvariable im Zähler und fallende Potenzen
|-
|}

* Mit Nullstellen und Polen: 
:[[Datei:ClipCapIt-211201-194105.PNG]]

* Mit positiven Potenzen:
:[[Datei:ClipCapIt-211201-194144.PNG]]

* Mit negativen Potenzen:
:[[Datei:ClipCapIt-211201-194214.PNG]]

