# inv8

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`inv8` – Funktionen für Ganzzahlen.

## Detaillierte Beschreibung

bitweises NICHT mit 8 bit

Alias/Kompatibilitätsname zu `binv`.

bitweise Invertieren und die letzten 8 Bit bestimmen

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [binv](../binv/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
inv8(x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl/Ausdruck | nein |

## Beispiele

**Beispiel:** `inv8(0b1001)`  
**Ergebnis:** 0b11110110

| Ausdruck | Ergebnis |
| --- | --- |
| inv8(0b1001) | 0b11110110 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateBitOperators.java`, Klasse `INV8`.

[Zurück zu Berechnungen](../../../index.md)
