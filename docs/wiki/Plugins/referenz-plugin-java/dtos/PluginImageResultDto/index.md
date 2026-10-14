# PluginImageResultDto
<!-- generiert aus plugin-demo-java @ 010a31c (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Sammelt Status und Fehlermeldungen der Plugin-Bilderzeugung.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginImageResultDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginImageResultDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `ok` | boolean | `true` | Nur wenn ok true ist, ist das Bild auch wirklich korrekt gerendert worden |
| `messages` | List&lt;String&gt; | `new ArrayList<String>()` | Liste aller Fehlermeldungen, welche beim Rendern des Bildes aufgetreten sind |

## Verwendet in Endpunkten

wird in keinem Endpunkt verwendet

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

* [`parseDrawParams`](../../plugin-api/index.md): `void parseDrawParams(String params,`[`PluginQuestionDto`](../../dtos/PluginQuestionDto/index.md) `q, PluginImageResultDto pluginImageResultDto)`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
