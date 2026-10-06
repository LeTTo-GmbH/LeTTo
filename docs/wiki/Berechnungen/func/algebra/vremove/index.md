# vremove

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vremove` – Algebra.

## Detaillierte Beschreibung

löscht ein Element einer Menge

Alias/Kompatibilitätsname zu `setremove`.

löscht ein Element eines Vektors [Video](https://www.youtube.com/watch?v=T82YIt3e8ac)

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [setremove](../../mengen-funktionen/setremove/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

## Syntax

```text
vremove(variable, anzahl)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `anzahl` | Anzahl der Elemente, Stellen oder Wiederholungen. | Ganzzahl | nein |

## Beispiele

**Beispiel:** `vremove([12,13,14],1)`  
**Ergebnis:** [12,14]

| Ausdruck | Ergebnis |
| --- | --- |
| vremove(&#91;12,13,14&#93;,1) | &#91;12,14&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3439)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VRemove`.

[Zurück zu Berechnungen](../../../index.md)
