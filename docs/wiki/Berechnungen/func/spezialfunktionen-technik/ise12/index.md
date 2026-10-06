# ise12

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`ise12` – Spezialfunktionen Technik.

## Detaillierte Beschreibung

prüft ob der als Parameter übergebenen Wert ein Wert der Normreihe E12 ist.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
ise12(wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `ise12(680Ohm)`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| ise12(680Ohm) | true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3506)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `IsE12`.

[Zurück zu Berechnungen](../../../index.md)
