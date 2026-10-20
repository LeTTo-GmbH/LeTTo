# PluginGeneralInfoList
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Liefert allgemein Informationen zu einem Plugin, welche ohne Definition einer Plugin-Instanz allgemein gültig sind

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginGeneralInfoList` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginGeneralInfoList.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `pluginInfos` | List&lt;[PluginGeneralInfo](../PluginGeneralInfo/index.md)&gt; |  | Allgemeine Informationen der enthaltenen Plugins. |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`GET /open/generalinfolist`](../../rest-schnittstelle/ApiController/pluginGeneralInfoList/index.md) | Response | Liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services |
| [`GET /<endpoint>/api/open/generalinfolist`](../../rest-schnittstelle/ApiExternOpenController/pluginGeneralInfoList/index.md) | Response | liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
