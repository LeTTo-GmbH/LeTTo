siehe auch
* [[docker compose files]]
* [[Administration]]

== Setup Environment ==
{| class="wikitable" style="text-align: left; width: 100%;"
| Variable || Beschreibung  || mögliche/default Werte
|-
| LETTO_UID     || user-id des Benutzers letto im Unix-Filesystem des Host-Systems. Wird aktuell nicht verwendet || 
|-
| RUN_AS_ROOT   || Das Setup-Service wird als Benutzer root im Docker-Container ausgeführt || true, false 
|-
| LETTO_RESTKEY || Schlüssel welcher vom LeTTo-Lizenzserver für diesen Server vergeben wurde || 
|-
| LETTO_PATH || Pfad in dem sich das docker und setup-Verzeichnis des LeTTo-Servers befindet || /opt/letto
|-
| SETUP_COMPOSE || Pfad der docker-compose.yml für das Setup-Service || /opt/letto/docker/compose/setup
|-
| LETTO_COMPOSE || Pfad der docker-compose.yml für die LeTTo-Services || /opt/letto/docker/compose/letto
|-
| HOST_BS       || Betriebssystem des Host-Rechners. Notwendig um Startscripts,etc. korrekt zu erstellen || LINUX, WINDOWS, MAC
|-
| PATH_SEPERATOR  || Pfad-Trennzeichen des Host-Betriebssystems || /,\
|-
| STABLE          || wird nicht mehr verwendet || false
|-
| DEBUG           || ermöglicht Debug-Konfigurationen im Setup-Service || false,true
|-
| SETUP_MAIN      || Definiert welches Setup-Service die Master-Rolle übernehmen soll. || AUTO, DOCKER, LOCAL
|-
| SERVICE_USER_PASSWORD || Klartextpasswort für die Service to Service Kommunikation als normaler Benutzer ||
|-
| SERVICE_GAST_PASSWORD || Klartextpasswort für die Service to Service Kommunikation als Gast-Benutzer ||
|-
| SERVICE_ADMIN_PASSWORD|| Klartextpasswort für die Service to Service Kommunikation als Administrator ||
|-
| JWT_SECRET || Secret für den JWT-Token der Token Authentifikation ||
|-
| Server_SECRET || Secret für den Server-Token ||
|-
| LETTO_LOCAL_PRIVATE_KEY || Private-Key für Verschlüsselung ||
|-
| LETTO_LOCAL_PUBLIC_KEY  || Public-Key für Verschlüsselung - darf auch nach aussen weitergegeben werden || 
|-
| ADMIN_LOGFILE_WITH_DOCKER || Logfiles mit dem Setup-Service im Docker-Container verwalten || false, true
|-
| WATCHDOG || Analysiert die CPU-Auslastung der Dockercontainer und restartet Container bei zu starker CPU-Belastung auch wenn sie noch healthy sind. || false, true
|-
| WATCHDOG_MAX_CPU || CPU-Last in Prozent eines Cores, welche für den Watchdog dauernd für WACHDOG_MAX_TIME Sekunden überschritten sein muss. || 
|-
| WATCHDOG_MAX_TIME || Zeit in Sekunden ab der der Watchdog anschlägt. ||
|-
| ADMIN_PASSWORD || Wenn hier ein Klartextpasswort gesetzt ist wird beim Start des Setup-Services ein Passwort-Hash in ADMIN_PASSWORD_ENCRYPTED gespeichert und dieser Eintrag gelöscht. ||
|-
| ADMIN_PASSWORD_ENCRYPTED || Passwort Hash des Admin-Passwortes für den Login mit dem User "admin" am Setup-Service ||
|-
| HTTPS_PORT || Port der für das Setup-Service am Host für https(selbstsigniert) reserviert wird. ||
|-
| SETUP_UPDATE || Standard Update-Plan für das Setup-Service. Aktuell nicht verwendet || daily,stable,beta
|-
| LOCAL_BACKIUP || Gibt an ob der Datenbank-Dump(Datensicherung) vom Setup-Service am Host gemacht werden soll. Andernfalls vom Docker-Setup-Service. || true, false
|-
| REFRESH_LETS_ENCRYPT_AUTO || Gibt an ob das Lets-Encrypt Zertifikat bei der Datensicherung automatisch mit dem Certbot erneuert werden soll || false,true
|-
| CHECK_LICENSE_AUTO || Gibt an ob die Lizenz automatisch bei der Datensicherung aktualisiert werden soll. || true, false
|-
| TIME_DAILY_BACKUP || Zeitpunkt zu dem die Datensicherung(Database-Dump) ausgeführt wird. || hh:mm
|-
| BACKUP_STOP_LETTO || vor dem Backup wird der LeTTo-Server gestoppt und nachher wieder gestartet || true, false
|-
| BACKUP_MIN_FREE_DISK_SPACE_MB || Vor dem Backup wird geprüft ob der Speicherplatz in MB mindestens im Filesystem vorhanden ist und ggf. werden alte Datenbank-Dumps gelöscht. || 
|-
| BACKUP_DATABASE || Zum Datensicherungszeitpunkt wird ein Datenbankdump ausgeführt.  || true, false
|-
| BACKUP_DATABASE_DAY_OF_WEEK || Es wird für den aktuellen Wochentag eine Kopie des aktuellen Datenbank-Dumps erstellt. || true, false
|-
| BACKUP_DATABASE_MONTHLY_IMAGE || Es wird am ersten jeden Monats eine Kopie des aktuellen Datenbank-Dumps erstellt.  || true, false
|-
| BACKUP_IMAGE || nicht verwendet || false, true
|-
| BACKUP_IMAGE_DAY_OF_WEEK || nicht verwendet || false, true
|-
| BACKUP_IMAGE_MONTHLY_IMAGE || nicht verwendet || false, true
|-
| BACKUP_PROJEKTE || nicht verwendet || false, true
|-
| BACKUP_PROJEKTE_DAY_OF_WEEK || nicht verwendet || false, true
|-
| BACKUP_PROJEKTE_MONTHLY_IMAGE || nicht verwendet || false, true
|-
|}

