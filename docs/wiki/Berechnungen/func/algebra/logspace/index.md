# logspace

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`logspace` – Algebra.

## Detaillierte Beschreibung

logspace(start,ende,anzahl) liefert ein Feld von Werte von Startwert bis Endwert mit gleichem logarithmischen Abstand

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 3 Argumente.

## Syntax

```text
logspace(von, bis, anz)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `von` | Untere Grenze bzw. Startwert. | Ganzzahl / Zahl | nein |
| `bis` | Obere Grenze bzw. Endwert. | Ganzzahl / Zahl | nein |
| `anz` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

## Beispiele

**Beispiel:** `logspace(10,10000,4)`  
**Ergebnis:** [10,100,1000,10000]

| Ausdruck | Ergebnis |
| --- | --- |
| logspace(10,10000,4) | &#91;10,100,1000,10000&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3470)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `LogSpace`.

[Zurück zu Berechnungen](../../../index.md)
