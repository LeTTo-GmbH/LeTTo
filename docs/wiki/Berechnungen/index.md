# Berechnungen

<!-- Inhaltsverzeichnis -->
<div id="toc"></div>

##  Allgemeines
Berechnungen werden in mehreren Bereichen der Frageerstellung verwendet und bilden die Basis für [Berechnungsfrage](../Fragetypen/index.md#berechnungsfrage-) und [Mehrfachberechnungsfrage](../Fragetypen/index.md#mehfachberechnungsfrage).

Alle Berechnungen unterstützen [Einheiten](../Einheit/index.md) und symbolische Auswertung.

## Grundsätzlicher Aufbau der Ergebnis-Berechnung bei Fragen mit Berechnungen
![BerechnungSchema.png](600px-BerechnungSchema.png)
Die Berechnung und die Beurteilung einer Frage teilt sich in 3 grundsätzliche Schritte:
* Berechnnug der geschlossenen Lösung (Formel) aus den Maxima-Feldern
* Berechnung des Ergebnisses einer Frage durch Einsetzen der Zahlenwerte aus den Datensätzen in die geschlossene Lösung
* Beurteilung der Schülereingabe durch Vergleich mit dem Ergebnis

## Konstante
Alle Konstante welche in Letto definiert sind beginnen mit einem Prozentzeichen. Verwendet man den Variablennamen ohne Prozenzzeichen, so wird die Konstante wie eine Variable mit dem Wert der Konstanten verwendet.

Liste der definierten Konstanten:

| Name      | Wert                                                       | Beschreibung                                                                                                            |
|-----------|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| %i        | i                                                          | komplexer Parameter als Lösung der Gleichung x^2=-1                                                                     |
| %j        | i                                                          | komplexer Parameter als Lösung der Gleichung x^2=-1<br><b>Wichtig:</b> Wir nur vom Parser unterstützt, nicht von Maxima |
| %e        | 2.718281828459045                                          | Eulersche Zahl                                                                                                          |
| %pi       | 3.141592653589793                                          | Kreiszahl                                                                                                               |
| %mu0      | magnetische Feldkonstante                                  | 4*%pi*1E-7'Vs/Am'                                                                                                       |
| %m0       | magnetische Feldkonstante (alt, wird bald entfernt werden) | 4*%pi*1E-7'Vs/Am'                                                                                                       |
| %epsilon0 | elektrische Feldkonstante                                  | 8.85418781762039E-12'As/Vm'                                                                                             |
| %e0       | elektrische Feldkonstante (alt, wird bald entfernt werden) | 8.85418781762039E-12'As/Vm'                                                                                             |
| %c0       | Lichtgeschwindigkeit                                       | 299792458'm/s'                                                                                                          |
| %Qe       | Elementarladung                                            | 1.602176620898E-19As                                                                                                    |
| %g        | Erdbeschleunigung                                          | 9.81'm/s^2'                                                                                                             |
| %NA       | Avogadro Konstante                                         | 6.02214085774E23/mol                                                                                                    |
| %k        | Stefan Bolzman Konstante                                   | 1.3806485279E-23'J/K'                                                                                                   |
| %R0       | Universelle Gaskonstante                                   | 8.314459848'J/Kmol'                                                                                                     |
| %h        | planksches Wirkungsquantum                                 | 6.6260704081E-34Js                                                                                                      |


## Berechnung mit Maxima
* Maxima wird **nur für symbolische Berechnungen** bei der Erstellung von Beispielen verwendet. Hierbei wird, wie schon oberhalb im Schema angegeben, zuerst die Moodle.mac geladen, dann das [Maxima-Feld](../BeispielsammlungEditieren/index.md#maxima-feld) berechnet und anschließend die Maxima-Felder aller Teilfragen. Das Ergebnis der Berechnung wird dann als symbolischer Ausdruck im Lösungfeld eingetragen.
* Da zum Zeitpunkt der **Maxima-Berechnung keine Datensätze** vorhanden sind, kann keine numerische Berechnung in Maxima durchgeführt werden, welche die [Datensätze](../Datensätze/index.md) benötigt. Dies muss der interne Parser zum Zeitpunkt des Online-Test-Laufes erledigen. Numerische Berechnungen, welche der interne Parser nicht kann können deshalb auch nicht mit Maxima berechnet werden.
* Da das Lösungsfeld, welches mit Maxima berechnet wird symbolisch ausgewertet wird, können in Maxima sämtliche symbolischen Berechnungsverfahren angewendet werden, welche ein symbolisches Ergebnis liefern und keine numerischen Werte der Datensätze benötigen.
* Reicht im Maximafeld die Zeilenlänge nicht aus ist es möglich einen defninierten Zeilenumbruch zu realisieren. Schreiben Sie dazu "&#92;" (einfacher Backslash) am Ende der Zeile.
* **Funktionsdeklarationen** wie **f(x):=**x^2 mit Doppelpunkt-Ist-Gleich sind im Maxima-Feld nur eingeschränkt bis gar **nicht verwendbar**, da sie vom Parser nicht unterstützt werden.
* **Mengen von Maxima** sind in LeTTo n**icht verwendbar**. LeTTo verwender hierzu eigene Funktionen des Parsers welche mit "set" beginnen und auf Vektoren basieren.

###  Berechnungen mit "Vorberechnung" und Maxima (Parser nicht angehakt)
* Es werden die Datensätze ohne Einheiten vor der Durchrechnung des Maxima-Feldes an Maxima gesendet
* Im Maxima-Feld werden durch den Preprozessor alle Einheiten von allen konstanten Werten entfernt
* Die Ergebnisse nach der Maxima-Durchrechnung sind somit alle ohne Einheit
* Der Postpozesser fügt an alle Ergebnisse der Maxima-Berechnung die definierten Einheiten an

####  Einheitendfinition für den Postprozessor (nur bei Berechnung mit Vorberechnung ohne Parser wirksam!)
* Definition einer Einheit mit der Funktion unit in einem Kommentar
* Setzen der Einheit Volt (V) für alle Variablen die mit U beginnen
  <pre>//unit(U*)=V</pre>
* Setzen der Einheit Ampere(A) für alle Variablen die mit I oder ix beginnen
  <pre>//unit(I*,ix*)=A</pre>

## Berechnung mit dem internen Parser
* Der interne Parser kann durch Wahl der Checkbox "Parser" anstatt von Maxima für die Berechnung des Maxima-Feldes verwendet werden.
* Jedenfalls wird der Parser zur Test-Laufzeit für die Berechnung des Ergebnisses einer Frage aus Lösung und Datensätzen und zum Berechnen der Schülereingabe verwendet.

### Operatoren
####  VORSICHT mit MAXIMA
* Einige Operatoren sind in **Maxima anders**, oder **nicht definiert**. Möchte man im Maximafeld die Operatoren des Parsers-verwenden, so muss das gesamte Maxima-Feld **mit dem Parser gerechnet** werden. Man verliert dadurch jedoch die Vorteile der Maxima-Berechnung.
* Alternativ kann man statt der Operatoren auch **Funktionen verwenden** (zB: ne() statt != ). Diese werden dann von Maxima zwar nicht ausgewertet, die Berechnung bleibt aber trotzdem korrekt und kann mit Maxima durchgeführt werden.
* Es gibt einige Funktionen welche in **Maxima existieren** aber im **Parser nicht, oder mit anderem Syntax**.
  * Wenn diese von Maxima nicht ausgewertet werden können, da sie **Datensätze** enthalten welche zum Auswertezeitpunkt von Maxima
    noch **nicht mit Werten belegt** sind muss **"Vorberechnung"** in der Frage angehakt werden damit die Datensätze schon vor dem
    Durchlauf von Maxima eingesetzt werden.
  * Manche Funktionen sind syntaktisch nicht funktional aufgebaut und können deshalb nicht vom Parser ausgewertet werden - in diesem
    Fall darf in der Frage das Hackerl "Parser" nicht angehakt werden oder es muss eine andere Funktion verwendet werden (wie etwa wenn statt if)
* Wenn "Parser" nicht angehakt ist bleiben alle Funktionen welche von Maxima nicht unterstützt werden von Maxima unberechnet und werden dann bei der Lösungsberechnung vom Parser ausgewertet.
* Wenn "Parser" angehakt ist werden nur ausgewählte Funktionen (siehe weiter unten) von Maxima ausgewertet. Alle anderen Funktionen werden vom Parser ausgewertet.

Liste der problematischen Funktionen:

| Funktion in Maxima                 | Funktion im Parser          | Beschreibung  |
|------------------------------------|-----------------------------|---------------|
| if bedingung then wahr else falsch | if(bedingung,wahr,falsch)   | Wenn-Funktion |
|                                    | wenn(bedingung,wahr,falsch) | Wenn-Funktion |

#### Infix Operatoren
##### arithmetische Operatoren

| Operator              | Priorität | Beschreibung                                                                 | Beispiel             | Ergebnis  |
|-----------------------|-----------|------------------------------------------------------------------------------|----------------------|-----------|
| +                     | 40        | Addition                                                                     | 4+5                  | 9         |
| -                     | 40        | Subtraktion                                                                  | 6-2                  | 4         |
| *                     | 50        | Multiplikation                                                               | 4*5                  | 20        |
| /                     | 51        | Division                                                                     | 20/4                 | 5         |
| %                     | 51        | Divisionsrest                                                                | 104%20               | 4         |
| &#124; &#124; | 60        | Parallelschaltung                                                            | x &#124; &#124; y    | x*y/(x+y) |
| ^                     | 90        | Potenz                                                                       | 2^3                  | 8         |
| .*.                   | 200       | Operator der intern für eine fehlende bindende Multiplikation verwendet wird | 4x                   | 4*x       |


##### Bitoperatoren

| Operator | Priorität | Beschreibung                              | Beispiel       | Ergebnis    |
|----------|-----------|-------------------------------------------|----------------|-------------|
| &#124;   | 20        | Bitweise oder logisches ODER              |  9&#124;5 <br> true&#124;false | 13 <br>true |
| or       | 20        | Bitweise oder logisches ODER              | 9 or 5         | 13          |
| &amp;    | 21        | Bitweise oder logisches UND               | 13&amp;10      | 8           |
| and      | 21        | Bitweise oder logisches UND               | 13 and 10      | 8           |
| xor      | 22        | Bitweise oder logisches exklusiv oder XOR | 13 xor 10      | 7           |
| imp      | 23        | Bitweise oder logisches impliziert IMP    | 13 imp 10      | 8           |
| &lt;&lt; | 35        | Bitweise links schieben                   | 5&lt;&lt;2     | 20          |
| &gt;&gt; | 35        | Bitweise rechts schieben                  | 8&gt;&gt;2     | 2           |


##### Vergleichsoperatoren

| Operator | Priorität | Beschreibung         | Beispiel |
|----------|-----------|----------------------|----------|
| =        | 3         | Gleichungsoperator   | x=y      |
| ==       | 30        | Gleichungsoperator   | x==y     |
| !=       | 30        | Ungleichungsoperator | x!=y     |
| &lt;     | 32        | Kleiner              | x&lt;y   |
| &lt;=    | 32        | Kleiner gleich       | x&lt;=y  |
| &gt;     | 32        | größer               | x&gt;y   |
| &gt;=    | 32        | größer gleich        | x&gt;=y  |

##### Organisative Operatoren

| Operator | Priorität | Beschreibung                                                                        | Beispiel | Ergebnis |
|----------|-----------|-------------------------------------------------------------------------------------|----------|----------|
| ,        | 0         | Listen-Trennzeichen                                                                 | x,y      |          |
| $        | 1         | Trennzeichen zwischen mehreren Berechnungen                                         |          |          |
| ;        | 1         | Trennzeichen zwischen mehreren Berechnungen                                         |          |          |
| :        | 2         | Zuweisung an eine Variable auf der linken Seite                                     | x:4/12   | 1/3      |
| ::       | 2         | Zuweisung an eine Variable auf der linken Seite ohne die rechte Seite zu optimieren | x::4/12  | 4/12     |


#### Prefix Operatoren

| Operator | Priorität | Beschreibung                                          | Beispiel  | Ergebnis                                                                |
|----------|-----------|-------------------------------------------------------|-----------|-------------------------------------------------------------------------|
| +        | 45        | positives Vorzeichen                                  | +5        | 5                                                                       |
| -        | 45        | negatives Vorzeichen                                  | -(-5)     | 5                                                                       |
| ~        | 95        | bitweise Inversion einer 64bit-Ganzzahl               | ~0x0F0F   | 0xFFFFFFFFFFFFF0F0                                                      |
| !        | 120       | logisches NOT                                         | !(3&lt;4) | false                                                                   |
| ++       | 130       | Inkrement von Ganzzahlen                              | ++x       | erhöht x um eins und gibt das Ergebnis nach der Erhöhung zurück         |
| --       | 130       | Dekrement von Ganzzahlen                              | --x       | vermindert x um eins und gibt das Ergebnis nach der Verminderung zurück |
| %        | 200       | Prefix für Namen, welche als Konstante definiert sind | %pi       | 3.141592653589793                                                       |


#### Suffix Operatoren

| Operator | Priorität | Beschreibung             | Beispiel | Ergebnis                                                                    |
|----------|-----------|--------------------------|----------|-----------------------------------------------------------------------------|
| ++       | 135       | Inkrement von Ganzzahlen | x++      | erhöht x um eins und gibt den Variablenwert vor der Erhöhung zurück         |
| --       | 135       | Dekrement von Ganzzahlen | x--      | vermindert x um eins und gibt den Variablenwert vor der Verminderung zurück |


### Klammern
* ( ) runde Klammern werden für mathematische Ausdrücke zur Klammerung verwendet
* { } geschwungene Klammer werden im Angabetext für die Namen der Datensätze verwendet
* &#91; &#93; eckige Klammern werden für Vektoren und Matrizen verwendet. VORSICHT! Der Index in eckigen Klammer beginnt bei 1 (wegen Maxima-Kompatibilität). Allen anderen Indizes sind Nullbasiert (zB. vget, etc.)!

### Funktionen
#### Funktionen für Ganzzahlen

| Funktion                                | Beschreibung                                                                                                                                                                | Beispiel                    | Ergebnis           |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------------|
| band                                    | bitweises UND [DEMO-Beispiel](../../demobsp.html?id=3514)                                                                                                                   | band(4,12)                  | 4                  |
| bor                                     | bitweises ODER                                                                                                                                                              | bor(4,1)                    | 5                  |
| bxor                                    | bitweises EXKLUSIV ODER                                                                                                                                                     | band(4,5)                   | 1                  |
| bimp                                    | bitweises Parameter1 impliziert Parameter2                                                                                                                                  | bimp(13,10)                 | 8                  |
| binv                                    | bitweises NICHT mit 8 bit                                                                                                                                                   | binv(0x0F)                  | 0xF0               |
| shl                                     | Schiebe Ganzzahl bitweise nach links                                                                                                                                        | shl(8,2)                    | 32                 |
| shr                                     | Schiebe Ganzzahl bitweise nach rechts                                                                                                                                       | shr(8,2)                    | 2                  |
| div                                     | Ganzzahldivision, Ergebnis wird abgeschnitten                                                                                                                               | div(5,2)                    | 2                  |
| inv8                                    | bitweise Invertieren und die letzten 8 Bit bestimmen                                                                                                                        | inv8(0b1001)                | 0b11110110         |
| inv16                                   | bitweise Invertieren und die letzten 16 Bit bestimmen                                                                                                                       | inv16(0xF0)                 | 0xFF0F             |
| inv32                                   | bitweise Invertieren und die letzten 32 Bit bestimmen                                                                                                                       | inv32(0xF0)                 | 0bFFFFFF0F         |
| inv64                                   | bitweise Invertieren und die letzten 64 Bit bestimmen                                                                                                                       | inv64(0xF0)                 | 0bFFFFFFFFFFFFFF0F |
| byte                                    | Zahl in eine Ganzzahl wandeln und die letzten 8bit der Zahl Abschneiden, Einheit geht verloren                                                                              | byte(34.2)                  | 34                 |
| word                                    | Zahl in eine Ganzzahl wandeln und die letzten 16bit der Zahl Abschneiden, Einheit geht verloren                                                                             | word(34.2)                  | 34                 |
| int                                     | Zahl in eine Ganzzahl wandeln und die letzten 32bit der Zahl Abschneiden, Einheit geht verloren                                                                             | int(34.2)                   | 34                 |
| long                                    | Zahl in eine Ganzzahl wandeln , Einheit geht verloren                                                                                                                       | long(34.2)                  | 34                 |
| [parity](/notimplemented/index.md)      | Paritätsberechnung : parity(Parität,Codewortlänge,Datenwort)                                                                                                                | parity(even,7,"xy")         |                    |
| [blockparity](/notimplemented/index.md) | Kreuz oder Blockparität : blockparity(Parität,Codewortlänge,Codewortanzahl,Datenwort)                                                                                       | blockparity(even,7,3,"abc") |                    |
| [bcd](/notimplemented/index.md)         | Wandelt in eine Long-Zahl in ein Feld aus BCD-kodierten Zahlen um                                                                                                           | bcd(124)                    | &#91;1,2,4&#93;    |
| [code](/notimplemented/index.md)        | Code aus mehreren Codeworten zusammensetzen : code(Codewortlänge,Datenwort)                                                                                                 | code(5,4,3,5)               | 0b1000001100101    |
| [hamming](/notimplemented/index.md)     | Bestimmt den Hamming-Abstand von mehreren Codeworten                                                                                                                        | hamming(1,2,4,8,16)         | 2                  |
| [komplement](/notimplemented/index.md)  | Bildet das Zweierkomplement mit einer negativen Zahl mit einer bestimmten Bitanzahl, fehlt die Bitanzahl, so wird ein 32Bit-2er-komplement gebildet                         | komplement(-5,8)            | 0b11111011         |
| [bitstream](./func/bitstream/index.md)  | Erzeugt aus einer Ganzzahl einen Bitstrom als String mit einer definierten Anzahl von Bit (MSB werden nötigenfalls mit 0 gefüllt) : bitstream(Daten,Bitanzahl,Gruppengröße) | bitstream(0x184,12,4)       | "0001 1000 0100"   |
| dechex                                  | Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Hexadezimal-String mit Präfix `0x` aus.                                                                                   | dechex(12)                   | "0xC"              |
| hex                                     | Alias zu `dechex`: Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Hexadezimal-String aus.                                                                                | hex(12)                      | "0xC"              |
| decbin                                  | Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Binär-String mit Präfix `0b` aus.                                                                                         | decbin(10)                   | "0b1010"           |
| bin                                     | Alias zu `decbin`: Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Binär-String aus.                                                                                      | bin(10)                      | "0b1010"           |


#### Funktionen für rationale und Ganzzahlen

| Funktion      | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                        | Beispiel                                                 | Ergebnis                                                  |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------|
| kgV           | berechnet das kleinste gemeinsame Vielfache von mehreren Zahlen [DEMO-Beispiel](../../demobsp.html?id=3197)                                                                                                                                                                                                                                                                                                                                         | kgV(3,10)                                                | 30                                                        |
| ggT           | berechnet den größten gemeinsamen Teiler von mehreren Zahlen [DEMO-Beispiel](../../demobsp.html?id=3199)                                                                                                                                                                                                                                                                                                                                            | ggT(12,10)                                               | 2                                                         |
| isprim        | prüft ob die angegebene Zahl eine Primzahl ist [DEMO-Beispiel](../../demobsp.html?id=3200)                                                                                                                                                                                                                                                                                                                                                          | isprim(13)                                               | true                                                      |
| prims         | zerlegt eine Ganzzahl in ihre Primfaktoren [DEMO-Beispiel](../../demobsp.html?id=3201)                                                                                                                                                                                                                                                                                                                                                              | prims(12)                                                | &#91;2,2,3&#93;                                           |
| defracmix     | zerlegt eine rationale Zahl in einen gemischten Bruch aus ganzzahligem Summanden, Zähler und Nenner als Menge<br>Die erhaltene Menge kann mit dem Format-Modfier **frac** als gemischter Bruch dargestellt werden (siehe [Zahlendarstellung](../Zahlendarstellung/index.md)) [DEMO-Beispiel](../../demobsp.html?id=3202)                                                                                                                            | defracmix(14/12)<br>defracmix(-15/12)<br>defracmix(3/12) | &#91;1,2/12&#93;<br>&#91;-1,3,12&#93;<br>&#91;0,3,12&#93; |
| defrac        | zerlegt eine rationale Zahl in Zähler und Nenner als Menge <br>Die erhaltene Menge kann mit dem Format-Modfier **frac** als gemischter Bruch dargestellt werden [DEMO-Beispiel](../../demobsp.html?id=3203)                                                                                                                                                                                                                                         | defrac(14/12)                                            | &#91;13,12&#93;                                           |
| frac          | erzeugt aus einer Menge aus 2 oder 3 Elementen (von defrac) eine rationale Zahl [DEMO-Beispiel](../../demobsp.html?id=3204)                                                                                                                                                                                                                                                                                                                         | frac(&#91;3,7&#93;)<br>frac(&#91;1,2,3&#93;)             | 3/7 <br> 5/3                                              |
| mod           | Mathematische Implementierung von [modulo](https://de.wikipedia.org/wiki/Division_mit_Rest#Modulo): Divisionsrest einer Division mit ganzzahligem Ergebnis [DEMO-Beispiel](../../demobsp.html?id=3205)                                                                                                                                                                                                                                              | mod(5,2) <br> mod(6.2,2.5) <br> mod(-4,3)                | 1<br>1.2 <br> 2                                           |
| mod2          | Symmetrische Implementierung von [modulo](https://de.wikipedia.org/wiki/Division_mit_Rest#Modulo): Divisionsrest einer Division mit ganzzahligem Ergebnis <br>Der Unterschied zu mod liegt in der Behandlung von negativen Zahlen des ersten Arguments <br>Siehe auch Divisionsrest des Parser-Operators % [Berechnungen arithmetische-operatoren-](../Berechnungen/index.md#arithmetische-operatoren-) [DEMO-Beispiel](../../demobsp.html?id=3206) | mod2(5,2) <br> mod2(6.2,2.5) <br> mod2(-4,3)             | 1<br>1.2 <br> -1                                          |
| isNearInteger | prüft ob eine Zahl nahe genug an einer Ganzzahl liegt, um als Ganzzahl interpretiert zu werden. Es wird die Toleranz der Frage verwendet                                                                                                                                                                                                                                                                                                            | isNearInteger(3.00000000001) <br> isNearInteger(3.1)     | true <br> false                                           |
| ni            | Kurzform von isNearInteger - prüft ob eine Zahl nahe genug an einer Ganzzahl liegt, um als Ganzzahl interpretiert zu werden. Es wird die Toleranz der Frage verwendet                                                                                                                                                                                                                                                                               | ni(3.00000000001) <br> ni(3.1)                           | true <br> false                                           |

#### Funktionen für Winkel im Gradmaß

| Funktion  | Beschreibung                                                                                                                                                                         | Beispiel                                                           | Ergebnis                          |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|-----------------------------------|
| degmix    | zerlegt einen Winkel im Bogenmaß in einen Winkel in Grad, Minuten und Sekunden in einem Vektor [DEMO-Beispiel](../../demobsp.html?id=3194)                                           | degmix(0.5)                                                        | &#91;28,38,52.4031239082&#93;     |
| deg       | erzeugt aus einem Vektor mit Grad, Minuten und Sekunden als Zahlenwerte oder einen WinkelString einen Winkel im Bogenmaß [DEMO-Beispiel](../../demobsp.html?id=3195)                 | deg(&#91;2,15,22&#93;) <br> deg(&quot;2°15&#39;22&#39;&#39;&quot;) | 2.25611111111°                    | 
| degstring | erzeugt aus einem Vektor mit Grad, Minuten und Sekunden als Zahlenwerte oder einen Winkel im Bogenmaß einen String der Winkeldarstellung [DEMO-Beispiel](../../demobsp.html?id=3196) | degstring(0.5)                                                     | &quot;2°15&#39;22&#39;&#39;&quot; |

#### boolesche(boolsche) Funktionen

| Funktion  | Beschreibung                                                                                                                                                                                                                                             | Beispiel               | Ergebnis |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|----------|
| eq        | gleich eq(wert1,wert2),eq(wert1,wert2,toleranz),eq(wert1,wert2,toleranz,absolut) [DEMO-Beispiel](../../demobsp.html?id=3182)                                                                                                                             | eq(4,4)                | true     |
| eqruntime | symbolischer Vergleich, welcher **symbolisch erst bei der Ergebnisberechnung** ausgeführt wird. Muss verwendet werden, wenn bei Vergleichen symbolische Antworten von Schülern (Q0,Q1,...) verwendet werden. [DEMO-Beispiel](../../demobsp.html?id=3183) | eqruntime(x+3*y,3*y+x) | true     |
| ne        | ungleich ne(wert1,wert2),ne(wert1,wert2,toleranz),ne(wert1,wert2,toleranz,absolut) [DEMO-Beispiel](../../demobsp.html?id=3184)                                                                                                                           | ne(6,4)                | true     |
| ge        | größer gleich ge(wert1,wert2),ge(wert1,wert2,toleranz),ge(wert1,wert2,toleranz,absolut) [DEMO-Beispiel](../../demobsp.html?id=3185)                                                                                                                      | ge(6,4)                | true     |
| le        | kleiner gleich le(wert1,wert2),le(wert1,wert2,toleranz),le(wert1,wert2,toleranz,absolut) [DEMO-Beispiel](../../demobsp.html?id=3186)                                                                                                                     | le(6,4)                | false    |
| gt        | größer [DEMO-Beispiel](../../demobsp.html?id=3187)                                                                                                                                                                                                       | gt(6,4)                | true     |
| lt        | kleiner [DEMO-Beispiel](../../demobsp.html?id=3188)                                                                                                                                                                                                      | lt(6,4)                | false    |
| between   | prüft ob Parameter1 kleiner als Parameter2 und Parameter2 kleiner als Parameter 3 . Parameter 4 und 5 können optinal für die Toleranz verwendet werden. [DEMO-Beispiel](../../demobsp.html?id=3189)                                                      | between(3,4,5)         | true     |
| land      | logisches UND [DEMO-Beispiel](../../demobsp.html?id=3190)                                                                                                                                                                                                | land(a&lt;b,b&lt;c)    |          |
| lor       | logisches ODER [DEMO-Beispiel](../../demobsp.html?id=3191)                                                                                                                                                                                               | lor(a&lt;b,b&lt;c)     |          |
| not       | logisches NICHT. Vorsicht ein symbolisches Ergebnis von Maxima liefert not als Prefix-Operator, welcher vom Parser nicht unterstützt wird ( Verwende statt dessen **lnot** ) [DEMO-Beispiel](../../demobsp.html?id=3192)                                 | not(a&lt;b)            |          |
| lnot      | logisches NICHT, wie not jedoch wird es von Maxima nicht ausgewertet [DEMO-Beispiel](../../demobsp.html?id=3193)                                                                                                                                         | lnot(a&lt;b)           |          |


#### Funktionen zu Einheiten

| Funktion      | Beschreibung                                                                                                                                                                                                                                                                                                                                                                            | Beispiel                                                                    | Ergebnis                   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------|
| double        | Zahl in eine Gleitkommazahl umwandeln, die Einheit geht dabei verloren [DEMO-Beispiel](../../demobsp.html?id=3176)                                                                                                                                                                                                                                                                      | double(3.4V)                                                                | 3.4                        |
| float         | Zahl in eine Gleitkommazahl umwandeln, die Einheit geht dabei verloren (wie double)                                                                                                                                                                                                                                                                                                     | float(3.4V)                                                                 | 3.4                        |
| numeric       | verwirft die Einheit, wenn eine vorhanden ist und liefert nur den Zahlenwert (bezogen auf die Einheit!). Bei einer SI-Einheit wird der Zahlenwert bezogen auf die Basiseinheit geliefert, bei dimensonslosen Größen wird der Zahlenwert bezogen auf die verwendete dimensionslose Einheit gewählt. <br> numeric(x)*unit(x) liefert wieder x [DEMO-Beispiel](../../demobsp.html?id=3177) | numeric(2.3mA) <br> numeric(5%)                                             | 0.0023 <br> 5              |
| originnumeric | liefert immer den Zahlenwert einer einheitenbehafteten Größe bezogen auf die vorhandene Einheit. Gibt es keine Originaleinheit da der Wert berechnet wurde wird der Zahlenwert bezogen auf die SI-Grundeinheit genommen. <br> originnumeric(x)*originunit(x) liefert wieder x [DEMO-Beispiel](../../demobsp.html?id=3178)                                                               | originnumeric(2.3mA) <br> originnumeric(2.3mA*2Ohm) <br> originnumeric(15°) | 2.3 <br> 0.0046 <br> 15    |
| removeunit    | entfernt bei einem Ausdruck alle Einheiten und ersetzt dabei alle einheitenbehafteten Größen durch den Zahlenwert bezogen auf die BasisEinheit des SI-Systems [DEMO-Beispiel](../../demobsp.html?id=3179)                                                                                                                                                                               | removeunit(t*5'm/s'+4cm)                                                    | t*5+0.04                   |
| unit          | gibt die SI-Einheit eines einheitenbehafteten Wertes mit dem Zahlenwert 1 ohne Einheitenvielfache zurück. <br> numeric(x)*unit(x) liefert wieder x [DEMO-Beispiel](../../demobsp.html?id=3180)                                                                                                                                                                                          | unit(3.1kA) <br> unit(5%)                                                   | 1A <br> 1%                 |
| originunit    | gibt die SI-Einheit eines einheitenbehafteten Wertes mit dem Zahlenwert 1 zurück. <br> originnumeric(x)*originunit(x) liefert wieder x [DEMO-Beispiel](../../demobsp.html?id=3181)                                                                                                                                                                                                      | unit(3.1kA) <br> unit(5%)                                                   | 1kA <br> 1%                |
| splitunit     | Zerlegt einen numerischen Wert in Zahlenwert und die originale/optimale Einheit mit Zahlenwert 1 als Feld mit Zahlenwert als Index 0 und Einheit als Index 1                                                                                                                                                                                                                            | splitunit(1300kVA)                                                          | &#91;1300,1kVA&#93;        |
| splitoptunit  | Zerlegt einen numerischen Wert in Zahlenwert und die optimale Einheit mit Zahlenwert 1 als Feld mit Zahlenwert als Index 0 und Einheit als Index 1                                                                                                                                                                                                                            | splitoptunit(1300kVA)                                                       | &#91;1.3,1MVA&#93;         |
| unitopt       | liefert bei einem einheitenbehafteten Wert die optimale SI-Einheit mit optimierten Einheitenvielfachen  | unitopt(1300kVA)                                                       | 1.3MVA                     |
| eh            | Liefert zu einem numerischen Wert die zugehörige Einheit als Wert 1 zurück; bei einem einheitenlosen Wert wird `1` geliefert. | eh(2.3mA) | 1mA |
| dB            | Wandelt einen Zahlenwert in eine nicht skalierende [Dezibel](../Dezibel/index.md)-Einheit um. Einheitenlos wird in dB20 gewandelt, mit den Einheiten V,mV,uV,W,mW,uW wird in die zugehörige dB-Einheit gewandelt. [DEMO-Beispiel](../../demobsp.html?id=3213)                                                                                                                           | dB(100) <br> dB(100)+1                                                      | 40 dB<sub>20</sub> <br> 41 |
| fromdB        | Wandelt eine nicht skalierende [Dezibel](../Dezibel/index.md)-Einheit in einen normalen Zahlenwert um [DEMO-Beispiel](../../demobsp.html?id=3214)                                                                                                                                                                                                                                       | fromdB(40)                                                                  | 100                        |
| todB          | versieht einen Zahlenwert mit der skalierenden [Dezibel](../Dezibel/index.md)-Einheit dB welche mit 20*log<sub>10</sub> berechnet wird [DEMO-Beispiel](../../demobsp.html?id=3215)                                                                                                                                                                                                      | todB(100)<br> todB(100)*2                                                   | 40dB <br> 200              |
| dB10          | wandelt eine Zahl in einen [Dezibel](../Dezibel/index.md) Wert dB<sub>10</sub> mit 10dB pro Dekade [DEMO-Beispiel](../../demobsp.html?id=3216)                                                                                                                                                                                                                                          | dB10(100)                                                                   | 20dB<sub>10</sub>          |
| fromdB10      | wandelt einen [Dezibel](../Dezibel/index.md) Wert mit 10dB pro Dekade in den Ausgangswert [DEMO-Beispiel](../../demobsp.html?id=3217)                                                                                                                                                                                                                                                   | fromdB10(20)                                                                | 100                        |
| dBW           | wandelt eine Leistung in einen [Dezibel](../Dezibel/index.md) Wert dB<sub>W</sub> mit 10dB pro Dekade [DEMO-Beispiel](../../demobsp.html?id=3218)                                                                                                                                                                                                                                       | dBW(100)                                                                    | 20dB<sub>W</sub>           |
| fromdBW       | wandelt einen [Dezibel](../Dezibel/index.md) Wert mit 10dB pro Dekade in eine Leistung [DEMO-Beispiel](../../demobsp.html?id=3219)                                                                                                                                                                                                                                                      | fromdBW(20)                                                                 | 100W                       |
| dBm           | Wandelt eine Leistung in dBm um. Bezugsleistung ist 1 mW: `10*log10(P/1mW)`. Bei komplexen Leistungen wird der Betrag verwendet; vorhandene dBW/dBm/dBu-Werte werden entsprechend umgerechnet. | dBm(1mW) | 0dBm |
| fromdBm       | Wandelt einen dBm-Wert in eine Leistung zurück. Ein einheitenloser Zahlenwert wird als dBm interpretiert und als Leistung in mW zurückgegeben. | fromdBm(0) | 1mW |
| dBu           | Wandelt eine Leistung in den in LeTTo verwendeten dBu-Pegel mit Bezugsleistung 1 µW um: `10*log10(P/1uW)`. **Hinweis:** Dies ist die LeTTo-Definition von dBu und nicht die übliche Spannungsdefinition bezogen auf 0,775 V. | dBu(1uW) | 0dBu |
| fromdBu       | Wandelt einen LeTTo-dBu-Wert in eine Leistung zurück. Ein einheitenloser Zahlenwert wird als dBu interpretiert und als Leistung in µW zurückgegeben. | fromdBu(0) | 1uW |
| dBV           | Wandelt eine Spannung in dBV um. Bezugsspannung ist 1 V: `20*log10(U/1V)`. Bei komplexen Spannungen wird der Betrag verwendet; vorhandene dBV/dBmV/dBuV-Werte werden entsprechend umgerechnet. | dBV(1V) | 0dBV |
| fromdBV       | Wandelt einen dBV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBV interpretiert und als Spannung in V zurückgegeben. | fromdBV(0) | 1V |
| dBmV          | Wandelt eine Spannung in dBmV um. Bezugsspannung ist 1 mV: `20*log10(U/1mV)`. Bei komplexen Spannungen wird der Betrag verwendet. | dBmV(1mV) | 0dBmV |
| fromdBmV      | Wandelt einen dBmV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBmV interpretiert und als Spannung in mV zurückgegeben. | fromdBmV(0) | 1mV |
| dBuV          | Wandelt eine Spannung in dBuV um. Bezugsspannung ist 1 µV: `20*log10(U/1uV)`. Bei komplexen Spannungen wird der Betrag verwendet. | dBuV(1uV) | 0dBuV |
| fromdBuV      | Wandelt einen dBuV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBuV interpretiert und als Spannung in µV zurückgegeben. | fromdBuV(0) | 1uV |


#### arithmetische Funktionen

| Funktion | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Beispiel                                       | Ergebnis             |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------------|
| cround   | Rundet die Zahl kaufmännisch, der zweite Parameter gibt die Anzahl der Kommastellen an, ohne 2.Parameter wird auf Ganzzahlen gerundet, bei komplexen Zahlen wird Betrag und Winkel in Grad gerundet. [DEMO-Beispiel](../../demobsp.html?id=3220)                                                                                                                                                                                                                                                                                                                                                           | cround(23.535,2)<br>cround(2.435arg34.5364°,1) | 23.54<br>2.4arg34.5° |
| ccround  | Rundet die Zahl kaufmännisch, der zweite Parameter gibt die Anzahl der Kommastellen an, bei komplexe Zahlen wird Real und Imaginärteil gerundet. [DEMO-Beispiel](../../demobsp.html?id=3221)                                                                                                                                                                                                                                                                                                                                                                                                               | ccround(2.4534+5.645*%i,2)                     | 2.45+5.65i           |
| round    | Rundet die Zahl kaufmännisch, aus Kompatibilitätsgründen zu Maxima hat round nur einen Parameter [DEMO-Beispiel](../../demobsp.html?id=3222)                                                                                                                                                                                                                                                                                                                                                                                                                                                               | round(23.535)                                  | 24                   |
| ground   | Rundet die Zahl auf die im zweiten Parameter angegebenen gültigen Ziffern [DEMO-Beispiel](../../demobsp.html?id=3223)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | ground(2453.43,2)                              | 2500                 |
| floor    | Rundet auf die größte ganze Zahl, welche kleiner oder gleich x ist [DEMO-Beispiel](../../demobsp.html?id=3224)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | floor(24.5)                                    | 24                   |
| trunc    | Schneidet die Zahl nach dem Komma ab [DEMO-Beispiel](../../demobsp.html?id=3226)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | trunc(24.5)                                    | 24                   |
| ceiling  | ceiling(x) Rundet auf die kleinste ganze Zahl, welche größer oder gleich x ist [DEMO-Beispiel](../../demobsp.html?id=3227)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | ceiling(13.2)                                  | 14                   |
| pow      | Potenzfunktion [DEMO-Beispiel](../../demobsp.html?id=3229)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | pow(2,3)                                       | 8                    |
| par      | Parallelschaltung von Widerständen [DEMO-Beispiel](../../demobsp.html?id=3230)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | par(x,y)                                       | x*y/(x+y)            |
| min      | Minimum von mehrere Werten suchen [DEMO-Beispiel](../../demobsp.html?id=3231)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | min(3,5,1)                                     | 1                    |
| max      | Maximum von mehreren Werten suchen [DEMO-Beispiel](../../demobsp.html?id=3232)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | max(3,5,1)                                     | 5                    |
| random   | Zufallszahl aus einem definierten Zahlenbereich random(minimal,maximal)<br>VORSICHT! Die Zufallszahl wird bei jedem Aufruf neu berechnet, weshalb sich der Wert bei jedem Anzeigevorgang einer Frage ändert. Sollte sich der berechnete Wert für eine Schülerangabe zwischen Fragestellung und Ergebniskontrolle nicht ändern dürfen (ist der Normalfall) muss man einen **Datensatz statt einer Zufallszahl** verwenden! <br> Zufallszahlen haben in der Ergebnisberechnung keinen Sinn, und sollten maximal für angezeigte zufällige Werte verwendet werden! [DEMO-Beispiel](../../demobsp.html?id=3244) | random(2,8)                                    | 3.4532               |
| randomC  | komplexe Zufallszahl aus einem definierten Zahlenbereich für den Betrag<br>VORSICHT! Die Zufallszahl wird bei jedem Aufruf neu berechnet! [DEMO-Beispiel](../../demobsp.html?id=3245)                                                                                                                                                                                                                                                                                                                                                                                                                      | randomC(2,8)                                   | 3.4532arg40.3°       |
| signum   | Liefert das Vorzeichen einer Zahl (-1,0,1). Bei einer komplexen Zahl das Vorzeichen des Realteils. [DEMO-Beispiel](../../demobsp.html?id=3246)                                                                                                                                                                                                                                                                                                                                                                                                                                                             | signum(-4)                                     | -1                   |


####  Maxima-basierte Funktionen
* Diese Funktionen funktionieren nur wenn Maxima installiert ist und werden immer an Maxima gesendet, auch wenn der interne Parser aktiviert ist.
* Weiters werden sie bei der Ausgabe als TeX-Formel auch korrekt mit LaTeX gesetzt.

| Funktion  | Beschreibung                                                                                                                                                                                     | Beispiel                                   | Ergebnis       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|----------------|
| integrate | Berechnet das unbestimmte oder bestimmte Integral einer Funktion. [DEMO-Beispiel](../../demobsp.html?id=3250)                                                                                    | integrate(x^2,x) <br> integrate(x^2,x,0,2) | x^3/3 <br> 8/3 |
| diff      | Berechnet die Ableitung einer Funktion. [DEMO-Beispiel](../../demobsp.html?id=3251)                                                                                                              | diff(x^2,x)<br>diff(3*x^2,x,2)             | x <br> 6       |
| tomaxima  | Führt die Berechnung aller Parameter von links nach rechts hintereinander mit Maxima aus. Das Ergebnis ist dann das Ergebnis des letzten Parameters. [DEMO-Beispiel](../../demobsp.html?id=3263) | tomaxima(y:x^2,y+2)                        | x^2+2          |
| laplace   | Bestimmt die Laplace-Transformierte einer Funktion. [DEMO-Beispiel](../../demobsp.html?id=3264)                                                                                                  | laplace(sin(t),t,s)                        | 1/(1+s^2)      |
| ilt       | Bestimmt die inverse Laplace-Transformierte eine Laplace-Funktion [DEMO-Beispiel](../../demobsp.html?id=3265)                                                                                    | ilt(1/(1+s),s,t)                           | e^(-t)         |
| sum       | Summenbildung [DEMO-Beispiel](../../demobsp.html?id=3266)                                                                                                                                        | sum(1/k,k,1,2)                             | 3/2            |
| product   | Produktbildung [DEMO-Beispiel](../../demobsp.html?id=3267)                                                                                                                                       | product(1/k,k,1,3)                         | 1/6            |


#### erweiterte arithmetische Funktionen

| Funktion                             | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                | Beispiel                                                                            | Ergebnis                                                                                                                                                     |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sigma                                | Sprungfunktion: sigma(x) liefert 0 für x&lt;0 und 1 für x&gt;=0 [DEMO-Beispiel](../../demobsp.html?id=3268)                                                                                                                                                                                                                                                                                                                 | sigma(243.3)                                                                        | 1                                                                                                                                                            |
| pulse                                | Rechteckfunktion: <br>pulse(x,x0) ist gleich 1 für x0 &lt; x &lt; x0 + 1, sonst 0<br>pulse(x,x0,L) ist gleich 1 für x0 &lt; x &lt; x0 + L, sonst 0<br>![300px-Pulse.png](300px-Pulse.png) [DEMO-Beispiel](../../demobsp.html?id=3269)                                                                                                                                                                                       | pulse(x,2,4)                                                                        | ![100px-pulse_x_2_4.png](100px-pulse_x_2_4.png)                                                                                                              |
| ramp                                 | Rampenfunktion: <br>ramp(x,x0) Rampe von x0 &lt; x &lt; x0 + 1<br>ramp(x,x0,L) Rampe von x0 &lt; x &lt; x0 + L<br>![300px-Funktion_ramp.png](300px-Funktion_ramp.png) [DEMO-Beispiel](../../demobsp.html?id=3270)                                                                                                                                                                                                           | ramp(x,2,4)                                                                         | ![100px-Ramp_Plot.png](100px-Ramp_Plot.png)                                                                                                                  |
| interpol                             | Interpolationsfunktion zwischen mehreren Stützpunkten in einem Koordinatensystem. <br> interpol(WerteX,WerteY,x) [DEMO-Beispiel](../../demobsp.html?id=3272)                                                                                                                                                                                                                                                                | interpol(&#91;0,1,2&#93;,&#91;0,3,3&#93;,1.5)                                       | 3                                                                                                                                                            |
| interpol(pv,wert)                    | Interpoliert Zwischenwerte durch lineare Interpolation in einer als PV-Vektor gegebenen Tabelle [DEMO-Beispiel](../../demobsp.html?id=3273)                                                                                                                                                                                                                                                                                 | interpol(&#91;&#91;0,0&#93;,&#91;1,2&#93;,&#91;2,2.2&#93;,&#91;3,1.4&#93;&#93;,1.5) | 2.1                                                                                                                                                          |
| [periodic](/notimplemented/index.md) | Erzeugt aus einer beliebigen Funktion zwischen 0 und Periodendauer eine periodische Funktion <br> periodic(Variable,Periodendauer,Funktion)<br> periodic(Variable,Periodendauer,Funktionsperiodendauer,Funktion) [DEMO-Beispiel](../../demobsp.html?id=3274)                                                                                                                                                                | ch1(t):periodic(t,5ms,2'Vms-2'*t^2) <br> ch1(t):periodic(t,5ms,1,2V*t^2)            | <br>![100px-ClipCapIt-190318-113524.PNG](100px-ClipCapIt-190318-113524.PNG) <br> <br>![100px-ClipCapIt-190318-113644.PNG](100px-ClipCapIt-190318-113644.PNG) |
| numint                               | numerische Integration <br> numint(untereGrenze,obereGrenze,funktion,Variable)<br> numint(untereGrenze,obereGrenze,funktion,Variable,punkteAnzahl) [DEMO-Beispiel](../../demobsp.html?id=3275)                                                                                                                                                                                                                              | numint(0,2pi,sin(t),t)                                                              | 0                                                                                                                                                            |
| numdif                               | numerisches Differenzieren einer Funktion "funktion" nach einer Variablen "Variable" an der Stelle "position" mit einer Differenz der Variablen von "differenz" <br> numdif(position,funktion,Variable,differenz) [DEMO-Beispiel](../../demobsp.html?id=3276)                                                                                                                                                               | numdif(0,sin(t),t,0.01)                                                             | 1                                                                                                                                                            |
| solve                                | löst eine Gleichung oder ein Gleichungssystem nach einer oder mehrerer Variablen [DEMO-Beispiel](../../demobsp.html?id=3277)                                                                                                                                                                                                                                                                                                | solve(&#91;2*x+y=3,x-y=0&#93;,&#91;x,y&#93;)                                        | &#91;&#91; x=1,y=1 &#93;&#93;                                                                                                                                |
| solvevalue                           | löst eine Gleichung oder ein Gleichungssystem nach einer Variablen und liefert genau die erste Lösung wenn sie numerisch berechenbar ist [DEMO-Beispiel](../../demobsp.html?id=3278)                                                                                                                                                                                                                                        | solvevalue(&#91; 2*x+y=3,x-y=0 &#93;,&#91; x,y &#93;,x)                             | 1                                                                                                                                                            |
| newton                               | Bestimmt eine Nullstelle einer Funktion nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der Startwert. [DEMO-Beispiel](../../demobsp.html?id=3279)                                                                                                                                                                                                             | newton(x^2-4,4)                                                                     | 2                                                                                                                                                            |
| cnewton                              | Bestimmt eine komplexe Nullstelle einer Funktion nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der komplexe Startwert. [DEMO-Beispiel](../../demobsp.html?id=3280)                                                                                                                                                                                           | cnewton (x^2+4,4)                                                                   | 2*%i                                                                                                                                                         |
| newtonall                            | Bestimmt alle Nullstellen einer Funktion mit einem Betrag des Funktionsparameters kleiner als ein definierter Wert nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der maximale Betrag des Funktionsparameters. Das Ergebnis ist immer ein Vektor mit den nach aufsteigendem Funktionswert sortierten Nullstellen. [DEMO-Beispiel](../../demobsp.html?id=3281) | newtonall (x^2-4,4)                                                                 | &#91;-2,2&#93;                                                                                                                                               |
| cnewtonall                           | Bestimmt alle komplexen Nullstellen einer Funktion mit einem Betrag des Funktionsparameters kleiner als ein definierter Wert nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der maximale Betrag des Funktionsparameters. Das Ergebnis ist immer ein Vektor mit den Nullstellen. [DEMO-Beispiel](../../demobsp.html?id=3282)                                   | cnewtonall (x^2+4,4)                                                                | &#91;-2*%i,2*%i&#93;                                                                                                                                         |


####  Gleichungen und Gleichungssysteme

| Funktion | Beschreibung                                                                                                                                                               | Beispiel                                                                                                                     | Ergebnis                                            | ab Revision |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|-------------|
| solve    | löst eine Gleichung oder ein Gleichungssystem nach einer oder mehrerer Variablen [DEMO-Beispiel](../../demobsp.html?id=3283)                                               | solve(&#91;2*x+y=3,x-y=0&#93;,&#91;x,y&#93;)                                                                                 | &#91;&#91; x=1,y=1 &#93;&#93;                       |             |
| lhs      | liefert die linke Seite einer Gleichung, Ungleichung oder eines Infix Operators [DEMO-Beispiel](../../demobsp.html?id=3284)                                                | lhs(x+y=c+2)                                                                                                                 | x+y                                                 | 6521        |
| rhs      | liefert die rechte Seite einer Gleichung, Ungleichung oder eines Infix Operators [DEMO-Beispiel](../../demobsp.html?id=3285)                                               | rhs(x+y=c+2)                                                                                                                 | c+2                                                 | 6521        |
| onlypos  | liefert aus dem Lösungsvektor von solve welcher aus lauter Gleichungen besteht nur die Lösungen welche positiv nicht Null sind [DEMO-Beispiel](../../demobsp.html?id=3286) | onlypos(&#91;&#91;x=3,y=-3&#93;,&#91;x=4,y=5&#93;,&#91;x=-2,y=4&#93;&#93;) <br> onlypos(&#91;x=-2,x=0,x=6,x=8&#93;)          | &#91;&#91;x=4,y=5&#93;&#93; <br> &#91;x=7,x=8&#93;  | 6522        |
| onlyreal | liefert aus dem Lösungsvektor von solve welcher aus lauter Gleichungen besteht nur die Lösungen welche reell sind [DEMO-Beispiel](../../demobsp.html?id=3287)              | onlyreal(&#91;&#91;x=1,y=%i&#93;,&#91;x=1,y=-%i&#93;,&#91;x=3,y=4&#93;&#93;) <br> onlyreal(&#91;x=%i+1,x=1-%i,x=3,x=8&#93;) | &#91;&#91;x=3,y=4&#93;&#93; <br> &#91;x=3,x=8&#93; | 6522        |


#### Stringfunktionen

| Funktion               | Beschreibung                                                                                                                                                                      | Beispiel                                     | Ergebnis    |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|-------------|
| dechex                 | Zahl in eine Ganzzahl wandeln und als Hexadezimal-String ausgeben [DEMO-Beispiel](../../demobsp.html?id=3288)                                                                     | dexhex(12)                                   | "0xC"       |
| chr                    | Bestimmt die Zeichen mit dem ASC-II-Code der Long-Parameter und setzt daraus einen String zusammen. [DEMO-Beispiel](../../demobsp.html?id=3289)                                   | chr(0x65,105)                                | "ei"        |
| val                    | Bestimmt den ASC-II-Code des ersten Zeichens welches als String-Parameter übergeben wurde. [DEMO-Beispiel](../../demobsp.html?id=3290)                                            | val("a")                                     | 97          |
| strcat                 | Fügt mehrere Strings zusammen. [DEMO-Beispiel](../../demobsp.html?id=3291)                                                                                                        | strcat("a","b")                              | "ab"        |
| string                 | Wandelt eine Zahl in einen String um.                                                                                                                                             | string(123)                                  | "123"       |
| parse                  | Wenn der Parameter ein String ist wird dieser String mit dem Parser interpretiert [DEMO-Beispiel](../../demobsp.html?id=3482)                                                     | parse("2+3")                                 | 5           |
| substring              | Liefert einen Teil eines Strings substring(string,startindex,endindex). Index beginnt bei 0 und endindex ist optional.  [DEMO-Beispiel](../../demobsp.html?id=5025)               | substring("abcdefg",2,3)                     | "cd"        |
| tailstring             | liefert den letzten Teil eines Strings teilstring(tailstring,zeichenanzahl) [DEMO-Beispiel](../../demobsp.html?id=5026)                                                           | tailstring("abcdefg",2)                      | "fg"        |
| replacestring          | Ersetzt alle Vorkommen einer Zeichenkette in einem String durch eine andere Zeichenkette. [DEMO-Beispiel](../../demobsp.html?id=5027)                                             | replacestring("abcdefg","bc","xy")           | "axydefg" |
| replaceallstring       | Ersetzt alle Vorkommen einer Zeichenkette ([regulärer Ausdruck](../RegularExpression/index.md)) durch eine andere Zeichenkette.  [DEMO-Beispiel](../../demobsp.html?id=5027)      | replaceallstring("abcdefg","b.*e","xy")      | "axyfg" |
| replacefirststring    | Ersetzt das erste Vorkommen einer Zeichenkette ([regulärer Ausdruck](../RegularExpression/index.md)) durch eine andere Zeichenkette. [DEMO-Beispiel](../../demobsp.html?id=5027) | replacefirststring("abcdefg","b.*e","xy") | "axyfg" |
| splitstring            | Teilt einen String in ein Array von Strings splitstring(string,separator) [DEMO-Beispiel](../../demobsp.html?id=5028)                                                             | splitstring("abcdefg","b")                   | "a","c","defg" |
| matchstring | Prüft ob eine String einem [regulären Ausdruck](../RegularExpression/index.md) entspricht.  [DEMO-Beispiel](../../demobsp.html?id=5029)                                                                          | matchstring("abcdefg","b.*e") | true |

#### trigonometrische Funktionen

| Funktion                             | Beschreibung                                                                                                                                   | Beispiel         | Ergebnis                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------|---------------------------------------|
| sin                                  | Sinus [DEMO-Beispiel](../../demobsp.html?id=3292)                                                                                              | sin(%pi/2)       | 1                                     |
| cos                                  | Cosinus [DEMO-Beispiel](../../demobsp.html?id=3302)                                                                                            | cos(%pi/2)       | 0                                     |
| tan                                  | Tangens [DEMO-Beispiel](../../demobsp.html?id=3303)                                                                                            | tan(%pi/4)       | 1                                     |
| cot                                  | Cotangens, `cot(x)=1/tan(x)`.                                                                                                                   | cot(%pi/4)       | 1                                     |
| asin                                 | Arcus-Sinus [DEMO-Beispiel](../../demobsp.html?id=3304)                                                                                        | asin(1)          | %pi/2                                 |
| arcsin                               | Arcus-Sinus [DEMO-Beispiel](../../demobsp.html?id=3305)                                                                                        | asin(1)          | %pi/2                                 |
| acos                                 | Arcus-Cosinus [DEMO-Beispiel](../../demobsp.html?id=3306)                                                                                      | acos(1)          | 0                                     |
| arccos                               | Arcus-Cosinus [DEMO-Beispiel](../../demobsp.html?id=3307)                                                                                      | acos(1)          | 0                                     |
| atan                                 | Arcus-Tangens [DEMO-Beispiel](../../demobsp.html?id=3308)                                                                                      | atan(1)          | %pi/4                                 |
| arctan                               | Arcus-Tangens [DEMO-Beispiel](../../demobsp.html?id=3309)                                                                                      | arctan(1)        | %pi/4                                 |
| acot                                 | Arcus-Cotangens.                                                                                                                                | acot(1)          | %pi/4                                 |
| arccot                               | Alias zu `acot`: Arcus-Cotangens.                                                                                                               | arccot(1)        | %pi/4                                 |
| atan2                                | Arcus-Tangens atan2(y,x)=arctan(y/x) [DEMO-Beispiel](../../demobsp.html?id=3310)                                                               | atan2(-2,-2)     | -%pi*3/4                              |
| arctan2                              | Arcus-Tangens arctan2(y,x)=arctan(y/x) [DEMO-Beispiel](../../demobsp.html?id=3311)                                                             | arctan2(-2,-2)   | -%pi*3/4                              |
| sinh                                 | Sinus-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3312)                                                                                 | sinh(1)          | 1.1752012                             |
| cosh                                 | Cosinus-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3313)                                                                               | cosh(1)          | 1.5430806                             |
| tanh                                 | Tangens-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3314)                                                                               | tanh(1)          | 0.7615941                             |
| coth                                 | Cotangens-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3315)                                                                             | coth(1)          | 1.313035                              |
| sec                                  | Secans, `sec(x)=1/cos(x)`.                                                                                                                      | sec(0)           | 1                                     |
| csc                                  | Kosecans, `csc(x)=1/sin(x)`.                                                                                                                    | csc(%pi/2)       | 1                                     |
| sech                                 | Secans-Hyperbolicus, `sech(x)=1/cosh(x)`.                                                                                                       | sech(0)          | 1                                     |
| csch                                 | Kosecans-Hyperbolicus, `csch(x)=1/sinh(x)`.                                                                                                     | csch(1)          | 0.850918...                           |
| asinh                                | Area-Sinus-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3316)                                                                            | asinh(1.1752012) | 1                                     |
| acosh                                | Area-Cosinus-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3317)                                                                          | acosh(1.5430806) | 1                                     |
| atanh                                | Area-Tangens-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3318)                                                                          | atanh(0.7615941) | 1                                     |
| acoth                                | Area-Cotangens-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3319)                                                                        | acoth(1.313035)  | 1                                     |
| asec                                 | Arcus-Secans, inverse Funktion zu `sec`.                                                                                                         | asec(2)          | %pi/3                                 |
| acsc                                 | Arcus-Kosekans, inverse Funktion zu `csc`.                                                                                                       | acsc(2)          | %pi/6                                 |
| asech                                | Area-Secans-Hyperbolicus, inverse Funktion zu `sech`.                                                                                            | asech(1)         | 0                                     |
| acsch                                | Area-Kosekans-Hyperbolicus, inverse Funktion zu `csch`.                                                                                          | acsch(1)         | 0.881373...                           |
| [csin](/notimplemented/index.md)     | Erzeugt aus einer komplexen Zahl (Effektivwert) und einer Frequenz einen Sinusfunktion in der Zeit [DEMO-Beispiel](../../demobsp.html?id=3320) | csin(U)          | sqrt(2)*cabs(U)*sin(2*pi*f*t+carg(U)) |
| cssin                                | Erzeugt aus einer komplexen Zahl, die als Spitzenwert interpretiert wird, eine Sinusfunktion. `cssin(U)`, `cssin(U,f)` oder `cssin(U,f,x)`. | cssin(U) | cabs(U)*sin(2*pi*f*t+carg(U)) |
| [quadrant](/notimplemented/index.md) | Liefert den Quadranten eines Winkels mit einer Toleranzangabe. [DEMO-Beispiel](../../demobsp.html?id=3321)                                     | quadrant(20°,5°) | 1                                     |
| argnorm                              | Wandelt einen Winkel auf den Bereich von 0°-360° [DEMO-Beispiel](../../demobsp.html?id=3322)                                                   | argnorm(-50°)    | 310°                                  |
| pi                                   | Funktionsschreibweise der Kreiszahl Pi. `pi()` hat keine Parameter und entspricht `%pi`.                                                        | pi()             | %pi                                   |


#### Exponentialfunktionen

| Funktion | Beschreibung                                                         | Beispiel   | Ergebnis |
|----------|----------------------------------------------------------------------|------------|----------|
| pow      | Potenzfunktion [DEMO-Beispiel](../../demobsp.html?id=3324)           | pow(2,3)   | 8        |
| sqrt     | Quadratwurzel. Entspricht `root(x,2)`.                               | sqrt(9)    | 3        |
| root     | n-te Wurzel `root(x,n)`; ohne zweiten Parameter wird die Quadratwurzel verwendet. | root(8,3) | 2 |
| exp      | Exponentialfunktion [DEMO-Beispiel](../../demobsp.html?id=3325)      | exp(1)     | %e       |
| log      | natürlicher Logarythmus [DEMO-Beispiel](../../demobsp.html?id=3326)  | log(%e)    | 1        |
| ln       | natürlicher Logarythmus [DEMO-Beispiel](../../demobsp.html?id=3327)  | ln(%e)     | 1        |
| log10    | Logarythmus zur Basis 10 [DEMO-Beispiel](../../demobsp.html?id=3328) | log10(100) | 2        |


#### komplexe Zahlen
Die Funktionen zu komplexen Zahlen werden (anders als in Maxima) nur ausgewertet wenn das Ergebnis numerisch berechenbar ist, ansonsten bleibt die Funktion symbolisch erhalten.

| Funktion  | Beschreibung                                                                                                                                             | Beispiel                  | Ergebnis |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------|
| abs       | Liefert den Absolutbetrag einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3329)                                                               | abs(3+4*%i)               | 5        |
| cabs      | Liefert den Absolutbetrag einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3330)                                                               | cabs(3+4*%i)              | 5        |
| cAbs      | Kompatibilitätsalias zu `cabs`.                                                                                                                           | cAbs(3+4*%i)              | 5        |
| carg      | Liefert das Argument einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3331)                                                                    | carg(4*%e^(3*%i))         | 3        |
| cArg      | Kompatibilitätsalias zu `carg`.                                                                                                                           | cArg(4*%e^(3*%i))         | 3        |
| realpart  | Liefert den Realteil einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3332)                                                                    | realpart(3+4*%i)          | 3        |
| cRe       | Kompatibilitätsalias zu `realpart`.                                                                                                                       | cRe(3+4*%i)               | 3        |
| imagpart  | Liefert den Imaginärteil einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3333)                                                                | imagpart(3+4*%i)          | 4        |
| cIm       | Kompatibilitätsalias zu `imagpart`.                                                                                                                       | cIm(3+4*%i)               | 4        |
| conjugate | Liefert die konjugiert komplexe Zahl einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3334)                                                    | conjugate(3+4*%i)         | 3-4*%i   |
| cConjugate | Kompatibilitätsalias zu `conjugate`.                                                                                                                     | cConjugate(3+4*%i)        | 3-4*%i   |
| rectform  | hat in LeTTo keine Relevanz, da die Zahlendarstellung bei der Ausgabe definiert wird wie zB.: {=3arg2;karti} [DEMO-Beispiel](../../demobsp.html?id=3335) |                           |          |
| cRectform | Kompatibilitätsalias zu `rectform`.                                                                                                                       |                           |          |
| pol       | erzeugt aus Betrag und Argument eine komplexe Zahl [DEMO-Beispiel](../../demobsp.html?id=3336)                                                           | pol(5,0.9272952180016122) | 3+4*%i   |
| polgrad   | Erzeugt aus Betrag und einem Winkel im Gradmaß eine komplexe Zahl.                                                                                        | polgrad(5,53.130102°/1°)  | 3+4*%i   |

