# JavascriptLibrary
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Beschreibt eine JavaScript-Bibliothek als lokale Ressource, Serverdatei oder Quelltext.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.JavascriptLibrary` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/JavascriptLibrary.html` |

## Konstanten

| Konstante | Typ | Wert | Bedeutung |
|---|---|---|---|
| `LOCAL` | String | `"LOCAL"` | JS-Bibliothek local als Ressource verfügbar |
| `SERVER` | String | `"SERVER"` | JS-Bibliothek von einem Server mit vollständiger Adresse verfügbar |
| `JAVASCRIPT` | String | `"JAVASCRIPT"` | JS-Library als vollständiger Text verfügbar |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `library` | String |  | Ressourcenverzeichnis oder Serveradresse der JavaScript-Bibliothek. |
| `name` | String |  | Name / Bezeichner der Bibliothek |
| `globalName` | String |  | relativer Pfad am JS-Server ohne Server-Adresse bei glob. JS-Libraries |
| `local` | String | `LOCAL` | Definition, wie JS im Template eingebaut wird (lokal, server, text) |
| `js_code` | String | `""` | Vollständiger JS-Code im Text-Modus |

## Hinweise

* Konstruktoren: `(path)` lokale Ressource, `(name, jscode, true)` Quelltext (Modus `JAVASCRIPT`), `(server, path)` bzw. `(server, pathlocal, pathGlobal)` externe Library (Modus `SERVER`).
* `loadPath(localServer)` liefert den Ladepfad je nach Modus; `equals(lib)` vergleicht Modus, Name und ggf. Serverpfad.

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`GET /open/generalinfolist`](../../rest-schnittstelle/ApiController/pluginGeneralInfoList/index.md) | Response über [`PluginGeneralInfoList.pluginInfos`](../../dtos/PluginGeneralInfoList/index.md) → [`PluginGeneralInfo.javascriptLibraries`](../../dtos/PluginGeneralInfo/index.md) (und 1 weiterer Weg) | Liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services |
| [`POST /open/generalinfo`](../../rest-schnittstelle/ApiController/pluginGeneralInfo/index.md) | Response über [`PluginGeneralInfo.javascriptLibraries`](../../dtos/PluginGeneralInfo/index.md) (und 1 weiterer Weg) | Liefert die allgemeinen Konfigurationsinformationen zu einem Plugin |
| [`GET /<endpoint>/api/open/generalinfolist`](../../rest-schnittstelle/ApiExternOpenController/pluginGeneralInfoList/index.md) | Response über [`PluginGeneralInfoList.pluginInfos`](../../dtos/PluginGeneralInfoList/index.md) → [`PluginGeneralInfo.javascriptLibraries`](../../dtos/PluginGeneralInfo/index.md) (und 1 weiterer Weg) | liefert eine Liste aller globalen Informationen über alle Plugins des verwalteten Services |
| [`POST /<endpoint>/api/open/generalinfo`](../../rest-schnittstelle/ApiExternOpenController/pluginGeneralInfo/index.md) | Response über [`PluginGeneralInfo.javascriptLibraries`](../../dtos/PluginGeneralInfo/index.md) (und 1 weiterer Weg) | liefert die allgemeinen Konfigurationsinformationen zu einem Plugin Body: String - Name des Plugins |

## Verwendet in DTOs

* [PluginGeneralInfo](../../dtos/PluginGeneralInfo/index.md) – Feld `javascriptLibraries`
* [PluginGeneralInfo](../../dtos/PluginGeneralInfo/index.md) – Feld `javascriptLibrariesLocal`

## Verwendet in der Plugin-API

* [`javascriptLibraries`](../../plugin-api/index.md): `List<JavascriptLibrary> javascriptLibraries()`
* [`javascriptLibrariesLocal`](../../plugin-api/index.md): `List<JavascriptLibrary> javascriptLibrariesLocal()`


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
