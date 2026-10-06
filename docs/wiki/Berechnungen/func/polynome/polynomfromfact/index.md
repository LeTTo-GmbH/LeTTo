# polynomfromfact

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`polynomfromfact` – Polynome.

## Detaillierte Beschreibung

Erzeugt aus einer Faktoren-Liste, welche mit factfrompolynom erstellt wurde ein neues Polynom

Erzeugt aus Zähler und Nenner Faktor-Vektoren ein neues Polynom

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 4 Argumente.

## Syntax

```text
polynomfromfact(faktoren)
polynomfromfact(faktoren, variable)
polynomfromfact(zaehler, nenner, variable)
polynomfromfact(zaehler, nenner, variable, einheit)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| faktoren | Vektor der Faktoren oder strukturierter Vektor mit Zähler- und Nennerfaktoren. | Vektor | alternative Kurzform |
| zaehler | Faktoren des Zählers. | Vektor | Langform |
| nenner | Faktoren des Nenners. | Vektor | Langform |
| variable | Polynomvariable. | Variable | ja |
| einheit | Einheit der Polynomvariable. | String / numerischer Wert mit Einheit | ja |

## Beispiele

**Beispiel:** `polynomfromfact([[1,0.5],[0.5,1],"x",""])`  
**Ergebnis:** (2+x)/(1+2*x)

| Ausdruck | Ergebnis |
| --- | --- |
| polynomfromfact(&#91;&#91;1,0.5&#93;,&#91;0.5,1&#93;,"x",""&#93;) | (2+x)/(1+2*x) |

| Ausdruck | Ergebnis |
| --- | --- |
| polynomfromfact(&#91;1,0.5&#93;,&#91;0.5,1&#93;,x,"") | (2+x)/(1+2*x) |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePolynomFunctions.java`, Klasse `PolynomFromFact`.

[Zurück zu Berechnungen](../../../index.md)
