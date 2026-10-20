# PluginParserRequestDto
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Anfragedaten für die Auswertung einer Plugin-Parserfunktion.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginParserRequestDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginParserRequestDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `typ` | String | `""` | Typ des Plugins |
| `name` | String | `""` | Name des Plugins in der Frage |
| `config` | String | `""` | Konfigurationsstring des Plugins |
| `vars` | [VarHashDto](../VarHashDto/index.md) |  | Alle Variablen der Frage |
| `cp` | [CalcParamsDto](../CalcParamsDto/index.md) |  | Berechnungsparameter |
| `p` | [CalcErgebnisDto](../CalcErgebnisDto/index.md)[] |  | Liste von CalcErgebnis-Werten, welche an das Plugin von der Question aus übergeben werden können |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/parserplugin`](../../rest-schnittstelle/ApiController/parserPlugin/index.md) | Request | Wird verwendet wenn im Lösungsfeld die Funktion plugin("pluginname",p1,p2,p3) verwendet wird |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
