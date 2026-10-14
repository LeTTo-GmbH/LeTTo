# REST-Schnittstelle des Referenz-Plugins
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

* Alle Pfade sind in `at.letto.plugins.config.Endpoint` definiert. `<endpoint>` steht für den Endpoint-Pfad des Plugins (im Demo `plugindemo`).
* Request- und Response-Bodies sind JSON. Die Datenklassen sind unter [DTOs](../dtos/index.md) und [Enums](../enums/index.md) beschrieben.
* Die Swagger-UI des laufenden Services liegt unter `/<endpoint>/swagger-ui.html`; die Beschreibungen dort stammen aus der JavaDoc.
* Jeder Endpunkt hat eine eigene Seite mit Request-Feldern, Ablauf, Fehlerfällen und Querverweisen.

## Controller

| Controller | Basispfad | Erreichbarkeit | Endpunkte | Zweck |
|---|---|---|---|---|
| [ApiController](ApiController/index.md) | `/open` | nur im Docker-Netzwerk (`http://letto-<endpoint>.nw-letto:8080/open/...`) | 24 | REST-Schnittstelle des Plugins zwischen LeTTo und Plugin (nur aus dem Docker-Netzwerk erreichbar) |
| [ApiExternOpenController](ApiExternOpenController/index.md) | `/<endpoint>/api/open` | extern über den Proxy | 4 | offene Endpoints welche von extern erreichbar sein müssen für ajax und allgemeine Informationen (von extern erreichbar) |
| [ConfigHttpController](ConfigHttpController/index.md) | – | extern über den Proxy | 1 | Liefert den Konfigurationsdialog eines Plugins im Mode CONFIGMODE_URL als HTML-Seite, welche von LeTTo in einem iframe oder Browser-Tab geöffnet wird |
| [HelpController](HelpController/index.md) | – | extern über den Proxy | 1 | Liefert die Hilfeseite des Plugin-Services mit einer kurzen Beschreibung und Links zur JavaDoc und zur Swagger-Dokumentation |
| [InfoController](InfoController/index.md) | – | teils intern, teils extern (siehe Tabelle) | 5 | REST-Endpunkte zur Erreichbarkeit, Version und Laufzeitinformation des Plugin-Services |

## Alle Endpunkte

