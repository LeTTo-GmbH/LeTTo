# Build und Deployment des Referenz-Plugins (Python)
<!-- erstellt aus plugin-demo-python @ 10ecc4f (revision 1000) – bei Änderungen im Plugin-Repo nachziehen -->

## Build

`build.bat` (Windows, am Entwicklungsrechner mit LeTTo-Installation):

1. Docker-Image `lettohub/letto-plugin-demopython:latest` bauen
2. laufenden Container mit `docker compose … down` stoppen
3. `yml/docker-service-plugindemopython.yml` nach `/opt/letto/docker/compose/letto/` kopieren
4. Container mit `docker compose … up -d` starten

Nur das Image bauen:

```bash
docker build -t lettohub/letto-plugin-demopython:latest -f Dockerfile .
```

Das fertige Image wird auf Docker Hub als [lettohub/letto-plugin-demopython](https://hub.docker.com/r/lettohub/letto-plugin-demopython) veröffentlicht.

## Docker

`Dockerfile`:

* Basis `python:3.12-slim`, Abhängigkeiten aus `requirements.txt`
* Code in `/app/app`, Ressourcen in `/app/resources` (`RESOURCE_DIR`), Scripts in `/scripts`
* Port 8080 (REST-API); bei `debug=true` zusätzlich 5080 (debugpy)
* Healthcheck alle 30 s mit `scripts/healthcheck.sh`: ruft `http://localhost:8080/ping` auf und erwartet `pong`.
  Nach `UNHEALTHY_RETRIES` (Standard 100) Fehlschlägen werden die Prozesse im Container beendet.
* Start mit `scripts/start.sh` (uvicorn, Log in `/log/start.log`)

### Startoptionen (`scripts/start.sh`)

| Variable | Standard | Bedeutung |
|---|---|---|
| `debug` bzw. `DEBUG` | `false` | Start mit debugpy auf `DEBUG_BIND:DEBUG_PORT` |
| `DEBUG_PORT`, `DEBUG_BIND` | `5080`, `0.0.0.0` | Port und Adresse des Debuggers |
| `DEBUG_SUSPEND` | `false` | wartet beim Start, bis sich der Debugger verbindet |
| `PORT`, `APP_HOST` | `8080`, `0.0.0.0` | Port und Adresse von uvicorn |
| `LOG_LEVEL` | `info` | Log-Level von uvicorn |
| `UVICORN_WORKERS` | `1` | Anzahl der Worker (nicht im Debug-Modus) |
| `UVICORN_RELOAD` | `false` | Neuladen bei Codeänderungen |
| `APP_MODULE` | `app.main:app` | FastAPI-Anwendung |

Hinweis: Die Konfigurationssitzungen liegen im Speicher eines Prozesses. Mit mehreren Workern können Anfragen derselben Sitzung
in verschiedenen Prozessen landen; im Code ist dazu nichts dokumentiert, der Standard ist ein Worker.

### Compose-Datei `yml/docker-service-plugindemopython.yml`

* Netzwerk `nw-letto` (extern), Container und Hostname `letto-plugindemopython`, Projektname `letto-plugin-demopython`
* Volumes: Log (`/log`), Bilder (`/opt/letto/images`), Plugin-Bilder (`/opt/letto/plugins`)
* Ports: `8209` → 8080 (REST-API), `5209` → 5080 (Debugger)
* Speicherlimit `${PLUGINDEMOPYTHON_MEMORY_LIMIT:-500m}`

Wichtige Umgebungsvariablen:

| Variable | Standard | Bedeutung |
|---|---|---|
| `SERVICEPATH` | `/plugindemopython` | Servicepfad, muss zur `location` der Proxy-Konfiguration passen |
| `letto_setup_uri` | `http://letto-setup.nw-letto:8096` | URI des Setup-Services |
| `letto_user_user_password` | `SERVICE_USER_PASSWORD` | Passwort für die Registrierung |
| `letto_plugin_uri_intern` | `http://letto-plugindemopython.nw-letto:8080` | interne URI im Docker-Netz |
| `letto_plugin_uri_extern` | `https://${SERVER_NAME}` | externe URI des Servers; Basis für `pluginDtoUri` |
| `network_letto_address`, `docker_container_name` | `letto-plugindemopython` | werden an das Setup gemeldet |
| `RESOURCE_DIR` | `/app/resources` | Verzeichnis der Ressourcen |
| `debug` | `DEBUG_PLUGINS` bzw. `DEBUG` | Start mit Debugger |

Weitere Variablen (`letto_pathImages`, `letto_webPathImages`, `letto_pathPlugins`, `letto_webPathPlugins`, `letto_schulen`,
`letto_user_gast_password`, `servername`) sind gesetzt, werden im Python-Code aber nicht ausgewertet.

Einstellungen der Registrierung (nicht in der Compose-Datei, Standardwerte im Code):

| Variable | Standard | Bedeutung |
|---|---|---|
| `PLUGIN_REGISTER_ON_READY` | `true` | Registrierung beim Start |
| `PLUGIN_REGISTER_RETRIES` | 30 | Versuche je Durchlauf |
| `PLUGIN_REGISTER_DELAY_SECONDS` | 1.0 | Abstand zwischen den Versuchen |
| `PLUGIN_REGISTER_PAUSE_SECONDS` | 60.0 | Pause nach einem fehlgeschlagenen Durchlauf |

## Proxy

`proxy/plugindemopython.conf`:

```text
location /plugindemopython/ {
     resolver 127.0.0.11 valid=5s ipv6=off;
     set $plugindemopythonpath     letto-plugindemopython.nw-letto:8080;
     proxy_set_header   Host $host;
     proxy_set_header   X-Real-IP $remote_addr;
     proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
     proxy_set_header   X-Forwarded-Proto $scheme;
     proxy_pass         http://$plugindemopythonpath;
     proxy_read_timeout 90;
}
```

## Installation am LeTTo-Server

```bash
cp yml/docker-service-plugindemopython.yml /opt/letto/docker/compose/letto/
docker compose -f /opt/letto/docker/compose/letto/docker-service-plugindemopython.yml up -d
cp proxy/plugindemopython.conf /opt/letto/docker/proxy/
docker restart letto-proxy
```

## Registrierung am LeTTo-Server

* Nach dem Start wartet der Service, bis seine Endpunkte über die interne URI erreichbar sind, und registriert sich dann am Setup-Service
  (Ablauf siehe [Architektur](../architektur/index.md#registrierung-am-setup-service)).
* `POST <letto_setup_uri>/config/auth/user/registerplugin` mit Basic Auth (Benutzer `user`, Passwort `letto_user_user_password`).
* Gesendet wird ein JSON-Objekt mit den Feldern von [ConfigServiceDto](../../referenz-plugin-java/dtos/ConfigServiceDto/index.md):

| Feld | Wert |
|---|---|
| `name`, `version`, `author`, `license` | `CONF_PLUGIN_NAME`, `CONF_VERSION`, `CONF_PLUGIN_AUTHOR`, `CONF_PLUGIN_LICENSE` |
| `bs`, `ip` | Betriebssystem und IP des Containers |
| `encoding`, `programmingLanguage` | `UTF-8`, `python` |
| `nwLettoAddress`, `dockerName` | `network_letto_address`, `docker_container_name` |
| `uriIntern` | `letto_plugin_uri_intern` + `/open` |
| `extern`, `uriExtern` | `false`, `letto_plugin_uri_extern` |
| `plugin`, `scalable`, `stateless` | `true`, `false`, `true` |
| `username`, `password`, `usePluginToken` | `""`, `""`, `false` |
| `serviceStartTime`, `lastRegistrationTime` | Unix-Zeit in Sekunden |
| `params` | `{}` |
| `htmlServiceStartTime`, `htmlLastRegistrationTime` | zusätzlich: formatierte Zeitpunkte `TT.MM.JJJJ hh:mm:ss` |

* Jede Antwort mit HTTP 2xx gilt als erfolgreich; der Inhalt der Antwort wird nicht ausgewertet.
* Unterschied zu Java: Dort wird `extern = true` gemeldet und `uriExtern` endet auf `/<endpoint>/auth/user`.

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest
```

Die Tests laufen ohne Docker und ohne LeTTo (`PLUGIN_REGISTER_ON_READY=false`, Ressourcen aus dem Projektverzeichnis):

| Datei | prüft |
|---|---|
| `tests/test_scorer.py` | Zeitumrechnung, Uhrzeit-Vergleich über 12 Uhr, relative und absolute Toleranz, `PluginDemo.score`, Endpunkt `/open/score` unter `/open` und `<servicepath>/open` |
| `tests/test_openapi.py` | alphabetische Sortierung in der OpenAPI-Beschreibung, Links jedes Endpunkts, DTOs und Enum-Felds auf die Java-Doku, Link auf diese Python-Doku in OpenAPI-Beschreibung und `externalDocs`, Links auf Java- und Python-Doku auf der Hilfeseite |

## Debugging mit PyCharm

* Am LeTTo-Server bzw. Entwicklungsrechner `DEBUG=true` (oder `DEBUG_PLUGINS=true`) in der `.env`-Datei der LeTTo-Installation setzen.
* Container neu starten, damit die Debug-Optionen wirksam werden: `docker restart letto-plugindemopython`.
* In PyCharm: Run → Edit Configurations → Add New Configuration → **Attach to DAP**
  * Remote address: `localhost:5209`
  * Path Mapping: lokales Verzeichnis `app` des Projekts → `/app/app`
* Dann die Konfiguration mit „Debug" starten.

![PyCharm: Attach to DAP](pycharm-debug.png)

[Referenz-Plugin (Python)](../index.md)
