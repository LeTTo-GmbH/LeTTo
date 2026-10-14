# PluginDatasetDto
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Informationen über einen Dataset welcher vom Plugin angeforder werden kann

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginDatasetDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginDatasetDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `name` | String |  | Variablenname |
| `bereich` | String |  | Datensatzdefinition mit Zahlenbereichsdefinition |
| `einheit` | String |  | Zieleinheit des Datensatzes |
| `useTemplate` | boolean |  | Bei true werden die Standardwerte der übergeordneten Kategorie verwendet und nicht der angegebene Bereich |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/generatedatasets`](../../rest-schnittstelle/ApiController/generateDatasets/index.md) | Response über [`PluginDatasetListDto.datasets`](../../dtos/PluginDatasetListDto/index.md) | Liefert alle Datensätze, welche für das Plugin in der Frage vorhanden sein sollten |

## Verwendet in DTOs

* [PluginDatasetListDto](../../dtos/PluginDatasetListDto/index.md) – Feld `datasets`

## Verwendet in der Plugin-API

* [`generateDatasets`](../../plugin-api/index.md): `List<PluginDatasetDto> generateDatasets()`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
