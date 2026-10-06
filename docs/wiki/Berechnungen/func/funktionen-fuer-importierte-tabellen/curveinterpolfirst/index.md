# curveinterpolfirst

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`curveinterpolfirst` – Funktionen für importierte Tabellen.

## Detaillierte Beschreibung

Interpoliert in einer gespeicherten Tabelle und liefert den ersten interpolierten Punkt auf der Kennlinie.

## Syntax

```text
curveinterpolfirst(tabelle, xSpalte, ySpalte, wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `tabelle` | Parameter der Funktion. | Matrix | nein |
| `xSpalte` | Parameter der Funktion. | Vektor / Zahl | nein |
| `ySpalte` | Parameter der Funktion. | Vektor / Zahl | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `curveinterpolfirst(KL,0,1,1.5)`  
**Ergebnis:** 2.1

| Ausdruck | Ergebnis |
| --- | --- |
| curveinterpolfirst(KL,0,1,1.5) | 2.1 |

## Demobeispiele

In der bereitgestellten Übersicht ist kein Demobeispiel verlinkt.

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `CurveInterpolationFirst`.

[Zurück zu Berechnungen](../../../index.md)
