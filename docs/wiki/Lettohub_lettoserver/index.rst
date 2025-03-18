siehe auch
* [[docker compose files]]

= LeTTo-Server aktuelle Version =
Monolith welcher aktuell noch fast alles erledigt. Wird in Zukunft in mehrere Micro-Services zerteilt.
== Container ==
'''lettohub/lettoserver'''

== Tags ==
{| class="wikitable" style="text-align: left; width: 100%;"
| Tag || Beschreibung || Anmerkung
|- 
| beta || Beta Version für Beta-Test-Phasen, nicht für den Produktivbetrieb || 
|-
| daily || tagesaktuelle Letztversion für den Produktivbetrieb von ausgewählten Testschulen ||
|-
| stable || letzte stabile Version für den Produktivbetrieb ||
|-
| debug || Bitte nicht verwenden ist tagesaktuell nur für Debugging-Zwecke ||
|-
| revXXXX || Revision mit der Nummer XXXX. Nur wenn man eine definierte Version verwenden möchte. ||
|-
|}

== Ports ==
{| class="wikitable" style="text-align: left; width: 100%;"
| Port || Beschreibung
|- 
| 8080 || http-Port für die interne Kommunikation innerhalb des Docker-Netzwerkes
|-
| 9080 || https-Port mit selbstsigniertem Zertifikat für externe Kommunkation 
|-
| 5080 || debugging-Port, aktiv wenn die Environment-Variable debug=true gesetzt wird
|}

== Pfade welche als Volume verbunden werden sollten ==
school muss durch das Schulkürzel ersetzt werden!!

{| class="wikitable" style="text-align: left; width: 100%;"
| Pfad im Docker Container || Beschreibung || üblicher Wert
|- 
| /opt/letto/public || statische öffentliche Webinhalte vom Server für Werbeeinschaltungen || /opt/letto/docker/public
|-
| /opt/letto/images || Bilddateien müssen über https://dnsname/images erreichbar sein  || /opt/letto/docker/storage/images
|-
| /opt/letto/plugins || Plugin-Bilddateien, müssen über https://dnsname/images/plugins/school erreichbar sein || /opt/letto/docker/storage/plugins/school
|-
| /opt/letto/pluginstmp || temporäre Plugin-Bilddateien, müssen über https://dnsname/images/plugins/schooltmp erreichbar sein || /opt/letto/docker/storage/plugins/schooltmp
|-
| /opt/letto/photos || Schülerphotos, müssen über https://dnsname/images/photos/school erreichbar sein || /opt/letto/docker/storage/photos/school
|-
| /opt/letto/projekte|| Dateibgaben von Schülern, müssen über https://dnsname/projekte/school erreichbar sein || /opt/letto/docker/storage/projekte/school
|-
| /opt/letto/print || PDF-Dateien, noch nicht verwendet || /opt/letto/docker/storage/print
|-
| /opt/letto/export || Export und Import-Dateien für das Export-Service || /opt/letto/docker/storage/export
|-
| /opt/letto/log || Verzeichnis für die Logfiles || /opt/letto/docker/storage/log/letto/school
|}

