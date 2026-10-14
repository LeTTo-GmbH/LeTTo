# PluginEinheitRequestDto
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Anfragedaten für die Bestimmung der Ergebniseinheit.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginEinheitRequestDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginEinheitRequestDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `typ` | String | `""` | Typ des Plugins |
| `name` | String | `""` | Name des Plugins in der Frage |
| `config` | String | `""` | Konfigurationsstring des Plugins |
| `p` | String[] |  | Einheiten der Parameter als Recheneinheiten |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/parserplugineinheit`](../../rest-schnittstelle/ApiController/parserPluginEinheit/index.md) | Request | Bestimmt die Recheneinheit, welche bei der Methode parserPlugin als Ergebnis herauskommt wenn die Parameter die Einheiten wie in der Liste p haben |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
