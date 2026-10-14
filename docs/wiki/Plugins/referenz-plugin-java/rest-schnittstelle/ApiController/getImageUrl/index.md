# POST /open/imageurl
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `getImageUrl` |
| HTTP-Methode | POST |
| Pfad | `/open/imageurl` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginRequestDto](../../../dtos/PluginRequestDto/index.md) |
| Response | [ImageUrlDto](../../../dtos/ImageUrlDto/index.md) |

## Beschreibung

Liefert eine öffentliche URL auf das gerenderte Bild.

Das Bild wird im Image-Service des Plugins gespeichert. Der LeTTo-Server ruft diesen Endpoint vor `image` auf und verwendet das Base64-Bild nur, wenn hier keine URL geliefert wird.

## Request

Body: [PluginRequestDto](../../../dtos/PluginRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `params` | String | ja | Plugin-Parameter |
| `q` | [PluginQuestionDto](../../../dtos/PluginQuestionDto/index.md) | ja | Frage wo das Plugin eingebettet ist |
| `pluginMaximaCalcMode` | [PluginMaximaCalcModeDto](../../../dtos/PluginMaximaCalcModeDto/index.md) | nein | Art der Berechnung |

## Response

Typ: [ImageUrlDto](../../../dtos/ImageUrlDto/index.md)

Bild-URL mit Bildinformationen und gegebenenfalls einer Fehlermeldung

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`getImageUrl`](../../../plugin-api/index.md).
* Das Bild wird über `parseDrawParams` und `paint` erzeugt und im Image-Service des Plugins gespeichert (Verzeichnis `letto.pathPlugins` + Servicepfad); `imageUrl` und `imageInfoDto.url` enthalten die öffentliche URL.
* Der LeTTo-Server ruft diesen Endpunkt vor `image` auf. Liefert er keine URL oder schlägt er fehl, verwendet der Server das Base64-Bild von `image`.
* Kann das Bild nicht gespeichert werden, steht die Meldung in `error`.

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
* [`POST /open/loadplugindto`](../../../rest-schnittstelle/ApiController/loadPluginDto/index.md) – Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
