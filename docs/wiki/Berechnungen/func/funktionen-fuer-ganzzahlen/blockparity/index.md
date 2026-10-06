# blockparity

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`blockparity` – Funktionen für Ganzzahlen.

## Detaillierte Beschreibung

Kreuz oder Blockparität : blockparity(Parität,Codewortlänge,Codewortanzahl,Datenwort)

## Syntax

```text
blockparity(paritaet, codewortlaenge, codewortanzahl, datenwort, ...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `paritaet` | Parameter der Funktion. | Variable / String | nein |
| `codewortlaenge` | Parameter der Funktion. | Ganzzahl | nein |
| `codewortanzahl` | Parameter der Funktion. | Ganzzahl | nein |
| `datenwort` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

## Beispiele

**Beispiel:** `blockparity(even,7,3,"abc")`

| Ausdruck | Ergebnis |
| --- | --- |
| blockparity(even,7,3,"abc") | In der Übersicht nicht angegeben. |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateBitOperators.java`, Klasse `BlockParity`.

[Zurück zu Berechnungen](../../../index.md)
