# max

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`max` – arithmetische Funktionen.

## Detaillierte Beschreibung

Maximum von mehreren Werten suchen

Vergleicht die angegebenen Werte und liefert den größten Wert. Die Argumente müssen sich im Berechnungskontext vergleichen lassen; bei physikalischen Größen müssen die Einheiten kompatibel sein.

## Syntax

```text
max(werte, ...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `werte` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `weitereParameter` | Weitere Parameter desselben Funktionsaufrufs; Anzahl ist variabel. | Ausdruck / passender Datentyp | ja, beliebig oft |

## Beispiele

**Beispiel:** `max(3,5,1)`  
**Ergebnis:** 5

| Ausdruck | Ergebnis |
| --- | --- |
| max(3,5,1) | 5 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3232)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Max`.

[Zurück zu Berechnungen](../../../index.md)
