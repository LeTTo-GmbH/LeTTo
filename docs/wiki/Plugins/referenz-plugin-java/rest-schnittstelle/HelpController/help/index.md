# GET /&lt;endpoint&gt;
<!-- generiert aus plugin-demo-java @ a8aca2d (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

| | |
|---|---|
| Controller | [HelpController](../index.md) |
| Java-Methode | `help` |
| HTTP-Methode | GET |
| Pfad | `/<endpoint>`<br>`/<endpoint>/`<br>`/<endpoint>/index.html`<br>`/<endpoint>/help` |
| Erreichbarkeit | extern über den Proxy |
| Content-Type | `text/html` |
| Request | – |
| Response | String |

## Beschreibung

Liefert die Hilfeseite.

## Response

Typ: String

Hilfeseite als HTML

Die Antwort ist eine HTML-Seite.

## Ablauf im Service

* Die Seite stammt aus `src/main/resources/help/index.html`; `{% raw %}{{servicepath}}{% endraw %}`, `{% raw %}{{name}}{% endraw %}` und `{% raw %}{{version}}{% endraw %}` werden beim Start einmalig ersetzt.

## Fehlerfälle

* keine eigenen Fehlerfälle im Code


[HelpController](../index.md) · [REST-Schnittstelle](../../index.md) · [Referenz-Plugin (Java)](../../../index.md)
