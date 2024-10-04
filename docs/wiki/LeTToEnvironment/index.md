# LeTTo Environment
siehe auch
* [docker compose files](/notimplemented/index.md)
* [Administration](../Administration/index.md)

##  Environment Variablen 
* Alle Variablen sind gespeichert in der Datei .env im Verzeichnis /opt/letto/docker/compose/letto 
* Zuständig für die Docker-Compose Dateien aller Services mit Ausnahme von MySQL und Setup
* Unten sind die wesentlichen Variablen dokumentiert
* Das Setup-Service erstellt beim ersten Start alle notwendigen .env Dateien und belegt sie mit Standard-Werten
* Undokumentierte Variablen welche in den yml-Dateien verwendet werden sollten einen Defaultwert haben und können natürlich ebenfalls in der .env-Datei gesetzt werden. 

###  LeTTo Environment 
<div  class="wikitable" style="text-align: left; width: 100%;" >

| Variable                   | Beschreibung                                                                                                      | mögliche/default Werte                      |
|----------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| LETTO_UID                  | user-id des Benutzers letto im Unix-Filesystem des Host-Systems. Wird aktuell nicht verwendet                     |                                             |
| RUN_AS_ROOT                | Das Setup-Service wird als Benutzer root im Docker-Container ausgeführt                                           | true, false                                 |
| LETTO_RESTKEY              | Schlüssel welcher vom LeTTo-Lizenzserver für diesen Server vergeben wurde                                         |                                             |
| SERVICE_USER_PASSWORD      | Klartextpasswort für die Service to Service Kommunikation als normaler Benutzer (erforderlich)                    |                                             |
| SERVICE_GAST_PASSWORD      | Klartextpasswort für die Service to Service Kommunikation als Gast-Benutzer (erforderlich)                        |                                             |
| SERVICE_ADMIN_PASSWORD     | Klartextpasswort für die Service to Service Kommunikation als Administrator (erforderlich)                        |                                             |
| JWT_SECRET                 | Secret für den JWT-Token der Token Authentifikation (erforderlich)                                                |                                             |
| Server_SECRET              | Secret für den Server-Token (erforderlich)                                                                        |                                             |
| LETTO_LOCAL_PRIVATE_KEY    | Private-Key für Verschlüsselung (erforderlich)                                                                    |                                             |
| LETTO_LOCAL_PUBLIC_KEY     | Public-Key für Verschlüsselung - darf auch nach aussen weitergegeben werden (erforderlich)                        |                                             |
| SERVER_NAME                | DNS Name des Servers. Für Weiterleitungen und das Let's encrypt Zertifikat (erforderlich)                         |                                             |
| DOMAIN_ALTERNATIV          | Liste weiterer DNS-Namen für die Erstellung des Let'e encrypt Zertifaktes, durch Leerzeichen getrennt             | s1.xy.at s1.xy.at                           |
| SERVER_INFO                | Allgemeine Information über den Server welche auch an den Lizenzserver gesendet wird.                             | LeTTo Server HTL St.Pölten                  |
| EMAIL                      | Mail Adresse des Server Administrators                                                                            |                                             |
| REDIRECT                   | Gibt an wohin (welcher Endpunkt) redirectet wird wenn der DNS-Name ohne Endpunkt angegeben wird                   | lettoschool                                 |
| LETTO_PATH                 | Pfad in dem sich das docker und setup-Verzeichnis des LeTTo-Servers befindet (erforderlich)                       | /opt/letto                                  |
| SETUP_COMPOSE              | Pfad der docker-compose.yml für das Setup-Service                                                                 | /opt/letto/docker/compose/setup             |
| LETTO_COMPOSE              | Pfad der docker-compose.yml für die LeTTo-Services                                                                | /opt/letto/docker/compose/letto             |
| DOCKER_BASE                | Pfad in dem sich alle Daten der Docker-Installation befinden (erforderlich)                                       | /opt/letto/docker                           |
| CERT_CREATED               | Gibt an ob ein Let's Encrypt Zertifikat über das Setup-Service erstellt wurde.                                    | true                                        |
| MYSQL_ROOT_PASSWORD        | Klartextpasswort des Benutzers root am MySQL-Server                                                               |                                             |
| MYSQL_PORT                 | Port mit dem der MySQL-Server am Host zur Verfügung steht                                                         | 13306                                       |
| MYSQL_HOST                 | Containername und hostname des MySQL-Docker Containers.                                                           | letto-mysql                                 |
| VOLUME_DATABASE            | Wird nicht verwendet                                                                                              |                                             |
| MYSQL_DUMP_PATH            | Pfad wo alle MySQL-Datenbank-Dump gespeichert werden                                                              | /opt/letto/docker/storage/database-dump     |
| MYSQL_BACKUP_PATH          | Wird nicht verwendet                                                                                              |                                             |
| PHP_MYADMIN_HOST           | Containername und hostname des PHP-MyAdmin                                                                        | phpmyadmin                                  |
| MYSQL_LTI_HOST             | Docker-interne Adresse und Port des LTI-Services                                                                  | letto-mysql.nw-letto:3306                   |
| MYSQL_LTI_DATABASE         | Datenbankname der Datenbank des LTI-Services                                                                      | lettolti                                    |
| MYSQL_LTI_USER             | Datenbank user für den Zugriff auf die LTI-Datenbank                                                              | lettolti                                    |
| MYSQL_LTI_PASSWORD         | Datenbank Klartext-Passwort für den User MYSQL_LTI_USER                                                           |                                             |
| PROXY_PATH                 | Pfad der Konfigurationsdatein für den Reverse-Proxy                                                               | /opt/letto/docker/proxy                     |
| VOLUME_PUBLIC              | Pfad der statischen Webseiten, welche mit dem nginx-Server auf den Endpunkt /public gehostet werden               | /opt/letto/docker/public                    |
| VOLUME_IMAGES              | Pfad der Bilddateien, welche mit dem nginx-Server auf den Endpunkt /images gehostet werden                        | /opt/letto/docker/storage/images            |
| VOLUME_PLUGINS             | Pfad der PLugin-Bilddateien, welche mit dem nginx-Server auf den Endpunkt /images/plugins gehostet werden         | /opt/letto/docker/storage/plugins           |
| VOLUME_PHOTOS              | Pfad der Schülerphotos, welche mit dem nginx-Server auf den Endpunkt /images/photos gehostet werden               | /opt/letto/docker/storage/photos            |
| VOLUME_PROJEKTE            | Pfad der Schülerprojekt Dateiabgaben                                                                              | /opt/letto/docker/storage/projekte          |
| VOLUME_PRINT               | Pfad generierten PDF-Dateien (noch nicht verwendet)                                                               | /opt/letto/docker/storage/print             |
| VOLUME_EXPORT              | Pfad der Export- und Import-Dateien.                                                                              | /opt/letto/docker/storage/export            |
| VOLUME_LOG                 | Pfad der Logfiles aller Services                                                                                  | /opt/letto/docker/storage/log               |
| LETTO_LTI_URI              | Docker-Interne URL des LTI-Services                                                                               | http://letto-lti.nw-letto:8090              |
| LETTO_IMAGE_URI            | Docker-Interne URL des Image-Services                                                                             | http://letto-image.nw-letto:8091            |
| LETTO_MATH_URI             | Docker-Interne URL des Mathematik-Services                                                                        | http://letto-math.nw-letto:8092             |
| LETTO_DEMO_URI             | Docker-Interne URL für Debugging-Zwecke                                                                           | http://letto-demo.nw-letto:8093             |
| LETTO_MAIL_URI             | Noch nicht verwendet                                                                                              | http://letto-mail.nw-letto:8094             |
| LETTO_LOGIN_URI            | Docker-Interne URL des Login-Services                                                                             | http://letto-login.nw-letto:8095            |
| LETTO_SETUP_URI            | Docker-Interne URL des Setup-Services im Docker-Container                                                         | http://letto-setup.nw-letto:8096            |
| LETTO_PRINT_URI            | Noch nicht verwendet                                                                                              | http://letto-print.nw-letto:8098            |
| LETTO_EXPORT_URI           | Docker-Interne URL des Export-Services                                                                            | http://letto-export.nw-letto:8099           |
| LETTO_BEURTEILUNG_URI      | Noch nicht verwendet                                                                                              | http://letto-beurteilung.nw-letto:8100      |
| LETTO_TEST_URI             | Noch nicht verwendet                                                                                              | http://letto-test.nw-letto:8101             |
| LETTO_QUESTION_URI         | Docker-Interne URL des Question-Services                                                                          | http://letto-question.nw-letto:8102         |
| LETTO_PLUGIN_URI           | Docker-Interne URL des Plugin-Services                                                                            | http://letto-plugin.nw-letto:8200           |
| LETTO_PLUGINSOURCECODE_URI | Docker-Interne URL des Plugin-Sourcecode-Services                                                                 | http://letto-pluginsourcecode.nw-letto:8204 |
| LETTO_LETTOEDIT_URI        | Docker-Interne URL des Edit-Services                                                                              | http://letto-lettoedit.nw-letto:8310        |
| LETTO_LEHRPLAN_URI         | URL des Lehrplan-Services                                                                                         | http://letto-lehrplan.nw-letto:8700         |
| LETTO_SCHULEN              | Liste der installierten Schulen mit den Schulkürzeln durch Leerzeichen getrennt                                   | schule1 schule2                             |
| MAIN_MEMORY_LIMIT          | Maximale verwendeter Speicher des Docker-Containers vom Main-Service                                              |                                             |
| LETTO_MEMORY_LIMIT         | Maximale verwendeter Speicher des Docker-Containers vom Main-Service                                              |                                             |
| DATA_MEMORY_LIMIT          | Maximale verwendeter Speicher des Docker-Containers vom Main-Service                                              |                                             |
| LETTO_MEMORY_LIMIT         | Maximale verwendeter Speicher des Docker-Containers vom Main-Service                                              |                                             |
| LOGIN_MEMORY_LIMIT         | Maximale verwendeter Speicher des Docker-Containers vom Main-Service                                              |                                             |
| JAVA_OPTS_LOGIN            | standard Speichereinstellungen für das Login-Service                                                              | -Xms50m -Xmx80m                             |
| SELF_SIGNED                | Gibt an ob ein selbstsigniertes Zertifkat erstellt werden soll                                                    | 1,0                                         |
| CERT_EXTERN                | Gibt an ob ein externes Zertifikat verwendet werden soll                                                          | 0,1                                         |
| CREATE_HTTPS_CONF          | Gibt an ob die Datei https.conf der Proxy-Konfiguration automatisch beim Start des Proxy neu erzeugt werden soll. | 1,0                                         |
| USE_HTTP                   | Gibt an ob HTTP-Anfragen an Port 80 verarbeitet (1) oder automatisch an Port 443 redirected werden sollen(0).     | 1,0                                         |
</div>

###  Environment Variablen für jede installierte Schule 
* Alle Variablen beginngn mit LETTO_X_ wobei X durch die Nummer der Schule ( 1,2,...)  zu ersetzen ist. 
* Die Nummer der Schule muss mit der Nummer in der docker-compose-school.yml Datei übereinstimmen. 
* Die Nummer der Schule sowie das Schulkürzel (school in docker-compose-school.yml) sollten nicht verändert werden!!
