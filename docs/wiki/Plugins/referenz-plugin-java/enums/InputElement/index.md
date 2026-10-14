# InputElement
<!-- generiert aus plugin-demo-java @ 060a0b1 (revision 1000) – nicht manuell editieren, Änderungen im Plugin-Repo bzw. im Skill plugin-doku vornehmen -->

Definiert das Eingabeelement für die Subquestion, deren Typ auf Plugin gesetzt ist. Mögliche Eingabetypen:

| | |
|---|---|
| Enum | `at.letto.plugins.enums.InputElement` |
| JavaDoc | `/<endpoint>/open/javadoc/at/letto/plugins/enums/InputElement.html` |

## Werte

| Wert | Bedeutung |
|---|---|
| `TextField` | TextField für ein Textfeld |
| `TextArea` | TextArea für einen größeren Eingabebereich |
| `Button` | Schaltfläche als Eingabeelement. |
| `MULTICHOICE` | Auswahl mehrerer vorgegebener Antworten. |
| `XHTML` | Eingabeelement mit XHTML-Inhalt. |
| `SourceCode` | JavaScript-Editor für Eingabe von Quelltext von Programmen |
| `JAVASCRIPT` | Interaktive JavaScript-Eingabe. |

## Verwendet in Endpunkten

wird in keinem Endpunkt verwendet

## Verwendet in DTOs

in keinem DTO als Feldtyp verwendet

## Verwendet in der Plugin-API

* [`getInputElement`](../../plugin-api/index.md): `InputElement getInputElement()`


[Enums](../index.md) · [Referenz-Plugin (Java)](../../index.md)
