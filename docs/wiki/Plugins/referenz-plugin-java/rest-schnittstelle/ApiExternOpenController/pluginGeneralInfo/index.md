# POST /&lt;endpoint&gt;/api/open/generalinfo
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiExternOpenController](../index.md) |
| Java-Methode | `pluginGeneralInfo` |
| HTTP-Methode | POST |
| Pfad | `/<endpoint>/api/open/generalinfo` |
| Erreichbarkeit | extern über den Proxy |
| Request-Body | String |
| Response | [PluginGeneralInfo](../../../dtos/PluginGeneralInfo/index.md) |

## Beschreibung

liefert die allgemeinen Konfigurationsinformationen zu einem Plugin

Body: String - Name des Plugins


## Request

Body: `String` – Name des registrierten Plugin-Typs

## Response

Typ: [PluginGeneralInfo](../../../dtos/PluginGeneralInfo/index.md)

HTTP-Antwort mit den allgemeinen Informationen des angefragten Plugins

## Ablauf im Service

* Delegiert an [`POST /open/generalinfo`](../../../rest-schnittstelle/ApiController/pluginGeneralInfo/index.md) ([`ApiController.pluginGeneralInfo`](../../../rest-schnittstelle/ApiController/pluginGeneralInfo/index.md)).
* Der Request-Body ist der Plugin-Typ als reiner String (kein JSON-Objekt).

## Fehlerfälle

* 404 Not Found, wenn der Plugin-Typ nicht registriert ist.

## Siehe auch

* [`POST /open/generalinfo`](../../../rest-schnittstelle/ApiController/pluginGeneralInfo/index.md) – Liefert die allgemeinen Konfigurationsinformationen zu einem Plugin


[ApiExternOpenController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
