# ConfigHttpController
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Liefert den Konfigurationsdialog eines Plugins im Mode CONFIGMODE_URL als HTML-Seite, welche von LeTTo in einem iframe oder Browser-Tab geöffnet wird. Die Seite bindet die JavaScript-Libraries des Plugins ein und ruft die Konfigurations-Methode des Plugins mit dem [PluginConfigDto](../../dtos/PluginConfigDto/index.md) der Konfigurations-Verbindung auf. Änderungen der Konfiguration werden vom Plugin-JavaScript über den reloadPluginDto-Endpoint an die Verbindung übertragen, von wo LeTTo sie über getConfiguration abholt.

Swagger: Konfigurationsdialog des Plugins im iframe-Modus (CONFIGMODE_URL) [JavaDoc](

| | |
|---|---|
| Klasse | `at.letto.plugins.controller.ConfigHttpController` |
| Basispfad | – |
| Erreichbarkeit | extern über den Proxy |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/controller/ConfigHttpController.html` |

## Endpunkte

| Methode | Pfad | Request | Response | Beschreibung |
|---|---|---|---|---|
| GET | [`/<endpoint>/open/confighttp`](configHttp/index.md) | `typ`, `configurationID` | String | Liefert die HTML-Seite des Konfigurationsdialogs |


[REST-Schnittstelle](../index.md) · [Referenz-Plugin (Java)](../../index.md)
