# vabs

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vabs` – Algebra.

## Detaillierte Beschreibung

Berechnet den Betrag eines Vektors

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

## Syntax

```text
vabs(variable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

## Beispiele

**Beispiel:** `vabs([3,4])`  
**Ergebnis:** 5

| Ausdruck | Ergebnis |
| --- | --- |
| vabs(&#91;3,4&#93;) | 5 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3440)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VectorAbs`.

[Zurück zu Berechnungen](../../../index.md)
