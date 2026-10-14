# IMAGEUNIT
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Einheiten welche für die Größenangaben von Bildern verwendet werden können none : keine Angabe der Dateigröße px : Pixel pt : Punkte cm : Zentimeter percent : Prozent der Bildschirmbreite em : Vielfache der Standardschriftgröße

| | |
|---|---|
| Enum | `at.letto.plugins.enums.IMAGEUNIT` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/enums/IMAGEUNIT.html` |

## Werte

| Wert | Bedeutung |
|---|---|
| `none` | Keine Angabe der Dateigröße |
| `px` | Angabe in Bildschirmpixel |
| `pt` | Angabe in Punkten |
| `cm` | Angabe in cm |
| `percent` | Angabe in Prozent |
| `em` | Angabe in Vielfachen der Standardschriftgröße |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /open/image`](../../rest-schnittstelle/ApiController/getImage/index.md) | Response über [`ImageBase64Dto.imageInfoDto`](../../dtos/ImageBase64Dto/index.md) → [`ImageInfoDto.unit`](../../dtos/ImageInfoDto/index.md) | Liefert ein Base64 codiertes Bild mit den angegebenen Parametern |
| [`POST /open/imageurl`](../../rest-schnittstelle/ApiController/getImageUrl/index.md) | Response über [`ImageUrlDto.imageInfoDto`](../../dtos/ImageUrlDto/index.md) → [`ImageInfoDto.unit`](../../dtos/ImageInfoDto/index.md) | Liefert eine öffentliche URL auf das gerenderte Bild |

## Verwendet in DTOs

* [ImageInfoDto](../../dtos/ImageInfoDto/index.md) – Feld `unit`

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[Enums](../index.md) · [Referenz-Plugin (Java)](../../index.md)
