# DTOs des Referenz-Plugins
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

* Paket `at.letto.plugins.dto`; die DTOs werden als JSON übertragen, Feldnamen im JSON entsprechen den Java-Feldnamen.
* Getter/Setter und Konstruktoren erzeugt Lombok.
* Jede Seite listet die Felder und alle Endpunkte, in denen das DTO direkt oder verschachtelt vorkommt.
* Die Enums sind unter [Enums](../enums/index.md) beschrieben.

## Request-DTOs

| DTO | Beschreibung | Endpunkte |
|---|---|---|
| [PluginRequestDto](PluginRequestDto/index.md) | Anfragedaten für die Auswahl eines Plugins anhand von Typ, Name und Konfiguration | 8 |
| [LoadPluginRequestDto](LoadPluginRequestDto/index.md) | Anfragedaten für das Laden eines Plugin-DTOs | 3 |
| [PluginAngabeRequestDto](PluginAngabeRequestDto/index.md) | Anfragedaten für die Verarbeitung eines Angabetextes | 2 |
| [PluginParserRequestDto](PluginParserRequestDto/index.md) | Anfragedaten für die Auswertung einer Plugin-Parserfunktion | 1 |
| [PluginEinheitRequestDto](PluginEinheitRequestDto/index.md) | Anfragedaten für die Bestimmung der Ergebniseinheit | 1 |
| [PluginScoreRequestDto](PluginScoreRequestDto/index.md) | Anfragedaten für die Bewertung einer Plugin-Antwort | 1 |
| [PluginRenderResultRequestDto](PluginRenderResultRequestDto/index.md) | Anfragedaten für die Darstellung einer bewerteten Antwort | 1 |
| [PluginRenderLatexRequestDto](PluginRenderLatexRequestDto/index.md) | Anfragedaten für die LaTeX-Ausgabe eines Plugins | 1 |
| [PluginUpdateJavascriptRequestDto](PluginUpdateJavascriptRequestDto/index.md) | Anfragedaten für die Aktualisierung einer Plugin-Definition anhand der JavaScript-Eingabe | 1 |
| [PluginConfigurationInfoRequestDto](PluginConfigurationInfoRequestDto/index.md) | Anfragedaten für das Öffnen einer Plugin-Konfiguration | 1 |
| [PluginSetConfigurationDataRequestDto](PluginSetConfigurationDataRequestDto/index.md) | Anfragedaten für die Übermittlung von Konfigurationsdaten | 1 |
| [PluginConfigurationRequestDto](PluginConfigurationRequestDto/index.md) | Anfragedaten für das Abfragen einer Plugin-Konfiguration | 1 |

## Frage und Variablen

| DTO | Beschreibung | Endpunkte |
|---|---|---|
| [PluginQuestionDto](PluginQuestionDto/index.md) | Daten die von einer Question an ein Plugin übergeben werden sollten | 14 |
| [PluginSubQuestionDto](PluginSubQuestionDto/index.md) | Daten die von einer SubQuestion an ein Plugin übergeben werden sollten | 14 |
| [VarHashDto](VarHashDto/index.md) | VarHash für den Transport in Rest-Services | 17 |
| [VarDto](VarDto/index.md) | Ein Eintrag eines VarHashes für die Übertragung in einem Rest-Service | 17 |
| [CalcErgebnisDto](CalcErgebnisDto/index.md) | Speichert ein CalcErgebnis als Dto um über eine Rest- oder Service-Schittstelle zu übertragen | 17 |
| [CalcParamsDto](CalcParamsDto/index.md) | Berechnungsparameter für Parser, Zahlendarstellung und Toleranzvergleich | 17 |
| [ToleranzDto](ToleranzDto/index.md) | Beschreibt Wert und Modus der Toleranz bei der Antwortbewertung | 17 |
| [PluginMaximaCalcModeDto](PluginMaximaCalcModeDto/index.md) | Legt fest, ob Maxima verwendet und ob Datensatzwerte vor der Berechnung eingesetzt werden | 8 |

