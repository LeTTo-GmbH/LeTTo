# vex

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vex` – Algebra.

## Detaillierte Beschreibung

Berechnet das ex-Produkt von 2 Vektoren im 3-dimensionalen Raum

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
vex(v1, v2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Zahl | nein |
| `v2` | Parameter der Funktion. | Vektor / Zahl | nein |

## Beispiele

**Beispiel:** `vex([1,2,3],[4,5,6])`  
**Ergebnis:** [-3,6,-3]

| Ausdruck | Ergebnis |
| --- | --- |
| vex(&#91;1,2,3&#93;,&#91;4,5,6&#93;) | &#91;-3,6,-3&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3442)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VectorEx`.

[Zurück zu Berechnungen](../../../index.md)
