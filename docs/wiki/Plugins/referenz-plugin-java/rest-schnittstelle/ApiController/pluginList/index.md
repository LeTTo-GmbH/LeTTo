# GET /open/pluginlist
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `pluginList` |
| HTTP-Methode | GET |
| Pfad | `/open/pluginlist` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request | – |
| Response | List&lt;String&gt; |

## Beschreibung

Liefert eine Liste aller Plugins (Pluginnamen) , welche mit diesem Service verwaltet werden.

## Response

Typ: List&lt;String&gt;

liefert eine Liste aller Plugins (Pluginnamen) , welche mit diesem Service verwaltet werden

## Ablauf im Service

* Verwendet `PluginConfiguration`: `getPluginList`.

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Siehe auch

* [`GET /<endpoint>/api/open/pluginlist`](../../../rest-schnittstelle/ApiExternOpenController/pluginList/index.md) – liefert eine Liste aller Plugins (Pluginnamen) , welche mit diesem Service verwaltet werden
* [`GET /open/generalinfolist`](../../../rest-schnittstelle/ApiController/pluginGeneralInfoList/index.md) – Liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
