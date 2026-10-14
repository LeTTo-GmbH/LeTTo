# LoadPluginRequestDto
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Anfragedaten für das Laden eines Plugin-DTOs.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.LoadPluginRequestDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/LoadPluginRequestDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `typ` | String | `""` | Typ des Plugins |
| `name` | String | `""` | Name des Plugins in der Frage |
| `config` | String | `""` | Konfigurationsstring des Plugins |
| `params` | String | `""` | Parameter für die Antworterzeugung |
| `q` | [PluginQuestionDto](../../dtos/PluginQuestionDto/index.md) |  | Frage wo das Plugin eingebettet ist |
| `nr` | int |  | Laufende Nummer für alle PIG-Tags und Question-Plugins |
| `configurationID` | String |  | Konfigurations-ID, wenn das [PluginDto](../../dtos/PluginDto/index.md) über AJAX bei der Konfiguration angefordert wird |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/loadplugindto`](../../rest-schnittstelle/ApiController/loadPluginDto/index.md) | Request | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /open/reloadplugindto`](../../rest-schnittstelle/ApiController/reloadPluginDto/index.md) | Request | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |
| [`POST /<endpoint>/api/open/reloadplugindto`](../../rest-schnittstelle/ApiExternOpenController/reloadPluginDto/index.md) | Request | Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
