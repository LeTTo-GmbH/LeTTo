# arcsin

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`arcsin` – trigonometrische Funktionen.

## Detaillierte Beschreibung

Arcus-Sinus

Alias/Kompatibilitätsname zu `asin`.

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [asin](../asin/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

Berechnet die Umkehrfunktion von `sin` im dafür gewählten Zweig. Für ein reelles Ergebnis muss x zwischen -1 und 1 liegen. Außerhalb des reellen Bereichs kann ein komplexes Ergebnis erforderlich sein; die genaue Behandlung übernimmt die Rechenbibliothek.

## Syntax

```text
arcsin(x1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

## Beispiele

**Beispiel:** `asin(1)`  
**Ergebnis:** %pi/2

| Ausdruck | Ergebnis |
| --- | --- |
| asin(1) | %pi/2 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3305)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTrigonometricFunctions.java`, Klasse `Asin`.

[Zurück zu Berechnungen](../../../index.md)
