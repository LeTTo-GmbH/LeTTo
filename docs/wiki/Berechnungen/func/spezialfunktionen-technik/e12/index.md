# e12

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`e12` – Spezialfunktionen Technik.

## Detaillierte Beschreibung

rundet einen Zahlenwert auf den nächstliegenden Wert der Normreihe E12. Die Rundung erfolgt geometrisch d.h. der Quotient zwischen Normwert und zu rundendem Wert wird minimiert.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
e12(A)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `A` | Parameter der Funktion. | Zahl | nein |

## Beispiele

**Beispiel:** `e12(700Ohm)`  
**Ergebnis:** 680Ohm

| Ausdruck | Ergebnis |
| --- | --- |
| e12(700Ohm) | 680Ohm |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3503)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `E12`.

[Zurück zu Berechnungen](../../../index.md)
