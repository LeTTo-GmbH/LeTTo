# float

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`float` – Funktionen zu Einheiten.

## Detaillierte Beschreibung

Zahl in eine Gleitkommazahl umwandeln, die Einheit geht dabei verloren (wie double)

### Anwendung und Besonderheiten

Alternative Schreibweise zu `double` laut Übersicht. Der Zahlenwert wird in eine Gleitkommazahl umgewandelt; die Einheit wird entfernt. Die Registrierung dieses Alias ist in den mitgelieferten Dateien nicht enthalten.

Die Übersicht führt diesen Namen als alternative Schreibweise bzw. kompatible Variante zu [double](../double/index.md). Maßgeblich sind die hier angegebenen Aufrufvarianten.

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
float(wert)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| wert | Numerischer Wert, dessen Einheit entfernt wird. | Zahl mit oder ohne Einheit | nein |

## Beispiele

| Ausdruck | Ergebnis |
| --- | --- |
| float(3.4V) | 3.4 |

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateArithmeticFunctions.java`, Klasse `DOUBLE`.

[Zurück zu Berechnungen](../../../index.md)
