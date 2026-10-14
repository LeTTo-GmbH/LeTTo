# PluginQuestionDto
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Daten die von einer Question an ein Plugin übergeben werden sollten

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginQuestionDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginQuestionDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `id` | long |  | id der Frage |
| `name` | String |  | Name der Frage |
| `maximaDefs` | String |  | Standarddefinitionen welche vor dem Durchlauf von Maxima ausgeführt werden |
| `moodlemac` | String |  | Inhalt der Moodle.mac |
| `points` | double |  | erreichbare Punkteanzahl einer Frage |
| `subQuestions` | List&lt;[PluginSubQuestionDto](../../dtos/PluginSubQuestionDto/index.md)&gt; |  | Liste aller Teilfragen der Frage |
| `maxima` | String |  | Haupt-Maxima-Feld der Frage |
| `images` | List&lt;String&gt; |  | Liste aller Dateinamen (md5-Prüfsumme.extension) aller Bilder |
| `imagesContent` | List&lt;String&gt; |  | Liste aller Bilder entweder Base64 codiert (mit base64:beginnend) oder als externe URL(mit http:// oder https:// beginnend!!) oder als reiner Text (mit text:beginnend wenn die Datei eine reine Textdatei ist) vorzugsweise wird die externe URL verwendet, nur wenn dem Server bekannt ist, dass das Plugin nicht selbst auf die externe Url der Images zugreifen kann UND die Dateien vom Plugin nicht direkt über das Dateisystem erreichbar sind (externe Plugins) wird base64: oder text: verwendet |
| `dsNr` | int |  | Nummer des aktuellen Datensatzes |
| `vars` | [VarHashDto](../../dtos/VarHashDto/index.md) |  | Werte alle gesetzten Datensatz-Variablen |
| `cvars` | [VarHashDto](../../dtos/VarHashDto/index.md) |  | Konstante und Variablen welche als Datensatz definiert sind kombiniert in einem Hash |
| `varsMaxima` | [VarHashDto](../../dtos/VarHashDto/index.md) |  | Ergebnisse aller Maxima-Berechnungen ohne eingesetzte Datensatz-Variable |
| `mvars` | [VarHashDto](../../dtos/VarHashDto/index.md) |  | Konstante, Variablen welche als Datensatz definiert und Maxima-Ergebnisse mit eingesetzten Werten kombiniert in einem Hash |

## Hinweise

* `clone()` liefert eine flache Kopie.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/gethtml`](../../rest-schnittstelle/ApiController/getHtml/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) | Berechnet den Fragetext für das Fragefeld des Webservers für die angegebenen Parameter für die Verwendung in einem PIT Tag |
| [`POST /open/angabe`](../../rest-schnittstelle/ApiController/getAngabe/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) | Liefert einen Angabestring für die Text-Angabe |
| [`POST /open/generatedatasets`](../../rest-schnittstelle/ApiController/generateDatasets/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) | Liefert alle Datensätze, welche für das Plugin in der Frage vorhanden sein sollten |
| [`POST /open/maxima`](../../rest-schnittstelle/ApiController/getMaxima/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) | Liefert einen Maxima-Berechnungsstring für die Berechnung des Plugins |
| [`POST /open/image`](../../rest-schnittstelle/ApiController/getImage/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) | Liefert ein Base64 codiertes Bild mit den angegebenen Parametern |
| [`POST /open/imageurl`](../../rest-schnittstelle/ApiController/getImageUrl/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) | Liefert eine öffentliche URL auf das gerenderte Bild |
| [`POST /open/imagetemplates`](../../rest-schnittstelle/ApiController/getImageTemplates/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) | Liefert eine Liste aller möglichen Varianten von Bildern in String-Arrays |
| [`POST /open/getvars`](../../rest-schnittstelle/ApiController/getVars/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) | Liefert eine Liste aller Variablen welche als Dataset benötigt werden |
| [`POST /open/modifyangabe`](../../rest-schnittstelle/ApiController/modifyAngabe/index.md) | Request über [`PluginAngabeRequestDto.q`](../../dtos/PluginAngabeRequestDto/index.md) | verändert einen Angabetext, der in der Angabe in PI Tags eingeschlossen wurde Die Funktion wird vor dem Darstellen der Frage ausgeführt |
| [`POST /open/modifyangabetextkomplett`](../../rest-schnittstelle/ApiController/modifyAngabeTextkomplett/index.md) | Request über [`PluginAngabeRequestDto.q`](../../dtos/PluginAngabeRequestDto/index.md) | verändert den kompletten Angabetext der Frage |
| [`POST /open/loadplugindto`](../../rest-schnittstelle/ApiController/loadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../../dtos/LoadPluginRequestDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /open/setconfigurationdata`](../../rest-schnittstelle/ApiController/setConfigurationData/index.md) | Request über [`PluginSetConfigurationDataRequestDto.questionDto`](../../dtos/PluginSetConfigurationDataRequestDto/index.md) | Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration |
| [`POST /open/reloadplugindto`](../../rest-schnittstelle/ApiController/reloadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../../dtos/LoadPluginRequestDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /<endpoint>/api/open/reloadplugindto`](../../rest-schnittstelle/ApiExternOpenController/reloadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../../dtos/LoadPluginRequestDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |

## Verwendet in DTOs

* [LoadPluginRequestDto](../../dtos/LoadPluginRequestDto/index.md) – Feld `q`
* [PluginAngabeRequestDto](../../dtos/PluginAngabeRequestDto/index.md) – Feld `q`
* [PluginConfigurationConnection](../../dtos/PluginConfigurationConnection/index.md) – Feld `pluginQuestionDto`
* [PluginRequestDto](../../dtos/PluginRequestDto/index.md) – Feld `q`
* [PluginSetConfigurationDataRequestDto](../../dtos/PluginSetConfigurationDataRequestDto/index.md) – Feld `questionDto`

## Verwendet in der Plugin-API

* [`getHTML`](../../plugin-api/index.md): `String getHTML(String params, PluginQuestionDto q)`
* [`getMaxima`](../../plugin-api/index.md): `String getMaxima(String params, PluginQuestionDto q,` [`PluginMaximaCalcModeDto`](../../dtos/PluginMaximaCalcModeDto/index.md) `pluginMaximaCalcMode )`
* [`parseDrawParams`](../../plugin-api/index.md): `void parseDrawParams(String params,PluginQuestionDto q,` [`PluginImageResultDto`](../../dtos/PluginImageResultDto/index.md) `pluginImageResultDto)`
* [`getImageDto`](../../plugin-api/index.md): [`ImageBase64Dto`](../../dtos/ImageBase64Dto/index.md) `getImageDto(String params, PluginQuestionDto q)`
* [`getImageUrl`](../../plugin-api/index.md): [`ImageUrlDto`](../../dtos/ImageUrlDto/index.md) `getImageUrl(String params, PluginQuestionDto q)`
* [`getPluginImageDescription`](../../plugin-api/index.md): `String getPluginImageDescription(String imageParams, PluginQuestionDto q)`
* [`loadPluginDto`](../../plugin-api/index.md): [`PluginDto`](../../dtos/PluginDto/index.md) `loadPluginDto(String params, PluginQuestionDto q, int nr)`
* [`modifyAngabe`](../../plugin-api/index.md): `String modifyAngabe(String text, PluginQuestionDto q)`
* [`modifyAngabeTextkomplett`](../../plugin-api/index.md): `String modifyAngabeTextkomplett(String text, PluginQuestionDto q)`
* [`setConfigurationData`](../../plugin-api/index.md): [`PluginConfigDto`](../../dtos/PluginConfigDto/index.md) `setConfigurationData(String configuration, PluginQuestionDto questionDto)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
