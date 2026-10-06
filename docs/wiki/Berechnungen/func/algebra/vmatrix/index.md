# vmatrix

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vmatrix` – Algebra.

## Detaillierte Beschreibung

Erzeugt aus genau einem Vektor eine Matrix. Enthaltene Vektoren werden zu Matrixzeilen, einzelne Werte zu ein-elementigen Zeilen; eine Matrix wird unverändert zurückgegeben.

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
vmatrix(variable)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |

## Beispiele

**Beispiel:** `vmatrix([[1,2],[3,4]])`  
**Ergebnis:** [[1,2],[3,4]]

| Ausdruck | Ergebnis |
| --- | --- |
| vmatrix(&#91;&#91;1,2&#93;,&#91;3,4&#93;&#93;) | &#91;&#91;1,2&#93;,&#91;3,4&#93;&#93; |

## Demobeispiele

In der bereitgestellten Übersicht ist kein Demobeispiel verlinkt.

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VMatrix`.

[Zurück zu Berechnungen](../../../index.md)
