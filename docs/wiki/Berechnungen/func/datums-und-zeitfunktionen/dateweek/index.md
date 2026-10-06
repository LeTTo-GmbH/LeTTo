# dateweek

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`dateweek` – Datums und Zeitfunktionen.

## Detaillierte Beschreibung

Liefert die Kalenderwoche des Tages innerhalb des Jahres

## Syntax

```text
dateweek(date)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date` | Parameter der Funktion. | String / Ganzzahl | nein |

## Beispiele

```text
dateweek(date(2026,10,6))
```

**Ergebnis:** Wochennummer des angegebenen Datums; deren Konvention wird an die nicht mitgelieferte Datum-Hilfsklasse delegiert.

## Demobeispiele

In der bereitgestellten Übersicht ist kein Demobeispiel verlinkt.

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6530

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDateFunctions.java`, Klasse `Week`.

[Zurück zu Berechnungen](../../../index.md)
