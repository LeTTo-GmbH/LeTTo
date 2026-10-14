# ImageInfoDto
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Information of an Image which is stored in the Image-Service or returned from other service. It consists any Data about the source of then image and the properties to view in LeTTo.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.ImageInfoDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/ImageInfoDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `version` | String | `""` | version of the plugin if image was built in a plugin |
| `pluginTyp` | String | `""` | pugin-type of the plugin if image was built in a plugin |
| `filename` | String | `""` | filename of then image file |
| `url` | String | `""` | open URL of the image or stringlength=0 if it is not an open image |
| `width` | int |  | origin width of then image in pixel |
| `height` | int |  | orogin height of then image in pixel |
| `unit` | [IMAGEUNIT](../../enums/IMAGEUNIT/index.md) | [`IMAGEUNIT.none`](../../enums/IMAGEUNIT/index.md) | the unit of imageWidth to display image in HTML |
| `imageWidth` | int | `100` | image-width to display in percent of the screen or with the defined unit |
| `style` | String |  | CSS style definition to display on a browser with HTML |
| `alternate` | String | `"plugin image"` | alternative text used for a handicapped accessible html-site |
| `title` | String | `""` | title of the image |
| `lifetime` | long | `(new Date()).getTime() + 365L*24L*3600L*1000L` | lifetime of the image file in milliseconds since 1.1.1970 file can be deleted if lifetime is reached default lifetime is one year from now if lifetime is equal or less then zero there is no lifetime defined |

## Hinweise

* `lifetimeOutdated()` prüft, ob `lifetime` überschritten ist.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/image`](../../rest-schnittstelle/ApiController/getImage/index.md) | Response über [`ImageBase64Dto.imageInfoDto`](../../dtos/ImageBase64Dto/index.md) | Liefert ein Base64 codiertes Bild mit den angegebenen Parametern |
| [`POST /open/imageurl`](../../rest-schnittstelle/ApiController/getImageUrl/index.md) | Response über [`ImageUrlDto.imageInfoDto`](../../dtos/ImageUrlDto/index.md) | Liefert eine öffentliche URL auf das gerenderte Bild |

## Verwendet in DTOs

* [ImageBase64Dto](../../dtos/ImageBase64Dto/index.md) – Feld `imageInfoDto`
* [ImageUrlDto](../../dtos/ImageUrlDto/index.md) – Feld `imageInfoDto`

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
