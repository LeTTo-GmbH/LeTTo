# polynom

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`polynom` – Polynome.

## Detaillierte Beschreibung

Erzeugt aus einem Ausdruck welcher genau eine Variable besitzen muss ein Polynom in dieser Variablen

Erzeugt aus einem Ausdruck ein Polynom in einer definierten Variablen. Ist p ein gültiger Polynom-Ausdruck mit reelen Koeffizienten in der Variablen var wird das Polynom erzeugt, ansonsten bleibt die Funktion erhalten.

Erzeugt ein Polynom in der Variablen var, mit der Einheit "einheit" für die Polynomvariable. Die Einheit muss als String in Doppelhochkomma angegeben werden! Das Polynom p muss entweder ohne Einheiten oder mit den korrekten Einheiten angegeben werden!

### Anwendung und Besonderheiten

Erzeugt eine interne Polynomdarstellung aus einem Ausdruck. Optional können die Polynomvariable, ihre Einheit und eine Zieleinheit angegeben werden. Die Zieleinheit ist der vierte Parameter. Die Parameterreferenz nennt `polynom()`; der mitgelieferte Code greift jedoch immer auf das erste Argument zu. Deshalb ist diese parameterlose Variante kein gültiges Anwendungsbeispiel.

Die Implementierung erwartet 0 bis 4 Argumente.

## Syntax

```text
polynom(ausdruck)
polynom(ausdruck, variable)
polynom(ausdruck, variable, einheit)
polynom(ausdruck, variable, einheit, zieleinheit)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| ausdruck | Als Polynom darzustellender Ausdruck. | Ausdruck | nein |
| variable | Name der Polynomvariable. | Variable | ja |
| einheit | Einheit der Polynomvariable. | String / numerischer Wert mit Einheit | ja |
| zieleinheit | Gewünschte Zieleinheit. | String | ja |

## Beispiele

**Beispiel:** `polynom(1+x)`  
**Ergebnis:** 1+x²

| Ausdruck | Ergebnis |
| --- | --- |
| polynom(1+x) | 1+x² |

| Ausdruck | Ergebnis |
| --- | --- |
| polynom(1+a*x^2,x) <br> polynom(1+2*x^2,x) | polynom(1+a*x^2,x)<br>1+2*x² |

| Ausdruck | Ergebnis |
| --- | --- |
| polynom(1+2*p^2,p,"s-1") <br> polynom(1+2's2'*p^2,p,"s-1") | 1+2's2'*p^2 <br>1+2's2'*p^2 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3337)

[DEMO-Beispiel](../../../../../demobsp.html?id=3338)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePolynomFunctions.java`, Klasse `Polynom`.

[Zurück zu Berechnungen](../../../index.md)
