# Umstieg von Glassfish 4.1 auf TomEE 8
Zurst den TomEE-Server installieren: [Installation TomEE-8](../InstallationTomEE-8/index.md)

Der aktuelle Produktionsserver und TomEE8 können in der Umstellungsphase parallel betrieben werden. Dazu muss LeTTo am TomEE unter einem anderen Anwendungsnamen deployed werden und diese Anwendung dann über AJP verlinkt werden.

<pre>
cd /opt/tomee8/webapps
cp letto.war tomee.war
</pre>

Damit ist die Anwendung unter dem Anwendungsnamen **tomee** verfügbar und muss am Apache integriert werden:
<pre>
cd /etc/apache2/sites-enabled/
sudo nano letto.conf
</pre>
Dort einen Proxy für die Anwendung tomee einfügen
<pre>
#Proxy für den Tomee8-Server
&lt;Location /tomee&gt;
    ProxyPass ajp://localhost:8089/tomee
&lt;/Location&gt;
</pre>

Damit ist die Anwendung unter ...Webadresse.../tomee erreichbar.

Um den Server endgültig in Betrieb zu nehmen, wird einfach die Umleitung auf den Glassfish-Server durch die AJP-Adresse des Tomee-Servers ersetzt.

<pre>
&lt;Location /letto&gt;
     ProxyPass ajp://localhost:8089/letto
&lt;/Location&gt;
</pre>

###  siehe auch 
* [Installation](../Installation/index.md)

