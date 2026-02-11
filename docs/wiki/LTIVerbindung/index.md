# LTI-Service
##  Allgemeines zu LTI
[LTI](https://www.imsglobal.org/activity/learning-tools-interoperability) kann für die Anbindung von [LeTTo über LTI](https://docs.moodle.org/501/en/LTI_and_Moodle) ab einen [Moodle-Server](https://moodle.com) verwendet werden.

Die Anbindung erfolgt über das LTI-Service welches in einem eigenen Docker-Container läuft.

## Installation des LTI-Services
* wähle "update-config" im Setup-Service(/config)<br>![img.png](img.png)
* wähle unten bei den verfügbaren yml-Files bei lti "install Service"<br>![img_1.png](img_1.png)
* starte das LTI-Service<br>![img_2.png](img_2.png)
* Verbinde mit dem Letto-Server der Schule als globaler Administrator. Wechsle zur Rolle "Global" und zum Punkt "LTI-Konfiguration"<br>![img_10.png](img_10.png)
* Initialisiere die LTO-Verbindung mit "LTI-Verbindung initialisieren".<br>![img_11.png](img_11.png)
* Prüfe die Verbindung mit "Ping LTI-Service". Es sollte "Ping war erfolgreich" angezeigt werden.
* Wechsle auf Platformen und klicke auf "Neue Plattform erzeugen"
* Fülle die Felder wie folgt aus:
  * URL: die URL des Moodle-Servers, zB https://moodle.htlstp.ac.at
  * Die restlichen Felder können frei gelassen werden, bzw. werden automatisch ausgefüllt.
  * Speichere die Plattform mit "speichern"<br>![img_9.png](img_9.png)
  * Die Werte im Unteren Bereich "Links und Keys" werden für die Konfiguration des externen Tools am Moodle-Server benötigt.

## LTI-Verbindung im Moodle konfigurieren
* Am Moodle als Administrator anmelden
* Gehe zu "Website-Administration" -> "Plugins" -> "External tool" -> "Manage tools"
* Klicke auf "Neues Werkzeug hinzufügen"
* Kurze Erklärung der Felder:

| -                                                   |                                                                                                                                                                            | Beispiel                                       |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| Name des Tools                                      | Ist frei vergebbar aber sinnvollerweise **LeTTo**                                                                                                                          | LeTTo                                          |
| Tool-URL                                            | Wird aus dem Formular der Plattform-Konfiguration von LeTTo übernommen.                                                                                                    | https://t1.letto.at/lti/lti3                   |
| Tool-Beschreibung                                   | frei wählbar                                                                                                                                                               | LeTTo t1 Testserver                            |
| LTI-Version                                         | LTI 1.3                                                                                                                                                                    | LTI 1.3                                        | 
| Client-ID                                           | Wird erst beim Speichern des externen Tools berechnet. Zum Auslesen der Client-ID muss nach dem Speichern des externen Tools nochmals das externer Tool bearbeitet werden. |                                                |
| öffentlicher Schlüssel                              | Wird aus dem Formular der Plattform-Konfiguration von LeTTo übernommen.                                                                                                    |                                                |
| Anmelde-URL                                         | Wird aus dem Formular der Plattform-Konfiguration von LeTTo übernommen.                                                                                                    | https://t1.letto.at/lti/oidc/login_initiations |
| Umleitungs-URI(s)                                   | Wird aus dem Formular der Plattform-Konfiguration von LeTTo übernommen.                                                                                                    | https://t1.letto.at/lti/lti3                   |
| Angepasste Parameter                                | können noch frei bleiben, werden erst bei der Verwendung in einem Kurs gesetzt.                                                                                            |                                                |
| Services                                            | werden aktuell noch nicht verwendet                                                                                                                                        |                                                |
| Datenschutz - Anwendernamen an Tool übergeben       | Immer                                                                                                                                                                      | Immer                                          |
| Datenschutz - Email des Anwenders an Tool übergeben | Immer                                                                                                                                                                      | Immer                                          |
| Datenschutz - Bewertungen aus dem Tool akzeptieren  | Immer                                                                                                                                                                      | Immer                                          |
* Beispielhafte Konfiguration eines externen Tools am Moodle-Server: <br> ![img_3.png](img_3.png)<br>![img_4.png](img_4.png)
* Die Adressen des LeTTo-Servers und der Public-Key kann aus der LeTTo-Konfigurationsseite übernommen werden.
* Name und Email-Adresse müssen im Punkt "Privacy" mitgeschickt werden!

## LTI-Verbindung in einem Moodle-Kurs verwenden
* Am Moodle als Lehrer anmelden
* Wechsle zu "Beispiele Editieren" oder "Beispielsammlung"
* Erzeuge eine neue Online-Aktivität und füge Beipspiele hinzu.
* Erstelle einen LTI-Link des erstellten Tests<br>![img_8.png](img_8.png)
* Kopiere den LTI-Link in die Zwischenablage<br>![img_6.png](img_6.png)
* Erstelle in einem Moodle-Kurs eine Aktivität als LeTTo-Tool und füge die Daten des LTI-Link 
  als Custom -Parameters hinzu<br>![img_7.png](img_7.png)
* Der Student kann nun über diese Aktivität mit dem LeTTo-Server über einen Button verbunden werden.
