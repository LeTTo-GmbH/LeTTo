# Lettohub/letto-service-data
siehe auch
* [docker compose files](/notimplemented/index.md)

##  Data-Service 
Erledigt den Zugriff auf die Schuldatenbank einer Schule.
###  Container 
**lettohub/letto-service-data**

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
| 8300 | http-Port für die interne Kommunikation innerhalb des Docker-Netzwerkes     |
| 9300 | https-Port mit selbstsigniertem Zertifikat für externe Kommunkation         |
| 5300 | debugging-Port, aktiv wenn die Environment-Variable debug=true gesetzt wird |


###  Pfade welche als Volume verbunden werden sollten 
school muss durch das Schulkürzel ersetzt werden!!


| Pfad im Docker Container | Beschreibung                 | üblicher Wert                             |
|--------------------------|------------------------------|-------------------------------------------|
| /log                     | Verzeichnis für die Logfiles | /opt/letto/docker/storage/log/data/school |


###  Environment Variable 

| Variable                         | Beschreibung                                                                                        | üblicher Wert                                                                                                                                                               | muss gesetzt sein |
|----------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| TZ                               | Zeitzone                                                                                            | Europe/Berlin                                                                                                                                                               | nein              |
| LC_ALL                           | Spracheinstellung                                                                                   | de_DE.UTF-8                                                                                                                                                                 | nein              |
| spring_datasource_url            | Spring-Boot kompatible Datenbank-Quelle                                                             | jdbc:mysql://letto-mysql.nw-letto:3306/letto?useSSL=false&amp;useUnicode=true&amp;useJDBCCompliantTimezoneShift=true&amp;useLegacyDatetimeCode=false&amp;serverTimezone=UTC | ja                |
| spring_datasource_username       | Datenbankbenutzer an der Schuldatenbank                                                             | letto                                                                                                                                                                       | ja                |
| spring_datasource_password       | Klartext-Datenbankpasswort an der Schuldatenbank                                                    |                                                                                                                                                                             | ja                |
| letto_school                     | Schulkürzel mit dem dann auch der Server erreichbar sein soll                                       |                                                                                                                                                                             | ja                |
| jwt_secret                       | Base64 kodiertes Token-Secret für die Authentifizierung                                             |                                                                                                                                                                             | ja                |
| server_secret                    | Base64 kodiertes Token-Secret für die Server-Server Kommunikation                                   |                                                                                                                                                                             | ja                |
| letto_log                        | Verzeichnis innerhalb des Containers wo die Logdateien gespeichert werden                           | /log                                                                                                                                                                        | ja                |
| letto_schulen                    | Liste aller Schulkürzel der Schulen die auf dem gesamten Server laufen, durch Leerzeichen getrennt. |                                                                                                                                                                             | nein              |
| letto_user_user_password         | Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer user                   |                                                                                                                                                                             | ja                |
| letto_user_gast_password         | Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer gast                   |                                                                                                                                                                             | ja                |
| letto_user_admin_password        | Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer admin                  |                                                                                                                                                                             | ja                |
| letto_login_uri                  | Docker-Interne URL des Login-Services                                                               | http://letto-login.nw-letto:8095                                                                                                                                            | ja                |
| letto_setup_uri                  | Docker-Interne URL des Setup-Services im Docker-Container                                           | http://letto-setup.nw-letto:8096                                                                                                                                            | ja                |
| letto_lettodata_redirecttokenuri | Öffentlich erreichbare URL des LeTTo-Servers für einen temporären Token                             | https://externe.dns.at/lettoschool/loginTempToken.jsf                                                                                                                       | ja                |
| JAVA_OPTS                        | Java Options-Variable für den Speicherbedarf                                                        | -Xms50m -Xmx100m                                                                                                                                                            | nein              |
| debug                            | Startet den Container im Debugging-Mode auf Port 5096                                               | false                                                                                                                                                                       | nein              |


##  Docker Compose 
* .yml File: [https://build.letto.at/download/install/yml/docker-compose-school.yml](https://build.letto.at/download/install/yml/docker-compose-school.yml)
* Environment Einstellungen für die .env-Datei [LeTTo Environment](../LeTToEnvironment/index.md)

[Administration](../Administration/index.md)

