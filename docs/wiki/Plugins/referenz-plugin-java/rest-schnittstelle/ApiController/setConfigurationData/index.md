# POST /open/setconfigurationdata
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `setConfigurationData` |
| HTTP-Methode | POST |
| Pfad | `/open/setconfigurationdata` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginSetConfigurationDataRequestDto](../../../dtos/PluginSetConfigurationDataRequestDto/index.md) |
| Response | [PluginConfigDto](../../../dtos/PluginConfigDto/index.md) |

## Beschreibung

Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration

## Request

Body: [PluginSetConfigurationDataRequestDto](../../../dtos/PluginSetConfigurationDataRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `configurationID` | String | ja | zu verwendende Konfigurations-ID (muss am Plugin-Service zuvor angelegt worden sein mit configurationInfo) |
| `configuration` | String | ja | aktueller Konfigurations-String des Plugins |
| `questionDto` | [PluginQuestionDto](../../../dtos/PluginQuestionDto/index.md) | ja | Question-DTO mit Varhashes |

## Response

Typ: [PluginConfigDto](../../../dtos/PluginConfigDto/index.md)

Fehlermeldung wenn etwas nicht korrekt funktioniert hat

## Ablauf im Service

* Verwendet `PluginConfiguration`: `setConfigurationData`, `getUriGetPluginDto`.
* Ruft `setConfigurationData` des Plugins auf und ergänzt im Ergebnis `configurationID`, `typ`, `name`, `config`, `tagName` sowie ein `pluginDto` (über `loadPluginDto` mit leeren Parametern).
* Der Controller setzt `pluginDtoUri` auf den externen Endpunkt [`/<endpoint>/api/open/reloadplugindto`](../../../rest-schnittstelle/ApiExternOpenController/reloadPluginDto/index.md) und `pluginDtoToken` auf einen Leerstring.
* Ohne gültige Sitzung enthält das Ergebnis `errorMsg = "cannot find connection or plugin"`.

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Beispiel-Request

JSON-Gerüst aus den Feldern des DTOs, Werte sind Platzhalter:

```json
{
  "typ": "<typ>",
  "configurationID": "<configurationID>",
  "configuration": "<configuration>",
  "questionDto": {
    "…": "PluginQuestionDto"
  }
}
```

## Siehe auch

* [`POST /open/configurationinfo`](../../../rest-schnittstelle/ApiController/configurationInfo/index.md) – Liefert die Informationen welche notwendig sind um einen Konfigurationsdialog zu starten Ist die configurationID gesetzt wird eine Konfiguration gestartet und damit auch die restlichen Endpoints für die Konfiguration aktiviert
* [`POST /<endpoint>/api/open/reloadplugindto`](../../../rest-schnittstelle/ApiExternOpenController/reloadPluginDto/index.md) – Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung
* [`POST /open/getconfiguration`](../../../rest-schnittstelle/ApiController/getConfiguration/index.md) – Liefert die aktuelle Konfiguration eines Plugins welches sich gerade in einem CONFIGMODE_URL Konfigurationsdialog befindet


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
