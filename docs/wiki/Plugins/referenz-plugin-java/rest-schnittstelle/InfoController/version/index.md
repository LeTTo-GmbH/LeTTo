# GET /version
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [InfoController](../index.md) |
| Java-Methode | `version` |
| HTTP-Methode | GET |
| Pfad | `/version` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request | – |
| Response | String |

## Beschreibung

Liefert die Version des Plugin-Services.

## Response

Typ: String

HTTP-Antwort mit der Service-Version

## Ablauf im Service

* Liefert die Konstante `PluginConfiguration.PLUGIN_VERSION`.

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Siehe auch

* [`GET /info`](../info/index.md) – Liefert Informationen über den laufenden Plugin-Service


[InfoController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
