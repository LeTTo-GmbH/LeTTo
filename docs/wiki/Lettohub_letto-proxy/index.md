# Lettohub/letto-proxy
siehe auch
* [docker compose files](/notimplemented/index.md)

##  Reverse Proxy-Server 
###  Container 
**lettohub/letto-proxy**

###  Tags 

| Tag     | Beschreibung                                                                         | Anmerkung |
|---------|--------------------------------------------------------------------------------------|-----------|
| beta    | Beta Version für Beta-Test-Phasen, nicht für den Produktivbetrieb                    |           |
| daily   | tagesaktuelle Letztversion für den Produktivbetrieb von ausgewählten Testschulen     |           |
| stable  | letzte stabile Version für den Produktivbetrieb                                      |           |
| debug   | Bitte nicht verwenden ist tagesaktuell nur für Debugging-Zwecke                      |           |
| revXXXX | Revision mit der Nummer XXXX. Nur wenn man eine definierte Version verwenden möchte. |           |


###  Ports 

| Port | Beschreibung |
|------|--------------|
| 80   | http-Port    |
| 443  | https-Port   |


###  Pfade welche als Volume verbunden werden sollten 


| Pfad im Docker Container     | Beschreibung                                                       | üblicher Wert                      |
|------------------------------|--------------------------------------------------------------------|------------------------------------|
| /etc/nginx/conf.d/include    | Verzeichnis wo alle Konfigurationsdateien des nginx-Servers liegen | /opt/letto/docker/proxy            |
| /etc/letsencrypt             | Docker-Volume wo die Zertifikat gespeichert sind                   | certs                              |
| /data/letsencrypt            | Docker-Volume für die Zertifikatsinformationen für den Certbot     | certs-data                         |
| /etc/cert                    | eigene Zertifikate welche nicht automatisch erstellt werden        | /opt/letto/docker/cert             |
| /var/www/html/images         | Bilddateien                                                        | /opt/letto/docker/storage/images   |
| /var/www/html/images/photos  | Schülerphotos-Verzeichnis                                          | /opt/letto/docker/storage/photos   |
| /var/www/html/images/plugins | Plugin-Bilder-Verzeichnis                                          | /opt/letto/docker/storage/plugins  |
| /var/www/html/projekte       | Schülerabgaben Verzeichnis                                         | /opt/letto/docker/storage/projekte |
| /var/www/html/print          | PDF-Ausdrucke                                                      | /opt/letto/docker/storage/print    |
| /var/www/html/export         | Export-Dateien für Import und Export                               | /opt/letto/docker/storage/export   |
| /var/www/html/public         | veränderbare statische Inhalte zB. für Werbung                     | /opt/letto/docker/public           |
| /log                         | Verzeichnis für die Logfiles                                       | /opt/letto/docker/storage/log      |


###  Environment Variable 

| Variable          | Beschreibung                                                                                                      | üblicher Wert     | muss gesetzt sein |
|-------------------|-------------------------------------------------------------------------------------------------------------------|-------------------|-------------------|
| TZ                | Zeitzone                                                                                                          | Europe/Berlin     | nein              |
| LC_ALL            | Spracheinstellung                                                                                                 | de_DE.UTF-8       | nein              |
| SERVER_NAME       | DNS Name des Servers. Für Weiterleitungen und das Let's encrypt Zertifikat                                        |                   | ja                |
| EMAIL             | Mail Adresse des Server Administrators                                                                            |                   | ja                |
| REDIRECT          | Gibt an wohin (welcher Endpunkt) redirectet wird wenn der DNS-Name ohne Endpunkt angegeben wird                   | lettoschool       | ja                |
| DOMAIN_ALTERNATIV | Liste weiterer DNS-Namen für die Erstellung des Let'e encrypt Zertifaktes, durch Leerzeichen getrennt             | s1.xy.at s1.xy.at | nein              |
| SELF_SIGNED       | Gibt an ob ein selbstsigniertes Zertifkat erstellt werden soll                                                    | 1                 | ja                |
| CERT_EXTERN       | Gibt an ob ein externes Zertifikat verwendet werden soll                                                          | 0                 | ja                |
| CREATE_HTTPS_CONF | Gibt an ob die Datei https.conf der Proxy-Konfiguration automatisch beim Start des Proxy neu erzeugt werden soll. | 1                 | ja                |
| USE_HTTP          | Gibt an ob HTTP-Anfragen an Port 80 verarbeitet (1) oder automatisch an Port 443 redirected werden sollen(0).     | 0                 | ja                |


##  Docker Compose 
* .yml File: [https://build.letto.at/download/install/yml/docker-compose-letto.yml](https://build.letto.at/download/install/yml/docker-compose-letto.yml)
* Environment Einstellungen für die .env-Datei [LeTTo Environment](../LeTToEnvironment/index.md)

[Administration](../Administration/index.md)

