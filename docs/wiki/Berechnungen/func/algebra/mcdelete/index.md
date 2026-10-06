# mcdelete

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`mcdelete` – Algebra.

## Detaillierte Beschreibung

mcdelete(matrix,position) Löscht die angegebene Spalte aus einer Matrix

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
mcdelete(matrix, pos)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `pos` | Parameter der Funktion. | Matrix / Ganzzahl | nein |

## Beispiele

**Beispiel:** `mcdelete([[1,2,3],[4,5,6],[7,8,9]],1)`  
**Ergebnis:** [[1,3],[4,6],[7,9]]

| Ausdruck | Ergebnis |
| --- | --- |
| mcdelete(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,1) | &#91;&#91;1,3&#93;,&#91;4,6&#93;,&#91;7,9&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3460)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `MCDelete`.

[Zurück zu Berechnungen](../../../index.md)
