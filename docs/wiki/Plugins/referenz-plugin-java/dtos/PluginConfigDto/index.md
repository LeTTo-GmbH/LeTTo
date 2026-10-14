# PluginConfigDto
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Dto welches vom Plugin über Letto zum JavaScript der Konfiguration des Plugins geschickt wird

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginConfigDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginConfigDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `typ` | String | `""` | Typ des Plugins |
| `name` | String | `""` | Name des Plugins im Dialog |
| `config` | String | `""` | Konfigurationsstring |
| `tagName` | String | `""` | Eindeutiger Bezeichner des PluginTags |
| `width` | int | `500` | Breite des Plugin-Bereiches in Pixel |
| `height` | int | `500` | Höhe des Plugin-Bereiches in Pixel |
| `configurationID` | String |  | Konfigurations-ID |
| `errorMsg` | String |  | Fehlermeldung wenn das DTO nicht korrekt erzeugt wurde |
| `pluginDto` | [PluginDto](../../dtos/PluginDto/index.md) |  | [PluginDto](../../dtos/PluginDto/index.md) für die Initialisierung des Plugins |
| `pluginDtoUri` | String |  | Uri am Question-Service für das [PluginDto](../../dtos/PluginDto/index.md) |
| `pluginDtoToken` | String |  | Token welcher an der pluginDtoUri benötigt wird |
| `params` | HashMap&lt;String,String&gt; | `new HashMap<>()` | Parameter welche vom Plugin an JavaScript weitergegeben werden sollen, wird von LeTTo nicht verwendet, kann aber gelesen und verändert werden |
| `jsonData` | String |  | JSON-String welcher vom Plugin an JavaScript weitergegeben werden soll, wird von LeTTo nicht verwendet |

## Hinweise

* Konstruktoren mit `params` übernehmen `size=<B>x<H>` bzw. `size=<N>` aus den durch Komma getrennten Parametern.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/setconfigurationdata`](../../rest-schnittstelle/ApiController/setConfigurationData/index.md) | Response | Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration |

## Verwendet in DTOs

* [PluginConfigurationConnection](../../dtos/PluginConfigurationConnection/index.md) – Feld `pluginConfigDto`

## Verwendet in der Plugin-API

* [`setConfigurationData`](../../plugin-api/index.md): `PluginConfigDto setConfigurationData(String configuration, PluginQuestionDto questionDto)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
