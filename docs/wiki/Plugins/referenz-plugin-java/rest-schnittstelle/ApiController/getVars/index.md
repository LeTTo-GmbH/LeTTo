# POST /open/getvars
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `getVars` |
| HTTP-Methode | POST |
| Pfad | `/open/getvars` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginRequestDto](../../../dtos/PluginRequestDto/index.md) |
| Response | Vector&lt;String&gt; |

## Beschreibung

Liefert eine Liste aller Variablen welche als Dataset benötigt werden.

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

Typ: Vector&lt;String&gt;

Liste aller Variablen des Plugins

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`getVars`](../../../plugin-api/index.md).

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

* [`POST /open/generatedatasets`](../../../rest-schnittstelle/ApiController/generateDatasets/index.md) – Liefert alle Datensätze, welche für das Plugin in der Frage vorhanden sein sollten


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
