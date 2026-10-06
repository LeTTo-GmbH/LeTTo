# cIm

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`cIm` – komplexe Zahlen.

## Detaillierte Beschreibung

Liefert den Imaginärteil einer komplexen Zahl

Alias/Kompatibilitätsname zu `imagpart`.

Kompatibilitätsalias zu `imagpart`.

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [imagpart](../imagpart/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

Für `z = a+b*%i` wird `b` zurückgegeben, also der Koeffizient von `%i`, nicht das Produkt `b*%i`.

## Syntax

```text
cIm(re)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `re` | Parameter der Funktion. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `cIm(3+4*%i)`  
**Ergebnis:** 4

| Ausdruck | Ergebnis |
| --- | --- |
| cIm(3+4*%i) | 4 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Im`.

[Zurück zu Berechnungen](../../../index.md)
