# setcount

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`setcount` – Mengen-Funktionen.

## Detaillierte Beschreibung

Bestimmt die Anzahl wie oft ein Element in einer Menge vorkommt oder die Anzahl der Elemente der Menge

## Syntax

```text
setcount(menge)
setcount(menge, wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `menge` | Menge bzw. Vektor, auf dem die Operation ausgeführt wird. | Vektor / Matrix | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | ja (bei 2 Parametern) |

## Beispiele

**Beispiel:** `setcount([31,-3,2,31,0,5,2],31) setcount([2,5,3,6])`  
**Ergebnis:** 2 4

| Ausdruck | Ergebnis |
| --- | --- |
| setcount(&#91;31,-3,2,31,0,5,2&#93;,31) <br> setcount(&#91;2,5,3,6&#93;) | 2 <br> 4 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3352)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMengenFunctions.java`, Klasse `SetCount`.

[Zurück zu Berechnungen](../../../index.md)
