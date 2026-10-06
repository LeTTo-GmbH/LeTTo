# todB

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`todB` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

versieht einen Zahlenwert mit der skalierenden Dezibel-Einheit dB welche mit 20*log10 berechnet wird

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
todB(oe)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oe` | Parameter der Funktion. | Zahl | nein |

## Beispiele

**Beispiel:** `todB(100) todB(100)*2`  
**Ergebnis:** 40dB 200

| Ausdruck | Ergebnis |
| --- | --- |
| todB(100)<br> todB(100)*2 | 40dB <br> 200 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3215)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDbFunctions.java`, Klasse `ToDB`.

[Zurück zu Berechnungen](../../../index.md)
