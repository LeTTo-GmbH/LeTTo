# shr

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`shr` – Funktionen für Ganzzahlen.

## Detaillierte Beschreibung

Schiebe Ganzzahl bitweise nach rechts

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

Die Implementierung verwendet BigInteger.shiftRight. Ohne zweiten Parameter wird um ein Bit geschoben. Es handelt sich um ein arithmetisches Rechtsschieben mit Vorzeichenerhaltung; ein negativer Wert kehrt die Schieberichtung um.

## Syntax

```text
shr(wert)
shr(wert, stellen)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `stellen` | Parameter der Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `shr(8,2)`  
**Ergebnis:** 2

| Ausdruck | Ergebnis |
| --- | --- |
| shr(8,2) | 2 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateBitOperators.java`, Klasse `SHR`.

[Zurück zu Berechnungen](../../../index.md)
