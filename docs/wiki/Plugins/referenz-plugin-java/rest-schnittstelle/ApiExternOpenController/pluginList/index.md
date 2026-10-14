# GET /&lt;endpoint&gt;/api/open/pluginlist
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiExternOpenController](../index.md) |
| Java-Methode | `pluginList` |
| HTTP-Methode | GET |
| Pfad | `/<endpoint>/api/open/pluginlist` |
| Erreichbarkeit | extern über den Proxy |
| Request | – |
| Response | List&lt;String&gt; |

## Beschreibung

liefert eine Liste aller Plugins (Pluginnamen) , welche mit diesem Service verwaltet werden

## Response

Typ: List&lt;String&gt;

HTTP-Antwort mit den Namen der Plugin-Typen

## Ablauf im Service

* Delegiert an [`GET /open/pluginlist`](../../../rest-schnittstelle/ApiController/pluginList/index.md) ([`ApiController.pluginList`](../../../rest-schnittstelle/ApiController/pluginList/index.md)).

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Siehe auch

* [`GET /open/pluginlist`](../../../rest-schnittstelle/ApiController/pluginList/index.md) – Liefert eine Liste aller Plugins (Pluginnamen) , welche mit diesem Service verwaltet werden


[ApiExternOpenController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
