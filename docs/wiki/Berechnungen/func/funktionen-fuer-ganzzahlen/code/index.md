# code

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`code` – Funktionen für Ganzzahlen.

## Detaillierte Beschreibung

Code aus mehreren Codeworten zusammensetzen : code(Codewortlänge,Datenwort)

## Syntax

```text
code(codewortlaenge, datenwort1, ...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `codewortlaenge` | Parameter der Funktion. | Ganzzahl | nein |
| `datenwort1` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

## Beispiele

**Beispiel:** `code(5,4,3,5)`  
**Ergebnis:** 0b1000001100101

| Ausdruck | Ergebnis |
| --- | --- |
| code(5,4,3,5) | 0b1000001100101 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateBitOperators.java`, Klasse `Code`.

[Zurück zu Berechnungen](../../../index.md)
