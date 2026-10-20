# POST /open/generatedatasets
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `generateDatasets` |
| HTTP-Methode | POST |
| Pfad | `/open/generatedatasets` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginRequestDto](../../../dtos/PluginRequestDto/index.md) |
| Response | [PluginDatasetListDto](../../../dtos/PluginDatasetListDto/index.md) |

## Beschreibung

Liefert alle Datensätze, welche für das Plugin in der Frage vorhanden sein sollten

## Request

Body: [PluginRequestDto](../../../dtos/PluginRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `params` | String | nein | Parameter für die Antworterzeugung |
| `q` | [PluginQuestionDto](../../../dtos/PluginQuestionDto/index.md) | nein | Frage wo das Plugin eingebettet ist |
| `pluginMaximaCalcMode` | [PluginMaximaCalcModeDto](../../../dtos/PluginMaximaCalcModeDto/index.md) | nein | Art der Berechnung |

## Response

Typ: [PluginDatasetListDto](../../../dtos/PluginDatasetListDto/index.md)

Liste der Datensatzdefinitionen welche vom Plugin in der Frage angefordert werden

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`generateDatasets`](../../../plugin-api/index.md).

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
  "pluginMaximaCalcMode": {
    "…": "PluginMaximaCalcModeDto"
  }
}
```

## Siehe auch

* [`POST /open/getvars`](../getVars/index.md) – Liefert eine Liste aller Variablen welche als Dataset benötigt werden
* [`POST /open/angabe`](../getAngabe/index.md) – Liefert einen Angabestring für die Text-Angabe


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
