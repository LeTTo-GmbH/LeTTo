= Verzeichnisse einrichten=
'''Empfohlene Verzeichnisstruktur'''
* /opt/letto 
In diesem Ordner liegen alle Daten, die von LeTTo gespeichert und verwendet werden.

* /opt/letto/war 
In diesen Ordner wird die aktuelle Version der letto.war heruntergeladen (händisch oder vom Update-Script)

* /opt/letto/images ... Speicherort für alle Bilder und Dateien, die innerhalb von Letto hochgeladen werden.
* /opt/letto/js ... Speicherort für Javascript-Dateien. Alle extern verwendeten Javaspript-Dateien können in der [[Letto-Konfiguration|Letto-Konfiguration]] hierher kopiert werden, damit bei der Durchführung von Tests keine externen Daten benötigt werden. Damit kann die Firewall für User-Browser alle externen Zugriffe sperren.

Diese 2 Verzeichnisse (images, js) müssen auch in das [Apache|Apache-Base-Verzeichnis verlinkt] werden.

Der Ordner '''/opt/letto/images''' muss in das '''Backup''' eingebunden werden!

Die weiteren Ordner werden von LeTTo automatisch erzeugt:
* /opt/letto/pdf ... Ordner zum Zwischenspeichern von erzeugten User-PDF-Dokumenten.
* /opt/letto/tex ... Ordner zum Zwischenspeichern von erzeugten Tex-Dokumenten (Verwendung auch bei der Generierung von PDFs).
* /opt/letto/projekt ... In diesem Ordner werden Schülerprojekte gezippt für alle Abgaben abgelegt.
* /opt/letto/images/photos ... Speicherort für Schülerfotos: Bildname: SokratesID.jpg

==Erzeugung der Ordner und Verlinkung zum Apache-Server==
&lt;pre&gt;
sudo mkdir /opt/letto/images
sudo mkdir /opt/letto/js
&lt;/pre&gt;

Symbolische Links für Apache
&lt;pre&gt;
cd /var/www/html
ln -s /opt/letto/images images
ln -s /opt/letto/js js
&lt;/pre&gt;

= Installation TomEE 8 Server=

