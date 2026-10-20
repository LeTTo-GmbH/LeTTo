# POST /open/modifyangabe
<!-- generiert aus plugin-demo-java @ dced892 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [ApiController](../index.md) |
| Java-Methode | `modifyAngabe` |
| HTTP-Methode | POST |
| Pfad | `/open/modifyangabe` |
| Erreichbarkeit | nur im Docker-Netzwerk |
| Request-Body | [PluginAngabeRequestDto](../../../dtos/PluginAngabeRequestDto/index.md) |
| Response | String |

## Beschreibung

verändert einen Angabetext, der in der Angabe in PI Tags eingeschlossen wurde

Die Funktion wird vor dem Darstellen der Frage ausgeführt.

## Request

Body: [PluginAngabeRequestDto](../../../dtos/PluginAngabeRequestDto/index.md)

| Feld | Typ | ausgewertet | Bedeutung |
|---|---|---|---|
| `typ` | String | ja | Typ des Plugins |
| `name` | String | ja | Name des Plugins in der Frage |
| `config` | String | ja | Konfigurationsstring des Plugins |
| `text` | String | ja | Text der innerhalb der PI Tags gestanden ist |
| `q` | [PluginQuestionDto](../../../dtos/PluginQuestionDto/index.md) | ja | Frage wo das Plugin eingebettet ist |

## Response

Typ: String

veränderter Text

## Ablauf im Service

* Erzeugt über `PluginConfiguration.createPluginService(typ, name, config)` eine neue Plugin-Instanz und ruft auf: [`modifyAngabe`](../../../plugin-api/index.md).

## Fehlerfälle

* 404 Not Found, wenn der Plugin-Typ nicht registriert ist oder das Plugin nicht erzeugt werden kann („Plugin vom Typ … kann nicht erzeugt werden").

## Beispiel-Request

JSON-Gerüst aus den Feldern des DTOs, Werte sind Platzhalter:

```json
{
  "typ": "<typ>",
  "name": "<name>",
  "config": "<config>",
  "text": "<text>",
  "q": {
    "…": "PluginQuestionDto"
  }
}
```

## Siehe auch

* [`POST /open/modifyangabetextkomplett`](../modifyAngabeTextkomplett/index.md) – verändert den kompletten Angabetext der Frage


[ApiController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
