# REST-Schnittstelle des Referenz-Plugins (Python)
<!-- erstellt aus plugin-demo-python @ 7902099 (revision 1000) – bei Änderungen im Plugin-Repo nachziehen -->

* Die Python-Version bietet dieselben Pfade, Request- und Response-DTOs wie das Java-Plugin. Jeder Endpunkt verlinkt unten auf seine
  ausführliche Beschreibung in der [REST-Schnittstelle des Java-Plugins](../../referenz-plugin-java/rest-schnittstelle/index.md);
  die Spalte „Python" nennt, was die Python-Version tatsächlich liefert.
* `<servicepath>` ist der Servicepfad des Plugins (Standard `/plugindemopython`).
* Die Swagger-UI des laufenden Services liegt unter `<servicepath>/docs`; jeder Endpunkt verlinkt dort ebenfalls auf die Java-Doku.
* Unbekannter Plugin-Typ: Die Python-Version antwortet **nicht** mit 404 wie das Java-Plugin, sondern mit HTTP 200 und einem leeren Ergebnis (siehe Tabelle).

## Plugin-API – `/open` und `<servicepath>/open`

Die interne Plugin-API steht zweimal zur Verfügung: unter `/open/...` (nur Docker-Netzwerk, wird von LeTTo verwendet) und
zusätzlich unter `<servicepath>/open/...` (über den Proxy erreichbar).

