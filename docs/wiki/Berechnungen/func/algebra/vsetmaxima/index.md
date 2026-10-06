# vsetmaxima

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vsetmaxima` – Algebra.

## Detaillierte Beschreibung

setzt ein Element eines Vektors oder einer Matrix wobei der Index (wie bei Maxima) bei 1 startet.

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

## Syntax

```text
vsetmaxima(vektorOderMatrix, indexOderZeile, wertOderSpalte)
vsetmaxima(vektorOderMatrix, indexOderZeile, wertOderSpalte, wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `vektorOderMatrix` | Parameter der Funktion. | Matrix | nein |
| `indexOderZeile` | Parameter der Funktion. | Ganzzahl | nein |
| `wertOderSpalte` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja (bei 4 Parametern) |

## Beispiele

**Beispiel:** `vsetmaxima([12,13,14],1,35)`  
**Ergebnis:** [35,13,14]

| Ausdruck | Ergebnis |
| --- | --- |
| vsetmaxima(&#91;12,13,14&#93;,1,35) | &#91;35,13,14&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3437)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VSetMaxima`.

[Zurück zu Berechnungen](../../../index.md)
