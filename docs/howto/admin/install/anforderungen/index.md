# Anforderungen an die virtuelle Maschine eines LeTTo-Servers
* In dem virtuellen Server wo der LeTTo-Server läuft wird ein Docker-System installiert
* Als Betriebssystem des virtuellen Servers empfehlen wir Ubuntu-Server LTS (22.04)

## Hardware
### minimale Anforderungen
* 8 GB RAM
* 4 CPU Kerne
* 100GB Festplattenspeicher
* Docker fähiges Betriebssystem
* Java 21 (wird vom setup-script mit installiert)
* öffentlich aus dem Internet mit DNS-Namen erreichbar

### empfohlen
* 16 GB RAM oder mehr
* 6 CPU Kerne
* 200 GB Festplattenspeicher
* Ubuntu 22.04
* Java 21 (wird vom setup-script mit installiert)
* öffentlich aus dem Internet mit DNS-Namen erreichbar
  
## Ports
### eingehende Verbindungen
* ICMP Ping
* Port 22 (ssh) für eine Remote-Konfiguration
* Port 443 (https) für den Lettoserver
* Port 9096 (https) für das Setup-Service

### ausgehende Verbindungen
* ICMP Ping
* DNS
* Port 80 (http) und 443 (https) zu hub.docker.com, letto.at, www.letto.at, exchange.letto.at und allen Schulserver von denen Beispiele importiert werden sollen
* DOCKER: Port 443 (https) zu allen notwendigen Adressen:  https://hub.docker.com, https://index.dockerhub.io, https://dockerhub.io, https://registry-1.docker.io, https://auth.docker.io, https://index.docker.io/, https://dseasb33srnrn.cloudfront.net/, https://production.cloudflare.docker.com/

## Zertifikat
* Das Zertifikat wird von letto-proxy mit einem nginx-Server und certbot realisiert.
* Eigene Zertifikate können natürlich am nginx installiert werden, siehe dazu die nginx-Doku.

# DNS
Der DNS-Eintrag des Servers ( und die öffentliche IP-Adresse ) müssen für die Erstellung der Lizenz bekannt sein und bei der Installation aktiv sein.
