# mrunion

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`mrunion` – Algebra.

## Detaillierte Beschreibung

Fügt mehrere Matrizen oder Vektoren zeileweise(untereinander) zusammen

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
mrunion(matrix1, wert2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `matrix1` | Parameter der Funktion. | Matrix | nein |
| `wert2` | Wert bzw. Ausdruck des 2. Parameters. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `mrunion([[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15]])`  
**Ergebnis:** [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]

| Ausdruck | Ergebnis |
| --- | --- |
| mrunion(&#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;&#93;,&#91;&#91;10,11,12&#93;,&#91;13,14,15&#93;&#93;) | &#91;&#91;1,2,3&#93;,&#91;4,5,6&#93;,&#91;7,8,9&#93;,&#91;10,11,12&#93;,&#91;13,14,15&#93;&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3455)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `MRUnion`.

[Zurück zu Berechnungen](../../../index.md)
