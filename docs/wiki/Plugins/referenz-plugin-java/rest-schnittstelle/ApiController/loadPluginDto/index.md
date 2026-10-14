# POST /open/loadplugindto
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `loadPluginDto` |
| HTTP-Methode | POST |
| Pfad | `/open/loadplugindto` |
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
| `q` | [PluginQuestionDto](../../../dtos/PluginQuestionDto/index.md) | ja | Frage wo das Plugin eingebettet ist |
| `nr` | int | ja | Laufende Nummer für alle PIG-Tags und Question-Plugins |
| `configurationID` | String | nein | Konfigurations-ID, wenn das [PluginDto](../../../dtos/PluginDto/index.md) über AJAX bei der Konfiguration angefordert wird |

## Response

Typ: [PluginDto](../../../dtos/PluginDto/index.md)

[PluginDto](../../../dtos/PluginDto/index.md) welches von LeTTo an JavaScript übergeben wird

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`loadPluginDto`](../../../plugin-api/index.md).

## Fehlerfälle

* 404 Not Found, wenn der Plugin-Typ nicht registriert ist oder das Plugin nicht erzeugt werden kann („Plugin vom Typ … kann nicht erzeugt werden").

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

* [`POST /open/score`](../../../rest-schnittstelle/ApiController/score/index.md) – Prüft die Eingabe eines Schülers
* [`POST /open/reloadplugindto`](../../../rest-schnittstelle/ApiController/reloadPluginDto/index.md) – Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung
* [`POST /open/renderlatex`](../../../rest-schnittstelle/ApiController/renderLatex/index.md) – Rendert ein Plugin für den Fragedruck als LaTeX-Quelltext


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
