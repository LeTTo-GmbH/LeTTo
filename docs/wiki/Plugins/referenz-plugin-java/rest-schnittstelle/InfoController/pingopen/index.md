# GET /&lt;endpoint&gt;/open/ping
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [InfoController](../index.md) |
| Java-Methode | `pingopen` |
| HTTP-Methode | GET |
| Pfad | `/<endpoint>/open/ping` |
| Erreichbarkeit | extern über den Proxy |
| Request | – |
| Response | String |

## Beschreibung

Bestätigt die Erreichbarkeit des öffentlichen Endpunkts.

## Response

Typ: String

HTTP-Antwort mit der Erreichbarkeitsmeldung

## Ablauf im Service

* Liefert fest den Text `pong`.

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Siehe auch

* [`GET /ping`](../ping/index.md) – Bestätigt die Erreichbarkeit des internen Endpunkts


[InfoController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
