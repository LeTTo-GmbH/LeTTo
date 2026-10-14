# Architektur des Referenz-Plugins
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

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
| `at.letto.plugins.controller` | REST-Controller: [`ApiController`](../rest-schnittstelle/ApiController/index.md), [`ApiExternOpenController`](../rest-schnittstelle/ApiExternOpenController/index.md), [`ConfigHttpController`](../rest-schnittstelle/ConfigHttpController/index.md), [`InfoController`](../rest-schnittstelle/InfoController/index.md), [`HelpController`](../rest-schnittstelle/HelpController/index.md) |
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
| `/open/...` | [`ApiController`](../rest-schnittstelle/ApiController/index.md) | nur im Docker-Netzwerk (interne URI `http://letto-<endpoint>.nw-letto:8080/open`) |
| [`/ping`](../rest-schnittstelle/InfoController/ping/index.md), [`/info`](../rest-schnittstelle/InfoController/info/index.md), [`/version`](../rest-schnittstelle/InfoController/version/index.md) | [`InfoController`](../rest-schnittstelle/InfoController/index.md) | nur im Docker-Netzwerk |
| `/<endpoint>/api/open/...` | [`ApiExternOpenController`](../rest-schnittstelle/ApiExternOpenController/index.md) | extern über den Proxy |
| `/<endpoint>/open/...` | [`InfoController`](../rest-schnittstelle/InfoController/index.md), [`ConfigHttpController`](../rest-schnittstelle/ConfigHttpController/index.md), statische Dateien | extern über den Proxy |
| [`/<endpoint>/`](../rest-schnittstelle/HelpController/help/index.md), [`/<endpoint>/help`](../rest-schnittstelle/HelpController/help/index.md) | [`HelpController`](../rest-schnittstelle/HelpController/index.md) | extern über den Proxy |
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

1. LeTTo fragt die allgemeinen Plugin-Informationen ab ([`/open/generalinfolist`](../rest-schnittstelle/ApiController/pluginGeneralInfoList/index.md) bzw. [`/open/generalinfo`](../rest-schnittstelle/ApiController/pluginGeneralInfo/index.md)), u.a. Name der
   JavaScript-Init-Methode und die JavaScript-Libraries.
2. Für die Darstellung einer Frage ruft LeTTo [`/open/loadplugindto`](../rest-schnittstelle/ApiController/loadPluginDto/index.md) auf. Das Plugin liefert ein [`PluginDto`](../dtos/PluginDto/index.md) (Bild als URL
   oder Base64, Größe, Tag-Name, Parameter).
3. Im Browser wird die Init-Methode des Plugins (`initPluginJS`, beim Uhr-Plugin `initPluginUhr1(dtoString, active)`) mit dem
   [`PluginDto`](../dtos/PluginDto/index.md) als JSON aufgerufen. Das Plugin zeichnet in das `div` `#<tagName>_div` und schreibt die Eingabe in das versteckte
   Feld `.<tagName>_inp`.
4. Die Schülereingabe wird über [`/open/score`](../rest-schnittstelle/ApiController/score/index.md) bewertet; das Plugin liefert ein [`PluginScoreInfoDto`](../dtos/PluginScoreInfoDto/index.md).
5. Für Druck und Ergebnisansicht gibt es [`/open/renderlatex`](../rest-schnittstelle/ApiController/renderLatex/index.md) und [`/open/renderpluginresult`](../rest-schnittstelle/ApiController/renderPluginResult/index.md).

### Konfigurationsdialog

* Der Modus wird vom Plugin in [`PluginConfigurationInfoDto.configurationMode`](../dtos/PluginConfigurationInfoDto/index.md) festgelegt:

| Konstante | Wert | Bedeutung |
|---|---|---|
| `CONFIGMODE_STRING` | 0 | kein Dialog, nur der Konfigurationsstring |
| `CONFIGMODE_JSF` | 1 | Konfiguration über eine JSF-Seite im Edit-Service |
| `CONFIGMODE_JAVASCRIPT` | 2 | Konfiguration über eine JavaScript-Funktion des Plugins |
| `CONFIGMODE_URL` | 3 | Dialog in einem iframe oder Browser-Tab, vom Plugin-Service über eine URL bereitgestellt |

* [`/open/configurationinfo`](../rest-schnittstelle/ApiController/configurationInfo/index.md) legt eine Konfigurationssitzung ([`PluginConfigurationConnection`](../dtos/PluginConfigurationConnection/index.md)) mit der `configurationID` an.
  Die Konfiguration ist **nicht zustandslos** – `typ`, `name` und `config` werden in der Sitzung gespeichert.
  Ohne `configurationID` erzeugt der Service eine zufällige ID.
* Sitzungen werden nach Ablauf von `timeout` Sekunden ohne Zugriff entfernt.
* [`/open/setconfigurationdata`](../rest-schnittstelle/ApiController/setConfigurationData/index.md) übergibt Konfiguration und Frage; das Plugin liefert ein [`PluginConfigDto`](../dtos/PluginConfigDto/index.md) für das JavaScript.
* Im Modus `CONFIGMODE_URL` liefert `/<endpoint>/open/confighttp?typ=..&configurationID=..` die HTML-Seite des Dialogs;
  die URL steht in [`PluginConfigurationInfoDto.configurationUrl`](../dtos/PluginConfigurationInfoDto/index.md).
* Die Vorschau im Dialog holt per Ajax ein neues [`PluginDto`](../dtos/PluginDto/index.md) über [`/<endpoint>/api/open/reloadplugindto`](../rest-schnittstelle/ApiExternOpenController/reloadPluginDto/index.md) (URL in
  [`PluginConfigDto.pluginDtoUri`](../dtos/PluginConfigDto/index.md)); dabei wird die Konfiguration der Sitzung aktualisiert.
* LeTTo holt das Ergebnis mit [`/open/getconfiguration`](../rest-schnittstelle/ApiController/getConfiguration/index.md) ab.

[Referenz-Plugin (Java)](../index.md)
