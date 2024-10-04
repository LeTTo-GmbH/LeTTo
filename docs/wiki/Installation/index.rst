= Allgemeines =
Der LeTTo-Server wurde in Java für JavaEE [https://www.oracle.com/technetwork/java/javaee/overview/index.html] Server entwickelt. Prinzipiell sollte LeTTo auf jedem JavaEE-Server unter Windows oder Linux lauffähig sein. Wir haben jedoch als Serverumgebung nur Ubuntu-Server mit TomEE getestet und empfehlen deshalb auch diese Laufzeitumgebung.

Als Datenbank wird eine MySQL-Datenbank verwendet, welche idealerweise am gleichen Server wie der TomEE läuft. Es ist jedoch auch mögliche einen zentralen MySQL-Server zu verwenden welcher im LAN zur Verfügung steht.

=== siehe auch ===
* [[Administration]]
* [[Anforderungen]]
* [[Migration LeTTo zu Docker]]
* [[Dockerinstallation Erstkonfiguration]]
* [[Verzeichnisse und Docker-Volumes]]
* [[Container Struktur]]
* [[Setup-Service]]
* [[Datensicherung-Docker]]

= Installation des Servers =

== Installation auf einem Ubuntu/Debian-Server mit Docker-Containern (empfohlen) ==
* Installation von Ubuntu 22.04 Server oder Debian 11 ohne apache webserver (Port 80,443 und 9096 müssen frei sein!)
** !! '''Docker aus den Ubuntu oder Debian-Quellen darf nicht installiert sein''', bzw. muss vor dem Installationsscript deinstalliert werden. Das Install-Script installiert Docker aus den original Docker-Quellen !! 
* Einrichten der Namensauflösung dass der Server aus dem Internet über seinen Namen erreichbar ist
* Download des Installationsscripts von [http://letto.at/download/letto/install-letto-ubuntu-docker.sh http://letto.at/download/letto/install-letto-ubuntu-docker.sh]
  &lt;pre&gt;wget http://letto.at/download/letto/install-letto-ubuntu-docker.sh&lt;/pre&gt;
* start des Installationsscripts als '''root'''
  &lt;pre&gt;bash ./install-letto-ubuntu-docker.sh&lt;/pre&gt;
* Nach der Installation ist das Setup-Service über einen Browser auf dem https-Port 9096 erreichbar. 
* Alle weiteren Konfigurationen erfolgen dann im [[Setup-Service]]
** Beim [[Dockerinstallation Erstkonfiguration|ersten Start]] muss eine allgemeine Information des Servers für den Lizenzserver und die Passwörter für den MySQL-Server angegeben werden.
** Dann kann die Schule angelegt werden. Es wird dabei vom Lizenzserver eine beschränkte Demolizenz angefordert. Das Schulkürzel welches bei der Einrichtung agegeben wird erscheint immer als Kennung der Schule am Server (auch in der URL) und kann später nicht mehr geändert werden!
** Nach der Installation der Schule bitte mit uns in Verbindung setzen, dass wir eine angepasste Demolizenz vergeben können.

== Installation auf anderen Host-Systemen mit Docker-Containern ==
* Prinzipiell ist natürlich jeder Server für die Docker-Installation von LeTTo verwendbar. Es existiert lediglich nur für Ubuntu ein fertiges Installationsscript für die Installation. Für andere Host-Betriebssysteme bitte ebenfalls das Installationsscript für Ubuntu herunterladen jedoch nicht direkt ausführen sondern an das Betriebssystem anpassen bzw. schrittweise angepasst die Installation händisch durchführen. Den Großteil der Installation übernimmt das Setup-Programm lettosetup.jar welches nach der Installation direkt am Host am https-Port 9096 läuft.
* Unter Windows gibts es nur ein sehr experimentelles Basis-Script nachdem noch einige undokumentierte Anpassungen notwendig sind [https://letto.at/download/letto/install-letto-windows-docker.bat https://letto.at/download/letto/install-letto-windows-docker.bat]

== Installation unter Ubuntu (unterstützt bis September 2023) ==
* getestet für die LTS-Version 18.04, 20.04 und 22.04
* VIDEO-Anleitung: [https://www.dropbox.com/s/pyljp9g8pwt4zfp/Letto-Installation.mp4?dl=0 Installation] [https://www.dropbox.com/s/fimmw23l4s6zc6z/Letto-Installation-fertigstellung.mp4?dl=0 Fertigstellung]
* Download von Ubuntu Server [http://cdimage.ubuntu.com/releases/22.04/release/]und Erzeugung eines Boot Mediums [https://wiki.ubuntuusers.de/Ubuntu-CD/] (zB. DVD)
* Installation mit einem Benutzer '''letto'''
* Bei der Installation nur den '''OpenSSH Server''' mit installieren
* Der Server sollte über eine '''funktionierende Namensauflösung''' aus dem '''Internet''' erreichbar sein.
* Eine gegebenenfalls vor dem Server sitzende Firewall sollte ins Internet mindestens folgende Ports freischalten:
** Eingehend TCP: 80(HTTP), 443(HTTPS)
** Eingehend ICMP: echo(ping)
** Ausgehend TCP: 80(HTTP), 443(HTTPS)
** Ausgehend UDP: 53(DNS)			
** Ausgehend ICMP: echo(ping)
** Und natürlich alle Antworten auf ausgehende Anfragen
** Falls eine Authentifizierung über LDAP gewünscht wird muss natürlich der LDAP oder AD-Server mit den notwendigen Ports erreichbar sein.

* falls der Server nicht auf aktuellem Stand ist, die Updates einspielen und den Server neu starten
&lt;pre&gt;
  sudo apt-get -y update 
  sudo apt-get -y upgrade
  sudo apt-get -y dist-upgrade
  sudo apt-get -y autoremove
  sudo apt-get -y install -f
  sudo reboot
&lt;/pre&gt;
* Konfiguration des Servers
** Starten des Servers
** Wechseln zu Benutzer root.&lt;pre&gt;sudo su&lt;/pre&gt;
** Wechsel in das Verzeichnis opt&lt;pre&gt;cd /opt&lt;/pre&gt;
** '''Download''' des Installationsscripts&lt;pre&gt;wget https://letto.at/download/letto/install-letto-ubuntu.sh&lt;/pre&gt;
** Script in einem Editor '''konfigurieren''' &lt;pre&gt;nano install-letto-ubuntu.sh&lt;/pre&gt;
*** Wenn gewünscht, setzen von DNS-Namen, Passwörtern, Email und Heap-Speicher. Notwendíge Einstellungen werden interaktiv abgefragt wenn sie nicht angegeben werden.
*** Mit &lt;Strg&gt;-O und Enter das Script speichern
*** Mit &lt;Strg&gt;-X den Editor verlassen 
** Setzen von Ausführungsrechten &lt;pre&gt;chmod 755 install-letto-ubuntu.sh&lt;/pre&gt;
** Script '''starten''' &lt;pre&gt;./install-letto-ubuntu.sh&lt;/pre&gt; Die Ausführung des Scripts wird je nach Server-Hardware zwischen 20 und 60 Minuten dauern, da die notwendige Installation von LaTeX und Inkscape relativ lange dauert. Falls das Script während der Ausführung abbricht sollte es (ggf. nach Behebung des Fehlers) einfach nochmals gestartet werden.

* Zertifikat für den Server installieren:&lt;br&gt;Bei der Standardeinstellung wurde noch das selbstsignierte Zertifikat vom Apache2 in der Datei /etc/apache2/sites-enabled/letto.conf eingebunden. Dieses Zertifikat kann nun durch ein eigenes gültiges Zertifikat für den Server-DNS-Namen ersetzt werden. &lt;br&gt; Falls kein eigenes Zertifikat vorhanden ist, kann auch mit dem Certbot ein selbstzertifiziertes Zertifikat installiert werden. Hierzu kann wie folgt vorgegangen werden:
** Starten des certbot als root-Benuter &lt;pre&gt;certbot --apache -d meinedomain.at&lt;/pre&gt;
*** Hierbei müssen einige Fragen wie email etc. beantwortet werden.
** Eintragen des certbot in einen Cronjob wie zB. in der Datei /etc/crontab &lt;pre&gt;05 05 * * * root certbot renew&lt;/pre&gt;

* Datensicherung einrichten: &lt;br&gt;Die Datensicherung wird durch das Script so eingerichtet, das täglich in das Verzeichnis /sicherung gesichert wird. Diese Verzeichnis sollte nun auf eine externe Hardware regelmäßig mit einem sinnvollen Archivierungskonzept gesichert werden.

* Konfiguration von LeTTo : &lt;br&gt; Nun kann der Server über seine URL erreicht und konfiguriert werden. &lt;br&gt;
* globalen Administrator anlegen: &lt;br&gt; :[[Datei:ClipCapIt-211209-151804.PNG|600px]]
** Der Ping zum Lizenzserver muss OK sein damit der Server am Lizenzserver eingetragen werden kann
** Die Webadresse muss die Adresse sein, mit welcher der Server vom Browser auch erreicht wird, da daran die Lizenz gebunden wird!
** Der globale Administrator ist für die Administration des Servers zuständig. Für die Verwaltung der Klassen,Lehrer und Schüler gibt es einen getrennten Schuladministrator, welcher bei der Anlage der Schule erstellt wird.
** Daten speichern und weiter ist nur möglich wenn der Lizenzserver erreichbar ist.

* als globaler Administator eine Schule anlegen: &lt;br&gt; :[[Datei:ClipCapIt-211209-135032.PNG|600px]] &lt;br&gt; &lt;br&gt; :[[Datei:ClipCapIt-211209-135555.PNG|600px]] &lt;br&gt; Durch "Schule anlegen und Probelizenz anfordern" wird die Schule erzeugt und vom Lizenzserver eine Demolizenz geladen.
* als Schuladministrator eine Abteilung anlegen: &lt;br&gt; :[[Datei:ClipCapIt-211209-140145.PNG|600px]]

== Installation unter Ubuntu 18.04 ==
* Wir empfehlen ausdrücklich die Installation unter Ubuntu 20.04. Das Installationsscript für 18.04 wird ab 2021 nicht mehr gewartet.
* Download von Ubuntu Server [http://cdimage.ubuntu.com/releases/18.04/release/] und Erzeugung eines Boot Mediums [https://wiki.ubuntuusers.de/Ubuntu-CD/] (zB. DVD)
* Die weitere Vorgehensweise ist gleich wie bei Ubuntu 20.04 nur sollte das Script '''install-letto-ubuntu.sh''' statt install-letto-ubuntu-20.04.sh verwendet werden &lt;pre&gt;wget https://letto.at/download/letto/install-letto-ubuntu.sh&lt;/pre&gt;

= Migration einer bestehenden LeTTo-Installation auf eine Docker-Installation =
== Migration einer Linux-basierten LeTTo-Installation direkt auf den bestehenden Server ==
Besteht bereits eine lokale Installation auf einem Linux Server (idealerweise Ubuntu 18.04,20.04,22.04 oder Debian 11) dann kann direkt auf diesem Server eine dockerbasierte Installation vorgenommen und dabei die bestehenden Daten übernommen werden.

[[Migration_LeTTo_zu_Docker#Migration_einer_Linux-basierten_LeTTo-Installation_direkt_auf_den_bestehenden_Server|Migration Linux Installation auf Docker am gleichen Server]]

== Migration einer bestehenden LeTTo-Installation auf einen neuen Linux-Server als Docker-Installation ==
Liegt eine LeTTo-Installation auf einem beliebigen System vor, so kann sie wie hier beschrieben in eine Docker-Installation auf einem Linux-Server übertragen werden.

[[Migration_LeTTo_zu_Docker#Migration_einer_bestehenden_LeTTo-Installation_auf_einen_neuen_Linux-Server_als_Docker-Installation|Migration LeTTo Installation auf Docker]]

== Migration einer bestehenden LeTTo-Installation auf einen neuen Windows-Server als Docker-Installation ==
[[Migration_LeTTo_zu_Docker#Migration_einer_bestehenden_LeTTo-Installation_auf_einen_neuen_Windows-Server_als_Docker-Installation|Migration zu Docker auf Windows]]

== Migration einer bestehenden LeTTo-Installation auf einen neuen MAC-Server als Docker-Installation ==
[[Migration_LeTTo_zu_Docker#Migration_einer_bestehenden_LeTTo-Installation_auf_einen_neuen_MAC-Server_als_Docker-Installation|Migration zu Docker auf einem Mac]]

= globale Konfiguration =
Folgende Einstellungen sollte der [[Globaler Administrator|globale Administrator]] vornehmen:
* Anpassen der notwendigen Systemeinstellungen in der '''[[Globale Konfiguration|globalen Konfiguration]]'''.
** [[Globale Konfiguration#Parameter für den Active-Directory-Login|Parameter]] für die Active-Directory oder LDAP Authentifikation
** [[Globale Konfiguration#Parameter für den Serverbetrieb|Parameter]] für den Server-Betrieb 
** Wenn nur eine Schule vorhanden ist, die Konfiguration der [[Globale Konfiguration#Parameter der Schule|Schul-Parameter]]
** Konfiguration des [[Globale Konfiguration#Allgemeine Konfiguration des Serververhaltens|Serververhaltens]]
* Konfiguration des [[Schultypen|Schultyps]]
* Anlegen einer neuen [[Schul-Konfiguration|Schule]]
* Konfiguration der [[Globale Konfiguration#Parameter der Schule|Schul-Parameter]]

= Lizenz-Key einspielen =
* Im Regelfall wird die Lizenz automatisch bei der Konfiguration als globaler Administrator als Demolizenz angelegt. 
* Bitte danach mit dem LeTTo-Team in Verbindung setzen damit wir die Demolizenz verlängern oder ein Angebot für eine Lizenz legen können.

= Einspielen der Daten = 
* Das [[Datenimport|Einspielen der Daten]] wird bei einer LeTTo-Admin-Schulung erklärt

= Konfiguration der globalen Einstellungen =
:[[Datei:ClipCapIt-190121-191552.PNG|200px]]
* Im Dialog "[[Globale Konfiguration]]" müssen noch die Parameter für Server, AD-Login und Schule eingestellt werden.
* Als globaler Administrator kann man mit dem Menüpunkt "[[AD-check]]" die Authentifikation an einem LDAP-Server oder an einem Active-Directory konfigurieren.

= Letzte wichtige Server-Konfigurationen =
Folgende Konfigurationen sollten noch vorgenommmen werden, werden aber in diesem Wiki nicht explizit beschrieben, sondern sollten von einem Linux/Unix-Fachmann vorgenommen werden.
* [[Datensicherung-Docker#Datensicherung|Datensicherung]] einrichten 
* Firewall einrichten

[[Kategorie:Administration]]

