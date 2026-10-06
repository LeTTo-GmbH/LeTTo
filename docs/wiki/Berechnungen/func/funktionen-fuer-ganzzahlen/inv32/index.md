# inv32

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`inv32` – Funktionen für Ganzzahlen.

## Detaillierte Beschreibung

bitweise Invertieren und die letzten 32 Bit bestimmen

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
inv32(x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl/Ausdruck | nein |

## Beispiele

**Beispiel:** `inv32(0xF0)`  
**Ergebnis:** 0bFFFFFF0F

| Ausdruck | Ergebnis |
| --- | --- |
| inv32(0xF0) | 0bFFFFFF0F |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateBitOperators.java`, Klasse `INV32`.

[Zurück zu Berechnungen](../../../index.md)
