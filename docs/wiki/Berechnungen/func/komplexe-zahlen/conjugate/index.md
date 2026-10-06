# conjugate

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`conjugate` – komplexe Zahlen.

## Detaillierte Beschreibung

Liefert die konjugiert komplexe Zahl einer komplexen Zahl

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

Für `z = a+b*%i` entsteht `a-b*%i`. Die konjugierte Zahl hat denselben Betrag und einen entgegengesetzten Phasenwinkel.

## Syntax

```text
conjugate(x)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `x` | X-Wert bzw. Ausdruck. | komplexe Zahl / Zahl | nein |

## Beispiele

**Beispiel:** `conjugate(3+4*%i)`  
**Ergebnis:** 3-4*%i

| Ausdruck | Ergebnis |
| --- | --- |
| conjugate(3+4*%i) | 3-4*%i |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3334)

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
