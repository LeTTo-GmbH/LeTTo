# normup

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`normup` – Spezialfunktionen Technik.

## Detaillierte Beschreibung

rundet einen Zahlenwert auf den nächstgrößerern Wert einer gegebenen Wertereihe oder Normreihe.

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
normup(wert, normreihe)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `normreihe` | Parameter der Funktion. | Zahl | nein |

## Beispiele

**Beispiel:** `normup(730Ohm[1,3,5,8])`  
**Ergebnis:** 800Ohm

| Ausdruck | Ergebnis |
| --- | --- |
| normup(730Ohm&#91;1,3,5,8&#93;) | 800Ohm |

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3508)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** Nicht aus den bereitgestellten Unterlagen ermittelbar.

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `NORMup`.

[Zurück zu Berechnungen](../../../index.md)
