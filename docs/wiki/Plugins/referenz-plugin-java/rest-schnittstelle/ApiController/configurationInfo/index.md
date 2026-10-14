# POST /open/configurationinfo
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `configurationInfo` |
| HTTP-Methode | POST |
| Pfad | `/open/configurationinfo` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginConfigurationInfoRequestDto](../../../dtos/PluginConfigurationInfoRequestDto/index.md) |
| Response | [PluginConfigurationInfoDto](../../../dtos/PluginConfigurationInfoDto/index.md) |

## Beschreibung

Liefert die Informationen welche notwendig sind um einen Konfigurationsdialog zu starten

Ist die configurationID gesetzt wird eine Konfiguration gestartet und damit auch die restlichen Endpoints für die Konfiguration aktiviert.

LeTTo/Plugintester muss die configurationID für jeden Konfigurationsdialog eindeutig setzen, sie dient als Zustandsdefinition

Die Konfiguration ist NICHT stateless - der Zustand muss über die configurationID beidseitig gespeichert werden.

Nach längerer Untätigkeit sollte der Zustand der ConfigurationID wieder entfernt werden (z.B. über die timeout Angabe) damit es nicht zu einem Speicherüberlauf am Plugin-Service kommt

Im Zustand müssen typ,name und config gespeichert werden

Die Konfiguration kann über die configurationID jederzeit über open-Endpoints mit den restlichen Endpoints abgefragt und verändert werden

Die configurationID wird also als Authentifizierung an den Open-Endpoints verwendet.


## Request

Body: [PluginConfigurationInfoRequestDto](../../../dtos/PluginConfigurationInfoRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `configurationID` | String | ja | eindeutige ID welche für die Verbindung zwischen Edit-Service, Browser und Plugin-Konfiguration verwendet wird |
| `timeout` | long | ja | maximale Gültigkeit der Konfigurations-Verbindung in Sekunden ohne Verbindungsanfragen, Notwendig um bei Verbindungsabbruch die Daten am Plugin-Service auch wieder zu löschen |

## Response

Typ: [PluginConfigurationInfoDto](../../../dtos/PluginConfigurationInfoDto/index.md)

alle notwendigen Konfigurationen

## Ablauf im Service

* Verwendet `PluginConfiguration`: `configurationInfo`, `getBaseUriExtern`.
* Legt eine Konfigurationssitzung ([`PluginConfigurationConnection`](../../../dtos/PluginConfigurationConnection/index.md)) an bzw. aktualisiert sie; ohne `configurationID` erzeugt der Service eine zufällige ID (30 Zeichen).
* Der Controller setzt `configurationUrl` auf `<letto.plugin.uri.extern>/<endpoint>/open/confighttp?typ=<typ>&configurationID=<id>` (URL-codiert).
* Bei jedem Zugriff werden Sitzungen entfernt, deren letzter Zugriff länger als `timeout` Sekunden zurückliegt.
* Kann das Plugin nicht erzeugt werden, wird ein leeres [`PluginConfigurationInfoDto`](../../../dtos/PluginConfigurationInfoDto/index.md) geliefert (kein 404).

## Fehlerfälle

* keine eigenen Fehlerfälle im Code

## Beispiel-Request

JSON-Gerüst aus den Feldern des DTOs, Werte sind Platzhalter:

```json
{
  "typ": "<typ>",
  "name": "<name>",
  "config": "<config>",
  "configurationID": "<configurationID>",
  "timeout": 0
}
```

## Siehe auch

* [`POST /open/setconfigurationdata`](../../../rest-schnittstelle/ApiController/setConfigurationData/index.md) – Sendet alle notwendigen (im ConfigurationInfo) angeforderten Daten im Mode CONFIGMODE_URL an die Plugin-Konfiguration
* [`GET /<endpoint>/open/confighttp`](../../../rest-schnittstelle/ConfigHttpController/configHttp/index.md) – Liefert die HTML-Seite des Konfigurationsdialogs
* [`POST /open/getconfiguration`](../../../rest-schnittstelle/ApiController/getConfiguration/index.md) – Liefert die aktuelle Konfiguration eines Plugins welches sich gerade in einem CONFIGMODE_URL Konfigurationsdialog befindet


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
