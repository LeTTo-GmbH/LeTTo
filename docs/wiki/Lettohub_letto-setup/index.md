# Lettohub/letto-setup
siehe auch
* [docker compose files](/notimplemented/index.md)

##  Setup-Service 
###  Container 
**lettohub/letto-setup**

###  Tags 

| Tag     | Beschreibung                                                                         | Anmerkung |
|---------|--------------------------------------------------------------------------------------|-----------|
| beta    | Beta Version für Beta-Test-Phasen, nicht für den Produktivbetrieb                    |           |
| daily   | tagesaktuelle Letztversion für den Produktivbetrieb von ausgewählten Testschulen     |           |
| stable  | letzte stabile Version für den Produktivbetrieb                                      |           |
| debug   | Bitte nicht verwenden ist tagesaktuell nur für Debugging-Zwecke                      |           |
| revXXXX | Revision mit der Nummer XXXX. Nur wenn man eine definierte Version verwenden möchte. |           |


###  Ports 

| Port | Beschreibung                                                                |
|------|-----------------------------------------------------------------------------|
| 8096 | http-Port für die interne Kommunikation innerhalb des Docker-Netzwerkes     |
| 9096 | https-Port mit selbstsigniertem Zertifikat für externe Kommunkation         |
| 5096 | debugging-Port, aktiv wenn die Environment-Variable debug=true gesetzt wird |


###  Pfade welche als Volume verbunden werden sollten 

| Pfad im Docker Container | Beschreibung                                                                                                               | üblicher Wert                   |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| /host                    | Verzeichnis in dem docker-compose gestartet wurde                                                                          | /opt/letto/docker/compose/setup |
| /opt/letto               | Zugriff auf das LeTTo-Hauptverzeichnis des Host damit das Setup-Service die Verzeichnisstruktur erstellen und prüfen kann. | /opt/letto                      |
| /letto_compose           | Verzeichnis wo sich die Unterverzeichnisse mysql,setup und letto mit den yml-Dateien für docker-compose befinden.          | /opt/letto/docker/compose/letto |
| /var/run/docker.sock     | Zugriff auf das Docker-System um mit dem Setup-Service alle Docker-Informationen und Docker-Befehle ausführen zu können    | /var/run/docker.sock            |
| /opt/letto/log           | Verzeichnis für alle Logfiles der LeTTo-Installation                                                                       | /opt/letto/docker/storage/log   |


###  Environment Variable 

| Variable                  | Beschreibung                                                                       | üblicher Wert                         | muss gesetzt sein                              |
|---------------------------|------------------------------------------------------------------------------------|---------------------------------------|------------------------------------------------|
| TZ                        | Zeitzone                                                                           | Europe/Berlin                         | nein                                           |
| ADMIN_PASSWORD            | Klartext Administrator-Passwort, bevorzugt gegen das ADMIN_PASSWORD_ENCRYPTED      |                                       | ADMIN_PASSWORD  oder  ADMIN_PASSWORD_ENCRYPTED |
| ADMIN_PASSWORD_ENCRYPTED  | Password-Hash des Administrator-Passwortes                                         |                                       | ADMIN_PASSWORD  oder  ADMIN_PASSWORD_ENCRYPTED |
| LETTO_UID                 | Linux-User-id des Benutzers letto                                                  | 1000                                  | nein                                           |
| RUN_AS_ROOT               | Setup arbeitet als Benutzer root                                                   | true                                  | ja                                             |
| letto_local_restkey       | Schlüssel mit dem der Server am Lizenzserver registriert ist                       |                                       | nein                                           |
| jwt_secret                | Base64 kodiertes Token-Secret für die Authentifizierung                            |                                       | jaSE                                           |
| server_secret             | Base64 kodiertes Token-Secret für die Server-Server Kommunikation                  |                                       | jaSE                                           |
| letto_local_privatkey     | Privater Schlüssel für die Kommunkation                                            |                                       | jaSE                                           |
| letto_local_publickey     | öffentlicher Schlüssel für die Kommunikation                                       |                                       | jaSE                                           |
| letto_user_user_password  | Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer user  |                                       | jaSE                                           |
| letto_user_gast_password  | Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer gast  |                                       | jaSE                                           |
| letto_user_admin_password | Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer admin |                                       | jaSE                                           |
| letto_login_uri           | Docker-interne URL des Login-Services                                              | http://letto-login.nw-letto:8095      | ja                                             |
| letto_license_server      | Lizenzserver der verwendet wird                                                    | https://license.letto.at/lettolicense | nein                                           |
| JAVA_OPTS                 | Java Options-Variable für das Setup-Service                                        | -Xms50m -Xmx100m                      | nein                                           |
| setup_debug               | Konfigurationsparameter für das Debugging sind aktiviert                           | false                                 | nein                                           |
| debug                     | Startet den Container im Debugging-Mode auf Port 5096                              | false                                 | nein                                           |

jaSE: ja - wird vom Setup erzeugt und in die .env Datei geschrieben

##  Docker Compose 
* .yml File: [https://build.letto.at/download/install/yml/docker-compose-setup.yml](https://build.letto.at/download/install/yml/docker-compose-setup.yml)
* Environment Einstellungen für die .env-Datei [Setup Environment](../SetupEnvironment/index.md)


[Administration](../Administration/index.md)

