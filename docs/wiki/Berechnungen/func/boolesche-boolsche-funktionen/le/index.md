# le

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`le` – boolesche(boolsche) Funktionen.

## Detaillierte Beschreibung

kleiner gleich le(wert1,wert2),le(wert1,wert2,toleranz),le(wert1,wert2,toleranz,absolut)

### Anwendung und Besonderheiten

Die Implementierung erwartet 2 bis 4 Argumente.

## Syntax

```text
le(wert1, wert2)
le(wert1, wert2, toleranz, absolut)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |
| `absolut` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | ja |

## Beispiele

**Beispiel:** `le(6,4)`  
**Ergebnis:** false

| Ausdruck | Ergebnis |
| --- | --- |
| le(6,4) | false |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3186)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateCompareOperators.java`, Klasse `LE`.

[Zurück zu Berechnungen](../../../index.md)
