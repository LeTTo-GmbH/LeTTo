# POST /open/reloadplugindto
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `reloadPluginDto` |
| HTTP-Methode | POST |
| Pfad | `/open/reloadplugindto` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [LoadPluginRequestDto](../../../dtos/LoadPluginRequestDto/index.md) |
| Response | [PluginDto](../../../dtos/PluginDto/index.md) |

## Beschreibung

Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung

## Request

Body: [LoadPluginRequestDto](../../../dtos/LoadPluginRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `params` | String | ja | Plugin-Parameter |
| `q` | [PluginQuestionDto](../../../dtos/PluginQuestionDto/index.md) | nein | Frage wo das Plugin eingebettet ist |
| `nr` | int | ja | Laufende Nummer für alle PIG-Tags und Question-Plugins |
| `configurationID` | String | ja | ID der aktuellen Konfiguration |

## Response

Typ: [PluginDto](../../../dtos/PluginDto/index.md)

[PluginDto](../../../dtos/PluginDto/index.md) welches von LeTTo an JavaScript übergeben wird

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`loadPluginDto`](../../../plugin-api/index.md).
* Verwendet `PluginConfiguration`: `getConfigurationConnection`.
* Sucht die Sitzung zur `configurationID`, erzeugt das Plugin mit der übergebenen `config` neu und aktualisiert damit die Sitzung (`changeConfig`), sodass `getconfiguration` danach die neue Konfiguration liefert.
* Das [`PluginDto`](../../../dtos/PluginDto/index.md) wird mit der in der Sitzung gespeicherten Frage (`pluginQuestionDto`) erzeugt, `q` aus dem Request wird ignoriert.

## Fehlerfälle

* 404 Not Found, wenn der Plugin-Typ nicht registriert ist oder das Plugin nicht erzeugt werden kann („Plugin vom Typ … kann nicht erzeugt werden").
* 404 Not Found ohne Body, wenn zur `configurationID` keine gültige Sitzung existiert.

## Beispiel-Request

JSON-Gerüst aus den Feldern des DTOs, Werte sind Platzhalter:

```json
{
  "typ": "<typ>",
  "name": "<name>",
  "config": "<config>",
  "params": "<params>",
  "q": {
    "…": "PluginQuestionDto"
  },
  "nr": 0,
  "configurationID": "<configurationID>"
}
```

## Siehe auch

* [`POST /<endpoint>/api/open/reloadplugindto`](../../ApiExternOpenController/reloadPluginDto/index.md) – Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung
* [`POST /open/loadplugindto`](../loadPluginDto/index.md) – Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung
* [`POST /open/configurationinfo`](../configurationInfo/index.md) – Liefert die Informationen welche notwendig sind um einen Konfigurationsdialog zu starten Ist die configurationID gesetzt wird eine Konfiguration gestartet und damit auch die restlichen Endpoints für die Konfiguration aktiviert


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
