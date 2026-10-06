# mod2

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`mod2` – Funktionen für rationale und Ganzzahlen.

## Detaillierte Beschreibung

Symmetrische Implementierung von modulo: Divisionsrest einer Division mit ganzzahligem Ergebnis Der Unterschied zu mod liegt in der Behandlung von negativen Zahlen des ersten Arguments Siehe auch Divisionsrest des Parser-Operators % Berechnungen arithmetische-operatoren-

Bei Ganzzahlen verwendet die Implementierung den Java-Rest `a % b`. Das Vorzeichen eines von 0 verschiedenen Restes folgt dem Dividenden. Beispiel: `mod2(-5,3) = -2`. Der Divisor darf nicht 0 sein. Bei physikalischen Zahlen müssen die Einheiten übereinstimmen.

## Syntax

```text
mod2(re1, re2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re1` | Parameter der Funktion. | Ganzzahl / Zahl | nein |
| `re2` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

## Beispiele

**Beispiel:** `mod2(5,2) mod2(6.2,2.5) mod2(-4,3)`  
**Ergebnis:** 1 1.2 -1

| Ausdruck | Ergebnis |
| --- | --- |
| mod2(5,2) <br> mod2(6.2,2.5) <br> mod2(-4,3) | 1<br>1.2 <br> -1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3206)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticOperators.java`, Klasse `MOD2`.

[Zurück zu Berechnungen](../../../index.md)
