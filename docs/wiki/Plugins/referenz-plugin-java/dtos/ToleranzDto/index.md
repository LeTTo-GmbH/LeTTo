# ToleranzDto
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Beschreibt Wert und Modus der Toleranz bei der Antwortbewertung.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.ToleranzDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/ToleranzDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `toleranz` | double |  | Wert der Toleranz als Absolutwert, oder als relativer Wert (bei 1Prozent ist toleranz=0.01) |
| `mode` | [TOLERANZMODE](../../enums/TOLERANZMODE/index.md) |  | RELATIV : Die Toleranz wird relativ zum größeren Wert des Vergleiches bestimmt ABSOLUT : Die Toleranz wird absolut angegeben und ist von den Werten unabhängig |

## Hinweise

* Der Standardkonstruktor erzeugt eine relative Toleranz von `1e-10`.
* `relativ()` / `absolut()` prüfen den Modus.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/gethtml`](../../rest-schnittstelle/ApiController/getHtml/index.md) | Request über [`PluginRequestDto.q`](../PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Berechnet den Fragetext für das Fragefeld des Webservers für die angegebenen Parameter für die Verwendung in einem PIT Tag |
| [`POST /open/angabe`](../../rest-schnittstelle/ApiController/getAngabe/index.md) | Request über [`PluginRequestDto.q`](../PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert einen Angabestring für die Text-Angabe |
| [`POST /open/generatedatasets`](../../rest-schnittstelle/ApiController/generateDatasets/index.md) | Request über [`PluginRequestDto.q`](../PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert alle Datensätze, welche für das Plugin in der Frage vorhanden sein sollten |
| [`POST /open/maxima`](../../rest-schnittstelle/ApiController/getMaxima/index.md) | Request über [`PluginRequestDto.q`](../PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert einen Maxima-Berechnungsstring für die Berechnung des Plugins |
| [`POST /open/image`](../../rest-schnittstelle/ApiController/getImage/index.md) | Request über [`PluginRequestDto.q`](../PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert ein Base64 codiertes Bild mit den angegebenen Parametern |
| [`POST /open/imageurl`](../../rest-schnittstelle/ApiController/getImageUrl/index.md) | Request über [`PluginRequestDto.q`](../PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert eine öffentliche URL auf das gerenderte Bild |
| [`POST /open/imagetemplates`](../../rest-schnittstelle/ApiController/getImageTemplates/index.md) | Request über [`PluginRequestDto.q`](../PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert eine Liste aller möglichen Varianten von Bildern in String-Arrays |
| [`POST /open/parserplugin`](../../rest-schnittstelle/ApiController/parserPlugin/index.md) | Request über [`PluginParserRequestDto.cp`](../PluginParserRequestDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 1 weiterer Weg) | Wird verwendet wenn im Lösungsfeld die Funktion plugin("pluginname",p1,p2,p3) verwendet wird |
| [`POST /open/score`](../../rest-schnittstelle/ApiController/score/index.md) | Request über [`PluginScoreRequestDto.toleranz`](../PluginScoreRequestDto/index.md) (und 1 weiterer Weg) | Prüft die Eingabe eines Schülers |
| [`POST /open/getvars`](../../rest-schnittstelle/ApiController/getVars/index.md) | Request über [`PluginRequestDto.q`](../PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert eine Liste aller Variablen welche als Dataset benötigt werden |
| [`POST /open/modifyangabe`](../../rest-schnittstelle/ApiController/modifyAngabe/index.md) | Request über [`PluginAngabeRequestDto.q`](../PluginAngabeRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | verändert einen Angabetext, der in der Angabe in PI Tags eingeschlossen wurde Die Funktion wird vor dem Darstellen der Frage ausgeführt |
| [`POST /open/modifyangabetextkomplett`](../../rest-schnittstelle/ApiController/modifyAngabeTextkomplett/index.md) | Request über [`PluginAngabeRequestDto.q`](../PluginAngabeRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | verändert den kompletten Angabetext der Frage |
| [`POST /open/loadplugindto`](../../rest-schnittstelle/ApiController/loadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../LoadPluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /open/renderpluginresult`](../../rest-schnittstelle/ApiController/renderPluginResult/index.md) | Request über [`PluginRenderResultRequestDto.toleranz`](../PluginRenderResultRequestDto/index.md) (und 1 weiterer Weg) | Rendert das Plugin inklusive der Schülereingabe und korrekter Lösung Es wird dabei entweder direkt ein HTML-Code oder LaTeX-Code erzeugt |
| [`POST /open/setconfigurationdata`](../../rest-schnittstelle/ApiController/setConfigurationData/index.md) | Request über [`PluginSetConfigurationDataRequestDto.questionDto`](../PluginSetConfigurationDataRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration |
| [`POST /open/reloadplugindto`](../../rest-schnittstelle/ApiController/reloadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../LoadPluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /<endpoint>/api/open/reloadplugindto`](../../rest-schnittstelle/ApiExternOpenController/reloadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../LoadPluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../PluginQuestionDto/index.md) → [`VarHashDto.vars`](../VarHashDto/index.md) → [`VarDto.cp`](../VarDto/index.md) → [`CalcParamsDto.toleranz`](../CalcParamsDto/index.md) (und 3 weitere Wege) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |

## Verwendet in DTOs

* [CalcParamsDto](../CalcParamsDto/index.md) – Feld `toleranz`
* [PluginRenderResultRequestDto](../PluginRenderResultRequestDto/index.md) – Feld `toleranz`
* [PluginScoreRequestDto](../PluginScoreRequestDto/index.md) – Feld `toleranz`

## Verwendet in der Plugin-API

* [`score`](../../plugin-api/index.md): [`PluginScoreInfoDto`](../PluginScoreInfoDto/index.md) `score(`[`PluginDto`](../PluginDto/index.md) `pluginDto, String antwort, ToleranzDto toleranz,` [`VarHashDto`](../VarHashDto/index.md) `varsQuestion,` [`PluginAnswerDto`](../PluginAnswerDto/index.md) `answerDto, double grade)`
* [`renderPluginResult`](../../plugin-api/index.md): [`PluginRenderDto`](../PluginRenderDto/index.md) `renderPluginResult(boolean tex,` [`PluginDto`](../PluginDto/index.md) `pluginDto, String antwort, ToleranzDto toleranz,` [`VarHashDto`](../VarHashDto/index.md) `varsQuestion,` [`PluginAnswerDto`](../PluginAnswerDto/index.md) `answerDto, double grade)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
