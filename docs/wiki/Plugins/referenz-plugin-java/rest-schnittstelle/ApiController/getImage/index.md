# POST /open/image
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `getImage` |
| HTTP-Methode | POST |
| Pfad | `/open/image` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginRequestDto](../../../dtos/PluginRequestDto/index.md) |
| Response | [ImageBase64Dto](../../../dtos/ImageBase64Dto/index.md) |

## Beschreibung

Liefert ein Base64 codiertes Bild mit den angegebenen Parametern

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

Typ: [ImageBase64Dto](../../../dtos/ImageBase64Dto/index.md)

Base64 kodiertes Bild

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`getImageDto`](../../../plugin-api/index.md).

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

* [`POST /open/imageurl`](../../../rest-schnittstelle/ApiController/getImageUrl/index.md) – Liefert eine öffentliche URL auf das gerenderte Bild
* [`POST /open/imagetemplates`](../../../rest-schnittstelle/ApiController/getImageTemplates/index.md) – Liefert eine Liste aller möglichen Varianten von Bildern in String-Arrays
* [`POST /open/loadplugindto`](../../../rest-schnittstelle/ApiController/loadPluginDto/index.md) – Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
