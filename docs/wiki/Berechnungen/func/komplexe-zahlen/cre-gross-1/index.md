# cRe

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`cRe` – komplexe Zahlen.

## Detaillierte Beschreibung

Liefert den Realteil einer komplexen Zahl

Alias/Kompatibilitätsname zu `realpart`.

Kompatibilitätsalias zu `realpart`.

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [realpart](../realpart/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

Für `z = a+b*%i` wird `a` zurückgegeben. Damit kann der Realteil getrennt vom Imaginärteil in weiteren Berechnungen verwendet werden.

## Syntax

```text
cRe(re)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `cRe(3+4*%i)`  
**Ergebnis:** 3

| Ausdruck | Ergebnis |
| --- | --- |
| cRe(3+4*%i) | 3 |

## Demobeispiele

In der bereitgestellten Übersicht ist kein Demobeispiel verlinkt.

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
