# LeTTo Environment
siehe auch
* [Docker compose files](../Dockercomposefiles/index.md)
* [Administration](../Administration/index.md)

##  Environment Variablen 
* Alle Variablen sind gespeichert in der Datei .env im Verzeichnis /opt/letto/docker/compose/letto 
* Zuständig für die Docker-Compose Dateien aller Services mit Ausnahme von MySQL und Setup
* Unten sind die wesentlichen Variablen dokumentiert
* Das Setup-Service erstellt beim ersten Start alle notwendigen .env Dateien und belegt sie mit Standard-Werten
* Undokumentierte Variablen welche in den yml-Dateien verwendet werden sollten einen Defaultwert haben und können natürlich ebenfalls in der .env-Datei gesetzt werden. 

#### Security Variable

| Variable                 | Beschreibung                                                                                                                                          | mögliche/default Werte                |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| ADMIN_PASSWORD           | Klartextpasswort für den Admin-Benutzer am Setup-Service. Wird automatisch beim Start des Setup-Services in das ADMIN_PASSWORD_ENCRYPTED umgewandelt. |                                       |
| ADMIN_PASSWORD_ENCRYPTED | Verschlüsseltes Passwort für den Admin-Benutzer am Setup-Service. Wird automatisch beim Start des Setup-Services aus dem Klartextpasswort generiert.  |                                       |
| LETTO_LICENSE_SERVER     | URL des LeTTo-Lizenzservers, welcher für die Lizenzprüfung verwendet wird.                                                                            | https://license.letto.at/lettolicense |
| LETTO_LOCAL_PRIVATE_KEY  | Private-Key für Verschlüsselung (erforderlich)                                                                                                        |                                       |
| LETTO_LOCAL_PUBLIC_KEY   | Public-Key für Verschlüsselung - darf auch nach aussen weitergegeben werden (erforderlich)                                                            |                                       |
| LETTO_UID                | user-id des Benutzers letto im Unix-Filesystem des Host-Systems. Wird aktuell nicht verwendet                                                         |                                       |
| LETTO_RESTKEY            | Schlüssel welcher vom LeTTo-Lizenzserver für diesen Server vergeben wurde                                                                             |                                       |
| JWT_SECRET               | Secret für den JWT-Token der Token Authentifikation (erforderlich)                                                                                    |                                       |
| JWT_EXPIRATION_MS        | Gültigkeitsdauer des JWT-Tokens in Millisekunden                                                                                                      | 600000 (10 Minuten)                   |
| JWT_REFRESH_TIME_MS      | Sinkt die Token-Gültigkeit unter den Wert wird ein automatischer Token-Refresh ausgeführt.                                                            | 300000 (5 Minuten)                    |
| RUN_AS_ROOT              | Das Setup-Service wird als Benutzer root im Docker-Container ausgeführt                                                                               | true, false                           |
| Server_SECRET            | Secret für den Server-Token (erforderlich)                                                                                                            |                                       |
| SERVICE_ADMIN_PASSWORD   | Klartextpasswort für die Service to Service Kommunikation als Administrator (erforderlich)                                                            |                                       |
| SERVICE_GAST_PASSWORD    | Klartextpasswort für die Service to Service Kommunikation als Gast-Benutzer (erforderlich)                                                            |                                       |
| SERVICE_USER_PASSWORD    | Klartextpasswort für die Service to Service Kommunikation als normaler Benutzer (erforderlich)                                                        |                                       |

#### [Login](../../howto/login/index.md) Konfiguration

| Variable                  | Beschreibung                                                                                   | mögliche/default Werte |
|---------------------------|------------------------------------------------------------------------------------------------|------------------------|
| STUDEND_MULTIPLE_LOGIN    | Gibt an ob sich ein Student mehrfach am Server anmelden darf.                                  | false                  |
| STUDENT_FINGERPRINT_CHECK | Gibt an ob geprüft wird ob der Schüler bereits von einem anderen Browser/Gerät eingeloggt ist. | false                  |
 
* STUDENT_FINGERPRINT_CHECK hat nur einen Effekt bei Schülern/Studenten wenn STUDENT_MULTIPLE_LOGIN auf false gesetzt ist
* Der Fingerprint des Browsers wird bei der Anmeldung gespeichert und bei jedem Request überprüft
* Stimmt der Fingerprint nicht mehr überein wird der Benutzer automatisch ausgeloggt
* Ist beim Login eines Schülers/Studenten bereits ein anderer Login mit anderem Fingerprint aktiv wird wie folgt reagiert:
  
 | STUDENT_FINGERPRINT_CHECK | Beschreibung                                                                                                                                                                                                                                                                        |
 |---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
 | true                      | Der aktuelle Login auf dem weiteren Browser wird verweigert. Schließt oder hat der Schüler den ersten Browser bereits geschlossen kann er sich nur von diesem Browser wieder einloggen - dort müsste er sich ausloggen um sich von einem anderen Browser/Gerät einloggen zu können. |
 | false                     | Der aktuelle Login wird ausgeführt jedoch wird der Schüler, wenn kein Mehrfachlogin erlaubt ist, aus der anderen Session automatisch ausgeloggt.                                                                                                                                    |
 | true htlxy                | Für alle Schulen des Servers true, ausser bei der Schule mit dem Kürzel htlxy                                                                                                                                                                                                       |
 | false htlxy               | Für alle Schulen des Servers false, ausser bei der Schule mit dem Kürzel htlxy                                                                                                                                                                                                      |

* Jeder Lehrer kann einen eingeloggten Schüler/Studenten jederzeit abmelden (auch wenn dieser auf einem Browser eingeloggt ist).