| Methode | Pfad | Controller | Request | Response | Beschreibung |
|---|---|---|---|---|---|
| GET | [`/open/pluginlist`](ApiController/pluginList/index.md) | [ApiController](ApiController/index.md) | – | List&lt;String&gt; | Liefert eine Liste aller Plugins (Pluginnamen) , welche mit diesem Service verwaltet werden |
| GET | [`/open/generalinfolist`](ApiController/pluginGeneralInfoList/index.md) | [ApiController](ApiController/index.md) | – | [PluginGeneralInfoList](../dtos/PluginGeneralInfoList/index.md) | Liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services |
| POST | [`/open/generalinfo`](ApiController/pluginGeneralInfo/index.md) | [ApiController](ApiController/index.md) | String | [PluginGeneralInfo](../dtos/PluginGeneralInfo/index.md) | Liefert die allgemeinen Konfigurationsinformationen zu einem Plugin |
| POST | [`/open/gethtml`](ApiController/getHtml/index.md) | [ApiController](ApiController/index.md) | [PluginRequestDto](../dtos/PluginRequestDto/index.md) | String | Berechnet den Fragetext für das Fragefeld des Webservers für die angegebenen Parameter für die Verwendung in einem PIT Tag |
| POST | [`/open/angabe`](ApiController/getAngabe/index.md) | [ApiController](ApiController/index.md) | [PluginRequestDto](../dtos/PluginRequestDto/index.md) | String | Liefert einen Angabestring für die Text-Angabe |
| POST | [`/open/generatedatasets`](ApiController/generateDatasets/index.md) | [ApiController](ApiController/index.md) | [PluginRequestDto](../dtos/PluginRequestDto/index.md) | [PluginDatasetListDto](../dtos/PluginDatasetListDto/index.md) | Liefert alle Datensätze, welche für das Plugin in der Frage vorhanden sein sollten |
| POST | [`/open/maxima`](ApiController/getMaxima/index.md) | [ApiController](ApiController/index.md) | [PluginRequestDto](../dtos/PluginRequestDto/index.md) | String | Liefert einen Maxima-Berechnungsstring für die Berechnung des Plugins |
| POST | [`/open/image`](ApiController/getImage/index.md) | [ApiController](ApiController/index.md) | [PluginRequestDto](../dtos/PluginRequestDto/index.md) | [ImageBase64Dto](../dtos/ImageBase64Dto/index.md) | Liefert ein Base64 codiertes Bild mit den angegebenen Parametern |
| POST | [`/open/imageurl`](ApiController/getImageUrl/index.md) | [ApiController](ApiController/index.md) | [PluginRequestDto](../dtos/PluginRequestDto/index.md) | [ImageUrlDto](../dtos/ImageUrlDto/index.md) | Liefert eine öffentliche URL auf das gerenderte Bild |
| POST | [`/open/imagetemplates`](ApiController/getImageTemplates/index.md) | [ApiController](ApiController/index.md) | [PluginRequestDto](../dtos/PluginRequestDto/index.md) | Vector&lt;String[]&gt; | Liefert eine Liste aller möglichen Varianten von Bildern in String-Arrays |
| POST | [`/open/parserplugin`](ApiController/parserPlugin/index.md) | [ApiController](ApiController/index.md) | [PluginParserRequestDto](../dtos/PluginParserRequestDto/index.md) | [CalcErgebnisDto](../dtos/CalcErgebnisDto/index.md) | Wird verwendet wenn im Lösungsfeld die Funktion plugin("pluginname",p1,p2,p3) verwendet wird |
| POST | [`/open/parserplugineinheit`](ApiController/parserPluginEinheit/index.md) | [ApiController](ApiController/index.md) | [PluginEinheitRequestDto](../dtos/PluginEinheitRequestDto/index.md) | String | Bestimmt die Recheneinheit, welche bei der Methode parserPlugin als Ergebnis herauskommt wenn die Parameter die Einheiten wie in der Liste p haben |
| POST | [`/open/score`](ApiController/score/index.md) | [ApiController](ApiController/index.md) | [PluginScoreRequestDto](../dtos/PluginScoreRequestDto/index.md) | [PluginScoreInfoDto](../dtos/PluginScoreInfoDto/index.md) | Prüft die Eingabe eines Schülers |
| POST | [`/open/getvars`](ApiController/getVars/index.md) | [ApiController](ApiController/index.md) | [PluginRequestDto](../dtos/PluginRequestDto/index.md) | Vector&lt;String&gt; | Liefert eine Liste aller Variablen welche als Dataset benötigt werden |
| POST | [`/open/modifyangabe`](ApiController/modifyAngabe/index.md) | [ApiController](ApiController/index.md) | [PluginAngabeRequestDto](../dtos/PluginAngabeRequestDto/index.md) | String | verändert einen Angabetext, der in der Angabe in PI Tags eingeschlossen wurde Die Funktion wird vor dem Darstellen der Frage ausgeführt |
| POST | [`/open/modifyangabetextkomplett`](ApiController/modifyAngabeTextkomplett/index.md) | [ApiController](ApiController/index.md) | [PluginAngabeRequestDto](../dtos/PluginAngabeRequestDto/index.md) | String | verändert den kompletten Angabetext der Frage |
| POST | [`/open/updatepluginstringjavascript`](ApiController/updatePluginstringJavascript/index.md) | [ApiController](ApiController/index.md) | [PluginUpdateJavascriptRequestDto](../dtos/PluginUpdateJavascriptRequestDto/index.md) | String | Passt die Plugindefinition an die Eingabe aus dem JavaScript-Result an |
| POST | [`/open/loadplugindto`](ApiController/loadPluginDto/index.md) | [ApiController](ApiController/index.md) | [LoadPluginRequestDto](../dtos/LoadPluginRequestDto/index.md) | [PluginDto](../dtos/PluginDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| POST | [`/open/renderlatex`](ApiController/renderLatex/index.md) | [ApiController](ApiController/index.md) | [PluginRenderLatexRequestDto](../dtos/PluginRenderLatexRequestDto/index.md) | [PluginRenderDto](../dtos/PluginRenderDto/index.md) | Rendert ein Plugin für den Fragedruck als LaTeX-Quelltext |
| POST | [`/open/renderpluginresult`](ApiController/renderPluginResult/index.md) | [ApiController](ApiController/index.md) | [PluginRenderResultRequestDto](../dtos/PluginRenderResultRequestDto/index.md) | [PluginRenderDto](../dtos/PluginRenderDto/index.md) | Rendert das Plugin inklusive der Schülereingabe und korrekter Lösung Es wird dabei entweder direkt ein HTML-Code oder LaTeX-Code erzeugt |
| POST | [`/open/configurationinfo`](ApiController/configurationInfo/index.md) | [ApiController](ApiController/index.md) | [PluginConfigurationInfoRequestDto](../dtos/PluginConfigurationInfoRequestDto/index.md) | [PluginConfigurationInfoDto](../dtos/PluginConfigurationInfoDto/index.md) | Liefert die Informationen welche notwendig sind um einen Konfigurationsdialog zu starten Ist die configurationID gesetzt wird eine Konfiguration gestartet und damit auch die restlichen Endpoints für die Konfiguration aktiviert |
| POST | [`/open/setconfigurationdata`](ApiController/setConfigurationData/index.md) | [ApiController](ApiController/index.md) | [PluginSetConfigurationDataRequestDto](../dtos/PluginSetConfigurationDataRequestDto/index.md) | [PluginConfigDto](../dtos/PluginConfigDto/index.md) | Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration |
| POST | [`/open/getconfiguration`](ApiController/getConfiguration/index.md) | [ApiController](ApiController/index.md) | [PluginConfigurationRequestDto](../dtos/PluginConfigurationRequestDto/index.md) | String | Liefert die aktuelle Konfiguration eines Plugins welches sich gerade in einem CONFIGMODE_URL Konfigurationsdialog befindet |
| POST | [`/open/reloadplugindto`](ApiController/reloadPluginDto/index.md) | [ApiController](ApiController/index.md) | [LoadPluginRequestDto](../dtos/LoadPluginRequestDto/index.md) | [PluginDto](../dtos/PluginDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| GET | [`/<endpoint>/api/open/pluginlist`](ApiExternOpenController/pluginList/index.md) | [ApiExternOpenController](ApiExternOpenController/index.md) | – | List&lt;String&gt; | liefert eine Liste aller Plugins (Pluginnamen) , welche mit diesem Service verwaltet werden |
| GET | [`/<endpoint>/api/open/generalinfolist`](ApiExternOpenController/pluginGeneralInfoList/index.md) | [ApiExternOpenController](ApiExternOpenController/index.md) | – | [PluginGeneralInfoList](../dtos/PluginGeneralInfoList/index.md) | liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services |
| POST | [`/<endpoint>/api/open/generalinfo`](ApiExternOpenController/pluginGeneralInfo/index.md) | [ApiExternOpenController](ApiExternOpenController/index.md) | String | [PluginGeneralInfo](../dtos/PluginGeneralInfo/index.md) | liefert die allgemeinen Konfigurationsinformationen zu einem Plugin Body: String - Name des Plugins |
| POST | [`/<endpoint>/api/open/reloadplugindto`](ApiExternOpenController/reloadPluginDto/index.md) | [ApiExternOpenController](ApiExternOpenController/index.md) | [LoadPluginRequestDto](../dtos/LoadPluginRequestDto/index.md) | [PluginDto](../dtos/PluginDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| GET | [`/<endpoint>/open/confighttp`](ConfigHttpController/configHttp/index.md) | [ConfigHttpController](ConfigHttpController/index.md) | `typ`, `configurationID` | String | Liefert die HTML-Seite des Konfigurationsdialogs |
| GET | [`/<endpoint>`](HelpController/help/index.md) | [HelpController](HelpController/index.md) | – | String | Liefert die Hilfeseite |
| GET | [`/ping`](InfoController/ping/index.md) | [InfoController](InfoController/index.md) | – | String | Bestätigt die Erreichbarkeit des internen Endpunkts |
| GET | [`/<endpoint>/open/ping`](InfoController/pingopen/index.md) | [InfoController](InfoController/index.md) | – | String | Bestätigt die Erreichbarkeit des öffentlichen Endpunkts |
| GET | [`/info`](InfoController/info/index.md) | [InfoController](InfoController/index.md) | – | [ServiceInfoDTO](../dtos/ServiceInfoDTO/index.md) | Liefert Informationen über den laufenden Plugin-Service |
| GET | [`/<endpoint>/open/info`](InfoController/infoOpen/index.md) | [InfoController](InfoController/index.md) | – | [ServiceInfoDTO](../dtos/ServiceInfoDTO/index.md) | Liefert Service-Informationen über den öffentlichen Endpunkt |
| GET | [`/version`](InfoController/version/index.md) | [InfoController](InfoController/index.md) | – | String | Liefert die Version des Plugin-Services |

## Konfigurationssitzung

* [configurationinfo](ApiController/configurationInfo/index.md) muss vor [setconfigurationdata](ApiController/setConfigurationData/index.md), [getconfiguration](ApiController/getConfiguration/index.md), [reloadplugindto](ApiController/reloadPluginDto/index.md) und [confighttp](ConfigHttpController/configHttp/index.md) aufgerufen werden.
* Die `configurationID` muss für jeden Konfigurationsdialog eindeutig sein und dient an den offenen Endpunkten als Authentifizierung.
* Die Sitzung wird nach `timeout` Sekunden ohne Zugriff entfernt.

## Registrierung am Setup-Service (ausgehend)

| Methode | Pfad am Setup-Service | Request | Response | Authentifizierung |
|---|---|---|---|---|
| POST | `/config/auth/user/registerplugin` | [ConfigServiceDto](../dtos/ConfigServiceDto/index.md) | [RegisterServiceResultDto](../dtos/RegisterServiceResultDto/index.md) | Basic Auth (`letto.user.user.name` / `letto.user.user.password`) |

Siehe [Build und Deployment](../build-deployment/index.md#registrierung-am-letto-server).

## Hinweise

* `EXTERN_API` (`/<endpoint>/auth/user`) wird bei der Registrierung als externe URI (`uriExtern`) an das Setup-Service gemeldet; ein Controller für eine authentifizierte externe API ist im Demo nicht implementiert.

[Referenz-Plugin (Java)](../index.md)
