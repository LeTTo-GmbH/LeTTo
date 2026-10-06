# newton

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`newton` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

Bestimmt eine Nullstelle einer Funktion nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der Startwert.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
newton(funktion, startwert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `startwert` | Untere Grenze bzw. Startwert. | Zahl / Ausdruck | nein |

## Beispiele

**Beispiel:** `newton(x^2-4,4)`  
**Ergebnis:** 2

| Ausdruck | Ergebnis |
| --- | --- |
| newton(x^2-4,4) | 2 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3279)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `Newton`.

[Zurück zu Berechnungen](../../../index.md)
