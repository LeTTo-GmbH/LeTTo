# hamming

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`hamming` – Funktionen für Ganzzahlen.

## Detaillierte Beschreibung

Bestimmt den Hamming-Abstand von mehreren Codeworten

## Syntax

```text
hamming(codewort1, codewort2, ...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `codewort1` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `codewort2` | Parameter der Funktion. | Ausdruck / passender Datentyp | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

## Beispiele

**Beispiel:** `hamming(1,2,4,8,16)`  
**Ergebnis:** 2

| Ausdruck | Ergebnis |
| --- | --- |
| hamming(1,2,4,8,16) | 2 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateBitOperators.java`, Klasse `Hamming`.

[Zurück zu Berechnungen](../../../index.md)
