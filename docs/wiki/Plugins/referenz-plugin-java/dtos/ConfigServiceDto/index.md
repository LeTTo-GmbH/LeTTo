# ConfigServiceDto
<!-- generiert aus plugin-demo-java @ f0143d1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Service welches im Setup-Service registriert ist

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.ConfigServiceDto` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/ConfigServiceDto.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `name` | String |  | Name des Services |
| `version` | String | `""` | Version des Services |
| `author` | String | `""` | Information über den Autor des Services |
| `license` | String | `""` | Information über die Lizenz des Services |
| `bs` | String | `""` | Betriebssystem auf dem das Service läuft |
| `ip` | String | `""` | IP des Services |
| `encoding` | String | `""` | Zeichen-Encoding |
| `programmingLanguage` | String | `""` | Programmiersprache in der das Service Programmiert wurde |
| `nwLettoAddress` | String |  | Adresse innerhalb des Docker-Netzwerkes nw-letto, wenn das Service dort direkt erreichbar ist |
| `dockerName` | String |  | Name des Docker-Containers, dieser muss eindeutig sein!! Bei externen Services auf anderen Servcern gibt es keinen dockerName, dann muss die externe URI eindeutig sein |
| `uriIntern` | String |  | interne URI mit der auf das Service ohne Authentifizierung zugegriffen werden kann. die URI muss protokoll://adresse:port/basisendpunkt enthalten woran dann die Standard-Plugin-Endpoints angehängt werden. Ist die uriIntern nicht gesetzt dann wird wenn extern=true ist auf der uriExtern verbunden. Läuft das Service also auf einem Fremdserver muss Benutzername und Passwort angegeben sein um sich am Fremdserver zu authentifizieren oder alle Endpunkte müssen offen sein. |
| `extern` | boolean |  | Service ist von Extern (Browser) direkt erreichbar |
| `uriExtern` | String |  | externe URI mit der vom Browser auf das Service zugegriffen werden kann (wenn extern=true) Hier muss die gesamte absolute Basis-URI angegeben werden unter der die Plugin-Endpoints liegen |
| `plugin` | boolean |  | Gibt an ob es sich bei dem Service um ein Plugin handelt |
| `scalable` | boolean |  | Gibt an ob das Service skalierbar (mehrfach vorkommen kann) ist |
| `stateless` | boolean |  | Gibt an ob das Service nur Stateless-Endpoints hat |
| `username` | String |  | Benutzername wenn das Service mit einer User-Authentifizierung am Plugin anmelden muss |
| `password` | String |  | Passwort wenn das Service mit einer User-Authentifizierung am Plugin anmelden muss |
| `usePluginToken` | boolean | `false` | Wenn hier true steht, dann muss für das Plugin ein Token verwendet werden, der in der Schule gespeichert ist. Dieser Token muss für die Authentifizierung am Plugin verwendet werden. - Ist noch nicht implementiert. |
| `serviceStartTime` | long |  | Datum und Uhrzeit an der das Service gestartet wurde als DateInteger |
| `lastRegistrationTime` | long |  | Datum und Uhrzeit der letzten Service-Registratur |
| `params` | HashMap&lt;String,String&gt; |  | zusätzliche nicht weiter definierte Parameter des Plugins |

## Hinweise

* `htmlServiceStartTime()` / `htmlLastRegistrationTime()` formatieren die Zeitpunkte für die Anzeige.
* Das Demo übergibt in `programmingLanguage` die Java-Version (`serverStatus.getJavaVersion()`).

## Verwendet in Endpunkten

| Endpunkt | Rolle | Beschreibung |
|---|---|---|
| [`POST /config/auth/user/registerplugin`](../../build-deployment/index.md#registrierung-am-letto-server) (ausgehend, Setup-Service) | Request | Registrierung des Plugin-Services am Setup-Service beim Start |

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
