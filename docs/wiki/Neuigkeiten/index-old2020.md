# ältere Änderungen - Archiv
## Aktuelle Änderungen in LeTTo
### 5.1.2020 Rev
* Datensatz-Namen dürfen bei automatischer Erzeugung nur aus Buchstaben, Zahlen und Unterstrich bestehen, wobei sie mit einem Buchstaben beginnen müssen.
* Datensatz-Definitionen dürfen mehr als 100 Zeichen haben. Achtung: Bei bestehenden Versionen muss dafür in der Datenbank in der Tabelle **datasetdefinition** die Spalte **ZAHLENBEREICH** auf longtext gesetzt werden!
* Im Ergebnisdialog zu einer Testfrage kann man die Schülereingaben einer Freitextfrage jetzt markieren und kopieren
* Verwaltung von Noten über Semestergrenzen möglich (Eingabe von Noten im WS, die für das Sommersemester zählen)
* Fehler beim Gruppieren von Tests (Nachtests,...) ist behoben
* Export  von allen klassenweisen Beurteilungen und Import in neuem Schuljahr
* Importieren von Noten in klassenweisen Beurteilungen durch Eingabe aller Noten in Eingabefeld
* Größe der Dialoge **Vorschau** / **Ergebnisse einer Testfrage** vom Benutzer in Konfiguration -&gt; User-Konfiguration unter **dialogSize** definierbar
* Abzug von Punkten bei fehlerhaften Eingaben, kann auch für HÜ, RÜ, Projekte,... ausgewählt werden und ermöglicht so ein schrittweises Abarbeiten von langen und ausführlichen Beispielen.
* Bilder austauschen in der Bilderverwaltung
* Fragen löschen über Konext-Menü mit Bestätigungs-Dialog
* Neues Layout für die Beispielerstellung
* Umstellung auf Primefaces 7.0
* CSV-Export in UTF8 oder ISO-8859-1 möglich: Konfiguration -&gt; User-Konfiguration unter **exportFormat** definierbar
* Testeinstellungen: 
  * Fragenreihenfolge fixieren: Der Schüler kann sich die Reihenfolge der Beantwortung der Fragen nicht mehr aussuchen
  * Begrenzung: Bei aktiver Zeitbegrenzung sieht der Schüler die Zeit, die noch für die Bearbeitung zur Verfügung steht. Fehler in diesem Modul wurden behoben.
* Lehrer-Beurteilung für eine Testfrage aufheben wurde implementiert.
* Falsche Zuordnung von Tooltips zu den einzelnen Teilfrage im Ergebnisdialog (Ergebnisse von Online-Tests) wurde korrigiert.
* Mehrfachverwendung des gleichen Tags (zB. 2 malige Eingabe von [Q0](Q0)) für eine Teilfrage führte zu Exception. Fehler wurde behoben.

### 25.3.2019 Rev 4867
* I2C Bus und allgemeine Digitalsignale im [DigiGraph](../DigiGraph/index.md)-Plugin
* [Graph](../Graph/index.md)-Plugin mit [Oszilloskop](../KonfigurationdesOszilloskopes/index.md) für beliebige Zeitsignale
* Folgefehler mit Calculated-SubQuestions
* Neue Funktionen im Parser:
  * csin : Erzeugt aus einer komplexen Zahl und einer Frequenz eine periodische Sinusschwingung in der Zeitvariablen t
  * dataset : lädt einen kompletten Datensatz in einen Vektor
  * interpol : Interpolationsfunktion
  * solve : Lösen von linearen Gleichungssystemen
  * solvevalue: numerische Lösung von linearen Gleichungssystem nach einer Variablen
  * periodic : Erzeugen einer periodischen Funktion aus einer beliebigen Funktion
  * numint : numerische Integration 
  * numdif : numerisches Differenzieren
  * unit : liefert die Einheit einer Größe

### 18.2.2019 Rev 4715
#### Fragedruck
* Druck als PDF von ClozeCalc mit Multiplechoice-Fragen werden die Fragetexte nicht gedruckt 
* Ausdruck von Lückentext-Fragen liefert beim Ergebnisdruck falsche  Werte und die Ergebnisse sind nicht rot 
* Beim Ausdruck funktioniert fett und kursiv 
* Ausdruck Zuordnungsfrage überarbeitet!
* Druck von Lückentextfragen
* Druck von Zuordnungsfragen und Multiple-Choice-Fragen mit Bildern und Plugins
#### Neu
* Reihenfolge bei mehreren Antworten einer Subquestion: Die erste Antwort die trifft entscheidet! **VORSICHT**: Bei bestehenden berechnenden Fragen mit mehreren Antworten kann sich das Verhalten der Frage ändern.
#### Fehlerkorrektur
* Plot Achsenskalierung
* Leerzeichen im Maximafeld vor einer Zuweisung werden richtig verarbeitet

