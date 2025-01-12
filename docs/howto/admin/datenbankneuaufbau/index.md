# Neuaufbau der Datenbank aus der Datensicherung

* Bei einem totalen Crash der Datenbank kann es notwendig sein die Datenbank komplett neu aufzubauen und aus den
Datensicherungen wiederherzustellen.
* Bei dem Vorgang wird das Volume der Datenbank inklusive aller Datenbanken komplett gelöscht, und dann die LeTTo-Schuldatenbank aus der Datensicherung wiederhergestellt.
* Versichern sie sich vor dem Löschen des Volumes dass die Datensicherung auch wirklich aktuell und vollständig im Verzeichnis /opt/letto/docker/storage/database-dump liegt.

## Vorgangsweise 
* Stopp aller Schulen (für jede Schule) und des LTI-Dienstes wenn es vorhanden ist
  <pre>
  cd /opt/letto/docker/compose/letto
  docker compose -f docker-compose-schulname.yml down
  docker compose -f docker-service-lti.yml down
  </pre>  
* Stopp des Mysql-Docker-Containers
  <pre>
  cd /opt/letto/docker/compose/mysql
  docker compose down
  </pre>
* Lösche das Volume lettomysql und lege es neu an
  <pre>
  docker volume remove lettomysql
  docker volume create lettomysql
  </pre>
* Start des MySQL-Docker-Containers und Initialisierung der Datenbank
  <pre>
  docker compose up -d
  docker exec -it letto-mysql /init-db.sh
  docker exec -it letto-mysql cua letto DAS_LETTO_MYSQL_PASSWORT_AUS_DER_ENV_DATEI
  docker exec -it letto-mysql cua lettolti DAS_LETTOLTI_MYSQL_PASSWORT_AUS_DER_ENV_DATEI
  </pre>
* Importieren der Schuldatenbanken für jede Schule
  <pre>
  docker exec -it letto-mysql import letto_schulname
  </pre>
* Importieren der LTI-Datenbank
  <pre>
  docker exec -it letto-mysql import lettolti
  </pre>
* Start aller Schulen (für jede Schule) und des LTI-Dienstes wenn es vorhanden ist
  <pre>
  cd /opt/letto/docker/compose/letto
  docker compose -f docker-compose-schulname.yml up -d
  docker compose -f docker-service-lti.yml up -d
  </pre>  
