# defrac

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`defrac` – Funktionen für rationale und Ganzzahlen.

## Detaillierte Beschreibung

zerlegt eine rationale Zahl in Zähler und Nenner als Menge Die erhaltene Menge kann mit dem Format-Modfier frac als gemischter Bruch dargestellt werden

zerlegt eine rationale Zahl in Zähler und Nenner als Menge <br>Die erhaltene Menge kann mit dem Format-Modfier **frac** als gemischter Bruch dargestellt werden

## Syntax

```text
defrac(wertOderZaehler)
defrac(wertOderZaehler, nenner)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wertOderZaehler` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `nenner` | Parameter der Funktion. | Vektor / Ganzzahl | ja (bei 2 Parametern) |

## Beispiele

**Beispiel:** `defrac(14/12)`  
**Ergebnis:** [13,12]

| Ausdruck | Ergebnis |
| --- | --- |
| defrac(14/12) | &#91;13,12&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3203)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `DeFrac`.

[Zurück zu Berechnungen](../../../index.md)