### 11.2.2019 Rev 4694
* Bei _Klassenweisen Beurteilungen_ kann bei jeder Beurteilung das Datum eingeblendet werden und Noten können importiert werden. Siehe auch [Klassenweise Beurteilungen](../Katalog/index.md#hinzufügen-einer-klassenweisen-beurteilung).
* Fehler wurde behoben bei der Ergebnisdarstellung von Tests: Bisher gab es Probleme, wenn die Fragen eines Tests nachträglich geändert worden waren.
* Umstellung des Hochladens von Dateien, die Dokumente zu Testfragen sind. Ab sofort wird der Pfadname des Dokuments in der Datenbank gespeichert.
* Fehler beim Gruppieren von Tests wurde behoben.
* Freihand-Plugin: Beim Freihand-Plugin kann es passieren, dass das Ergebnis nicht als SVG dargestellt werden kann. Dann kam es bisher in der Ergebnisansicht zu Fehlern. Ab sofort wird in diesem Fall wieder der Freihand-Editor geladen und dort die Eingabe angezeigt.
### 1.2.2019 Rev 4678
#### Fehlerkorrekturen
* Vektor: Datensatz als Vektor -&gt; Es kann im Ergebnis mit vget auch bei symbolischen Lösungen auf ein Element eines Datensatzes zugegriffen werden.
* Fragen mit Folgefehler: Bei falscher Antwort wird der String der 1. Teilfrage geliefert
* Boolsche Fragen mit komplexen Zahlen funktionieren

### 19.1.2019
#### Neues
* Änderungen in der Ergebnisansicht eines Tests
  * Frage kann direkt aus der Ergebnisanicht geändert werden und man kommt über zurück wieder zur Ergebnisansicht zurück
  * Aufruf der Ergebnisse eines Test jetzt direkt über das Icon links von der Testbezeichnung
* Ergebnisansicht einer beantworteten Testfrage:
  * Der Bereich mit den Punkten für Teilfragen und Individualfeedback ist eingefroren und wird bei langen Fragen nicht mehr mitgeschoben.
  * Navigationsmöglichkeiten für "nächste Frage", "vorige Frage", "nächster Schüler" und "voriger Schüler".
* Exportfunktion für Katalog nach Excel: zusätzliche Gruppenspalte und Gesamt-Prozentzahl werden mit ausgegeben
* Beurteilungsschemen:
  * Zusammenführen von Online-Tests und allen anderen Beurteilungsformen. 
  * Vom Adinistrator kann nun jede Beurteilungsart als Online-Test-Art festgelegt werden. Damit können zB. auch Projekte etc. als Online-Test geführt werden.
  * Neuer Summenmodus: Es kann definiert werden, ob in der Summendarstellung über mehrere Lehrer, die den gleichen Gegenstand unterrichten, alle Dateilnoten oder nur die Gesamtsumme in Prozent von jedem unterrichtenden Lehrer angezeigt werden. 
  * Direktverlinkung aus einem Katalog zum verwendeten Beurteilungsschema, um dieses zu ändern oder anzupassen.
* LDAP-Test: Der Admin kann unter LDAP-Test jetzt alle Parameter für den LDAP-Zugang in Eingabefeldern anpassen, um die korrekten Parameter für sein System zu finden. Diese Parameter gehören dann in die Konfigurations-Felder eingetragen
* Direkter Link zu Testergebnissen über das Icon links vom Test realisiert
* Administratoren können Beispielsammlungen von ganzen Kategorien erzeugen und für alle Schüler zum Üben freigeben. Die hier angelegeten Online-Tests haben anderes Veralten: Die Beurteilungen werden nicht in der Datenbank gespeichert und sind nur während der Session verfügbar.
* Neue Checkbox **symbolisch** bei der Fragebeantwortung

#### Fehlerkorrekturen
* Wenn zwei Fragen nebeneinander den gleichen Plugin-Tag verwendeten, udann wurde bisher die Plugin-Vorschau nicht neu gezeichnet. 
* Nach [Strg](Strg)-Q bei einer Mehrfachberechnungsfrage konnte man nicht direkt weitertippen. 
* Beücksichtigung des Einheiten-Fehlers (Abzug wurde bisher bei Einheitenfehler immer mit 0.1 gerechnet)

* Source-Code-Plugin: Vorschau-Modus konnte man keinen Sourcecode eingeben
* Export in Summenansicht funktionierte nicht vollständig
* Im Vorschaumodus konnte eine Frage nur einmal beantwortet werden.
* Fehlerhafte Auswahl von Fragen in der Fragesammlung nach Änderung des Fragenamens wurde korrigiert.
* Nach einer Änderung einer Testfrage wurden alle Detailergebnisse von Teilfragen gelöscht. Damit konnte der Lehrer nicht mehr die Punkte der Teilfragen bearbeiten und nach einer Neubeurteilung wurden von Lehrer vergebene Teilpunkte auf alle Teilfragen gleichmäßig aufgeteilt.
* Nach dem Einfügen der ersten Frage in einer vormals leeren Kategorie konnte man keinen Fragetext eingeben.
* Fragen mischen bei Tests: Fragen wurden bisher immer gemischt, auch wenn das Häckchen bei _mischen_ in den Testeinstellungen nicht gesetzt war.
* Exception beim 2. Versuch einer Hausübung/RÜ : Fehler wurde behoben
* Neue Klassenzuordnung löschte eingegebene Bezeichnungen von anderen Klassenzuordnungen
* Umbenennen der Beurteilungsart hatte auf Button in der Klassenbeurteilung keinen Einfluss
* In der Gesamt-Prozent-Auswertung standen bisher keine Namen von Klassenweisen Beurteilungen, sondern nur die Beurteilungsart
* Nach Session-Timout war der Baum der Online-Tests nicht verfügbar
* Fehler beim Löschen von Antwortmöglichkeiten in der Edit-Ansicht behoben.

### 1.12.2018 - 17.1.2019
* bessere Parametrierbarkeit von Zeigerdiagrammen
* Darstellungsprobleme im WSR behoben
* komplexe Eingangsspannung bei Quellen im WSR
* Umlaute bei Strings in der wenn-Funktion ermöglicht
* Felder als Ergebnis von Methoden im Sourcecode-Plugin ermöglichen
* Bodediagramm bei Zuordnungsfragen ermöglichen
* Fehlerkorrekturen bei mathematischen Funktionen
* symbolischer Berechnungsmodus bei berechnenden Fragen
* Fehler bei Brückenschaltungen
* Induktivitätssymbol angepasst
* ground Fehler behoben
* Fehler bei komplexen Datensätzen behoben

### 8.12.2018
* [Schülerfotos importieren#hochladen-von-schülerfotos-](../Datenimport#hochladen-von-schülerfotos-/index.md#hochladen-von-schülerfotos-)
* [Katalog im Summenmodus](../LehrerübergreifenderKatalog/index.md) für Gegenstandsübersicht (negative Noten werden farbig hinterlegt). Die Konfiguration erfolgt über die [Beurteilungskonfiguration#summe-über-lehrer-](../Beurteilungskonfiguration#summe-über-lehrer-/index.md#summe-über-lehrer-)
* Export des Katalogs um Gruppierung und Prozentwerte erweitert, Umstellung auf Windows-ANSI-Format
* Verbesserungen der Beurteilungskonfigurationen bei Verwendung von Zwischennoten

### 3.12.2018
**ACHTUNG: größere Datenbankänderung im Hintergrund, ein Wechsel zurück auf eine ältere Version ist nicht möglich!! **
* [Änderungen im Beurteilungsschema#beurteilungsgruppierungen-](../Beurteilungskonfiguration#beurteilungsgruppierungen-/index.md#beurteilungsgruppierungen-): Die Unterteilung in Online-Test und andere Beurteilungen entfällt. Online-Tests sind in den Beurteilungen SMÜ, Rechenübung, Hausübung, Test, Schularbeit möglich. Der Testmodus greift jetzt direkt auf diese Beurteiungsarten zu.
* In der Ergebnisansicht von Tests wurde in der Detailansicht der Schülereingaben eine [Navigationmöglichkeit '''Nächster/Letzter Schüler''' und '''Nächstes/Letztes Beispiel'''#weiterschalten-/-abschliessen-der-eingaben-](../Test-Ergebnisse#weiterschalten-/-abschliessen-der-eingaben-/index.md#weiterschalten-/-abschliessen-der-eingaben-) angelegt.

### 30.11.2018
* Zuweisen von Themen zu einem Ordner/Kategorie: Damit bekommen alle Fragen in einer Kategorie diese Kompetenz zugewiesen. Kennzeichnung dieser Ordner durch ein Icon.
* Bei Fragen mit zugeteilten Themen werden in der Fragenliste Icons und Tooltips zu den Themen angezeigt
* Änderungen in den Dialogen zur Kategoriezuteilung
* In diesem Schuljahr in Online-Tests verwendete Beispiele werden während der Testbearbeitung mit einem Icon gekennzeichnet. Tooltips zeigen an, wo eine Frage bereits verwendet wurde.

* Test-Eigenschaften:
  * Die Beurteilungsschemen von Tests wurden an die Beurteilungskonfiguration angepasst. Damit werden auch die im Beurteilungsschema definierten Symbole und Noten verwendet. (zB.: wird dann nicht mehr _Sehr Gut_ für eine Hausübung vergeben)
  * Neue Testeigenschaft **Fragenreihenfolge fixieren**: Der Schüler muss die Fragen in der gestellten Reihenfolge bearbeiten und kann nicht mehr zu bereits beantworteten Fragen zurückschalten.

* Export der Schülernoten in CSV-File: 
  * Umstellung des Namens auf Nachname + Vorname (für alphabetische Sortierung)
  * Dezimaltrennzeichen ist jetzt der Beistrich

