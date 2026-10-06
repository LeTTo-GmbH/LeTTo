# onlyreal

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`onlyreal` – Gleichungen und Gleichungssysteme.

## Detaillierte Beschreibung

liefert aus dem Lösungsvektor von solve welcher aus lauter Gleichungen besteht nur die Lösungen welche reell sind

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
onlyreal(matrix)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |

## Beispiele

**Beispiel:** `onlyreal([[x=1,y=%i],[x=1,y=-%i],[x=3,y=4]]) onlyreal([x=%i+1,x=1-%i,x=3,x=8])`  
**Ergebnis:** [[x=3,y=4]] [x=3,x=8]

| Ausdruck | Ergebnis |
| --- | --- |
| onlyreal(&#91;&#91;x=1,y=%i&#93;,&#91;x=1,y=-%i&#93;,&#91;x=3,y=4&#93;&#93;) <br> onlyreal(&#91;x=%i+1,x=1-%i,x=3,x=8&#93;) | &#91;&#91;x=3,y=4&#93;&#93; <br> &#91;x=3,x=8&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3287)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6522

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `OnlyReal`.

[Zurück zu Berechnungen](../../../index.md)
