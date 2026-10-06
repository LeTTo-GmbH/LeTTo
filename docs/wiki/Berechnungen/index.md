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
| [%i](konstanten/i/index.md) | i | komplexer Parameter als Lösung der Gleichung x^2=-1 |
| [%j](konstanten/j/index.md) | i | komplexer Parameter als Lösung der Gleichung x^2=-1<br><b>Wichtig:</b> Wir nur vom Parser unterstützt, nicht von Maxima |
| [%e](konstanten/e/index.md) | 2.718281828459045 | Eulersche Zahl |
| [%pi](konstanten/pi/index.md) | 3.141592653589793 | Kreiszahl |
| [%mu0](konstanten/mu0/index.md) | magnetische Feldkonstante | 4*%pi*1E-7'Vs/Am' |
| [%m0](konstanten/m0/index.md) | magnetische Feldkonstante (alt, wird bald entfernt werden) | 4*%pi*1E-7'Vs/Am' |
| [%epsilon0](konstanten/epsilon0/index.md) | elektrische Feldkonstante | 8.85418781762039E-12'As/Vm' |
| [%e0](konstanten/e0/index.md) | elektrische Feldkonstante (alt, wird bald entfernt werden) | 8.85418781762039E-12'As/Vm' |
| [%c0](konstanten/c0/index.md) | Lichtgeschwindigkeit | 299792458'm/s' |
| [%Qe](konstanten/qe/index.md) | Elementarladung | 1.602176620898E-19As |
| [%g](konstanten/g/index.md) | Erdbeschleunigung | 9.81'm/s^2' |
| [%NA](konstanten/na/index.md) | Avogadro Konstante | 6.02214085774E23/mol |
| [%k](konstanten/k/index.md) | Stefan Bolzman Konstante | Boltzmann-Konstante |
| [%R0](konstanten/r0/index.md) | Universelle Gaskonstante | 8.314459848'J/Kmol' |
| [%h](konstanten/h/index.md) | planksches Wirkungsquantum | 6.6260704081E-34Js |


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
| if bedingung then wahr else falsch | [if(bedingung,wahr,falsch)](func/auswertung-und-programmierung/if/index.md)   | Wenn-Funktion |
|                                    | [wenn(bedingung,wahr,falsch)](func/auswertung-und-programmierung/wenn/index.md) | Wenn-Funktion |

#### Infix Operatoren
##### arithmetische Operatoren

