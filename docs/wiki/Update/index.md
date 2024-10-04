# Update
##  Update Einspielen 
Das Update des Letto-Servers erfolgt durch das Einspielen einer neueren **letto.war** Datei. Diese Datei kann über den [Download-Link](https://letto.at/download/letto) heruntergeladen werden, der von uns per Email bereitgestellt wurde.

Prinzipiell gibt es mehrere Möglichkeiten die war-Datei einzuspielen, nämlich direkt durch kopieren der neuen letto.war nach /opt/tomee/webapps/letto.war, über das Updatescript /opt/letto/update.sh, über das Setup-Service wenn es installiert ist und als globaler Administrator direkt aus LeTTo heraus über das LTI-Service welches dazu laufen muss.

Bei einem nicht-automatisierten Update bitte darauf achten, dass die war-Datei bzw. das Update-Script als der Benutzer ausgeführt wird, mit dem auch der TomEE-Server gestartet wird!

##  Download-Server 
* Der Download der aktuellen Version von letto erfolgt von [https://letto.at/download/letto/](https://letto.at/download/letto/)
* Eine gültiger Download-Benutzer und das dazugehörige Passwort wird gleichzeitig mit der Lizenzvergabe vergeben, bzw. kann auch bei [office@letto.at](mailto://office@letto.at) angefragt werden.
* Folgende Dateien stehen auf dem Download-Server zur Verfügung:

| Datei               | Inhalt                                                                              |
|---------------------|-------------------------------------------------------------------------------------|
| letto-daily.war     | tagesaktuelle Version von Letto                                                     |
| daily-revision.txt  | Revisionsnummer der tagesaktuellen Version                                          |
| letto-stable.war    | aktuelle Stable-Version von Letto                                                   |
| stable-revision.txt | Revisionsnummer der Stable-Version                                                  |
| lettoupdate.sh      | Update-Script für den automatischen Download und die Installation des Letto-Updates |
| archiv              | Verzeichnis aller älteren Versionen von Letto                                       |


[Administration](../Administration/index.md)

