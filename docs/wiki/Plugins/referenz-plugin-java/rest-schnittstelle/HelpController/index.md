# HelpController
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Liefert die Hilfeseite des Plugin-Services mit einer kurzen Beschreibung und Links zur JavaDoc und zur Swagger-Dokumentation. Die Seite liegt in src/main/resources/help/index.html, die Platzhalter {% raw %}{{servicepath}}{% endraw %}, {% raw %}{{name}}{% endraw %} und {% raw %}{{version}}{% endraw %} werden beim Laden ersetzt.

Swagger: Hilfeseite des Plugin-Services [JavaDoc](

| | |
|---|---|
| Klasse | `at.letto.plugins.controller.HelpController` |
| Basispfad | – |
| Erreichbarkeit | extern über den Proxy |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/controller/HelpController.html` |

## Endpunkte

| Methode | Pfad | Request | Response | Beschreibung |
|---|---|---|---|---|
| GET | [`/<endpoint>`](help/index.md) | – | String | Liefert die Hilfeseite |


[REST-Schnittstelle](../index.md) · [Referenz-Plugin (Java)](../../index.md)
