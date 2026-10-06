# vinsert

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vinsert` – Algebra.

## Detaillierte Beschreibung

fügt ein Element in eine Menge an eine gegebene Stelle ein

Alias/Kompatibilitätsname zu `setinsert`.

fügt ein Element in einen Vektor an eine gegebene Stelle ein

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [setinsert](../../mengen-funktionen/setinsert/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

## Syntax

```text
vinsert(menge, index, wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `menge` | Menge bzw. Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `index` | Index des gewünschten Elements; die Zählweise richtet sich nach der jeweiligen Funktion. | Ganzzahl | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `vinsert([12,13,14],1,25)`  
**Ergebnis:** [12,25,13,14]

| Ausdruck | Ergebnis |
| --- | --- |
| vinsert(&#91;12,13,14&#93;,1,25) | &#91;12,25,13,14&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3438)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VInsert`.

[Zurück zu Berechnungen](../../../index.md)
