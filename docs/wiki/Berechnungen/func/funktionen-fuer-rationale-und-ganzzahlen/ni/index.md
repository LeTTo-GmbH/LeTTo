# ni

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`ni` – Funktionen für rationale und Ganzzahlen.

## Detaillierte Beschreibung

prüft ob eine Zahl nahe genug an einer Ganzzahl liegt, um als Ganzzahl interpretiert zu werden. Es wird die Toleranz der Frage verwendet

Alias/Kompatibilitätsname zu `isNearInteger`.

Kurzform von isNearInteger - prüft ob eine Zahl nahe genug an einer Ganzzahl liegt, um als Ganzzahl interpretiert zu werden. Es wird die Toleranz der Frage verwendet

### Anwendung und Besonderheiten

Prüft den Abstand des Betrags der Zahl zur nächstliegenden Ganzzahl. Ohne zweiten Parameter stammt die Toleranz aus dem Berechnungskontext. Im mitgelieferten Code wird bei zwei Parametern irrtümlich der erste Parameter als Toleranz gelesen; der angegebene zweite Toleranzwert wird dabei ignoriert. Die Parameterliste beschreibt die vorgesehene Schnittstelle; eine frei wählbare Toleranz funktioniert mit dieser Implementierung daher nicht wie dokumentiert.

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [isNearInteger](../isnearinteger-gross-2-6/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet 1 bis 2 Argumente.

## Syntax

```text
ni(wert)
ni(wert, toleranz)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |

## Beispiele

**Beispiel:** `ni(3.00000000001) ni(3.1)`  
**Ergebnis:** true false

| Ausdruck | Ergebnis |
| --- | --- |
| ni(3.00000000001) <br> ni(3.1) | true <br> false |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateCompareOperators.java`, Klasse `IsNearInteger`.

[Zurück zu Berechnungen](../../../index.md)
