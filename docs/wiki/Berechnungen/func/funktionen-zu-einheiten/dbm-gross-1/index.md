# dBm

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`dBm` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

Wandelt eine Leistung in dBm um. Bezugsleistung ist 1 mW: `10*log10(P/1mW)`. Bei komplexen Leistungen wird der Betrag verwendet; vorhandene dBW/dBm/dBu-Werte werden entsprechend umgerechnet.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
dBm(oe)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `dBm(1mW)`  
**Ergebnis:** 0dBm

| Ausdruck | Ergebnis |
| --- | --- |
| dBm(1mW) | 0dBm |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDbFunctions.java`, Klasse `DBm`.

[Zurück zu Berechnungen](../../../index.md)
