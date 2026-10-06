# pvcompare

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`pvcompare` – Punkte-Mengen-Funktionen.

## Detaillierte Beschreibung

Vergleicht einen Referenz-Linienzug mit einem eingegebenen Linienzug unter Berücksichtigung der Toleranz. Die Toleranz stellt eine relative Tolerenz bezogen auf den Bereich zwischen MinXY und MaxXY da, wobei eine Toleranz von 0.1 gleichbedeutend 10 Prozent bezogen auf Max-Min ist (Mit dem String "a0.1" könnte man auch ein absolute Toleranz von 0.1 für x und y realisieren) pvcompare(Referenz,Eingabe) pvcompare(Referenz,Eingabe,Toleranz) pvcompare(Referenz,Eingabe,MinX,MaxX,MinY,MaxY) pvcompare(Referenz,Eingabe,MinX,MaxX,MinY,MaxY,Toleranz)

## Syntax

```text
pvcompare(referenz, eingabe)
pvcompare(referenz, eingabe, toleranz)
pvcompare(referenz, eingabe, toleranz, minX, maxX, minY)
pvcompare(referenz, eingabe, toleranz, minX, maxX, minY, maxY)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `referenz` | Referenz-Linienzug. | Vektor / Zahl | nein |
| `eingabe` | Zu vergleichender Linienzug. | Vektor / Zahl | nein |
| `toleranz` | Optionale Toleranz. | Zahl / Toleranzangabe | ja (bei 3/6/7 Parametern) |
| `minX` | Optionaler minimaler X-Wert des Bezugsbereichs. | Zahl | ja (bei 6/7 Parametern) |
| `maxX` | Optionaler maximaler X-Wert des Bezugsbereichs. | Zahl | ja (bei 6/7 Parametern) |
| `minY` | Optionaler minimaler Y-Wert des Bezugsbereichs. | Zahl | ja (bei 6/7 Parametern) |
| `maxY` | Optionaler maximaler Y-Wert des Bezugsbereichs. | Zahl/Ausdruck | ja (bei 7 Parametern) |

## Beispiele

**Beispiel:** `pvcompare([[0,0],[1,1],[2,1],[3,0]],[[0,0],[1,1],[2,1],[3,0]],0,3,-5,5)`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| pvcompare(&#91;&#91;0,0&#93;,&#91;1,1&#93;,&#91;2,1&#93;,&#91;3,0&#93;&#93;,&#91;&#91;0,0&#93;,&#91;1,1&#93;,&#91;2,1&#93;,&#91;3,0&#93;&#93;,0,3,-5,5) | true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3419)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6080

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePointVectorFunctions.java`, Klasse `PVCompare`.

[Zurück zu Berechnungen](../../../index.md)
