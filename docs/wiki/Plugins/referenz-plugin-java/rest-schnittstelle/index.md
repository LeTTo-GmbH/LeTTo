# REST-Schnittstelle des Referenz-Plugins
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

* Alle Pfade sind in `at.letto.plugins.config.Endpoint` definiert. `<endpoint>` steht für den Endpoint-Pfad des Plugins (im Demo `plugindemo`).
* Request- und Response-Bodies sind JSON. Die DTOs sind unter [DTOs und Enums](../dtos/index.md) beschrieben.
* Die Swagger-UI des laufenden Services liegt unter `/<endpoint>/swagger-ui.html`; die Beschreibungen dort stammen aus der JavaDoc.
* Kann ein Plugin-Typ nicht erzeugt werden, antworten die Plugin-Endpunkte mit HTTP 404.
* Die meisten Request-DTOs enthalten `typ`, `name` und `config`, damit der Service die passende Plugin-Instanz erzeugen kann.

## ApiController – `/open`

Plugin-Schnittstelle zwischen LeTTo und Plugin, nur aus dem Docker-Netzwerk erreichbar
(z.B. `http://letto-plugindemo.nw-letto:8080/open/...`).

| Methode | Pfad | Request | Response | Beschreibung |
|---|---|---|---|---|
| GET | `/open/pluginlist` | – | `List<String>` | Liste aller Plugin-Typen dieses Services |
| GET | `/open/generalinfolist` | – | `PluginGeneralInfoList` | allgemeine Informationen aller Plugins des Services |
| POST | `/open/generalinfo` | `String` (Plugin-Typ) | `PluginGeneralInfo` | allgemeine Informationen zu einem Plugin; 404 wenn der Typ nicht registriert ist |
| POST | `/open/gethtml` | `PluginRequestDto` | `String` | HTML-Fragetext für einen PIT-Tag |
| POST | `/open/angabe` | `PluginRequestDto` | `String` | Angabetext für das Textfeld der Frage |
| POST | `/open/generatedatasets` | `PluginRequestDto` | `PluginDatasetListDto` | Datensätze, die das Plugin in der Frage benötigt |
| POST | `/open/maxima` | `PluginRequestDto` (mit `pluginMaximaCalcMode`) | `String` | Maxima-Berechnungsstring |
| POST | `/open/image` | `PluginRequestDto` | `ImageBase64Dto` | Bild Base64-codiert |
| POST | `/open/imagetemplates` | `PluginRequestDto` | `Vector<String[]>` | Bildvarianten: [0] Beschreibung, [1] PIG-Tag, [2] Hilfetext |
| POST | `/open/parserplugin` | `PluginParserRequestDto` | `CalcErgebnisDto` | Funktion `plugin("name",p1,p2,…)` im Lösungsfeld |
| POST | `/open/parserplugineinheit` | `PluginEinheitRequestDto` | `String` | Recheneinheit des Ergebnisses von `parserplugin` |
| POST | `/open/score` | `PluginScoreRequestDto` | `PluginScoreInfoDto` | Bewertung der Schülereingabe |
| POST | `/open/getvars` | `PluginRequestDto` | `Vector<String>` | Variablen, die als Dataset benötigt werden |
| POST | `/open/modifyangabe` | `PluginAngabeRequestDto` | `String` | verändert einen Text in PI-Tags vor dem Darstellen der Frage |
| POST | `/open/modifyangabetextkomplett` | `PluginAngabeRequestDto` | `String` | verändert den gesamten Angabetext vor dem Darstellen der Frage |
| POST | `/open/updatepluginstringjavascript` | `PluginUpdateJavascriptRequestDto` | `String` | passt die Plugindefinition an das JavaScript-Ergebnis an |
| POST | `/open/loadplugindto` | `LoadPluginRequestDto` | `PluginDto` | rendert das Plugin-Bild und baut das DTO für das JavaScript |
| POST | `/open/renderlatex` | `PluginRenderLatexRequestDto` | `PluginRenderDto` | LaTeX-Quelltext für den Fragedruck |
| POST | `/open/renderpluginresult` | `PluginRenderResultRequestDto` | `PluginRenderDto` | HTML- oder LaTeX-Code mit Schülereingabe und Lösung |
| POST | `/open/configurationinfo` | `PluginConfigurationInfoRequestDto` | `PluginConfigurationInfoDto` | startet eine Konfigurationssitzung; setzt `configurationUrl` auf `<uri.extern>/<endpoint>/open/confighttp?typ=..&configurationID=..` |
| POST | `/open/setconfigurationdata` | `PluginSetConfigurationDataRequestDto` | `PluginConfigDto` | übergibt Konfiguration und Frage an die Sitzung; setzt `pluginDtoUri` auf den externen `reloadplugindto`-Endpunkt |
| POST | `/open/getconfiguration` | `PluginConfigurationRequestDto` | `String` | aktuelle Konfiguration oder `@Error: …` |
| POST | `/open/reloadplugindto` | `LoadPluginRequestDto` (mit `configurationID`) | `PluginDto` | neues `PluginDto` innerhalb einer Konfigurationssitzung, aktualisiert deren Konfiguration; 404 ohne gültige Sitzung |

