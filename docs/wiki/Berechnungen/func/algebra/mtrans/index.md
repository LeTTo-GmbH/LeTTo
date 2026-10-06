# mtrans

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`mtrans` – Algebra.

## Detaillierte Beschreibung

Bildet die transponierte Matrix

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
mtrans(matrix)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |

## Beispiele

**Beispiel:** `mtrans([[1,2],[3,4]])`  
**Ergebnis:** [[1,3],[2,4]]

| Ausdruck | Ergebnis |
| --- | --- |
| mtrans(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;) | &#91;&#91;1,3&#93;,&#91;2,4&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3451)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `MatrixTranspose`.

[Zurück zu Berechnungen](../../../index.md)