| Operator              | Priorität | Beschreibung                                                                 | Beispiel             | Ergebnis  |
|-----------------------|-----------|------------------------------------------------------------------------------|----------------------|-----------|
| [+](operatoren/infix/plus/index.md) | 40 | Addition | 4+5 | 9 |
| [-](operatoren/infix/minus/index.md) | 40 | Subtraktion | 6-2 | 4 |
| [*](operatoren/infix/multiplikation/index.md) | 50 | Multiplikation | 4*5 | 20 |
| [/](operatoren/infix/division/index.md) | 51 | Division | 20/4 | 5 |
| [%](operatoren/infix/prozent/index.md) | 51 | Divisionsrest | 104%20 | 4 |
| [&#124; &#124;](operatoren/infix/parallel/index.md) | 60 | Parallelschaltung | x &#124; &#124; y | x*y/(x+y) |
| [^](operatoren/infix/potenz/index.md) | 90 | Potenz | 2^3 | 8 |
| [.*.](operatoren/infix/implizite-multiplikation/index.md) | 200 | Operator der intern für eine fehlende bindende Multiplikation verwendet wird | 4x | 4*x |


##### Bitoperatoren

| Operator | Priorität | Beschreibung                              | Beispiel       | Ergebnis    |
|----------|-----------|-------------------------------------------|----------------|-------------|
| [&#124;](operatoren/infix/oder/index.md) | 20 | Bitweise oder logisches ODER | 9&#124;5 <br> true&#124;false | 13 <br>true |
| [or](operatoren/infix/or/index.md) | 20 | Bitweise oder logisches ODER | 9 or 5 | 13 |
| [&amp;](operatoren/infix/und/index.md) | 21 | Bitweise oder logisches UND | 13&amp;10 | 8 |
| [and](operatoren/infix/and/index.md) | 21 | Bitweise oder logisches UND | 13 and 10 | 8 |
| [xor](operatoren/infix/xor/index.md) | 22 | Bitweise oder logisches exklusiv oder XOR | 13 xor 10 | 7 |
| [imp](operatoren/infix/imp/index.md) | 23 | Bitweise oder logisches impliziert IMP | 13 imp 10 | -5 (siehe Detailseite) |
| [&lt;&lt;](operatoren/infix/links-schieben/index.md) | 35 | Bitweise links schieben | 5&lt;&lt;2 | 20 |
| [&gt;&gt;](operatoren/infix/rechts-schieben/index.md) | 35 | Bitweise rechts schieben | 8&gt;&gt;2 | 2 |


##### Vergleichsoperatoren

| Operator | Priorität | Beschreibung         | Beispiel |
|----------|-----------|----------------------|----------|
| [=](operatoren/infix/gleichung/index.md) | 3 | Gleichungsoperator | x=y |
| [==](operatoren/infix/gleich/index.md) | 30 | Gleichungsoperator | x==y |
| [!=](operatoren/infix/ungleich/index.md) | 30 | Ungleichungsoperator | x!=y |
| [&lt;](operatoren/infix/kleiner/index.md) | 32 | Kleiner | x&lt;y |
| [&lt;=](operatoren/infix/kleiner-gleich/index.md) | 32 | Kleiner gleich | x&lt;=y |
| [&gt;](operatoren/infix/groesser/index.md) | 32 | größer | x&gt;y |
| [&gt;=](operatoren/infix/groesser-gleich/index.md) | 32 | größer gleich | x&gt;=y |

##### Organisative Operatoren

| Operator | Priorität | Beschreibung                                                                        | Beispiel | Ergebnis |
|----------|-----------|-------------------------------------------------------------------------------------|----------|----------|
| [,](operatoren/infix/komma/index.md) | 0 | Listen-Trennzeichen | x,y |  |
| [$](operatoren/infix/dollar/index.md) | 1 | Trennzeichen zwischen mehreren Berechnungen |  |  |
| [;](operatoren/infix/semikolon/index.md) | 1 | Trennzeichen zwischen mehreren Berechnungen |  |  |
| [:](operatoren/infix/zuweisung/index.md) | 2 | Zuweisung an eine Variable auf der linken Seite | x:4/12 | 1/3 |
| [::](operatoren/infix/zuweisung-ohne-optimierung/index.md) | 2 | Zuweisung an eine Variable auf der linken Seite ohne die rechte Seite zu optimieren | x::4/12 | 4/12 |


#### Prefix Operatoren

| Operator | Priorität | Beschreibung                                          | Beispiel  | Ergebnis                                                                |
|----------|-----------|-------------------------------------------------------|-----------|-------------------------------------------------------------------------|
| [+](operatoren/prefix/plus/index.md) | 45 | positives Vorzeichen | +5 | 5 |
| [-](operatoren/prefix/minus/index.md) | 45 | negatives Vorzeichen | -(-5) | 5 |
| [~](operatoren/prefix/bit-inversion/index.md) | 95 | bitweise Inversion einer 64bit-Ganzzahl | ~0x0F0F | 0xFFFFFFFFFFFFF0F0 |
| [!](operatoren/prefix/logisches-nicht/index.md) | 120 | logisches NOT | !(3&lt;4) | false |
| [++](operatoren/prefix/inkrement/index.md) | 130 | Inkrement von Ganzzahlen | ++x | erhöht x um eins und gibt das Ergebnis nach der Erhöhung zurück |
| [--](operatoren/prefix/dekrement/index.md) | 130 | Dekrement von Ganzzahlen | --x | vermindert x um eins und gibt das Ergebnis nach der Verminderung zurück |
| [%](operatoren/prefix/prozent/index.md) | 200 | Prefix für Namen, welche als Konstante definiert sind | %pi | 3.141592653589793 |


#### Suffix Operatoren

| Operator | Priorität | Beschreibung             | Beispiel | Ergebnis                                                                    |
|----------|-----------|--------------------------|----------|-----------------------------------------------------------------------------|
| [++](operatoren/suffix/inkrement/index.md) | 135 | Inkrement von Ganzzahlen | x++ | erhöht x um eins und gibt den Variablenwert vor der Erhöhung zurück |
| [--](operatoren/suffix/dekrement/index.md) | 135 | Dekrement von Ganzzahlen | x-- | vermindert x um eins und gibt den Variablenwert vor der Verminderung zurück |


### Klammern
* [( )](klammern/runde-klammern/index.md) runde Klammern werden für mathematische Ausdrücke zur Klammerung verwendet
* [{ }](klammern/geschweifte-klammern/index.md) geschwungene Klammer werden im Angabetext für die Namen der Datensätze verwendet
* [&#91; &#93;](klammern/eckige-klammern/index.md) eckige Klammern werden für Vektoren und Matrizen verwendet. VORSICHT! Der Index in eckigen Klammer beginnt bei 1 (wegen Maxima-Kompatibilität). Allen anderen Indizes sind Nullbasiert (zB. vget, etc.)!

### Funktionen


Alle Funktionsnamen, Operatoren, Konstanten und Klammerarten in den folgenden Tabellen verlinken auf eigene Beschreibungsseiten. Die ausführliche Parameterreferenz ist in diese Seiten integriert. Eine [alphabetische Funktionsübersicht](func/index.md) erleichtert die Suche.
#### Funktionen für Ganzzahlen

| Funktion                                | Beschreibung                                                                                                                                                                | Beispiel                    | Ergebnis           |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------------|
| [band](func/funktionen-fuer-ganzzahlen/band/index.md) | bitweises UND [DEMO-Beispiel](../../demobsp.html?id=3514) | band(4,12) | 4 |
| [bor](func/funktionen-fuer-ganzzahlen/bor/index.md) | bitweises ODER | bor(4,1) | 5 |
| [bxor](func/funktionen-fuer-ganzzahlen/bxor/index.md) | bitweises EXKLUSIV ODER | bxor(4,5) | 1 |
| [bimp](func/funktionen-fuer-ganzzahlen/bimp/index.md) | bitweises Parameter1 impliziert Parameter2 | bimp(13,10) | -5 (laut aktueller Implementierung; siehe Detailseite) |
| [binv](func/funktionen-fuer-ganzzahlen/binv/index.md) | bitweises NICHT mit 8 bit | binv(0x0F) | 0xF0 |
| [shl](func/funktionen-fuer-ganzzahlen/shl/index.md) | Schiebe Ganzzahl bitweise nach links | shl(8,2) | 32 |
| [shr](func/funktionen-fuer-ganzzahlen/shr/index.md) | Schiebe Ganzzahl bitweise nach rechts | shr(8,2) | 2 |
| [div](func/funktionen-fuer-ganzzahlen/div/index.md) | Ganzzahldivision, Ergebnis wird abgeschnitten | div(5,2) | 2 |
| [inv8](func/funktionen-fuer-ganzzahlen/inv8/index.md) | bitweise Invertieren und die letzten 8 Bit bestimmen | inv8(0b1001) | 0b11110110 |
| [inv16](func/funktionen-fuer-ganzzahlen/inv16/index.md) | bitweise Invertieren und die letzten 16 Bit bestimmen | inv16(0xF0) | 0xFF0F |
| [inv32](func/funktionen-fuer-ganzzahlen/inv32/index.md) | bitweise Invertieren und die letzten 32 Bit bestimmen | inv32(0xF0) | 0bFFFFFF0F |
| [inv64](func/funktionen-fuer-ganzzahlen/inv64/index.md) | bitweise Invertieren und die letzten 64 Bit bestimmen | inv64(0xF0) | 0bFFFFFFFFFFFFFF0F |
| [byte](func/funktionen-fuer-ganzzahlen/byte/index.md) | Zahl in eine Ganzzahl wandeln und die letzten 8bit der Zahl Abschneiden, Einheit geht verloren | byte(34.2) | 34 |
| [word](func/funktionen-fuer-ganzzahlen/word/index.md) | Zahl in eine Ganzzahl wandeln und die letzten 16bit der Zahl Abschneiden, Einheit geht verloren | word(34.2) | 34 |
| [int](func/funktionen-fuer-ganzzahlen/int/index.md) | Zahl in eine Ganzzahl wandeln und die letzten 32bit der Zahl Abschneiden, Einheit geht verloren | int(34.2) | 34 |
| [long](func/funktionen-fuer-ganzzahlen/long/index.md) | Zahl in eine Ganzzahl wandeln , Einheit geht verloren | long(34.2) | 34 |
| [parity](func/funktionen-fuer-ganzzahlen/parity/index.md) | Paritätsberechnung : parity(Parität,Codewortlänge,Datenwort) | parity(even,7,"xy") |  |
| [blockparity](func/funktionen-fuer-ganzzahlen/blockparity/index.md) | Kreuz oder Blockparität : blockparity(Parität,Codewortlänge,Codewortanzahl,Datenwort) | blockparity(even,7,3,"abc") |  |
| [bcd](func/funktionen-fuer-ganzzahlen/bcd/index.md) | Wandelt in eine Long-Zahl in ein Feld aus BCD-kodierten Zahlen um | bcd(124) | &#91;1,2,4&#93; |
| [code](func/funktionen-fuer-ganzzahlen/code/index.md) | Code aus mehreren Codeworten zusammensetzen : code(Codewortlänge,Datenwort) | code(5,4,3,5) | 0b1000001100101 |
| [hamming](func/funktionen-fuer-ganzzahlen/hamming/index.md) | Bestimmt den Hamming-Abstand von mehreren Codeworten | hamming(1,2,4,8,16) | 2 |
| [komplement](func/funktionen-fuer-ganzzahlen/komplement/index.md) | Bildet das Zweierkomplement mit einer negativen Zahl mit einer bestimmten Bitanzahl, fehlt die Bitanzahl, so wird ein 32Bit-2er-komplement gebildet | komplement(-5,8) | 0b11111011 |
| [bitstream](func/funktionen-fuer-ganzzahlen/bitstream/index.md) | Erzeugt aus einer Ganzzahl einen Bitstrom als String mit einer definierten Anzahl von Bit (MSB werden nötigenfalls mit 0 gefüllt) : bitstream(Daten,Bitanzahl,Gruppengröße) | bitstream(0x184,12,4) | "0001 1000 0100" |
| [dechex](func/funktionen-fuer-ganzzahlen/dechex/index.md) | Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Hexadezimal-String mit Präfix `0x` aus. | dechex(12) | "0xC" |
| [hex](func/funktionen-fuer-ganzzahlen/hex/index.md) | Alias zu `dechex`: Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Hexadezimal-String aus. | hex(12) | "0xC" |
| [decbin](func/funktionen-fuer-ganzzahlen/decbin/index.md) | Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Binär-String mit Präfix `0b` aus. | decbin(10) | "0b1010" |
| [bin](func/funktionen-fuer-ganzzahlen/bin/index.md) | Alias zu `decbin`: Wandelt eine Zahl in eine Ganzzahl um und gibt sie als Binär-String aus. | bin(10) | "0b1010" |


#### Funktionen für rationale und Ganzzahlen

| Funktion      | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                        | Beispiel                                                 | Ergebnis                                                  |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------|
| [kgV](func/funktionen-fuer-rationale-und-ganzzahlen/kgv-gross-2/index.md) | berechnet das kleinste gemeinsame Vielfache von mehreren Zahlen [DEMO-Beispiel](../../demobsp.html?id=3197) | kgV(3,10) | 30 |
| [ggT](func/funktionen-fuer-rationale-und-ganzzahlen/ggt-gross-2/index.md) | berechnet den größten gemeinsamen Teiler von mehreren Zahlen [DEMO-Beispiel](../../demobsp.html?id=3199) | ggT(12,10) | 2 |
| [isprim](func/funktionen-fuer-rationale-und-ganzzahlen/isprim/index.md) | prüft ob die angegebene Zahl eine Primzahl ist [DEMO-Beispiel](../../demobsp.html?id=3200) | isprim(13) | true |
| [prims](func/funktionen-fuer-rationale-und-ganzzahlen/prims/index.md) | zerlegt eine Ganzzahl in ihre Primfaktoren [DEMO-Beispiel](../../demobsp.html?id=3201) | prims(12) | &#91;2,2,3&#93; |
| [defracmix](func/funktionen-fuer-rationale-und-ganzzahlen/defracmix/index.md) | zerlegt eine rationale Zahl in einen gemischten Bruch aus ganzzahligem Summanden, Zähler und Nenner als Menge<br>Die erhaltene Menge kann mit dem Format-Modfier **frac** als gemischter Bruch dargestellt werden (siehe [Zahlendarstellung](../Zahlendarstellung/index.md)) [DEMO-Beispiel](../../demobsp.html?id=3202) | defracmix(14/12)<br>defracmix(-15/12)<br>defracmix(3/12) | &#91;1,2/12&#93;<br>&#91;-1,3,12&#93;<br>&#91;0,3,12&#93; |
| [defrac](func/funktionen-fuer-rationale-und-ganzzahlen/defrac/index.md) | zerlegt eine rationale Zahl in Zähler und Nenner als Menge <br>Die erhaltene Menge kann mit dem Format-Modfier **frac** als gemischter Bruch dargestellt werden [DEMO-Beispiel](../../demobsp.html?id=3203) | defrac(14/12) | &#91;13,12&#93; |
| [frac](func/funktionen-fuer-rationale-und-ganzzahlen/frac/index.md) | erzeugt aus einer Menge aus 2 oder 3 Elementen (von defrac) eine rationale Zahl [DEMO-Beispiel](../../demobsp.html?id=3204) | frac(&#91;3,7&#93;)<br>frac(&#91;1,2,3&#93;) | 3/7 <br> 5/3 |
| [mod](func/funktionen-fuer-rationale-und-ganzzahlen/mod/index.md) | Mathematische Implementierung von [modulo](https://de.wikipedia.org/wiki/Division_mit_Rest#Modulo): Divisionsrest einer Division mit ganzzahligem Ergebnis [DEMO-Beispiel](../../demobsp.html?id=3205) | mod(5,2) <br> mod(6.2,2.5) <br> mod(-4,3) | 1<br>1.2 <br> 2 |
| [mod2](func/funktionen-fuer-rationale-und-ganzzahlen/mod2/index.md) | Symmetrische Implementierung von [modulo](https://de.wikipedia.org/wiki/Division_mit_Rest#Modulo): Divisionsrest einer Division mit ganzzahligem Ergebnis <br>Der Unterschied zu mod liegt in der Behandlung von negativen Zahlen des ersten Arguments <br>Siehe auch Divisionsrest des Parser-Operators % [Berechnungen arithmetische-operatoren-](../Berechnungen/index.md#arithmetische-operatoren-) [DEMO-Beispiel](../../demobsp.html?id=3206) | mod2(5,2) <br> mod2(6.2,2.5) <br> mod2(-4,3) | 1<br>1.2 <br> -1 |
| [isNearInteger](func/funktionen-fuer-rationale-und-ganzzahlen/isnearinteger-gross-2-6/index.md) | prüft ob eine Zahl nahe genug an einer Ganzzahl liegt, um als Ganzzahl interpretiert zu werden. Es wird die Toleranz der Frage verwendet | isNearInteger(3.00000000001) <br> isNearInteger(3.1) | true <br> false |
| [ni](func/funktionen-fuer-rationale-und-ganzzahlen/ni/index.md) | Kurzform von isNearInteger - prüft ob eine Zahl nahe genug an einer Ganzzahl liegt, um als Ganzzahl interpretiert zu werden. Es wird die Toleranz der Frage verwendet | ni(3.00000000001) <br> ni(3.1) | true <br> false |

#### Funktionen für Winkel im Gradmaß

| Funktion  | Beschreibung                                                                                                                                                                         | Beispiel                                                           | Ergebnis                          |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|-----------------------------------|
| [degmix](func/funktionen-fuer-winkel-im-gradmass/degmix/index.md) | zerlegt einen Winkel im Bogenmaß in einen Winkel in Grad, Minuten und Sekunden in einem Vektor [DEMO-Beispiel](../../demobsp.html?id=3194) | degmix(0.5) | &#91;28,38,52.4031239082&#93; |
| [deg](func/funktionen-fuer-winkel-im-gradmass/deg/index.md) | erzeugt aus einem Vektor mit Grad, Minuten und Sekunden als Zahlenwerte oder einen WinkelString einen Winkel im Bogenmaß [DEMO-Beispiel](../../demobsp.html?id=3195) | deg(&#91;2,15,22&#93;) <br> deg(&quot;2°15&#39;22&#39;&#39;&quot;) | 2.25611111111° |
| [degstring](func/funktionen-fuer-winkel-im-gradmass/degstring/index.md) | erzeugt aus einem Vektor mit Grad, Minuten und Sekunden als Zahlenwerte oder einen Winkel im Bogenmaß einen String der Winkeldarstellung [DEMO-Beispiel](../../demobsp.html?id=3196) | degstring(0.5) | &quot;2°15&#39;22&#39;&#39;&quot; |

#### boolesche(boolsche) Funktionen

| Funktion  | Beschreibung                                                                                                                                                                                                                                             | Beispiel               | Ergebnis |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|----------|
| [eq](func/boolesche-boolsche-funktionen/eq/index.md) | gleich eq(wert1,wert2),eq(wert1,wert2,toleranz),eq(wert1,wert2,toleranz,absolut) [DEMO-Beispiel](../../demobsp.html?id=3182) | eq(4,4) | true |
| [eqruntime](func/boolesche-boolsche-funktionen/eqruntime/index.md) | symbolischer Vergleich, welcher **symbolisch erst bei der Ergebnisberechnung** ausgeführt wird. Muss verwendet werden, wenn bei Vergleichen symbolische Antworten von Schülern (Q0,Q1,...) verwendet werden. [DEMO-Beispiel](../../demobsp.html?id=3183) | eqruntime(x+3*y,3*y+x) | true |
| [ne](func/boolesche-boolsche-funktionen/ne/index.md) | ungleich ne(wert1,wert2),ne(wert1,wert2,toleranz),ne(wert1,wert2,toleranz,absolut) [DEMO-Beispiel](../../demobsp.html?id=3184) | ne(6,4) | true |
| [ge](func/boolesche-boolsche-funktionen/ge/index.md) | größer gleich ge(wert1,wert2),ge(wert1,wert2,toleranz),ge(wert1,wert2,toleranz,absolut) [DEMO-Beispiel](../../demobsp.html?id=3185) | ge(6,4) | true |
| [le](func/boolesche-boolsche-funktionen/le/index.md) | kleiner gleich le(wert1,wert2),le(wert1,wert2,toleranz),le(wert1,wert2,toleranz,absolut) [DEMO-Beispiel](../../demobsp.html?id=3186) | le(6,4) | false |
| [gt](func/boolesche-boolsche-funktionen/gt/index.md) | größer [DEMO-Beispiel](../../demobsp.html?id=3187) | gt(6,4) | true |
| [lt](func/boolesche-boolsche-funktionen/lt/index.md) | kleiner [DEMO-Beispiel](../../demobsp.html?id=3188) | lt(6,4) | false |
| [between](func/boolesche-boolsche-funktionen/between/index.md) | prüft ob Parameter1 kleiner als Parameter2 und Parameter2 kleiner als Parameter 3 . Parameter 4 und 5 können optinal für die Toleranz verwendet werden. [DEMO-Beispiel](../../demobsp.html?id=3189) | between(3,4,5) | true |
| [land](func/boolesche-boolsche-funktionen/land/index.md) | logisches UND [DEMO-Beispiel](../../demobsp.html?id=3190) | land(a&lt;b,b&lt;c) |  |
| [lor](func/boolesche-boolsche-funktionen/lor/index.md) | logisches ODER [DEMO-Beispiel](../../demobsp.html?id=3191) | lor(a&lt;b,b&lt;c) |  |
| [not](func/boolesche-boolsche-funktionen/not/index.md) | logisches NICHT. Vorsicht ein symbolisches Ergebnis von Maxima liefert not als Prefix-Operator, welcher vom Parser nicht unterstützt wird ( Verwende statt dessen **lnot** ) [DEMO-Beispiel](../../demobsp.html?id=3192) | not(a&lt;b) |  |
| [lnot](func/boolesche-boolsche-funktionen/lnot/index.md) | logisches NICHT, wie not jedoch wird es von Maxima nicht ausgewertet [DEMO-Beispiel](../../demobsp.html?id=3193) | lnot(a&lt;b) |  |


#### Funktionen zu Einheiten

| Funktion      | Beschreibung                                                                                                                                                                                                                                                                                                                                                                            | Beispiel                                                                    | Ergebnis                   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------|
| [double](func/funktionen-zu-einheiten/double/index.md) | Zahl in eine Gleitkommazahl umwandeln, die Einheit geht dabei verloren [DEMO-Beispiel](../../demobsp.html?id=3176) | double(3.4V) | 3.4 |
| [float](func/funktionen-zu-einheiten/float/index.md) | Zahl in eine Gleitkommazahl umwandeln, die Einheit geht dabei verloren (wie double) | float(3.4V) | 3.4 |
| [numeric](func/funktionen-zu-einheiten/numeric/index.md) | verwirft die Einheit, wenn eine vorhanden ist und liefert nur den Zahlenwert (bezogen auf die Einheit!). Bei einer SI-Einheit wird der Zahlenwert bezogen auf die Basiseinheit geliefert, bei dimensonslosen Größen wird der Zahlenwert bezogen auf die verwendete dimensionslose Einheit gewählt. <br> numeric(x)*unit(x) liefert wieder x [DEMO-Beispiel](../../demobsp.html?id=3177) | numeric(2.3mA) <br> numeric(5%) | 0.0023 <br> 5 |
| [originnumeric](func/funktionen-zu-einheiten/originnumeric/index.md) | liefert immer den Zahlenwert einer einheitenbehafteten Größe bezogen auf die vorhandene Einheit. Gibt es keine Originaleinheit da der Wert berechnet wurde wird der Zahlenwert bezogen auf die SI-Grundeinheit genommen. <br> originnumeric(x)*originunit(x) liefert wieder x [DEMO-Beispiel](../../demobsp.html?id=3178) | originnumeric(2.3mA) <br> originnumeric(2.3mA*2Ohm) <br> originnumeric(15°) | 2.3 <br> 0.0046 <br> 15 |
| [removeunit](func/funktionen-zu-einheiten/removeunit/index.md) | entfernt bei einem Ausdruck alle Einheiten und ersetzt dabei alle einheitenbehafteten Größen durch den Zahlenwert bezogen auf die BasisEinheit des SI-Systems [DEMO-Beispiel](../../demobsp.html?id=3179) | removeunit(t*5'm/s'+4cm) | t*5+0.04 |
| [unit](func/funktionen-zu-einheiten/unit/index.md) | gibt die SI-Einheit eines einheitenbehafteten Wertes mit dem Zahlenwert 1 ohne Einheitenvielfache zurück. <br> numeric(x)*unit(x) liefert wieder x [DEMO-Beispiel](../../demobsp.html?id=3180) | unit(3.1kA) <br> unit(5%) | 1A <br> 1% |
| [originunit](func/funktionen-zu-einheiten/originunit/index.md) | gibt die SI-Einheit eines einheitenbehafteten Wertes mit dem Zahlenwert 1 zurück. <br> originnumeric(x)*originunit(x) liefert wieder x [DEMO-Beispiel](../../demobsp.html?id=3181) | unit(3.1kA) <br> unit(5%) | 1kA <br> 1% |
| [splitunit](func/funktionen-zu-einheiten/splitunit/index.md) | Zerlegt einen numerischen Wert in Zahlenwert und die originale/optimale Einheit mit Zahlenwert 1 als Feld mit Zahlenwert als Index 0 und Einheit als Index 1 | splitunit(1300kVA) | &#91;1300,1kVA&#93; |
| [splitoptunit](func/funktionen-zu-einheiten/splitoptunit/index.md) | Zerlegt einen numerischen Wert in Zahlenwert und die optimale Einheit mit Zahlenwert 1 als Feld mit Zahlenwert als Index 0 und Einheit als Index 1 | splitoptunit(1300kVA) | &#91;1.3,1MVA&#93; |
| [unitopt](func/funktionen-zu-einheiten/unitopt/index.md) | liefert bei einem einheitenbehafteten Wert die optimale SI-Einheit mit optimierten Einheitenvielfachen | unitopt(1300kVA) | 1.3MVA |
| [eh](func/funktionen-zu-einheiten/eh/index.md) | Liefert zu einem numerischen Wert die zugehörige Einheit als Wert 1 zurück; bei einem einheitenlosen Wert wird `1` geliefert. | eh(2.3mA) | 1mA |
| [dB](func/funktionen-zu-einheiten/db-gross-1/index.md) | Wandelt einen Zahlenwert in eine nicht skalierende [Dezibel](../Dezibel/index.md)-Einheit um. Einheitenlos wird in dB20 gewandelt, mit den Einheiten V,mV,uV,W,mW,uW wird in die zugehörige dB-Einheit gewandelt. [DEMO-Beispiel](../../demobsp.html?id=3213) | dB(100) <br> dB(100)+1 | 40 dB<sub>20</sub> <br> 41 |
| [fromdB](func/funktionen-zu-einheiten/fromdb-gross-5/index.md) | Wandelt eine nicht skalierende [Dezibel](../Dezibel/index.md)-Einheit in einen normalen Zahlenwert um [DEMO-Beispiel](../../demobsp.html?id=3214) | fromdB(40) | 100 |
| [todB](func/funktionen-zu-einheiten/todb-gross-3/index.md) | versieht einen Zahlenwert mit der skalierenden [Dezibel](../Dezibel/index.md)-Einheit dB welche mit 20*log<sub>10</sub> berechnet wird [DEMO-Beispiel](../../demobsp.html?id=3215) | todB(100)<br> todB(100)*2 | 40dB <br> 200 |
| [dB10](func/funktionen-zu-einheiten/db10-gross-1/index.md) | wandelt eine Zahl in einen [Dezibel](../Dezibel/index.md) Wert dB<sub>10</sub> mit 10dB pro Dekade [DEMO-Beispiel](../../demobsp.html?id=3216) | dB10(100) | 20dB<sub>10</sub> |
| [fromdB10](func/funktionen-zu-einheiten/fromdb10-gross-5/index.md) | wandelt einen [Dezibel](../Dezibel/index.md) Wert mit 10dB pro Dekade in den Ausgangswert [DEMO-Beispiel](../../demobsp.html?id=3217) | fromdB10(20) | 100 |
| [dBW](func/funktionen-zu-einheiten/dbw-gross-1-2/index.md) | wandelt eine Leistung in einen [Dezibel](../Dezibel/index.md) Wert dB<sub>W</sub> mit 10dB pro Dekade [DEMO-Beispiel](../../demobsp.html?id=3218) | dBW(100) | 20dB<sub>W</sub> |
| [fromdBW](func/funktionen-zu-einheiten/fromdbw-gross-5-6/index.md) | wandelt einen [Dezibel](../Dezibel/index.md) Wert mit 10dB pro Dekade in eine Leistung [DEMO-Beispiel](../../demobsp.html?id=3219) | fromdBW(20) | 100W |
| [dBm](func/funktionen-zu-einheiten/dbm-gross-1/index.md) | Wandelt eine Leistung in dBm um. Bezugsleistung ist 1 mW: `10*log10(P/1mW)`. Bei komplexen Leistungen wird der Betrag verwendet; vorhandene dBW/dBm/dBu-Werte werden entsprechend umgerechnet. | dBm(1mW) | 0dBm |
| [fromdBm](func/funktionen-zu-einheiten/fromdbm-gross-5/index.md) | Wandelt einen dBm-Wert in eine Leistung zurück. Ein einheitenloser Zahlenwert wird als dBm interpretiert und als Leistung in mW zurückgegeben. | fromdBm(0) | 1mW |
| [dBu](func/funktionen-zu-einheiten/dbu-gross-1/index.md) | Wandelt eine Leistung in den in LeTTo verwendeten dBu-Pegel mit Bezugsleistung 1 µW um: `10*log10(P/1uW)`. **Hinweis:** Dies ist die LeTTo-Definition von dBu und nicht die übliche Spannungsdefinition bezogen auf 0,775 V. | dBu(1uW) | 0dBu |
| [fromdBu](func/funktionen-zu-einheiten/fromdbu-gross-5/index.md) | Wandelt einen LeTTo-dBu-Wert in eine Leistung zurück. Ein einheitenloser Zahlenwert wird als dBu interpretiert und als Leistung in µW zurückgegeben. | fromdBu(0) | 1uW |
| [dBV](func/funktionen-zu-einheiten/dbv-gross-1-2/index.md) | Wandelt eine Spannung in dBV um. Bezugsspannung ist 1 V: `20*log10(U/1V)`. Bei komplexen Spannungen wird der Betrag verwendet; vorhandene dBV/dBmV/dBuV-Werte werden entsprechend umgerechnet. | dBV(1V) | 0dBV |
| [fromdBV](func/funktionen-zu-einheiten/fromdbv-gross-5-6/index.md) | Wandelt einen dBV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBV interpretiert und als Spannung in V zurückgegeben. | fromdBV(0) | 1V |
| [dBmV](func/funktionen-zu-einheiten/dbmv-gross-1-3/index.md) | Wandelt eine Spannung in dBmV um. Bezugsspannung ist 1 mV: `20*log10(U/1mV)`. Bei komplexen Spannungen wird der Betrag verwendet. | dBmV(1mV) | 0dBmV |
| [fromdBmV](func/funktionen-zu-einheiten/fromdbmv-gross-5-7/index.md) | Wandelt einen dBmV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBmV interpretiert und als Spannung in mV zurückgegeben. | fromdBmV(0) | 1mV |
| [dBuV](func/funktionen-zu-einheiten/dbuv-gross-1-3/index.md) | Wandelt eine Spannung in dBuV um. Bezugsspannung ist 1 µV: `20*log10(U/1uV)`. Bei komplexen Spannungen wird der Betrag verwendet. | dBuV(1uV) | 0dBuV |
| [fromdBuV](func/funktionen-zu-einheiten/fromdbuv-gross-5-7/index.md) | Wandelt einen dBuV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBuV interpretiert und als Spannung in µV zurückgegeben. | fromdBuV(0) | 1uV |


#### arithmetische Funktionen

| Funktion | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Beispiel                                       | Ergebnis             |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------------|
| [cround](func/arithmetische-funktionen/cround/index.md) | Rundet die Zahl kaufmännisch, der zweite Parameter gibt die Anzahl der Kommastellen an, ohne 2.Parameter wird auf Ganzzahlen gerundet, bei komplexen Zahlen wird Betrag und Winkel in Grad gerundet. [DEMO-Beispiel](../../demobsp.html?id=3220) | cround(23.535,2)<br>cround(2.435arg34.5364°,1) | 23.54<br>2.4arg34.5° |
| [ccround](func/arithmetische-funktionen/ccround/index.md) | Rundet die Zahl kaufmännisch, der zweite Parameter gibt die Anzahl der Kommastellen an, bei komplexe Zahlen wird Real und Imaginärteil gerundet. [DEMO-Beispiel](../../demobsp.html?id=3221) | ccround(2.4534+5.645*%i,2) | 2.45+5.65i |
| [round](func/arithmetische-funktionen/round/index.md) | Rundet die Zahl kaufmännisch, aus Kompatibilitätsgründen zu Maxima hat round nur einen Parameter [DEMO-Beispiel](../../demobsp.html?id=3222) | round(23.535) | 24 |
| [ground](func/arithmetische-funktionen/ground/index.md) | Rundet die Zahl auf die im zweiten Parameter angegebenen gültigen Ziffern [DEMO-Beispiel](../../demobsp.html?id=3223) | ground(2453.43,2) | 2500 |
| [floor](func/arithmetische-funktionen/floor/index.md) | Rundet auf die größte ganze Zahl, welche kleiner oder gleich x ist [DEMO-Beispiel](../../demobsp.html?id=3224) | floor(24.5) | 24 |
| [trunc](func/arithmetische-funktionen/trunc/index.md) | Schneidet die Zahl nach dem Komma ab [DEMO-Beispiel](../../demobsp.html?id=3226) | trunc(24.5) | 24 |
| [ceiling](func/arithmetische-funktionen/ceiling/index.md) | ceiling(x) Rundet auf die kleinste ganze Zahl, welche größer oder gleich x ist [DEMO-Beispiel](../../demobsp.html?id=3227) | ceiling(13.2) | 14 |
| [pow](func/arithmetische-funktionen/pow/index.md) | Potenzfunktion [DEMO-Beispiel](../../demobsp.html?id=3229) | pow(2,3) | 8 |
| [par](func/arithmetische-funktionen/par/index.md) | Parallelschaltung von Widerständen [DEMO-Beispiel](../../demobsp.html?id=3230) | par(x,y) | x*y/(x+y) |
| [min](func/arithmetische-funktionen/min/index.md) | Minimum von mehrere Werten suchen [DEMO-Beispiel](../../demobsp.html?id=3231) | min(3,5,1) | 1 |
| [max](func/arithmetische-funktionen/max/index.md) | Maximum von mehreren Werten suchen [DEMO-Beispiel](../../demobsp.html?id=3232) | max(3,5,1) | 5 |
| [random](func/arithmetische-funktionen/random/index.md) | Zufallszahl aus einem definierten Zahlenbereich random(minimal,maximal)<br>VORSICHT! Die Zufallszahl wird bei jedem Aufruf neu berechnet, weshalb sich der Wert bei jedem Anzeigevorgang einer Frage ändert. Sollte sich der berechnete Wert für eine Schülerangabe zwischen Fragestellung und Ergebniskontrolle nicht ändern dürfen (ist der Normalfall) muss man einen **Datensatz statt einer Zufallszahl** verwenden! <br> Zufallszahlen haben in der Ergebnisberechnung keinen Sinn, und sollten maximal für angezeigte zufällige Werte verwendet werden! [DEMO-Beispiel](../../demobsp.html?id=3244) | random(2,8) | 3.4532 |
| [randomC](func/arithmetische-funktionen/randomc-gross-6/index.md) | komplexe Zufallszahl aus einem definierten Zahlenbereich für den Betrag<br>VORSICHT! Die Zufallszahl wird bei jedem Aufruf neu berechnet! [DEMO-Beispiel](../../demobsp.html?id=3245) | randomC(2,8) | 3.4532arg40.3° |
| [signum](func/arithmetische-funktionen/signum/index.md) | Liefert das Vorzeichen einer Zahl (-1,0,1). Bei einer komplexen Zahl das Vorzeichen des Realteils. [DEMO-Beispiel](../../demobsp.html?id=3246) | signum(-4) | -1 |


####  Maxima-basierte Funktionen
* Diese Funktionen funktionieren nur wenn Maxima installiert ist und werden immer an Maxima gesendet, auch wenn der interne Parser aktiviert ist.
* Weiters werden sie bei der Ausgabe als TeX-Formel auch korrekt mit LaTeX gesetzt.

| Funktion  | Beschreibung                                                                                                                                                                                     | Beispiel                                   | Ergebnis       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|----------------|
| [integrate](func/maxima-basierte-funktionen/integrate/index.md) | Berechnet das unbestimmte oder bestimmte Integral einer Funktion. [DEMO-Beispiel](../../demobsp.html?id=3250) | integrate(x^2,x) <br> integrate(x^2,x,0,2) | x^3/3 <br> 8/3 |
| [diff](func/maxima-basierte-funktionen/diff/index.md) | Berechnet die Ableitung einer Funktion. [DEMO-Beispiel](../../demobsp.html?id=3251) | diff(x^2,x)<br>diff(3*x^2,x,2) | 2*x <br> 6 |
| [tomaxima](func/maxima-basierte-funktionen/tomaxima/index.md) | Führt die Berechnung aller Parameter von links nach rechts hintereinander mit Maxima aus. Das Ergebnis ist dann das Ergebnis des letzten Parameters. [DEMO-Beispiel](../../demobsp.html?id=3263) | tomaxima(y:x^2,y+2) | x^2+2 |
| [laplace](func/maxima-basierte-funktionen/laplace/index.md) | Bestimmt die Laplace-Transformierte einer Funktion. [DEMO-Beispiel](../../demobsp.html?id=3264) | laplace(sin(t),t,s) | 1/(1+s^2) |
| [ilt](func/maxima-basierte-funktionen/ilt/index.md) | Bestimmt die inverse Laplace-Transformierte eine Laplace-Funktion [DEMO-Beispiel](../../demobsp.html?id=3265) | ilt(1/(1+s),s,t) | e^(-t) |
| [sum](func/maxima-basierte-funktionen/sum/index.md) | Summenbildung [DEMO-Beispiel](../../demobsp.html?id=3266) | sum(1/k,k,1,2) | 3/2 |
| [product](func/maxima-basierte-funktionen/product/index.md) | Produktbildung [DEMO-Beispiel](../../demobsp.html?id=3267) | product(1/k,k,1,3) | 1/6 |


#### erweiterte arithmetische Funktionen

| Funktion                             | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                | Beispiel                                                                            | Ergebnis                                                                                                                                                     |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [sigma](func/erweiterte-arithmetische-funktionen/sigma/index.md) | Sprungfunktion: sigma(x) liefert 0 für x&lt;0 und 1 für x&gt;=0 [DEMO-Beispiel](../../demobsp.html?id=3268) | sigma(243.3) | 1 |
| [pulse](func/erweiterte-arithmetische-funktionen/pulse/index.md) | Rechteckfunktion: <br>pulse(x,x0) ist gleich 1 für x0 &lt;= x &lt;= x0 + 1, sonst 0<br>pulse(x,x0,L) ist gleich 1 für x0 &lt;= x &lt;= x0 + L, sonst 0<br>![300px-Pulse.png](300px-Pulse.png) [DEMO-Beispiel](../../demobsp.html?id=3269) | pulse(x,2,4) | ![100px-pulse_x_2_4.png](100px-pulse_x_2_4.png) |
| [ramp](func/erweiterte-arithmetische-funktionen/ramp/index.md) | Rampenfunktion: <br>ramp(x,x0) Rampe von x0 &lt; x &lt; x0 + 1<br>ramp(x,x0,L) Rampe von x0 &lt; x &lt; x0 + L<br>![300px-Funktion_ramp.png](300px-Funktion_ramp.png) [DEMO-Beispiel](../../demobsp.html?id=3270) | ramp(x,2,4) | ![100px-Ramp_Plot.png](100px-Ramp_Plot.png) |
| [interpol](func/erweiterte-arithmetische-funktionen/interpol/index.md) | Interpolationsfunktion zwischen mehreren Stützpunkten in einem Koordinatensystem. <br> interpol(WerteX,WerteY,x) [DEMO-Beispiel](../../demobsp.html?id=3272) | interpol(&#91;0,1,2&#93;,&#91;0,3,3&#93;,1.5) | 3 |
| [interpol](func/erweiterte-arithmetische-funktionen/interpol/index.md)(pv,wert) | Interpoliert Zwischenwerte durch lineare Interpolation in einer als PV-Vektor gegebenen Tabelle [DEMO-Beispiel](../../demobsp.html?id=3273) | interpol(&#91;&#91;0,0&#93;,&#91;1,2&#93;,&#91;2,2.2&#93;,&#91;3,1.4&#93;&#93;,1.5) | 2.1 |
| [periodic](func/erweiterte-arithmetische-funktionen/periodic/index.md) | Erzeugt aus einer beliebigen Funktion zwischen 0 und Periodendauer eine periodische Funktion <br> periodic(Variable,Periodendauer,Funktion)<br> periodic(Variable,Periodendauer,Funktionsperiodendauer,Funktion) [DEMO-Beispiel](../../demobsp.html?id=3274) | ch1(t):periodic(t,5ms,2'Vms-2'*t^2) <br> ch1(t):periodic(t,5ms,1,2V*t^2) | <br>![100px-ClipCapIt-190318-113524.PNG](100px-ClipCapIt-190318-113524.PNG) <br> <br>![100px-ClipCapIt-190318-113644.PNG](100px-ClipCapIt-190318-113644.PNG) |
| [numint](func/erweiterte-arithmetische-funktionen/numint/index.md) | numerische Integration <br> numint(untereGrenze,obereGrenze,funktion,Variable)<br> numint(untereGrenze,obereGrenze,funktion,Variable,punkteAnzahl) [DEMO-Beispiel](../../demobsp.html?id=3275) | numint(0,2pi,sin(t),t) | 0 |
| [numdif](func/erweiterte-arithmetische-funktionen/numdif/index.md) | numerisches Differenzieren einer Funktion "funktion" nach einer Variablen "Variable" an der Stelle "position" mit einer Differenz der Variablen von "differenz" <br> numdif(position,funktion,Variable,differenz) [DEMO-Beispiel](../../demobsp.html?id=3276) | numdif(0,sin(t),t,0.01) | 1 |
| [solve](func/erweiterte-arithmetische-funktionen/solve/index.md) | löst eine Gleichung oder ein Gleichungssystem nach einer oder mehrerer Variablen [DEMO-Beispiel](../../demobsp.html?id=3277) | solve(&#91;2*x+y=3,x-y=0&#93;,&#91;x,y&#93;) | &#91;&#91; x=1,y=1 &#93;&#93; |
| [solvevalue](func/erweiterte-arithmetische-funktionen/solvevalue/index.md) | löst eine Gleichung oder ein Gleichungssystem nach einer Variablen und liefert genau die erste Lösung wenn sie numerisch berechenbar ist [DEMO-Beispiel](../../demobsp.html?id=3278) | solvevalue(&#91; 2*x+y=3,x-y=0 &#93;,&#91; x,y &#93;,x) | 1 |
| [newton](func/erweiterte-arithmetische-funktionen/newton/index.md) | Bestimmt eine Nullstelle einer Funktion nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der Startwert. [DEMO-Beispiel](../../demobsp.html?id=3279) | newton(x^2-4,4) | 2 |
| [cnewton](func/erweiterte-arithmetische-funktionen/cnewton/index.md) | Bestimmt eine komplexe Nullstelle einer Funktion nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der komplexe Startwert. [DEMO-Beispiel](../../demobsp.html?id=3280) | cnewton (x^2+4,4) | 2*%i |
| [newtonall](func/erweiterte-arithmetische-funktionen/newtonall/index.md) | Bestimmt alle Nullstellen einer Funktion mit einem Betrag des Funktionsparameters kleiner als ein definierter Wert nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der maximale Betrag des Funktionsparameters. Das Ergebnis ist immer ein Vektor mit den nach aufsteigendem Funktionswert sortierten Nullstellen. [DEMO-Beispiel](../../demobsp.html?id=3281) | newtonall (x^2-4,4) | &#91;-2,2&#93; |
| [cnewtonall](func/erweiterte-arithmetische-funktionen/cnewtonall/index.md) | Bestimmt alle komplexen Nullstellen einer Funktion mit einem Betrag des Funktionsparameters kleiner als ein definierter Wert nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der maximale Betrag des Funktionsparameters. Das Ergebnis ist immer ein Vektor mit den Nullstellen. [DEMO-Beispiel](../../demobsp.html?id=3282) | cnewtonall (x^2+4,4) | &#91;-2*%i,2*%i&#93; |


####  Gleichungen und Gleichungssysteme

| Funktion | Beschreibung                                                                                                                                                               | Beispiel                                                                                                                     | Ergebnis                                            | ab Revision |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|-------------|
| [solve](func/erweiterte-arithmetische-funktionen/solve/index.md) | löst eine Gleichung oder ein Gleichungssystem nach einer oder mehrerer Variablen [DEMO-Beispiel](../../demobsp.html?id=3283) | solve(&#91;2*x+y=3,x-y=0&#93;,&#91;x,y&#93;) | &#91;&#91; x=1,y=1 &#93;&#93; |  |
| [lhs](func/gleichungen-und-gleichungssysteme/lhs/index.md) | liefert die linke Seite einer Gleichung, Ungleichung oder eines Infix Operators [DEMO-Beispiel](../../demobsp.html?id=3284) | lhs(x+y=c+2) | x+y | 6521 |
| [rhs](func/gleichungen-und-gleichungssysteme/rhs/index.md) | liefert die rechte Seite einer Gleichung, Ungleichung oder eines Infix Operators [DEMO-Beispiel](../../demobsp.html?id=3285) | rhs(x+y=c+2) | c+2 | 6521 |
| [onlypos](func/gleichungen-und-gleichungssysteme/onlypos/index.md) | liefert aus dem Lösungsvektor von solve welcher aus lauter Gleichungen besteht nur die Lösungen welche positiv nicht Null sind [DEMO-Beispiel](../../demobsp.html?id=3286) | onlypos(&#91;&#91;x=3,y=-3&#93;,&#91;x=4,y=5&#93;,&#91;x=-2,y=4&#93;&#93;) <br> onlypos(&#91;x=-2,x=0,x=6,x=8&#93;) | &#91;&#91;x=4,y=5&#93;&#93; <br> &#91;x=7,x=8&#93; | 6522 |
| [onlyreal](func/gleichungen-und-gleichungssysteme/onlyreal/index.md) | liefert aus dem Lösungsvektor von solve welcher aus lauter Gleichungen besteht nur die Lösungen welche reell sind [DEMO-Beispiel](../../demobsp.html?id=3287) | onlyreal(&#91;&#91;x=1,y=%i&#93;,&#91;x=1,y=-%i&#93;,&#91;x=3,y=4&#93;&#93;) <br> onlyreal(&#91;x=%i+1,x=1-%i,x=3,x=8&#93;) | &#91;&#91;x=3,y=4&#93;&#93; <br> &#91;x=3,x=8&#93; | 6522 |


#### Stringfunktionen

| Funktion               | Beschreibung                                                                                                                                                                      | Beispiel                                     | Ergebnis    |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|-------------|
| [dechex](func/funktionen-fuer-ganzzahlen/dechex/index.md) | Zahl in eine Ganzzahl wandeln und als Hexadezimal-String ausgeben [DEMO-Beispiel](../../demobsp.html?id=3288) | dexhex(12) | "0xC" |
| [chr](func/stringfunktionen/chr/index.md) | Bestimmt die Zeichen mit dem ASC-II-Code der Long-Parameter und setzt daraus einen String zusammen. [DEMO-Beispiel](../../demobsp.html?id=3289) | chr(0x65,105) | "ei" |
| [val](func/stringfunktionen/val/index.md) | Bestimmt den ASC-II-Code des ersten Zeichens welches als String-Parameter übergeben wurde. [DEMO-Beispiel](../../demobsp.html?id=3290) | val("a") | 97 |
| [strcat](func/stringfunktionen/strcat/index.md) | Fügt mehrere Strings zusammen. [DEMO-Beispiel](../../demobsp.html?id=3291) | strcat("a","b") | "ab" |
| [string](func/stringfunktionen/string/index.md) | Wandelt eine Zahl in einen String um. | string(123) | "123" |
| [parse](func/stringfunktionen/parse/index.md) | Wenn der Parameter ein String ist wird dieser String mit dem Parser interpretiert [DEMO-Beispiel](../../demobsp.html?id=3482) | parse("2+3") | 5 |
| [substring](func/stringfunktionen/substring/index.md) | Liefert einen Teil eines Strings substring(string,startindex,endindex). Index beginnt bei 0 und endindex ist optional.  [DEMO-Beispiel](../../demobsp.html?id=5025) | substring("abcdefg",2,3) | "cd" |
| [tailstring](func/stringfunktionen/tailstring/index.md) | liefert den letzten Teil eines Strings teilstring(tailstring,zeichenanzahl) [DEMO-Beispiel](../../demobsp.html?id=5026) | tailstring("abcdefg",2) | "fg" |
| [replacestring](func/stringfunktionen/replacestring/index.md) | Ersetzt alle Vorkommen einer Zeichenkette in einem String durch eine andere Zeichenkette. [DEMO-Beispiel](../../demobsp.html?id=5027) | replacestring("abcdefg","bc","xy") | "axydefg" |
| [replaceallstring](func/stringfunktionen/replaceallstring/index.md) | Ersetzt alle Vorkommen einer Zeichenkette ([regulärer Ausdruck](../RegularExpression/index.md)) durch eine andere Zeichenkette.  [DEMO-Beispiel](../../demobsp.html?id=5027) | replaceallstring("abcdefg","b.*e","xy") | "axyfg" |
| [replacefirststring](func/stringfunktionen/replacefirststring/index.md) | Ersetzt das erste Vorkommen einer Zeichenkette ([regulärer Ausdruck](../RegularExpression/index.md)) durch eine andere Zeichenkette. [DEMO-Beispiel](../../demobsp.html?id=5027) | replacefirststring("abcdefg","b.*e","xy") | "axyfg" |
| [splitstring](func/stringfunktionen/splitstring/index.md) | Teilt einen String in ein Array von Strings splitstring(string,separator) [DEMO-Beispiel](../../demobsp.html?id=5028) | splitstring("abcdefg","b") | "a","c","defg" |
| [matchstring](func/stringfunktionen/matchstring/index.md) | Prüft ob eine String einem [regulären Ausdruck](../RegularExpression/index.md) entspricht.  [DEMO-Beispiel](../../demobsp.html?id=5029) | matchstring("abcdefg","b.*e") | true |

#### trigonometrische Funktionen

| Funktion                             | Beschreibung                                                                                                                                   | Beispiel         | Ergebnis                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------|---------------------------------------|
| [sin](func/trigonometrische-funktionen/sin/index.md) | Sinus [DEMO-Beispiel](../../demobsp.html?id=3292) | sin(%pi/2) | 1 |
| [cos](func/trigonometrische-funktionen/cos/index.md) | Cosinus [DEMO-Beispiel](../../demobsp.html?id=3302) | cos(%pi/2) | 0 |
| [tan](func/trigonometrische-funktionen/tan/index.md) | Tangens [DEMO-Beispiel](../../demobsp.html?id=3303) | tan(%pi/4) | 1 |
| [cot](func/trigonometrische-funktionen/cot/index.md) | Cotangens, `cot(x)=1/tan(x)`. | cot(%pi/4) | 1 |
| [asin](func/trigonometrische-funktionen/asin/index.md) | Arcus-Sinus [DEMO-Beispiel](../../demobsp.html?id=3304) | asin(1) | %pi/2 |
| [arcsin](func/trigonometrische-funktionen/arcsin/index.md) | Arcus-Sinus [DEMO-Beispiel](../../demobsp.html?id=3305) | asin(1) | %pi/2 |
| [acos](func/trigonometrische-funktionen/acos/index.md) | Arcus-Cosinus [DEMO-Beispiel](../../demobsp.html?id=3306) | acos(1) | 0 |
| [arccos](func/trigonometrische-funktionen/arccos/index.md) | Arcus-Cosinus [DEMO-Beispiel](../../demobsp.html?id=3307) | acos(1) | 0 |
| [atan](func/trigonometrische-funktionen/atan/index.md) | Arcus-Tangens [DEMO-Beispiel](../../demobsp.html?id=3308) | atan(1) | %pi/4 |
| [arctan](func/trigonometrische-funktionen/arctan/index.md) | Arcus-Tangens [DEMO-Beispiel](../../demobsp.html?id=3309) | arctan(1) | %pi/4 |
| [acot](func/trigonometrische-funktionen/acot/index.md) | Arcus-Cotangens. | acot(1) | %pi/4 |
| [arccot](func/trigonometrische-funktionen/arccot/index.md) | Alias zu `acot`: Arcus-Cotangens. | arccot(1) | %pi/4 |
| [atan2](func/trigonometrische-funktionen/atan2/index.md) | Arcus-Tangens atan2(y,x)=arctan(y/x) [DEMO-Beispiel](../../demobsp.html?id=3310) | atan2(-2,-2) | -%pi*3/4 |
| [arctan2](func/trigonometrische-funktionen/arctan2/index.md) | Arcus-Tangens arctan2(y,x)=arctan(y/x) [DEMO-Beispiel](../../demobsp.html?id=3311) | arctan2(-2,-2) | -%pi*3/4 |
| [sinh](func/trigonometrische-funktionen/sinh/index.md) | Sinus-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3312) | sinh(1) | 1.1752012 |
| [cosh](func/trigonometrische-funktionen/cosh/index.md) | Cosinus-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3313) | cosh(1) | 1.5430806 |
| [tanh](func/trigonometrische-funktionen/tanh/index.md) | Tangens-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3314) | tanh(1) | 0.7615941 |
| [coth](func/trigonometrische-funktionen/coth/index.md) | Cotangens-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3315) | coth(1) | 1.313035 |
| [sec](func/trigonometrische-funktionen/sec/index.md) | Secans, `sec(x)=1/cos(x)`. | sec(0) | 1 |
| [csc](func/trigonometrische-funktionen/csc/index.md) | Kosecans, `csc(x)=1/sin(x)`. | csc(%pi/2) | 1 |
| [sech](func/trigonometrische-funktionen/sech/index.md) | Secans-Hyperbolicus, `sech(x)=1/cosh(x)`. | sech(0) | 1 |
| [csch](func/trigonometrische-funktionen/csch/index.md) | Kosecans-Hyperbolicus, `csch(x)=1/sinh(x)`. | csch(1) | 0.850918... |
| [asinh](func/trigonometrische-funktionen/asinh/index.md) | Area-Sinus-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3316) | asinh(1.1752012) | 1 |
| [acosh](func/trigonometrische-funktionen/acosh/index.md) | Area-Cosinus-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3317) | acosh(1.5430806) | 1 |
| [atanh](func/trigonometrische-funktionen/atanh/index.md) | Area-Tangens-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3318) | atanh(0.7615941) | 1 |
| [acoth](func/trigonometrische-funktionen/acoth/index.md) | Area-Cotangens-Hyperbolicus [DEMO-Beispiel](../../demobsp.html?id=3319) | acoth(1.313035) | 1 |
| [asec](func/trigonometrische-funktionen/asec/index.md) | Arcus-Secans, inverse Funktion zu `sec`. | asec(2) | %pi/3 |
| [acsc](func/trigonometrische-funktionen/acsc/index.md) | Arcus-Kosekans, inverse Funktion zu `csc`. | acsc(2) | %pi/6 |
| [asech](func/trigonometrische-funktionen/asech/index.md) | Area-Secans-Hyperbolicus, inverse Funktion zu `sech`. | asech(1) | 0 |
| [acsch](func/trigonometrische-funktionen/acsch/index.md) | Area-Kosekans-Hyperbolicus, inverse Funktion zu `csch`. | acsch(1) | 0.881373... |
| [csin](func/trigonometrische-funktionen/csin/index.md) | Erzeugt aus einer komplexen Zahl (Effektivwert) und einer Frequenz einen Sinusfunktion in der Zeit [DEMO-Beispiel](../../demobsp.html?id=3320) | csin(U) | sqrt(2)*cabs(U)*sin(2*pi*f*t+carg(U)) |
| [cssin](func/trigonometrische-funktionen/cssin/index.md) | Erzeugt aus einer komplexen Zahl, die als Spitzenwert interpretiert wird, eine Sinusfunktion. `cssin(U)`, `cssin(U,f)` oder `cssin(U,f,x)`. | cssin(U) | cabs(U)*sin(2*pi*f*t+carg(U)) |
| [quadrant](func/trigonometrische-funktionen/quadrant/index.md) | Liefert den Quadranten eines Winkels mit einer Toleranzangabe. [DEMO-Beispiel](../../demobsp.html?id=3321) | quadrant(20°,5°) | 1 |
| [argnorm](func/trigonometrische-funktionen/argnorm/index.md) | Wandelt einen Winkel auf den Bereich von 0°-360° [DEMO-Beispiel](../../demobsp.html?id=3322) | argnorm(-50°) | 310° |
| [pi](func/trigonometrische-funktionen/pi/index.md) | Funktionsschreibweise der Kreiszahl Pi. `pi()` hat keine Parameter und entspricht `%pi`. | pi() | %pi |


#### Exponentialfunktionen

| Funktion | Beschreibung                                                         | Beispiel   | Ergebnis |
|----------|----------------------------------------------------------------------|------------|----------|
| [pow](func/arithmetische-funktionen/pow/index.md) | Potenzfunktion [DEMO-Beispiel](../../demobsp.html?id=3324) | pow(2,3) | 8 |
| [sqrt](func/exponentialfunktionen/sqrt/index.md) | Quadratwurzel. Entspricht `root(x,2)`. | sqrt(9) | 3 |
| [root](func/exponentialfunktionen/root/index.md) | n-te Wurzel `root(x,n)`; ohne zweiten Parameter wird die Quadratwurzel verwendet. | root(8,3) | 2 |
| [exp](func/exponentialfunktionen/exp/index.md) | Exponentialfunktion [DEMO-Beispiel](../../demobsp.html?id=3325) | exp(1) | %e |
| [log](func/exponentialfunktionen/log/index.md) | natürlicher Logarythmus [DEMO-Beispiel](../../demobsp.html?id=3326) | log(%e) | 1 |
| [ln](func/exponentialfunktionen/ln/index.md) | natürlicher Logarythmus [DEMO-Beispiel](../../demobsp.html?id=3327) | ln(%e) | 1 |
| [log10](func/exponentialfunktionen/log10/index.md) | Logarythmus zur Basis 10 [DEMO-Beispiel](../../demobsp.html?id=3328) | log10(100) | 2 |


#### komplexe Zahlen
Die Funktionen zu komplexen Zahlen werden (anders als in Maxima) nur ausgewertet wenn das Ergebnis numerisch berechenbar ist, ansonsten bleibt die Funktion symbolisch erhalten.

| Funktion  | Beschreibung                                                                                                                                             | Beispiel                  | Ergebnis |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------|
| [abs](func/komplexe-zahlen/abs/index.md) | Liefert den Absolutbetrag einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3329) | abs(3+4*%i) | 5 |
| [cabs](func/komplexe-zahlen/cabs/index.md) | Liefert den Absolutbetrag einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3330) | cabs(3+4*%i) | 5 |
| [cAbs](func/komplexe-zahlen/cabs-gross-1/index.md) | Kompatibilitätsalias zu `cabs`. | cAbs(3+4*%i) | 5 |
| [carg](func/komplexe-zahlen/carg/index.md) | Liefert das Argument einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3331) | carg(4*%e^(3*%i)) | 3 |
| [cArg](func/komplexe-zahlen/carg-gross-1/index.md) | Kompatibilitätsalias zu `carg`. | cArg(4*%e^(3*%i)) | 3 |
| [realpart](func/komplexe-zahlen/realpart/index.md) | Liefert den Realteil einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3332) | realpart(3+4*%i) | 3 |
| [cRe](func/komplexe-zahlen/cre-gross-1/index.md) | Kompatibilitätsalias zu `realpart`. | cRe(3+4*%i) | 3 |
| [imagpart](func/komplexe-zahlen/imagpart/index.md) | Liefert den Imaginärteil einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3333) | imagpart(3+4*%i) | 4 |
| [cIm](func/komplexe-zahlen/cim-gross-1/index.md) | Kompatibilitätsalias zu `imagpart`. | cIm(3+4*%i) | 4 |
| [conjugate](func/komplexe-zahlen/conjugate/index.md) | Liefert die konjugiert komplexe Zahl einer komplexen Zahl [DEMO-Beispiel](../../demobsp.html?id=3334) | conjugate(3+4*%i) | 3-4*%i |
| [cConjugate](func/komplexe-zahlen/cconjugate-gross-1/index.md) | Kompatibilitätsalias zu `conjugate`. | cConjugate(3+4*%i) | 3-4*%i |
| [rectform](func/komplexe-zahlen/rectform/index.md) | hat in LeTTo keine Relevanz, da die Zahlendarstellung bei der Ausgabe definiert wird wie zB.: {=3arg2;karti} [DEMO-Beispiel](../../demobsp.html?id=3335) |  |  |
| [cRectform](func/komplexe-zahlen/crectform-gross-1/index.md) | Kompatibilitätsalias zu `rectform`. |  |  |
| [pol](func/komplexe-zahlen/pol/index.md) | erzeugt aus Betrag und Argument eine komplexe Zahl [DEMO-Beispiel](../../demobsp.html?id=3336) | pol(5,0.9272952180016122) | 3+4*%i |
| [polgrad](func/komplexe-zahlen/polgrad/index.md) | Erzeugt aus Betrag und einem Winkel im Gradmaß eine komplexe Zahl. | polgrad(5,53.130102°/1°) | 3+4*%i |

#### Polynome
Polynome mit reellen Koeffizienten in einer Variablen können mit folgenden Funktionen erstellt und verarbeitet werden. Für die interne Verarbeitung wird hierzu ein eigener Polynom-Datentyp verwendet.

siehe auch [Zahlendarstellung Polynome](../Zahlendarstellung/index.md#für-polynome-und-gebrochen-rationale-funktionen-mit-numerischen-koeffizienten-in-einer-variablen-können-folgende-parameter-angegeben-werden)

| Funktion                                           | Beschreibung                                                                                                                                                                                                                                                           | Beispiel                                                          | Ergebnis                                         |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------|
| [polynom](func/polynome/polynom/index.md)(p) | Erzeugt aus einem Ausdruck welcher genau eine Variable besitzen muss ein Polynom in dieser Variablen [DEMO-Beispiel](../../demobsp.html?id=3337) | polynom(1+x) | 1+x² |
| [polynom](func/polynome/polynom/index.md)(p,var) | Erzeugt aus einem Ausdruck ein Polynom in einer definierten Variablen. Ist p ein gültiger Polynom-Ausdruck mit reelen Koeffizienten in der Variablen var wird das Polynom erzeugt, ansonsten bleibt die Funktion erhalten. [DEMO-Beispiel](../../demobsp.html?id=3338) | polynom(1+a*x^2,x) <br> polynom(1+2*x^2,x) | polynom(1+a*x^2,x)<br>1+2*x² |
| [polynom](func/polynome/polynom/index.md)(p,var,"einheit") | Erzeugt ein Polynom in der Variablen var, mit der Einheit "einheit" für die Polynomvariable. Die Einheit muss als String in Doppelhochkomma angegeben werden! Das Polynom p muss entweder ohne Einheiten oder mit den korrekten Einheiten angegeben werden! | polynom(1+2*p^2,p,"s-1") <br> polynom(1+2's2'*p^2,p,"s-1") | 1+2's2'*p^2 <br>1+2's2'*p^2 |
| [factfrompolynom](func/polynome/factfrompolynom/index.md)(p) | Erzeugt aus einem Polynom einen Vektor mit den Polynomfaktoren. Erste Zeile Zählerfaktoren, zweite Zeile Nennerfaktoren, dritte Zeile Polynomvariable, vierte Zeile Einheit der Polynomvariable | factfrompolynom(polynom((2+x)/(1+2*x))) | &#91;&#91;1,0.5&#93;,&#91;0.5,1&#93;,"x",""&#93; |
| [polynomfromfact](func/polynome/polynomfromfact/index.md)(f) | Erzeugt aus einer Faktoren-Liste, welche mit factfrompolynom erstellt wurde ein neues Polynom | polynomfromfact(&#91;&#91;1,0.5&#93;,&#91;0.5,1&#93;,"x",""&#93;) | (2+x)/(1+2*x) |
| [polynomfromfact](func/polynome/polynomfromfact/index.md)(zähler,nenner,var,einheit) | Erzeugt aus Zähler und Nenner Faktor-Vektoren ein neues Polynom | polynomfromfact(&#91;1,0.5&#93;,&#91;0.5,1&#93;,x,"") | (2+x)/(1+2*x) |
| [nullfrompolynom](func/polynome/nullfrompolynom/index.md)(p) | Erzeugt aus einem Polynom einen Vektor mit den PolynomNullstellen und Polstellen. Erste Zeile gemeinsamer Faktor, zweite Zeile Nullstellen, dritte Zeile Polstellen, vierte Zeile Polynomvariable | nullfrompolynom(polynom((2+x)/(1+2*x))) | &#91;0.5,&#91;-2&#93;,&#91;-0.5&#93;,x&#93; |
| [polynomfromnull](func/polynome/polynomfromnull/index.md)(n) | Erzeugt aus einer Nullstellen-Polstellen-Liste, welche mit nullfrompolynom erstellt wurde ein neues Polynom | polynomfromnull(&#91;0.5,&#91;-2&#93;,&#91;-0.5&#93;,x&#93;) | (2+x)/(1+2*x) |
| [polynomfromnull](func/polynome/polynomfromnull/index.md)(faktor,nullstellen,polstellen,var) | Erzeugt aus einer Faktor-Vektoren ein neues Polynom | polynomfromnull(0.5,&#91;-2&#93;,&#91;-0.5&#93;,x) | (2+x)/(1+2*x) |
| [polynomk](func/polynome/polynomk/index.md)(p) | Bestimmt den Faktor, welcher vom Polynom herausgehoben werden kann, so dass die höchste Potenz der Polynomvariable den Multiplikator Eins hat. | polynomk(polynom((2+x)/(1+2*x))) | 0.5 |
| [ispolynom](func/polynome/ispolynom/index.md)(p) | Prüft, ob der Ausdruck ein Polynom ist. Die Funktion wird ausgewertet, sobald der Parameter als Polynom erkannt bzw. nicht als Polynom erkannt werden kann. | ispolynom(polynom(x^2+1)) | true |
| [getvars](func/polynome/getvars/index.md)(ausdruck) | Liefert alle im Ausdruck vorkommenden Variablennamen als Vektor von Strings. | getvars(x^2+a*y) | &#91;"a","x","y"&#93; |


#### statistische Funktionen
Die Funktionen funktionieren nur ohne Einheiten.

| Funktion  | Beschreibung                                                                                                   | Beispiel      | Ergebnis |
|-----------|----------------------------------------------------------------------------------------------------------------|---------------|----------|
| [factorial](func/statistische-funktionen/factorial/index.md) | Liefert die Fakultät einer positiven ganzen Zahl [DEMO-Beispiel](../../demobsp.html?id=3339) | factorial(5) | 120 |
| [binomial](func/statistische-funktionen/binomial/index.md) | Liefert den Binomialkoeffizienten von zwei positiven ganzen Zahlen [DEMO-Beispiel](../../demobsp.html?id=3340) | binomial(5,2) | 10 |


#### Mengen-Funktionen
Mengen werden intern als Vektoren verarbeitet und sind deshalb auch direkt durch Vektoren ersetzbar. Auch alle Vektor-Funktionen sind somit auch auf Mengen anwendbar und umgekehrt.

| Funktion         | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Beispiel                                                                                                                                                                                           | Ergebnis                                                          | ab Rev |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|--------|
| [setget](func/mengen-funktionen/setget/index.md) | Liefert ein Element einer Menge oder einer Matrix (Menge von Mengen) [DEMO-Beispiel](../../demobsp.html?id=3341) | setget(&#91;12,13,14&#93;,1) <br> setget(matrix([9,2&#93;,[3,4&#93;),0,1) | 13 <br> 2 |  |
| [setset](func/mengen-funktionen/setset/index.md) | setzt ein Element einer Menge oder einer Matrix (Menge von Mengen) [DEMO-Beispiel](../../demobsp.html?id=3342) | setset(&#91;12,13,14&#93;,1,35) <br> setset(matrix([9,2&#93;,[3,4&#93;),0,0,-9) | &#91;12,35,14&#93; <br> &#91;&#91;-9,2&#93;,&#91;3,4&#93;&#93; |  |
| [setlength](func/mengen-funktionen/setlength/index.md) | liefert die Anzahl der Elemente einer Liste, Menge oder eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3343) | setlength(&#91;3,6,54,34,3,54&#93;) | 6 |  |
| [setinsert](func/mengen-funktionen/setinsert/index.md) | fügt ein Element in eine Menge an eine gegebene Stelle ein [DEMO-Beispiel](../../demobsp.html?id=3344) | setinsert(&#91;12,13,14&#93;,1,25) | &#91;12,25,13,14&#93; |  |
| [setremove](func/mengen-funktionen/setremove/index.md) | löscht ein Element einer Menge [DEMO-Beispiel](../../demobsp.html?id=3346) | setremove(&#91;12,13,14&#93;,1) | &#91;12,14&#93; |  |
| [setapply](func/mengen-funktionen/setapply/index.md) | wendet einen Ausdruck oder Funktion auf alle Elemente einer Menge an [DEMO-Beispiel](../../demobsp.html?id=3347) | setapply(y,&#91;1,2,3&#93;,y*2) | &#91;2,4,6&#93; | 5965 |
| [setmedian](func/mengen-funktionen/setmedian/index.md) | Liefert den Median einer Menge [DEMO-Beispiel](../../demobsp.html?id=3348) | setmedian(&#91;4,3,1,5,6&#93; | 4 |  |
| [setboxplot](func/mengen-funktionen/setboxplot/index.md) | Liefert die Werte des Boxplot einer Menge (Minimum, unteres Quartil, Median, oberes Quartil, Maximum) als Vektor verwendbar für das [Plot-Plugin#definierte-zeichenelemente-](../Plot#definierte-zeichenelemente-/index.md#definierte-zeichenelemente-) [DEMO-Beispiel](../../demobsp.html?id=3349) | setboxplot(&#91;1,2,3,10,8,9&#93; | &#91;1,2,5.5,9,10&#93; |  |
| [setsort](func/mengen-funktionen/setsort/index.md) | Sortiert die Elemente einer Menge aufsteigend [DEMO-Beispiel](../../demobsp.html?id=3350) | setsort(&#91;3,-3,2,0,5,2&#93;) | &#91;-3,0,2,2,3,5&#93; |  |
| [setsortnd](func/mengen-funktionen/setsortnd/index.md) | Sortiert die Elemente einer Menge aufsteigend und entfernt alle mehrfach vorkommenden Elemente [DEMO-Beispiel](../../demobsp.html?id=3351) | setsortnd(&#91;31,-3,2,31,0,5,2&#93;) | &#91;-3,0,2,5,31&#93; |  |
| [setcount](func/mengen-funktionen/setcount/index.md) | Bestimmt die Anzahl wie oft ein Element in einer Menge vorkommt oder die Anzahl der Elemente der Menge [DEMO-Beispiel](../../demobsp.html?id=3352) | setcount(&#91;31,-3,2,31,0,5,2&#93;,31) <br> setcount(&#91;2,5,3,6&#93;) | 2 <br> 4 |  |
| [setmodus](func/mengen-funktionen/setmodus/index.md) | Liefert das Element einer Menge, welches am öftesten vorkommt oder die Elemente als Menge wenn mehrere Elemente gleich oft vorkommen [DEMO-Beispiel](../../demobsp.html?id=3353) | setmodus(&#91;3,-3,2,0,5,2&#93;) | 2 |  |
| [setreverse](func/mengen-funktionen/setreverse/index.md) | Dreht die Reihenfolge einer Menge um [DEMO-Beispiel](../../demobsp.html?id=3354) | setreverse(&#91;3,-3,2,0,5,2&#93;) | &#91;2,5,0,2,-3,3&#93; |  |
| [reverse](func/mengen-funktionen/reverse/index.md) | Alias zu `setreverse`: Dreht die Reihenfolge eines Vektors/einer Menge um. | reverse(&#91;1,2,3&#93;) | &#91;3,2,1&#93; |  |
| [setnd](func/mengen-funktionen/setnd/index.md) | Löscht alle Duplikate aus der Menge [DEMO-Beispiel](../../demobsp.html?id=3355) | setnd(&#91;3,-3,2,0,5,2&#93;)) | &#91;3,-3,2,0,5&#93; |  |
| [setshuffle](func/mengen-funktionen/setshuffle/index.md) | Mischt eine Menge in eine andere Reihenfolge. VORSICHT, ohne zweiten Parameter (ganze Zahl) ändert sich die Reihenfolge bei jedem mal neu Laden automatisch und ist nicht nachvollziehbar, weshalb sie dann für Schülerbeispiele nicht einsetzbar ist! Daher ist es für eine praktische Anwendung in einem Schülerbeispiel **erforderlich**, dass der zweite Parameter determiniert (beispielsweise über einen Integer-Datensatz-Wert zwischen 0 und 1000) festgelegt wird. [DEMO-Beispiel](../../demobsp.html?id=3356) | setshuffle(&#91;3,-3,2,0,5,2&#93;,5) | &#91;2,3,−3,2,0,5&#93; | 6082 |
| [setmittel](func/mengen-funktionen/setmittel/index.md) | Bestimmt den Mittelwert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3357) | setmittel(&#91;1,3,2,4&#93;) | 2.5 |  |
| [setgeomittel](func/mengen-funktionen/setgeomittel/index.md) | Bestimmt das geometrische Mittelwert einer Menge aus positiven reellen Zahlen [DEMO-Beispiel](../../demobsp.html?id=3358) | setgeomittel(&#91;10,20,30&#93;) | 18.171206 |  |
| [setvarianz](func/mengen-funktionen/setvarianz/index.md) | Bestimmt die empirische Varianz einer Menge [DEMO-Beispiel](../../demobsp.html?id=3359) | setvarianz(&#91;3,1,2,5,4&#93;) | ((3-3)^2+(1-3)^2+(2-3)^2+(5-3)^2+(4-3)^2)/5=2 |  |
| [setquadratmittel](func/mengen-funktionen/setquadratmittel/index.md) | Bestimmt den quadratischen Mittelwert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3360) | setquadratmittel(&#91;10,20,30&#93;) | 21.6025 |  |
| [setsum](func/mengen-funktionen/setsum/index.md) | Bestimmt die Summe aller Werte einer Menge [DEMO-Beispiel](../../demobsp.html?id=3361) | setsum(&#91;1,3,2,4&#93;) | 10 |  |
| [setprod](func/mengen-funktionen/setprod/index.md) | Bestimmt das Produkt aller Werte einer Menge [DEMO-Beispiel](../../demobsp.html?id=3363) | setprod(&#91;1,3,2,4&#93;) | 24 |  |
| [setunion](func/mengen-funktionen/setunion/index.md) | Fügt mehrere Mengen zu einer neuen Menge zusammen [DEMO-Beispiel](../../demobsp.html?id=3364) | setunion(&#91;1,3,2,4&#93;,[3,7&#93;) | &#91;1,3,2,4,3,7&#93; |  |
| [setunionnd](func/mengen-funktionen/setunionnd/index.md) | Fügt mehrere Mengen zu einer neuen Menge zusammen, sortiert diese und entfernt alle mehrfachen Elemente [DEMO-Beispiel](../../demobsp.html?id=3365) | setunionnd(&#91;1,3,2,4&#93;,[3,7&#93;) | &#91;1,2,3,4,7&#93; |  |
| [setcut](func/mengen-funktionen/setcut/index.md) | Bildet die Schnittmenge aus mehreren Mengen [DEMO-Beispiel](../../demobsp.html?id=3366) | setcut(&#91;1,3,2,4&#93;,[3,7&#93;) | &#91;3&#93; |  |
| [setcompare](func/mengen-funktionen/setcompare/index.md) | vergleicht zwei Mengen miteinander, wobei die Reihenfolge egal ist [DEMO-Beispiel](../../demobsp.html?id=3368) | setcompare(&#91;1,3,2,4&#93;,[3,7&#93;) <br> setcompare(&#91;1,3,2&#93;,&#91;1,2,3&#93;) <br> setcompare(&#91;1,3,2&#93;,&#91;1,3,2,3&#93;) <br> setcompare(&#91;1,2,3&#93;,[1,2,3&#93;) | false <br> true <br> false <br> true |  |
| [setcomparend](func/mengen-funktionen/setcomparend/index.md) | vergleicht zwei Mengen miteinander, wobei die Reihenfolge egal ist und doppelte Werte als einfach behandelt werden. [DEMO-Beispiel](../../demobsp.html?id=3369) | setcomparend(&#91;1,3,2,4&#93;,[3,7&#93;) <br> setcomparend([1,3,2&#93;,[1,2,3&#93;) <br> setcomparend([1,3,2&#93;,[1,3,2,3&#93;) <br> setcomparend([1,2,3&#93;,[1,2,3&#93;) | false <br> true <br> true <br> true |  |
| [setpartof](func/mengen-funktionen/setpartof/index.md) | prüft ob die erste Menge eine Teilmenge der zweite Menge ist wobei die Reihenfolge egal ist aber mehrfache Werte berücksichtigt werden [DEMO-Beispiel](../../demobsp.html?id=3370) | setpartof(&#91;1,4&#93;,&#91;1,3,7&#93;) <br> setpartof(&#91;1,3&#93;,[1,2,3&#93;) <br> setpartof([1,3,3&#93;,[1,3,5,7&#93;) <br> setpartof([1,4,4&#93;,[1,2,3,4&#93;) | false <br> true <br> false <br> false |  |
| [setpartofnd](func/mengen-funktionen/setpartofnd/index.md) | prüft ob die erste Menge eine Teilmenge der zweite Menge ist wobei die Reihenfolge und mehrfache Werte egal sind [DEMO-Beispiel](../../demobsp.html?id=3372) | setpartofnd(&#91;1,4&#93;,&#91;1,3,7&#93;) <br> setpartofnd(&#91;1,3&#93;,[1,2,3&#93;) <br> setpartofnd([1,3,3&#93;,[1,3,5,7&#93;) <br> setpartofnd([1,4,4&#93;,[1,2,3,4&#93;) | false <br> true <br> true <br> true |  |
| [setgetmin](func/mengen-funktionen/setgetmin/index.md) | Liefert den kleinsten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3374) | setgetmin(&#91;1,3,-2,4&#93;) | -2 |  |
| [setgetmax](func/mengen-funktionen/setgetmax/index.md) | Liefert den größten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3375) | setgetmax(&#91;1,3,-2,4&#93;) | 4 |  |
| [setremovefirst](func/mengen-funktionen/setremovefirst/index.md) | Entfernt den ersten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3376) | setremovefirst(&#91;1,3,-2,4&#93;) | &#91;3,-2,4&#93; |  |
| [setremovelast](func/mengen-funktionen/setremovelast/index.md) | Entfernt den letzten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3377) | setremovelast(&#91;1,3,-2,4&#93;) | &#91;1,3,-2&#93; |  |
| [setgetfirst](func/mengen-funktionen/setgetfirst/index.md) | Liefert den ersten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3378) | setgetfirst(&#91;1,3,-2,4&#93;) | 1 |  |
| [setgetlast](func/mengen-funktionen/setgetlast/index.md) | Liefert den letzten Wert einer Menge [DEMO-Beispiel](../../demobsp.html?id=3379) | setgetlast(&#91;1,3,-2,4&#93;) | 4 |  |
| [setsub](func/mengen-funktionen/setsub/index.md) | setsub(M,x,y) Liefert eine Teilmenge von M der Elemente vom index x bis zum Index y [DEMO-Beispiel](../../demobsp.html?id=3380) | setsub(&#91;1,3,-2,4&#93;,1,2) | &#91;3,-2&#93; |  |
| [setmakelist](func/mengen-funktionen/setmakelist/index.md) | setmakelist(f,x,start,stop) setzt in den Ausdruck f für x die Werte von start bis stop mit einer Schrittweite von 1 ein. [DEMO-Beispiel](../../demobsp.html?id=3381) | setmakelist(x^2,x,1,4) | &#91; 1,4,9,16 &#93; |  |
|                  | setmakelist(f,x,start,stop,schrittweite) setzt in den Ausdruck f für x die Werte von start bis stop mit dem Abstand schrittweite ein.                                                                                                                                                                                                                                                                                                                                       | setmakelist(x^2,x,1,2,0.5)                                                                                                                                                                         | &#91; 1,2.25,4 &#93;                                     |        |
|                  | setmakelist(f,x,set) setzt die Werte des Vektors set in den Ausdruck f für x ein.                                                                                                                                                                                                                                                                                                                                                                                                                                      | setmakelist(x^2,x,&#91;3,1,2&#93;)                                                                                                                                                                  | &#91; 9,1,4 &#93;                                      |        |
| [foreach](func/mengen-funktionen/foreach/index.md) | Führt für jedes Element eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion [DEMO-Beispiel](../../demobsp.html?id=3383) | foreach(&#91;2,-3,5,-6&#93;,p,cabs(p),"+") | 16 | 6075 |

Für die Korrektur können Mengen über die Zieleinheit auch ohne Reihenfolge vergliechen werden - siehe [Zieleinheit](../ZielEinheit/index.md#parameter-für-den-ergebnisvergleich-von-vektoren-und-mengen-bei-der-schülereingabe)

#### Funktionen für importierte Tabellen

Werden Tabellen aus [csv-Dateien](../BeispielsammlungEditieren/csv-tabellen_importieren/index.md) importiert dann kann auf sie als Matrix zugegriffen werden.

| Funktion                                         | Beschreibung                                                                                                                                                                                        | Beispiel                                                                                                  | Ergebnis                                                              |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [curvepv](func/funktionen-fuer-importierte-tabellen/curvepv/index.md)(tabelle,spalteX,spalteY) | Liest aus einer gespeicherten Tabelle die Spalte "spalteX" für die x-Werte und die Spalte "spalteY" für die Y-Werte eines pv-Vektors [DEMO-Beispiel](../../demobsp.html?id=3384) | curvepv(&#91;&#91;0,0,2&#93;,&#91;1,2,3&#93;,&#91;2,2.2,1.5&#93;,&#91;3,1.4,1.8&#93;&#93;,0,1) | &#91;&#91;0,0&#93;,&#91;1,2&#93;,&#91;2,2.2&#93;,&#91;3,1.4&#93;&#93; |
| [curveinterpol](func/funktionen-fuer-importierte-tabellen/curveinterpol/index.md)(tabelle,spalteX,spalteY,wert) | Interpoliert in einer gespeicherten Tabelle zwischen den Stützpunkten. Als Ergebnis wird ein Vektor aller gefundenen Punkte auf der Kennlinie geliefert [DEMO-Beispiel](../../demobsp.html?id=3385) | curveinterpol(KL,0,1,3.5) | &#91;2.1&#93; |
| [curveinterpolfirst](func/funktionen-fuer-importierte-tabellen/curveinterpolfirst/index.md)(tabelle,spalteX,spalteY,wert) | Interpoliert in einer gespeicherten Tabelle und liefert den ersten interpolierten Punkt auf der Kennlinie. | curveinterpolfirst(KL,0,1,1.5) | 2.1 |
| [interpol](func/erweiterte-arithmetische-funktionen/interpol/index.md)(pv,wert) | Interpoliert Zwischenwerte durch lineare Interpolation in einer als PV-Vektor gegebenen Tabelle [DEMO-Beispiel](../../demobsp.html?id=3386) | interpol(&#91;&#91;0,0&#93;,&#91;1,2&#93;,&#91;2,2.2&#93;,&#91;3,1.4&#93;&#93;,1.5) | 2.1 |
| [curveHTML](func/funktionen-fuer-importierte-tabellen/curvehtml-gross-5-6-7-8/index.md)(tabelle,spaltennamen,einheiten) | Liefert eine HTML-Ansicht einer Tabelle. | curvHTML(KL,KL_names,curveunits(KL)) | HTML-Code der Tabelle |
| [curveunits](func/funktionen-fuer-importierte-tabellen/curveunits/index.md)(tabelle) | Liefert einen Vektor aller Einheiten der Spalten einer Matrix | curveunits(curvepv(&#91;&#91;3A,7V,2&#93;,&#91;2A,2V,3&#93;,&#91;2A,2.2V&#93;,&#91;3A,1.4V&#93;&#93;) | &#91;1A,1V&#93; |

####  Punkte-Mengen-Funktionen
Bei der Eingabe mit dem Plot-Plugin werden Punkte-Mengen als Matrizen in der Form &#91;&#91;x1,y1&#93;,&#91;x2,y2&#93;,&#91;y3,y3&#93;&#93;&#93; für die gespeicherten Punkte welcher der Schüler eingegeben hat verwendet.

Um die Verarbeitung der Eingaben zu erleichtern kann man die Funktionen beginnend mit pv verwenden.

| Funktion      | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Beispiel                                                                                                                                                                                            | Ergebnis                                                                                                                                          | ab Rev |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| [pvabs](func/punkte-mengen-funktionen/pvabs/index.md) | Bestimmt den Betrag eines Punktes oder aller Ortsvektoren zu den Punkten. [DEMO-Beispiel](../../demobsp.html?id=3387) | pvabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) <br> pvabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1) | &#91;3.6056,6.4031,6.7082,4.4721&#93; <br> 6.4031 | 6077 |
| [pvarg](func/punkte-mengen-funktionen/pvarg/index.md) | Bestimmt den Winkel eines Punktes oder aller Ortsvektoren zu den Punkten. [DEMO-Beispiel](../../demobsp.html?id=3388) | pvarg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) <br> pvarg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1) | &#91;0.98279,0.89606,0.46365,2.0344&#93; <br> 0.89606 | 6077 |
| [pvget](func/punkte-mengen-funktionen/pvget/index.md) | Liefert einen Punkt der Punkteliste. [DEMO-Beispiel](../../demobsp.html?id=3389) | pvget(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1) | &#91;4,5&#93; | 6077 |
| [pvgetx](func/punkte-mengen-funktionen/pvgetx/index.md) | Bestimmt die x-Koordinate eines Punktes oder aller Punkte. [DEMO-Beispiel](../../demobsp.html?id=3390) | pvgetx(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) <br> pvgetx(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1) | &#91;2,4,6,-2&#93;<br>4 | 6077 |
| [pvgety](func/punkte-mengen-funktionen/pvgety/index.md) | Bestimmt die y-Koordinate eines Punktes oder aller Punkte. [DEMO-Beispiel](../../demobsp.html?id=3391) | pvgety(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) <br> pvgety(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,1) | &#91;3,5,3,4&#93;<br>3 | 6077 |
| [pvinsert](func/punkte-mengen-funktionen/pvinsert/index.md) | Fügt einen Punkt in die Punktemenge ein [DEMO-Beispiel](../../demobsp.html?id=3392) | pvinsert(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,&#91;7,8&#93;,2) | &#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;7,8&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93; | 6678 |
| [pvinsertlast](func/punkte-mengen-funktionen/pvinsertlast/index.md) | Fügt am Ende der Punktemenge einen Punkt ein [DEMO-Beispiel](../../demobsp.html?id=3393) | pvinsertlast(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,&#91;7,8&#93;) | &#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;7,8&#93;&#93; | 6678 |
| [pvremove](func/punkte-mengen-funktionen/pvremove/index.md) | Löscht einen Punkt aus der Punktemenge [DEMO-Beispiel](../../demobsp.html?id=3394) | pvremove(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,2) | &#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;-2,4&#93;&#93; | 6678 |
| [pvdistance](func/punkte-mengen-funktionen/pvdistance/index.md) | Bestimmt die Abstände als Vektoren zwischen den Punkten. pvdistance(&#91;A,B,C&#93;) liefert &#91;AB,BC,CA&#93; [DEMO-Beispiel](../../demobsp.html?id=3395) | pvdistance(&#91;&#91;1,2&#93;,&#91;3,4&#93;,&#91;10,10&#93;&#93;) | &#91;&#91;2,2&#93;,&#91;7,6&#93;,&#91;-9,-8&#93;&#93; | 6569 |
| [pvlineabs](func/punkte-mengen-funktionen/pvlineabs/index.md) | Bestimmt aus dem n-ten Punktepaar den Absolutbetrag des Abstandes. [DEMO-Beispiel](../../demobsp.html?id=3396) | pvlineabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvlineabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0) | &#91;2.8284,8.0623&#93;<br>2.82842712475 | 6075 |
| [pvlinearg](func/punkte-mengen-funktionen/pvlinearg/index.md) | Bestimmt aus dem n-ten Punktepaar den Winkel der Strecke zur x-Achse [DEMO-Beispiel](../../demobsp.html?id=3397) | pvlinearg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvlinearg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0) | &#91;45°,172.87°&#93;<br>45° | 6075 |
| [pvlinek](func/punkte-mengen-funktionen/pvlinek/index.md) | Bestimmt die Steigung der zugehörigen Geraden dem n-ten Punktepaar [DEMO-Beispiel](../../demobsp.html?id=3398) | pvlinek(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvlinek(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0) | &#91;1,−0.125&#93;<br>1 | 6075 |
| [pvlined](func/punkte-mengen-funktionen/pvlined/index.md) | Bestimmt den Schnittpunkt einer Geraden durch das n-te Punktepaar mit der y-Achse [DEMO-Beispiel](../../demobsp.html?id=3399) | pvlined(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvlined(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0) | &#91;1,3.75&#93; <br>1 | 6075 |
| [pvline](func/punkte-mengen-funktionen/pvline/index.md) | Bestimmt die Geradengleichung einer Geraden durch das n-te Punktepaar [DEMO-Beispiel](../../demobsp.html?id=3400) | pvline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;)<br>pvline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0) | &#91;y=1+x,y=3.75−0.125⋅x&#93;<br>y=x+1 | 6075 |
| [pvpoints](func/punkte-mengen-funktionen/pvpoints/index.md) | Bestimmt die Anzahl der Punkte [DEMO-Beispiel](../../demobsp.html?id=3401) | pvpoints(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;) | 4 | 6075 |
| [pvlines](func/punkte-mengen-funktionen/pvlines/index.md) | Bestimmt die Anzahl der Linien bzw. Punktepaare eines Punktevektors. | pvlines(&#91;&#91;1,2&#93;,&#91;3,4&#93;,&#91;5,6&#93;,&#91;7,8&#93;&#93;) | 2 |  |
| [pvvect](func/punkte-mengen-funktionen/pvvect/index.md) | Bestimmt einen Vector aus dem n-te Punktepaar [DEMO-Beispiel](../../demobsp.html?id=3402) | pvvect(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,0) | &#91;2,2&#93; | 6075 |
| [pvrect](func/punkte-mengen-funktionen/pvrect/index.md) | Liefert aus einer Punktewolke ein Rechteck als zwei Eckpunkte links-unten und rechts-oben. | pvrect(&#91;&#91;1,2&#93;,&#91;4,5&#93;,&#91;2,3&#93;&#93;) | &#91;&#91;1,2&#93;,&#91;4,5&#93;&#93; |  |
| [pvsort](func/punkte-mengen-funktionen/pvsort/index.md) | Sortiert die Punkte zuerst nach steigender x-Koordinate und bei gleicher x-Koordinate nach steigender y-Koordinate. | pvsort(&#91;&#91;2,3&#93;,&#91;1,5&#93;,&#91;1,2&#93;&#93;) | &#91;&#91;1,2&#93;,&#91;1,5&#93;,&#91;2,3&#93;&#93; |  |
| [pvsortx](func/punkte-mengen-funktionen/pvsortx/index.md) | Sortiert die Punkte nach steigender x-Koordinate [DEMO-Beispiel](../../demobsp.html?id=3403) | pvsortx(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;) | &#91;&#91;−7,−9&#93;,&#91;−3,5&#93;,&#91;−2,4&#93;,&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;&#93; | 6077 |
| [pvsorty](func/punkte-mengen-funktionen/pvsorty/index.md) | Sortiert die Punkte nach steigender y-Koordinate [DEMO-Beispiel](../../demobsp.html?id=3404) | pvsorty(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;) | &#91;&#91;−7,−9&#93;,&#91;2,3&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;4,5&#93;,&#91;−3,5&#93;&#93; | 6077 |
| [pvsortabs](func/punkte-mengen-funktionen/pvsortabs/index.md) | Sortiert die Punkte nach steigendem Absolutbetrag des Ortsvektors [DEMO-Beispiel](../../demobsp.html?id=3405) | pvsortabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;) | &#91;&#91;2,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−7,−9&#93;&#93; | 6077 |
| [pvsortarg](func/punkte-mengen-funktionen/pvsortarg/index.md) | Sortiert die Punkte nach steigendem Winkel des Ortsvektors (-pi bis pi) [DEMO-Beispiel](../../demobsp.html?id=3406) | pvsortarg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;) | &#91;&#91;−7,−9&#93;,&#91;6,3&#93;,&#91;4,5&#93;,&#91;2,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;&#93; | 6077 |
| [pvsortlinex](func/punkte-mengen-funktionen/pvsortlinex/index.md) | Sortiert Punktepaare nach steigender x-Koordinate der kleineren x-Koordinate des Paares. [DEMO-Beispiel](../../demobsp.html?id=3407) | pvsortlinex(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;) | &#91;&#91;−3,5&#93;,&#91;−7,−9&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;2,3&#93;,&#91;4,5&#93;&#93; | 6077 |
| [pvsortliney](func/punkte-mengen-funktionen/pvsortliney/index.md) | Sortiert Punktepaare nach steigender y-Koordinate der kleineren y-Koordinate des Paares. [DEMO-Beispiel](../../demobsp.html?id=3408) | pvsortliney(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;) | &#91;&#91;−3,5&#93;,&#91;−7,−9&#93;,&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;&#93; | 6077 |
| [pvsortlineabs](func/punkte-mengen-funktionen/pvsortlineabs/index.md) | Sortiert Punktepaare nach steigendem Betrag der Linienlänge. [DEMO-Beispiel](../../demobsp.html?id=3409) | pvsortlineabs(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;) | &#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93; | 6077 |
| [pvsortlinearg](func/punkte-mengen-funktionen/pvsortlinearg/index.md) | Sortiert Punktepaare nach steigendem Winkel der Linienrichtung. [DEMO-Beispiel](../../demobsp.html?id=3410) | pvsortlinearg(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;,&#91;−3,5&#93;,&#91;−7,−9&#93;&#93;) | &#91;&#91;−3,5&#93;,&#91;−7,−9&#93;,&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;−2,4&#93;&#93; | 6077 |
| [pvequals](func/punkte-mengen-funktionen/pvequals/index.md) | Prüft ob zwei Punktevektoren gleich sind. Die Genauigkeit wird als dritter Parameter angegeben, oder bei einem Antwortfeld von der Antworttoleranz genommen. Prozentangaben der Genauigkeit beziehen sich auf die Breite bzw. Höhe des Punktefeldes im karthesischen Koordinatensystem. [DEMO-Beispiel](../../demobsp.html?id=3412) | pvequals(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,&#91;4,5&#93;,&#91;6.01,3&#93;,&#91;-2,3.99&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,2%) | true | 6077 |
| [pvhaspoint](func/punkte-mengen-funktionen/pvhaspoint/index.md) | Prüft ob sich ein Punkt innerhalb des Punktefeldes befindet. Die Genauigkeit kann wie bei pvequals als dritter Parameter angegeben werden. [DEMO-Beispiel](../../demobsp.html?id=3413) | pvhaspoint(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,&#91;4,5&#93;,2%) | true | 6077 |
| [pvhasline](func/punkte-mengen-funktionen/pvhasline/index.md) | Prüft ob sich eine Linie innerhalb des Punktefeldes von Linien befindet. Die Genauigkeit kann wie bei pvequals als dritter Parameter angegeben werden. [DEMO-Beispiel](../../demobsp.html?id=3414) | pvhasline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;,&#91;-3,5&#93;,&#91;-7,-9&#93;&#93;,&#91;&#91;6,3&#93;,&#91;-2,4&#93;&#93;,2%) | true | 6078 |
| [pvforeachline](func/punkte-mengen-funktionen/pvforeachline/index.md) | Führt für jedes Punktepaar eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion [DEMO-Beispiel](../../demobsp.html?id=3416) | pvforeachline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,p,pvlineabs(p),"+") | 10.890684873 | 6075 |
| [pvfunc](func/punkte-mengen-funktionen/pvfunc/index.md) | Erzeugt aus einer Funktionen in einer Variablen (x-Achse) eine Punktmatrix der Funktionswerte (y-Achse). pvfunc(funktion,variable,minx,maxx,deltax) [DEMO-Beispiel](../../demobsp.html?id=3417) | pvfunc(x^2,x,-2,2,0.5) | &#91;&#91;−2,4&#93;,&#91;−1.5,2.25&#93;,&#91;−1,1&#93;,&#91;−0.5,0.25&#93;,&#91;0,0&#93;,&#91;0.5,0.25&#93;,&#91;1,1&#93;,&#91;1.5,2.25&#93;&#93; | 6080 |
| [pvcompare](func/punkte-mengen-funktionen/pvcompare/index.md) | Vergleicht einen Referenz-Linienzug mit einem eingegebenen Linienzug unter Berücksichtigung der Toleranz. Die Toleranz stellt eine relative Tolerenz bezogen auf den Bereich zwischen MinXY und MaxXY da, wobei eine Toleranz von 0.1 gleichbedeutend 10 Prozent bezogen auf Max-Min ist (Mit dem String "a0.1" könnte man auch ein absolute Toleranz von 0.1 für x und y realisieren) <br> pvcompare(Referenz,Eingabe)<br> pvcompare(Referenz,Eingabe,Toleranz)<br> pvcompare(Referenz,Eingabe,MinX,MaxX,MinY,MaxY) <br> pvcompare(Referenz,Eingabe,MinX,MaxX,MinY,MaxY,Toleranz) [DEMO-Beispiel](../../demobsp.html?id=3419) | pvcompare(&#91;&#91;0,0&#93;,&#91;1,1&#93;,&#91;2,1&#93;,&#91;3,0&#93;&#93;,&#91;&#91;0,0&#93;,&#91;1,1&#93;,&#91;2,1&#93;,&#91;3,0&#93;&#93;,0,3,-5,5) | true | 6080 |
| [pvunion](func/punkte-mengen-funktionen/pvunion/index.md) | hängt mehrere Punktevektoren zu einem größereren Punktevektor zusammen [DEMO-Beispiel](../../demobsp.html?id=3421) | pvunion(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;,&#91;&#91;5,6&#93;,&#91;7,8&#93;&#93;,&#91;9,10&#93;) | &#91;&#91;1,2&#93;,&#91;3,4&#93;,&#91;5,6&#93;,&#91;7,8&#93;,&#91;9,10&#93;&#93; | 6569 |


#### Typ-Funktionen
Werden nur dann ausgewertet wenn der Parameter ein numerischer Wert oder eine Menge ist.

| Funktion     | Beschreibung                                                                                           | Beispiel                           | Ergebnis |
|--------------|--------------------------------------------------------------------------------------------------------|------------------------------------|----------|
| [isset](func/typ-funktionen/isset/index.md) | Prüft ob es sich um eine Menge handelt. [DEMO-Beispiel](../../demobsp.html?id=3422) | isset(&#91;12,13,14&#93;) | true |
| [issetnumeric](func/typ-funktionen/issetnumeric/index.md) | Prüft ob es sich um eine Menge aus reellen Zahlen handelt. [DEMO-Beispiel](../../demobsp.html?id=3423) | issetnumeric(&#91;12,13.4,14&#93;) | true |
| [issetlong](func/typ-funktionen/issetlong/index.md) | Prüft ob es sich um eine Menge aus ganzen Zahlen handelt. [DEMO-Beispiel](../../demobsp.html?id=3424) | issetlong(&#91;12,13,14&#93;) | true |
| [islong](func/typ-funktionen/islong/index.md) | Prüft ob es sich um eine ganze Zahl handelt. [DEMO-Beispiel](../../demobsp.html?id=3425) | islong(12) | true |


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
| [matrix](func/algebra/matrix/index.md) | erzeugt aus mehreren gleich langen Vektoren eine Matrix [DEMO-Beispiel](../../demobsp.html?id=3426) | matrix([1,2&#93;,&#91;3,4&#93;) | &#91;&#91;1,2&#93;,&#91;3,4&#93;&#93; |
| [vmatrix](func/algebra/vmatrix/index.md) | Erzeugt aus genau einem Vektor eine Matrix. Enthaltene Vektoren werden zu Matrixzeilen, einzelne Werte zu ein-elementigen Zeilen; eine Matrix wird unverändert zurückgegeben. | vmatrix(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;) | &#91;&#91;1,2&#93;,&#91;3,4&#93;&#93; |
| [inv](func/algebra/inv/index.md) | invertiert eine quadratische Matrix oder bildet 1/x [DEMO-Beispiel](../../demobsp.html?id=3427) | inv(matrix(&#91;1,2&#93;,&#91;3,4&#93;)) | &#91;&#91;-2,1&#93;,&#91;3/2,-1/2&#93;&#93; |
| [vget](func/algebra/vget/index.md) | liefert ein Element eines Vektors oder einer Matrix [Video](https://www.youtube.com/watch?v=T82YIt3e8ac) [DEMO-Beispiel](../../demobsp.html?id=3428) | vget(&#91;12,13,14&#93;,1) <br> vget(matrix(&#91;9,2&#93;,&#91;3,4&#93;),0,1) | 13 <br> 2 |
| [first](func/algebra/first/index.md) | liefert das erste Element mit dem Index 0 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3429) | first(&#91;12,13,14&#93;) | 12 |
| [second](func/algebra/second/index.md) | liefert das zweite Element mit dem Index 1 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3430) | second(&#91;12,13,14&#93;) | 13 |
| [third](func/algebra/third/index.md) | liefert das dritte Element mit dem Index 2 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3431) | third(&#91;12,13,14&#93;) | 14 |
| [fourth](func/algebra/fourth/index.md) | liefert das vierte Element mit dem Index 3 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3432) | fourth (&#91;12,13,14,15,16,17,18&#93;) | 15 |
| [fifth](func/algebra/fifth/index.md) | liefert das fünfte Element mit dem Index 4 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3433) | fifth (&#91;12,13,14,15,16,17,18&#93;) | 16 |
| [sixth](func/algebra/sixth/index.md) | liefert das sechste Element mit dem Index 5 eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3434) | sixth (&#91;12,13,14,15,16,17,18&#93;) | 17 |
| [last](func/algebra/last/index.md) | liefert das letzte Element eines Vektors | first(&#91;12,13,14&#93;) | 14 |
| [vgetmaxima](func/algebra/vgetmaxima/index.md) | liefert ein Element eines Vektors oder einer Matrix wobei der Index (wie bei Maxima) bei 1 startet. [DEMO-Beispiel](../../demobsp.html?id=3435) | vgetmaxima(&#91;12,13,14&#93;,1) | 12 |
| [vset](func/algebra/vset/index.md) | setzt ein Element eines Vektors oder einer Matrix [DEMO-Beispiel](../../demobsp.html?id=3436) | vset(&#91;12,13,14&#93;,1,35) <br> vset(matrix(&#91;9,2&#93;,&#91;3,4&#93;),0,0,-9) | &#91;12,35,14&#93; <br> &#91;&#91;-9,2&#93;,&#91;3,4&#93;&#93; |
| [vsetmaxima](func/algebra/vsetmaxima/index.md) | setzt ein Element eines Vektors oder einer Matrix wobei der Index (wie bei Maxima) bei 1 startet. [DEMO-Beispiel](../../demobsp.html?id=3437) | vsetmaxima(&#91;12,13,14&#93;,1,35) | &#91;35,13,14&#93; |
| [vinsert](func/algebra/vinsert/index.md) | fügt ein Element in einen Vektor an eine gegebene Stelle ein [DEMO-Beispiel](../../demobsp.html?id=3438) | vinsert(&#91;12,13,14&#93;,1,25) | &#91;12,25,13,14&#93; |
| [vremove](func/algebra/vremove/index.md) | löscht ein Element eines Vektors [Video](https://www.youtube.com/watch?v=T82YIt3e8ac) [DEMO-Beispiel](../../demobsp.html?id=3439) | vremove(&#91;12,13,14&#93;,1) | &#91;12,14&#93; |
| [vabs](func/algebra/vabs/index.md) | Berechnet den Betrag eines Vektors [DEMO-Beispiel](../../demobsp.html?id=3440) | vabs(&#91;3,4&#93;) | 5 |
| [vin](func/algebra/vin/index.md) | Berechnet das innere Produkt von 2 Vektoren [DEMO-Beispiel](../../demobsp.html?id=3441) | vin(&#91;1,2,3&#93;,&#91;4,5,6&#93;) | 32 |
| [vex](func/algebra/vex/index.md) | Berechnet das ex-Produkt von 2 Vektoren im 3-dimensionalen Raum [DEMO-Beispiel](../../demobsp.html?id=3442) | vex(&#91;1,2,3&#93;,&#91;4,5,6&#93;) | &#91;-3,6,-3&#93; |
| [vadd](func/algebra/vadd/index.md) | Addiert zwei Vektoren elementweise [DEMO-Beispiel](../../demobsp.html?id=3443) | vadd(&#91;1,2,3&#93;,&#91;4,5,6&#93;) | &#91;5,7,9&#93; |
| [vsub](func/algebra/vsub/index.md) | Subtrahiert zwei Vektoren elementweise [DEMO-Beispiel](../../demobsp.html?id=3444) | vsub(&#91;1,2,3&#93;,&#91;4,5,6&#93;) | &#91;-3,-3,-3&#93; |
| [vmul](func/algebra/vmul/index.md) | Multipliziert zwei Vektoren elementweise [DEMO-Beispiel](../../demobsp.html?id=3445) | vmul(&#91;1,2,3&#93;,&#91;4,5,6&#93;) | &#91;4,10,18&#93; |
| [vdiv](func/algebra/vdiv/index.md) | Dividiert zwei Vektoren elementweise [DEMO-Beispiel](../../demobsp.html?id=3446) | vdiv(&#91;1,2,3&#93;,&#91;4,5,6&#93;) | &#91;1/3,2/5,3/6&#93; |
| [vpow](func/algebra/vpow/index.md) | Potenziert zwei Vektoren elementweise [DEMO-Beispiel](../../demobsp.html?id=3447) | vpow(&#91;1,2,3&#93;,&#91;4,5,6&#93;) | &#91;1,32,729&#93; |
| [mrows](func/algebra/mrows/index.md) | liefert die Anzahl der Zeilen einer Matrix [DEMO-Beispiel](../../demobsp.html?id=3448) | mrows(&#91;&#91;3,4,4&#93;,&#91;3,6,54,34,3,54&#93;&#93;) | 2 |
| [mcols](func/algebra/mcols/index.md) | liefert die Anzahl der Spalten einer Matrix [DEMO-Beispiel](../../demobsp.html?id=3449) | mcols(&#91;&#91;3,4,4&#93;,&#91;3,6,54,34,3,54&#93;&#93;) | 6 |
| [mprod](func/algebra/mprod/index.md) | Bildet das Matrixprodukt aus zwei Matrizen [DEMO-Beispiel](../../demobsp.html?id=3450) | mprod(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;,&#91;&#91;5,6&#93;,&#91;7,8&#93;&#93;) | &#91;&#91;19,22&#93;,&#91;43,50&#93;&#93; |
| [mtrans](func/algebra/mtrans/index.md) | Bildet die transponierte Matrix [DEMO-Beispiel](../../demobsp.html?id=3451) | mtrans(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;) | &#91;&#91;1,3&#93;,&#91;2,4&#93;&#93; |
| [minv](func/algebra/minv/index.md) | Bildet die inverse Matrix [DEMO-Beispiel](../../demobsp.html?id=3452) | minv(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;) | &#91;&#91;-2,1&#93;,&#91;3/2,-1/2&#93;&#93; |
| [mdet](func/algebra/mdet/index.md) | Bildet die Determinante einer quadratischen Matrix [DEMO-Beispiel](../../demobsp.html?id=3453) | mdet(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;) | -2 |
| [mcunion](func/algebra/mcunion/index.md) | Fügt mehrere Matrizen oder Vektoren spaltenweise(nebeneinander) zusammen [DEMO-Beispiel](../../demobsp.html?id=3454) | mcunion(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,&#91;&#91;10,11&#93;,&#91;12,13&#93;,&#91;14,15&#93;&#93;) | &#91;&#91;1,2,3,10,11&#93;,&#91;4,5,6,12,13&#93;,&#91;7,8,9,14,15&#93;&#93; |
| [mrunion](func/algebra/mrunion/index.md) | Fügt mehrere Matrizen oder Vektoren zeileweise(untereinander) zusammen [DEMO-Beispiel](../../demobsp.html?id=3455) | mrunion(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,&#91;&#91;10,11,12&#93;,&#91;13,14,15&#93;&#93;) | &#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;,&#91;10,11,12&#93;,&#91;13,14,15&#93;&#93; |
| [msub](func/algebra/msub/index.md) | msub(matrix,zeile,spalte,zeilen,spalten) Liefert eine Untermatrix beginnend bei Zeile und Spalten mit der angegebenen Anzahl von Zeilen und Spalten. Die Parameter Spalte,Zeilen und Spalten sind dabei optional. [DEMO-Beispiel](../../demobsp.html?id=3456) | msub(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,0,1,2,2) | &#91;&#91;2,3&#93;,&#91;5,6&#93;&#93; |
| [mcinsert](func/algebra/mcinsert/index.md) | mcinsert(matrix,matrixodervektor,position) Fügt an der Spaltenposition eine Matrix oder einen Vektor als neue Spalten ein [DEMO-Beispiel](../../demobsp.html?id=3457) | mcinsert(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,&#91;&#91;10,11&#93;,&#91;12,13&#93;,&#91;14,15&#93;&#93;,1) | &#91;&#91;1,10,11,2,3&#93;,&#91;4,12,13,5,6&#93;,&#91;7,14,15,8,9&#93;&#93; |
| [mrinsert](func/algebra/mrinsert/index.md) | mrinsert(matrix,matrixodervektor,position) Fügt an der Zeilenposition eine Matrix oder einen Vektor als neue Zeilen ein [DEMO-Beispiel](../../demobsp.html?id=3459) | mrinsert(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,&#91;&#91;10,11,12&#93;,&#91;13,14,15&#93;&#93;,1) | &#91;&#91;1,2,3&#93;,&#91;10,11,12&#93;,&#91;13,14,15&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93; |
| [mcdelete](func/algebra/mcdelete/index.md) | mcdelete(matrix,position) Löscht die angegebene Spalte aus einer Matrix [DEMO-Beispiel](../../demobsp.html?id=3460) | mcdelete(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,1) | &#91;&#91;1,3&#93;,&#91;4,6&#93;,&#91;7,9&#93;&#93; |
| [mrdelete](func/algebra/mrdelete/index.md) | mrdelete(matrix,position) Löscht die angegebene Zeile aus einer Matrix [DEMO-Beispiel](../../demobsp.html?id=3461) | mrdelete(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,1) | &#91;&#91;1,2,3&#93;,&#91;7,8,9&#93;&#93; |
| [vindex](func/algebra/vindex/index.md) | vindex(v,x) liefert den Index des Elementes eines Vektors, welcher am nächsten bei x liegt [DEMO-Beispiel](../../demobsp.html?id=3462) | vindex(&#91;10,30,70&#93;,40) | 1 |
| [vindexup](func/algebra/vindexup/index.md) | vindexup(v,x) liefert den Index des Elementes eines Vektors, welcher größer oder gleich x ist [DEMO-Beispiel](../../demobsp.html?id=3463) | vindexup(&#91;10,30,70&#93;,40) | 2 |
| [vindexdown](func/algebra/vindexdown/index.md) | vindexdown(v,x) liefert den Index des Elementes eines Vektors, welcher kleiner oder gleich x ist [DEMO-Beispiel](../../demobsp.html?id=3464) | vindexdown(&#91;10,30,70&#93;,60) | 1 |
| [verweis](func/algebra/verweis/index.md) | verweis(M,x,n) liefert den Wert der n-ten Spalte (ohne Angabe von n die 2.Spalte) einer Matrix M wo x dem Wert in der ersten Spalte am nächsten liegt [DEMO-Beispiel](../../demobsp.html?id=3465) | verweis(&#91;&#91;10,33&#93;,&#91;20,77&#93;,&#91;30,99&#93;&#93;,21) | 77 |
| [verweisup](func/algebra/verweisup/index.md) | verweisup(M,x,n) liefert den Wert der n-ten Spalte (ohne Angabe von n die 2.Spalte) einer Matrix M wo x dem Wert in der ersten Spalte am nächsten liegt [DEMO-Beispiel](../../demobsp.html?id=3466) | verweisup(&#91;&#91;10,33&#93;,&#91;20,77&#93;,&#91;30,99&#93;&#93;,21) | 99 |
| [verweisdown](func/algebra/verweisdown/index.md) | verweisdown(M,x,n) liefert den Wert der n-ten Spalte (ohne Angabe von n die 2.Spalte) einer Matrix M wo x dem Wert in der ersten Spalte am nächsten liegt [DEMO-Beispiel](../../demobsp.html?id=3467) | verweisdown(&#91;&#91;10,33&#93;,&#91;20,77&#93;,&#91;30,99&#93;&#93;,27,1) | 77 |
| [range](func/algebra/range/index.md) | range(anzahl) liefert ein Feld von ganzzahligen Werten von 0 beginnend [DEMO-Beispiel](../../demobsp.html?id=3468) | range(5) | &#91;0,1,2,3,4&#93; |
| [linspace](func/algebra/linspace/index.md) | linspace(start,ende,anzahl) liefert ein Feld von Werte von Startwert bis Endwert mit gleichem Abstand [DEMO-Beispiel](../../demobsp.html?id=3469) | linspace(4,8,5) | &#91;4,5,6,7,8&#93; |
| [logspace](func/algebra/logspace/index.md) | logspace(start,ende,anzahl) liefert ein Feld von Werte von Startwert bis Endwert mit gleichem logarithmischen Abstand [DEMO-Beispiel](../../demobsp.html?id=3470) | logspace(10,10000,4) | &#91;10,100,1000,10000&#93; |


#### Variable

| Funktion | Beschreibung                                                                                                                                                      | Beispiel                                      | Ergebnis                                                                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|------------------------------------------------------------------------------------------------------|
| [kill](func/variable/kill/index.md) | löscht Variable aus dem Variablenspeicher [DEMO-Beispiel](../../demobsp.html?id=3471) | kill(x,y) <br> kill(allbut(y)) <br> kill(all) | löscht die Variablen x und y <br> löscht alle Variablen mit Ausnahme von y <br> löscht alle Variable |
| [allbut](func/variable/allbut/index.md) | Liefert eine Liste aller Variablen des Parsers als Menge(Vektor) mit Ausnahme der als Parameter angegebenen Variablen [DEMO-Beispiel](../../demobsp.html?id=3472) | allbut(x,y) | &#91;a,b,c&#93; |


#### Auswertung und Programmierung

| Funktion                         | Beschreibung                                                                                                                                                                                                                                                                                                                                                                       | Beispiel                                                                                   | Ergebnis                                                                          | Revision |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|----------|
| [ev](func/auswertung-und-programmierung/ev/index.md) | Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden [DEMO-Beispiel](../../demobsp.html?id=3473) | ev(x*y,y=4) | x*4 |  |
| [evruntime](func/auswertung-und-programmierung/evruntime/index.md) | Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden. Das **Einsetzen erfolgt erst bei der Ergebnisberechnung**! [DEMO-Beispiel](../../demobsp.html?id=3474) | evruntime(x*y,y=4) | x*4 |  |
| [nv](func/auswertung-und-programmierung/nv/index.md) | Auswertung eines Ausdruckes, als Parameter können Gleichungen angegeben werden, welche dann in den Ausdruck eingesetzt werden. Im Gegensatz zu ev werden bestehende Variable nur in den Gleichungen, aber nicht im Ausdruck selbst eingesetzt! [DEMO-Beispiel](../../demobsp.html?id=3475) | nv(x*y,y=4) | x*4 |  |
| [if](func/auswertung-und-programmierung/if/index.md) | Bedingungsfunktion if(bedingung,wahrwert,falschwert) [DEMO-Beispiel](../../demobsp.html?id=3476) | if(4&lt;6,10,12) | 10 |  |
| [wenn](func/auswertung-und-programmierung/wenn/index.md) | Bedingungsfunktion wenn(bedingung,wahrwert,falschwert). Im Prinzip identisch wie if, jedoch kann if mit Maxima nicht verwendet werden. [DEMO-Beispiel](../../demobsp.html?id=3477) | wenn(4&lt;6,10,12) | 10 |  |
| [plugin](func/auswertung-und-programmierung/plugin/index.md) | Ruft die Berechnungsmethode des Plugins, welches als erster Stringparameter angegeben werden muss auf und übergibt die weiteren Parameter an die Berechnungsmethode des Plugins. [DEMO-Beispiel](../../demobsp.html?id=3478) | plugin("plugin1",3) | führt die Berechnung des Plugins mit dem Namen "plugin1" mit dem Parameter 3 aus. |  |
| [symbolic](func/auswertung-und-programmierung/symbolic/index.md) | Bei allen Variablen innerhalb von symbolic werden nur nicht-numerische Werte eingesetzt! Wird vor allem im Angabtext bei {= } verwendet [DEMO-Beispiel](../../demobsp.html?id=3479) | symbolic(x^2+2) | x^2+2 |  |
| [runtime](func/auswertung-und-programmierung/runtime/index.md) | Bei dieser Funktion wird **erst bei der Berechnung der Frageantwort, nach dem Einsetzen der Datensätze** das **komplette Maxima-Feld** mit dem internen **Parser** durchgerechnet und danach der Parameter-Ausdruck berechnet. Dadurch kann man bei komplizierten Berechnungen eine sehr aufwendige symbolische Berechnung verhindern! [DEMO-Beispiel](../../demobsp.html?id=3480) | runtime(U) |  |  |
| [dataset](func/auswertung-und-programmierung/dataset/index.md) | liefert alle Datensätze einer Datensatz-Definition in einem Vektor [DEMO-Beispiel](../../demobsp.html?id=3481) | dataset(x) |  |  |
| [parse](func/stringfunktionen/parse/index.md) | Wenn der Parameter ein String ist wird dieser String mit dem Parser interpretiert [DEMO-Beispiel](../../demobsp.html?id=3482) | parse("2+3") | 5 |  |
| [foreach](func/mengen-funktionen/foreach/index.md) | Führt für jedes Element einer Menge eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion [DEMO-Beispiel](../../demobsp.html?id=3484) | foreach(&#91;2,-3,5,-6&#93;,p,cabs(p),"+") | 16 | 6075 |
| [pvforeachline](func/punkte-mengen-funktionen/pvforeachline/index.md) | Führt für jedes Punktepaar einer Punktemenge eine Berechnung aus und verbindet die Ergebnisse mit der Aggregatfunktion [DEMO-Beispiel](../../demobsp.html?id=3485) | pvforeachline(&#91;&#91;2,3&#93;,&#91;4,5&#93;,&#91;6,3&#93;,&#91;-2,4&#93;&#93;,p,pvlineabs(p),"+") | 10.890684873 | 6075 |
| [forloop](func/auswertung-und-programmierung/forloop/index.md) | Führt eine Zählschleife aus forloop(Variable,Startwert,Wiederholbedingung,Inkrement,Ausdruck,Aggregatsfunktion). <br>Ohne Aggregatsfunktion wird ein Feld mit den Ergebnissen der Schleifeniterationen geliefert. [DEMO-Beispiel](../../demobsp.html?id=3486) | forloop(i,1,i&lt;7,i++,i,"+")<br>forloop(i,1,i&lt;7,i:i+2,i) | 21<br>&#91;1,3,5&#93; | 6077 |


#### Optimierung der Ausdrücke

| Funktion    | Beschreibung                                                                                                                                                                                                                                                                | Beispiel         | Ergebnis         |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------------|
| [opt](func/optimierung-der-ausdruecke/opt/index.md) | Ausdruck wird vollständig optimiert, die Funktion wird ausgewertet und ist danach nicht mehr vorhanden. Nur bei der Verwendung des internen Parser sinnvoll. [DEMO-Beispiel](../../demobsp.html?id=3489) | opt(x+x) | 2*x |
| [optorder](func/optimierung-der-ausdruecke/optorder/index.md) | Optimiert nur die symbolische Reihenfolge des Ausdrucks. Optional steuert ein zweiter ganzzahliger Modus, ob bzw. wie lange die Funktion im Ausdruck erhalten bleibt. | optorder(y+x) | x+y |
| [number](func/optimierung-der-ausdruecke/number/index.md) | Erzwingt die numerische Auswertung aller numerisch berechenbaren Teile. Bleibt bei einem weiterhin symbolischen Ergebnis als Funktion erhalten. | number(2+3+x) | number(5+x) |
| [mathe](func/optimierung-der-ausdruecke/mathe/index.md) | Wertet Ganzzahlen und Konstanten numerisch nur soweit aus, wie es der symbolische Mathematikmodus zulässt; ein symbolisches Ergebnis bleibt in `mathe(...)` erhalten. | mathe(2+3+x) | mathe(5+x) |
| [ratsimp](func/optimierung-der-ausdruecke/ratsimp/index.md) | Ausdruck wird vollständig optimiert, die Funktion wird ausgewertet und ist danach nicht mehr vorhanden (wie opt, wird jedoch auch von Maxima ausgewertet) [DEMO-Beispiel](../../demobsp.html?id=3490) | ratsimp(x+x) | 2*x |
| [noopt](func/optimierung-der-ausdruecke/noopt/index.md) | Ausdruck wird nicht optimiert, bleibt also so erhalten wie angegeben. Die Funktion an sich geht aber verloren. [DEMO-Beispiel](../../demobsp.html?id=3491) | noopt(2+3) | 2+3 |
| [nopt](func/optimierung-der-ausdruecke/nopt/index.md) | Ausdruck wird nicht optimiert, bleibt also so erhalten wie angegeben. Die Funktion bleibt erhalten und wird erst bei der Lösungsberechnung oder durch opt() entfernt. [DEMO-Beispiel](../../demobsp.html?id=3492) | noopt(2+3) | 2+3 |
| [lopt](func/optimierung-der-ausdruecke/lopt/index.md) | Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {=  wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck vollständig optimiert. [DEMO-Beispiel](../../demobsp.html?id=3493) | lopt(x+3) | lopt(x+3) |
| [qopt](func/optimierung-der-ausdruecke/qopt/index.md) | Im Maximafeld wird alles innerhalb der Funktion nicht ausgewertet und die Funktion bleibt erhalten, bei der Lösung wird nach dem Einsetzen der Werte der Ausdruck vollständig optimiert. <br> Anwendung findet die Funktion bei boolschen Fragen und Folgefehlerbehandlung. | qopt(x+3) | qopt(x+3) |
| [lnoopt](func/optimierung-der-ausdruecke/lnoopt/index.md) | Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {=  wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck nicht mehr optimiert. | lnoopt(x+3+2) | lnoopt(x+5) |
| [loptnumeric](func/optimierung-der-ausdruecke/loptnumeric/index.md) | Im Maximafeld bleibt die Funktion ohne Funktion erhalten, im Ergebnis {=  wird die Funktion entfernt und in der Lösung wird nach dem Einsetzen der Werte der Ausdruck nur numerisch optimiert. | loptnumeric(x+y) | loptnumeric(x+y) |
| [aopt](func/optimierung-der-ausdruecke/aopt/index.md) | Bei Maxima und Lösung geht die Funktion verloren, nur innerhalb von noopt bleibt sie erhalten. Bei der Anzeige führt sie zur Optimierung das Ausdruckes nach Einsetzen der Datensätze. | aopt(x) | x |


#### Anzeige und Lösungsberechnung
Diese Funktionen haben entweder einen oder zwei Parameter. Der erste Parameter stellt die darzustellende Funktion dar, der zweite Parameter, welcher eine Ganzzahl sein muss, gibt an, wie die Darstellung erfolgen soll. Wird der 2.Parameter weggelassen, so wird er als 0 interpretiert.
* 0 Bei Berechnungen hat die Funktion keine Wirkung, bleibt aber als Funktion erhalten. Bei Lösung und Anzeige wird die Funktion ausgewertet
* 1 Wirkt nur bei Lösung, bei Berechnungen bleibt die Funktion erhalten
* 2 Wirkt nur bei Anzeige, bei Berechnungen bleibt die Funktion erhalten

| Funktion | Beschreibung                                                                                                                                              | Beispiel          | Ergebnis |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------|
| [viewpow](func/anzeige-und-loesungsberechnung/viewpow/index.md) | Gibt alle Wurzeln als Potenzen aus, und stellt alle Potenzen im Nenner als negativen Exponenten im Zähler dar [DEMO-Beispiel](../../demobsp.html?id=3495) | viewpow(sqrt(x)) | x^(1/2) |
| [viewsqrt](func/anzeige-und-loesungsberechnung/viewsqrt/index.md) | Gibt Potenzen welche als Wurzel darstellbar sind auch als als Wurzeln mit der Funktion sqrt oder root aus [DEMO-Beispiel](../../demobsp.html?id=3496) | viewsqrt(x^(1/2)) | sqrt(x) |


####  Datums und Zeitfunktionen

| Funktion       | Beschreibung                                                                                                                        | Beispiel | Ergebnis | REvision |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------|----------|----------|----------|
| [dateparse](func/datums-und-zeitfunktionen/dateparse/index.md) | Wandelt einen String in ein Datum als Ganzzahl in Sekunden seit 1.1.0000 [DEMO-Beispiel](../../demobsp.html?id=3497) |  |  | 6530 |
| [date](func/datums-und-zeitfunktionen/date/index.md) | date(y,m,d,h,min,sec) erzeugt ein Datum als Ganzzahl in Sekunden seit 1.1.0000 00:00:00 [DEMO-Beispiel](../../demobsp.html?id=3634) |  |  | 6530 |
| [date](func/datums-und-zeitfunktionen/date/index.md) | date(y,m,d) erzeugt ein Datum als Ganzzahl in Sekunden seit 1.1.0000 00:00:00 [DEMO-Beispiel](../../demobsp.html?id=3634) |  |  | 6530 |
| [time](func/datums-und-zeitfunktionen/time/index.md) | time(h,min,sec) erzeugt eine Uhrzeit als Ganzzahl in Sekunden seit Mitternacht [DEMO-Beispiel](../../demobsp.html?id=3635) |  |  | 6762 |
| [datestring](func/datums-und-zeitfunktionen/datestring/index.md) | datestring(x) datestring(x,&quot;format&quot;) erzeugt aus einem Datum in Sekunden seit 1.1.0000 eine Stringausgabe |  |  | 6530 |
| [timestring](func/datums-und-zeitfunktionen/timestring/index.md) | erzeugt eine Uhrzeit als String |  |  | 6530 |
| [datetimestring](func/datums-und-zeitfunktionen/datetimestring/index.md) | erzeugt Datum und Uhrzeit als String |  |  | 6530 |
| [dateyear](func/datums-und-zeitfunktionen/dateyear/index.md) | Erzeugt aus einem Datum als Ganzzahl das Jahr |  |  | 6530 |
| [datemonth](func/datums-und-zeitfunktionen/datemonth/index.md) | Erzeugt aus einem Datum als Ganzzahl das Monat |  |  | 6530 |
| [dateday](func/datums-und-zeitfunktionen/dateday/index.md) | Erzeugt aus einem Datum als Ganzzahl den Tag |  |  | 6530 |
| [datehour](func/datums-und-zeitfunktionen/datehour/index.md) | Erzeugt aus einem Datum als Ganzzahl die Stunde |  |  | 6530 |
| [dateminute](func/datums-und-zeitfunktionen/dateminute/index.md) | Erzeugt aus einem Datum als Ganzzahl die Minute |  |  | 6530 |
| [datesecond](func/datums-und-zeitfunktionen/datesecond/index.md) | Erzeugt aus einem Datum als Ganzzahl die Sekunde |  |  | 6530 |
| [datemix](func/datums-und-zeitfunktionen/datemix/index.md) | Erzeugt aus einem Datumswert (Sekunden seit 1.1.00 0:00:00) einen Vektor mit Jahr,Monat,Tag,Stunde,Minute,Sekunde |  |  | 6641 |
| [datediff](func/datums-und-zeitfunktionen/datediff/index.md) | Rechnet die Differenz von 2 ganzzahligen Datumswerten. Erstes minus zweites Datum. Ergebnis als Double in Sekunden |  |  | 6530 |
| [dateweekday](func/datums-und-zeitfunktionen/dateweekday/index.md) | Liefert den Wochentag beginnend mit Montag als 1 und Sonntag als 7 |  |  | 6530 |
| [dateweek](func/datums-und-zeitfunktionen/dateweek/index.md) | Liefert die Kalenderwoche des Tages innerhalb des Jahres |  |  | 6530 |
| [datedayofyear](func/datums-und-zeitfunktionen/datedayofyear/index.md) | Liefert den Tag des Jahres |  |  | 6530 |
| [years](func/datums-und-zeitfunktionen/years/index.md) | Erzeugt aus einem Sekundenwert die Jahre (/365d) als Double ohne Einheit |  |  | 6530 |
| [months](func/datums-und-zeitfunktionen/months/index.md) | Erzeugt aus einem Sekundenwert die Monate (/30d) als Double ohne Einheit |  |  | 6530 |
| [weeks](func/datums-und-zeitfunktionen/weeks/index.md) | Erzeugt aus einem Sekundenwert die Wochen (/7d) als Double ohne Einheit |  |  | 6530 |
| [days](func/datums-und-zeitfunktionen/days/index.md) | Erzeugt aus einem Sekundenwert die Tage als Double ohne Einheit |  |  | 6530 |
| [hours](func/datums-und-zeitfunktionen/hours/index.md) | Erzeugt aus einem Sekundenwert die Stunden als Double ohne Einheit |  |  | 6530 |
| [minutes](func/datums-und-zeitfunktionen/minutes/index.md) | Erzeugt aus einem Sekundenwert die Minuten als Double ohne Einheit |  |  | 6530 |
| [seconds](func/datums-und-zeitfunktionen/seconds/index.md) | Erzeugt aus einem Sekundenwert die Sekunden als Double ohne Einheit |  |  | 6530 |


####  Spezialfunktionen LeTTo

| Funktion | Beschreibung                                                                                                       | Beispiel  | Ergebnis |
|----------|--------------------------------------------------------------------------------------------------------------------|-----------|----------|
| [points](func/spezialfunktionen-letto/points/index.md) | Berechnet die erreichbare Gesamtpunkteanzahl einer Frage [DEMO-Beispiel](../../demobsp.html?id=3498) | points() | 2 |
| [points](func/spezialfunktionen-letto/points/index.md) | Berechnet die erreichbare Punkteanzahl einer Teilfrage. Als Parameter wird die Fragenummer als Ganzzahl angegeben. | points(0) | 1 |
| [parser](func/spezialfunktionen-letto/parser/index.md) | Markierungsfunktion für Ausdrücke, die von Maxima unverändert an den internen Parser weitergereicht werden sollen. Im internen Parser selbst wird lediglich der einzelne Parameter ausgewertet. | parser(x+1) | x+1 |
| [declare](func/spezialfunktionen-letto/declare/index.md) | Deklariert Variablentypen für die Maxima-Kompatibilität. Die Funktion ist im internen Parser derzeit noch nicht funktional umgesetzt und liefert dort `false`. | declare(x,real) | false |
| [selective_kill](func/spezialfunktionen-letto/selective-kill/index.md) | Löscht alle Variablen aus dem Variablenspeicher außer den angegebenen Variablen bzw. Variablenvektoren und liefert die Anzahl der gelöschten Variablen. | selective_kill(x,y) | Anzahl der gelöschten Variablen |
| [stackoverflow](func/spezialfunktionen-letto/stackoverflow/index.md) | **Test-/Diagnosefunktion:** erzeugt absichtlich einen StackOverflow. Nicht für reguläre Aufgaben verwenden. | stackoverflow() | Fehler |
| [runtimeexception](func/spezialfunktionen-letto/runtimeexception/index.md) | **Test-/Diagnosefunktion:** erzeugt absichtlich eine RuntimeException. Ein optionaler Parameter wird als Fehlermeldung verwendet. | runtimeexception("Test") | Fehler |
| [infiniteloop](func/spezialfunktionen-letto/infiniteloop/index.md) | **Test-/Diagnosefunktion:** erzeugt absichtlich eine Endlosschleife und dient zum Testen der Timeout-Behandlung. Nicht für reguläre Aufgaben verwenden. | infiniteloop() | Timeout |
| [delay](func/spezialfunktionen-letto/delay/index.md) | **Test-/Diagnosefunktion:** verzögert die Auswertung um die angegebene Anzahl Sekunden und prüft dabei regelmäßig auf einen Timeout/Abbruch. | delay(1) | nach ca. 1 s |


#### Spezialfunktionen Technik

| Funktion   | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                      | Beispiel                          | Ergebnis                   |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|----------------------------|
| [color](func/spezialfunktionen-technik/color/index.md) | Widerstandsfarbcode berechnen.<br>1. Parameter muss ein Double sein<br> 2. Parameter sind die Anzahl der Farbringe<br> 3. Parameter ist der Darstellungsmodus (0 = Deutsch ausgeschrieben, 1 = Abkürzung Deutsch mit drei Buchstaben, 2 = Abkürzung Deutsch mit zwei Buchstaben, 3 = Englisch ausgeschrieben, 4 = Abkürzung Englisch mit drei Buchstaben, 5 = Abkürzung Englisch mit zwei Buchstaben) [DEMO-Beispiel](../../demobsp.html?id=3499) | color(120,3,0) | braun,rot,braun |
| [parsecolor](func/spezialfunktionen-technik/parsecolor/index.md) | Wandelt einen String mit einem Widerstandsfarbcode in einen Double-Wert [DEMO-Beispiel](../../demobsp.html?id=3500) | parsecolor("br-rt-br") | 120 |
| [ip](func/spezialfunktionen-technik/ip/index.md) | Wandelt eine Long-Zahl in einen String als IP-Adresse um, oder 4 Byte-Zahlen in eine Long Zahl als IP-32-bit-Adresse [DEMO-Beispiel](../../demobsp.html?id=3501) | ip(1534536453)<br>ip(10,20,30,40) | "91.119.43.5"<br>169090600 |
| [parseip](func/spezialfunktionen-technik/parseip/index.md) | Wandelt einen String mit einer IP-Adresse in einen Long-Wert [DEMO-Beispiel](../../demobsp.html?id=3502) | parseip("91.119.43.5") | 1534536453 |
| [e12](func/spezialfunktionen-technik/e12/index.md) | rundet einen Zahlenwert auf den nächstliegenden Wert der [Normreihe](../Normreihe/index.md) E12.<br>Die Rundung erfolgt geometrisch d.h. der Quotient zwischen Normwert und zu rundendem Wert wird minimiert. [DEMO-Beispiel](../../demobsp.html?id=3503) | e12(700Ohm) | 680Ohm |
| [e12up](func/spezialfunktionen-technik/e12up/index.md) | rundet einen Zahlenwert auf den nächstgrößerern Wert der [Normreihe](../Normreihe/index.md) E12 [DEMO-Beispiel](../../demobsp.html?id=3504) | e12(670Ohm) | 680Ohm |
| [e12down](func/spezialfunktionen-technik/e12down/index.md) | rundet einen Zahlenwert auf den nächstkleineren Wert der [Normreihe](../Normreihe/index.md) E12 [DEMO-Beispiel](../../demobsp.html?id=3505) | e12(700Ohm) | 680Ohm |
| [ise12](func/spezialfunktionen-technik/ise12/index.md) | prüft ob der als Parameter übergebenen Wert ein Wert der [Normreihe](../Normreihe/index.md) E12 ist. [DEMO-Beispiel](../../demobsp.html?id=3506) | ise12(680Ohm) | true |
| [norm](func/spezialfunktionen-technik/norm/index.md) | rundet einen Zahlenwert auf den nächstliegenden Wert einer gegebenen Wertereihe oder [Normreihe](../Normreihe/index.md).<br>Die Rundung erfolgt geometrisch wenn es sich um eine logarithmisch aufgeteilte Normreihe handelt, oder sonst linear. [DEMO-Beispiel](../../demobsp.html?id=3507) | norm(700Ohm,E12) | 680Ohm |
| [normup](func/spezialfunktionen-technik/normup/index.md) | rundet einen Zahlenwert auf den nächstgrößerern Wert einer gegebenen Wertereihe oder [Normreihe](../Normreihe/index.md). [DEMO-Beispiel](../../demobsp.html?id=3508) | normup(730Ohm&#91;1,3,5,8&#93;) | 800Ohm |
| [normdown](func/spezialfunktionen-technik/normdown/index.md) | rundet einen Zahlenwert auf den nächstkleineren Wert einer gegebenen Wertereihe oder [Normreihe](../Normreihe/index.md). [DEMO-Beispiel](../../demobsp.html?id=3509) | normdown(700Ohm,E12) | 680Ohm |
| [isnorm](func/spezialfunktionen-technik/isnorm/index.md) | prüft ob der als Parameter übergebenen Wert ein Wert einer gegebenen Wertereihe oder [Normreihe](../Normreihe/index.md) ist. [DEMO-Beispiel](../../demobsp.html?id=3511) | isnorm(680Ohm,E12) | true |


#### Raumzeiger für elektrische Maschinen

| Funktion                                                       | Beschreibung                                                                                                                                                                                                          | Beispiel                                  | Ergebnis                   |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|----------------------------|
| [svphtosv](func/raumzeiger-fuer-elektrische-maschinen/svphtosv/index.md)(a,b,c) | berechnet aus den Stranggrößen (a,b,c) einen komplexen Raumzeiger [DEMO-Beispiel](../../demobsp.html?id=3512) | svphtosv(0.5,0.5,-1) | 1arg60° |
| [svsvtoph](func/raumzeiger-fuer-elektrische-maschinen/svsvtoph/index.md)(sv)<br>svsvtoph(sv,index) | berechnet aus einem komplexen Raumzeiger die Stranggrössen <br> berechnet aus einem komplexen Raumzeiger die Stranggrössen, index selektiert Stranggröße als Rückgabewert [DEMO-Beispiel](../../demobsp.html?id=3513) | svsvtoph(1arg60°)<br> svsvtoph(1arg60°,3) | &#91;0.5,0.5,-1&#93; <br> -1 |


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

