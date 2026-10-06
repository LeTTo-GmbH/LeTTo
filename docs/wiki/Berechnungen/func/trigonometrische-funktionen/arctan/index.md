# arctan

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`arctan` – trigonometrische Funktionen.

## Detaillierte Beschreibung

Arcus-Tangens

Alias/Kompatibilitätsname zu `atan`.

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [atan](../atan/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

Berechnet die Umkehrfunktion von `tan` im dafür gewählten Zweig. Für jeden reellen Eingabewert ist ein reeller Winkel definiert. Außerhalb des reellen Bereichs kann ein komplexes Ergebnis erforderlich sein; die genaue Behandlung übernimmt die Rechenbibliothek.

## Syntax

```text
arctan(x1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

## Beispiele

**Beispiel:** `arctan(1)`  
**Ergebnis:** %pi/4

| Ausdruck | Ergebnis |
| --- | --- |
| arctan(1) | %pi/4 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3309)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTrigonometricFunctions.java`, Klasse `Atan`.

[Zurück zu Berechnungen](../../../index.md)
