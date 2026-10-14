# POST /open/imagetemplates
<!-- generiert aus plugin-demo-java @ f0143d1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `getImageTemplates` |
| HTTP-Methode | POST |
| Pfad | `/open/imagetemplates` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginRequestDto](../../../dtos/PluginRequestDto/index.md) |
| Response | Vector&lt;String[]&gt; |

## Beschreibung

Liefert eine Liste aller möglichen Varianten von Bildern in String-Arrays

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

Typ: Vector&lt;String[]&gt;

Liefert eine Liste aller möglichen Varianten von Bildern in String-Arrays Element 0 : beschreibender Text Element 1 : PIG Tag Element 2 : Hilfetext

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`getImageTemplates`](../../../plugin-api/index.md).
* Die Antwort ist ein Array von String-Arrays: [0] beschreibender Text, [1] PIG-Tag, [2] Hilfetext.

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

* [`POST /open/image`](../../../rest-schnittstelle/ApiController/getImage/index.md) – Liefert ein Base64 codiertes Bild mit den angegebenen Parametern


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
