# ImageUrlDto
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

image with image-information of an image-file at an open Url

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.ImageUrlDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/ImageUrlDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `imageUrl` | String | `""` | image Url |
| `imageInfoDto` | [ImageInfoDto](../../dtos/ImageInfoDto/index.md) | `new ImageInfoDto()` | image information |
| `error` | String | `""` | error message if the image cannot be created |

## Verwendet in Endpunkten

wird in keinem Endpunkt verwendet

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

* [`getImageUrl`](../../plugin-api/index.md): `ImageUrlDto getImageUrl(String params, PluginQuestionDto q)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
