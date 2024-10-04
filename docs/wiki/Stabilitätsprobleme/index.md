# Stabilitätsprobleme
####  siehe auch 
* [Administration](../Administration/index.md)
* [Installation ](../Installation/index.md) 

= Betrieb von LeTTo in Docker-Containern = 
* Doku in Arbeit

= Betrieb eines lokalen LeTTo-Servers mit TomEE-Server = 
* Im Betrieb des Servers kann es (vor allem bei der Verwendung von tagesaktuellen Versionen) zu **Serverabstürzen** kommen wodurch dann der Betrieb von Letto nicht mehr funktioniert. 
* Hat sich nur die Letto-Instanz "erhängt", reicht es die Letto-Instanz neu zu starten. /opt/letto/restart.sh oder /opt/letto/start.sh
* Information über die PID der laufenden LeTTo-Instanz bzw. ob der Server überhaupt läuft erhält man mit /opt/letto/status.sh
* Das sich der Linux-Server selbst erhängt hat ist bei uns im Betrieb noch nicht aufgetreten und ist dann auf eine Fehlkonfiguration des Servers oder meist auf einen Hardwaredefekt zurück zu führen.
* Keine Software kann fehlerfrei programmiert werden, wodurch es immer wieder einmal zu einem Server-Absturz kommen kann. Wir versuchen unser Möglichstes um solche Abstürze möglichst zu verhindern.
* Probleme beim Betrieb des TomEE-Servers werden in der Datei /opt/tomee/logs/catalina.out dokumentiert. Falls die Datei sehr groß ist und häufige Fehler auftreten ist es ratsam den Server zu stoppen (/opt/letto/stop.sh), die Datei catalina.out zu löschen (ggf. zu sichern) und dann den Server neu zu starten, dann ist die Logdatei überschaubarer.

###  Watchdog 
* Da der Server-Administrator nicht immer sofort mitbekommt das der Serverdienst nicht mehr verfügbar ist bietet sich an den Server automatisch neu zu starten.
* Das automatische Neustarten des Servers kann über das LTI-Service realisiert werden
* Während der **Datensicherung** kann es auch zu Verzögerungen des Servers kommen. Um einen Restart des Servers während der Datensicherung zu verhindern ist es sinnvoll zu Beginn der Datensicherung die Datei welche als "sicherungslock" angegeben ist anzulegen und zum Ende der Sicherung die Datei wieder zu löschen. Das Watchdog-Script restartet dann den Server niemals während einer Sicherung. Hängt die Sicherung bleibt dann natürlich der Watchdog auch hängen (ist bei uns aber noch nie passiert).

###  Prüfen der Serveraktivität über eine Anfrage am Webserver 
Haben wir bei uns noch nicht realisiert, ist aber sicher auch möglich.

[Administration](../Administration/index.md)

