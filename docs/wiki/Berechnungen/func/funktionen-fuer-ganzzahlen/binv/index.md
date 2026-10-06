# binv

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`binv` – Funktionen für Ganzzahlen.

## Detaillierte Beschreibung

bitweises NICHT mit 8 bit

### Anwendung und Besonderheiten

Es werden ausschließlich die unteren 8 Bit invertiert. Diese Funktion ist von der unbeschränkten BigInteger-Inversion und dem Prefixoperator `~` zu unterscheiden.

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
binv(x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl/Ausdruck | nein |

## Beispiele

**Beispiel:** `binv(0x0F)`  
**Ergebnis:** 0xF0

| Ausdruck | Ergebnis |
| --- | --- |
| binv(0x0F) | 0xF0 |

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
