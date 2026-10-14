# POST /open/getconfiguration
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `getConfiguration` |
| HTTP-Methode | POST |
| Pfad | `/open/getconfiguration` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginConfigurationRequestDto](../../../dtos/PluginConfigurationRequestDto/index.md) |
| Response | String |

## Beschreibung

Liefert die aktuelle Konfiguration eines Plugins welches sich gerade in einem CONFIGMODE_URL Konfigurationsdialog befindet

## Request

Body: [PluginConfigurationRequestDto](../../../dtos/PluginConfigurationRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | PluginTyp |
| `configurationID` | String | ja | zu verwendende Konfigurations-ID (muss am Plugin-Service zuvor angelegt worden sein mit configurationInfo) |

## Response

Typ: String

Konfigurationsparameter oder "@ERROR: Meldung" wenn etwas nicht funktioniert hat

## Ablauf im Service

* Verwendet `PluginConfiguration`: `getConfiguration`.
* Fehler werden nicht als HTTP-Status, sondern im Text gemeldet: `@Error:cannot find connection or plugin` bzw. `@Error: error during configuration of plugin`.

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Beispiel-Request

JSON-Gerüst aus den Feldern des DTOs, Werte sind Platzhalter:

```json
{
  "typ": "<typ>",
  "configurationID": "<configurationID>"
}
```

## Siehe auch

* [`POST /open/configurationinfo`](../../../rest-schnittstelle/ApiController/configurationInfo/index.md) – Liefert die Informationen welche notwendig sind um einen Konfigurationsdialog zu starten Ist die configurationID gesetzt wird eine Konfiguration gestartet und damit auch die restlichen Endpoints für die Konfiguration aktiviert
* [`POST /open/setconfigurationdata`](../../../rest-schnittstelle/ApiController/setConfigurationData/index.md) – Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
