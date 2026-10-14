# ApiController
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

REST-Schnittstelle des Plugins zwischen LeTTo und Plugin (nur aus dem Docker-Netzwerk erreichbar)

| | |
|---|---|
| Klasse | `at.letto.plugins.controller.ApiController` |
| Basispfad | `/open` |
| Erreichbarkeit | nur im Docker-Netzwerk (`http://letto-<endpoint>.nw-letto:8080/open/...`) |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/controller/ApiController.html` |

## Endpunkte

| Methode | Pfad | Request | Response | Beschreibung |
|---|---|---|---|---|
| GET | [`/open/pluginlist`](pluginList/index.md) | – | List&lt;String&gt; | Liefert eine Liste aller Plugins (Pluginnamen) , welche mit diesem Service verwaltet werden |
| GET | [`/open/generalinfolist`](pluginGeneralInfoList/index.md) | – | [PluginGeneralInfoList](../../dtos/PluginGeneralInfoList/index.md) | Liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services |
| POST | [`/open/generalinfo`](pluginGeneralInfo/index.md) | String | [PluginGeneralInfo](../../dtos/PluginGeneralInfo/index.md) | Liefert die allgemeinen Konfigurationsinformationen zu einem Plugin |
| POST | [`/open/gethtml`](getHtml/index.md) | [PluginRequestDto](../../dtos/PluginRequestDto/index.md) | String | Berechnet den Fragetext für das Fragefeld des Webservers für die angegebenen Parameter für die Verwendung in einem PIT Tag |
| POST | [`/open/angabe`](getAngabe/index.md) | [PluginRequestDto](../../dtos/PluginRequestDto/index.md) | String | Liefert einen Angabestring für die Text-Angabe |
| POST | [`/open/generatedatasets`](generateDatasets/index.md) | [PluginRequestDto](../../dtos/PluginRequestDto/index.md) | [PluginDatasetListDto](../../dtos/PluginDatasetListDto/index.md) | Liefert alle Datensätze, welche für das Plugin in der Frage vorhanden sein sollten |
| POST | [`/open/maxima`](getMaxima/index.md) | [PluginRequestDto](../../dtos/PluginRequestDto/index.md) | String | Liefert einen Maxima-Berechnungsstring für die Berechnung des Plugins |
| POST | [`/open/image`](getImage/index.md) | [PluginRequestDto](../../dtos/PluginRequestDto/index.md) | [ImageBase64Dto](../../dtos/ImageBase64Dto/index.md) | Liefert ein Base64 codiertes Bild mit den angegebenen Parametern |
| POST | [`/open/imageurl`](getImageUrl/index.md) | [PluginRequestDto](../../dtos/PluginRequestDto/index.md) | [ImageUrlDto](../../dtos/ImageUrlDto/index.md) | Liefert eine öffentliche URL auf das gerenderte Bild |
| POST | [`/open/imagetemplates`](getImageTemplates/index.md) | [PluginRequestDto](../../dtos/PluginRequestDto/index.md) | Vector&lt;String[]&gt; | Liefert eine Liste aller möglichen Varianten von Bildern in String-Arrays |
| POST | [`/open/parserplugin`](parserPlugin/index.md) | [PluginParserRequestDto](../../dtos/PluginParserRequestDto/index.md) | [CalcErgebnisDto](../../dtos/CalcErgebnisDto/index.md) | Wird verwendet wenn im Lösungsfeld die Funktion plugin("pluginname",p1,p2,p3) verwendet wird |
| POST | [`/open/parserplugineinheit`](parserPluginEinheit/index.md) | [PluginEinheitRequestDto](../../dtos/PluginEinheitRequestDto/index.md) | String | Bestimmt die Recheneinheit, welche bei der Methode parserPlugin als Ergebnis herauskommt wenn die Parameter die Einheiten wie in der Liste p haben |
| POST | [`/open/score`](score/index.md) | [PluginScoreRequestDto](../../dtos/PluginScoreRequestDto/index.md) | [PluginScoreInfoDto](../../dtos/PluginScoreInfoDto/index.md) | Prüft die Eingabe eines Schülers |
| POST | [`/open/getvars`](getVars/index.md) | [PluginRequestDto](../../dtos/PluginRequestDto/index.md) | Vector&lt;String&gt; | Liefert eine Liste aller Variablen welche als Dataset benötigt werden |
| POST | [`/open/modifyangabe`](modifyAngabe/index.md) | [PluginAngabeRequestDto](../../dtos/PluginAngabeRequestDto/index.md) | String | verändert einen Angabetext, der in der Angabe in PI Tags eingeschlossen wurde Die Funktion wird vor dem Darstellen der Frage ausgeführt |
| POST | [`/open/modifyangabetextkomplett`](modifyAngabeTextkomplett/index.md) | [PluginAngabeRequestDto](../../dtos/PluginAngabeRequestDto/index.md) | String | verändert den kompletten Angabetext der Frage |
| POST | [`/open/updatepluginstringjavascript`](updatePluginstringJavascript/index.md) | [PluginUpdateJavascriptRequestDto](../../dtos/PluginUpdateJavascriptRequestDto/index.md) | String | Passt die Plugindefinition an die Eingabe aus dem JavaScript-Result an |
| POST | [`/open/loadplugindto`](loadPluginDto/index.md) | [LoadPluginRequestDto](../../dtos/LoadPluginRequestDto/index.md) | [PluginDto](../../dtos/PluginDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| POST | [`/open/renderlatex`](renderLatex/index.md) | [PluginRenderLatexRequestDto](../../dtos/PluginRenderLatexRequestDto/index.md) | [PluginRenderDto](../../dtos/PluginRenderDto/index.md) | Rendert ein Plugin für den Fragedruck als LaTeX-Quelltext |
| POST | [`/open/renderpluginresult`](renderPluginResult/index.md) | [PluginRenderResultRequestDto](../../dtos/PluginRenderResultRequestDto/index.md) | [PluginRenderDto](../../dtos/PluginRenderDto/index.md) | Rendert das Plugin inklusive der Schülereingabe und korrekter Lösung Es wird dabei entweder direkt ein HTML-Code oder LaTeX-Code erzeugt |
| POST | [`/open/configurationinfo`](configurationInfo/index.md) | [PluginConfigurationInfoRequestDto](../../dtos/PluginConfigurationInfoRequestDto/index.md) | [PluginConfigurationInfoDto](../../dtos/PluginConfigurationInfoDto/index.md) | Liefert die Informationen welche notwendig sind um einen Konfigurationsdialog zu starten Ist die configurationID gesetzt wird eine Konfiguration gestartet und damit auch die restlichen Endpoints für die Konfiguration aktiviert |
| POST | [`/open/setconfigurationdata`](setConfigurationData/index.md) | [PluginSetConfigurationDataRequestDto](../../dtos/PluginSetConfigurationDataRequestDto/index.md) | [PluginConfigDto](../../dtos/PluginConfigDto/index.md) | Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration |
| POST | [`/open/getconfiguration`](getConfiguration/index.md) | [PluginConfigurationRequestDto](../../dtos/PluginConfigurationRequestDto/index.md) | String | Liefert die aktuelle Konfiguration eines Plugins welches sich gerade in einem CONFIGMODE_URL Konfigurationsdialog befindet |
| POST | [`/open/reloadplugindto`](reloadPluginDto/index.md) | [LoadPluginRequestDto](../../dtos/LoadPluginRequestDto/index.md) | [PluginDto](../../dtos/PluginDto/index.md) | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |

## Hinweise

* Für jede Anfrage wird mit `typ`, `name` und `config` eine neue Plugin-Instanz erzeugt; kann der Typ nicht erzeugt werden, antwortet der Endpunkt mit 404.
* Die Endpunkte für den Konfigurationsdialog (`configurationinfo`, `setconfigurationdata`, `getconfiguration`, `reloadplugindto`) arbeiten mit einer Sitzung, die über die `configurationID` identifiziert wird.


[REST-Schnittstelle](../index.md) · [Referenz-Plugin (Java)](../../index.md)
