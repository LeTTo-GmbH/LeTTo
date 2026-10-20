# GET /open/generalinfolist
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `pluginGeneralInfoList` |
| HTTP-Methode | GET |
| Pfad | `/open/generalinfolist` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request | – |
| Response | [PluginGeneralInfoList](../../../dtos/PluginGeneralInfoList/index.md) |

## Beschreibung

Liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services.

## Response

Typ: [PluginGeneralInfoList](../../../dtos/PluginGeneralInfoList/index.md)

liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services

## Ablauf im Service

* Verwendet `PluginConfiguration`: `getPluginGeneralInfoList`.

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Siehe auch

* [`GET /<endpoint>/api/open/generalinfolist`](../../ApiExternOpenController/pluginGeneralInfoList/index.md) – liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services
* [`POST /open/generalinfo`](../pluginGeneralInfo/index.md) – Liefert die allgemeinen Konfigurationsinformationen zu einem Plugin


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
