# ramp

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`ramp` – erweiterte arithmetische Funktionen.

## Detaillierte Beschreibung

Rampenfunktion: ramp(x,x0) Rampe von x0 < x < x0 + 1 ramp(x,x0,L) Rampe von x0 < x < x0 + L !300px-Funktion_ramp.png

Rampenfunktion: <br>ramp(x,x0) Rampe von x0 &lt; x &lt; x0 + 1<br>ramp(x,x0,L) Rampe von x0 &lt; x &lt; x0 + L<br>

### Anwendung und Besonderheiten

Ohne Startwert gilt `x0 = 0`, ohne Länge `L = 1`. Unterhalb von `x0` ist das Ergebnis 0, oberhalb von `x0 + L` ist es 1; dazwischen `(x-x0)/L`. Eine negative Länge wird durch Verschieben des Startpunkts und Umkehren der Länge behandelt. Eine Länge 0 sollte vermieden werden.

Die Implementierung erwartet 1 bis 3 Argumente.

## Syntax

```text
ramp(x)
ramp(x, x0)
ramp(x, x0, L)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| x | Auswertungsstelle. | Zahl | nein |
| x0 | Startpunkt; Vorgabe 0. | Zahl | ja |
| L | Länge des Anstiegs; Vorgabe 1. | Zahl | ja |

## Beispiele

**Beispiel:** `ramp(x,2,4)`  
**Ergebnis:** !100px-Ramp_Plot.png

| Ausdruck | Ergebnis |
| --- | --- |
| ramp(x,2,4) | ![100px-Ramp_Plot.png](../../../100px-Ramp_Plot.png) |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3270)

## Bildschirmhardcopys

![300px-Funktion_ramp.png](../../../300px-Funktion_ramp.png)

![100px-Ramp_Plot.png](../../../100px-Ramp_Plot.png)

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Ramp`.

[Zurück zu Berechnungen](../../../index.md)
