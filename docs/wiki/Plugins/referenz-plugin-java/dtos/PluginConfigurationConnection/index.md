# PluginConfigurationConnection
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Speichert Zustand und Gültigkeit einer Plugin-Konfigurationssitzung.

| | |
|---|---|
| Klasse | `at.letto.plugins.dto.PluginConfigurationConnection` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/dto/PluginConfigurationConnection.html` |

## Felder

| Feld | Typ | Standard | Bedeutung |
|---|---|---|---|
| `configurationID` | String |  | Konfigurations ID |
| `typ` | String |  | Typ des Plugins |
| `name` | String |  | Name des Plugins |
| `config` | String |  | Konfigurationsstring des Plugins |
| `pluginService` | PluginService |  | Plugin das gerade bearbeitet wird |
| `pluginConfigurationInfoDto` | [PluginConfigurationInfoDto](../../dtos/PluginConfigurationInfoDto/index.md) |  | Plugin Konfigurations-Information |
| `pluginConfigDto` | [PluginConfigDto](../../dtos/PluginConfigDto/index.md) |  | [PluginConfigDto](../../dtos/PluginConfigDto/index.md) welches aktuell gültig ist |
| `pluginQuestionDto` | [PluginQuestionDto](../../dtos/PluginQuestionDto/index.md) |  | [PluginQuestionDto](../../dtos/PluginQuestionDto/index.md) der Frage welche zu dem Plugin gehört |
| `timeout` | long |  | Gültigkeitsdauer in Sekunden |
| `lastTime` | long | `Datum.nowDateInteger()` | Zugriffszeitstempel des letzten Zugriffes als DateInteger in Sekunden |

## Hinweise

* **Interne Klasse, wird nicht über REST übertragen.** Sie hält im Plugin-Service den Zustand einer Konfigurationssitzung; `PluginConfiguration` speichert die Sitzungen nach `configurationID`.
* Der Konstruktor erzeugt eine zufällige ID (30 Zeichen), wenn keine `configurationID` übergeben wird, und legt ein [`PluginConfigDto`](../../dtos/PluginConfigDto/index.md) mit Größe 800×600 an.
* `changeConfig(config, pluginService)` setzt Konfiguration und Plugin-Instanz neu und holt `configurationInfo` vom Plugin.

## Verwendet in Endpunkten

wird in keinem Endpunkt verwendet

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

nicht direkt in `PluginService` verwendet


[DTOs](../index.md) · [Referenz-Plugin (Java)](../../index.md)
