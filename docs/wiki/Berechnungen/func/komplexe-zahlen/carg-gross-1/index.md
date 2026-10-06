# cArg

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`cArg` – komplexe Zahlen.

## Detaillierte Beschreibung

Liefert das Argument einer komplexen Zahl

Alias/Kompatibilitätsname zu `carg`.

Kompatibilitätsalias zu `carg`.

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [carg](../carg/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

Liefert den Phasenwinkel einer komplexen Zahl. Für `z = a+b*%i` wird der Winkel durch Real- und Imaginärteil bestimmt. Die Java-Implementierung liefert den numerischen Winkel im Bogenmaß.

## Syntax

```text
cArg(x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `cArg(4*%e^(3*%i))`  
**Ergebnis:** 3

| Ausdruck | Ergebnis |
| --- | --- |
| cArg(4*%e^(3*%i)) | 3 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `CArg`.

[Zurück zu Berechnungen](../../../index.md)
