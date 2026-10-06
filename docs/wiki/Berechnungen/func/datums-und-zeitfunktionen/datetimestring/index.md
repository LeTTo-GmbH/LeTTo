# datetimestring

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`datetimestring` – Datums und Zeitfunktionen.

## Detaillierte Beschreibung

erzeugt Datum und Uhrzeit als String

### Anwendung und Besonderheiten

Die Implementierung erwartet einen Ganzzahlwert. Das Format ist optional und verwendet die Muster von DateTimeFormatter. Die Typangabe String / Ganzzahl und die Pflichtkennzeichnung des Formats in der ursprünglichen Parameterreferenz wurden entsprechend der Implementierung berichtigt.

## Syntax

```text
datetimestring(datum)
datetimestring(datum, format)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
| --- | --- | --- | --- |
| datum | Numerischer Datums- bzw. Uhrzeitwert. | Ganzzahl | nein |
| format | Formatmuster für java.time.DateTimeFormatter; etwa yyyy-MM-dd oder HH:mm:ss. | String | ja |

## Beispiele

```text
datetimestring(date(2026,10,6,12,30,0),"yyyy-MM-dd HH:mm:ss")
```

**Ergebnis:** "2026-10-06 12:30:00"

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

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDateFunctions.java`, Klasse `DateTimeString`.

[Zurück zu Berechnungen](../../../index.md)
