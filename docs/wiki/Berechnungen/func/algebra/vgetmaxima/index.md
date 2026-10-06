# vgetmaxima

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`vgetmaxima` – Algebra.

## Detaillierte Beschreibung

liefert ein Element eines Vektors oder einer Matrix wobei der Index (wie bei Maxima) bei 1 startet.

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

## Syntax

```text
vgetmaxima(variable, anzahl)
vgetmaxima(variable, anzahl, string)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | nein |
| `anzahl` | Anzahl der Elemente, Stellen oder Wiederholungen. | Ganzzahl | nein |
| `string` | Zeichenkette, die verarbeitet werden soll. | String | ja (bei 3 Parametern) |

## Beispiele

**Beispiel:** `vgetmaxima([12,13,14],1)`  
**Ergebnis:** 12

| Ausdruck | Ergebnis |
| --- | --- |
| vgetmaxima(&#91;12,13,14&#93;,1) | 12 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3435)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `VGetMaxima`.

[Zurück zu Berechnungen](../../../index.md)
