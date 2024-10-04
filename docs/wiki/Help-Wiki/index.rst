==Grundlagen==

===Neuer Beitrag===
Ein neuer Wiki-Beitrag wird erzeugt, indem man in einem bestehenden Beitrag den Titel des neuen Beitrags "wikifiziert", also als internen Link kennzeichnet. Das soll bewirken, dass keine isolierten (also nicht verlinkte und kategorisierte) Beiträge entstehen, denn diese sind nur über die Suchfunktion auffindbar. 

Um dennoch einen neuen unverlinkten Beitrag zu erstellen, kann man einen beliebigen Beitrag '''bearbeiten''' (obere Navigationsreiter):
#Ein Klick auf '''Bearbeiten''' öffnet einen Editor im Browser,
#dort gibt man gleich oben den gewünschten Beitragstitel (z.B. &lt;code&gt;&lt;nowiki&gt;[[Vorlage Beitrag]]&lt;/nowiki&gt;&lt;/code&gt;) ein und 
#klickt ganz unten auf '''Vorschau zeigen''' (dadurch wird die Änderung nicht gespeichert, sondern nur ein Link zum noch nicht vorhandenen Beitrag erzeugt.
#In der Vorschau klickt man einfach auf den roten Link mit dem neuen Beitragstitel (z.B. [[Vorlage Beitrag]]) und kommt in ein leeres Editorfenster. (Der editierte Beitrag wird dabei '''nicht''' gespeichert (nur die Vorschau wird angezeigt), daher ist der neu angelegte Beitrag auch nicht verlinkt!)
#Hier sollte man zumindest eine [[#Kategorien|Kategorie]] (üblicherweise ganz unten) eintragen: &lt;code&gt;&lt;nowiki&gt;[[Kategorie:Einführung]]&lt;/nowiki&gt;&lt;/code&gt;.
#Mit '''Vorschau zeigen''' kann man sich das Ergebnis der Eingaben ansehen, ohne die Datenbank mit jeder kleinen Änderung unnötig zu vergrößern.
#Schließlich wird mit '''Seite speichern''' (ganz unten) der Inhalt des Editors in der Datenbank gespeichert (samt Zeitpunkt und Autor|in des Beitrags).
#'''Tipp:''' Jede|r Benutzer|in hat eine "persönliche" Seite. (Diese ist allerdings für alle Benutzer|innen sichtbar!) Ganz oben rechts im Browserfenster sieht man eine Symbolfigur und daneben den Benutzer|innen|namen. Ein Klick darauf, "Bearbeiten" oben im Reiter klicken und schon man kann an seiner ersten Wikiseite arbeiten und die Syntax ausprobieren.


----
__TOC__
 
===Interne Verlinkung===
Wenn man in einem bestehenden Beitrag einen internen Link zu einem '''neuen Begriff (Zielartikel)''' z.B. &lt;code&gt;&lt;nowiki&gt;[[Zielartikel]]&lt;/nowiki&gt;&lt;/code&gt; einfügt, wird mit einem Klick auf den nach dem Speichern rot angezeigten Link automatisch der neue Beitrag im Editor angezeigt.

Soll ein vom Namen des Zielartikels abweichender Text ("Linktitel") angezeigt werden, so ist dies mit Hilfe eines senkrechten Strichs "|" möglich: &lt;code&gt;&lt;nowiki&gt;[[Zielartikel|alternativer Text]]&lt;/nowiki&gt;&lt;/code&gt;. Sollen lediglich Zeichen angehängt werden, so ist diese Schreibweise des &lt;code&gt;&lt;nowiki&gt;[[Zielartikel]]s&lt;/nowiki&gt;&lt;/code&gt; möglich.

