# PluginAnswerDto
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

korrekte Antwort und Informationen für den Scorer des Plugins

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginAnswerDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginAnswerDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `ergebnis` | [CalcErgebnisDto](../CalcErgebnisDto/index.md) |  | korrektes Ergebnis |
| `answerText` | String |  | korrekte Antwort aus der Frage als String |
| `ze` | String |  | Zieleinheit für die Korrektur |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/score`](../../rest-schnittstelle/ApiController/score/index.md) | Request über [`PluginScoreRequestDto.answerDto`](../PluginScoreRequestDto/index.md) | Prüft die Eingabe eines Schülers |
| [`POST /open/renderpluginresult`](../../rest-schnittstelle/ApiController/renderPluginResult/index.md) | Request über [`PluginRenderResultRequestDto.answerDto`](../PluginRenderResultRequestDto/index.md) | Rendert das Plugin inklusive der Schülereingabe und korrekter Lösung Es wird dabei entweder direkt ein HTML-Code oder LaTeX-Code erzeugt |

## Verwendet in DTOs

* [PluginRenderResultRequestDto](../PluginRenderResultRequestDto/index.md) – Feld `answerDto`
* [PluginScoreRequestDto](../PluginScoreRequestDto/index.md) – Feld `answerDto`

## Verwendet in der Plugin-API

* [`score`](../../plugin-api/index.md): [`PluginScoreInfoDto`](../PluginScoreInfoDto/index.md) `score(`[`PluginDto`](../PluginDto/index.md) `pluginDto, String antwort,` [`ToleranzDto`](../ToleranzDto/index.md) `toleranz,` [`VarHashDto`](../VarHashDto/index.md) `varsQuestion, PluginAnswerDto answerDto, double grade)`
* [`renderPluginResult`](../../plugin-api/index.md): [`PluginRenderDto`](../PluginRenderDto/index.md) `renderPluginResult(boolean tex,` [`PluginDto`](../PluginDto/index.md) `pluginDto, String antwort,` [`ToleranzDto`](../ToleranzDto/index.md) `toleranz,` [`VarHashDto`](../VarHashDto/index.md) `varsQuestion, PluginAnswerDto answerDto, double grade)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
