# cConjugate

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`cConjugate` – komplexe Zahlen.

## Detaillierte Beschreibung

Liefert die konjugiert komplexe Zahl einer komplexen Zahl

Alias/Kompatibilitätsname zu `conjugate`.

Kompatibilitätsalias zu `conjugate`.

### Anwendung und Besonderheiten

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [conjugate](../conjugate/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

Für `z = a+b*%i` entsteht `a-b*%i`. Die konjugierte Zahl hat denselben Betrag und einen entgegengesetzten Phasenwinkel.

## Syntax

```text
cConjugate(x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `cConjugate(3+4*%i)`  
**Ergebnis:** 3-4*%i

| Ausdruck | Ergebnis |
| --- | --- |
| cConjugate(3+4*%i) | 3-4*%i |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `Conjugate`.

[Zurück zu Berechnungen](../../../index.md)
