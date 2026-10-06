# eh

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`eh` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

Liefert zu einem numerischen Wert die zugehörige Einheit als Wert 1 zurück; bei einem einheitenlosen Wert wird `1` geliefert.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
eh(wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `eh(2.3mA)`  
**Ergebnis:** 1mA

| Ausdruck | Ergebnis |
| --- | --- |
| eh(2.3mA) | 1mA |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `Eh`.

[Zurück zu Berechnungen](../../../index.md)
