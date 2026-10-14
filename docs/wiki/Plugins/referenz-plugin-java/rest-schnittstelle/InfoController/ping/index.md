# GET /ping
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [InfoController](../index.md) |
| Java-Methode | `ping` |
| HTTP-Methode | GET |
| Pfad | `/ping` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request | – |
| Response | String |

## Beschreibung

Bestätigt die Erreichbarkeit des internen Endpunkts.

## Response

Typ: String

HTTP-Antwort mit der Erreichbarkeitsmeldung

## Ablauf im Service

* Liefert fest den Text `pong`.
* Wird vom Docker-Healthcheck (`scripts/healthcheck.sh`) aufgerufen; erwartet wird genau `pong`.

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Siehe auch

* [`GET /<endpoint>/open/ping`](../../../rest-schnittstelle/InfoController/pingopen/index.md) – Bestätigt die Erreichbarkeit des öffentlichen Endpunkts


[InfoController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
