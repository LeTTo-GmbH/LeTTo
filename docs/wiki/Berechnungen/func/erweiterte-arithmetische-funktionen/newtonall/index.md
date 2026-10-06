# newtonall

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`newtonall` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

Bestimmt alle Nullstellen einer Funktion mit einem Betrag des Funktionsparameters kleiner als ein definierter Wert nach dem Newton-Verfahren. Der erste Parameter ist ein Ausdruck in einer Variablen, der zweite Parameter ist der maximale Betrag des Funktionsparameters. Das Ergebnis ist immer ein Vektor mit den nach aufsteigendem Funktionswert sortierten Nullstellen.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
newtonall(funktion, maximalerBetrag)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `funktion` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `maximalerBetrag` | Parameter der Funktion. | Zahl | nein |

## Beispiele

**Beispiel:** `newtonall (x^2-4,4)`  
**Ergebnis:** [-2,2]

| Ausdruck | Ergebnis |
| --- | --- |
| newtonall (x^2-4,4) | &#91;-2,2&#93; |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3281)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateFunctions.java`, Klasse `NewtonAll`.

[Zurück zu Berechnungen](../../../index.md)
