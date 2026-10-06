# sqrt

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`sqrt` – Exponentialfunktionen.

## Detaillierte Beschreibung

Quadratwurzel. Entspricht `root(x,2)`.

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

Ohne zweiten Parameter wird die Quadratwurzel berechnet. Der optionale zweite Parameter legt den Wurzelexponenten fest; mathematisch entspricht dies `wert^(1/wurzelexponent)`. Für reelle positive Werte ist die Quadratwurzel die nicht negative Zahl, deren Quadrat den Ausgangswert ergibt.

## Syntax

```text
sqrt(wert)
sqrt(wert, wurzelexponent)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wurzelexponent` | Parameter der Funktion. | Zahl / Ausdruck | ja |

## Beispiele

**Beispiel:** `sqrt(9)`  
**Ergebnis:** 3

| Ausdruck | Ergebnis |
| --- | --- |
| sqrt(9) | 3 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Sqrt`.

[Zurück zu Berechnungen](../../../index.md)
