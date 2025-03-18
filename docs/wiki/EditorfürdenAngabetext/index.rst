Der Editor basiert auf dem [https://ckeditor.com/ckeditor-4/ CKEditor] und dient zum Erstellen des Fragetextes.
Die Angabe für die Frage kann im Editor vernünftig formatiert werden, es können Bilder zur Frage gekoppelt werden sowie die [[Plugins]] eingebunden werden. Die Einbindung von Variablen und Datensätzen erfolgt ebenfalls im Angabetext. Für schön formatierte mathematische Formeln kann eine TEX-Syntag in der Angabestellung verwendet werden.
==Toolbar des Editors für den Angabetext==
[[Datei:ClipCapIt-180831-150726.PNG|500px]]
Über den Toolbar des Editors können Sie mit den Icons 
* [[Datei:ClipCapIt-180831-151417.PNG|80px]]: Umschalten zwichen HTML-Ansicht und der Vorschau
* [[Datei:ClipCapIt-180831-151453.PNG|50px]]: Im Fragetext nach Wörten suchen bzw. Inhalte ersetzten
* [[Datei:ClipCapIt-180831-151645.PNG|70px]]: Zeichen Fett, Kursiv oder Unterstrichen formatieren
* [[Datei:ClipCapIt-180831-151757.PNG|50px]]: Formatierung kopieren und entfernen
* [[Datei:ClipCapIt-180831-151847.PNG|50px]]: Numerierte Listen und Listen erstellen
* [[Datei:ClipCapIt-180831-170748.PNG|25px]]: Tabelle einfügen und formatieren
* [[Datei:ClipCapIt-180831-170829.PNG|25px]]: Horizontale Trennlinie einfügen
* [[Datei:ClipCapIt-180831-170909.PNG|25px]]: Sonderzeichen einfügen
* [[Datei:ClipCapIt-180831-170932.PNG|25px]]: Bild in den Fragetext einfügen
* [[Datei:ClipCapIt-180831-170942.PNG|25px]]: Bild löschen, wenn der Cursor auf einem Image-Tag [IMG...] steht.
* [[Datei:ClipCapIt-180831-170951.PNG|25px]]: Neue Teilfrage in einer Mehrfachberechnungsfrage einfügen
* [[Datei:ClipCapIt-180831-171001.PNG|25px]]: Teilfrage löschen, wenn der Cursor auf einem Teilfrage-Tag [Q...] steht.
* [[Datei:ClipCapIt-180831-171032.PNG|130px]]: Absatzformate definieren, Textfarbe und Hintergrundfarbe auswählen

==Kontext-Menü des Editors==
:[[Datei:ClipCapIt-180831-175632.PNG|thumb|200px]]
====Einfügen:====
Einfügen des Inhalts der Zwischenablage. Wenn in der Zwischenablage ein Bild gespeichert ist, dann wird das Bild in der Frage gespeichert und der entsprechende zugordnete IMG-Tag an der Cursor-Position eingefügt.
====Bild von Datei einbinden:====
Es wird ein Diolog zur Datei-Auswahl geöffnet und nach Auswahl des Bildes dieses zur Frage hinzugefügt und der IMG-Tag an der Cursor-Position eingefügt.

Alle Dateien, die in der Frage verwendet werden können, können auch über den Dialog [[Dateien zur Frage verwalten]] verwaltet werden. 
Auch das manuelle Eintippen von [IMG...]-tags ist möglich, wenn Sie die den Tag des Bildes aus obigem Dialog ermittelt haben.

====Listing einfügen (CTRL-L)====
Einfügen eines Listings, siehe auch [[#Listing|hier]].
====Freihandskizze einfügen (CTRL-F)====
Öffnen einer Möglichkeit zum Erstellen von einfachen Freihand-Skizzen, die dann als Image zur Frage gebunden werden können.
:[[Datei:ClipCapIt-180831-172611.PNG|400px]]
====Datensatz ergänzen (F2)====
Anlegen eines Datensatzes, die Variablenbezeichnung wird aus dem Wort der akt. Cursorposition abgeleitet. Die Variable wird in geschwungene Klammern gesetzt. Bp.: An der Cursorposition (vor dem Cursor) steht "U2". Es wird ein Datensatz (Variable) mit dem Namen U2 mit der Einheit Volt erzeugt und an der Cursorposition wird U2 durch {U2} ersetzt.
====Datensatz als Formel ergänzen (F3)====
Anlegen eines Datensatz wie oben, die Variable wird mit einer Zuweisung in einer Formel gesetzt. 
Bp.: aus "U1 &lt;F3&gt;" wird $U_1 = {U1}$
====Neue Teilfrage (STRG-Q)====
Verwendung bei [[Mehrfachberechnungsfrage|Mehrfachberechnungsfragen]]: Im Angabetext wird ein TAG für neue Teilfrage an der Cursorposition  gesetzt und eine neue Teilfrage wird erzeugt und im Detailbereich der Mehrfachberechnungsfrage angezeigt. Der [Q...]-Tag liefert dann in der fertigen Frage ein Eingabefeld zur Lösungseingabe. Die Ergebnisse der Teilfge sind im Detailbereich der Frage zu definieren.

====Aktuellen Tag löschen (STRG-DEL)====
Wenn der Cursor auf oder hinter einem TAG steht, dann wird der tAG und die zugehörige Information gelöscht:
zB: [IMG...]-Tag: Der Tag verschwindet und das Bild wird aus der Datenbank gelöscht.
[Q...]-Tag: Die zugehörige Teilfrage wird gelöscht.
====Plugin====
Wenn in der Frage [[Plugins]] definiert sind, dann können auch über das Kontext-Menü pluginspezifische Teile eingefügt werden. Pro definiertem Plugin wird eine Zeile im Kontext-Menü hinzugefügt. Die Menü-Einträge enthalten Namen und Art des Plugins. Je nach gewähltem Plugin unterscheiden sich die Untermenüs stark.

==Formeln==
Formeln werden innerhalb von '''Dollarzeichen''' gesetzt und können dann wie eine Formel in LaTeX gesetzt werden:
zB. liefert '''$k = \sum_{i=1}^{n} (i+2)$''' die Formel im Browser: [[Datei:ClipCapIt-180620-200224.PNG|110px]]

Tutorial zum Erstellen von Tex-Formeln: https://de.wikipedia.org/wiki/Hilfe:TeX

==HTML-Tags==
Im Fragetext können nur die folgenden HTML-Tags verwendet werden, alle anderen Tags werden automatisch entfernt und sollten deshalb nicht verwendet werden.

zulässige HTML-Tags:
{| class="wikitable"
| '''name''' || '''Funktion''' 
|+
| [https://www.w3schools.com/tags/tag_html.asp html] || HTML-Seite
|+ 
| [https://www.w3schools.com/tags/tag_head.asp head] || HTML-Seitenkopf
|+
| [https://www.w3schools.com/tags/tag_body.asp body] || HTML-Seitenrumpf
|+
| [https://www.w3schools.com/tags/tag_a.asp a] || Link
|+
| [https://www.w3schools.com/tags/tag_hr.asp hr] || horizontale Linie
|+
| [https://www.w3schools.com/tags/tag_br.asp br] || neue Zeile
|+
| [https://www.w3schools.com/tags/tag_p.asp p] || Absatz
|+
| [https://www.w3schools.com/tags/tag_span.asp span] || Tag zum Gruppieren und Formatieren mit CSS
|+
| [https://www.w3schools.com/tags/tag_table.asp table] || Tabelle
|+
| [https://www.w3schools.com/tags/tag_tbody.asp tbody] || Hauptbereich einer Tabelle
|+
| [https://www.w3schools.com/tags/tag_thead.asp thead] || Kopfbereich einer Tabelle
|+
| [https://www.w3schools.com/tags/tag_tfoot.asp tfoot] || Fußbereich einer Tabelle
|+
| [https://www.w3schools.com/tags/tag_tr.asp tr] || Tabellenzeile
|+
| [https://www.w3schools.com/tags/tag_td.asp td] || Tabellenzelle
|+
| [https://www.w3schools.com/tags/tag_th.asp th] || Tabellen-Kopf-Zelle
|+
| [https://www.w3schools.com/tags/tag_img.asp img] || Bild
|+
| [https://www.w3schools.com/tags/tag_area.asp area] || Bereich in einem Bild
|+
| [https://www.w3schools.com/tags/tag_ul.asp ul] || unsortierte Liste
|+
| [https://www.w3schools.com/tags/tag_ol.asp ol] || sortierte Liste
|+
| [https://www.w3schools.com/tags/tag_li.asp li] || Listenelement
|+ 
| [https://www.w3schools.com/tags/tag_div.asp div] || Bereich eines Dokuments
|+
| [https://www.w3schools.com/tags/tag_pre.asp pre] || vorformatierter Text mit fixer Schrift
|+
| [https://www.w3schools.com/tags/tag_b.asp b] || Fettschrift
|+
| [https://www.w3schools.com/tags/tag_i.asp i] || Kursivschrift
|+
| [https://www.w3schools.com/tags/tag_u.asp u] || Unterstrichen
|+
| [https://www.w3schools.com/tags/tag_s.asp s] || Text ist nicht mehr länger gültig (durchgestrichen)
|+
| [https://www.w3schools.com/tags/tag_strong.asp strong] || Wichtiger Text (Fett)
|+
| [https://www.w3schools.com/tags/tag_em.asp em] || Hervorgehoben (kursiv)
|+
| [https://www.w3schools.com/tags/tag_hn.asp h1,h2,h3,h4,h5,h6] || Überschriften
|+
| [https://www.w3schools.com/tags/default.asp abbr] || Acronym
|+
| [https://www.w3schools.com/tags/tag_audio.asp audio] || Audio-Datei
|+
|}

==Spezielle TAGs im Fragentext==
{| class="wikitable"
| Tagbezeichnung || Beschreibung
|+
| [listing]  ||  Tag zum Einfügen von Programm-Listings in den Angabetext einer Frage. Zwischen dem Start mit [listing]  und dem Ende mit [/listing] befindet sich dann der Programmcode, der speziell formatiert wird. Dies erreicht man am besten über die rechte Maustaste "Listing einfügen" oder mit STRG-L
|+
| [IMG0]     ||  Platzhaltersymbol für eine Grafik: Alle Grafiken werden als Dateien an die Frage angeschlossen und mit dem IMG-Tag zur Anzeige gebracht. Die Dateien, die in der Frage verwendet werden können, können über den Dialog [[Dateien zur Frage verwalten]] verwaltet werden. Details: Siehe Bilder
|+
| [LINK0 text] || Link auf eine Datei aus der Dateiliste der Frage. Der Text wird als Link-Text angezeigt.
|+
| [Q0]       ||  Referenz auf eine Teilfrage eine [[Mehrfachberechnungsfrage]]. Der [Q...]-Tag liefert dann in der fertigen Frage ein Eingabefeld zur Lösungseingabe für diese Teilfrage
|+
| [PIG ..]   || Tag zum Einbinden einer Grafik, die von einem [[Plugins|Plugin]] zur Laufzeit erzeugt wird.
|}

==Bilder==
Bilder werden im Editor durch ein Image-Tag [IMG0], [IMG1], etc. als Platzhalter angezeigt. Grafiken werden als Dateien an die Frage angeschlossen und mit dem IMG-Tag zur Anzeige gebracht. 
Die Vorschau des Bildes wird im linken unteren Vorschaufenster angezeigt, wenn der Image-Tag angeklickt wird.

'''Einfügen von neuen Bildern: ''' 
* Images aus der Zwischenablage können über ''CTRL-V'' eingefügt werden. Das Bild wird als Datei an die Frage angehängt und der entsprechende [IMG]-Tag wird eingefügt.
* Über den Toolbar des Editors mit dem Button [[Datei:ClipCapIt-180620-202922.PNG|22px]]: Ein Dialog zum Auswählen einer Grafik wird angezeigt, nach erfolgter Auswahl wird der [IMG]-Tag und die Datei eingefügt.

==Schnelleingabe / Tastatur-Shortcuts==
* F2: Tippt man nach der Eingabe eines Variablennamens die Funktionstaste F2, so wird ein Datensatz angelegt und die Variable wird in geschwungene Klammern gesetzt zB.: aus "U2 &lt;F2&gt;" wird {U2}
* F3: Tippt man nach der Eingabe eines Variablennamens die Funktionstaste F3, so wird ein Datensatz angelegt und die Variable mit einer Zuweisung in einer Formel gesetzt zB. aus "U1 &lt;F3&gt;" wird $U_1 = {U1}$
* F8: Nur bei Lückentextfragen: Mit F8 kann das aktuelle Wort, bei dem der Cursor steht, als Textlücke definiert werden.
* CTRL-L: Einfügen eines Textbereichs für Programm-Listings
* CTRL-F: Einfügen einer Freihandskizze
* CTRL-Q: Einfügen einer neuen Teilfrage bei [[Mehrfachberechnungsfrage|Mehrfachberechnungsfragen]]
* CTRL-DEL: Aktuellen Tag löschen, wenn der Cursor auf einem Tag mit eckigen Klammern steht.

Wird eine [[Datensätze|Variable]] direkt in geschwungene Klammern gesetzt, so wird nach dem Verlassen des Editors geprüft, ob die Variable schon vorhanden ist und diese wird gegebenenfalls neu angelegt.

Die Grafiken von [[Plugins]] werden im Editor ebenfalls durch Plugin-Tags mit Platzhaltern angezeigt.

==Listings==
Sourcecode Listings müssen innerhalb von Listings-Tags gesetzt werden. Dies erreicht man am Besten über die rechte Maustaste "Listing einfügen" oder mit STRG-L.

Im Start-Tag des Listings kann auch mit dem Parameter lang="C" eine gewünschte Programmiersprache angegeben werden. Diese Angabe wird dann beim Druck an das LaTeX Listings-Packet geschickt, online wird diese Angabe ignoriert.

Innerhalb von Listings können natürlich auch Variable verwendet werden, die dann wie im Rest des Textes ersetzt werden.

== Sonderzeichen ==
* Bis auf einige Ausnahmen können im Fragetext alle Zeichen des UTF-8-Zeichensatzes verwendet werden.
* Spezielle Sonderzeichen des CK-Editors können mit dem Button :[[Datei:ClipCapIt-220113-153145.PNG]] eingefügt werden
* Folgende Zeichen haben im Fragetext eine Sonderstellung und müssen deshalb teilweise gesondert behandelt werden:
{| class="wikitable"
! Zeichen !!  Bezeichnung !! Funktion   !!  Verwendung im Fragetext
|-
| $ || Dollar || Start und Ende einer Formelumgebung im Fragetext || \$
|-
| { || geschwungene Klammer || Variablen und Berechnungsfeld || wird nur als Variablenklammer interpretiert wenn dazu eine gültige Variable gefunden wird, ggf. nach der Klammer ein Leerzeichen einfügen
|-
| &lt; || kleiner Zeichen || HTML-Tag-Begrenzer || wird durch den CK-Editor automatisch in die Entity &amp;lt; gewandelt und ist deshalb normal verwendbar
|-
| &gt; || kleiner Zeichen || HTML-Tag-Begrenzer || wird durch den CK-Editor automatisch in die Entity &amp;gt; gewandelt und ist deshalb normal verwendbar
|-
| [ || eckige Klammer || Frage, Bild, Link Begrenzer || Kann normal verwendet werden wird nur bei einem gültigen Tag IMG,LINK,Q,... ausgewertet
|-
|}

== Sonderzeichen in einer Formelumgebung im Fragetext ==
* Eine Formelumgebung beginnt im Fragetext mit Dollar und endet mit Dollar. Dazwischen wird der Text als Formel wie in LaTeX gesetzt. 
* Sonderzeichen werden dabei wie folgt angegeben:
{| class="wikitable"
! Zeichen !! Verwendung in der Formelumgebung
|-
| $ || \$ 
|-
| { || \{
|-
| } || \}
|-
| _ || \_
|-
| ^ || \^
|-
| # || \#
|-
| ~ || \sim
|-
| \ || \backslash
|-
| x² || x^2
|-
| x³ || x^3
|-
| % || \%
|}

==Datensätze und Variable==
Die Verwendung von Datensätzen oder Ergebnissen von Berechnungen erfolgt immer über geschwungene Klammern!

Datensatz erstellen: siehe [[Datensätze definieren]], [[Datensätze definieren#Erstellung aus dem Editor|Eingabe im Editor]]

Alle  Datensätze, die bei der Frage definiert wurden sowie alle Ergebnisse der Maxima-Berechnung können im Fragetext innerhalb oder außerhalb von Tex-Formeln verwendet werden.

{| class="wikitable"
! Bezeichnung 	!!  Syntax !!  Beispiel   !!  Beschreibung
|-
| Variable, die in einem Datensatz definiert wurde  ||  {name}  ||  {x}  ||  x wird duch den Wert des Datensatzes ersetzt
|-
| Variable mit Einheit  ||  {name,einheit}  ||  {I1,A}  ||  I1 wird mit der Einheit A mit gültigen Einheitenvielfachen von A ausgegeben
|-
| Variable mit erzwungener Einheit  ||  {name,=einheit}  ||  {I1,=mA}  ||  I1 wird mit mA ausgegeben, es wird nicht nach besseren Einheitenvielfachen gesucht
|-
| Variable mit definierter Genauigkeit  ||  {name,ziffern}  ||  {I1,2}  ||  I1 wird auf 2 gültige Ziffern gerundet und ausgegeben
|-
| Variable mit definierter Genauigkeit und erzwungener Einheit  ||  {name,=einheit,ziffern}  ||  {U1,=mV,3}  ||  U1 wird auf 3 gültige Ziffern gerundet und in mV ausgegeben. ( siehe [[Einheit]], [[Zahlendarstellung]] )
|-
| konstanter Wert  ||  name={wert,einheit}  ||  U_2={5,V}  ||  der konstante Wert von U2 ist 5V, und kann in Maxima und für alle Ergebnisse verwendet werden
|-
| symbolischer Wert, der in Maxima berechnet wurde  ||  {=name}  ||  {=y}  ||  setzt in die Variable y, die in Maxima berechnet wurde, die Datensätze ein und gibt das Ergebnis aus, wobei nur numerische Optimierungen vorgenommen werden
|-
| symbolischer Ausdruck  ||  {=ausdruck}  ||  {=x+y}  ||  berechnet den Ausdruck x+y und setzt alle Ergebnisse aus den Maxima-Berechnungen und alle Datensätze in den Ausdruck ein
|-
| symbolischer Ausdruck mit Auswertung  ||  {=ev(ausdruck)}  ||  {=ev(x+y)}  ||  setzt alle Maxima-Ergebnisse in den Ausdruck ein, und setzt danach noch alle Datensätze ein
|-
| symbolischer Wert/Ausdruck ohne Vereinfachung  ||  {=:name}  ||  {=:y}  ||  gibt die Variable y, welche in Maxima berechnet wurde, exakt so, wie sie berechnet wurde aus. Soll in Maxima nichts berechnet werden, so ist dort die Funktion noopt() zu verwenden
|-
| symbolischer Wert mit voller Optimierung  ||  {=opt:name}  ||  {=opt:y}  ||  setzt in den Ausdruck y, welcher in Maxima berechnet wurde, alle Datensätze ein und optimiert das Ergebnis so stark wie möglich
|-
| symbolscher Wert mit Einheit und Genauigkeit  ||  {=ausdruck;=einheit,ziffern}  ||  {=y;=mV,3}  ||  setzt in den Ausdruck y, welcher in Maxima berechnet wurde, alle Datensätze ein und gibt in mV mit 3 gültigen Ziffern aus.
|-
| Datensatz - Vektor  ||  {name}  ||  {v}  ||  Vektoren werden normal als Spaltenvektor dargestellt 
|-
| Zeilenvektor  ||  {name,line}  ||  {v,line}  ||  Vektor als Zeilenvektor: (1/2/3)
|-
| Vektor in Eingabedarstellung  ||  {name,input}  ||  {v,input}  ||  Vektor wird so dargestellt, wie er eingegeben werden kann: [1,2,3]
|-
| Matrix  ||  {name}  ||  {M}  ||  Darstellungsmodi von Matrizen sind gleich wie bei Vektoren
|}

==Beispiele==

Nachfolgende Beispiele basieren auf zwei Datensätze a und b:

[[Datei:Datensatz_a_b.png]]

{| class="wikitable"
! Angabetext 	!!  Kommentar !! Darstellung 
|-
| $\dfrac { a}{ b}$  ||  Die Leerzeichen sind mit anzugeben || [[Datei:Bruch_1.png]]
|-
| $\dfrac &amp;#123;&amp;#123;a&amp;#125;&amp;#125;&amp;#123;&amp;#123;b&amp;#125;&amp;#125;$  ||  Einsetzen der Datensatz-Werte || [[Datei:Bruch_2.png]]
|}