#### Server Konfiguration

| Variable          | Beschreibung                                                                                                      | mögliche/default Werte     |
|-------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------|
| CERT_CREATED      | Gibt an ob ein Let's Encrypt Zertifikat über das Setup-Service erstellt wurde.                                    | true                       |
| CERT_EXTERN       | Gibt an ob ein externes Zertifikat verwendet werden soll                                                          | 0,1                        |
| CREATE_HTTPS_CONF | Gibt an ob die Datei https.conf der Proxy-Konfiguration automatisch beim Start des Proxy neu erzeugt werden soll. | 1,0                        |
| DOMAIN_ALTERNATIV | Liste weiterer DNS-Namen für die Erstellung des Let'e encrypt Zertifaktes, durch Leerzeichen getrennt             | s1.xy.at s1.xy.at          |
| EMAIL             | Mail Adresse des Server Administrators                                                                            |                            |
| HTTP_PORT         | Port für den HTTP-Zugriff, wird für die Weiterleitung auf HTTPS und für den Certbot (Let's encrypt) verwendet     | 80                         |
| HTTPS_PORT        | Port für den HTTPS-Zugriff                                                                                        | 443                        |
| LOCALE            | Zeichensatz des Servers, wird für alle Systembefehle im Server verwendet.                                         | de_DE.UTF-8                |
| REDIRECT          | Gibt an wohin (welcher Endpunkt) redirectet wird wenn der DNS-Name ohne Endpunkt angegeben wird                   | lettoschool                |
| SELF_SIGNED       | Gibt an ob ein selbstsigniertes Zertifkat erstellt werden soll                                                    | 1,0                        |
| SERVER_INFO       | Allgemeine Information über den Server welche auch an den Lizenzserver gesendet wird.                             | LeTTo Server HTL St.Pölten |
| SERVER_NAME       | DNS Name des Servers. Für Weiterleitungen und das Let's encrypt Zertifikat (erforderlich)                         |                            |
| TIMEZONE          | Zeitzone des Servers, wird für die Zeitstempel in den Logfiles verwendet                                          | Europe/Berlin              |
| USE_HTTP          | Gibt an ob HTTP-Anfragen an Port 80 verarbeitet (1) oder automatisch an Port 443 redirected werden sollen(0).     | 1,0                        |

#### Setup-Service Konfiguration

| Variable      | Beschreibung                                                   | mögliche/default Werte          |
|---------------|----------------------------------------------------------------|---------------------------------|
| PORT_SETUP    | Port für den Zugriff auf das Setup-Service im Docker Container | 3096                            |
| SETUP_COMPOSE | Pfad der docker-compose.yml für das Setup-Service              | /opt/letto/docker/compose/setup |

#### Download-Service Konfiguration

| Variable                 | Beschreibung                                                                                                                                          | mögliche/default Werte             |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| ADMIN_PASSWORD           | Klartextpasswort für den Admin-Benutzer am Setup-Service. Wird automatisch beim Start des Setup-Services in das ADMIN_PASSWORD_ENCRYPTED umgewandelt. |                                    |
| ADMIN_PASSWORD_ENCRYPTED | Verschlüsseltes Passwort für den Admin-Benutzer am Setup-Service. Wird automatisch beim Start des Setup-Services aus dem Klartextpasswort generiert.  |                                    |
| DOWNLOAD_USERNAME        | Benutzername für den Download-Zugriff auf das Download-Service.  (Standardmäßig deaktiviert, Passwort: SERVICE_USER_PASSWORD)                         | user                               |
| DOWNLOAD_ADMINNAME       | Benutzer mit Admin-Rechten für den ssh-Zugriff auf das Download-Service. (Standardmäßig deaktiviert, Passwort: SERVICE_ADMIN_PASSWORD)                | admin                              |        
| VOLUME_DOWNLOAD          | Pfad der Dateien welche mit einem Apache-Server(incl. php) auf den Endpunkt /download gehostet werden                                                 | /opt/letto/docker/storage/download |
| VOLUME_WIKI              | Pfad der Dateien welche mit einem Apache-Server(incl. php) auf den Endpunkt /wiki gehostet werden                                                     | /opt/letto/docker/storage/wiki     |

#### LeTTo Konfiguration

| Variable                                 | Beschreibung                                                                                                   | mögliche/default Werte                                           |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| ANGULAR_URI                              | URI des Angular-Frontends, welches für die LeTTo-App verwendet wird. (main-service)                            | https://build.letto.at/private                                   |
| LATEX_HALT_ON_ERROR                      | Gibt an ob der Export-Service bei einem Fehler im LaTeX den Druck sofort stoppen soll                          | true,false                                                       |
| LETTO_APP_DEFAULT_URI                    | Standard-URI für die LeTTo-App für die service-app wenn sie auf dem Server laufen soll                         | https://build.letto.at/private                                   |
| LETTO_MAIN_EXPORT_QUESTIONSERVICE_INTERN |                                                                                                                |                                                                  |
| LETTO_MAIN_EXPORT_QUESTIONSERVICE_URI    |                                                                                                                |                                                                  |
| LETTO_SCHULEN                            | Liste der installierten Schulen mit den Schulkürzeln durch Leerzeichen getrennt                                | schule1 schule2                                                  |
| LOGOUT_MISSING_FINGERPRINT               | Wenn bei einem Token-Refresh oder Token-Check der Browser-Fingerprint nicht passt wird der Benutzer ausgeloggt | true,false                                                       |
| PROJEKTE_ENDPOINT                        | Endpunkt für die Schülerprojekte                                                                               | projekte                                                         |
| SAVE_QUESTION_ASYNC                      | Gibt an ob die Fragen asynchron gespeichert werden sollen.                                                     | true,false                                                       |
| USEANGULAR                               | Gibt an ob die Anbindung an das Angular-Frontend verwendet werden soll.                                        | true,false                                                       |
| SERVICE_URI_PROJEKTE                     | externe Uri der Schülerprojekte - überschreibt den PROJEKTE_ENDPOINT                                           | https://${SERVER_NAME:-localhost}}/${PROJEKTE_ENDPOINT:-projekte |

#### App Konfiguration

| Variable         | Beschreibung                                                                                                                                                                  | mögliche/default Werte                                        |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| APP_SERVER_LIST  | Angabe der Server, auf denen nach Schulen für den Login gesucht wird. Wenn leer, dann werden die Schulen der akt. Instanz verwendent. Trennung der Schulen durch Leerzeichen! | Leer oder zB. build.letto.at/private  s1.letto.at s2.letto.at | 
| APP_PRIVATE_URI  | URI, unter der die Services für LeTTo-Private zu finden sind. Wenn leer, dann kein LeTTo-Private!                                                                             | Leer oder zB. https://build.letto.at/private                  |


#### Debugging Konfiguration

| Variable                    | Beschreibung                                                                                                | mögliche/default Werte |
|-----------------------------|-------------------------------------------------------------------------------------------------------------|------------------------|
| DEBUG                       | Gibt an ob die Services im Debug-Modus für Remote-Debugging gestartet werden sollen                         | true,false             |
| DEBUG_APP                   | Gibt an ob der LeTTo-App-Service im Debug-Modus für Remote-Debugging gestartet werden soll                  | true,false             |
| DEBUG_EDIT                  | Gibt an ob der Edit-Service im Debug-Modus für Remote-Debugging gestartet werden soll                       | true,false             |
| DEBUG_EXPORT                | Gibt an ob der Export-Service im Debug-Modus für Remote-Debugging gestartet werden soll                     | true,false             |
| DEBUG_LOGIN                 | Gibt an ob der Login-Service im Debug-Modus für Remote-Debugging gestartet werden soll                      | true,false             |
| DEBUG_LTI                   | Gibt an ob der LTI-Service im Debug-Modus für Remote-Debugging gestartet werden soll                        | true,false             |
| DEBUG_MAIN                  | Gibt an ob das Main-Service im Debug-Modus für Remote-Debugging gestartet werden soll                       | true,false             |
| DEBUG_PLUGIN                | Gibt an ob der Plugin-Service im Debug-Modus für Remote-Debugging gestartet werden soll                     | true,false             |
| DEBUG_PLUGINS               | Gibt an ob der Pluginuhr und Plugintester-Service im Debug-Modus für Remote-Debugging gestartet werden soll | true,false             |
| DEBUG_PLUGINSOURCECODE      | Gibt an ob der Plugin-Sourcecode-Service im Debug-Modus für Remote-Debugging gestartet werden soll          | true,false             |
| DEBUG_QUESTION              | Gibt an ob der Question-Service im Debug-Modus für Remote-Debugging gestartet werden soll                   | true,false             |
| DEBUG_SETUP                 | Gibt an ob das Setup-Service im Debug-Modus für Remote-Debugging gestartet werden soll                      | true,false             |
| DEBUG_PORT_APP              | Port für den Remote-Debugging-Zugriff auf den LeTTo-App-Service                                             | 5199                   |
| DEBUG_PORT_EDIT             | Port für den Remote-Debugging-Zugriff auf den Edit-Service                                                  | 5103                   |
| DEBUG_PORT_EXPORT           | Port für den Remote-Debugging-Zugriff auf den Export-Service                                                | 5099                   |
| DEBUG_PORT_LOGIN            | Port für den Remote-Debugging-Zugriff auf den Login-Service                                                 | 5095                   |
| DEBUG_PORT_LTI              | Port für den Remote-Debugging-Zugriff auf den LTI-Service                                                   | 5090                   |
| DEBUG_PORT_MAIN             | Port für den Remote-Debugging-Zugriff auf das Main-Service                                                  | 4180                   |
| DEBUG_PORT_PLUGIN           | Port für den Remote-Debugging-Zugriff auf den Plugin-Service                                                | 5200                   |
| DEBUG_PORT_PLUGINSOURCECODE | Port für den Remote-Debugging-Zugriff auf den Plugin-Sourcecode-Service                                     | 5204                   |
| DEBUG_PORT_PLUGIN_TESTER    | Port für den Remote-Debugging-Zugriff auf den Plugintester-Service                                          | 5290                   |
| DEBUG_PORT_PLUGIN_UHR       | Port für den Remote-Debugging-Zugriff auf den Pluginuhr-Service                                             | 5205                   |
| DEBUG_PORT_QUESTION         | Port für den Remote-Debugging-Zugriff auf den Question-Service                                              | 5102                   |
| DEBUG_PORT_SETUP            | Port für den Remote-Debugging-Zugriff auf das Setup-Service                                                 | 5096                   |
| LETTO_1_DATA_DEBUG          | Gibt an ob der Data-Service im Debug-Modus für Remote-Debugging gestartet werden soll                       | true,false             |
| LETTO_1_DEBUG_PORT_DATA     | Port für den Remote-Debugging-Zugriff auf den Data-Service                                                  | 4200                   |
| LETTO_1_DEBUG_PORT_LETTO    | Port für den Remote-Debugging-Zugriff auf den LeTTo-Service                                                 | 4100                   |
| STABLE                      | Gibt an ob die Stable-Version des LeTTo-Servers verwendet wird. nocht nicht verwendet                       | true,false             |

#### Health Check Konfiguration

| Variable                       | Beschreibung                                                                                                                 | mögliche/default Werte |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------|
| UNHEALTHY_RETRIES              | Anzahl der Versuche bis ein Service als ungesund markiert wird und neu gestartet wird                                        | 30                     |
| DATA_UNHEALTHY_RETRIES         | Anzahl der Versuche bis der Data-Service als ungesund markiert wird und neu gestartet wird                                   | 20                     |
| EDIT_UNHEALTHY_RETRIES         | Anzahl der Versuche bis der Edit-Service als ungesund markiert wird und neu gestartet wird                                   | 20                     |
| EXPORT_UNHEALTHY_RETRIES       | Anzahl der Versuche bis der Export-Service als ungesund markiert wird und neu gestartet wird                                 | 20                     |
| LETTO_UNHEALTHY_RETRIES        | Anzahl der Versuche bis der LeTTo-Service als ungesund markiert wird und neu gestartet wird                                  | 20                     |
| LOGIN_UNHEALTHY_RETRIES        | Anzahl der Versuche bis der Login-Service als ungesund markiert wird und neu gestartet wird                                  | 30                     |
| LTI_UNHEALTHY_RETRIES          | Anzahl der Versuche bis der LTI-Service als ungesund markiert wird und neu gestartet wird                                    | 20                     |
| MAIN_UNHEALTHY_RETRIES         | Anzahl der Versuche bis das Main-Service als ungesund markiert wird und neu gestartet wird                                   | 20                     |
| PLUGIN_UNHEALTHY_RETRIES       | Anzahl der Versuche bis der Plugin-Service als ungesund markiert wird und neu gestartet wird                                 | 20                     |
| PLUGINTESTER_UNHEALTHY_RETRIES | Anzahl der Versuche bis der Plugintester-Service als ungesund markiert wird und neu gestartet wird                           | 20                     |
| QUESTION_UNHEALTHY_RETRIES     | Anzahl der Versuche bis der Question-Service als ungesund markiert wird und neu gestartet wird                               | 20                     |
| SETUP_UNHEALTHY_RETRIES        | Anzahl der Versuche bis das Setup-Service als ungesund markiert wird und neu gestartet wird                                  | 20                     |
| WATCHDOG                       | Nur für Setup-Service - Gibt an ob ein Watchdog im Setup-Service aktiv ist welcher überlastete Services automatisch rebootet | ON,OFF                 |
| WATCHDOG_MAX_CPU               | CPU-Auslastung in Prozent eines Cores ab der der Watchdog ei Service als überlastet bewertet                                 | 400                    |
| WATCHDOG_MAX_TIME              | Dauerhafte Überlastung in Sekunden ab der der Watchdog einen überlastetes Service neu startet                                | 130                    |

#### Logging Konfiguration

| Variable          | Beschreibung                                                                      | mögliche/default Werte |
|-------------------|-----------------------------------------------------------------------------------|------------------------|
| LOGIN_LEVEL       | Log-Level des Login-Services                                                      | INFO,DEBUG,ERROR       |
| LOG_LEVEL_EDIT    | Log-Level des Edit-Services                                                       | INFO,DEBUG,ERROR       |
| LETTO_1_LOGAD     | Gibt an ob der LeTTo-Server Logins am Active-Directory-Server protokollieren soll | true,false             |
| LETTO_1_LOGMAXIMA | Gibt an ob die Maxima-Berechnungen genauer geloggt werden sollen                  | true,false             |

#### Datenbank Konfiguration

| Variable                            | Beschreibung                                                                           | mögliche/default Werte                                                                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MYSQL_BACKUP_PATH                   | Wird nicht verwendet                                                                   |                                                                                                                                                                           |
| MYSQL_DUMP_PATH                     | Pfad wo alle MySQL-Datenbank-Dump gespeichert werden                                   | /opt/letto/docker/storage/database-dump                                                                                                                                   |
| MYSQL_HOST                          | Containername und hostname des MySQL-Docker Containers.                                | letto-mysql                                                                                                                                                               |
| MYSQL_LTI_HOST                      | Docker-interne Adresse und Port des LTI-Services                                       | letto-mysql.nw-letto:3306                                                                                                                                                 |
| MYSQL_LTI_DATABASE                  | Datenbankname der Datenbank des LTI-Services                                           | lettolti                                                                                                                                                                  |
| MYSQL_LTI_USER                      | Datenbank user für den Zugriff auf die LTI-Datenbank                                   | lettolti                                                                                                                                                                  |
| MYSQL_LTI_PASSWORD                  | Datenbank Klartext-Passwort für den User MYSQL_LTI_USER                                |                                                                                                                                                                           |
| MYSQL_LTI_PARS                      | Datenbank Parameter für den LTI-Service                                                | useSSL=false                                                                                                                                                              |
| MYSQL_PORT                          | Port mit dem der MySQL-Server am Host zur Verfügung steht                              | 13306                                                                                                                                                                     |
| MYSQL_ROOT_PASSWORD                 | Klartextpasswort des Benutzers root am MySQL-Server                                    |                                                                                                                                                                           |
| MYSQL_VOLUME                        | Volume für die MySQL-Datenbank                                                         | lettomysql                                                                                                                                                                |
| LETTO_1_MYSQL_HOST                  | Host auf dem die Datenbank der Schule liegt                                            | letto-mysql.nw-letto:3306                                                                                                                                                 |
| LETTO_1_MYSQL_DATABASE              | Name der Datenbank für die Schule                                                      | letto_htlstp                                                                                                                                                              |
| LETTO_1_MYSQL_DATA_PARS             | Parameter für die Datenbankverbindung, welche an den Data-Service weitergegeben werden | useSSL=false&useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=Europe/Berlin                                                  |
| LETTO_1_MYSQL_LETTO_PARS            | Parameter für die Datenbankverbindung, welche an den LeTTo-Server weitergegeben werden | useSSL=false&amp;useUnicode=true&amp;useJDBCCompliantTimezoneShift=true&amp;useLegacyDatetimeCode=false&amp;serverTimezone=Europe/Berlin&amp;allowPublicKeyRetrieval=true |
| LETTO_1_MYSQL_USER                  | Benutzername für den Zugriff auf die Datenbank                                         | letto                                                                                                                                                                     |
| LETTO_1_MYSQL_PASSWORD              | Passwort für den Zugriff auf die Datenbank                                             |                                                                                                                                                                           |
| PHP_MYADMIN_HOST                    | Containername und hostname des PHP-MyAdmin                                             | phpmyadmin                                                                                                                                                                |
| REDIS_PASSWORD                      | Passwort für den Zugriff auf die Redis-Datenbank                                       |                                                                                                                                                                           |
| EDIT_REDIS_DEFAULT_DATABASE         | Standard-Datenbank am Redis-Server für den Edit-Service                                | 4                                                                                                                                                                         |
| LOGIN_REDIS_DEFAULT_DATABASE        | Standard-Datenbank am Redis-Server für den Login-Service                               | 1                                                                                                                                                                         |
| QUESTION_REDIS_DEFAULT_DATABASE     | Standard-Datenbank am Redis-Server für den Question-Service                            | 2                                                                                                                                                                         |
| MONGO_ROOT_PASSWORD                 | Klartextpasswort des Benutzers root am Mongo-Server                                    |                                                                                                                                                                           |
| EDIT_MONGO_DEFAULT_DATABASE         | Standard-Datenbank am Mongo-Server für den Edit-Service                                | edit                                                                                                                                                                      |
| EXPORT_MONGO_DEFAULT_DATABASE       | Standard-Datenbank am Mongo-Server für den Export-Service                              | export                                                                                                                                                                    |
| LEHRPLAN_MONGO_DEFAULT_DATABASE     | Standard-Datenbank am Mongo-Server für den Lehrplan-Service                            | lehrplan                                                                                                                                                                  |
| LOGIN_MONGO_DEFAULT_DATABASE        | Standard-Datenbank auf der Mongo für den Login-Service                                 | login                                                                                                                                                                     |
| PLUGIN_MONGO_DEFAULT_DATABASE       | Standard-Datenbank am Mongo-Server für den Plugin-Service                              | plugin                                                                                                                                                                    |
| PLUGINTESTER_MONGO_DEFAULT_DATABASE | Standard-Datenbank am Mongo-Server für den Plugintester-Service                        | plugintester                                                                                                                                                              |
| QUESTION_MONGO_DEFAULT_DATABASE     | Standard-Datenbank am Mongo-Server für den Question-Service                            | data  ????                                                                                                                                                                |
| SETUP_MONGO_DEFAULT_DATABASE        | Standard-Datenbank am Mongo-Server für das Setup-Service                               | setup                                                                                                                                                                     |
| VOLUME_DATABASE                     | Wird nicht verwendet                                                                   |                                                                                                                                                                           |
| ADDITIONAL_DATABASES                | Liste aller Datenbanken die zusätzlich ins Datenbankbackup integriert werden           |                                                                                                                                                                           |

#### Pfade und Volumes

| Variable         | Beschreibung                                                                                              | mögliche/default Werte              |
|------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------|
| LETTO_PATH       | Pfad in dem sich das docker und setup-Verzeichnis des LeTTo-Servers befindet (erforderlich)               | /opt/letto                          |
| SETUP_COMPOSE    | Pfad der docker-compose.yml für das Setup-Service                                                         | /opt/letto/docker/compose/setup     |
| LETTO_COMPOSE    | Pfad der docker-compose.yml für die LeTTo-Services                                                        | /opt/letto/docker/compose/letto     |
| DOCKER_BASE      | Pfad in dem sich alle Daten der Docker-Installation befinden (erforderlich)                               | /opt/letto/docker                   |
| PROXY_PATH       | Pfad der Konfigurationsdatein für den Reverse-Proxy                                                       | /opt/letto/docker/proxy             |
| VOLUME_DOWNLOAD  | Pfad der Dateien welche mit einem Apache-Server(incl. php) auf den Endpunkt /download gehostet werden     | /opt/letto/docker/storage/download  |
| VOLUME_WIKI      | Pfad der Dateien welche mit einem Apache-Server(incl. php) auf den Endpunkt /wiki gehostet werden         | /opt/letto/docker/storage/wiki      |
| VOLUME_EXPORT    | Pfad der Export- und Import-Dateien.                                                                      | /opt/letto/docker/storage/export    |
| VOLUME_IMAGES    | Pfad der Bilddateien, welche mit dem nginx-Server auf den Endpunkt /images gehostet werden                | /opt/letto/docker/storage/images    |
| VOLUME_LOG       | Pfad der Logfiles aller Services                                                                          | /opt/letto/docker/storage/log       |
| VOLUME_LOGIN     | Pfad der gespeicherte Daten des Login-Services                                                            | /opt/letto/docker/storage/login     |
| VOLUME_PHOTOS    | Pfad der Schülerphotos, welche mit dem nginx-Server auf den Endpunkt /images/photos gehostet werden       | /opt/letto/docker/storage/photos    |
| VOLUME_PLUGINS   | Pfad der PLugin-Bilddateien, welche mit dem nginx-Server auf den Endpunkt /images/plugins gehostet werden | /opt/letto/docker/storage/plugins   |
| VOLUME_PRINT     | Pfad generierten PDF-Dateien (noch nicht verwendet)                                                       | /opt/letto/docker/storage/print     |
| VOLUME_PROJEKTE  | Pfad der Schülerprojekt Dateiabgaben                                                                      | /opt/letto/docker/storage/projekte  |
| VOLUME_PUBLIC    | Pfad der statischen Webseiten, welche mit dem nginx-Server auf den Endpunkt /public gehostet werden       | /opt/letto/docker/public            |
| VOLUME_QUESTIONS | Pfad wo die Frage vom Question-Service an ein externes Question-Service gespeichert werden                | /opt/letto/docker/storage/questions |

#### Interne und externe URLs

| Variable                   | Beschreibung                                                            | mögliche/default Werte                      |
|----------------------------|-------------------------------------------------------------------------|---------------------------------------------|
| LETTO_BEURTEILUNG_URI      | Docker-Interne URL für das Beurteilungsservice - Noch nicht verwendet   | http://letto-beurteilung.nw-letto:8100      |
| LETTO_DEMO_URI             | Docker-Interne URL für Debugging-Zwecke                                 | http://letto-demo.nw-letto:8093             |
| LETTO_LETTOEDIT_URI        | Docker-Interne URL des Edit-Services                                    | http://letto-edit.nw-letto:8103             |
| LETTO_EXPORT_URI           | Docker-Interne URL des Export-Services                                  | http://letto-export.nw-letto:8099           |
| LETTO_IMAGE_URI            | Docker-Interne URL des Image-Services                                   | http://letto-image.nw-letto:8091            |
| LETTO_LEHRPLAN_URI         | URL des Lehrplan-Services                                               | http://letto-lehrplan.nw-letto:8700         |
| LETTO_LEHRPLAN_EXTERN_URI  | Externe URL des Lehrplan-Services, wird für globale Lehrpläne verwendet | https://lehrplan.letto.at/                  |
| LETTO_LETTOEDIT_URI        | Docker-Interne URL des Edit-Services                                    | http://letto-lettoedit.nw-letto:8310        |
| LETTO_LOGIN_URI            | Docker-Interne URL des Login-Services                                   | http://letto-login.nw-letto:8095            |
| LETTO_LTI_URI              | Docker-Interne URL des LTI-Services                                     | http://letto-lti.nw-letto:8090              |
| LETTO_MAIL_URI             | Noch nicht verwendet                                                    | http://letto-mail.nw-letto:8094             |
| LETTO_MATH_URI             | Docker-Interne URL des Mathematik-Services                              | http://letto-math.nw-letto:8092             |
| LETTO_PLUGIN_URI           | Docker-Interne URL des Plugin-Services                                  | http://letto-plugin.nw-letto:8200           |
| LETTO_PLUGINSOURCECODE_URI | Docker-Interne URL des Plugin-Sourcecode-Services                       | http://letto-pluginsourcecode.nw-letto:8204 |
| LETTO_PRINT_URI            | Noch nicht verwendet                                                    | http://letto-print.nw-letto:8098            |
| LETTO_QUESTION_URI         | Docker-Interne URL des Question-Services                                | http://letto-question.nw-letto:8102         |
| LETTO_SETUP_URI            | Docker-Interne URL des Setup-Services im Docker-Container               | http://letto-setup.nw-letto:8096            |
| LETTO_TEST_URI             | Noch nicht verwendet                                                    | http://letto-test.nw-letto:8101             |

#### Speicherkonfiguration

| Variable                      | Beschreibung                                                                      | mögliche/default Werte            |
|-------------------------------|-----------------------------------------------------------------------------------|-----------------------------------|
| MEMORY_LIMIT                  | Maximale verwendeter Speicher des Docker-Containers (MySQL und Setup)             | 1G                                |
| APP_MEMORY_LIMIT              | Maximale verwendeter Speicher des Docker-Containers vom App-Service               | 1G                                |
| DATA_MEMORY_LIMIT             | Maximale verwendeter Speicher des Docker-Containers vom Data-Service              | 1G                                |
| DOWNLOAD_MEMORY_LIMIT         | Maximale verwendeter Speicher des Docker-Containers vom Download-Service          | 1G                                |
| EDIT_MEMORY_LIMIT             | Maximale verwendeter Speicher des Docker-Containers vom Edit-Service              | 1G                                |
| EXPORT_MEMORY_LIMIT           | Maximale verwendeter Speicher des Docker-Containers vom Export-Service            | 5G                                |
| LETTO_MEMORY_LIMIT            | Maximale verwendeter Speicher des Docker-Containers vom Lettoserver-Service       | 6G                                |
| LOGIN_MEMORY_LIMIT            | Maximale verwendeter Speicher des Docker-Containers vom Login-Service             | 500M                              |
| LTI_MEMORY_LIMIT              | Maximale verwendeter Speicher des Docker-Containers vom LTI-Service               | 1G                                |
| MAIN_MEMORY_LIMIT             | Maximale verwendeter Speicher des Docker-Containers vom Main-Service              | 2G                                |
| MAIN_MEMORY                   | Maximal verwendeter Speicher innerhalg des Containers für den Main-Service        | 500M                              |
| MONGO_MEMORY_LIMIT            | Maximale verwendeter Speicher des Docker-Containers vom Mongo-Service             | 1G                                |
| PLUGIN_MEMORY_LIMIT           | Maximale verwendeter Speicher des Docker-Containers vom Plugin-Service            | 1G                                |
| PLUGINSOURCECODE_MEMORY_LIMIT | Maximale verwendeter Speicher des Docker-Containers vom Plugin-Sourcecode-Service | 1G                                |
| PLUGINTESTER_MEMORY_LIMIT     | Maximale verwendeter Speicher des Docker-Containers vom Plugin-Tester-Service     | 1G                                |
| PLUGINUHR_MEMORY_LIMIT        | Maximale verwendeter Speicher des Docker-Containers vom Plugin-Uhr-Service        | 1G                                |
| PROXY_MEMORY_LIMIT            | Maximale verwendeter Speicher des Docker-Containers vom Proxy-Service             | 100M                              |
| PLUGIN_MEMORY_LIMIT           | Maximale verwendeter Speicher des Docker-Containers vom Plugin-Service            | 1G                                |
| QUESTION_MEMORY_LIMIT         | Maximale verwendeter Speicher des Docker-Containers vom Question-Service          | 1G                                |
| REDIS_MEMORY_LIMIT            | Maximale verwendeter Speicher des Docker-Containers vom Redis-Service             | 1G                                |
| JAVA_OPTS_APP                 | Standard Speichereinstellungen für den App-Service                                | -Xms50m -Xmx300m                  |
| JAVA_OPTS_EDIT                | Standard Speichereinstellungen für den Edit-Service                               | -Xms50m -Xmx300m                  |
| JAVA_OPTS_EXPORT              | Standard Speichereinstellungen für das Export-Service                             | -Xms50m -Xmx4500m                 |
| JAVA_OPTS_LOGIN               | standard Speichereinstellungen für das Login-Service                              | -Xms50m -Xmx300m                  |
| JAVA_OPTS_MAIN                | Standard Speichereinstellungen für das Main-Service                               | -Xms100m -Xmx${MAIN_MEMORY:-500m} |
| JAVA_OPTS_PLUGIN              | Standard Speichereinstellungen für das Plugin-Service                             | -Xms50m -Xmx300m                  |
| JAVA_OPTS_PLUGINSOURCECODE    | Standard Speichereinstellungen für das Plugin-Sourcecode-Service                  | -Xms50m -Xmx300m                  |
| JAVA_OPTS_PLUGINTESTER        | Standard Speichereinstellungen für das Plugin-Tester-Service                      | -Xms50m -Xmx500m                  |
| JAVA_OPTS_QUESTION            | Standard Speichereinstellungen für das Question-Service                           | -Xms50m -Xmx500m                  |
| JAVA_OPTS_SETUP               | Standard Speichereinstellungen für das Setup-Service                              | -Xms50m -Xmx300m                  |
| MAIN_MEMORY_LIMIT             | Maximale verwendeter Speicher des Docker-Containers vom Main-Service              | 2G                                |
| MYADMIN_MEMORY_LIMIT          | Maximale verwendeter Speicher des Docker-Containers vom phpMyAdmin-Service        | 100M                              |
| MYSQL_MEMORY_LIMIT            | Maximale verwendeter Speicher des Docker-Containers vom MySQL-Service             | 1G                                |

#### EMail-Sender Konfiguration

| Variable                                         | Beschreibung                                                            | mögliche/default Werte |
|--------------------------------------------------|-------------------------------------------------------------------------|------------------------|
| spring_mail_host                                 | Hostname des Mail-Servers, der für den Versand von Mails verwendet wird | smtp.letto.at          |
| spring_mail_port                                 | Port des Mail-Servers, der für den Versand von Mails verwendet wird     | 587,465,...            |
| spring_mail_username                             | Benutzername für den Zugriff auf den Mail-Server                        |                        |
| spring_mail_password                             | Passwort für den Zugriff auf den Mail-Server                            |                        |
| spring_mail_properties_mail_smtp_auth            | Gibt an ob der Mail-Server eine Authentifizierung benötigt              | true,false             |
| spring_mail_properties_mail_smtp_starttls_enable | Gibt an ob der Mail-Server STARTTLS unterstützt                         | true,false             |
| spring_mail_properties_mail_smtp_ssl_enable      | Gibt an ob der Mail-Server SSL unterstützt                              | true,false             |
| spring_mail_properties_mail_debug                | Gibt an Debug Infos beim Mail ausgegeben werden sollen                  | true,false             |
| spring_mail_address_noreply                      | EMail-Adresse von der aus die Mails versendet werden                    | noreply@letto.at       |
| spring_mail_address_reply                        | EMail-Adresse an die Antworten gesendet werden                          | noreply@letto.at       |

#### Schul-spezifische Variablen

* Alle Variablen beginngn mit LETTO_X_ wobei X durch die Nummer der Schule ( 1,2,...)  zu ersetzen ist.
* Die Nummer der Schule muss mit der Nummer in der docker-compose-school.yml Datei übereinstimmen.
* Die Nummer der Schule sowie das Schulkürzel (school in docker-compose-school.yml) sollten nicht verändert werden!!
* Alle Variablen sind hier für die Schule mit der Nummer 1 dokumentiert.

| Variable                  | Beschreibung                                                                                          | mögliche/default Werte                                                                                                                                                    |
|---------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LETTO_1_SCHOOL            | Kürzel der Schule mit dem alle Verbindungen zur Schule auf diesem Server zusammenhängen               | htlstp                                                                                                                                                                    |
| LETTO_1_MYSQL_HOST        | Host auf dem die Datenbank der Schule liegt                                                           | letto-mysql.nw-letto:3306                                                                                                                                                 |
| LETTO_1_MYSQL_DATABASE    | Name der Datenbank für die Schule                                                                     | letto_htlstp                                                                                                                                                              |
| LETTO_1_MYSQL_DATA_PARS   | Parameter für die Datenbankverbindung, welche an den Data-Service weitergegeben werden                | useSSL=false&useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=Europe/Berlin                                                  |
| LETTO_1_MYSQL_LETTO_PARS  | Parameter für die Datenbankverbindung, welche an den LeTTo-Server weitergegeben werden                | useSSL=false&amp;useUnicode=true&amp;useJDBCCompliantTimezoneShift=true&amp;useLegacyDatetimeCode=false&amp;serverTimezone=Europe/Berlin&amp;allowPublicKeyRetrieval=true |
| LETTO_1_MYSQL_USER        | Benutzername für den Zugriff auf die Datenbank                                                        | letto                                                                                                                                                                     |
| LETTO_1_MYSQL_PASSWORD    | Passwort für den Zugriff auf die Datenbank                                                            |                                                                                                                                                                           |
| LETTO_1_MEMORY            | Maximale verwendeter Speicher des Docker-Containers für die Schule                                    | 500M                                                                                                                                                                      |
| LETTO_1_JAVA_OPTS_LETTO   | Standard Speichereinstellungen für den LeTTo-Server                                                   | -Xms2G -Xmx3G                                                                                                                                                             |
| LETTO_1_JAVA_OPTS_DATA    | Standard Speichereinstellungen für den Data-Service                                                   | -Xms100m -Xmx1000m                                                                                                                                                        |
| LETTO_1_DATA_DEBUG        | Gibt an ob der Data-Service im Debug-Modus für Remote-Debugging gestartet werden soll                 | true,false                                                                                                                                                                |
| LETTO_1_DEBUG_PORT_DATA   | Port für den Remote-Debugging-Zugriff auf den Data-Service                                            | 4200                                                                                                                                                                      |
| LETTO_1_DEBUG_PORT_LETTO  | Port für den Remote-Debugging-Zugriff auf den LeTTo-Service                                           | 4100                                                                                                                                                                      |
| LETTO_1_LICENCE           | Lizenz für die Schule                                                                                 |                                                                                                                                                                           |
| LETTO_1_ID_SCHULE_LIZENZ  | ID der Schule am Lizenzserver                                                                         | 234                                                                                                                                                                       |
| LETTO_1_ID_SCHULE_DATA    | ID der Schule in der MySQL-Datenbank                                                                  | 1/1                                                                                                                                                                       |
| LETTO_1_SCHULNAME         | Name der Schule, wie sie im Setup-Service angezeigt wird                                              | HTBLuVA St. Pölten                                                                                                                                                        |
| LETTO_1_DATA_MEMORY_LIMIT | Maximale verwendeter Speicher des Docker-Containers vom Data-Service - überschreibt DATA_MEMORY_LIMIT | 1.5G                                                                                                                                                                      |
| LETTO_1_DATA_URI          | Docker-Interne URL des Data-Services für die Schule                                                   | http://letto-data-htlstp.nw-letto:8300                                                                                                                                    |
| LETTO_1_DATA_USER         | Benutzername für den Zugriff auf die MySQL Datenbank der Schule                                       | letto                                                                                                                                                                     |
| LETTO_1_DATA_PASSWORD     | Passwort für den Zugriff auf die MySQL Datenbank der Schule                                           |                                                                                                                                                                           |
| LETTO_1_LETTO_URI         | Docker-Interne URL des LeTTo-Servers für die Schule                                                   | http://letto-server-htlstp.nw-letto:8080                                                                                                                                  |
| LETTO_1_LOGIN_URI_EXTERN  | Externe URL des Login-Services für die Schule                                                         | https://letto.schule.at/login                                                                                                                                             |
| LETTO_1_LETTO_URI_EXTERN  | Externe URL des LeTTo-Servers für die Schule                                                          | https://letto.schule.at/lettohtlstp                                                                                                                                       |
| LETTO_1_USEEDIT           | Gibt an ob das Edit-Service für die Schule verwendet werden soll                                      | true,false                                                                                                                                                                |
| LETTO_1_USE_AD_SERVER     | Gibt an ob ein Active-Directory-Server für die Schule verwendet werden soll                           | true,false/false                                                                                                                                                          |
| LETTO_1_LETTO_DEBUG       | Gibt an ob der LeTTo-Server im Debug-Modus gestartet werden soll                                      | true,false                                                                                                                                                                |
| LETTO_1_LOGAD             | Gibt an ob der LeTTo-Server Logins am Active-Directory-Server protokollieren soll                     | true,false                                                                                                                                                                |
| LETTO_1_LOGMAXIMA         | Gibt an ob die Maxima-Berechnungen genauer geloggt werden sollen                                      | true,false                                                                                                                                                                |

#### zusätzliche Question-Service Variablen für externe Question-Services (Verlage, etc.)

* Alle Variablen beginngn mit QUESTION_X_ wobei X durch die Nummer des Question-Services ( 1,2,...)  zu ersetzen ist.
* Die Nummer des Question-Services muss mit der Nummer in der docker-service-question-extern.yml Datei übereinstimmen.
* Alle Variablen sind hier für das Question-Service mit der Nummer 1 dokumentiert.

| Variable             | Beschreibung                                                                                                      | mögliche/default Werte |
|----------------------|-------------------------------------------------------------------------------------------------------------------|------------------------|
| QUESTION_1_NAME      | Name des Question-Services, wie er im Setup-Service angezeigt wird (container: letto-question-${QUESTION_1_NAME}) | hanser                 |
| QUESTION_1_OPEN      |                                                                                                                   | true,false/true        |
| QUESTION_1_PRERENDER |                                                                                                                   | true,false/false       |
| QUESTION_1_CACHE     |                                                                                                                   | true,false/true        |
