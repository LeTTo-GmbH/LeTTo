# POST /open/updatepluginstringjavascript
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `updatePluginstringJavascript` |
| HTTP-Methode | POST |
| Pfad | `/open/updatepluginstringjavascript` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginUpdateJavascriptRequestDto](../../../dtos/PluginUpdateJavascriptRequestDto/index.md) |
| Response | String |

## Beschreibung

Passt die Plugindefinition an die Eingabe aus dem JavaScript-Result an. zB: Interaktive Karte

## Request

Body: [PluginUpdateJavascriptRequestDto](../../../dtos/PluginUpdateJavascriptRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `pluginDef` | String | ja | akt. Plugin-Definition |
| `jsResult` | String | ja | Rückgabe von JavaScript |

## Response

Typ: String

aktualisierte Plugindefinition

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`updatePluginstringJavascript`](../../../plugin-api/index.md).

## Fehlerfälle

* 404 Not Found, wenn der Plugin-Typ nicht registriert ist oder das Plugin nicht erzeugt werden kann („Plugin vom Typ … kann nicht erzeugt werden").

## Beispiel-Request

JSON-Gerüst aus den Feldern des DTOs, Werte sind Platzhalter:

```json
{
  "typ": "<typ>",
  "name": "<name>",
  "config": "<config>",
  "pluginDef": "<pluginDef>",
  "jsResult": "<jsResult>"
}
```

## Siehe auch

* [`POST /open/loadplugindto`](../../../rest-schnittstelle/ApiController/loadPluginDto/index.md) – Rendern des Plugin-Images, Aufbau eines DTOs zur späteren JavaScript - Bearbeitung


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
