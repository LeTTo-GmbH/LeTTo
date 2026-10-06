# msub

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`msub` – Algebra.

## Detaillierte Beschreibung

msub(matrix,zeile,spalte,zeilen,spalten) Liefert eine Untermatrix beginnend bei Zeile und Spalten mit der angegebenen Anzahl von Zeilen und Spalten. Die Parameter Spalte,Zeilen und Spalten sind dabei optional.

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet 2 bis 5 Argumente.

## Syntax

```text
msub(matrix, oz)
msub(matrix, oz, os, zeilen, spalten)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `oz` | Parameter der Funktion. | Matrix / Ganzzahl | nein |
| `os` | Parameter der Funktion. | Matrix / Ganzzahl | ja |
| `zeilen` | Parameter der Funktion. | Vektor / Matrix | ja |
| `spalten` | Parameter der Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `msub([[1,2,3],[4,5,6],[7,8,9]],0,1,2,2)`  
**Ergebnis:** [[2,3],[5,6]]

| Ausdruck | Ergebnis |
| --- | --- |
| msub(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,0,1,2,2) | &#91;&#91;2,3&#93;,&#91;5,6&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3456)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `MSub`.

[Zurück zu Berechnungen](../../../index.md)
