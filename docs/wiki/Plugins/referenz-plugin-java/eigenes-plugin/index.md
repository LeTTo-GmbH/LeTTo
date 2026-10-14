# Eigenes Plugin erstellen
<!-- generiert aus plugin-demo-java @ f0143d1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

## Voraussetzungen

* Java 25 (JDK), Maven (oder der Maven-Wrapper `mvnw` des Projekts), Docker
* Eine LeTTo-Installation am Entwicklungsrechner (Compose-Verzeichnis `/opt/letto/docker/compose/letto`, Proxy `letto-proxy`)
* Unter Windows: `setpluginname.bat` verwendet PowerShell und `dos2unix`

## 1. Demoprojekt auschecken

```bash
git clone https://github.com/LeTTo-GmbH/plugin-demo-java.git
```

## 2. Endpoint-Pfad festlegen

Der Endpoint-Pfad ist der öffentliche Pfad des Plugins direkt nach dem Servernamen, z.B. `https://servername/pluginuhr/`.
Er muss am Zielserver eindeutig sein.

```bash
build\setpluginname.bat pluginuhr
```

Das Script (nur Windows) führt folgende Schritte aus:

| Ziel | Änderung |
|---|---|
| `src/main/resources/application.properties` | neu aus `build/templates`, `plugindemo` durch den Endpoint ersetzt (Swagger-Pfade, Anwendungsname) |
| `yml/docker-service-plugin.yml` | neu aus `build/templates`, `plugindemo`/`PLUGINDEMO` ersetzt (Image, Container, Umgebungsvariablen) |
| `src/main/resources/static/<endpoint>/open/` | neu aus `build/templates/open` (CSS, JS, Fonts, Bilder) und `head_include.html` |
| `config/Endpoint.java` | `servicepath = "/<endpoint>"` |
| `config/PluginConfiguration.java` | `PLUGIN_NAME = "letto-<endpoint>"`, Default für Netzwerkadresse und Containername, interne URI `http://letto-<endpoint>.nw-letto:8080` |
| `controller/ApiController.java` | JavaDoc-Link in der Swagger-Beschreibung |
| `build/vars.bat` | `urlpath=<endpoint>` (wird von `build.bat` und `build.sh` gelesen) |
| `proxy/<endpoint>.conf` | Verzeichnis `proxy` wird neu erzeugt, enthält die nginx-Konfiguration |

Achtung: Das Script entfernt `src/main/resources/static` mit `git rm -r` und legt es neu an.

## 3. Plugin-Klasse erstellen

* Neue Klasse im Paket `at.letto.plugins.plugin` (z.B. `at.letto.plugins.plugin.meinplugin.PluginMein`), die von `BasePlugin` erbt.
* Der Konstruktor muss die Signatur `(String name, String params)` haben – das Plugin wird per Reflection erzeugt.
  Beim Registrieren wird er mit `name=""` und `params=""` aufgerufen und muss dabei alle Standardwerte korrekt setzen.
* Die abstrakte Methode `paint(Graphics2D g,` [`PluginImageResultDto`](../dtos/PluginImageResultDto/index.md) `r)` muss implementiert werden.
* Details siehe [Plugin-API](../plugin-api/index.md).

```java
public class PluginMein extends BasePlugin {
    public PluginMein(String name, String params) {
        super(name, params);
        version        = "1.0";
        helpfiles      = new String[]{"plugins/mein/Mein.html"};
        javascriptLibs = new String[]{"plugins/mein/meinScript.js"};
        javaScript     = true;
        initPluginJS   = "initPluginMein";
        // params auswerten ...
    }

    @Override
    public void paint(Graphics2D g, PluginImageResultDto r) {
        // Bild zeichnen (width x height)
    }
}
```

## 4. Plugin registrieren

In `config/StartupConfiguration.java` den Plugin-Typ mit Name und vollständigem Klassennamen registrieren:

```java
pluginConfiguration.registerPlugin("Mein", "at.letto.plugins.plugin.meinplugin.PluginMein");
```

* Der Name (Typ) ist der Plugin-Typ, mit dem das Plugin in LeTTo angesprochen wird.
* Das Uhr-Plugin (`Uhr1`) aus der Registrierung entfernen.

## 5. Ressourcen anlegen

* Verzeichnis `src/main/resources/plugins/<plugin>/` anlegen (ein Verzeichnis je Plugin).
* Darin:
  * Hilfedatei(en) als HTML – nur der Inhalt von `<body>` wird verwendet. Der Platzhalter `{% raw %}{{servicepath}}{% endraw %}` wird durch den Endpoint-Pfad ersetzt (z.B. für Links zur Swagger-UI).
  * JavaScript-Dateien für die interaktive Eingabe und den Konfigurationsdialog. Sie werden als Quelltext an LeTTo übergeben (`javascriptLibrariesLocal()`).
* Pfade in `helpfiles` und `javascriptLibs` relativ zum Klassenpfad angeben, z.B. `plugins/uhr/uhr1Script.js`.

### JavaScript-Schnittstelle

| Funktion | Aufruf | Vorgaben von LeTTo |
|---|---|---|
| Init-Methode (`initPluginJS`) | `initPluginUhr1(dtoString, active)` – `dtoString` ist das [`PluginDto`](../dtos/PluginDto/index.md) als JSON, `active=false` bedeutet keine Eingabe erlaubt (Lösungsansicht) | Ausgabe in das `div` `#<tagName>_div`, Ergebnis in das versteckte Feld `.<tagName>_inp` |
| Konfigurations-Methode (`configPluginJS`) | `configPluginUhr1(dtoString)` – `dtoString` ist das [`PluginConfigDto`](../dtos/PluginConfigDto/index.md) als JSON | Ausgabe in `#configform_div`, Ergebnis (Konfigurationsstring) in das versteckte Feld `.configform_config` |

* Alle Hilfsfunktionen als innere Funktionen der Init- bzw. Konfigurationsmethode anlegen, um Namenskonflikte zu vermeiden.
* jQuery steht zur Verfügung.
* Für die Vorschau im Konfigurationsdialog sendet das Uhr-Plugin per Ajax einen [`LoadPluginRequestDto`](../dtos/LoadPluginRequestDto/index.md) an `dto.pluginDtoUri`
  und ruft mit dem erhaltenen [`PluginDto`](../dtos/PluginDto/index.md) die Init-Methode erneut auf.

## 6. Bauen, deployen, testen

* Build mit `build\build.bat` bzw. `build/build.sh`, Proxy-Konfiguration einspielen – siehe [Build und Deployment](../build-deployment/index.md).
* Testen mit dem Plugintester (`https://<servername>/plugintester`) und im Debugger.

[Referenz-Plugin (Java)](../index.md)
