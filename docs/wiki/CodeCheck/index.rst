= Allgemeines =
Das [[Plugins|Plugin]] CodeCheck(SourceCode) wird verwendet um Programme von Schülern in verschiedenen Programmiersprachen (aktuell nur Java) automatische korrigieren zu können.
= Verwendung =
* Das Plugin kann nur in [[Fragetypen#Mehrfachberechnungsfrage|Mehrfachberechnungsfragen]] korrekt verwendet werden
* Definition des Plugins: Im Edit-Modus einer Frage im Plugin-Dialog "SourceCode" hinzufügen 
:[[Datei:ClipCapIt-181029-115529.PNG]]

* [[SourceCode_Konfiguration|Konfiguration]] des Plugins mit dem Werkzeug-Button 
:[[Datei:ClipCapIt-181029-115614.PNG]]

* Einfügen einer neuen Antwort mit Strg-Q

* Durch einen Klick auf den MODE: Auswahl des Mode '''Plugin'''
:[[Datei:ClipCapIt-181029-120038.PNG]]


= Konfiguration =

[[SourceCode Konfiguration|Konfigurationsdialog]]

= Server Konfiguration für Security-Prüfung =
Um die Security-Prüfung am Server korrekt durchführen zu können muss am Server nach einer Standard-Installation folgende Änderung vorgenommen werden!
=== Glassfish Server 4.1 ===
In der Glassfish-Admin Konsole (Port 4848) im Punkt ''Configurations-server-config-JVM Settings-JVM Options''
* Suche nach -Djava.security.policy=${com.sun.aas.instanceRoot}/config/server.policy
:[[Datei:ClipCapIt-181105-084000.PNG]]
* An die oben angegebene Datei (z.B.: /opt/glassfish4/glassfish/domains/domain1/config/server.policy ) hinten anfügen:
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
* Suche in der Datei nach:
&lt;pre&gt;
  permission java.io.FilePermission       "&lt;&lt;ALL FILES&gt;&gt;", "read,write";
&lt;/pre&gt;
und ändere auf:
&lt;pre&gt;
  permission java.io.FilePermission "&lt;&lt;ALL FILES&gt;&gt;","read";
&lt;/pre&gt;

=== Tomcat v8.5 und Eclipse ===
* Suche im Installationspfad vom Tomcat nach der Datei ''catalina.policy'' und füge hinten an:
&lt;pre&gt;
grant {
  permission java.util.PropertyPermission "java.security.policy", "write";
  permission java.lang.RuntimePermission "createSecurityManager";
  permission java.lang.RuntimePermission "setSecurityManager";
  permission java.security.SecurityPermission "getPolicy";
  permission java.lang.RuntimePermission "accessDeclaredMembers";
  permission java.io.FilePermission "C:\workspace-oxygen-letto\.metadata\.plugins\org.eclipse.wst.server.core\tmp0\webapps", "read";
  permission java.lang.RuntimePermission "setIO";
  permission java.lang.reflect.ReflectPermission "suppressAccessChecks";
};
&lt;/pre&gt;
* In der Eclipse: Run-Run Configurations -&gt; Apache Tomcat - Tomcat v8.5 Server -&gt; Arguments - VM-Arguments: füge hinzu:
&lt;pre&gt;
-Djava.security.policy="C:\workspace-oxygen-letto\Servers\Tomcat v8.5 Server at localhost-config\catalina.policy"
&lt;/pre&gt;

=== andere JavaEE-Server ===
Haben wir noch nicht getestet.


[[Category:Plugins]]

