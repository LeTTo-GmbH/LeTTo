Das Export-Service wird für folgende Aufgaben bei einem LeTTo-Server verwendet:

* Export von .lto-Dateien
* Import von .lto-Dateien
* Import von Moodle-XML-Dateien
* Druck von PDF-Dateien
* Export von Fragen in ein eigenständiges Question-Service

== siehe auch ==
* [[Docker_compose_files]]
* [[LeTTo_Environment]]

== Erhöhen des RAM-Speichers ==
Für den Export und Import von großen Datenmengen kann eine Erhöhung des RAM-Speichers sinnvoll sein.

Vorgangsweise:
* editiere die .env-Datei von LeTTo (/opt/letto/docker/compose/letto/.env) &lt;br&gt;[[Datei:LeTTo Env.png|800px]]
** setze bei der Variablen JAVA_OPTS_EXPORT den Xmx-Wert auf einen größeren Wert (zB.: 2.5GB). Fehlt die Variable füge sie hinzu. &lt;pre&gt;JAVA_OPTS_EXPORT=-Xms50m -Xmx2500m &lt;/pre&gt;
** setze bei der Variablen EXPORT_MEMORY_LIMIT einen um mindestens 300MB größeren Wert als den zuvor gesetzten Xmx-Wert (zB.: 3GB). Fehlt die Variable füge sie hinzu. &lt;pre&gt;EXPORT_MEMORY_LIMIT=3GB&lt;/pre&gt;
* restarte (stop und start) das Export Services &lt;br&gt; [[Datei:Restart Export.png|800px]]

