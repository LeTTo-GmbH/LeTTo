# quadrant

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`quadrant` – trigonometrische Funktionen.

## Detaillierte Beschreibung

Liefert den Quadranten eines Winkels mit einer Toleranzangabe.

## Syntax

```text
quadrant(winkel)
quadrant(winkel, toleranz)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `winkel` | Parameter der Funktion. | Zahl / Ausdruck | nein |
| `toleranz` | Toleranz für Vergleich bzw. numerische Auswertung. | Zahl / Toleranzangabe | ja |

## Beispiele

**Beispiel:** `quadrant(20°,5°)`  
**Ergebnis:** 1

| Ausdruck | Ergebnis |
| --- | --- |
| quadrant(20°,5°) | 1 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3321)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTrigonometricFunctions.java`, Klasse `Quadrant`.

[Zurück zu Berechnungen](../../../index.md)
