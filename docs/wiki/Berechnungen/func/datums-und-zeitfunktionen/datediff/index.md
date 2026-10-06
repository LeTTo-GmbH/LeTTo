# datediff

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`datediff` – Datums und Zeitfunktionen.

## Detaillierte Beschreibung

Rechnet die Differenz von 2 ganzzahligen Datumswerten. Erstes minus zweites Datum. Ergebnis als Double in Sekunden

## Syntax

```text
datediff(date1, date2)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `date1` | Parameter der Funktion. | String / Ganzzahl | nein |
| `date2` | Parameter der Funktion. | String / Ganzzahl | nein |

## Beispiele

```text
datediff(date(2026,10,7),date(2026,10,6))
```

**Ergebnis:** 86400 s

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDateFunctions.java`, Klasse `DateDiff`.

[Zurück zu Berechnungen](../../../index.md)
