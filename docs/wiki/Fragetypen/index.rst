siehe auch [[Beispielsammlung]] und [[Beispielsammlung Editieren]]

= [[Beispielsammlung_Editieren#Mehrfachberechnungsfrage|Mehrfachberechnungsfrage]] = 
[https://youtu.be/z_xfPxh33hA Video]
* Fragen dieses Typs sind sehr flexibel. 
* Die Frage kann mehrere Teilantworten beinhalten. Jede Teilfrage wird im Fragetext durch einen [Qx]-Tag (x..Fragenummer) positioniert. Bei der Schülereingabe wird der Tag durch ein Eingabefeld für die Ergebniseingabe ersetzt.
* Die Angabewerte sind wie bei Berechnungsfragen mittels Datensätzen definierbar und variieren von Schüler zu Schüler.
* Alle verwendeten Variablen müssen im Angabetext in geschwungene Klammern gesetzt werden. Im Maximafeld und im Lösungsfeld ist die Klammer nicht notwendig.
* Für jede Variable wird ein Dataset mit möglichen Werten angelegt. Diese Datasets können über einen Formatierungsstring definiert werden und danach auch direkt in einer Liste bearbeitet werden.

[[Berechnungen]]

= [[Beispielsammlung_Editieren#Zuordnungsfrage|Zuordnungsfrage]] =
[https://youtu.be/UUfoF03YkFM Video]

Die Antwort auf jede der Unterfragen muss aus einer Liste von Möglichkeiten ausgewählt werden.Bei der Zuordnungsfrage können die Begriffe auf der linken und auf der rechten Seite gemischt werden. Im Prinzip hat der Schüler 2 Listen mit Antworten und Fragen, die er richtig zuordnen muss. Geben Sie in den beiden Listen Elemente an, welche keine korrekten Zuordnungen haben sollen, dann ist die entsprechende Zelle in der Tabelle ohne Eintrag zu verwenden. Es können Bsp. der Variante 2 aus 5 oder 4 aus 8 sehr schnell und einfach erstellt werden. 
:[[Datei:ClipCapIt-200504-112206.PNG|300px|thumb|right||Lehrersicht (Editiermodus) der Zuordnungsfrage]]
:[[Datei:ClipCapIt-200504-112850.PNG|300px|thumb|right||Schüleransicht Zuordnungsfrage]]

Dem Schüler stehen zwei unterschiedliche Modi zur Fragenbeantwortung zur Verfügung:
* drag &amp; drop
* klick-klick

Moduswechsel erfolgt durch den Schüler zur Laufzeit des Tests mit einem Klick auf das Symbol [[Datei:ClipCapIt-200504-113148.PNG]]. Der Schüler kann den Modus beliebig oft wechseln.

Für eine dynamische Fragenerstellung ist es möglich Werte aus dem Maximaberechnungsfeld oder auch Werte aus Datensätzen zu benutzen. Bsp: Eine Variable mit der Bezeichnung "wert" soll eingesetzt werden. Diese ist mit "{=wert}" in die Tabelle der Zuorndungsfrage einzutragen. 
:[[Datei:ClipCapIt-200504-114756.PNG]]

Die Variable "wert" kann jetzt aus einem Datensatz oder aber auch als Berechnung aus dem Maximafeld stammen.
Als Angabe bzw. Lösungen werden auch Bilder unterstützt. Diese sind in der betreffenden Zelle der Tabellen einfach mit STRG+V (wenn das Bild im Zwischenspeicher ist) oder über Klick der rechten Maustaste auf die entsprechende Zelle und dem Menüpunkt Image einfügen, einzubinden.

= [[Beispielsammlung_Editieren#Multiple-Choice-Frage|Multiple-Choice-Frage]] = 

[https://youtu.be/NLEePJMMWoE Video]

Vorteil dieses Fragentyps
* Fragen sind schnell erstellt
* dynamische Bsp-Gestaltung möglich
* Bilder in Frage und Antwort möglich
* schnelle Beantwortung durch Schüler beim Test 

Nach Forumulierung der Frage werden die möglichen Antworten in Form einer Tabelle definiert. Die Selektion der korrekten Antworten erfolgt durch Markieren der selbigen.
:[[Datei:ClipCapIt-200504-115517.PNG|300px|thumb|right||Lehrersicht (Editiermodus) der Multiple-Choice-Frage]]
:[[Datei:ClipCapIt-200504-115649.PNG|300px|thumb|right||Schüleransicht der Multiple-Choice-Frage]]
Für eine dynamsiche Beispielgestaltung können Werte aus definierten Datensätzen aber auch Werte aus dem Maximafeld als Antwort defniert werden - siehe Vorgangsweise Zuordnungsfrage.



= [[Beispielsammlung_Editieren#Freitextfrage|Freitextfrage]] =
[https://youtu.be/drhmdWO2PAE Video]

Vorteile der Freitextfrage sind
* Frage schnell erstellt
* dynamische Fragengestalltung ist möglich
* Beantwortung ist handschriftlich möglich --&gt; Upload von Kammerafoto
* Bilder aus Zwischenablage können vom Schüler zur Beantwortung der Frage genutzt werden
* Enzyklopädisches Wissen kann abgefragt werden
* Subjektiver Einfluss der Beurteilung durch die Schülerhandschrift kann entfallen
* Einheitliches Fragenlayout bei der Verwendung der Frage in einem klassischen Test (=Test auf Papier) --&gt; Frage in LeTTo erstellt --&gt; Druck der Frage

Nachteile
* keine Vollautomatische Beurteilung möglich
* Subjektiver Einfluss durch Lehrerkorrektur 
* Schüler verliert zeitnahes Feedback --&gt; Bewertung durch Lehrer erfolgt verspätet

Die Frage wird im Fragentextfenster formuliert. Der Schüler hat dich Möglichkeit die Frage in einem eigenen Textfenster mit Hilfe der Tastatur zu beantworten. Zusätzlich besteht die Möglichkeit Images aus dem Zwischenspeicher für die Beantwortung der Frage zu nutzen.

Enthält die Fragenbeantwortung z.B. Handskizzen, dann sind diese nach deren Anfertigung auf Papier mittels der Funktion "Foto aufnehmen" vom Schüler hochladbar. Diese stehen dem Lehrkörper bei der Beurteilung zur Verfügung.
:[[Datei:ClipCapIt-200504-131942.PNG|300px|thumb|right||Schüleransicht der Freitextfrage]]

= [[Beispielsammlung_Editieren#Berechnungsfrage|Berechnungsfrage]] =

* Berechnende Fragen sind wie die [[#Mehrfachberechnungsfrage|Mehrfachberechnungsfrage]] mit nur einer Teilfrage, bei dem das Antwortfeld automatisch erscheint.
* Jeder Schüler bekommt eine eigene Angabe
* Durch das Drucken kann die Frage auch für Projektangaben verwendet werden (Jeder Schüler hat eigene Angaben).
* [[Berechnungen]] erfolgen mit [[Beispielsammlung Editieren#Maxima-Feld|Maxima]]
* Alle verwendeten [[Datensätze|Variablen]] müssen im Angabtext in geschwungene Klammern gesetzt werden. Im Maximafeld und im Lösungsfeld ist die Klammer nicht notwendig.
* Für jede Variable wird ein [[Datensätze|Datensatz]] mit möglichen Werten angelegt. Diese [[Datensätze|Datasets]] können über einen Formatierungsstring definiert werden und danach auch direkt in einer [[Datensatz-Dialog#Anzeige aller Variablenwerte und Ergebnisse|Liste]] bearbeitet werden.

= [[Beispielsammlung_Editieren#Lückentextfrage|Lückentextfrage]] =
[https://youtu.be/qfj6tPgWl0U Video]

:[[Datei:ClipCapIt-200504-134347.PNG|300px|thumb|right||Lehreransicht (Editiermodus) der Lückentextfrage]]
:[[Datei:ClipCapIt-200504-134545.PNG|300px|thumb|right||Schüleransicht der Lückentextfrage]]

Vorteile der Lückentextfrage sind
* Frage schnell erstellt
* dynamische Fragengestalltung ist möglich
* Einheitliches Fragenlayout bei der Verwendung der Frage in einem klassischen Test (=Test auf Papier) --&gt; Frage in LeTTo erstellt --&gt; Druck der Frage

