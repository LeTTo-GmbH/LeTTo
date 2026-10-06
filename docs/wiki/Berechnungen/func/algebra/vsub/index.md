# vsub

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vsub` – Algebra.

## Detaillierte Beschreibung

Subtrahiert zwei Vektoren elementweise

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
vsub(v1, v2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor | nein |
| `v2` | Parameter der Funktion. | Vektor | nein |

## Beispiele

**Beispiel:** `vsub([1,2,3],[4,5,6])`  
**Ergebnis:** [-3,-3,-3]

| Ausdruck | Ergebnis |
| --- | --- |
| vsub(&#91;1,2,3&#93;,&#91;4,5,6&#93;) | &#91;-3,-3,-3&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3444)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VectorSub`.

[Zurück zu Berechnungen](../../../index.md)