| Methode | Pfad | Request | Response | Python | Java-Doku |
|---|---|---|---|---|---|
| GET | `/open/pluginlist` | – | `List<String>` | Liste der registrierten Typen (`UhrPy`) | [pluginList](../../referenz-plugin-java/rest-schnittstelle/ApiController/pluginList/index.md) |
| GET | `/open/generalinfolist` | – | [PluginGeneralInfoList](../../referenz-plugin-java/dtos/PluginGeneralInfoList/index.md) | allgemeine Informationen aller Plugins | [pluginGeneralInfoList](../../referenz-plugin-java/rest-schnittstelle/ApiController/pluginGeneralInfoList/index.md) |
| POST | `/open/generalinfo` | `String` (Plugin-Typ) | [PluginGeneralInfo](../../referenz-plugin-java/dtos/PluginGeneralInfo/index.md) | unbekannter Typ: `PluginGeneralInfo` nur mit `typ` statt 404 | [pluginGeneralInfo](../../referenz-plugin-java/rest-schnittstelle/ApiController/pluginGeneralInfo/index.md) |
| POST | `/open/gethtml` | [PluginRequestDto](../../referenz-plugin-java/dtos/PluginRequestDto/index.md) | `String` | fester HTML-Hinweis; unbekannter Typ: `""` | [getHtml](../../referenz-plugin-java/rest-schnittstelle/ApiController/getHtml/index.md) |
| POST | `/open/angabe` | [PluginRequestDto](../../referenz-plugin-java/dtos/PluginRequestDto/index.md) | `String` | fester Angabetext; unbekannter Typ: `""` | [getAngabe](../../referenz-plugin-java/rest-schnittstelle/ApiController/getAngabe/index.md) |
| POST | `/open/generatedatasets` | [PluginRequestDto](../../referenz-plugin-java/dtos/PluginRequestDto/index.md) | [PluginDatasetListDto](../../referenz-plugin-java/dtos/PluginDatasetListDto/index.md) | immer leere Liste | [generateDatasets](../../referenz-plugin-java/rest-schnittstelle/ApiController/generateDatasets/index.md) |
| POST | `/open/maxima` | [PluginRequestDto](../../referenz-plugin-java/dtos/PluginRequestDto/index.md) | `String` | immer `""` | [getMaxima](../../referenz-plugin-java/rest-schnittstelle/ApiController/getMaxima/index.md) |
| POST | `/open/image` | [PluginRequestDto](../../referenz-plugin-java/dtos/PluginRequestDto/index.md) | [ImageBase64Dto](../../referenz-plugin-java/dtos/ImageBase64Dto/index.md) | Uhrblatt 320 × 320 Pixel, `params` werden nicht ausgewertet; unbekannter Typ: `error = "unknown plugin"` | [getImage](../../referenz-plugin-java/rest-schnittstelle/ApiController/getImage/index.md) |
| POST | `/open/imagetemplates` | [PluginRequestDto](../../referenz-plugin-java/dtos/PluginRequestDto/index.md) | `List<String[]>` | fest `[["default", "[PIG PluginVomTester \"\"]", "Uhrblatt"]]` – der Plugin-Name im PIG-Tag ist fest eingetragen | [getImageTemplates](../../referenz-plugin-java/rest-schnittstelle/ApiController/getImageTemplates/index.md) |
| POST | `/open/parserplugin` | [PluginParserRequestDto](../../referenz-plugin-java/dtos/PluginParserRequestDto/index.md) | [CalcErgebnisDto](../../referenz-plugin-java/dtos/CalcErgebnisDto/index.md) | `CalcErgebnisDto` mit `string = null`, `type = "STRING"` (Java: `null`) | [parserPlugin](../../referenz-plugin-java/rest-schnittstelle/ApiController/parserPlugin/index.md) |
| POST | `/open/parserplugineinheit` | [PluginEinheitRequestDto](../../referenz-plugin-java/dtos/PluginEinheitRequestDto/index.md) | `String` | immer `""` (Java: `null`) | [parserPluginEinheit](../../referenz-plugin-java/rest-schnittstelle/ApiController/parserPluginEinheit/index.md) |
| POST | `/open/score` | [PluginScoreRequestDto](../../referenz-plugin-java/dtos/PluginScoreRequestDto/index.md) | [PluginScoreInfoDto](../../referenz-plugin-java/dtos/PluginScoreInfoDto/index.md) | Bewertung, siehe [Plugin-API](../plugin-api/index.md); unbekannter Typ: leeres `PluginScoreInfoDto` | [score](../../referenz-plugin-java/rest-schnittstelle/ApiController/score/index.md) |
| POST | `/open/getvars` | [PluginRequestDto](../../referenz-plugin-java/dtos/PluginRequestDto/index.md) | `List<String>` | immer `[]` (Java: `null`) | [getVars](../../referenz-plugin-java/rest-schnittstelle/ApiController/getVars/index.md) |
| POST | `/open/modifyangabe` | [PluginAngabeRequestDto](../../referenz-plugin-java/dtos/PluginAngabeRequestDto/index.md) | `String` | `text` unverändert | [modifyAngabe](../../referenz-plugin-java/rest-schnittstelle/ApiController/modifyAngabe/index.md) |
| POST | `/open/modifyangabetextkomplett` | [PluginAngabeRequestDto](../../referenz-plugin-java/dtos/PluginAngabeRequestDto/index.md) | `String` | `text` unverändert | [modifyAngabeTextkomplett](../../referenz-plugin-java/rest-schnittstelle/ApiController/modifyAngabeTextkomplett/index.md) |
| POST | `/open/updatepluginstringjavascript` | [PluginUpdateJavascriptRequestDto](../../referenz-plugin-java/dtos/PluginUpdateJavascriptRequestDto/index.md) | `String` | `pluginDef` unverändert | [updatePluginstringJavascript](../../referenz-plugin-java/rest-schnittstelle/ApiController/updatePluginstringJavascript/index.md) |
| POST | `/open/loadplugindto` | [LoadPluginRequestDto](../../referenz-plugin-java/dtos/LoadPluginRequestDto/index.md) | [PluginDto](../../referenz-plugin-java/dtos/PluginDto/index.md) | Bild als `data:image/png;base64,…`, `tagName = <frageId>_<name>_<nr>`, Größe aus `CONF_width`/`CONF_height`; unbekannter Typ: leeres `PluginDto` | [loadPluginDto](../../referenz-plugin-java/rest-schnittstelle/ApiController/loadPluginDto/index.md) |
| POST | `/open/renderlatex` | [PluginRenderLatexRequestDto](../../referenz-plugin-java/dtos/PluginRenderLatexRequestDto/index.md) | [PluginRenderDto](../../referenz-plugin-java/dtos/PluginRenderDto/index.md) | immer leeres `PluginRenderDto` | [renderLatex](../../referenz-plugin-java/rest-schnittstelle/ApiController/renderLatex/index.md) |
| POST | `/open/renderpluginresult` | [PluginRenderResultRequestDto](../../referenz-plugin-java/dtos/PluginRenderResultRequestDto/index.md) | [PluginRenderDto](../../referenz-plugin-java/dtos/PluginRenderDto/index.md) | HTML: Hinweis von `get_html` plus `Wert:<antwort>`; bei `tex = true` leer | [renderPluginResult](../../referenz-plugin-java/rest-schnittstelle/ApiController/renderPluginResult/index.md) |
| POST | `/open/configurationinfo` | [PluginConfigurationInfoRequestDto](../../referenz-plugin-java/dtos/PluginConfigurationInfoRequestDto/index.md) | [PluginConfigurationInfoDto](../../referenz-plugin-java/dtos/PluginConfigurationInfoDto/index.md) | legt nur mit `configurationID` eine Sitzung an; `configurationUrl` bleibt leer; unbekannter Typ: `configurationMode = 0` | [configurationInfo](../../referenz-plugin-java/rest-schnittstelle/ApiController/configurationInfo/index.md) |
| POST | `/open/setconfigurationdata` | [PluginSetConfigurationDataRequestDto](../../referenz-plugin-java/dtos/PluginSetConfigurationDataRequestDto/index.md) | [PluginConfigDto](../../referenz-plugin-java/dtos/PluginConfigDto/index.md) | `params` enthält `config`, `help` und `vars`; ohne Sitzung `errorMsg = "configurationID unknown or expired"` | [setConfigurationData](../../referenz-plugin-java/rest-schnittstelle/ApiController/setConfigurationData/index.md) |
| POST | `/open/getconfiguration` | [PluginConfigurationRequestDto](../../referenz-plugin-java/dtos/PluginConfigurationRequestDto/index.md) | `String` | Konfiguration der Sitzung; ohne Sitzung `""` (Java: `@Error:…`) | [getConfiguration](../../referenz-plugin-java/rest-schnittstelle/ApiController/getConfiguration/index.md) |
| POST | `/open/reloadplugindto` | [LoadPluginRequestDto](../../referenz-plugin-java/dtos/LoadPluginRequestDto/index.md) | [PluginDto](../../referenz-plugin-java/dtos/PluginDto/index.md) | siehe unten | [reloadPluginDto](../../referenz-plugin-java/rest-schnittstelle/ApiController/reloadPluginDto/index.md) |

