# InfoController
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

REST-Endpunkte zur Erreichbarkeit, Version und Laufzeitinformation des Plugin-Services.

Swagger: Erreichbarkeit, Version und Informationen über den laufenden Plugin-Service [JavaDoc](

| | |
|---|---|
| Klasse | `at.letto.plugins.controller.InfoController` |
| Basispfad | – |
| Erreichbarkeit | teils intern, teils extern (siehe Tabelle) |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/controller/InfoController.html` |

## Endpunkte

| Methode | Pfad | Request | Response | Beschreibung |
|---|---|---|---|---|
| GET | [`/ping`](ping/index.md) | – | String | Bestätigt die Erreichbarkeit des internen Endpunkts |
| GET | [`/<endpoint>/open/ping`](pingopen/index.md) | – | String | Bestätigt die Erreichbarkeit des öffentlichen Endpunkts |
| GET | [`/info`](info/index.md) | – | [ServiceInfoDTO](../../dtos/ServiceInfoDTO/index.md) | Liefert Informationen über den laufenden Plugin-Service |
| GET | [`/<endpoint>/open/info`](infoOpen/index.md) | – | [ServiceInfoDTO](../../dtos/ServiceInfoDTO/index.md) | Liefert Service-Informationen über den öffentlichen Endpunkt |
| GET | [`/version`](version/index.md) | – | String | Liefert die Version des Plugin-Services |

## Hinweise

* Der Controller hat keinen gemeinsamen Basispfad; [`/ping`](../../rest-schnittstelle/InfoController/ping/index.md), [`/info`](../../rest-schnittstelle/InfoController/info/index.md) und [`/version`](../../rest-schnittstelle/InfoController/version/index.md) sind nur im Docker-Netzwerk erreichbar.


[REST-Schnittstelle](../index.md) · [Referenz-Plugin (Java)](../../index.md)
