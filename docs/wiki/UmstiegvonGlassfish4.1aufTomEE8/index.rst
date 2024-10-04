Zurst den TomEE-Server installieren: [[Installation TomEE-8]]

Der aktuelle Produktionsserver und TomEE8 können in der Umstellungsphase parallel betrieben werden. Dazu muss LeTTo am TomEE unter einem anderen Anwendungsnamen deployed werden und diese Anwendung dann über AJP verlinkt werden.

&lt;pre&gt;
cd /opt/tomee8/webapps
cp letto.war tomee.war
&lt;/pre&gt;

Damit ist die Anwendung unter dem Anwendungsnamen '''tomee''' verfügbar und muss am Apache integriert werden:
&lt;pre&gt;
cd /etc/apache2/sites-enabled/
sudo nano letto.conf
&lt;/pre&gt;
Dort einen Proxy für die Anwendung tomee einfügen
&lt;pre&gt;
#Proxy für den Tomee8-Server
&lt;Location /tomee&gt;
	ProxyPass ajp://localhost:8089/tomee
&lt;/Location&gt;
&lt;/pre&gt;

Damit ist die Anwendung unter ...Webadresse.../tomee erreichbar.

Um den Server endgültig in Betrieb zu nehmen, wird einfach die Umleitung auf den Glassfish-Server durch die AJP-Adresse des Tomee-Servers ersetzt.

&lt;pre&gt;
&lt;Location /letto&gt;
     ProxyPass ajp://localhost:8089/letto
&lt;/Location&gt;
&lt;/pre&gt;

== siehe auch ==
* [[Installation]]

