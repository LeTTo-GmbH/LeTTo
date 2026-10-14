# RegisterServiceResultDto
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Ergebnis der Registratur eines Services

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.RegisterServiceResultDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/RegisterServiceResultDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `registrationOK` | boolean |  | Registration erfolgreich |
| `newRegistered` | boolean |  | Gibt an ob das Service neu registriert wurde oder schon vorhanden war |
| `registrationCounter` | int |  | Gibt die Anzahl der insgesamt registrierten Services dieses Plugin-Services an |
| `msg` | String |  | Rückmeldung wenn ein Fehler aufgetreten ist |

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /config/auth/user/registerplugin`](../../build-deployment/index.md#registrierung-am-letto-server) (ausgehend, Setup-Service) | Response | Registrierung des Plugin-Services am Setup-Service beim Start |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
