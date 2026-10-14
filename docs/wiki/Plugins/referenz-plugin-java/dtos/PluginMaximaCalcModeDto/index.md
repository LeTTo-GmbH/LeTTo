# PluginMaximaCalcModeDto
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Legt fest, ob Maxima verwendet und ob Datensatzwerte vor der Berechnung eingesetzt werden.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginMaximaCalcModeDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginMaximaCalcModeDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `maxima` | boolean | `false` | true bei Berechnung mit Maxima, false bei Berechnung mit Parser |
| `preCalc` | boolean | `true` | true wenn die Datensätze vor Maxima eingesetzt werden |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/gethtml`](../../rest-schnittstelle/ApiController/getHtml/index.md) | Request über [`PluginRequestDto.pluginMaximaCalcMode`](../../dtos/PluginRequestDto/index.md) | Berechnet den Fragetext für das Fragefeld des Webservers für die angegebenen Parameter für die Verwendung in einem PIT Tag |
| [`POST /open/angabe`](../../rest-schnittstelle/ApiController/getAngabe/index.md) | Request über [`PluginRequestDto.pluginMaximaCalcMode`](../../dtos/PluginRequestDto/index.md) | Liefert einen Angabestring für die Text-Angabe |
| [`POST /open/generatedatasets`](../../rest-schnittstelle/ApiController/generateDatasets/index.md) | Request über [`PluginRequestDto.pluginMaximaCalcMode`](../../dtos/PluginRequestDto/index.md) | Liefert alle Datensätze, welche für das Plugin in der Frage vorhanden sein sollten |
| [`POST /open/maxima`](../../rest-schnittstelle/ApiController/getMaxima/index.md) | Request über [`PluginRequestDto.pluginMaximaCalcMode`](../../dtos/PluginRequestDto/index.md) | Liefert einen Maxima-Berechnungsstring für die Berechnung des Plugins |
| [`POST /open/image`](../../rest-schnittstelle/ApiController/getImage/index.md) | Request über [`PluginRequestDto.pluginMaximaCalcMode`](../../dtos/PluginRequestDto/index.md) | Liefert ein Base64 codiertes Bild mit den angegebenen Parametern |
| [`POST /open/imageurl`](../../rest-schnittstelle/ApiController/getImageUrl/index.md) | Request über [`PluginRequestDto.pluginMaximaCalcMode`](../../dtos/PluginRequestDto/index.md) | Liefert eine öffentliche URL auf das gerenderte Bild |
| [`POST /open/imagetemplates`](../../rest-schnittstelle/ApiController/getImageTemplates/index.md) | Request über [`PluginRequestDto.pluginMaximaCalcMode`](../../dtos/PluginRequestDto/index.md) | Liefert eine Liste aller möglichen Varianten von Bildern in String-Arrays |
| [`POST /open/getvars`](../../rest-schnittstelle/ApiController/getVars/index.md) | Request über [`PluginRequestDto.pluginMaximaCalcMode`](../../dtos/PluginRequestDto/index.md) | Liefert eine Liste aller Variablen welche als Dataset benötigt werden |

## Verwendet in DTOs

* [PluginRequestDto](../../dtos/PluginRequestDto/index.md) – Feld `pluginMaximaCalcMode`

## Verwendet in der Plugin-API

* [`getMaxima`](../../plugin-api/index.md): `String getMaxima(String params,` [`PluginQuestionDto`](../../dtos/PluginQuestionDto/index.md) `q, PluginMaximaCalcModeDto pluginMaximaCalcMode )`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
