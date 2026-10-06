# fourth

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`fourth` – Algebra.

## Detaillierte Beschreibung

liefert das vierte Element mit dem Index 3 eines Vektors

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

## Syntax

```text
fourth()
fourth(variable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | ja |

## Beispiele

**Beispiel:** `fourth ([12,13,14,15,16,17,18])`  
**Ergebnis:** 15

| Ausdruck | Ergebnis |
| --- | --- |
| fourth (&#91;12,13,14,15,16,17,18&#93;) | 15 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3432)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `Fourth`.

[Zurück zu Berechnungen](../../../index.md)