### Konfigurationssitzung

* `configurationinfo` muss vor `setconfigurationdata`, `getconfiguration`, `reloadplugindto` und `confighttp` aufgerufen werden.
* Die `configurationID` muss für jeden Konfigurationsdialog eindeutig sein und dient an den offenen Endpunkten als Authentifizierung.
* Die Sitzung wird nach `timeout` Sekunden ohne Zugriff entfernt.

## ApiExternOpenController – `/<endpoint>/api/open`

Offene Endpunkte, die über den Proxy von extern erreichbar sind (Ajax aus dem Browser). Sie delegieren an den `ApiController`.

| Methode | Pfad | Request | Response | Beschreibung |
|---|---|---|---|---|
| GET | `/<endpoint>/api/open/pluginlist` | – | `List<String>` | Liste aller Plugin-Typen |
| GET | `/<endpoint>/api/open/generalinfolist` | – | `PluginGeneralInfoList` | allgemeine Informationen aller Plugins |
| POST | `/<endpoint>/api/open/generalinfo` | `String` (Plugin-Typ) | `PluginGeneralInfo` | allgemeine Informationen zu einem Plugin |
| POST | `/<endpoint>/api/open/reloadplugindto` | `LoadPluginRequestDto` (mit `configurationID`) | `PluginDto` | Vorschau im Konfigurationsdialog |

## ConfigHttpController

| Methode | Pfad | Parameter | Response | Beschreibung |
|---|---|---|---|---|
| GET | `/<endpoint>/open/confighttp` | `typ`, `configurationID` (Query) | HTML | Konfigurationsdialog im Modus `CONFIGMODE_URL` für iframe oder Browser-Tab |

* Die Seite bindet jQuery und die lokalen JavaScript-Libraries des Plugins ein und ruft die Konfigurations-Methode
  (`javaScriptMethode`) mit dem `PluginConfigDto` als JSON auf.
* Antwortet mit 404, wenn die Sitzung fehlt oder abgelaufen ist, und mit 500, wenn das Plugin keine gültige Konfigurations-Methode angibt.

## InfoController

| Methode | Pfad | Response | erreichbar | Beschreibung |
|---|---|---|---|---|
| GET | `/ping` | `String` `pong` | intern | Erreichbarkeit (wird vom Docker-Healthcheck verwendet) |
| GET | `/<endpoint>/open/ping` | `String` `pong` | extern | Erreichbarkeit über den Proxy |
| GET | `/info` | `ServiceInfoDTO` | intern | Informationen über den laufenden Service |
| GET | `/<endpoint>/open/info` | `ServiceInfoDTO` | extern | Informationen über den laufenden Service |
| GET | `/version` | `String` | intern | Version des Services |

## HelpController

| Methode | Pfad | Response | Beschreibung |
|---|---|---|---|
| GET | `/<endpoint>`, `/<endpoint>/`, `/<endpoint>/index.html`, `/<endpoint>/help` | HTML | Hilfeseite des Services mit Links zu Swagger-UI, JavaDoc und OpenAPI-JSON |

Die Seite liegt in `src/main/resources/help/index.html`; die Platzhalter `{{servicepath}}`, `{{name}}` und `{{version}}` werden ersetzt.

## Registrierung am Setup-Service (ausgehend)

| Methode | Pfad am Setup-Service | Request | Response | Authentifizierung |
|---|---|---|---|---|
| POST | `/config/auth/user/registerplugin` | `ConfigServiceDto` | `RegisterServiceResultDto` | Basic Auth (`letto.user.user.name` / `letto.user.user.password`) |

Siehe [Build und Deployment](../build-deployment/index.md#registrierung-am-letto-server).

## Offene Punkte im Code

* In `Endpoint` sind `getImageUrl` (`/imageurl`) und `EXTERN_API` (`/<endpoint>/auth/user`) definiert, aber kein Controller stellt
  Endpunkte darunter bereit. `EXTERN_API` wird nur als externe URI an das Setup-Service gemeldet. Im Code nicht dokumentiert, wofür sie vorgesehen sind.

[Referenz-Plugin (Java)](../index.md)
