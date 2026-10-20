# PluginScoreInfoDto
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

ScoreInfoDto für die score-Methode von Plugins

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginScoreInfoDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginScoreInfoDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `schuelerErgebnis` | [CalcErgebnisDto](../CalcErgebnisDto/index.md) |  | Eingabe des Schülers geparst als [CalcErgebnisDto](../CalcErgebnisDto/index.md) |
| `zielEinheit` | String |  | ZielEinheit der Korrektur als String |
| `punkteIst` | double |  | Punkte IST von der Korrektur |
| `punkteSoll` | double |  | Punkte SOLL erreichbar |
| `status` | [Score](../../enums/Score/index.md) |  | Score Ergebnis als Enum-Feld |
| `htmlScoreInfo` | String |  | HTML-Text mit zusätzlichen Informationen zur Bewertung. |
| `feedback` | String |  | Feedback |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/score`](../../rest-schnittstelle/ApiController/score/index.md) | Response | Prüft die Eingabe eines Schülers |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

* [`score`](../../plugin-api/index.md): `PluginScoreInfoDto score(`[`PluginDto`](../PluginDto/index.md) `pluginDto, String antwort,` [`ToleranzDto`](../ToleranzDto/index.md) `toleranz,` [`VarHashDto`](../VarHashDto/index.md) `varsQuestion,` [`PluginAnswerDto`](../PluginAnswerDto/index.md) `answerDto, double grade)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
