# Anforderungen
##  siehe auch 
* [Administration](../Administration/index.md)
* [Installation](../Installation/index.md)

##  Betrieb in Docker-Containern (empfohlen) 
###  Hardware 
####  minimal 
* 8 GB RAM
* 4 CPU Kerne
* 100GB Festplattenspeicher
* Docker fähiges Betriebssystem
* Java 21 (für das lokale Setup-Service)
* öffentlich aus dem Internet mit DNS-Namen erreichbar

####  empfohlen 
* 16 GB RAM oder mehr
* 6 CPU Kerne
* 200 GB Festplattenspeicher
* Ubuntu 22.04 oder Debian 11 
* Java 21 (wird vom setup-script mit installiert)
* öffentlich aus dem Internet mit DNS-Namen erreichbar

###  Ports 
####  eingehende Verbindungen 
* ICMP Ping
* Port 22 (ssh) für eine Remote-Konfiguration
* Port 443 (https) für den Lettoserver
* Port 9096 (https) für das Setup-Service

####  ausgehende Verbindungen 
* ICMP Ping
* DNS
* Port 80 (http) und 443 (https) zu hub.docker.com, letto.at, www.letto.at, exchange.letto.at und allen Schulserver von denen Beispiele importiert werden sollen
* DOCKER: Port 443 (https) zu allen notwendigen Adressen:  https://hub.docker.com, https://index.dockerhub.io, https://dockerhub.io, https://registry-1.docker.io, https://auth.docker.io, https://index.docker.io/, https://dseasb33srnrn.cloudfront.net/, https://production.cloudflare.docker.com/

###  Zertifikat 
* Das Zertifikat wird von letto-proxy mit einem nginx-Server und certbot realisiert. 
* Eigene Zertifikate können natürlich am nginx installiert werden, siehe dazu die nginx-Doku.

##  Betrieb direkt am Server (bestehende Systeme, wird bis September 2023 unterstützt, bis dahin sollte auf Docker umgestellt werden) 
###  Hardware 
####  minimal 
* 4 GB RAM
* 1 CPU Kern
* 50GB Festplattenspeicher
* Ubuntu 18.04, 20.04, 22.05 oder Debian 11
* Java 17
* öffentlich aus dem Internet erreichbar

####  empfohlen 
* 16 GB RAM oder mehr
* 4 CPU Kerne
* 200 GB Festplattenspeicher
* Ubuntu 22.04
* Java 17
* öffentlich aus dem Internet erreichbar
* Apache als ajp-Proxy für die Verwaltung der https-Zertifikate

###  Ports 
Der Server muss über das Internet erreichbar sein, hierzu sind folgende Anforderungen zu erfüllen:
####  eingehende Verbindungen 
* ICMP Ping
* Port 22 (ssh) für eine Remote-Konfiguration
* Port 443 (https) für den Lettoserver
* Port 9096 (https) für das Setup-Service

###  Zertifikat 
* Das Zertifikat für https wird am Besten über einen AJP-Proxy mit einem Apache2 Webserver realisiert

####  ausgehende Verbindungen 
* ICMP Ping
* DNS
* Port 80 (http) und 443 (https) zu letto.at, www.letto.at, exchange.letto.at und allen Schulserver von denen Beispiele importiert werden sollen 

= DNS = 
Der DNS-Eintrag des Servers ( und die öffentliche IP-Adresse ) müssen für die Erstellung der Lizenz bekannt sein und bei der Installation aktiv sein.

[Administration](../Administration/index.md)

