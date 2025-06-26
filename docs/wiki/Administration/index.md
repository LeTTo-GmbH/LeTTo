# Administration
##  Installation eines LeTTo-Servers 
* [Anforderungen](../Anforderungen/index.md) an den LeTTo-Server
* [Installation](../Installation/index.md) des LeTTo-Servers
* [Migration_LeTTo_zu_Docker](../MigrationLeTTozuDocker/index.md) eines bestehenden LeTTo-Servers ohne Docker
* Einspielen der Daten einer neuen Schule oder eines neuen Schuljahres
  * [Datenimport aus Untis und Sokrates](../Datenimport/index.md) wenn damit gearbeitet wird
  * [Datenimport ohne Untis-Daten](../DatenimportohneUntis-Daten/index.md) mit Hilfe von CSV-Dateien
  * direktes [Anlegen von einzelnen Lehrern mit Gegenständen](../AnlegenvoneinzelnenLehrernmitGegenständen/index.md) und Schülern
* [Login-Seite](../Login-Seite/index.md) anpassen

##  Betrieb einer Docker-basierten Installation 
* [Verzeichnisse und Docker-Volumes](../VerzeichnisseundDocker-Volumes/index.md)
* [Container Struktur](../ContainerStruktur/index.md)
* [Setup-Service](../Setup-Service/index.md)
* [Datensicherung-Docker](../Datensicherung-Docker/index.md)
* [https-Zertifikat](/notimplemented/index.md)
* [docker compose files](../Dockercomposefiles/index.md)
* [Update von rev65xx auf aktuelle Stable rev66xx](../Updaterev66xx/index.md)

##  Betrieb einer Linux-basierten Installation ohne Docker 
* Nur zur Info - Wird für Neuinstallationen nicht mehr unterstützt! Bitte verwenden sie für Neuinstallationen die Docker-Version !
* [Globale Konfiguration](../GlobaleKonfiguration/index.md) für die Einstellung der Parameter für Server, AD-Login und Schule
* [LTI Verbindung](../LTIVerbindung/index.md) für die Anbindung von LeTTo als externes Tool an einen Moodle-Server
* [Datensicherung](../Datensicherung/index.md) von Installationen
* [Stabilitätsprobleme](../Stabilitätsprobleme/index.md) beim Betrieb eines Servers

##  Administrative FAQ 
* Im Setup-Service steht die **rote Fehlermeldung** "FAIL https://schulename/config/ping" neben "https-REST-ping self" - siehe [Https REST ping](../HttpsRESTping/index.md)
* Ein oder mehrere Docker-Container restarten permanent und kommen nicht hoch -&gt; Das System hat zu wenig CPU-Leistung oder wenig RAM weshalb die Container nicht innerhalb einer gewissen Zeitspanne starten können und deshalb nach dieser Zeit automatisch neu starten -&gt; Abhilfe : CPU Leistung erhöhen bzw. RAM-Speicher erweitern.
* Beim Import oder Export einer großen .lto-Datei bekommt man einen OutOfMemoryError  -&gt; Abhilfe: Erhöhen des RAM-Speichers vom [Export-Service](../Export-Service/index.md)


