# Lettohub/letto-service-login
siehe auch
* [docker compose files](/notimplemented/index.md)

##  Login-Service 
###  Container 
**lettohub/letto-service-login**

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
| 8095 | http-Port für die interne Kommunikation innerhalb des Docker-Netzwerkes     |
| 9095 | https-Port mit selbstsigniertem Zertifikat für externe Kommunkation         |
| 5095 | debugging-Port, aktiv wenn die Environment-Variable debug=true gesetzt wird |


###  Pfade welche als Volume verbunden werden sollten 


| Pfad im Docker Container | Beschreibung                 | üblicher Wert                       |
|--------------------------|------------------------------|-------------------------------------|
| /log                     | Verzeichnis für die Logfiles | /opt/letto/docker/storage/log/login |


###  Environment Variable 

| Variable                  | Beschreibung                                                                                        | üblicher Wert                         | muss gesetzt sein |
|---------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------|-------------------|
| TZ                        | Zeitzone                                                                                            | Europe/Berlin                         | nein              |
| LC_ALL                    | Spracheinstellung                                                                                   | de_DE.UTF-8                           | nein              |
| letto_schulen             | Liste aller Schulkürzel der Schulen die auf dem gesamten Server laufen, durch Leerzeichen getrennt. |                                       | nein              |
| jwt_secret                | Base64 kodiertes Token-Secret für die Authentifizierung                                             |                                       | ja                |
| server_secret             | Base64 kodiertes Token-Secret für die Server-Server Kommunikation                                   |                                       | ja                |
| use_http                  | Gibt an ob redirections mit http gemacht werden sollen                                              | 0                                     | nein              |
| letto_local_privatkey     | Privater Schlüssel für die Kommunkation                                                             |                                       | ja                |
| letto_local_publickey     | öffentlicher Schlüssel für die Kommunikation                                                        |                                       | ja                |
| letto_user_user_password  | Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer user                   |                                       | ja                |
| letto_user_gast_password  | Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer gast                   |                                       | ja                |
| letto_user_admin_password | Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer admin                  |                                       | ja                |
| letto_license_server      | zu verwendender Lizenzserver                                                                        | https://license.letto.at/lettolicense | ja                |
| letto_setup_uri           | Docker-Interne URL des Setup-Services im Docker-Container                                           | http://letto-setup.nw-letto:8096      | ja                |
| JAVA_OPTS                 | Java Options-Variable für das Service                                                               | -Xms50m -Xmx100m                      | nein              |
| debug                     | Startet den Container im Debugging-Mode auf Port 5096                                               | false                                 | nein              |


##  Docker Compose 
* .yml File: [https://build.letto.at/download/install/yml/docker-compose-letto.yml](https://build.letto.at/download/install/yml/docker-compose-letto.yml)
* Environment Einstellungen für die .env-Datei [LeTTo Environment](../LeTToEnvironment/index.md)

[Administration](../Administration/index.md)

