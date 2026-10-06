# realpart

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`realpart` – komplexe Zahlen.

## Detaillierte Beschreibung

Liefert den Realteil einer komplexen Zahl

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Für `z = a+b*%i` wird `a` zurückgegeben. Damit kann der Realteil getrennt vom Imaginärteil in weiteren Berechnungen verwendet werden.

## Syntax

```text
realpart(re)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `realpart(3+4*%i)`  
**Ergebnis:** 3

| Ausdruck | Ergebnis |
| --- | --- |
| realpart(3+4*%i) | 3 |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3332)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Re`.

[Zurück zu Berechnungen](../../../index.md)
