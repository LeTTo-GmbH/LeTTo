# Neuigkeiten

## laufend
* Performance-Verbesserungen im Parser #2250


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
* debug-Variable in der [Fragevorschau](../Fragen-Vorschau/index.md#debug-ansicht-mit-debug-variablen) 
* Speicherüberlauf bei Maxima-Berechnungen behoben
* Einheiten Bit und Byte mit deren Vielfachen k,M,G,T,P
* Korrekte Verarbeitung von komplexem Logarithmus und Potenzen
* Korrektur beim Mustervergleich in der Zieleinheit
* Browser-Fingerprint für die Verhinderung von Mehrfachanmeldungen
* Login-Logging in MongoDB
* asynchornes Speichern von Fragen
* RDP-Druck im Edit-Service

## Stable - Rev 6669/6670 - 13.2.2025
* Definition der Größe und Art des Eingabefeldes der Schülerantwort bei Mehrfachberechnungsfragen über die [Zieleinheit](../ZielEinheit/index.md#parameter-für-die-größe-und-art-des-eingabefeldes-bei-berechneten-teilfragen-einer-mehrfachberechnungsfrage)
* Base-Container auf Letztversionen aktualisiert
* MathJax 3
* Toleranz mit Testvektoren bei booleschen(boolschen) Teilfragen [Testvektoren](../Korrektur/index.md#korrektur-von-symbolischen-ausdrücken-mit-testvektoren)
* Funktionen curveinterpol und curvepv für globale und importierte Tabellen [Berechnungen](../Berechnungen/index.md#funktionen-für-importierte-tabellen)
* Healthcheck Timout verlängert
* Redis-Datenbank 
* Mongo-Datenbank
* Bugfixes
* Euro-Symbol
* Latex-Parser für LeTTo-app
* Login-Logging in Mongo-DB
* Korrektur von Vektoren und Mengen [Zieleinheit Vektoren-Mengen](../ZielEinheit/index.md#parameter-für-den-ergebnisvergleich-von-vektoren-und-mengen-bei-der-schülereingabe)

## Stable - Rev6544 10.12.2024
* verschiedenste Bugfixes - siehe https://project.letto.at/projects/letto/work_packages
* pom für alle Services angepasst
* Setup-Service überarbeitet
* globale und importierte Tabellen aus CSV-Dateien [CSV-Dateien importiert](../BeispielsammlungEditieren/csv-tabellen_importieren/index.md)
* CPU-Trend überarbeitet
* REST-Ping-Check im Setup überarbeitet
* Pi-Bug behoben
* Einheit Log und Grad überarbeitet
* Unique Vektoren als Datensatz wie zB uV3:1-5 siehe auch [Datensatz definieren](../Datensätzedefinieren/index.md#definition-der-werte)
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