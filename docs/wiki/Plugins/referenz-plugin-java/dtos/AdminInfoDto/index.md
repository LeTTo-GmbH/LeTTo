# AdminInfoDto
<!-- generiert aus plugin-demo-java @ f0143d1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Information über ein Service für den Admin

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.AdminInfoDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/AdminInfoDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `servicename` | String | `""` | Name des Services |
| `pid` | String | `""` | PID des Prozesses |
| `homedir` | String | `""` | Home-Verzeichnis des Services am Server |
| `startuptime` | long | `0` | Zeit des Service-Starts in ms |
| `updtime` | long | `0` | Zeit die seit dem Service-Start vergangen ist in ms |
| `version` | String | `""` | Version des Services |
| `time` | String | `""` | aktuelle Zeit am Service |
| `betriebssystem` | String | `""` | Betriebssystem auf dem das Service läuft |
| `ip` | String | `""` | IP des Rechners |
| `encoding` | String | `""` | Tastatur-Bildschirm-Encoding |
| `fileEncoding` | String | `""` | File-Encoding |
| `fileSeparator` | String | `""` | File-Trennzeichen Slash-Backslash |
| `javaSpecificVersion` | String | `""` | Java Versionsnummer zB. 1.8 |
| `javaVendor` | String | `""` | Hersteller der Java-Runtime zB.: Oracle Corporation |
| `javaVersion` | String | `""` | Genauere Java Versionsbeschreibung zB.: Oracle Corporation 1.8.0_241-b07 |
| `javaVersionNumber` | String | `""` | Genauere Java Versionsnummer zB.: 1.8.0_241-b07 |
| `hostname` | String | `""` | Hostname |
| `language` | String | `""` | Sprache des Rechner auf dem das Service installiert ist |
| `linuxDescription` | String | `""` | Beschreibung der Linux Version auf dem das Service läuft |
| `linuxDistribution` | String | `""` | Linux Distribution auf der das Service läuft |
| `linuxRelease` | String | `""` | Linux Release auf der das Service läuft |
| `serverUsername` | String | `""` | Benutzername unter welchem das Service gestartet wurde |
| `serverVersion` | String | `""` | Version des JEE-Servers |
| `systemHome` | String | `""` | System Home-Verzeichnis |
| `isLinux` | boolean | `false` | true wenn das Service unter Linux läuft |
| `isUbuntu` | boolean | `false` | true wenn das Service unter Ubuntu läuft |
| `isWindows` | boolean | `false` | true wenn das Service unter Windows läuft |
| `httpPort` | int | `0` | Portnummer des http-Servers |
| `ajpPort` | int | `0` | Portnummer des ajp-Servers |
| `httpsPort` | int | `0` | Portnummer des https-Servers |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`GET /info`](../../rest-schnittstelle/InfoController/info/index.md) | Response über [`ServiceInfoDTO.adminInfoDto`](../../dtos/ServiceInfoDTO/index.md) | Liefert Informationen über den laufenden Plugin-Service |
| [`GET /<endpoint>/open/info`](../../rest-schnittstelle/InfoController/infoOpen/index.md) | Response über [`ServiceInfoDTO.adminInfoDto`](../../dtos/ServiceInfoDTO/index.md) | Liefert Service-Informationen über den öffentlichen Endpunkt |

## Verwendet in DTOs

* [ServiceInfoDTO](../../dtos/ServiceInfoDTO/index.md) – Feld `adminInfoDto`

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
