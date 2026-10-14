# GET /&lt;endpoint&gt;/api/open/generalinfolist
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiExternOpenController](../index.md) |
| Java-Methode | `pluginGeneralInfoList` |
| HTTP-Methode | GET |
| Pfad | `/<endpoint>/api/open/generalinfolist` |
| Erreichbarkeit | extern über den Proxy |
| Request | – |
| Response | [PluginGeneralInfoList](../../../dtos/PluginGeneralInfoList/index.md) |

## Beschreibung

liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services


## Response

Typ: [PluginGeneralInfoList](../../../dtos/PluginGeneralInfoList/index.md)

HTTP-Antwort mit den allgemeinen Informationen aller registrierten Plugins

## Ablauf im Service

* Delegiert an [`GET /open/generalinfolist`](../../../rest-schnittstelle/ApiController/pluginGeneralInfoList/index.md) ([`ApiController.pluginGeneralInfoList`](../../../rest-schnittstelle/ApiController/pluginGeneralInfoList/index.md)).

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Siehe auch

* [`GET /open/generalinfolist`](../../../rest-schnittstelle/ApiController/pluginGeneralInfoList/index.md) – Liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services


[ApiExternOpenController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
