# PluginDto
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Dto welches vom Plugin über Letto zum JavaScript des Plugins geschickt wird

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `imageUrl` | String | `""` | Url eines eingebetteten Bildes - meist base64 codiert |
| `pig` | boolean |  | True wenn das Plugin über ein PIG-Tag direkt in der Frage eingebunden ist |
| `result` | boolean |  | True wenn Plugin in einer Subquestion definiert ist |
| `tagName` | String | `""` | Eindeutiger Bezeichner des PluginTags |
| `width` | int | `500` | Breite des Plugin-Bereiches in Pixel |
| `height` | int | `500` | Höhe des Plugin-Bereiches in Pixel |
| `params` | HashMap&lt;String,String&gt; | `new HashMap<>()` | Parameter welche vom Plugin an JavaScript weitergegeben werden sollen, wird von LeTTo nicht verwendet |
| `jsonData` | String |  | JSON-String welcher vom Plugin an JavaScript weitergegeben werden soll, wird von LeTTo nicht verwendet |

## Hinweise

* Konstruktor `PluginDto(params, pluginService, q, nr)`: setzt `tagName = <frageId>_<name>_<nr>`, übernimmt `size=` aus den Parametern und erzeugt das Bild – zuerst über `getImageUrl`, sonst als `data:image/png;base64,…` über `getImageDto`; `width`/`height` kommen danach vom Plugin.
* Konstruktor `PluginDto(params, name, nr, idQuestion)`: nur Tag-Name und Größe.
* `toJson()` liefert das DTO als JSON.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/score`](../../rest-schnittstelle/ApiController/score/index.md) | Request über [`PluginScoreRequestDto.pluginDto`](../../dtos/PluginScoreRequestDto/index.md) | Prüft die Eingabe eines Schülers |
| [`POST /open/loadplugindto`](../../rest-schnittstelle/ApiController/loadPluginDto/index.md) | Response | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /open/renderlatex`](../../rest-schnittstelle/ApiController/renderLatex/index.md) | Request über [`PluginRenderLatexRequestDto.pluginDto`](../../dtos/PluginRenderLatexRequestDto/index.md) | Rendert ein Plugin für den Fragedruck als LaTeX-Quelltext |
| [`POST /open/renderpluginresult`](../../rest-schnittstelle/ApiController/renderPluginResult/index.md) | Request über [`PluginRenderResultRequestDto.pluginDto`](../../dtos/PluginRenderResultRequestDto/index.md) | Rendert das Plugin inklusive der Schülereingabe und korrekter Lösung Es wird dabei entweder direkt ein HTML-Code oder LaTeX-Code erzeugt |
| [`POST /open/setconfigurationdata`](../../rest-schnittstelle/ApiController/setConfigurationData/index.md) | Response über [`PluginConfigDto.pluginDto`](../../dtos/PluginConfigDto/index.md) | Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration |
| [`POST /open/reloadplugindto`](../../rest-schnittstelle/ApiController/reloadPluginDto/index.md) | Response | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /<endpoint>/api/open/reloadplugindto`](../../rest-schnittstelle/ApiExternOpenController/reloadPluginDto/index.md) | Response | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |

## Verwendet in DTOs

* [PluginConfigDto](../../dtos/PluginConfigDto/index.md) – Feld `pluginDto`
* [PluginRenderLatexRequestDto](../../dtos/PluginRenderLatexRequestDto/index.md) – Feld `pluginDto`
* [PluginRenderResultRequestDto](../../dtos/PluginRenderResultRequestDto/index.md) – Feld `pluginDto`
* [PluginScoreRequestDto](../../dtos/PluginScoreRequestDto/index.md) – Feld `pluginDto`

## Verwendet in der Plugin-API

* [`loadPluginDto`](../../plugin-api/index.md): `PluginDto loadPluginDto(String params,` [`PluginQuestionDto`](../../dtos/PluginQuestionDto/index.md) `q, int nr)`
* [`renderLatex`](../../plugin-api/index.md): [`PluginRenderDto`](../../dtos/PluginRenderDto/index.md) `renderLatex(PluginDto pluginDto, String answer, String mode)`
* [`score`](../../plugin-api/index.md): [`PluginScoreInfoDto`](../../dtos/PluginScoreInfoDto/index.md) `score(PluginDto pluginDto, String antwort,` [`ToleranzDto`](../../dtos/ToleranzDto/index.md) `toleranz,` [`VarHashDto`](../../dtos/VarHashDto/index.md) `varsQuestion,` [`PluginAnswerDto`](../../dtos/PluginAnswerDto/index.md) `answerDto, double grade)`
* [`renderPluginResult`](../../plugin-api/index.md): [`PluginRenderDto`](../../dtos/PluginRenderDto/index.md) `renderPluginResult(boolean tex, PluginDto pluginDto, String antwort,` [`ToleranzDto`](../../dtos/ToleranzDto/index.md) `toleranz,` [`VarHashDto`](../../dtos/VarHashDto/index.md) `varsQuestion,` [`PluginAnswerDto`](../../dtos/PluginAnswerDto/index.md) `answerDto, double grade)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
