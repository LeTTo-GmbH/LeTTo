# inv

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`inv` – Algebra.

## Detaillierte Beschreibung

invertiert eine quadratische Matrix oder bildet 1/x

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
inv(wertOderMatrix)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wertOderMatrix` | Wert bzw. Ausdruck für die Berechnung. | Matrix | nein |

## Beispiele

**Beispiel:** `inv(matrix([1,2],[3,4]))`  
**Ergebnis:** [[-2,1],[3/2,-1/2]]

| Ausdruck | Ergebnis |
| --- | --- |
| inv(matrix(&#91;1,2&#93;,&#91;3,4&#93;)) | &#91;&#91;-2,1&#93;,&#91;3/2,-1/2&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3427)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `Inv`.

[Zurück zu Berechnungen](../../../index.md)
