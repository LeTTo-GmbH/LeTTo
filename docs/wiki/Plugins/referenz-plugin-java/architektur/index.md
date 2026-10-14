# Architektur des Referenz-Plugins
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

## Aufbau des Services

* Spring-Boot-Anwendung, Startklasse `at.letto.plugins.PluginDemoJavaApplication`.
* Der Service läuft im Docker-Container `letto-<endpoint>` im Netzwerk `nw-letto`, intern auf Port 8080.
* Für jede Anfrage von LeTTo wird eine **neue Plugin-Instanz** erzeugt (`PluginConfiguration.createPluginService(typ, name, config)`),
  die Anfragen sind dadurch zustandslos. Ausnahme: der Konfigurationsdialog, dessen Zustand über eine `configurationID` gehalten wird.
* Die Plugin-Typen werden beim Start in der `StartupConfiguration` registriert (Typname → Klassenname).

## Paketstruktur

| Paket / Verzeichnis | Inhalt |
|---|---|
| `at.letto.plugins` | `PluginDemoJavaApplication` – Startklasse |
| `at.letto.plugins.config` | `Endpoint` (alle Pfade), `PluginConfiguration` (Plugin-Verwaltung, Registrierung, Konfigurationssitzungen), `StartupConfiguration` (Registrierung der Plugin-Typen), `PluginRegistrationOnReady` (Registrierung am Setup-Service), `OpenApiConfig` (Swagger) |
| `at.letto.plugins.controller` | REST-Controller: `ApiController`, `ApiExternOpenController`, `ConfigHttpController`, `InfoController`, `HelpController` |
| `at.letto.plugins.dto` | DTOs der REST-Schnittstelle |
| `at.letto.plugins.enums` | Enums der Schnittstelle |
| `at.letto.plugins.plugin` | `PluginService` (Interface), `BasePlugin` (abstrakte Basisklasse) |
| `at.letto.plugins.plugin.uhr` | `PluginUhr` – Beispiel-Plugin |
| `at.letto.plugins.plugin.tools` | `PluginToolsAwt` (Zeichenhilfen), `PluginToolsMath` (Toleranzvergleich) |
| `at.letto.plugins.tools` | Hilfsklassen (Bildablage `BaseImageService`, `JSON`, `Datum`, `PluginResource`, `ServerStatus` u.a.) |
| `src/main/resources/plugins/<plugin>/` | JavaScript- und HTML-Ressourcen je Plugin |
| `src/main/resources/help/index.html` | Hilfeseite des Services |
| `src/main/resources/static/<endpoint>/open/` | statische Dateien (CSS, JS, Bilder, JavaDoc) – wird von `setpluginname.bat` und dem Build erzeugt |

## Erreichbarkeit der Endpunkte

| Basispfad | Controller | erreichbar |
|---|---|---|
| `/open/...` | `ApiController` | nur im Docker-Netzwerk (interne URI `http://letto-<endpoint>.nw-letto:8080/open`) |
| `/ping`, `/info`, `/version` | `InfoController` | nur im Docker-Netzwerk |
| `/<endpoint>/api/open/...` | `ApiExternOpenController` | extern über den Proxy |
| `/<endpoint>/open/...` | `InfoController`, `ConfigHttpController`, statische Dateien | extern über den Proxy |
| `/<endpoint>/`, `/<endpoint>/help` | `HelpController` | extern über den Proxy |
| `/<endpoint>/swagger-ui.html`, `/<endpoint>/v3/api-docs` | springdoc | extern über den Proxy |

Der Proxy leitet nur `/<endpoint>/` an den Container weiter, daher sind die Pfade ohne Endpoint-Präfix von außen nicht erreichbar.

## Ablauf LeTTo-Server ↔ Plugin

