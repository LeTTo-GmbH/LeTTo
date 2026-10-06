# mrdelete

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`mrdelete` – Algebra.

## Detaillierte Beschreibung

mrdelete(matrix,position) Löscht die angegebene Zeile aus einer Matrix

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
mrdelete(matrix, pos)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `pos` | Parameter der Funktion. | Matrix / Ganzzahl | nein |

## Beispiele

**Beispiel:** `mrdelete([[1,2,3],[4,5,6],[7,8,9]],1)`  
**Ergebnis:** [[1,2,3],[7,8,9]]

| Ausdruck | Ergebnis |
| --- | --- |
| mrdelete(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,1) | &#91;&#91;1,2,3&#93;,&#91;7,8,9&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3461)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `MRDelete`.

[Zurück zu Berechnungen](../../../index.md)
