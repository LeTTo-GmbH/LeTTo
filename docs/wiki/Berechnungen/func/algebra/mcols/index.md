# mcols

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`mcols` – Algebra.

## Detaillierte Beschreibung

liefert die Anzahl der Spalten einer Matrix

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
mcols(m1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `m1` | Parameter der Funktion. | Matrix / Vektor | nein |

## Beispiele

**Beispiel:** `mcols([[3,4,4],[3,6,54,34,3,54]])`  
**Ergebnis:** 6

| Ausdruck | Ergebnis |
| --- | --- |
| mcols(&#91;&#91;3,4,4&#93;,&#91;3,6,54,34,3,54&#93;&#93;) | 6 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3449)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `MCols`.

[Zurück zu Berechnungen](../../../index.md)
