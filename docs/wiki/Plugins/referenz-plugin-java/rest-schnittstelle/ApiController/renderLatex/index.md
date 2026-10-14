# POST /open/renderlatex
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `renderLatex` |
| HTTP-Methode | POST |
| Pfad | `/open/renderlatex` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginRenderLatexRequestDto](../../../dtos/PluginRenderLatexRequestDto/index.md) |
| Response | [PluginRenderDto](../../../dtos/PluginRenderDto/index.md) |

## Beschreibung

Rendert ein Plugin für den Fragedruck als LaTeX-Quelltext

## Request

Body: [PluginRenderLatexRequestDto](../../../dtos/PluginRenderLatexRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `pluginDto` | [PluginDto](../../../dtos/PluginDto/index.md) | ja | Das [PluginDto](../../../dtos/PluginDto/index.md) welches am Webserver an das JavaScript des Plugins zum Rendern gesandt wird |
| `answer` | String | ja | Inhalt des Antwortfeldes welches der Schüler eingegeben hat |
| `mode` | String | ja | Druckmode |

## Response

Typ: [PluginRenderDto](../../../dtos/PluginRenderDto/index.md)

[PluginDto](../../../dtos/PluginDto/index.md) welches von LeTTo an JavaScript übergeben wird

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`renderLatex`](../../../plugin-api/index.md).

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
  "answer": "<answer>",
  "mode": "<mode>"
}
```

## Siehe auch

* [`POST /open/renderpluginresult`](../../../rest-schnittstelle/ApiController/renderPluginResult/index.md) – Rendert das Plugin inklusive der Schülereingabe und korrekter Lösung Es wird dabei entweder direkt ein HTML-Code oder LaTeX-Code erzeugt
* [`POST /open/loadplugindto`](../../../rest-schnittstelle/ApiController/loadPluginDto/index.md) – Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
