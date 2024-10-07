# Installation TomEE Server
##  Installation TomEE 7 Server
* Aktionen durchführen als user "letto"
* Download des Servers [https://javaee.github.io/glassfish/download](https://javaee.github.io/glassfish/download), entpacken der Datei und verschieben nach /opt
<pre>
wget http://mirror.klaus-uwe.me/apache/tomee/tomee-7.1.0/apache-tomee-7.1.0-plume.tar.gz
tar -xzf apache-tomee-7.1.0-plume.tar.gz
sudo mv apache-tomee-plume-7.1.0 /opt/tomee7
</pre>
* Kontrolle ob der Benutzer "letto" alle Recht im Verzeichnis /opt/tomee7 hat
* MySQL Database-Connector [https://dev.mysql.com/downloads/connector/j/](https://dev.mysql.com/downloads/connector/j/) herunterladen und ins TomEE-Verzeichnis kopieren:
<pre>wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.47.zip
unzip mysql-connector-java-5.1.47.zip
cp mysql-connector-java-5.1.47/mysql-connector-java-5.1.47.jar /opt/tomee7/lib/
</pre>

* Datenbank eintragen in der Datei **/opt/tomee7/conf/tomee.xml**
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
        Password    xxxgewähltesPasswortxxx                
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

* Für die Funktion von Primefaces einfügen am Ende der Datei **/opt/tomee7/conf/catalina.properties**
<pre>
org.apache.el.parser.SKIP_IDENTIFIER_CHECK=true
</pre>

* In /opt/tomee7/conf/context.xml =&gt; Kommentar löschen, sodass diese Zeile aktiv
<pre>
&lt;!-- Uncomment this to disable session persistence across Tomcat restarts --&gt;
  &lt;Manager pathname="" /&gt;
</pre>
  
* Port Festlegen in der Datei **/opt/tomee7/conf/server.xml**: <br> zB.: http(8088), https(8483), AJP(8089)
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

###  Einrichten des Security-Managers für das SourceCode-Plugin 
* Von der Konsole aus die Datei /opt/tomee7/conf/catalina.policy bearbeiten
* Am Ende anfügen: 
<pre>
grant {
    permission java.util.PropertyPermission "java.security.policy", "write";
    permission java.lang.RuntimePermission "createSecurityManager";
    permission java.lang.RuntimePermission "setSecurityManager";
    permission java.security.SecurityPermission "getPolicy";
    permission java.lang.RuntimePermission "accessDeclaredMembers";
    permission java.io.FilePermission "C:&#92;workspace-oxygen-letto&#92;.metadata&#92;.plugins&#92;org.eclipse.wst.server.core&#92;tmp0&#92;webapps", "read";
    permission java.lang.RuntimePermission "setIO";
    permission java.lang.reflect.ReflectPermission "suppressAccessChecks";
};
</pre>

###  TomEE starten
<pre>
/opt/tomee7/bin/startup.sh
</pre>

###  TomEE stoppen 
<pre>
/opt/tomee7/bin/shutdown.sh
</pre>

###  letto.war deployen 
<pre>
cp letto.war /opt/tomee7/webapps/
</pre>

###  siehe auch 
* [Installation](../Installation/index.md)

