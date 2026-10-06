# polynomfromnull

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`polynomfromnull` – Polynome.

## Detaillierte Beschreibung

Erzeugt aus einer Nullstellen-Polstellen-Liste, welche mit nullfrompolynom erstellt wurde ein neues Polynom

Erzeugt aus einer Faktor-Vektoren ein neues Polynom

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 4 Argumente.

## Syntax

```text
polynomfromnull(daten)
polynomfromnull(daten, variable)
polynomfromnull(faktor, nullstellen, variable)
polynomfromnull(faktor, nullstellen, polstellen, variable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| daten | Strukturierter Vektor mit Faktor, Nullstellen, optional Polstellen und Variablenname. | Vektor | alternative Kurzform |
| faktor | Multiplikativer Faktor. | reelle Zahl | Langform |
| nullstellen | Nullstellen des Zählers. | numerischer Wert / Vektor | Langform |
| polstellen | Nullstellen des Nenners. | numerischer Wert / Vektor | ja |
| variable | Polynomvariable; Standardname s. | Variable | ja |

## Beispiele

**Beispiel:** `polynomfromnull([0.5,[-2],[-0.5],x])`  
**Ergebnis:** (2+x)/(1+2*x)

| Ausdruck | Ergebnis |
| --- | --- |
| polynomfromnull(&#91;0.5,&#91;-2&#93;,&#91;-0.5&#93;,x&#93;) | (2+x)/(1+2*x) |

| Ausdruck | Ergebnis |
| --- | --- |
| polynomfromnull(0.5,&#91;-2&#93;,&#91;-0.5&#93;,x) | (2+x)/(1+2*x) |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePolynomFunctions.java`, Klasse `PolynomFromNull`.

[Zurück zu Berechnungen](../../../index.md)
