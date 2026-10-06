# setget

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setget` – Mengen-Funktionen.

## Detaillierte Beschreibung

Liefert ein Element einer Menge oder einer Matrix (Menge von Mengen)

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Mit zwei Argumenten wird ein Vektorelement oder eine Matrixzeile gelesen. Mit drei Argumenten wird ein Matrixelement gelesen. Die Indizes beginnen bei 0; für den Maxima-kompatiblen Zugriff mit Indizes ab 1 sind die entsprechenden Maxima-Varianten vorgesehen.

## Syntax

```text
setget(vektorOderMatrix, index)
setget(matrix, zeile, spalte)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| vektorOderMatrix | Vektor oder Matrix, aus dem ein Element gelesen werden soll. | Vektor / Matrix | nein |
| index / zeile | Elementindex oder Zeilenindex; beginnt bei 0. | Ganzzahl | nein |
| spalte | Spaltenindex bei Matrixzugriff; beginnt bei 0. | Ganzzahl | ja, für Matrixelement |

## Beispiele

**Beispiel:** `setget([12,13,14],1) setget(matrix([9,2],[3,4]),0,1)`  
**Ergebnis:** 13 2

| Ausdruck | Ergebnis |
| --- | --- |
| setget(&#91;12,13,14&#93;,1) <br> setget(matrix([9,2&#93;,[3,4&#93;),0,1) | 13 <br> 2 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3341)

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
