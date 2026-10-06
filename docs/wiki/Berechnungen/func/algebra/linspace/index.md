# linspace

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`linspace` – Algebra.

## Detaillierte Beschreibung

linspace(start,ende,anzahl) liefert ein Feld von Werte von Startwert bis Endwert mit gleichem Abstand

### Anwendung und Besonderheiten

Funktionsindizes zählen grundsätzlich ab 0. Bei `vgetmaxima` und `vsetmaxima` gelten die Maxima-kompatiblen Varianten; Zugriffe mit eckigen Klammern wie `M[2,3]` zählen ab 1. Beispiel: `vget(M,1,2)` entspricht `M[2,3]`.

Die Implementierung erwartet genau 3 Argumente.

## Syntax

```text
linspace(von, bis, anz)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `von` | Untere Grenze bzw. Startwert. | Ganzzahl / Zahl | nein |
| `bis` | Obere Grenze bzw. Endwert. | Ganzzahl / Zahl | nein |
| `anz` | Parameter der Funktion. | Ganzzahl / Zahl | nein |

## Beispiele

**Beispiel:** `linspace(4,8,5)`  
**Ergebnis:** [4,5,6,7,8]

| Ausdruck | Ergebnis |
| --- | --- |
| linspace(4,8,5) | &#91;4,5,6,7,8&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3469)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateAlgebraFunctions.java`, Klasse `LinSpace`.

[Zurück zu Berechnungen](../../../index.md)
