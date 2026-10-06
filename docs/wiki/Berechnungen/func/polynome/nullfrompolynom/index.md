# nullfrompolynom

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`nullfrompolynom` – Polynome.

## Detaillierte Beschreibung

Erzeugt aus einem Polynom einen Vektor mit den PolynomNullstellen und Polstellen. Erste Zeile gemeinsamer Faktor, zweite Zeile Nullstellen, dritte Zeile Polstellen, vierte Zeile Polynomvariable

## Syntax

```text
nullfrompolynom(polynom)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `polynom` | Parameter der Funktion. | Zahl/Ausdruck | nein |

## Beispiele

**Beispiel:** `nullfrompolynom(polynom((2+x)/(1+2*x)))`  
**Ergebnis:** [0.5,[-2],[-0.5],x]

| Ausdruck | Ergebnis |
| --- | --- |
| nullfrompolynom(polynom((2+x)/(1+2*x))) | &#91;0.5,&#91;-2&#93;,&#91;-0.5&#93;,x&#93; |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePolynomFunctions.java`, Klasse `NullFromPolynom`.

[Zurück zu Berechnungen](../../../index.md)
