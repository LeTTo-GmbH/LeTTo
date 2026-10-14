# PluginSubQuestionDto
<!-- generiert aus plugin-demo-java @ f0143d1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Daten die von einer SubQuestion an ein Plugin übergeben werden sollten

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginSubQuestionDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginSubQuestionDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `name` | String |  | Name der SubQuestion |
| `points` | double |  | die erreichbare Punkteanzahl einer Teilfrage |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/gethtml`](../../rest-schnittstelle/ApiController/getHtml/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Berechnet den Fragetext für das Fragefeld des Webservers für die angegebenen Parameter für die Verwendung in einem PIT Tag |
| [`POST /open/angabe`](../../rest-schnittstelle/ApiController/getAngabe/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Liefert einen Angabestring für die Text-Angabe |
| [`POST /open/generatedatasets`](../../rest-schnittstelle/ApiController/generateDatasets/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Liefert alle Datensätze, welche für das Plugin in der Frage vorhanden sein sollten |
| [`POST /open/maxima`](../../rest-schnittstelle/ApiController/getMaxima/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Liefert einen Maxima-Berechnungsstring für die Berechnung des Plugins |
| [`POST /open/image`](../../rest-schnittstelle/ApiController/getImage/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Liefert ein Base64 codiertes Bild mit den angegebenen Parametern |
| [`POST /open/imageurl`](../../rest-schnittstelle/ApiController/getImageUrl/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Liefert eine öffentliche URL auf das gerenderte Bild |
| [`POST /open/imagetemplates`](../../rest-schnittstelle/ApiController/getImageTemplates/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Liefert eine Liste aller möglichen Varianten von Bildern in String-Arrays |
| [`POST /open/getvars`](../../rest-schnittstelle/ApiController/getVars/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Liefert eine Liste aller Variablen welche als Dataset benötigt werden |
| [`POST /open/modifyangabe`](../../rest-schnittstelle/ApiController/modifyAngabe/index.md) | Request über [`PluginAngabeRequestDto.q`](../../dtos/PluginAngabeRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | verändert einen Angabetext, der in der Angabe in PI Tags eingeschlossen wurde Die Funktion wird vor dem Darstellen der Frage ausgeführt |
| [`POST /open/modifyangabetextkomplett`](../../rest-schnittstelle/ApiController/modifyAngabeTextkomplett/index.md) | Request über [`PluginAngabeRequestDto.q`](../../dtos/PluginAngabeRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | verändert den kompletten Angabetext der Frage |
| [`POST /open/loadplugindto`](../../rest-schnittstelle/ApiController/loadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../../dtos/LoadPluginRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /open/setconfigurationdata`](../../rest-schnittstelle/ApiController/setConfigurationData/index.md) | Request über [`PluginSetConfigurationDataRequestDto.questionDto`](../../dtos/PluginSetConfigurationDataRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration |
| [`POST /open/reloadplugindto`](../../rest-schnittstelle/ApiController/reloadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../../dtos/LoadPluginRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /<endpoint>/api/open/reloadplugindto`](../../rest-schnittstelle/ApiExternOpenController/reloadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../../dtos/LoadPluginRequestDto/index.md) → [`PluginQuestionDto.subQuestions`](../../dtos/PluginQuestionDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |

## Verwendet in DTOs

* [PluginQuestionDto](../../dtos/PluginQuestionDto/index.md) – Feld `subQuestions`

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
