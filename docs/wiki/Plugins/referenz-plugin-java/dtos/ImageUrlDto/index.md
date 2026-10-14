# ImageUrlDto
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

image with image-information of an image-file at an open Url

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.ImageUrlDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/ImageUrlDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `imageUrl` | String | `""` | image Url |
| `imageInfoDto` | [ImageInfoDto](../../dtos/ImageInfoDto/index.md) | `new` [`ImageInfoDto`](../../dtos/ImageInfoDto/index.md)`()` | image information |
| `error` | String | `""` | error message if the image cannot be created |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/imageurl`](../../rest-schnittstelle/ApiController/getImageUrl/index.md) | Response | Liefert eine öffentliche URL auf das gerenderte Bild |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

* [`getImageUrl`](../../plugin-api/index.md): `ImageUrlDto getImageUrl(String params,` [`PluginQuestionDto`](../../dtos/PluginQuestionDto/index.md) `q)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
