siehe auch
* [[docker compose files]]
* [[Administration]]

== MySQL Environment ==
{| class="wikitable" style="text-align: left; width: 100%;"
| Variable || Beschreibung  || mögliche/default Werte
|-
| MYSQL_ROOT_PASSWORD || Klartext-Passwort für den root-Benutzer am MySQL-Server || 
|-
| MYSQL_PORT  || Port für den MySQL-Server am Host || 13306
|-
| MYSQL_DUMP_PATH || Verzeichnis wo die Datenbank Dump gespeichert werden || /opt/letto/docker/storage/database-dump
|-
| MYSQL_BACKUP_PATH || aktuell nicht verwendet || /opt/letto/docker/storage/database-backup
|-
| MYSQL_HOST || Container und Host-Name des MySQL-Containers || letto-mysql
|-
| SERVER_NAME || Servername des Servers || zB.: letto.htlstp.ac.at
|-
| PHP_MYADMIN_HOST || Container und Host-Name des PHPmyAdmin-Containers || phpmyadmin
|-
| MEMORY_LIMIT || Maximaler Speicher der vom MySQL-Server verwendet wird || 2G
|}

