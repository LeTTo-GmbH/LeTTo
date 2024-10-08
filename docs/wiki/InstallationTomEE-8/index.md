# Installation TomEE-8
##  Verzeichnisse einrichten
**Empfohlene Verzeichnisstruktur**
* /opt/letto 
In diesem Ordner liegen alle Daten, die von LeTTo gespeichert und verwendet werden.

* /opt/letto/war 
In diesen Ordner wird die aktuelle Version der letto.war heruntergeladen (händisch oder vom Update-Script)

* /opt/letto/images ... Speicherort für alle Bilder und Dateien, die innerhalb von Letto hochgeladen werden.
* /opt/letto/js ... Speicherort für Javascript-Dateien. Alle extern verwendeten Javaspript-Dateien können in der [Letto-Konfiguration](/notimplemented/index.md) hierher kopiert werden, damit bei der Durchführung von Tests keine externen Daten benötigt werden. Damit kann die Firewall für User-Browser alle externen Zugriffe sperren.

Diese 2 Verzeichnisse (images, js) müssen auch in das [verlinkt](Apache|Apache-Base-Verzeichnis) werden.

Der Ordner **/opt/letto/images** muss in das **Backup** eingebunden werden!

Die weiteren Ordner werden von LeTTo automatisch erzeugt:
* /opt/letto/pdf ... Ordner zum Zwischenspeichern von erzeugten User-PDF-Dokumenten.
* /opt/letto/tex ... Ordner zum Zwischenspeichern von erzeugten Tex-Dokumenten (Verwendung auch bei der Generierung von PDFs).
* /opt/letto/projekt ... In diesem Ordner werden Schülerprojekte gezippt für alle Abgaben abgelegt.
* /opt/letto/images/photos ... Speicherort für Schülerfotos: Bildname: SokratesID.jpg

### Erzeugung der Ordner und Verlinkung zum Apache-Server
<pre>
sudo mkdir /opt/letto/images
sudo mkdir /opt/letto/js
</pre>

Symbolische Links für Apache
<pre>
cd /var/www/html
ln -s /opt/letto/images images
ln -s /opt/letto/js js
</pre>

##  Installation TomEE 8 Server

###  TomEE download und Installation
* Aktionen durchführen als user "letto"
  * Der user "letto" sollte Schreibrechte im Verzeichnis /opt haben, am einfachsten man trägt den Benutzer als Owner ein.
<pre>
sudo chown letto /opt
sudo chmod 755 /opt
</pre>
* Download des Servers [https://mirror.klaus-uwe.me/apache/tomee/tomee-8.0.3/](https://mirror.klaus-uwe.me/apache/tomee/tomee-8.0.3/), entpacken der Datei, verschieben nach /opt und einen Link auf /opt/tomee legen
<pre>
wget https://mirror.klaus-uwe.me/apache/tomee/tomee-8.0.3/apache-tomee-8.0.3-plume.tar.gz
tar -xzf apache-tomee-8.0.3-plume.tar.gz
sudo mv apache-tomee-plume-8.0.3 /opt/tomee8

cd /opt/letto
ln -s /opt/tomee8 /opt/tomee
</pre>
* Kontrolle ob der Benutzer "letto" alle Recht im Verzeichnis /opt/tomee hat
* MySQL Database-Connector [https://dev.mysql.com/downloads/connector/j/](https://dev.mysql.com/downloads/connector/j/) herunterladen und ins TomEE-Verzeichnis kopieren:
<pre>wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.47.zip
unzip mysql-connector-java-5.1.47.zip
cp mysql-connector-java-5.1.47/mysql-connector-java-5.1.47.jar /opt/tomee/lib/
</pre>

* Datenbank eintragen in der Datei **/opt/tomee/conf/tomee.xml**
<pre>
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
</pre>

* Für die Funktion von Primefaces einfügen am Ende der Datei **/opt/tomee/conf/catalina.properties**
<pre>
org.apache.el.parser.SKIP_IDENTIFIER_CHECK=true
</pre>

* In **/opt/tomee/conf/context.xml** =&gt; Kommentar löschen, sodass diese Zeile aktiv
<pre>
&lt;!-- Uncomment this to disable session persistence across Tomcat restarts --&gt;
  &lt;Manager pathname="" /&gt;
</pre>
  
* Port Festlegen in der Datei **/opt/tomee/conf/server.xml**: <br> zB.: http(8088), https(8483), AJP(8089)
<pre>
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
</pre>

* Damit mit den korrekten Dateirechten gespeichert wird suche in der Datei **/opt/tomee/bin/catalina.sh** nach
<pre>
# Set UMASK unless it has been overridden                                                                                                                                   if [ -z "$UMASK" ]( -z "$UMASK" ); then                                                                                                                                                        UMASK="0027"                                                                                                                                                            fi                                                                                                                                                                          umask $UMASK 
</pre>
und ersetze 0027 durch 002 :
<pre>
# Set UMASK unless it has been overridden                                                                                                                                   if [ -z "$UMASK" ]( -z "$UMASK" ); then                                                                                                                                                        UMASK="0002"                                                                                                                                                            fi                                                                                                                                                                          umask $UMASK 
</pre>

###  Einrichten des Security-Managers für das SourceCode-Plugin 
* Von der Konsole aus die Datei **/opt/tomee/conf/catalina.policy** bearbeiten
* Am Ende anfügen: 
<pre>
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
</pre>

###  Setzen des Heap-Speichers für den TomEE Server 
Der Heap-Speicher sollte für den Server auf 2/3 bis 3/4 vom physikalischen Speicher gesetzt werden. 

Dazu ist eine Datei **/opt/tomee/bin/setenv.sh** zu erstellen, in der der Speicher in Megabyte anzugeben ist. 

Hier ein Beispiel für einen Rechner mit 16GB physikalischem RAM und demnach 12GB Heap-Speicher:
<pre>
#!/bin/sh -e
export CATALINA_OPTS=&quot;-Xms12000M -Xmx12000M&quot;
</pre>

Diese Datei ist dann noch mit Ausführungsrechten zu versehen.
<pre>
chmod 755 /opt/tomee/bin/setenv.sh
</pre>

###  TomEE starten
<pre>
/opt/tomee/bin/startup.sh
</pre>

###  TomEE stoppen 
<pre>
/opt/tomee/bin/shutdown.sh
</pre>

###  letto.war deployen 
<pre>
cd /opt/letto/war
wget -q -c --user letto --password xxxPASSWORTyyy https://letto.at/download/letto/letto-daily.war
cp letto-daily.war /opt/tomee/webapps/letto.war
</pre>
Das Passwort wird von uns auf Anfrage zur Verfügung gestellt.

###  Update der Anwendung 
[siehe Update TomEE](../Update/index.md#update-tomee-8-)


###  siehe auch 
* [Installation](../Installation/index.md)

