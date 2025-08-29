siehe auch
* [[docker compose files]]

= MySQL Server =
== Container ==
'''lettohub/letto-mysql'''

== Tags ==
{| class="wikitable" style="text-align: left; width: 100%;"
| Tag || Beschreibung || Anmerkung
|- 
| beta || Beta Version für Beta-Test-Phasen, nicht für den Produktivbetrieb || 
|-
| daily || tagesaktuelle Letztversion für den Produktivbetrieb von ausgewählten Testschulen ||
|-
| stable || letzte stabile Version für den Produktivbetrieb ||
|-
| debug || Bitte nicht verwenden ist tagesaktuell nur für Debugging-Zwecke ||
|-
| rev6501 || Basierend auf MySQL 8.0.32 und Oracle Linux || 
|-
| rev6503 || Basierend auf MySQL 8.0.34 und Debian || 
|-
| rev6504 || Basierend auf MySQL 8.0.34 und Oracle Linux || 
|}

== Ports ==
{| class="wikitable" style="text-align: left; width: 100%;"
| Port || Beschreibung
|- 
| 3306 || MySQL Datenbank-Port
|-
|}

== Pfade welche als Volume verbunden werden sollten ==

{| class="wikitable" style="text-align: left; width: 100%;"
| Pfad im Docker Container || Beschreibung || üblicher Wert
|-
| /var/lib/mysql || Docker-Volume für die eigentliche Datenbank || lettomysql
|-
| /opt/dump || Verzeichnis für den Import und Export von Datenbank-Dumps || /opt/letto/docker/storage/database-dump
|-
| /opt/backup || wird nicht verwendet || /opt/letto/docker/storage/database-backup
|-
|}

== Environment Variable ==
{| class="wikitable" style="text-align: left; width: 100%;"
| Variable || Beschreibung || üblicher Wert || muss gesetzt sein
|- 
| TZ || Zeitzone || Europe/Berlin || nein
|-
| MYSQL_ROOT_PASSWORD || Passwort des Datebank root Benutzers || || nein
|-
|}

= Docker Compose =
* .yml File: [http://letto.at/download/letto/setup/yml/docker-compose-mysql.yml https://build.letto.at/download/install/yml/docker-compose-mysql.yml]
* Environment Einstellungen für die .env-Datei [[MySQL Environment]]

= Scripts im Container =
Der Container besitzt ein paar nützliche Scripts um die Verwaltung zu erleichtern.

Aufruf der Scripts über die Commandline mit:
&lt;pre&gt;docker exec -it letto-mysql scriptname parameter&lt;/pre&gt;

{| class="wikitable" style="text-align: left; width: 100%;"
| Script || Beschreibung || Beispiel
|- 
| help || gibt einen kurzen Hilfetext über die Scripts aus || docker exec -it letto-mysql help
|-
| 
|}

[[Kategorie:Administration]]

