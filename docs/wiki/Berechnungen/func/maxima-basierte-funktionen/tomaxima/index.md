# tomaxima

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`tomaxima` – Maxima-basierte Funktionen.

## Detaillierte Beschreibung

Führt die Berechnung aller Parameter von links nach rechts hintereinander mit Maxima aus. Das Ergebnis ist dann das Ergebnis des letzten Parameters.

### Anwendung und Besonderheiten

Diese Funktion benötigt ein installiertes Maxima und wird auch bei aktiviertem internen Parser an Maxima gesendet.

## Syntax

```text
tomaxima(ausdruck1)
tomaxima(ausdruck1, wert2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck1` | Parameter der Funktion. | Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck des 2. Parameters. | Zahl / Ausdruck | ja |

## Beispiele

**Beispiel:** `tomaxima(y:x^2,y+2)`  
**Ergebnis:** x^2+2

| Ausdruck | Ergebnis |
| --- | --- |
| tomaxima(y:x^2,y+2) | x^2+2 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3263)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateMaximaFunctions.java`, Klasse `ToMaxima`.

[Zurück zu Berechnungen](../../../index.md)
