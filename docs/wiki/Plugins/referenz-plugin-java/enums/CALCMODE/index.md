# CALCMODE
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Art der Berechnung MAXIMA : Berechnung im Maxima-Feld einer Frage LOESUNG : Berechnung der Lösung aus dem Lösungsfeld EQUALS : Vergleich des Ergebnisses des Schülers mit dem Ergebnis des Lehrers VIEW : Berechnungen direkt mit Angabefeld mit {=

| | |
|---|---|
| Enum | `at.letto.plugins.enums.CALCMODE` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/enums/CALCMODE.html` |

## Werte

| Wert | Bedeutung |
|---|---|
| `MAXIMA` | Berechnung im Maxima-Feld einer Frage. |
| `LOESUNG` | Berechnung der Musterlösung. |
| `EQUALS` | Vergleich von Schülerantwort und Musterlösung. |
| `VIEW` | Berechnung eines Ausdrucks innerhalb des Angabetextes. |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/gethtml`](../../rest-schnittstelle/ApiController/getHtml/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Berechnet den Fragetext für das Fragefeld des Webservers für die angegebenen Parameter für die Verwendung in einem PIT Tag |
| [`POST /open/angabe`](../../rest-schnittstelle/ApiController/getAngabe/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert einen Angabestring für die Text-Angabe |
| [`POST /open/generatedatasets`](../../rest-schnittstelle/ApiController/generateDatasets/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert alle Datensätze, welche für das Plugin in der Frage vorhanden sein sollten |
| [`POST /open/maxima`](../../rest-schnittstelle/ApiController/getMaxima/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert einen Maxima-Berechnungsstring für die Berechnung des Plugins |
| [`POST /open/image`](../../rest-schnittstelle/ApiController/getImage/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert ein Base64 codiertes Bild mit den angegebenen Parametern |
| [`POST /open/imageurl`](../../rest-schnittstelle/ApiController/getImageUrl/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert eine öffentliche URL auf das gerenderte Bild |
| [`POST /open/imagetemplates`](../../rest-schnittstelle/ApiController/getImageTemplates/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert eine Liste aller möglichen Varianten von Bildern in String-Arrays |
| [`POST /open/parserplugin`](../../rest-schnittstelle/ApiController/parserPlugin/index.md) | Request über [`PluginParserRequestDto.cp`](../../dtos/PluginParserRequestDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 1 weiterer Weg) | Wird verwendet wenn im Lösungsfeld die Funktion plugin("pluginname",p1,p2,p3) verwendet wird |
| [`POST /open/score`](../../rest-schnittstelle/ApiController/score/index.md) | Request über [`PluginScoreRequestDto.varsQuestion`](../../dtos/PluginScoreRequestDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) | Prüft die Eingabe eines Schülers |
| [`POST /open/getvars`](../../rest-schnittstelle/ApiController/getVars/index.md) | Request über [`PluginRequestDto.q`](../../dtos/PluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Liefert eine Liste aller Variablen welche als Dataset benötigt werden |
| [`POST /open/modifyangabe`](../../rest-schnittstelle/ApiController/modifyAngabe/index.md) | Request über [`PluginAngabeRequestDto.q`](../../dtos/PluginAngabeRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | verändert einen Angabetext, der in der Angabe in PI Tags eingeschlossen wurde Die Funktion wird vor dem Darstellen der Frage ausgeführt |
| [`POST /open/modifyangabetextkomplett`](../../rest-schnittstelle/ApiController/modifyAngabeTextkomplett/index.md) | Request über [`PluginAngabeRequestDto.q`](../../dtos/PluginAngabeRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | verändert den kompletten Angabetext der Frage |
| [`POST /open/loadplugindto`](../../rest-schnittstelle/ApiController/loadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../../dtos/LoadPluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /open/renderpluginresult`](../../rest-schnittstelle/ApiController/renderPluginResult/index.md) | Request über [`PluginRenderResultRequestDto.varsQuestion`](../../dtos/PluginRenderResultRequestDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) | Rendert das Plugin inklusive der Schülereingabe und korrekter Lösung Es wird dabei entweder direkt ein HTML-Code oder LaTeX-Code erzeugt |
| [`POST /open/setconfigurationdata`](../../rest-schnittstelle/ApiController/setConfigurationData/index.md) | Request über [`PluginSetConfigurationDataRequestDto.questionDto`](../../dtos/PluginSetConfigurationDataRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration |
| [`POST /open/reloadplugindto`](../../rest-schnittstelle/ApiController/reloadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../../dtos/LoadPluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /<endpoint>/api/open/reloadplugindto`](../../rest-schnittstelle/ApiExternOpenController/reloadPluginDto/index.md) | Request über [`LoadPluginRequestDto.q`](../../dtos/LoadPluginRequestDto/index.md) → [`PluginQuestionDto.cvars`](../../dtos/PluginQuestionDto/index.md) → [`VarHashDto.vars`](../../dtos/VarHashDto/index.md) → [`VarDto.cp`](../../dtos/VarDto/index.md) → [`CalcParamsDto.calcmode`](../../dtos/CalcParamsDto/index.md) (und 3 weitere Wege) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |

## Verwendet in DTOs

* [CalcParamsDto](../../dtos/CalcParamsDto/index.md) – Feld `calcmode`

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[Enums](../index.md) · [Referenz-Plugin (Java)](../../index.md)
