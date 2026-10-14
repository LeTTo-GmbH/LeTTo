# PluginRenderLatexRequestDto
<!-- generiert aus plugin-demo-java @ f0143d1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

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
| `mode` | String |  | Druckmode. Der LeTTo-Server übergibt hier derzeit `TexPrintMode.toString()`; da diese Klasse kein eigenes toString() hat, ist der Wert nur ein Objekt-Bezeichner (z.B. `at.letto.tools.tex.TexPrintMode@6d06d69c`) und kann vom Plugin nicht ausgewertet werden. |

## Hinweise

* `mode` lässt sich derzeit nicht auswerten: Der LeTTo-Server übergibt `TexPrintMode.toString()`, und diese Klasse hat kein eigenes `toString()` – das Plugin erhält nur einen Objekt-Bezeichner wie `at.letto.tools.tex.TexPrintMode@6d06d69c`.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/renderlatex`](../../rest-schnittstelle/ApiController/renderLatex/index.md) | Request | Rendert ein Plugin für den Fragedruck als LaTeX-Quelltext |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
