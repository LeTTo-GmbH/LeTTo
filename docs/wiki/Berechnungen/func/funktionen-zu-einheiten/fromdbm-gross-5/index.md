# fromdBm

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`fromdBm` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

Wandelt einen dBm-Wert in eine Leistung zurück. Ein einheitenloser Zahlenwert wird als dBm interpretiert und als Leistung in mW zurückgegeben.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
fromdBm(oe)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

## Beispiele

**Beispiel:** `fromdBm(0)`  
**Ergebnis:** 1mW

| Ausdruck | Ergebnis |
| --- | --- |
| fromdBm(0) | 1mW |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDbFunctions.java`, Klasse `FromDBm`.

[Zurück zu Berechnungen](../../../index.md)