```text
[Start]   Plugin-Service --POST /config/auth/user/registerplugin (ConfigServiceDto)--> Setup-Service
          Plugin-Service <------------------------------ RegisterServiceResultDto --- Setup-Service

[Frage]   LeTTo-Server   --POST /open/generalinfolist, /open/loadplugindto ---------> Plugin-Service
          LeTTo-Server   <---------------------- PluginGeneralInfoList, PluginDto --- Plugin-Service
          LeTTo-Server   --HTML + JS-Libraries + PluginDto (JSON) ------------------> Browser: initPluginJS(...)
          LeTTo-Server   --POST /open/score (Schülereingabe) -----------------------> Plugin-Service
          LeTTo-Server   <-------------------------------- PluginScoreInfoDto ------- Plugin-Service

[Konfig]  LeTTo-Server   --POST /open/configurationinfo (configurationID) ----------> Plugin-Service
          LeTTo-Server   --POST /open/setconfigurationdata -------------------------> Plugin-Service
          LeTTo-Server   --PluginConfigDto ------------------------------------------> Browser: configPluginJS(...)
          Browser        --POST /<endpoint>/api/open/reloadplugindto (Vorschau) ----> Plugin-Service (über Proxy)
          LeTTo-Server   --POST /open/getconfiguration -----------------------------> Plugin-Service
```

### Fragedarstellung und Bewertung

1. LeTTo fragt die allgemeinen Plugin-Informationen ab (`/open/generalinfolist` bzw. `/open/generalinfo`), u.a. Name der
   JavaScript-Init-Methode und die JavaScript-Libraries.
2. Für die Darstellung einer Frage ruft LeTTo `/open/loadplugindto` auf. Das Plugin liefert ein `PluginDto` (Bild als URL
   oder Base64, Größe, Tag-Name, Parameter).
3. Im Browser wird die Init-Methode des Plugins (`initPluginJS`, beim Uhr-Plugin `initPluginUhr1(dtoString, active)`) mit dem
   `PluginDto` als JSON aufgerufen. Das Plugin zeichnet in das `div` `#<tagName>_div` und schreibt die Eingabe in das versteckte
   Feld `.<tagName>_inp`.
4. Die Schülereingabe wird über `/open/score` bewertet; das Plugin liefert ein `PluginScoreInfoDto`.
5. Für Druck und Ergebnisansicht gibt es `/open/renderlatex` und `/open/renderpluginresult`.

### Konfigurationsdialog

* Der Modus wird vom Plugin in `PluginConfigurationInfoDto.configurationMode` festgelegt:

| Konstante | Wert | Bedeutung |
|---|---|---|
| `CONFIGMODE_STRING` | 0 | kein Dialog, nur der Konfigurationsstring |
| `CONFIGMODE_JSF` | 1 | Konfiguration über eine JSF-Seite im Edit-Service |
| `CONFIGMODE_JAVASCRIPT` | 2 | Konfiguration über eine JavaScript-Funktion des Plugins |
| `CONFIGMODE_URL` | 3 | Dialog in einem iframe oder Browser-Tab, vom Plugin-Service über eine URL bereitgestellt |

* `/open/configurationinfo` legt eine Konfigurationssitzung (`PluginConfigurationConnection`) mit der `configurationID` an.
  Die Konfiguration ist **nicht zustandslos** – `typ`, `name` und `config` werden in der Sitzung gespeichert.
  Ohne `configurationID` erzeugt der Service eine zufällige ID.
* Sitzungen werden nach Ablauf von `timeout` Sekunden ohne Zugriff entfernt.
* `/open/setconfigurationdata` übergibt Konfiguration und Frage; das Plugin liefert ein `PluginConfigDto` für das JavaScript.
* Im Modus `CONFIGMODE_URL` liefert `/<endpoint>/open/confighttp?typ=..&configurationID=..` die HTML-Seite des Dialogs;
  die URL steht in `PluginConfigurationInfoDto.configurationUrl`.
* Die Vorschau im Dialog holt per Ajax ein neues `PluginDto` über `/<endpoint>/api/open/reloadplugindto` (URL in
  `PluginConfigDto.pluginDtoUri`); dabei wird die Konfiguration der Sitzung aktualisiert.
* LeTTo holt das Ergebnis mit `/open/getconfiguration` ab.

[Referenz-Plugin (Java)](../index.md)
