# Betreiben hinter einem Apache-Server
* Dies hat den Vorteil, dass der Apache-Server das Zertifikat für https Verwalten kann.
* Konfiguration des Apache Servers als AJP-Proxy:
<pre>
a2enmod ssl
a2enmod proxy
a2enmod proxy_ajp
a2enmod rewrite
systemctl restart apache2
</pre>

###  Betreiben des TomEE-Servers hinter einem Apache-Server 
* In der Konfigurationsdatei des Apache eintragen, wenn der AJP Port des TomEE-Servers auf 8089 liegt:
<pre>
&lt;IfModule mod_ssl.c&gt;
    &lt;VirtualHost _default_:443&gt;
        ServerAdmin x.y@z.at
        ...
        SSLProxyEngine  On
        ProxyRequests Off
        ProxyPreserveHost  On
        
        &lt;Location /letto&gt;
              ProxyPass ajp://localhost:8089/letto
        &lt;/Location&gt;
       ...
    &lt;/VirtualHost&gt;
&lt;/IfModule&gt;
</pre>

###  Betreiben des Glassfish-Servers hinter einem Apache-Server 
* Den Glassfish für den AJP-Proxy auf Port 8009 vorbereiten ( Dabei wird auch das admin-Passwort abgefragt! )
<pre>
/opt/glassfish4/glassfish/bin/asadmin --user admin --host localhost --port 4848 create-http-listener --listeneraddress 0.0.0.0 --listenerport 8009 --defaultvs server jk-connector-8009
/opt/glassfish4/glassfish/bin/asadmin --user admin --host localhost --port 4848 set configs.config.server-config.network-config.network-listeners.network-listener.jk-connector-8009.jk-enabled=true
/opt/glassfish4/glassfish/bin/asadmin stop-domain
/opt/glassfish4/glassfish/bin/asadmin start-domain
</pre>
* In der Konfigurationsdatei des Apache eintragen:
<pre>
&lt;IfModule mod_ssl.c&gt;
    &lt;VirtualHost _default_:443&gt;
        ServerAdmin x.y@z.at
        ...
        SSLProxyEngine  On
        ProxyRequests Off
        ProxyPreserveHost  On
        
        &lt;Location /letto&gt;
              ProxyPass ajp://localhost:8009/letto
        &lt;/Location&gt;
       ...
    &lt;/VirtualHost&gt;
&lt;/IfModule&gt;
</pre>

###  siehe auch 
* [Installation](../Installation/index.md)

