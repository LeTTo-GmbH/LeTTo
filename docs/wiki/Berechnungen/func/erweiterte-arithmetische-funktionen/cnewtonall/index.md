# cnewtonall

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`cnewtonall` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

Bestimmt alle komplexen Nullstellen einer Funktion mit einem Betrag des Funktionsparameters kleiner als ein definierter Wert nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der maximale Betrag des Funktionsparameters. Das Ergebnis ist immer ein Vektor mit den Nullstellen.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
cnewtonall(funktion, maximalerBetrag)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `maximalerBetrag` | Parameter der Funktion. | Zahl | nein |

## Beispiele

**Beispiel:** `cnewtonall (x^2+4,4)`  
**Ergebnis:** [-2*%i,2*%i]

| Ausdruck | Ergebnis |
| --- | --- |
| cnewtonall (x^2+4,4) | &#91;-2*%i,2*%i&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3282)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `NewtonComplexAll`.

[Zurück zu Berechnungen](../../../index.md)