Zu einem bestimmten Abschnitt ''innerhalb eines Artikels'' kann mit Hilfe des Raute-Zeichens verlinkt werden: &lt;code&gt;&lt;nowiki&gt;[[Titel#Überschrift des Abschnitts]]&lt;/nowiki&gt;&lt;/code&gt;. Auch hier kann ein alternativer Text nach einem senkrechten Strich eingefügt werden. Soll innerhalb ''desselben'' Artikels verlinkt werden, kann auf die Angabe des Artikelnamens verzichtet werden: &lt;code&gt;&lt;nowiki&gt;[[#Überschrift des Abschnitts|alternativer Text]]&lt;/nowiki&gt;&lt;/code&gt;. Mehr in [https://de.wikipedia.org/w/index.php?title=Hilfe:Links Hilfe:Links].

===Externe Verlinkung===
Eine externe Internetadresse im laufenden Text wandelt die Software automatisch in einen anklickbaren Link um, wenn sie vollständig angegeben wird.
: ''Beispiel:'' http://www.openusability.org/
''Achtung: Ein unmittelbar der URL folgendes Satzzeichen wie Punkt, Komma, Semikolon sowie Fragezeichen und Ausrufezeichen wird als nicht zur URL gehörig betrachtet und bei der automatischen Generierung der Verlinkung nicht einbezogen. In solchen Fällen den Satz umformulieren oder eckige Klammern benutzen.''

In den meisten Fällen sollte man dem Link einen Titel geben; hierzu wird die URL und der Titel gemeinsam in einfache eckige Klammern gesetzt, getrennt durch ein Leerzeichen: &lt;code&gt;&lt;nowiki&gt;[http://www.openusability.org/ Website von OpenUsability]&lt;/nowiki&gt;&lt;/code&gt; ergibt: [http://www.openusability.org/ Website von OpenUsability]

==Textgestaltung==
===Überschriften===
&lt;code&gt;&lt;nowiki&gt;= Überschrift Ebene 1 =&lt;/nowiki&gt;&lt;/code&gt; &lt;br /&gt; &lt;code&gt;&lt;nowiki&gt;== Überschrift Ebene 2 ==&lt;/nowiki&gt;&lt;/code&gt;

===Formate===
Im Wiki wird Text durch Steuerzeichen formatiert:
&lt;code&gt;&lt;nowiki&gt;'''fett'''&lt;/nowiki&gt;&lt;/code&gt; erzeugt '''fett''', &lt;code&gt;&lt;nowiki&gt;''kursiv''&lt;/nowiki&gt;&lt;/code&gt; erzeugt ''kursiv''.

&lt;code&gt;Text &lt;nowiki&gt;&lt;sup&gt;hochgestellt&lt;/sup&gt;&lt;/nowiki&gt;&lt;/code&gt;
| Text &lt;sup&gt;hochgestellt&lt;/sup&gt; und &lt;code&gt;Text &lt;nowiki&gt;&lt;sub&gt;tiefgestellt&lt;/sub&gt;&lt;/nowiki&gt;&lt;/code&gt;
| Text &lt;sub&gt;tiefgestellt&lt;/sub&gt; sind einfach möglich.
----

mehr in der [https://de.wikipedia.org/wiki/Hilfe:Textgestaltung Wikipediahilfe]
----

===Beispiele===

Es gibt verschiedene Möglichkeiten Text auszuzeichnen ([https://de.wikipedia.org/wiki/Wikipedia:Zitate#Layout siehe auch Wikipedia]):

====&lt;nowiki&gt;&lt;tt&gt;Text&lt;/tt&gt;&lt;/nowiki&gt;====
&lt;code&gt;&lt;nowiki&gt;&lt;tt&gt;vorformatierter Text&lt;br&gt;neue Zeile&lt;br&gt;"&amp;_nbsp;" mit einem erzwungenen Leerzeichen am Zeilenanfang&lt;/tt&gt;&lt;/nowiki&gt;&lt;/code&gt; 

Erzeugt:

&lt;tt&gt;vorformatierter Text&lt;br&gt;neue Zeile&lt;br&gt;
&amp;nbsp;mit einem erzwungenen Leerzeichen am Zeilenanfang&lt;/tt&gt;

:&lt;tt&gt;mit : vorformatierter Text&lt;br&gt;neue Zeile&lt;br&gt;Zeilenumbruch kein Problem bei tt!!! Zeilenumbruch kein Problem bei tt!!! Zeilenumbruch kein Problem bei tt!!! Zeilenumbruch kein Problem bei tt!!! &lt;/tt&gt;
----
In Tabellen:

&lt;code&gt;&lt;nowiki&gt;&lt;tt&gt;Beispiel:&lt;/nowiki&gt;&lt;/code&gt;&lt;br&gt;
&lt;code&gt;&lt;nowiki&gt;:{| &lt;/nowiki&gt;&lt;/code&gt;&lt;br&gt;
&lt;code&gt;&lt;nowiki&gt;| Zitat || Zitat&lt;/nowiki&gt;&lt;/code&gt;&lt;br&gt;
&lt;code&gt;&lt;nowiki&gt;|-&lt;/nowiki&gt;&lt;/code&gt;&lt;br&gt;
&lt;code&gt;&lt;nowiki&gt;| Zitat || Zitat&lt;/nowiki&gt;&lt;/code&gt;&lt;br&gt;
&lt;code&gt;&lt;nowiki&gt;|}&lt;/nowiki&gt;&lt;/code&gt;&lt;br&gt;
&lt;code&gt;&lt;nowiki&gt;&lt;/tt&gt;&lt;/nowiki&gt;&lt;/code&gt; 

Erzeugt:

&lt;tt&gt;Beispiel:
:{| 
| Zitat || Zitat
|-
| Zitat || Zitat
|}
&lt;/tt&gt;

====&lt;nowiki&gt;&lt;code&gt;Text&lt;/code&gt;&lt;/nowiki&gt;====
&lt;code&gt;&lt;nowiki&gt;&lt;code&gt;Mit &lt;nowiki&gt;&lt;code&gt;&lt;/nowiki&gt;&lt;nowiki&gt;&lt;/nowiki&gt;&lt;/nowiki&gt; hat man auch eine Möglichkeit Beispiele hervorzuheben. Der Zeilenumbruch macht keinen Ärger. Der Zeilenumbruch macht keinen Ärger. Der Zeilenumbruch macht keinen Ärger. Der Zeilenumbruch macht keinen Ärger.&lt;/nowiki&gt;&lt;nowiki&gt;&lt;/code&gt;&lt;/nowiki&gt;&lt;/code&gt; 

Erzeugt:

&lt;code&gt;Mit &lt;nowiki&gt;&lt;code&gt;&lt;/nowiki&gt; hat man auch eine Möglichkeit Beispiele hervorzuheben.&lt;/code&gt;
----

====Blank am Zeilenbeginn====
 Alternativ geht das auch so (einfach ein Blank am Zeilenanfang). Es entsteht ein Kästchen mit Courier-Schrift im Text. 
 
 Eine Zeile Abstand erzeugt ein neues Kästchen.

===Nummerierung und Bullets===
# Bullet: &lt;code&gt;&lt;nowiki&gt;# eins&lt;/nowiki&gt;&lt;/code&gt;
# zweite Ebene: &lt;code&gt;&lt;nowiki&gt;# zwei&lt;/nowiki&gt;&lt;/code&gt;
## zweite Ebene: &lt;code&gt;&lt;nowiki&gt;** zwei-eins&lt;/nowiki&gt;&lt;/code&gt;

Eine Alternative ist HTML:

&lt;code&gt;&lt;nowiki&gt;&lt;ol&gt;&lt;/nowiki&gt;&lt;/code&gt;

&lt;code&gt;&lt;nowiki&gt;  &lt;li&gt;Coffee&lt;/li&gt;&lt;/nowiki&gt;&lt;/code&gt;

&lt;code&gt;&lt;nowiki&gt;  &lt;li&gt;Tea&lt;/li&gt;&lt;/nowiki&gt;&lt;/code&gt;

&lt;code&gt;&lt;nowiki&gt;    &lt;ul&gt;&lt;/nowiki&gt;&lt;/code&gt;

&lt;code&gt;&lt;nowiki&gt;      &lt;li&gt;Black tea&lt;/li&gt;&lt;/nowiki&gt;&lt;/code&gt;

&lt;code&gt;&lt;nowiki&gt;      &lt;li&gt;Green tea&lt;/li&gt;&lt;/nowiki&gt;&lt;/code&gt;

&lt;code&gt;&lt;nowiki&gt;    &lt;/ul&gt;&lt;/nowiki&gt;&lt;/code&gt;

&lt;code&gt;&lt;nowiki&gt;  &lt;li&gt;Milk&lt;/li&gt;&lt;/nowiki&gt;&lt;/code&gt;

&lt;code&gt;&lt;nowiki&gt;&lt;/ol&gt;&lt;/nowiki&gt;&lt;/code&gt;

erzeugt:

&lt;ol&gt;
  &lt;li&gt;Coffee&lt;/li&gt;
  &lt;li&gt;Tea&lt;/li&gt;
    &lt;ul&gt;
      &lt;li&gt;Black tea&lt;/li&gt;
      &lt;li&gt;Green tea&lt;/li&gt;
    &lt;/ul&gt;
  &lt;li&gt;Milk&lt;/li&gt;
&lt;/ol&gt;

* Bullet: &lt;code&gt;&lt;nowiki&gt;* eins&lt;/nowiki&gt;&lt;/code&gt;
** zweite Ebene: &lt;code&gt;&lt;nowiki&gt;** zwei&lt;/nowiki&gt;&lt;/code&gt;

:Einrückungen kann man mit einem Doppelpunkt ":" am Zeilenanfang erreichen.
::Zwei Doppelpunkte, etc.

===Fußnoten===
Fußnoten werden mit &lt;code&gt;&lt;nowiki&gt;&lt;ref&gt;das ist eine Fußnote&lt;/ref&gt;&lt;/nowiki&gt;&lt;/code&gt; erzeugt.&lt;ref&gt;das ist eine Fußnote&lt;/ref&gt;

Am Ende des Artikels (oder des Abschnitts) werden dann alle Fußnoten mit &lt;code&gt;&lt;nowiki&gt;&lt;references /&gt;&lt;/nowiki&gt;&lt;/code&gt; aufgelistet.

Beispiel für Fußnote im Abschnitt (im nächsten Abschnitt beginnt die Nummerierung von vorne!):

&lt;references /&gt;

Fußnote am Ende: &lt;ref&gt;das ist eine Fußnote&lt;/ref&gt;

===Bilder und Dateien===
[[File:lettoLogo.jpg|100px|thumb|right|Logo]] 
Grafiken können nach dem Hochladen (Menü links "Datei hochladen") mit &lt;code&gt;&lt;nowiki&gt;[[File:lettoLogo.jpg|200px|thumb|right|Logo]]&lt;/nowiki&gt;&lt;/code&gt; eingebunden werden. Mehr: [https://de.wikipedia.org/wiki/Hilfe:Bilder Hilfe in Wikipedia]

PDF-Dateien können hochgeladen und direkt zum Öffnen verlinkt werden: 
*&lt;code&gt;&lt;nowiki&gt;[[Medium:Handbuch.pdf|Handbuch]]&lt;/nowiki&gt;&lt;/code&gt;  [[Medium:Handbuch.pdf|Handbuch]]

====Suchen hochgeladener Dateien====
Ab einfachsten findet man hochgeladene Dateien mit dem Logbuch: [[Special:ListFiles]]. Dazu am besten 500 Dateien anzeigen lassen und mit [Strg]+[F] im Browser suchen. Ein Klick auf den Dateinamen führt zu den Metadaten (wo man z.B. neue Versionen der Datei hochladen kann).

==Kommentare==
Um für später Text vorzubereiten kann man diesen als ausgeblendeten Kommentar kennzeichnen: &lt;code&gt;&lt;nowiki&gt;&lt;!-- zwischen diesen Zeichen ist Text unsichtbar!  --&gt;&lt;/nowiki&gt;&lt;/code&gt;  
&lt;!-- zwischen diesen Zeichen ist Text unsichtbar!  --&gt;

==Struktur==
===Kategorien===
Um Beiträge inhaltlich und strukturell zu verbinden, können Kategorien vergeben werden (auch mehrfach, auch Kategorien sind in Kategorien zusammenfassbar. Dadurch entstehen Unterkategorien).

Alle Seiten einer Kategorie werden in Übersichtsseiten '''automatisch''' alphabetisch sortiert zusammengetragen, etwa:

Dies erfolgt z.B. für Beiträge betreffend Exportfunktionen durch den Eintrag &lt;code&gt;&lt;nowiki&gt;[[Kategorie:Export‎]]&lt;/nowiki&gt;&lt;/code&gt;.

Zu einer Kategorieübersicht verlinkt man mit &lt;code&gt;&lt;nowiki&gt;[[:Kategorie:Export‎]]&lt;/nowiki&gt;&lt;/code&gt;.

Hier sind '''[[Special:Categories|alle Kategorien]]''' aufgelistet.

===Portale===
Das sind Seiten, die '''manuell''' zur Organisation oder Strukturierung mit Beiträgen verlinkt werden, z.B.: [[Portal:Datenverwaltung]]. Ist total flexibel, aber Arbeit.

===Suchen===
{| class="wikitable"
| [[Special:Search/Server|&lt;code&gt;Server&lt;/code&gt;]] || Suche nach Worten. || n Ergebnisse &lt;sup&gt;(1.1.2019)&lt;/sup&gt;
|-
| [[Special:Search/"Einrichten des Servers"|&lt;code&gt;"Einrichten des Servers"&lt;/code&gt;]] || Suche nach der genauen Wortgruppe. || 1 Ergebnis &lt;sup&gt;-"-&lt;/sup&gt;
|-
| [[Special:Search/Server* |&lt;code&gt;Server*&lt;/code&gt;]] || Platzhalter für einen Teil eines Wortes. || m Ergebnisse &lt;sup&gt;-"-&lt;/sup&gt;
|-
| [[Special:Search/LSR -Quelle|&lt;code&gt;LSR -Quelle&lt;/code&gt;]] || Ausschluss eines Wortes oder einer Wortgruppe. || n Ergebnisse &lt;sup&gt;-"-&lt;/sup&gt;
|-
| [[Special:Search/~Server|&lt;code&gt;~Server&lt;/code&gt;]] || Anzeige des Suchergebnisses erzwingen und nicht automatisch zum Artikel weiterleiten. || m Ergebnisse &lt;sup&gt;-"-&lt;/sup&gt;
|-
|}

==Drucken==
Das Erzeugen eines Druckdokuments ist für ausgewählte Beiträge am effizientesten, indem man einfach das HTML (Druckversion, links unten inder Navigation) in Word kopiert. Dann kann man noch formatieren,es kann ein Inhaltsverzeichnis generiert werden etc.


[[Datei:logo.png|thumb|Logo]]'''[[Letto]]''' ist ein E-Learning-Server, der vor allem für technisch-mathematische-Gegenstände optimiert ist.
Mit einer Tabelle auf der Startseite kann man eine übersichtliche Hauptnavigation gestalten:
{| class="wikitable"
! Tabellenbeispiel !! Link !! Bemerkung !! Zuständig !! begonnen!! erledigt
|-
| Hilfe || [[Help-Wiki]] ||  || Andi || 25.5.2018 || 
|-
| Offenes || [[ToDo-Liste]] ||  || alle || immer || 
|-
| Kategorien|| [[:Kategorie:Einführung|Einführung]] || [[:Kategorie:Fragetypen|Fragetypen]] || [[:Category:Plugins|Liste der Plugins]] ||  || 
|-
| wichtige Links|| [[Beispielsammlung]] || [[Beispielsammlung Editieren|Beispielsammlung editieren]] ||  ||  || 
|-
| || colspan=4 | &lt;span style="background-color:yellow"&gt;&lt;span style="color:red"&gt;'''Neu:'''&lt;/span&gt; ''So lassen sich Infos hervorheben!''&lt;/span&gt;
||
|}
&lt;div style="clear:both"&gt;&lt;/div&gt; 
----
* Wie kann man eigentlich [[Help-Wiki|selbst Wiki-Seiten machen]]?

----
* [[ToDo-Liste]] für's Wiki
----
&lt;div align="right"&gt;&lt;span style="background-color:orange"&gt;[[Letto:Impressum|'''Impressum''']]&lt;/span&gt;&lt;/div&gt;



&lt;strong&gt;MediaWiki wurde installiert.&lt;/strong&gt;

Hilfe zur Benutzung und Konfiguration der Wiki-Software findest du im [https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Contents Benutzerhandbuch].

== Starthilfen ==

* [https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Configuration_settings Liste der Konfigurationsvariablen]
* [https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:FAQ MediaWiki-FAQ]
* [https://lists.wikimedia.org/mailman/listinfo/mediawiki-announce Mailingliste neuer MediaWiki-Versionen]
* [https://www.mediawiki.org/wiki/Special:MyLanguage/Localisation#Translation_resources Übersetze MediaWiki für deine Sprache]
* [https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Combating_spam Erfahre, wie du Spam auf deinem Wiki bekämpfen kannst]

----
=Endnoten=
&lt;references /&gt;
&lt;!-- [[Kategorie:Einführung]] --&gt;

