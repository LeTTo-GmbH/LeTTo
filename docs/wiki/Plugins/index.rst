==Plugin==
===Allgemeines:===
* Plugins sind kleine Unterprogramme, welche in allen Fragetypen verwendet werden können und Graphiken, Texte und Berechnungen automatisch generieren können.
* Die Definition eines Plugins erfolgt über einen Definitionsstring und dem Plugin-Typ. zB. erzeugt der Pluginstring "R+C" der Plugins "WSR" eine Serienschaltung von einem Widerstand und einem Kondensator
* Die genaue Definition wie der Plugin-String eingegeben werden muss ist in der Hilfe des jeweiligen Plugins ersichtlich
* aktuell sind in LeTTo folgende Plugins realisiert:
** [[Gsr]]: zeichnet elektrische Schaltungen und liefert auch die Maxima-Berechnung dazu - siehe [https://youtu.be/TIG0KI59k6I Video]
** [[Wsr]]: zeichnet lineare elektrische Schaltungen und liefert auch die Maxima-Berechnung dazu  - siehe [https://youtu.be/YL-T-61QUh4 Video]
** [[Dsr]]: zeichnet lineare Drehstromschaltungen und liefert auch die Maxima-Berechnung dazu  - siehe [https://youtu.be/Z62GKTSbKDA Video]
** [[Elektronik]]: zeichnet elektroniksche Schaltungen mit OPV und Transistor
** [[Zp]]: zeichnet eine elektrische Schaltung als Zweipol auf den Bildschirm. Dieses Plugin ist nur aus Kompatibilitätsgründen  vorhanden. Es sollte statt dessen nur mehr "Wsr" verwendet werden.
** [[CodeCheck|SourceCode]]: automatische Bewertung von Sourcecode(aktuell nur Java)
** [[Graph]]: zeichnet ein Zeitsignal in ein virtuelles Oszilloskop  - siehe [https://youtu.be/O7dSg1LACq8 Video]
** [[DigiGraph]]: zeichnet digitale Signale in ein virtuelles Oszilloskop 
** [[Plot]]: zeichnet Funktionsgraphen  - siehe [https://youtu.be/s0ju5sV31yU Video]
** [[Freihand]]: Stellt für den Schüler ein Zeichenfenster zur Verfügung, in dem der Schüler Freihand zeichnen kann
** [[MultiMeter]]: einfache Multimeter für die Anzeige von elektrischen Größen und interaktive Schülereingaben  - siehe [https://youtu.be/FYuSCteWRQc Video]
* Sobald ein Plugin definiert ist, kann über die rechte Maustaste im Fragetext-Editor auf die verfügbaren Plugin-Textmodule zugegriffen werden.
:[[Datei:ClipCapIt-210124-094149.PNG|350px]]
Folgende Module stehen zur Verfügung:
* Angabe: Hier wird aus dem Plugin ein Angabetext automatisch generiert und in den Text eingefügt. Dieser Text ändert sich nicht, falls am Plugin-String etwas geändert wird, muss also nach einer Plugin-String-Änderung neu eingefügt werden.
* Graphik: Hiermit  wird ein Graphig Tag in eckigen Klammern [PIG ... ] im Fragetext eingefügt. Die Berechnung der Graphik erfolgt dann zur Laufzeit und wird deshalb individuell für jeden Schüler mit seinen Datensätzen berechnet. Der PIG-Tag kann je nach Plugin auch Parameter enthalten welcher zur Konfiguration der Graphik verwendet werden können. Diese Parameter sind vom Plugin abhängig und werden deshalb in der Plugin-Hilfe des Plugins beschrieben. Die Paramter des PIG-Tags können im Fragetext ganz normal verändert werden. 

Ein Anführungszeichen " muss im Definitionsstring mit einem Backslash verblockt werden.
&lt;pre&gt; [PIG Plugin2 "text(2,2,tex=\"\alpha\")"/] &lt;/pre&gt;
* Im [[Beispielsammlung Editieren#Maxima-Feld|Maxima-Feld]] kann mit der rechten Maustaste auf das Berechnungsmodul eines Plugins zugegriffen werden, falls das Plugin eine Maxima-Berechung ausgeben kann.

=== Plugin-Entwicklung ===

* Um eigene Plugins entwickeln zu können steht ein Demoplugin einer einfachen Uhr auf Github zur Verfügung https://github.com/LeTTo-GmbH/letto-pluginuhr.git
* Die Kommunikation erfolgt über eine Rest-Schnittstelle (Swagger-Doku des Uhr Plugins https://build.letto.at/pluginuhr/swagger-ui/index.html)
* Das Plugin muss am eigenen LeTTo-Server der Schule wo es genutzt werden soll über das Setup-Service [https://name/config https://servername/config] regisitriert werden und eingebunden sein.
** Die Doku für die Endpoints des Setup-Services liegt ebenfalls als Swagger-Doku vor (https://build.letto.at/config/swagger-ui/index.html) 
** Für die Registratur eines Plugins benötigt man den Endpoint '''/config/auth/user/registerplugin''' aus dem config-controller
* Die Dokumentation befindet sich ebenfalls im Uhr-Plugin im Sourcecode.
** JavaDoc vom Uhr-Plugin : https://build.letto.at/pluginuhr/open/javadoc/index.html
*** DTO-Klassen für die REST-Schnittstelle: https://build.letto.at/pluginuhr/open/javadoc/at/letto/plugins/dto/package-summary.html
*** Controller-Klassen der REST-Schnittstelle: https://build.letto.at/pluginuhr/open/javadoc/at/open/letto/plugin/controller/package-summary.html
** Die notwendigen Controller für die REST-Kommunikation findet man im Verzeichnis '''src/main/java/at/open/letto/plugin/controller''' - https://build.letto.at/pluginuhr/open/javadoc/at/open/letto/plugin/controller/package-summary.html
*** [https://build.letto.at/pluginuhr/open/javadoc/at/open/letto/plugin/controller/InfoController.html info-controller] :  allgemeine Information welche jedes Plugin liefern muss (von extern erreichbar)
*** [https://build.letto.at/pluginuhr/open/javadoc/at/open/letto/plugin/controller/ApiExternOpenController.html api-extern-open-controller]: offene Endpoints welche von extern erreichbar sein müssen für ajax und allgemeine Informationen (von extern erreichbar)
*** [https://build.letto.at/pluginuhr/open/javadoc/at/open/letto/plugin/controller/ApiController.html api-controller] : die eigentliche Plugin-Schnittstelle zwischen LeTTo und Plugin (nur aus dem Docker-Netzwerk erreichbar)
*** [https://build.letto.at/pluginuhr/open/javadoc/at/open/letto/plugin/controller/ApiExternController.html api-extern-controller] : für eine gesicherte Verbindung von einem externen LeTTo-Server wenn Plugin und LeTTo nicht auf dem gleichen Server liegen (noch nicht fertig implementiert) jedoch gleiche Funktion wie api-controller  (von extern erreichbar)
*** [https://build.letto.at/pluginuhr/open/javadoc/at/open/letto/plugin/controller/IFrameConfigurationController.html iframe-configuration-controller] : Wenn die Konfiguration des Plugins nicht über JavaScript sondern über ein IFrame in LeTTo eingebunden wird ist hier der Konfigurationsdialog des Plugins (von extern erreichbar)
** jedes Service und Plugin sollte auch die Endpoints des BaseInfoControllers und PingControllers implementieren ('''src/main/java/at/letto/basespringboot/controller)''' 
*** [https://build.letto.at/pluginuhr/open/javadoc/at/letto/basespringboot/controller/BaseInfoController.html base-info-controller] : allgemeine Information welche jedes Service liefern muss (nur aus dem Docker-Netzwerk erreichbar)
*** [https://build.letto.at/pluginuhr/open/javadoc/at/letto/basespringboot/controller/PingController.html ping-controller] : interner und externer Ping für health-check etc.
** Den Rest-Client für die Registratur am Setup-Service findet man in der Klasse RestSetupService.class (Methode registerPlugin()) im Verzeichnis '''src/main/java/at/letto/setup/restclient'''
*** Im Uhr Plugin erledigt die Registrator das ConnectionService mit der Methode registerPluigin()
*** JavaDOC: https://build.letto.at/pluginuhr/open/javadoc/at/letto/setup/restclient/RestSetupService.html
** Die Datentransfer-JSON-Klassen für die REST-Schnittstelle als dokumentierte Java-Klassen findet man im Verzeichnis '''src/main/java/at/letto/plugins/'''
* Um selbst entwickelte Plugins testen zu können kann der Plugintester(https://servername/plugintester)  verwendet werden, welcher über das Setup-Service (https://servername/config) installiert werden kann.

[[Category:Plugins]]

