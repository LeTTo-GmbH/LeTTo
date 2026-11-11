# Neuigkeiten

## Version 1.3 - 10.11.2026 (Entwicklungsstand)
* **Lernmaterialien und Info-Seite für Schüler:** Der Menüpunkt „Beispiele“ heißt jetzt **Lernmaterialien** und erscheint
  nur, wenn es für den Schüler Übungsaufgaben gibt; auch Klassen allgemein gültiger Schuljahre, in denen der Schüler direkt
  Mitglied ist, zählen dazu. Allgemein gültige Schuljahre sind für Schüler nie das aktuelle Schuljahr. Sind Info-Seite und
  Lernmaterialien aktiv und hat der Schüler keine Inhalte im aktuellen Schuljahr, werden Dashboard und Startseite
  ausgeblendet. Die mitgelieferte Info-Seite erklärt das Selbstlernen und gibt es in allen 5 Sprachen – siehe
  [Lernmaterialien](../../Schueler/Lernmaterialien/index.md) und [Info-Seite](../../Schueler/Info-Seite/index.md)
* **Beurteilungsschema:** Prüfung vor dem Speichern mit Prüfbericht (Ampel), Notenskala als Balken, Beispielrechnung
  „Was wäre wenn?“ mit Rechenweg, Vorlagen, Hilfetexte zu jedem Feld, Zuordnung globaler Definitionen bei Import/Kopie,
  eindeutiges Default-Schema, Markierungen (-1 %) nie aus einem Prozentwert; im Admin-Modus „Schemen prüfen“ und
  Schutz verwendeter globaler Definitionen – siehe [Beurteilungskonfiguration](../../Konfiguration/Beurteilung/index.md)
