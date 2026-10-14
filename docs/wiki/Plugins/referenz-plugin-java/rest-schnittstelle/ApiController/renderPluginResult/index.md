# POST /open/renderpluginresult
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `renderPluginResult` |
| HTTP-Methode | POST |
| Pfad | `/open/renderpluginresult` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginRenderResultRequestDto](../../../dtos/PluginRenderResultRequestDto/index.md) |
| Response | [PluginRenderDto](../../../dtos/PluginRenderDto/index.md) |

## Beschreibung

Rendert das Plugin inklusive der Schülereingabe und korrekter Lösung

Es wird dabei entweder direkt ein HTML-Code oder LaTeX-Code erzeugt


## Request

Body: [PluginRenderResultRequestDto](../../../dtos/PluginRenderResultRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `tex` | boolean | ja | true für LaTeX-Code, false für html-Code |
| `pluginDto` | [PluginDto](../../../dtos/PluginDto/index.md) | ja | Das [PluginDto](../../../dtos/PluginDto/index.md) welches am Webserver an das JavaScript des Plugins zum Rendern gesandt wird |
| `antwort` | String | ja | Antwort die der Schüler eingegeben hat |
| `toleranz` | [ToleranzDto](../../../dtos/ToleranzDto/index.md) | ja | Toleranz für die Lösung |
| `varsQuestion` | [VarHashDto](../../../dtos/VarHashDto/index.md) | ja | VarHash aller Variablen der Frage |
| `answerDto` | [PluginAnswerDto](../../../dtos/PluginAnswerDto/index.md) | ja | korrekte Antwort und Informationen für den Scorer des Plugins |
| `grade` | double | ja | Maximale Punktanzahl für die richtige Antwort |

## Response

Typ: [PluginRenderDto](../../../dtos/PluginRenderDto/index.md)

HTML-Code oder LaTeX-Code mit Bildern

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`renderPluginResult`](../../../plugin-api/index.md).

## Fehlerfälle

* 404 Not Found, wenn der Plugin-Typ nicht registriert ist oder das Plugin nicht erzeugt werden kann („Plugin vom Typ … kann nicht erzeugt werden").

## Beispiel-Request

JSON-Gerüst aus den Feldern des DTOs, Werte sind Platzhalter:

```json
{
  "typ": "<typ>",
  "name": "<name>",
  "config": "<config>",
  "tex": false,
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

* [`POST /open/score`](../../../rest-schnittstelle/ApiController/score/index.md) – Prüft die Eingabe eines Schülers
* [`POST /open/renderlatex`](../../../rest-schnittstelle/ApiController/renderLatex/index.md) – Rendert ein Plugin für den Fragedruck als LaTeX-Quelltext


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
