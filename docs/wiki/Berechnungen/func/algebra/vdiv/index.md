# vdiv

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vdiv` – Algebra.

## Detaillierte Beschreibung

Dividiert zwei Vektoren elementweise

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
vdiv(v1, v2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor | nein |
| `v2` | Parameter der Funktion. | Vektor | nein |

## Beispiele

**Beispiel:** `vdiv([1,2,3],[4,5,6])`  
**Ergebnis:** [1/3,2/5,3/6]

| Ausdruck | Ergebnis |
| --- | --- |
| vdiv(&#91;1,2,3&#93;,&#91;4,5,6&#93;) | &#91;1/3,2/5,3/6&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3446)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VectorDiv`.

[Zurück zu Berechnungen](../../../index.md)
