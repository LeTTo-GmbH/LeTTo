# range

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`range` – Algebra.

## Detaillierte Beschreibung

range(anzahl) liefert ein Feld von ganzzahligen Werten von 0 beginnend

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
range(x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Vektor / Ganzzahl | nein |

## Beispiele

**Beispiel:** `range(5)`  
**Ergebnis:** [0,1,2,3,4]

| Ausdruck | Ergebnis |
| --- | --- |
| range(5) | &#91;0,1,2,3,4&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3468)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `Range`.

[Zurück zu Berechnungen](../../../index.md)
