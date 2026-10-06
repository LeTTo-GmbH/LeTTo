# matrix

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`matrix` – Algebra.

## Detaillierte Beschreibung

erzeugt aus mehreren gleich langen Vektoren eine Matrix

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

## Syntax

```text
matrix(...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `zeile1` | Parameter der Funktion. | Zahl/Ausdruck | ja, beliebig oft |

## Beispiele

**Beispiel:** `matrix([1,2],[3,4])`  
**Ergebnis:** [[1,2],[3,4]]

| Ausdruck | Ergebnis |
| --- | --- |
| matrix([1,2&#93;,&#91;3,4&#93;) | &#91;&#91;1,2&#93;,&#91;3,4&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3426)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `Matrix`.

[Zurück zu Berechnungen](../../../index.md)
