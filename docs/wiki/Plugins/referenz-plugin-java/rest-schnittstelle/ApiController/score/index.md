# POST /open/score
<!-- generiert aus plugin-demo-java @ f0143d1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `score` |
| HTTP-Methode | POST |
| Pfad | `/open/score` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginScoreRequestDto](../../../dtos/PluginScoreRequestDto/index.md) |
| Response | [PluginScoreInfoDto](../../../dtos/PluginScoreInfoDto/index.md) |

## Beschreibung

Prüft die Eingabe eines Schülers

## Request

Body: [PluginScoreRequestDto](../../../dtos/PluginScoreRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `pluginDto` | [PluginDto](../../../dtos/PluginDto/index.md) | ja | [PluginDto](../../../dtos/PluginDto/index.md) welches für die JavaScript aktive Eingabe aufbereitet wurde |
| `antwort` | String | ja | Antwort die der Schüler eingegeben hat |
| `toleranz` | [ToleranzDto](../../../dtos/ToleranzDto/index.md) | ja | Toleranz für die Lösung |
| `varsQuestion` | [VarHashDto](../../../dtos/VarHashDto/index.md) | ja | VarHash aller Variablen der Frage |
| `answerDto` | [PluginAnswerDto](../../../dtos/PluginAnswerDto/index.md) | ja | korrekte Antwort und Informationen für den Scorer des Plugins |
| `grade` | double | ja | Maximale Punktanzahl für die richtige Antwort |

## Response

Typ: [PluginScoreInfoDto](../../../dtos/PluginScoreInfoDto/index.md)

[PluginScoreInfoDto](../../../dtos/PluginScoreInfoDto/index.md): Bewertung

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`score`](../../../plugin-api/index.md).

## Fehlerfälle

* 404 Not Found, wenn der Plugin-Typ nicht registriert ist oder das Plugin nicht erzeugt werden kann („Plugin vom Typ … kann nicht erzeugt werden").

## Beispiel-Request

JSON-Gerüst aus den Feldern des DTOs, Werte sind Platzhalter:

```json
{
  "typ": "<typ>",
  "name": "<name>",
  "config": "<config>",
  "pluginDto": {
    "…": "PluginDto"
  },
  "antwort": "<antwort>",
  "toleranz": {
    "…": "ToleranzDto"
  },
  "varsQuestion": {
    "…": "VarHashDto"
  },
  "answerDto": {
    "…": "PluginAnswerDto"
  },
  "grade": 0
}
```

## Siehe auch

* [`POST /open/loadplugindto`](../../../rest-schnittstelle/ApiController/loadPluginDto/index.md) – Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung
* [`POST /open/renderpluginresult`](../../../rest-schnittstelle/ApiController/renderPluginResult/index.md) – Rendert das Plugin inklusive der Schülereingabe und korrekter Lösung Es wird dabei entweder direkt ein HTML-Code oder LaTeX-Code erzeugt


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
