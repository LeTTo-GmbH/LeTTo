# Score
<!-- generiert aus plugin-demo-java @ f0143d1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Ergebnis einer Fragen-Beurteilung NotScored : nicht bewertet, da das richtige Ergebnis nicht bekannt ist. zB bei Freitextfragen OK : Antwort ist richtig FALSCH : Antwort ist falsch TEILWEISE_OK : Antwort ist teilweise richtig EINHEITENFEHLER : Antwort hat einen Einheitenfehler OK_Lehrer : Das Ergebnis wurde vom Lehrer händisch als richtig beurteilt FALSCH_Lehrer : Das Ergebnis wurde vom Lehrer händisch als falsch beurteilt TEILWEISE_OK_Lehrer : Das Ergebnis wurde vom Lehrer händisch als teilweise richtig beurteilt EINHEITENFEHLER_Lehrer : Im Ergebnis der Beispielangabe ist ein Einheitenfehler ANGABEFEHLER_EH : Das Ergebnis der Beispielangabe kann wegen eines Rechenfehlers nicht berechnet werden PARSERFEHLER_SYSTEM : Der Parser kann das richtige Ergebnis nicht berechnen NichtEntschieden : Calculated: die Bewertung ist noch nicht entschieden, da das Ergebnis nicht gepasst hat. Sind alle Answers einer Frage nicht entschieden, so ist die Antwort falsch

| | |
|---|---|
| Enum | `at.letto.plugins.enums.Score` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/enums/Score.html` |

## Werte

| Wert | Bedeutung |
|---|---|
| `NotScored` | nicht bewertet, da das richtige Ergebnis nicht bekannt ist. zB bei Freitextfragen |
| `OK` | Antwort ist richtig |
| `FALSCH` | Antwort ist falsch |
| `TEILWEISE_OK` | Antwort ist teilweise richtig |
| `EINHEITENFEHLER` | Antwort hat einen Einheitenfehler |
| `OK_Lehrer` | Das Ergebnis wurde vom Lehrer händisch als richtig beurteilt |
| `FALSCH_Lehrer` | Das Ergebnis wurde vom Lehrer händisch als falsch beurteilt |
| `TEILWEISE_OK_Lehrer` | Das Ergebnis wurde vom Lehrer händisch als teilweise richtig beurteilt |
| `EINHEITENFEHLER_Lehrer` | Im Ergebnis der Beispielangabe ist ein Einheitenfehler |
| `ANGABEFEHLER_EH` | Das Ergebnis der Beispielangabe kann wegen eines Rechenfehlers nicht berechnet werden |
| `PARSERFEHLER_SYSTEM` | Der Parser kann das richtige Ergebnis nicht berechnen |
| `NichtEntschieden` | Calculated: die Bewertung ist noch nicht entschieden, da das Ergebnis nicht gepasst hat. Sind alle Answers einer Frage nicht entschieden, so ist die Antwort falsch |
| `MEHRFACHANTWORT_OK` | Mehrfachbeantwortung der Frage, Antwort richtig |
| `MEHRFACHANTWORT_OK_LEHRER` | Mehrfachbeantwortung der Frage, Antwort richtig, vom Lehrer definiert |
| `MEHRFACHANTWORT_TW_RICHTIG` | Mehrfachbeantwortung der Frage, Antwort tw. richtig |
| `MEHRFACHANTWORT_TW_RICHTIG_LEHRER` | Mehrfachbeantwortung der Frage, Antwort tw. richtig, Lehrerbeurteilung |

## Hinweise

* Neue Werte dürfen nur hinten angefügt werden (Kommentar im Code).
* `getScoreTexColor()` liefert die LaTeX-Farbe des Status, `htmlColor(text)` formatiert HTML-Text farbig (grün richtig, gelb teilweise, rot falsch, magenta Angabe-/Systemfehler).

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/score`](../../rest-schnittstelle/ApiController/score/index.md) | Response über [`PluginScoreInfoDto.status`](../../dtos/PluginScoreInfoDto/index.md) | Prüft die Eingabe eines Schülers |

## Verwendet in DTOs

* [PluginScoreInfoDto](../../dtos/PluginScoreInfoDto/index.md) – Feld `status`

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[Enums](../index.md) · [Referenz-Plugin (Java)](../../index.md)
