# LTI Verbindung
##  Allgemeines zu LTI 
LTI[https://www.imsglobal.org/activity/learning-tools-interoperability|LTI](https://www.imsglobal.org/activity/learning-tools-interoperability|LTI) kann für die Anbindung[https://docs.moodle.org/311/de/LTI_und_Moodle|Anbindung](https://docs.moodle.org/311/de/LTI_und_Moodle|Anbindung) von LeTTo an einen Moodle-Server[https://moodle.com/|Moodle](https://moodle.com/|Moodle) verwendet werden. 

Die Anbindung erfolgt über ein neben LeTTo laufendes LTI-Service. Bei einer Standardinstallation wird das LTI-Service im Verzeichnis /opt/letto/lti mit Start- und Stoppscript installiert. Mit dem Script /opt/letto/status.sh wird angezeigt ob neben dem LeTTo-Server auch das LTI-Service läuft.

##  Installation 
###  Installation des LTI-Services 
####  Standardinstallation 
* Der LTI-Dienst wird bei einem normalen Setup durch das Installationsscript im Verzeichnis /opt/letto/lti installiert. 
* Hierbei wird auch die benötigte MySQL-Datenbank angelegt, welche in der Datei /opt/letto/lti/application.properties angegeben ist.
* Auch die Verbindung nach aussen mit einem AJP-Connector auf Port 9099 und den zwei Endpunkten /lti und /oidc werden durch das Installationsscript im apache-proxy eingetragen.

####  manuelle Installation von LTI bei einem manuell installierten System 
Für alle älteren Installationen muss LTI mit einem eigenen Installationsscript installiert werden.

Hierzu wird wie folgt vorgegangen:
* Am LeTTo-Server auf der Konsole als Benutzer root anmelden.<pre>sudo su</pre>Ins Verzeichnis /opt wechseln<pre>cd /opt</pre>**Download** des Installationsscripts von LTI :<pre>wget https://letto.at/download/letto/install-letto-lti.sh</pre>
* Script in einem Editor **konfigurieren**<pre>nano install-letto-lti.sh</pre>
  * Setzen des MySQL-Passwortes und des Linux LeTTo-Benutzers
  * Die Definition "Config=0"  auf "Config=1" ändern
  * Mit &lt;Strg&gt;-O und Enter das Script speichern
  * Mit &lt;Strg&gt;-X den Editor verlassen 
* Script **ausführbar** machen: <pre>chmod 755 install-letto-lti.sh</pre>
* Wenn der Login auf der Datenbank als root-Benutzer ohne Passwort möglich ist kann das Script die MySQL-Datenbank und den MySQL-Benutzer selbst anlegen. Prüfe mit:<pre>mysql -u root -h localhost</pre>Funktioniert der Login, dann bitte wieder mit exit; aussteigen und mit der Installation fortfahren.<br>Funktioniert der Login nicht, dann müssen die MySQL-Datenbank und der MySQL-Benutzer vor dem Start des Scripts noch angelegt werden.
* Script **starten**:<pre>./install-letto-lti.sh</pre>
* Einen **AJP-Connector** für den LTI-Dienst am Apache2 konfigurieren. In der Konfigurationsdatei des LeTTo-Servers am Apache (meist: /etc/apache2/sites-enabled/letto.conf) sollte schon ein AJP-Connector für den LeTTo-Server gesetzt werden. Dieser sieht in etwa so aus: 
<pre>      &lt;Location /letto&gt; 
     ProxyPass ajp://localhost:8089/letto
      &lt;/Location&gt; 
</pre>
* Danach bitte den AJP-Connector für LTI eintragen: 
<pre>      &lt;Location  /lti3&gt;
            ProxyPass ajp://localhost:9099/lti3 
      &lt;/Location&gt;
      &lt;Location /oidc&gt;
            ProxyPass ajp://localhost:9099/oidc
      &lt;/Location&gt;
</pre>
* Das Startscript /opt/letto/lti/ltistart.sh beim Systemstart als LeTTo-Benutzer starten. Dies kann z.B. in der Datei /etc/rc.local mit folgendem Eintrag erfolgen:<pre>sudo -u letto /opt/letto/lti/ltistart.sh </pre>
* Die MySQL Datenbank von LTI in die Datensicherung mit aufnehmen.

Das LTI-Service sollte nun im Verzeichis /opt/letto/lti installiert worden sein und ist von dort aus mit den Scripts ltistart.sh, ltistatus.sh, ltistop.sh und ltiupdate.sh zu verwalten.

####  Docker-Installation 
Ist noch nicht fertig realisiert.

###  LTI-Verbindung zum LeTTo-Server 
Nach dem ersten Start des LTI-Services muss das LTI-Service noch mit LeTTo verbunden werden.
* Login als globaler Administrator
* LTI-Konfiguration wählen
* LTI-Service initialisieren
* Durch "ping LTI-Service" kann die Verbindung zum LTI-Service überprüft werden.

###  LTI-Verbindung in LeTTo konfigurieren 
* In LeTTo als globaler Administrator
* LTI-Konfiguration im Tab Plattformen
* Existiert noch keine Verbindung mit einem Moodle-Server oder soll eine zusätzlicher Moodle-Server verbunden werden, so kann man diesen mit **Neue Plattform erzeugen** anlegen. Ist der Server schon vorhanden so braucht man nur auf die Zeile klicken und die Konfiguration wird geöffnet.
* Parallel dazu sollte man am Moodle-Server ein externes Tool anlegen. Am Besten als Administrator (unter Website Administration - Plugins - externesTool - Tool Verwalten) oder wenn man kein Administrator ist bei einem Kurs als Aktivität.
* Konfigurationsparameter am LeTTo-Server:

| -                                             |                                                                                                                                                                                    |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primärschlüssel                               | bitte hier nichts verändern                                                                                                                                                        |
| URL                                           | Hier bitte die URL des Moodle-Servers angeben z.B.: https://letto.htlstp.ac.at/moodle                                                                                              |
| Client-ID                                     | Wird am Moodle-Server nach dem Anlegen des externen Tools angezeigt wenn man wieder auf die Konfiguration des Tools geht. Bitte von dort übernehmen und am LeTTo-Server eintragen. |
| OIDC-Endpunkt, JWKS-Endpunkt, OAUTH2-Endpunkt | ergeben sich für Moodle aus der Moodle-Server-URL und sollte automatisch aus dieser korrekt gesetzt werden.                                                                        |
| Deployment-ID                                 | Kommt vom Moodle Server und ist im Normalfall 1                                                                                                                                    |
| Tool-KID-ID                                   | Ist eine ID die den LeTTo-Server beschreibt und wird aktuell noch nicht verwendet. Setze hier irgendeinen Wert ein.                                                                |
| Plattform-KID                                 | Ist eine ID die den Moodle-Server beschreibt und wird aktuell noch nicht verwendet. Setze hier irgendeinen Wert ein.                                                               |

* Nach der Konfiguration des LeTTo-Servers bitte die Daten **speichern**.
*  Konfigurationsparameter am **externen Tool** von **Moodle**:

| -                                                   |                                                                                                                                                                            |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name des Tools                                      | Ist frei vergebbar aber sinnvollerweise **LeTTo**                                                                                                                          |
| Tool-URL                                            | Wird aus dem Formular der Plattform-Konfiguration von LeTTo übernommen.                                                                                                    |
| Tool-Beschreibung                                   | frei wählbar                                                                                                                                                               |
| LTI-Version                                         | LTI 1.3                                                                                                                                                                    |
| Client-ID                                           | Wird erst beim Speichern des externen Tools berechnet. Zum Auslesen der Client-ID muss nach dem Speichern des externen Tools nochmals das externer Tool bearbeitet werden. |
| öffentlicher Schlüssel                              | Wird aus dem Formular der Plattform-Konfiguration von LeTTo übernommen.                                                                                                    |
| Anmelde-URL                                         | Wird aus dem Formular der Plattform-Konfiguration von LeTTo übernommen.                                                                                                    |
| Umleitungs-URI(s)                                   | Wird aus dem Formular der Plattform-Konfiguration von LeTTo übernommen.                                                                                                    |
| Angepasste Parameter                                | können noch frei bleiben, werden erst bei der Verwendung in einem Kurs gesetzt.                                                                                            |
| Services                                            | werden aktuell noch nicht verwendet                                                                                                                                        |
| Datenschutz - Anwendernamen an Tool übergeben       | Immer                                                                                                                                                                      |
| Datenschutz - Email des Anwenders an Tool übergeben | Immer                                                                                                                                                                      |
| Datenschutz - Bewertungen aus dem Tool akzeptieren  | Immer                                                                                                                                                                      |


##  Verhalten des LTI-Service in einer Schule konfigurieren 
Ist eine Schüler, Lehrer oder Kurs am LeTTo-Server nicht vorhanden, so kann dieser bei einer Verlinkung über LTI automatische angelegt werden. Dieses Verhalten kann für die Schule global konfiguriert werden.
* LeTTo muss mindestens in der Revision 5714 vorliegen und das LTI-Service muss installiert und gestartet sein.
* Login auf LeTTo als Admin einer Schule.
* **LTI-Konfiguration Schule** anwählen.

##  Verwendung des LTI-Services in einem Moodle-Kurs 
####  Konfiguration am Moodle-Server 
* Im Moodle Kurs unter Bearbeiten Einschalten - Material oder Aktivität anlegen - externes Tool 
* Name der Aktivität: Beliebig vergeben
* Vorkonfiguriertes Tool: Hier das Tool auswählen, welches im vorigen Punkt konfiguriert wurde.
* Speichern und zum Kurs
####  Testverlinkung erstellen 
* In LeTTo mit der rechten Maustaste auf einen Testlink und **LTI-Link kopieren**
* Den angegebenen Text in die Zwischenablage kopieren
* Im Moodle Kurs unter Bearbeiten Einschalten - Material oder Aktivität anlegen - externes Tool
* Name der Aktivität: Beliebig vergeben
* Vorkonfiguriertes Tool: Hier das Tool auswählen, welches im vorigen Punkt konfiguriert wurde.
* Allgemeines - mehr Anzeigen - Angepasste Parameter : Hier den in LeTTo markierten Text einfügen.
* Speichern und zum Kurs
####  Verbinden mit einem Kurs 
* In Moodle einen Kurs mit einem gewünschten Namen anlegen
* Im Moodle Kurs unter Bearbeiten Einschalten - Material oder Aktivität anlegen - externes Tool 
  * Name der Aktivität: Beliebig vergeben
  * Vorkonfiguriertes Tool: Hier das Tool auswählen, welches im vorigen Punkt konfiguriert wurde.
  * Allgemeines - mehr Anzeigen - Angepasste Parameter<br>Hier den Text "Kursname="  gefolgt von dem gewünschten Namen des Kurses(der Klasse) in LeTTo angeben.<pre>kursname=Der Name des Kurses in LeTTo</pre><br>Soll der Name des Kurses in Letto gleich sein wie der Kursname in Moodle, so kann man als Kursname "_self" angeben:<pre>kursname=_self</pre>
  * Ist der Kurs in LeTTo noch nicht vorhanden und in der Benutzerkonfiguration von LTI der Schule ist am LeTTo-Server die automatische Anlage des Kurses aktiviert, so wird der Kurs am LeTTo-Server automatisch angelegt, sobald sich der Lehrer mit dem LTI-Link zu LeTTo verbindet.<br>Die Abteilung/Institut deren der Kurs zugeordnet ist wird automatisch als erste Abteilung in der Abteilungsliste am LeTTo-Server gelistet. Soll der Kurs einer definierten Abteilung zugeordnet sein, so muss diese durch einen Doppelpunkt getrennt angegeben werden (Diese Abteilung muss auf LeTTo schon existieren, andernfalls kommt es beim Verlinken zu einer Fehlermeldung) <pre>kursname=_self:E370-02</pre>
  * Speichern und zum Kurs

