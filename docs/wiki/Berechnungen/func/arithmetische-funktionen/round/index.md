# round

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`round` – arithmetische Funktionen.

## Detaillierte Beschreibung

Rundet die Zahl kaufmännisch, der zweite Parameter gibt die Anzahl der Kommastellen an, ohne 2.Parameter wird auf Ganzzahlen gerundet, bei komplexen Zahlen wird Betrag und Winkel in Grad gerundet.

Alias/Kompatibilitätsname zu `cround`.

Rundet die Zahl kaufmännisch, aus Kompatibilitätsgründen zu Maxima hat round nur einen Parameter

### Anwendung und Besonderheiten

Die Klasse Round akzeptiert genau einen Parameter und rundet auf ganze Zahlen. Bei komplexen Zahlen werden Betrag und Winkel in Grad gerundet. Die Zweiparametervariante aus der ursprünglichen Parameterreferenz widerspricht diesem Code; für Kommastellen ist cround(wert, kommastellen) vorgesehen.

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [cround](../cround/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
round(wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| wert | Zu rundender Wert; bei komplexen Zahlen werden Betrag und Winkel in Grad gerundet. | Zahl | nein |

## Beispiele

**Beispiel:** `round(23.535)`  
**Ergebnis:** 24

| Ausdruck | Ergebnis |
| --- | --- |
| round(23.535) | 24 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3222)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Round`.

[Zurück zu Berechnungen](../../../index.md)