## Plugin-Informationen

| DTO | Beschreibung | Endpunkte |
|---|---|---|
| [PluginGeneralInfo](PluginGeneralInfo/index.md) | Liefert allgemein Informationen zu einem Plugin, welche ohne Definition einer Plugin-Instanz allgemein gültig sind | 4 |
| [PluginGeneralInfoList](PluginGeneralInfoList/index.md) | Liefert allgemein Informationen zu einem Plugin, welche ohne Definition einer Plugin-Instanz allgemein gültig sind | 2 |
| [JavascriptLibrary](JavascriptLibrary/index.md) | Beschreibt eine JavaScript-Bibliothek als lokale Ressource, Serverdatei oder Quelltext | 4 |

## Darstellung und Bilder

| DTO | Beschreibung | Endpunkte |
|---|---|---|
| [PluginDto](PluginDto/index.md) | Dto welches vom Plugin über Letto zum JavaScript des Plugins geschickt wird | 7 |
| [PluginRenderDto](PluginRenderDto/index.md) | Enthält gerenderten HTML- oder LaTeX-Code und die zugehörigen Bilder | 2 |
| [ImageBase64Dto](ImageBase64Dto/index.md) | image with image-information of an image-file which is coded in base64 | 1 |
| [ImageUrlDto](ImageUrlDto/index.md) | image with image-information of an image-file at an open Url | 1 |
| [ImageInfoDto](ImageInfoDto/index.md) | Information of an Image which is stored in the Image-Service or returned from other service | 2 |
| [PluginImageResultDto](PluginImageResultDto/index.md) | Sammelt Status und Fehlermeldungen der Plugin-Bilderzeugung | 0 |

## Bewertung

| DTO | Beschreibung | Endpunkte |
|---|---|---|
| [PluginAnswerDto](PluginAnswerDto/index.md) | korrekte Antwort und Informationen für den Scorer des Plugins | 2 |
| [PluginScoreInfoDto](PluginScoreInfoDto/index.md) | ScoreInfoDto für die score-Methode von Plugins | 1 |

## Datensätze

| DTO | Beschreibung | Endpunkte |
|---|---|---|
| [PluginDatasetDto](PluginDatasetDto/index.md) | Informationen über einen Dataset welcher vom Plugin angeforder werden kann | 1 |
| [PluginDatasetListDto](PluginDatasetListDto/index.md) | Informationen über einen Dataset welcher vom Plugin angeforder werden kann | 1 |

## Konfiguration

| DTO | Beschreibung | Endpunkte |
|---|---|---|
| [PluginConfigurationInfoDto](PluginConfigurationInfoDto/index.md) | Information vom Plugin an LeTTo welche Informationen für die Konfiguration des Plugins benötigt werden und wie die Konfiguration des Plugins erfolgen soll | 1 |
| [PluginConfigDto](PluginConfigDto/index.md) | Dto welches vom Plugin über Letto zum JavaScript der Konfiguration des Plugins geschickt wird | 1 |

## Service und Registrierung

| DTO | Beschreibung | Endpunkte |
|---|---|---|
| [ConfigServiceDto](ConfigServiceDto/index.md) | Service welches im Setup-Service registriert ist | 1 |
| [RegisterServiceResultDto](RegisterServiceResultDto/index.md) | Ergebnis der Registratur eines Services | 1 |
| [ServiceInfoDTO](ServiceInfoDTO/index.md) | Überträgt allgemeine Service-Informationen und Angaben zur Laufzeitumgebung | 2 |
| [AdminInfoDto](AdminInfoDto/index.md) | Information über ein Service für den Admin | 2 |

## Intern

| DTO | Beschreibung | Endpunkte |
|---|---|---|
| [PluginConfigurationConnection](PluginConfigurationConnection/index.md) | Speichert Zustand und Gültigkeit einer Plugin-Konfigurationssitzung | 0 |


[Referenz-Plugin (Java)](../index.md)
