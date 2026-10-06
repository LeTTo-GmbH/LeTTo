# cnewton

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`cnewton` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

Bestimmt eine komplexe Nullstelle einer Funktion nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der komplexe Startwert.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
cnewton(funktion, startwert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `startwert` | Untere Grenze bzw. Startwert. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `cnewton (x^2+4,4)`  
**Ergebnis:** 2*%i

| Ausdruck | Ergebnis |
| --- | --- |
| cnewton (x^2+4,4) | 2*%i |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3280)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `NewtonComplex`.

[Zurück zu Berechnungen](../../../index.md)
