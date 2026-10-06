# polynomk

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`polynomk` – Polynome.

## Detaillierte Beschreibung

Bestimmt den Faktor, welcher vom Polynom herausgehoben werden kann, so dass die höchste Potenz der Polynomvariable den Multiplikator Eins hat.

## Syntax

```text
polynomk(polynom)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `polynom` | Parameter der Funktion. | Zahl/Ausdruck | nein |

## Beispiele

**Beispiel:** `polynomk(polynom((2+x)/(1+2*x)))`  
**Ergebnis:** 0.5

| Ausdruck | Ergebnis |
| --- | --- |
| polynomk(polynom((2+x)/(1+2*x))) | 0.5 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePolynomFunctions.java`, Klasse `PolynomK`.

[Zurück zu Berechnungen](../../../index.md)
