# frac

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`frac` – Funktionen für rationale und Ganzzahlen.

## Detaillierte Beschreibung

erzeugt aus einer Menge aus 2 oder 3 Elementen (von defrac) eine rationale Zahl

## Syntax

```text
frac(v1)
frac(v1, anzahl)
frac(v1, anzahl, anzahl)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `v1` | Parameter der Funktion. | Vektor / Ganzzahl | nein |
| `anzahl` | Anzahl der Elemente, Stellen oder Wiederholungen. | Ganzzahl | ja (bei 2/3 Parametern) |
| `anzahl` | Anzahl der Elemente, Stellen oder Wiederholungen. | Ganzzahl | ja (bei 3 Parametern) |

## Beispiele

**Beispiel:** `frac([3,7]) frac([1,2,3])`  
**Ergebnis:** 3/7 5/3

| Ausdruck | Ergebnis |
| --- | --- |
| frac(&#91;3,7&#93;)<br>frac(&#91;1,2,3&#93;) | 3/7 <br> 5/3 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3204)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Frac`.

[Zurück zu Berechnungen](../../../index.md)
