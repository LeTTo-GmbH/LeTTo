# csch

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`csch` – trigonometrische Funktionen.

## Detaillierte Beschreibung

Kosecans-Hyperbolicus, `csch(x)=1/sinh(x)`.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Berechnet den Kosekans hyperbolicus. Die mathematische Definition lautet `1/sinh(x)`. Bei x = 0 ist der reelle Quotient nicht definiert.

## Syntax

```text
csch(x1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

## Beispiele

**Beispiel:** `csch(1)`  
**Ergebnis:** 0.850918...

| Ausdruck | Ergebnis |
| --- | --- |
| csch(1) | 0.850918... |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTrigonometricFunctions.java`, Klasse `Csch`.

[Zurück zu Berechnungen](../../../index.md)
