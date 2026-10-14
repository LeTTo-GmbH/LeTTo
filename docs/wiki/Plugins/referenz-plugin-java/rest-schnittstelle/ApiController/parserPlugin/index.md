# POST /open/parserplugin
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `parserPlugin` |
| HTTP-Methode | POST |
| Pfad | `/open/parserplugin` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginParserRequestDto](../../../dtos/PluginParserRequestDto/index.md) |
| Response | [CalcErgebnisDto](../../../dtos/CalcErgebnisDto/index.md) |

## Beschreibung

Wird verwendet wenn im Lösungsfeld die Funktion plugin("pluginname",p1,p2,p3) verwendet wird

## Request

Body: [PluginParserRequestDto](../../../dtos/PluginParserRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `vars` | [VarHashDto](../../../dtos/VarHashDto/index.md) | ja | Alle Variablen der Frage |
| `cp` | [CalcParamsDto](../../../dtos/CalcParamsDto/index.md) | ja | Berechnungsparameter |
| `p` | [CalcErgebnisDto](../../../dtos/CalcErgebnisDto/index.md)[] | ja | Liste von CalcErgebnis-Werten, welche an das Plugin von der Question aus übergeben werden können |

## Response

Typ: [CalcErgebnisDto](../../../dtos/CalcErgebnisDto/index.md)

Ergebnis der Funktion als [CalcErgebnisDto](../../../dtos/CalcErgebnisDto/index.md)

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`parserPlugin`](../../../plugin-api/index.md).

## Fehlerfälle

* 404 Not Found, wenn der Plugin-Typ nicht registriert ist oder das Plugin nicht erzeugt werden kann („Plugin vom Typ … kann nicht erzeugt werden").

## Beispiel-Request

JSON-Gerüst aus den Feldern des DTOs, Werte sind Platzhalter:

```json
{
  "typ": "<typ>",
  "name": "<name>",
  "config": "<config>",
  "vars": {
    "…": "VarHashDto"
  },
  "cp": {
    "…": "CalcParamsDto"
  },
  "p": []
}
```

## Siehe auch

* [`POST /open/parserplugineinheit`](../../../rest-schnittstelle/ApiController/parserPluginEinheit/index.md) – Bestimmt die Recheneinheit, welche bei der Methode parserPlugin als Ergebnis herauskommt wenn die Parameter die Einheiten wie in der Liste p haben
* [`POST /open/maxima`](../../../rest-schnittstelle/ApiController/getMaxima/index.md) – Liefert einen Maxima-Berechnungsstring für die Berechnung des Plugins


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
