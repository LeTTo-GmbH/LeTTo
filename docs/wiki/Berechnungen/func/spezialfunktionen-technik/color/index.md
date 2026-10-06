# color

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`color` – Spezialfunktionen Technik.

## Detaillierte Beschreibung

Widerstandsfarbcode berechnen. 1. Parameter muss ein Double sein 2. Parameter sind die Anzahl der Farbringe 3. Parameter ist der Darstellungsmodus (0 = Deutsch ausgeschrieben, 1 = Abkürzung Deutsch mit drei Buchstaben, 2 = Abkürzung Deutsch mit zwei Buchstaben, 3 = Englisch ausgeschrieben, 4 = Abkürzung Englisch mit drei Buchstaben, 5 = Abkürzung Englisch mit zwei Buchstaben)

### Anwendung und Besonderheiten

Die Implementierung erwartet 1 bis 3 Argumente.

## Syntax

```text
color(wert)
color(wert, farbringe, modus)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `farbringe` | Parameter der Funktion. | Ganzzahl | ja |
| `modus` | Modus, der die Art der Verarbeitung oder Darstellung festlegt. | String / Ganzzahl | ja |

## Beispiele

**Beispiel:** `color(120,3,0)`  
**Ergebnis:** braun,rot,braun

| Ausdruck | Ergebnis |
| --- | --- |
| color(120,3,0) | braun,rot,braun |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3499)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateStringFunctions.java`, Klasse `Color`.

[Zurück zu Berechnungen](../../../index.md)
