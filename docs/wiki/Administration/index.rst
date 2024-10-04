= Installation eines LeTTo-Servers =
* [[Anforderungen]] an den LeTTo-Server
* [[Installation]] des LeTTo-Servers
* [[Migration_LeTTo_zu_Docker]] eines bestehenden LeTTo-Servers ohne Docker
* Einspielen der Daten einer neuen Schule oder eines neuen Schuljahres
** [[Datenimport|Datenimport aus Untis und Sokrates]] wenn damit gearbeitet wird
** [[Datenimport ohne Untis-Daten]] mit Hilfe von CSV-Dateien
** direktes [[Anlegen von einzelnen Lehrern mit Gegenständen]] und Schülern
* [[Login-Seite]] anpassen

= Betrieb einer Docker-basierten Installation =
* [[Verzeichnisse und Docker-Volumes]]
* [[Container Struktur]]
* [[Setup-Service]]
* [[Datensicherung-Docker]]
* [[https-Zertifikat]]
* [[docker compose files]]
* [[Update rev66xx|Update von rev65xx auf aktuelle Stable rev66xx]]

= Betrieb einer Linux-basierten Installation ohne Docker =
* Nur zur Info - Wird für Neuinstallationen nicht mehr unterstützt! Bitte verwenden sie für Neuinstallationen die Docker-Version !
* [[Globale Konfiguration]] für die Einstellung der Parameter für Server, AD-Login und Schule
* [[LTI Verbindung]] für die Anbindung von LeTTo als externes Tool an einen Moodle-Server
* [[Datensicherung]] von Installationen
* [[Stabilitätsprobleme]] beim Betrieb eines Servers

= Administrative FAQ =
* Im Setup-Service steht die '''rote Fehlermeldung''' "FAIL https://schulename/config/ping" neben "https-REST-ping self" - siehe [[Https REST ping]]
* Ein oder mehrere Docker-Container restarten permanent und kommen nicht hoch -&gt; Das System hat zu wenig CPU-Leistung oder wenig RAM weshalb die Container nicht innerhalb einer gewissen Zeitspanne starten können und deshalb nach dieser Zeit automatisch neu starten -&gt; Abhilfe : CPU Leistung erhöhen bzw. RAM-Speicher erweitern.
* Beim Import oder Export einer großen .lto-Datei bekommt man einen OutOfMemoryError  -&gt; Abhilfe: Erhöhen des RAM-Speichers vom [[Export-Service]]


[[Kategorie:Administration]]