### reloadplugindto

* Mit gültiger `configurationID` werden Typ, Name und Frage aus der Sitzung genommen. Schickt der Request ein `config`-Feld mit,
  hat es Vorrang und wird in der Sitzung gespeichert (aktuelle Eingabe im Dialog); sonst gilt die Konfiguration der Sitzung.
* Ohne gültige Sitzung werden die Werte aus dem Request verwendet – kein 404 wie in Java.
* Das `PluginDto` enthält in `params` den Eintrag `config`.

## Offene API – `<servicepath>/api/open`

Für den Browser, über den Proxy erreichbar (wie der `ApiExternOpenController` in Java).

| Methode | Pfad | Request | Response | Java-Doku |
|---|---|---|---|---|
| GET | `<servicepath>/api/open/pluginlist` | – | `List<String>` | [pluginList](../../referenz-plugin-java/rest-schnittstelle/ApiExternOpenController/pluginList/index.md) |
| GET | `<servicepath>/api/open/generalinfolist` | – | [PluginGeneralInfoList](../../referenz-plugin-java/dtos/PluginGeneralInfoList/index.md) | [pluginGeneralInfoList](../../referenz-plugin-java/rest-schnittstelle/ApiExternOpenController/pluginGeneralInfoList/index.md) |
| POST | `<servicepath>/api/open/generalinfo` | `String` (Plugin-Typ) | [PluginGeneralInfo](../../referenz-plugin-java/dtos/PluginGeneralInfo/index.md) | [pluginGeneralInfo](../../referenz-plugin-java/rest-schnittstelle/ApiExternOpenController/pluginGeneralInfo/index.md) |
| POST | `<servicepath>/api/open/reloadplugindto` | [LoadPluginRequestDto](../../referenz-plugin-java/dtos/LoadPluginRequestDto/index.md) | [PluginDto](../../referenz-plugin-java/dtos/PluginDto/index.md) | [reloadPluginDto](../../referenz-plugin-java/rest-schnittstelle/ApiExternOpenController/reloadPluginDto/index.md) |

