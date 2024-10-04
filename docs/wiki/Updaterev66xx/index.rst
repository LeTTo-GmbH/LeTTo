Datum 4.9.2024

zurück zu [[Administration]]

= Update einer Version 65xx auf die Stable-Version 66xx vom September 2024 =

Das Update besteht aus 3 Phasen.
* 1. Update des hostbasierten Setup-Services (https://servername/setup) - ist nur notwendig wenn es auch verwendet wird und läuft
* 2. Update des dockerbasierten Setup-Services (https://servername/config) 
* 3. Update aller anderen Services '''nachdem''' das Setup-Service aktualisiert wurde!!

== Update des hostbasierten Setup-Services ==
* vor einem Java-Update sollten alle anstehenden Betriebsystem-Aktualisierungen durchgeführt werden. &lt;br&gt;
&lt;pre&gt;    apt-get update -y
    apt-get upgrade -y
    apt-get dist-upgrade -y
    apt-get autoremove -y
    reboot&lt;/pre&gt;
* Falls am System noch Java 17 oder älter läuft muss zuerst das [[Install JDK-21|JDK-21]] installiert werden. (siehe auch [[Install JDK-21]]) &lt;br&gt;:[[Datei:Java-version setup.png|1000px]]
** in Ubuntu 22.04 oder 24.04
*** entweder in der shell: &lt;pre&gt;apt-get -y install openjdk-21-jre openjdk-21-jdk openjdk-21-jre-headless openjdk-21-source&lt;/pre&gt;
*** oder über das Setup-Service (https://servername/setup) über den Button Kommandoeingabe:  &lt;br&gt;:[[Datei:Java install 21.png|1000px]]
** in Debian siehe [[Install JDK-21]]
** danach muss das Setup-Service neu gestartet werden &lt;br&gt;:[[Datei:Setup restart.png|1000px]]
** Nach dem Neustart des Setup-Services sollte die Java Version 21 eingetragen sein &lt;br&gt;:[[Datei:Java Version 21.png|1000px]]&lt;br&gt;
* Update des hostbasierten Setup-Services
** Entweder über die Kommandozeile &lt;pre&gt;bash /opt/letto/setup/updatelettosetup.sh&lt;/pre&gt;
** oder über Update-Config &lt;br&gt;:[[Datei:Update-Config.png|500px]]
*** über den Button Update-to-Stable bei Host &lt;br&gt;:[[Datei:Setup-Update-Stable.png|300px]]

== Update des dockerbasierten Setup-Services ==
Das Update kann entweder webbasiert oder in der Ubuntu-bash erfolgen.
* webbasiertes Update: &lt;br&gt; Das Update kann entweder über das dockerbasierte https://servername/config oder über das hostbasierte https://servername/setup Setup-Service erfolgen.&lt;br&gt;Hierzu bitte über Update-Config zuerst den Update-Plan auf "stable" setzen und danach das Update starten.&lt;br&gt;[[Datei:Setup docker update stable.png|1000px]]
* in der Ubuntu-bash:
** ins Verzeichnis /opt/letto/docker/compose/setup wechseln&lt;pre&gt;cd /opt/letto/docker/compose/setup&lt;/pre&gt;
** in der Datei docker-compose.yml den tag beim image auf stable setzen&lt;pre&gt;image: lettohub/letto-setup:stable&lt;/pre&gt;
** container pullen und neu starten 
&lt;pre&gt;     docker compose down
     docker compose pull
     docker compose up -d&lt;/pre&gt;

== Update aller anderen Services ==
Auch das Update aller anderen Services kann entweder webbasiert(empfohlen) oder in der Ubuntu-bash erfolgen.
* webbasiertes Update im Setup-Service über Update-Config und dann &lt;br&gt;:[[Datei:Update stable all.png|600px]]
* in der Ubuntu-bash müssten relativ viele Operationen durchgeführt werden um das Update komplett zu erledigen weshalb ich mal diese Art hier nicht näher beschreibe sondern nur die Schritte angebe
** Aktualisierung aller .yml Dateien in /opt/letto/docker/compose und den Unterverzeichnissen (dabei den Tag aller LeTTo-Container auf stable setzen)
** alle container mit docker compose stoppen, pullen und neu starten
** Installation der neuen Services edit,main,question,plugins,pluginsourcecode falls sie noch nicht installiert sind über die .yml,.conf Dateien und Start der Services