#### Polynome
Polynome mit reellen Koeffizienten in einer Variablen können mit folgenden Funktionen erstellt und verarbeitet werden. Für die interne Verarbeitung wird hierzu ein eigener Polynom-Datentyp verwendet.

siehe auch [Zahlendarstellung Polynome](../Zahlendarstellung/index.md#für-polynome-und-gebrochen-rationale-funktionen-mit-numerischen-koeffizienten-in-einer-variablen-können-folgende-parameter-angegeben-werden)

| Funktion                                           | Beschreibung                                                                                                                                                                                                                                                           | Beispiel                                                          | Ergebnis                                         |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------|
| polynom(p)                                         | Erzeugt aus einem Ausdruck welcher genau eine Variable besitzen muss ein Polynom in dieser Variablen [DEMO-Beispiel](../../demobsp.html?id=3337)                                                                                                                       | polynom(1+x)                                                      | 1+x²                                             |
| polynom(p,var)                                     | Erzeugt aus einem Ausdruck ein Polynom in einer definierten Variablen. Ist p ein gültiger Polynom-Ausdruck mit reelen Koeffizienten in der Variablen var wird das Polynom erzeugt, ansonsten bleibt die Funktion erhalten. [DEMO-Beispiel](../../demobsp.html?id=3338) | polynom(1+a*x^2,x) <br> polynom(1+2*x^2,x)                        | polynom(1+a*x^2,x)<br>1+2*x²                     |
| polynom(p,var,"einheit")                           | Erzeugt ein Polynom in der Variablen var, mit der Einheit "einheit" für die Polynomvariable. Die Einheit muss als String in Doppelhochkomma angegeben werden! Das Polynom p muss entweder ohne Einheiten oder mit den korrekten Einheiten angegeben werden!            | polynom(1+2*p^2,p,"s-1") <br> polynom(1+2's2'*p^2,p,"s-1")        | 1+2's2'*p^2 <br>1+2's2'*p^2                      |
| factfrompolynom(p)                                 | Erzeugt aus einem Polynom einen Vektor mit den Polynomfaktoren. Erste Zeile Zählerfaktoren, zweite Zeile Nennerfaktoren, dritte Zeile Polynomvariable, vierte Zeile Einheit der Polynomvariable                                                                        | factfrompolynom(polynom((2+x)/(1+2*x)))                           | &#91;&#91;1,0.5&#93;,&#91;0.5,1&#93;,"x",""&#93; |
| polynomfromfact(f)                                 | Erzeugt aus einer Faktoren-Liste, welche mit factfrompolynom erstellt wurde ein neues Polynom                                                                                                                                                                          | polynomfromfact(&#91;&#91;1,0.5&#93;,&#91;0.5,1&#93;,"x",""&#93;) | (2+x)/(1+2*x)                                    |
| polynomfromfact(zähler,nenner,var,einheit)         | Erzeugt aus Zähler und Nenner Faktor-Vektoren ein neues Polynom                                                                                                                                                                                                        | polynomfromfact(&#91;1,0.5&#93;,&#91;0.5,1&#93;,x,"")             | (2+x)/(1+2*x)                                    |
| nullfrompolynom(p)                                 | Erzeugt aus einem Polynom einen Vektor mit den PolynomNullstellen und Polstellen. Erste Zeile gemeinsamer Faktor, zweite Zeile Nullstellen, dritte Zeile Polstellen, vierte Zeile Polynomvariable                                                                      | nullfrompolynom(polynom((2+x)/(1+2*x)))                           | &#91;0.5,&#91;-2&#93;,&#91;-0.5&#93;,x&#93;    |
| polynomfromnull(n)                                 | Erzeugt aus einer Nullstellen-Polstellen-Liste, welche mit nullfrompolynom erstellt wurde ein neues Polynom                                                                                                                                                            | polynomfromnull(&#91;0.5,&#91;-2&#93;,&#91;-0.5&#93;,x&#93;)      | (2+x)/(1+2*x)                                    |
| polynomfromnull(faktor,nullstellen,polstellen,var) | Erzeugt aus einer Faktor-Vektoren ein neues Polynom                                                                                                                                                                                                                    | polynomfromnull(0.5,&#91;-2&#93;,&#91;-0.5&#93;,x)               | (2+x)/(1+2*x)                                    |
| polynomk(p)                                        | Bestimmt den Faktor, welcher vom Polynom herausgehoben werden kann, so dass die höchste Potenz der Polynomvariable den Multiplikator Eins hat.                                                                                                                         | polynomk(polynom((2+x)/(1+2*x)))                                  | 0.5                                              |
| ispolynom(p)                                     | Prüft, ob der Ausdruck ein Polynom ist. Die Funktion wird ausgewertet, sobald der Parameter als Polynom erkannt bzw. nicht als Polynom erkannt werden kann. | ispolynom(polynom(x^2+1)) | true |
| getvars(ausdruck)                              | Liefert alle im Ausdruck vorkommenden Variablennamen als Vektor von Strings. | getvars(x^2+a*y) | &#91;"a","x","y"&#93; |


#### statistische Funktionen
Die Funktionen funktionieren nur ohne Einheiten.

| Funktion  | Beschreibung                                                                                                   | Beispiel      | Ergebnis |
|-----------|----------------------------------------------------------------------------------------------------------------|---------------|----------|
| factorial | Liefert die Fakultät einer positiven ganzen Zahl [DEMO-Beispiel](../../demobsp.html?id=3339)                   | factorial(5)  | 120      |
| binomial  | Liefert den Binomialkoeffizienten von zwei positiven ganzen Zahlen [DEMO-Beispiel](../../demobsp.html?id=3340) | binomial(5,2) | 10       |


#### Mengen-Funktionen
Mengen werden intern als Vektoren verarbeitet und sind deshalb auch direkt durch Vektoren ersetzbar. Auch alle Vektor-Funktionen sind somit auch auf Mengen anwendbar und umgekehrt.

| Funktion         | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Beispiel                                                                                                                                                                                           | Ergebnis                                                          | ab Rev |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|--------|
| setget           | Liefert ein Element einer Menge oder einer Matrix (Menge von Mengen) [DEMO-Beispiel](../../demobsp.html?id=3341)                                                                                                                                                                                                                                                                                                                                                                                                       | setget(&#91;12,13,14&#93;,1) <br> setget(matrix([9,2&#93;,[3,4&#93;),0,1)                                                                                                                      | 13 <br> 2                                                         |        |
| setset           | setzt ein Element einer Menge oder einer Matrix (Menge von Mengen) [DEMO-Beispiel](../../demobsp.html?id=3342)                                                                                                                                                                                                                                                                                                                                                                                                         | setset(&#91;12,13,14&#93;,1,35) <br> setset(matrix([9,2&#93;,[3,4&#93;),0,0,-9)                                                                                                                | &#91;12,35,14&#93; <br> &#91;&#91;-9,2&#93;,&#91;3,4&#93;&#93; |        |
| setlength        | liefert die Anzahl der Elemente einer Liste, Menge oder eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3343)                                                                                                                                                                                                                                                                                                                                                                                                      | setlength(&#91;3,6,54,34,3,54&#93;)                                                                                                                                                        | 6                                                                 |        |
| setinsert        | fügt ein Element in eine Menge an eine gegebene Stelle ein [DEMO-Beispiel](../../demobsp.html?id=3344)                                                                                                                                                                                                                                                                                                                                                                                                                 | setinsert(&#91;12,13,14&#93;,1,25)                                                                                                                                                               | &#91;12,25,13,14&#93;                                    |        |
| setremove        | löscht ein Element einer Menge [DEMO-Beispiel](../../demobsp.html?id=3346)                                                                                                                                                                                                                                                                                                                                                                                                                                             | setremove(&#91;12,13,14&#93;,1)                                                                                                                                                                  | &#91;12,14&#93;                                                |        |
| setapply         | wendet einen Ausdruck oder Funktion auf alle Elemente einer Menge an [DEMO-Beispiel](../../demobsp.html?id=3347)                                                                                                                                                                                                                                                                                                                                                                                                       | setapply(y,&#91;1,2,3&#93;,y*2)                                                                                                                                                                     | &#91;2,4,6&#93;                                                | 5965   |
| setmedian        | Liefert den Median einer Menge [DEMO-Beispiel](../../demobsp.html?id=3348)                                                                                                                                                                                                                                                                                                                                                                                                                                             | setmedian(&#91;4,3,1,5,6&#93;                                                                                                                                                              | 4                                                                 |        |
| setboxplot       | Liefert die Werte des Boxplot einer Menge (Minimum, unteres Quartil, Median, oberes Quartil, Maximum) als Vektor verwendbar für das [Plot-Plugin#definierte-zeichenelemente-](../Plot#definierte-zeichenelemente-/index.md#definierte-zeichenelemente-) [DEMO-Beispiel](../../demobsp.html?id=3349)                                                                                                                                                                                                                    | setboxplot(&#91;1,2,3,10,8,9&#93;                                                                                                                                                          | &#91;1,2,5.5,9,10&#93;                                 |        |
| setsort          | Sortiert die Elemente einer Menge aufsteigend [DEMO-Beispiel](../../demobsp.html?id=3350)                                                                                                                                                                                                                                                                                                                                                                                                                              | setsort(&#91;3,-3,2,0,5,2&#93;)                                                                                                                                                              | &#91;-3,0,2,2,3,5&#93;                                  |        |
| setsortnd        | Sortiert die Elemente einer Menge aufsteigend und entfernt alle mehrfach vorkommenden Elemente [DEMO-Beispiel](../../demobsp.html?id=3351)                                                                                                                                                                                                                                                                                                                                                                             | setsortnd(&#91;31,-3,2,31,0,5,2&#93;)                                                                                                                                                    | &#91;-3,0,2,5,31&#93;                                   |        |
| setcount         | Bestimmt die Anzahl wie oft ein Element in einer Menge vorkommt oder die Anzahl der Elemente der Menge [DEMO-Beispiel](../../demobsp.html?id=3352)                                                                                                                                                                                                                                                                                                                                                                     | setcount(&#91;31,-3,2,31,0,5,2&#93;,31) <br> setcount(&#91;2,5,3,6&#93;)                                                                                                                | 2 <br> 4                                                          |        |
| setmodus         | Liefert das Element einer Menge, welches am öftesten vorkommt oder die Elemente als Menge wenn mehrere Elemente gleich oft vorkommen [DEMO-Beispiel](../../demobsp.html?id=3353)                                                                                                                                                                                                                                                                                                                                       | setmodus(&#91;3,-3,2,0,5,2&#93;)                                                                                                                                                             | 2                                                                 |        |
| setreverse       | Dreht die Reihenfolge einer Menge um [DEMO-Beispiel](../../demobsp.html?id=3354)                                                                                                                                                                                                                                                                                                                                                                                                                                       | setreverse(&#91;3,-3,2,0,5,2&#93;)                                                                                                                                                           | &#91;2,5,0,2,-3,3&#93;                                  |        |
| reverse          | Alias zu `setreverse`: Dreht die Reihenfolge eines Vektors/einer Menge um. | reverse(&#91;1,2,3&#93;) | &#91;3,2,1&#93; | |
| setnd            | Löscht alle Duplikate aus der Menge [DEMO-Beispiel](../../demobsp.html?id=3355)                                                                                                                                                                                                                                                                                                                                                                                                                                        | setnd(&#91;3,-3,2,0,5,2&#93;))                                                                                                                                                                | &#91;3,-3,2,0,5&#93;                                     |        |
| setshuffle       | Mischt eine Menge in eine andere Reihenfolge. VORSICHT, ohne zweiten Parameter (ganze Zahl) ändert sich die Reihenfolge bei jedem mal neu Laden automatisch und ist nicht nachvollziehbar, weshalb sie dann für Schülerbeispiele nicht einsetzbar ist! Daher ist es für eine praktische Anwendung in einem Schülerbeispiel **erforderlich**, dass der zweite Parameter determiniert (beispielsweise über einen Integer-Datensatz-Wert zwischen 0 und 1000) festgelegt wird. [DEMO-Beispiel](../../demobsp.html?id=3356) | setshuffle(&#91;3,-3,2,0,5,2&#93;,5)                                                                                                                                                         | &#91;2,3,−3,2,0,5&#93;                                 | 6082   |
| setmittel        | Bestimmt den Mittelwert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3357)                                                                                                                                                                                                                                                                                                                                                                                                                                        | setmittel(&#91;1,3,2,4&#93;)                                                                                                                                                                      | 2.5                                                               |        |
| setgeomittel     | Bestimmt das geometrische Mittelwert einer Menge aus positiven reellen Zahlen [DEMO-Beispiel](../../demobsp.html?id=3358)                                                                                                                                                                                                                                                                                                                                                                                              | setgeomittel(&#91;10,20,30&#93;)                                                                                                                                                                 | 18.171206                                                         |        |
| setvarianz       | Bestimmt die empirische Varianz einer Menge [DEMO-Beispiel](../../demobsp.html?id=3359)                                                                                                                                                                                                                                                                                                                                                                                                                                | setvarianz(&#91;3,1,2,5,4&#93;)                                                                                                                                                                 | ((3-3)^2+(1-3)^2+(2-3)^2+(5-3)^2+(4-3)^2)/5=2                     |        |
| setquadratmittel | Bestimmt den quadratischen Mittelwert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3360)                                                                                                                                                                                                                                                                                                                                                                                                                          | setquadratmittel(&#91;10,20,30&#93;)                                                                                                                                                             | 21.6025                                                           |        |
| setsum           | Bestimmt die Summe aller Werte einer Menge [DEMO-Beispiel](../../demobsp.html?id=3361)                                                                                                                                                                                                                                                                                                                                                                                                                                 | setsum(&#91;1,3,2,4&#93;)                                                                                                                                                                         | 10                                                                |        |
| setprod          | Bestimmt das Produkt aller Werte einer Menge [DEMO-Beispiel](../../demobsp.html?id=3363)                                                                                                                                                                                                                                                                                                                                                                                                                               | setprod(&#91;1,3,2,4&#93;)                                                                                                                                                                        | 24                                                                |        |
| setunion         | Fügt mehrere Mengen zu einer neuen Menge zusammen [DEMO-Beispiel](../../demobsp.html?id=3364)                                                                                                                                                                                                                                                                                                                                                                                                                          | setunion(&#91;1,3,2,4&#93;,[3,7&#93;)                                                                                                                                                            | &#91;1,3,2,4,3,7&#93;                                   |        |
| setunionnd       | Fügt mehrere Mengen zu einer neuen Menge zusammen, sortiert diese und entfernt alle mehrfachen Elemente [DEMO-Beispiel](../../demobsp.html?id=3365)                                                                                                                                                                                                                                                                                                                                                                    | setunionnd(&#91;1,3,2,4&#93;,[3,7&#93;)                                                                                                                                                          | &#91;1,2,3,4,7&#93;                                       |        |
| setcut           | Bildet die Schnittmenge aus mehreren Mengen [DEMO-Beispiel](../../demobsp.html?id=3366)                                                                                                                                                                                                                                                                                                                                                                                                                                | setcut(&#91;1,3,2,4&#93;,[3,7&#93;)                                                                                                                                                              | &#91;3&#93;                                                        |        |
| setcompare       | vergleicht zwei Mengen miteinander, wobei die Reihenfolge egal ist [DEMO-Beispiel](../../demobsp.html?id=3368)                                                                                                                                                                                                                                                                                                                                                                                                         | setcompare(&#91;1,3,2,4&#93;,[3,7&#93;) <br> setcompare(&#91;1,3,2&#93;,&#91;1,2,3&#93;) <br> setcompare(&#91;1,3,2&#93;,&#91;1,3,2,3&#93;) <br> setcompare(&#91;1,2,3&#93;,[1,2,3&#93;)         | false <br> true <br> false <br> true                              |        |
| setcomparend     | vergleicht zwei Mengen miteinander, wobei die Reihenfolge egal ist und doppelte Werte als einfach behandelt werden. [DEMO-Beispiel](../../demobsp.html?id=3369)                                                                                                                                                                                                                                                                                                                                                        | setcomparend(&#91;1,3,2,4&#93;,[3,7&#93;) <br> setcomparend([1,3,2&#93;,[1,2,3&#93;) <br> setcomparend([1,3,2&#93;,[1,3,2,3&#93;) <br> setcomparend([1,2,3&#93;,[1,2,3&#93;) | false <br> true <br> true <br> true                               |        |
| setpartof        | prüft ob die erste Menge eine Teilmenge der zweite Menge ist wobei die Reihenfolge egal ist aber mehrfache Werte berücksichtigt werden [DEMO-Beispiel](../../demobsp.html?id=3370)                                                                                                                                                                                                                                                                                                                                     | setpartof(&#91;1,4&#93;,&#91;1,3,7&#93;) <br> setpartof(&#91;1,3&#93;,[1,2,3&#93;) <br> setpartof([1,3,3&#93;,[1,3,5,7&#93;) <br> setpartof([1,4,4&#93;,[1,2,3,4&#93;)                 | false <br> true <br> false <br> false                             |        |
| setpartofnd      | prüft ob die erste Menge eine Teilmenge der zweite Menge ist wobei die Reihenfolge und mehrfache Werte egal sind [DEMO-Beispiel](../../demobsp.html?id=3372)                                                                                                                                                                                                                                                                                                                                                           | setpartofnd(&#91;1,4&#93;,&#91;1,3,7&#93;) <br> setpartofnd(&#91;1,3&#93;,[1,2,3&#93;) <br> setpartofnd([1,3,3&#93;,[1,3,5,7&#93;) <br> setpartofnd([1,4,4&#93;,[1,2,3,4&#93;)         | false <br> true <br> true <br> true                               |        |
| setgetmin        | Liefert den kleinsten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3374)                                                                                                                                                                                                                                                                                                                                                                                                                                     | setgetmin(&#91;1,3,-2,4&#93;)                                                                                                                                                                    | -2                                                                |        |
| setgetmax        | Liefert den größten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3375)                                                                                                                                                                                                                                                                                                                                                                                                                                       | setgetmax(&#91;1,3,-2,4&#93;)                                                                                                                                                                    | 4                                                                 |        |
| setremovefirst   | Entfernt den ersten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3376)                                                                                                                                                                                                                                                                                                                                                                                                                                       | setremovefirst(&#91;1,3,-2,4&#93;)                                                                                                                                                               | &#91;3,-2,4&#93;                                           |        |
| setremovelast    | Entfernt den letzten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3377)                                                                                                                                                                                                                                                                                                                                                                                                                                      | setremovelast(&#91;1,3,-2,4&#93;)                                                                                                                                                                | &#91;1,3,-2&#93;                                            |        |
| setgetfirst      | Liefert den ersten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3378)                                                                                                                                                                                                                                                                                                                                                                                                                                        | setgetfirst(&#91;1,3,-2,4&#93;)                                                                                                                                                                  | 1                                                                 |        |
| setgetlast       | Liefert den letzten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3379)                                                                                                                                                                                                                                                                                                                                                                                                                                       | setgetlast(&#91;1,3,-2,4&#93;)                                                                                                                                                                   | 4                                                                 |        |
| setsub           | setsub(M,x,y) Liefert eine Teilmenge von M der Elemente vom index x bis zum Index y [DEMO-Beispiel](../../demobsp.html?id=3380)                                                                                                                                                                                                                                                                                                                                                                                        | setsub(&#91;1,3,-2,4&#93;,1,2)                                                                                                                                                                   | &#91;3,-2&#93;                                              |        |
| setmakelist      | setmakelist(f,x,start,stop) setzt in den Ausdruck f für x die Werte von start bis stop mit einer Schrittweite von 1 ein. [DEMO-Beispiel](../../demobsp.html?id=3381)                                                                                                                                                                                                                                                                                                                                                   | setmakelist(x^2,x,1,4)                                                                                                                                                                             | &#91; 1,4,9,16 &#93;                                   |        |
|                  | setmakelist(f,x,start,stop,schrittweite) setzt in den Ausdruck f für x die Werte von start bis stop mit dem Abstand schrittweite ein.                                                                                                                                                                                                                                                                                                                                       | setmakelist(x^2,x,1,2,0.5)                                                                                                                                                                         | &#91; 1,2.25,4 &#93;                                     |        |
|                  | setmakelist(f,x,set) setzt die Werte des Vektors set in den Ausdruck f für x ein.                                                                                                                                                                                                                                                                                                                                                                                                                                      | setmakelist(x^2,x,&#91;3,1,2&#93;)                                                                                                                                                                  | &#91; 9,1,4 &#93;                                      |        |
| foreach          | Führt für jedes Element eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion [DEMO-Beispiel](../../demobsp.html?id=3383)                                                                                                                                                                                                                                                                                                                                                                                                                     | foreach(&#91;2,-3,5,-6&#93;,p,cabs(p),"+")                                                                                                                                                      | 16                                                                | 6075   |

Für die Korrektur können Mengen über die Zieleinheit auch ohne Reihenfolge vergliechen werden - siehe [Zieleinheit](../ZielEinheit/index.md#parameter-für-den-ergebnisvergleich-von-vektoren-und-mengen-bei-der-schülereingabe)

#### Funktionen für importierte Tabellen

Werden Tabellen aus [csv-Dateien](../BeispielsammlungEditieren/csv-tabellen_importieren/index.md) importiert dann kann auf sie als Matrix zugegriffen werden.

| Funktion                                         | Beschreibung                                                                                                                                                                                        | Beispiel                                                                                                  | Ergebnis                                                              |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| curvepv(tabelle,spalteX,spalteY)                 | Liest aus einer gespeicherten Tabelle die Spalte "spalteX" für die x-Werte und die Spalte "spalteY" für die Y-Werte eines pv-Vektors [DEMO-Beispiel](../../demobsp.html?id=3384)                    | curvepv(&#91;&#91;0,0,2&#93;,&#91;1,2,3&#93;,&#91;2,2.2,1.5&#93;,&#91;3,1.4,1.8&#93;&#93;,0,1)            | &#91;&#91;0,0&#93;,&#91;1,2&#93;,&#91;2,2.2&#93;,&#91;3,1.4&#93;&#93; |
| curveinterpol(tabelle,spalteX,spalteY,wert)      | Interpoliert in einer gespeicherten Tabelle zwischen den Stützpunkten. Als Ergebnis wird ein Vektor aller gefundenen Punkte auf der Kennlinie geliefert [DEMO-Beispiel](../../demobsp.html?id=3385) | curveinterpol(KL,0,1,3.5)                                                                                 | &#91;2.1&#93;                                                         |
| curveinterpolfirst(tabelle,spalteX,spalteY,wert) | Interpoliert in einer gespeicherten Tabelle und liefert den ersten interpolierten Punkt auf der Kennlinie.                                                                                          | curveinterpolfirst(KL,0,1,1.5)                                                                            | 2.1                                                                   |
| interpol(pv,wert)                                | Interpoliert Zwischenwerte durch lineare Interpolation in einer als PV-Vektor gegebenen Tabelle [DEMO-Beispiel](../../demobsp.html?id=3386)                                                         | interpol(&#91;&#91;0,0&#93;,&#91;1,2&#93;,&#91;2,2.2&#93;,&#91;3,1.4&#93;&#93;,1.5)                       | 2.1                                                                   |
| curveHTML(tabelle,spaltennamen,einheiten)        | Liefert eine HTML-Ansicht einer Tabelle.                                                                                                                                                            | curvHTML(KL,KL_names,curveunits(KL))                                                                      | HTML-Code der Tabelle                                                 |
| curveunits(tabelle)                              | Liefert einen Vektor aller Einheiten der Spalten einer Matrix                                                                                                                                       | curveunits(curvepv(&#91;&#91;3A,7V,2&#93;,&#91;2A,2V,3&#93;,&#91;2A,2.2V&#93;,&#91;3A,1.4V&#93;&#93;) | &#91;1A,1V&#93; |

####  Punkte-Mengen-Funktionen
Bei der Eingabe mit dem Plot-Plugin werden Punkte-Mengen als Matrizen in der Form &#91;&#91;x1,y1&#93;,&#91;x2,y2&#93;,&#91;y3,y3&#93;&#93;&#93; für die gespeicherten Punkte welcher der Schüler eingegeben hat verwendet.

Um die Verarbeitung der Eingaben zu erleichtern kann man die Funktionen beginnend mit pv verwenden.

| Funktion      | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Beispiel                                                                                                                                                                                            | Ergebnis                                                                                                                                          | ab Rev |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| pvabs         | Bestimmt den Betrag eines Punktes oder aller Ortsvektoren zu den Punkten. [DEMO-Beispiel](../../demobsp.html?id=3387)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | pvabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) <br> pvabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1)                                          | &#91;3.6056,6.4031,6.7082,4.4721&#93; <br> 6.4031                                                                                                 | 6077   |
| pvarg         | Bestimmt den Winkel eines Punktes oder aller Ortsvektoren zu den Punkten. [DEMO-Beispiel](../../demobsp.html?id=3388)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | pvarg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) <br> pvarg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1)                                          | &#91;0.98279,0.89606,0.46365,2.0344&#93; <br> 0.89606                                                                                             | 6077   |
| pvget         | Liefert einen Punkt der Punkteliste. [DEMO-Beispiel](../../demobsp.html?id=3389)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | pvget(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1)                                                                                                                         | &#91;4,5&#93;                                                                                                                                     | 6077   |
| pvgetx        | Bestimmt die x-Koordinate eines Punktes oder aller Punkte. [DEMO-Beispiel](../../demobsp.html?id=3390)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | pvgetx(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) <br> pvgetx(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1)                                        | &#91;2,4,6,-2&#93;<br>4                                                                                                                           | 6077   |
| pvgety        | Bestimmt die y-Koordinate eines Punktes oder aller Punkte. [DEMO-Beispiel](../../demobsp.html?id=3391)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | pvgety(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) <br> pvgety(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1)                                        | &#91;3,5,3,4&#93;<br>3                                                                                                                            | 6077   |
| pvinsert      | Fügt einen Punkt in die Punktemenge ein [DEMO-Beispiel](../../demobsp.html?id=3392)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | pvinsert(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,&#91;7,8&#93;,2)                                                                                                        | &#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;7,8&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;                                                                  | 6678   |
| pvinsertlast  | Fügt am Ende der Punktemenge einen Punkt ein [DEMO-Beispiel](../../demobsp.html?id=3393)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | pvinsertlast(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,&#91;7,8&#93;)                                                                                                      | &#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;7,8&#93;&#93;                                                                  | 6678   |
| pvremove      | Löscht einen Punkt aus der Punktemenge [DEMO-Beispiel](../../demobsp.html?id=3394)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | pvremove(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,2)                                                                                                                      | &#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;-2,4&#93;&#93;                                                                                              | 6678   |
| pvdistance    | Bestimmt die Abstände als Vektoren zwischen den Punkten. pvdistance(&#91;A,B,C&#93;) liefert &#91;AB,BC,CA&#93; [DEMO-Beispiel](../../demobsp.html?id=3395)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | pvdistance(&#91;&#91;1,2&#93;,&#91;3,4&#93;,&#91;10,10&#93;&#93;)                                                                                                                                   | &#91;&#91;2,2&#93;,&#91;7,6&#93;,&#91;-9,-8&#93;&#93;                                                                                             | 6569   |
| pvlineabs     | Bestimmt aus dem n-ten Punktepaar den Absolutbetrag des Abstandes. [DEMO-Beispiel](../../demobsp.html?id=3396)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | pvlineabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvlineabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0)                                    | &#91;2.8284,8.0623&#93;<br>2.82842712475                                                                                                          | 6075   |
| pvlinearg     | Bestimmt aus dem n-ten Punktepaar den Winkel der Strecke zur x-Achse [DEMO-Beispiel](../../demobsp.html?id=3397)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | pvlinearg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvlinearg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0)                                    | &#91;45°,172.87°&#93;<br>45°                                                                                                                      | 6075   |
| pvlinek       | Bestimmt die Steigung der zugehörigen Geraden dem n-ten Punktepaar [DEMO-Beispiel](../../demobsp.html?id=3398)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | pvlinek(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvlinek(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0)                                        | &#91;1,−0.125&#93;<br>1                                                                                                                           | 6075   |
| pvlined       | Bestimmt den Schnittpunkt einer Geraden durch das n-te Punktepaar mit der y-Achse [DEMO-Beispiel](../../demobsp.html?id=3399)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | pvlined(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvlined(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0)                                        | &#91;1,3.75&#93; <br>1                                                                                                                            | 6075   |
| pvline        | Bestimmt die Geradengleichung einer Geraden durch das n-te Punktepaar [DEMO-Beispiel](../../demobsp.html?id=3400)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | pvline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0)                                          | &#91;y=1+x,y=3.75−0.125⋅x&#93;<br>y=x+1                                                                                                           | 6075   |
| pvpoints      | Bestimmt die Anzahl der Punkte [DEMO-Beispiel](../../demobsp.html?id=3401)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | pvpoints(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)                                                                                                                        | 4                                                                                                                                                 | 6075   |
| pvlines       | Bestimmt die Anzahl der Linien bzw. Punktepaare eines Punktevektors. | pvlines(&#91;&#91;1,2&#93;,&#91;3,4&#93;,&#91;5,6&#93;,&#91;7,8&#93;&#93;) | 2 | |
| pvvect        | Bestimmt einen Vector aus dem n-te Punktepaar [DEMO-Beispiel](../../demobsp.html?id=3402)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | pvvect(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0)                                                                                                                        | &#91;2,2&#93;                                                                                                                                     | 6075   |
| pvrect        | Liefert aus einer Punktewolke ein Rechteck als zwei Eckpunkte links-unten und rechts-oben. | pvrect(&#91;&#91;1,2&#93;,&#91;4,5&#93;,&#91;2,3&#93;&#93;) | &#91;&#91;1,2&#93;,&#91;4,5&#93;&#93; | |
| pvsort        | Sortiert die Punkte zuerst nach steigender x-Koordinate und bei gleicher x-Koordinate nach steigender y-Koordinate. | pvsort(&#91;&#91;2,3&#93;,&#91;1,5&#93;,&#91;1,2&#93;&#93;) | &#91;&#91;1,2&#93;,&#91;1,5&#93;,&#91;2,3&#93;&#93; | |
| pvsortx       | Sortiert die Punkte nach steigender x-Koordinate [DEMO-Beispiel](../../demobsp.html?id=3403)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | pvsortx(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;)                                                                                          | &#91;&#91;−7,−9&#93;,&#91;−3,5&#93;,&#91;−2,4&#93;,&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;&#93;                                                 | 6077   |
| pvsorty       | Sortiert die Punkte nach steigender y-Koordinate [DEMO-Beispiel](../../demobsp.html?id=3404)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | pvsorty(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;)                                                                                          | &#91;&#91;−7,−9&#93;,&#91;2,3&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;4,5&#93;,&#91;−3,5&#93;&#93;                                                 | 6077   |
| pvsortabs     | Sortiert die Punkte nach steigendem Absolutbetrag des Ortsvektors [DEMO-Beispiel](../../demobsp.html?id=3405)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | pvsortabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;)                                                                                        | &#91;&#91;2,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−7,−9&#93;&#93;                                                 | 6077   |
| pvsortarg     | Sortiert die Punkte nach steigendem Winkel des Ortsvektors (-pi bis pi) [DEMO-Beispiel](../../demobsp.html?id=3406)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | pvsortarg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;)                                                                                        | &#91;&#91;−7,−9&#93;,&#91;6,3&#93;,&#91;4,5&#93;,&#91;2,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;&#93;                                                 | 6077   |
| pvsortlinex   | Sortiert Punktepaare nach steigender x-Koordinate der kleineren x-Koordinate des Paares. [DEMO-Beispiel](../../demobsp.html?id=3407)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | pvsortlinex(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;)                                                                                      | &#91;&#91;−3,5&#93;,&#91;−7,−9&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;2,3&#93;,&#91;4,5&#93;&#93;                                                 | 6077   |
| pvsortliney   | Sortiert Punktepaare nach steigender y-Koordinate der kleineren y-Koordinate des Paares. [DEMO-Beispiel](../../demobsp.html?id=3408)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | pvsortliney(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;)                                                                                      | &#91;&#91;−3,5&#93;,&#91;−7,−9&#93;,&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;&#93;                                                 | 6077   |
| pvsortlineabs | Sortiert Punktepaare nach steigendem Betrag der Linienlänge. [DEMO-Beispiel](../../demobsp.html?id=3409)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | pvsortlineabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;)                                                                                    | &#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;                                                 | 6077   |
| pvsortlinearg | Sortiert Punktepaare nach steigendem Winkel der Linienrichtung. [DEMO-Beispiel](../../demobsp.html?id=3410)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | pvsortlinearg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;)                                                                                    | &#91;&#91;−3,5&#93;,&#91;−7,−9&#93;,&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;&#93;                                                 | 6077   |
| pvequals      | Prüft ob zwei Punktevektoren gleich sind. Die Genauigkeit wird als dritter Parameter angegeben, oder bei einem Antwortfeld von der Antworttoleranz genommen. Prozentangaben der Genauigkeit beziehen sich auf die Breite bzw. Höhe des Punktefeldes im karthesischen Koordinatensystem. [DEMO-Beispiel](../../demobsp.html?id=3412)                                                                                                                                                                                                                                                                                            | pvequals(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,&#91;4,5&#93;,&#91;6.01,3&#93;,&#91;-2,3.99&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,2%) | true                                                                                                                                              | 6077   |
| pvhaspoint    | Prüft ob sich ein Punkt innerhalb des Punktefeldes befindet. Die Genauigkeit kann wie bei pvequals als dritter Parameter angegeben werden. [DEMO-Beispiel](../../demobsp.html?id=3413)                                                                                                                                                                                                                                                                                                                                                                                                                                         | pvhaspoint(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,&#91;4,5&#93;,2%)                                                                      | true                                                                                                                                              | 6077   |
| pvhasline     | Prüft ob sich eine Linie innerhalb des Punktefeldes von Linien befindet. Die Genauigkeit kann wie bei pvequals als dritter Parameter angegeben werden. [DEMO-Beispiel](../../demobsp.html?id=3414)                                                                                                                                                                                                                                                                                                                                                                                                                             | pvhasline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,&#91;&#91;6,3&#93;,&#91;-2,4&#93;&#93;,2%)                                         | true                                                                                                                                              | 6078   |
| pvforeachline | Führt für jedes Punktepaar eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion [DEMO-Beispiel](../../demobsp.html?id=3416)                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | pvforeachline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,p,pvlineabs(p),"+")                                                                                                | 10.890684873                                                                                                                                      | 6075   |
| pvfunc        | Erzeugt aus einer Funktionen in einer Variablen (x-Achse) eine Punktmatrix der Funktionswerte (y-Achse). pvfunc(funktion,variable,minx,maxx,deltax) [DEMO-Beispiel](../../demobsp.html?id=3417)                                                                                                                                                                                                                                                                                                                                                                                                                                | pvfunc(x^2,x,-2,2,0.5)                                                                                                                                                                              | &#91;&#91;−2,4&#93;,&#91;−1.5,2.25&#93;,&#91;−1,1&#93;,&#91;−0.5,0.25&#93;,&#91;0,0&#93;,&#91;0.5,0.25&#93;,&#91;1,1&#93;,&#91;1.5,2.25&#93;&#93; | 6080   |
| pvcompare     | Vergleicht einen Referenz-Linienzug mit einem eingegebenen Linienzug unter Berücksichtigung der Toleranz. Die Toleranz stellt eine relative Tolerenz bezogen auf den Bereich zwischen MinXY und MaxXY da, wobei eine Toleranz von 0.1 gleichbedeutend 10 Prozent bezogen auf Max-Min ist (Mit dem String "a0.1" könnte man auch ein absolute Toleranz von 0.1 für x und y realisieren) <br> pvcompare(Referenz,Eingabe)<br> pvcompare(Referenz,Eingabe,Toleranz)<br> pvcompare(Referenz,Eingabe,MinX,MaxX,MinY,MaxY) <br> pvcompare(Referenz,Eingabe,MinX,MaxX,MinY,MaxY,Toleranz) [DEMO-Beispiel](../../demobsp.html?id=3419) | pvcompare(&#91;&#91;0,0&#93;,&#91;1,1&#93;,&#91;2,1&#93;,&#91;3,0&#93;&#93;,&#91;&#91;0,0&#93;,&#91;1,1&#93;,&#91;2,1&#93;,&#91;3,0&#93;&#93;,0,3,-5,5)                                             | true                                                                                                                                              | 6080   |
| pvunion       | hängt mehrere Punktevektoren zu einem größereren Punktevektor zusammen [DEMO-Beispiel](../../demobsp.html?id=3421)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | pvunion(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;,&#91;&#91;5,6&#93;,&#91;7,8&#93;&#93;,&#91;9,10&#93;)                                                                                                 | &#91;&#91;1,2&#93;,&#91;3,4&#93;,&#91;5,6&#93;,&#91;7,8&#93;,&#91;9,10&#93;&#93;                                                                  | 6569   |


#### Typ-Funktionen
Werden nur dann ausgewertet wenn der Parameter ein numerischer Wert oder eine Menge ist.

| Funktion     | Beschreibung                                                                                           | Beispiel                           | Ergebnis |
|--------------|--------------------------------------------------------------------------------------------------------|------------------------------------|----------|
| isset        | Prüft ob es sich um eine Menge handelt. [DEMO-Beispiel](../../demobsp.html?id=3422)                    | isset(&#91;12,13,14&#93;)          | true     |
| issetnumeric | Prüft ob es sich um eine Menge aus reellen Zahlen handelt. [DEMO-Beispiel](../../demobsp.html?id=3423) | issetnumeric(&#91;12,13.4,14&#93;) | true     |
| issetlong    | Prüft ob es sich um eine Menge aus ganzen Zahlen handelt. [DEMO-Beispiel](../../demobsp.html?id=3424)  | issetlong(&#91;12,13,14&#93;)      | true     |
| islong       | Prüft ob es sich um eine ganze Zahl handelt. [DEMO-Beispiel](../../demobsp.html?id=3425)               | islong(12)                         | true     |


#### Algebra
##### Index von Matrizen
* Als Parameter von Matrix-, PV- und Vektor-**Funktion** beginnt der Index immer **bei 0 zu zählen**.
* Greift man über den Namen und **eckige Klammer** auf den Index zu wird der Maxima-kompatible Index verwendet welcher **bei 1 zu zählen** beginnt.
  Beispiel:
<pre>
M:&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;
a:vget(M,1,2)
b:M&#91;2,3&#93;
c:M&#91;2&#93;&#91;3&#93;
</pre>
a,b,c liefert immer das gleiche Element der Matrix!

##### Funktionen

| Funktion    | Beschreibung                                                                                                                                                                                                                                                  | Beispiel                                                                                                    | Ergebnis                                                                                        |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| matrix      | erzeugt aus mehreren gleich langen Vektoren eine Matrix [DEMO-Beispiel](../../demobsp.html?id=3426)                                                                                                                                                           | matrix([1,2&#93;,&#91;3,4&#93;)                                                                               | &#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;                                                           |
| vmatrix     | Erzeugt aus genau einem Vektor eine Matrix. Enthaltene Vektoren werden zu Matrixzeilen, einzelne Werte zu ein-elementigen Zeilen; eine Matrix wird unverändert zurückgegeben. | vmatrix(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;) | &#91;&#91;1,2&#93;,&#91;3,4&#93;&#93; |
| inv         | invertiert eine quadratische Matrix oder bildet 1/x [DEMO-Beispiel](../../demobsp.html?id=3427)                                                                                                                                                               | inv(matrix(&#91;1,2&#93;,&#91;3,4&#93;))                                                                          | &#91;&#91;-2,1&#93;,&#91;3/2,-1/2&#93;&#93;                                                     |
| vget        | liefert ein Element eines Vektors oder einer Matrix [Video](https://www.youtube.com/watch?v=T82YIt3e8ac) [DEMO-Beispiel](../../demobsp.html?id=3428)                                                                                                          | vget(&#91;12,13,14&#93;,1) <br> vget(matrix(&#91;9,2&#93;,&#91;3,4&#93;),0,1)                                   | 13 <br> 2                                                                                       |
| first       | liefert das erste Element mit dem Index 0 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3429)                                                                                                                                                           | first(&#91;12,13,14&#93;)                                                                                 | 12                                                                                              |
| second      | liefert das zweite Element mit dem Index 1 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3430)                                                                                                                                                          | second(&#91;12,13,14&#93;)                                                                                | 13                                                                                              |
| third       | liefert das dritte Element mit dem Index 2 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3431)                                                                                                                                                          | third(&#91;12,13,14&#93;)                                                                                 | 14                                                                                              |
| fourth      | liefert das vierte Element mit dem Index 3 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3432)                                                                                                                                                          | fourth (&#91;12,13,14,15,16,17,18&#93;)                                                       | 15                                                                                              |
| fifth       | liefert das fünfte Element mit dem Index 4 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3433)                                                                                                                                                          | fifth (&#91;12,13,14,15,16,17,18&#93;)                                                        | 16                                                                                              |
| sixth       | liefert das sechste Element mit dem Index 5 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3434)                                                                                                                                                         | sixth (&#91;12,13,14,15,16,17,18&#93;)                                                        | 17                                                                                              |
| last        | liefert das letzte Element eines Vektors                                                                                                                                                          | first(&#91;12,13,14&#93;)                                                                                 | 14                                                                                            |
| vgetmaxima  | liefert ein Element eines Vektors oder einer Matrix wobei der Index (wie bei Maxima) bei 1 startet. [DEMO-Beispiel](../../demobsp.html?id=3435)                                                                                                               | vgetmaxima(&#91;12,13,14&#93;,1)                                                                          | 12                                                                                              |
| vset        | setzt ein Element eines Vektors oder einer Matrix [DEMO-Beispiel](../../demobsp.html?id=3436)                                                                                                                                                                 | vset(&#91;12,13,14&#93;,1,35) <br> vset(matrix(&#91;9,2&#93;,&#91;3,4&#93;),0,0,-9)                             | &#91;12,35,14&#93; <br> &#91;&#91;-9,2&#93;,&#91;3,4&#93;&#93;                                  |
| vsetmaxima  | setzt ein Element eines Vektors oder einer Matrix wobei der Index (wie bei Maxima) bei 1 startet. [DEMO-Beispiel](../../demobsp.html?id=3437)                                                                                                                 | vsetmaxima(&#91;12,13,14&#93;,1,35)                                                                       | &#91;35,13,14&#93;                                                                              |
| vinsert     | fügt ein Element in einen Vektor an eine gegebene Stelle ein [DEMO-Beispiel](../../demobsp.html?id=3438)                                                                                                                                                      | vinsert(&#91;12,13,14&#93;,1,25)                                                                          | &#91;12,25,13,14&#93;                                                                           |
| vremove     | löscht ein Element eines Vektors [Video](https://www.youtube.com/watch?v=T82YIt3e8ac) [DEMO-Beispiel](../../demobsp.html?id=3439)                                                                                                                             | vremove(&#91;12,13,14&#93;,1)                                                                             | &#91;12,14&#93;                                                                                 |
| vabs        | Berechnet den Betrag eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3440)                                                                                                                                                                                | vabs(&#91;3,4&#93;)                                                                                            | 5                                                                                               |
| vin         | Berechnet das innere Produkt von 2 Vektoren [DEMO-Beispiel](../../demobsp.html?id=3441)                                                                                                                                                                       | vin(&#91;1,2,3&#93;,&#91;4,5,6&#93;)                                                                          | 32                                                                                              |
| vex         | Berechnet das ex-Produkt von 2 Vektoren im 3-dimensionalen Raum [DEMO-Beispiel](../../demobsp.html?id=3442)                                                                                                                                                   | vex(&#91;1,2,3&#93;,&#91;4,5,6&#93;)                                                                          | &#91;-3,6,-3&#93;                                                                               |
| vadd        | Addiert zwei Vektoren elementweise [DEMO-Beispiel](../../demobsp.html?id=3443)                                                                                                                                                                                | vadd(&#91;1,2,3&#93;,&#91;4,5,6&#93;)                                                                         | &#91;5,7,9&#93;                                                                                 |
| vsub        | Subtrahiert zwei Vektoren elementweise [DEMO-Beispiel](../../demobsp.html?id=3444)                                                                                                                                                                            | vsub(&#91;1,2,3&#93;,&#91;4,5,6&#93;)                                                                         | &#91;-3,-3,-3&#93;                                                                              |
| vmul        | Multipliziert zwei Vektoren elementweise [DEMO-Beispiel](../../demobsp.html?id=3445)                                                                                                                                                                          | vmul(&#91;1,2,3&#93;,&#91;4,5,6&#93;)                                                                         | &#91;4,10,18&#93;                                                                               |
| vdiv        | Dividiert zwei Vektoren elementweise [DEMO-Beispiel](../../demobsp.html?id=3446)                                                                                                                                                                              | vdiv(&#91;1,2,3&#93;,&#91;4,5,6&#93;)                                                                         | &#91;1/3,2/5,3/6&#93;                                                                           |
| vpow        | Potenziert zwei Vektoren elementweise [DEMO-Beispiel](../../demobsp.html?id=3447)                                                                                                                                                                             | vpow(&#91;1,2,3&#93;,&#91;4,5,6&#93;)                                                                         | &#91;1,32,729&#93;                                                                              |
| mrows       | liefert die Anzahl der Zeilen einer Matrix [DEMO-Beispiel](../../demobsp.html?id=3448)                                                                                                                                                                        | mrows(&#91;&#91;3,4,4&#93;,&#91;3,6,54,34,3,54&#93;&#93;)                                                   | 2                                                                                               |
| mcols       | liefert die Anzahl der Spalten einer Matrix [DEMO-Beispiel](../../demobsp.html?id=3449)                                                                                                                                                                       | mcols(&#91;&#91;3,4,4&#93;,&#91;3,6,54,34,3,54&#93;&#93;)                                                   | 6                                                                                               |
| mprod       | Bildet das Matrixprodukt aus zwei Matrizen [DEMO-Beispiel](../../demobsp.html?id=3450)                                                                                                                                                                        | mprod(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;,&#91;&#91;5,6&#93;,&#91;7,8&#93;&#93;)                                                    | &#91;&#91;19,22&#93;,&#91;43,50&#93;&#93;                                                       |
| mtrans      | Bildet die transponierte Matrix [DEMO-Beispiel](../../demobsp.html?id=3451)                                                                                                                                                                                   | mtrans(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;)                                                                            | &#91;&#91;1,3&#93;,&#91;2,4&#93;&#93;                                                           |
| minv        | Bildet die inverse Matrix [DEMO-Beispiel](../../demobsp.html?id=3452)                                                                                                                                                                                         | minv(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;)                                                                              | &#91;&#91;-2,1&#93;,&#91;3/2,-1/2&#93;&#93;                                                     |
| mdet        | Bildet die Determinante einer quadratischen Matrix [DEMO-Beispiel](../../demobsp.html?id=3453)                                                                                                                                                                | mdet(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;)                                                                              | -2                                                                                              |
| mcunion     | Fügt mehrere Matrizen oder Vektoren spaltenweise(nebeneinander) zusammen [DEMO-Beispiel](../../demobsp.html?id=3454)                                                                                                                                          | mcunion(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,&#91;&#91;10,11&#93;,&#91;12,13&#93;,&#91;14,15&#93;&#93;)    | &#91;&#91;1,2,3,10,11&#93;,&#91;4,5,6,12,13&#93;,&#91;7,8,9,14,15&#93;&#93;                     |
| mrunion     | Fügt mehrere Matrizen oder Vektoren zeileweise(untereinander) zusammen [DEMO-Beispiel](../../demobsp.html?id=3455)                                                                                                                                            | mrunion(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,&#91;&#91;10,11,12&#93;,&#91;13,14,15&#93;&#93;)       | &#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;,&#91;10,11,12&#93;,&#91;13,14,15&#93;&#93; |
| msub        | msub(matrix,zeile,spalte,zeilen,spalten) Liefert eine Untermatrix beginnend bei Zeile und Spalten mit der angegebenen Anzahl von Zeilen und Spalten. Die Parameter Spalte,Zeilen und Spalten sind dabei optional. [DEMO-Beispiel](../../demobsp.html?id=3456) | msub(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,0,1,2,2)                                               | &#91;&#91;2,3&#93;,&#91;5,6&#93;&#93;                                                           |
| mcinsert    | mcinsert(matrix,matrixodervektor,position) Fügt an der Spaltenposition eine Matrix oder einen Vektor als neue Spalten ein [DEMO-Beispiel](../../demobsp.html?id=3457)                                                                                         | mcinsert(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,&#91;&#91;10,11&#93;,&#91;12,13&#93;,&#91;14,15&#93;&#93;,1) | &#91;&#91;1,10,11,2,3&#93;,&#91;4,12,13,5,6&#93;,&#91;7,14,15,8,9&#93;&#93;                     |
| mrinsert    | mrinsert(matrix,matrixodervektor,position) Fügt an der Zeilenposition eine Matrix oder einen Vektor als neue Zeilen ein [DEMO-Beispiel](../../demobsp.html?id=3459)                                                                                           | mrinsert(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,&#91;&#91;10,11,12&#93;,&#91;13,14,15&#93;&#93;,1)    | &#91;&#91;1,2,3&#93;,&#91;10,11,12&#93;,&#91;13,14,15&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93; |
| mcdelete    | mcdelete(matrix,position) Löscht die angegebene Spalte aus einer Matrix [DEMO-Beispiel](../../demobsp.html?id=3460)                                                                                                                                           | mcdelete(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,1)                                                 | &#91;&#91;1,3&#93;,&#91;4,6&#93;,&#91;7,9&#93;&#93;                                             |
| mrdelete    | mrdelete(matrix,position) Löscht die angegebene Zeile aus einer Matrix [DEMO-Beispiel](../../demobsp.html?id=3461)                                                                                                                                            | mrdelete(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,1)                                                 | &#91;&#91;1,2,3&#93;,&#91;7,8,9&#93;&#93;                                                       |
| vindex      | vindex(v,x) liefert den Index des Elementes eines Vektors, welcher am nächsten bei x liegt [DEMO-Beispiel](../../demobsp.html?id=3462)                                                                                                                        | vindex(&#91;10,30,70&#93;,40)                                                                             | 1                                                                                               |
| vindexup    | vindexup(v,x) liefert den Index des Elementes eines Vektors, welcher größer oder gleich x ist [DEMO-Beispiel](../../demobsp.html?id=3463)                                                                                                                     | vindexup(&#91;10,30,70&#93;,40)                                                                           | 2                                                                                               |
| vindexdown  | vindexdown(v,x) liefert den Index des Elementes eines Vektors, welcher kleiner oder gleich x ist [DEMO-Beispiel](../../demobsp.html?id=3464)                                                                                                                  | vindexdown(&#91;10,30,70&#93;,60)                                                                         | 1                                                                                               |
| verweis     | verweis(M,x,n) liefert den Wert der n-ten Spalte (ohne Angabe von n die 2.Spalte) einer Matrix M wo x dem Wert in der ersten Spalte am nächsten liegt [DEMO-Beispiel](../../demobsp.html?id=3465)                                                             | verweis(&#91;&#91;10,33&#93;,&#91;20,77&#93;,&#91;30,99&#93;&#93;,21)                                                 | 77                                                                                              |
| verweisup   | verweisup(M,x,n) liefert den Wert der n-ten Spalte (ohne Angabe von n die 2.Spalte) einer Matrix M wo x dem Wert in der ersten Spalte am nächsten liegt [DEMO-Beispiel](../../demobsp.html?id=3466)                                                           | verweisup(&#91;&#91;10,33&#93;,&#91;20,77&#93;,&#91;30,99&#93;&#93;,21)                                               | 99                                                                                              |
| verweisdown | verweisdown(M,x,n) liefert den Wert der n-ten Spalte (ohne Angabe von n die 2.Spalte) einer Matrix M wo x dem Wert in der ersten Spalte am nächsten liegt [DEMO-Beispiel](../../demobsp.html?id=3467)                                                         | verweisdown(&#91;&#91;10,33&#93;,&#91;20,77&#93;,&#91;30,99&#93;&#93;,27,1)                                           | 77                                                                                              |
| range       | range(anzahl) liefert ein Feld von ganzzahligen Werten von 0 beginnend [DEMO-Beispiel](../../demobsp.html?id=3468)                                                                                                                                            | range(5)                                                                                                    | &#91;0,1,2,3,4&#93;                                                                             |
| linspace    | linspace(start,ende,anzahl) liefert ein Feld von Werte von Startwert bis Endwert mit gleichem Abstand [DEMO-Beispiel](../../demobsp.html?id=3469)                                                                                                             | linspace(4,8,5)                                                                                             | &#91;4,5,6,7,8&#93;                                                                             |
| logspace    | logspace(start,ende,anzahl) liefert ein Feld von Werte von Startwert bis Endwert mit gleichem logarithmischen Abstand [DEMO-Beispiel](../../demobsp.html?id=3470)                                                                                             | logspace(10,10000,4)                                                                                        | &#91;10,100,1000,10000&#93;                                                                     |


#### Variable

| Funktion | Beschreibung                                                                                                                                                      | Beispiel                                      | Ergebnis                                                                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|------------------------------------------------------------------------------------------------------|
| kill     | löscht Variable aus dem Variablenspeicher [DEMO-Beispiel](../../demobsp.html?id=3471)                                                                             | kill(x,y) <br> kill(allbut(y)) <br> kill(all) | löscht die Variablen x und y <br> löscht alle Variablen mit Ausnahme von y <br> löscht alle Variable |
| allbut   | Liefert eine Liste aller Variablen des Parsers als Menge(Vektor) mit Ausnahme der als Parameter angegebenen Variablen [DEMO-Beispiel](../../demobsp.html?id=3472) | allbut(x,y)                                   | &#91;a,b,c&#93;                                                                                        |


#### Auswertung und Programmierung

| Funktion                         | Beschreibung                                                                                                                                                                                                                                                                                                                                                                       | Beispiel                                                                                   | Ergebnis                                                                          | Revision |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|----------|
| ev                               | Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden [DEMO-Beispiel](../../demobsp.html?id=3473)                                                                                                                                                                                                          | ev(x*y,y=4)                                                                                | x*4                                                                               |          |
| evruntime                        | Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden. Das **Einsetzen erfolgt erst bei der Ergebnisberechnung**! [DEMO-Beispiel](../../demobsp.html?id=3474)                                                                                                                                              | evruntime(x*y,y=4)                                                                         | x*4                                                                               |          |
| [nv](/notimplemented/index.md)   | Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden. Im Gegensatz zu ev werden bestehende Variable nur in den Gleichungen, aber nicht im Ausdruck selbst eingesetzt! [DEMO-Beispiel](../../demobsp.html?id=3475)                                                                                         | nv(x*y,y=4)                                                                                | x*4                                                                               |          |
| [if](/notimplemented/index.md)   | Bedingungsfunktion if(bedingung,wahrwert,falschwert) [DEMO-Beispiel](../../demobsp.html?id=3476)                                                                                                                                                                                                                                                                                   | if(4&lt;6,10,12)                                                                           | 10                                                                                |          |
| [wenn](/notimplemented/index.md) | Bedingungsfunktion wenn(bedingung,wahrwert,falschwert). Im Prinzip identisch wie if, jedoch kann if mit Maxima nicht verwendet werden. [DEMO-Beispiel](../../demobsp.html?id=3477)                                                                                                                                                                                                 | wenn(4&lt;6,10,12)                                                                         | 10                                                                                |          |
| plugin                           | Ruft die Berechnungsmethode des Plugins, welches als erster Stringparameter angegeben werden muss auf und übergibt die weiteren Parameter an die Berechnungsmethode des Plugins. [DEMO-Beispiel](../../demobsp.html?id=3478)                                                                                                                                                       | plugin("plugin1",3)                                                                        | führt die Berechnung des Plugins mit dem Namen "plugin1" mit dem Parameter 3 aus. |          |
| symbolic                         | Bei allen Variablen innerhalb von symbolic werden nur nicht-numerische Werte eingesetzt! Wird vor allem im Angabtext bei {= } verwendet [DEMO-Beispiel](../../demobsp.html?id=3479)                                                                                                                                                                                                | symbolic(x^2+2)                                                                            | x^2+2                                                                             |          |
| runtime                          | Bei dieser Funktion wird **erst bei der Berechnung der Frageantwort, nach dem Einsetzen der Datensätze** das **komplette Maxima-Feld** mit dem internen **Parser** durchgerechnet und danach der Parameter-Ausdruck berechnet. Dadurch kann man bei komplizierten Berechnungen eine sehr aufwendige symbolische Berechnung verhindern! [DEMO-Beispiel](../../demobsp.html?id=3480) | runtime(U)                                                                                 |                                                                                   |          |
| dataset                          | liefert alle Datensätze einer Datensatz-Definition in einem Vektor [DEMO-Beispiel](../../demobsp.html?id=3481)                                                                                                                                                                                                                                                                     | dataset(x)                                                                                 |                                                                                   |          |
| parse                            | Wenn der Parameter ein String ist wird dieser String mit dem Parser interpretiert [DEMO-Beispiel](../../demobsp.html?id=3482)                                                                                                                                                                                                                                                      | parse("2+3")                                                                               | 5                                                                                 |          |
| foreach                          | Führt für jedes Element einer Menge eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion [DEMO-Beispiel](../../demobsp.html?id=3484)                                                                                                                                                                                                                          | foreach(&#91;2,-3,5,-6&#93;,p,cabs(p),"+")                                                   | 16                                                                                | 6075     |
| pvforeachline                    | Führt für jedes Punktepaar einer Punktemenge eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion [DEMO-Beispiel](../../demobsp.html?id=3485)                                                                                                                                                                                                                 | pvforeachline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,p,pvlineabs(p),"+") | 10.890684873                                                                      | 6075     |
| forloop                          | Führt eine Zählschleife aus forloop(Variable,Startwert,Wiederholbedingung,Inkrement,Ausdruck,Aggregatsfunktion). <br>Ohne Aggregatsfunktion wird ein Feld mit den Ergebnissen der Schleifeniterationen geliefert. [DEMO-Beispiel](../../demobsp.html?id=3486)                                                                                                                      | forloop(i,1,i&lt;7,i++,i,"+")<br>forloop(i,1,i&lt;7,i:i+2,i)                               | 21<br>&#91;1,3,5&#93;                                                               | 6077     |


#### Optimierung der Ausdrücke

| Funktion    | Beschreibung                                                                                                                                                                                                                                                                | Beispiel         | Ergebnis         |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------------|
| opt         | Ausdruck wird vollständig optimiert, die Funktion wird ausgewertet und ist danach nicht mehr vorhanden. Nur bei der Verwendung des internen Parser sinnvoll. [DEMO-Beispiel](../../demobsp.html?id=3489)                                                                    | opt(x+x)         | 2*x              |
| optorder    | Optimiert nur die symbolische Reihenfolge des Ausdrucks. Optional steuert ein zweiter ganzzahliger Modus, ob bzw. wie lange die Funktion im Ausdruck erhalten bleibt. | optorder(y+x) | x+y |
| number      | Erzwingt die numerische Auswertung aller numerisch berechenbaren Teile. Bleibt bei einem weiterhin symbolischen Ergebnis als Funktion erhalten. | number(2+3+x) | number(5+x) |
| mathe       | Wertet Ganzzahlen und Konstanten numerisch nur soweit aus, wie es der symbolische Mathematikmodus zulässt; ein symbolisches Ergebnis bleibt in `mathe(...)` erhalten. | mathe(2+3+x) | mathe(5+x) |
| ratsimp     | Ausdruck wird vollständig optimiert, die Funktion wird ausgewertet und ist danach nicht mehr vorhanden (wie opt, wird jedoch auch von Maxima ausgewertet) [DEMO-Beispiel](../../demobsp.html?id=3490)                                                                       | ratsimp(x+x)     | 2*x              |
| noopt       | Ausdruck wird nicht optimiert, bleibt also so erhalten wie angegeben. Die Funktion an sich geht aber verloren. [DEMO-Beispiel](../../demobsp.html?id=3491)                                                                                                                  | noopt(2+3)       | 2+3              |
| nopt        | Ausdruck wird nicht optimiert, bleibt also so erhalten wie angegeben. Die Funktion bleibt erhalten und wird erst bei der Lösungsberechnung oder durch opt() entfernt. [DEMO-Beispiel](../../demobsp.html?id=3492)                                                           | noopt(2+3)       | 2+3              |
| lopt        | Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {=  wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck vollständig optimiert. [DEMO-Beispiel](../../demobsp.html?id=3493)                                    | lopt(x+3)        | lopt(x+3)        |
| qopt        | Im Maximafeld wird alles innerhalb der Funktion nicht ausgewertet und die Funktion bleibt erhalten, bei der Lösung wird nach dem Einsetzen der Werte der Ausdruck vollständig optimiert. <br> Anwendung findet die Funktion bei boolschen Fragen und Folgefehlerbehandlung. | qopt(x+3)        | qopt(x+3)        |
| lnoopt      | Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {=  wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck nicht mehr optimiert.                                                                                 | lnoopt(x+3+2)    | lnoopt(x+5)      |
| loptnumeric | Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {=  wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck nur numerisch optimiert.                                                                              | loptnumeric(x+y) | loptnumeric(x+y) |
| aopt        | Bei Maxima und Lösung geht die Funktion verloren, nur innerhalb von noopt bleibt sie erhalten. Bei der Anzeige führt sie zur Optimierung das Ausdruckes nach Einsetzen der Datensätze.                                                                                      | aopt(x)          | x                |


#### Anzeige und Lösungsberechnung
Diese Funktionen haben entweder einen oder zwei Parameter. Der erste Parameter stellt die darzustellende Funktion dar, der zweite Parameter, welcher eine Ganzzahl sein muss, gibt an, wie die Darstellung erfolgen soll. Wird der 2.Parameter weggelassen, so wird er als 0 interpretiert.
* 0 Bei Berechnungen hat die Funktion keine Wirkung, bleibt aber als Funktion erhalten. Bei Lösung und Anzeige wird die Funktion ausgewertet
* 1 Wirkt nur bei Lösung, bei Berechnungen bleibt die Funktion erhalten
* 2 Wirkt nur bei Anzeige, bei Berechnungen bleibt die Funktion erhalten

| Funktion | Beschreibung                                                                                                                                              | Beispiel          | Ergebnis |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------|
| viewpow  | Gibt alle Wurzeln als Potenzen aus, und stellt alle Potenzen im Nenner als negativen Exponenten im Zähler dar [DEMO-Beispiel](../../demobsp.html?id=3495) | viewpow(sqrt(x))  | x^(1/2)  |
| viewsqrt | Gibt Potenzen welche als Wurzel darstellbar sind auch als als Wurzeln mit der Funktion sqrt oder root aus [DEMO-Beispiel](../../demobsp.html?id=3496)     | viewsqrt(x^(1/2)) | sqrt(x)  |


####  Datums und Zeitfunktionen

| Funktion       | Beschreibung                                                                                                                        | Beispiel | Ergebnis | REvision |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------|----------|----------|----------|
| dateparse      | Wandelt einen String in ein Datum als Ganzzahl in Sekunden seit 1.1.0000 [DEMO-Beispiel](../../demobsp.html?id=3497)                |          |          | 6530     |
| date           | date(y,m,d,h,min,sec) erzeugt ein Datum als Ganzzahl in Sekunden seit 1.1.0000 00:00:00 [DEMO-Beispiel](../../demobsp.html?id=3634) |          |          | 6530     |
| date           | date(y,m,d) erzeugt ein Datum als Ganzzahl in Sekunden seit 1.1.0000 00:00:00 [DEMO-Beispiel](../../demobsp.html?id=3634)                                                      |          |          | 6530     |
| time           | time(h,min,sec) erzeugt eine Uhrzeit als Ganzzahl in Sekunden seit Mitternacht [DEMO-Beispiel](../../demobsp.html?id=3635)          |          |          | 6762     |
| datestring     | datestring(x) datestring(x,&quot;format&quot;) erzeugt aus einem Datum in Sekunden seit 1.1.0000 eine Stringausgabe                 |          |          | 6530     |
| timestring     | erzeugt eine Uhrzeit als String                                                                                                     |          |          | 6530     |
| datetimestring | erzeugt Datum und Uhrzeit als String                                                                                                |          |          | 6530     |
| dateyear       | Erzeugt aus einem Datum als Ganzzahl das Jahr                                                                                       |          |          | 6530     |
| datemonth      | Erzeugt aus einem Datum als Ganzzahl das Monat                                                                                      |          |          | 6530     |
| dateday        | Erzeugt aus einem Datum als Ganzzahl den Tag                                                                                        |          |          | 6530     |
| datehour       | Erzeugt aus einem Datum als Ganzzahl die Stunde                                                                                     |          |          | 6530     |
| dateminute     | Erzeugt aus einem Datum als Ganzzahl die Minute                                                                                     |          |          | 6530     |
| datesecond     | Erzeugt aus einem Datum als Ganzzahl die Sekunde                                                                                    |          |          | 6530     |
| datemix        | Erzeugt aus einem Datumswert (Sekunden seit 1.1.00 0:00:00) einen Vektor mit Jahr,Monat,Tag,Stunde,Minute,Sekunde                   |          |          | 6641     |
| datediff       | Rechnet die Differenz von 2 ganzzahligen Datumswerten. Erstes minus zweites Datum. Ergebnis als Double in Sekunden                  |          |          | 6530     |
| dateweekday    | Liefert den Wochentag beginnend mit Montag als 1 und Sonntag als 7                                                                  |          |          | 6530     |
| dateweek       | Liefert die Kalenderwoche des Tages innerhalb des Jahres                                                                            |          |          | 6530     |
| datedayofyear  | Liefert den Tag des Jahres                                                                                                          |          |          | 6530     |
| years          | Erzeugt aus einem Sekundenwert die Jahre (/365d) als Double ohne Einheit                                                            |          |          | 6530     |
| months         | Erzeugt aus einem Sekundenwert die Monate (/30d) als Double ohne Einheit                                                            |          |          | 6530     |
| weeks          | Erzeugt aus einem Sekundenwert die Wochen (/7d) als Double ohne Einheit                                                             |          |          | 6530     |
| days           | Erzeugt aus einem Sekundenwert die Tage als Double ohne Einheit                                                                     |          |          | 6530     |
| hours          | Erzeugt aus einem Sekundenwert die Stunden als Double ohne Einheit                                                                  |          |          | 6530     |
| minutes        | Erzeugt aus einem Sekundenwert die Minuten als Double ohne Einheit                                                                  |          |          | 6530     |
| seconds        | Erzeugt aus einem Sekundenwert die Sekunden als Double ohne Einheit                                                                 |          |          | 6530     |


####  Spezialfunktionen LeTTo

| Funktion | Beschreibung                                                                                                       | Beispiel  | Ergebnis |
|----------|--------------------------------------------------------------------------------------------------------------------|-----------|----------|
| points   | Berechnet die erreichbare Gesamtpunkteanzahl einer Frage [DEMO-Beispiel](../../demobsp.html?id=3498)               | points()  | 2        |
| points   | Berechnet die erreichbare Punkteanzahl einer Teilfrage. Als Parameter wird die Fragenummer als Ganzzahl angegeben. | points(0) | 1        |
| parser         | Markierungsfunktion für Ausdrücke, die von Maxima unverändert an den internen Parser weitergereicht werden sollen. Im internen Parser selbst wird lediglich der einzelne Parameter ausgewertet. | parser(x+1) | x+1 |
| declare        | Deklariert Variablentypen für die Maxima-Kompatibilität. Die Funktion ist im internen Parser derzeit noch nicht funktional umgesetzt und liefert dort `false`. | declare(x,real) | false |
| selective_kill | Löscht alle Variablen aus dem Variablenspeicher außer den angegebenen Variablen bzw. Variablenvektoren und liefert die Anzahl der gelöschten Variablen. | selective_kill(x,y) | Anzahl der gelöschten Variablen |
| stackoverflow  | **Test-/Diagnosefunktion:** erzeugt absichtlich einen StackOverflow. Nicht für reguläre Aufgaben verwenden. | stackoverflow() | Fehler |
| runtimeexception | **Test-/Diagnosefunktion:** erzeugt absichtlich eine RuntimeException. Ein optionaler Parameter wird als Fehlermeldung verwendet. | runtimeexception("Test") | Fehler |
| infiniteloop   | **Test-/Diagnosefunktion:** erzeugt absichtlich eine Endlosschleife und dient zum Testen der Timeout-Behandlung. Nicht für reguläre Aufgaben verwenden. | infiniteloop() | Timeout |
| delay          | **Test-/Diagnosefunktion:** verzögert die Auswertung um die angegebene Anzahl Sekunden und prüft dabei regelmäßig auf einen Timeout/Abbruch. | delay(1) | nach ca. 1 s |


#### Spezialfunktionen Technik

| Funktion   | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                      | Beispiel                          | Ergebnis                   |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|----------------------------|
| color      | Widerstandsfarbcode berechnen.<br>1. Parameter muss ein Double sein<br> 2. Parameter sind die Anzahl der Farbringe<br> 3. Parameter ist der Darstellungsmodus (0 = Deutsch ausgeschrieben, 1 = Abkürzung Deutsch mit drei Buchstaben, 2 = Abkürzung Deutsch mit zwei Buchstaben, 3 = Englisch ausgeschrieben, 4 = Abkürzung Englisch mit drei Buchstaben, 5 = Abkürzung Englisch mit zwei Buchstaben) [DEMO-Beispiel](../../demobsp.html?id=3499) | color(120,3,0)                    | braun,rot,braun            |
| parsecolor | Wandelt einen String mit einem Widerstandsfarbcode in einen Double-Wert [DEMO-Beispiel](../../demobsp.html?id=3500)                                                                                                                                                                                                                                                                                                                               | parsecolor("br-rt-br")            | 120                        |
| ip         | Wandelt eine Long-Zahl in einen String als IP-Adresse um, oder 4 Byte-Zahlen in eine Long Zahl als IP-32-bit-Adresse [DEMO-Beispiel](../../demobsp.html?id=3501)                                                                                                                                                                                                                                                                                  | ip(1534536453)<br>ip(10,20,30,40) | "91.119.43.5"<br>169090600 |
| parseip    | Wandelt einen String mit einer IP-Adresse in einen Long-Wert [DEMO-Beispiel](../../demobsp.html?id=3502)                                                                                                                                                                                                                                                                                                                                          | parseip("91.119.43.5")            | 1534536453                 |
| e12        | rundet einen Zahlenwert auf den nächstliegenden Wert der [Normreihe](../Normreihe/index.md) E12.<br>Die Rundung erfolgt geometrisch d.h. der Quotient zwischen Normwert und zu rundendem Wert wird minimiert. [DEMO-Beispiel](../../demobsp.html?id=3503)                                                                                                                                                                                         | e12(700Ohm)                       | 680Ohm                     |
| e12up      | rundet einen Zahlenwert auf den nächstgrößerern Wert der [Normreihe](../Normreihe/index.md) E12 [DEMO-Beispiel](../../demobsp.html?id=3504)                                                                                                                                                                                                                                                                                                       | e12(670Ohm)                       | 680Ohm                     |
| e12down    | rundet einen Zahlenwert auf den nächstkleineren Wert der [Normreihe](../Normreihe/index.md) E12 [DEMO-Beispiel](../../demobsp.html?id=3505)                                                                                                                                                                                                                                                                                                       | e12(700Ohm)                       | 680Ohm                     |
| ise12      | prüft ob der als Parameter übergebenen Wert ein Wert der [Normreihe](../Normreihe/index.md) E12 ist. [DEMO-Beispiel](../../demobsp.html?id=3506)                                                                                                                                                                                                                                                                                                  | ise12(680Ohm)                     | true                       |
| norm       | rundet einen Zahlenwert auf den nächstliegenden Wert einer gegebenen Wertereihe oder [Normreihe](../Normreihe/index.md).<br>Die Rundung erfolgt geometrisch wenn es sich um eine logarithmisch aufgeteilte Normreihe handelt, oder sonst linear. [DEMO-Beispiel](../../demobsp.html?id=3507)                                                                                                                                                      | norm(700Ohm,E12)                  | 680Ohm                     |
| normup     | rundet einen Zahlenwert auf den nächstgrößerern Wert einer gegebenen Wertereihe oder [Normreihe](../Normreihe/index.md). [DEMO-Beispiel](../../demobsp.html?id=3508)                                                                                                                                                                                                                                                                              | normup(730Ohm&#91;1,3,5,8&#93;)     | 800Ohm                     |
| normdown   | rundet einen Zahlenwert auf den nächstkleineren Wert einer gegebenen Wertereihe oder [Normreihe](../Normreihe/index.md). [DEMO-Beispiel](../../demobsp.html?id=3509)                                                                                                                                                                                                                                                                              | normdown(700Ohm,E12)              | 680Ohm                     |
| isnorm     | prüft ob der als Parameter übergebenen Wert ein Wert einer gegebenen Wertereihe oder [Normreihe](../Normreihe/index.md) ist. [DEMO-Beispiel](../../demobsp.html?id=3511)                                                                                                                                                                                                                                                                          | isnorm(680Ohm,E12)                | true                       |


#### Raumzeiger für elektrische Maschinen

| Funktion                                                       | Beschreibung                                                                                                                                                                                                          | Beispiel                                  | Ergebnis                   |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|----------------------------|
| [svphtosv](/notimplemented/index.md)(a,b,c)                    | berechnet aus den Stranggrößen (a,b,c) einen komplexen Raumzeiger [DEMO-Beispiel](../../demobsp.html?id=3512)                                                                                                         | svphtosv(0.5,0.5,-1)                      | 1arg60°                    |
| [svsvtoph](/notimplemented/index.md)(sv)<br>svsvtoph(sv,index) | berechnet aus einem komplexen Raumzeiger die Stranggrössen <br> berechnet aus einem komplexen Raumzeiger die Stranggrössen, index selektiert Stranggröße als Rückgabewert [DEMO-Beispiel](../../demobsp.html?id=3513) | svsvtoph(1arg60°)<br> svsvtoph(1arg60°,3) | &#91;0.5,0.5,-1&#93; <br> -1 |

### Detaillierte Parameterreferenz der Funktionen

Die folgenden Angaben werden aus den registrierten Parserfunktionen und deren Implementierung abgeleitet. Bei Funktionen mit mehreren zulässigen Parameterzahlen sind alle Aufrufvarianten angegeben. Datentypen bezeichnen die vom Parser akzeptierte bzw. erwartete Art des Parameters.

<details markdown="1">
<summary><code>abs(x)</code></summary>

Liefert den Absolutbetrag einer komplexen Zahl

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl | nein |

**Beispiel:** `abs(3+4*%i)`  
**Ergebnis:** 5

</details>

<details markdown="1">
<summary><code>acos(x1)</code></summary>

Arcus-Cosinus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `acos(1)`  
**Ergebnis:** 0

</details>

<details markdown="1">
<summary><code>acosh(x1)</code></summary>

Area-Cosinus-Hyperbolicus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `acosh(1.5430806)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>acot(x1)</code></summary>

Arcus-Cotangens.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `acot(1)`  
**Ergebnis:** %pi/4

</details>

<details markdown="1">
<summary><code>acoth(x1)</code></summary>

Area-Cotangens-Hyperbolicus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `acoth(1.313035)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>acsc(x1)</code></summary>

Arcus-Kosekans, inverse Funktion zu `csc`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `acsc(2)`  
**Ergebnis:** %pi/6

</details>

<details markdown="1">
<summary><code>acsch(x1)</code></summary>

Area-Kosekans-Hyperbolicus, inverse Funktion zu `csch`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

**Beispiel:** `acsch(1)`  
**Ergebnis:** 0.881373...

</details>

<details markdown="1">
<summary><code>allbut(...)</code></summary>

Liefert eine Liste aller Variablen des Parsers als Menge(Vektor) mit Ausnahme der als Parameter angegebenen Variablen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable1` | Parameter der Funktion. | Variable | ja, beliebig oft |

**Beispiel:** `allbut(x,y)`  
**Ergebnis:** [a,b,c]

</details>

<details markdown="1">
<summary><code>aopt(x)</code></summary>

Bei Maxima und Lösung geht die Funktion verloren, nur innerhalb von noopt bleibt sie erhalten. Bei der Anzeige führt sie zur Optimierung das Ausdruckes nach Einsetzen der Datensätze.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl/Ausdruck | nein |

**Beispiel:** `aopt(x)`  
**Ergebnis:** x

</details>

<details markdown="1">
<summary><code>arccos(x1)</code></summary>

Arcus-Cosinus

Alias/Kompatibilitätsname zu `acos`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `acos(1)`  
**Ergebnis:** 0

</details>

<details markdown="1">
<summary><code>arccot(x1)</code></summary>

Arcus-Cotangens.

Alias/Kompatibilitätsname zu `acot`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `arccot(1)`  
**Ergebnis:** %pi/4

</details>

<details markdown="1">
<summary><code>arcsin(x1)</code></summary>

Arcus-Sinus

Alias/Kompatibilitätsname zu `asin`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `asin(1)`  
**Ergebnis:** %pi/2

</details>

<details markdown="1">
<summary><code>arctan(x1)</code></summary>

Arcus-Tangens

Alias/Kompatibilitätsname zu `atan`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `arctan(1)`  
**Ergebnis:** %pi/4

</details>

<details markdown="1">
<summary><code>arctan2(y, x)</code></summary>

Arcus-Tangens atan2(y,x)=arctan(y/x)

Alias/Kompatibilitätsname zu `atan2`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `y` | Y-Wert bzw. Ausdruck. | Zahl | nein |
| `x` | X-Wert bzw. Ausdruck. | Zahl | nein |

**Beispiel:** `arctan2(-2,-2)`  
**Ergebnis:** -%pi*3/4

</details>

<details markdown="1">
<summary><code>argnorm(arg)</code></summary>

Wandelt einen Winkel auf den Bereich von 0°-360°

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `arg` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `argnorm(-50°)`  
**Ergebnis:** 310°

</details>

<details markdown="1">
<summary><code>asec(x1)</code></summary>

Arcus-Secans, inverse Funktion zu `sec`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `asec(2)`  
**Ergebnis:** %pi/3

</details>

<details markdown="1">
<summary><code>asech(x1)</code></summary>

Area-Secans-Hyperbolicus, inverse Funktion zu `sech`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

**Beispiel:** `asech(1)`  
**Ergebnis:** 0

</details>

<details markdown="1">
<summary><code>asin(x1)</code></summary>

Arcus-Sinus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `asin(1)`  
**Ergebnis:** %pi/2

</details>

<details markdown="1">
<summary><code>asinh(x1)</code></summary>

Area-Sinus-Hyperbolicus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `asinh(1.1752012)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>atan(x1)</code></summary>

Arcus-Tangens

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `atan(1)`  
**Ergebnis:** %pi/4

</details>

<details markdown="1">
<summary><code>atan2(y, x)</code></summary>

Arcus-Tangens atan2(y,x)=arctan(y/x)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `y` | Y-Wert bzw. Ausdruck. | Zahl | nein |
| `x` | X-Wert bzw. Ausdruck. | Zahl | nein |

**Beispiel:** `atan2(-2,-2)`  
**Ergebnis:** -%pi*3/4

</details>

<details markdown="1">
<summary><code>atanh(x1)</code></summary>

Area-Tangens-Hyperbolicus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `atanh(0.7615941)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>band(wert1, ...)</code></summary>

bitweises UND

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja, beliebig oft |

**Beispiel:** `band(4,12)`  
**Ergebnis:** 4

</details>

<details markdown="1">
<summary><code>bcd(x)</code></summary>

Wandelt in eine Long-Zahl in ein Feld aus BCD-kodierten Zahlen um

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl / Zahl | nein |

**Beispiel:** `bcd(124)`  
**Ergebnis:** [1,2,4]

</details>

<details markdown="1">
<summary><code>between(minimum, wert, maximum) / between(minimum, wert, maximum, toleranz, absolut)</code></summary>

prüft ob Parameter1 kleiner als Parameter2 und Parameter2 kleiner als Parameter 3 . Parameter 4 und 5 können optinal für die Toleranz verwendet werden.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `minimum` | Untere Grenze bzw. Startwert. | Zahl / Ausdruck | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `maximum` | Obere Grenze bzw. Endwert. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |
| `absolut` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | ja |

**Beispiel:** `between(3,4,5)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>bimp(wert1, wert2)</code></summary>

bitweises Parameter1 impliziert Parameter2

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `bimp(13,10)`  
**Ergebnis:** 8

</details>

<details markdown="1">
<summary><code>bin(A)</code></summary>

Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Binär-String mit Präfix `0b` aus.

Alias/Kompatibilitätsname zu `decbin`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `A` | Parameter der Funktion. | String / Ganzzahl | nein |

**Beispiel:** `bin(10)`  
**Ergebnis:** "0b1010"

</details>

<details markdown="1">
<summary><code>binomial(x, y)</code></summary>

Liefert den Binomialkoeffizienten von zwei positiven ganzen Zahlen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl | nein |
| `y` | Y-Wert bzw. Ausdruck. | Ganzzahl | nein |

**Beispiel:** `binomial(5,2)`  
**Ergebnis:** 10

</details>

<details markdown="1">
<summary><code>binv(x)</code></summary>

bitweises NICHT mit 8 bit

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl/Ausdruck | nein |

**Beispiel:** `binv(0x0F)`  
**Ergebnis:** 0xF0

</details>

<details markdown="1">
<summary><code>bitstream(x, bit) / bitstream(x, bit, groupSize)</code></summary>

Erzeugt aus einer Ganzzahl einen Bitstrom als String mit einer definierten Anzahl von Bit (MSB werden nötigenfalls mit 0 gefüllt) : bitstream(Daten,Bitanzahl,Gruppengröße)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl | nein |
| `bit` | Parameter der Funktion. | Ganzzahl | nein |
| `groupSize` | Parameter der Funktion. | Ganzzahl | ja |

**Beispiel:** `bitstream(0x184,12,4)`  
**Ergebnis:** "0001 1000 0100"

</details>

<details markdown="1">
<summary><code>blockparity(paritaet, codewortlaenge, codewortanzahl, datenwort, ...)</code></summary>

Kreuz oder Blockparität : blockparity(Parität,Codewortlänge,Codewortanzahl,Datenwort)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `paritaet` | Parameter der Funktion. | Variable / String | nein |
| `codewortlaenge` | Parameter der Funktion. | Ganzzahl | nein |
| `codewortanzahl` | Parameter der Funktion. | Ganzzahl | nein |
| `datenwort` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `blockparity(even,7,3,"abc")`

</details>

<details markdown="1">
<summary><code>bor(wert1, ...)</code></summary>

bitweises ODER

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja, beliebig oft |

**Beispiel:** `bor(4,1)`  
**Ergebnis:** 5

</details>

<details markdown="1">
<summary><code>bxor(wert1, ...)</code></summary>

bitweises EXKLUSIV ODER

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja, beliebig oft |

**Beispiel:** `band(4,5)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>byte(x)</code></summary>

Zahl in eine Ganzzahl wandeln und die letzten 8bit der Zahl Abschneiden, Einheit geht verloren

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl / Zahl | nein |

**Beispiel:** `byte(34.2)`  
**Ergebnis:** 34

</details>

<details markdown="1">
<summary><code>cabs(x)</code></summary>

Liefert den Absolutbetrag einer komplexen Zahl

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl | nein |

**Beispiel:** `cabs(3+4*%i)`  
**Ergebnis:** 5

</details>

<details markdown="1">
<summary><code>cAbs(x)</code></summary>

Liefert den Absolutbetrag einer komplexen Zahl

Alias/Kompatibilitätsname zu `cabs`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl | nein |

**Beispiel:** `cAbs(3+4*%i)`  
**Ergebnis:** 5

</details>

<details markdown="1">
<summary><code>carg(x)</code></summary>

Liefert das Argument einer komplexen Zahl

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |

**Beispiel:** `carg(4*%e^(3*%i))`  
**Ergebnis:** 3

</details>

<details markdown="1">
<summary><code>cArg(x)</code></summary>

Liefert das Argument einer komplexen Zahl

Alias/Kompatibilitätsname zu `carg`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |

**Beispiel:** `cArg(4*%e^(3*%i))`  
**Ergebnis:** 3

</details>

<details markdown="1">
<summary><code>cConjugate(x)</code></summary>

Liefert die konjugiert komplexe Zahl einer komplexen Zahl

Alias/Kompatibilitätsname zu `conjugate`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |

**Beispiel:** `cConjugate(3+4*%i)`  
**Ergebnis:** 3-4*%i

</details>

<details markdown="1">
<summary><code>ccround(wert) / ccround(wert, kommastellen)</code></summary>

Rundet die Zahl kaufmännisch, der zweite Parameter gibt die Anzahl der Kommastellen an, bei komplexe Zahlen wird Real und Imaginärteil gerundet.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `kommastellen` | Parameter der Funktion. | Ganzzahl | ja |

**Beispiel:** `ccround(2.4534+5.645*%i,2)`  
**Ergebnis:** 2.45+5.65i

</details>

<details markdown="1">
<summary><code>ceiling(x)</code></summary>

ceiling(x) Rundet auf die kleinste ganze Zahl, welche größer oder gleich x ist

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `ceiling(13.2)`  
**Ergebnis:** 14

</details>

<details markdown="1">
<summary><code>chr(...)</code></summary>

Bestimmt die Zeichen mit dem ASC-II-Code der Long-Parameter und setzt daraus einen String zusammen.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `code1` | Parameter der Funktion. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `chr(0x65,105)`  
**Ergebnis:** "ei"

</details>

<details markdown="1">
<summary><code>cIm(re)</code></summary>

Liefert den Imaginärteil einer komplexen Zahl

Alias/Kompatibilitätsname zu `imagpart`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `cIm(3+4*%i)`  
**Ergebnis:** 4

</details>

<details markdown="1">
<summary><code>cnewton(funktion, startwert)</code></summary>

Bestimmt eine komplexe Nullstelle einer Funktion nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der komplexe Startwert.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `startwert` | Untere Grenze bzw. Startwert. | Zahl / Ausdruck | nein |

**Beispiel:** `cnewton (x^2+4,4)`  
**Ergebnis:** 2*%i

</details>

<details markdown="1">
<summary><code>cnewtonall(funktion, maximalerBetrag)</code></summary>

Bestimmt alle komplexen Nullstellen einer Funktion mit einem Betrag des Funktionsparameters kleiner als ein definierter Wert nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der maximale Betrag des Funktionsparameters. Das Ergebnis ist immer ein Vektor mit den Nullstellen.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `maximalerBetrag` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `cnewtonall (x^2+4,4)`  
**Ergebnis:** [-2*%i,2*%i]

</details>

<details markdown="1">
<summary><code>code(codewortlaenge, datenwort1, ...)</code></summary>

Code aus mehreren Codeworten zusammensetzen : code(Codewortlänge,Datenwort)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `codewortlaenge` | Parameter der Funktion. | Ganzzahl | nein |
| `datenwort1` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `code(5,4,3,5)`  
**Ergebnis:** 0b1000001100101

</details>

<details markdown="1">
<summary><code>color(wert) / color(wert, farbringe, modus)</code></summary>

Widerstandsfarbcode berechnen. 1. Parameter muss ein Double sein 2. Parameter sind die Anzahl der Farbringe 3. Parameter ist der Darstellungsmodus (0 = Deutsch ausgeschrieben, 1 = Abkürzung Deutsch mit drei Buchstaben, 2 = Abkürzung Deutsch mit zwei Buchstaben, 3 = Englisch ausgeschrieben, 4 = Abkürzung Englisch mit drei Buchstaben, 5 = Abkürzung Englisch mit zwei Buchstaben)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `farbringe` | Parameter der Funktion. | Ganzzahl | ja |
| `modus` | Modus, der die Art der Verarbeitung oder Darstellung festlegt. | String / Ganzzahl | ja |

**Beispiel:** `color(120,3,0)`  
**Ergebnis:** braun,rot,braun

</details>

<details markdown="1">
<summary><code>conjugate(x)</code></summary>

Liefert die konjugiert komplexe Zahl einer komplexen Zahl

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |

**Beispiel:** `conjugate(3+4*%i)`  
**Ergebnis:** 3-4*%i

</details>

<details markdown="1">
<summary><code>cos(x1)</code></summary>

Cosinus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `cos(%pi/2)`  
**Ergebnis:** 0

</details>

<details markdown="1">
<summary><code>cosh(x1)</code></summary>

Cosinus-Hyperbolicus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `cosh(1)`  
**Ergebnis:** 1.5430806

</details>

<details markdown="1">
<summary><code>cot(x1)</code></summary>

Cotangens, `cot(x)=1/tan(x)`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `cot(%pi/4)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>coth(x1)</code></summary>

Cotangens-Hyperbolicus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `coth(1)`  
**Ergebnis:** 1.313035

</details>

<details markdown="1">
<summary><code>cRe(re)</code></summary>

Liefert den Realteil einer komplexen Zahl

Alias/Kompatibilitätsname zu `realpart`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `cRe(3+4*%i)`  
**Ergebnis:** 3

</details>

<details markdown="1">
<summary><code>cRectform(x)</code></summary>

hat in LeTTo keine Relevanz, da die Zahlendarstellung bei der Ausgabe definiert wird wie zB.: {=3arg2;karti}

Alias/Kompatibilitätsname zu `rectform`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl | nein |

</details>

<details markdown="1">
<summary><code>cround(wert) / cround(wert, kommastellen)</code></summary>

Rundet die Zahl kaufmännisch, der zweite Parameter gibt die Anzahl der Kommastellen an, ohne 2.Parameter wird auf Ganzzahlen gerundet, bei komplexen Zahlen wird Betrag und Winkel in Grad gerundet.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `kommastellen` | Parameter der Funktion. | Ganzzahl | ja |

**Beispiel:** `cround(23.535,2) cround(2.435arg34.5364°,1)`  
**Ergebnis:** 23.54 2.4arg34.5°

</details>

<details markdown="1">
<summary><code>csc(x1)</code></summary>

Kosecans, `csc(x)=1/sin(x)`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `csc(%pi/2)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>csch(x1)</code></summary>

Kosecans-Hyperbolicus, `csch(x)=1/sinh(x)`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `csch(1)`  
**Ergebnis:** 0.850918...

</details>

<details markdown="1">
<summary><code>csin(zeiger) / csin(zeiger, frequenz, zeitvariable)</code></summary>

Erzeugt aus einer komplexen Zahl (Effektivwert) und einer Frequenz einen Sinusfunktion in der Zeit

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `zeiger` | Parameter der Funktion. | Zahl/Ausdruck | nein |
| `frequenz` | Parameter der Funktion. | Zahl / Ausdruck | ja |
| `zeitvariable` | Parameter der Funktion. | Variable | ja |

**Beispiel:** `csin(U)`  
**Ergebnis:** sqrt(2)*cabs(U)*sin(2*pi*f*t+carg(U))

</details>

<details markdown="1">
<summary><code>cssin(zeiger) / cssin(zeiger, frequenz, zeitvariable)</code></summary>

Erzeugt aus einer komplexen Zahl, die als Spitzenwert interpretiert wird, eine Sinusfunktion. `cssin(U)`, `cssin(U,f)` oder `cssin(U,f,x)`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `zeiger` | Parameter der Funktion. | Zahl/Ausdruck | nein |
| `frequenz` | Parameter der Funktion. | Zahl / Ausdruck | ja |
| `zeitvariable` | Parameter der Funktion. | Variable | ja |

**Beispiel:** `cssin(U)`  
**Ergebnis:** cabs(U)*sin(2*pi*f*t+carg(U))

</details>

<details markdown="1">
<summary><code>curveHTML(mat, variable, variable)</code></summary>

Liefert eine HTML-Ansicht einer Tabelle.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `mat` | Parameter der Funktion. | Matrix / Vektor | nein |
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

**Beispiel:** `curvHTML(KL,KL_names,curveunits(KL))`  
**Ergebnis:** HTML-Code der Tabelle

</details>

<details markdown="1">
<summary><code>curveinterpol(tabelle, xSpalte, ySpalte, wert)</code></summary>

Interpoliert in einer gespeicherten Tabelle zwischen den Stützpunkten. Als Ergebnis wird ein Vektor aller gefundenen Punkte auf der Kennlinie geliefert

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `tabelle` | Parameter der Funktion. | Matrix | nein |
| `xSpalte` | Parameter der Funktion. | Vektor / Zahl | nein |
| `ySpalte` | Parameter der Funktion. | Vektor / Zahl | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `curveinterpol(KL,0,1,3.5)`  
**Ergebnis:** [2.1]

</details>

<details markdown="1">
<summary><code>curveinterpolfirst(tabelle, xSpalte, ySpalte, wert)</code></summary>

Interpoliert in einer gespeicherten Tabelle und liefert den ersten interpolierten Punkt auf der Kennlinie.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `tabelle` | Parameter der Funktion. | Matrix | nein |
| `xSpalte` | Parameter der Funktion. | Vektor / Zahl | nein |
| `ySpalte` | Parameter der Funktion. | Vektor / Zahl | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `curveinterpolfirst(KL,0,1,1.5)`  
**Ergebnis:** 2.1

</details>

<details markdown="1">
<summary><code>curvepv(tabelle, xSpalte, ySpalte)</code></summary>

Liest aus einer gespeicherten Tabelle die Spalte "spalteX" für die x-Werte und die Spalte "spalteY" für die Y-Werte eines pv-Vektors

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `tabelle` | Parameter der Funktion. | Matrix | nein |
| `xSpalte` | Parameter der Funktion. | Matrix / Zahl | nein |
| `ySpalte` | Parameter der Funktion. | Matrix / Zahl | nein |

**Beispiel:** `curvepv([[0,0,2],[1,2,3],[2,2.2,1.5],[3,1.4,1.8]],0,1)`  
**Ergebnis:** [[0,0],[1,2],[2,2.2],[3,1.4]]

</details>

<details markdown="1">
<summary><code>curveunits(mat)</code></summary>

Liefert einen Vektor aller Einheiten der Spalten einer Matrix

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `mat` | Parameter der Funktion. | Matrix / Vektor | nein |

**Beispiel:** `curveunits(curvepv([[3A,7V,2],[2A,2V,3],[2A,2.2V],[3A,1.4V]])`  
**Ergebnis:** [1A,1V]

</details>

<details markdown="1">
<summary><code>dataset(name)</code></summary>

liefert alle Datensätze einer Datensatz-Definition in einem Vektor

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `name` | Parameter der Funktion. | Variable | nein |

**Beispiel:** `dataset(x)`

</details>

<details markdown="1">
<summary><code>date(year, month, day, hour, minute, second, ...)</code></summary>

date(y,m,d,h,min,sec) erzeugt ein Datum als Ganzzahl in Sekunden seit 1.1.0000 00:00:00

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `year` | Parameter der Funktion. | String / Vektor | nein |
| `month` | Parameter der Funktion. | Ganzzahl | nein |
| `day` | Parameter der Funktion. | Ganzzahl | nein |
| `hour` | Parameter der Funktion. | Ganzzahl | nein |
| `minute` | Parameter der Funktion. | Ganzzahl | nein |
| `second` | Parameter der Funktion. | Ganzzahl | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

</details>

<details markdown="1">
<summary><code>dateday(date)</code></summary>

Erzeugt aus einem Datum als Ganzzahl den Tag

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date` | Parameter der Funktion. | String / Ganzzahl | nein |

</details>

<details markdown="1">
<summary><code>datedayofyear(date)</code></summary>

Liefert den Tag des Jahres

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date` | Parameter der Funktion. | String / Ganzzahl | nein |

</details>

<details markdown="1">
<summary><code>datediff(date1, date2)</code></summary>

Rechnet die Differenz von 2 ganzzahligen Datumswerten. Erstes minus zweites Datum. Ergebnis als Double in Sekunden

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date1` | Parameter der Funktion. | String / Ganzzahl | nein |
| `date2` | Parameter der Funktion. | String / Ganzzahl | nein |

</details>

<details markdown="1">
<summary><code>datehour(date)</code></summary>

Erzeugt aus einem Datum als Ganzzahl die Stunde

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date` | Parameter der Funktion. | String / Ganzzahl | nein |

</details>

<details markdown="1">
<summary><code>dateminute(date)</code></summary>

Erzeugt aus einem Datum als Ganzzahl die Minute

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date` | Parameter der Funktion. | String / Ganzzahl | nein |

</details>

<details markdown="1">
<summary><code>datemix(di)</code></summary>

Erzeugt aus einem Datumswert (Sekunden seit 1.1.00 0:00:00) einen Vektor mit Jahr,Monat,Tag,Stunde,Minute,Sekunde

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `di` | Parameter der Funktion. | String / Ganzzahl | nein |

</details>

<details markdown="1">
<summary><code>datemonth(date)</code></summary>

Erzeugt aus einem Datum als Ganzzahl das Monat

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date` | Parameter der Funktion. | String / Ganzzahl | nein |

</details>

<details markdown="1">
<summary><code>dateparse(string)</code></summary>

Wandelt einen String in ein Datum als Ganzzahl in Sekunden seit 1.1.0000

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |

</details>

<details markdown="1">
<summary><code>datesecond(date)</code></summary>

Erzeugt aus einem Datum als Ganzzahl die Sekunde

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date` | Parameter der Funktion. | String / Ganzzahl | nein |

</details>

<details markdown="1">
<summary><code>datestring(datum, format)</code></summary>

datestring(x) datestring(x,"format") erzeugt aus einem Datum in Sekunden seit 1.1.0000 eine Stringausgabe

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `datum` | Parameter der Funktion. | String / Ganzzahl | nein |
| `format` | Formatangabe für die Ausgabe. | String | nein |

</details>

<details markdown="1">
<summary><code>datetimestring(datum, format)</code></summary>

erzeugt Datum und Uhrzeit als String

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `datum` | Parameter der Funktion. | String / Ganzzahl | nein |
| `format` | Formatangabe für die Ausgabe. | String | nein |

</details>

<details markdown="1">
<summary><code>dateweek(date)</code></summary>

Liefert die Kalenderwoche des Tages innerhalb des Jahres

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date` | Parameter der Funktion. | String / Ganzzahl | nein |

</details>

<details markdown="1">
<summary><code>dateweekday(date)</code></summary>

Liefert den Wochentag beginnend mit Montag als 1 und Sonntag als 7

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date` | Parameter der Funktion. | String / Ganzzahl | nein |

</details>

<details markdown="1">
<summary><code>dateyear(date)</code></summary>

Erzeugt aus einem Datum als Ganzzahl das Jahr

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date` | Parameter der Funktion. | String / Ganzzahl | nein |

</details>

<details markdown="1">
<summary><code>days(sec)</code></summary>

Erzeugt aus einem Sekundenwert die Tage als Double ohne Einheit

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `sec` | Parameter der Funktion. | Zahl | nein |

</details>

<details markdown="1">
<summary><code>dB(oe)</code></summary>

Wandelt einen Zahlenwert in eine nicht skalierende Dezibel-Einheit um. Einheitenlos wird in dB20 gewandelt, mit den Einheiten V,mV,uV,W,mW,uW wird in die zugehörige dB-Einheit gewandelt.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `dB(100) dB(100)+1`  
**Ergebnis:** 40 dB20 41

</details>

<details markdown="1">
<summary><code>dB10(oe)</code></summary>

wandelt eine Zahl in einen Dezibel Wert dB10 mit 10dB pro Dekade

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `dB10(100)`  
**Ergebnis:** 20dB10

</details>

<details markdown="1">
<summary><code>dBm(oe)</code></summary>

Wandelt eine Leistung in dBm um. Bezugsleistung ist 1 mW: `10*log10(P/1mW)`. Bei komplexen Leistungen wird der Betrag verwendet; vorhandene dBW/dBm/dBu-Werte werden entsprechend umgerechnet.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `dBm(1mW)`  
**Ergebnis:** 0dBm

</details>

<details markdown="1">
<summary><code>dBmV(oe)</code></summary>

Wandelt eine Spannung in dBmV um. Bezugsspannung ist 1 mV: `20*log10(U/1mV)`. Bei komplexen Spannungen wird der Betrag verwendet.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `dBmV(1mV)`  
**Ergebnis:** 0dBmV

</details>

<details markdown="1">
<summary><code>dBu(oe)</code></summary>

Wandelt eine Leistung in den in LeTTo verwendeten dBu-Pegel mit Bezugsleistung 1 µW um: `10*log10(P/1uW)`. Hinweis: Dies ist die LeTTo-Definition von dBu und nicht die übliche Spannungsdefinition bezogen auf 0,775 V.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `dBu(1uW)`  
**Ergebnis:** 0dBu

</details>

<details markdown="1">
<summary><code>dBuV(oe)</code></summary>

Wandelt eine Spannung in dBuV um. Bezugsspannung ist 1 µV: `20*log10(U/1uV)`. Bei komplexen Spannungen wird der Betrag verwendet.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `dBuV(1uV)`  
**Ergebnis:** 0dBuV

</details>

<details markdown="1">
<summary><code>dBV(oe)</code></summary>

Wandelt eine Spannung in dBV um. Bezugsspannung ist 1 V: `20*log10(U/1V)`. Bei komplexen Spannungen wird der Betrag verwendet; vorhandene dBV/dBmV/dBuV-Werte werden entsprechend umgerechnet.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `dBV(1V)`  
**Ergebnis:** 0dBV

</details>

<details markdown="1">
<summary><code>dBW(oe)</code></summary>

wandelt eine Leistung in einen Dezibel Wert dBW mit 10dB pro Dekade

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `dBW(100)`  
**Ergebnis:** 20dBW

</details>

<details markdown="1">
<summary><code>decbin(A)</code></summary>

Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Binär-String mit Präfix `0b` aus.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `A` | Parameter der Funktion. | String / Ganzzahl | nein |

**Beispiel:** `decbin(10)`  
**Ergebnis:** "0b1010"

</details>

<details markdown="1">
<summary><code>dechex(A)</code></summary>

Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Hexadezimal-String mit Präfix `0x` aus.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `A` | Parameter der Funktion. | String / Ganzzahl | nein |

**Beispiel:** `dechex(12)`  
**Ergebnis:** "0xC"

</details>

<details markdown="1">
<summary><code>declare(variable)</code></summary>

Deklariert Variablentypen für die Maxima-Kompatibilität. Die Funktion ist im internen Parser derzeit noch nicht funktional umgesetzt und liefert dort `false`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

**Beispiel:** `declare(x,real)`  
**Ergebnis:** false

</details>

<details markdown="1">
<summary><code>defrac(wertOderZaehler) / defrac(wertOderZaehler, nenner)</code></summary>

zerlegt eine rationale Zahl in Zähler und Nenner als Menge Die erhaltene Menge kann mit dem Format-Modfier frac als gemischter Bruch dargestellt werden

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wertOderZaehler` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `nenner` | Parameter der Funktion. | Vektor / Ganzzahl | ja (bei 2 Parametern) |

**Beispiel:** `defrac(14/12)`  
**Ergebnis:** [13,12]

</details>

<details markdown="1">
<summary><code>defracmix(wertOderGanzzahl) / defracmix(wertOderGanzzahl, nennerOderZaehler) / defracmix(wertOderGanzzahl, nennerOderZaehler, nenner)</code></summary>

zerlegt eine rationale Zahl in einen gemischten Bruch aus ganzzahligem Summanden, Zähler und Nenner als Menge Die erhaltene Menge kann mit dem Format-Modfier frac als gemischter Bruch dargestellt werden (siehe Zahlendarstellung)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wertOderGanzzahl` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `nennerOderZaehler` | Parameter der Funktion. | Vektor / Ganzzahl | ja (bei 2/3 Parametern) |
| `nenner` | Parameter der Funktion. | Ganzzahl | ja (bei 3 Parametern) |

**Beispiel:** `defracmix(14/12) defracmix(-15/12) defracmix(3/12)`  
**Ergebnis:** [1,2/12] [-1,3,12] [0,3,12]

</details>

<details markdown="1">
<summary><code>deg(string)</code></summary>

erzeugt aus einem Vektor mit Grad, Minuten und Sekunden als Zahlenwerte oder einen WinkelString einen Winkel im Bogenmaß

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |

**Beispiel:** `deg([2,15,22]) deg("2°15&#39;22&#39;&#39;")`  
**Ergebnis:** 2.25611111111°

</details>

<details markdown="1">
<summary><code>degmix(string)</code></summary>

zerlegt einen Winkel im Bogenmaß in einen Winkel in Grad, Minuten und Sekunden in einem Vektor

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |

**Beispiel:** `degmix(0.5)`  
**Ergebnis:** [28,38,52.4031239082]

</details>

<details markdown="1">
<summary><code>degstring(winkel)</code></summary>

erzeugt aus einem Vektor mit Grad, Minuten und Sekunden als Zahlenwerte oder einen Winkel im Bogenmaß einen String der Winkeldarstellung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `winkel` | Parameter der Funktion. | Zahl / Ausdruck | nein |

**Beispiel:** `degstring(0.5)`  
**Ergebnis:** "2°15&#39;22&#39;&#39;"

</details>

<details markdown="1">
<summary><code>delay(t)</code></summary>

Test-/Diagnosefunktion: verzögert die Auswertung um die angegebene Anzahl Sekunden und prüft dabei regelmäßig auf einen Timeout/Abbruch.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `t` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `delay(1)`  
**Ergebnis:** nach ca. 1 s

</details>

<details markdown="1">
<summary><code>diff(funktion, variable) / diff(funktion, variable, anzahl)</code></summary>

Berechnet die Ableitung einer Funktion.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck, der abgeleitet wird. | Ausdruck | nein |
| `variable` | Variable, nach der abgeleitet wird. | Variable | nein |
| `anzahl` | Ordnung der Ableitung. | Ganzzahl | ja (bei 3 Parametern) |

**Beispiel:** `diff(x^2,x) diff(3*x^2,x,2)`  
**Ergebnis:** x 6

</details>

<details markdown="1">
<summary><code>div(dividend, divisor)</code></summary>

Ganzzahldivision, Ergebnis wird abgeschnitten

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `dividend` | Parameter der Funktion. | Ganzzahl / Zahl | nein |
| `divisor` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

**Beispiel:** `div(5,2)`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>double(A)</code></summary>

Zahl in eine Gleitkommazahl umwandeln, die Einheit geht dabei verloren

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `A` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `double(3.4V)`  
**Ergebnis:** 3.4

</details>

<details markdown="1">
<summary><code>e12(A)</code></summary>

rundet einen Zahlenwert auf den nächstliegenden Wert der Normreihe E12. Die Rundung erfolgt geometrisch d.h. der Quotient zwischen Normwert und zu rundendem Wert wird minimiert.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `A` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `e12(700Ohm)`  
**Ergebnis:** 680Ohm

</details>

<details markdown="1">
<summary><code>e12down(A)</code></summary>

rundet einen Zahlenwert auf den nächstkleineren Wert der Normreihe E12

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `A` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `e12(700Ohm)`  
**Ergebnis:** 680Ohm

</details>

<details markdown="1">
<summary><code>e12up(A)</code></summary>

rundet einen Zahlenwert auf den nächstgrößerern Wert der Normreihe E12

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `A` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `e12(670Ohm)`  
**Ergebnis:** 680Ohm

</details>

<details markdown="1">
<summary><code>eh(wert)</code></summary>

Liefert zu einem numerischen Wert die zugehörige Einheit als Wert 1 zurück; bei einem einheitenlosen Wert wird `1` geliefert.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `eh(2.3mA)`  
**Ergebnis:** 1mA

</details>

<details markdown="1">
<summary><code>eq(wert1, wert2) / eq(wert1, wert2, toleranz, absolut)</code></summary>

gleich eq(wert1,wert2),eq(wert1,wert2,toleranz),eq(wert1,wert2,toleranz,absolut)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |
| `absolut` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | ja |

**Beispiel:** `eq(4,4)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>eqruntime(x1, x2)</code></summary>

symbolischer Vergleich, welcher symbolisch erst bei der Ergebnisberechnung ausgeführt wird. Muss verwendet werden, wenn bei Vergleichen symbolische Antworten von Schülern (Q0,Q1,...) verwendet werden.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |
| `x2` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |

**Beispiel:** `eqruntime(x+3*y,3*y+x)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>ev(ausdruck, ...)</code></summary>

Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `zuweisungen` | Parameter der Funktion. | Ausdruck | ja, beliebig oft |

**Beispiel:** `ev(x*y,y=4)`  
**Ergebnis:** x*4

</details>

<details markdown="1">
<summary><code>evruntime(ausdruck, ...)</code></summary>

Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden. Das Einsetzen erfolgt erst bei der Ergebnisberechnung!

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `zuweisungen` | Parameter der Funktion. | Ausdruck | ja, beliebig oft |

**Beispiel:** `evruntime(x*y,y=4)`  
**Ergebnis:** x*4

</details>

<details markdown="1">
<summary><code>exp(x1)</code></summary>

Exponentialfunktion

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `exp(1)`  
**Ergebnis:** %e

</details>

<details markdown="1">
<summary><code>factfrompolynom(polynom)</code></summary>

Erzeugt aus einem Polynom einen Vektor mit den Polynomfaktoren. Erste Zeile Zählerfaktoren, zweite Zeile Nennerfaktoren, dritte Zeile Polynomvariable, vierte Zeile Einheit der Polynomvariable

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `polynom` | Parameter der Funktion. | Zahl/Ausdruck | nein |

**Beispiel:** `factfrompolynom(polynom((2+x)/(1+2*x)))`  
**Ergebnis:** [[1,0.5],[0.5,1],"x",""]

</details>

<details markdown="1">
<summary><code>factorial(wert)</code></summary>

Liefert die Fakultät einer positiven ganzen Zahl

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `factorial(5)`  
**Ergebnis:** 120

</details>

<details markdown="1">
<summary><code>fifth() / fifth(variable)</code></summary>

liefert das fünfte Element mit dem Index 4 eines Vektors

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | ja |

**Beispiel:** `fifth ([12,13,14,15,16,17,18])`  
**Ergebnis:** 16

</details>

<details markdown="1">
<summary><code>first() / first(variable)</code></summary>

liefert das erste Element mit dem Index 0 eines Vektors

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | ja |

**Beispiel:** `first([12,13,14])`  
**Ergebnis:** 12

</details>

<details markdown="1">
<summary><code>floor(x)</code></summary>

Rundet auf die größte ganze Zahl, welche kleiner oder gleich x ist

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `floor(24.5)`  
**Ergebnis:** 24

</details>

<details markdown="1">
<summary><code>foreach(menge, variable, ausdruck)</code></summary>

Führt für jedes Element eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `menge` | Menge bzw. Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `foreach([2,-3,5,-6],p,cabs(p),"+")`  
**Ergebnis:** 16

</details>

<details markdown="1">
<summary><code>forloop(variable, startwert, bedingung, inkrement, ausdruck)</code></summary>

Führt eine Zählschleife aus forloop(Variable,Startwert,Wiederholbedingung,Inkrement,Ausdruck,Aggregatsfunktion). Ohne Aggregatsfunktion wird ein Feld mit den Ergebnissen der Schleifeniterationen geliefert.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Schleifenvariable. | Variable | nein |
| `startwert` | Startwert der Schleifenvariable. | Zahl / Ausdruck | nein |
| `bedingung` | Bedingung für die Fortsetzung der Schleife. | Ausdruck | nein |
| `inkrement` | Ausdruck, der die Schleifenvariable verändert. | Ausdruck | nein |
| `ausdruck` | Pro Schleifendurchlauf auszuwertender Ausdruck. | Ausdruck | nein |

**Beispiel:** `forloop(i,1,i<7,i++,i,"+") forloop(i,1,i<7,i:i+2,i)`  
**Ergebnis:** 21 [1,3,5]

</details>

<details markdown="1">
<summary><code>fourth() / fourth(variable)</code></summary>

liefert das vierte Element mit dem Index 3 eines Vektors

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | ja |

**Beispiel:** `fourth ([12,13,14,15,16,17,18])`  
**Ergebnis:** 15

</details>

<details markdown="1">
<summary><code>frac(v1) / frac(v1, anzahl) / frac(v1, anzahl, anzahl)</code></summary>

erzeugt aus einer Menge aus 2 oder 3 Elementen (von defrac) eine rationale Zahl

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Ganzzahl | nein |
| `anzahl` | Anzahl der Elemente, Stellen oder Wiederholungen. | Ganzzahl | ja (bei 2/3 Parametern) |
| `anzahl` | Anzahl der Elemente, Stellen oder Wiederholungen. | Ganzzahl | ja (bei 3 Parametern) |

**Beispiel:** `frac([3,7]) frac([1,2,3])`  
**Ergebnis:** 3/7 5/3

</details>

<details markdown="1">
<summary><code>fromdB(oe)</code></summary>

Wandelt eine nicht skalierende Dezibel-Einheit in einen normalen Zahlenwert um

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `fromdB(40)`  
**Ergebnis:** 100

</details>

<details markdown="1">
<summary><code>fromdB10(oe)</code></summary>

wandelt einen Dezibel Wert mit 10dB pro Dekade in den Ausgangswert

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `fromdB10(20)`  
**Ergebnis:** 100

</details>

<details markdown="1">
<summary><code>fromdBm(oe)</code></summary>

Wandelt einen dBm-Wert in eine Leistung zurück. Ein einheitenloser Zahlenwert wird als dBm interpretiert und als Leistung in mW zurückgegeben.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `fromdBm(0)`  
**Ergebnis:** 1mW

</details>

<details markdown="1">
<summary><code>fromdBmV(oe)</code></summary>

Wandelt einen dBmV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBmV interpretiert und als Spannung in mV zurückgegeben.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `fromdBmV(0)`  
**Ergebnis:** 1mV

</details>

<details markdown="1">
<summary><code>fromdBu(oe)</code></summary>

Wandelt einen LeTTo-dBu-Wert in eine Leistung zurück. Ein einheitenloser Zahlenwert wird als dBu interpretiert und als Leistung in µW zurückgegeben.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `fromdBu(0)`  
**Ergebnis:** 1uW

</details>

<details markdown="1">
<summary><code>fromdBuV(oe)</code></summary>

Wandelt einen dBuV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBuV interpretiert und als Spannung in µV zurückgegeben.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `fromdBuV(0)`  
**Ergebnis:** 1uV

</details>

<details markdown="1">
<summary><code>fromdBV(oe)</code></summary>

Wandelt einen dBV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBV interpretiert und als Spannung in V zurückgegeben.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `fromdBV(0)`  
**Ergebnis:** 1V

</details>

<details markdown="1">
<summary><code>fromdBW(oe)</code></summary>

wandelt einen Dezibel Wert mit 10dB pro Dekade in eine Leistung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `fromdBW(20)`  
**Ergebnis:** 100W

</details>

<details markdown="1">
<summary><code>ge(wert1, wert2) / ge(wert1, wert2, toleranz, absolut)</code></summary>

größer gleich ge(wert1,wert2),ge(wert1,wert2,toleranz),ge(wert1,wert2,toleranz,absolut)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |
| `absolut` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | ja |

**Beispiel:** `ge(6,4)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>getvars(variable)</code></summary>

Liefert alle im Ausdruck vorkommenden Variablennamen als Vektor von Strings.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

**Beispiel:** `getvars(x^2+a*y)`  
**Ergebnis:** ["a","x","y"]

</details>

<details markdown="1">
<summary><code>ggT(wert1, ...)</code></summary>

berechnet den größten gemeinsamen Teiler von mehreren Zahlen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `ggT(12,10)`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>ground(wert, gueltigeZiffern)</code></summary>

Rundet die Zahl auf die im zweiten Parameter angegebenen gültigen Ziffern

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `gueltigeZiffern` | Parameter der Funktion. | Ganzzahl | nein |

**Beispiel:** `ground(2453.43,2)`  
**Ergebnis:** 2500

</details>

<details markdown="1">
<summary><code>gt(wert1, wert2) / gt(wert1, wert2, toleranz, absolut)</code></summary>

größer

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |
| `absolut` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | ja |

**Beispiel:** `gt(6,4)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>hamming(codewort1, codewort2, ...)</code></summary>

Bestimmt den Hamming-Abstand von mehreren Codeworten

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `codewort1` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `codewort2` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `hamming(1,2,4,8,16)`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>hex(A)</code></summary>

Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Hexadezimal-String mit Präfix `0x` aus.

Alias/Kompatibilitätsname zu `dechex`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `A` | Parameter der Funktion. | String / Ganzzahl | nein |

**Beispiel:** `hex(12)`  
**Ergebnis:** "0xC"

</details>

<details markdown="1">
<summary><code>hours(sec)</code></summary>

Erzeugt aus einem Sekundenwert die Stunden als Double ohne Einheit

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `sec` | Parameter der Funktion. | Zahl | nein |

</details>

<details markdown="1">
<summary><code>if(e1, e2, e3)</code></summary>

if(bedingung,wahr,falsch)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `e1` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |
| `e2` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |
| `e3` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |

**Beispiel:** `Wenn-Funktion`  
**Ergebnis:** 10

</details>

<details markdown="1">
<summary><code>ilt(funktion, variable, zielvariable)</code></summary>

Bestimmt die inverse Laplace-Transformierte eine Laplace-Funktion

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck in der Laplace-Domäne. | Ausdruck | nein |
| `variable` | Variable der Laplace-Domäne. | Variable | nein |
| `zielvariable` | Zielvariable der inversen Transformation. | Variable | nein |

**Beispiel:** `ilt(1/(1+s),s,t)`  
**Ergebnis:** e^(-t)

</details>

<details markdown="1">
<summary><code>imagpart(re)</code></summary>

Liefert den Imaginärteil einer komplexen Zahl

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `imagpart(3+4*%i)`  
**Ergebnis:** 4

</details>

<details markdown="1">
<summary><code>infiniteloop()</code></summary>

Test-/Diagnosefunktion: erzeugt absichtlich eine Endlosschleife und dient zum Testen der Timeout-Behandlung. Nicht für reguläre Aufgaben verwenden.


**Beispiel:** `infiniteloop()`  
**Ergebnis:** Timeout

</details>

<details markdown="1">
<summary><code>int(x)</code></summary>

Zahl in eine Ganzzahl wandeln und die letzten 32bit der Zahl Abschneiden, Einheit geht verloren

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl / Zahl | nein |

**Beispiel:** `int(34.2)`  
**Ergebnis:** 34

</details>

<details markdown="1">
<summary><code>integrate(funktion, variable) / integrate(funktion, variable, untergrenze, obergrenze)</code></summary>

Berechnet das unbestimmte oder bestimmte Integral einer Funktion.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Zu integrierender Ausdruck. | Ausdruck | nein |
| `variable` | Integrationsvariable. | Variable | nein |
| `untergrenze` | Untere Integrationsgrenze. | Zahl / Ausdruck | ja (bei 4 Parametern) |
| `obergrenze` | Obere Integrationsgrenze. | Zahl / Ausdruck | ja (bei 4 Parametern) |

**Beispiel:** `integrate(x^2,x) integrate(x^2,x,0,2)`  
**Ergebnis:** x^3/3 8/3

</details>

<details markdown="1">
<summary><code>interpol(pv, py) / interpol(pv, py, x)</code></summary>

Interpolationsfunktion zwischen mehreren Stützpunkten in einem Koordinatensystem. interpol(WerteX,WerteY,x)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `pv` | Parameter der Funktion. | Matrix / Vektor | nein |
| `py` | Parameter der Funktion. | Matrix / Vektor | nein |
| `x` | X-Wert bzw. Ausdruck. | Vektor / Zahl | ja (bei 3 Parametern) |

**Beispiel:** `interpol([0,1,2],[0,3,3],1.5)`  
**Ergebnis:** 3

</details>

<details markdown="1">
<summary><code>inv(wertOderMatrix)</code></summary>

invertiert eine quadratische Matrix oder bildet 1/x

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wertOderMatrix` | Wert bzw. Ausdruck für die Berechnung. | Matrix | nein |

**Beispiel:** `inv(matrix([1,2],[3,4]))`  
**Ergebnis:** [[-2,1],[3/2,-1/2]]

</details>

<details markdown="1">
<summary><code>inv16(x)</code></summary>

bitweise Invertieren und die letzten 16 Bit bestimmen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl/Ausdruck | nein |

**Beispiel:** `inv16(0xF0)`  
**Ergebnis:** 0xFF0F

</details>

<details markdown="1">
<summary><code>inv32(x)</code></summary>

bitweise Invertieren und die letzten 32 Bit bestimmen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl/Ausdruck | nein |

**Beispiel:** `inv32(0xF0)`  
**Ergebnis:** 0bFFFFFF0F

</details>

<details markdown="1">
<summary><code>inv64(x)</code></summary>

bitweise Invertieren und die letzten 64 Bit bestimmen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl/Ausdruck | nein |

**Beispiel:** `inv64(0xF0)`  
**Ergebnis:** 0bFFFFFFFFFFFFFF0F

</details>

<details markdown="1">
<summary><code>inv8(x)</code></summary>

bitweises NICHT mit 8 bit

Alias/Kompatibilitätsname zu `binv`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl/Ausdruck | nein |

**Beispiel:** `inv8(0b1001)`  
**Ergebnis:** 0b11110110

</details>

<details markdown="1">
<summary><code>ip(e1) / ip(e1, e2, e3, e4)</code></summary>

Wandelt eine Long-Zahl in einen String als IP-Adresse um, oder 4 Byte-Zahlen in eine Long Zahl als IP-32-bit-Adresse

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `e1` | Parameter der Funktion. | String / Ganzzahl | nein |
| `e2` | Parameter der Funktion. | Ganzzahl / Zahl | ja (bei 4 Parametern) |
| `e3` | Parameter der Funktion. | Ganzzahl / Zahl | ja (bei 4 Parametern) |
| `e4` | Parameter der Funktion. | Ganzzahl / Zahl | ja (bei 4 Parametern) |

**Beispiel:** `ip(1534536453) ip(10,20,30,40)`  
**Ergebnis:** "91.119.43.5" 169090600

</details>

<details markdown="1">
<summary><code>ise12(wert)</code></summary>

prüft ob der als Parameter übergebenen Wert ein Wert der Normreihe E12 ist.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `ise12(680Ohm)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>islong(wert)</code></summary>

Prüft ob es sich um eine ganze Zahl handelt.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `islong(12)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>isNearInteger(wert) / isNearInteger(wert, toleranz)</code></summary>

prüft ob eine Zahl nahe genug an einer Ganzzahl liegt, um als Ganzzahl interpretiert zu werden. Es wird die Toleranz der Frage verwendet

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |

**Beispiel:** `isNearInteger(3.00000000001) isNearInteger(3.1)`  
**Ergebnis:** true false

</details>

<details markdown="1">
<summary><code>isnorm(wert, normreihe)</code></summary>

prüft ob der als Parameter übergebenen Wert ein Wert einer gegebenen Wertereihe oder Normreihe ist.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `normreihe` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |

**Beispiel:** `isnorm(680Ohm,E12)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>ispolynom(ausdruck) / ispolynom(ausdruck, variable, numerisch)</code></summary>

Prüft, ob der Ausdruck ein Polynom ist. Die Funktion wird ausgewertet, sobald der Parameter als Polynom erkannt bzw. nicht als Polynom erkannt werden kann.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | ja |
| `numerisch` | Parameter der Funktion. | Ausdruck / passender Datentyp | ja |

**Beispiel:** `ispolynom(polynom(x^2+1))`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>isprim(x1)</code></summary>

prüft ob die angegebene Zahl eine Primzahl ist

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / Boolean/Ausdruck | nein |

**Beispiel:** `isprim(13)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>isset(wert)</code></summary>

Prüft ob es sich um eine Menge handelt.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `isset([12,13,14])`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>issetlong(wert)</code></summary>

Prüft ob es sich um eine Menge aus ganzen Zahlen handelt.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `issetlong([12,13,14])`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>issetnumeric(wert)</code></summary>

Prüft ob es sich um eine Menge aus reellen Zahlen handelt.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `issetnumeric([12,13.4,14])`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>kgV(wert1, ...)</code></summary>

berechnet das kleinste gemeinsame Vielfache von mehreren Zahlen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `kgV(3,10)`  
**Ergebnis:** 30

</details>

<details markdown="1">
<summary><code>kill(variable1)</code></summary>

löscht Variable aus dem Variablenspeicher

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable1` | Parameter der Funktion. | Variable | nein |

**Beispiel:** `kill(x,y) kill(allbut(y)) kill(all)`  
**Ergebnis:** löscht die Variablen x und y löscht alle Variablen mit Ausnahme von y löscht alle Variable

</details>

<details markdown="1">
<summary><code>komplement(x) / komplement(x, bit)</code></summary>

Bildet das Zweierkomplement mit einer negativen Zahl mit einer bestimmten Bitanzahl, fehlt die Bitanzahl, so wird ein 32Bit-2er-komplement gebildet

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl | nein |
| `bit` | Parameter der Funktion. | Ganzzahl | ja |

**Beispiel:** `komplement(-5,8)`  
**Ergebnis:** 0b11111011

</details>

<details markdown="1">
<summary><code>land(...)</code></summary>

logisches UND

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja, beliebig oft |

**Beispiel:** `land(a<b,b<c)`

</details>

<details markdown="1">
<summary><code>laplace(funktion, variable, zielvariable)</code></summary>

Bestimmt die Laplace-Transformierte einer Funktion.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Zu transformierender Ausdruck. | Ausdruck | nein |
| `variable` | Ursprüngliche Variable, meist Zeitvariable. | Variable | nein |
| `zielvariable` | Variable der Laplace-Domäne. | Variable | nein |

**Beispiel:** `laplace(sin(t),t,s)`  
**Ergebnis:** 1/(1+s^2)

</details>

<details markdown="1">
<summary><code>last() / last(variable)</code></summary>

liefert das letzte Element eines Vektors

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | ja |

**Beispiel:** `first([12,13,14])`  
**Ergebnis:** 14

</details>

<details markdown="1">
<summary><code>le(wert1, wert2) / le(wert1, wert2, toleranz, absolut)</code></summary>

kleiner gleich le(wert1,wert2),le(wert1,wert2,toleranz),le(wert1,wert2,toleranz,absolut)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |
| `absolut` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | ja |

**Beispiel:** `le(6,4)`  
**Ergebnis:** false

</details>

<details markdown="1">
<summary><code>lhs(ausdruck)</code></summary>

liefert die linke Seite einer Gleichung, Ungleichung oder eines Infix Operators

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `lhs(x+y=c+2)`  
**Ergebnis:** x+y

</details>

<details markdown="1">
<summary><code>linspace(von, bis, anz)</code></summary>

linspace(start,ende,anzahl) liefert ein Feld von Werte von Startwert bis Endwert mit gleichem Abstand

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `von` | Untere Grenze bzw. Startwert. | Ganzzahl / Zahl | nein |
| `bis` | Obere Grenze bzw. Endwert. | Ganzzahl / Zahl | nein |
| `anz` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

**Beispiel:** `linspace(4,8,5)`  
**Ergebnis:** [4,5,6,7,8]

</details>

<details markdown="1">
<summary><code>ln(x1)</code></summary>

natürlicher Logarythmus

Alias/Kompatibilitätsname zu `log`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `ln(%e)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>lnoopt(ausdruck)</code></summary>

Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {= wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck nicht mehr optimiert.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `lnoopt(x+3+2)`  
**Ergebnis:** lnoopt(x+5)

</details>

<details markdown="1">
<summary><code>lnot(bedingung)</code></summary>

logisches NICHT. Vorsicht ein symbolisches Ergebnis von Maxima liefert not als Prefix-Operator, welcher vom Parser nicht unterstützt wird ( Verwende statt dessen lnot )

Alias/Kompatibilitätsname zu `not`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `bedingung` | Parameter der Funktion. | Ausdruck | nein |

**Beispiel:** `lnot(a<b)`

</details>

<details markdown="1">
<summary><code>log(x1)</code></summary>

natürlicher Logarythmus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `log(%e)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>log10(x1)</code></summary>

Logarythmus zur Basis 10

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

**Beispiel:** `log10(100)`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>logspace(von, bis, anz)</code></summary>

logspace(start,ende,anzahl) liefert ein Feld von Werte von Startwert bis Endwert mit gleichem logarithmischen Abstand

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `von` | Untere Grenze bzw. Startwert. | Ganzzahl / Zahl | nein |
| `bis` | Obere Grenze bzw. Endwert. | Ganzzahl / Zahl | nein |
| `anz` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

**Beispiel:** `logspace(10,10000,4)`  
**Ergebnis:** [10,100,1000,10000]

</details>

<details markdown="1">
<summary><code>long(A)</code></summary>

Zahl in eine Ganzzahl wandeln , Einheit geht verloren

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `A` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

**Beispiel:** `long(34.2)`  
**Ergebnis:** 34

</details>

<details markdown="1">
<summary><code>lopt(ausdruck)</code></summary>

Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {= wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck vollständig optimiert.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `lopt(x+3)`  
**Ergebnis:** lopt(x+3)

</details>

<details markdown="1">
<summary><code>loptnumeric(ausdruck)</code></summary>

Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {= wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck nur numerisch optimiert.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `loptnumeric(x+y)`  
**Ergebnis:** loptnumeric(x+y)

</details>

<details markdown="1">
<summary><code>lor(...)</code></summary>

logisches ODER

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja, beliebig oft |

**Beispiel:** `lor(a<b,b<c)`

</details>

<details markdown="1">
<summary><code>lt(wert1, wert2) / lt(wert1, wert2, toleranz, absolut)</code></summary>

kleiner

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |
| `absolut` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | ja |

**Beispiel:** `lt(6,4)`  
**Ergebnis:** false

</details>

<details markdown="1">
<summary><code>matchstring(string, regexp)</code></summary>

Prüft ob eine String einem regulären Ausdruck entspricht.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |
| `regexp` | Parameter der Funktion. | Boolean/Ausdruck | nein |

**Beispiel:** `matchstring("abcdefg","b.*e")`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>matrix(...)</code></summary>

erzeugt aus mehreren gleich langen Vektoren eine Matrix

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `zeile1` | Parameter der Funktion. | Zahl/Ausdruck | ja, beliebig oft |

**Beispiel:** `matrix([1,2],[3,4])`  
**Ergebnis:** [[1,2],[3,4]]

</details>

<details markdown="1">
<summary><code>max(werte, ...)</code></summary>

Maximum von mehreren Werten suchen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `werte` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `max(3,5,1)`  
**Ergebnis:** 5

</details>

<details markdown="1">
<summary><code>mcdelete(matrix, pos)</code></summary>

mcdelete(matrix,position) Löscht die angegebene Spalte aus einer Matrix

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `pos` | Parameter der Funktion. | Matrix / Ganzzahl | nein |

**Beispiel:** `mcdelete([[1,2,3],[4,5,6],[7,8,9]],1)`  
**Ergebnis:** [[1,3],[4,6],[7,9]]

</details>

<details markdown="1">
<summary><code>mcinsert(matrix, matrixOderVektor, position)</code></summary>

mcinsert(matrix,matrixodervektor,position) Fügt an der Spaltenposition eine Matrix oder einen Vektor als neue Spalten ein

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `matrixOderVektor` | Parameter der Funktion. | Matrix | nein |
| `position` | Parameter der Funktion. | Zahl / Ausdruck | nein |

**Beispiel:** `mcinsert([[1,2,3],[4,5,6],[7,8,9]],[[10,11],[12,13],[14,15]],1)`  
**Ergebnis:** [[1,10,11,2,3],[4,12,13,5,6],[7,14,15,8,9]]

</details>

<details markdown="1">
<summary><code>mcols(m1)</code></summary>

liefert die Anzahl der Spalten einer Matrix

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `m1` | Parameter der Funktion. | Matrix / Vektor | nein |

**Beispiel:** `mcols([[3,4,4],[3,6,54,34,3,54]])`  
**Ergebnis:** 6

</details>

<details markdown="1">
<summary><code>mcunion(matrix1, wert2)</code></summary>

Fügt mehrere Matrizen oder Vektoren spaltenweise(nebeneinander) zusammen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix1` | Parameter der Funktion. | Matrix | nein |
| `wert2` | Wert bzw. Ausdruck des 2. Parameters. | Zahl / Ausdruck | nein |

**Beispiel:** `mcunion([[1,2,3],[4,5,6],[7,8,9]],[[10,11],[12,13],[14,15]])`  
**Ergebnis:** [[1,2,3,10,11],[4,5,6,12,13],[7,8,9,14,15]]

</details>

<details markdown="1">
<summary><code>mdet(matrix)</code></summary>

Bildet die Determinante einer quadratischen Matrix

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |

**Beispiel:** `mdet([[1,2],[3,4]])`  
**Ergebnis:** -2

</details>

<details markdown="1">
<summary><code>min(werte, ...)</code></summary>

Minimum von mehrere Werten suchen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `werte` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `min(3,5,1)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>minutes(sec)</code></summary>

Erzeugt aus einem Sekundenwert die Minuten als Double ohne Einheit

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `sec` | Parameter der Funktion. | Zahl | nein |

</details>

<details markdown="1">
<summary><code>minv(matrix)</code></summary>

Bildet die inverse Matrix

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |

**Beispiel:** `minv([[1,2],[3,4]])`  
**Ergebnis:** [[-2,1],[3/2,-1/2]]

</details>

<details markdown="1">
<summary><code>mod(re1, re2)</code></summary>

Mathematische Implementierung von modulo: Divisionsrest einer Division mit ganzzahligem Ergebnis

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re1` | Parameter der Funktion. | Ganzzahl / Zahl | nein |
| `re2` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

**Beispiel:** `mod(5,2) mod(6.2,2.5) mod(-4,3)`  
**Ergebnis:** 1 1.2 2

</details>

<details markdown="1">
<summary><code>mod2(re1, re2)</code></summary>

Symmetrische Implementierung von modulo: Divisionsrest einer Division mit ganzzahligem Ergebnis Der Unterschied zu mod liegt in der Behandlung von negativen Zahlen des ersten Arguments Siehe auch Divisionsrest des Parser-Operators % Berechnungen arithmetische-operatoren-

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re1` | Parameter der Funktion. | Ganzzahl / Zahl | nein |
| `re2` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

**Beispiel:** `mod2(5,2) mod2(6.2,2.5) mod2(-4,3)`  
**Ergebnis:** 1 1.2 -1

</details>

<details markdown="1">
<summary><code>months(sec)</code></summary>

Erzeugt aus einem Sekundenwert die Monate (/30d) als Double ohne Einheit

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `sec` | Parameter der Funktion. | Zahl | nein |

</details>

<details markdown="1">
<summary><code>mprod(matrix1, matrix2)</code></summary>

Bildet das Matrixprodukt aus zwei Matrizen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix1` | Parameter der Funktion. | Matrix | nein |
| `matrix2` | Parameter der Funktion. | Matrix | nein |

**Beispiel:** `mprod([[1,2],[3,4]],[[5,6],[7,8]])`  
**Ergebnis:** [[19,22],[43,50]]

</details>

<details markdown="1">
<summary><code>mrdelete(matrix, pos)</code></summary>

mrdelete(matrix,position) Löscht die angegebene Zeile aus einer Matrix

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `pos` | Parameter der Funktion. | Matrix / Ganzzahl | nein |

**Beispiel:** `mrdelete([[1,2,3],[4,5,6],[7,8,9]],1)`  
**Ergebnis:** [[1,2,3],[7,8,9]]

</details>

<details markdown="1">
<summary><code>mrinsert(matrix, matrixOderVektor, position)</code></summary>

mrinsert(matrix,matrixodervektor,position) Fügt an der Zeilenposition eine Matrix oder einen Vektor als neue Zeilen ein

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `matrixOderVektor` | Parameter der Funktion. | Matrix | nein |
| `position` | Parameter der Funktion. | Zahl / Ausdruck | nein |

**Beispiel:** `mrinsert([[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15]],1)`  
**Ergebnis:** [[1,2,3],[10,11,12],[13,14,15],[4,5,6],[7,8,9]]

</details>

<details markdown="1">
<summary><code>mrows(m1)</code></summary>

liefert die Anzahl der Zeilen einer Matrix

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `m1` | Parameter der Funktion. | Matrix / Vektor | nein |

**Beispiel:** `mrows([[3,4,4],[3,6,54,34,3,54]])`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>mrunion(matrix1, wert2)</code></summary>

Fügt mehrere Matrizen oder Vektoren zeileweise(untereinander) zusammen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix1` | Parameter der Funktion. | Matrix | nein |
| `wert2` | Wert bzw. Ausdruck des 2. Parameters. | Zahl / Ausdruck | nein |

**Beispiel:** `mrunion([[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15]])`  
**Ergebnis:** [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]

</details>

<details markdown="1">
<summary><code>msub(matrix, oz) / msub(matrix, oz, os, zeilen, spalten)</code></summary>

msub(matrix,zeile,spalte,zeilen,spalten) Liefert eine Untermatrix beginnend bei Zeile und Spalten mit der angegebenen Anzahl von Zeilen und Spalten. Die Parameter Spalte,Zeilen und Spalten sind dabei optional.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `oz` | Parameter der Funktion. | Matrix / Ganzzahl | nein |
| `os` | Parameter der Funktion. | Matrix / Ganzzahl | ja |
| `zeilen` | Parameter der Funktion. | Vektor / Matrix | ja |
| `spalten` | Parameter der Funktion. | Ganzzahl | ja |

**Beispiel:** `msub([[1,2,3],[4,5,6],[7,8,9]],0,1,2,2)`  
**Ergebnis:** [[2,3],[5,6]]

</details>

<details markdown="1">
<summary><code>mtrans(matrix)</code></summary>

Bildet die transponierte Matrix

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |

**Beispiel:** `mtrans([[1,2],[3,4]])`  
**Ergebnis:** [[1,3],[2,4]]

</details>

<details markdown="1">
<summary><code>ne(wert1, wert2) / ne(wert1, wert2, toleranz, absolut)</code></summary>

ungleich ne(wert1,wert2),ne(wert1,wert2,toleranz),ne(wert1,wert2,toleranz,absolut)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |
| `absolut` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | ja |

**Beispiel:** `ne(6,4)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>newton(funktion, startwert)</code></summary>

Bestimmt eine Nullstelle einer Funktion nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der Startwert.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `startwert` | Untere Grenze bzw. Startwert. | Zahl / Ausdruck | nein |

**Beispiel:** `newton(x^2-4,4)`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>newtonall(funktion, maximalerBetrag)</code></summary>

Bestimmt alle Nullstellen einer Funktion mit einem Betrag des Funktionsparameters kleiner als ein definierter Wert nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der maximale Betrag des Funktionsparameters. Das Ergebnis ist immer ein Vektor mit den nach aufsteigendem Funktionswert sortierten Nullstellen.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `maximalerBetrag` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `newtonall (x^2-4,4)`  
**Ergebnis:** [-2,2]

</details>

<details markdown="1">
<summary><code>ni(wert) / ni(wert, toleranz)</code></summary>

prüft ob eine Zahl nahe genug an einer Ganzzahl liegt, um als Ganzzahl interpretiert zu werden. Es wird die Toleranz der Frage verwendet

Alias/Kompatibilitätsname zu `isNearInteger`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |

**Beispiel:** `ni(3.00000000001) ni(3.1)`  
**Ergebnis:** true false

</details>

<details markdown="1">
<summary><code>noopt(ausdruck)</code></summary>

Ausdruck wird nicht optimiert, bleibt also so erhalten wie angegeben. Die Funktion an sich geht aber verloren.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `noopt(2+3)`  
**Ergebnis:** 2+3

</details>

<details markdown="1">
<summary><code>nopt(ausdruck)</code></summary>

Ausdruck wird nicht optimiert, bleibt also so erhalten wie angegeben. Die Funktion bleibt erhalten und wird erst bei der Lösungsberechnung oder durch opt() entfernt.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `noopt(2+3)`  
**Ergebnis:** 2+3

</details>

<details markdown="1">
<summary><code>norm(wert, normreihe)</code></summary>

rundet einen Zahlenwert auf den nächstliegenden Wert einer gegebenen Wertereihe oder Normreihe. Die Rundung erfolgt geometrisch wenn es sich um eine logarithmisch aufgeteilte Normreihe handelt, oder sonst linear.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `normreihe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `norm(700Ohm,E12)`  
**Ergebnis:** 680Ohm

</details>

<details markdown="1">
<summary><code>normdown(wert, normreihe)</code></summary>

rundet einen Zahlenwert auf den nächstkleineren Wert einer gegebenen Wertereihe oder Normreihe.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `normreihe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `normdown(700Ohm,E12)`  
**Ergebnis:** 680Ohm

</details>

<details markdown="1">
<summary><code>normup(wert, normreihe)</code></summary>

rundet einen Zahlenwert auf den nächstgrößerern Wert einer gegebenen Wertereihe oder Normreihe.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `normreihe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `normup(730Ohm[1,3,5,8])`  
**Ergebnis:** 800Ohm

</details>

<details markdown="1">
<summary><code>not(bedingung)</code></summary>

logisches NICHT. Vorsicht ein symbolisches Ergebnis von Maxima liefert not als Prefix-Operator, welcher vom Parser nicht unterstützt wird ( Verwende statt dessen lnot )

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `bedingung` | Parameter der Funktion. | Ausdruck | nein |

**Beispiel:** `not(a<b)`

</details>

<details markdown="1">
<summary><code>nullfrompolynom(polynom)</code></summary>

Erzeugt aus einem Polynom einen Vektor mit den PolynomNullstellen und Polstellen. Erste Zeile gemeinsamer Faktor, zweite Zeile Nullstellen, dritte Zeile Polstellen, vierte Zeile Polynomvariable

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `polynom` | Parameter der Funktion. | Zahl/Ausdruck | nein |

**Beispiel:** `nullfrompolynom(polynom((2+x)/(1+2*x)))`  
**Ergebnis:** [0.5,[-2],[-0.5],x]

</details>

<details markdown="1">
<summary><code>number(ausdruck)</code></summary>

Erzwingt die numerische Auswertung aller numerisch berechenbaren Teile. Bleibt bei einem weiterhin symbolischen Ergebnis als Funktion erhalten.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `number(2+3+x)`  
**Ergebnis:** number(5+x)

</details>

<details markdown="1">
<summary><code>numdif(position, funktion, variable, schrittweite)</code></summary>

numerisches Differenzieren einer Funktion "funktion" nach einer Variablen "Variable" an der Stelle "position" mit einer Differenz der Variablen von "differenz" numdif(position,funktion,Variable,differenz)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `position` | Stelle, an der differenziert wird. | Zahl / Ausdruck | nein |
| `funktion` | Zu differenzierender Ausdruck. | Ausdruck | nein |
| `variable` | Variable, nach der differenziert wird. | Variable | nein |
| `schrittweite` | Differenz für die numerische Ableitung. | Zahl / Ausdruck | nein |

**Beispiel:** `numdif(0,sin(t),t,0.01)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>numeric(oE)</code></summary>

verwirft die Einheit, wenn eine vorhanden ist und liefert nur den Zahlenwert (bezogen auf die Einheit!). Bei einer SI-Einheit wird der Zahlenwert bezogen auf die Basiseinheit geliefert, bei dimensonslosen Größen wird der Zahlenwert bezogen auf die verwendete dimensionslose Einheit gewählt. numeric(x)*unit(x) liefert wieder x

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oE` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `numeric(2.3mA) numeric(5%)`  
**Ergebnis:** 0.0023 5

</details>

<details markdown="1">
<summary><code>numint(untergrenze, obergrenze, funktion, variable, anzahl, ...)</code></summary>

numerische Integration numint(untereGrenze,obereGrenze,funktion,Variable) numint(untereGrenze,obereGrenze,funktion,Variable,punkteAnzahl)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `untergrenze` | Untere Integrationsgrenze. | Zahl / Ausdruck | nein |
| `obergrenze` | Obere Integrationsgrenze. | Zahl / Ausdruck | nein |
| `funktion` | Zu integrierender Ausdruck. | Ausdruck | nein |
| `variable` | Integrationsvariable. | Variable | nein |
| `anzahl` | Optionale Anzahl der Integrationsschritte. | Ganzzahl | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `numint(0,2pi,sin(t),t)`  
**Ergebnis:** 0

</details>

<details markdown="1">
<summary><code>nv(ausdruck, ...)</code></summary>

Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden. Im Gegensatz zu ev werden bestehende Variable nur in den Gleichungen, aber nicht im Ausdruck selbst eingesetzt!

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `zuweisungen` | Parameter der Funktion. | Ausdruck | ja, beliebig oft |

**Beispiel:** `nv(x*y,y=4)`  
**Ergebnis:** x*4

</details>

<details markdown="1">
<summary><code>onlypos(variable)</code></summary>

liefert aus dem Lösungsvektor von solve welcher aus lauter Gleichungen besteht nur die Lösungen welche positiv nicht Null sind

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

**Beispiel:** `onlypos([[x=3,y=-3],[x=4,y=5],[x=-2,y=4]]) onlypos([x=-2,x=0,x=6,x=8])`  
**Ergebnis:** [[x=4,y=5]] [x=7,x=8]

</details>

<details markdown="1">
<summary><code>onlyreal(matrix)</code></summary>

liefert aus dem Lösungsvektor von solve welcher aus lauter Gleichungen besteht nur die Lösungen welche reell sind

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |

**Beispiel:** `onlyreal([[x=1,y=%i],[x=1,y=-%i],[x=3,y=4]]) onlyreal([x=%i+1,x=1-%i,x=3,x=8])`  
**Ergebnis:** [[x=3,y=4]] [x=3,x=8]

</details>

<details markdown="1">
<summary><code>opt(ausdruck)</code></summary>

Ausdruck wird vollständig optimiert, die Funktion wird ausgewertet und ist danach nicht mehr vorhanden. Nur bei der Verwendung des internen Parser sinnvoll.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `opt(x+x)`  
**Ergebnis:** 2*x

</details>

<details markdown="1">
<summary><code>optorder(ausdruck)</code></summary>

Optimiert nur die symbolische Reihenfolge des Ausdrucks. Optional steuert ein zweiter ganzzahliger Modus, ob bzw. wie lange die Funktion im Ausdruck erhalten bleibt.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `optorder(y+x)`  
**Ergebnis:** x+y

</details>

<details markdown="1">
<summary><code>originnumeric(x)</code></summary>

liefert immer den Zahlenwert einer einheitenbehafteten Größe bezogen auf die vorhandene Einheit. Gibt es keine Originaleinheit da der Wert berechnet wurde wird der Zahlenwert bezogen auf die SI-Grundeinheit genommen. originnumeric(x)*originunit(x) liefert wieder x

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |

**Beispiel:** `originnumeric(2.3mA) originnumeric(2.3mA*2Ohm) originnumeric(15°)`  
**Ergebnis:** 2.3 0.0046 15

</details>

<details markdown="1">
<summary><code>originunit(oE)</code></summary>

gibt die SI-Einheit eines einheitenbehafteten Wertes mit dem Zahlenwert 1 zurück. originnumeric(x)*originunit(x) liefert wieder x

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oE` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `unit(3.1kA) unit(5%)`  
**Ergebnis:** 1kA 1%

</details>

<details markdown="1">
<summary><code>par(wert1) / par(wert1, wert2)</code></summary>

Parallelschaltung von Widerständen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja (bei 2 Parametern) |

**Beispiel:** `par(x,y)`  
**Ergebnis:** x*y/(x+y)

</details>

<details markdown="1">
<summary><code>parity(paritaet, codewortlaenge, datenwort, ...)</code></summary>

Paritätsberechnung : parity(Parität,Codewortlänge,Datenwort)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `paritaet` | Parameter der Funktion. | Variable / String | nein |
| `codewortlaenge` | Parameter der Funktion. | Ganzzahl | nein |
| `datenwort` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `parity(even,7,"xy")`

</details>

<details markdown="1">
<summary><code>parse(string)</code></summary>

Wenn der Parameter ein String ist wird dieser String mit dem Parser interpretiert

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |

**Beispiel:** `parse("2+3")`  
**Ergebnis:** 5

</details>

<details markdown="1">
<summary><code>parsecolor(farbcode)</code></summary>

Wandelt einen String mit einem Widerstandsfarbcode in einen Double-Wert

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `farbcode` | Parameter der Funktion. | String | nein |

**Beispiel:** `parsecolor("br-rt-br")`  
**Ergebnis:** 120

</details>

<details markdown="1">
<summary><code>parseip(ipAdresse)</code></summary>

Wandelt einen String mit einer IP-Adresse in einen Long-Wert

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ipAdresse` | Parameter der Funktion. | String | nein |

**Beispiel:** `parseip("91.119.43.5")`  
**Ergebnis:** 1534536453

</details>

<details markdown="1">
<summary><code>parser(ausdruck)</code></summary>

Markierungsfunktion für Ausdrücke, die von Maxima unverändert an den internen Parser weitergereicht werden sollen. Im internen Parser selbst wird lediglich der einzelne Parameter ausgewertet.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `parser(x+1)`  
**Ergebnis:** x+1

</details>

<details markdown="1">
<summary><code>periodic(variable, periodeExtern, periodeIntern, funktion)</code></summary>

Erzeugt aus einer beliebigen Funktion zwischen 0 und Periodendauer eine periodische Funktion periodic(Variable,Periodendauer,Funktion) periodic(Variable,Periodendauer,Funktionsperiodendauer,Funktion)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `periodeExtern` | Parameter der Funktion. | Variable | nein |
| `periodeIntern` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `funktion` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `ch1(t):periodic(t,5ms,2'Vms-2'*t^2) ch1(t):periodic(t,5ms,1,2V*t^2)`  
**Ergebnis:** !100px-ClipCapIt-190318-113524.PNG !100px-ClipCapIt-190318-113644.PNG

</details>

<details markdown="1">
<summary><code>pi()</code></summary>

Funktionsschreibweise der Kreiszahl Pi. `pi()` hat keine Parameter und entspricht `%pi`.


**Beispiel:** `pi()`  
**Ergebnis:** %pi

</details>

<details markdown="1">
<summary><code>plugin(pluginname, ...)</code></summary>

Ruft die Berechnungsmethode des Plugins, welches als erster Stringparameter angegeben werden muss auf und übergibt die weiteren Parameter an die Berechnungsmethode des Plugins.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `pluginname` | Parameter der Funktion. | String | nein |
| `wert2` | Wert bzw. Ausdruck des 2. Parameters. | Zahl / Ausdruck | ja, beliebig oft |

**Beispiel:** `plugin("plugin1",3)`  
**Ergebnis:** führt die Berechnung des Plugins mit dem Namen "plugin1" mit dem Parameter 3 aus.

</details>

<details markdown="1">
<summary><code>points(teilfrage)</code></summary>

Berechnet die erreichbare Gesamtpunkteanzahl einer Frage

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `teilfrage` | Parameter der Funktion. | Ganzzahl | nein |

**Beispiel:** `points()`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>pol(betrag, winkel)</code></summary>

erzeugt aus Betrag und Argument eine komplexe Zahl

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `betrag` | Parameter der Funktion. | Zahl | nein |
| `winkel` | Parameter der Funktion. | Zahl / Ausdruck | nein |

**Beispiel:** `pol(5,0.9272952180016122)`  
**Ergebnis:** 3+4*%i

</details>

<details markdown="1">
<summary><code>polgrad(betrag, winkel)</code></summary>

Erzeugt aus Betrag und einem Winkel im Gradmaß eine komplexe Zahl.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `betrag` | Parameter der Funktion. | Zahl | nein |
| `winkel` | Parameter der Funktion. | Zahl / Ausdruck | nein |

**Beispiel:** `polgrad(5,53.130102°/1°)`  
**Ergebnis:** 3+4*%i

</details>

<details markdown="1">
<summary><code>polynom() / polynom(polynom, varName, varEinheit, wert4)</code></summary>

Erzeugt aus einem Ausdruck welcher genau eine Variable besitzen muss ein Polynom in dieser Variablen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `polynom` | Parameter der Funktion. | Zahl/Ausdruck | ja |
| `varName` | Parameter der Funktion. | Variable | ja |
| `varEinheit` | Parameter der Funktion. | String / Zahl | ja |
| `wert4` | Wert bzw. Ausdruck des 4. Parameters. | Zahl / Ausdruck | ja |

**Beispiel:** `polynom(1+x)`  
**Ergebnis:** 1+x²

</details>

<details markdown="1">
<summary><code>polynomfromfact(x) / polynomfromfact(x, varName, varName, ee)</code></summary>

Erzeugt aus einer Faktoren-Liste, welche mit factfrompolynom erstellt wurde ein neues Polynom

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Variable / String | nein |
| `varName` | Parameter der Funktion. | Variable / String | ja |
| `varName` | Parameter der Funktion. | Variable / String | ja |
| `ee` | Parameter der Funktion. | Variable / Vektor | ja |

**Beispiel:** `polynomfromfact([[1,0.5],[0.5,1],"x",""])`  
**Ergebnis:** (2+x)/(1+2*x)

</details>

<details markdown="1">
<summary><code>polynomfromnull(x, varName, varName)</code></summary>

Erzeugt aus einer Nullstellen-Polstellen-Liste, welche mit nullfrompolynom erstellt wurde ein neues Polynom

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Vektor / Zahl | nein |
| `varName` | Parameter der Funktion. | Zahl | nein |
| `varName` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `polynomfromnull([0.5,[-2],[-0.5],x])`  
**Ergebnis:** (2+x)/(1+2*x)

</details>

<details markdown="1">
<summary><code>polynomk(polynom)</code></summary>

Bestimmt den Faktor, welcher vom Polynom herausgehoben werden kann, so dass die höchste Potenz der Polynomvariable den Multiplikator Eins hat.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `polynom` | Parameter der Funktion. | Zahl/Ausdruck | nein |

**Beispiel:** `polynomk(polynom((2+x)/(1+2*x)))`  
**Ergebnis:** 0.5

</details>

<details markdown="1">
<summary><code>pow(basis, exponent)</code></summary>

Potenzfunktion

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `basis` | Parameter der Funktion. | Zahl / Ausdruck | nein |
| `exponent` | Parameter der Funktion. | Zahl / Ausdruck | nein |

**Beispiel:** `pow(2,3)`  
**Ergebnis:** 8

</details>

<details markdown="1">
<summary><code>prims(x1)</code></summary>

zerlegt eine Ganzzahl in ihre Primfaktoren

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

**Beispiel:** `prims(12)`  
**Ergebnis:** [2,2,3]

</details>

<details markdown="1">
<summary><code>product(funktion, variable, untergrenze, obergrenze)</code></summary>

Produktbildung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck des Faktors. | Ausdruck | nein |
| `variable` | Laufvariable des Produkts. | Variable | nein |
| `untergrenze` | Erster Wert der Laufvariable. | Zahl / Ausdruck | nein |
| `obergrenze` | Letzter Wert der Laufvariable. | Zahl / Ausdruck | nein |

**Beispiel:** `product(1/k,k,1,3)`  
**Ergebnis:** 1/6

</details>

<details markdown="1">
<summary><code>pulse(wert) / pulse(wert, wert, wert)</code></summary>

Rechteckfunktion: pulse(x,x0) ist gleich 1 für x0 < x < x0 + 1, sonst 0 pulse(x,x0,L) ist gleich 1 für x0 < x < x0 + L, sonst 0 !300px-Pulse.png

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja |

**Beispiel:** `pulse(x,2,4)`  
**Ergebnis:** !100px-pulse_x_2_4.png

</details>

<details markdown="1">
<summary><code>pvabs(punkte) / pvabs(punkte, index)</code></summary>

Bestimmt den Betrag eines Punktes oder aller Ortsvektoren zu den Punkten.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

**Beispiel:** `pvabs([[2,3],[4,5],[6,3],[-2,4]]) pvabs([[2,3],[4,5],[6,3],[-2,4]],1)`  
**Ergebnis:** [3.6056,6.4031,6.7082,4.4721] 6.4031

</details>

<details markdown="1">
<summary><code>pvarg(punkte) / pvarg(punkte, index)</code></summary>

Bestimmt den Winkel eines Punktes oder aller Ortsvektoren zu den Punkten.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

**Beispiel:** `pvarg([[2,3],[4,5],[6,3],[-2,4]]) pvarg([[2,3],[4,5],[6,3],[-2,4]],1)`  
**Ergebnis:** [0.98279,0.89606,0.46365,2.0344] 0.89606

</details>

<details markdown="1">
<summary><code>pvcompare(referenz, eingabe) / pvcompare(referenz, eingabe, toleranz) / pvcompare(referenz, eingabe, toleranz, minX, maxX, minY) / pvcompare(referenz, eingabe, toleranz, minX, maxX, minY, maxY)</code></summary>

Vergleicht einen Referenz-Linienzug mit einem eingegebenen Linienzug unter Berücksichtigung der Toleranz. Die Toleranz stellt eine relative Tolerenz bezogen auf den Bereich zwischen MinXY und MaxXY da, wobei eine Toleranz von 0.1 gleichbedeutend 10 Prozent bezogen auf Max-Min ist (Mit dem String "a0.1" könnte man auch ein absolute Toleranz von 0.1 für x und y realisieren) pvcompare(Referenz,Eingabe) pvcompare(Referenz,Eingabe,Toleranz) pvcompare(Referenz,Eingabe,MinX,MaxX,MinY,MaxY) pvcompare(Referenz,Eingabe,MinX,MaxX,MinY,MaxY,Toleranz)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `referenz` | Referenz-Linienzug. | Vektor / Zahl | nein |
| `eingabe` | Zu vergleichender Linienzug. | Vektor / Zahl | nein |
| `toleranz` | Optionale Toleranz. | Zahl / Toleranzangabe | ja (bei 3/6/7 Parametern) |
| `minX` | Optionaler minimaler X-Wert des Bezugsbereichs. | Zahl | ja (bei 6/7 Parametern) |
| `maxX` | Optionaler maximaler X-Wert des Bezugsbereichs. | Zahl | ja (bei 6/7 Parametern) |
| `minY` | Optionaler minimaler Y-Wert des Bezugsbereichs. | Zahl | ja (bei 6/7 Parametern) |
| `maxY` | Optionaler maximaler Y-Wert des Bezugsbereichs. | Zahl/Ausdruck | ja (bei 7 Parametern) |

**Beispiel:** `pvcompare([[0,0],[1,1],[2,1],[3,0]],[[0,0],[1,1],[2,1],[3,0]],0,3,-5,5)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>pvdistance(punkte)</code></summary>

Bestimmt die Abstände als Vektoren zwischen den Punkten. pvdistance([A,B,C]) liefert [AB,BC,CA]

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

**Beispiel:** `pvdistance([[1,2],[3,4],[10,10]])`  
**Ergebnis:** [[2,2],[7,6],[-9,-8]]

</details>

<details markdown="1">
<summary><code>pvequals(referenz, eingabe) / pvequals(referenz, eingabe, toleranz)</code></summary>

Prüft ob zwei Punktevektoren gleich sind. Die Genauigkeit wird als dritter Parameter angegeben, oder bei einem Antwortfeld von der Antworttoleranz genommen. Prozentangaben der Genauigkeit beziehen sich auf die Breite bzw. Höhe des Punktefeldes im karthesischen Koordinatensystem.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `referenz` | Parameter der Funktion. | Vektor / Zahl | nein |
| `eingabe` | Parameter der Funktion. | Vektor / Zahl | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |

**Beispiel:** `pvequals([[2,3],[4,5],[6,3],[-2,4],[-3,5],[-7,-9]],[4,5],[6.01,3],[-2,3.99],[-3,5],[-7,-9]],2%)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>pvforeachline(punkte, variable, ausdruck) / pvforeachline(punkte, variable, ausdruck, aggregation)</code></summary>

Führt für jedes Punktepaar eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `aggregation` | Parameter der Funktion. | Ausdruck | ja |

**Beispiel:** `pvforeachline([[2,3],[4,5],[6,3],[-2,4]],p,pvlineabs(p),"+")`  
**Ergebnis:** 10.890684873

</details>

<details markdown="1">
<summary><code>pvfunc(y, varlist, isnumeric, bis, schrittweite)</code></summary>

Erzeugt aus einer Funktionen in einer Variablen (x-Achse) eine Punktmatrix der Funktionswerte (y-Achse). pvfunc(funktion,variable,minx,maxx,deltax)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `y` | Y-Wert bzw. Ausdruck. | Vektor / Zahl | nein |
| `varlist` | Parameter der Funktion. | Variable / Zahl | nein |
| `isnumeric` | Parameter der Funktion. | Variable / Zahl | nein |
| `bis` | Obere Grenze bzw. Endwert. | Variable / Zahl | nein |
| `schrittweite` | Schrittweite bzw. Abstand zwischen zwei Berechnungsschritten. | Zahl / Ausdruck | nein |

**Beispiel:** `pvfunc(x^2,x,-2,2,0.5)`  
**Ergebnis:** [[−2,4],[−1.5,2.25],[−1,1],[−0.5,0.25],[0,0],[0.5,0.25],[1,1],[1.5,2.25]]

</details>

<details markdown="1">
<summary><code>pvget(punkte, index)</code></summary>

Liefert einen Punkt der Punkteliste.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | nein |

**Beispiel:** `pvget([[2,3],[4,5],[6,3],[-2,4]],1)`  
**Ergebnis:** [4,5]

</details>

<details markdown="1">
<summary><code>pvgetx(punkte) / pvgetx(punkte, index)</code></summary>

Bestimmt die x-Koordinate eines Punktes oder aller Punkte.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

**Beispiel:** `pvgetx([[2,3],[4,5],[6,3],[-2,4]]) pvgetx([[2,3],[4,5],[6,3],[-2,4]],1)`  
**Ergebnis:** [2,4,6,-2] 4

</details>

<details markdown="1">
<summary><code>pvgety(punkte) / pvgety(punkte, index)</code></summary>

Bestimmt die y-Koordinate eines Punktes oder aller Punkte.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

**Beispiel:** `pvgety([[2,3],[4,5],[6,3],[-2,4]]) pvgety([[2,3],[4,5],[6,3],[-2,4]],1)`  
**Ergebnis:** [3,5,3,4] 3

</details>

<details markdown="1">
<summary><code>pvhasline(punkte, linie) / pvhasline(punkte, linie, toleranz)</code></summary>

Prüft ob sich eine Linie innerhalb des Punktefeldes von Linien befindet. Die Genauigkeit kann wie bei pvequals als dritter Parameter angegeben werden.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `linie` | Parameter der Funktion. | Vektor / Zahl | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |

**Beispiel:** `pvhasline([[2,3],[4,5],[6,3],[-2,4],[-3,5],[-7,-9]],[[6,3],[-2,4]],2%)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>pvhaspoint(punkte, punkt) / pvhaspoint(punkte, punkt, toleranz)</code></summary>

Prüft ob sich ein Punkt innerhalb des Punktefeldes befindet. Die Genauigkeit kann wie bei pvequals als dritter Parameter angegeben werden.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `punkt` | Parameter der Funktion. | Vektor / Zahl | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |

**Beispiel:** `pvhaspoint([[2,3],[4,5],[6,3],[-2,4],[-3,5],[-7,-9]],[4,5],2%)`  
**Ergebnis:** true

</details>

<details markdown="1">
<summary><code>pvinsert(punkte, punkt, index)</code></summary>

Fügt einen Punkt in die Punktemenge ein

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `punkt` | Parameter der Funktion. | Vektor / Ganzzahl | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | nein |

**Beispiel:** `pvinsert([[2,3],[4,5],[6,3],[-2,4]],[7,8],2)`  
**Ergebnis:** [[2,3],[4,5],[7,8],[6,3],[-2,4]]

</details>

<details markdown="1">
<summary><code>pvinsertlast(punkte, punkt)</code></summary>

Fügt am Ende der Punktemenge einen Punkt ein

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `punkt` | Parameter der Funktion. | Vektor | nein |

**Beispiel:** `pvinsertlast([[2,3],[4,5],[6,3],[-2,4]],[7,8])`  
**Ergebnis:** [[2,3],[4,5],[6,3],[-2,4],[7,8]]

</details>

<details markdown="1">
<summary><code>pvline(punkte) / pvline(punkte, index)</code></summary>

Bestimmt die Geradengleichung einer Geraden durch das n-te Punktepaar

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

**Beispiel:** `pvline([[2,3],[4,5],[6,3],[-2,4]]) pvline([[2,3],[4,5],[6,3],[-2,4]],0)`  
**Ergebnis:** [y=1+x,y=3.75−0.125⋅x] y=x+1

</details>

<details markdown="1">
<summary><code>pvlineabs(punkte) / pvlineabs(punkte, index)</code></summary>

Bestimmt aus dem n-ten Punktepaar den Absolutbetrag des Abstandes.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

**Beispiel:** `pvlineabs([[2,3],[4,5],[6,3],[-2,4]]) pvlineabs([[2,3],[4,5],[6,3],[-2,4]],0)`  
**Ergebnis:** [2.8284,8.0623] 2.82842712475

</details>

<details markdown="1">
<summary><code>pvlinearg(punkte) / pvlinearg(punkte, index)</code></summary>

Bestimmt aus dem n-ten Punktepaar den Winkel der Strecke zur x-Achse

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

**Beispiel:** `pvlinearg([[2,3],[4,5],[6,3],[-2,4]]) pvlinearg([[2,3],[4,5],[6,3],[-2,4]],0)`  
**Ergebnis:** [45°,172.87°] 45°

</details>

<details markdown="1">
<summary><code>pvlined(punkte) / pvlined(punkte, index)</code></summary>

Bestimmt den Schnittpunkt einer Geraden durch das n-te Punktepaar mit der y-Achse

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

**Beispiel:** `pvlined([[2,3],[4,5],[6,3],[-2,4]]) pvlined([[2,3],[4,5],[6,3],[-2,4]],0)`  
**Ergebnis:** [1,3.75] 1

</details>

<details markdown="1">
<summary><code>pvlinek(punkte) / pvlinek(punkte, index)</code></summary>

Bestimmt die Steigung der zugehörigen Geraden dem n-ten Punktepaar

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

**Beispiel:** `pvlinek([[2,3],[4,5],[6,3],[-2,4]]) pvlinek([[2,3],[4,5],[6,3],[-2,4]],0)`  
**Ergebnis:** [1,−0.125] 1

</details>

<details markdown="1">
<summary><code>pvlines(punkte) / pvlines(punkte, reserviert)</code></summary>

Bestimmt die Anzahl der Linien bzw. Punktepaare eines Punktevektors.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `reserviert` | Optionaler zusätzlicher Parameter; wird von der aktuellen Implementierung akzeptiert, aber nicht ausgewertet. | Ausdruck / passender Datentyp | ja |

**Beispiel:** `pvlines([[1,2],[3,4],[5,6],[7,8]])`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>pvpoints(punkte) / pvpoints(punkte, reserviert)</code></summary>

Bestimmt die Anzahl der Punkte

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `reserviert` | Optionaler zusätzlicher Parameter; wird von der aktuellen Implementierung akzeptiert, aber nicht ausgewertet. | Ausdruck / passender Datentyp | ja |

**Beispiel:** `pvpoints([[2,3],[4,5],[6,3],[-2,4]])`  
**Ergebnis:** 4

</details>

<details markdown="1">
<summary><code>pvrect(punkte)</code></summary>

Liefert aus einer Punktewolke ein Rechteck als zwei Eckpunkte links-unten und rechts-oben.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

**Beispiel:** `pvrect([[1,2],[4,5],[2,3]])`  
**Ergebnis:** [[1,2],[4,5]]

</details>

<details markdown="1">
<summary><code>pvremove(punkte, index)</code></summary>

Löscht einen Punkt aus der Punktemenge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | nein |

**Beispiel:** `pvremove([[2,3],[4,5],[6,3],[-2,4]],2)`  
**Ergebnis:** [[2,3],[4,5],[-2,4]]

</details>

<details markdown="1">
<summary><code>pvsort(punkte)</code></summary>

Sortiert die Punkte zuerst nach steigender x-Koordinate und bei gleicher x-Koordinate nach steigender y-Koordinate.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

**Beispiel:** `pvsort([[2,3],[1,5],[1,2]])`  
**Ergebnis:** [[1,2],[1,5],[2,3]]

</details>

<details markdown="1">
<summary><code>pvsortabs(punkte)</code></summary>

Sortiert die Punkte nach steigendem Absolutbetrag des Ortsvektors

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

**Beispiel:** `pvsortabs([[2,3],[4,5],[6,3],[−2,4],[−3,5],[−7,−9]])`  
**Ergebnis:** [[2,3],[−2,4],[−3,5],[4,5],[6,3],[−7,−9]]

</details>

<details markdown="1">
<summary><code>pvsortarg(punkte)</code></summary>

Sortiert die Punkte nach steigendem Winkel des Ortsvektors (-pi bis pi)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

**Beispiel:** `pvsortarg([[2,3],[4,5],[6,3],[−2,4],[−3,5],[−7,−9]])`  
**Ergebnis:** [[−7,−9],[6,3],[4,5],[2,3],[−2,4],[−3,5]]

</details>

<details markdown="1">
<summary><code>pvsortlineabs(punkte)</code></summary>

Sortiert Punktepaare nach steigendem Betrag der Linienlänge.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

**Beispiel:** `pvsortlineabs([[2,3],[4,5],[6,3],[−2,4],[−3,5],[−7,−9]])`  
**Ergebnis:** [[2,3],[4,5],[6,3],[−2,4],[−3,5],[−7,−9]]

</details>

<details markdown="1">
<summary><code>pvsortlinearg(punkte)</code></summary>

Sortiert Punktepaare nach steigendem Winkel der Linienrichtung.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

**Beispiel:** `pvsortlinearg([[2,3],[4,5],[6,3],[−2,4],[−3,5],[−7,−9]])`  
**Ergebnis:** [[−3,5],[−7,−9],[2,3],[4,5],[6,3],[−2,4]]

</details>

<details markdown="1">
<summary><code>pvsortlinex(punkte)</code></summary>

Sortiert Punktepaare nach steigender x-Koordinate der kleineren x-Koordinate des Paares.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

**Beispiel:** `pvsortlinex([[2,3],[4,5],[6,3],[−2,4],[−3,5],[−7,−9]])`  
**Ergebnis:** [[−3,5],[−7,−9],[6,3],[−2,4],[2,3],[4,5]]

</details>

<details markdown="1">
<summary><code>pvsortliney(punkte)</code></summary>

Sortiert Punktepaare nach steigender y-Koordinate der kleineren y-Koordinate des Paares.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

**Beispiel:** `pvsortliney([[2,3],[4,5],[6,3],[−2,4],[−3,5],[−7,−9]])`  
**Ergebnis:** [[−3,5],[−7,−9],[2,3],[4,5],[6,3],[−2,4]]

</details>

<details markdown="1">
<summary><code>pvsortx(punkte)</code></summary>

Sortiert die Punkte nach steigender x-Koordinate

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

**Beispiel:** `pvsortx([[2,3],[4,5],[6,3],[−2,4],[−3,5],[−7,−9]])`  
**Ergebnis:** [[−7,−9],[−3,5],[−2,4],[2,3],[4,5],[6,3]]

</details>

<details markdown="1">
<summary><code>pvsorty(punkte)</code></summary>

Sortiert die Punkte nach steigender y-Koordinate

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |

**Beispiel:** `pvsorty([[2,3],[4,5],[6,3],[−2,4],[−3,5],[−7,−9]])`  
**Ergebnis:** [[−7,−9],[2,3],[6,3],[−2,4],[4,5],[−3,5]]

</details>

<details markdown="1">
<summary><code>pvunion(punktevektor1, wert2, ...)</code></summary>

hängt mehrere Punktevektoren zu einem größereren Punktevektor zusammen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punktevektor1` | Parameter der Funktion. | Vektor / Matrix | nein |
| `wert2` | Wert bzw. Ausdruck des 2. Parameters. | Zahl / Ausdruck | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `pvunion([[1,2],[3,4]],[[5,6],[7,8]],[9,10])`  
**Ergebnis:** [[1,2],[3,4],[5,6],[7,8],[9,10]]

</details>

<details markdown="1">
<summary><code>pvvect(punkte) / pvvect(punkte, index)</code></summary>

Bestimmt einen Vector aus dem n-te Punktepaar

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `punkte` | Parameter der Funktion. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

**Beispiel:** `pvvect([[2,3],[4,5],[6,3],[-2,4]],0)`  
**Ergebnis:** [2,2]

</details>

<details markdown="1">
<summary><code>qopt(ausdruck)</code></summary>

Im Maximafeld wird alles innerhalb der Funktion nicht ausgewertet und die Funktion bleibt erhalten, bei der Lösung wird nach dem Einsetzen der Werte der Ausdruck vollständig optimiert. Anwendung findet die Funktion bei boolschen Fragen und Folgefehlerbehandlung.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `qopt(x+3)`  
**Ergebnis:** qopt(x+3)

</details>

<details markdown="1">
<summary><code>quadrant(winkel) / quadrant(winkel, toleranz)</code></summary>

Liefert den Quadranten eines Winkels mit einer Toleranzangabe.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `winkel` | Parameter der Funktion. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |

**Beispiel:** `quadrant(20°,5°)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>ramp(x) / ramp(x, wert, wert)</code></summary>

Rampenfunktion: ramp(x,x0) Rampe von x0 < x < x0 + 1 ramp(x,x0,L) Rampe von x0 < x < x0 + L !300px-Funktion_ramp.png

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja |

**Beispiel:** `ramp(x,2,4)`  
**Ergebnis:** !100px-Ramp_Plot.png

</details>

<details markdown="1">
<summary><code>random(minimum) / random(minimum, maximum)</code></summary>

Zufallszahl aus einem definierten Zahlenbereich random(minimal,maximal) VORSICHT! Die Zufallszahl wird bei jedem Aufruf neu berechnet, weshalb sich der Wert bei jedem Anzeigevorgang einer Frage ändert. Sollte sich der berechnete Wert für eine Schülerangabe zwischen Fragestellung und Ergebniskontrolle nicht ändern dürfen (ist der Normalfall) muss man einen Datensatz statt einer Zufallszahl verwenden! Zufallszahlen haben in der Ergebnisberechnung keinen Sinn, und sollten maximal für angezeigte zufällige Werte verwendet werden!

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `minimum` | Kleinster möglicher Wert. | Zahl / Ausdruck | nein |
| `maximum` | Größter möglicher Wert. | Zahl / Ausdruck | ja |

**Beispiel:** `random(2,8)`  
**Ergebnis:** 3.4532

</details>

<details markdown="1">
<summary><code>randomC(minimum) / randomC(minimum, maximum)</code></summary>

komplexe Zufallszahl aus einem definierten Zahlenbereich für den Betrag VORSICHT! Die Zufallszahl wird bei jedem Aufruf neu berechnet!

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `minimum` | Kleinster möglicher Betrag. | Zahl / Ausdruck | nein |
| `maximum` | Größter möglicher Betrag. | Zahl / Ausdruck | ja |

**Beispiel:** `randomC(2,8)`  
**Ergebnis:** 3.4532arg40.3°

</details>

<details markdown="1">
<summary><code>range(x)</code></summary>

range(anzahl) liefert ein Feld von ganzzahligen Werten von 0 beginnend

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Vektor / Ganzzahl | nein |

**Beispiel:** `range(5)`  
**Ergebnis:** [0,1,2,3,4]

</details>

<details markdown="1">
<summary><code>ratsimp(ausdruck)</code></summary>

Ausdruck wird vollständig optimiert, die Funktion wird ausgewertet und ist danach nicht mehr vorhanden (wie opt, wird jedoch auch von Maxima ausgewertet)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `ratsimp(x+x)`  
**Ergebnis:** 2*x

</details>

<details markdown="1">
<summary><code>realpart(re)</code></summary>

Liefert den Realteil einer komplexen Zahl

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `realpart(3+4*%i)`  
**Ergebnis:** 3

</details>

<details markdown="1">
<summary><code>rectform(x)</code></summary>

hat in LeTTo keine Relevanz, da die Zahlendarstellung bei der Ausgabe definiert wird wie zB.: {=3arg2;karti}

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl | nein |

</details>

<details markdown="1">
<summary><code>removeunit(ausdruck)</code></summary>

entfernt bei einem Ausdruck alle Einheiten und ersetzt dabei alle einheitenbehafteten Größen durch den Zahlenwert bezogen auf die BasisEinheit des SI-Systems

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `removeunit(t*5'm/s'+4cm)`  
**Ergebnis:** t*5+0.04

</details>

<details markdown="1">
<summary><code>replaceallstring(string, sold, snew)</code></summary>

Ersetzt alle Vorkommen einer Zeichenkette (regulärer Ausdruck) durch eine andere Zeichenkette.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |
| `sold` | Parameter der Funktion. | String | nein |
| `snew` | Parameter der Funktion. | String | nein |

**Beispiel:** `replaceallstring("abcdefg","b.*e","xy")`  
**Ergebnis:** "axyfg"

</details>

<details markdown="1">
<summary><code>replacefirststring(string, sold, snew)</code></summary>

Ersetzt das erste Vorkommen einer Zeichenkette (regulärer Ausdruck) durch eine andere Zeichenkette.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |
| `sold` | Parameter der Funktion. | String | nein |
| `snew` | Parameter der Funktion. | String | nein |

**Beispiel:** `replacefirststring("abcdefg","b.*e","xy")`  
**Ergebnis:** "axyfg"

</details>

<details markdown="1">
<summary><code>replacestring(string, sold, snew)</code></summary>

Ersetzt alle Vorkommen einer Zeichenkette in einem String durch eine andere Zeichenkette.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |
| `sold` | Parameter der Funktion. | String | nein |
| `snew` | Parameter der Funktion. | String | nein |

**Beispiel:** `replacestring("abcdefg","bc","xy")`  
**Ergebnis:** "axydefg"

</details>

<details markdown="1">
<summary><code>reverse(v1)</code></summary>

Alias zu `setreverse`: Dreht die Reihenfolge eines Vektors/einer Menge um.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Matrix / Vektor | nein |

**Beispiel:** `reverse([1,2,3])`  
**Ergebnis:** [3,2,1]

</details>

<details markdown="1">
<summary><code>rhs(ausdruck)</code></summary>

liefert die rechte Seite einer Gleichung, Ungleichung oder eines Infix Operators

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `rhs(x+y=c+2)`  
**Ergebnis:** c+2

</details>

<details markdown="1">
<summary><code>root(wert) / root(wert, wurzelexponent)</code></summary>

Quadratwurzel. Entspricht `root(x,2)`.

Alias/Kompatibilitätsname zu `sqrt`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wurzelexponent` | Parameter der Funktion. | Zahl / Ausdruck | ja |

**Beispiel:** `root(8,3)`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>round(wert) / round(wert, kommastellen)</code></summary>

Rundet die Zahl kaufmännisch, der zweite Parameter gibt die Anzahl der Kommastellen an, ohne 2.Parameter wird auf Ganzzahlen gerundet, bei komplexen Zahlen wird Betrag und Winkel in Grad gerundet.

Alias/Kompatibilitätsname zu `cround`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `kommastellen` | Parameter der Funktion. | Ganzzahl | ja |

**Beispiel:** `round(23.535)`  
**Ergebnis:** 24

</details>

<details markdown="1">
<summary><code>runtime(ausdruck)</code></summary>

Bei dieser Funktion wird erst bei der Berechnung der Frageantwort, nach dem Einsetzen der Datensätze das komplette Maxima-Feld mit dem internen Parser durchgerechnet und danach der Parameter-Ausdruck berechnet. Dadurch kann man bei komplizierten Berechnungen eine sehr aufwendige symbolische Berechnung verhindern!

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `runtime(U)`

</details>

<details markdown="1">
<summary><code>runtimeexception(wert1)</code></summary>

Test-/Diagnosefunktion: erzeugt absichtlich eine RuntimeException. Ein optionaler Parameter wird als Fehlermeldung verwendet.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck des 1. Parameters. | Zahl / Ausdruck | nein |

**Beispiel:** `runtimeexception("Test")`  
**Ergebnis:** Fehler

</details>

<details markdown="1">
<summary><code>sec(x1)</code></summary>

Secans, `sec(x)=1/cos(x)`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `sec(0)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>sech(x1)</code></summary>

Secans-Hyperbolicus, `sech(x)=1/cosh(x)`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `sech(0)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>second() / second(variable)</code></summary>

liefert das zweite Element mit dem Index 1 eines Vektors

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | ja |

**Beispiel:** `second([12,13,14])`  
**Ergebnis:** 13

</details>

<details markdown="1">
<summary><code>seconds(sec)</code></summary>

Erzeugt aus einem Sekundenwert die Sekunden als Double ohne Einheit

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `sec` | Parameter der Funktion. | Zahl | nein |

</details>

<details markdown="1">
<summary><code>selective_kill(...)</code></summary>

Löscht alle Variablen aus dem Variablenspeicher außer den angegebenen Variablen bzw. Variablenvektoren und liefert die Anzahl der gelöschten Variablen.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable1` | Parameter der Funktion. | Variable | ja, beliebig oft |

**Beispiel:** `selective_kill(x,y)`  
**Ergebnis:** Anzahl der gelöschten Variablen

</details>

<details markdown="1">
<summary><code>setapply(variable, menge, ausdruck)</code></summary>

wendet einen Ausdruck oder Funktion auf alle Elemente einer Menge an

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `menge` | Menge bzw. Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `setapply(y,[1,2,3],y*2)`  
**Ergebnis:** [2,4,6]

</details>

<details markdown="1">
<summary><code>setboxplot(v1)</code></summary>

Liefert die Werte des Boxplot einer Menge (Minimum, unteres Quartil, Median, oberes Quartil, Maximum) als Vektor verwendbar für das Plot-Plugin#definierte-zeichenelemente-

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setboxplot([1,2,3,10,8,9]`  
**Ergebnis:** [1,2,5.5,9,10]

</details>

<details markdown="1">
<summary><code>setcompare(p1, p2)</code></summary>

vergleicht zwei Mengen miteinander, wobei die Reihenfolge egal ist

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `p1` | Parameter der Funktion. | Vektor / Zahl | nein |
| `p2` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setcompare([1,3,2,4],[3,7]) setcompare([1,3,2],[1,2,3]) setcompare([1,3,2],[1,3,2,3]) setcompare([1,2,3],[1,2,3])`  
**Ergebnis:** false true false true

</details>

<details markdown="1">
<summary><code>setcomparend(p1, p2)</code></summary>

vergleicht zwei Mengen miteinander, wobei die Reihenfolge egal ist und doppelte Werte als einfach behandelt werden.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `p1` | Parameter der Funktion. | Vektor / Zahl | nein |
| `p2` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setcomparend([1,3,2,4],[3,7]) setcomparend([1,3,2],[1,2,3]) setcomparend([1,3,2],[1,3,2,3]) setcomparend([1,2,3],[1,2,3])`  
**Ergebnis:** false true true true

</details>

<details markdown="1">
<summary><code>setcount(menge) / setcount(menge, wert)</code></summary>

Bestimmt die Anzahl wie oft ein Element in einer Menge vorkommt oder die Anzahl der Elemente der Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `menge` | Menge bzw. Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja (bei 2 Parametern) |

**Beispiel:** `setcount([31,-3,2,31,0,5,2],31) setcount([2,5,3,6])`  
**Ergebnis:** 2 4

</details>

<details markdown="1">
<summary><code>setcut()</code></summary>

Bildet die Schnittmenge aus mehreren Mengen


**Beispiel:** `setcut([1,3,2,4],[3,7])`  
**Ergebnis:** [3]

</details>

<details markdown="1">
<summary><code>setgeomittel(v1)</code></summary>

Bestimmt das geometrische Mittelwert einer Menge aus positiven reellen Zahlen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setgeomittel([10,20,30])`  
**Ergebnis:** 18.171206

</details>

<details markdown="1">
<summary><code>setget(variable, anzahl) / setget(variable, anzahl, string)</code></summary>

Liefert ein Element einer Menge oder einer Matrix (Menge von Mengen)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `anzahl` | Anzahl der Elemente, Stellen oder Wiederholungen. | Ganzzahl | nein |
| `string` | Zeichenkette, die verarbeitet werden soll. | String | ja (bei 3 Parametern) |

**Beispiel:** `setget([12,13,14],1) setget(matrix([9,2],[3,4]),0,1)`  
**Ergebnis:** 13 2

</details>

<details markdown="1">
<summary><code>setgetfirst(v1)</code></summary>

Liefert den ersten Wert einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setgetfirst([1,3,-2,4])`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>setgetlast(v1)</code></summary>

Liefert den letzten Wert einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setgetlast([1,3,-2,4])`  
**Ergebnis:** 4

</details>

<details markdown="1">
<summary><code>setgetmax(v1)</code></summary>

Liefert den größten Wert einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setgetmax([1,3,-2,4])`  
**Ergebnis:** 4

</details>

<details markdown="1">
<summary><code>setgetmin(v1)</code></summary>

Liefert den kleinsten Wert einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setgetmin([1,3,-2,4])`  
**Ergebnis:** -2

</details>

<details markdown="1">
<summary><code>setinsert(menge, index, wert)</code></summary>

fügt ein Element in eine Menge an eine gegebene Stelle ein

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `menge` | Menge bzw. Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `setinsert([12,13,14],1,25)`  
**Ergebnis:** [12,25,13,14]

</details>

<details markdown="1">
<summary><code>setlength(v1)</code></summary>

liefert die Anzahl der Elemente einer Liste, Menge oder eines Vektors

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setlength([3,6,54,34,3,54])`  
**Ergebnis:** 6

</details>

<details markdown="1">
<summary><code>setmakelist(ausdruck, variable, startOderMenge, stop, schrittweite, ...)</code></summary>

setmakelist(f,x,start,stop) setzt in den Ausdruck f für x die Werte von start bis stop mit einer Schrittweite von 1 ein.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `startOderMenge` | Parameter der Funktion. | Vektor / Matrix | nein |
| `stop` | Parameter der Funktion. | Vektor / Ganzzahl | nein |
| `schrittweite` | Schrittweite bzw. Abstand zwischen zwei Berechnungsschritten. | Zahl / Ausdruck | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

**Beispiel:** `setmakelist(x^2,x,1,4)`  
**Ergebnis:** [ 1,4,9,16 ]

</details>

<details markdown="1">
<summary><code>setmedian(v1)</code></summary>

Liefert den Median einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setmedian([4,3,1,5,6]`  
**Ergebnis:** 4

</details>

<details markdown="1">
<summary><code>setmittel(v1)</code></summary>

Bestimmt den Mittelwert einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setmittel([1,3,2,4])`  
**Ergebnis:** 2.5

</details>

<details markdown="1">
<summary><code>setmodus(v1)</code></summary>

Liefert das Element einer Menge, welches am öftesten vorkommt oder die Elemente als Menge wenn mehrere Elemente gleich oft vorkommen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setmodus([3,-3,2,0,5,2])`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>setnd(v1)</code></summary>

Löscht alle Duplikate aus der Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setnd([3,-3,2,0,5,2]))`  
**Ergebnis:** [3,-3,2,0,5]

</details>

<details markdown="1">
<summary><code>setpartof(p1, p2)</code></summary>

prüft ob die erste Menge eine Teilmenge der zweite Menge ist wobei die Reihenfolge egal ist aber mehrfache Werte berücksichtigt werden

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `p1` | Parameter der Funktion. | Vektor / Zahl | nein |
| `p2` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setpartof([1,4],[1,3,7]) setpartof([1,3],[1,2,3]) setpartof([1,3,3],[1,3,5,7]) setpartof([1,4,4],[1,2,3,4])`  
**Ergebnis:** false true false false

</details>

<details markdown="1">
<summary><code>setpartofnd(p1, p2)</code></summary>

prüft ob die erste Menge eine Teilmenge der zweite Menge ist wobei die Reihenfolge und mehrfache Werte egal sind

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `p1` | Parameter der Funktion. | Vektor / Zahl | nein |
| `p2` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setpartofnd([1,4],[1,3,7]) setpartofnd([1,3],[1,2,3]) setpartofnd([1,3,3],[1,3,5,7]) setpartofnd([1,4,4],[1,2,3,4])`  
**Ergebnis:** false true true true

</details>

<details markdown="1">
<summary><code>setprod(v1)</code></summary>

Bestimmt das Produkt aller Werte einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setprod([1,3,2,4])`  
**Ergebnis:** 24

</details>

<details markdown="1">
<summary><code>setquadratmittel(v1)</code></summary>

Bestimmt den quadratischen Mittelwert einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setquadratmittel([10,20,30])`  
**Ergebnis:** 21.6025

</details>

<details markdown="1">
<summary><code>setremove(variable, anzahl)</code></summary>

löscht ein Element einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `anzahl` | Anzahl der Elemente, Stellen oder Wiederholungen. | Ganzzahl | nein |

**Beispiel:** `setremove([12,13,14],1)`  
**Ergebnis:** [12,14]

</details>

<details markdown="1">
<summary><code>setremovefirst(v1)</code></summary>

Entfernt den ersten Wert einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setremovefirst([1,3,-2,4])`  
**Ergebnis:** [3,-2,4]

</details>

<details markdown="1">
<summary><code>setremovelast(v1)</code></summary>

Entfernt den letzten Wert einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setremovelast([1,3,-2,4])`  
**Ergebnis:** [1,3,-2]

</details>

<details markdown="1">
<summary><code>setreverse(v1)</code></summary>

Alias zu `setreverse`: Dreht die Reihenfolge eines Vektors/einer Menge um.

Alias/Kompatibilitätsname zu `reverse`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Matrix / Vektor | nein |

**Beispiel:** `setreverse([3,-3,2,0,5,2])`  
**Ergebnis:** [2,5,0,2,-3,3]

</details>

<details markdown="1">
<summary><code>setset(mengeOderMatrix, indexOderZeile, wertOderSpalte) / setset(mengeOderMatrix, indexOderZeile, wertOderSpalte, wert)</code></summary>

setzt ein Element einer Menge oder einer Matrix (Menge von Mengen)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `mengeOderMatrix` | Parameter der Funktion. | Matrix | nein |
| `indexOderZeile` | Parameter der Funktion. | Ganzzahl | nein |
| `wertOderSpalte` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja (bei 4 Parametern) |

**Beispiel:** `setset([12,13,14],1,35) setset(matrix([9,2],[3,4]),0,0,-9)`  
**Ergebnis:** [12,35,14] [[-9,2],[3,4]]

</details>

<details markdown="1">
<summary><code>setshuffle(v1) / setshuffle(v1, nummer)</code></summary>

Mischt eine Menge in eine andere Reihenfolge. VORSICHT, ohne zweiten Parameter (ganze Zahl) ändert sich die Reihenfolge bei jedem mal neu Laden automatisch und ist nicht nachvollziehbar, weshalb sie dann für Schülerbeispiele nicht einsetzbar ist! Daher ist es für eine praktische Anwendung in einem Schülerbeispiel erforderlich, dass der zweite Parameter determiniert (beispielsweise über einen Integer-Datensatz-Wert zwischen 0 und 1000) festgelegt wird.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Ganzzahl | nein |
| `nummer` | Nummer bzw. Auswahlindex. | Ganzzahl | ja (bei 2 Parametern) |

**Beispiel:** `setshuffle([3,-3,2,0,5,2],5)`  
**Ergebnis:** [2,3,−3,2,0,5]

</details>

<details markdown="1">
<summary><code>setsort(v1)</code></summary>

Sortiert die Elemente einer Menge aufsteigend

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setsort([3,-3,2,0,5,2])`  
**Ergebnis:** [-3,0,2,2,3,5]

</details>

<details markdown="1">
<summary><code>setsortnd(v1)</code></summary>

Sortiert die Elemente einer Menge aufsteigend und entfernt alle mehrfach vorkommenden Elemente

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setsortnd([31,-3,2,31,0,5,2])`  
**Ergebnis:** [-3,0,2,5,31]

</details>

<details markdown="1">
<summary><code>setsub(v1, von, bis)</code></summary>

setsub(M,x,y) Liefert eine Teilmenge von M der Elemente vom index x bis zum Index y

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Ganzzahl | nein |
| `von` | Untere Grenze bzw. Startwert. | Ganzzahl / Zahl | nein |
| `bis` | Obere Grenze bzw. Endwert. | Vektor / Ganzzahl | nein |

**Beispiel:** `setsub([1,3,-2,4],1,2)`  
**Ergebnis:** [3,-2]

</details>

<details markdown="1">
<summary><code>setsum(v1)</code></summary>

Bestimmt die Summe aller Werte einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setsum([1,3,2,4])`  
**Ergebnis:** 10

</details>

<details markdown="1">
<summary><code>setunion()</code></summary>

Fügt mehrere Mengen zu einer neuen Menge zusammen


**Beispiel:** `setunion([1,3,2,4],[3,7])`  
**Ergebnis:** [1,3,2,4,3,7]

</details>

<details markdown="1">
<summary><code>setunionnd()</code></summary>

Fügt mehrere Mengen zu einer neuen Menge zusammen, sortiert diese und entfernt alle mehrfachen Elemente


**Beispiel:** `setunionnd([1,3,2,4],[3,7])`  
**Ergebnis:** [1,2,3,4,7]

</details>

<details markdown="1">
<summary><code>setvarianz(v1)</code></summary>

Bestimmt die empirische Varianz einer Menge

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `setvarianz([3,1,2,5,4])`  
**Ergebnis:** ((3-3)^2+(1-3)^2+(2-3)^2+(5-3)^2+(4-3)^2)/5=2

</details>

<details markdown="1">
<summary><code>shl(wert) / shl(wert, stellen)</code></summary>

Schiebe Ganzzahl bitweise nach links

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `stellen` | Parameter der Funktion. | Ganzzahl | ja |

**Beispiel:** `shl(8,2)`  
**Ergebnis:** 32

</details>

<details markdown="1">
<summary><code>shr(wert) / shr(wert, stellen)</code></summary>

Schiebe Ganzzahl bitweise nach rechts

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `stellen` | Parameter der Funktion. | Ganzzahl | ja |

**Beispiel:** `shr(8,2)`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>sigma(x) / sigma(x, wert)</code></summary>

Sprungfunktion: sigma(x) liefert 0 für x<0 und 1 für x>=0

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja |

**Beispiel:** `sigma(243.3)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>signum(wert)</code></summary>

Liefert das Vorzeichen einer Zahl (-1,0,1). Bei einer komplexen Zahl das Vorzeichen des Realteils.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `signum(-4)`  
**Ergebnis:** -1

</details>

<details markdown="1">
<summary><code>sin(x1)</code></summary>

Sinus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `sin(%pi/2)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>sinh(x1)</code></summary>

Sinus-Hyperbolicus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `sinh(1)`  
**Ergebnis:** 1.1752012

</details>

<details markdown="1">
<summary><code>sixth() / sixth(variable)</code></summary>

liefert das sechste Element mit dem Index 5 eines Vektors

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | ja |

**Beispiel:** `sixth ([12,13,14,15,16,17,18])`  
**Ergebnis:** 17

</details>

<details markdown="1">
<summary><code>solve(gleichungen, varlist)</code></summary>

löst eine Gleichung oder ein Gleichungssystem nach einer oder mehrerer Variablen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `gleichungen` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `varlist` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |

**Beispiel:** `solve([2*x+y=3,x-y=0],[x,y])`  
**Ergebnis:** [[ x=1,y=1 ]]

</details>

<details markdown="1">
<summary><code>solvevalue(cc, varlist, ausdruck)</code></summary>

löst eine Gleichung oder ein Gleichungssystem nach einer Variablen und liefert genau die erste Lösung wenn sie numerisch berechenbar ist

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `cc` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `varlist` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `solvevalue([ 2*x+y=3,x-y=0 ],[ x,y ],x)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>splitoptunit(oE)</code></summary>

Zerlegt einen numerischen Wert in Zahlenwert und die optimale Einheit mit Zahlenwert 1 als Feld mit Zahlenwert als Index 0 und Einheit als Index 1

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oE` | Parameter der Funktion. | Vektor / Ganzzahl | nein |

**Beispiel:** `splitoptunit(1300kVA)`  
**Ergebnis:** [1.3,1MVA]

</details>

<details markdown="1">
<summary><code>splitstring(string, tz)</code></summary>

Teilt einen String in ein Array von Strings splitstring(string,separator)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |
| `tz` | Parameter der Funktion. | String | nein |

**Beispiel:** `splitstring("abcdefg","b")`  
**Ergebnis:** "a","c","defg"

</details>

<details markdown="1">
<summary><code>splitunit(oE)</code></summary>

Zerlegt einen numerischen Wert in Zahlenwert und die originale/optimale Einheit mit Zahlenwert 1 als Feld mit Zahlenwert als Index 0 und Einheit als Index 1

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oE` | Parameter der Funktion. | Vektor / Ganzzahl | nein |

**Beispiel:** `splitunit(1300kVA)`  
**Ergebnis:** [1300,1kVA]

</details>

<details markdown="1">
<summary><code>sqrt(wert) / sqrt(wert, wurzelexponent)</code></summary>

Quadratwurzel. Entspricht `root(x,2)`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wurzelexponent` | Parameter der Funktion. | Zahl / Ausdruck | ja |

**Beispiel:** `sqrt(9)`  
**Ergebnis:** 3

</details>

<details markdown="1">
<summary><code>stackoverflow()</code></summary>

Test-/Diagnosefunktion: erzeugt absichtlich einen StackOverflow. Nicht für reguläre Aufgaben verwenden.


**Beispiel:** `stackoverflow()`  
**Ergebnis:** Fehler

</details>

<details markdown="1">
<summary><code>strcat(...)</code></summary>

Fügt mehrere Strings zusammen.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja, beliebig oft |

**Beispiel:** `strcat("a","b")`  
**Ergebnis:** "ab"

</details>

<details markdown="1">
<summary><code>string(...)</code></summary>

Fügt mehrere Strings zusammen.

Alias/Kompatibilitätsname zu `strcat`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja, beliebig oft |

**Beispiel:** `string(123)`  
**Ergebnis:** "123"

</details>

<details markdown="1">
<summary><code>substring(string, startindex) / substring(string, startindex, endindex)</code></summary>

Liefert einen Teil eines Strings substring(string,startindex,endindex). Index beginnt bei 0 und endindex ist optional.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |
| `startindex` | Parameter der Funktion. | Ganzzahl | nein |
| `endindex` | Parameter der Funktion. | Ganzzahl | ja |

**Beispiel:** `substring("abcdefg",2,3)`  
**Ergebnis:** "cd"

</details>

<details markdown="1">
<summary><code>sum(funktion, variable, untergrenze, obergrenze)</code></summary>

Summenbildung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck des Summanden. | Ausdruck | nein |
| `variable` | Laufvariable der Summe. | Variable | nein |
| `untergrenze` | Erster Wert der Laufvariable. | Zahl / Ausdruck | nein |
| `obergrenze` | Letzter Wert der Laufvariable. | Zahl / Ausdruck | nein |

**Beispiel:** `sum(1/k,k,1,2)`  
**Ergebnis:** 3/2

</details>

<details markdown="1">
<summary><code>svphtosv(phaseA) / svphtosv(phaseA, phaseB, phaseC)</code></summary>

berechnet aus den Stranggrößen (a,b,c) einen komplexen Raumzeiger

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `phaseA` | Parameter der Funktion. | Zahl / Ausdruck | nein |
| `phaseB` | Parameter der Funktion. | Zahl / Ausdruck | ja (bei 3 Parametern) |
| `phaseC` | Parameter der Funktion. | Zahl / Ausdruck | ja (bei 3 Parametern) |

**Beispiel:** `svphtosv(0.5,0.5,-1)`  
**Ergebnis:** 1arg60°

</details>

<details markdown="1">
<summary><code>svsvtoph(raumzeiger) / svsvtoph(raumzeiger, index)</code></summary>

berechnet aus einem komplexen Raumzeiger die Stranggrössen berechnet aus einem komplexen Raumzeiger die Stranggrössen, index selektiert Stranggröße als Rückgabewert

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `raumzeiger` | Parameter der Funktion. | Zahl / Ausdruck | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | ja |

**Beispiel:** `svsvtoph(1arg60°) svsvtoph(1arg60°,3)`  
**Ergebnis:** [0.5,0.5,-1] -1

</details>

<details markdown="1">
<summary><code>symbolic(ausdruck)</code></summary>

Bei allen Variablen innerhalb von symbolic werden nur nicht-numerische Werte eingesetzt! Wird vor allem im Angabtext bei {= } verwendet

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `symbolic(x^2+2)`  
**Ergebnis:** x^2+2

</details>

<details markdown="1">
<summary><code>tailstring(string, length)</code></summary>

liefert den letzten Teil eines Strings teilstring(tailstring,zeichenanzahl)

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |
| `length` | Parameter der Funktion. | String / Ganzzahl | nein |

**Beispiel:** `tailstring("abcdefg",2)`  
**Ergebnis:** "fg"

</details>

<details markdown="1">
<summary><code>tan(x1)</code></summary>

Tangens

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `tan(%pi/4)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>tanh(x1)</code></summary>

Tangens-Hyperbolicus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

**Beispiel:** `tanh(1)`  
**Ergebnis:** 0.7615941

</details>

<details markdown="1">
<summary><code>third() / third(variable)</code></summary>

liefert das dritte Element mit dem Index 2 eines Vektors

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | ja |

**Beispiel:** `third([12,13,14])`  
**Ergebnis:** 14

</details>

<details markdown="1">
<summary><code>time(hour, minute, second, ...)</code></summary>

time(h,min,sec) erzeugt eine Uhrzeit als Ganzzahl in Sekunden seit Mitternacht

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `hour` | Parameter der Funktion. | String / Vektor | nein |
| `minute` | Parameter der Funktion. | Ganzzahl | nein |
| `second` | Parameter der Funktion. | Ganzzahl | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

</details>

<details markdown="1">
<summary><code>timestring(zeit, format)</code></summary>

erzeugt eine Uhrzeit als String

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `zeit` | Parameter der Funktion. | Zahl / Ausdruck | nein |
| `format` | Formatangabe für die Ausgabe. | String | nein |

</details>

<details markdown="1">
<summary><code>todB(oe)</code></summary>

versieht einen Zahlenwert mit der skalierenden Dezibel-Einheit dB welche mit 20*log10 berechnet wird

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

**Beispiel:** `todB(100) todB(100)*2`  
**Ergebnis:** 40dB 200

</details>

<details markdown="1">
<summary><code>tomaxima(ausdruck1) / tomaxima(ausdruck1, wert2)</code></summary>

Führt die Berechnung aller Parameter von links nach rechts hintereinander mit Maxima aus. Das Ergebnis ist dann das Ergebnis des letzten Parameters.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck1` | Parameter der Funktion. | Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck des 2. Parameters. | Zahl / Ausdruck | ja |

**Beispiel:** `tomaxima(y:x^2,y+2)`  
**Ergebnis:** x^2+2

</details>

<details markdown="1">
<summary><code>trunc(wert)</code></summary>

Schneidet die Zahl nach dem Komma ab

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `trunc(24.5)`  
**Ergebnis:** 24

</details>

<details markdown="1">
<summary><code>unit(oE)</code></summary>

gibt die SI-Einheit eines einheitenbehafteten Wertes mit dem Zahlenwert 1 ohne Einheitenvielfache zurück. numeric(x)*unit(x) liefert wieder x

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oE` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `unit(3.1kA) unit(5%)`  
**Ergebnis:** 1A 1%

</details>

<details markdown="1">
<summary><code>unitopt(calcPhysical)</code></summary>

liefert bei einem einheitenbehafteten Wert die optimale SI-Einheit mit optimierten Einheitenvielfachen

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `calcPhysical` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

**Beispiel:** `unitopt(1300kVA)`  
**Ergebnis:** 1.3MVA

</details>

<details markdown="1">
<summary><code>vabs(variable)</code></summary>

Berechnet den Betrag eines Vektors

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

**Beispiel:** `vabs([3,4])`  
**Ergebnis:** 5

</details>

<details markdown="1">
<summary><code>vadd(v1, v2)</code></summary>

Addiert zwei Vektoren elementweise

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor | nein |
| `v2` | Parameter der Funktion. | Vektor | nein |

**Beispiel:** `vadd([1,2,3],[4,5,6])`  
**Ergebnis:** [5,7,9]

</details>

<details markdown="1">
<summary><code>val(string)</code></summary>

Bestimmt den ASC-II-Code des ersten Zeichens welches als String-Parameter übergeben wurde.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |

**Beispiel:** `val("a")`  
**Ergebnis:** 97

</details>

<details markdown="1">
<summary><code>vdiv(v1, v2)</code></summary>

Dividiert zwei Vektoren elementweise

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor | nein |
| `v2` | Parameter der Funktion. | Vektor | nein |

**Beispiel:** `vdiv([1,2,3],[4,5,6])`  
**Ergebnis:** [1/3,2/5,3/6]

</details>

<details markdown="1">
<summary><code>verweis(matrix, wert, spalte)</code></summary>

verweis(M,x,n) liefert den Wert der n-ten Spalte (ohne Angabe von n die 2.Spalte) einer Matrix M wo x dem Wert in der ersten Spalte am nächsten liegt

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `spalte` | Parameter der Funktion. | Matrix / Ganzzahl | nein |

**Beispiel:** `verweis([[10,33],[20,77],[30,99]],21)`  
**Ergebnis:** 77

</details>

<details markdown="1">
<summary><code>verweisdown(matrix, wert, spalte)</code></summary>

verweisdown(M,x,n) liefert den Wert der n-ten Spalte (ohne Angabe von n die 2.Spalte) einer Matrix M wo x dem Wert in der ersten Spalte am nächsten liegt

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `spalte` | Parameter der Funktion. | Matrix / Ganzzahl | nein |

**Beispiel:** `verweisdown([[10,33],[20,77],[30,99]],27,1)`  
**Ergebnis:** 77

</details>

<details markdown="1">
<summary><code>verweisup(matrix, wert, spalte)</code></summary>

verweisup(M,x,n) liefert den Wert der n-ten Spalte (ohne Angabe von n die 2.Spalte) einer Matrix M wo x dem Wert in der ersten Spalte am nächsten liegt

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `spalte` | Parameter der Funktion. | Matrix / Ganzzahl | nein |

**Beispiel:** `verweisup([[10,33],[20,77],[30,99]],21)`  
**Ergebnis:** 99

</details>

<details markdown="1">
<summary><code>vex(v1, v2)</code></summary>

Berechnet das ex-Produkt von 2 Vektoren im 3-dimensionalen Raum

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |
| `v2` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `vex([1,2,3],[4,5,6])`  
**Ergebnis:** [-3,6,-3]

</details>

<details markdown="1">
<summary><code>vget(variable, anzahl) / vget(variable, anzahl, string)</code></summary>

Liefert ein Element einer Menge oder einer Matrix (Menge von Mengen)

Alias/Kompatibilitätsname zu `setget`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `anzahl` | Anzahl der Elemente, Stellen oder Wiederholungen. | Ganzzahl | nein |
| `string` | Zeichenkette, die verarbeitet werden soll. | String | ja (bei 3 Parametern) |

**Beispiel:** `vget([12,13,14],1) vget(matrix([9,2],[3,4]),0,1)`  
**Ergebnis:** 13 2

</details>

<details markdown="1">
<summary><code>vgetmaxima(variable, anzahl) / vgetmaxima(variable, anzahl, string)</code></summary>

liefert ein Element eines Vektors oder einer Matrix wobei der Index (wie bei Maxima) bei 1 startet.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `anzahl` | Anzahl der Elemente, Stellen oder Wiederholungen. | Ganzzahl | nein |
| `string` | Zeichenkette, die verarbeitet werden soll. | String | ja (bei 3 Parametern) |

**Beispiel:** `vgetmaxima([12,13,14],1)`  
**Ergebnis:** 12

</details>

<details markdown="1">
<summary><code>viewpow(ausdruck)</code></summary>

Gibt alle Wurzeln als Potenzen aus, und stellt alle Potenzen im Nenner als negativen Exponenten im Zähler dar

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `viewpow(sqrt(x))`  
**Ergebnis:** x^(1/2)

</details>

<details markdown="1">
<summary><code>viewsqrt(ausdruck)</code></summary>

Gibt Potenzen welche als Wurzel darstellbar sind auch als als Wurzeln mit der Funktion sqrt oder root aus

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |

**Beispiel:** `viewsqrt(x^(1/2))`  
**Ergebnis:** sqrt(x)

</details>

<details markdown="1">
<summary><code>vin(v1, v2)</code></summary>

Berechnet das innere Produkt von 2 Vektoren

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |
| `v2` | Parameter der Funktion. | Vektor / Zahl | nein |

**Beispiel:** `vin([1,2,3],[4,5,6])`  
**Ergebnis:** 32

</details>

<details markdown="1">
<summary><code>vindex(vektor, wert)</code></summary>

vindex(v,x) liefert den Index des Elementes eines Vektors, welcher am nächsten bei x liegt

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `vektor` | Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `vindex([10,30,70],40)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>vindexdown(vektor, wert)</code></summary>

vindexdown(v,x) liefert den Index des Elementes eines Vektors, welcher kleiner oder gleich x ist

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `vektor` | Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `vindexdown([10,30,70],60)`  
**Ergebnis:** 1

</details>

<details markdown="1">
<summary><code>vindexup(vektor, wert)</code></summary>

vindexup(v,x) liefert den Index des Elementes eines Vektors, welcher größer oder gleich x ist

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `vektor` | Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `vindexup([10,30,70],40)`  
**Ergebnis:** 2

</details>

<details markdown="1">
<summary><code>vinsert(menge, index, wert)</code></summary>

fügt ein Element in eine Menge an eine gegebene Stelle ein

Alias/Kompatibilitätsname zu `setinsert`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `menge` | Menge bzw. Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

**Beispiel:** `vinsert([12,13,14],1,25)`  
**Ergebnis:** [12,25,13,14]

</details>

<details markdown="1">
<summary><code>vmatrix(variable)</code></summary>

Erzeugt aus genau einem Vektor eine Matrix. Enthaltene Vektoren werden zu Matrixzeilen, einzelne Werte zu ein-elementigen Zeilen; eine Matrix wird unverändert zurückgegeben.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

**Beispiel:** `vmatrix([[1,2],[3,4]])`  
**Ergebnis:** [[1,2],[3,4]]

</details>

<details markdown="1">
<summary><code>vmul(v1, v2)</code></summary>

Multipliziert zwei Vektoren elementweise

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor | nein |
| `v2` | Parameter der Funktion. | Vektor | nein |

**Beispiel:** `vmul([1,2,3],[4,5,6])`  
**Ergebnis:** [4,10,18]

</details>

<details markdown="1">
<summary><code>vpow(v1, v2)</code></summary>

Potenziert zwei Vektoren elementweise

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor | nein |
| `v2` | Parameter der Funktion. | Vektor | nein |

**Beispiel:** `vpow([1,2,3],[4,5,6])`  
**Ergebnis:** [1,32,729]

</details>

<details markdown="1">
<summary><code>vremove(variable, anzahl)</code></summary>

löscht ein Element einer Menge

Alias/Kompatibilitätsname zu `setremove`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `anzahl` | Anzahl der Elemente, Stellen oder Wiederholungen. | Ganzzahl | nein |

**Beispiel:** `vremove([12,13,14],1)`  
**Ergebnis:** [12,14]

</details>

<details markdown="1">
<summary><code>vset(mengeOderMatrix, indexOderZeile, wertOderSpalte) / vset(mengeOderMatrix, indexOderZeile, wertOderSpalte, wert)</code></summary>

setzt ein Element einer Menge oder einer Matrix (Menge von Mengen)

Alias/Kompatibilitätsname zu `setset`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `mengeOderMatrix` | Parameter der Funktion. | Matrix | nein |
| `indexOderZeile` | Parameter der Funktion. | Ganzzahl | nein |
| `wertOderSpalte` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja (bei 4 Parametern) |

**Beispiel:** `vset([12,13,14],1,35) vset(matrix([9,2],[3,4]),0,0,-9)`  
**Ergebnis:** [12,35,14] [[-9,2],[3,4]]

</details>

<details markdown="1">
<summary><code>vsetmaxima(vektorOderMatrix, indexOderZeile, wertOderSpalte) / vsetmaxima(vektorOderMatrix, indexOderZeile, wertOderSpalte, wert)</code></summary>

setzt ein Element eines Vektors oder einer Matrix wobei der Index (wie bei Maxima) bei 1 startet.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `vektorOderMatrix` | Parameter der Funktion. | Matrix | nein |
| `indexOderZeile` | Parameter der Funktion. | Ganzzahl | nein |
| `wertOderSpalte` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja (bei 4 Parametern) |

**Beispiel:** `vsetmaxima([12,13,14],1,35)`  
**Ergebnis:** [35,13,14]

</details>

<details markdown="1">
<summary><code>vsub(v1, v2)</code></summary>

Subtrahiert zwei Vektoren elementweise

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor | nein |
| `v2` | Parameter der Funktion. | Vektor | nein |

**Beispiel:** `vsub([1,2,3],[4,5,6])`  
**Ergebnis:** [-3,-3,-3]

</details>

<details markdown="1">
<summary><code>weeks(sec)</code></summary>

Erzeugt aus einem Sekundenwert die Wochen (/7d) als Double ohne Einheit

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `sec` | Parameter der Funktion. | Zahl | nein |

</details>

<details markdown="1">
<summary><code>wenn(e1, e2, e3)</code></summary>

if(bedingung,wahr,falsch)

Alias/Kompatibilitätsname zu `if`.

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `e1` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |
| `e2` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |
| `e3` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |

**Beispiel:** `wenn(4<6,10,12)`  
**Ergebnis:** 10

</details>

<details markdown="1">
<summary><code>word(x)</code></summary>

Zahl in eine Ganzzahl wandeln und die letzten 16bit der Zahl Abschneiden, Einheit geht verloren

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Ganzzahl / Zahl | nein |

**Beispiel:** `word(34.2)`  
**Ergebnis:** 34

</details>

<details markdown="1">
<summary><code>years(sec)</code></summary>

Erzeugt aus einem Sekundenwert die Jahre (/365d) als Double ohne Einheit

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `sec` | Parameter der Funktion. | Zahl | nein |

</details>

## Probleme mit großen Gleichungssystemen
Bei der Verwendung von Plugins (zB: Drehstromplugin) können sehr rasch sehr große Gleichungssysteme entstehen. Der Standard-Lösungsweg, dass die Gleichungen algebraisch aufgelöst werden und dann zur Laufzeit die Werte eingesetzt werden, kann somit sehr lange Berechnungszeiten nach sich ziehen. Effizienter ist es, das Gleichungssystem zur Laufzeit mit eingesetzten Zahlen zu rechnen.

Dazu gibt es die Möglichkeit, in der Frage das Häkchen Vorberechnung auszuwählen, dann werden die Ergebnisse erst zur Laufzeit gerechnet.

**Achtung:** Der Parser hat Probleme mit der Berechnung von großen Gleichungssystemen. Es sollte daher zur Laufzeit bei der Verwendung von Drehstrom-Plugins mit Maxima gerechnet werden.
Dabei werden allerdings alle Einheiten entfernt und können wieder über .... zu den entsprechenden Formelzeichen hinzugefügt werden. Bedenken Sie aber, dass die Einheiten bei Berechnung mit Maxima zur Laufzeit prinzipiell verloren gehen.

## Ergebnisvorschau
Aufruf dieses Dialoges über den ![25px-ClipCapIt-180904-181443.PNG](25px-ClipCapIt-180904-181443.PNG)-Button aus dem [Toolbar](../Toolbar/index.md).

Die Berechnungen aus dem Maxima-Feld bei der [Fragendefinition](/notimplemented/index.md) können auch über den ![25px-ClipCapIt-180904-182120.PNG](25px-ClipCapIt-180904-182120.PNG)-Button durchgeführt werden. Hier wird die Berechnung durchgeführt und das Lösungsfeld ausgefüllt, aber der Rechengang wird nicht angezeigt.
<br>![400px-ClipCapIt-180904-181415.PNG](400px-ClipCapIt-180904-181415.PNG)

Beim Fehlersuchen oder bei komplexen Berechnungen kann es aber hilfreich sein, den ganzen Maxima-Lösungsweg zu sehen, dies ist über den ![25px-ClipCapIt-180904-181443.PNG](25px-ClipCapIt-180904-181443.PNG)-Button möchlich.

Kategorie:Berechnung

