# shl

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`shl` – Funktionen für Ganzzahlen.

## Detaillierte Beschreibung

Schiebe Ganzzahl bitweise nach links

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

Die Implementierung verwendet BigInteger.shiftLeft. Ohne zweiten Parameter wird um ein Bit geschoben. Für positive Schiebeanzahl entspricht dies einer Multiplikation mit einer Zweierpotenz; ein negativer Wert kehrt die Schieberichtung um.

## Syntax

```text
shl(wert)
shl(wert, stellen)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `stellen` | Parameter der Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `shl(8,2)`  
**Ergebnis:** 32

| Ausdruck | Ergebnis |
| --- | --- |
| shl(8,2) | 32 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateBitOperators.java`, Klasse `SHL`.

[Zurück zu Berechnungen](../../../index.md)
