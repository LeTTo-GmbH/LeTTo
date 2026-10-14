# PluginUpdateJavascriptRequestDto
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Anfragedaten für die Aktualisierung einer Plugin-Definition anhand der JavaScript-Eingabe.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginUpdateJavascriptRequestDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginUpdateJavascriptRequestDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `typ` | String | `""` | Typ des Plugins |
| `name` | String | `""` | Name des Plugins in der Frage |
| `config` | String | `""` | Konfigurationsstring des Plugins |
| `pluginDef` | String | `""` | akt. Plugin-Definition |
| `jsResult` | String |  | Rückgabe von JavaScript |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/updatepluginstringjavascript`](../../rest-schnittstelle/ApiController/updatePluginstringJavascript/index.md) | Request | Passt die Plugindefinition an die Eingabe aus dem JavaScript-Result an |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
