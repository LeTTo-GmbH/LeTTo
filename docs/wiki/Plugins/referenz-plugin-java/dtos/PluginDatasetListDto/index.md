# PluginDatasetListDto
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Informationen über einen Dataset welcher vom Plugin angeforder werden kann

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginDatasetListDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginDatasetListDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `datasets` | List&lt;[PluginDatasetDto](../../dtos/PluginDatasetDto/index.md)&gt; |  | Datensätze der Liste. |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/generatedatasets`](../../rest-schnittstelle/ApiController/generateDatasets/index.md) | Response | Liefert alle Datensätze, welche für das Plugin in der Frage vorhanden sein sollten |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
