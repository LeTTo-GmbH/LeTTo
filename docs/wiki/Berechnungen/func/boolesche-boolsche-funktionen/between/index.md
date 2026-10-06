# between

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`between` – boolesche(boolsche) Funktionen.

## Detaillierte Beschreibung

prüft ob Parameter1 kleiner als Parameter2 und Parameter2 kleiner als Parameter 3 . Parameter 4 und 5 können optinal für die Toleranz verwendet werden.

### Anwendung und Besonderheiten

Die Implementierung erwartet 3 bis 5 Argumente.

## Syntax

```text
between(minimum, wert, maximum)
between(minimum, wert, maximum, toleranz, absolut)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `minimum` | Untere Grenze bzw. Startwert. | Zahl / Ausdruck | nein |
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `maximum` | Obere Grenze bzw. Endwert. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |
| `absolut` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | ja |

## Beispiele

**Beispiel:** `between(3,4,5)`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| between(3,4,5) | true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3189)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateCompareOperators.java`, Klasse `BETWEEN`.

[Zurück zu Berechnungen](../../../index.md)
