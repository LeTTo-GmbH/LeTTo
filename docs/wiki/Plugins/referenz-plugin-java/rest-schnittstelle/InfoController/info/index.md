# GET /info
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [InfoController](../index.md) |
| Java-Methode | `info` |
| HTTP-Methode | GET |
| Pfad | `/info` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request | – |
| Response | [ServiceInfoDTO](../../../dtos/ServiceInfoDTO/index.md) |

## Beschreibung

Liefert Informationen über den laufenden Plugin-Service.

## Response

Typ: [ServiceInfoDTO](../../../dtos/ServiceInfoDTO/index.md)

HTTP-Antwort mit Service-Informationen

## Ablauf im Service

* Verwendet `PluginConfiguration`: `getServiceInfoDto`.
* Die Informationen werden beim ersten Aufruf ermittelt und danach zwischengespeichert (Startzeit, Laufzeit usw. ändern sich daher nicht mehr).

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Siehe auch

* [`GET /<endpoint>/open/info`](../../../rest-schnittstelle/InfoController/infoOpen/index.md) – Liefert Service-Informationen über den öffentlichen Endpunkt
* [`GET /version`](../../../rest-schnittstelle/InfoController/version/index.md) – Liefert die Version des Plugin-Services


[InfoController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
