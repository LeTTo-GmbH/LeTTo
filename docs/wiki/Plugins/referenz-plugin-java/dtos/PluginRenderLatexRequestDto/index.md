# PluginRenderLatexRequestDto
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Anfragedaten für die LaTeX-Ausgabe eines Plugins.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginRenderLatexRequestDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginRenderLatexRequestDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `typ` | String | `""` | Typ des Plugins |
| `name` | String | `""` | Name des Plugins in der Frage |
| `config` | String | `""` | Konfigurationsstring des Plugins |
| `pluginDto` | [PluginDto](../../dtos/PluginDto/index.md) |  | Das [PluginDto](../../dtos/PluginDto/index.md) welches am Webserver an das JavaScript des Plugins zum Rendern gesandt wird |
| `answer` | String |  | Inhalt des Antwortfeldes welches der Schüler eingegeben hat |
| `mode` | String |  | Druckmode |

## Hinweise

* Die möglichen Werte von `mode` sind im Code nicht dokumentiert.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/renderlatex`](../../rest-schnittstelle/ApiController/renderLatex/index.md) | Request | Rendert ein Plugin für den Fragedruck als LaTeX-Quelltext |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
