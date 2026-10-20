# GET /&lt;endpoint&gt;/open/info
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [InfoController](../index.md) |
| Java-Methode | `infoOpen` |
| HTTP-Methode | GET |
| Pfad | `/<endpoint>/open/info` |
| Erreichbarkeit | extern über den Proxy |
| Request | – |
| Response | [ServiceInfoDTO](../../../dtos/ServiceInfoDTO/index.md) |

## Beschreibung

Liefert Service-Informationen über den öffentlichen Endpunkt.

## Response

Typ: [ServiceInfoDTO](../../../dtos/ServiceInfoDTO/index.md)

HTTP-Antwort mit Service-Informationen

## Ablauf im Service

* Verwendet `PluginConfiguration`: `getServiceInfoDto`.
* Die Informationen werden beim ersten Aufruf ermittelt und danach zwischengespeichert.

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Siehe auch

* [`GET /info`](../info/index.md) – Liefert Informationen über den laufenden Plugin-Service


[InfoController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
