# POST /open/angabe
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `getAngabe` |
| HTTP-Methode | POST |
| Pfad | `/open/angabe` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginRequestDto](../../../dtos/PluginRequestDto/index.md) |
| Response | String |

## Beschreibung

Liefert einen Angabestring für die Text-Angabe

## Request

Body: [PluginRequestDto](../../../dtos/PluginRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `params` | String | ja | Plugin-Parameter |
| `q` | [PluginQuestionDto](../../../dtos/PluginQuestionDto/index.md) | nein | Frage wo das Plugin eingebettet ist |
| `pluginMaximaCalcMode` | [PluginMaximaCalcModeDto](../../../dtos/PluginMaximaCalcModeDto/index.md) | nein | Art der Berechnung |

## Response

Typ: String

Angabetext für das Textfeld der Frage

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`getAngabe`](../../../plugin-api/index.md).

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
* [`POST /open/modifyangabe`](../../../rest-schnittstelle/ApiController/modifyAngabe/index.md) – verändert einen Angabetext, der in der Angabe in PI Tags eingeschlossen wurde Die Funktion wird vor dem Darstellen der Frage ausgeführt


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
