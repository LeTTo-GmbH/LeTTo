# ground

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`ground` – arithmetische Funktionen.

## Detaillierte Beschreibung

Rundet die Zahl auf die im zweiten Parameter angegebenen gültigen Ziffern

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

Die Anzahl gültiger Ziffern bezieht sich auf die gesamte Zahl, nicht nur auf Nachkommastellen. Beispiel: Zwei gültige Ziffern machen aus 2453.43 den Wert 2500. Für eine feste Anzahl Nachkommastellen ist `cround` vorgesehen.

## Syntax

```text
ground(wert, gueltigeZiffern)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `gueltigeZiffern` | Parameter der Funktion. | Ganzzahl | nein |

## Beispiele

**Beispiel:** `ground(2453.43,2)`  
**Ergebnis:** 2500

| Ausdruck | Ergebnis |
| --- | --- |
| ground(2453.43,2) | 2500 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3223)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `GRound`.

[Zurück zu Berechnungen](../../../index.md)
