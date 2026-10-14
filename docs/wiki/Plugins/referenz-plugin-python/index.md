# Referenz-Plugin (Python)
<!-- erstellt aus plugin-demo-python @ 10ecc4f (revision 1000) – bei Änderungen im Plugin-Repo nachziehen -->

Das Projekt **plugin-demo-python** ist eine Referenzimplementierung eines LeTTo-Plugin-Services in Python (FastAPI).
Es ist eine Portierung des [Referenz-Plugins (Java)](../referenz-plugin-java/index.md) und implementiert **dieselbe REST-Schnittstelle**.
Als Beispiel enthält es das Plugin **UhrPy** – ein Uhrblatt, auf dem eine Uhrzeit eingestellt und mit der Musterlösung verglichen wird.
Das Plugin dient nur zur Veranschaulichung und ist nicht für den Unterricht gedacht.

## Allgemeines

* Der Plugin-Service läuft als eigener Docker-Container im Netzwerk `nw-letto` neben dem LeTTo-Server.
* LeTTo kommuniziert mit dem Plugin über dieselben REST-Endpunkte und JSON-DTOs wie beim Java-Plugin.
  Die ausführliche Beschreibung jedes Endpunkts, DTOs und Enums steht deshalb in der Java-Doku; diese Seiten beschreiben die Python-Umsetzung und die Unterschiede.
* Beim Start registriert sich der Service selbst am Setup-Service des LeTTo-Servers.
* Der gesamte Service steckt in einer Datei: `app/main.py`.

## Technische Daten

| Eigenschaft | Wert |
|---|---|
| Sprache | Python 3.12 |
| Framework | FastAPI 0.115, Server uvicorn 0.34, DTOs mit Pydantic 2.10 |
| Bilderzeugung | Pillow 10.4 |
| HTTP-Client (Registrierung) | httpx 0.28 |
| Debugger | debugpy |
| Docker-Image | `lettohub/letto-plugin-demopython:latest` (Basis `python:3.12-slim`) |
| Servicepfad im Demo | `/plugindemopython` (Umgebungsvariable `SERVICEPATH`) |
| Service-Name | `letto-plugindemopython`, Version 1.0 |
| Plugin-Typ | `UhrPy` |

## Links

* Quellcode: [https://github.com/LeTTo-GmbH/plugin-demo-python](https://github.com/LeTTo-GmbH/plugin-demo-python)
* Docker-Image: [https://hub.docker.com/r/lettohub/letto-plugin-demopython](https://hub.docker.com/r/lettohub/letto-plugin-demopython)
* Am eigenen Server (bei installiertem Plugin):
  * Hilfeseite: `https://<servername>/plugindemopython/help`
  * Swagger-UI: `https://<servername>/plugindemopython/docs` – oben mit Link auf diese Doku, jeder Endpunkt und jedes DTO verlinkt auf die passende Seite der Java-Doku
  * OpenAPI-Beschreibung (JSON): `https://<servername>/plugindemopython/openapi.json`
* Plugintester zum Testen: `https://<servername>/plugintester` (über das Setup-Service installierbar)

## Python oder Java?

| | Java | Python |
|---|---|---|
| Aufbau | Spring Boot, Klassen je Aufgabe, `BasePlugin` als Basisklasse | eine Datei `app/main.py`, Plugin-Klasse `PluginDemo` |
| Neues Plugin anlegen | Script `setpluginname.bat` | Konstanten und Konfigurationsdateien von Hand anpassen |
| Bild | wird in Java gezeichnet (`paint`) | wird mit Pillow gezeichnet |
| Konfigurationsdialog im iframe (`CONFIGMODE_URL`) | implementiert | nicht implementiert |
| Tests | – | pytest, ohne Docker und ohne LeTTo lauffähig |

## Inhalt

* [Architektur](architektur/index.md): Aufbau von `app/main.py`, Pfade, Konfigurationssitzungen, Registrierung
* [Eigenes Plugin erstellen](eigenes-plugin/index.md): neues Plugin aus dem Python-Demo erstellen
* [Plugin-API](plugin-api/index.md): die Plugin-Klasse `PluginDemo`, die `CONF_*`-Konstanten und das Uhr-Plugin
* [REST-Schnittstelle](rest-schnittstelle/index.md): alle Endpunkte mit Links zur Java-Doku und den Unterschieden der Python-Version
* [DTOs](dtos/index.md): Pydantic-Modelle und ihre Abweichungen von den Java-DTOs
* [Build und Deployment](build-deployment/index.md): Docker, Proxy, Registrierung, Tests, Debugging mit PyCharm

[Plugins](../index.md)
