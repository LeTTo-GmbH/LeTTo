# cabs

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`cabs` – komplexe Zahlen.

## Detaillierte Beschreibung

Liefert den Absolutbetrag einer komplexen Zahl

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [abs](../abs/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

Für eine komplexe Zahl `z = a + b*%i` ist der Betrag `sqrt(a^2+b^2)`. Für reelle Zahlen entspricht dies dem Abstand von 0; das Ergebnis ist nicht negativ.

## Syntax

```text
cabs(x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | Zahl | nein |

## Beispiele

**Beispiel:** `cabs(3+4*%i)`  
**Ergebnis:** 5

| Ausdruck | Ergebnis |
| --- | --- |
| cabs(3+4*%i) | 5 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3330)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `CAbs`.

[Zurück zu Berechnungen](../../../index.md)
