# verweisup

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`verweisup` – Algebra.

## Detaillierte Beschreibung

verweisup(M,x,n) liefert den Wert der n-ten Spalte (ohne Angabe von n die 2.Spalte) einer Matrix M wo x dem Wert in der ersten Spalte am nächsten liegt

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

## Syntax

```text
verweisup(matrix, wert, spalte)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix` | Matrix, auf der die Operation ausgeführt wird. | Matrix | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `spalte` | Parameter der Funktion. | Matrix / Ganzzahl | nein |

## Beispiele

**Beispiel:** `verweisup([[10,33],[20,77],[30,99]],21)`  
**Ergebnis:** 99

| Ausdruck | Ergebnis |
| --- | --- |
| verweisup(&#91;&#91;10,33&#93;,&#91;20,77&#93;,&#91;30,99&#93;&#93;,21) | 99 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3466)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VerweisUp`.

[Zurück zu Berechnungen](../../../index.md)
