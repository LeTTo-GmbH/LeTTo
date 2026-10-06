# acsc

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`acsc` – trigonometrische Funktionen.

## Detaillierte Beschreibung

Arcus-Kosekans, inverse Funktion zu `csc`.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Berechnet die Umkehrfunktion von `csc` im dafür gewählten Zweig. Ein reelles Ergebnis setzt einen Betrag von x mindestens 1 voraus. Außerhalb des reellen Bereichs kann ein komplexes Ergebnis erforderlich sein; die genaue Behandlung übernimmt die Rechenbibliothek.

## Syntax

```text
acsc(x1)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x1` | Parameter der Funktion. | Ganzzahl / komplexe Zahl | nein |

## Beispiele

**Beispiel:** `acsc(2)`  
**Ergebnis:** %pi/6

| Ausdruck | Ergebnis |
| --- | --- |
| acsc(2) | %pi/6 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateTrigonometricFunctions.java`, Klasse `Acsc`.

[Zurück zu Berechnungen](../../../index.md)
