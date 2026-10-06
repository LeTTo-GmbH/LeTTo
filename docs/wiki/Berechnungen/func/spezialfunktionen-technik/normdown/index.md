# normdown

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`normdown` – Spezialfunktionen Technik.

## Detaillierte Beschreibung

rundet einen Zahlenwert auf den nächstkleineren Wert einer gegebenen Wertereihe oder Normreihe.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
normdown(wert, normreihe)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `normreihe` | Parameter der Funktion. | Zahl | nein |

## Beispiele

**Beispiel:** `normdown(700Ohm,E12)`  
**Ergebnis:** 680Ohm

| Ausdruck | Ergebnis |
| --- | --- |
| normdown(700Ohm,E12) | 680Ohm |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3509)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `NORMdown`.

[Zurück zu Berechnungen](../../../index.md)
