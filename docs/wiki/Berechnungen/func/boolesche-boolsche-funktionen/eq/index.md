# eq

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`eq` – boolesche(boolsche) Funktionen.

## Detaillierte Beschreibung

gleich eq(wert1,wert2),eq(wert1,wert2,toleranz),eq(wert1,wert2,toleranz,absolut)

### Anwendung und Besonderheiten

Die Implementierung erwartet 2 bis 4 Argumente.

## Syntax

```text
eq(wert1, wert2)
eq(wert1, wert2, toleranz, absolut)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |
| `absolut` | Parameter der Funktion. | Boolean/Ausdruck / Zahl | ja |

## Beispiele

**Beispiel:** `eq(4,4)`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| eq(4,4) | true |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3182)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateCompareOperators.java`, Klasse `EQ`.

[Zurück zu Berechnungen](../../../index.md)
