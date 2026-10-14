# ServiceInfoDTO
<!-- generiert aus plugin-demo-java @ f0143d1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Überträgt allgemeine Service-Informationen und Angaben zur Laufzeitumgebung.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.ServiceInfoDTO` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/ServiceInfoDTO.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `serviceName` | String | `""` | Name des Services |
| `version` | String | `""` | Version des Services |
| `author` | String | `""` | Information über den Autor des Services |
| `license` | String | `""` | Information über die Lizenz des Services |
| `endpoints` | String | `""` | Information über die Endpoints des Services |
| `jarfilename` | String | `""` | Jardatei welche gestartet wurde |
| `starttime` | String | `""` | Datum und Uhrzeit des Service-Starts |
| `adminInfoDto` | [AdminInfoDto](../../dtos/AdminInfoDto/index.md) | `null` | Administrative Information über das Service |
| `jarLibs` | List&lt;String&gt; | `new ArrayList<>()` | Liste aller Library-jars welche in diesem Service verwendet werden |

## Hinweise

* Im Demo bleibt `endpoints` leer und `jarLibs` ist `null`.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`GET /info`](../../rest-schnittstelle/InfoController/info/index.md) | Response | Liefert Informationen über den laufenden Plugin-Service |
| [`GET /<endpoint>/open/info`](../../rest-schnittstelle/InfoController/infoOpen/index.md) | Response | Liefert Service-Informationen über den öffentlichen Endpunkt |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
