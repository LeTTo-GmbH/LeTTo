# min

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`min` – arithmetische Funktionen.

## Detaillierte Beschreibung

Minimum von mehrere Werten suchen

Vergleicht die angegebenen Werte und liefert den kleinsten Wert. Die Argumente müssen sich im Berechnungskontext vergleichen lassen; bei physikalischen Größen müssen die Einheiten kompatibel sein.

## Syntax

```text
min(werte, ...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `werte` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

## Beispiele

**Beispiel:** `min(3,5,1)`  
**Ergebnis:** 1

| Ausdruck | Ergebnis |
| --- | --- |
| min(3,5,1) | 1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3231)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Min`.

[Zurück zu Berechnungen](../../../index.md)
