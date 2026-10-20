# Datensicherung
Für eine Datensicherung ist einerseits die **Datenbank** zu sichern, und andererseits alle Dateien, welche in lokale Verzeichnisse vom Letto-Server gespeichert werden. Alle lokalen Verzeichnisse sind in der globalen Konfiguration vom Server angegeben und liegen bei einer Standardkonfiguration im Verzeichnis /opt/letto.

Ein mögliches Script für die Datensicherung:
<pre>
#!/bin/bash

touch /sicherung/sqlsicherungaktiv
mysqldump --user=Username --password=dasPasswortEinesUsersMitLeserecht -h 127.0.0.1 letto | gzip -9 &gt;/sicherung/letto.sql.gz
tar -czf /sicherung/opt.tgz /opt
tar -czf /sicherung/etc.tgz /etc
rm -f /sicherung/sqlsicherungaktiv
</pre>

