# vget

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vget` – Algebra.

## Detaillierte Beschreibung

Liefert ein Element einer Menge oder einer Matrix (Menge von Mengen)

Alias/Kompatibilitätsname zu `setget`.

liefert ein Element eines Vektors oder einer Matrix [Video](https://www.youtube.com/watch?v=T82YIt3e8ac)

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [setget](../../mengen-funktionen/setget/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Mit zwei Argumenten wird ein Vektorelement oder eine Matrixzeile gelesen. Mit drei Argumenten wird ein Matrixelement nach Zeile und Spalte gelesen. Die Funktionsindizes sind nullbasiert; ein Index außerhalb der Dimensionen wird im Code abgewiesen.

## Syntax

```text
vget(vektorOderMatrix, index)
vget(matrix, zeile, spalte)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| vektorOderMatrix | Vektor oder Matrix, aus dem ein Element gelesen werden soll. | Vektor / Matrix | nein |
| index / zeile | Elementindex oder Zeilenindex; beginnt bei 0. | Ganzzahl | nein |
| spalte | Spaltenindex bei Matrixzugriff; beginnt bei 0. | Ganzzahl | ja, für Matrixelement |

## Beispiele

**Beispiel:** `vget([12,13,14],1) vget(matrix([9,2],[3,4]),0,1)`  
**Ergebnis:** 13 2

| Ausdruck | Ergebnis |
| --- | --- |
| vget(&#91;12,13,14&#93;,1) <br> vget(matrix(&#91;9,2&#93;,&#91;3,4&#93;),0,1) | 13 <br> 2 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3428)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VGet`.

[Zurück zu Berechnungen](../../../index.md)
