# defracmix

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`defracmix` – Funktionen für rationale und Ganzzahlen.

## Detaillierte Beschreibung

zerlegt eine rationale Zahl in einen gemischten Bruch aus ganzzahligem Summanden, Zähler und Nenner als Menge Die erhaltene Menge kann mit dem Format-Modfier frac als gemischter Bruch dargestellt werden (siehe Zahlendarstellung)

zerlegt eine rationale Zahl in einen gemischten Bruch aus ganzzahligem Summanden, Zähler und Nenner als Menge<br>Die erhaltene Menge kann mit dem Format-Modfier **frac** als gemischter Bruch dargestellt werden (siehe [Zahlendarstellung](../../../../Zahlendarstellung/index.md))

## Syntax

```text
defracmix(wertOderGanzzahl)
defracmix(wertOderGanzzahl, nennerOderZaehler)
defracmix(wertOderGanzzahl, nennerOderZaehler, nenner)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wertOderGanzzahl` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `nennerOderZaehler` | Parameter der Funktion. | Vektor / Ganzzahl | ja (bei 2/3 Parametern) |
| `nenner` | Parameter der Funktion. | Ganzzahl | ja (bei 3 Parametern) |

## Beispiele

**Beispiel:** `defracmix(14/12) defracmix(-15/12) defracmix(3/12)`  
**Ergebnis:** [1,2/12] [-1,3,12] [0,3,12]

| Ausdruck | Ergebnis |
| --- | --- |
| defracmix(14/12)<br>defracmix(-15/12)<br>defracmix(3/12) | &#91;1,2/12&#93;<br>&#91;-1,3,12&#93;<br>&#91;0,3,12&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3202)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `DeFracMix`.

[Zurück zu Berechnungen](../../../index.md)
