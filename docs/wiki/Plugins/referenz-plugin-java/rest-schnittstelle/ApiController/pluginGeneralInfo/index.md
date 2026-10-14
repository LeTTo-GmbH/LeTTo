# POST /open/generalinfo
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `pluginGeneralInfo` |
| HTTP-Methode | POST |
| Pfad | `/open/generalinfo` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | String |
| Response | [PluginGeneralInfo](../../../dtos/PluginGeneralInfo/index.md) |

## Beschreibung

Liefert die allgemeinen Konfigurationsinformationen zu einem Plugin.

## Request

Body: `String` – Typ des Plugins (z.B. Wsr) mit dem das Plugin auch in LeTTo angesprochen wird

## Response

Typ: [PluginGeneralInfo](../../../dtos/PluginGeneralInfo/index.md)

liefert die allgemeinen Konfigurationsinformationen zu einem Plugin

## Ablauf im Service

* Verwendet `PluginConfiguration`: `getPluginGeneralInfo`.
* Der Request-Body ist der Plugin-Typ als reiner String (kein JSON-Objekt).

## Fehlerfälle

* 404 Not Found, wenn der Plugin-Typ nicht registriert ist.

## Siehe auch

* [`POST /<endpoint>/api/open/generalinfo`](../../../rest-schnittstelle/ApiExternOpenController/pluginGeneralInfo/index.md) – liefert die allgemeinen Konfigurationsinformationen zu einem Plugin Body: String - Name des Plugins
* [`GET /open/generalinfolist`](../../../rest-schnittstelle/ApiController/pluginGeneralInfoList/index.md) – Liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