Das Verhalten entspricht den gleichnamigen Endpunkten unter `/open`.

## Info-Endpunkte

| Methode | Pfad | Response | erreichbar | Java-Doku |
|---|---|---|---|---|
| GET | `/ping` | `pong` | intern (Docker-Healthcheck) | [ping](../../referenz-plugin-java/rest-schnittstelle/InfoController/ping/index.md) |
| GET | `<servicepath>/ping` | `pong` | extern, nur in Python | [ping](../../referenz-plugin-java/rest-schnittstelle/InfoController/ping/index.md) |
| GET | `<servicepath>/open/ping` | `pong` | extern | [pingopen](../../referenz-plugin-java/rest-schnittstelle/InfoController/pingopen/index.md) |
| GET | `/info` | [ServiceInfoDTO](../../referenz-plugin-java/dtos/ServiceInfoDTO/index.md) | intern | [info](../../referenz-plugin-java/rest-schnittstelle/InfoController/info/index.md) |
| GET | `<servicepath>/open/info` | [ServiceInfoDTO](../../referenz-plugin-java/dtos/ServiceInfoDTO/index.md) | extern | [infoOpen](../../referenz-plugin-java/rest-schnittstelle/InfoController/infoOpen/index.md) |
| GET | `/version` | `1.0` | intern | [version](../../referenz-plugin-java/rest-schnittstelle/InfoController/version/index.md) |

`ServiceInfoDTO` enthält in der Python-Version nur Name, Version, Autor, Startzeit (Zeitpunkt der Anfrage) und ein `AdminInfoDto` mit dem Anwendungsnamen – siehe [DTOs](../dtos/index.md).

## Hilfe und Dokumentation

| Pfad | Inhalt |
|---|---|
| `<servicepath>/`, `<servicepath>/index.html`, `<servicepath>/help` | Hilfeseite aus `resources/index.html` (erscheint nicht in der Swagger-UI) |
| `<servicepath>/docs` | Swagger-UI, Endpunkte und Schemas alphabetisch sortiert, mit Links zur Java-Doku |
| `<servicepath>/openapi.json` | OpenAPI-Beschreibung |

## Nicht vorhanden

* `confighttp` – der Konfigurationsdialog im iframe (`CONFIGMODE_URL`) ist nicht implementiert, siehe [ConfigHttpController](../../referenz-plugin-java/rest-schnittstelle/ConfigHttpController/index.md) in Java.

## Registrierung am Setup-Service (ausgehend)

| Methode | Pfad am Setup-Service | Request | Authentifizierung |
|---|---|---|---|
| POST | `/config/auth/user/registerplugin` | JSON-Objekt mit den Feldern von [ConfigServiceDto](../../referenz-plugin-java/dtos/ConfigServiceDto/index.md) | Basic Auth (Benutzer `user`, Passwort aus `letto_user_user_password`) |

Die Antwort wird nicht ausgewertet; jede Antwort mit HTTP 2xx gilt als erfolgreich. Siehe [Build und Deployment](../build-deployment/index.md#registrierung-am-letto-server).

[Referenz-Plugin (Python)](../index.md)
