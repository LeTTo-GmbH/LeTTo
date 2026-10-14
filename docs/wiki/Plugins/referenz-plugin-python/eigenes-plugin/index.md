# Eigenes Plugin in Python erstellen
<!-- erstellt aus plugin-demo-python @ 9b07fcd (revision 1000) – bei Änderungen im Plugin-Repo nachziehen -->

Ein Script wie `setpluginname.bat` im Java-Projekt gibt es im Python-Projekt nicht; Servicepfad und Namen werden von Hand angepasst.
Die folgenden Schritte ergeben sich aus dem Aufbau des Projekts.

## Voraussetzungen

* Python 3.12 (für Tests und Entwicklung ohne Docker), Docker
* Eine LeTTo-Installation am Entwicklungsrechner (Compose-Verzeichnis `/opt/letto/docker/compose/letto`, Proxy `letto-proxy`)
* Optional PyCharm zum Debuggen im Container

## 1. Demoprojekt auschecken

```bash
git clone https://github.com/LeTTo-GmbH/plugin-demo-python.git
```

## 2. Servicepfad und Namen festlegen

Der Servicepfad ist der öffentliche Pfad des Plugins nach dem Servernamen (im Demo `/plugindemopython`) und muss am Server eindeutig sein.
Er und die Namen kommen an mehreren Stellen vor und müssen überall gleich geändert werden:

| Datei | Anpassen |
|---|---|
| `app/main.py` | `CONF_STANDARD_SERVICEPATH`, `CONF_APPLICATION_NAME`, `CONF_PLUGIN_NAME`, Standardwerte von `NW_LETTO_ADDRESS` und `DOCKER_CONTAINER_NAME` |
| `yml/docker-service-plugindemopython.yml` | Dateiname, Projektname (`name:`), Service-Name, Image, `hostname`, `container_name`, Log-Verzeichnis, `SERVICEPATH`, `network_letto_address`, `docker_container_name`, `letto_plugin_uri_intern`, Ports (8209/5209 dürfen nicht mit anderen Plugins kollidieren) |
| `proxy/plugindemopython.conf` | Dateiname, `location /<servicepath>/`, Variablenname und Ziel `letto-<name>.nw-letto:8080` |
| `Dockerfile` | `ENV SERVICEPATH` |
| `build.bat` | Image-Name und Name der yml-Datei |
| `resources/index.html`, Hilfedateien | Links auf Swagger-UI und Quellcode |
| `tests/` | Pfade `/plugindemopython/...` in den Tests |

Die Umgebungsvariable `SERVICEPATH` in der Compose-Datei hat Vorrang vor `CONF_STANDARD_SERVICEPATH`.

## 3. Plugin konfigurieren

In `app/main.py` die `CONF_*`-Konstanten setzen – Bedeutung siehe [Plugin-API](../plugin-api/index.md):

```python
CONF_PLUGIN = "MeinPlugin"                        # Plugin-Typ in LeTTo
CONF_VERSION = "1.0"
CONF_INIT_JS = "initPluginMein"                   # JS-Methode für die Eingabe
CONF_CONFIG_JS = "configPluginMein"               # JS-Methode für den Konfigurationsdialog
CONF_HELPFILES = ["plugins/mein/Mein.html"]
CONF_JSLIBS = ["plugins/mein/meinScript.js", "plugins/mein/meinConfigScript.js"]
```

## 4. Plugin-Klasse programmieren

* Die Klasse `PluginDemo` übernehmen oder eine eigene Klasse mit denselben Methoden schreiben:
  `__init__(name, params)`, `get_help`, `plugin_general_info`, `get_image_base64`, `get_image_url`, `get_html`, `get_angabe`, `score`.
* Der Konstruktor wertet den Konfigurationsstring aus (im Demo durch `;` getrennt).
* Endpunkte, die im Demo feste Antworten liefern (z.B. `maxima`, `generatedatasets`, `renderlatex`), in `mount_internal_open` auf eigene
  Methoden der Plugin-Klasse umstellen, wenn das Plugin sie braucht. Was jeder Endpunkt liefern soll, steht in der
  [REST-Schnittstelle des Java-Plugins](../../referenz-plugin-java/rest-schnittstelle/index.md).
* Den Eintrag in `/open/imagetemplates` anpassen – dort ist der PIG-Tag fest eingetragen.

## 5. Plugin registrieren

```python
REGISTERED_PLUGINS: Dict[str, str] = {
    CONF_PLUGIN: "Mein Plugin",
}

def create_plugin(typ: str, name: str, params: str) -> Optional[PluginDemo]:
    if typ == CONF_PLUGIN:
        return PluginDemo(name, params)
    return None
```

Für mehrere Plugins in einem Service weitere Einträge in `REGISTERED_PLUGINS` und weitere Fälle in `create_plugin` ergänzen.
Die `CONF_*`-Konstanten gelten dann für alle Plugins des Services; Werte, die je Plugin verschieden sind, in die Plugin-Klasse verlegen.

## 6. Ressourcen anlegen

* Verzeichnis `resources/plugins/<plugin>/` mit Hilfedatei (HTML) und JavaScript-Dateien.
* Der Quelltext der JavaScript-Dateien wird in `PluginGeneralInfo.javascriptLibrariesLocal` an LeTTo übergeben.
* Für die JavaScript-Schnittstelle (Init- und Konfigurations-Methode, vorgegebene `div`- und Input-Elemente) gelten dieselben Regeln wie beim Java-Plugin –
  siehe [Eigenes Plugin erstellen (Java)](../../referenz-plugin-java/eigenes-plugin/index.md).

## 7. Testen, bauen, deployen

* Tests ohne Docker: `pip install -r requirements-dev.txt` und `python -m pytest`.
* Build und Installation am Entwicklungsrechner mit `build.bat`, Proxy-Konfiguration einspielen – siehe [Build und Deployment](../build-deployment/index.md).
* Mit dem Plugintester (`https://<servername>/plugintester`) und im Debugger testen.

[Referenz-Plugin (Python)](../index.md)
