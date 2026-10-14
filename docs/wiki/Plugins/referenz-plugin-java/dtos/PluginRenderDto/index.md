# PluginRenderDto
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Enthält gerenderten HTML- oder LaTeX-Code und die zugehörigen Bilder.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginRenderDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginRenderDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `source` | String | `""` | LaTeX-Quelltext oder HTML-Quelltext |
| `images` | HashMap&lt;String,String&gt; | `new HashMap<>()` | Liste der Bilder welche im Quelltext eingebunden werden. Sie werden im Verzeichnis img/ relativ zum LaTeX-Quelltext positioniert. Müssen deshalb auch dementsprechend im LaTeX-Quelltext eingebunden sein. Zulässig sind nur Bilder mit der Extension .png, .jpg, .jpeg, .pdf key : Dateiname value : Base64 codiertes Bild |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/renderlatex`](../../rest-schnittstelle/ApiController/renderLatex/index.md) | Response | Rendert ein Plugin für den Fragedruck als LaTeX-Quelltext |
| [`POST /open/renderpluginresult`](../../rest-schnittstelle/ApiController/renderPluginResult/index.md) | Response | Rendert das Plugin inklusive der Schülereingabe und korrekter Lösung Es wird dabei entweder direkt ein HTML-Code oder LaTeX-Code erzeugt |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

* [`renderLatex`](../../plugin-api/index.md): `PluginRenderDto renderLatex(`[`PluginDto`](../../dtos/PluginDto/index.md) `pluginDto, String answer, String mode)`
* [`renderPluginResult`](../../plugin-api/index.md): `PluginRenderDto renderPluginResult(boolean tex,` [`PluginDto`](../../dtos/PluginDto/index.md) `pluginDto, String antwort,` [`ToleranzDto`](../../dtos/ToleranzDto/index.md) `toleranz,` [`VarHashDto`](../../dtos/VarHashDto/index.md) `varsQuestion,` [`PluginAnswerDto`](../../dtos/PluginAnswerDto/index.md) `answerDto, double grade)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
