# datemix

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`datemix` – Datums und Zeitfunktionen.

## Detaillierte Beschreibung

Erzeugt aus einem Datumswert (Sekunden seit 1.1.00 0:00:00) einen Vektor mit Jahr,Monat,Tag,Stunde,Minute,Sekunde

### Anwendung und Besonderheiten

Die Implementierung erwartet genau 1 Argumente.

## Syntax

```text
datemix(di)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `di` | Parameter der Funktion. | String / Ganzzahl | nein |

## Beispiele

```text
datemix(date(2026,10,6,12,30,15))
```

**Ergebnis:** [2026,10,6,12,30,15]

## Demobeispiele

In der bereitgestellten Übersicht ist kein Demobeispiel verlinkt.

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6641

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDateFunctions.java`, Klasse `DateMix`.

[Zurück zu Berechnungen](../../../index.md)