== TomEE download und Installation==
* Aktionen durchführen als user "letto"
** Der user "letto" sollte Schreibrechte im Verzeichnis /opt haben, am einfachsten man trägt den Benutzer als Owner ein.
&lt;pre&gt;
sudo chown letto /opt
sudo chmod 755 /opt
&lt;/pre&gt;
* Download des Servers [https://mirror.klaus-uwe.me/apache/tomee/tomee-8.0.3/], entpacken der Datei, verschieben nach /opt und einen Link auf /opt/tomee legen
&lt;pre&gt;
wget https://mirror.klaus-uwe.me/apache/tomee/tomee-8.0.3/apache-tomee-8.0.3-plume.tar.gz
tar -xzf apache-tomee-8.0.3-plume.tar.gz
sudo mv apache-tomee-plume-8.0.3 /opt/tomee8

cd /opt/letto
ln -s /opt/tomee8 /opt/tomee
&lt;/pre&gt;
* Kontrolle ob der Benutzer "letto" alle Recht im Verzeichnis /opt/tomee hat
* MySQL Database-Connector [https://dev.mysql.com/downloads/connector/j/] herunterladen und ins TomEE-Verzeichnis kopieren:
&lt;pre&gt;wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.47.zip
unzip mysql-connector-java-5.1.47.zip
cp mysql-connector-java-5.1.47/mysql-connector-java-5.1.47.jar /opt/tomee/lib/
&lt;/pre&gt;

* Datenbank eintragen in der Datei '''/opt/tomee/conf/tomee.xml'''
&lt;pre&gt;
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;tomee&gt;
  &lt;!-- see http://tomee.apache.org/containers-and-resources.html --&gt;
  &lt;!-- activate next line to be able to deploy applications in apps --&gt;
  &lt;!-- &lt;Deployments dir="apps" /&gt; --&gt;
  &lt;Resource id="jdbc/letto" type="DataSource"&gt;
		JdbcDriver  com.mysql.jdbc.Driver
		JdbcUrl     jdbc:mysql://localhost/letto?autoReconnect=true
		UserName    letto
		Password    xxx-gewähltesPasswort-xxx                
                jtaManaged = true
                testOnReturn = true
                testWhileIdle = true
                timeBetweenEvictionRunsMillis = 60
                initialSize = 2
                minIdle = 2
                validationQuery = "select 1"
  &lt;/Resource&gt;
&lt;/tomee&gt;
&lt;/pre&gt;

* Für die Funktion von Primefaces einfügen am Ende der Datei '''/opt/tomee/conf/catalina.properties'''
&lt;pre&gt;
org.apache.el.parser.SKIP_IDENTIFIER_CHECK=true
&lt;/pre&gt;

* In '''/opt/tomee/conf/context.xml''' =&gt; Kommentar löschen, sodass diese Zeile aktiv
&lt;pre&gt;
&lt;!-- Uncomment this to disable session persistence across Tomcat restarts --&gt;
  &lt;Manager pathname="" /&gt;
&lt;/pre&gt;
  
* Port Festlegen in der Datei '''/opt/tomee/conf/server.xml''': &lt;br&gt; zB.: http(8088), https(8483), AJP(8089)
&lt;pre&gt;
...
&lt;Server port="8005" shutdown="SHUTDOWN"&gt;
   ...
   &lt;Service name="Catalina"&gt;
      ...
      &lt;Connector port="8088" protocol="HTTP/1.1"
                 connectionTimeout="20000"
                 redirectPort="8483" xpoweredBy="false" server="Apache TomEE" /&gt;
      ...
      &lt;Connector port="8089" protocol="AJP/1.3" redirectPort="8483" /&gt;
      ...
    
   &lt;/Service&gt;
&lt;/Server&gt;
&lt;/pre&gt;

* Damit mit den korrekten Dateirechten gespeichert wird suche in der Datei '''/opt/tomee/bin/catalina.sh''' nach
&lt;pre&gt;
# Set UMASK unless it has been overridden                                                                                                                                   if [ -z "$UMASK" ]; then                                                                                                                                                        UMASK="0027"                                                                                                                                                            fi                                                                                                                                                                          umask $UMASK 
&lt;/pre&gt;
und ersetze 0027 durch 002 :
&lt;pre&gt;
# Set UMASK unless it has been overridden                                                                                                                                   if [ -z "$UMASK" ]; then                                                                                                                                                        UMASK="0002"                                                                                                                                                            fi                                                                                                                                                                          umask $UMASK 
&lt;/pre&gt;

== Einrichten des Security-Managers für das SourceCode-Plugin ==
* Von der Konsole aus die Datei '''/opt/tomee/conf/catalina.policy''' bearbeiten
* Am Ende anfügen: 
&lt;pre&gt;
grant {
    permission java.util.PropertyPermission "java.security.policy", "write";
    permission java.lang.RuntimePermission "createSecurityManager";
    permission java.lang.RuntimePermission "setSecurityManager";
    permission java.security.SecurityPermission "getPolicy";
    permission java.security.SecurityPermission "setPolicy";
    permission java.lang.RuntimePermission "accessDeclaredMembers";
    permission java.lang.RuntimePermission "setIO";
    permission java.lang.reflect.ReflectPermission "suppressAccessChecks";
};
&lt;/pre&gt;

== Setzen des Heap-Speichers für den TomEE Server ==
Der Heap-Speicher sollte für den Server auf 2/3 bis 3/4 vom physikalischen Speicher gesetzt werden. 

Dazu ist eine Datei '''/opt/tomee/bin/setenv.sh''' zu erstellen, in der der Speicher in Megabyte anzugeben ist. 

Hier ein Beispiel für einen Rechner mit 16GB physikalischem RAM und demnach 12GB Heap-Speicher:
&lt;pre&gt;
#!/bin/sh -e
export CATALINA_OPTS="-Xms12000M -Xmx12000M\"
&lt;/pre&gt;

Diese Datei ist dann noch mit Ausführungsrechten zu versehen.
&lt;pre&gt;
chmod 755 /opt/tomee/bin/setenv.sh
&lt;/pre&gt;

== TomEE starten==
&lt;pre&gt;
/opt/tomee/bin/startup.sh
&lt;/pre&gt;

== TomEE stoppen ==
&lt;pre&gt;
/opt/tomee/bin/shutdown.sh
&lt;/pre&gt;

== letto.war deployen ==
&lt;pre&gt;
cd /opt/letto/war
wget -q -c --user letto --password xxxPASSWORTyyy https://letto.at/download/letto/letto-daily.war
cp letto-daily.war /opt/tomee/webapps/letto.war
&lt;/pre&gt;
Das Passwort wird von uns auf Anfrage zur Verfügung gestellt.

== Update der Anwendung ==
[[Update#Update_TomEE_8|siehe Update TomEE ]]


== siehe auch ==
* [[Installation]]

