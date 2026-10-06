# mrinsert

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`mrinsert` – Algebra.

## Detaillierte Beschreibung

mrinsert(matrix,matrixodervektor,position) Fügt an der Zeilenposition eine Matrix oder einen Vektor als neue Zeilen ein

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 3 Argumente.

## Syntax

```text
mrinsert(matrix, matrixOderVektor, position)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `matrixOderVektor` | Parameter der Funktion. | Matrix | nein |
| `position` | Parameter der Funktion. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `mrinsert([[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15]],1)`  
**Ergebnis:** [[1,2,3],[10,11,12],[13,14,15],[4,5,6],[7,8,9]]

| Ausdruck | Ergebnis |
| --- | --- |
| mrinsert(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,&#91;&#91;10,11,12&#93;,&#91;13,14,15&#93;&#93;,1) | &#91;&#91;1,2,3&#93;,&#91;10,11,12&#93;,&#91;13,14,15&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3459)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `MRInsert`.

[Zurück zu Berechnungen](../../../index.md)
