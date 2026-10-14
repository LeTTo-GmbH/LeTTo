# ImageBase64Dto
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

image with image-information of an image-file which is coded in base64

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.ImageBase64Dto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/ImageBase64Dto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `base64Image` | String | `""` | base64 coded image |
| `imageInfoDto` | [ImageInfoDto](../../dtos/ImageInfoDto/index.md) | `new ImageInfoDto()` | image information |
| `error` | String | `""` | error message if the image cannot be created |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/image`](../../rest-schnittstelle/ApiController/getImage/index.md) | Response | Liefert ein Base64 codiertes Bild mit den angegebenen Parametern |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

* [`getImageDto`](../../plugin-api/index.md): `ImageBase64Dto getImageDto(String params, PluginQuestionDto q)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
