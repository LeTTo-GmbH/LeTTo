# onlypos

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`onlypos` – Gleichungen und Gleichungssysteme.

## Detaillierte Beschreibung

liefert aus dem Lösungsvektor von solve welcher aus lauter Gleichungen besteht nur die Lösungen welche positiv nicht Null sind

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
onlypos(variable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

## Beispiele

**Beispiel:** `onlypos([[x=3,y=-3],[x=4,y=5],[x=-2,y=4]]) onlypos([x=-2,x=0,x=6,x=8])`  
**Ergebnis:** [[x=4,y=5]] [x=7,x=8]

| Ausdruck | Ergebnis |
| --- | --- |
| onlypos(&#91;&#91;x=3,y=-3&#93;,&#91;x=4,y=5&#93;,&#91;x=-2,y=4&#93;&#93;) <br> onlypos(&#91;x=-2,x=0,x=6,x=8&#93;) | &#91;&#91;x=4,y=5&#93;&#93; <br> &#91;x=7,x=8&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3286)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6522

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `OnlyPos`.

[Zurück zu Berechnungen](../../../index.md)
