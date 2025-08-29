# Docker compose files
##  siehe auch 
* [Administration](../Administration/index.md)
* [Container Struktur](../ContainerStruktur/index.md)
* [LeTTo Environment](../LeTToEnvironment/index.md)
* [Verzeichnisse und Docker-Volumes](../VerzeichnisseundDocker-Volumes/index.md)

##  Docker compose 
###  yml-Dateien für docker compose 
* Normalerweise werden alle yml-Dateien über das Setup-Service verwaltet und auch durch diese aktualisiert.
* Einen aktuellen Satz von yml-Dateien findet man bei [https://build.letto.at/download/install/yml/](https://build.letto.at/download/install/yml/)
* Beachten Sie, dass setup und mysql in einem eigenen Ordner mit separater .env Datei liegen sollten (/opt/letto/docker/compose/setup und /opt/letto/docker/compose/mysql)
* Alle weiteren .yml-Dateien verwenden eine gemeinsame .env Datei und sollten deshalb im gleichen Ordner liegen (/opt/letto/docker/compose/letto) 
* Für die Verbindung der Container über das interne Docker-Netzwerk siehe [Container Struktur](../ContainerStruktur/index.md)
* Das Setup-Service setzt eine Verzeichnisstruktur voraus (siehe [Verzeichnisse und Docker-Volumes](../VerzeichnisseundDocker-Volumes/index.md)) welche im Normalfall auf das Basisverzeichnis /opt/letto/docker aufbaut. 


| Dateiname                                                           | Download                                                                                                                                                     | Startet                        | Environment Variable                              |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|---------------------------------------------------|
| /opt/letto/docker/compose/setup/docker-compose.yml                  | [https://build.letto.at/download/install/yml/docker-compose-setup.yml](https://build.letto.at/download/install/yml/docker-compose-setup.yml)                       | Setup-Service                  | [Setup Environment](../SetupEnvironment/index.md) |
| /opt/letto/docker/compose/mysql/docker-compose.yml                  | [https://build.letto.at/download/install/yml/docker-compose-mysql.yml](https://build.letto.at/download/install/yml/docker-compose-mysql.yml)                       | MySQL-Server, phpmyadmin       | [MySQL Environment](../MySQLEnvironment/index.md) |
| /opt/letto/docker/compose/letto/docker-compose.yml                  | [https://build.letto.at/download/install/yml/docker-compose-letto.yml](https://build.letto.at/download/install/yml/docker-compose-letto.yml)                       | Login-Service, Reverse-Proxy   | [LeTTo Environment](../LeTToEnvironment/index.md) |
| /opt/letto/docker/compose/letto/docker-compose-school.yml           | [https://build.letto.at/download/install/yml/docker-compose-school.yml](https://build.letto.at/download/install/yml/docker-compose-school.yml)                     | LeTTo-Server, Data-Service     | [LeTTo Environment](../LeTToEnvironment/index.md) |
| /opt/letto/docker/compose/letto/docker-service-lti.yml              | [https://build.letto.at/download/install/yml/docker-service-lti.yml](https://build.letto.at/download/install/yml/docker-service-lti.yml)                           | LTI-Service                    | [LeTTo Environment](../LeTToEnvironment/index.md) |
| /opt/letto/docker/compose/letto/docker-service-main.yml             | [https://build.letto.at/download/install/yml/docker-service-main.yml](https://build.letto.at/download/install/yml/docker-service-main.yml)                         | neues Main-Service             | [LeTTo Environment](../LeTToEnvironment/index.md) |
| /opt/letto/docker/compose/letto/docker-service-pluginsourcecode.yml | [https://build.letto.at/download/install/yml/docker-service-pluginsourcecode.yml](https://build.letto.at/download/install/yml/docker-service-pluginsourcecode.yml) | Plugin für Java Programmabgabe | [LeTTo Environment](../LeTToEnvironment/index.md) |
| /opt/letto/docker/compose/letto/docker-service-plugins.yml          | [https://build.letto.at/download/install/yml/docker-service-plugins.yml](https://build.letto.at/download/install/yml/docker-service-plugins.yml)                   | Plugin-Sammlung von LeTTo      | [LeTTo Environment](../LeTToEnvironment/index.md) |
| /opt/letto/docker/compose/letto/docker-service-edit.yml             | [https://build.letto.at/download/install/yml/docker-service-edit.yml](https://build.letto.at/download/install/yml/docker-service-edit.yml)                         | neues Edit-Service             | [LeTTo Environment](../LeTToEnvironment/index.md) |
| /opt/letto/docker/compose/letto/docker-service-export.yml           | [https://build.letto.at/download/install/yml/docker-service-export.yml](https://build.letto.at/download/install/yml/docker-service-export.yml)                     | neues Export-Service           | [LeTTo Environment](../LeTToEnvironment/index.md) |
| /opt/letto/docker/compose/letto/docker-service-main.yml             | [https://build.letto.at/download/install/yml/docker-service-main.yml](https://build.letto.at/download/install/yml/docker-service-main.yml)                         | neues Main-Service             | [LeTTo Environment](../LeTToEnvironment/index.md) |
| /opt/letto/docker/compose/letto/docker-service-question.yml         | [https://build.letto.at/download/install/yml/docker-service-question.yml](https://build.letto.at/download/install/yml/docker-service-question.yml)                 | neues Question-Service         | [LeTTo Environment](../LeTToEnvironment/index.md) |

###  Mindestkonfiguration für den Betrieb des LeTTo-Servers Rev6539 
* MySQL-Server
* Setup-Service
* LeTTo-Proxy - neben der Revers-Proxy-Funktion stellt er auch alle Java-Script-Dateien und statischen Inhalte für den LeTTo-Server zur Verfügung
* Login-Service
* Lettoserver und Data-Service (in einer gemeinsamen .yml-Datei)
* Alle weiteren Services sind für die neueren Funktionalitäten und Weiterentwicklungen notwendig und können je nach Bedarf dazu installiert werden. 

##  Proxy Konfiguration 
* In der Standard-Installation wird ein leicht modifizierter nginx-reverse-proxy verwendet
* Die Konfigurationsdateien (.conf) für den Proxy liegen im Normalfall im Verzeichnis /opt/letto/docker/proxy
* Im Normalfall werden die Konfigurationsdateien über das Setup-Service verwaltet
* Vorlagen für die Konfigurationsdateien findet man aber auch am [https://build.letto.at/download/install/proxy/](https://build.letto.at/download/install/proxy/)

###  Container auf Dockerhub 
Doku in Arbeit

| Name                                                     | Beschreibung                  |
|----------------------------------------------------------|-------------------------------|
| [lettohub/letto-setup](/notimplemented/index.md)         | Setup-Service                 |
| [lettohub/letto-service-login](/notimplemented/index.md) | LeTTo Login-Service           |
| [lettohub/letto-proxy](/notimplemented/index.md)         | nginx-based reverse proxy     |
| [lettohub/letto-mysql](/notimplemented/index.md)         | MySQL-Server                  |
| [lettohub/lettoserver](/notimplemented/index.md)         | LeTTo Hauptprogramm (aktuell) |
| [lettohub/letto-service-data](/notimplemented/index.md)  | LeTTo Data-Service            |


[Administration](../Administration/index.md)

