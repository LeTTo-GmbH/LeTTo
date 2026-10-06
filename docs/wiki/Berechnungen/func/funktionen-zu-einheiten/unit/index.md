# unit

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`unit` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

gibt die SI-Einheit eines einheitenbehafteten Wertes mit dem Zahlenwert 1 ohne Einheitenvielfache zurück. numeric(x)*unit(x) liefert wieder x

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Gibt die zugehörige Einheit als Größe mit Zahlenwert 1 zurück, bei SI-Einheiten ohne das ursprüngliche Präfix. Beispiel: `unit(3.1kA)` ergibt 1 A.

## Syntax

```text
unit(oE)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `oE` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `unit(3.1kA) unit(5%)`  
**Ergebnis:** 1A 1%

| Ausdruck | Ergebnis |
| --- | --- |
| unit(3.1kA) <br> unit(5%) | 1A <br> 1% |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3180)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Unit`.

[Zurück zu Berechnungen](../../../index.md)
