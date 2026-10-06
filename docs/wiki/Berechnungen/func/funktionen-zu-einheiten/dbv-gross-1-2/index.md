# dBV

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`dBV` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

Wandelt eine Spannung in dBV um. Bezugsspannung ist 1 V: `20*log10(U/1V)`. Bei komplexen Spannungen wird der Betrag verwendet; vorhandene dBV/dBmV/dBuV-Werte werden entsprechend umgerechnet.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
dBV(oe)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `dBV(1V)`  
**Ergebnis:** 0dBV

| Ausdruck | Ergebnis |
| --- | --- |
| dBV(1V) | 0dBV |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDbFunctions.java`, Klasse `DBV`.

[Zurück zu Berechnungen](../../../index.md)
