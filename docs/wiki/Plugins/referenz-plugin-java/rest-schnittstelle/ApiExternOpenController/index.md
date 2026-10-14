# ApiExternOpenController
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

offene Endpoints welche von extern erreichbar sein müssen für ajax und allgemeine Informationen (von extern erreichbar)

Swagger: Öffentliche Schnittstelle des Plugins (über den Proxy erreichbar), z.B. für die Vorschau im Konfigurationsdialog [JavaDoc](

| | |
|---|---|
| Klasse | `at.letto.plugins.controller.ApiExternOpenController` |
| Basispfad | `/<endpoint>/api/open` |
| Erreichbarkeit | extern über den Proxy |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/controller/ApiExternOpenController.html` |

## Endpunkte

| Methode | Pfad | Request | Response | Beschreibung |
|---|---|---|---|---|
| GET | [`/<endpoint>/api/open/pluginlist`](pluginList/index.md) | – | List&lt;String&gt; | liefert eine Liste aller Plugins (Pluginnamen) , welche mit diesem Service verwaltet werden |
| GET | [`/<endpoint>/api/open/generalinfolist`](pluginGeneralInfoList/index.md) | – | [PluginGeneralInfoList](../../dtos/PluginGeneralInfoList/index.md) | liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services |
| POST | [`/<endpoint>/api/open/generalinfo`](pluginGeneralInfo/index.md) | String | [PluginGeneralInfo](../../dtos/PluginGeneralInfo/index.md) | liefert die allgemeinen Konfigurationsinformationen zu einem Plugin Body: String - Name des Plugins |
| POST | [`/<endpoint>/api/open/reloadplugindto`](reloadPluginDto/index.md) | [LoadPluginRequestDto](../../dtos/LoadPluginRequestDto/index.md) | [PluginDto](../../dtos/PluginDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |

## Hinweise

* Alle Endpunkte delegieren an den gleichnamigen Endpunkt des [ApiController](../ApiController/index.md).


[REST-Schnittstelle](../index.md) · [Referenz-Plugin (Java)](../../index.md)