* **Katalog:** ohne Schülerauswahl werden alle Schüler angezeigt, die Auswahl gilt auch für die Testergebnisse –
  siehe [Anzeigekonfiguration](../../Beurteilungen/Katalog/Anzeigekonfiguration/index.md#klassen-und-schüler)
* **Untis-Import:** Login-Name neuer Schüler wählbar (vorname.nachname oder Sokrates-ID) – siehe
  [Untis-Import](../../admin/untis-import/index.md#schüler-und-zusatzdaten)
* **Plugins:** Design und Prüfen-Buttons der App für das Plugin-JavaScript (`window.LeTTo`, `plugintools.js`) – siehe
  [JavaScript-Schnittstelle](../../Plugins/JavaScript-Schnittstelle/index.md)
* **Einstellung BIBLIOTHEK_NEU:** je Schule wählbar, ob „Aktivität/Fragen bearbeiten“ und das Bearbeiten einer Frage aus
  den Ergebnissen in die Bibliothek neu oder in die alte Oberfläche führen – siehe
  [LeTTo Environment](../../Administration/Docker/LeTToEnvironment/index.md#app-konfiguration)
* **Bugfixes Aktivitäten und Ergebnisse:**
  * keine leere Seite mehr bei „Eigene Eingaben ansehen“; nach der Abgabe Status aller Fragen bei Aktivitäten mit
    Prüfen, Lösungen erst nach dem Ende (#2562, #2344) – siehe [Aktivität starten](../../Schueler/AktivitaetStart/index.md#nach-der-abgabe)
  * abgegebene Versuche werden nicht wieder bearbeitbar, kein doppelter Start (#2500, #2544)
  * gleiche Beispielnummern bei Lehrer und Schüler, Ergebnisspalten in der Reihenfolge der Aktivität, Gruppieren
    speichert einen zusammenhängenden Block, Hinweis „Reihenfolge kontrollieren“ (#2543) – siehe
    [Fragen der Aktivität](../../Bibliothek/Aktivitaeten/index.md#hinweis-reihenfolge-kontrollieren)
  * Sortierung der Ergebnisliste bleibt beim Polling und wird gemerkt (#2569) – siehe
    [Test-Ergebnisse](../../Tests/Test-Ergebnisse/index.md#sortierung)
  * Stopp-Knopf mit drei Zuständen (läuft / Bereich offen / beendet) (#2548) – siehe
    [Aktivität beenden](../../Tests/Test-Ergebnisse/index.md#aktivität-beenden)
  * Start-/Stoppzeit im Aktivitäts-Dialog wieder sichtbar und änderbar (#2573) – siehe
    [Online-Aktivität](../../Beurteilungen/Katalog/OnlineAktivitaet/index.md#zeitbegrenzung)
  * Reihenfolge der Aktivitäten bleibt erhalten (#2565)
* **Bugfixes Verwaltung und alte Oberfläche:**
  * Benutzer-Dialog öffnet den richtigen Benutzer, Login und Nachname Pflicht, Löschen im Dialog, richtige Tooltips
    (#2567, #2574) – siehe [Benutzer bearbeiten](../../Konfiguration/Benutzer/Dialoge/Benutzer-bearbeiten/index.md)
  * Fragensuche: richtige Meldung bei Suche nur nach dem Autor (#1386)
  * Beispielsammlung merkt den zuletzt gewählten Ordner/Test (#2575)
  * Verbindungsfehler zu Fremdservern (Exchange) werden in main in `/opt/letto/log/fremdserver.log` und im Docker-Log protokolliert (#2557)

## Stable - Rev 7044 - Version 1.3 - Oktober 2026
* [Update von Version 1.2 auf 1.3](../../Administration/Updaterev70xx/index.md)
* Hilfe Maxima-Feld
* Bugfixes
* Neue Docker-Container-Struktur (siehe [Update rev70xx](../../Administration/Updaterev70xx/index.md))
* Verwaltungs-Bereich für die LeTTo-App
* Plugin-Konfiguration Umstellung auf Javascript
* Pluginverwaltung im Setup-Service
* Userstatistik im Setup-Service
* System-Status im Setup-Service: Verlauf der letzten 30 Tage in der MongoDB, Tagesauswahl, Sessions pro Schule, Docker-Container in Gruppen (siehe [System-Status](../../Administration/Setup-Service/System-Status/index.md))

## Stable - Rev 6893 - Version 1.2 - Juli 2026
* Bugfixes
* LeTTo-App: User-Konfiguration 
* Performance-Verbesserungen im Parser
* verbesserter sicherer Prüfungsmodus
* Schnittstelle für externe Plugins fertig definiert

## Stable - Rev 6754 - 8.10.2025
* Integration der LeTTo-App in den Setup-Service
* Bugfixes
* Konfigurationsmöglichkeit für den Fingerprint

## Stable - Rev 6746 - 13.9.2025
* Bugfixes
* Linux-Container auf Letztversionen aktualisiert
* Import von Moodle-XML-Dateien mit Bildern verbessert
* Datensicherung von MongoDB und RedisDB integriert
* Fingerprint Bugfixes
* Backup Email angepasst

## Stable - Rev 6730 - 5.7.2025
* MathJax3 in Questionservice
* Bugfixes #2066, #1932, #2124, #2129
* Docker-Container aktualisiert
* Rundungsfehler bei Genauigkeit a0 behoben
* Logfilearchiv für Lettoserver definiert
* Überarbeiteter Scorer bei symbolischen Ergebnissen
* pvremove, pvinsert, pvinserlast
* debug-Variable in der [Fragevorschau](../../Fragen/Fragen-Vorschau/index.md#debug-ansicht-mit-debug-variablen) 
* Speicherüberlauf bei Maxima-Berechnungen behoben
* Einheiten Bit und Byte mit deren Vielfachen k,M,G,T,P
* Korrekte Verarbeitung von komplexem Logarithmus und Potenzen
* Korrektur beim Mustervergleich in der Zieleinheit
* Browser-Fingerprint für die Verhinderung von Mehrfachanmeldungen
* Login-Logging in MongoDB
* asynchornes Speichern von Fragen
* RDP-Druck im Edit-Service

## Stable - Rev 6669/6670 - 13.2.2025
* Definition der Größe und Art des Eingabefeldes der Schülerantwort bei Mehrfachberechnungsfragen über die [Zieleinheit](../../Berechnungen/ZielEinheit/index.md#parameter-für-die-größe-und-art-des-eingabefeldes-bei-berechneten-teilfragen-einer-mehrfachberechnungsfrage)
* Base-Container auf Letztversionen aktualisiert
* MathJax 3
* Toleranz mit Testvektoren bei booleschen(boolschen) Teilfragen [Testvektoren](../../Fragen/Korrektur/index.md#korrektur-von-symbolischen-ausdrücken-mit-testvektoren)
* Funktionen curveinterpol und curvepv für globale und importierte Tabellen [Berechnungen](../../Berechnungen/index.md#funktionen-für-importierte-tabellen)
* Healthcheck Timout verlängert
* Redis-Datenbank 
* Mongo-Datenbank
* Bugfixes
* Euro-Symbol
* Latex-Parser für LeTTo-app
* Login-Logging in Mongo-DB
* Korrektur von Vektoren und Mengen [Zieleinheit Vektoren-Mengen](../../Berechnungen/ZielEinheit/index.md#parameter-für-den-ergebnisvergleich-von-vektoren-und-mengen-bei-der-schülereingabe)

## Stable - Rev6544 10.12.2024
* verschiedenste Bugfixes - siehe https://project.letto.at/projects/letto/work_packages
* pom für alle Services angepasst
* Setup-Service überarbeitet
* globale und importierte Tabellen aus CSV-Dateien [CSV-Dateien importiert](../../Fragen/BeispielsammlungEditieren/csv-tabellen_importieren/index.md)
* CPU-Trend überarbeitet
* REST-Ping-Check im Setup überarbeitet
* Pi-Bug behoben
* Einheit Log und Grad überarbeitet
* Unique Vektoren als Datensatz wie zB uV3:1-5 siehe auch [Datensatz definieren](../../Berechnungen/Datensätzedefinieren/index.md#definition-der-werte)
* AI-Integration
* Testdruck in der neuen Edit-Oberfläche
* Bugfix-Bildsortierung
* Wiki umgestellt auf doc.letto.at
* AD-Login überarbeitet
* Server-Token für Schul-Schul-Datenverbindung eingeführt
* PLugintester für die Entwicklung eigener Plugins 
* Pluginuhr Demoplugin
* download-Service mit Apache und php integriert
* Export-Service für Beispiel-Export und Import in der neuen Edit-Oberfläche
* neue Edit-Oberfläche überarbeitet und als Standard integriert