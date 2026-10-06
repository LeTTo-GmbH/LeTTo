# cround

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`cround` – arithmetische Funktionen.

## Detaillierte Beschreibung

Rundet die Zahl kaufmännisch, der zweite Parameter gibt die Anzahl der Kommastellen an, ohne 2.Parameter wird auf Ganzzahlen gerundet, bei komplexen Zahlen wird Betrag und Winkel in Grad gerundet.

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
cround(wert)
cround(wert, kommastellen)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `kommastellen` | Parameter der Funktion. | Ganzzahl | ja |

## Beispiele

**Beispiel:** `cround(23.535,2) cround(2.435arg34.5364°,1)`  
**Ergebnis:** 23.54 2.4arg34.5°

| Ausdruck | Ergebnis |
| --- | --- |
| cround(23.535,2)<br>cround(2.435arg34.5364°,1) | 23.54<br>2.4arg34.5° |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3220)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `CRound`.

[Zurück zu Berechnungen](../../../index.md)
