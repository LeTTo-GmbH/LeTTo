# PluginScoreRequestDto
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Anfragedaten für die Bewertung einer Plugin-Antwort.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginScoreRequestDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginScoreRequestDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `typ` | String | `""` | Typ des Plugins |
| `name` | String | `""` | Name des Plugins in der Frage |
| `config` | String | `""` | Konfigurationsstring des Plugins |
| `pluginDto` | [PluginDto](../PluginDto/index.md) |  | [PluginDto](../PluginDto/index.md) welches für die JavaScript aktive Eingabe aufbereitet wurde |
| `antwort` | String |  | Antwort die der Schüler eingegeben hat |
| `toleranz` | [ToleranzDto](../ToleranzDto/index.md) |  | Toleranz für die Lösung |
| `varsQuestion` | [VarHashDto](../VarHashDto/index.md) |  | Referenz auf VarHash, wird dynamisch nachgeladen |
| `answerDto` | [PluginAnswerDto](../PluginAnswerDto/index.md) |  | korrekte Antwort und Informationen für den Scorer des Plugins (Musterlösung, nicht die Antwort des Schülers) |
| `grade` | double |  | Maximale Punktanzahl für die richtige Antwort |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/score`](../../rest-schnittstelle/ApiController/score/index.md) | Request | Prüft die Eingabe eines Schülers |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
