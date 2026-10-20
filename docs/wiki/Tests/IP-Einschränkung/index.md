# IP-Einschränkung
###  IP-Einschränkung für Tests 
In der neuen Version von LeTTo können IP-Bereiche für die Verwendung eines Tests definiert werden.

####  Definition bei der Testkonfiguration 
IP-Bereiche sind eine Liste von von mehreren IP-Bereichen, die durch einen Strichpunkt getrennt sind.

* Jeder IP-Bereich besteht aus 2 IP-Adressen, die aufsteigend angeordnet sein müssen.
* Der Definitionsstring kann also folgendermaßen aussehen:
  10.3.4.1-10.3.5.255;192.168.1.1-192.168.1.100

Die Benutzer können auch aus vordefinierten IP-Bereichen auswählen. Dann wird im Konfigurationsstring der Name des definierten Bereichs eingeblendet.

####  Konfiguration von vordefinierten IP-Bereichen 

Da die IP-Bereiche für die meisten Benutzer unbekannt sind, kann der Administrator für die Schule vordefinierte IP-Bereiche definieren.
Diese sind unter der Schulkonfiguration unter dem Parameter **ipRanges** definiert:
Jeder Bereich besteht aus einem Namen, gefolgt von einem Doppelpunkt und dann der IP-Definition.
Mehrere Bereiche können mit Strichpunkten getrennt definiert werden.

Syntax:
  Name1:IP1min-IP1max;Name2:IP2min-IP2max....

Bp. für Konfiguration von vordefinierten IP-Bereichen:
  WLAN:172.16.0.1-172.31.255.254;EDV-ET:10.40.0.1-10.40.255.254;ET:10.32.0.1-10.39.255.254

Dies definiert drei vordefinierte IP-Bereiche mit den Namen WLAN, ET und ET-EDV.

