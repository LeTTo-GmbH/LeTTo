# mod

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`mod` – Funktionen für rationale und Ganzzahlen.

## Detaillierte Beschreibung

Mathematische Implementierung von modulo: Divisionsrest einer Division mit ganzzahligem Ergebnis

Bei Ganzzahlen verwendet die Implementierung `((a % b)+b)%b`. Für einen positiven Divisor liegt der Rest deshalb im Bereich von 0 bis knapp unter b. Beispiel: `mod(-5,3) = 1`. Der Divisor darf nicht 0 sein. Bei physikalischen Zahlen müssen die Einheiten übereinstimmen.

## Syntax

```text
mod(re1, re2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re1` | Parameter der Funktion. | Ganzzahl / Zahl | nein |
| `re2` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

## Beispiele

**Beispiel:** `mod(5,2) mod(6.2,2.5) mod(-4,3)`  
**Ergebnis:** 1 1.2 2

| Ausdruck | Ergebnis |
| --- | --- |
| mod(5,2) <br> mod(6.2,2.5) <br> mod(-4,3) | 1<br>1.2 <br> 2 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3205)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticOperators.java`, Klasse `MOD`.

[Zurück zu Berechnungen](../../../index.md)
