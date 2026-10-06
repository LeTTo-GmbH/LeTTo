# bimp

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`bimp` – Funktionen für Ganzzahlen.

## Detaillierte Beschreibung

Verknüpft zwei Werte bitweise bzw. logisch. Der Funktionsname steht für eine Implikation; die mitgelieferte Implementierung weist davon abweichende Fälle auf.

### Anwendung und Besonderheiten

Die aktuelle Java-Implementierung berechnet bei Ganzzahlen `(~a) | b` mit BigInteger ohne feste Bitbreite. Daher liefert `bimp(13,10)` den Wert **-5**, nicht 8. Bei booleschen Parametern implementiert der Code derzeit `!(a || b)` (NOR), etwa `bimp(false,false) = true`; das entspricht nicht der üblichen Implikation `!a || b`. Der Name beschreibt die beabsichtigte Operation, diese Angaben beschreiben den mitgelieferten Code.

Die Implementierung erwartet genau 2 Argumente.

## Syntax

```text
bimp(wert1, wert2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `wert1` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |
| `wert2` | Wert bzw. Ausdruck für die Berechnung. | Zahl / Ausdruck | nein |

## Beispiele

| Ausdruck | Ergebnis laut Java-Implementierung |
| --- | --- |
| `bimp(13,10)` | -5 |
| `bimp(false,false)` | true |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateBitOperators.java`, Klasse `IMP`.

[Zurück zu Berechnungen](../../../index.md)
