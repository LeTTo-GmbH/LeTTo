# factfrompolynom

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`factfrompolynom` – Polynome.

## Detaillierte Beschreibung

Erzeugt aus einem Polynom einen Vektor mit den Polynomfaktoren. Erste Zeile Zählerfaktoren, zweite Zeile Nennerfaktoren, dritte Zeile Polynomvariable, vierte Zeile Einheit der Polynomvariable

## Syntax

```text
factfrompolynom(polynom)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `polynom` | Parameter der Funktion. | Zahl/Ausdruck | nein |

## Beispiele

**Beispiel:** `factfrompolynom(polynom((2+x)/(1+2*x)))`  
**Ergebnis:** [[1,0.5],[0.5,1],"x",""]

| Ausdruck | Ergebnis |
| --- | --- |
| factfrompolynom(polynom((2+x)/(1+2*x))) | &#91;&#91;1,0.5&#93;,&#91;0.5,1&#93;,"x",""&#93; |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePolynomFunctions.java`, Klasse `FactFromPolynom`.

[Zurück zu Berechnungen](../../../index.md)
