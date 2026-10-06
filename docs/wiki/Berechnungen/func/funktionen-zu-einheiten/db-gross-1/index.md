# dB

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`dB` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

Wandelt einen Zahlenwert in eine nicht skalierende Dezibel-Einheit um. Einheitenlos wird in dB20 gewandelt, mit den Einheiten V,mV,uV,W,mW,uW wird in die zugehörige dB-Einheit gewandelt.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
dB(oe)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `dB(100) dB(100)+1`  
**Ergebnis:** 40 dB20 41

| Ausdruck | Ergebnis |
| --- | --- |
| dB(100) <br> dB(100)+1 | 40 dB<sub>20</sub> <br> 41 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3213)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDbFunctions.java`, Klasse `DB`.

[Zurück zu Berechnungen](../../../index.md)
