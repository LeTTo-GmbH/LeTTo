# ispolynom

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`ispolynom` – Polynome.

## Detaillierte Beschreibung

Prüft, ob der Ausdruck ein Polynom ist. Die Funktion wird ausgewertet, sobald der Parameter als Polynom erkannt bzw. nicht als Polynom erkannt werden kann.

## Syntax

```text
ispolynom(ausdruck)
ispolynom(ausdruck, variable, numerisch)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `ausdruck` | Ausdruck bzw. Funktion, die verarbeitet werden soll. | Ausdruck | nein |
| `variable` | Variable, auf die sich die Operation bezieht. | Variable | ja |
| `numerisch` | Parameter der Funktion. | Ausdruck / passender Datentyp | ja |

## Beispiele

**Beispiel:** `ispolynom(polynom(x^2+1))`  
**Ergebnis:** true

| Ausdruck | Ergebnis |
| --- | --- |
| ispolynom(polynom(x^2+1)) | true |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculatePolynomFunctions.java`, Klasse `IsPolynom`.

[Zurück zu Berechnungen](../../../index.md)
