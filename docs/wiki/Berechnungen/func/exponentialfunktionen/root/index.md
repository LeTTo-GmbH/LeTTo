# root

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`root` – Exponentialfunktionen.

## Detaillierte Beschreibung

Quadratwurzel. Entspricht `root(x,2)`.

Alias/Kompatibilitätsname zu `sqrt`.

n-te Wurzel `root(x,n)`; ohne zweiten Parameter wird die Quadratwurzel verwendet.

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [sqrt](../sqrt/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet 1 bis 2 Argumente.

Ohne zweiten Parameter wird die Quadratwurzel berechnet. Der optionale zweite Parameter legt den Wurzelexponenten fest; mathematisch entspricht dies `wert^(1/wurzelexponent)`. Für reelle positive Werte ist die Quadratwurzel die nicht negative Zahl, deren Quadrat den Ausgangswert ergibt.

## Syntax

```text
root(wert)
root(wert, wurzelexponent)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wurzelexponent` | Parameter der Funktion. | Zahl / Ausdruck | ja |

## Beispiele

**Beispiel:** `root(8,3)`  
**Ergebnis:** 2

| Ausdruck | Ergebnis |
| --- | --- |
| root(8,3) | 2 |

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