== Environment Variable ==
{| class="wikitable" style="text-align: left; width: 100%;"
| Variable || Beschreibung || üblicher Wert || muss gesetzt sein
|- 
| TZ || Zeitzone || Europe/Berlin || nein
|-
| mysqlhost || Adresse des MySQL-Servers der Schuldatenbank || letto-mysql.nw-letto:3306 || ja
|-
| mysqldb || Datenbankname der Schuldatenbank || letto || ja
|-
| mysqlpars || Datenbankparameter für den Datenbankzugriff || useSSL=false&amp;useUnicode=true&amp;useJDBCCompliantTimezoneShift=true&amp;useLegacyDatetimeCode=false&amp;serverTimezone=UTC&amp;allowPublicKeyRetrieval=true || ja
|-
| memory || maximal verwendeter RAM-Speicher || 500m || nein
|-
| mysqluser || Datenbankbenutzer an der Schuldatenbank || letto || ja
|-
| mysqlpassword || Klartext-Datenbankpasswort an der Schuldatenbank || || ja
|-
| letto_local_restkey || Authentifizierungsschlüssel des Servers am Lizenzserver || || ja
|-
| jwt_secret || Base64 kodiertes Token-Secret für die Authentifizierung || || ja
|-
| server_secret || Base64 kodiertes Token-Secret für die Server-Server Kommunikation || || ja
|-
| letto_local_privatkey || Privater Schlüssel für die Kommunkation || || ja
|-
| letto_local_publickey || öffentlicher Schlüssel für die Kommunikation || || ja
|-
| school || Schulkürzel mit dem dann auch der Server erreichbar sein soll || || ja
|-
| letto_school || Schulkürzel mit dem dann auch der Server erreichbar sein soll || || ja
|-
| letto_schulen || Liste aller Schulkürzel der Schulen die auf dem gesamten Server laufen, durch Leerzeichen getrennt. || || nein
|-
| letto_pathImages || Pfad der Bilder innerhalb des Docker-Containers || /opt/letto/images || ja
|-
| letto_webPathImages || öffentlicher Endpunkt am Server wo die Bilder erreichbar sind || /images || ja
|-
| letto_pathImagesPhotos || Pfad der Schülerphotos innerhalb des Docker-Containers || /opt/letto/photos || ja
|-
| letto_webPathImagesPhotos ||  öffentlicher Endpunkt am Server wo die Schülerphotos erreichbar sind || /images/photos/school || ja
|-
| letto_pathImagesPlugins || Pfad der Pluginbilder innerhalb des Docker-Containers || /opt/letto/plugins || ja
|-
| letto_webPathImagesPlugins ||  öffentlicher Endpunkt am Server wo die Pluginbilder erreichbar sind || /images/plugins/school || ja
|-
| letto_pathProjekt || Pfad der Schülerabgaben des Docker-Containers || /opt/letto/projekte|| ja
|-
| letto_pathProjektAbgaben || Pfad der Schülerabgaben des Docker-Containers || /opt/letto/projekte|| ja
|-
| letto_webPathProjekte ||  öffentlicher Endpunkt am Server wo die Schülerabgaben erreichbar sind || /projekte/school || ja
|-
| letto_schule_standard_lizenz || Lizenz der Schule || || ja
|-
| letto_schule_standard_idschule_lizenz || ID der Schule am Lizenzserver || || ja
|-
| letto_schule_standard_idschule_data || ID der Schule in der Datenbank || || ja
|-
| letto_schule_standard_schulname || Name der Schule || || ja
|-
| letto_schule_standard_lettodata_uri ||Docker-Interne URL des Data-Services der Schule || http://letto-data-school.nw-letto:8300 || ja
|-
| letto_schule_standard_lettodata_user || Benutzer mit dem sie andere Services am Data-Service einloggen können || user || ja
|-
| letto_schule_standard_lettodata_password || Klartextpasswort für den Benutzer LETTO_1_DATA_USER || || ja
|-
| letto_schule_standard_letto_uri || Docker-Interne URL des LeTTo-Servers der Schule || http://letto-server-school.nw-letto:8080 || ja
|-
| letto_schule_standard_login_uriextern || Öffentlich ereichbare URL des Login-Services || https://externe.dns.at/login || ja
|-
| letto_schule_standard_letto_uriextern  || Öffentlich erreichbar URL des LeTTo-Servers || https://externe.dns.at/lettoschool || ja
|-
| letto_lizenzAutomatic=0 || automatische Lizenz sollte auf 0 gesetzt sein! || ja
|-
| letto_license_server || URL des Lizenz-Servers für den Lizenz-Check || https://letto.at/lettolicense || nein
|-
| letto_user_user_password || Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer user || || ja
|-
| letto_user_gast_password || Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer gast|| || ja
|-
| letto_user_admin_password || Klartextpasswort für die Kommunikation zu einem anderen Service als Benutzer admin|| || ja
|-
| letto_lettodata_uri || Docker-Interne URL des Data-Services der Schule || http://letto-data-school.nw-letto:8300 || ja
|-
| letto_lti_uri || Docker-Interne URL des LTI-Services || http://letto-lti.nw-letto:8090 || ja
|-
| letto_image_uri ||  Docker-Interne URL des Image-Services || http://letto-image.nw-letto:8091  || ja
|-
| letto_math_uri || Docker-Interne URL des Mathematik-Services || http://letto-math.nw-letto:8092 || ja
|-
| letto_demo_uri || Docker-Interne URL für Debugging-Zwecke || http://letto-demo.nw-letto:8093 || nein
|-
| letto_mail_uri || Noch nicht verwendet || http://letto-mail.nw-letto:8094 || nein
|-
| letto_login_uri || Docker-Interne URL des Login-Services  || http://letto-login.nw-letto:8095 || ja
|-
| letto_setup_uri || Docker-Interne URL des Setup-Services im Docker-Container || http://letto-setup.nw-letto:8096 || ja
|-
| letto_print_uri || Noch nicht verwendet || http://letto-print.nw-letto:8098 || nein
|-
| letto_export_uri || Docker-Interne URL des Export-Services  || http://letto-export.nw-letto:8099 || ja
|-
| letto_beurteilung_uri || Noch nicht verwendet || http://letto-beurteilung.nw-letto:8100 || nein
|-
| letto_test_uri || Noch nicht verwendet || http://letto-test.nw-letto:8101 || nein
|-
| letto_question_uri || Docker-Interne URL des Question-Services || http://letto-question.nw-letto:8102 || ja
|-
| letto_plugin_uri || Docker-Interne URL des Plugin-Services || http://letto-plugin.nw-letto:8200 || ja
|-
| letto_pluginsourcecode_uri || Docker-Interne URL des Plugin-Sourcecode-Services || http://letto-pluginsourcecode.nw-letto:8204 || ja
|-
| letto_lettoedit_uri || Docker-Interne URL des Edit-Services || http://letto-lettoedit.nw-letto:8310 || ja
|-
| letto_lehrplan_uri || URL des Lehrplan-Services || http://letto-lehrplan.nw-letto:8700 || ja
|-
| letto_servername || öffentlicher DNS-Name des Servers für Redirections || || ja
|-
| letto_letto_uri || Docker-Interne URL des LeTTo-Servers der Schule || http://letto-server-school.nw-letto:8080 || ja
|-
| letto_login_uri || Docker-interne URL des Login-Services || http://letto-login.nw-letto:8095 || ja
|-
| letto_letto_uri_extern || Öffentlich erreichbar URL des LeTTo-Servers || https://externe.dns.at/lettoschool || ja
|-
| letto_useEdit || neues Edit-Service ist aktiviert || true || nein
|-
| letto_public_js || Endpunkt der öffentlichen Java-Script-Libraries (werden vom letto-proxy verwaltet) || /opt/letto/public/js || ja
|-
| letto_use_http || Gibt an ob redirections mit http gemacht werden sollen || 0 || nein
|-
| CATALINA_OPTS || Java Options-Variable für den LeTTo-Server || -Xms500m -Xmx1G || ja
|-
| debug || Startet den Container im Debugging-Mode auf Port 5096 || false || nein
|-
|}

= Docker Compose =
* .yml File: [http://letto.at/download/letto/setup/yml/docker-compose-school.yml http://letto.at/download/letto/setup/yml/docker-compose-school.yml]
* Environment Einstellungen für die .env-Datei [[LeTTo Environment]]


[[Kategorie:Administration]]

