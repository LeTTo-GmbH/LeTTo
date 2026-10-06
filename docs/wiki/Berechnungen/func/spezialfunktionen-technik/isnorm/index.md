# isnorm

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`isnorm` – Spezialfunktionen Technik.

## Detaillierte Beschreibung

prüft ob der als Parameter übergebenen Wert ein Wert einer gegebenen Wertereihe oder Normreihe ist.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
isnorm(wert, normreihe)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `normreihe` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | nein |

## Beispiele

**Beispiel:** `isnorm(680Ohm,E12)`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| isnorm(680Ohm,E12) | true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3511)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `IsNORM`.

[Zurück zu Berechnungen](../../../index.md)
