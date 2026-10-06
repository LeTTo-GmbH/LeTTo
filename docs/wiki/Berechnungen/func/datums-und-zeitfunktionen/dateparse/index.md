# dateparse

[Zurück zu Berechnungen](../../../index.md) · [Weitere Funktionen dieser Gruppe](../index.md)

## Name

`dateparse` – Datums und Zeitfunktionen.

## Detaillierte Beschreibung

Wandelt einen String in ein Datum als Ganzzahl in Sekunden seit 1.1.0000

### Anwendung und Besonderheiten

Liest eine Zeichenkette über Datum.toDateInteger ein. Im Java-Kommentar sind unter anderem die Formate d.m.yy, d.m.yyyy, yyyy-m-d, d.m.y h:m:s, h:m:s und h:m genannt. Das Ergebnis ist ein Datumswert in Sekunden ab dem Jahr 0.

## Syntax

```text
dateparse(string)
```

## Parameterbeschreibung

| Parameter | Beschreibung | Möglicher Datentyp | Optional |
|---|---|---|---|
| `string` | Zeichenkette, die verarbeitet werden soll. | String | nein |

## Beispiele

```text
dateparse("6.10.2026")
```

**Ergebnis:** Numerischer Datumswert für den 06.10.2026.

## Demobeispiele

[DEMO-Beispiel](../../../../../demobsp.html?id=3497)

## Bildschirmhardcopys

Für dieses Element sind in den bereitgestellten Unterlagen keine Bildschirmhardcopys enthalten.

## Programmrevision

**Verfügbar seit Revision:** 6530

## Datum der letzten Änderung

**Diese Dokumentationsseite:** 06.10.2026.

Das Datum der letzten Änderung der Implementierung ist aus den bereitgestellten Dateien nicht ermittelbar.

## Grundlage

Parameterreferenz und Übersicht „Berechnungen“; Java-Implementierung `CalculateDateFunctions.java`, Klasse `ParseDate`.

[Zurück zu Berechnungen](../../../index.md)
