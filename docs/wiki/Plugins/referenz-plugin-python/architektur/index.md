# Architektur des Referenz-Plugins (Python)
<!-- erstellt aus plugin-demo-python @ 7a69b2c (revision 1000) – bei Änderungen im Plugin-Repo nachziehen -->

## Aufbau des Services

* FastAPI-Anwendung `app.main:app`, gestartet mit uvicorn auf Port 8080 (`scripts/start.sh`).
* Für jede Anfrage von LeTTo wird mit `create_plugin(typ, name, config)` eine **neue Plugin-Instanz** erzeugt; die Anfragen sind dadurch zustandslos.
  Ausnahme ist der Konfigurationsdialog, dessen Zustand über die `configurationID` gehalten wird.
* Der Ablauf zwischen LeTTo-Server und Plugin ist derselbe wie beim Java-Plugin – siehe [Architektur des Java-Plugins](../../referenz-plugin-java/architektur/index.md).

## Aufbau von `app/main.py`

| Abschnitt | Inhalt |
|---|---|
| CONFIGURATION | `CONF_*`-Konstanten: Servicepfad, Namen, Version, JavaScript-Methoden, Hilfe- und JS-Dateien, Bildgröße, Konfigurations-Modus und Schalter wie `useVars` – siehe [Plugin-API](../plugin-api/index.md) |
| Environment | Werte aus der Compose-Datei: Setup-URI, Passwort, interne/externe URI, Einstellungen der Registrierung |
| Paths | Basispfade `LOCAL_API` (`/open`), `EXTERN_OPEN` (`<servicepath>/api/open`), Ping- und Info-Pfade |
| Logging | Log-Format; Aufrufe von `/open/pluginlist`, `/open/generalinfolist`, `/version` und `/ping` werden aus dem Zugriffslog gefiltert |
| Utilities | Zeitumrechnung `parse_time_seconds`, Uhrzeit-Vergleich mit Toleranz, Lesen von Ressourcen, Zeichnen des Uhrblatts mit Pillow, Speichern von Bildern in der Bildablage (`save_plugin_image`) |
| DTOs | Pydantic-Modelle mit denselben Feldnamen wie die Java-DTOs – siehe [DTOs](../dtos/index.md) |
| Plugin | Klasse `PluginDemo` – die eigentliche Plugin-Logik |
| Plugin registry | `REGISTERED_PLUGINS` und `create_plugin` (entspricht der `StartupConfiguration` in Java) |
| Registrierung | Warten auf die eigene Erreichbarkeit, dann Registrierung am Setup-Service mit Wiederholungen |
| Zustandsverarbeitung | `PluginConfigurationState` und `CONFIG_STATES` für die Konfigurationssitzungen |
| FastAPI app | App mit Swagger-UI unter `<servicepath>/docs`, Router für die Endpunkte |
| OpenAPI | Beschreibung und `externalDocs` verlinken auf diese Python-Doku (`DOC_PYTHON_URL`); jeder Endpunkt und jedes DTO verlinkt auf seine Seite in der Java-Doku; alphabetische Sortierung |

Weitere Dateien:

| Datei / Verzeichnis | Inhalt |
|---|---|
| `resources/index.html` | Hilfeseite des Services |
| `resources/plugins/uhr/` | Hilfetext `UhrPy.html` und JavaScript `uhrPyScript.js`, `uhrPyConfigScript.js` |
| `tests/` | pytest-Tests für Bewertung, Score-Endpunkt und OpenAPI-Doku |
| `scripts/` | `start.sh` (Start mit/ohne Debugger), `healthcheck.sh` |
| `yml/`, `proxy/`, `Dockerfile`, `build.bat` | Deployment – siehe [Build und Deployment](../build-deployment/index.md) |
| `dockerhub/README.md`, `dockerhub/dockerhub-description.ps1` | Beschreibung des Images auf Docker Hub und Script zum Hochladen |

## Erreichbarkeit der Endpunkte

| Basispfad | Inhalt | erreichbar |
|---|---|---|
| `/open/...` | interne Plugin-API (wie der `ApiController` in Java) | nur im Docker-Netzwerk |
| `<servicepath>/open/...` | **derselbe Satz** an Endpunkten noch einmal, zusätzlich zum Java-Plugin | extern über den Proxy |
| `<servicepath>/api/open/...` | offene API für den Browser (wie `ApiExternOpenController`) | extern über den Proxy |
| `/ping`, `/info`, `/version` | Erreichbarkeit und Service-Informationen | nur im Docker-Netzwerk |
| `<servicepath>/ping`, `<servicepath>/open/ping`, `<servicepath>/open/info` | Erreichbarkeit und Service-Informationen | extern über den Proxy |
| `<servicepath>/`, `<servicepath>/index.html`, `<servicepath>/help` | Hilfeseite | extern über den Proxy |
| `<servicepath>/docs`, `<servicepath>/openapi.json` | Swagger-UI und OpenAPI-Beschreibung | extern über den Proxy |

Hinweis: Weil die interne Plugin-API auch unter `<servicepath>/open/...` angeboten wird, sind alle Plugin-Endpunkte – anders als beim Java-Plugin – über den Proxy von außen erreichbar.

## Konfigurationssitzungen

* [configurationinfo](../../referenz-plugin-java/rest-schnittstelle/ApiController/configurationInfo/index.md) legt eine Sitzung (`PluginConfigurationState`) an,
  **aber nur, wenn eine `configurationID` mitgeschickt wird** – anders als in Java wird keine ID erzeugt.
* Die Sitzung speichert Typ, Name, Konfiguration, Plugin-Instanz, `PluginConfigurationInfoDto`, `PluginConfigDto` und die Frage.
* Bei jedem Zugriff werden Sitzungen entfernt, deren letzter Zugriff länger als `timeout` Sekunden zurückliegt (Standard 300).
* `PluginConfigDto.pluginDtoUri` zeigt auf `<letto_plugin_uri_extern><servicepath>/api/open/reloadplugindto`; die Vorschau im Dialog holt darüber ein neues `PluginDto`.
* Der Konfigurationsdialog im iframe (`CONFIGMODE_URL`) ist nicht implementiert: `configurationUrl` bleibt leer, einen `confighttp`-Endpunkt gibt es nicht.

## Registrierung am Setup-Service

1. Beim Start (FastAPI-`lifespan`) wird ein Hintergrund-Task gestartet, sofern `PLUGIN_REGISTER_ON_READY` nicht `false` ist.
2. Der Task wartet, bis der Service über seine interne URI erreichbar ist: `/ping`, `/open/pluginlist`, `/open/generalinfolist` und
   `POST /open/generalinfo` müssen mit HTTP 200 antworten (bis zu `PLUGIN_REGISTER_RETRIES` Versuche im Abstand von `PLUGIN_REGISTER_DELAY_SECONDS`).
   Grund: Das Setup ruft direkt nach der Registrierung weitere Endpunkte auf.
3. Dann wird `POST <letto_setup_uri>/config/auth/user/registerplugin` mit Basic Auth (Benutzer `user`, Passwort aus `letto_user_user_password`) aufgerufen.
4. Schlägt ein Durchlauf fehl, wird nach `PLUGIN_REGISTER_PAUSE_SECONDS` (Standard 60 s) erneut versucht, bis die Registrierung gelingt.

Details zu den Daten der Registrierung siehe [Build und Deployment](../build-deployment/index.md#registrierung-am-letto-server).

[Referenz-Plugin (Python)](../index.md)
