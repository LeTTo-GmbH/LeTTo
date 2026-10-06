# vindex

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vindex` – Algebra.

## Detaillierte Beschreibung

vindex(v,x) liefert den Index des Elementes eines Vektors, welcher am nächsten bei x liegt

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

## Syntax

```text
vindex(vektor, wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `vektor` | Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `vindex([10,30,70],40)`  
**Ergebnis:** 1

| Ausdruck | Ergebnis |
| --- | --- |
| vindex(&#91;10,30,70&#93;,40) | 1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3462)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `Vindex`.

[Zurück zu Berechnungen](../../../index.md)
