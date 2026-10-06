# par

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`par` – arithmetische Funktionen.

## Detaillierte Beschreibung

Parallelschaltung von Widerständen

### Anwendung und Besonderheiten

Für zwei Argumente lautet die Formel `a*b/(a+b)`. Ein einzelnes Argument wird unverändert geliefert. Die Implementierung verarbeitet auch mehrere Argumente durch wiederholte Parallelschaltung. Die Werte müssen sich sinnvoll addieren und multiplizieren lassen; bei Widerständen werden kompatible Einheiten verwendet.

## Syntax

```text
par(wert1, ...)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| wert1 | Erster Widerstand bzw. parallel zu verknüpfender Wert. | Zahl / Ausdruck | nein |
| weitereWerte | Weitere kompatible Werte. | Zahl / Ausdruck | ja, beliebig oft |

## Beispiele

**Beispiel:** `par(x,y)`  
**Ergebnis:** x*y/(x+y)

| Ausdruck | Ergebnis |
| --- | --- |
| par(x,y) | x*y/(x+y) |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3230)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticOperators.java`, Klasse `Parallel`.

[Zurück zu Berechnungen](../../../index.md)
