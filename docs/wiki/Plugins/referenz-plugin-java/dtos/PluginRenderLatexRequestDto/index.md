# PluginRenderLatexRequestDto
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

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
| `mode` | String |  | Druckmode, vom LeTTo-Server als `TexPrintMode.toString()` übergeben, z.B. `PRINTFRAGE;datasets=0,1;recurse=false;newPage=false;line=false`. Der erste Teil ist der Druckmodus: PRINTFRAGE, PRINTERGEBNIS, PRINTFORMEL, PRINTINFO, PRINTHTML, PRINTANTWORT, PRINTANTWORTERGEBNIS oder PRINTEINSICHTNAHME (z.B. `mode.split(";")[0]`); danach folgen die zu druckenden Datensätze, rekursiver Druck, neue Seite und Linie nach jeder Frage. Ältere LeTTo-Server übergeben nur einen nicht auswertbaren Objekt-Bezeichner (z.B. `at.letto.tools.tex.TexPrintMode@6d06d69c`). |

## Hinweise

* `mode` hat das Format `<PRINTMODE>;datasets=<Nr,Nr>;recurse=<bool>;newPage=<bool>;line=<bool>` (`TexPrintMode.toString()` des LeTTo-Servers), z.B. `PRINTERGEBNIS;datasets=0,3;recurse=false;newPage=true;line=false`. Der Druckmodus ist der erste Teil (`mode.split(";")[0]`): `PRINTFRAGE`, `PRINTERGEBNIS`, `PRINTFORMEL`, `PRINTINFO`, `PRINTHTML`, `PRINTANTWORT`, `PRINTANTWORTERGEBNIS` oder `PRINTEINSICHTNAHME`.
* Ältere LeTTo-Server übergeben nur einen nicht auswertbaren Objekt-Bezeichner wie `at.letto.tools.tex.TexPrintMode@6d06d69c`.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/renderlatex`](../../rest-schnittstelle/ApiController/renderLatex/index.md) | Request | Rendert ein Plugin für den Fragedruck als LaTeX-Quelltext |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
