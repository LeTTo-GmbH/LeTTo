# PluginSetConfigurationDataRequestDto
<!-- generiert aus plugin-demo-java @ f0143d1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Anfragedaten für die Übermittlung von Konfigurationsdaten.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginSetConfigurationDataRequestDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginSetConfigurationDataRequestDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `typ` | String |  | Typ des Plugins |
| `configurationID` | String | `""` | eindeutige ID welche für die Verbindung zwischen Edit-Service, Browser und Plugin-Konfiguration verwendet wird |
| `configuration` | String |  | aktueller Konfigurations-String des Plugins |
| `questionDto` | [PluginQuestionDto](../../dtos/PluginQuestionDto/index.md) |  | Question-DTO mit Varhashes |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/setconfigurationdata`](../../rest-schnittstelle/ApiController/setConfigurationData/index.md) | Request | Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
