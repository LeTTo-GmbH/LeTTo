# curveinterpol

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`curveinterpol` – Funktionen für importierte Tabellen.

## Detaillierte Beschreibung

Interpoliert in einer gespeicherten Tabelle zwischen den Stützpunkten. Als Ergebnis wird ein Vektor aller gefundenen Punkte auf der Kennlinie geliefert

## Syntax

```text
curveinterpol(tabelle, xSpalte, ySpalte, wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `tabelle` | Parameter der Funktion. | Matrix | nein |
| `xSpalte` | Parameter der Funktion. | Vektor / Zahl | nein |
| `ySpalte` | Parameter der Funktion. | Vektor / Zahl | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `curveinterpol(KL,0,1,3.5)`  
**Ergebnis:** [2.1]

| Ausdruck | Ergebnis |
| --- | --- |
| curveinterpol(KL,0,1,3.5) | &#91;2.1&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3385)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `CurveInterpolation`.

[Zurück zu Berechnungen](../../../index.md)
