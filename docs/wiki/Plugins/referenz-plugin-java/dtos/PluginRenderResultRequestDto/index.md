# PluginRenderResultRequestDto
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Anfragedaten für die Darstellung einer bewerteten Antwort.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginRenderResultRequestDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginRenderResultRequestDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `typ` | String | `""` | Typ des Plugins |
| `name` | String | `""` | Name des Plugins in der Frage |
| `config` | String | `""` | Konfigurationsstring des Plugins |
| `tex` | boolean |  | true für LaTeX-Code, false für html-Code |
| `pluginDto` | [PluginDto](../../dtos/PluginDto/index.md) |  | Das [PluginDto](../../dtos/PluginDto/index.md) welches am Webserver an das JavaScript des Plugins zum Rendern gesandt wird |
| `antwort` | String |  | Antwort die der Schüler eingegeben hat |
| `toleranz` | [ToleranzDto](../../dtos/ToleranzDto/index.md) |  | Toleranz für die Lösung |
| `varsQuestion` | [VarHashDto](../../dtos/VarHashDto/index.md) |  | Referenz auf VarHash, wird dynamisch nachgeladen |
| `answerDto` | [PluginAnswerDto](../../dtos/PluginAnswerDto/index.md) |  | Antwort des Schülers |
| `grade` | double |  | Maximale Punktanzahl für die richtige Antwort |

## Hinweise

* Unstimmigkeit im Code: Die JavaDoc von `answerDto` lautet „Antwort des Schülers"; laut Controller und Plugin-API ist es die Musterlösung mit Informationen für den Scorer.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/renderpluginresult`](../../rest-schnittstelle/ApiController/renderPluginResult/index.md) | Request | Rendert das Plugin inklusive der Schülereingabe und korrekter Lösung Es wird dabei entweder direkt ein HTML-Code oder LaTeX-Code erzeugt |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
