# vset

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vset` – Algebra.

## Detaillierte Beschreibung

setzt ein Element einer Menge oder einer Matrix (Menge von Mengen)

Alias/Kompatibilitätsname zu `setset`.

setzt ein Element eines Vektors oder einer Matrix

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [setset](../../mengen-funktionen/setset/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

## Syntax

```text
vset(mengeOderMatrix, indexOderZeile, wertOderSpalte)
vset(mengeOderMatrix, indexOderZeile, wertOderSpalte, wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `mengeOderMatrix` | Parameter der Funktion. | Matrix | nein |
| `indexOderZeile` | Parameter der Funktion. | Ganzzahl | nein |
| `wertOderSpalte` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja (bei 4 Parametern) |

## Beispiele

**Beispiel:** `vset([12,13,14],1,35) vset(matrix([9,2],[3,4]),0,0,-9)`  
**Ergebnis:** [12,35,14] [[-9,2],[3,4]]

| Ausdruck | Ergebnis |
| --- | --- |
| vset(&#91;12,13,14&#93;,1,35) <br> vset(matrix(&#91;9,2&#93;,&#91;3,4&#93;),0,0,-9) | &#91;12,35,14&#93; <br> &#91;&#91;-9,2&#93;,&#91;3,4&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3436)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VSet`.

[Zurück zu Berechnungen](../../../index.md)
