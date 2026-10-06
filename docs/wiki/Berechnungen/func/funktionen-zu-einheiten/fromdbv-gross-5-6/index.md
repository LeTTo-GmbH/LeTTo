# fromdBV

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`fromdBV` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

Wandelt einen dBV-Wert in eine Spannung zurück. Ein einheitenloser Zahlenwert wird als dBV interpretiert und als Spannung in V zurückgegeben.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
fromdBV(oe)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

## Beispiele

**Beispiel:** `fromdBV(0)`  
**Ergebnis:** 1V

| Ausdruck | Ergebnis |
| --- | --- |
| fromdBV(0) | 1V |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDbFunctions.java`, Klasse `FromDBV`.

[Zurück zu Berechnungen](../../../index.md)
