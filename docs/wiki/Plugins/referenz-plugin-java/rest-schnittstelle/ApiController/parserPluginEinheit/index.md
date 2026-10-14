# POST /open/parserplugineinheit
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `parserPluginEinheit` |
| HTTP-Methode | POST |
| Pfad | `/open/parserplugineinheit` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginEinheitRequestDto](../../../dtos/PluginEinheitRequestDto/index.md) |
| Response | String |

## Beschreibung

Bestimmt die Recheneinheit, welche bei der Methode parserPlugin als Ergebnis herauskommt wenn die Parameter die Einheiten wie in der Liste p haben

## Request

Body: [PluginEinheitRequestDto](../../../dtos/PluginEinheitRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `p` | String[] | ja | Einheiten der Parameter als Recheneinheiten |

## Response

Typ: String

Recheneinheit des Ergebnisses

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`parserPluginEinheit`](../../../plugin-api/index.md).

## Fehlerfälle

* 404 Not Found, wenn der Plugin-Typ nicht registriert ist oder das Plugin nicht erzeugt werden kann („Plugin vom Typ … kann nicht erzeugt werden").

## Beispiel-Request

JSON-Gerüst aus den Feldern des DTOs, Werte sind Platzhalter:

```json
{
  "typ": "<typ>",
  "name": "<name>",
  "config": "<config>",
  "p": []
}
```

## Siehe auch

* [`POST /open/parserplugin`](../../../rest-schnittstelle/ApiController/parserPlugin/index.md) – Wird verwendet wenn im Lösungsfeld die Funktion plugin("pluginname",p1,p2,p3) verwendet wird


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
